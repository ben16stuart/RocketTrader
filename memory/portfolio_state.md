# Portfolio State

**Last Updated**: 2026-11-14 16:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,750.25 |
| Rocket's Allocated Slice (30%) | $2,925.07 |
| Cash Available (shared, pooled) | $586.40 |
| Total Invested (both agents) | $9,163.85 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$8 (-0.29%)** vs IWM -0.32% · daily loss cap $146: OK |
| **Rocket own book since 7/20** | **+0.74%** vs IWM -5.05% → **+5.80 pts** |
| **Rocket own book since 10/6 (new rules)** | **+3.89%** vs IWM -1.35% → **+5.24 pts** |
| **Rocket own book this week** | **+1.61%** vs IWM +1.41% → **+0.20 pts** |
| Rocket return since rebase (SHARED account, not own book) | -3.52% |
| IWM return since rebase | -4.80% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.28% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 102.9% | must be >= 50.0% |
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

| Symbol | Shares | Entry Price | Price (⚠️ NOT a settled close) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| AMPL | 20 ($347) | $17.15 | $17.34 | $17.34 | $+3.80 | +1.1% |
| CAKE | 3 ($327) | $117.25 | $109.11 | $109.11 | $-24.42 | -6.9% |
| CDNA | 4 ($312) | $86.10 | $77.88 | $77.88 | $-32.88 | -9.5% |
| CVX | 4 ($880) | $210.70 | $219.89 | $219.89 | $+36.76 | +4.4% |
| GTLB | 6 ($286) | $56.75 | $47.73 | $47.73 | $-54.12 | -15.9% |
| JNJ | 3 ($857) | $277.80 | $285.75 | $285.75 | $+23.85 | +2.9% |
| MRK | 5 ($739) | $148.46 | $147.76 | $147.76 | $-3.49 | -0.5% |
| NSIT | 2 ($338) | $162.53 | $168.76 | $168.76 | $+12.46 | +3.8% |
| OABI | 70 ($344) | $5.08 | $4.91 | $4.91 | $-11.90 | -3.3% |
| PANW | 2 ($644) | $318.08 | $322.24 | $322.24 | $+8.32 | +1.3% |
| PBF | 5 ($356) | $70.54 | $71.28 | $71.28 | $+3.70 | +1.0% |
| REPL | 32 ($700) | $10.99 | $21.89 | $21.89 | $+348.80 | +99.2% |
| SPY | 0.671 ($506) | $756.33 | $754.37 | $754.37 | $-1.31 | -0.3% |
| STT | 5 ($867) | $165.11 | $173.45 | $173.45 | $+41.70 | +5.1% |
| TGT | 5 ($807) | $152.86 | $161.45 | $161.45 | $+42.95 | +5.6% |
| XOM | 5 ($853) | $164.24 | $170.59 | $170.59 | $+31.75 | +3.9% |

⚠️ **The market is CLOSED. The price column is the last trade, which outside
regular hours can be a single thin pre/post-market print — it is NOT a settled
close and must never be recorded as one, quoted as a session move, or used to
decide whether a trailing stop has fired.** Alpaca trailing stops evaluate on
regular-hours trades only. Use the **Prior Settled Close** column for anything
written into memory; re-read live at `market_open`.

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($347), CAKE ($327), CDNA ($312), GTLB ($286), NSIT ($338), OABI ($344), PBF ($356), REPL ($700)
- **Bull's positions** (7): CVX ($880), JNJ ($857), MRK ($739), PANW ($644), SPY ($506), TGT ($807), XOM ($853)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($867) — do not size against this until ownership is resolved.


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
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
