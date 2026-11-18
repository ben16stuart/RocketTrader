# Portfolio State

**Last Updated**: 2026-11-18 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,491.98 |
| Rocket's Allocated Slice (30%) | $2,847.59 |
| Cash Available (shared, pooled) | $833.12 |
| Total Invested (both agents) | $8,658.86 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **+$57 (+1.98%)** vs IWM +0.39% · daily loss cap $142: OK |
| **Rocket own book since 7/20** | **+0.46%** vs IWM -7.60% → **+8.06 pts** |
| **Rocket own book since 10/6 (new rules)** | **+3.59%** vs IWM -4.00% → **+7.59 pts** |
| **Rocket own book this week** | **-0.28%** vs IWM -2.68% → **+2.40 pts** |
| Rocket return since rebase (SHARED account, not own book) | -6.07% |
| IWM return since rebase | -7.34% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.27% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 94.0% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 6.0% | buffer only (<= 10%) |

✅ **Satellite floor met.**

**Rebase Date**: 2026-07-20 (account merged with Bull — prior standalone
history since 2026-04-20 is preserved in memory/weekly_reviews/)

⚠️ **Cash and buying power above are POOLED with Bull.** Before sizing any
trade, check actual available cash — do not assume the full allocated slice
is available if Bull has open positions consuming shared cash.

---

## Open Positions (shared account — yours AND Bull's)

Ownership is reconciled below — do not re-derive it from the trade log.

| Symbol | Shares | Entry Price | Price (LIVE, session open) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| AMPL | 20 ($338) | $17.15 | $16.91 | $16.97 | $-4.70 | -1.4% |
| CAKE | 3 ($361) | $117.25 | $120.18 | $111.96 | $+8.79 | +2.5% |
| CBRL | 5 ($372) | $67.16 | $74.36 | $69.57 | $+36.00 | +10.7% |
| CDNA | 4 ($298) | $86.10 | $74.47 | $74.56 | $-46.52 | -13.5% |
| CVX | 4 ($823) | $210.70 | $205.84 | $216.13 | $-19.46 | -2.3% |
| GTLB | 6 ($267) | $56.75 | $44.44 | $44.58 | $-73.86 | -21.7% |
| IOVA | 44 ($329) | $7.70 | $7.47 | $7.53 | $-9.77 | -2.9% |
| JNJ | 3 ($819) | $277.80 | $273.06 | $278.70 | $-14.22 | -1.7% |
| MRK | 5 ($689) | $148.46 | $137.88 | $143.37 | $-52.89 | -7.1% |
| PANW | 2 ($679) | $318.08 | $339.66 | $309.29 | $+43.16 | +6.8% |
| PAYS | 37 ($371) | $9.38 | $10.03 | $9.81 | $+24.05 | +6.9% |
| SPY | 0.695 ($508) | $731.83 | $730.46 | $732.44 | $-0.95 | -0.2% |
| STT | 5 ($827) | $165.11 | $165.49 | $167.29 | $+1.90 | +0.2% |
| TGT | 5 ($831) | $152.86 | $166.26 | $159.53 | $+67.00 | +8.8% |
| TXG | 6 ($343) | $55.86 | $57.09 | $56.30 | $+7.38 | +2.2% |
| XOM | 5 ($804) | $164.24 | $160.78 | $167.21 | $-17.32 | -2.1% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($338), CAKE ($361), CBRL ($372), CDNA ($298), GTLB ($267), IOVA ($329), PAYS ($371), TXG ($343)
- **Bull's positions** (7): CVX ($823), JNJ ($819), MRK ($689), PANW ($679), SPY ($508), TGT ($831), XOM ($804)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($827) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 39ae6bab… | CBRL | sell | 5 | trailing_stop | new |
| 66b0d7ff… | PAYS | sell | 37 | trailing_stop | new |
| f2eb8105… | IOVA | sell | 44 | trailing_stop | new |
| ab2f8825… | TXG | sell | 6 | trailing_stop | new |
| 9bc10b9b… | AMPL | sell | 20 | trailing_stop | new |
| 402787f0… | XOM | sell | 5 | trailing_stop | new |
| bc4c3fd4… | CVX | sell | 4 | trailing_stop | new |
| dea7e594… | JNJ | sell | 3 | trailing_stop | new |
| a5a7524a… | PANW | sell | 2 | trailing_stop | new |
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
