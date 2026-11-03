# Portfolio State

**Last Updated**: 2026-11-03 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,968.54 |
| Rocket's Allocated Slice (30%) | $2,990.56 |
| Cash Available (shared, pooled) | $557.93 |
| Total Invested (both agents) | $9,410.61 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+3.36%** vs IWM -4.38% → **+7.73 pts** |
| **Rocket own book since 10/6 (new rules)** | **+6.58%** vs IWM -0.65% → **+7.23 pts** |
| **Rocket own book this week** | **+1.10%** vs IWM +0.07% → **+1.03 pts** |
| Rocket return since rebase (SHARED account, not own book) | -1.36% |
| IWM return since rebase | -4.12% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.76% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 103.1% | must be >= 50.0% |
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
| CAKE | 3 ($331) | $117.25 | $110.28 | $112.95 | $-20.91 | -5.9% |
| CDNA | 4 ($355) | $86.10 | $88.65 | $85.88 | $+10.20 | +3.0% |
| CLDT | 25 ($375) | $14.30 | $14.99 | $15.01 | $+17.25 | +4.8% |
| CRWD | 3 ($734) | $257.46 | $244.77 | $241.81 | $-38.08 | -4.9% |
| FTNT | 6 ($770) | $136.85 | $128.36 | $126.21 | $-50.94 | -6.2% |
| GTLB | 6 ($314) | $56.75 | $52.27 | $52.11 | $-26.91 | -7.9% |
| HPE | 16 ($852) | $53.24 | $53.25 | $51.19 | $+0.16 | +0.0% |
| ILMN | 3 ($715) | $231.29 | $238.22 | $226.58 | $+20.79 | +3.0% |
| MRK | 5 ($722) | $148.46 | $144.34 | $148.36 | $-20.59 | -2.8% |
| MRNA | 4 ($915) | $221.26 | $228.66 | $220.83 | $+29.60 | +3.3% |
| NSIT | 2 ($334) | $162.53 | $167.15 | $166.77 | $+9.23 | +2.8% |
| OABI | 70 ($359) | $5.08 | $5.12 | $5.09 | $+3.15 | +0.9% |
| QMCO | 20 ($355) | $17.62 | $17.75 | $16.73 | $+2.60 | +0.7% |
| REPL | 32 ($662) | $10.99 | $20.68 | $19.49 | $+310.08 | +88.2% |
| STT | 5 ($848) | $165.11 | $169.56 | $169.31 | $+22.25 | +2.7% |
| TGT | 5 ($771) | $152.86 | $154.26 | $158.38 | $+7.00 | +0.9% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CAKE ($331), CDNA ($355), CLDT ($375), GTLB ($314), NSIT ($334), OABI ($359), QMCO ($355), REPL ($662)
- **Bull's positions** (7): CRWD ($734), FTNT ($770), HPE ($852), ILMN ($715), MRK ($722), MRNA ($915), TGT ($771)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($848) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 24eb760e… | HPE | sell | 16 | trailing_stop | new |
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
