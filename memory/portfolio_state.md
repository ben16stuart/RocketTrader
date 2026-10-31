# Portfolio State

**Last Updated**: 2026-10-31 15:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,988.50 |
| Rocket's Allocated Slice (30%) | $2,996.55 |
| Cash Available (shared, pooled) | $334.28 |
| Total Invested (both agents) | $9,654.22 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+2.23%** vs IWM -4.44% → **+6.67 pts** |
| **Rocket own book since 10/6 (new rules)** | **+5.42%** vs IWM -0.71% → **+6.13 pts** |
| **Rocket own book this week** | **+7.32%** vs IWM +1.30% → **+6.02 pts** |
| Rocket return since rebase (SHARED account, not own book) | -1.16% |
| IWM return since rebase | -4.19% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +3.03% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 101.7% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 0.0% | buffer only (<= 10%) |

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
| BNY | 6 ($883) | $141.86 | $147.11 | $147.11 | $+31.50 | +3.7% |
| CLDT | 25 ($369) | $14.30 | $14.75 | $14.75 | $+11.25 | +3.1% |
| CRWD | 3 ($751) | $257.46 | $250.43 | $250.43 | $-21.10 | -2.7% |
| FTNT | 6 ($816) | $136.85 | $136.08 | $136.08 | $-4.62 | -0.6% |
| GTLB | 6 ($325) | $56.75 | $54.09 | $54.09 | $-15.96 | -4.7% |
| HPE | 15 ($826) | $56.91 | $55.09 | $55.09 | $-27.24 | -3.2% |
| KELYA | 22 ($365) | $16.41 | $16.59 | $16.59 | $+3.96 | +1.1% |
| MRNA | 4 ($887) | $221.26 | $221.72 | $221.72 | $+1.84 | +0.2% |
| NEO | 21 ($365) | $16.83 | $17.38 | $17.38 | $+11.55 | +3.3% |
| NSIT | 2 ($345) | $162.53 | $172.74 | $172.74 | $+20.42 | +6.3% |
| NUE | 3 ($822) | $248.90 | $273.87 | $273.87 | $+74.91 | +10.0% |
| QMCO | 20 ($365) | $17.62 | $18.27 | $18.27 | $+13.00 | +3.7% |
| REPL | 32 ($564) | $10.99 | $17.61 | $17.61 | $+211.84 | +60.2% |
| STT | 5 ($849) | $165.11 | $169.77 | $169.77 | $+23.30 | +2.8% |
| TGT | 5 ($772) | $152.86 | $154.38 | $154.38 | $+7.60 | +1.0% |
| TXG | 5 ($351) | $69.59 | $70.11 | $70.11 | $+2.58 | +0.7% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CLDT ($369), GTLB ($325), KELYA ($365), NEO ($365), NSIT ($345), QMCO ($365), REPL ($564), TXG ($351)
- **Bull's positions** (6): BNY ($883), CRWD ($751), FTNT ($816), MRNA ($887), NUE ($822), TGT ($772)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($826) — do not size against this until ownership is resolved.
  - STT ($849) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 67cfc779… | CRWD | sell | 3 | trailing_stop | new |
| 85effa8c… | FTNT | sell | 6 | trailing_stop | new |
| 5d804037… | MRNA | sell | 4 | trailing_stop | new |
| 6f3717c0… | KELYA | sell | 22 | trailing_stop | new |
| d6f20cea… | CLDT | sell | 25 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| 6ae5ec26… | QMCO | sell | 20 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| 30eae37d… | NEO | sell | 21 | trailing_stop | new |
| 81d4992e… | TXG | sell | 5 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 65d0299a… | HPE | sell | 15 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
