"""The learning ledger -- scores the ranking AND the agent's judgment against its benchmark.

Shared by Bull (vs SPY) and Rocket (vs IWM) since 2026-10-17; the agent is read from the
repo path. Text below says Bull/SPY for readability.

Added 2026-10-06. Bull's old learning loop was one-sided: every losing trade added
a rule, nothing ever measured what the rules REJECTED, so the rules could only
tighten -- until nothing passed. This ledger makes learning symmetric. It answers
three questions every week, with numbers instead of narrative:

  1. SIGNAL   -- do top-ranked names (rank_screen.py) actually beat SPY going
                 forward, and beat lower-ranked names?  (memory/ledger/ranks/*.csv)
  2. JUDGMENT -- when Bull overrides the ranking (VETO a top name, or BUY a lower
                 one), do its overrides beat the names it passed over?
  3. PICKS    -- do Bull's actual BUYs beat SPY over 5 / 10 / 20 trading days?

Usage:
  python scripts/candidate_ledger.py log SYMBOL BUY|VETO|EXIT "reason" [--rank N]
  python scripts/candidate_ledger.py score          # prints + writes memory/ledger/scorecard.md

Decision meanings:
  BUY  -- bought it as a satellite.
  VETO -- a name inside the top 8 eligible that Bull deliberately did NOT buy.
          The reason must name the specific concern (earnings in 3 days, accounting
          restatement, 4th name in one sector...). "Didn't like it" is not a reason.
  EXIT -- sold a satellite for a reason other than its stop (rank decay, thesis break).

Forward returns are measured from the last close BEFORE the decision date (the
information Bull had), and from the as-of close of each ranking file.
"""
import os
import sys
import csv
import glob
import argparse
import warnings
from datetime import date, datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IS_BULL = os.path.basename(REPO) == "OpusTrader"
ME, BENCH = ("Bull", "SPY") if IS_BULL else ("Rocket", "IWM")
LEDGER = (os.environ.get("AGENT_LEDGER_DIR") or os.environ.get("BULL_LEDGER_DIR")
          or os.path.join(REPO, "memory", "ledger"))  # env override = tests only
DECISIONS = os.path.join(LEDGER, "decisions.csv")
RANKS = os.path.join(LEDGER, "ranks")
SCORECARD = os.path.join(LEDGER, "scorecard.md")
HORIZONS = (5, 10, 20)
FIELDS = ["date", "time", "sym", "decision", "rank", "reason"]


