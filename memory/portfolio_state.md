# Portfolio State

**Last Updated**: 2026-10-17 15:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,960.18 |
| Rocket's Allocated Slice (30%) | $2,988.05 |
| Cash Available (shared, pooled) | $986.15 |
| Total Invested (both agents) | $8,974.03 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-6.41%** vs IWM -7.48% → **+1.07 pts** |
| **Rocket own book since 10/6 (new rules)** | **-3.49%** vs IWM -3.87% → **+0.38 pts** |
| **Rocket own book this week** | **-2.75%** vs IWM -3.05% → **+0.30 pts** |
| Rocket return since rebase (SHARED account, not own book) | -1.44% |
| IWM return since rebase | -7.24% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +5.80% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 0.0% | must be >= 50.0% |
| Core (IWM) | 90.3% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 9.7% | buffer only (<= 10%) |

🚨 **SATELLITE FLOOR BREACHED — 0.0% < 50%.** Rocket is not deployed in enough stock picks (the shortfall sits in IWM, not cash). This is not a market call to sit out. Fill open slots from `python scripts/rank_screen.py` (max 5 new per week); every skipped top-8 name must be a logged VETO.

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
| BNY | 6 ($860) | $141.86 | $143.30 | $143.30 | $+8.64 | +1.0% |
| ILMN | 3 ($788) | $276.76 | $262.54 | $262.54 | $-42.66 | -5.1% |
| IWM | 9.9763 ($2,698) | $290.69 | $270.44 | $270.44 | $-202.06 | -7.0% |
| NTRS | 5 ($828) | $170.45 | $165.54 | $165.54 | $-24.55 | -2.9% |
| NUE | 3 ($769) | $248.90 | $256.29 | $256.29 | $+22.17 | +3.0% |
| SPY | 2.962 ($2,261) | $768.46 | $763.25 | $763.25 | $-15.42 | -0.7% |
| TGT | 5 ($771) | $152.86 | $154.26 | $154.26 | $+7.00 | +0.9% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

✅ **Balanced.** Every live position is attributed.

- **Rocket's core** (1): IWM ($2,698)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (6): BNY ($860), ILMN ($788), NTRS ($828), NUE ($769), SPY ($2,261), TGT ($771)


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 2e9dbabf… | NTRS | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |
| 8211961c… | ILMN | sell | 3 | trailing_stop | new |
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
