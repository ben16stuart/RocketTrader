# Portfolio State

**Last Updated**: 2026-11-26 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,528.83 |
| Rocket's Allocated Slice (30%) | $2,858.65 |
| Cash Available (shared, pooled) | $660.09 |
| Total Invested (both agents) | $8,868.74 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$0 (-0.00%)** vs IWM +0.00% · daily loss cap $143: OK |
| **Rocket own book since 7/20** | **-0.24%** vs IWM -8.02% → **+7.78 pts** |
| **Rocket own book since 10/6 (new rules)** | **+2.87%** vs IWM -4.43% → **+7.30 pts** |
| **Rocket own book this week** | **+5.12%** vs IWM +4.78% → **+0.34 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.71% |
| IWM return since rebase | -7.78% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.07% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 86.3% | must be >= 50.0% |
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
| AMPL | 20 ($342) | $17.15 | $17.10 | $17.10 | $-1.00 | -0.3% |
| APPN | 6 ($330) | $51.73 | $55.08 | $55.08 | $+20.10 | +6.5% |
| CAKE | 3 ($329) | $117.25 | $109.66 | $109.66 | $-22.77 | -6.5% |
| CBRL | 5 ($377) | $67.16 | $75.35 | $75.35 | $+40.95 | +12.2% |
| CDNA | 4 ($303) | $86.10 | $75.86 | $75.86 | $-40.96 | -11.9% |
| CVX | 4 ($844) | $210.70 | $210.95 | $210.95 | $+1.00 | +0.1% |
| ILMN | 4 ($802) | $195.98 | $200.39 | $200.39 | $+17.64 | +2.2% |
| INTA | 3 ($137) | $43.65 | $45.81 | $45.81 | $+6.48 | +4.9% |
| IOVA | 44 ($314) | $7.70 | $7.13 | $7.13 | $-24.95 | -7.4% |
| IWM | 0.33 ($89) | $265.70 | $268.87 | $268.87 | $+1.05 | +1.2% |
| JNJ | 3 ($822) | $277.80 | $273.94 | $273.94 | $-11.58 | -1.4% |
| KO | 8 ($781) | $95.22 | $97.59 | $97.59 | $+18.95 | +2.5% |
| MRK | 5 ($701) | $148.46 | $140.29 | $140.29 | $-40.84 | -5.5% |
| PANW | 2 ($712) | $318.08 | $356.14 | $356.14 | $+76.12 | +12.0% |
| TGT | 5 ($861) | $152.86 | $172.22 | $172.22 | $+96.80 | +12.7% |
| TXG | 6 ($334) | $55.86 | $55.68 | $55.68 | $-1.08 | -0.3% |
| XOM | 5 ($790) | $164.24 | $158.08 | $158.08 | $-30.80 | -3.8% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($89)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($342), APPN ($330), CAKE ($329), CBRL ($377), CDNA ($303), INTA ($137), IOVA ($314), TXG ($334)
- **Bull's positions** (8): CVX ($844), ILMN ($802), JNJ ($822), KO ($781), MRK ($701), PANW ($712), TGT ($861), XOM ($790)


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
