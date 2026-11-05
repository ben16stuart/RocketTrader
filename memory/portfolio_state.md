# Portfolio State

**Last Updated**: 2026-11-05 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,462.12 |
| Rocket's Allocated Slice (30%) | $2,838.64 |
| Cash Available (shared, pooled) | $603.47 |
| Total Invested (both agents) | $8,858.65 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-3.10%** vs IWM -7.22% → **+4.12 pts** |
| **Rocket own book since 10/6 (new rules)** | **-0.08%** vs IWM -3.61% → **+3.53 pts** |
| **Rocket own book this week** | **-5.22%** vs IWM -2.91% → **-2.30 pts** |
| Rocket return since rebase (SHARED account, not own book) | -6.37% |
| IWM return since rebase | -6.93% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +0.56% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 103.4% | must be >= 50.0% |
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
| CAKE | 3 ($333) | $117.25 | $110.88 | $115.39 | $-19.11 | -5.4% |
| CDNA | 4 ($307) | $86.10 | $76.75 | $85.86 | $-37.38 | -10.9% |
| CLDT | 25 ($378) | $14.30 | $15.11 | $14.98 | $+20.12 | +5.6% |
| DELL | 2 ($630) | $346.11 | $315.24 | $372.36 | $-61.74 | -8.9% |
| FTNT | 6 ($734) | $136.85 | $122.36 | $129.39 | $-86.94 | -10.6% |
| GTLB | 6 ($293) | $56.75 | $48.76 | $52.37 | $-47.97 | -14.1% |
| MRK | 5 ($734) | $148.46 | $146.75 | $150.36 | $-8.54 | -1.1% |
| MRNA | 4 ($967) | $221.26 | $241.65 | $258.38 | $+81.57 | +9.2% |
| NSIT | 2 ($305) | $162.53 | $152.41 | $175.62 | $-20.24 | -6.2% |
| OABI | 70 ($339) | $5.08 | $4.84 | $5.18 | $-16.45 | -4.6% |
| PD | 21 ($340) | $16.56 | $16.20 | $17.00 | $-7.67 | -2.2% |
| REPL | 32 ($641) | $10.99 | $20.02 | $20.69 | $+288.96 | +82.2% |
| SPY | 1.7 ($1,246) | $735.01 | $732.99 | $766.81 | $-3.43 | -0.3% |
| STT | 5 ($826) | $165.11 | $165.23 | $173.41 | $+0.60 | +0.1% |
| TGT | 5 ($789) | $152.86 | $157.72 | $163.10 | $+24.30 | +3.2% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CAKE ($333), CDNA ($307), CLDT ($378), GTLB ($293), NSIT ($305), OABI ($339), PD ($340), REPL ($641)
- **Bull's positions** (6): DELL ($630), FTNT ($734), MRK ($734), MRNA ($967), SPY ($1,246), TGT ($789)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($826) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| f421c912… | PD | sell | 21 | trailing_stop | new |
| f41e5de4… | DELL | sell | 2 | trailing_stop | new |
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| 2031c796… | OABI | sell | 70 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| 85effa8c… | FTNT | sell | 6 | trailing_stop | new |
| 5d804037… | MRNA | sell | 4 | trailing_stop | new |
| d6f20cea… | CLDT | sell | 25 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
