# Portfolio State

**Last Updated**: 2026-10-30 19:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,979.39 |
| Rocket's Allocated Slice (30%) | $2,993.82 |
| Cash Available (shared, pooled) | $334.32 |
| Total Invested (both agents) | $9,645.07 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+2.05%** vs IWM -4.49% → **+6.53 pts** |
| **Rocket own book since 10/6 (new rules)** | **+5.23%** vs IWM -0.76% → **+5.99 pts** |
| **Rocket own book this week** | **+7.12%** vs IWM +1.25% → **+5.87 pts** |
| Rocket return since rebase (SHARED account, not own book) | -1.25% |
| IWM return since rebase | -4.19% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.94% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 101.6% | must be >= 50.0% |
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
| BNY | 6 ($882) | $141.86 | $147.07 | $149.37 | $+31.26 | +3.7% |
| CLDT | 25 ($368) | $14.30 | $14.71 | $14.98 | $+10.25 | +2.9% |
| CRWD | 3 ($751) | $257.46 | $250.44 | $261.15 | $-21.07 | -2.7% |
| FTNT | 6 ($816) | $136.85 | $135.96 | $139.10 | $-5.37 | -0.7% |
| GTLB | 6 ($324) | $56.75 | $54.05 | $56.65 | $-16.23 | -4.8% |
| HPE | 15 ($827) | $56.91 | $55.14 | $58.87 | $-26.53 | -3.1% |
| KELYA | 22 ($364) | $16.41 | $16.55 | $16.26 | $+3.08 | +0.9% |
| MRNA | 4 ($888) | $221.26 | $221.93 | $222.76 | $+2.68 | +0.3% |
| NEO | 21 ($365) | $16.83 | $17.36 | $17.93 | $+11.23 | +3.2% |
| NSIT | 2 ($345) | $162.53 | $172.68 | $178.57 | $+20.30 | +6.2% |
| NUE | 3 ($820) | $248.90 | $273.40 | $275.29 | $+73.50 | +9.8% |
| QMCO | 20 ($365) | $17.62 | $18.23 | $20.77 | $+12.20 | +3.5% |
| REPL | 32 ($563) | $10.99 | $17.59 | $17.39 | $+211.36 | +60.1% |
| STT | 5 ($848) | $165.11 | $169.60 | $173.75 | $+22.45 | +2.7% |
| TGT | 5 ($770) | $152.86 | $153.98 | $151.82 | $+5.60 | +0.7% |
| TXG | 5 ($349) | $69.59 | $69.88 | $81.55 | $+1.43 | +0.4% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CLDT ($368), GTLB ($324), KELYA ($364), NEO ($365), NSIT ($345), QMCO ($365), REPL ($563), TXG ($349)
- **Bull's positions** (6): BNY ($882), CRWD ($751), FTNT ($816), MRNA ($888), NUE ($820), TGT ($770)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - HPE ($827) — do not size against this until ownership is resolved.
  - STT ($848) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 67cfc779… | CRWD | sell | 3 | trailing_stop | new |
| 85effa8c… | FTNT | sell | 6 | trailing_stop | new |
| 5d804037… | MRNA | sell | 4 | trailing_stop | new |
| 6f3717c0… | KELYA | sell | 22 | trailing_stop | new |
| d6f20cea… | CLDT | sell | 25 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| 6ae5ec26… | QMCO | sell | 20 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| 30eae37d… | NEO | sell | 21 | trailing_stop | new |
| 81d4992e… | TXG | sell | 5 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 65d0299a… | HPE | sell | 15 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |
| 7653f815… | BNY | sell | 6 | trailing_stop | new |
| afa14659… | NUE | sell | 3 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
