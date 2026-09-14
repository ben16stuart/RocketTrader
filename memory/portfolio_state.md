# Portfolio State

**Last Updated**: 2026-09-14 20:00 UTC (market_close)
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

**Note**: `portfolio_snapshot.py` failed both attempts this session — `/v2/orders`
timed out repeatedly (confirmed Alpaca-side via direct curl: `/v2/clock`, `/v2/positions`,
`/v2/account` all returned in <0.2s, `/v2/orders?status=open` hung 15s+ three times in a
row). Figures below pulled directly via `alpaca_client.py account`/`positions` and a raw
`/v2/positions/IWM` call, bypassing the broken endpoint. Open-orders table below could
not be refreshed this session — carried forward from the prior snapshot.

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,468.76 |
| Rocket's Allocated Slice (30%) | $3,140.63 |
| Cash Available (shared, pooled) | $427.02 |
| Total Invested (both agents) | $10,041.89 |
| Rocket return since rebase | See trade_log.md hand-built book chain (lesson 23a) — **stale**, last computed W35 8/28: **−2.51% vs SPY**. Do NOT use `portfolio_snapshot.py`'s own since-rebase number, it mixes in Bull's P&L. W36/W37 `weekly_review` still overdue. |

**Rebase Date**: 2026-07-20 (account merged with Bull — prior standalone
history since 2026-04-20 is preserved in memory/weekly_reviews/)

⚠️ **Cash and buying power above are POOLED with Bull.** Before sizing any
trade, check actual available cash — do not assume the full allocated slice
is available if Bull has open positions consuming shared cash.

---

## Open Positions (shared account — yours AND Bull's)

Ownership is reconciled below — do not re-derive it from the trade log.

| Symbol | Shares | Entry Price | Price (LIVE, market_close) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| IWM | 9.8636 (raw qty, lesson 24a) | $295.12 | $287.90 | $288.89 | $-71.25 | -2.4% |
| JPM | 6 | $313.30 | $350.12 | — | $+220.92 | +11.8% |
| SCHW | 5 | $103.91 | $107.34 | — | $+17.15 | +3.3% |
| SPY | 6 | $767.97 | $760.79 | — | $-43.03 | -0.9% |

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,839.73)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (3): JPM ($2,107), SCHW ($537), SPY ($4,569)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 3d0e7965… | JPM | sell | 6 | trailing_stop | new |
| 8002a4e3… | SCHW | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 3 max
Market open: Yes
