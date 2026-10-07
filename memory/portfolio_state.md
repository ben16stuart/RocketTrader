# Portfolio State

**Last Updated**: 2026-10-07 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,360.97 |
| Rocket's Allocated Slice (30%) | $3,108.29 |
| Cash Available (shared, pooled) | $1,045.26 |
| Total Invested (both agents) | $9,315.71 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +2.53% |
| IWM return since rebase | -4.76% |
| Rocket vs IWM | +7.29% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 0.0% | must be >= 50.0% |
| Core (IWM) | 89.1% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 10.9% | buffer only (<= 10%) |

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
| AMD | 1 | $646.48 | $646.13 | $649.42 | $-0.35 | -0.1% |
| BNY | 6 | $141.86 | $142.54 | $143.73 | $+4.11 | +0.5% |
| DELL | 1 | $573.43 | $578.28 | $574.00 | $+4.85 | +0.8% |
| IWM | 10 | $290.69 | $277.66 | $281.34 | $-130.03 | -4.5% |
| NUE | 3 | $248.90 | $246.59 | $251.07 | $-6.95 | -0.9% |
| SPY | 5 | $769.44 | $777.39 | $779.09 | $+38.11 | +1.0% |

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,770)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (5): AMD ($646), BNY ($855), DELL ($578), NUE ($740), SPY ($3,726)


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
