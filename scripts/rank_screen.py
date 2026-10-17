"""Rocket's systematic ranker -- the backbone of satellite selection (since 2026-10-17).

WHY THIS EXISTS
Rocket picked stocks through a veto checklist: a named, dated catalyst, US
incorporation, a $50M-$2B cap, no same-day entries, dilution, float and ADV checks.
Every rule came from a real loss, and nothing measured the names it rejected. From
9/17 to 10/16 Rocket sat below its 50% stock-pick floor every single session (22 in a
row), with 0% in stocks after 10/5. Lifting the IWM cap only moved the idle money into
IWM. Ben: "Rocket needs to be a rocket." A ranking always produces candidates; a veto
checklist can produce none.

WHAT IT DOES
Ranks ~1,800 US-listed small/mid caps (the Russell 2000's range: $150M-$10B, avg volume
>= 300k shares, price >= $3, from Yahoo's screener) by 6-1 month return / 1-year vol.

BACKTEST (scratch, 2020-01 -> 2026-10, this universe, top 8, weekly check, exit rank >
25, 20 bp per side; survivorship-biased because the universe is today's survivors, so
relative comparisons only):
  6-1 risk-adjusted momentum beat IWM in 5 of 7 years with no stop (+11.6%/yr), and was
  the most consistent of 6 signals tried. Bull's 12-1/6-1 blend was stronger on paper but
  depended on 2020. A "catalyst shock" signal (up-moves on 3x volume) and a 52-week-high
  blend both lost to the equal-weight universe. Stops: no width was consistently better.
  25% gave the best CAGR, while 7% traded ~300 times a year, which a 5-per-week cap cannot
  follow. Expect 50%-type volatility and -60% drawdowns in the stock sleeve: this is a
  rocket.

THE AI'S JOB is the layer on top: catalysts, dilution, binary events, pumps. Every
override is logged with scripts/candidate_ledger.py and scored against IWM.

Usage:
  python scripts/rank_screen.py              # top 20; saves memory/ledger/ranks/<asof>.csv
  python scripts/rank_screen.py --top 30
  python scripts/rank_screen.py --no-save
"""
import os
import sys
import time
import argparse
import warnings
from datetime import date, datetime

import numpy as np
import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, REPO)

LEDGER = os.path.join(REPO, "memory", "ledger")
RANK_DIR = os.path.join(LEDGER, "ranks")
UNIVERSE_CACHE = os.path.join(LEDGER, "universe.csv")
N_TARGET = 8
EXIT_RANK = 25
MIN_ADV = 300_000
MIN_PRICE = 3.0
CAP_LO, CAP_HI = 150e6, 10e9


def fetch_universe():
    """US-listed small/mid caps from Yahoo's screener; falls back to the cached copy."""
    from yfinance import EquityQuery as Q
    q = Q("and", [Q("eq", ["region", "us"]),
                  Q("is-in", ["exchange", "NMS", "NYQ", "NGM", "NCM", "ASE"]),
                  Q("btwn", ["intradaymarketcap", CAP_LO, CAP_HI]),
                  Q("gt", ["avgdailyvol3m", MIN_ADV]),
                  Q("gt", ["intradayprice", MIN_PRICE])])
    rows, off = [], 0
    try:
        while True:
            r = yf.screen(q, size=250, offset=off, sortField="intradaymarketcap", sortAsc=False)
            qs = r.get("quotes", [])
            rows += [dict(sym=x["symbol"], cap=x.get("marketCap"), name=x.get("shortName"),
                          qt=x.get("quoteType"),
                          earn_ts=x.get("earningsTimestampStart") or x.get("earningsTimestamp"))
                     for x in qs]
            if len(qs) < 250:
                break
            off += 250
            time.sleep(0.3)
        df = pd.DataFrame(rows)
        df = df[df.qt == "EQUITY"]
        if len(df) < 1000:
            raise RuntimeError(f"screener returned only {len(df)} names")
        os.makedirs(LEDGER, exist_ok=True)
        df.to_csv(UNIVERSE_CACHE, index=False)
        return df, "fresh"
    except Exception as exc:
        if os.path.exists(UNIVERSE_CACHE):
            age = (time.time() - os.path.getmtime(UNIVERSE_CACHE)) / 86400
            return pd.read_csv(UNIVERSE_CACHE), f"CACHED ({age:.0f}d old; screener failed: {str(exc)[:60]})"
        raise


def rocket_satellites():
    try:
        from scripts.alpaca_client import get_positions
        from scripts.position_reconciler import reconcile
        return set(reconcile(get_positions(), REPO, "Rocket", "Bull").get("matched", []))
    except Exception:
        return set()


