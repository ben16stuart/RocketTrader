# Portfolio State

**Last Updated**: 2026-10-22 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,062.24 |
| Rocket's Allocated Slice (30%) | $3,018.67 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,070.21 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-4.70%** vs IWM -5.37% → **+0.67 pts** |
| **Rocket own book since 10/6 (new rules)** | **-1.73%** vs IWM -1.68% → **-0.05 pts** |
| **Rocket own book this week** | **+1.83%** vs IWM +2.28% → **-0.46 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.43% |
| IWM return since rebase | -5.11% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +4.68% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 57.0% | must be >= 50.0% |
| Core (IWM) | 34.1% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 8.9% | buffer only (<= 10%) |

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
| BNY | 6 ($870) | $141.86 | $145.01 | $145.85 | $+18.90 | +2.2% |
| DELL | 1 ($451) | $464.53 | $451.17 | $485.88 | $-13.37 | -2.9% |
| DK | 4 ($304) | $79.18 | $75.94 | $78.22 | $-12.98 | -4.1% |
| FTNT | 5 ($864) | $171.34 | $172.82 | $174.05 | $+7.42 | +0.9% |
| HPE | 15 ($831) | $56.91 | $55.43 | $58.17 | $-22.14 | -2.6% |
| ILMN | 3 ($810) | $276.76 | $269.87 | $282.86 | $-20.67 | -2.5% |
| IWM | 3.7163 ($1,028) | $282.38 | $276.62 | $276.48 | $-21.41 | -2.0% |
| NEO | 21 ($345) | $16.83 | $16.41 | $17.04 | $-8.93 | -2.5% |
| NSIT | 2 ($341) | $162.53 | $170.72 | $171.19 | $+16.39 | +5.0% |
| NUE | 3 ($773) | $248.90 | $257.65 | $264.54 | $+26.25 | +3.5% |
| REPL | 32 ($383) | $10.99 | $11.98 | $11.72 | $+31.68 | +9.0% |
| SPY | 0.122 ($93) | $763.26 | $763.51 | $773.09 | $+0.03 | +0.0% |
| STT | 5 ($838) | $165.11 | $167.59 | $168.95 | $+12.38 | +1.5% |
| TGT | 5 ($790) | $152.86 | $158.07 | $152.38 | $+26.05 | +3.4% |
| TXG | 5 ($349) | $69.59 | $69.77 | $75.59 | $+0.88 | +0.3% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,028)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($304), NEO ($345), NSIT ($341), REPL ($383), TXG ($349)
- **Bull's positions** (7): BNY ($870), DELL ($451), FTNT ($864), ILMN ($810), NUE ($773), SPY ($93), TGT ($790)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($831) — do not size against this until ownership is resolved.
  - STT ($838) — do not size against this until ownership is resolved.


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
