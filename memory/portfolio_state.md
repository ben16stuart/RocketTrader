# Portfolio State

**Last Updated**: 2026-10-20 16:15 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,057.26 |
| Rocket's Allocated Slice (30%) | $3,017.18 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,065.23 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-4.93%** vs IWM -5.78% → **+0.85 pts** |
| **Rocket own book since 10/6 (new rules)** | **-1.97%** vs IWM -2.11% → **+0.14 pts** |
| **Rocket own book this week** | **+1.58%** vs IWM +1.84% → **-0.26 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.48% |
| IWM return since rebase | -5.55% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +5.07% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 57.0% | must be >= 50.0% |
| Core (IWM) | 33.9% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 9.1% | buffer only (<= 10%) |

✅ **Satellite floor met.**

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
| BNY | 6 ($866) | $141.86 | $144.28 | $142.44 | $+14.52 | +1.7% |
| DELL | 1 ($464) | $464.53 | $464.21 | $455.44 | $-0.32 | -0.1% |
| DK | 4 ($304) | $79.18 | $75.97 | $75.08 | $-12.86 | -4.1% |
| FTNT | 5 ($855) | $171.34 | $170.93 | $171.50 | $-2.05 | -0.2% |
| HPE | 15 ($846) | $56.91 | $56.41 | $55.87 | $-7.44 | -0.9% |
| ILMN | 3 ($811) | $276.76 | $270.19 | $262.66 | $-19.71 | -2.4% |
| IWM | 3.7163 ($1,023) | $282.38 | $275.38 | $271.28 | $-26.00 | -2.5% |
| NEO | 21 ($353) | $16.83 | $16.82 | $16.42 | $-0.10 | -0.0% |
| NSIT | 2 ($333) | $162.53 | $166.25 | $163.73 | $+7.45 | +2.3% |
| NUE | 3 ($777) | $248.90 | $259.13 | $260.73 | $+30.69 | +4.1% |
| REPL | 32 ($366) | $10.99 | $11.44 | $11.05 | $+14.40 | +4.1% |
| SPY | 0.122 ($94) | $763.26 | $769.40 | $766.48 | $+0.75 | +0.8% |
| STT | 5 ($837) | $165.11 | $167.38 | $165.43 | $+11.35 | +1.4% |
| TGT | 5 ($774) | $152.86 | $154.71 | $153.29 | $+9.25 | +1.2% |
| TXG | 5 ($363) | $69.59 | $72.64 | $69.89 | $+15.23 | +4.4% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,023)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($304), NEO ($353), NSIT ($333), REPL ($366), TXG ($363)
- **Bull's positions** (7): BNY ($866), DELL ($464), FTNT ($855), ILMN ($811), NUE ($777), SPY ($94), TGT ($774)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($846) — do not size against this until ownership is resolved.
  - STT ($837) — do not size against this until ownership is resolved.


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
Market open: Yes
