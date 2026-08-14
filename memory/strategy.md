# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-08-14 (Week 33 review — **the constraint has moved from allocation to
entry timing**)

---

## ⚠️ Standing Meta-Problem — REDIAGNOSED 2026-08-14

| Constraint | Status |
|---|---|
| Deployment / idle cash | ✅ **Solved and proven.** Cash drag −0.49% (W32) → **−0.04%** (W33) |
| Fractional core rebalancing | ✅ Three live rebalances, all within $0.20 of target |
| Idea flow / scanner | ✅ Fixed 8/07 |
| Research quality | ✅ **Now a strength** — 4/4 skips validated in W33, ladder filter 4-for-4 |
| **Entry timing (which DAY)** | 🔴 **NEW — this is the binding constraint.** See below. |
| **Performance measurement** | 🔴 Error grew 67bp → **88bp**. Priority 1. |
| **Routine completion (monitors / midday)** | 🔴 Cost ≈−0.70% in W33 alone |

### 🥇 The binding constraint: Rocket enters on the wrong day

| Entry type | Trades | Result |
|---|---|---|
| **Same-day** (day one of the gap) | CSTL, FF, VELO | **0 for 3** |
| **Second-day continuation** | MRLN, OMER (open, green) | **2 for 2** |

Both same-day losses failed the *same* way: Rocket bought the retrace of a failed opening
spike and called it a base. VELO travelled **22.7% in fifteen minutes** before the "9:45
base" formed at $15.27 — that was not a base, it was the middle of a range. On a name that
volatile, a 7% trailing stop sits **inside the noise band** and is a coin flip, not risk
management.

> This document has asserted since May that second-day is *"where Rocket makes money."*
> **Week 33 is the first week it was tested against a same-day control group, and it held.**

### Research is no longer what loses money — execution is

Week 33's three losses ranked by cost:
1. **≈−0.70%** — OMER never evaluated on 8/13 (monitor died silently). Infrastructure.
2. **−0.39%** — FF, a P2 promoted only because the P1 failed and a slot was open. Discipline.
3. **−0.17%** — VELO, correct research, wrong entry day. Timing.

**None of it was bad analysis. Do not loosen the research bar to fix an execution problem.**

### 🔴 Rocket still cannot measure Rocket — and the error is growing

`portfolio_snapshot.py` derives Rocket's return from a fixed 30% of the *shared* account,
which is algebraically the whole account's return with Bull's P&L included. Snapshot reads
**+0.10% vs SPY since rebase; the true hand-built figure is −0.78%.** The gap was 67bp last
week and is **88bp** now.

⚠️ **New this week (lesson 26):** the *daily* session notes drifted back onto the
contaminated slice as their base, so they reported +0.09%→+0.53% all week. **The
hand-built book, not the slice, is the only valid daily base.**

---

## Core Edge

Rocket trades small cap stocks ($50M–$2B, not S&P 500) with identifiable catalysts. Most
institutional money cannot trade small caps at scale; individual catalysts create outsized
moves larger funds cannot exploit. Rocket moves fast and manages tight.

## Catalyst Hierarchy (best to worst — updated from real results)

1. **Earnings beat + RAISED guidance, on the SECOND day.** The raise is load-bearing and
   the day is load-bearing. Everything below assumes both.
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

- **Opening-range gate (>10% → defer to day 2)** — new, untested against a live entry
- **P2-is-not-a-substitute** — new
- **7% trailing stop on high-volatility names.** VELO's stop sat inside its noise band.
  Open question: should a name whose opening range exceeds ~15% be skipped outright rather
  than sized around a stop that cannot work?
- No entries after 3:30 PM ET; no pre-earnings entries

## Open Questions

- **Does the $2B ceiling cost more than it saves?** Five names in two weeks were killed or
  capped by it — APPS, BW, HLIT, ETON, UMAC — several the strongest catalyst of their day.
  **Not overridden. Escalated to the user.**
- Second-day vs same-day: 2-for-2 vs 0-for-3. Needs more n, but is now the working thesis.
- What hold time maximizes returns? (1 vs 3 vs 5 days) — n=5 closed trades, still no signal
- Does pre-market volume >5x avg predict intraday continuation?
