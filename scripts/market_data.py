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


# Rocket is benchmarked against IWM (Russell 2000), not SPY -- see CLAUDE.md
# "Portfolio Construction". Bull is the SPY-benchmarked agent; these two repos
# diverged deliberately on 2026-09-17 so each agent's core IS its own benchmark,
# which is what makes the core contribute exactly zero excess return by
# construction (the same property Bull already had against SPY).
BENCHMARK_SYMBOL = "IWM"


def get_benchmark_return(since_date: str) -> float:
    """Return IWM % gain from since_date (YYYY-MM-DD) to today's close."""
    spy = yf.Ticker(BENCHMARK_SYMBOL)
    # end must be TOMORROW — yfinance end is exclusive, so end=today omits today's bar
    end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    data = spy.history(start=since_date, end=end)
    # Premarket, today's bar exists with volume but a NaN close — taking iloc[-1]
    # blindly propagates NaN into every downstream return figure. Drop unpriced bars.
    data = data[data["Close"].notna()]
    if data.empty or len(data) < 2:
        return 0.0
    price_then = float(data["Close"].iloc[0])
    price_now  = float(data["Close"].iloc[-1])
    return round((price_now - price_then) / price_then * 100, 2)


def get_benchmark_daily_return() -> float:
    """Return IWM % change for today (today's close vs yesterday's close)."""
    spy = yf.Ticker(BENCHMARK_SYMBOL)
    end = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    data = spy.history(start=(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"), end=end)
    # Same NaN-close guard as get_spy_return. Premarket this correctly yields the
    # last *completed* session's return rather than NaN.
    data = data[data["Close"].notna()]
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


# ---------------------------------------------------------------------------
# Universe thresholds — the ONE place these live. Mirrors CLAUDE.md's
# "Investment Universe" section. Rocket's copy of this file sets its own values.
# ---------------------------------------------------------------------------
UNIVERSE = {
    "name":           "Rocket",
    "min_market_cap": 50_000_000,
    "max_market_cap": 2_000_000_000,   # small caps only — NOT S&P 500 names
    "min_avg_volume": 300_000,
    "min_price":      3.00,            # avoid sub-$3 micro-cap traps
}

MACRO_TICKERS = [
    ("^VIX",      "VIX"),
    ("^TNX",      "10Y yield"),
    ("ES=F",      "S&P fut"),
    ("NQ=F",      "Nasdaq fut"),
    ("RTY=F",     "Russell fut"),
    ("BZ=F",      "Brent"),
    ("CL=F",      "WTI"),
    ("DX-Y.NYB",  "Dollar idx"),
    ("GC=F",      "Gold"),
    ("SPY",       "SPY"),
    ("IWM",       "IWM"),
]


def _resolve_futures_contract(sym, cont):
    """Resolve a continuous `=F` symbol to the ACTUAL contract it is quoting.

    THIRD defect in macro_snapshot, found 2026-09-15, and the most damaging so far.
    A `=F` symbol is CONTINUOUS FRONT-MONTH: on roll day it silently starts quoting
    a different underlying contract, so `last/prev-1` compares two different
    instruments and reports the *calendar spread* as if it were a price move. On
    2026-09-15 FOUR of seven futures rows rolled at once (ES/NQ/RTY Sep->Dec on the
    quarterly cycle, BZ Nov->Dec) and THREE printed the WRONG SIGN: S&P fut read
    +0.51% on a true -0.35%, Nasdaq +0.61% on a true -0.37%, Russell +0.33% on a
    true -0.47%, Brent -2.82% on a true +2.07%. Every one looked perfectly
    plausible. The day before an FOMC, the table said "risk-on" when futures were
    in fact broadly down.

    Prior art: the same failure was found one session earlier (2026-09-14) on
    `ZQ=F`, where it corrupted the magnitude of a live thesis-break test. That was
    patched by WRITING DOWN an explicit contract pair. This is the same bug class
    in a script, so it gets a code fix -- and a fix that needs no contract calendar,
    because a hand-maintained calendar is just a slower version of the same defect.

    Method: yfinance's `.info` names the candidate contracts (`underlyingSymbol` /
    `underlyingExchangeSymbol` -- on a roll these two DISAGREE, one naming the old
    contract and one the new). Pick whichever candidate's latest close sits closest
    to the continuous symbol's latest close, then read the change off THAT
    contract's own series. Matching is nearest-neighbour, not equality: a still
    forming live bar can differ slightly between the continuous feed and the
    explicit contract (RTY=F printed 2902.70 against RTYZ26's 2902.50).

    Returns (contract_symbol, its_close_series) or (None, None) to fall back.
    """
    try:
        info = yf.Ticker(sym).info
    except Exception:
        return None, None
    cands = {info.get(k) for k in ("underlyingSymbol", "underlyingExchangeSymbol")}
    cands = {c for c in cands if c and isinstance(c, str)}
    if not cands:
        return None, None
    best, best_err, best_s = None, None, None
    for c in sorted(cands):
        try:
            s = yf.Ticker(c).history(period="1mo")["Close"].dropna()
            if len(s) < 2:
                continue
            err = abs(float(s.iloc[-1]) - float(cont.iloc[-1])) / abs(float(cont.iloc[-1]))
        except Exception:
            continue
        if best_err is None or err < best_err:
            best, best_err, best_s = c, err, s
    # A resolved contract that does not actually track the quoted price is worse
    # than no resolution at all -- fall back rather than report a mismatched series.
    if best is None or best_err > 0.02:
        return None, None
    return best, best_s


def macro_snapshot() -> str:
    """Every macro number the premarket routines need, in one batched call.

    Replaces ~28 natural-language web searches per premarket session ("VIX index
    level today", "Brent crude price today", "S&P 500 futures premarket"...). Each
    of those was a separate conversation turn that re-sent the whole context, and
    search often returned a number parsed out of a news snippet rather than the
    actual quote -- so the agent would re-ask the same question three or four
    different ways. This is exact, one call, ~250 tokens.
    """
    syms = [s for s, _ in MACRO_TICKERS]
    try:
        data = yf.download(syms, period="5d", interval="1d",
                           progress=False, auto_adjust=True)["Close"]
    except Exception as exc:
        return f"MACRO SNAPSHOT unavailable ({exc}) — fall back to web search."

    # `s.iloc[-1]` is the LATEST BAR, which in a premarket session is TODAY's
    # partially-formed bar -- not yesterday's close. This header used to read
    # "last close vs prior close", and every premarket session recorded the
    # number into market_context.md as the prior day's close. Found 2026-08-13:
    # the whole 8/5-8/11 gold series in memory was too high by $60-$135 with
    # every error in the same direction, and 8/6 was recorded UP on a day gold
    # actually closed DOWN -- a sign error in a macro series, from a label.
    # Both bars are now printed with their dates so the two cannot be confused.
    # SECOND defect in the same function, found 2026-09-01. Printing each row's
    # own dates (the 8/13 fix above) is necessary and NOT sufficient: yfinance
    # drops whole sessions for individual series, and when it does, that row's
    # `change` silently spans TWO sessions while its neighbours span one. On
    # 2026-09-01 ^TNX and IWM had no 8/28 bar at all, so 10Y read "+1.84%" and
    # IWM "-1.96%" against 8/27 while SPY in the same table read against 8/28 --
    # both ~3x the true one-session move. The 8/31 session had already recorded
    # two such rows into market_context.md's "8/28 settled" column, where they
    # were not 8/28 closes at all. Rule #30's "one table, two dates, no labels"
    # recurring in the CHANGE column instead of the price column.
    today = datetime.now().date()
    rows, prev_dates, rolled = [], [], []
    for sym, label in MACRO_TICKERS:
        try:
            s = data[sym].dropna()
            last, prev = float(s.iloc[-1]), float(s.iloc[-2])
            d_last, d_prev = s.index[-1].date(), s.index[-2].date()
            contract = None
            if sym.endswith("=F"):
                contract, cs = _resolve_futures_contract(sym, s)
                if contract is not None:
                    cd = {d.date(): float(v) for d, v in cs.items()}
                    # A roll shows up as the continuous feed's PRIOR close
                    # disagreeing with the resolved contract's own close on that
                    # same date -- i.e. yesterday's number came from a different
                    # instrument than today's. Re-read both legs off the contract.
                    if d_prev in cd and abs(cd[d_prev] - prev) / abs(prev) > 5e-4:
                        rolled.append((label, contract,
                                       (last / prev - 1) * 100,
                                       (last / cd[d_prev] - 1) * 100))
                        prev = cd[d_prev]
                    else:
                        contract = None   # tracking cleanly; nothing to report
            rows.append((label, last, prev, d_last, d_prev, contract))
            prev_dates.append(d_prev)
        except Exception:
            rows.append((label, None, None, None, None, None))

    # Comparing prior-close DATES across rows is wrong and the first version of
    # this check did it: futures carry a live bar dated today (prior = 8/31)
    # while equities pre-open carry 8/31 itself (prior = 8/28), so SPY flagged
    # as stale when it was perfectly current. The rows do not share a latest
    # date, so they cannot share a prior date either.
    # The actual question is whether a row SKIPPED a session, so it needs a
    # trading calendar: SPY's own index, which defines US equity sessions.
    try:
        cal = [d.date() for d in data["SPY"].dropna().index]
    except Exception:
        cal = []
    stale = []
    out = ["MACRO SNAPSHOT (yfinance)",
           "  latest bar (PARTIAL if dated today) | prior daily CLOSE | change"]
    for label, last, prev, d_last, d_prev, contract in rows:
        if last is None:
            out.append(f"  {label:<12}{'n/a':>11}")
            continue
        tag = "LIVE" if d_last >= today else "close"
        flag = ""
        if contract:
            flag = f"  🔄 ROLLED — both legs re-read off {contract}"
        skipped = [d for d in cal if d_prev < d < d_last]
        if skipped:
            flag += f"  🔴 MISSING BAR(S) {','.join(str(d) for d in skipped)} — change spans >1 session"
            stale.append((label, d_prev, skipped))
        out.append(f"  {label:<12}{last:>11,.2f} {tag:<5}{d_last}"
                   f" | {prev:>10,.2f} close {d_prev} | {(last/prev-1)*100:+6.2f}%{flag}")
    out.append("  ⚠️  A bar tagged LIVE is still forming. Record the PRIOR CLOSE column")
    out.append("      into market_context.md under THE DATE PRINTED ON THAT ROW —")
    out.append("      the rows do not all share a prior date. Never the LIVE column.")
    if stale:
        out.append(f"  🔴 {len(stale)} row(s) SKIPPED a session the SPY calendar shows "
                   f"as traded, so their")
        out.append("      % change is NOT a one-session move. Do not record it as one: "
                   + ", ".join(f"{l} (jumps {d} → skips {','.join(str(x) for x in sk)})"
                               for l, d, sk in stale))
    if rolled:
        out.append(f"  🔄 {len(rolled)} futures row(s) ROLLED to a new contract. The continuous "
                   f"`=F` feed changed")
        out.append("      instrument underneath the series, so the NAIVE change was a calendar "
                   "spread, not a")
        out.append("      price move. Both legs above are re-read off the named contract. "
                   "Naive vs true:")
        for label, contract, naive, true in rolled:
            sign = " 🔴 SIGN FLIP" if naive * true < 0 else ""
            out.append(f"      {label:<12} {contract:<12} naive {naive:+6.2f}%  →  "
                       f"true {true:+6.2f}%{sign}")
    out.append("  (VIX >22 = pause new entries, >25 = reduce size, >30 = no new longs)")
    return "\n".join(out)



def check_eligibility(symbol: str) -> str:
    """Hard universe check for one ticker: price, volume, cap, float, earnings.

    Replaces searches like "RCKY average daily volume shares outstanding dilution
    shelf offering", which routinely needed two or three attempts to land a number.
    Returns an explicit PASS/FAIL per rule so the agent doesn't have to infer it.
    """
    sym = symbol.upper()
    try:
        tk = yf.Ticker(sym)
        info = tk.info or {}
    except Exception as exc:
        return f"{sym}: lookup failed ({exc})"

    price   = info.get("currentPrice") or info.get("regularMarketPrice")
    cap     = info.get("marketCap")
    avgvol  = info.get("averageVolume")
    shares  = info.get("sharesOutstanding")
    flt     = info.get("floatShares")
    exch    = info.get("exchange", "?")
    name    = info.get("longName", sym)

    lines = [f"{sym} — {name}", f"  exchange {exch}"]

    def verdict(ok):
        return "PASS" if ok else "**FAIL**"

    # A missing field must never read as a pass -- yfinance has real gaps (CRM
    # returned no marketCap on 2026-07-29). Say "unknown" loudly instead.
    if price is None:
        lines.append("  price          unknown — VERIFY MANUALLY")
    if cap is None:
        lines.append("  market cap     unknown — VERIFY MANUALLY (universe gate)")
    if avgvol is None:
        lines.append("  avg volume     unknown — VERIFY MANUALLY (universe gate)")

    if price is not None:
        lines.append(f"  price          ${price:,.2f}" +
                     (f"   {verdict(price >= UNIVERSE['min_price'])} (min ${UNIVERSE['min_price']})"
                      if UNIVERSE["min_price"] else ""))
    if cap is not None:
        lo, hi = UNIVERSE["min_market_cap"], UNIVERSE["max_market_cap"]
        ok = (lo is None or cap >= lo) and (hi is None or cap <= hi)
        rng = f"min ${lo/1e6:,.0f}M" + (f", max ${hi/1e9:,.1f}B" if hi else "")
        lines.append(f"  market cap     ${cap/1e6:,.0f}M   {verdict(ok)} ({rng})")
    if avgvol is not None:
        ok = avgvol >= UNIVERSE["min_avg_volume"]
        lines.append(f"  avg volume     {avgvol:,.0f}   {verdict(ok)} "
                     f"(min {UNIVERSE['min_avg_volume']:,})")
    if shares:
        lines.append(f"  shares out     {shares/1e6:,.1f}M")
    if flt:
        lines.append(f"  float          {flt/1e6:,.1f}M ({flt/shares*100:.0f}% of shares)"
                     if shares else f"  float          {flt/1e6:,.1f}M")

    # Earnings proximity — both agents gate on this, and it was being searched for.
    try:
        cal = tk.calendar
        ed = None
        if isinstance(cal, dict):
            v = cal.get("Earnings Date")
            ed = (v[0] if isinstance(v, list) and v else v)
        if ed:
            days = (pd.Timestamp(ed).tz_localize(None) - pd.Timestamp.now().normalize()).days
            flag = "  ⚠️ EARNINGS WEEK" if 0 <= days <= 7 else ""
            lines.append(f"  next earnings  {ed}  ({days:+d} days){flag}")
        else:
            lines.append("  next earnings  unknown — verify before entry")
    except Exception:
        lines.append("  next earnings  unknown — verify before entry")

    if any("FAIL" in l for l in lines):
        lines.append("  => OUT OF UNIVERSE — do not trade.")
    elif any("VERIFY MANUALLY" in l for l in lines):
        lines.append("  => INCOMPLETE — one or more universe gates could not be checked.")
    else:
        lines.append("  => in universe on all checked gates.")

    return "\n".join(lines)


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
        print("Commands: macro, eligibility, price, fundamentals, chart, screen, benchmark")
        sys.exit(0)

    cmd = args[0].lower()

    if cmd == "macro":
        print(macro_snapshot())

    elif cmd == "eligibility":
        if len(args) < 2:
            print("Usage: market_data.py eligibility TICKER [TICKER ...]")
            sys.exit(1)
        for s in args[1:]:
            print(check_eligibility(s))
            print()

    elif cmd == "price":
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

    elif cmd == "benchmark":
        since = args[1] if len(args) > 1 else "2026-04-20"
        ret = get_benchmark_return(since)
        print(f"{BENCHMARK_SYMBOL} return since {since}: {ret:+.2f}%")

    elif cmd == "benchmark-today":
        ret = get_benchmark_daily_return()
        print(f"{BENCHMARK_SYMBOL} today: {ret:+.2f}%")

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
