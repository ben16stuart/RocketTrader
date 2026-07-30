"""Reconcile each agent's book against the shared live Alpaca account.

Bull and Rocket keep separate trade logs but trade one pooled Alpaca account.
Nothing previously verified that the two books add up to what the broker actually
holds: portfolio_snapshot.py printed every position and told the model, in prose,
to "cross-reference with memory/trade_log.md to identify which positions are
Bull's". That pushed a deterministic join -- which position belongs to whom --
into the LLM's lap on every single session. Tokens spent re-deriving a fixed
fact, and no check that anything tied out.

This does the join in code, in the shape of a bank reconciliation: our book,
the sibling's book, the broker's statement, and anything that doesn't tie.

Reconciling item categories:
  MATCHED       in our book and in the account          -- normal
  SIBLING       the other agent's, per their trade log  -- normal in a shared account
  UNATTRIBUTED  held at the broker, claimed by neither  -- INVESTIGATE
  MISSING       in our book, not held at the broker     -- INVESTIGATE (stop hit? manual close?)

Nothing here raises. Reconciliation is a diagnostic layer bolted onto a live
trading routine, so any parsing failure degrades to "unknown" rather than taking
down the snapshot that market_close depends on.
"""

import os
import re

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\b")
TICKER_RE = re.compile(r"\b[A-Z]{1,5}\b")

# Words that look like tickers in a header but aren't.
NOT_TICKERS = {
    "BUY", "SELL", "OPEN", "CLOSED", "CLOSE", "ENTRY", "EXIT", "ALL", "AND",
    "POSITIONS", "POSITION", "LIQUIDATED", "RESET", "EVENT", "PORTFOLIO",
    "SYMBOL", "TRIM", "ADD", "STOP", "HIT", "PARTIAL", "FULL", "NEW", "OLD",
    "PRE", "POST", "R", "P", "L", "PL", "USD", "ET", "AM", "PM", "MDT", "UTC",
}

CLOSE_WORDS = ("SELL", "CLOSED", "CLOSE", "EXIT", "LIQUIDATED", "STOPPED")
OPEN_WORDS = ("BUY", "ENTRY", "ADD")


def _extract_ticker(text):
    """First plausible ticker in a header segment, or None."""
    for cand in TICKER_RE.findall(text):
        if cand not in NOT_TICKERS:
            return cand
    return None


def open_symbols_from_trade_log(path):
    """Replay a trade_log.md forward and return the set of still-open symbols.

    Handles both house formats:
      Bull    "## 2026-05-07 - JPM - BUY"      /  "## 2026-07-23 - KO - SELL (...)"
      Rocket  "## 2026-06-16 - CAMP ENTRY"     /  "## 2026-06-05 - MRLN CLOSED (...)"

    Returns (symbols, ok). ok=False means the log couldn't be read at all, which
    is reported as "unknown" rather than silently becoming an empty book -- an
    empty book would make every real position look UNATTRIBUTED.
    """
    try:
        with open(path) as fh:
            lines = fh.readlines()
    except Exception:
        return set(), False, set()

    # Collect events first, then replay in DATE order. The logs are appended in
    # edited batches, not chronologically -- Bull's runs 06-01, 05-26, 05-18,
    # 05-05, 05-07 ... so replaying in file order applies a later liquidation to
    # trades that were logged after it. Sorting is stable, so entries sharing a
    # date keep their file order (a same-day buy-then-sell still resolves).
    events = []
    for raw in lines:
        if not raw.startswith("## "):
            continue
        header = raw[3:].strip()

        # Skip the format template and any non-dated section heading
        # ("## Performance Summary", "## YYYY-MM-DD - SYMBOL - BUY/SELL").
        m = DATE_RE.match(header)
        if not m:
            continue

        date = m.group(1)
        upper = header.upper()

        # An entry corrected by a later correcting entry is not replayed. Books get
        # fixed by posting a correction, never by deleting history -- the erroneous
        # record stays readable for audit, but must not drive state.
        if "SUPERSEDED" in upper:
            continue
        body = header[10:]  # everything after the ISO date

        if "ALL POSITIONS" in upper or "LIQUIDATED" in upper or "RESET" in upper:
            events.append((date, "reset", None))
            continue

        sym = _extract_ticker(body)
        if not sym:
            continue

        # Check close before open: "SELL" and "CLOSED" are unambiguous, whereas a
        # closing header can still mention the original entry.
        if any(w in upper for w in CLOSE_WORDS):
            events.append((date, "close", sym))
        elif any(w in upper for w in OPEN_WORDS):
            events.append((date, "open", sym))

    events.sort(key=lambda e: e[0])

    open_syms = set()
    cleared_by_reset = set()
    for _date, kind, sym in events:
        if kind == "reset":
            # Remember what a bulk-liquidation entry swept away. If one of those
            # symbols is still held at the broker, the liquidation record is
            # probably wrong -- which is worth saying explicitly, because a false
            # liquidation makes a real position look UNATTRIBUTED forever after.
            cleared_by_reset |= open_syms
            open_syms = set()
        elif kind == "close":
            open_syms.discard(sym)
        else:
            open_syms.add(sym)
            cleared_by_reset.discard(sym)

    return open_syms, True, cleared_by_reset


