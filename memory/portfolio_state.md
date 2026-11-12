# Portfolio State

**Last Updated**: 2026-11-12 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,728.62 |
| Rocket's Allocated Slice (30%) | $2,918.59 |
| Cash Available (shared, pooled) | $586.43 |
| Total Invested (both agents) | $9,142.19 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$9 (-0.29%)** vs IWM -1.69% · daily loss cap $146: OK |
| **Rocket own book since 7/20** | **+0.90%** vs IWM -4.79% → **+5.69 pts** |
| **Rocket own book since 10/6 (new rules)** | **+4.05%** vs IWM -1.08% → **+5.13 pts** |
| **Rocket own book this week** | **+1.77%** vs IWM +1.70% → **+0.08 pts** |
| Rocket return since rebase (SHARED account, not own book) | -3.73% |
| IWM return since rebase | -4.54% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +0.81% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 103.3% | must be >= 50.0% |
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
| AMPL | 20 ($346) | $17.15 | $17.32 | $17.21 | $+3.30 | +1.0% |
| CAKE | 3 ($318) | $117.25 | $106.03 | $109.67 | $-33.65 | -9.6% |
| CDNA | 4 ($319) | $86.10 | $79.80 | $81.17 | $-25.20 | -7.3% |
| CVX | 4 ($867) | $210.70 | $216.65 | $213.28 | $+23.80 | +2.8% |
| GTLB | 6 ($284) | $56.75 | $47.27 | $47.32 | $-56.91 | -16.7% |
| JNJ | 3 ($851) | $277.80 | $283.69 | $280.41 | $+17.67 | +2.1% |
| MRK | 5 ($735) | $148.46 | $146.96 | $147.18 | $-7.49 | -1.0% |
| NSIT | 2 ($345) | $162.53 | $172.66 | $169.44 | $+20.26 | +6.2% |
| OABI | 70 ($345) | $5.08 | $4.92 | $5.10 | $-10.85 | -3.1% |
| PANW | 2 ($646) | $318.08 | $322.86 | $334.47 | $+9.56 | +1.5% |
| PBF | 5 ($354) | $70.54 | $70.88 | $69.73 | $+1.70 | +0.5% |
| REPL | 32 ($703) | $10.99 | $21.98 | $21.78 | $+351.68 | +100.0% |
| SPY | 0.671 ($508) | $756.33 | $756.89 | $759.81 | $+0.38 | +0.1% |
| STT | 5 ($868) | $165.11 | $173.62 | $174.17 | $+42.52 | +5.2% |
| TGT | 5 ($805) | $152.86 | $160.92 | $162.70 | $+40.30 | +5.3% |
| XOM | 5 ($848) | $164.24 | $169.68 | $166.71 | $+27.18 | +3.3% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($346), CAKE ($318), CDNA ($319), GTLB ($284), NSIT ($345), OABI ($345), PBF ($354), REPL ($703)
- **Bull's positions** (7): CVX ($867), JNJ ($851), MRK ($735), PANW ($646), SPY ($508), TGT ($805), XOM ($848)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($868) — do not size against this until ownership is resolved.


---

## Open Orders

| Order ID | Symbol | Side | Qty | Type | Status |
|----------|--------|------|-----|------|--------|
| 9bc10b9b… | AMPL | sell | 20 | trailing_stop | new |
| dec6ba63… | PBF | sell | 5 | trailing_stop | new |
| 402787f0… | XOM | sell | 5 | trailing_stop | new |
| bc4c3fd4… | CVX | sell | 4 | trailing_stop | new |
| dea7e594… | JNJ | sell | 3 | trailing_stop | new |
| a5a7524a… | PANW | sell | 2 | trailing_stop | new |
| 2eba575a… | CDNA | sell | 4 | trailing_stop | new |
| ff9145d1… | CAKE | sell | 3 | trailing_stop | new |
| 2031c796… | OABI | sell | 70 | trailing_stop | new |
| db547488… | MRK | sell | 5 | trailing_stop | new |
| 656ee463… | GTLB | sell | 6 | trailing_stop | new |
| c47ab843… | NSIT | sell | 2 | trailing_stop | new |
| cd496a08… | REPL | sell | 32 | trailing_stop | new |
| c69037b3… | STT | sell | 5 | trailing_stop | new |
| 4df6cc1d… | TGT | sell | 5 | trailing_stop | new |

---

## Weekly Trade Count

Trades placed this week: 0 / 5 max
Market open: Yes
