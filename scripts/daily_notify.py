#!/usr/bin/env python3
"""The daily ntfy summary, one fixed layout for both agents (since 2026-10-13).

Ben reads the lock-screen preview: the title plus about three lines. So the order is
fixed by script, not by whatever the model writes that day:

  TITLE   🐂 Bull -0.56% vs SPY -0.02% today         <- performance vs benchmark
  line 1  Since 7/20: +4.41% vs SPY +4.83% (-0.42)    <- the scoreboard
  line 2  Today: bought DELL, NUE · sold MU (stop)    <- activity
  line 3  Picks 83% (8) · SPY 12% · cash 5%           <- how the book is deployed
  ----    details: performance table, positions, every fill, stops, books, notes

Every number comes from the broker or agent_performance.py (each agent's OWN book,
time-weighted). The model contributes only --notes: two to four short lines of plain
English, such as what it did and why, and the plan for tomorrow.

Usage:
  python scripts/daily_notify.py --notes "..."    # build and send (market_close STEP)
  python scripts/daily_notify.py --dry-run        # print, send nothing
Identical file in OpusTrader and RocketTrader; the agent is read from the repo path.
"""
import argparse
import os
import sys
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

IS_BULL = os.path.basename(REPO) == "OpusTrader"
ME, SIB = ("Bull", "Rocket") if IS_BULL else ("Rocket", "Bull")
BENCH = "SPY" if IS_BULL else "IWM"
ICON = "🐂" if IS_BULL else "🚀"
FLOOR = 0.50
# The 50% floor took effect for Rocket on 9/17; Bull's on 10/6 with a ramp week, so its count starts 10/12.
FLOOR_SINCE = date(2026, 10, 12) if IS_BULL else date(2026, 9, 17)


def pct(x, nd=2):
    return "n/a" if x is None else f"{100 * x:+.{nd}f}%"


def pts(a, b):
    return "" if a is None or b is None else f"{100 * (a - b):+.2f}"


TIE_PTS = 0.05   # |agent - benchmark| under 0.05 percentage points counts as a tie


def verdict(a, b):
    """🟢 beat / 🟡 tied / 🔴 lost the benchmark today; ⚪ if either number is missing."""
    if a is None or b is None:
        return "⚪"
    d = 100 * (a - b)
    return "🟡" if abs(d) < TIE_PTS else ("🟢" if d > 0 else "🔴")


def money(x):
    return f"{'+' if x >= 0 else '-'}${abs(x):,.0f}"


def _realized(fills, sym, sell_idx):
    """Realized $ on the sell fill at sell_idx, from the running average cost of `sym`'s fills."""
    qty = cost = 0.0
    for i, f in fills[fills.sym == sym].sort_values("time").iterrows():
        if f.qty > 0:
            cost += f.qty * f.px
            qty += f.qty
        else:
            if qty <= 0:
                return None                   # held before the fill history begins: cost unknown
            avg = cost / qty
            if i == sell_idx:
                return (f.px - avg) * -f.qty
            cost -= avg * -f.qty
            qty += f.qty
    return None


