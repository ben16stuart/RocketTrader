#!/usr/bin/env python3
"""This agent's OWN performance vs its benchmark, rebuilt from broker fills.

Why this exists (2026-10-13): Bull and Rocket share one Alpaca account, and each
"slice" is a fixed % of the WHOLE account. So the old "return since rebase" figure
(slice value vs the 7/20 slice) was just the shared account's return, identical for
both agents. Rocket's "+6.65% vs IWM" was really (whole account +1.6%) - (IWM -5.1%),
which says nothing about Rocket's picks.

Method (time-weighted, the standard for a sleeve inside a shared account):
  day P&L   = sum over this agent's symbols of (end value - start value - net cash spent on fills)
  day return = day P&L / slice at the prior close   (slice = AGENT_PCT x account equity)
  period return = product of (1 + day return) - 1
Holdings are rebuilt backwards from today's positions using every fill since the
rebase. Symbols are attributed by the BUY/SELL headers in each agent's trade_log.md;
SPY is Bull's core and IWM is Rocket's. Price returns only, for the agent and the
benchmark alike: the paper account does not book dividends.

Data check: both agents' P&L summed is compared with the account's actual equity
change. `coverage` reports the share explained; anything far from 100% means a
fill could not be attributed (listed in `unattributed`).

Usage:  python scripts/agent_performance.py          # summary
        python scripts/agent_performance.py --days   # plus the last 10 daily rows
"""
import os
import re
import sys
import argparse
import warnings
from datetime import date, datetime, timedelta, timezone

import pandas as pd

warnings.filterwarnings("ignore")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

IS_BULL = os.path.basename(REPO) == "OpusTrader"
ME, SIB = ("Bull", "Rocket") if IS_BULL else ("Rocket", "Bull")
CORE = {"Bull": "SPY", "Rocket": "IWM"}
PCT = {"Bull": 0.70, "Rocket": 0.30}
BENCH = CORE[ME]
REBASE = date(2026, 7, 20)        # shared-account rebase: returns are measured from this close
RESET = date(2026, 10, 6)         # new rules for both agents (Bull rank->judge; Rocket uncapped IWM)
SIB_DIR = os.path.join(os.path.dirname(REPO), "RocketTrader" if IS_BULL else "OpusTrader")


def _api():
    import requests
    h = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
         "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
    base = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets").rstrip("/")
    if base.endswith("/v2"):
        base = base[:-3]
    return lambda path, **p: requests.get(f"{base}/v2{path}", params=p, headers=h, timeout=30).json()


def header_symbols(repo_dir):
    """Tickers named in this agent's trade_log BUY/SELL headers."""
    path = os.path.join(repo_dir, "memory", "trade_log.md")
    if not os.path.exists(path):
        return set()
    syms = set()
    for line in open(path):
        if line.startswith("## ") and re.search(r"\b(BUY|SELL)\b", line):
            syms |= set(re.findall(r"\b[A-Z]{1,5}\b", line))
    return syms


def fetch_fills(get):
    out, token = [], None
    while True:
        p = dict(activity_types="FILL", after=(REBASE - timedelta(days=1)).isoformat(),
                 direction="asc", page_size=100)
        if token:
            p["page_token"] = token
        page = get("/account/activities", **p)
        if not isinstance(page, list) or not page:
            break
        out += page
        token = page[-1]["id"]
        if len(page) < 100:
            break
    rows = []
    for f in out:
        t = pd.Timestamp(f["transaction_time"]).tz_convert("America/New_York")
        q = float(f["qty"]) * (1 if f["side"] == "buy" else -1)
        rows.append(dict(day=t.date(), sym=f["symbol"], qty=q, px=float(f["price"]),
                         order_id=f.get("order_id"), side=f["side"], time=t))
    return pd.DataFrame(rows)


