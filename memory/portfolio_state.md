# Portfolio State

**Last Updated**: 2026-10-23 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,100.53 |
| Rocket's Allocated Slice (30%) | $3,030.16 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,108.50 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-4.72%** vs IWM -5.64% → **+0.92 pts** |
| **Rocket own book since 10/6 (new rules)** | **-1.75%** vs IWM -1.96% → **+0.21 pts** |
| **Rocket own book this week** | **+1.81%** vs IWM +1.99% → **-0.18 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.05% |
| IWM return since rebase | -5.39% |
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

| Symbol | Shares | Entry Price | Price (LIVE, session open) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| BNY | 6 ($872) | $141.86 | $145.25 | $145.32 | $+20.37 | +2.4% |
| DELL | 1 ($457) | $464.53 | $456.56 | $452.95 | $-7.97 | -1.7% |
| DK | 4 ($297) | $79.18 | $74.21 | $75.79 | $-19.88 | -6.3% |
| FTNT | 5 ($901) | $171.34 | $180.11 | $172.98 | $+43.85 | +5.1% |
| HPE | 15 ($852) | $56.91 | $56.77 | $55.47 | $-2.04 | -0.2% |
| ILMN | 3 ($808) | $276.76 | $269.38 | $269.40 | $-22.12 | -2.7% |
| IWM | 3.7163 ($1,025) | $282.38 | $275.82 | $276.67 | $-24.35 | -2.3% |
| NEO | 21 ($349) | $16.83 | $16.61 | $16.39 | $-4.62 | -1.3% |
| NSIT | 2 ($354) | $162.53 | $177.06 | $171.27 | $+29.07 | +8.9% |
| NUE | 3 ($775) | $248.90 | $258.37 | $258.06 | $+28.41 | +3.8% |
| REPL | 32 ($367) | $10.99 | $11.46 | $11.99 | $+15.04 | +4.3% |
| SPY | 0.122 ($93) | $763.26 | $760.00 | $763.96 | $-0.40 | -0.4% |
| STT | 5 ($838) | $165.11 | $167.66 | $167.84 | $+12.75 | +1.5% |
| TGT | 5 ($764) | $152.86 | $152.86 | $158.11 | $-0.01 | -0.0% |
| TXG | 5 ($358) | $69.59 | $71.64 | $69.75 | $+10.23 | +2.9% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,025)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($297), NEO ($349), NSIT ($354), REPL ($367), TXG ($358)
- **Bull's positions** (7): BNY ($872), DELL ($457), FTNT ($901), ILMN ($808), NUE ($775), SPY ($93), TGT ($764)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($852) — do not size against this until ownership is resolved.
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
