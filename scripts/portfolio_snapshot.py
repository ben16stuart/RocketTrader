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
from scripts.alpaca_client import get_account, get_positions, get_open_orders, is_market_open

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "memory", "portfolio_state.md"
)

INCEPTION_DATE = "2026-04-20"
INCEPTION_PORTFOLIO_VALUE = 10_000.00


def get_spy_return_since_inception() -> float:
    try:
        sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        from scripts.market_data import get_spy_return
        return get_spy_return(INCEPTION_DATE)
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

    portfolio_value = float(account["portfolio_value"])
    cash            = float(account["cash"])
    invested        = portfolio_value - cash
    unrealized_pl   = float(account.get("unrealized_pl", 0))

    bull_return = (portfolio_value - INCEPTION_PORTFOLIO_VALUE) / INCEPTION_PORTFOLIO_VALUE * 100
    spy_return  = get_spy_return_since_inception()
    vs_spy      = bull_return - spy_return

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    trade_log_path = os.path.join(os.path.dirname(MEMORY_FILE), "trade_log.md")
    weekly_trades  = count_weekly_trades(trade_log_path)

    lines = [
        f"# Portfolio State",
        f"",
        f"**Last Updated**: {now_str}",
        f"**Account**: Alpaca Paper Trading",
        f"",
        f"---",
        f"",
        f"## Account Summary",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Account Value | ${portfolio_value:,.2f} |",
        f"| Cash Available | ${cash:,.2f} |",
        f"| Invested | ${invested:,.2f} |",
        f"| Unrealized P&L | ${unrealized_pl:+,.2f} |",
        f"| Bull return since inception | {bull_return:+.2f}% |",
        f"| SPY return since inception | {spy_return:+.2f}% |",
        f"| Bull vs SPY | {vs_spy:+.2f}% |",
        f"",
        f"**Inception Date**: {INCEPTION_DATE}",
        f"",
        f"---",
        f"",
        f"## Open Positions",
        f"",
    ]

    if positions:
        lines += [
            f"| Symbol | Shares | Entry Price | Current Price | Unrealized P&L | P&L % |",
            f"|--------|--------|-------------|---------------|----------------|-------|",
        ]
        for p in positions:
            sym    = p["symbol"]
            qty    = float(p["qty"])
            entry  = float(p["avg_entry_price"])
            curr   = float(p["current_price"])
            pl     = float(p["unrealized_pl"])
            pl_pct = float(p["unrealized_plpc"]) * 100
            lines.append(
                f"| {sym} | {qty:.0f} | ${entry:.2f} | ${curr:.2f} | ${pl:+,.2f} | {pl_pct:+.1f}% |"
            )
    else:
        lines.append("*No open positions.*")

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
