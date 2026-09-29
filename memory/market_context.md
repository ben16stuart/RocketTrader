# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-29 Tuesday premarket (Week 40 day 2 — **floor breached 6 closes; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Mon 2026-09-28 settled closes** except where noted. LIVE = indicative only.

| Metric | Level | Read |
|---|---|---|
| **VIX** | **16.07 close 9/28** → 16.13 LIVE | Flat. Far below the 22 brake. No size restriction |
| **10-yr** | **5.24% close 9/28** (5.18% 9/25) | Still above the 4.75% trigger and rising. Standing flag (34) |
| **FUTURES** | ES −0.01% · NQ +0.14% · **RTY −0.06%** LIVE | Flat open after Monday's risk-off. No information (28) |
| **Brent / WTI** | **97.83 / 92.60 close 9/28** (LIVE 97.29 / 92.20) | 🔄 Brent roll corrected by the tool (naive −7.59% → true −0.55%, 50). Back under $100 |
| Gold / Dollar | 4,168 / 101.20 close 9/28 | Quiet |
| **SPY / IWM** | **765.61 / 280.02 close 9/28** (−0.74% / −0.69%) | Small caps in line with large on Monday's dip |

**Rule 29:** no Fed/CPI blocker found. **MU reports tonight (9/29 AMC)** — semis tape risk for Wed.
CNXC also tonight (ceiling-bound, track only). Name-level binary: QTTB EADV data 9/30.
**Binding constraint (53a): board quality.** ~45 names → 12 eligibility → 8 in universe → 2 catalysts
(AGEN, QTTB) → 1 enterable today (AGEN).

### Instrument health
- ✅ `eligibility` 12/12 rows (43 ✓). ✅ `macro` complete, Brent roll corrected.
- ⚠️ Scanner ran at 04:20 ET on Monday data; RelVol ≤1.0× on every `unusual_volume` row and
  `breakouts` Finviz returned "No results" on one query (17/64). Names only.
- ⚠️ yfinance `totalCash` for AGEN ($18.7M) predates the July $85M PIPE — stale field, don't size off it.
- ✅ Nasdaq earnings API reachable (19 rows 9/28, 18 rows 9/29).

## Instrument health
- ⚠️ **Scanner Change %/price is broken again (17/64).** ACCO printed +8.2% @ $4.66; eligibility
  and web quotes say $4.31. AMPX printed +6.7% @ $10.40; the real 9/25 close was $9.75 (+0.6%).
  RelVol is <1.0× on 18/20 `unusual_volume` rows. Names only.
- ✅ `eligibility` returned 8/8, then 2/2 rows (43 ✓). ✅ `macro` complete, roll corrected.
- ✅ Nasdaq earnings API reachable (21 rows on 9/28, 12 on 9/25).
