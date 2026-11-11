# Portfolio State

**Last Updated**: 2026-11-11 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,789.33 |
| Rocket's Allocated Slice (30%) | $2,936.80 |
| Cash Available (shared, pooled) | $152.89 |
| Total Invested (both agents) | $9,636.44 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+1.23%** vs IWM -3.18% → **+4.41 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.39%** vs IWM +0.60% → **+3.80 pts** |
| **Rocket own book this week** | **+2.11%** vs IWM +3.41% → **-1.31 pts** |
| Rocket return since rebase (SHARED account, not own book) | -3.13% |
| IWM return since rebase | -2.93% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | -0.20% |

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
| AMPL | 20 ($344) | $17.15 | $17.20 | $16.83 | $+1.10 | +0.3% |
| CAKE | 3 ($329) | $117.25 | $109.75 | $108.80 | $-22.50 | -6.4% |
| CDNA | 4 ($326) | $86.10 | $81.45 | $80.77 | $-18.60 | -5.4% |
| CVX | 4 ($853) | $210.70 | $213.15 | $211.22 | $+9.80 | +1.2% |
| GTLB | 6 ($284) | $56.75 | $47.31 | $46.66 | $-56.64 | -16.6% |
| JNJ | 3 ($842) | $277.80 | $280.53 | $280.78 | $+8.19 | +1.0% |
| MRK | 5 ($737) | $148.46 | $147.43 | $148.05 | $-5.17 | -0.7% |
| MRNA | 4 ($994) | $221.26 | $248.51 | $250.83 | $+109.02 | +12.3% |
| NSIT | 2 ($338) | $162.53 | $168.80 | $168.75 | $+12.54 | +3.9% |
| OABI | 70 ($357) | $5.08 | $5.09 | $5.10 | $+1.05 | +0.3% |
| PANW | 2 ($668) | $318.08 | $334.17 | $326.36 | $+32.18 | +5.1% |
| PBF | 5 ($349) | $70.54 | $69.75 | $65.91 | $-3.92 | -1.1% |
| REPL | 32 ($698) | $10.99 | $21.82 | $23.28 | $+346.56 | +98.5% |
| STT | 5 ($872) | $165.11 | $174.37 | $171.62 | $+46.27 | +5.6% |
| TGT | 5 ($814) | $152.86 | $162.76 | $161.78 | $+49.50 | +6.5% |
| XOM | 5 ($833) | $164.24 | $166.58 | $164.47 | $+11.70 | +1.4% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($344), CAKE ($329), CDNA ($326), GTLB ($284), NSIT ($338), OABI ($357), PBF ($349), REPL ($698)
- **Bull's positions** (7): CVX ($853), JNJ ($842), MRK ($737), MRNA ($994), PANW ($668), TGT ($814), XOM ($833)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($872) — do not size against this until ownership is resolved.


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
