"""
Small cap scanner — finds momentum and catalyst candidates in the $50M–$2B market cap range.
Excludes S&P 500 components. Uses finviz screener for filtering + yfinance for detail.

Usage:
  python scripts/smallcap_scanner.py top_movers       # Top % gainers today with volume
  python scripts/smallcap_scanner.py unusual_volume   # 3x+ avg volume surges
  python scripts/smallcap_scanner.py short_squeeze    # High short float + volume surge
  python scripts/smallcap_scanner.py breakouts        # Near 52-week highs with volume
  python scripts/smallcap_scanner.py detail TICKER    # Full detail on a specific ticker
"""

import sys
import time
from datetime import datetime, timedelta

import yfinance as yf
import pandas as pd

try:
    from finviz.screener import Screener
    HAS_FINVIZ = True
except ImportError:
    HAS_FINVIZ = False
    print("Warning: finviz not installed — install with: pip install finviz")
    print("Falling back to yfinance-only mode with predefined universe.\n")


# ---------------------------------------------------------------------------
# S&P 500 components to exclude (top 100 by weight — keep list lean)
# ---------------------------------------------------------------------------
SP500_EXCLUDE = {
    "AAPL","MSFT","NVDA","AMZN","GOOGL","GOOG","META","TSLA","AVGO","BRK.B",
    "JPM","LLY","UNH","V","XOM","MA","COST","HD","PG","JNJ","WMT","ABBV",
    "NFLX","BAC","CRM","CVX","MRK","AMD","ORCL","KO","PEP","TMO","ACN","CSCO",
    "MCD","ABT","GE","CAT","LIN","IBM","TXN","NOW","ISRG","PM","QCOM","GS",
    "INTU","SPGI","UBER","AMGN","MS","HON","RTX","NEE","LOW","DHR","PFE",
    "UNP","T","BKNG","VRTX","C","BSX","AXP","SCHW","BX","SYK","DE","PLD",
    "TMUS","ETN","CB","MDT","SO","DUK","MO","CME","ZTS","CL","MMC","HCA",
    "PANW","TJX","MCO","WM","TGT","USB","AON","PYPL","APH","INTC","F","GM",
    "BAX","BDX","ELV","CI","HUM","CVS","WBA","WFC","AIG","PRU","ALL","MET",
}


# ---------------------------------------------------------------------------
# Finviz screener helpers
# ---------------------------------------------------------------------------

def _unshift(row: dict) -> dict:
    """Correct finviz's off-by-one column shift.

    Finviz renders a logo cell ahead of the ticker, so every value lands under the
    preceding column's header ('Ticker' gets a stray initial, 'Company' gets the real
    ticker) and the final column falls off the end. Detected by the stray value being a
    single character that prefixes the real ticker; returns the row untouched otherwise
    so this self-disables if finviz reverts.
    """
    keys = list(row.keys())
    vals = list(row.values())
    if len(keys) < 3:
        return row
    stray, real = str(vals[1]), str(vals[2])
    if len(stray) != 1 or not real.startswith(stray):
        return row
    fixed = {keys[0]: vals[0]}
    for i in range(1, len(keys) - 1):
        fixed[keys[i]] = vals[i + 1]
    fixed[keys[-1]] = ""  # last column is truncated by the shift
    return fixed


def _screen_table(filters: list, order: str, limit: int, table: str) -> dict:
    """Fetch one finviz table view, de-shifted, keyed by ticker."""
    try:
        rows = Screener(filters=filters, order=order, rows=limit, table=table).data
    except Exception as e:
        print(f"Finviz screener error ({table}): {e}")
        return {}
    out = {}
    for r in rows:
        r = _unshift(r)
        sym = r.get("Ticker", "")
        if sym:
            out[sym] = r
    return out


