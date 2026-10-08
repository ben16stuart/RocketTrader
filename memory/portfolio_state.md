# Portfolio State

**Last Updated**: 2026-10-08 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,321.04 |
| Rocket's Allocated Slice (30%) | $3,096.31 |
| Cash Available (shared, pooled) | $1,045.19 |
| Total Invested (both agents) | $9,275.85 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +2.13% |
| IWM return since rebase | -4.74% |
| Rocket vs IWM | +6.87% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 0.0% | must be >= 50.0% |
| Core (IWM) | 89.5% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 10.5% | buffer only (<= 10%) |

🚨 **SATELLITE FLOOR BREACHED — 0.0% < 50%.** Rocket is not deployed in enough stock picks (the shortfall sits in IWM, not cash). This is not a market call to sit out — it is a research gap. Finding a qualifying name is the top priority of the next session, not an optional nice-to-have.

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
| AMD | 1 | $646.48 | $620.99 | $645.86 | $-25.49 | -3.9% |
| BNY | 6 | $141.86 | $143.65 | $142.72 | $+10.74 | +1.3% |
| DELL | 1 | $573.43 | $575.00 | $578.96 | $+1.57 | +0.3% |
| IWM | 10 | $290.69 | $277.71 | $277.70 | $-129.53 | -4.5% |
| NUE | 3 | $248.90 | $246.27 | $246.44 | $-7.89 | -1.1% |
| SPY | 5 | $769.43 | $773.76 | $777.22 | $+20.78 | +0.6% |

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,771)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (5): AMD ($621), BNY ($862), DELL ($575), NUE ($739), SPY ($3,709)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| 678d9c30… | AMD | sell | 1 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |
| 5e832980… | DELL | sell | 1 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 1 / 5 max
Market open: Yes
