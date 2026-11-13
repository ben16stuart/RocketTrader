# Portfolio State

**Last Updated**: 2026-11-13 20:58 UTC
**Account**: Alpaca Paper Trading — SHARED with Bull (merged 2026-07-20)

---

## Account Summary

| Metric | Value |
|--------|-------|
| Shared Account Value (Bull + Rocket) | $9,746.27 |
| Rocket's Allocated Slice (30%) | $2,923.88 |
| Cash Available (shared, pooled) | $586.40 |
| Total Invested (both agents) | $9,159.87 |
| Unrealized P&L (shared) | $+0.00 |
| **Rocket own book TODAY** | **-$10 (-0.34%)** vs IWM -0.36% · daily loss cap $146: OK |
| **Rocket own book since 7/20** | **+0.69%** vs IWM -5.09% → **+5.78 pts** |
| **Rocket own book since 10/6 (new rules)** | **+3.83%** vs IWM -1.39% → **+5.22 pts** |
| **Rocket own book this week** | **+1.56%** vs IWM +1.38% → **+0.19 pts** |
| Rocket return since rebase (SHARED account, not own book) | -3.56% |
| IWM return since rebase | -4.83% |
| Shared account vs IWM (not Rocket's own — use the bold rows) | +1.27% |

### Deployment — Satellite Floor

| Sleeve | % of slice | Rule |
|--------|-----------|------|
| **Satellites (stock picks)** | 102.9% | must be >= 50.0% |
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
| AMPL | 20 ($347) | $17.15 | $17.35 | $17.33 | $+4.00 | +1.2% |
| CAKE | 3 ($327) | $117.25 | $109.04 | $106.20 | $-24.63 | -7.0% |
| CDNA | 4 ($312) | $86.10 | $77.93 | $79.81 | $-32.68 | -9.5% |
| CVX | 4 ($878) | $210.70 | $219.48 | $216.35 | $+35.12 | +4.2% |
| GTLB | 6 ($286) | $56.75 | $47.71 | $47.28 | $-54.25 | -15.9% |
| JNJ | 3 ($857) | $277.80 | $285.77 | $283.52 | $+23.91 | +2.9% |
| MRK | 5 ($739) | $148.46 | $147.79 | $146.95 | $-3.33 | -0.4% |
| NSIT | 2 ($337) | $162.53 | $168.45 | $172.85 | $+11.84 | +3.6% |
| OABI | 70 ($343) | $5.08 | $4.89 | $4.95 | $-12.95 | -3.6% |
| PANW | 2 ($643) | $318.08 | $321.61 | $322.66 | $+7.06 | +1.1% |
| PBF | 5 ($356) | $70.54 | $71.20 | $70.96 | $+3.30 | +0.9% |
| REPL | 32 ($701) | $10.99 | $21.91 | $21.98 | $+349.60 | +99.4% |
| SPY | 0.671 ($506) | $756.33 | $753.67 | $757.12 | $-1.78 | -0.4% |
| STT | 5 ($867) | $165.11 | $173.48 | $173.70 | $+41.85 | +5.1% |
| TGT | 5 ($807) | $152.86 | $161.44 | $160.90 | $+42.92 | +5.6% |
| XOM | 5 ($853) | $164.24 | $170.60 | $169.78 | $+31.82 | +3.9% |

---

## Position Reconciliation

🚨 **Does not balance — see reconciling items below.**

- **Rocket's core** (0): none  — benchmark sleeve; no stop, exempt from position limits
- **Rocket's satellites** (8): AMPL ($347), CAKE ($327), CDNA ($312), GTLB ($286), NSIT ($337), OABI ($343), PBF ($356), REPL ($701)
- **Bull's positions** (7): CVX ($878), JNJ ($857), MRK ($739), PANW ($643), SPY ($506), TGT ($807), XOM ($853)

🚨 **UNATTRIBUTED — held at the broker but in neither trade log:**

  - STT ($867) — do not size against this until ownership is resolved.


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
