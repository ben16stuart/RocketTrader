# Portfolio State

**Last Updated**: 2026-10-24 15:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,097.46 |
| Rocket's Allocated Slice (30%) | $3,029.24 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,105.43 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-4.74%** vs IWM -5.67% → **+0.93 pts** |
| **Rocket own book since 10/6 (new rules)** | **-1.77%** vs IWM -1.99% → **+0.22 pts** |
| **Rocket own book this week** | **+1.79%** vs IWM +1.96% → **-0.18 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.08% |
| IWM return since rebase | -5.42% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +5.34% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 56.9% | must be >= 50.0% |
| Core (IWM) | 33.8% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 9.3% | buffer only (<= 10%) |

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
| BNY | 6 ($872) | $141.86 | $145.27 | $145.27 | $+20.46 | +2.4% |
| DELL | 1 ($456) | $464.53 | $456.44 | $456.44 | $-8.09 | -1.7% |
| DK | 4 ($298) | $79.18 | $74.41 | $74.41 | $-19.08 | -6.0% |
| FTNT | 5 ($900) | $171.34 | $179.99 | $179.99 | $+43.25 | +5.0% |
| HPE | 15 ($850) | $56.91 | $56.69 | $56.69 | $-3.24 | -0.4% |
| ILMN | 3 ($808) | $276.76 | $269.42 | $269.42 | $-22.02 | -2.7% |
| IWM | 3.7163 ($1,025) | $282.38 | $275.75 | $275.75 | $-24.62 | -2.3% |
| NEO | 21 ($348) | $16.83 | $16.59 | $16.59 | $-5.04 | -1.4% |
| NSIT | 2 ($354) | $162.53 | $176.77 | $176.77 | $+28.48 | +8.8% |
| NUE | 3 ($774) | $248.90 | $258.11 | $258.11 | $+27.63 | +3.7% |
| REPL | 32 ($367) | $10.99 | $11.46 | $11.46 | $+15.04 | +4.3% |
| SPY | 0.122 ($93) | $763.26 | $759.97 | $759.97 | $-0.40 | -0.4% |
| STT | 5 ($839) | $165.11 | $167.83 | $167.83 | $+13.60 | +1.6% |
| TGT | 5 ($764) | $152.86 | $152.76 | $152.76 | $-0.50 | -0.1% |
| TXG | 5 ($358) | $69.59 | $71.55 | $71.55 | $+9.78 | +2.8% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,025)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($298), NEO ($348), NSIT ($354), REPL ($367), TXG ($358)
- **Bull's positions** (7): BNY ($872), DELL ($456), FTNT ($900), ILMN ($808), NUE ($774), SPY ($93), TGT ($764)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($850) — do not size against this until ownership is resolved.
  - STT ($839) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| b710d1cf… | DK | sell | 4 | trailing_stop | new |
| 30eae37d… | NEO | sell | 21 | trailing_stop | new |
| 81d4992e… | TXG | sell | 5 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 65d0299a… | HPE | sell | 15 | trailing_stop | new |
| f9d394d3… | FTNT | sell | 5 | trailing_stop | new |
| cb4662b7… | DELL | sell | 1 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |
| 8211961c… | ILMN | sell | 3 | trailing_stop | new |
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
