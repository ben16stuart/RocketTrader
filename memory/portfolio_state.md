# Portfolio State

**Last Updated**: 2026-11-25 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,545.47 |
| Rocket's Allocated Slice (30%) | $2,863.64 |
| Cash Available (shared, pooled) | $660.11 |
| Total Invested (both agents) | $8,885.36 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$15 (-0.54%)** vs IWM +0.76% · daily loss cap $143: OK |
| **Rocket own book since 7/20** | **-0.16%** vs IWM -7.92% → **+7.76 pts** |
| **Rocket own book since 10/6 (new rules)** | **+2.96%** vs IWM -4.33% → **+7.28 pts** |
| **Rocket own book this week** | **+5.20%** vs IWM +4.89% → **+0.31 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.54% |
| IWM return since rebase | -7.64% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.10% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 86.2% | must be >= 50.0% |
| Core (IWM) | 3.1% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 10.7% | buffer only (<= 10%) |

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
| AMPL | 20 ($342) | $17.15 | $17.11 | $16.98 | $-0.90 | -0.3% |
| APPN | 6 ($331) | $51.73 | $55.12 | $54.80 | $+20.34 | +6.6% |
| CAKE | 3 ($329) | $117.25 | $109.65 | $109.42 | $-22.80 | -6.5% |
| CBRL | 5 ($377) | $67.16 | $75.50 | $75.19 | $+41.67 | +12.4% |
| CDNA | 4 ($304) | $86.10 | $75.89 | $77.83 | $-40.84 | -11.9% |
| CVX | 4 ($846) | $210.70 | $211.46 | $208.73 | $+3.02 | +0.4% |
| ILMN | 4 ($802) | $195.98 | $200.48 | $204.52 | $+18.00 | +2.3% |
| INTA | 3 ($137) | $43.65 | $45.76 | $45.03 | $+6.33 | +4.8% |
| IOVA | 44 ($314) | $7.70 | $7.14 | $7.33 | $-24.51 | -7.2% |
| IWM | 0.33 ($89) | $265.70 | $269.18 | $267.14 | $+1.15 | +1.3% |
| JNJ | 3 ($824) | $277.80 | $274.77 | $276.46 | $-9.09 | -1.1% |
| KO | 8 ($783) | $95.22 | $97.92 | $97.62 | $+21.55 | +2.8% |
| MRK | 5 ($704) | $148.46 | $140.71 | $141.57 | $-38.77 | -5.2% |
| PANW | 2 ($713) | $318.08 | $356.61 | $352.99 | $+77.06 | +12.1% |
| TGT | 5 ($863) | $152.86 | $172.54 | $176.06 | $+98.40 | +12.9% |
| TXG | 6 ($334) | $55.86 | $55.73 | $57.27 | $-0.78 | -0.2% |
| XOM | 5 ($793) | $164.24 | $158.65 | $158.23 | $-27.95 | -3.4% |

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($89)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($342), APPN ($331), CAKE ($329), CBRL ($377), CDNA ($304), INTA ($137), IOVA ($314), TXG ($334)
- **Bull's positions** (8): CVX ($846), ILMN ($802), JNJ ($824), KO ($783), MRK ($704), PANW ($713), TGT ($863), XOM ($793)


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
Market open: Yes
