# Rocket learning ledger — scorecard

Generated 2026-11-07 09:20. Excess return = stock minus IWM over the same window. `n` = observations with that much forward data so far.

## 1. Signal — does the ranking work?

| Bucket | 5d excess (n) | 10d excess (n) | 20d excess (n) |
|---|---|---|---|
| top 8 |  +3.71% (88) |  +8.45% (48) |   n/a  (0) |
| 9–25 |  +0.46% (187) |  +0.48% (102) |   n/a  (0) |
| 26+ |  -0.20% (7579) |  -0.48% (3968) |   n/a  (0) |

Healthy signal: top 8 > 9–25 > 26+, and top 8 > 0. Judge it on the 20d column with n ≥ 100 before changing the score formula.

## 2. Judgment — Rocket's decisions vs IWM

| Decision | 5d excess (n) | 10d excess (n) | 20d excess (n) | hit rate 20d |
|---|---|---|---|---|
| BUY |  -0.33% (12) |  +4.31% (8) |   n/a  (0) | n/a |
| VETO |  +4.02% (18) |  +1.16% (11) |   n/a  (0) | n/a |
| EXIT |  -7.90% (4) | -13.30% (1) |   n/a  (0) | n/a |

- **BUY > 0** → the picks beat IWM.
- **VETO < BUY** → vetoes are helping (the names Rocket refused did worse than the ones it took).
  **VETO > BUY** with n ≥ 10 → Rocket's judgment is subtracting value: loosen whatever rule drove those vetoes, in writing, citing this table.
- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that went on to beat IWM: hold longer / widen the exit rank.

## Recent decisions (last 15)

| date | sym | decision | rank | 20d excess | reason |
|---|---|---|---|---|---|
| 2026-10-27 | XGN | VETO | 6 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-27 | TWST | VETO | 7 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-27 | KELYA | BUY | 25 |   n/a  | staffing turnaround, FCF 6x, DE inc, no dilution; fills last slot |
| 2026-11-02 | IOVA | VETO | 4 |   n/a  | hard: gate EARNINGS 11/05 (3d) |
| 2026-11-02 | CDNA | VETO | 6 |   n/a  | hard: healthcare sector cap full (TXG/REPL + OABI replacing NEO) |
| 2026-11-02 | ABCL | VETO | 8 |   n/a  | hard: gate FAIL non-US HQ (Canada) |
| 2026-11-02 | NEO | EXIT | 27 |   n/a  | rank decay 27 > 25 at W44 review |
| 2026-11-02 | KELYA | EXIT | 26 |   n/a  | rank decay 26 > 25 at W44 review |
| 2026-11-02 | OABI | BUY | 3 |   n/a  | Rank 3 momentum; 10-Q no going concern, ATM undrawn; replaces NEO |
| 2026-11-02 | CAKE | BUY | 15 |   n/a  | Q3 comps +15.2% beat, rank 15 promoted; replaces KELYA |
| 2026-11-02 | CDNA | BUY | 6 |   n/a  | TXG stop slot refill; rank 6, Q3 rev +39% and 3rd straight guide raise |
| 2026-11-02 | TXG | EXIT |  |   n/a  | 25% trailing stop fired (hwm 87.82, fill 65.91) |
| 2026-11-05 | PD | BUY | 23 |   n/a  | rank 23 promoted past vetoed names; Tech slot open after QMCO stop; ea |
| 2026-11-05 | QLYS | VETO | 9 |   n/a  | EARNINGS 11/09 within 5 trading days |
| 2026-11-05 | ATRC | VETO | 14 |   n/a  | Healthcare sector cap (OABI/CDNA/REPL) |