def compute():
    get = _api()
    fills = fetch_fills(get)
    positions = {p["symbol"]: p for p in get("/positions")}
    acct = get("/account")

    # --- attribution
    owner = {CORE["Bull"]: "Bull", CORE["Rocket"]: "Rocket"}
    mine = header_symbols(REPO)
    sib = header_symbols(SIB_DIR)
    bull_h, rocket_h = (mine, sib) if IS_BULL else (sib, mine)
    unattributed = []
    for s in set(fills.sym) | set(positions):
        if s in owner:
            continue
        b, r = s in bull_h, s in rocket_h
        if b and not r:
            owner[s] = "Bull"
        elif r and not b:
            owner[s] = "Rocket"
        else:
            unattributed.append(s)

    # --- trading days and equity at each close (broker's own record)
    ph = get("/account/portfolio/history", period="6M", timeframe="1D")
    # Alpaca stamps each daily bar at 8 PM New York time (00:00 UTC of the NEXT day), so the
    # trading date must be read in New York time; reading it in UTC shifts every day by one.
    from zoneinfo import ZoneInfo
    ny = ZoneInfo("America/New_York")
    eq = pd.Series(ph["equity"], index=[datetime.fromtimestamp(t, ny).date() for t in ph["timestamp"]])
    eq = eq[eq.index >= REBASE].astype(float)
    today = datetime.now(timezone.utc).astimezone().date()
    live = eq.index[-1] < today and float(acct["equity"]) > 0 and today.weekday() < 5
    if live:
        eq.loc[today] = float(acct["equity"])     # today, intraday (or after-close) equity
    days = list(eq.index)

    # --- prices: daily closes (price-only), today's live price from the broker
    import yfinance as yf
    syms = sorted(set(owner) | {"SPY", "IWM"})
    px = yf.download(syms, start=(REBASE - timedelta(days=7)).isoformat(),
                     end=(today + timedelta(days=1)).isoformat(),
                     auto_adjust=False, progress=False, threads=True)["Close"]
    px.index = [d.date() for d in px.index]
    px = px.reindex(sorted(set(px.index) | set(days))).ffill()
    if live:
        for s, p in positions.items():
            if s in px:
                px.loc[today, s] = float(p["current_price"])
        for b in ("SPY", "IWM"):
            if b in positions:
                continue
            try:
                import requests
                h = {"APCA-API-KEY-ID": os.environ["ALPACA_API_KEY"],
                     "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
                t = requests.get(f"https://data.alpaca.markets/v2/stocks/{b}/trades/latest",
                                 params={"feed": "iex"}, headers=h, timeout=15).json()
                px.loc[today, b] = float(t["trade"]["p"])
            except Exception:
                pass

    # --- holdings at the end of each day, rebuilt backwards from current positions
    cur = {s: float(p["qty"]) for s, p in positions.items()}
    net = fills.groupby(["day", "sym"]).qty.sum() if len(fills) else pd.Series(dtype=float)
    hold = {}
    q = dict(cur)
    for d in reversed(days):
        hold[d] = dict(q)
        if len(fills):
            for (fd, s), n in net.items():
                if fd == d:
                    q[s] = q.get(s, 0.0) - n
    start_hold = q            # holdings at the close before days[0]

    cash = fills.assign(cost=fills.qty * fills.px).groupby(["day", "sym"]).cost.sum() if len(fills) else pd.Series(dtype=float)

    def day_pnl(agent, i):
        d = days[i]
        prev = days[i - 1] if i > 0 else None
        h0 = hold[prev] if prev else start_hold
        h1 = hold[d]
        pnl = 0.0
        p0 = px.loc[prev] if prev else px.loc[px.index[px.index < d][-1]]
        p1 = px.loc[d]
        for s in set(h0) | set(h1):
            if owner.get(s) != agent:
                continue
            v1 = h1.get(s, 0.0) * p1.get(s, float("nan"))
            v0 = h0.get(s, 0.0) * p0.get(s, float("nan"))
            v1 = 0.0 if h1.get(s, 0.0) == 0 else v1
            v0 = 0.0 if h0.get(s, 0.0) == 0 else v0
            pnl += v1 - v0 - cash.get((d, s), 0.0)
        return pnl

    rows = []
    for i, d in enumerate(days):
        if i == 0:
            continue                                  # days[0] is the rebase close itself
        cap = {a: PCT[a] * eq.iloc[i - 1] for a in PCT}
        pb, pr = day_pnl("Bull", i), day_pnl("Rocket", i)
        mine_pnl = pb if IS_BULL else pr
        prev = days[i - 1]
        sat_val = sum(q * px.loc[d].get(s, 0.0) for s, q in hold[d].items()
                      if owner.get(s) == ME and s != CORE[ME] and q)
        rows.append(dict(day=d, pnl=mine_pnl, ret=mine_pnl / cap[ME],
                         sat_pct=sat_val / (PCT[ME] * eq.iloc[i]),
                         bench=px.loc[d, BENCH] / px.loc[prev, BENCH] - 1,
                         acct_pnl=eq.iloc[i] - eq.iloc[i - 1], both_pnl=pb + pr))
    df = pd.DataFrame(rows).set_index("day")

    def period(since):
        sub = df[df.index > since]
        if sub.empty:
            return None
        return dict(ret=(1 + sub.ret).prod() - 1, bench=(1 + sub.bench).prod() - 1, days=len(sub))

    monday = today - timedelta(days=today.weekday())
    last = df.iloc[-1]
    expl = df.both_pnl.sum() / df.acct_pnl.sum() if df.acct_pnl.sum() else float("nan")
    return dict(
        agent=ME, bench=BENCH, asof=df.index[-1], live=live,
        today=dict(ret=last.ret, bench=last.bench, pnl=last.pnl),
        week=period(monday - timedelta(days=3)) if df.index[-1] >= monday else None,
        since_reset=period(RESET), since_rebase=period(REBASE),
        coverage=expl, unattributed=sorted(unattributed),
        fills=fills, owner=owner,
        fills_today=fills[(fills.day == df.index[-1]) & fills.sym.map(lambda s: owner.get(s) == ME)] if len(fills) else fills,
        daily=df,
    )


def pct(x, nd=2):
    return "n/a" if x is None or pd.isna(x) else f"{100 * x:+.{nd}f}%"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", action="store_true")
    a = ap.parse_args()
    r = compute()
    print(f"{r['agent']} vs {r['bench']} — as of {r['asof']}{' (live)' if r['live'] else ''}")
    for k, lab in (("today", "Today"), ("week", "This week"), ("since_reset", f"Since {RESET:%m/%d} (new rules)"),
                   ("since_rebase", f"Since {REBASE:%m/%d} (rebase)")):
        v = r[k]
        if v:
            print(f"  {lab:26s} {r['agent']} {pct(v['ret']):>8s}   {r['bench']} {pct(v['bench']):>8s}   "
                  f"diff {100 * (v['ret'] - v['bench']):+.2f} pts")
    print(f"  attribution coverage: {pct(r['coverage'], 1)} of account P&L explained by Bull+Rocket fills"
          + (f"  ⚠️ unattributed: {', '.join(r['unattributed'])}" if r['unattributed'] else ""))
    if a.days:
        print(r["daily"].tail(10).to_string(float_format=lambda x: f"{x:.4f}"))


if __name__ == "__main__":
    main()
