# Rocket learning ledger — scorecard

Generated 2026-10-31 09:20. Excess return = stock minus IWM over the same window. `n` = observations with that much forward data so far.

## 1. Signal — does the ranking work?

| Bucket | 5d excess (n) | 10d excess (n) | 20d excess (n) |
|---|---|---|---|
| top 8 |  +7.43% (48) |  +9.59% (8) |   n/a  (0) |
| 9–25 |  +2.60% (102) |  +4.46% (17) |   n/a  (0) |
| 26+ |  -0.07% (3991) |  +0.66% (621) |   n/a  (0) |

Healthy signal: top 8 > 9–25 > 26+, and top 8 > 0. Judge it on the 20d column with n ≥ 100 before changing the score formula.

## 2. Judgment — Rocket's decisions vs IWM

| Decision | 5d excess (n) | 10d excess (n) | 20d excess (n) | hit rate 20d |
|---|---|---|---|---|
| BUY |  +0.76% (8) | +10.83% (5) |   n/a  (0) | n/a |
| VETO |  +4.72% (11) |  +6.73% (4) |   n/a  (0) | n/a |
| EXIT |  -2.43% (1) |   n/a  (0) |   n/a  (0) | n/a |

- **BUY > 0** → the picks beat IWM.
- **VETO < BUY** → vetoes are helping (the names Rocket refused did worse than the ones it took).
  **VETO > BUY** with n ≥ 10 → Rocket's judgment is subtracting value: loosen whatever rule drove those vetoes, in writing, citing this table.
- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that went on to beat IWM: hold longer / widen the exit rank.

## Recent decisions (last 15)

| date | sym | decision | rank | 20d excess | reason |
|---|---|---|---|---|---|
| 2026-10-26 | OABI | VETO | 3 |   n/a  | hard: gate EARNINGS 10/30 (4d) + healthcare sector cap full (TXG/REPL/ |
| 2026-10-26 | XGN | VETO | 4 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-26 | CDNA | VETO | 6 |   n/a  | hard: gate EARNINGS 10/29 (3d) + healthcare sector cap full (TXG/REPL/ |
| 2026-10-26 | TWST | VETO | 7 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-26 | APPS | VETO | 16 |   n/a  | hard: gate EARNINGS 11/02 (5d) |
| 2026-10-26 | QLYS | VETO | 20 |   n/a  | hard: tech sector cap (NSIT held + QMCO/GTLB picked) |
| 2026-10-26 | DK | EXIT | 75 |   n/a  | rank decay 75 > 25 at W43 review |
| 2026-10-26 | QMCO | BUY | 5 |   n/a  | turnaround, balance sheet repaired, no fresh dilution |
| 2026-10-26 | GTLB | BUY | 17 |   n/a  | Q2 beat + raise, strong momentum |
| 2026-10-26 | CLDT | BUY | 25 |   n/a  | low-vol momentum REIT, fills non-HC/non-Tech slot |
| 2026-10-27 | OABI | VETO | 3 |   n/a  | hard: gate EARNINGS 10/30 (3d) + healthcare sector cap full (TXG/REPL/ |
| 2026-10-27 | CDNA | VETO | 5 |   n/a  | hard: gate EARNINGS 10/29 (2d) + healthcare sector cap full (TXG/REPL/ |
| 2026-10-27 | XGN | VETO | 6 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-27 | TWST | VETO | 7 |   n/a  | hard: healthcare sector cap full (TXG/REPL/NEO held) |
| 2026-10-27 | KELYA | BUY | 25 |   n/a  | staffing turnaround, FCF 6x, DE inc, no dilution; fills last slot |