def _run_screener(filters: list, order: str = "-change", limit: int = 30) -> list[dict]:
    """Run finviz screener with given filters. Returns list of ticker dicts.

    Merges three table views because no single one carries every field Rocket needs:
    Overview (price/cap/sector), Performance (rel + avg volume), Ownership (float/short).
    """
    if not HAS_FINVIZ:
        return []

    overview = _screen_table(filters, order, limit, "Overview")
    if not overview:
        return []
    perf = _screen_table(filters, order, limit, "Performance")
    own = _screen_table(filters, order, limit, "Ownership")

    results = []
    for ticker, s in overview.items():
        if ticker in SP500_EXCLUDE:
            continue
        p = perf.get(ticker, {})
        o = own.get(ticker, {})
        results.append({
            "symbol":       ticker,
            "company":      s.get("Company", ""),
            "sector":       s.get("Sector", ""),
            "price":        _safe_float(s.get("Price")),
            # Finviz renamed this header 'Change' -> 'Change %' (broke 2026-08-03,
            # silently zeroing every row for 5 sessions). Accept both spellings.
            "change_pct":   _safe_float(str(s.get("Change %", s.get("Change", ""))).rstrip("%")),
            "volume":       _safe_int(o.get("Volume", "").replace(",", "")),
            "avg_volume":   _parse_vol(p.get("Avg Volume", "")),
            "market_cap":   s.get("Market Cap", ""),
            "short_float":  o.get("Short Float", ""),
            "float":        _parse_vol(o.get("Float", "")),
            "rel_volume":   _safe_float(p.get("Rel Volume")),
        })
    return results


def _parse_vol(val) -> int:
    """Parse finviz abbreviated volume/share counts ('726.36K', '29.20M') to int."""
    s = str(val).strip().replace(",", "")
    if not s or s == "-":
        return 0
    mult = {"K": 1_000, "M": 1_000_000, "B": 1_000_000_000}.get(s[-1].upper())
    try:
        return int(float(s[:-1]) * mult) if mult else int(float(s))
    except ValueError:
        return 0


def _safe_float(val) -> float:
    try:
        return float(str(val).strip("%").replace(",", "")) if val else 0.0
    except Exception:
        return 0.0


def _safe_int(val) -> int:
    try:
        return int(str(val).replace(",", "").replace(".", "")) if val else 0
    except Exception:
        return 0


# ---------------------------------------------------------------------------
# Screener commands
# ---------------------------------------------------------------------------

def top_movers(limit: int = 20) -> None:
    """Top small cap % gainers today with meaningful volume."""
    print(f"\n{'='*65}")
    print(f"  TOP SMALL CAP MOVERS — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*65}")

    # Finviz filters: small+micro cap, US, price>3, avg vol>300k, positive change
    filters = [
        "cap_small",   # Small cap and above ($300M+)
        "geo_usa",
        "sh_price_o3",     # Price > $3
        "sh_avgvol_o300",  # Avg volume > 300k
        "ta_change_u",     # Today's change positive
        "exch_nasd,exch_nyse",
    ]

    results = _run_screener(filters, order="-change", limit=limit * 2)

    # Also grab micro caps separately
    micro_filters = [
        "cap_micro",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o300",
        "ta_change_u",
    ]
    results += _run_screener(micro_filters, order="-change", limit=limit)

    # Deduplicate, filter S&P 500, sort by % change
    seen = set()
    clean = []
    for r in results:
        if r["symbol"] not in seen and r["symbol"] not in SP500_EXCLUDE:
            seen.add(r["symbol"])
            clean.append(r)

    clean.sort(key=lambda x: x["change_pct"], reverse=True)
    clean = clean[:limit]

    if not clean:
        print("No results from finviz — check internet connection or finviz availability.")
        return

    print(f"\n{'Symbol':<8} {'Change':>7} {'Price':>7} {'RelVol':>7} {'MCap':<10} {'Sector':<20} {'Company'}")
    print("-" * 80)
    for s in clean:
        rv = f"{s['rel_volume']:.1f}x" if s['rel_volume'] else "  —"
        print(f"{s['symbol']:<8} {s['change_pct']:>+6.1f}% {s['price']:>7.2f} {rv:>7} {s['market_cap']:<10} {s['sector'][:20]:<20} {s['company'][:30]}")


