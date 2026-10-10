# Portfolio State

**Last Updated**: 2026-10-10 15:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,361.08 |
| Rocket's Allocated Slice (30%) | $3,108.32 |
| Cash Available (shared, pooled) | $1,045.19 |
| Total Invested (both agents) | $9,315.89 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +2.53% |
| IWM return since rebase | -4.32% |
| Rocket vs IWM | +6.85% |

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

| Symbol | Shares | Entry Price | Price (⚠️ NOT a settled close) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| AMD | 1 | $646.48 | $608.10 | $608.10 | $-38.38 | -5.9% |
| BNY | 6 | $141.86 | $142.71 | $142.71 | $+5.10 | +0.6% |
| DELL | 1 | $573.43 | $586.06 | $586.06 | $+12.63 | +2.2% |
| IWM | 10 | $290.69 | $278.94 | $278.94 | $-117.26 | -4.0% |
| NUE | 3 | $248.90 | $250.33 | $250.33 | $+4.29 | +0.6% |
| SPY | 5 | $769.43 | $778.57 | $778.57 | $+43.81 | +1.2% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,783)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (5): AMD ($608), BNY ($856), DELL ($586), NUE ($751), SPY ($3,732)


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
Market open: No
