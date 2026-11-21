# Portfolio State

**Last Updated**: 2026-11-21 16:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,262.75 |
| Rocket's Allocated Slice (30%) | $2,778.82 |
| Cash Available (shared, pooled) | $511.74 |
| Total Invested (both agents) | $8,751.01 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$95 (-3.37%)** vs IWM -2.88% · daily loss cap $139: OK |
| **Rocket own book since 7/20** | **-5.10%** vs IWM -12.21% → **+7.12 pts** |
| **Rocket own book since 10/6 (new rules)** | **-2.14%** vs IWM -8.79% → **+6.65 pts** |
| **Rocket own book this week** | **-5.80%** vs IWM -7.54% → **+1.74 pts** |
| Rocket return since rebase (SHARED account, not own book) | -8.34% |
| IWM return since rebase | -11.98% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +3.64% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 92.4% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 7.6% | buffer only (<= 10%) |

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
| AMPL | 20 ($324) | $17.15 | $16.20 | $16.20 | $-19.00 | -5.5% |
| APPN | 6 ($311) | $51.73 | $51.79 | $51.79 | $+0.36 | +0.1% |
| CAKE | 3 ($324) | $117.25 | $107.94 | $107.94 | $-27.91 | -7.9% |
| CBRL | 5 ($354) | $67.16 | $70.75 | $70.75 | $+17.95 | +5.3% |
| CDNA | 4 ($280) | $86.10 | $70.00 | $70.00 | $-64.40 | -18.7% |
| CVX | 4 ($833) | $210.70 | $208.37 | $208.37 | $-9.32 | -1.1% |
| IOVA | 44 ($304) | $7.70 | $6.90 | $6.90 | $-35.07 | -10.4% |
| JNJ | 3 ($811) | $277.80 | $270.47 | $270.47 | $-21.99 | -2.6% |
| KO | 8 ($776) | $95.22 | $96.99 | $96.99 | $+14.15 | +1.9% |
| MRK | 5 ($669) | $148.46 | $133.72 | $133.72 | $-73.69 | -9.9% |
| PANW | 2 ($687) | $318.08 | $343.32 | $343.32 | $+50.48 | +7.9% |
| PAYS | 37 ($362) | $9.38 | $9.79 | $9.79 | $+15.17 | +4.4% |
| STT | 5 ($777) | $165.11 | $155.38 | $155.38 | $-48.65 | -5.9% |
| TGT | 5 ($829) | $152.86 | $165.83 | $165.83 | $+64.85 | +8.5% |
| TXG | 6 ($311) | $55.86 | $51.80 | $51.80 | $-24.36 | -7.3% |
| XOM | 5 ($800) | $164.24 | $159.99 | $159.99 | $-21.25 | -2.6% |

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
- **Rocket's satellites** (8): AMPL ($324), APPN ($311), CAKE ($324), CBRL ($354), CDNA ($280), IOVA ($304), PAYS ($362), TXG ($311)
- **Bull's positions** (7): CVX ($833), JNJ ($811), KO ($776), MRK ($669), PANW ($687), TGT ($829), XOM ($800)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($777) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| c4a03799… | APPN | sell | 6 | trailing_stop | new |
| 28312c92… | KO | sell | 8 | trailing_stop | new |
| 39ae6bab… | CBRL | sell | 5 | trailing_stop | new |
| 66b0d7ff… | PAYS | sell | 37 | trailing_stop | new |
| f2eb8105… | IOVA | sell | 44 | trailing_stop | new |
| ab2f8825… | TXG | sell | 6 | trailing_stop | new |
| 9bc10b9b… | AMPL | sell | 20 | trailing_stop | new |
| 402787f0… | XOM | sell | 5 | trailing_stop | new |
| bc4c3fd4… | CVX | sell | 4 | trailing_stop | new |
| dea7e594… | JNJ | sell | 3 | trailing_stop | new |
| a5a7524a… | PANW | sell | 2 | trailing_stop | new |
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