def unusual_volume(limit: int = 20) -> None:
    """Stocks with 3x+ relative volume — accumulation signal."""
    print(f"\n{'='*65}")
    print(f"  UNUSUAL VOLUME — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*65}")

    filters = [
        "cap_small",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o300",
        "ta_relvol_o3",    # Relative volume > 3x
    ]
    results = _run_screener(filters, order="-relativevolume", limit=limit * 2)

    micro_filters = [
        "cap_micro",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o300",
        "ta_relvol_o3",
    ]
    results += _run_screener(micro_filters, order="-relativevolume", limit=limit)

    seen = set()
    clean = []
    for r in results:
        if r["symbol"] not in seen and r["symbol"] not in SP500_EXCLUDE:
            seen.add(r["symbol"])
            clean.append(r)

    clean.sort(key=lambda x: x["rel_volume"], reverse=True)
    clean = clean[:limit]

    if not clean:
        print("No results — check finviz availability.")
        return

    print(f"\n{'Symbol':<8} {'RelVol':>7} {'Change':>7} {'Price':>7} {'MCap':<10} {'Sector':<20} {'Company'}")
    print("-" * 80)
    for s in clean:
        rv = f"{s['rel_volume']:.1f}x" if s['rel_volume'] else "  —"
        print(f"{s['symbol']:<8} {rv:>7} {s['change_pct']:>+6.1f}% {s['price']:>7.2f} {s['market_cap']:<10} {s['sector'][:20]:<20} {s['company'][:30]}")


def short_squeeze(limit: int = 20) -> None:
    """High short float stocks with recent volume surge — squeeze candidates."""
    print(f"\n{'='*65}")
    print(f"  SHORT SQUEEZE CANDIDATES — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*65}")

    filters = [
        "cap_small",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o200",
        "sh_short_o15",    # Short float > 15%
    ]
    results = _run_screener(filters, order="-short", limit=limit * 2)

    micro_filters = [
        "cap_micro",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o200",
        "sh_short_o15",
    ]
    results += _run_screener(micro_filters, order="-short", limit=limit)

    seen = set()
    clean = []
    for r in results:
        if r["symbol"] not in seen and r["symbol"] not in SP500_EXCLUDE:
            seen.add(r["symbol"])
            clean.append(r)

    clean.sort(key=lambda x: _safe_float(x.get("short_float", "0").rstrip("%")), reverse=True)
    clean = clean[:limit]

    if not clean:
        print("No results — check finviz availability.")
        return

    print(f"\n{'Symbol':<8} {'Short%':>7} {'RelVol':>7} {'Change':>7} {'Price':>7} {'MCap':<10} {'Company'}")
    print("-" * 75)
    for s in clean:
        rv = f"{s['rel_volume']:.1f}x" if s['rel_volume'] else "  —"
        sf = s.get("short_float", "—")
        print(f"{s['symbol']:<8} {sf:>7} {rv:>7} {s['change_pct']:>+6.1f}% {s['price']:>7.2f} {s['market_cap']:<10} {s['company'][:30]}")


def breakouts(limit: int = 20) -> None:
    """Stocks breaking out near 52-week highs with volume expansion."""
    print(f"\n{'='*65}")
    print(f"  BREAKOUT CANDIDATES — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*65}")

    filters = [
        "cap_small",
        "geo_usa",
        "sh_price_o3",
        "sh_avgvol_o300",
        "ta_highlow52w_nh",   # Near 52-week high
        "ta_relvol_o1",       # Above avg volume
    ]
    results = _run_screener(filters, order="-change", limit=limit * 2)

    micro_filters = [
        "cap_micro",
        "geo_usa",
        "sh_price_o5",
        "sh_avgvol_o200",
        "ta_highlow52w_nh",
        "ta_relvol_o1",
    ]
    results += _run_screener(micro_filters, order="-change", limit=limit)

    seen = set()
    clean = []
    for r in results:
        if r["symbol"] not in seen and r["symbol"] not in SP500_EXCLUDE:
            seen.add(r["symbol"])
            clean.append(r)

    clean.sort(key=lambda x: x["change_pct"], reverse=True)
    clean = clean[:limit]

    if not clean:
        print("No results — check finviz availability.")
        return

    print(f"\n{'Symbol':<8} {'Change':>7} {'RelVol':>7} {'Price':>7} {'MCap':<10} {'Sector':<20} {'Company'}")
    print("-" * 80)
    for s in clean:
        rv = f"{s['rel_volume']:.1f}x" if s['rel_volume'] else "  —"
        print(f"{s['symbol']:<8} {s['change_pct']:>+6.1f}% {rv:>7} {s['price']:>7.2f} {s['market_cap']:<10} {s['sector'][:20]:<20} {s['company'][:30]}")


