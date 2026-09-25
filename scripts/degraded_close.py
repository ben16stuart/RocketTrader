#!/usr/bin/env python3
"""No-LLM fallback for the market_close routine.

When Claude is unavailable at the close (the account-wide session limit is the usual
cause), the parts of market_close that matter most are deterministic and need no model:
the daily summary, the books-vs-broker reconcile check, and the memory push. This does
those, and nothing else.

What it does:
  1. syncs memory/portfolio_state.md from Alpaca,
  2. reconciles this agent's book against the broker,
  3. sends ONE ntfy summary (position table, day P&L vs benchmark, stops, orders),
  4. prepends a clearly-labelled note to memory/session_notes.md,
  5. commits and pushes memory/ (nothing else).

What it will NEVER do: place, cancel or modify an order; touch trade_log.md, lessons or
research_log.md; rebalance the core. Those need judgment and a live market, and the
summary says plainly that they were not done. Rebalance drift is reported for
information only -- it is executed at the next real market_close.

Why not a small local model instead? The agents load ~70-100k tokens of memory before
they can act and edit the files they run on; a 9B model doing that with permissions
skipped is a poor trade against a script that cannot damage anything.

Usage:
  python scripts/degraded_close.py               # run for real (run_agent.sh calls this)
  python scripts/degraded_close.py --dry-run     # compose and print; touch nothing
  python scripts/degraded_close.py --test        # send a "TEST" ntfy only; no memory/git writes
Flags: --no-push  --no-ntfy  --force (run even if a real close already succeeded today)
Env:   DEGRADED_WHY / DEGRADED_HINT  why the real close failed, and whether it may have run (run_agent.sh sets these)

Exit 0 = the summary was delivered (or dry-run); non-zero = it was not, so the caller
should fall back to its generic failure alert.
"""
import argparse
import glob
import math
import os
import subprocess
import sys
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

IS_BULL = os.path.basename(REPO) == "OpusTrader"
ME, SIB = ("Bull", "Rocket") if IS_BULL else ("Rocket", "Bull")
BENCH = "SPY" if IS_BULL else "IWM"          # each agent's benchmark, and its core sleeve
NOTES = os.path.join(REPO, "memory", "session_notes.md")

SAT_FLOOR_PCT = None if IS_BULL else 50.0     # Rocket's hard guardrail (CLAUDE.md, 2026-09-17)
BUFFER = 0.10                                 # 10% operating cash buffer
BAND = 0.03                                   # rebalance band, as a fraction of slice


def money(x, sign=False):
    return f"{'+' if sign and x >= 0 else ''}{'-' if x < 0 else ''}${abs(x):,.0f}"


def bench_return():
    """Today's benchmark % change. Bull's helper returns a tuple, Rocket's a float."""
    import scripts.market_data as md
    fn = getattr(md, "get_benchmark_daily_return", None) or getattr(md, "get_spy_daily_return")
    r = fn()
    return float(r[0] if isinstance(r, tuple) else r)


def rebalance_line(slice_, sat_val, core_val, core_qty, core_px):
    """Would the core rebalance have traded? Informational: this script never trades."""
    target = slice_ - sat_val - BUFFER * slice_
    if not IS_BULL:
        target = min(target, 0.50 * slice_)   # Rocket's IWM cap
    target = max(target, 0.0)
    drift = core_val - target
    in_band = abs(drift) <= BAND * slice_
    note = ""
    if IS_BULL and core_px:
        # Bull's core is whole SPY shares and its rule rounds the target UP.
        tq = target / core_px
        if not in_band and core_qty == math.ceil(tq):
            in_band, note = True, " (whole-share rounding)"
    verdict = "in band" if in_band else f"OUTSIDE the 3% band by {money(abs(drift))}"
    return (f"{BENCH} {money(core_val)} vs target {money(target)}{note} -> {verdict}", in_band)


def git(*args, check=False):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True, env=env)


