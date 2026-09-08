# Portfolio State

**Last Updated**: 2026-09-08 20:02 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,592.36 |
| Rocket's Allocated Slice (30%) | $3,177.71 |
| Cash Available (shared, pooled) | $427.02 |
| Total Invested (both agents) | $10,165.34 |
| Unrealized P&L (shared) | $+0.00 |
| Rocket return since rebase | +4.82% |
| SPY return since rebase | +3.22% |
| Rocket vs SPY | +1.60% |

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
| IWM | 10 | $295.12 | $294.65 | $296.01 | $-4.67 | -0.2% |
| JPM | 6 | $313.30 | $355.00 | $358.64 | $+250.20 | +13.3% |
| SCHW | 5 | $103.91 | $106.87 | $109.29 | $+14.80 | +2.8% |
| SPY | 6 | $767.97 | $765.78 | $770.19 | $-13.12 | -0.3% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,906)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (3): JPM ($2,130), SCHW ($534), SPY ($4,595)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 3d0e7965… | JPM | sell | 6 | trailing_stop | new |
| 8002a4e3… | SCHW | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 3 max
Market open: No
