# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---


## Snapshot — 2026-09-08 Tuesday premarket (Week 37 day 1)  ← CURRENT

First session after Labor Day. All "last close" figures below are **Friday 2026-09-04's
settled closes** — Monday was a market holiday, so there is no intervening session and
these are real settled prints, not thin holiday quotes.

| Metric | Level | Read |
|---|---|---|
| 🚨 **10-yr** | **4.78%** (**+0.46%**) | **Turned back UP** after two flat/down sessions (4.796 → 4.760 → **4.78**). **Fifth session through the 4.75% trigger** — and now with a **hot** labor print behind it. Flag live and, for the first time in this stretch, the trend and the fundamentals agree |
| **VIX** | **15.70** (+2.61%) | Up from Friday's 14.21 two-week low, but far below the 22 brake. **No size restriction** |
| **Russell fut** | 2,965.50 (**−0.37%**) | 🚨 **The weakest leg** — S&P −0.24%, Nasdaq **+0.10%**. Small caps leaning risk-off into the open, opposite to Friday's cash tape |
| SPY / IWM | **770.19 (−0.39%)** / **296.01 (+0.28%)** | Friday's settled closes. **Factor +0.67% — in Rocket's favour** |
| 🚨 **Brent / WTI** | **98.53 (+2.34%)** / 93.86 (+2.60%) | **The ramp did NOT break — it paused one session and resumed at a NEW HIGH.** 92.33 → 95.15 → 97.10 → 95.44 → **98.53 = +6.7% across the run**, WTI confirming every leg |
| Gold / Dollar | 4,439.60 (+0.22%) / 99.00 (−0.16%) | **Gold pulled back** (4,515.70 → 4,439.60 over the stretch); dollar turned back down |

### The jobs report was a 3× beat, and that changes the rate flag

**August NFP: +162K against a +53K consensus** — the strongest print since March, the
first up-month in five, with the **prior two months revised UP by a net +55K** (July
**−23K → +21K**). Unemployment **4.1%, unchanged**.

Friday's file called this "the whole session in one number." It resolved **hot**, which
makes a **September hike more live, not less** — under a chair who has refused forward
guidance. Combined with **Brent at a new run high** and the **10-yr turning back up through
4.75% for a fifth session**, the rates flag is no longer a lone technical trigger: it now
has a labor print and a commodity trend pointing the same way. **Lesson 34's "trend, not
one print" bar is met on rates for the first time.**

**The designed response for the core remains no action.** The core carries no trailing
stop, backed by 33 years of SPY testing in which every stop configuration lost to
buy-and-hold. **A live flag is not a licence to override a tested design**, and this is
recorded as a decision, not an omission.

### 🚩 Friday falsified this file's own 8/28 prediction — recorded, not buried

Friday's snapshot argued that **VIX 14.21 into a binary was the 8/28 configuration**, where
a hawkish surprise made **IWM take it ~7× harder than SPY (−1.35% vs −0.18%)**. The binary
landed hawkish-adjacent (a 3× payrolls beat), and **IWM went UP +0.28% while SPY went DOWN
−0.39% — IWM outperformed by 0.67%.** The predicted mechanism did **not** operate.

The plausible read is that a growth surprise helps domestic small caps more than the
implied rate path hurts them. **But lesson 28 bars booking one session as information —
and it bars it in this direction exactly as it barred it when the factor hurt.** So:
the *prediction* is marked failed (lesson 39a — do not let a claim harden by being copied
forward), while the *explanation* is left unproven.

### 🚨 The calendar for the rest of the week

- **FOMC September 15–16, decision Wednesday 9/16 — 6 trading days out.** A satellite
  opened today on a 1–5 day hold clears it; **anything opened Thursday or later carries
  into it.** A dated rule-29 gate for the back half of this week.
- **Today**: trade balance 8:30 AM (pre-open, the good case); Services PMI ~9:45 and **ISM
  Services 10:00 AM — 25 minutes AFTER the 9:35 decision window.** ⚠️ **The search source
  for today's calendar recycled stale content** (it named a Fed Vice Chair who does not hold
  the office and labelled August data as "September"), so these times are carried as
  **low-confidence** rather than asserted (lesson 39). The 10:00 ISM shape has held for
  several sessions and is the part worth planning around.
- **Wednesday 9/09 is the week's first real earnings slate** — see `research_log.md`.

### Factor watch

**IWM +0.28% vs SPY −0.39% = +0.67% of factor Friday**, carried at 93.83% core weight
≈ **+0.63% on the book.** **Lesson 28 applies with the same force as when it hurt**: one
session carries no information, and this does not dent the −2.50% since-rebase drift
escalated to the user. Read it in `weekly_review`.

### Instrument health

