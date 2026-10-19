# Portfolio State

**Last Updated**: 2026-10-19 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,931.21 |
| Rocket's Allocated Slice (30%) | $2,979.36 |
| Cash Available (shared, pooled) | $704.75 |
| Total Invested (both agents) | $9,226.46 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-6.83%** vs IWM -7.25% → **+0.42 pts** |
| **Rocket own book since 10/6 (new rules)** | **-3.92%** vs IWM -3.63% → **-0.29 pts** |
| **Rocket own book this week** | **-0.44%** vs IWM +0.25% → **-0.69 pts** |
| Rocket return since rebase (SHARED account, not own book) | -1.73% |
| IWM return since rebase | -6.99% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +5.26% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 0.0% | must be >= 50.0% |
| Core (IWM) | 43.5% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 56.5% | buffer only (<= 10%) |

🚨 **SATELLITE FLOOR BREACHED — 0.0% < 50%.** Rocket is not deployed in enough stock picks (the shortfall sits in IWM, not cash). This is not a market call to sit out. Fill open slots from `python scripts/rank_screen.py` (max 5 new per week); every skipped top-8 name must be a logged VETO.

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
| BNY | 6 ($853) | $141.86 | $142.24 | $143.30 | $+2.28 | +0.3% |
| DELL | 1 ($454) | $464.53 | $454.12 | $451.71 | $-10.41 | -2.2% |
| DK | 4 ($300) | $79.18 | $75.10 | $76.59 | $-16.32 | -5.2% |
| FTNT | 5 ($857) | $171.34 | $171.44 | $169.13 | $+0.50 | +0.1% |
| HPE | 15 ($836) | $56.91 | $55.73 | $55.13 | $-17.64 | -2.1% |
| ILMN | 3 ($787) | $276.76 | $262.49 | $262.54 | $-42.81 | -5.2% |
| IWM | 4.7763 ($1,295) | $290.69 | $271.11 | $270.44 | $-93.54 | -6.7% |
| NEO | 21 ($345) | $16.83 | $16.43 | $16.65 | $-8.29 | -2.3% |
| NSIT | 2 ($327) | $162.53 | $163.59 | $160.47 | $+2.11 | +0.6% |
| NUE | 3 ($783) | $248.90 | $261.09 | $256.29 | $+36.57 | +4.9% |
| REPL | 32 ($352) | $10.99 | $11.02 | $10.86 | $+0.80 | +0.2% |
| SPY | 0.122 ($94) | $768.46 | $766.76 | $763.25 | $-0.21 | -0.2% |
| STT | 5 ($826) | $165.11 | $165.25 | $165.72 | $+0.68 | +0.1% |
| TGT | 5 ($766) | $152.86 | $153.26 | $154.26 | $+2.00 | +0.3% |
| TXG | 5 ($349) | $69.59 | $69.79 | $69.86 | $+0.98 | +0.3% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (1): IWM ($1,295)  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (0): none
- **Bull's positions** (7): BNY ($853), DELL ($454), FTNT ($857), ILMN ($787), NUE ($783), SPY ($94), TGT ($766)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - DK ($300) — do not size against this until ownership is resolved.
  - HPE ($836) — do not size against this until ownership is resolved.
  - NEO ($345) — do not size against this until ownership is resolved.
  - NSIT ($327) — do not size against this until ownership is resolved.
  - REPL ($352) — do not size against this until ownership is resolved.
  - STT ($826) — do not size against this until ownership is resolved.
  - TXG ($349) — do not size against this until ownership is resolved.


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
