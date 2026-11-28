# Portfolio State

**Last Updated**: 2026-11-28 16:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,635.30 |
| Rocket's Allocated Slice (30%) | $2,890.59 |
| Cash Available (shared, pooled) | $660.09 |
| Total Invested (both agents) | $8,975.21 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **+$40 (+1.41%)** vs IWM +1.83% · daily loss cap $145: OK |
| **Rocket own book since 7/20** | **+1.16%** vs IWM -6.34% → **+7.50 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.32%** vs IWM -2.68% → **+7.00 pts** |
| **Rocket own book this week** | **+6.60%** vs IWM +6.69% → **-0.10 pts** |
| Rocket return since rebase (SHARED account, not own book) | -4.66% |
| IWM return since rebase | -6.09% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.43% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 86.7% | must be >= 50.0% |
| Core (IWM) | 3.1% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 10.2% | buffer only (<= 10%) |

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
| AMPL | 20 ($353) | $17.15 | $17.64 | $17.64 | $+9.80 | +2.9% |
| APPN | 6 ($337) | $51.73 | $56.13 | $56.13 | $+26.40 | +8.5% |
| CAKE | 3 ($334) | $117.25 | $111.20 | $111.20 | $-18.15 | -5.2% |
| CBRL | 5 ($383) | $67.16 | $76.59 | $76.59 | $+47.15 | +14.0% |
| CDNA | 4 ($309) | $86.10 | $77.16 | $77.16 | $-35.76 | -10.4% |
| CVX | 4 ($850) | $210.70 | $212.45 | $212.45 | $+7.00 | +0.8% |
| ILMN | 4 ($823) | $195.98 | $205.74 | $205.74 | $+39.04 | +5.0% |
| INTA | 3 ($138) | $43.65 | $46.09 | $46.09 | $+7.32 | +5.6% |
| IOVA | 44 ($313) | $7.70 | $7.12 | $7.12 | $-25.39 | -7.5% |
| IWM | 0.33 ($90) | $265.70 | $273.79 | $273.79 | $+2.67 | +3.0% |
| JNJ | 3 ($827) | $277.80 | $275.51 | $275.51 | $-6.87 | -0.8% |
| KO | 8 ($779) | $95.22 | $97.40 | $97.40 | $+17.43 | +2.3% |
| MRK | 5 ($707) | $148.46 | $141.32 | $141.32 | $-35.69 | -4.8% |
| PANW | 2 ($734) | $318.08 | $366.76 | $366.76 | $+97.36 | +15.3% |
| TGT | 5 ($860) | $152.86 | $171.97 | $171.97 | $+95.55 | +12.5% |
| TXG | 6 ($339) | $55.86 | $56.53 | $56.53 | $+4.02 | +1.2% |
| XOM | 5 ($801) | $164.24 | $160.18 | $160.18 | $-20.30 | -2.5% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($90)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($353), APPN ($337), CAKE ($334), CBRL ($383), CDNA ($309), INTA ($138), IOVA ($313), TXG ($339)
- **Bull's positions** (8): CVX ($850), ILMN ($823), JNJ ($827), KO ($779), MRK ($707), PANW ($734), TGT ($860), XOM ($801)


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