def next_earnings(t):
    try:
        cal = t.calendar
        ed = cal.get("Earnings Date") if isinstance(cal, dict) else None
        if ed:
            d = ed[0] if isinstance(ed, (list, tuple)) else ed
            return d if isinstance(d, date) else pd.Timestamp(d).date()
    except Exception:
        pass
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--no-save", action="store_true")
    a = ap.parse_args()

    held = rocket_satellites()
    udf, src = fetch_universe()
    # Market cap and next earnings come from the screener itself (one bulk call), so the
    # hard gates do not depend on per-ticker lookups that Yahoo rate-limits.
    meta = udf.set_index("sym")
    U = sorted(set(meta.index) | held)

    closes, vols = [], []
    for i in range(0, len(U), 250):
        d = yf.download(U[i:i + 250], period="2y", auto_adjust=True, progress=False, threads=True)
        closes.append(d["Close"])
        vols.append(d["Volume"])
    C = pd.concat(closes, axis=1)
    V = pd.concat(vols, axis=1)
    C = C.loc[:, ~C.columns.duplicated()]
    V = V.loc[:, ~V.columns.duplicated()]

    if C.iloc[-1].isna().mean() > 0.2:          # vendor gap on the newest bar (Standing Rule: date every bar)
        print(f"🔴 Dropped a mostly-empty last bar dated {C.index[-1].date()} (feed gap).")
        C, V = C.iloc[:-1], V.iloc[:-1]
    asof = C.index[-1].date()
    C = C.where(C > 0).ffill(limit=2)            # zero prints are data errors in small caps
    R = C.pct_change(fill_method=None)
    R = R.mask(R.abs() > 0.8)                    # >80% one-day moves: almost always bad ticks

    enough = C.notna().sum() >= 253
    px = C.iloc[-1]
    m61 = C.iloc[-22] / C.iloc[-127] - 1
    m121 = C.iloc[-22] / C.iloc[-253] - 1
    vol = R.iloc[-252:].std() * np.sqrt(252)
    ma200 = C.iloc[-200:].mean()
    adv = V.iloc[-20:].mean()
    df = pd.DataFrame(dict(px=px, m61=m61, m121=m121, vol=vol, ma200=ma200, adv=adv))
    df["ext200"] = df.px / df.ma200 - 1
    why = pd.Series("", index=df.index)
    why[~enough] = "short history"
    why[(why == "") & df.m61.isna()] = "no data"
    why[(why == "") & (df.px <= df.ma200)] = "below 200d"
    why[(why == "") & (df.adv < MIN_ADV)] = "volume < 300k"
    why[(why == "") & (df.px < MIN_PRICE)] = "price < $3"
    elig = df[why == ""].copy()
    elig["score"] = (elig.m61 / elig.vol).rank(pct=True)
    elig = elig.sort_values("score", ascending=False)
    elig["rank"] = np.arange(1, len(elig) + 1)

    today = date.today()
    show = list(elig.index[: a.top]) + [s for s in held if s in elig.index and s not in elig.index[: a.top]]
    rows = []
    for s in show:
        t = yf.Ticker(s)
        i = {}
        for attempt in range(3):          # Yahoo rate-limits right after the bulk download
            try:
                i = t.info or {}
            except Exception:
                i = {}
            if i.get("marketCap") or i.get("sector"):
                break
            time.sleep(2 + 2 * attempt)
        cap = i.get("marketCap") or (meta.at[s, "cap"] if s in meta.index and pd.notna(meta.at[s, "cap"]) else 0)
        ctry = i.get("country")
        gate = "OK"
        if ctry and ctry != "United States":
            gate = f"FAIL non-US HQ ({ctry})"
        elif cap and not (CAP_LO <= cap <= CAP_HI):
            gate = f"FAIL cap ${cap / 1e9:.1f}B"
        ed = None
        if s in meta.index and "earn_ts" in meta and pd.notna(meta.at[s, "earn_ts"]):
            ed = datetime.fromtimestamp(int(meta.at[s, "earn_ts"])).date()
            if ed < today:
                ed = None                    # that was the LAST report; look for the next one
        ed = ed or next_earnings(t)
        td = int(np.busday_count(today, ed)) if ed and ed >= today else None
        if gate == "OK" and td is not None and td <= 5:
            gate = f"EARNINGS in {td}d"
        # Missing data is not a pass (data-integrity rule): say what to verify by hand.
        if gate == "OK" and not i.get("country"):
            gate = "VERIFY HQ country (no company data)"
        elif gate == "OK" and ed is None:
            gate = "VERIFY earnings date"
        r = elig.loc[s]
        rows.append(dict(
            rk=int(r["rank"]), sym=s, sector=(i.get("sector") or "?")[:13],
            capM=cap / 1e6 if cap else np.nan, m6=100 * r.m61, vol=100 * r.vol, ext200=100 * r.ext200,
            revg=(i.get("revenueGrowth") or np.nan) * 100,
            short=(i.get("shortPercentOfFloat") or np.nan) * 100,
            earn=str(ed) if ed else "?", gate=gate, held="HELD" if s in held else ""))
    out = pd.DataFrame(rows)

    pd.set_option("display.width", 250)
    print(f"DATA AS OF: {asof}   universe {len(U)} ({src}) -> eligible {len(elig)} "
          f"(below 200d {int((why == 'below 200d').sum())}, low volume {int((why == 'volume < 300k').sum())}, "
          f"short history {int((why == 'short history').sum())})")
    print("score = pct-rank of 6-1 month return / 1y vol.  Everything right of `ext200` is INFO for judgment, not score.\n")
    if len(out):
        print(out.to_string(index=False, float_format=lambda x: f"{x:.1f}" if abs(x) < 100 else f"{x:.0f}"))

    if held:
        print(f"\nHELD SATELLITES — rank check (replace at the weekly review if rank > {EXIT_RANK}):")
        for s in sorted(held):
            if s in elig.index:
                rk = int(elig.loc[s, "rank"])
                print(f"  {s:6s} rank {rk}" + ("  ⚠️ below exit rank" if rk > EXIT_RANK else ""))
            else:
                print(f"  {s:6s} NOT ELIGIBLE ({why.get(s) or 'not in universe'})  ⚠️ replacement candidate")

    if not a.no_save:
        os.makedirs(RANK_DIR, exist_ok=True)
        path = os.path.join(RANK_DIR, f"{asof}.csv")
        save = elig[["rank", "score", "px", "m61", "m121", "vol", "ext200"]].copy()
        save.insert(0, "asof", asof)
        save.index.name = "sym"
        save.round(5).to_csv(path)
        print(f"\nSaved full ranking ({len(save)} names) -> {os.path.relpath(path, REPO)}")


if __name__ == "__main__":
    main()
