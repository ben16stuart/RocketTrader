# Portfolio State

**Last Updated**: 2026-11-10 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,763.59 |
| Rocket's Allocated Slice (30%) | $2,929.08 |
| Cash Available (shared, pooled) | $152.89 |
| Total Invested (both agents) | $9,610.70 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+1.60%** vs IWM -3.95% → **+5.55 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.77%** vs IWM -0.21% → **+4.97 pts** |
| **Rocket own book this week** | **+2.48%** vs IWM +2.59% → **-0.12 pts** |
| Rocket return since rebase (SHARED account, not own book) | -3.39% |
| IWM return since rebase | -3.70% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +0.31% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 103.6% | must be >= 50.0% |
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
| AMPL | 20 ($337) | $17.15 | $16.86 | $17.32 | $-5.90 | -1.7% |
| CAKE | 3 ($326) | $117.25 | $108.62 | $110.96 | $-25.89 | -7.4% |
| CDNA | 4 ($324) | $86.10 | $80.97 | $84.42 | $-20.52 | -6.0% |
| CVX | 4 ($845) | $210.70 | $211.25 | $210.78 | $+2.18 | +0.3% |
| GTLB | 6 ($279) | $56.75 | $46.53 | $47.12 | $-61.32 | -18.0% |
| JNJ | 3 ($843) | $277.80 | $280.89 | $282.11 | $+9.27 | +1.1% |
| MRK | 5 ($740) | $148.46 | $147.98 | $148.76 | $-2.39 | -0.3% |
| MRNA | 4 ($1,004) | $221.26 | $250.93 | $269.00 | $+118.66 | +13.4% |
| NSIT | 2 ($338) | $162.53 | $169.13 | $163.73 | $+13.20 | +4.1% |
| OABI | 70 ($357) | $5.08 | $5.09 | $5.30 | $+1.05 | +0.3% |
| PANW | 2 ($653) | $318.08 | $326.50 | $330.89 | $+16.83 | +2.6% |
| PBF | 5 ($329) | $70.54 | $65.89 | $69.55 | $-23.25 | -6.6% |
| REPL | 32 ($745) | $10.99 | $23.28 | $22.26 | $+393.28 | +111.8% |
| STT | 5 ($858) | $165.11 | $171.69 | $170.88 | $+32.90 | +4.0% |
| TGT | 5 ($810) | $152.86 | $161.91 | $165.90 | $+45.25 | +5.9% |
| XOM | 5 ($823) | $164.24 | $164.62 | $164.73 | $+1.90 | +0.2% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($337), CAKE ($326), CDNA ($324), GTLB ($279), NSIT ($338), OABI ($357), PBF ($329), REPL ($745)
- **Bull's positions** (7): CVX ($845), JNJ ($843), MRK ($740), MRNA ($1,004), PANW ($653), TGT ($810), XOM ($823)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($858) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 9bc10b9b… | AMPL | sell | 20 | trailing_stop | new |
| dec6ba63… | PBF | sell | 5 | trailing_stop | new |
| 402787f0… | XOM | sell | 5 | trailing_stop | new |
| bc4c3fd4… | CVX | sell | 4 | trailing_stop | new |
| dea7e594… | JNJ | sell | 3 | trailing_stop | new |
| a5a7524a… | PANW | sell | 2 | trailing_stop | new |
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| 2031c796… | OABI | sell | 70 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| 5d804037… | MRNA | sell | 4 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
