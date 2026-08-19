"""Render this agent's positions as a compact table for ntfy notifications.

Four figures per position, straight from Alpaca -- no arithmetic in the agent, so
the numbers can't drift from what the broker actually reports:

  today %    unrealized_intraday_plpc
  today $    unrealized_intraday_pl     position profit, NOT the share price move
  total %    unrealized_plpc
  total $    unrealized_pl              position profit since entry

The dollar columns are whole-position P&L (qty x price move), which is what you
actually made or lost, rather than the per-share price change.

Ownership comes from position_reconciler, so Rocket's notification lists Rocket's
positions only -- the Alpaca account is shared and a raw get_positions() would
show the sibling's holdings too.

Usage: python scripts/position_table.py          # this agent's table
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.alpaca_client import get_positions
from scripts.position_reconciler import reconcile

AGENT = "Rocket"
SIBLING = "Bull"


def _fmt_money(v):
    """Compact signed dollars: +$1.2k / -$62 / +$8.40."""
    a = abs(v)
    if a >= 1000:
        return f"{'+' if v >= 0 else '-'}${a/1000:.1f}k"
    if a >= 100:
        return f"{'+' if v >= 0 else '-'}${a:.0f}"
    return f"{'+' if v >= 0 else '-'}${a:.2f}"


def build_table(repo_dir=None, agent=AGENT, sibling=SIBLING):
    repo_dir = repo_dir or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    positions = get_positions()
    rec = reconcile(positions, repo_dir, agent, sibling)

    mine = set(rec.get("core", [])) | set(rec.get("matched", []))
    rows = [p for p in positions if p["symbol"] in mine]
    if not rows:
        return "No open positions."

    core = set(rec.get("core", []))
    # Core first, then satellites by size -- core is the resting state, so it
    # reads as the baseline the active bets sit on top of.
    rows.sort(key=lambda p: (p["symbol"] not in core, -float(p["market_value"])))

    lines = ["         today          all-time"]
    d_tot = t_tot = 0.0
    for p in rows:
        sym = p["symbol"]
        d_pct = float(p["unrealized_intraday_plpc"]) * 100
        d_usd = float(p["unrealized_intraday_pl"])
        t_pct = float(p["unrealized_plpc"]) * 100
        t_usd = float(p["unrealized_pl"])
        d_tot += d_usd
        t_tot += t_usd
        tag = "*" if sym in core else " "
        lines.append(
            f"{sym:<5}{tag}{d_pct:+6.2f}% {_fmt_money(d_usd):>8} |"
            f"{t_pct:+7.2f}% {_fmt_money(t_usd):>8}"
        )

    lines.append(f"{'TOTAL':<6}{'':>7} {_fmt_money(d_tot):>8} |{'':>8} {_fmt_money(t_tot):>8}")
    if core:
        lines.append("* = core (benchmark sleeve)")
    return "\n".join(lines)


if __name__ == "__main__":
    try:
        print(build_table())
    except Exception as exc:  # never break a notification over a table
        print(f"(position table unavailable: {exc})")