✅ **`market_data.py macro` clean for a SIXTH straight session** — every field populated.
🆕 **New calendar instrument adopted**: the **Nasdaq earnings-calendar API** returns ticker
+ market cap + BMO/AMC in one call. Earnings Whispers and stockanalysis.com both **404'd or
hit a login wall** via WebFetch, and three web searches produced only partial undated lists.
**This is now the lesson-41 calendar source.**
🚨 **WORST SCANNER SESSION ON RECORD — three sign flips and a 35-point error.**
`top_movers` printed **BNC "+41.0%, $4.92, 1393.8× RelVol"** against a real settled bar of
**+6.08%, $3.49, 1.86×**; **ENOV "+3.5%" was really −4.33%**, **TROX "+4.0%" really
−1.43%**, **WTI "+3.6%" really −1.80%**. Tenth straight lesson-17a demonstration, and the
first time the *sign* of the day's move was wrong on multiple rows. **The overlap tier was
BNC alone — mandate-excluded, and fictional in both lists.** See `research_log.md`.

---

## Snapshot — 2026-09-04 Friday premarket (Week 36 day 5)  ← CURRENT

| Metric | Level | Read |
|---|---|---|
| **10-yr** | **4.76%** (**−0.71%**) | **Second session not rising** (4.796 → 4.760). Still **through the 4.75% trigger for a fourth session**, so the flag stays live — but the seven-session grind has now stopped *and* backed off. Lesson 34 both ways: **watch, do not act** |
| 🚨 **VIX** | **14.21** (−0.77%) | **A two-week low — into the month's biggest event.** No brake (22). 🚨 **But this is the exact 8/28 configuration**: VIX at a low *ahead* of a binary is **positioning, not calm**, and that read paid when Warsh ran hawkish |
| Russell fut | 2,967.80 (−0.06%) | Flat, and **up from 2,952.60 yesterday** — the tape is not leaning either way into the print |
| SPY / IWM | 773.17 (+1.05%) / **295.19 (+0.40%)** | Thursday's settled closes. **Factor −0.65% — against Rocket** |
| Brent / WTI | 95.44 (−0.08%) / 91.00 (−0.33%) | 🆕 **The three-session ramp BROKE.** Both legs down together for the first time this week |
| Gold / Dollar | **4,515.70 (+0.53%)** / 99.11 (**+0.11%**) | Gold still bid, but **the dollar has turned UP** (was −0.34%) |

### The inflation trade paused; the event risk did not

Yesterday's file called out one input moving in a straight line all week: **energy up, gold
up, dollar down** — the market pricing inflation. **Two of those three legs broke
overnight.** Brent and WTI fell together for the first time this week, and the dollar
turned positive. Only gold is still rising.

**Lesson 34 forbids standing a flag down on one print exactly as it forbade raising one**,
so nothing changes on the rates flag at 4.76% — but the honest read is that the commodity
story is no longer the clean one-way trend it was 24 hours ago.

### 🚨 The whole session is one number, and it lands at 8:30 AM

**August nonfarm payrolls: +53K consensus** (street range +50K to +58K), **unemployment
4.1% expected, unchanged**, following July's **−23K**. It resolves **before the open**,
which is the good case — but it is the month's largest dispersion event, and it arrives
with a **September rate HIKE genuinely in debate** under a chair who has refused forward
guidance.

🚨 **The VIX at 14.21 into that is the 8/28 setup, not comfort.** On 8/28 a two-week-low
VIX ahead of Warsh's debut meant *nobody was positioned*, and **IWM took the result ~7×
harder than SPY (−1.35% vs −0.18%)**. Rate-sensitive small caps repricing a hawkish
surprise is a direct, demonstrated mechanism — and IWM is 93.8% of Rocket's book.

**The designed response for the core remains no action.** The core carries no trailing
stop, backed by 33 years of SPY testing in which every stop configuration lost to
buy-and-hold. **A live flag is not a licence to override a tested design**, and a jobs
print is not a reason to time the benchmark.

### 🚨 Labor Day — the calendar gate is stronger than usual today

**Monday 2026-09-07 is Labor Day and the market is CLOSED** (confirmed against the Alpaca
calendar: 9/04 → 9/08). Any satellite opened today is carried through the jobs reaction
**and a three-day weekend**. Rule 29 already argues against a same-day entry on an event
day; the extra day makes it decisive. **Next session is Tuesday 2026-09-08.**

### Factor watch

**IWM +0.40% vs SPY +1.05% = −0.65% of factor Thursday**, carried at 93.81% core weight
≈ **−0.61% on the book** — it gave back most of Wednesday's +0.69%. **Lesson 28 applies
with the same force as when it helped**: a one-session move carries no information, and
yesterday's file was careful not to book Wednesday's gain as recovery. The same discipline
applies to today's loss. **The six-week read (−2.50% since rebase) belongs in
`weekly_review`, which runs today.**

✅ **`market_data.py macro` clean for a fifth straight session.**
🔧 Scanners still poor: **`top_movers` 12 of 17 rows unusable**, **`unusual_volume` 14 of
17 below 1.0×**. 🚨 **And `top_movers` misreported BBCP as "$10.62, +17.4%" against a real
regular-session close of $9.05, +1.9%** — a 15-point error from quoting an after-hours
print, lesson 17a's ninth demonstration. Both of the session's real names came from the
**earnings calendar**, not the screener. See `research_log.md`.
⚠️ Yesterday's file recorded **Brent 97.10**; today's settled series implies a prior close
near **95.52**. The 97.10 was an unsettled intraday print — corrected here rather than left
to propagate (lesson 39a).

---
