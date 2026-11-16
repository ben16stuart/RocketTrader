# Portfolio State

**Last Updated**: 2026-11-16 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,584.54 |
| Rocket's Allocated Slice (30%) | $2,875.36 |
| Cash Available (shared, pooled) | $928.82 |
| Total Invested (both agents) | $8,655.72 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$69 (-2.35%)** vs IWM -1.75% · daily loss cap $144: OK |
| **Rocket own book since 7/20** | **-1.63%** vs IWM -6.72% → **+5.09 pts** |
| **Rocket own book since 10/6 (new rules)** | **+1.44%** vs IWM -3.08% → **+4.52 pts** |
| **Rocket own book this week** | **-2.35%** vs IWM -1.75% → **-0.60 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.16% |
| IWM return since rebase | -6.46% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.30% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 91.0% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 9.0% | buffer only (<= 10%) |

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
| AMPL | 20 ($355) | $17.15 | $17.75 | $17.34 | $+11.90 | +3.5% |
| CAKE | 3 ($329) | $117.25 | $109.76 | $109.11 | $-22.47 | -6.4% |
| CBRL | 5 ($340) | $67.16 | $67.96 | $66.95 | $+4.00 | +1.2% |
| CDNA | 4 ($295) | $86.10 | $73.70 | $77.88 | $-49.60 | -14.4% |
| CVX | 4 ($869) | $210.70 | $217.24 | $219.89 | $+26.16 | +3.1% |
| GTLB | 6 ($284) | $56.75 | $47.36 | $47.73 | $-56.34 | -16.5% |
| HUM | 1 ($462) | $458.76 | $461.61 | $450.00 | $+2.85 | +0.6% |
| IOVA | 44 ($331) | $7.70 | $7.53 | $7.76 | $-7.57 | -2.2% |
| JNJ | 3 ($848) | $277.80 | $282.79 | $285.75 | $+14.97 | +1.8% |
| MRK | 5 ($723) | $148.46 | $144.59 | $147.76 | $-19.34 | -2.6% |
| PANW | 2 ($631) | $318.08 | $315.64 | $322.24 | $-4.88 | -0.8% |
| PAYS | 37 ($353) | $9.38 | $9.54 | $9.52 | $+6.11 | +1.8% |
| SPY | 0.026 ($19) | $756.33 | $739.29 | $754.37 | $-0.44 | -2.3% |
| STT | 5 ($850) | $165.11 | $170.04 | $173.45 | $+24.68 | +3.0% |
| TGT | 5 ($800) | $152.86 | $160.06 | $161.45 | $+36.02 | +4.7% |
| TXG | 6 ($330) | $55.86 | $55.00 | $58.19 | $-5.16 | -1.5% |
| XOM | 5 ($836) | $164.24 | $167.12 | $170.59 | $+14.40 | +1.8% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($355), CAKE ($329), CBRL ($340), CDNA ($295), GTLB ($284), IOVA ($331), PAYS ($353), TXG ($330)
- **Bull's positions** (8): CVX ($869), HUM ($462), JNJ ($848), MRK ($723), PANW ($631), SPY ($19), TGT ($800), XOM ($836)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($850) — do not size against this until ownership is resolved.

🚨 **MISSING — in Rocket's book but not held at the broker:**

  - NSIT — likely a stop fill or manual close. Log the exit in trade_log.md.
  - OABI — likely a stop fill or manual close. Log the exit in trade_log.md.
  - PBF — likely a stop fill or manual close. Log the exit in trade_log.md.


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
