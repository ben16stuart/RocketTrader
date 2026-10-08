# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-10-08 Thursday premarket (Week 41 day 4 — **floor breached 13 closes; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Wed 2026-10-07 settled closes** (10Y row is 10/07 close). LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.08 close 10/07** → 15.72 LIVE | Calm, far below the 22 brake. No size restriction |
| **10-yr** | **5.28% close 10/07** (5.27% 10/06) | Yields "hitting new highs" in headlines. Standing flag (34) |
| **FUTURES** | ES −0.41% · NQ −0.59% · **RTY −0.84%** LIVE | Small caps leading lower for a second day. Not a signal alone (28) |
| **Brent / WTI** | **100.20 / 88.28 close 10/07** (+4.3% / +4.2% LIVE) | Pentagon reportedly readying Iran strikes; Hormuz shipping attacks |
| Gold / Dollar | 4,140.70 / 102.24 close 10/07 | Flat / dollar firmer |
| **SPY / IWM** | **777.22 / 277.70 close 10/07** (−0.24% / −1.29%) | Small caps lagging large caps by 1.05 pts again |

**Rule 29 / event risk today:** no FOMC. Fed speakers Barkin + Bowman 8:30, Schmid 11:30, Daly 1:00 PM ET;
EIA nat gas 10:00. **Geopolitical:** Iran-strike headlines can whipsaw oil and the tape intraday.
**Binding constraint (53a): board quality.** The one real overnight catalyst (WOLF) sits at the $2B ceiling (13).

### Instrument health
- ✅ `eligibility` 16/16 rows (43 ✓). ✅ `macro` complete. ✅ Nasdaq earnings calendar API works.
- ✅ Alpaca news API works. **Gotcha:** responses can carry raw control chars, so parse with `json.loads(..., strict=False)`.
- ⚠️ Scanner (04:20 ET) Change % reflects AH prints for some names (WOLF real), stale for others (17). Name source only.
