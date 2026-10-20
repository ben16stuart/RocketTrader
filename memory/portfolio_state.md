# Portfolio State

**Last Updated**: 2026-10-20 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,031.40 |
| Rocket's Allocated Slice (30%) | $3,009.42 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,039.37 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-5.17%** vs IWM -5.69% → **+0.52 pts** |
| **Rocket own book since 10/6 (new rules)** | **-2.21%** vs IWM -2.01% → **-0.20 pts** |
| **Rocket own book this week** | **+1.33%** vs IWM +1.94% → **-0.61 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.74% |
| IWM return since rebase | -5.45% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +4.71% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 56.8% | must be >= 50.0% |
| Core (IWM) | 34.0% | absorbs the leftover (no cap since 2026-10-06) |
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
| BNY | 6 ($864) | $141.86 | $143.94 | $142.44 | $+12.51 | +1.5% |
| DELL | 1 ($461) | $464.53 | $461.25 | $455.44 | $-3.28 | -0.7% |
| DK | 4 ($310) | $79.18 | $77.58 | $75.08 | $-6.40 | -2.0% |
| FTNT | 5 ($854) | $171.34 | $170.84 | $171.50 | $-2.52 | -0.3% |
| HPE | 15 ($841) | $56.91 | $56.05 | $55.87 | $-12.77 | -1.5% |
| ILMN | 3 ($804) | $276.76 | $267.92 | $262.66 | $-26.54 | -3.2% |
| IWM | 3.7163 ($1,024) | $282.38 | $275.67 | $271.28 | $-24.92 | -2.4% |
| NEO | 21 ($348) | $16.83 | $16.59 | $16.42 | $-5.14 | -1.5% |
| NSIT | 2 ($328) | $162.53 | $164.13 | $163.73 | $+3.21 | +1.0% |
| NUE | 3 ($784) | $248.90 | $261.45 | $260.73 | $+37.65 | +5.0% |
| REPL | 32 ($365) | $10.99 | $11.41 | $11.05 | $+13.60 | +3.9% |
| SPY | 0.122 ($94) | $763.26 | $768.55 | $766.48 | $+0.65 | +0.7% |
| STT | 5 ($833) | $165.11 | $166.50 | $165.43 | $+6.97 | +0.8% |
| TGT | 5 ($771) | $152.86 | $154.18 | $153.29 | $+6.60 | +0.9% |
| TXG | 5 ($358) | $69.59 | $71.53 | $69.89 | $+9.68 | +2.8% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,024)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($310), NEO ($348), NSIT ($328), REPL ($365), TXG ($358)
- **Bull's positions** (7): BNY ($864), DELL ($461), FTNT ($854), ILMN ($804), NUE ($784), SPY ($94), TGT ($771)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($841) — do not size against this until ownership is resolved.
  - STT ($833) — do not size against this until ownership is resolved.


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
