# Portfolio State

**Last Updated**: 2026-10-26 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,237.63 |
| Rocket's Allocated Slice (30%) | $3,071.29 |
| Cash Available (shared, pooled) | $734.24 |
| Total Invested (both agents) | $9,503.39 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-2.26%** vs IWM -5.29% → **+3.03 pts** |
| **Rocket own book since 10/6 (new rules)** | **+0.79%** vs IWM -1.60% → **+2.39 pts** |
| **Rocket own book this week** | **+2.60%** vs IWM +0.40% → **+2.21 pts** |
| Rocket return since rebase (SHARED account, not own book) | +1.30% |
| IWM return since rebase | -5.04% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +6.34% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 82.7% | must be >= 50.0% |
| Core (IWM) | 17.7% | absorbs the leftover (no cap since 2026-10-06) |
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
| BNY | 6 ($882) | $141.86 | $147.08 | $145.27 | $+31.32 | +3.7% |
| CLDT | 25 ($354) | $14.30 | $14.15 | $14.03 | $-3.75 | -1.0% |
| DELL | 1 ($468) | $464.53 | $467.76 | $456.44 | $+3.23 | +0.7% |
| FTNT | 5 ($917) | $171.34 | $183.34 | $179.99 | $+60.02 | +7.0% |
| GTLB | 6 ($340) | $56.75 | $56.60 | $56.28 | $-0.90 | -0.3% |
| HPE | 15 ($879) | $56.91 | $58.63 | $56.69 | $+25.86 | +3.0% |
| ILMN | 3 ($813) | $276.76 | $270.88 | $269.42 | $-17.64 | -2.1% |
| IWM | 1.9663 ($544) | $282.38 | $276.85 | $275.75 | $-10.87 | -2.0% |
| NEO | 21 ($351) | $16.83 | $16.70 | $16.59 | $-2.83 | -0.8% |
| NSIT | 2 ($357) | $162.53 | $178.60 | $176.77 | $+32.14 | +9.9% |
| NUE | 3 ($772) | $248.90 | $257.44 | $258.11 | $+25.64 | +3.4% |
| QMCO | 20 ($375) | $17.62 | $18.77 | $17.62 | $+23.00 | +6.5% |
| REPL | 32 ($400) | $10.99 | $12.51 | $11.46 | $+48.48 | +13.8% |
| SPY | 0.122 ($93) | $763.26 | $765.12 | $759.97 | $+0.23 | +0.2% |
| STT | 5 ($849) | $165.11 | $169.81 | $167.83 | $+23.50 | +2.8% |
| TGT | 5 ($744) | $152.86 | $148.81 | $152.76 | $-20.25 | -2.6% |
| TXG | 5 ($364) | $69.59 | $72.89 | $71.55 | $+16.48 | +4.7% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($544)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (7): CLDT ($354), GTLB ($340), NEO ($351), NSIT ($357), QMCO ($375), REPL ($400), TXG ($364)
- **Bull's positions** (7): BNY ($882), DELL ($468), FTNT ($917), ILMN ($813), NUE ($772), SPY ($93), TGT ($744)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($879) — do not size against this until ownership is resolved.
  - STT ($849) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
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
