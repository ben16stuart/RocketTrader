"""
Market data utility — price history, fundamentals, screening via yfinance.
Usage: python scripts/market_data.py <command> [args]
"""
import os
import sys
from datetime import datetime, timedelta

import yfinance as yf
import pandas as pd


def get_current_price(symbol: str) -> float:
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="2d")
    if data.empty:
        raise ValueError(f"No price data for {symbol}")
    return round(float(data["Close"].iloc[-1]), 2)


def get_price_history(symbol: str, period: str = "3mo") -> pd.DataFrame:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)
    return df


def get_spy_return(since_date: str) -> float:
    """Return SPY % gain from since_date (YYYY-MM-DD) to today's close."""
    spy = yf.Ticker("SPY")
    # end must be TOMORROW — yfinance end is exclusive, so end=today omits today's bar
    end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    data = spy.history(start=since_date, end=end)
    if data.empty or len(data) < 2:
        return 0.0
    price_then = float(data["Close"].iloc[0])
    price_now  = float(data["Close"].iloc[-1])
    return round((price_now - price_then) / price_then * 100, 2)


def get_spy_daily_return() -> float:
    """Return SPY % change for today (today's close vs yesterday's close)."""
    spy = yf.Ticker("SPY")
    end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    data = spy.history(start=(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"), end=end)
    if data.empty or len(data) < 2:
        return 0.0
    price_prev = float(data["Close"].iloc[-2])
    price_now  = float(data["Close"].iloc[-1])
    return round((price_now - price_prev) / price_prev * 100, 2)


def get_fundamentals(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    info = ticker.info
    return {
        "symbol":              symbol.upper(),
        "company":             info.get("longName", "N/A"),
        "sector":              info.get("sector", "N/A"),
        "market_cap":          info.get("marketCap", 0),
        "pe_ratio":            info.get("trailingPE"),
        "fwd_pe":              info.get("forwardPE"),
        "revenue_growth":      info.get("revenueGrowth"),
        "earnings_growth":     info.get("earningsGrowth"),
        "profit_margin":       info.get("profitMargins"),
        "debt_to_equity":      info.get("debtToEquity"),
        "avg_volume":          info.get("averageVolume"),
        "52w_high":            info.get("fiftyTwoWeekHigh"),
        "52w_low":             info.get("fiftyTwoWeekLow"),
        "analyst_target":      info.get("targetMeanPrice"),
        "recommendation":      info.get("recommendationKey"),
        "earnings_date":       str(info.get("earningsTimestamp", "N/A")),
    }


def screen_momentum(top_n: int = 10) -> list[dict]:
    """Screen a predefined list of large-cap liquid stocks by 1-month momentum."""
    universe = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "JPM",
        "V", "MA", "UNH", "HD", "COST", "AVGO", "AMD", "CRM", "NOW",
        "PANW", "PLTR", "UBER", "ABNB", "LLY", "ABBV", "MRK", "JNJ",
        "XOM", "CVX", "NEE", "DUK", "AMT", "PLD", "SPG", "BAC", "GS",
        "MS", "BLK", "SCHW", "WMT", "TGT", "PG", "KO", "PEP", "MCD",
    ]
    results = []
    for sym in universe:
        try:
            df = get_price_history(sym, period="2mo")
            if df.empty or len(df) < 22:
                continue
            price_now   = float(df["Close"].iloc[-1])
            price_1m    = float(df["Close"].iloc[-22])
            mom_1m      = (price_now - price_1m) / price_1m * 100
            avg_vol     = float(df["Volume"].tail(20).mean())
            if avg_vol < 1_000_000:
                continue
            results.append({
                "symbol":    sym,
                "price":     round(price_now, 2),
                "mom_1m":    round(mom_1m, 1),
                "avg_vol_m": round(avg_vol / 1_000_000, 1),
            })
        except Exception:
            continue

    results.sort(key=lambda x: x["mom_1m"], reverse=True)
    return results[:top_n]


def print_chart_summary(symbol: str) -> None:
    df = get_price_history(symbol, period="6mo")
    if df.empty:
        print(f"No data for {symbol}")
        return

    close = df["Close"]
    price_now  = float(close.iloc[-1])
    ma50       = float(close.tail(50).mean())
    ma200      = float(close.tail(200).mean()) if len(close) >= 200 else None
    week_high  = float(close.tail(5).max())
    week_low   = float(close.tail(5).min())
    month_chg  = (price_now - float(close.iloc[-22])) / float(close.iloc[-22]) * 100 if len(close) >= 22 else None
    ytd_chg    = (price_now - float(close.iloc[0])) / float(close.iloc[0]) * 100

    print(f"\n{'='*40}")
    print(f"  {symbol.upper()} — Technical Summary")
    print(f"{'='*40}")
    print(f"  Price:      ${price_now:.2f}")
    print(f"  MA50:       ${ma50:.2f}  ({'above' if price_now > ma50 else 'below'})")
    if ma200:
        print(f"  MA200:      ${ma200:.2f}  ({'above' if price_now > ma200 else 'below'})")
    print(f"  Week range: ${week_low:.2f} – ${week_high:.2f}")
    if month_chg is not None:
        print(f"  1-mo chg:   {month_chg:+.1f}%")
    print(f"  YTD chg:    {ytd_chg:+.1f}%")
    print(f"{'='*40}\n")


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: market_data.py <command> [args]")
        print("Commands: price, fundamentals, chart, screen, spy")
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "price":
        sym = args[1].upper()
        price = get_current_price(sym)
        print(f"{sym}: ${price:.2f}")

    elif cmd == "fundamentals":
        sym = args[1].upper()
        info = get_fundamentals(sym)
        for k, v in info.items():
            if v is not None:
                print(f"  {k}: {v}")

    elif cmd == "chart":
        sym = args[1].upper()
        print_chart_summary(sym)

    elif cmd == "screen":
        top_n = int(args[1]) if len(args) > 1 else 10
        print(f"\nTop {top_n} momentum stocks (1-month, vol >1M):\n")
        print(f"{'Symbol':<8} {'Price':>8} {'1M Chg':>8} {'AvgVol(M)':>10}")
        print("-" * 38)
        for s in screen_momentum(top_n):
            print(f"{s['symbol']:<8} {s['price']:>8.2f} {s['mom_1m']:>+7.1f}% {s['avg_vol_m']:>9.1f}M")

    elif cmd == "spy":
        since = args[1] if len(args) > 1 else "2026-04-20"
        ret = get_spy_return(since)
        print(f"SPY return since {since}: {ret:+.2f}%")

    elif cmd == "spy-today":
        ret = get_spy_daily_return()
        print(f"SPY today: {ret:+.2f}%")

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