def build(notes=None, banner=None, extra=None):
    from scripts.alpaca_client import _get, get_account, get_open_orders, get_positions
    from scripts.position_reconciler import reconcile
    problems = []

    # ---- performance (each agent's own book). Fallback: today's intraday P&L only.
    perf = None
    try:
        from scripts.agent_performance import compute, REBASE
        perf = compute()
    except Exception as exc:
        problems.append(f"performance history unavailable ({str(exc)[:80]})")

    positions = get_positions()
    acct = get_account()
    slice_ = float(acct["portfolio_value"]) * (0.70 if IS_BULL else 0.30)
    rec = reconcile(positions, REPO, ME, SIB)
    mv = {p["symbol"]: float(p["market_value"]) for p in positions}
    sats, core = rec.get("matched", []), rec.get("core", [])
    sat_v, core_v = sum(mv.get(s, 0) for s in sats), sum(mv.get(s, 0) for s in core)
    cash_v = max(slice_ - sat_v - core_v, 0.0)

    if perf:
        t, b = perf["today"]["ret"], perf["today"]["bench"]
        since = perf["since_rebase"]
    else:
        mine = set(sats) | set(core)
        day_pl = sum(float(p.get("unrealized_intraday_pl") or 0) for p in positions if p["symbol"] in mine)
        t = day_pl / (slice_ - day_pl) if slice_ else None
        try:
            import scripts.market_data as md
            fn = getattr(md, "get_benchmark_daily_return", None) or getattr(md, "get_spy_daily_return")
            r = fn()
            b = float(r[0] if isinstance(r, tuple) else r) / 100
        except Exception:
            b = None
        since = None

    # ---- activity: today's fills for this agent, with order type and realized P&L
    acts, act_lines = [], []
    if perf is not None and len(perf["fills_today"]):
        ft = perf["fills_today"]
        try:
            day0 = f"{perf['asof']}T00:00:00-04:00"
            otype = {o["id"]: o["type"] for o in _get(f"/v2/orders?status=closed&limit=200&after={day0}")}
        except Exception:
            otype = {}
        for sym, g in ft.groupby("sym", sort=False):
            for side, gs in g.groupby("side", sort=False):
                q = gs.qty.abs().sum()
                avg = (gs.qty.abs() * gs.px).sum() / q
                is_core = sym == BENCH
                stop = any(otype.get(o) == "trailing_stop" for o in gs.order_id)
                qtxt = f"{q:g}" if q == int(q) else f"{q:.3f}"
                if side == "buy":
                    act_lines.append(f"Bought {sym} {qtxt} @ ${avg:,.2f} (${q * avg:,.0f})" + (" — core" if is_core else ""))
                    acts.append(f"{sym} core +" if is_core else f"bought {sym}")
                else:
                    pl = None if is_core else sum(filter(None, (_realized(perf["fills"], sym, i) for i in gs.index))) or None
                    why = "stop hit" if stop else ("core" if is_core else "sold")
                    pl_txt = f", {money(pl)}" if pl is not None else ""
                    act_lines.append(f"Sold {sym} {qtxt} @ ${avg:,.2f} (${q * avg:,.0f}) — {why}{pl_txt}")
                    acts.append(f"{sym} core -" if is_core else (f"sold {sym} ({'stop' if stop else 'exit'}{pl_txt})"))
    picks = [a for a in acts if "core" not in a]
    if picks:
        activity = "Today: " + " · ".join(picks)
    elif acts:
        activity = f"Today: no stock trades ({BENCH} core rebalanced)"
    else:
        activity = "Today: no trades"

    # ---- deployment line, with the floor
    sp = sat_v / slice_ if slice_ else 0.0
    mix = f"Picks {100 * sp:.0f}% ({len(sats)}) · {BENCH} {100 * core_v / slice_:.0f}% · cash {100 * cash_v / slice_:.0f}%"
    if sp < FLOOR:
        streak = 0
        if perf is not None and "sat_pct" in perf["daily"]:
            daily = perf["daily"]
            for d, v in zip(reversed(list(daily.index)), reversed(list(daily.sat_pct))):
                if d < FLOOR_SINCE:
                    break
                if v < FLOOR:
                    streak += 1
                else:
                    break
        mix += f" — 🚨 below 50% floor" + (f", day {streak}" if streak else "")

    # ---- title and preview lines
    title = f"{verdict(t, b)} {ICON} {ME} {pct(t)} vs {BENCH} {pct(b)} today"
    lead = []
    if banner:   # automated fallback close: flag it in the title, explain it first in the details
        title = title.replace(f" {ICON} ", f" ⚠️ {ICON} ", 1) + " (auto)"
    if since:
        lead.append(f"Since 7/20: {pct(since['ret'])} vs {BENCH} {pct(since['bench'])} ({pts(since['ret'], since['bench'])} pts)")
    lead += [activity, mix]

    # ---- details
    det = (["", banner] if banner else []) + ["", "── Performance ──", f"{'':11s}{ME:>8s}{BENCH:>8s}{'+/-':>7s}"]
    if perf:
        for k, lab in (("today", "Today"), ("week", "This week"), ("since_reset", "Since 10/6"),
                       ("since_rebase", "Since 7/20")):
            v = perf.get(k)
            if v:
                det.append(f"{lab:11s}{pct(v['ret']):>8s}{pct(v['bench']):>8s}{pts(v['ret'], v['bench']):>7s}")
    else:
        det.append(f"{'Today':11s}{pct(t):>8s}{pct(b):>8s}{pts(t, b):>7s}")

    try:
        from scripts.position_table import build_table
        det += ["", "── Positions (today | all-time, $ = whole position) ──", build_table(REPO, ME, SIB)]
    except Exception as exc:
        problems.append(f"position table: {str(exc)[:60]}")

    det += ["", "── Trades today ──"] + (act_lines or ["None."])

    stop_syms = {o["symbol"] for o in get_open_orders() if o.get("side") == "sell" and "stop" in o.get("type", "")}
    naked = [s for s in sats if s not in stop_syms]
    books = "✅ balanced" if rec.get("balanced") else "🚨 do NOT balance — check portfolio_state.md"
    det += ["", (f"Stops armed: {len(sats) - len(naked)}/{len(sats)} picks" if sats else "Stops: no picks to protect") +
            (f"  ⚠️ NO STOP: {', '.join(naked)}" if naked else "") + f" · Books vs broker: {books}"]
    if perf is not None and perf.get("unattributed"):
        det.append(f"⚠️ Unattributed fills: {', '.join(perf['unattributed'])}")
    det += list(extra or [])
    if notes:
        det += ["", "── Notes ──", notes.strip()]
    if problems:
        det += ["", "⚠️ " + "; ".join(problems)]
    det += ["", f"Returns: {ME}'s own positions on its {'70' if IS_BULL else '30'}% slice, time-weighted, "
                f"price-only, rebuilt from broker fills."]
    body = "\n".join(lead + det)
    return title, body, dict(today=t, bench=b, since=since, mix=mix, activity=activity, perf=perf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notes", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--priority", default="default")
    a = ap.parse_args()
    title, body, _ = build(notes=a.notes)
    print(f"=== {title} ===\n{body}\n({len(body.encode())} bytes)")
    if a.dry_run:
        return 0
    from scripts.ntfy_notify import send_notification
    return 0 if send_notification(title, body, priority=a.priority) else 1


if __name__ == "__main__":
    sys.exit(main())
