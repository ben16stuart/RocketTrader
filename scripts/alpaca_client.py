"""
Alpaca paper trading API client.
Usage: python scripts/alpaca_client.py <command> [args]
"""
import os
import sys
import json
import math
from datetime import datetime, timezone

import requests

BASE_URL    = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")
API_KEY     = os.environ.get("ALPACA_API_KEY", "")
SECRET_KEY  = os.environ.get("ALPACA_SECRET_KEY", "")

# Bull and Rocket share one Alpaca paper account (merged 2026-07-20).
# Guardrails and position sizing are scaled to each agent's slice of the
# LIVE shared equity — not a fixed dollar figure — so they stay correct
# regardless of how the shared account's total balance moves.
AGENT_EQUITY_PCT = 0.30  # Rocket's share of the shared account

HEADERS = {
    "APCA-API-KEY-ID":     API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
    "Content-Type":        "application/json",
}


def _get(path: str) -> dict:
    r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def _post(path: str, body: dict) -> dict:
    r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=body, timeout=10)
    r.raise_for_status()
    return r.json()


def _delete(path: str) -> None:
    r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=10)
    r.raise_for_status()


def get_account() -> dict:
    return _get("/v2/account")


def get_positions() -> list:
    return _get("/v2/positions")


def get_position(symbol: str) -> dict:
    return _get(f"/v2/positions/{symbol}")


def get_open_orders() -> list:
    return _get("/v2/orders?status=open")


def is_market_open() -> bool:
    clock = _get("/v2/clock")
    return clock.get("is_open", False)


def _fmt_qty(qty) -> str:
    """Render an order quantity for Alpaca, fractional shares included.

    Alpaca accepts fractional qty (up to 9dp) on market/day orders, which is exactly
    what place_market_order sends. Whole numbers render without a trailing '.0' so
    integer orders look unchanged in the order JSON.
    """
    q = float(qty)
    if q == int(q):
        return str(int(q))
    return f"{q:.9f}".rstrip("0").rstrip(".")


def place_market_order(symbol: str, qty, side: str) -> dict:
    """Place a simple market order. side = 'buy' or 'sell'.

    qty may be fractional — the core (IWM) sleeve needs this. IWM at ~$300 against a
    ~$3,100 slice makes one whole share 9.6% of the book versus a 3% rebalance band,
    so whole-share-only rebalancing left ~14% permanently in idle cash (lesson 7a).
    """
    body = {
        "symbol":        symbol.upper(),
        "qty":           _fmt_qty(qty),
        "side":          side,
        "type":          "market",
        "time_in_force": "day",
    }
    return _post("/v2/orders", body)


def place_trailing_stop(symbol: str, qty: int, trail_percent: float = 10.0) -> dict:
    """Sell trailing stop order — trails price by trail_percent%.

    Alpaca rejects fractional qty on trailing stops, so satellites must be sized in
    whole shares. Fail loudly rather than leave a position silently unprotected.
    """
    if float(qty) != int(float(qty)):
        raise ValueError(
            f"Trailing stops require whole shares; got {qty} for {symbol}. "
            "Size satellites in whole shares — only the stopless IWM core may be fractional."
        )
    qty = int(float(qty))
    body = {
        "symbol":          symbol.upper(),
        "qty":             str(qty),
        "side":            "sell",
        "type":            "trailing_stop",
        "time_in_force":   "gtc",
        "trail_percent":   str(trail_percent),
    }
    return _post("/v2/orders", body)


def cancel_order(order_id: str) -> None:
    _delete(f"/v2/orders/{order_id}")


def cancel_all_orders() -> None:
    orders = get_open_orders()
    for o in orders:
        try:
            cancel_order(o["id"])
        except Exception as e:
            print(f"  Could not cancel {o['id']}: {e}")
    print(f"Cancelled {len(orders)} orders.")


def cancel_stops_for_symbol(symbol: str) -> None:
    orders = get_open_orders()
    cancelled = 0
    for o in orders:
        if o["symbol"] == symbol.upper() and o["type"] == "trailing_stop":
            cancel_order(o["id"])
            cancelled += 1
    print(f"Cancelled {cancelled} trailing stop(s) for {symbol}.")


def close_position(symbol: str) -> dict:
    r = requests.delete(
        f"{BASE_URL}/v2/positions/{symbol.upper()}",
        headers=HEADERS, timeout=10
    )
    r.raise_for_status()
    return r.json()


def liquidate_all() -> None:
    positions = get_positions()
    for p in positions:
        try:
            close_position(p["symbol"])
            print(f"  Closed {p['symbol']}")
        except Exception as e:
            print(f"  Could not close {p['symbol']}: {e}")


