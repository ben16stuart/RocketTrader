# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-09 Wednesday premarket (Week 37 day 2)  ← CURRENT

All "last close" figures are **Tuesday 2026-09-08's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **Brent / WTI** | **100.50 (+2.63%)** / 95.18 (+2.31%) | 🚨 **BRENT BROKE $100** — a round number and a new run high. 92.33 → 95.15 → 97.10 → 95.44 → 98.53 → **100.50 = +8.9% across the run.** WTI has confirmed every single leg. The one-session pause on 9/04 is now clearly noise, not a break |
| 🚨 **10-yr** | **4.81%** (**+0.46%**) | **SIXTH session through the 4.75% trigger**, and rising again (4.78 → 4.81). Lesson 34's "trend, not one print" bar was met yesterday and the trend has extended. Rates + energy now point the same way |
| **VIX** | **16.09** (+2.35%) | Third session up off the 14.21 low, still far below the 22 brake. **No size restriction** |
| **Russell fut** | 2,950.90 (**−0.43%**) | 🚨 **The weakest leg for a second straight session** — S&P −0.24%, Nasdaq −0.47%. Small caps still leaning risk-off, and now the whole complex is red |
| SPY / IWM | **765.96 (−0.55%)** / **294.67 (−0.45%)** | Tuesday's settled closes. **Factor +0.10% — marginally in Rocket's favour** |
| Gold / Dollar | 4,435.90 (+0.96%) / 98.82 (−0.02%) | Gold bid again after pulling back; dollar flat-to-down |

### The inflation trade is back to one-way, and this time it has a rates print behind it

For a week this file has tracked energy/gold/dollar as a proxy for the market pricing
inflation, and noted on 9/04 that two of three legs had broken. **They have re-formed, and
Brent is now through $100 at a new run high.** Combine that with the **10-yr through 4.75%
for a sixth session** and the **3× payrolls beat** (+162K vs +53K, prior two months revised
up a net +55K, unemployment 4.1%), and the September hike case has three independent inputs
pointing the same direction rather than one technical trigger.

**The designed response for the core remains no action.** The core carries no trailing
stop, backed by 33 years of SPY testing in which every stop configuration lost to
buy-and-hold. **A live flag is not a licence to override a tested design**, and this is
recorded as a decision, not an omission.

### 🚨 FOMC is now 5 trading days out and it is closing entry windows

**FOMC September 15–16, decision Wednesday 9/16.** A satellite opened **today** on a 1–5 day
hold reaches 9/16 at the far end; **anything opened Thursday or later carries into it.**
This is no longer a background note — it is the gate that closed the day-2 entry on CAL, the
only name that survived today's screen on instrument quality. See `research_log.md`.

### Factor watch

**IWM −0.45% vs SPY −0.55% = +0.10% of factor Tuesday**, carried at 93.80% core weight
≈ **+0.09% on the book.** **Lesson 28: a one-session move carries no information**, and
+0.10% is inside the noise of the noise. The six-week drift (−2.50% since rebase) is the
figure that matters and it belongs in `weekly_review`.

🚨 **`weekly_review` for W36 (due Fri 9/04) STILL has not run — second session flagging it.**
No `memory/weekly_reviews/2026-W36.md`, no 9/04 `market_close` entry in `trade_log.md`. The
hand-built Rocket-vs-SPY chain is now **over a week stale** (last good number: 8/28 W35,
−2.51%), and every session since has been correctly carrying it forward rather than
updating it. Lesson 47 / [[launchd-quota-contention]].

### Instrument health

✅ **`market_data.py macro` clean for a SEVENTH straight session** — every field populated.
✅ **Nasdaq earnings-calendar API delivered on its second use** — 24 reporters for 9/08, 45
for 9/09, with market cap and BMO/AMC in one call. **It produced four in-universe names with
real dated catalysts on a day the scanner produced one usable row.** This is now the
primary board source (lesson 41); the scanner is a name source only (17a).
🚨 **Lesson 17a, ELEVENTH straight demonstration.** `top_movers` printed **OCC "$15.41,
+12.5%"** against a real settled close of **$13.70, −1.08% at 11% of range** — and the
scanner ran at **04:22 ET, hours before any BMO release**, so that is a thin premarket print
reported as both the price and the day's change. **11 of 17 rows carried RelVol `—` or
`0.0x`; 18 of 20 `unusual_volume` rows were below 1.0×.** The overlap tier was **OCC** plus
**USDE** (standing rule-31 mandate kill) — one real name, and its live book was **bid $11.47
/ ask $20.01, a 55%-of-price spread.**
🆕 **New instrument caveat (46g)**: at ~06:25 ET **every** small cap shows a broken-looking
book — **AVO read 55% wide on a median ADV of 865,900**, passing the liquidity gate by 189%.
**The premarket spread check corroborates a median-ADV failure; it is noise on its own.**

---

## Snapshot — 2026-09-08 Tuesday premarket (Week 37 day 1)

| Metric | Level | Read |
|---|---|---|
| 🚨 **10-yr** | **4.78%** (+0.46%) | Turned back UP; fifth session through the 4.75% trigger, now with a hot labor print behind it |
| **VIX** | **15.70** (+2.61%) | Up from Friday's 14.21 two-week low, far below the 22 brake |
| **Russell fut** | 2,965.50 (**−0.37%**) | The weakest leg — S&P −0.24%, Nasdaq +0.10% |
| SPY / IWM | 770.19 (−0.39%) / 296.01 (+0.28%) | Friday's settled closes. **Factor +0.67% — in Rocket's favour** |
| 🚨 **Brent / WTI** | 98.53 (+2.34%) / 93.86 (+2.60%) | The ramp did not break — it paused one session and resumed at a new high |
| Gold / Dollar | 4,439.60 (+0.22%) / 99.00 (−0.16%) | Gold pulled back; dollar turned back down |

**August NFP was a 3× beat: +162K vs +53K consensus**, strongest since March, first up-month
in five, prior two months revised **up a net +55K** (July −23K → +21K). Unemployment 4.1%,
unchanged. **A September hike is more live, not less.**

🚩 **This file's own 8/28 prediction was falsified and recorded, not buried**: it argued a
low VIX into a binary would make IWM take a hawkish result ~7× harder than SPY (the 8/28
shape, −1.35% vs −0.18%). The binary landed hawkish-adjacent and **IWM went UP +0.28% while
SPY fell −0.39%.** The prediction is marked failed (lesson 39a); the explanation — that a
growth surprise helps domestic small caps more than the implied rate path hurts them — is
left **unproven**, because lesson 28 bars booking one session as information in the
favourable direction exactly as it bars it in the unfavourable one.

🚨 **Worst scanner session on record**: three sign flips and a 35-point error. `top_movers`
printed BNC "+41.0%, $4.92, 1393.8× RelVol" against a real bar of **+6.08%, $3.49, 1.86×**;
ENOV "+3.5%" was really −4.33%, TROX "+4.0%" really −1.43%, WTI "+3.6%" really −1.80%.

---
