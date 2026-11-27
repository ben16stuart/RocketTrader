# Portfolio State

**Last Updated**: 2026-11-27 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,641.26 |
| Rocket's Allocated Slice (30%) | $2,892.38 |
| Cash Available (shared, pooled) | $660.09 |
| Total Invested (both agents) | $8,981.17 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **+$29 (+1.02%)** vs IWM +2.12% · daily loss cap $145: OK |
| **Rocket own book since 7/20** | **+0.78%** vs IWM -6.07% → **+6.85 pts** |
| **Rocket own book since 10/6 (new rules)** | **+3.92%** vs IWM -2.41% → **+6.33 pts** |
| **Rocket own book this week** | **+6.19%** vs IWM +7.00% → **-0.80 pts** |
| Rocket return since rebase (SHARED account, not own book) | -4.60% |
| IWM return since rebase | -6.09% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.49% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 86.2% | must be >= 50.0% |
| Core (IWM) | 3.1% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 10.6% | buffer only (<= 10%) |

✅ **Satellite floor met.**

**Rebase Date**: 2026-07-20 (account merged with Bull — prior standalone
history since 2026-04-20 is preserved in memory/weekly_reviews/)

⚠️ **Cash and buying power above are POOLED with Bull.** Before sizing any
trade, check actual available cash — do not assume the full allocated slice
is available if Bull has open positions consuming shared cash.

---

## Open Positions (shared account — yours AND Bull's)

Ownership is reconciled below — do not re-derive it from the trade log.

| Symbol | Shares | Entry Price | Price (⚠️ NOT a settled close) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| AMPL | 20 ($353) | $17.15 | $17.64 | $17.10 | $+9.80 | +2.9% |
| APPN | 6 ($336) | $51.73 | $56.03 | $55.08 | $+25.80 | +8.3% |
| CAKE | 3 ($334) | $117.25 | $111.20 | $109.66 | $-18.15 | -5.2% |
| CBRL | 5 ($385) | $67.16 | $76.94 | $75.35 | $+48.90 | +14.6% |
| CDNA | 4 ($310) | $86.10 | $77.50 | $75.86 | $-34.40 | -10.0% |
| CVX | 4 ($853) | $210.70 | $213.30 | $210.95 | $+10.40 | +1.2% |
| ILMN | 4 ($820) | $195.98 | $205.01 | $200.39 | $+36.12 | +4.6% |
| INTA | 3 ($138) | $43.65 | $46.09 | $45.81 | $+7.32 | +5.6% |
| IOVA | 44 ($311) | $7.70 | $7.07 | $7.13 | $-27.59 | -8.1% |
| IWM | 0.33 ($91) | $265.70 | $274.56 | $268.87 | $+2.92 | +3.3% |
| JNJ | 3 ($825) | $277.80 | $275.00 | $273.94 | $-8.40 | -1.0% |
| KO | 8 ($780) | $95.22 | $97.55 | $97.59 | $+18.63 | +2.4% |
| MRK | 5 ($710) | $148.46 | $142.00 | $140.29 | $-32.29 | -4.3% |
| PANW | 2 ($736) | $318.08 | $367.85 | $356.14 | $+99.54 | +15.6% |
| TGT | 5 ($863) | $152.86 | $172.61 | $172.22 | $+98.75 | +12.9% |
| TXG | 6 ($328) | $55.86 | $54.60 | $55.68 | $-7.57 | -2.3% |
| XOM | 5 ($809) | $164.24 | $161.79 | $158.08 | $-12.25 | -1.5% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($91)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($353), APPN ($336), CAKE ($334), CBRL ($385), CDNA ($310), INTA ($138), IOVA ($311), TXG ($328)
- **Bull's positions** (8): CVX ($853), ILMN ($820), JNJ ($825), KO ($780), MRK ($710), PANW ($736), TGT ($863), XOM ($809)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| a2ae8b6b… | ILMN | sell | 4 | trailing_stop | new |
| 61a5d542… | INTA | sell | 3 | trailing_stop | new |
| c4a03799… | APPN | sell | 6 | trailing_stop | new |
| 28312c92… | KO | sell | 8 | trailing_stop | new |
| 39ae6bab… | CBRL | sell | 5 | trailing_stop | new |
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
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
