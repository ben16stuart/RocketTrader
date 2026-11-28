# Rocket learning ledger — scorecard

Generated 2026-11-28 09:21. Excess return = stock minus IWM over the same window. **`w` = non-overlapping windows, `names` = distinct stocks — these are the sample sizes. Overlapping daily rows are NOT independent observations** (RESEARCH_GATES §1).

## 1. Signal — does the ranking work?

| Bucket | 5d excess | 10d excess | 20d excess |
|---|---|---|---|
| top 8 |  +1.63% (w=5) |  +2.57% (w=2) | +10.05% (w=1) |
| 9–25 |  -0.36% (w=5) |  -0.36% (w=2) |  -9.08% (w=1) |
| 26+ |  +0.09% (w=5) |  +0.23% (w=2) |  +0.02% (w=1) |

- 5d top 8 minus 26+:  +1.54% over 5 window(s), t +0.49
- 10d top 8 minus 26+:  +2.34% over 2 window(s) (t needs ≥3 windows)
- 20d top 8 minus 26+: +10.03% over 1 window(s) (t needs ≥3 windows)

**Rule:** change the score formula only with **≥ 6 non-overlapping 20-day windows** (~6 months) and |t| ≥ 2 on the top-8-minus-26+ spread. One bad (or good) month is one observation.

## 2. Judgment — Rocket's decisions vs IWM (one obs per name per 20 days)

| Decision | names | 5d excess | 10d excess | 20d excess | hit rate 20d |
|---|---|---|---|---|---|
| BUY | 20 |  +0.96% (20) |  -0.14% (15) |  +1.94% (9) | 33% |
| VETO | 16 |  +0.50% (17) |  -0.92% (15) |  -6.97% (10) | 40% |
| EXIT | 11 |  -4.02% (10) |  -8.12% (6) | -12.32% (1) | 0% |

**BUYs vs random twins** (random picks from the same morning's eligible list, same horizon): 5d: 64th pct (n=20) · 10d: 51th pct (n=15) · 20d: 70th pct (n=9). Above the 95th percentile = evidence of skill; inside 5th–95th = indistinguishable from chance.

- **BUY > 0** → the picks beat IWM.
- **VETO < BUY** → vetoes are helping. **VETO > BUY** across **≥ 10 distinct names** at 20d → Rocket's judgment is subtracting value: loosen the rule behind those vetoes, in writing, citing this table.
- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that went on to beat IWM: hold longer / widen the exit rank.

## Recent decisions (last 15)

| date | sym | decision | rank | 20d excess | reason |
|---|---|---|---|---|---|
| 2026-11-16 | TXG | BUY | 1 |   n/a  | DE; Q3 filed, no dilution; #1 momentum |
| 2026-11-16 | IOVA | BUY | 3 |   n/a  | DE; ATM terminated 9/30, no new dilution, no binary in 10d |
| 2026-11-16 | PAYS | BUY | 9 |   n/a  | NV; Q3 profit guides raised, rev guide reaffirmed, no dilution |
| 2026-11-16 | CBRL | BUY | 15 |   n/a  | TN; earnings 12/09, annual meeting 11/19 not binary |
| 2026-11-20 | APPN | BUY | 9 |   n/a  | Rank 9; Q3 beat, FY guide raised, DE, no dilution found; fills GTLB sl |
| 2026-11-20 | RCEL | VETO | 4 |   n/a  | hard: healthcare sector cap full (CDNA/TXG/IOVA) |
| 2026-11-20 | ATRC | VETO | 6 |   n/a  | hard: healthcare sector cap full |
| 2026-11-20 | UTZ | VETO | 7 |   n/a  | judgment: pending going-private merger pins price |
| 2026-11-20 | SLN | VETO | 2 |   n/a  | hard: gate FAIL non-US HQ (UK) |
| 2026-11-23 | SLN | VETO | 2 |   n/a  | gate FAIL: non-US HQ (United Kingdom) |
| 2026-11-23 | RCEL | VETO | 4 |   n/a  | HC sector cap: CDNA/TXG/IOVA hold 3 HC satellites |
| 2026-11-23 | ATRC | VETO | 6 |   n/a  | HC sector cap: CDNA/TXG/IOVA hold 3 HC satellites |
| 2026-11-23 | UTZ | VETO | 7 |   n/a  | pending going-private deal pins the price |
| 2026-11-23 | PAYS | EXIT | 29 |   n/a  | rank decay 29 > 25 at W47 review |
| 2026-11-23 | INTA | BUY | 10 |   n/a  | Q1 FY27 beat, DE, no dilution/S-3; replaces PAYS; half size (VIX 26.8) |
