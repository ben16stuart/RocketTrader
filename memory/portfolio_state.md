# Portfolio State

**Last Updated**: 2026-11-19 21:05 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,413.32 |
| Rocket's Allocated Slice (30%) | $2,824.00 |
| Cash Available (shared, pooled) | $255.84 |
| Total Invested (both agents) | $9,157.48 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$64 (-2.26%)** vs IWM -2.19% · daily loss cap $141: OK |
| **Rocket own book since 7/20** | **-1.78%** vs IWM -9.61% → **+7.83 pts** |
| **Rocket own book since 10/6 (new rules)** | **+1.28%** vs IWM -6.09% → **+7.37 pts** |
| **Rocket own book this week** | **-2.50%** vs IWM -4.80% → **+2.30 pts** |
| Rocket return since rebase (SHARED account, not own book) | -6.85% |
| IWM return since rebase | -9.38% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.53% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 92.6% | must be >= 50.0% |
| Core (IWM) | 0.0% | absorbs the leftover (no cap since 2026-10-06) |
| Cash | 7.4% | buffer only (<= 10%) |

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
| AMPL | 20 ($331) | $17.15 | $16.54 | $16.89 | $-12.20 | -3.6% |
| CAKE | 3 ($337) | $117.25 | $112.38 | $120.05 | $-14.61 | -4.2% |
| CBRL | 5 ($358) | $67.16 | $71.67 | $74.34 | $+22.55 | +6.7% |
| CDNA | 4 ($288) | $86.10 | $71.92 | $74.44 | $-56.72 | -16.5% |
| CVX | 4 ($826) | $210.70 | $206.50 | $205.88 | $-16.80 | -2.0% |
| GTLB | 6 ($262) | $56.75 | $43.68 | $44.50 | $-78.42 | -23.0% |
| IOVA | 44 ($322) | $7.70 | $7.31 | $7.48 | $-17.07 | -5.0% |
| JNJ | 3 ($801) | $277.80 | $267.00 | $272.70 | $-32.40 | -3.9% |
| KO | 8 ($769) | $95.22 | $96.12 | $98.09 | $+7.19 | +0.9% |
| MRK | 5 ($664) | $148.46 | $132.81 | $137.78 | $-78.24 | -10.5% |
| PANW | 2 ($727) | $318.08 | $363.50 | $339.92 | $+90.84 | +14.3% |
| PAYS | 37 ($372) | $9.38 | $10.06 | $10.07 | $+25.16 | +7.2% |
| SPY | 0.445 ($318) | $731.83 | $715.11 | $730.20 | $-7.44 | -2.3% |
| STT | 5 ($806) | $165.11 | $161.23 | $165.15 | $-19.40 | -2.4% |
| TGT | 5 ($837) | $152.86 | $167.46 | $165.93 | $+73.00 | +9.6% |
| TXG | 6 ($344) | $55.86 | $57.38 | $57.07 | $+9.12 | +2.7% |
| XOM | 5 ($795) | $164.24 | $158.93 | $160.58 | $-26.55 | -3.2% |

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
- **Rocket's satellites** (8): AMPL ($331), CAKE ($337), CBRL ($358), CDNA ($288), GTLB ($262), IOVA ($322), PAYS ($372), TXG ($344)
- **Bull's positions** (8): CVX ($826), JNJ ($801), KO ($769), MRK ($664), PANW ($727), SPY ($318), TGT ($837), XOM ($795)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($806) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
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
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: No
