# Portfolio State

**Last Updated**: 2026-11-17 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,511.87 |
| Rocket's Allocated Slice (30%) | $2,853.56 |
| Cash Available (shared, pooled) | $928.76 |
| Total Invested (both agents) | $8,583.11 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **+$2 (+0.07%)** vs IWM -1.50% · daily loss cap $143: OK |
| **Rocket own book since 7/20** | **-1.51%** vs IWM -8.03% → **+6.52 pts** |
| **Rocket own book since 10/6 (new rules)** | **+1.56%** vs IWM -4.44% → **+6.00 pts** |
| **Rocket own book this week** | **-2.24%** vs IWM -3.13% → **+0.89 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.88% |
| IWM return since rebase | -7.78% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.90% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 91.8% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 8.2% | buffer only (<= 10%) |

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
| AMPL | 20 ($339) | $17.15 | $16.96 | $17.77 | $-3.80 | -1.1% |
| CAKE | 3 ($336) | $117.25 | $112.08 | $109.73 | $-15.53 | -4.4% |
| CBRL | 5 ($349) | $67.16 | $69.72 | $67.98 | $+12.78 | +3.8% |
| CDNA | 4 ($299) | $86.10 | $74.63 | $73.72 | $-45.88 | -13.3% |
| CVX | 4 ($865) | $210.70 | $216.22 | $217.14 | $+22.06 | +2.6% |
| GTLB | 6 ($268) | $56.75 | $44.59 | $47.33 | $-72.96 | -21.4% |
| HUM | 1 ($443) | $458.76 | $443.13 | $461.25 | $-15.63 | -3.4% |
| IOVA | 44 ($330) | $7.70 | $7.50 | $7.55 | $-8.67 | -2.6% |
| JNJ | 3 ($835) | $277.80 | $278.38 | $282.55 | $+1.74 | +0.2% |
| MRK | 5 ($715) | $148.46 | $143.05 | $144.46 | $-27.04 | -3.6% |
| PANW | 2 ($618) | $318.08 | $308.91 | $316.09 | $-18.34 | -2.9% |
| PAYS | 37 ($362) | $9.38 | $9.79 | $9.54 | $+15.36 | +4.4% |
| SPY | 0.026 ($19) | $756.33 | $730.90 | $739.95 | $-0.66 | -3.4% |
| STT | 5 ($836) | $165.11 | $167.25 | $170.03 | $+10.68 | +1.3% |
| TGT | 5 ($796) | $152.86 | $159.10 | $160.32 | $+31.20 | +4.1% |
| TXG | 6 ($338) | $55.86 | $56.36 | $54.99 | $+3.00 | +0.9% |
| XOM | 5 ($836) | $164.24 | $167.11 | $166.87 | $+14.35 | +1.7% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($339), CAKE ($336), CBRL ($349), CDNA ($299), GTLB ($268), IOVA ($330), PAYS ($362), TXG ($338)
- **Bull's positions** (8): CVX ($865), HUM ($443), JNJ ($835), MRK ($715), PANW ($618), SPY ($19), TGT ($796), XOM ($836)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($836) — do not size against this until ownership is resolved.


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
