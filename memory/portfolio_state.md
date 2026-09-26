# Portfolio State

**Last Updated**: 2026-09-26 15:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,370.66 |
| Rocket's Allocated Slice (30%) | $3,111.20 |
| Cash Available (shared, pooled) | $1,435.34 |
| Total Invested (both agents) | $8,935.32 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +2.62% |
| IWM return since rebase | -3.29% |
| Rocket vs IWM | +5.91% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 14.4% | must be >= 50.0% |
| Core (IWM) | 49.6% | capped at <= 50.0% |

🚨 **SATELLITE FLOOR BREACHED — 14.4% < 50%.** Rocket is not deployed in enough stock picks. This is not a market call to sit out — it is a research gap. Finding a qualifying name is the top priority of the next session, not an optional nice-to-have.

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
| IWM | 5 | $297.53 | $281.97 | $281.97 | $-85.20 | -5.2% |
| RARE | 31 | $15.08 | $14.50 | $14.50 | $-17.98 | -3.8% |
| SPY | 9 | $769.31 | $771.35 | $771.35 | $+18.37 | +0.3% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($1,544)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (1): RARE ($450)
- **Bull's positions** (1): SPY ($6,942)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| ca4a062c… | RARE | sell | 31 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
