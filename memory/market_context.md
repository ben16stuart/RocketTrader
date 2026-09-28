# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-28 Monday premarket (Week 40 day 1 — **floor breached 7 sessions; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Fri 2026-09-25 settled closes** (10Y, SPY, IWM, VIX, futures prior legs).
LIVE = forming bar, indicative only (never record as a close).

| Metric | Level | Read |
|---|---|---|
| **VIX** | 14.87 close 9/25 → **16.31 LIVE (+9.7%)** | Rising off the low, still far below the 22 brake. No size restriction |
| **10-yr** | **5.18% close 9/25** (5.16% 9/24) | Above the 4.75% trigger. A standing level flag, not a new event (34) |
| **FUTURES** | ES **−0.55%** · NQ **−1.05%** · RTY **−0.70%** LIVE | Broad risk-off open, led by tech. Russell weaker than ES. One session = no information (28) |
| **Brent / WTI** | 100.90 (+3.55%) / 96.23 (+4.13%) LIVE | 🔄 Brent ROLLED to BZZ26; **naive −3.28% → true +3.55%, SIGN FLIP**. The tool caught it (50). Brent is back above $100 |
| Gold / Dollar | 4,189 (**−3.05%** LIVE) / 101.13 (+0.16%) | Sharp gold drop, per web reports rotation out of metals into energy/staples |
| **SPY / IWM** | **771.35 / 281.97** closes 9/25 (+0.54% / +0.11%) | IWM indicated ~−0.6% premarket |

**Rule 29:** blocks nothing today. There are no Fed or CPI events in today's search. **MU reports 9/29 AMC**
(semis bellwether: tape risk for Tuesday, not a Rocket name). An oil spike plus tech weakness is
a mild headwind for small-cap growth. There is no macro reason to stand down and none to size up.

**Binding constraint today (53a): board quality / catalyst supply.** Not stop fit, not mandate.
Funnel: 5 sources, ~30 names screened, 11 run through eligibility, 5 survived the gates, **0 survived the
catalyst check.** Details are in the research_log W40-Mon section.

### Instrument health
- ⚠️ **Scanner Change %/price is broken again (17/64).** ACCO printed +8.2% @ $4.66; eligibility
  and web quotes say $4.31. AMPX printed +6.7% @ $10.40; the real 9/25 close was $9.75 (+0.6%).
  RelVol is <1.0× on 18/20 `unusual_volume` rows. Names only.
- ✅ `eligibility` returned 8/8, then 2/2 rows (43 ✓). ✅ `macro` complete, roll corrected.
- ✅ Nasdaq earnings API reachable (21 rows on 9/28, 12 on 9/25).
