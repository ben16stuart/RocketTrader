# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-07-31 (Week 31 review — deployment solved; uptime is the new constraint)

---

## ⚠️ Standing Meta-Problem — REDIAGNOSED 2026-07-31

The problem was framed on 7/24 as "under-deployment caused by a broken idea pipeline."
**Both halves of that diagnosis have now changed.**

**Half 1 — deployment: SOLVED by the core sleeve.** Rocket went from 0 positions /
~100% cash to ~87% invested in IWM on 7/28. Idle cash is no longer an unhedged short
against equity drift. This half is done; do not keep re-litigating it.

**Half 2 — idea flow: NOT the binding constraint anymore.** Week 31 surfaced three
genuine, verifiable catalysts (CSTL beat-and-raise, AMCX $500M Netflix deal + 21% short
float, REPL FDA AdCom 10–3). Ideas were not the problem. **Rocket still traded zero
satellites** — because the premarket routine hit a Claude **session limit**, finished at
10:05 AM ET, and the 9:45–9:50 base window was gone. AMCX then closed at its 52-week
high, above its stated entry trigger.

### The binding constraint is now UPTIME, not ideas.

| Constraint | Status |
|---|---|
| Deployment / idle cash | ✅ Solved (core sleeve, 7/28) |
| Idea flow / scanner | 🟡 Apparently recovered 7/31 — **on probation**, verify one more week |
| **Session-limit / routine uptime** | 🔴 **THE problem.** Cost Rocket the AMCX entry. |
| Midday routine | 🔴 Plist never loaded — has literally never run (see lesson 13) |

**Scanner status change:** after 7 broken sessions it has now run clean **three sessions
running (7/29, 7/31 premarket, 7/31 review)** — sane market caps, real RelVol, correct
company names, and AMCX independently surfacing on two screens. It is **no longer the
highest-leverage fix.** Keep spot-checking it weekly; if it degrades again, reinstate it as
priority 1. Note this does **not** retire lesson 10 — still confirm any entry base against
raw 5-min bars, never a scanner one-liner.

**The bar is not too strict.** Every skip this week was validated by the tape: CSTL
closed *below* its own entry trigger, REPL is a chase into a Monday binary, SOC turned
out to be raising $93M in discounted stock. Discipline is working. **Do not loosen the
chase / dilution / volume rules to manufacture trade count.**

---

## Core Edge

Rocket trades small cap stocks ($50M–$2B market cap, not S&P 500) with identifiable catalysts.
The edge is: most institutional money cannot trade small caps at scale. Individual catalysts
(earnings beats, unusual volume, short squeezes, FDA wins) create outsized price moves that
larger funds cannot exploit. Rocket moves fast and manages tight.

## Catalyst Hierarchy (best to worst — update based on real results)

1. Earnings beat + raised guidance (most reliable, move persists 2-5 days)
2. FDA/regulatory approval (biotech — explosive, binary)
3. Government contract / named funding (defense/drone — multi-day institutional accumulation)
4. Unusual volume + breakout (next day)
5. Short squeeze + catalyst (explosive but unpredictable)
6. Analyst initiation (slower, 1-2 day move)

## Entry Framework

**Same-day entries:**
- Gap <20%: Enter at open or first 10-min base
- Gap 20–35%: Enter on first 10-min consolidation (gap-and-go — this is NOT a chase)
- Gap >35%: Skip today. Add to second-day watchlist.

**Second-day entries (KEY — this is where Rocket makes money):**
- Catalyst ran >25% yesterday + stock closed near highs → today's open is the entry
- Entry zone: within 10% of prior day's close (do NOT wait for a 20%+ pullback that won't come)
- Volume requirement: >0.75x avg (pullbacks naturally have lower volume — that is normal)
- This applies on day 2 AND day 3 if catalyst thesis is still intact

**Pullback entries (days 2-5 after catalyst):**
- Watch for first red day after a strong catalyst move
- Entry: first sign of volume re-emerging + price holding above a key level
- Confirms institutional accumulation, not distribution

## Current Rules Under Observation

- 7% trailing stop (to be tightened or loosened based on results)
- No entries after 3:30 PM ET
- No pre-earnings entries (enter AFTER confirmed beat only)
- Second-day entry rule: added 2026-05-29 after week of missed trades on real catalysts

## Attribution Discipline — mandatory in every weekly_review

Rocket's core is IWM; the benchmark is SPY. **Divergence from SPY is therefore mostly
factor, not skill.** Split it every week before claiming anything:

```
Rocket vs SPY  =  (IWM − SPY) × core weight     ← factor, NOT alpha
                + cash drag                      ← friction, NOT alpha
                + satellite contribution         ← the ONLY real alpha
```

Two weeks of worked examples, both with **zero** satellite exposure:

| Week | IWM − SPY | Rocket vs SPY | Real alpha |
|------|-----------|---------------|------------|
| 30 (7/20–7/24) | — (100% cash) | **+0.43%** | **0.00%** |
| 31 (7/27–7/31) | −1.09% | **−0.98%** | **0.00%** |

Week 30 looked like a win and Week 31 looked like a loss. **Both were zero alpha.** Never
book factor drift as skill — and never book it as failure either.

## Open Questions

- What hold time maximizes returns? (1 day vs 3 day vs 5 day)
- Which sectors produce the most reliable small cap plays?
- Does pre-market volume >5x avg predict intraday continuation?
- How often do second-day entries outperform same-day gap-and-go entries?
