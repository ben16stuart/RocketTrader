# Portfolio State

**Last Updated**: 2026-11-18 17:15 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,518.69 |
| Rocket's Allocated Slice (30%) | $2,855.61 |
| Cash Available (shared, pooled) | $928.76 |
| Total Invested (both agents) | $8,589.93 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **+$44 (+1.53%)** vs IWM +0.62% · daily loss cap $143: OK |
| **Rocket own book since 7/20** | **+0.01%** vs IWM -7.38% → **+7.40 pts** |
| **Rocket own book since 10/6 (new rules)** | **+3.13%** vs IWM -3.77% → **+6.90 pts** |
| **Rocket own book this week** | **-0.73%** vs IWM -2.45% → **+1.73 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.81% |
| IWM return since rebase | -7.12% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.31% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 93.3% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 6.7% | buffer only (<= 10%) |

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
| AMPL | 20 ($338) | $17.15 | $16.89 | $16.97 | $-5.20 | -1.5% |
| CAKE | 3 ($352) | $117.25 | $117.28 | $111.96 | $+0.07 | +0.0% |
| CBRL | 5 ($369) | $67.16 | $73.71 | $69.57 | $+32.75 | +9.8% |
| CDNA | 4 ($295) | $86.10 | $73.81 | $74.56 | $-49.16 | -14.3% |
| CVX | 4 ($828) | $210.70 | $207.05 | $216.13 | $-14.60 | -1.7% |
| GTLB | 6 ($267) | $56.75 | $44.49 | $44.58 | $-73.53 | -21.6% |
| HUM | 1 ($406) | $458.76 | $405.69 | $443.34 | $-53.07 | -11.6% |
| IOVA | 44 ($328) | $7.70 | $7.45 | $7.53 | $-10.87 | -3.2% |
| JNJ | 3 ($830) | $277.80 | $276.65 | $278.70 | $-3.44 | -0.4% |
| MRK | 5 ($698) | $148.46 | $139.66 | $143.37 | $-43.99 | -5.9% |
| PANW | 2 ($659) | $318.08 | $329.63 | $309.29 | $+23.10 | +3.6% |
| PAYS | 37 ($375) | $9.38 | $10.14 | $9.81 | $+28.30 | +8.2% |
| SPY | 0.026 ($19) | $756.33 | $729.90 | $732.44 | $-0.69 | -3.5% |
| STT | 5 ($831) | $165.11 | $166.25 | $167.29 | $+5.72 | +0.7% |
| TGT | 5 ($845) | $152.86 | $169.06 | $159.53 | $+81.00 | +10.6% |
| TXG | 6 ($341) | $55.86 | $56.84 | $56.30 | $+5.88 | +1.8% |
| XOM | 5 ($808) | $164.24 | $161.65 | $167.21 | $-12.95 | -1.6% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($338), CAKE ($352), CBRL ($369), CDNA ($295), GTLB ($267), IOVA ($328), PAYS ($375), TXG ($341)
- **Bull's positions** (8): CVX ($828), HUM ($406), JNJ ($830), MRK ($698), PANW ($659), SPY ($19), TGT ($845), XOM ($808)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($831) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 39ae6bab… | CBRL | sell | 5 | trailing_stop | new |
| 66b0d7ff… | PAYS | sell | 37 | trailing_stop | new |
| f2eb8105… | IOVA | sell | 44 | trailing_stop | new |
| ab2f8825… | TXG | sell | 6 | trailing_stop | new |
| 32cc556a… | HUM | sell | 1 | trailing_stop | new |
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