def calculate_shares(symbol: str, entry_price: float, stop_price: float) -> dict:
    """Calculate position size using Rocket's 1.5% risk rule with 15% cap,
    scaled to Rocket's AGENT_EQUITY_PCT slice of the shared account."""
    account = get_account()
    shared_account_value = float(account["portfolio_value"])
    allocated_equity      = shared_account_value * AGENT_EQUITY_PCT

    risk_dollars   = allocated_equity * 0.015
    stop_distance  = abs(entry_price - stop_price)
    if stop_distance == 0:
        return {"error": "stop_price equals entry_price"}

    shares_from_risk = int(risk_dollars / stop_distance)
    max_shares       = int((allocated_equity * 0.15) / entry_price)
    final_shares     = min(shares_from_risk, max_shares)
    position_value   = final_shares * entry_price

    return {
        "symbol":              symbol.upper(),
        "entry_price":         entry_price,
        "stop_price":          stop_price,
        "shared_account_value": shared_account_value,
        "allocated_equity":    round(allocated_equity, 2),
        "risk_dollars":        round(risk_dollars, 2),
        "shares_from_risk":    shares_from_risk,
        "max_shares":          max_shares,
        "final_shares":        final_shares,
        "position_value":      round(position_value, 2),
        "pct_of_allocated":    round(position_value / allocated_equity * 100, 1) if allocated_equity else 0,
    }


def print_account_summary() -> None:
    a = get_account()
    shared_value = float(a['portfolio_value'])
    print(f"Shared Account Value: ${shared_value:,.2f}  (Bull + Rocket)")
    print(f"Rocket's Allocated Slice ({AGENT_EQUITY_PCT:.0%}): ${shared_value * AGENT_EQUITY_PCT:,.2f}")
    print(f"Cash:            ${float(a['cash']):,.2f}")
    print(f"Buying Power:    ${float(a['buying_power']):,.2f}")
    print(f"Unrealized P&L:  ${float(a.get('unrealized_pl', 0)):,.2f}")
    print(f"Market Open:     {is_market_open()}")


def print_positions() -> None:
    positions = get_positions()
    if not positions:
        print("No open positions.")
        return
    print(f"\n{'Symbol':<8} {'Qty':>6} {'Entry':>8} {'Current':>8} {'P&L':>10} {'P&L%':>7}")
    print("-" * 55)
    for p in positions:
        sym    = p["symbol"]
        qty    = float(p["qty"])
        entry  = float(p["avg_entry_price"])
        curr   = float(p["current_price"])
        pl     = float(p["unrealized_pl"])
        pl_pct = float(p["unrealized_plpc"]) * 100
        print(f"{sym:<8} {qty:>6.0f} {entry:>8.2f} {curr:>8.2f} {pl:>+10.2f} {pl_pct:>+6.1f}%")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if not API_KEY or not SECRET_KEY:
        print("ERROR: ALPACA_API_KEY and ALPACA_SECRET_KEY must be set in environment.")
        sys.exit(1)

    args = sys.argv[1:]
    if not args:
        print("Usage: alpaca_client.py <command> [args]")
        print("Commands: account, positions, buy, sell, close, trailing_stop,")
        print("          cancel_all, cancel_stops, liquidate_all, size, market_open")
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "account":
        print_account_summary()

    elif cmd == "positions":
        print_positions()

    elif cmd == "market_open":
        print("Market is open:" if is_market_open() else "Market is closed.")

    elif cmd == "buy":
        # alpaca_client.py buy SYMBOL SHARES   (SHARES may be fractional, e.g. 1.47)
        sym, shares = args[1].upper(), float(args[2])
        result = place_market_order(sym, shares, "buy")
        print(json.dumps(result, indent=2))

    elif cmd == "sell":
        # Partial reductions go through here — `close` always fully liquidates.
        sym, shares = args[1].upper(), float(args[2])
        result = place_market_order(sym, shares, "sell")
        print(json.dumps(result, indent=2))

    elif cmd == "close":
        sym = args[1].upper()
        result = close_position(sym)
        print(json.dumps(result, indent=2))

    elif cmd == "trailing_stop":
        # alpaca_client.py trailing_stop SYMBOL TRAIL_PCT
        sym       = args[1].upper()
        trail_pct = float(args[2]) if len(args) > 2 else 10.0
        pos       = get_position(sym)
        qty       = int(float(pos["qty"]))
        result    = place_trailing_stop(sym, qty, trail_pct)
        print(json.dumps(result, indent=2))

    elif cmd == "cancel_all":
        cancel_all_orders()

    elif cmd == "cancel_stops":
        sym = args[1].upper()
        cancel_stops_for_symbol(sym)

    elif cmd == "liquidate_all":
        confirm = input("Type YES to liquidate ALL positions: ")
        if confirm == "YES":
            liquidate_all()
        else:
            print("Aborted.")

    elif cmd == "size":
        # alpaca_client.py size SYMBOL ENTRY_PRICE STOP_PRICE
        sym        = args[1].upper()
        entry      = float(args[2])
        stop       = float(args[3])
        result     = calculate_shares(sym, entry, stop)
        for k, v in result.items():
            print(f"  {k}: {v}")

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