def detail(symbol: str) -> None:
    """Full technical + fundamental detail on a specific small cap ticker."""
    sym = symbol.upper()
    print(f"\n{'='*50}")
    print(f"  {sym} — Detail")
    print(f"{'='*50}")

    ticker = yf.Ticker(sym)
    info = ticker.info

    # Basic info
    print(f"Company:       {info.get('longName', 'N/A')}")
    print(f"Sector:        {info.get('sector', 'N/A')} / {info.get('industry', 'N/A')}")
    print(f"Market Cap:    ${info.get('marketCap', 0)/1e6:.0f}M")
    print(f"Float:         {info.get('floatShares', 0)/1e6:.1f}M shares")
    print(f"Short %:       {info.get('shortPercentOfFloat', 0)*100:.1f}%")
    print(f"Avg Volume:    {info.get('averageDailyVolume10Day', 0)/1e3:.0f}k")

    # Price
    hist = ticker.history(period="5d")
    if not hist.empty:
        price = float(hist["Close"].iloc[-1])
        prev = float(hist["Close"].iloc[-2]) if len(hist) > 1 else price
        daily_chg = (price - prev) / prev * 100
        vol = int(hist["Volume"].iloc[-1])
        avg_vol = int(hist["Volume"].mean())
        rel_vol = vol / avg_vol if avg_vol > 0 else 0
        print(f"\nPrice:         ${price:.2f} ({daily_chg:+.1f}% today)")
        print(f"Volume:        {vol/1e3:.0f}k ({rel_vol:.1f}x avg)")

    # 52-week range
    w52h = info.get("fiftyTwoWeekHigh")
    w52l = info.get("fiftyTwoWeekLow")
    if w52h and w52l:
        pct_from_high = (price - w52h) / w52h * 100
        print(f"52-wk range:   ${w52l:.2f} – ${w52h:.2f}  ({pct_from_high:+.1f}% from high)")

    # Technicals (longer history)
    hist_3m = ticker.history(period="3mo")
    if not hist_3m.empty and len(hist_3m) >= 20:
        close = hist_3m["Close"]
        ma20 = float(close.tail(20).mean())
        ma50 = float(close.tail(50).mean()) if len(close) >= 50 else None
        print(f"\nMA20:          ${ma20:.2f}  ({'above' if price > ma20 else 'BELOW'})")
        if ma50:
            print(f"MA50:          ${ma50:.2f}  ({'above' if price > ma50 else 'BELOW'})")
        mom_1m = (price - float(close.iloc[-22])) / float(close.iloc[-22]) * 100 if len(close) >= 22 else 0
        mom_5d = (price - float(close.iloc[-5])) / float(close.iloc[-5]) * 100 if len(close) >= 5 else 0
        print(f"5-day move:    {mom_5d:+.1f}%")
        print(f"1-month move:  {mom_1m:+.1f}%")

    # Fundamentals
    pe = info.get("trailingPE")
    fpe = info.get("forwardPE")
    rev_growth = info.get("revenueGrowth")
    print(f"\nTrailing P/E:  {pe:.1f}" if pe else "\nTrailing P/E:  N/A")
    print(f"Forward P/E:   {fpe:.1f}" if fpe else "Forward P/E:   N/A")
    print(f"Rev growth:    {rev_growth*100:+.1f}%" if rev_growth else "Rev growth:    N/A")
    print(f"Analyst target:${info.get('targetMeanPrice', 'N/A')}")
    print(f"Recommendation:{info.get('recommendationKey', 'N/A')}")
    print(f"\n{'='*50}")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: smallcap_scanner.py <command> [args]")
        print("Commands:")
        print("  top_movers       — Top small cap % gainers today")
        print("  unusual_volume   — 3x+ relative volume surge")
        print("  short_squeeze    — High short float + volume")
        print("  breakouts        — Near 52-week highs with volume")
        print("  detail TICKER    — Full detail on specific stock")
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "top_movers":
        top_movers()
    elif cmd == "unusual_volume":
        unusual_volume()
    elif cmd == "short_squeeze":
        short_squeeze()
    elif cmd == "breakouts":
        breakouts()
    elif cmd == "detail" and len(args) > 1:
        detail(args[1])
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
