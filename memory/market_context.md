# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-10 Thursday premarket (Week 37 day 3)  ← CURRENT

All "last close" figures are **Wednesday 2026-09-09's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **PPI today 8:30 ET · CPI tomorrow 8:30 ET · FOMC decision 9/16** | 🚨 **The single most important line in this file.** Friday's CPI is the **last inflation print before the decision**, and it lands 60 minutes before the open — a gap a 7% trail cannot protect against (lesson 29). **This closes Friday as an entry date**, which is exactly where rule 45's day-2 conversions land |
| 🚨 **Brent / WTI** | **102.11 (+0.89%)** / **97.46 (+1.47%)** | **A new run high, and now clearly through $100.** 92.33 → 95.15 → 97.10 → 95.44 → 98.53 → 100.50 → **102.11 = +10.6% across the run.** WTI confirmed every leg. **This is the input that makes tomorrow's CPI dangerous rather than routine** |
| 🚨 **10-yr** | **4.84%** (**+0.65%**) | **SEVENTH session through the 4.75% trigger, and still rising** (4.78 → 4.81 → 4.84). Lesson 34's "trend, not one print" bar was met three sessions ago |
| **VIX** | **16.47** (+0.06%) | Flat, fourth session up off the 14.21 low, far below the 22 brake. **No size restriction.** ⚠️ Note it is *not* pricing the CPI/FOMC pair |
| **Russell fut** | 2,925.50 (**+0.09%**) | Off yesterday's 2,950.90 — **the level fell 0.9% overnight even though the change print is flat.** S&P +0.09%, Nasdaq −0.19% |
| SPY / IWM | **762.40 (−0.46%)** / **290.64 (−1.37%)** | Wednesday's settled closes. 🚨 **Factor −0.91% — the largest single-session drag against Rocket in two weeks** |
| Gold / Dollar | 4,435.40 (+0.44%) / 98.78 (+0.01%) | Gold bid, dollar flat — the inflation trade intact on all three legs |

### The inflation trade is now three-for-three going into the print that tests it

Energy at a run high, the 10-yr through its trigger for a seventh session, gold bid, dollar
flat — every leg this file tracks points the same way, and the **August CPI lands tomorrow
at 8:30 ET as the last data the FOMC sees before 9/16.** For a week the setup has been
"three inputs pointing at a September hike"; tomorrow is when the market gets to reprice it
in one 30-second gap.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design**, and this is recorded as a
decision, not an omission.

**For satellites it is the opposite** — this is precisely rule 29's gate, and it did real
work today: it is one of the two binding kills on DBI (the only live name on the board) and
it independently closed IRD's day-2 window.

### Factor watch

🚨 **IWM −1.37% vs SPY −0.46% = −0.91% of factor on Wednesday**, carried at 93.7% core
weight ≈ **−0.85% on the book** — Rocket's whole day, since there are no satellites.
**Lesson 28 bars booking a one-session move as information**, and it is being honored here
in the unfavourable direction exactly as it was honored on 9/08 in the favourable one. But
note the *direction* is the same as the six-week drift (−2.50% since rebase), and that
figure is the one that matters. It belongs in `weekly_review`.

🚨 **`weekly_review` for W36 (due Fri 9/04) STILL has not run — THIRD session flagging it.**
No `memory/weekly_reviews/2026-W36.md`; no 9/04 `market_close` entry in `trade_log.md`.
W37's review is due **tomorrow, Fri 9/11**. The hand-built Rocket-vs-SPY chain is now
**nine sessions stale** (last good number: 8/28 W35, −2.51%). Lesson 47 /
[[launchd-quota-contention]].

### Instrument health

✅ **`market_data.py macro` clean for an EIGHTH straight session** — every field populated.
✅ **`eligibility`: 15 requested → 15 returned** (lesson 43 count held, run against full output).
✅ **Nasdaq earnings-calendar API delivered on its third use** — **41 reporters for 9/09,
39 for 9/10**, with market cap and BMO/AMC in one call. It produced **three in-universe
survivors** on a session where the scanner's overlap tier was **zero usable names**
(BNC = crypto-treasury mandate kill, LPA = Costa Rica domicile mandate kill).
🚨 **Lesson 17a, TWELFTH straight demonstration — two sign flips.** `top_movers` printed
**QUIK "$11.35, +5.8%"** against a real settled bar of **$10.73, −2.01% at 26% of range on
216,600**, and **NMAD "$4.00, +7.8%"** against **$3.71, −3.89% at 0% of range on 188,800**.
**Both names also fail the 300k volume gate outright.** 12 of 20 `top_movers` rows carried
RelVol `—` or `0.0x`; **19 of 20 `unusual_volume` rows were below 1.0×.**
⚠️ **SHOE is the "right by accident" case**: the scanner's −13.1% *is* a real move (a 6:10 AM
guidance cut), but it is still an extended-hours quote in a `Change %` column.
🚨 **NEW — `positions` / `portfolio_snapshot.py` rounding cost a wrong rebalance verdict.**
9/09's `market_close` struck its band check on **"raw qty 10 sh"**; the broker API returns
**9.8636**. Corrected, IWM was **2.01% over target — inside the band**, not 3.28% outside.
**This is lesson 24 exactly, firing on the same field it was written about.** See
`research_log.md`; the deferred SELL is withdrawn.

---

## Snapshot — 2026-09-09 Wednesday premarket (Week 37 day 2)

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
