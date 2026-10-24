# Rocket learning ledger — scorecard

Generated 2026-10-24 09:20. Excess return = stock minus IWM over the same window. `n` = observations with that much forward data so far.

## 1. Signal — does the ranking work?

| Bucket | 5d excess (n) | 10d excess (n) | 20d excess (n) |
|---|---|---|---|
| top 8 |  +0.16% (8) |   n/a  (0) |   n/a  (0) |
| 9–25 |  +2.22% (17) |   n/a  (0) |   n/a  (0) |
| 26+ |  +1.40% (623) |   n/a  (0) |   n/a  (0) |

Healthy signal: top 8 > 9–25 > 26+, and top 8 > 0. Judge it on the 20d column with n ≥ 100 before changing the score formula.

## 2. Judgment — Rocket's decisions vs IWM

| Decision | 5d excess (n) | 10d excess (n) | 20d excess (n) | hit rate 20d |
|---|---|---|---|---|
| BUY |  +1.02% (5) |   n/a  (0) |   n/a  (0) | n/a |
| VETO |  +1.10% (4) |   n/a  (0) |   n/a  (0) | n/a |
| EXIT |   n/a  (0) |   n/a  (0) |   n/a  (0) | n/a |

- **BUY > 0** → the picks beat IWM.
- **VETO < BUY** → vetoes are helping (the names Rocket refused did worse than the ones it took).
  **VETO > BUY** with n ≥ 10 → Rocket's judgment is subtracting value: loosen whatever rule drove those vetoes, in writing, citing this table.
- **EXIT < 0** → exits dodged underperformance (good). EXIT > 0 → exits sold names that went on to beat IWM: hold longer / widen the exit rank.

## Recent decisions (last 15)

| date | sym | decision | rank | 20d excess | reason |
|---|---|---|---|---|---|
| 2026-10-19 | SMWB | VETO | 2 |   n/a  | hard: gate FAIL non-US HQ (Israel) |
| 2026-10-19 | ABCL | VETO | 5 |   n/a  | hard: gate FAIL non-US HQ (Canada) |
| 2026-10-19 | OABI | VETO | 6 |   n/a  | hard: healthcare sector cap (REPL/TXG/NEO picked at ranks 1/3/4); othe |
| 2026-10-19 | SDGR | VETO | 7 |   n/a  | hard: healthcare sector cap (REPL/TXG/NEO picked at ranks 1/3/4); othe |
| 2026-10-19 | REPL | BUY | 1 |   n/a  | RP1 melanoma, 6-1 +493%, rank 1; no new negative news at open |
| 2026-10-19 | TXG | BUY | 3 |   n/a  | Q2 beat + raised FY guide, Atera demand |
| 2026-10-19 | NEO | BUY | 4 |   n/a  | Q2 beat + raised FY26 guide; earnings 10/27 is 6td out |
| 2026-10-19 | DK | BUY | 8 |   n/a  | refining margins, Brent ~109 blockade |
| 2026-10-19 | NSIT | BUY | 9 |   n/a  | Q2 beat, FY26 EPS guide raised |
