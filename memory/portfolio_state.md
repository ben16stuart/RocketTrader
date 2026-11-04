# Portfolio State

**Last Updated**: 2026-11-04 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $10,086.80 |
| Rocket's Allocated Slice (30%) | $3,026.04 |
| Cash Available (shared, pooled) | $557.90 |
| Total Invested (both agents) | $9,528.90 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **+3.49%** vs IWM -2.90% → **+6.40 pts** |
| **Rocket own book since 10/6 (new rules)** | **+6.72%** vs IWM +0.88% → **+5.84 pts** |
| **Rocket own book this week** | **+1.24%** vs IWM +1.61% → **-0.37 pts** |
| Rocket return since rebase (SHARED account, not own book) | -0.19% |
| IWM return since rebase | -2.61% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +2.42% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 102.0% | must be >= 50.0% |
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
| CAKE | 3 ($346) | $117.25 | $115.36 | $110.22 | $-5.68 | -1.6% |
| CDNA | 4 ($342) | $86.10 | $85.59 | $88.47 | $-2.02 | -0.6% |
| CLDT | 25 ($374) | $14.30 | $14.98 | $15.02 | $+17.00 | +4.8% |
| CRWD | 3 ($723) | $257.46 | $241.09 | $244.68 | $-49.12 | -6.4% |
| FTNT | 6 ($777) | $136.85 | $129.42 | $128.11 | $-44.58 | -5.4% |
| GTLB | 6 ($314) | $56.75 | $52.39 | $52.37 | $-26.16 | -7.7% |
| HPE | 16 ($801) | $53.24 | $50.05 | $53.10 | $-50.96 | -6.0% |
| ILMN | 3 ($679) | $231.29 | $226.46 | $238.21 | $-14.51 | -2.1% |
| MRK | 5 ($750) | $148.46 | $149.97 | $144.67 | $+7.56 | +1.0% |
| MRNA | 4 ($1,030) | $221.26 | $257.50 | $228.44 | $+144.94 | +16.4% |
| NSIT | 2 ($350) | $162.53 | $175.25 | $167.35 | $+25.43 | +7.8% |
| OABI | 70 ($362) | $5.08 | $5.17 | $5.15 | $+6.65 | +1.9% |
| QMCO | 20 ($336) | $17.62 | $16.79 | $17.67 | $-16.60 | -4.7% |
| REPL | 32 ($661) | $10.99 | $20.64 | $20.65 | $+308.96 | +87.9% |
| STT | 5 ($867) | $165.11 | $173.39 | $169.71 | $+41.40 | +5.0% |
| TGT | 5 ($816) | $152.86 | $163.12 | $154.40 | $+51.30 | +6.7% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CAKE ($346), CDNA ($342), CLDT ($374), GTLB ($314), NSIT ($350), OABI ($362), QMCO ($336), REPL ($661)
- **Bull's positions** (7): CRWD ($723), FTNT ($777), HPE ($801), ILMN ($679), MRK ($750), MRNA ($1,030), TGT ($816)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($867) — do not size against this until ownership is resolved.


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
