# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

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

## Snapshot — 2026-09-03 Thursday premarket (Week 36 day 4)

| Metric | Level | Read |
|---|---|---|
| **10-yr** | **4.796%** (**+0.00%**) | 🆕 **The grind STOPPED.** Seven straight up sessions (4.639 → 4.796) ended in a dead-flat print. Still **through the 4.75% trigger for a third session**, so the flag stays live — but lesson 34 cuts both ways: a trend that stops trending is information too. **Watch, do not act** |
| **VIX** | **15.38** (+1.2%) | 🆕 **The three-day rise broke.** 9/01's 16.34 spike has retraced (16.34 → 15.20 → 15.38). Far below the 22 brake. **No size restriction** |
| Russell fut | 2,952.60 (−0.21%) | Mildly risk-off, and the **least-bad leg** — Nasdaq −0.16%, S&P −0.03% |
| SPY / IWM | 765.16 (+0.44%) / **294.01 (+1.18%)** | Wednesday's settled closes. **Factor +0.74% — in Rocket's favour** |
| Brent / WTI | **97.10 (+1.54%)** / 92.62 (+1.77%) | 🚨 **Third straight confirmed session, and it is accelerating: Brent $92.33 → $95.15 → $97.10 = +5.2% in three days** |
| Gold | **4,471.40 (+2.41%)** | 🆕 Large one-day move, with the **dollar −0.34%** |

### The rate story paused; the inflation story did not

Two things eased overnight — the 10-yr went flat for the first time in seven sessions, and
VIX gave back its spike. Neither is a reversal, and **lesson 34 forbids standing a flag
down on one print** exactly as it forbade raising one. The flag stays live at 4.796%.

What did **not** ease is the commodity leg: **Brent +5.2% in three sessions with WTI
confirming every one of them**, now joined by **gold +2.41% against a falling dollar.**
That combination — energy up, gold up, dollar down — is the market pricing *inflation*,
not growth, underneath a chair who has refused forward guidance. It is the one input that
has moved in a straight line all week.

**The designed response for the core remains no action.** The core carries no trailing
stop, backed by 33 years of SPY testing in which every stop configuration lost to
buy-and-hold. A live flag is not a licence to override a tested design.

### 🚨 Today's calendar, and the reason it matters more than usual

**Jobless claims (205K exp vs 203K), trade balance and unit labor costs all land 8:30 AM**
— *before* the open, which is the good case — followed by **Services PMI 8:45 AM**. Then
🚨 **ISM Services at 10:00 AM** (54.5 exp vs 54.1), **25 minutes after the 9:35 decision
window** — the same hostile shape as the last three sessions.

🚨 **Then the August jobs report Friday 9/04.** Any satellite opened today is held
overnight through a payrolls print. **That is an argument against a same-day entry which
is independent of every name-specific gate** (rule 29), and it applied to a board on which
all ten screened names were killed on their own merits anyway.

### Factor watch

**IWM +1.18% vs SPY +0.44% = +0.74% of factor Wednesday**, carried at 93.79% core weight
≈ **+0.69% on the book.** This is the first meaningful session in Rocket's favour in some
time — **and lesson 28 applies with exactly the same force as when it hurt**: a
one-session factor move carries no information. It does **not** dent the −2.50%
since-rebase drift escalated to the user. **Read it in `weekly_review` tomorrow, not here,
and do not book it as recovery.**

✅ **`market_data.py macro` clean for a fourth straight session** — every field populated.
🔧 Scanners improved off a very low base: **`top_movers` unusable RelVol 13 of 20** (was
20 of 20), **`unusual_volume` 14 of 20 below 1.0×** (was 19 of 20) — and it produced
**one genuine 23.9× signal (TLYS)**, the first in six sessions. See `research_log.md`.
⚠️ Note: 9/02's file recorded VIX at **16.81**; the settled 9/01 close was **16.34**. Small,
but recorded here rather than left to propagate (lesson 39a).

---
