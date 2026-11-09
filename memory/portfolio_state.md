# Portfolio State

**Last Updated**: 2026-11-09 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,892.30 |
| Rocket's Allocated Slice (30%) | $2,967.69 |
| Cash Available (shared, pooled) | $152.97 |
| Total Invested (both agents) | $9,739.33 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+2.39%** vs IWM -3.35% → **+5.74 pts** |
| **Rocket own book since 10/6 (new rules)** | **+5.58%** vs IWM +0.42% → **+5.16 pts** |
| **Rocket own book this week** | **+3.27%** vs IWM +3.23% → **+0.04 pts** |
| Rocket return since rebase (SHARED account, not own book) | -2.11% |
| IWM return since rebase | -3.07% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +0.96% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 103.0% | must be >= 50.0% |
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
| AMPL | 20 ($347) | $17.15 | $17.36 | $16.70 | $+4.20 | +1.2% |
| CAKE | 3 ($333) | $117.25 | $110.87 | $106.76 | $-19.14 | -5.4% |
| CDNA | 4 ($337) | $86.10 | $84.31 | $78.56 | $-7.16 | -2.1% |
| CVX | 4 ($844) | $210.70 | $211.12 | $212.61 | $+1.68 | +0.2% |
| GTLB | 6 ($283) | $56.75 | $47.12 | $48.09 | $-57.78 | -17.0% |
| JNJ | 3 ($846) | $277.80 | $282.14 | $276.22 | $+13.04 | +1.6% |
| MRK | 5 ($742) | $148.46 | $148.37 | $146.73 | $-0.44 | -0.1% |
| MRNA | 4 ($1,076) | $221.26 | $269.05 | $254.19 | $+191.16 | +21.6% |
| NSIT | 2 ($327) | $162.53 | $163.65 | $158.25 | $+2.24 | +0.7% |
| OABI | 70 ($370) | $5.08 | $5.29 | $5.03 | $+14.35 | +4.0% |
| PANW | 2 ($663) | $318.08 | $331.36 | $313.84 | $+26.55 | +4.2% |
| PBF | 5 ($348) | $70.54 | $69.50 | $67.27 | $-5.20 | -1.5% |
| REPL | 32 ($712) | $10.99 | $22.26 | $21.62 | $+360.64 | +102.5% |
| STT | 5 ($856) | $165.11 | $171.24 | $165.56 | $+30.65 | +3.7% |
| TGT | 5 ($830) | $152.86 | $165.94 | $158.41 | $+65.42 | +8.6% |
| XOM | 5 ($825) | $164.24 | $164.99 | $165.87 | $+3.73 | +0.5% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($347), CAKE ($333), CDNA ($337), GTLB ($283), NSIT ($327), OABI ($370), PBF ($348), REPL ($712)
- **Bull's positions** (7): CVX ($844), JNJ ($846), MRK ($742), MRNA ($1,076), PANW ($663), TGT ($830), XOM ($825)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($856) — do not size against this until ownership is resolved.


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
