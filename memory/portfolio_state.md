# Portfolio State

**Last Updated**: 2026-09-21 20:00 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,517.28 |
| Rocket's Allocated Slice (30%) | $3,155.18 |
| Cash Available (shared, pooled) | $1,665.04 |
| Total Invested (both agents) | $8,852.24 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +4.07% |
| IWM return since rebase | -2.05% |
| Rocket vs IWM | +6.12% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 0.0% | must be >= 50.0% |
| Core (IWM) | 49.6% | capped at <= 50.0% |

🚨 **SATELLITE FLOOR BREACHED — 0.0% < 50%.** Rocket is not deployed in enough stock picks. This is not a market call to sit out — it is a research gap. Finding a qualifying name is the top priority of the next session, not an optional nice-to-have.

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
| IWM | 5 | $297.53 | $285.65 | $284.10 | $-65.05 | -4.0% |
| JPM | 6 | $313.30 | $352.04 | $349.67 | $+232.44 | +12.4% |
| SCHW | 5 | $103.91 | $106.88 | $105.25 | $+14.85 | +2.9% |
| SPY | 6 | $766.97 | $773.63 | $761.69 | $+39.97 | +0.9% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($1,564)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (3): JPM ($2,112), SCHW ($534), SPY ($4,642)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 3d0e7965… | JPM | sell | 6 | trailing_stop | new |
| 8002a4e3… | SCHW | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
