# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-10-07 Wednesday premarket (Week 41 day 3 — **floor breached 12 closes; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Tue 2026-10-06 settled closes**. LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.01 close 10/06** → 15.50 LIVE | Calm, far below the 22 brake. No size restriction |
| **10-yr** | **5.27% close 10/06** (5.31% 10/05) | First down day after three up. Standing flag (34) |
| **FUTURES** | ES −0.13% · NQ −0.42% · **RTY −0.48%** LIVE | Soft, small caps leading lower. Not a signal alone (28) |
| **Brent / WTI** | **100.58 / 89.44 close 10/06** (+1.4% / +0.7% LIVE) | Back above $100; Hormuz headlines |
| Gold / Dollar | 4,187.10 / 101.83 close 10/06 | Gold −1.1% LIVE, dollar firmer |
| **SPY / IWM** | **779.09 / 281.34 close 10/06** (+0.55% / −0.72%) | Small caps lagging large caps by 1.3 pts |

**Rule 29 / event risk today:** **FOMC minutes (Sept 15–16 meeting) 2:00 PM ET.** No name-level binary on the board.
**Binding constraint (53a): board quality.** The real catalysts overnight (NEOG, PENG, NLST) were all above $2B.

### Instrument health
- ✅ `eligibility` 7/7 rows (43 ✓). ✅ `macro` complete.
- ✅ **Alpaca news API (`data.alpaca.markets/v1beta1/news`) works and carries Benzinga headlines + full content** —
  this restores the initiation/mover source that the Benzinga site (403) lost. Use it as rung 3 going forward.
- ⚠️ Scanner (04:20 ET) Change % wrong vs settled bars for every checked mover (17). `breakouts` Finviz query empty (64, 7th session).
- ⚠️ Web search for dated FDA/initiation items returns nothing dated (thin source, 41b).
