"""
Sync live Alpaca account state into memory/portfolio_state.md.
Run at the start of every routine session.
Usage: python scripts/portfolio_snapshot.py
"""
import os
import sys
from datetime import datetime, timezone

# Allow running from project root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.alpaca_client import get_account, get_positions, get_open_orders, is_market_open, AGENT_EQUITY_PCT

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "memory", "portfolio_state.md"
)

# Original standalone-account inception (kept for historical reference in weekly_reviews/).
ORIGINAL_INCEPTION_DATE = "2026-04-20"

# Bull and Rocket merged onto one shared Alpaca account on this date. From here forward,
# "return since inception" tracks Rocket's AGENT_EQUITY_PCT slice of the shared account,
# rebased at the moment of the merge — not the original standalone $100k baseline, which
# no longer applies once the account is shared. Prior performance is preserved in
# memory/weekly_reviews/ and is not erased, just no longer the live tracking baseline.
REBASE_DATE = "2026-07-20"
REBASE_ALLOCATED_VALUE = 3_031.73  # Rocket's 30% slice of $10,105.77 shared value at rebase


def get_spy_return_since_inception() -> float:
    try:
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from scripts.market_data import get_spy_return
        return get_spy_return(REBASE_DATE)
    except Exception:
        return 0.0


def count_weekly_trades(trade_log_path: str) -> int:
    """Count trades placed this calendar week from trade_log.md."""
    try:
        from datetime import date
        today = date.today()
        week_start = today - __import__("datetime").timedelta(days=today.weekday())
        count = 0
        with open(trade_log_path) as f:
            for line in f:
                if line.startswith("## "):
                    parts = line.split("—")
                    if len(parts) >= 3 and "BUY" in line:
                        try:
                            trade_date = __import__("datetime").date.fromisoformat(parts[0].strip("## ").strip())
                            if trade_date >= week_start:
                                count += 1
                        except ValueError:
                            pass
        return count
    except Exception:
        return 0


