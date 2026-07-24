# Rocket Strategy — Evolving Edge Thesis

Last updated: 2026-07-24 (weekly review — flagged deployment + scanner-pipeline problems)

---

## ⚠️ Standing Meta-Problem — Under-Deployment (flagged 2026-07-24)

Since inception (2026-04-20, ~3 months) Rocket has executed only **2 trades**: MRLN
(+$33.40, closed) and CAMP (closed, exit unrecoverable). That is near-total inaction.
Week of 07-20 → 07-24: **0 trades, flat all 5 sessions.** Every flat call was individually
defensible (no clean fresh catalyst, garbled scanner, tiny pooled account), but the
cumulative result is zero productive output and zero real alpha. Lessons item 7 already
warns "missing real catalysts has a cost too" — yet the pattern persists.

**Root causes to fix, in priority order:**
1. **Idea pipeline is broken.** `smallcap_scanner.py` has been unreliable for 20+ sessions
   (single-letter symbol artifacts, RelVol all dashes, $0.00 prices, glitch % moves). With
   no working screener, idea generation collapses to ad-hoc web search and almost nothing
   clears the bar. **The scanner script is the highest-leverage fix — it should be repaired
   or replaced (a working small-cap gainers/volume feed) before expecting trade volume to
   recover.** Until then, lean harder on Q2 earnings-beat gappers found via web search.
2. **Bar may be too strict for the account size.** With a ~$3k slice, one good catalyst
   trade per week is plenty; the goal isn't more trades, it's *any* real participation.
   Do not loosen the chase/dilution/volume rules — those have saved real losses (ABAT). The
   fix is better idea flow, not looser discipline.

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

## Open Questions

- What hold time maximizes returns? (1 day vs 3 day vs 5 day)
- Which sectors produce the most reliable small cap plays?
- Does pre-market volume >5x avg predict intraday continuation?
- How often do second-day entries outperform same-day gap-and-go entries?
