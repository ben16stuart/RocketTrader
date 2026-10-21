# Portfolio State

**Last Updated**: 2026-10-21 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,237.05 |
| Rocket's Allocated Slice (30%) | $3,071.11 |
| Cash Available (shared, pooled) | $992.03 |
| Total Invested (both agents) | $9,245.02 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-3.31%** vs IWM -5.44% → **+2.13 pts** |
| **Rocket own book since 10/6 (new rules)** | **-0.30%** vs IWM -1.75% → **+1.45 pts** |
| **Rocket own book this week** | **+3.31%** vs IWM +2.21% → **+1.10 pts** |
| Rocket return since rebase (SHARED account, not own book) | +1.30% |
| IWM return since rebase | -5.19% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +6.49% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 57.5% | must be >= 50.0% |
| Core (IWM) | 33.4% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 9.0% | buffer only (<= 10%) |

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
| BNY | 6 ($876) | $141.86 | $146.03 | $144.25 | $+24.99 | +2.9% |
| DELL | 1 ($487) | $464.53 | $486.89 | $461.56 | $+22.36 | +4.8% |
| DK | 4 ($312) | $79.18 | $78.10 | $77.63 | $-4.32 | -1.4% |
| FTNT | 5 ($871) | $171.34 | $174.17 | $170.93 | $+14.15 | +1.7% |
| HPE | 15 ($874) | $56.91 | $58.24 | $56.09 | $+20.09 | +2.4% |
| ILMN | 3 ($850) | $276.76 | $283.20 | $267.93 | $+19.34 | +2.3% |
| IWM | 3.7163 ($1,027) | $282.38 | $276.42 | $275.78 | $-22.13 | -2.1% |
| NEO | 21 ($358) | $16.83 | $17.07 | $16.62 | $+4.93 | +1.4% |
| NSIT | 2 ($343) | $162.53 | $171.47 | $164.30 | $+17.88 | +5.5% |
| NUE | 3 ($794) | $248.90 | $264.78 | $261.50 | $+47.64 | +6.4% |
| REPL | 32 ($375) | $10.99 | $11.73 | $11.42 | $+23.68 | +6.7% |
| SPY | 0.122 ($94) | $763.26 | $773.51 | $769.05 | $+1.25 | +1.3% |
| STT | 5 ($842) | $165.11 | $168.46 | $166.58 | $+16.75 | +2.0% |
| TGT | 5 ($763) | $152.86 | $152.52 | $154.00 | $-1.70 | -0.2% |
| TXG | 5 ($378) | $69.59 | $75.57 | $71.46 | $+29.88 | +8.6% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,027)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (5): DK ($312), NEO ($358), NSIT ($343), REPL ($375), TXG ($378)
- **Bull's positions** (7): BNY ($876), DELL ($487), FTNT ($871), ILMN ($850), NUE ($794), SPY ($94), TGT ($763)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($874) — do not size against this until ownership is resolved.
  - STT ($842) — do not size against this until ownership is resolved.


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
