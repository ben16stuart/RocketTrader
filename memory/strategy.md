# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-09-26 (W39 review). **The binding constraint is now THROUGHPUT.** Rocket
enters almost nothing: 1 satellite in 19 sessions. Research quality and exits are not the
problem.
Prior version (W34 era, incl. same-day vs second-day evidence, filter write-ups, SPY-era
attribution): `memory/archive/strategy_history.md`.

---

## Standing Meta-Problem — re-diagnosed 2026-09-26

| Constraint | Status |
|---|---|
| **Throughput (entries per week)** | 🔴 **Binding.** 1 entry in W36–W39; satellites avg ≈2% over 4 weeks, 8.8% in W39 |
| **Satellite-floor design** | 🔴 **Unreachable unless 4/4 slots are full at the 15% cap** (3 × 15% = 45%). Escalated to Ben (W39 §6) |
| **Gate accretion** | 🔴 69 lessons, almost all new kills. File compressed 2026-09-26. New rule: a lesson must replace a check or state what it lets through |
| **Stale-reference errors inside a session** | 🔴 NEW (lesson 70): RARE's entry quoted +2.8% "breakout" against the wrong prior close. It was −3.6% |
| Research / catalyst verification | ✅ Strong. SCHL 8-K save, PRME Gate A, PAAI falsification |
| Exit discipline | ✅ No discretionary errors since ETON (W34). 32a applied correctly to RARE |
| Performance measurement | 🟡 Hand-built book chain rebuilt through W39. Snapshot's figure still invalid (lesson 23) |
| Routine completion | 🔴 W36–W38 reviews never ran. 9/21 premarket and 9/24 market_close never ran ([[launchd-quota-contention]]) |
| Instruments | 🟡 Scanner RelVol unusable (17g/64). No `sip` premarket data (66). Nasdaq calendar can invert beats (65) |

## Core Edge

Small caps ($50M–$2B, US-incorporated, not S&P 500) with a named, dated, primary-sourced
catalyst. Big funds can't trade these at scale, so individual catalysts produce outsized
moves. **At a ~$3.1k slice, a satellite is ~$465, so liquidity is never the practical
constraint.** Rocket's real constraint is finding enough names.

## Benchmark and attribution (IWM since 2026-09-17)

The core is IWM and the benchmark is IWM, so **the core contributes 0 excess by
construction.** Every basis point of "Rocket vs IWM" comes from satellites plus cash.

| Week | Book | IWM | Rocket vs IWM | Satellite % avg | Source of excess |
|---|---|---|---|---|---|
| W36 (8/31–9/04) | +0.10% | +0.09% | +0.01% | 0% | cash timing |
| W37 (9/08–9/11) | −2.26% | −2.41% | +0.15% | 0% | cash buffer in a down week |
| W38 (9/14–9/18) | −1.34% | −1.66% | +0.32% | 0% | 9/17 sale to cash before 9/18 drop |
| **W39 (9/21–9/25)** | **−0.99%** | **−0.75%** | **−0.24%** | **8.8%** | RARE −0.38%, cash +0.14% |
| Since rebase 7/20 | −2.12% | −3.54% | **+1.42%** | | mostly W34 OMER + pre-IWM cash |

Pre-W36 attribution vs SPY (W30–W35) lives in `archive/strategy_history.md`. Stock picking
was +0.68% cumulative through W35. It has added **nothing** since.

## Catalyst Hierarchy (from real results)

1. **Earnings beat + guidance RAISED, sized as a %, day 2.** Still the only type with realized
   winners (OMER, ETON's entry). Source it from the **earnings calendar first**, then
   **confirm on the issuer's 8-K**, never on the calendar row (lesson 65).
2. **FDA/regulatory approval or clearance.** 🆕 Produced **both** live candidates in W39
   (RARE, PRME). This is the most productive sourcing channel right now. Never inside a
   PDUFA window.
3. Government contract / named funding: grade the **committed** dollars, not the headline (49a).
4. Unusual volume + breakout (next day). Treat the scanner as a name source only.
5. Short squeeze + catalyst.
6. Analyst initiation: must be a Buy, dated, and in-universe. In W39 all 6 of 6 failed the universe.
7. 🚫 Beat without a raise, or with a sub-1% raise or a reaffirmation: disqualified (5/5a/5f).

## Entry Framework

- **Second-day is the default** (same-day 0-for-3, second-day 2-for-3). Gap >35% → day 2 only.
  Gap 20–35% → first 10-min base. 9:30–9:45 range >10% → defer.
- **Pre-commit gates as SHAPES** (close in the upper half of the range), not levels (42c).
  Validated 3× (IRD, ELMT, PRME).
- 🆕 **Rule 70: before any entry, name the prior SETTLED close and today's % against it,
  in the log line.** State where the breakout day was. If the catalyst's big up-day was
  yesterday and today is red, that's a day-2 fade: apply rule 2b/4 to it. It is not
  "a fresh high."
- **Stop fit uses max drawdown from the running high** (54c), not range ÷ trail.
- **Late-catalyst decay:** a catalyst more than ~3 sessions old needs a fresh trigger (a new
  base plus a green day-of print), not just "the thesis is intact."

## Filters that earn their keep (full text in lessons archive)

Dilution first (8) · analyst ladder vs a dated consensus (11) · close-position-in-range (4) ·
median ADV (46) · issuer filing over any secondary source (57b/65) · 8-K Item number (57a).

## Throughput commitments (new 2026-09-26)

1. **The board has three sources every premarket, in this order:** earnings calendar
   (confirm on the 8-K), FDA/regulatory news, then screeners. The screeners have
   contributed 0 entries in 4 weeks.
2. **A kill must name ONE binding gate.** If a name fails only a soft gate, write the
   entry plan anyway and let market_open decide it on the tape. Soft gates are ladder
   headroom, short-float, and float size.
3. **New lessons must replace a check or say what they let through** (W39 §6). Tool-defect
   notes go in the instruments section, not the trading rules.
4. **Track the funnel weekly: names screened → survivors → entries.** A week with zero
   survivors needs a check on the sourcing, as well as a write-up.

## Open questions / escalations (awaiting Ben)

- 🚨 **Satellite floor arithmetic** (W39 §6): recommend counting open slots (≥2 of 4) or a ~30%
  floor. As written, 50% needs all four slots full at max size.
- **Rebalance basis, slice vs book** (lesson 44). Not binding while IWM is at the 50% cap.
- **$2B ceiling vs +25% ladder** (lesson 13). It blocks CNXC and PRGS for W40 by construction.
- **Midday flat "−5% = cut" vs stop distance** (lesson 67).
- **Premarket liquidity check needs `sip` data** (lesson 66). Without it the check is aspirational.

## Rules under observation

- 32a (only override a stop >2% away): applied to RARE 9/25 midday. Pending outcome.
- Rule 70 (name the prior settled close): new.
- Late-catalyst decay: new; test on the next FDA name.
