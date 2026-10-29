# Portfolio State

**Last Updated**: 2026-10-29 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,430.89 |
| Rocket's Allocated Slice (30%) | $3,129.27 |
| Cash Available (shared, pooled) | $679.27 |
| Total Invested (both agents) | $9,751.62 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+6.95%** vs IWM -2.86% → **+9.82 pts** |
| **Rocket own book since 10/6 (new rules)** | **+10.29%** vs IWM +0.92% → **+9.36 pts** |
| **Rocket own book this week** | **+12.27%** vs IWM +2.97% → **+9.30 pts** |
| Rocket return since rebase (SHARED account, not own book) | +3.22% |
| IWM return since rebase | -2.61% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +5.83% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 101.8% | must be >= 50.0% |
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

| Symbol | Shares | Entry Price | Price (LIVE, session open) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| BNY | 6 ($896) | $141.86 | $149.39 | $148.59 | $+45.18 | +5.3% |
| CLDT | 25 ($374) | $14.30 | $14.95 | $14.89 | $+16.25 | +4.5% |
| DELL | 1 ($476) | $464.53 | $475.77 | $493.79 | $+11.24 | +2.4% |
| GTLB | 6 ($339) | $56.75 | $56.57 | $57.97 | $-1.08 | -0.3% |
| HPE | 15 ($885) | $56.91 | $58.99 | $60.33 | $+31.26 | +3.7% |
| ILMN | 3 ($868) | $276.76 | $289.25 | $288.79 | $+37.47 | +4.5% |
| KELYA | 22 ($357) | $16.41 | $16.25 | $16.47 | $-3.63 | -1.0% |
| MRNA | 4 ($892) | $221.26 | $223.00 | $214.16 | $+6.96 | +0.8% |
| NEO | 21 ($377) | $16.83 | $17.95 | $17.99 | $+23.62 | +6.7% |
| NSIT | 2 ($357) | $162.53 | $178.40 | $177.84 | $+31.74 | +9.8% |
| NUE | 3 ($827) | $248.90 | $275.64 | $271.79 | $+80.22 | +10.7% |
| QMCO | 20 ($415) | $17.62 | $20.77 | $20.72 | $+63.00 | +17.9% |
| REPL | 32 ($559) | $10.99 | $17.46 | $16.06 | $+207.04 | +58.9% |
| SPY | 0.122 ($94) | $763.26 | $769.49 | $772.31 | $+0.76 | +0.8% |
| STT | 5 ($870) | $165.11 | $173.90 | $173.54 | $+43.95 | +5.3% |
| TGT | 5 ($758) | $152.86 | $151.56 | $148.96 | $-6.50 | -0.9% |
| TXG | 5 ($408) | $69.59 | $81.65 | $83.62 | $+60.28 | +17.3% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CLDT ($374), GTLB ($339), KELYA ($357), NEO ($377), NSIT ($357), QMCO ($415), REPL ($559), TXG ($408)
- **Bull's positions** (7): BNY ($896), DELL ($476), ILMN ($868), MRNA ($892), NUE ($827), SPY ($94), TGT ($758)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($885) — do not size against this until ownership is resolved.
  - STT ($870) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
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
| cb4662b7… | DELL | sell | 1 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |
| 8211961c… | ILMN | sell | 3 | trailing_stop | new |
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