def _sibling_trade_log(repo_dir):
    """Path to the other agent's trade_log.md, or None if not found."""
    siblings = {"OpusTrader": "RocketTrader", "RocketTrader": "OpusTrader"}
    repo_dir = os.path.abspath(repo_dir)
    name = os.path.basename(repo_dir)
    other = siblings.get(name)
    if not other:
        return None
    path = os.path.join(os.path.dirname(repo_dir), other, "memory", "trade_log.md")
    return path if os.path.exists(path) else None


def reconcile(live_positions, repo_dir, agent_name, sibling_name):
    """Classify every live position against our book and the sibling's."""
    ours_path = os.path.join(repo_dir, "memory", "trade_log.md")
    ours, ours_ok, ours_reset = open_symbols_from_trade_log(ours_path)

    sib_path = _sibling_trade_log(repo_dir)
    if sib_path:
        theirs, theirs_ok, _ = open_symbols_from_trade_log(sib_path)
    else:
        theirs, theirs_ok = set(), False

    live = {p["symbol"] for p in live_positions}

    matched = sorted(live & ours)
    sibling = sorted((live & theirs) - ours)
    unattributed = sorted(live - ours - theirs)
    missing = sorted(ours - live)

    return {
        "agent": agent_name,
        "sibling": sibling_name,
        "ours_ok": ours_ok,
        "theirs_ok": theirs_ok,
        "matched": matched,
        "sibling_positions": sibling,
        "unattributed": unattributed,
        "missing": missing,
        "cleared_by_reset": sorted(ours_reset),
        "balanced": not unattributed and not missing,
    }


def format_report(rec, live_positions):
    """Compact markdown. Deliberately terse -- this replaces per-session LLM
    reasoning, so it must not cost more tokens than the work it removes."""
    by_sym = {p["symbol"]: p for p in live_positions}

    def val(sym):
        p = by_sym.get(sym)
        return f" (${float(p['market_value']):,.0f})" if p and p.get("market_value") else ""

    agent, sib = rec["agent"], rec["sibling"]
    lines = ["## Position Reconciliation", ""]

    if not rec["ours_ok"]:
        lines += [
            f"⚠️ Could not read {agent}'s trade_log.md — ownership UNVERIFIED this session.",
            "Treat the position table above as unreconciled and confirm manually before sizing.",
            "",
        ]
        return lines

    if rec["balanced"]:
        lines.append(f"✅ **Balanced.** Every live position is attributed.")
    else:
        lines.append(f"🚨 **Does not balance — see reconciling items below.**")
    lines.append("")

    lines.append(f"- **{agent}'s positions** ({len(rec['matched'])}): "
                 + (", ".join(f"{s}{val(s)}" for s in rec["matched"]) or "none"))

    if rec["theirs_ok"]:
        lines.append(f"- **{sib}'s positions** ({len(rec['sibling_positions'])}): "
                     + (", ".join(f"{s}{val(s)}" for s in rec["sibling_positions"]) or "none"))
    else:
        lines.append(f"- **{sib}'s book**: not readable — cannot confirm the split.")

    if rec["unattributed"]:
        lines += [
            "",
            "🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**",
            "",
        ]
        for s in rec["unattributed"]:
            if s in rec["cleared_by_reset"]:
                lines.append(
                    f"  - {s}{val(s)} — was opened in {agent}'s log, then written off by a "
                    f"bulk liquidation/reset entry. The broker still holds it, so that "
                    f"liquidation record is almost certainly WRONG. Correct the log; do not "
                    f"re-buy on the assumption this position is closed."
                )
            else:
                lines.append(
                    f"  - {s}{val(s)} — do not size against this until ownership is resolved."
                )

    if rec["missing"]:
        lines += [
            "",
            f"🚨 **MISSING — in {agent}'s book but not held at the broker:**",
            "",
            *[f"  - {s} — likely a stop fill or manual close. Log the exit in trade_log.md."
              for s in rec["missing"]],
        ]

    lines.append("")
    return lines
