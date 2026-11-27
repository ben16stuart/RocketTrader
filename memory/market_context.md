# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-11-20 Friday CLOSE (written at W47 review, Sat 11/21)  ← CURRENT

All figures are **Fri 2026-11-20 settled closes** (`market_data.py macro`). Prior closes are 11/19.

| Metric | Level | Read |
|---|---|---|
| **VIX** | **35.89** (+26% from 28.44) | **Above the 30 no-new-longs line.** 19.30 → 35.89 over the week |
| **10-yr** | **4.91%** (−14bp) | Off the 5.15% cycle high (11/13), a flight-to-quality bid |
| **Futures** | ES −3.64% · NQ −5.54% · RTY −2.85% | Growth/AI led the selling. Small caps fell less |
| **Brent / WTI** | **92.57 / 83.98** | Flat-ish for the week (95.84 → 92.57) |
| Gold / Dollar | 3,515.40 / 103.81 | Gold −9.5% on the week (3,886 → 3,515). Liquidation, not a haven bid |
| **SPY / IWM** | **689.81 / 256.61** (−3.64% / −2.88%) | **Week: IWM −7.54% (277.54 → 256.61), SPY −8.56% (754.37 → 689.81)** |

**Week's shape:** a straight risk-off week. Monday through Thursday ground IWM down (272.94 → 264.22). The post-NVDA bounce (Thu premarket NQ +2.35%) reversed into a sell-off, and Friday was the capitulation-style leg (VIX 35.89, gold −4.6% in a day).
Rocket's book (−5.80%) fell less than IWM. This is **not a bearish-cash thesis**: the rule is reduced size or no new longs while VIX is elevated, never raising cash.
**Live constraint for Monday:** **VIX > 30 = no new longs.** The PAYS rank-decay exit still happens, and its proceeds go to IWM. See research_log W48.

**Week 48 calendar:** Thanksgiving Thu 11/26 (closed), Fri 11/27 half day (1:00 PM ET close). Held names: no prints in the gate. CBRL earnings 12/02 or 12/09 (confirm). Macro: check at premarket.

**Mon 11/23 premarket (LIVE, not closes):** VIX 29.67 (−17% vs 35.89), RTY +2.37%, ES +2.92%, NQ +3.61%, gold 3,621 (+3.0%), Brent 88.58 / WTI 82.29 (roll-corrected −1.5% / −1.3%). A relief bounce is forming. **VIX is in the 25–30 band → half size** for any new long if it holds there at the open.

**Mon 11/23 CLOSES:** VIX 26.62, IWM 265.74 (+3.56%), SPY 722.29 (+4.71%), 10-yr 4.91% (11/20) → 4.92% (11/23). The relief bounce held.
**Tue 11/24 premarket (LIVE):** VIX 28.58 (+7.4%), RTY −0.43%, ES −0.90%, NQ −1.79%, gold 3,623 (−0.8%), Brent 86.83 / WTI 79.94 (Brent roll-corrected). Growth is giving some of it back. **Still in the 25–30 band → half size.** Data: Conference Board consumer confidence 10:00 ET.

**Tue 11/24 CLOSES:** VIX 26.36, IWM 267.14 (+0.53%), SPY 718.78 (−0.49%), 10-yr 4.90%. Small caps beat large caps again.
**Wed 11/25 premarket (LIVE):** VIX 29.23 (+10.9%), RTY −0.93%, ES −1.51%, NQ −2.42%, gold 3,556.5 (−0.96%, roll-corrected), Brent 88.07 / WTI 81.33 (Brent roll-corrected −0.8%), DXY 104.02. Growth/AI is leading the selling again, and RTY is falling less. **Still in the 25–30 band → half size.** Data at 8:30 ET: Q3 GDP second estimate, October PCE / personal income, jobless claims (moved up for the holiday). New home sales at 10:00. Pre-holiday thin tape, then Thanksgiving (closed) Thursday and a 1:00 PM close Friday.

**Wed 11/25 CLOSES:** VIX 28.29, IWM 268.87 (+0.65%), SPY 716.70 (−0.29%), 10-yr 4.85% (−5bp). Small caps beat large caps for the 3rd day running.
**Thu 11/26 (Thanksgiving, cash market closed) Globex LIVE:** VIX 27.36, RTY +0.28%, ES +0.41%, NQ +0.27%, gold 3,591 (+0.75%, roll-corrected), Brent 91.06 (+0.46%; the naive −3.75% is a roll artifact, sign flip) / WTI 84.44, DXY 103.76. Quiet holiday tape. **Still in the 25–30 band → half size.** Fri 11/27: 1:00 PM ET close, no major data.
**Fri 11/27 premarket (LIVE, half day, 1:00 PM ET close):** VIX 24.93 (−7.0% vs 26.80), **under 25 → full size** if it holds at the open. RTY +1.49%, ES +1.79%, NQ +2.45% vs the 11/25 closes. Gold 3,704.7 (+3.93%, roll-corrected to GCG27), Brent 92.01 (+1.51%; the naive −2.75% is a roll sign flip) / WTI 85.26, DXY 103.81. Last cash closes are still 11/25: IWM 268.87, SPY 716.70, 10-yr 4.85%. A post-holiday risk-on gap is forming into a thin half session.