def push_memory(message):
    """Stage memory/ ONLY, commit, push. Returns a one-line status."""
    git("add", "memory/")
    if git("diff", "--cached", "--quiet").returncode == 0:
        return "nothing new to commit"
    ident = []
    if not git("config", "user.name").stdout.strip():
        ident = ["-c", f"user.name={ME} Trading Agent", "-c", f"user.email={ME.lower()}@trading-agent.local"]
    c = git(*ident, "commit", "-m", message)
    if c.returncode != 0:
        return f"commit failed: {c.stderr.strip()[:120]}"
    p = git("push", "origin", "main")
    if p.returncode != 0:
        return f"committed locally, PUSH FAILED: {p.stderr.strip()[:120]}"
    return "committed and pushed"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--no-ntfy", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    write = not (a.dry_run or a.test)             # may this run write memory / git?

    today, now = date.today().isoformat(), datetime.now()
    stamp = now.astimezone().strftime("%H:%M %Z")
    # run_agent.sh passes the failure as two parts: WHY (what failed) and HINT (whether anything ran).
    why = os.environ.get("DEGRADED_WHY", "").strip() or "Claude was unavailable"
    hint = os.environ.get("DEGRADED_HINT", "").strip()
    why_short = why.split(". ")[0].rstrip(".")         # drop the "no fallback exists" boilerplate

    if not a.force and not a.test:
        for f in glob.glob(os.path.join(REPO, "logs", f"market_close_{today}_*.log")):
            if "── Done:" in open(f, errors="ignore").read():
                print(f"A real market_close already completed today ({os.path.basename(f)}); nothing to do.")
                return 0

    problems = []

    def stage(label, fn, default=None):
        try:
            return fn()
        except Exception as exc:                   # never let one broken stage kill the summary
            problems.append(f"{label}: {str(exc)[:90]}")
            return default

    from scripts.alpaca_client import AGENT_EQUITY_PCT, _get, get_account, get_open_orders, get_positions
    from scripts.position_reconciler import reconcile

    acct = stage("account", get_account, {}) or {}
    positions = stage("positions", get_positions, []) or []
    open_orders = stage("open orders", get_open_orders, []) or []
    if not acct or not positions:
        problems.append("no live Alpaca data")

    V = float(acct.get("portfolio_value", 0) or 0)
    slice_ = V * AGENT_EQUITY_PCT
    rec = stage("reconcile", lambda: reconcile(positions, REPO, ME, SIB), None) or {
        "core": [], "matched": [], "missing": [], "unattributed": [], "balanced": False}
    mv = {p["symbol"]: float(p["market_value"]) for p in positions}
    px = {p["symbol"]: float(p["current_price"]) for p in positions}
    qty = {p["symbol"]: float(p["qty"]) for p in positions}
    core_syms, sat_syms = rec["core"], rec["matched"]
    mine = set(core_syms) | set(sat_syms)

    core_val = sum(mv.get(s, 0) for s in core_syms)
    sat_val = sum(mv.get(s, 0) for s in sat_syms)
    cash_val = max(slice_ - core_val - sat_val, 0.0)
    pct = lambda v: (v / slice_ * 100) if slice_ else 0.0

    day_pl = sum(float(p.get("unrealized_intraday_pl") or 0) for p in positions if p["symbol"] in mine)
    prev_base = slice_ - day_pl
    day_pct = (day_pl / prev_base * 100) if prev_base else 0.0
    bench = stage("benchmark", bench_return, None)
    vs = f"{day_pct - bench:+.2f}pp" if bench is not None else "n/a"
    bench_txt = f"{bench:+.2f}%" if bench is not None else "n/a"

    table = stage("position table", lambda: __import__("scripts.position_table", fromlist=["x"]).build_table(),
                  "(position table unavailable)")

    orders = stage("orders", lambda: _get(f"/v2/orders?status=all&limit=100&direction=desc&after={today}"), []) or []
    watch = mine | set(rec["missing"]) | set(rec["unattributed"])
    todays = [o for o in orders if o.get("created_at", "")[:10] == today and o["symbol"] in watch]
    orders_txt = "; ".join(f"{o['side']} {o['symbol']} {o.get('filled_qty') or o.get('qty')} ({o['status']})"
                           for o in sorted(todays, key=lambda o: o["created_at"])) or "none"

    stop_syms = {o["symbol"] for o in open_orders if o.get("side") == "sell" and "stop" in o.get("type", "")}
    unstopped = [s for s in sat_syms if s not in stop_syms]
    stops_txt = (", ".join(sorted(s for s in sat_syms if s in stop_syms)) or "none needed (no satellites)")
    if unstopped:
        stops_txt += f"  ⚠️ NO STOP ON: {', '.join(unstopped)}"

    core_sym = core_syms[0] if core_syms else BENCH
    rb_txt, _ = rebalance_line(slice_, sat_val, core_val, qty.get(core_sym, 0.0), px.get(core_sym, 0.0))

    if rec["balanced"]:
        books = "✅ Balanced"
    else:
        bits = []
        if rec["missing"]:
            bits.append(f"MISSING {', '.join(rec['missing'])}")
        if rec["unattributed"]:
            bits.append(f"UNATTRIBUTED {', '.join(rec['unattributed'])}")
        books = "🚨 does NOT balance" + (f" — {'; '.join(bits)}" if bits else " (could not verify)")

    sat_line = f"Satellites {pct(sat_val):.1f}%"
    if SAT_FLOOR_PCT is not None:
        sat_line += f" (floor {SAT_FLOOR_PCT:.0f}% {'✅' if pct(sat_val) >= SAT_FLOOR_PCT else '🚨 breached'})"
    mix = f"{sat_line} | Core {pct(core_val):.1f}% | Cash {pct(cash_val):.1f}% of slice"

    banner = (f"⚠️ Today's close did not run: {why_short}. This is an AUTOMATED summary: no stop "
              f"review, rebalance or trade logging was done. {hint}").strip()

    title = f"{'📊 Bull' if IS_BULL else '🚀 Rocket'} — {now.strftime('%a %Y-%m-%d')} ⚠️ AUTOMATED"
    if a.test:
        title = "🧪 TEST — " + title
    body = "\n".join([
        banner, "",
        f"Day: {day_pct:+.2f}% ({money(day_pl, True)}) vs {BENCH} {bench_txt} -> {vs}   (as of {stamp})",
        mix, "", table, "",
        f"Books: {books}",
        f"Orders today: {orders_txt}",
        f"Stops armed: {stops_txt}",
        f"Rebalance (NOT executed): {rb_txt}",
        *([f"⚠️ Stages that failed: {'; '.join(problems)}"] if problems else []),
    ])

    note = "\n".join([
        f"## {today} — MARKET_CLOSE — DID NOT RUN [automated fallback, no LLM]",
        "",
        f"The market_close routine produced no output: {why_short}. {hint}".strip(),
        f"A no-LLM fallback (`scripts/degraded_close.py`) ran instead. It placed **no orders** and "
        f"touched no file except this note and `portfolio_state.md`.",
        "",
        "- **Done by the fallback:** portfolio snapshot synced, books reconciled, automated ntfy summary "
        "sent, memory commit and push attempted (the ntfy states the result).",
        "- **NOT done today:** stop review, core rebalance, fill logging in `trade_log.md`, lessons, "
        "and tomorrow's research priorities. Broker-side stops were unaffected.",
        f"- Day (as of {stamp}): {day_pct:+.2f}% ({money(day_pl, True)}) vs {BENCH} {bench_txt}. {mix}.",
        f"- Books vs broker: {books}.",
        f"- Orders today: {orders_txt}.",
        f"- Stops armed: {stops_txt}.",
        f"- Rebalance drift, informational and NOT executed: {rb_txt}. The core rebalance only runs at "
        f"`market_close`, so it is still owed if outside the band.",
        "",
        "---",
        "",
    ])

    print(f"=== {title} ===\n{body}\n")
    if a.dry_run:
        print("=== note that would be prepended to session_notes.md ===\n" + note)
        print("(dry run: nothing written, pushed or sent)")
        return 0

    if write:
        def snapshot():
            import scripts.portfolio_snapshot as snap
            text = snap.build_snapshot()
            with open(snap.MEMORY_FILE, "w") as fh:
                fh.write(text)
        stage("snapshot", snapshot)

        def add_note():
            body_txt = open(NOTES).read() if os.path.exists(NOTES) else "# Session Notes\n\n---\n\n"
            if f"## {today} — MARKET_CLOSE — DID NOT RUN" in body_txt:
                return
            i = body_txt.find("\n## ")
            new = body_txt + "\n" + note if i < 0 else body_txt[:i + 1] + note + body_txt[i + 1:]
            with open(NOTES, "w") as fh:
                fh.write(new)
        stage("session note", add_note)

        if not a.no_push:
            status = stage("push", lambda: push_memory(f"{ME} memory update — {today} (automated fallback close, no LLM)"),
                           "push errored")
            print(f"memory: {status}")
            body += f"\nMemory: {status}."

    if a.no_ntfy:
        return 0
    from scripts.ntfy_notify import send_notification
    ok = send_notification(title, body, priority="high")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
