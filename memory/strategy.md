# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-08-07 (Week 32 review — the constraint is measurement + execution plumbing)

---

## ⚠️ Standing Meta-Problem — REDIAGNOSED 2026-08-07

The diagnosis has moved twice. 7/24: "under-deployment from a broken idea pipeline."
7/31: "uptime." **Both are now stale.**

| Constraint | Status |
|---|---|
| Deployment / idle cash | ✅ **Actually solved 8/07** — see below. It was *not* solved on 7/28. |
| Idea flow / scanner | ✅ Root-caused and fixed 8/07 (`Change` → `Change %` rename) |
| Routine uptime (premarket / open / close) | ✅ Ran on time all five sessions of Week 32 |
| **Midday routine** | 🔴 Has not run since **2026-06-15** (died on a 429). Not loaded. Needs a user decision. |
| **Performance measurement** | 🔴 **NEW — Rocket cannot measure Rocket.** See below. |

### The core sleeve fixed allocation but not deployment

7/28's core sleeve was declared to have solved idle cash. **It did not.** IWM at ~$300
against a ~$3,150 slice makes one whole share **9.6% of the book against a 3% rebalance
band** — unsatisfiable by any whole-share trade. So the rebalance logic correctly declined
to trade, and correctly left **~14% in cash, every session**. Lesson 7a named this on
7/28 and named the fix; it sat open for eight sessions.

**Cost, Week 32 alone: −0.49%** — the single largest component of the week's −0.54% miss,
larger than the factor bet and larger than the only satellite trade.
**Fixed 8/07:** `alpaca_client.py buy/sell` now accept fractional quantities.

> **Never declare a structural problem solved until a live order proves it.** The 7/28
> entry was written the day the sleeve was created, before a single rebalance had been
> attempted against a real band. The first three rebalances all failed, and each one was
> logged as a one-off "share-granularity remainder" rather than as the recurring
> structural defect it was.

### 🔴 Rocket cannot currently measure its own performance

`portfolio_snapshot.py` computes `rocket_return = (0.30 × shared_account_value) /
REBASE_ALLOCATED_VALUE − 1`. Because Rocket's slice is a **fixed 30%** of the shared
account, that expression equals **the whole account's return — Bull's P&L included.**
Bull holds 5 of the 6 live positions.

**Every headline number since the 7/20 merge has been Bull-contaminated.** Week 32 reported
−0.25% vs SPY; hand-built attribution says **−0.54%**. The error flatters Rocket and grows
with Bull's book. **Until this is fixed, trust only the hand-built attribution in the
weekly review, never the snapshot table.** Priority 1 for Week 33.

### The bar is still not too strict

Every skip in Week 32 was validated by the tape — ASPN, EVH, NNBR, MRAM, SVCO, CVRX,
STLN, FIGS and REPL all faded or died. **Do not loosen the chase / dilution / volume rules
to manufacture trade count.** Underperformance this week came from plumbing, not from
being too picky.

---

## Core Edge

Rocket trades small cap stocks ($50M–$2B, not S&P 500) with identifiable catalysts. Most
institutional money cannot trade small caps at scale; individual catalysts create outsized
moves larger funds cannot exploit. Rocket moves fast and manages tight.

## Catalyst Hierarchy (best to worst — updated from real results)

1. **Earnings beat + RAISED guidance** — most reliable, persists 2–5 days. The raise is
   load-bearing: a beat *without* a raise (SVCO) and a beat *with a guide-cut* (CVRX) both
   faded on day one.
2. FDA/regulatory approval (biotech — explosive, binary)
3. Government contract / named funding (defense/drone — multi-day accumulation)
4. Unusual volume + breakout (next day)
5. Short squeeze + catalyst (explosive but unpredictable)
6. Analyst initiation (slower, 1–2 day move)

## The two filters that actually earn their keep

**1. The dilution / balance-sheet check — run it FIRST, before building any thesis.**
Rocket's single most profitable rule, and it costs one search. Week 32 kills: SVCO
(undisclosed $10M convertible on $13.0M cash), STLN (0.1% EBITDA margin, $41.1M cash,
active $15M ATM), NNBR ($3.06 PIPE). Every one traded badly afterwards. RCEL would have
been the fourth (active $200M shelf, <1yr runway) had it not been rejected on volume first.

> **A GAAP-profitable small cap with real operating cash flow is a structurally different
> and much rarer bet than a fast-growing one that still needs the equity market.** Growth
> rate is what makes a stock gap; funding structure decides whether it holds the gap over
> a 1–5 day hold.

**2. Close-position-in-range — NEW, added Week 32.** With a board full of genuine
catalysts, where a stock closed in its daily range separated survivors from corpses better
than catalyst quality did. ASPN (+37.5% → **28%** of range) and EVH (+16.6% → **9%**) both
had real news and both died. QNST (91%), RCEL (86%) and CRSR (92%) held.
**Below the day's midpoint on heavy volume = distribution = dead, catalyst regardless.**
Validating the catalyst is no longer the hard part; surviving day one is.

## Entry Framework

**Same-day:**
- Gap <20%: enter at open or first 10-min base
- Gap 20–35%: enter on the first 10-min consolidation (gap-and-go — NOT a chase)
- Gap >35%: skip today, add to the second-day watchlist

**Second-day (KEY — where Rocket makes money):**
- Catalyst ran >25% yesterday + closed **above the day's midpoint** → today's open is the entry
- Entry zone: within 10% of prior close (do NOT wait for a 20% pullback that won't come)
- Volume: >0.75x avg (pullbacks are naturally lighter — that is normal)
- Applies on day 2 AND day 3 if the thesis is intact

**Pullback (days 2–5):** first red day after a strong move; enter on volume re-emerging
with price holding a key level.

**Analyst targets are stale on a print day.** A breached mean target is a prompt to check
for revisions, **not** a disqualification. Rocket treated the pre-print $19.00 consensus as
a hard ceiling on QNST and passed at $20.21; it closed $21.08 at 91% of range.

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
| 31 (7/27–7/31) | −1.09% | — | −0.98% | **0.00%** |
| 32 (8/03–8/07) | **+0.05%** | **−0.49%** | −0.54% | **−0.13%** |

Week 30 looked like a win, Week 31 like a loss; both were zero alpha. **Week 32 is the
first week with any real alpha at all, and it was slightly negative.** Note that the
factor excuse was unavailable in Week 32 — IWM and SPY finished within 5bp — which is
precisely what exposed the cash drag.

## Current Rules Under Observation

- 7% trailing stop — CSTL round-tripped through it after a +5.8% high; working as designed
- No entries after 3:30 PM ET
- No pre-earnings entries (enter AFTER a confirmed beat only)
- Second-day entry rule (added 2026-05-29)
- **Fractional core rebalancing — untested against a live order.** Confirm the first fill.

## Open Questions

- What hold time maximizes returns? (1 vs 3 vs 5 days) — still n=3 closed trades, no signal
- Which sectors produce the most reliable small cap plays? (healthcare was Week 32's worst)
- Does pre-market volume >5x avg predict intraday continuation?
- How often do second-day entries outperform same-day gap-and-go entries?