def build_snapshot() -> str:
    account   = get_account()
    positions = get_positions()
    orders    = get_open_orders()

    shared_account_value = float(account["portfolio_value"])
    cash                 = float(account["cash"])
    unrealized_pl        = float(account.get("unrealized_pl", 0))

    allocated_equity = shared_account_value * AGENT_EQUITY_PCT
    invested         = shared_account_value - cash

    rocket_return = (allocated_equity - REBASE_ALLOCATED_VALUE) / REBASE_ALLOCATED_VALUE * 100
    spy_return    = get_spy_return_since_inception()
    vs_spy        = rocket_return - spy_return

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    trade_log_path = os.path.join(os.path.dirname(MEMORY_FILE), "trade_log.md")
    weekly_trades  = count_weekly_trades(trade_log_path)

    lines = [
        f"# Portfolio State",
        f"",
        f"**Last Updated**: {now_str}",
        f"**Account**: Alpaca Paper Trading — SHARED with Bull (merged {REBASE_DATE})",
        f"",
        f"---",
        f"",
        f"## Account Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Shared Account Value (Bull + Rocket) | ${shared_account_value:,.2f} |",
        f"| Rocket's Allocated Slice ({AGENT_EQUITY_PCT:.0%}) | ${allocated_equity:,.2f} |",
        f"| Cash Available (shared, pooled) | ${cash:,.2f} |",
        f"| Total Invested (both agents) | ${invested:,.2f} |",
        f"| Unrealized P&L (shared) | ${unrealized_pl:+,.2f} |",
        f"| Rocket return since rebase | {rocket_return:+.2f}% |",
        f"| SPY return since rebase | {spy_return:+.2f}% |",
        f"| Rocket vs SPY | {vs_spy:+.2f}% |",
        f"",
        f"**Rebase Date**: {REBASE_DATE} (account merged with Bull — prior standalone",
        f"history since {ORIGINAL_INCEPTION_DATE} is preserved in memory/weekly_reviews/)",
        f"",
        f"⚠️ **Cash and buying power above are POOLED with Bull.** Before sizing any",
        f"trade, check actual available cash — do not assume the full allocated slice",
        f"is available if Bull has open positions consuming shared cash.",
        f"",
        f"---",
        f"",
        f"## Open Positions (shared account — yours AND Bull's)",
        f"",
        f"Ownership is reconciled below — do not re-derive it from the trade log.",
        f"",
    ]

    if positions:
        # Alpaca's `current_price` is the last TRADE, which outside regular hours is a
        # thin pre/post-market print — while `avg_entry_price` in the same row is a
        # settled fill. Printing them side by side with no session label puts two
        # different dates in one row. Emit the session state and carry the settled
        # prior close alongside. (Fix mirrored from OpusTrader 2026-09-02.)
        _open = is_market_open()
        _price_hdr = "Price (LIVE, session open)" if _open else "Price (⚠️ NOT a settled close)"
        lines += [
            f"| Symbol | Shares | Entry Price | {_price_hdr} | Prior Settled Close | Unrealized P&L | P&L % |",
            f"|--------|--------|-------------|---------------|---------------------|----------------|-------|",
        ]
        for p in positions:
            sym    = p["symbol"]
            qty    = float(p["qty"])
            entry  = float(p["avg_entry_price"])
            curr   = float(p["current_price"])
            prior  = p.get("lastday_price")
            prior  = f"${float(prior):.2f}" if prior else "—"
            pl     = float(p["unrealized_pl"])
            pl_pct = float(p["unrealized_plpc"]) * 100
            lines.append(
                f"| {sym} | {qty:.0f} | ${entry:.2f} | ${curr:.2f} | {prior} | ${pl:+,.2f} | {pl_pct:+.1f}% |"
            )
        if not _open:
            lines += [
                f"",
                f"⚠️ **The market is CLOSED. The price column is the last trade, which outside",
                f"regular hours can be a single thin pre/post-market print — it is NOT a settled",
                f"close and must never be recorded as one, quoted as a session move, or used to",
                f"decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on",
                f"regular-hours trades only. Use the **Prior Settled Close** column for anything",
                f"written into memory; re-read live at `market_open`.",
            ]
    else:
        lines.append("*No open positions.*")

    # Reconcile both books against the broker before anything downstream sizes a
    # trade off this file. Wrapped in try/except on purpose: this is a diagnostic
    # layer inside a live trading routine, and it must never be the reason
    # market_close fails to produce a snapshot.
    try:
        from scripts.position_reconciler import reconcile, format_report
        _repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        _rec = reconcile(positions, _repo, "Rocket", "Bull")
        lines += ["", "---", ""] + format_report(_rec, positions)
    except Exception as _exc:
        lines += [
            "", "---", "", "## Position Reconciliation", "",
            f"⚠️ Reconciliation unavailable ({_exc}). Ownership is UNVERIFIED this",
            "session — confirm manually before sizing any trade.", "",
        ]

    lines += [
        f"",
        f"---",
        f"",
        f"## Open Orders",
        f"",
    ]

    if orders:
        lines += [
            f"| Order ID | Symbol | Side | Qty | Type | Status |",
            f"|----------|--------|------|-----|------|--------|",
        ]
        for o in orders:
            lines.append(
                f"| {o['id'][:8]}… | {o['symbol']} | {o['side']} | "
                f"{o.get('qty','?')} | {o['type']} | {o['status']} |"
            )
    else:
        lines.append("*No pending orders.*")

    lines += [
        f"",
        f"---",
        f"",
        f"## Weekly Trade Count",
        f"",
        f"Trades placed this week: {weekly_trades} / 3 max",
        f"Market open: {'Yes' if is_market_open() else 'No'}",
    ]

    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    if not os.environ.get("ALPACA_API_KEY") or not os.environ.get("ALPACA_SECRET_KEY"):
        print("ERROR: ALPACA_API_KEY and ALPACA_SECRET_KEY must be set.")
        sys.exit(1)

    print("Syncing portfolio state from Alpaca...")
    snapshot = build_snapshot()

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        f.write(snapshot)

    print(f"Written to {MEMORY_FILE}")
    print()

    # Also print summary to stdout for agent context
    for line in snapshot.split("\n")[:25]:
        print(line)
