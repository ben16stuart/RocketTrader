# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-10-01 Thursday premarket (Week 40 day 4 — **floor breached 8 closes; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Wed 2026-09-30 settled closes** (10-yr too). LIVE = indicative only.

| Metric | Level | Read |
|---|---|---|
| **VIX** | **16.34 close 9/30** → 16.76 LIVE | Up a touch, far below the 22 brake. No size restriction |
| **10-yr** | **5.29% close 9/30** (5.26% 9/29) | New grind higher; "global bond rout" headlines (gilts 6%). Standing flag (34) |
| **FUTURES** | ES +0.11% · NQ +0.39% · **RTY −0.17%** LIVE | Small caps lagging large again; rates are the headwind. Not a signal alone (28) |
| **Brent / WTI** | **98.03 / 90.42 close 9/30** (LIVE 100.44 / 92.19) | 🔄 Brent roll caught (naive −2.98% → true +2.46%, sign flip, 50). Brent testing $100 |
| Gold / Dollar | 4,186.70 / 101.45 close 9/30 | Dollar +0.5% LIVE (bond-rout bid) |
| **SPY / IWM** | **762.63 / 277.89 close 9/30** (−0.21% / −0.40%) | IWM lagged SPY a 3rd straight day |

**Rule 29 / event risk today:** not FOMC. **Jobless claims + Challenger 8:30, ISM Manufacturing 10:00 (55 exp.)**,
construction spending, and a heavy Fed-speaker slate (Waller, Williams, Logan, Bowman, Cook +4). The 10:00 ISM
lands *after* the 9:45–9:50 entry bar — a hot print with the 10-yr at 5.29% is the main intraday whipsaw risk
for small caps. Name-level: **GLUE data call 8:00 AM** (board, day 1). Nike AMC tonight (not in universe).
**Binding constraint (53a): board quality** — the dated 9/30 catalysts mostly hit out-of-universe names.

### Instrument health
- ✅ `eligibility` 13/13 rows (43 ✓). ✅ `macro` complete, Brent roll corrected.
- ⚠️ Scanner ran 04:20 ET; Change %/price fields = **premarket vs 9/30 close** (17). `breakouts` Finviz main
  query "No results" again (1 fallback row, ACRS) — 3rd session running (64).
- ✅ Nasdaq earnings API (17 rows 9/30, 16 rows 10/01). ✅ EDGAR submissions + full-text search OK.
- ✅ Alpaca `/v2/orders` read live stops (AGEN $9.5883, RARE $14.4336).
