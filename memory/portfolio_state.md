# Portfolio State

**Last Updated**: 2026-10-28 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,623.22 |
| Rocket's Allocated Slice (30%) | $3,186.97 |
| Cash Available (shared, pooled) | $749.93 |
| Total Invested (both agents) | $9,873.29 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+5.93%** vs IWM -3.85% → **+9.77 pts** |
| **Rocket own book since 10/6 (new rules)** | **+9.23%** vs IWM -0.10% → **+9.33 pts** |
| **Rocket own book this week** | **+11.20%** vs IWM +1.93% → **+9.27 pts** |
| Rocket return since rebase (SHARED account, not own book) | +5.12% |
| IWM return since rebase | -3.60% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +8.72% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 99.0% | must be >= 50.0% |
| Core (IWM) | 5.3% | absorbs the leftover (no cap since 2026-10-06) |
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

| Symbol | Shares | Entry Price | Price (LIVE, session open) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| BNY | 6 ($892) | $141.86 | $148.62 | $147.58 | $+40.56 | +4.8% |
| CLDT | 25 ($372) | $14.30 | $14.88 | $14.56 | $+14.50 | +4.1% |
| DELL | 1 ($494) | $464.53 | $494.14 | $501.96 | $+29.61 | +6.4% |
| FTNT | 5 ($870) | $171.34 | $173.99 | $185.00 | $+13.25 | +1.5% |
| GTLB | 6 ($348) | $56.75 | $57.94 | $56.82 | $+7.14 | +2.1% |
| HPE | 15 ($905) | $56.91 | $60.31 | $60.84 | $+51.06 | +6.0% |
| ILMN | 3 ($868) | $276.76 | $289.23 | $279.47 | $+37.40 | +4.5% |
| IWM | 0.6063 ($170) | $282.37 | $281.06 | $280.18 | $-0.79 | -0.5% |
| KELYA | 22 ($361) | $16.41 | $16.42 | $16.45 | $+0.22 | +0.1% |
| NEO | 21 ($377) | $16.83 | $17.95 | $17.27 | $+23.52 | +6.7% |
| NSIT | 2 ($356) | $162.53 | $178.01 | $178.35 | $+30.96 | +9.5% |
| NUE | 3 ($815) | $248.90 | $271.62 | $270.79 | $+68.14 | +9.1% |
| QMCO | 20 ($414) | $17.62 | $20.71 | $20.25 | $+61.80 | +17.5% |
| REPL | 32 ($509) | $10.99 | $15.91 | $13.05 | $+157.44 | +44.8% |
| SPY | 0.122 ($94) | $763.26 | $771.80 | $769.66 | $+1.04 | +1.1% |
| STT | 5 ($868) | $165.11 | $173.60 | $170.89 | $+42.48 | +5.1% |
| TGT | 5 ($742) | $152.86 | $148.46 | $148.01 | $-22.00 | -2.9% |
| TXG | 5 ($418) | $69.59 | $83.64 | $78.02 | $+70.23 | +20.2% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($170)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CLDT ($372), GTLB ($348), KELYA ($361), NEO ($377), NSIT ($356), QMCO ($414), REPL ($509), TXG ($418)
- **Bull's positions** (7): BNY ($892), DELL ($494), FTNT ($870), ILMN ($868), NUE ($815), SPY ($94), TGT ($742)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($905) — do not size against this until ownership is resolved.
  - STT ($868) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
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
