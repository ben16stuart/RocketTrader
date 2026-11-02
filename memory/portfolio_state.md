# Portfolio State

**Last Updated**: 2026-11-02 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,852.02 |
| Rocket's Allocated Slice (30%) | $2,955.61 |
| Cash Available (shared, pooled) | $633.33 |
| Total Invested (both agents) | $9,218.69 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+1.08%** vs IWM -4.58% → **+5.66 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.24%** vs IWM -0.86% → **+5.09 pts** |
| **Rocket own book this week** | **-1.12%** vs IWM -0.14% → **-0.98 pts** |
| Rocket return since rebase (SHARED account, not own book) | -2.51% |
| IWM return since rebase | -4.31% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.80% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 102.1% | must be >= 50.0% |
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
| CAKE | 3 ($339) | $117.25 | $113.08 | $112.64 | $-12.51 | -3.6% |
| CDNA | 4 ($344) | $86.10 | $85.92 | $87.41 | $-0.72 | -0.2% |
| CLDT | 25 ($374) | $14.30 | $14.98 | $14.75 | $+17.00 | +4.8% |
| CRWD | 3 ($725) | $257.46 | $241.67 | $250.43 | $-47.38 | -6.1% |
| FTNT | 6 ($756) | $136.85 | $126.00 | $136.08 | $-65.10 | -7.9% |
| GTLB | 6 ($312) | $56.75 | $52.05 | $54.09 | $-28.20 | -8.3% |
| ILMN | 3 ($679) | $231.29 | $226.41 | $235.99 | $-14.64 | -2.1% |
| MRK | 5 ($744) | $148.46 | $148.73 | $149.52 | $+1.36 | +0.2% |
| MRNA | 4 ($882) | $221.26 | $220.62 | $221.72 | $-2.58 | -0.3% |
| NSIT | 2 ($334) | $162.53 | $166.94 | $172.74 | $+8.82 | +2.7% |
| OABI | 70 ($357) | $5.08 | $5.09 | $5.11 | $+1.05 | +0.3% |
| QMCO | 20 ($334) | $17.62 | $16.68 | $18.27 | $-18.80 | -5.3% |
| REPL | 32 ($623) | $10.99 | $19.46 | $17.61 | $+271.20 | +77.1% |
| SPY | 1.03 ($774) | $752.26 | $751.72 | $755.72 | $-0.56 | -0.1% |
| STT | 5 ($846) | $165.11 | $169.24 | $169.77 | $+20.65 | +2.5% |
| TGT | 5 ($795) | $152.86 | $159.03 | $154.38 | $+30.82 | +4.0% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CAKE ($339), CDNA ($344), CLDT ($374), GTLB ($312), NSIT ($334), OABI ($357), QMCO ($334), REPL ($623)
- **Bull's positions** (7): CRWD ($725), FTNT ($756), ILMN ($679), MRK ($744), MRNA ($882), SPY ($774), TGT ($795)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($846) — do not size against this until ownership is resolved.

🚨 **MISSING — in Rocket's book but not held at the broker:**

  - KELYA — likely a stop fill or manual close. Log the exit in trade_log.md.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| 2031c796… | OABI | sell | 70 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| 24285d5d… | ILMN | sell | 3 | trailing_stop | new |
| 67cfc779… | CRWD | sell | 3 | trailing_stop | new |
| 85effa8c… | FTNT | sell | 6 | trailing_stop | new |
| 5d804037… | MRNA | sell | 4 | trailing_stop | new |
| d6f20cea… | CLDT | sell | 25 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| 6ae5ec26… | QMCO | sell | 20 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
