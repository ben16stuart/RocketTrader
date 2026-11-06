# Portfolio State

**Last Updated**: 2026-11-06 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,594.50 |
| Rocket's Allocated Slice (30%) | $2,878.35 |
| Cash Available (shared, pooled) | $603.41 |
| Total Invested (both agents) | $8,991.09 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-0.81%** vs IWM -6.36% → **+5.54 pts** |
| **Rocket own book since 10/6 (new rules)** | **+2.28%** vs IWM -2.70% → **+4.99 pts** |
| **Rocket own book this week** | **-2.98%** vs IWM -2.00% → **-0.97 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.06% |
| IWM return since rebase | -6.18% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.12% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 104.3% | must be >= 50.0% |
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
| CAKE | 3 ($320) | $117.25 | $106.79 | $110.71 | $-31.38 | -8.9% |
| CDNA | 4 ($314) | $86.10 | $78.54 | $76.33 | $-30.24 | -8.8% |
| CLDT | 25 ($387) | $14.30 | $15.48 | $15.10 | $+29.50 | +8.3% |
| DELL | 2 ($657) | $346.11 | $328.69 | $316.91 | $-34.85 | -5.0% |
| FTNT | 6 ($713) | $136.85 | $118.81 | $122.51 | $-108.24 | -13.2% |
| GTLB | 6 ($288) | $56.75 | $47.98 | $48.99 | $-52.65 | -15.5% |
| MRK | 5 ($734) | $148.46 | $146.86 | $146.94 | $-7.99 | -1.1% |
| MRNA | 4 ($1,015) | $221.26 | $253.80 | $241.46 | $+130.16 | +14.7% |
| NSIT | 2 ($316) | $162.53 | $157.96 | $152.72 | $-9.14 | -2.8% |
| OABI | 70 ($352) | $5.08 | $5.04 | $4.83 | $-3.15 | -0.9% |
| PD | 21 ($330) | $16.56 | $15.73 | $16.23 | $-17.43 | -5.0% |
| REPL | 32 ($694) | $10.99 | $21.68 | $20.02 | $+342.24 | +97.3% |
| SPY | 1.7 ($1,251) | $735.01 | $735.68 | $733.00 | $+1.14 | +0.1% |
| STT | 5 ($829) | $165.11 | $165.74 | $165.23 | $+3.15 | +0.4% |
| TGT | 5 ($790) | $152.86 | $158.03 | $157.95 | $+25.85 | +3.4% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): CAKE ($320), CDNA ($314), CLDT ($387), GTLB ($288), NSIT ($316), OABI ($352), PD ($330), REPL ($694)
- **Bull's positions** (6): DELL ($657), FTNT ($713), MRK ($734), MRNA ($1,015), SPY ($1,251), TGT ($790)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($829) — do not size against this until ownership is resolved.


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
