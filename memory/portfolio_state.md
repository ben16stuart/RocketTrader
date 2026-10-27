# Portfolio State

**Last Updated**: 2026-10-27 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,480.00 |
| Rocket's Allocated Slice (30%) | $3,144.00 |
| Cash Available (shared, pooled) | $749.95 |
| Total Invested (both agents) | $9,730.05 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+0.86%** vs IWM -4.18% → **+5.03 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.00%** vs IWM -0.44% → **+4.44 pts** |
| **Rocket own book this week** | **+5.87%** vs IWM +1.58% → **+4.29 pts** |
| Rocket return since rebase (SHARED account, not own book) | +3.70% |
| IWM return since rebase | -3.93% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +7.63% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 95.3% | must be >= 50.0% |
| Core (IWM) | 5.4% | absorbs the leftover (no cap since 2026-10-06) |
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
| BNY | 6 ($886) | $141.86 | $147.71 | $147.18 | $+35.07 | +4.1% |
| CLDT | 25 ($363) | $14.30 | $14.51 | $14.18 | $+5.25 | +1.5% |
| DELL | 1 ($502) | $464.53 | $501.78 | $467.09 | $+37.25 | +8.0% |
| FTNT | 5 ($924) | $171.34 | $184.82 | $183.33 | $+67.42 | +7.9% |
| GTLB | 6 ($341) | $56.75 | $56.88 | $56.65 | $+0.81 | +0.2% |
| HPE | 15 ($913) | $56.91 | $60.87 | $58.72 | $+59.46 | +7.0% |
| ILMN | 3 ($838) | $276.76 | $279.49 | $271.04 | $+8.19 | +1.0% |
| IWM | 0.6063 ($170) | $282.37 | $280.09 | $276.99 | $-1.38 | -0.8% |
| KELYA | 22 ($361) | $16.41 | $16.41 | $16.58 | $+0.00 | +0.0% |
| NEO | 21 ($363) | $16.83 | $17.28 | $16.69 | $+9.45 | +2.7% |
| NSIT | 2 ($357) | $162.53 | $178.63 | $178.72 | $+32.20 | +9.9% |
| NUE | 3 ($811) | $248.90 | $270.32 | $257.35 | $+64.26 | +8.6% |
| QMCO | 20 ($404) | $17.62 | $20.20 | $18.69 | $+51.60 | +14.6% |
| REPL | 32 ($418) | $10.99 | $13.05 | $12.47 | $+65.92 | +18.7% |
| SPY | 0.122 ($94) | $763.26 | $770.02 | $765.37 | $+0.82 | +0.9% |
| STT | 5 ($855) | $165.11 | $171.05 | $169.94 | $+29.70 | +3.6% |
| TGT | 5 ($739) | $152.86 | $147.76 | $148.53 | $-25.50 | -3.3% |
| TXG | 5 ($391) | $69.59 | $78.15 | $72.96 | $+42.78 | +12.3% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($170)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CLDT ($363), GTLB ($341), KELYA ($361), NEO ($363), NSIT ($357), QMCO ($404), REPL ($418), TXG ($391)
- **Bull's positions** (7): BNY ($886), DELL ($502), FTNT ($924), ILMN ($838), NUE ($811), SPY ($94), TGT ($739)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($913) — do not size against this until ownership is resolved.
  - STT ($855) — do not size against this until ownership is resolved.


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
