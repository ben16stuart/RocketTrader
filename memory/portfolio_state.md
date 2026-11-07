# Portfolio State

**Last Updated**: 2026-11-07 16:20 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,594.04 |
| Rocket's Allocated Slice (30%) | $2,878.21 |
| Cash Available (shared, pooled) | $603.41 |
| Total Invested (both agents) | $8,990.63 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book since 7/20** | **-0.86%** vs IWM -6.38% → **+5.52 pts** |
| **Rocket own book since 10/6 (new rules)** | **+2.24%** vs IWM -2.73% → **+4.96 pts** |
| **Rocket own book this week** | **-3.02%** vs IWM -2.03% → **-0.99 pts** |
| Rocket return since rebase (SHARED account, not own book) | -5.06% |
| IWM return since rebase | -6.13% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.07% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 104.2% | must be >= 50.0% |
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

| Symbol | Shares | Entry Price | Price (⚠️ NOT a settled close) | Prior Settled Close | Unrealized P&L | P&L % |
|--------|--------|-------------|---------------|---------------------|----------------|-------|
| CAKE | 3 ($320) | $117.25 | $106.76 | $106.76 | $-31.47 | -8.9% |
| CDNA | 4 ($314) | $86.10 | $78.56 | $78.56 | $-30.16 | -8.8% |
| CLDT | 25 ($388) | $14.30 | $15.50 | $15.50 | $+30.00 | +8.4% |
| DELL | 2 ($657) | $346.11 | $328.53 | $328.53 | $-35.16 | -5.1% |
| FTNT | 6 ($713) | $136.85 | $118.84 | $118.84 | $-108.06 | -13.2% |
| GTLB | 6 ($289) | $56.75 | $48.09 | $48.09 | $-51.96 | -15.3% |
| MRK | 5 ($734) | $148.46 | $146.73 | $146.73 | $-8.64 | -1.2% |
| MRNA | 4 ($1,017) | $221.26 | $254.19 | $254.19 | $+131.72 | +14.9% |
| NSIT | 2 ($316) | $162.53 | $158.25 | $158.25 | $-8.56 | -2.6% |
| OABI | 70 ($352) | $5.08 | $5.03 | $5.03 | $-3.50 | -1.0% |
| PD | 21 ($329) | $16.56 | $15.68 | $15.68 | $-18.48 | -5.3% |
| REPL | 32 ($692) | $10.99 | $21.62 | $21.62 | $+340.16 | +96.7% |
| SPY | 1.7 ($1,250) | $735.01 | $735.29 | $735.29 | $+0.48 | +0.0% |
| STT | 5 ($828) | $165.11 | $165.56 | $165.56 | $+2.25 | +0.3% |
| TGT | 5 ($792) | $152.86 | $158.41 | $158.41 | $+27.75 | +3.6% |

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
- **Rocket's satellites** (8): CAKE ($320), CDNA ($314), CLDT ($388), GTLB ($289), NSIT ($316), OABI ($352), PD ($329), REPL ($692)
- **Bull's positions** (6): DELL ($657), FTNT ($713), MRK ($734), MRNA ($1,017), SPY ($1,250), TGT ($792)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($828) — do not size against this until ownership is resolved.


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
Market open: No
