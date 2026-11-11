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


# ---------------------------------------------------------------------------------------
# Sample-size honesty (added 2026-11-11, per DockerApps/RESEARCH_GATES.md §1-2).
# The ranking is saved every day and the same names stay on top for weeks, so rows overlap:
# Bull's "n=56" at 20 days on 11/11 was ONE 20-day window. Every figure below therefore
# reports DISTINCT NAMES and NON-OVERLAPPING WINDOWS, and the headline mean uses only
# non-overlapping dates. Learning-loop thresholds are written in those units, never in rows.
# ---------------------------------------------------------------------------------------
def independent_dates(dates, idx, h):
    """Greedy earliest-first subset of dates at least h trading days apart, each with h days of data."""
    out, last = [], None
    for d in sorted(set(dates)):
        pos = idx.searchsorted(pd.Timestamp(d), side="right") - 1
        if pos < 0 or pos + h >= len(idx):
            continue
        if last is None or pos - last >= h:
            out.append(d)
            last = pos
    return out


def bucket_table(ranks, P, h):
    """Per independent window: equal-weight mean excess per bucket, and the top8 - 26+ spread."""
    wins = independent_dates(ranks["asof"], P.index, h)
    rows = []
    for d in wins:
        day = ranks[ranks["asof"] == d]
        r = {b: np.nanmean([fwd_excess(P, s, d, h, False) for s in day[day.bucket == b].sym])
             for b in ("top 8", "9–25", "26+")}
        rows.append(r)
    return pd.DataFrame(rows), wins


def random_twin_pct(dec_buys, ranks, P, h, sims=500, seed=7):
    """Percentile of the BUYs' mean h-day excess among random picks from the same morning's
    eligible list (turnover-matched random twin, RESEARCH_GATES §2). None if not computable."""
    rows = []
    for r in dec_buys.itertuples():
        prior = ranks[pd.to_datetime(ranks["asof"]) < pd.Timestamp(r.date)]
        if prior.empty:
            continue
        pool = prior[prior["asof"] == prior["asof"].max()].sym.tolist()
        x = fwd_excess(P, r.sym, r.date, h, True)
        if not np.isnan(x) and pool:
            rows.append((r.date, x, pool))
    if len(rows) < 3:
        return None, len(rows)
    real = np.mean([x for _, x, _ in rows])
    rng, cache, out = np.random.default_rng(seed), {}, []
    for _ in range(sims):
        v = []
        for d, _, pool in rows:
            s = pool[rng.integers(len(pool))]
            if (s, d) not in cache:
                cache[(s, d)] = fwd_excess(P, s, d, h, True)
            v.append(cache[(s, d)])
        out.append(np.nanmean(v))
    return float((np.array(out) < real).mean() * 100), len(rows)


def dedupe(sub, h_days=20):
    """One observation per name per decision type per 20 trading days (repeat vetoes of the
    same name on consecutive mornings are one judgment, not five)."""
    keep, last = [], {}
    for r in sub.sort_values("date").itertuples():
        d = pd.Timestamp(r.date)
        if r.sym in last and np.busday_count(last[r.sym].date(), d.date()) < h_days:
            continue
        last[r.sym] = d
        keep.append(r.Index)
    return sub.loc[keep]


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
           f"Generated {datetime.now():%Y-%m-%d %H:%M}. Excess return = stock minus {BENCH} over the same "
           f"window. **`w` = non-overlapping windows, `names` = distinct stocks — these are the sample sizes. "
           f"Overlapping daily rows are NOT independent observations** (RESEARCH_GATES §1).", ""]

    # 1. SIGNAL -- rank buckets, one observation per non-overlapping window
    out += ["## 1. Signal — does the ranking work?", "",
            "| Bucket | " + " | ".join(f"{h}d excess" for h in HORIZONS) + " |",
            "|---|" + "---|" * len(HORIZONS)]
    spread_lines = []
    if not ranks.empty:
        ranks["bucket"] = pd.cut(ranks["rank"], [0, 8, 25, 10_000], labels=["top 8", "9–25", "26+"])
        tabs = {h: bucket_table(ranks, P, h) for h in HORIZONS}
        for b in ["top 8", "9–25", "26+"]:
            cells = []
            for h in HORIZONS:
                t, wins = tabs[h]
                cells.append(f"{fmt(t[b].mean()) if len(t) else fmt(np.nan)} (w={len(wins)})")
            out.append(f"| {b} | " + " | ".join(cells) + " |")
        for h in HORIZONS:
            t, wins = tabs[h]
            if len(t):
                sp = (t["top 8"] - t["26+"]).dropna()
                tstat = sp.mean() / sp.std(ddof=1) * np.sqrt(len(sp)) if len(sp) >= 3 and sp.std(ddof=1) > 0 else np.nan
                spread_lines.append(f"- {h}d top 8 minus 26+: {fmt(sp.mean())} over {len(sp)} window(s)"
                                    + (f", t {tstat:+.2f}" if not np.isnan(tstat) else " (t needs ≥3 windows)"))
    out += [""] + spread_lines + ["",
            "**Rule:** change the score formula only with **≥ 6 non-overlapping 20-day windows** (~6 months) "
            "and |t| ≥ 2 on the top-8-minus-26+ spread. One bad (or good) month is one observation.", ""]

    # 2/3. JUDGMENT + PICKS -- deduplicated, with the random-twin control
    out += [f"## 2. Judgment — {ME}'s decisions vs {BENCH} (one obs per name per 20 days)", "",
            "| Decision | names | " + " | ".join(f"{h}d excess" for h in HORIZONS) + " | hit rate 20d |",
            "|---|---|" + "---|" * (len(HORIZONS) + 1)]
    for d in ["BUY", "VETO", "EXIT"]:
        sub = dedupe(dec[dec.decision == d]) if not dec.empty else dec
        cells, v20 = [], pd.Series(dtype=float)
        for h in HORIZONS:
            v = pd.Series([fwd_excess(P, r.sym, r.date, h, strictly_before=True) for r in sub.itertuples()]).dropna()
            cells.append(f"{fmt(v.mean())} ({len(v)})")
            if h == 20:
                v20 = v
        hit = f"{(v20 > 0).mean():.0%}" if len(v20) else "n/a"
        out.append(f"| {d} | {sub.sym.nunique() if len(sub) else 0} | " + " | ".join(cells) + f" | {hit} |")
    if not dec.empty and not ranks.empty:
        buys = dedupe(dec[dec.decision == "BUY"])
        twin = []
        for h in HORIZONS:
            pc, n = random_twin_pct(buys, ranks, P, h)
            twin.append(f"{h}d: " + (f"{pc:.0f}th pct (n={n})" if pc is not None else f"n/a (n={n})"))
        out += ["", "**BUYs vs random twins** (random picks from the same morning's eligible list, same "
                "horizon): " + " · ".join(twin) + ". Above the 95th percentile = evidence of skill; "
                "inside 5th–95th = indistinguishable from chance."]
    out += ["",
            f"- **BUY > 0** → the picks beat {BENCH}.",
            f"- **VETO < BUY** → vetoes are helping. **VETO > BUY** across **≥ 10 distinct names** at 20d → "
            f"{ME}'s judgment is subtracting value: loosen the rule behind those vetoes, in writing, citing this table.",
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
