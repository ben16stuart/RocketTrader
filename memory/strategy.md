# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-08-21 (Week 34 review — **the constraint has moved again: from entry
timing to EXIT discipline, and to auditing Rocket's own claims about itself**)

---

## ⚠️ Standing Meta-Problem — REDIAGNOSED 2026-08-14

| Constraint | Status |
|---|---|
| Deployment / idle cash | ✅ **Solved and proven.** Cash drag −0.49% (W32) → **−0.04%** (W33) |
| Fractional core rebalancing | ✅ Three live rebalances, all within $0.20 of target |
| Idea flow / scanner | ✅ Fixed 8/07 |
| Research quality | ✅ **Now a strength** — 4/4 skips validated in W33, ladder filter 4-for-4 |
| **Entry timing (which DAY)** | 🟡 **Improved, not solved.** W34's entry was good (+4.7% by Friday); the *exit* destroyed it. |
| **Exit discipline** | 🔴 **NEW — this is the binding constraint.** Cost **0.82% of book** in W34. See below. |
| **Auditing Rocket's own claims** | 🔴 **NEW.** A counterfactual was asserted, never checked, and was backwards. |
| **Performance measurement** | 🟡 Chain rebuilt 8/21 and it ties out. The *instrument* is still wrong — see below. |
| **Instrument integrity** | 🔴 `position_reconciler.py` was silently misreporting ownership. Fixed 8/21. |
| **Routine completion (monitors / midday)** | 🟡 No recurrence since 8/14; midday still dead since 6/15 |

### 🥇 The binding constraint: Rocket enters on the wrong day

| Entry type | Trades | Result |
|---|---|---|
| **Same-day** (day one of the gap) | CSTL, FF, VELO | **0 for 3** |
| **Second-day continuation** | MRLN, OMER (open, green), **ETON** | **2 for 3** |

Both same-day losses failed the *same* way: Rocket bought the retrace of a failed opening
spike and called it a base. VELO travelled **22.7% in fifteen minutes** before the "9:45
base" formed at $15.27 — that was not a base, it was the middle of a range. On a name that
volatile, a 7% trailing stop sits **inside the noise band** and is a coin flip, not risk
management.

> This document has asserted since May that second-day is *"where Rocket makes money."*
> **Week 33 is the first week it was tested against a same-day control group, and it held.**

⚠️ **Corrected 2026-08-21.** ETON was also a second-day entry and it booked a loss, so the
record is **2-for-3, not 2-for-2**. But the *cause* matters: ETON's entry was **+4.7% four
sessions later** and it lost only because Rocket closed it early. **The entry thesis
survives; the perfect record does not.** Do not let a clean number outlive its evidence —
that is the same failure this week's headline finding is about.

### 🥇 THE NEW BINDING CONSTRAINT: exits, and unaudited self-assessment

**W34's single satellite had a real catalyst, a good entry, and correct sizing — and still
lost, entirely at the exit.** The 8/20 close was justified as beating where the trailing
stop would have fired. The bars say the stop sat at **$59.36** and was **never touched**;
ETON closed the week at **$63.47**. Holding was **+$19.74**; closing **cost $25.83 —
0.82% of book**, four times the realised loss.

Three things went wrong, in increasing order of importance:

1. **A rule was broken.** Lesson 30a — "a Form 144 is not an exit trigger" — was written
   the day before and used as exactly that trigger.
2. **The asymmetry was computable and was not computed.** The stop was 0.7% below price:
   at most 0.7% to gain, unbounded to lose. → **new rule 32a: only override a trailing
   stop that is >2% away.**
