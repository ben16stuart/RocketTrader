# Rocket learning ledger — scorecard

Generated 2026-11-14 09:20. Excess return = stock minus IWM over the same window. **`w` = non-overlapping windows, `names` = distinct stocks — these are the sample sizes. Overlapping daily rows are NOT independent observations** (RESEARCH_GATES §1).

## 1. Signal — does the ranking work?

| Bucket | 5d excess | 10d excess | 20d excess |
|---|---|---|---|
| top 8 |  +1.95% (w=4) |  +2.57% (w=2) | +10.05% (w=1) |
| 9–25 |  -1.10% (w=4) |  -0.36% (w=2) |  -9.08% (w=1) |
| 26+ |  -0.03% (w=4) |  +0.24% (w=2) |  +0.04% (w=1) |

- 5d top 8 minus 26+:  +1.98% over 4 window(s), t +0.49
- 10d top 8 minus 26+:  +2.34% over 2 window(s) (t needs ≥3 windows)
- 20d top 8 minus 26+: +10.00% over 1 window(s) (t needs ≥3 windows)

**Rule:** change the score formula only with **≥ 6 non-overlapping 20-day windows** (~6 months) and |t| ≥ 2 on the top-8-minus-26+ spread. One bad (or good) month is one observation.

## 2. Judgment — Rocket's decisions vs IWM (one obs per name per 20 days)

| Decision | names | 5d excess | 10d excess | 20d excess | hit rate 20d |
|---|---|---|---|---|---|
| BUY | 15 |  -0.26% (15) |  -0.09% (12) | +12.59% (5) | 40% |
| VETO | 15 |  +1.28% (15) |  -0.34% (11) |  +4.99% (4) | 50% |
| EXIT | 6 |  -4.63% (6) | -13.39% (4) |   n/a  (0) | n/a |

**BUYs vs random twins** (random picks from the same morning's eligible list, same horizon): 5d: 48th pct (n=15) · 10d: 52th pct (n=12) · 20d: 97th pct (n=5). Above the 95th percentile = evidence of skill; inside 5th–95th = indistinguishable from chance.

- **BUY > 0** → the picks beat IWM.
- **VETO < BUY** → vetoes are helping. **VETO > BUY** across **≥ 10 distinct names** at 20d → Rocket's judgment is subtracting value: loosen the rule behind those vetoes, in writing, citing this table.
- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that went on to beat IWM: hold longer / widen the exit rank.

## Recent decisions (last 15)

| date | sym | decision | rank | 20d excess | reason |
|---|---|---|---|---|---|
| 2026-11-02 | CAKE | BUY | 15 |   n/a  | Q3 comps +15.2% beat, rank 15 promoted; replaces KELYA |
| 2026-11-02 | CDNA | BUY | 6 |   n/a  | TXG stop slot refill; rank 6, Q3 rev +39% and 3rd straight guide raise |
| 2026-11-02 | TXG | EXIT |  |   n/a  | 25% trailing stop fired (hwm 87.82, fill 65.91) |
| 2026-11-05 | PD | BUY | 23 |   n/a  | rank 23 promoted past vetoed names; Tech slot open after QMCO stop; ea |
| 2026-11-05 | QLYS | VETO | 9 |   n/a  | EARNINGS 11/09 within 5 trading days |
| 2026-11-05 | ATRC | VETO | 14 |   n/a  | Healthcare sector cap (OABI/CDNA/REPL) |
| 2026-11-09 | TXG | VETO | 1 |   n/a  | hard: healthcare sector cap full (CDNA/OABI/REPL held) |
| 2026-11-09 | UTZ | VETO | 3 |   n/a  | judgment: pending going-private merger pins price (DEFM14A 10/02, SC 1 |
| 2026-11-09 | IOVA | VETO | 4 |   n/a  | hard: healthcare sector cap full (CDNA/OABI/REPL held) |
| 2026-11-09 | RCEL | VETO | 6 |   n/a  | hard: healthcare sector cap full (CDNA/OABI/REPL held) |
| 2026-11-09 | HAE | VETO | 7 |   n/a  | hard: healthcare sector cap full (CDNA/OABI/REPL held) |
| 2026-11-09 | PD | EXIT | 26 |   n/a  | rank decay 26 > 25 at W45 review |
| 2026-11-09 | CLDT | EXIT | 58 |   n/a  | rank decay 58 > 25 at W45 review |
| 2026-11-09 | AMPL | BUY | 8 |   n/a  | Rank 8; Q3 rev +25%, FY guide raised 1.9%, DE, no dilution; replaces P |
| 2026-11-09 | PBF | BUY | 18 |   n/a  | Rank 18; Q3 EPS 12.54, dividend +18%, net debt cut; DE, no dilution; r |
