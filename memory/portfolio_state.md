# Portfolio State

**Last Updated**: 2026-11-20 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,252.10 |
| Rocket's Allocated Slice (30%) | $2,775.63 |
| Cash Available (shared, pooled) | $511.77 |
| Total Invested (both agents) | $8,740.33 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$95 (-3.35%)** vs IWM -2.79% · daily loss cap $139: OK |
| **Rocket own book since 7/20** | **-5.08%** vs IWM -12.13% → **+7.05 pts** |
| **Rocket own book since 10/6 (new rules)** | **-2.12%** vs IWM -8.70% → **+6.58 pts** |
| **Rocket own book this week** | **-5.78%** vs IWM -7.45% → **+1.67 pts** |
| Rocket return since rebase (SHARED account, not own book) | -8.45% |
| IWM return since rebase | -12.04% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +3.59% |

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

| Symbol | Shares | Entry Price | Price (LIVE, session open) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| AMPL | 20 ($324) | $17.15 | $16.20 | $16.54 | $-18.90 | -5.5% |
| APPN | 6 ($310) | $51.73 | $51.74 | $50.97 | $+0.06 | +0.0% |
| CAKE | 3 ($324) | $117.25 | $107.92 | $112.25 | $-27.98 | -8.0% |
| CBRL | 5 ($353) | $67.16 | $70.64 | $71.67 | $+17.40 | +5.2% |
| CDNA | 4 ($279) | $86.10 | $69.87 | $71.92 | $-64.92 | -18.9% |
| CVX | 4 ($832) | $210.70 | $207.90 | $206.50 | $-11.20 | -1.3% |
| IOVA | 44 ($303) | $7.70 | $6.90 | $7.31 | $-35.20 | -10.4% |
| JNJ | 3 ($811) | $277.80 | $270.29 | $267.14 | $-22.53 | -2.7% |
| KO | 8 ($775) | $95.22 | $96.82 | $96.09 | $+12.79 | +1.7% |
| MRK | 5 ($667) | $148.46 | $133.31 | $132.81 | $-75.77 | -10.2% |
| PANW | 2 ($687) | $318.08 | $343.56 | $361.73 | $+50.96 | +8.0% |
| PAYS | 37 ($364) | $9.38 | $9.84 | $10.06 | $+17.02 | +4.9% |
| STT | 5 ($775) | $165.11 | $155.08 | $161.23 | $-50.15 | -6.1% |
| TGT | 5 ($828) | $152.86 | $165.68 | $167.46 | $+64.10 | +8.4% |
| TXG | 6 ($311) | $55.86 | $51.76 | $57.38 | $-24.60 | -7.3% |
| XOM | 5 ($797) | $164.24 | $159.35 | $158.93 | $-24.45 | -3.0% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($324), APPN ($310), CAKE ($324), CBRL ($353), CDNA ($279), IOVA ($303), PAYS ($364), TXG ($311)
- **Bull's positions** (7): CVX ($832), JNJ ($811), KO ($775), MRK ($667), PANW ($687), TGT ($828), XOM ($797)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($775) — do not size against this until ownership is resolved.


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
Market open: Yes
