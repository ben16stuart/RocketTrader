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

## The filters that actually earn their keep

**1. The dilution / balance-sheet check — run it FIRST.** Rocket's most profitable rule,
one search. Grade the *structure*, not just the existence (lesson 6a): VWAP-discounted
converts are an automatic kill; a completed raise months old is not an overhang at all.

**2. The analyst-ladder check — now 4-for-4 and the best entry filter.** Strike both profit
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

| Week | IWM − SPY | Cash drag | Rocket vs SPY | **Real alpha** |
|------|-----------|-----------|---------------|----------------|
| 30 (7/20–7/24) | — (100% cash) | — | +0.43% | **0.00%** |
| 31 (7/27–7/31) | −1.09% | −0.14% | −0.98% | **0.00%** |
| 32 (8/03–8/07) | +0.05% | **−0.49%** | −0.54% | **−0.13%** |
| 33 (8/10–8/14) | **+0.77%** | −0.04% | **+0.15%** | **−0.52%** |
| **Cumulative** | | | **−0.78%** | **−0.65%** |

**Week 33's +0.15% headline is 100% factor.** Weeks 30 and 33 both "beat" SPY on beta;
Week 31 "lost" on the same beta. **Cash drag is solved. Real alpha is now the only thing
left to fix, and it has never been positive.**

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
- 🆕 **Should lesson-29 binary-risk names be sized at HALF rather than skipped?** ARCT was
  correctly declined (undated Phase 2 readout inside the hold window) and ran **+31%**. The
  gate is right — a 7% stop cannot protect against a data gap — but the rule currently
  forces all-or-nothing at full 15% size. A deliberate half-size sleeve would have captured
  ~+2.3% of book with the gap risk explicitly bounded. ⚠️ **Escalated to the user, NOT
  self-approved** — lesson 35 pre-committed against loosening a calendar gate because price
  went the other way, and that pre-commitment is being honoured.
- Second-day vs same-day: **2-for-3** vs 0-for-3, and the one second-day loss was an exit
  failure. Still the working thesis; n is still small.
- What hold time maximizes returns? (1 vs 3 vs 5 days) — n=5 closed trades, still no signal
- Does pre-market volume >5x avg predict intraday continuation?