def cmd_log(a):
    os.makedirs(LEDGER, exist_ok=True)
    new = not os.path.exists(DECISIONS)
    with open(DECISIONS, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(FIELDS)
        w.writerow([date.today().isoformat(), datetime.now().strftime("%H:%M"),
                     a.sym.upper(), a.decision, a.rank if a.rank is not None else "", a.reason])
    print(f"Logged {a.decision} {a.sym.upper()} -> {os.path.relpath(DECISIONS, REPO)}")


def load_prices(syms, start):
    import yfinance as yf
    raw = yf.download(sorted(set(syms)) + [BENCH], start=start, auto_adjust=True,
                      progress=False, threads=True)["Close"]
    if isinstance(raw, pd.Series):
        raw = raw.to_frame()
    return raw.ffill(limit=2)


def fwd_excess(P, sym, ref_day, h, strictly_before):
    """Excess return of sym over the benchmark for h trading days from the reference close."""
    idx = P.index
    pos = idx.searchsorted(pd.Timestamp(ref_day), side="left" if strictly_before else "right") - 1
    if pos < 0 or pos + h >= len(idx) or sym not in P:
        return np.nan
    a, b = P[sym].iloc[pos], P[sym].iloc[pos + h]
    sa, sb = P[BENCH].iloc[pos], P[BENCH].iloc[pos + h]
    if any(pd.isna(x) for x in (a, b, sa, sb)):
        return np.nan
    return (b / a - 1) - (sb / sa - 1)


def fmt(x):
    return "  n/a " if pd.isna(x) else f"{100 * x:+6.2f}%"


def cmd_score(_a):
    rank_files = sorted(glob.glob(os.path.join(RANKS, "*.csv")))
    ranks = pd.concat([pd.read_csv(f) for f in rank_files], ignore_index=True) if rank_files else pd.DataFrame()
    dec = pd.read_csv(DECISIONS) if os.path.exists(DECISIONS) else pd.DataFrame(columns=FIELDS)
    if ranks.empty and dec.empty:
        print("Ledger is empty -- nothing to score yet.")
        return
    syms = set(ranks.get("sym", pd.Series(dtype=str))) | set(dec.get("sym", pd.Series(dtype=str)))
    starts = []
    if not ranks.empty:
        starts.append(pd.to_datetime(ranks["asof"]).min())
    if not dec.empty:
        starts.append(pd.to_datetime(dec["date"]).min())
    first = min(starts)
    P = load_prices(syms, (first - pd.Timedelta(days=10)).date().isoformat())
    out = [f"# {ME} learning ledger — scorecard", "",
           f"Generated {datetime.now():%Y-%m-%d %H:%M}. Excess return = stock minus {BENCH} over the "
           f"same window. `n` = observations with that much forward data so far.", ""]

    # 1. SIGNAL -- rank buckets
    out += ["## 1. Signal — does the ranking work?", "",
            "| Bucket | " + " | ".join(f"{h}d excess (n)" for h in HORIZONS) + " |",
            "|---|" + "---|" * len(HORIZONS)]
    if not ranks.empty:
        ranks["bucket"] = pd.cut(ranks["rank"], [0, 8, 25, 10_000], labels=["top 8", "9–25", "26+"])
        for b in ["top 8", "9–25", "26+"]:
            sub = ranks[ranks.bucket == b]
            cells = []
            for h in HORIZONS:
                v = [fwd_excess(P, r.sym, r.asof, h, strictly_before=False) for r in sub.itertuples()]
                v = pd.Series(v).dropna()
                cells.append(f"{fmt(v.mean())} ({len(v)})")
            out.append(f"| {b} | " + " | ".join(cells) + " |")
    out += ["", "Healthy signal: top 8 > 9–25 > 26+, and top 8 > 0. Judge it on the 20d column "
            "with n ≥ 100 before changing the score formula.", ""]

    # 2/3. JUDGMENT + PICKS
    out += [f"## 2. Judgment — {ME}'s decisions vs {BENCH}", "",
            "| Decision | " + " | ".join(f"{h}d excess (n)" for h in HORIZONS) + " | hit rate 20d |",
            "|---|" + "---|" * (len(HORIZONS) + 1)]
    for d in ["BUY", "VETO", "EXIT"]:
        sub = dec[dec.decision == d] if not dec.empty else dec
        cells, v20 = [], pd.Series(dtype=float)
        for h in HORIZONS:
            v = pd.Series([fwd_excess(P, r.sym, r.date, h, strictly_before=True) for r in sub.itertuples()]).dropna()
            cells.append(f"{fmt(v.mean())} ({len(v)})")
            if h == 20:
                v20 = v
        hit = f"{(v20 > 0).mean():.0%}" if len(v20) else "n/a"
        out.append(f"| {d} | " + " | ".join(cells) + f" | {hit} |")
    out += ["",
            f"- **BUY > 0** → the picks beat {BENCH}.",
            f"- **VETO < BUY** → vetoes are helping (the names {ME} refused did worse than the ones it took).",
            f"  **VETO > BUY** with n ≥ 10 → {ME}'s judgment is subtracting value: loosen whatever rule "
            "drove those vetoes, in writing, citing this table.",
            "- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that "
            f"went on to beat {BENCH}: hold longer / widen the exit rank.", ""]

    # recent decision list
    if not dec.empty:
        out += ["## Recent decisions (last 15)", "", "| date | sym | decision | rank | 20d excess | reason |",
                "|---|---|---|---|---|---|"]
        for r in dec.tail(15).itertuples():
            out.append(f"| {r.date} | {r.sym} | {r.decision} | {'' if pd.isna(r.rank) else int(r.rank)} | "
                       f"{fmt(fwd_excess(P, r.sym, r.date, 20, True))} | {str(r.reason)[:70]} |")
    text = "\n".join(out) + "\n"
    os.makedirs(LEDGER, exist_ok=True)
    open(SCORECARD, "w").write(text)
    print(text)
    print(f"(written to {os.path.relpath(SCORECARD, REPO)})")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    lg = sp.add_parser("log")
    lg.add_argument("sym")
    lg.add_argument("decision", choices=["BUY", "VETO", "EXIT"])
    lg.add_argument("reason")
    lg.add_argument("--rank", type=int)
    sp.add_parser("score")
    a = ap.parse_args()
    {"log": cmd_log, "score": cmd_score}[a.cmd](a)


if __name__ == "__main__":
    main()