3. 🥇 **The self-grade was never audited.** Rocket applies rule 11a/lesson 33 ("undated
   claims are not evidence") to analysts and to news — **but not to its own trade log.**
   The counterfactual was recorded as fact and would have justified repeating the error.
   → **new rule 32c: every "it would have been worse" claim must cite the actual stop
   level and the actual subsequent low.**

**Generalised:** Rocket's research scepticism is strong and outward-facing. **Its weakest
audit surface is its own record of itself** — the trade log, the counterfactuals, the
attribution, and the scripts that produce them. Two of this week's three findings
(lesson 32, the reconciler) were errors *in Rocket's own bookkeeping*, not in the market.

### Research is no longer what loses money — execution is

Week 33's three losses ranked by cost:
1. **≈−0.70%** — OMER never evaluated on 8/13 (monitor died silently). Infrastructure.
2. **−0.39%** — FF, a P2 promoted only because the P1 failed and a slot was open. Discipline.
3. **−0.17%** — VELO, correct research, wrong entry day. Timing.

**None of it was bad analysis. Do not loosen the research bar to fix an execution problem.**

### 🔴 Rocket still cannot measure Rocket — and a near-match is the most dangerous state

`portfolio_snapshot.py` derives Rocket's return from a fixed 30% of the *shared* account,
which is algebraically the whole account's return with Bull's P&L included.

✅ **The hand-built chain was rebuilt 8/21** and ties to the cent: **Rocket +4.53% vs SPY
+3.18% = +1.35% since rebase** (first positive reading), cumulative real alpha **+1.53%**.

🚨 **The snapshot now reads +1.28% — only 7bp off, down from 88bp. This is the most
dangerous the instrument has ever been.** It did not get better; **Bull's cumulative
return happens to sit near Rocket's right now**, and it will diverge again with no
warning. A broken gauge that currently reads correctly is harder to distrust than one that
reads absurdly. **Keep the hand-built book. Re-derive it every week, including — especially
— the weeks the two agree.**

### 🔴 Instrument integrity — bugs that cancel out are worse than bugs that shout

`position_reconciler.py` opened the W34 review declaring Rocket's only satellite
**UNATTRIBUTED** ("do not size against this"). Three independent parser bugs — a substring
match reading `(market_close)` as a SELL, two-event headers dropping their second event,
and same-day round trips never closing because the log is written newest-first.

**They were cancelling.** Four phantom open positions were suppressed only because a
*different* bug filed them under "core", which is exempt from the missing-position check.
**The report looked plausible and was assembled from four compounding errors.** This is
lesson 15's thesis with the strongest evidence yet: **silent degradation is the failure
mode that costs money.** Every script that feeds a decision needs a periodic tie-out, not
just a glance at whether its output looks reasonable.

---

## Core Edge

Rocket trades small cap stocks ($50M–$2B, not S&P 500) with identifiable catalysts. Most
institutional money cannot trade small caps at scale; individual catalysts create outsized
moves larger funds cannot exploit. Rocket moves fast and manages tight.

## Catalyst Hierarchy (best to worst — updated from real results)

1. **Earnings beat + RAISED guidance, on the SECOND day.** The raise is load-bearing and
   the day is load-bearing. Everything below assumes both.
   - 🆕 **Live record (2026-08-21): the only catalyst type that has made money.** OMER
     **+12.4%** (open), ETON **+4.7% by Friday** on the entry (booked −1.4% only because
     of the exit). **Every other catalyst type Rocket has traded is net negative.** The
     hierarchy is not a ranking any more — it is a shortlist of one, and rungs 2–6 are
     hypotheses awaiting evidence.
2. FDA/regulatory approval (biotech — explosive, binary). Never inside a PDUFA window.
3. Government contract / named funding (defense/drone — multi-day accumulation)
4. Unusual volume + breakout (next day)
5. Short squeeze + catalyst (explosive but unpredictable)
6. Analyst initiation (slower, 1–2 day move)
7. 🚫 **Beat WITHOUT a raise — DISQUALIFIED, not demoted.** 3-for-3 as a fader: SVCO,
   CVRX, FF. Promoted from "caution" to a hard skip on 2026-08-14.

## 🥇 SOURCING — new 2026-08-28, and the highest-value change on this page

**Rung 1 is the only catalyst that has ever made money, and it does NOT require a
screener to find. Earnings are on a calendar, published in advance. STOP WAITING FOR
THEM TO BUBBLE UP THROUGH A BROKEN VOLUME SCREEN.**

**W35's proof: PagerDuty (PD).** Reported 8/27 after the close — revenue $124.4M beat,
ARR through $500M, **and raised** FY revenue guidance to $494M and FY adj EPS to $1.35.
Traded 8/28 **+9.5%, C $13.83, 69% of range, 2.7x volume.** A textbook rung-1 name.
**It appears in none of Friday's three session notes.** Premarket called the board
"empty by measurement" (correct on its inputs — PD hadn't gapped yet); market_open's
overlap tier returned NABL/OSG/BBW, all three correctly killed on catalyst. **PD was
never on the board.** It surfaced only on the post-close weekly scan.

**Mandatory premarket step, ahead of the screeners:**
1. Pull **yesterday's after-hours + this morning's before-open earnings reporters**
   inside the small-cap universe.
2. For each, ask the single rung-1 question: **was guidance RAISED?** Beat-only is a
   hard skip (5-for-5 as a fader).
3. Only the raises go to the full 5-step check. **Then** run the screeners for anything
   the calendar missed.

**Why this is cheap and why it matters:** the screener reports extended-hours quotes as
prices (rule 17a, **eight** straight falsifications), printed `0.0x` RelVol for 17 of 20
names on 8/28, and **returned empty output twice** in one week. **A degraded screener
feeding an "empty board" conclusion is how a real catalyst gets missed** — the earnings
calendar is a source that cannot silently degrade into a blank.

## The filters that actually earn their keep

**1. The dilution / balance-sheet check — run it FIRST.** Rocket's most profitable rule,
one search. Grade the *structure*, not just the existence (lesson 6a): VWAP-discounted
converts are an automatic kill; a completed raise months old is not an overhang at all.

**2. The analyst-ladder check — now 5-for-5 and the best entry filter.** 🥇 **W35 produced
its cleanest demonstration yet: OOMA.** Killed because consensus mean was $23.00 and the
**Street's highest target was $24.00**, below the +15% rung of $25.10. It then **spiked to
$26.19 — straight through the highest target — and closed $23.04, within $0.04 of the
consensus mean.** The ladder did not merely cap the advance; it named the closing price. Strike both profit
targets (+15%, +25%) against a **dated** consensus. If the ladder is capped, skip. CURI was
W33's proof: half-capped by a fresh dated cut, skipped, then **−11.0% and closed at 4% of
range.** ⚠️ **An un-runnable ladder is a FAIL, not a pass** — FF had *no analyst coverage*,
the filter could not run, and it was scored as an absence.

**3. Close-position-in-range — the day-one survival test.** Below the midpoint on heavy
volume = distribution = dead, catalyst regardless. Applies to carry-overs *and* same-day
entries (lesson 4a). **VELO validated it in an unexpected way**: the same-day close at
$15.09 beat Rocket's own trailing stop (which would have filled ≈$14.72 on 8/13's low) by
**$11.10**, even though the stock later recovered to $16.16.

## Entry Framework

**Second-day (the default, and where the record is):**
- Catalyst ran >25% yesterday + closed **above the day's midpoint** → today's open is the entry
- Entry zone: within 10% of prior close (do NOT wait for a 20% pullback that won't come)
- Volume >0.75x avg; a day-2 volume cooldown is normal, not a red flag
- Applies on day 2 AND day 3 if the thesis is intact

**Same-day — now gated, 0-for-3 without these gates:**
- Gap <20%: enter at open or first 10-min base
- Gap 20–35%: enter on the first 10-min consolidation
- Gap >35%: skip today, second-day watchlist
- 🆕 **Opening-range gate**: if the **9:30–9:45 range exceeds 10% of price**, there is no
  tradeable base — **defer to the second day.** (VELO: 22.7% → would have deferred to
  8/13's $14.95 open, now $16.16, **+8.1%**.)
- 🆕 **The 9:45–9:50 bar must close in the upper half of its own range.** OMER's did
  ($17.02/$17.38/$16.92/**$17.33**) — that is what a base looks like.

**Ranking discipline (NEW 2026-08-14):**
- 🚫 **P2 is not a substitute for a failed P1.** If the P1 fails its gate at the open, the
  default is **no satellite**, not the next name down. FF exists only because a slot was
  open, and it was known to be second-tier *before* the entry.

**Pullback (days 2–5):** first red day after a strong move; enter on volume re-emerging
with price holding a key level.

## Attribution Discipline — mandatory in every weekly_review

Rocket's core is IWM; the benchmark is SPY. **Divergence is mostly factor, not skill.**

```
Rocket vs SPY  =  (IWM − SPY) × core weight     ← factor, NOT alpha
                + cash drag                      ← friction, NOT alpha
                + satellite contribution         ← the ONLY real alpha
```

| Week | Factor (IWM−SPY × wt) | Cash drag | Rocket vs SPY | **Real alpha** |
|------|-----------|-----------|---------------|----------------|
| 30 (7/20–7/24) | — (100% cash) | +0.43% | +0.43% | **0.00%** |
| 31 (7/27–7/31) | −1.09% | −0.14% | −0.98% | **0.00%** |
| 32 (8/03–8/07) | +0.05% | **−0.49%** | −0.54% | **−0.13%** |
| 33 (8/10–8/14) | **+0.77%** | −0.04% | +0.15% | **−0.52%** |
| 34 (8/17–8/21) | −0.24% | +0.10% | **+2.03%** | **+2.18%** |
| **35 (8/24–8/28)** | **−1.63%** | −0.04% | **−2.51%** | **−0.85%** |
| **Cumulative** | **−2.14%** | −0.18% | **−1.27%** | **+0.68%** |

⚠️ Columns sum to ≈−1.64% against a measured −1.27%; **residual ≈+0.37%** from arithmetic
sums standing in for geometric chaining over six weeks. **Recorded, not reconciled away.**

**🚨 REDIAGNOSED 2026-08-28 — the problem inverted.** Real alpha is **+0.68% and positive**;
the cumulative deficit is **the core instrument**. Raw **IWM +1.18% vs SPY +3.67% since the
rebase = −2.50%**, carried at ~90% weight. **Rocket's entire shortfall to SPY is now the
IWM-vs-SPY factor, not stock picking.** W33's +0.15% "beat" was 100% factor and this file
said so; **the same honesty applies now that the factor hurts** — W35's −2.51% is 65%
factor and 35% a correct mechanical exit on a *winning* trade. Escalated to the user,
**not self-approved**: Rocket does not get to change its own benchmark sleeve because a
six-week drift went against it.

## Current Rules Under Observation

- 🆕 **32a — only override a trailing stop that is >2% away.** Direct response to ETON.
  Untested; the next end-of-day close decision is the test.
- 🆕 **32c — counterfactuals must cite the stop level and the subsequent low.** Applies
  retroactively: any "would have been worse" claim already in the log is unverified.
- **End-of-day close rule (4/4a) is now 1-for-2** — VELO **+$11.10**, ETON **−$25.83**,
  net **−$14.73**. Close-position-in-range did **not** separate them (both ~11–25% of
  range); **distance-to-stop did.** Watch whether 32a fixes the rule or retires it.
- **Opening-range gate (>10% → defer to day 2)** — still untested against a live entry
- **P2-is-not-a-substitute** — untested since W33
- **7% trailing stop on high-volatility names.** VELO's stop sat inside its noise band.
  Open question: should a name whose opening range exceeds ~15% be skipped outright rather
  than sized around a stop that cannot work?
- No entries after 3:30 PM ET; no pre-earnings entries

## Open Questions

- 🚨 **Does the $2B ceiling cost more than it saves?** Now the most expensive standing rule
  on the book. It capped ETON to a single profit rung on entry, and at **$63.47** it
  **blocks the re-entry** on a name whose beat-and-raise thesis is intact and which just
  closed at a new high. Six names in three weeks — APPS, BW, HLIT, ETON, UMAC, IQMX.
  **Not overridden. Escalation to the user stands and is now urgent.**
- 🚨 **NEW 2026-08-28 — is the IWM core costing more than the mandate-fit is worth?**
  **IWM +1.18% vs SPY +3.67% since the rebase = −2.50% at ~90% weight**, which is the
  **entire** cumulative deficit to the benchmark; stock selection is **+0.68% and
  positive**. CLAUDE.md approved this tradeoff on 2026-07-27 with eyes open, and one of
  the two reasons is **non-negotiable and unaffected by performance**: Bull holds SPY in
  the same pooled account, so a SPY core would make the two books unattributable at the
  broker. Any alternative has to preserve distinct tickers. ⚠️ **Escalated to the user,
  NOT self-approved.** Six weeks is a drift, not a verdict, and lesson 28/34's whole
  point is that Rocket does not get to re-decide its benchmark sleeve because the factor
  recently went against it. **Re-read every weekly review; do not act on it unilaterally.**
- 🔻 **DEMOTED — should lesson-29 binary-risk names be sized at HALF rather than skipped?**
  ARCT was declined (undated Phase 2 readout inside the hold window) and ran +45% at its
  peak. **The bars have now settled it against the request**: 8/28 printed **−6.1% at 50%
  of range on 0.6x volume — the first red day, with volume exhausted from 2.1x to 0.6x
  and the readout still undated.** The gate was right and the cost was transient. Leaving
  the question open at low priority; **the evidence that motivated it has weakened.**
- Second-day vs same-day: **2-for-3** vs 0-for-3, and the one second-day loss was an exit
  failure. Still the working thesis; n is still small.
- What hold time maximizes returns? (1 vs 3 vs 5 days) — n=5 closed trades, still no signal
- Does pre-market volume >5x avg predict intraday continuation?
