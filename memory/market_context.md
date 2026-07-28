# Rocket Market Context

Last updated: 2026-07-28 (Tuesday pre-open)

---

## Snapshot — 2026-07-28 Tuesday Pre-Open  ← CURRENT

### Account structure
- SHARED Alpaca account with Bull. Shared value **$10,141.75**; Rocket slice (30%) =
  **$3,042.53**. Pooled cash **$7,987.75**. **Rocket is FLAT — 0 positions.** JPM is Bull's
  (reconciler reports ✅ balanced; the JPM/CAMP discrepancies from 7/27 are resolved).
- Position math: 15% max satellite ≈ **$456**; 1.5% risk ≈ **$46**.
- Rocket +0.36% since 7/20 rebase vs SPY -0.40% → **+0.76% relative** — but this is the
  return on an *uninvested* book. It is not skill; it is the market being flat.

### 🚨 Structural issue — Rocket is ~100% cash with no bearish thesis
The core/satellite mandate adopted **2026-07-27** makes **IWM the default resting state** and
caps cash at a 10% buffer. Rocket holds nothing. Cash above the buffer is an active bet that
small caps fall, and requires a written thesis with a trigger and expiry — none exists.
**Correcting this (buy ~9 IWM) is the highest-priority action of the 7/28 session**, ahead of
any satellite idea. Note for `weekly_review`: once the core is on, divergence from SPY is
partly IWM small-cap beta — split beta from selection, do not book factor drift as alpha.

### Macro — MIXED, and the FOMC risk got bigger
- **VIX 18.67**, up from 17.58 Monday. Still under the 22 pause threshold → full 1.5% sizing.
- **Russell 2000 futures +1.16%** — small caps remain the strong side. But **Nasdaq futures
  turned negative overnight** on an Asia chip selloff following NVDA -5% Monday. Two-sided tape.
- Monday 7/27 close: **R2K +0.6%** (2,948.03), S&P 500 ~flat (7,413.18), Nasdaq -0.2%
  (24,932.08), Dow +0.5%. Small caps outperformed; mega-cap tech dragged.
- **Brent -4.4% to $87.64**, WTI -4.9% to $84.91 — geopolitical premium still unwinding.
- **US–Iran pause is holding but fragile** — both sides have accused each other of violations.
  Hormuz shipping subdued, tanker insurance elevated. Headline risk is two-sided.
- 10-yr yield ~4.64%, pulled back overnight.

### ⚠️ Event risk — FOMC is a live coin-flip, not a formality
- **Wed 7/29 2:00 PM ET — FOMC decision + presser (Chair Warsh).** Market pricing is
  **62% hold (3.50–3.75%) / 38% HIKE (3.75–4.00%)**. **This corrects the 7/27 note, which
  assumed a routine hold.** No SEP/dot-plot; the statement language and Warsh's inflation
  commentary are the event. Iran-driven inflation spillover is the cited hike risk.
- **Thu 7/30 — Q2 GDP advance + June PCE/Core PCE.**
- **Today 7/28**: Consumer Confidence 10:00 AM, Richmond Fed Manufacturing. FOMC day 1 of 2.
- **Implication**: a hike surprise hits small caps harder than large. **No fresh satellite
  risk into Wednesday afternoon.** The IWM core is a different question — it is the neutral
  benchmark position and is not market-timed.

### THEME READ (7/28)
- **Catalyst breadth NARROW for a second straight session.** Only **TRAX** clears the
  universe filters on a dated catalyst, and it is now **day 2 and fading**: closed $42.03
  Monday (+18.3%) but **~9.5% off its $46.45 high**, and is ~$40.80 premarket (-2.9%).
  It never built the required 9:45–9:50 volume base yesterday. Second-day rule does NOT
  trigger (needs >25% gap + close above prior midpoint; it met neither). **LOW conviction.**
- **Biotech binary risk on display**: **MPLT -72.9%** on the ZEPHYR Ph2 split result
  (twice-daily met endpoint, once-daily failed). A reminder of what small-cap biotech
  downside looks like — size accordingly.
- **Premarket gainer tape is again mostly unusable**: sub-$3 (GOSS $0.26, OMH $0.17, ALDX,
  OPK, LVWR) and sub-$50M-cap shells (DFNS, BKYI, POLA, BIYA, EHGO).
- **Zero small-cap analyst initiations/upgrades and zero FDA approvals** dated 7/27–7/28.
- **No verifiable short-squeeze setup** (>15% short float + fresh catalyst) found.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently 18.67, clear).
- **Scanner BROKEN — 5th consecutive session.** Single-letter symbol truncation, $0.00
  prices, RelVol all dashes, absurd quotes (INSP "$10.68", XERS "$124.58"). **Treat as
  unusable.** All idea flow this session came from web research + `market_data.py`.
  This has now cost 5 sessions of screening and needs a fix.
- Chase rule: no entry >20% above prior close except gap-and-go on a 9:45–9:50 base.
- Nasdaq/chip weakness bleeding into the broad tape would hit the IWM core — expected and
  accepted; the core is not stopped.
- Oil headline risk two-sided: a collapse of the Iran pause re-spikes crude and hits the tape.

---

## Snapshot — 2026-07-27 Monday Pre-Open (superseded)

### Account structure
- SHARED Alpaca account with Bull. Shared value **$10,125.55**; Rocket slice (30%) =
  **$3,037.66**. Pooled cash **$7,987.75**. **Rocket is FLAT** — JPM is Bull's only position.
- Position math: 15% max ≈ **$455**; 1.5% risk ≈ **$45**. Sizes are small — accept it.
- Rocket +0.20% since 7/20 rebase vs SPY -0.43% → **+0.63% relative**.

### Macro — FAVORABLE (risk-on), but a narrow window
- **VIX 17.58 (-5.4%)**, down from ~18.6–19.0 Friday. Well under the 22 pause threshold →
  full 1.5% sizing permitted.
- **US–Iran fighting paused** over the weekend → **Brent -7% to sub-$86**, unwinding Friday's
  oil/geopolitical overhang. This is the driver of today's bid.
- Futures: S&P +0.96%, Nasdaq-100 +1.59%, **Russell 2000 +1.27%**. Small caps participating.
- **Russell 2000 +20% YTD vs S&P +11%** — best year since 2003; small caps are LEADING, not
  lagging. Favorable regime for the strategy.
- Partial reversal of the 7/23 mega-cap capex selloff, but that thesis gets retested this week.

### ⚠️ Event risk — the tradeable window is Mon–Tue only
- **Wed 7/29 2:00 PM ET — FOMC decision + presser** (expected hold at 3.75%). Main event.
- **Thu 7/30 — Q2 GDP advance + June PCE/Core PCE.**
- **All week — MSFT, META, AAPL, AMZN earnings.**
- No CPI (next 8/12), no payrolls (next 8/7). Monday itself is light (Durable Goods, Dallas Fed).
- **Implication**: take entries Mon/Tue; tighten stops or scale out before Wednesday 2 PM.
  Do NOT initiate fresh risk into the FOMC print.

### THEME READ (7/27)
- **Catalyst breadth is NARROW.** One in-universe name found across two independent research
  passes: **TRAX** (+21% premarket on the argenx/Forte anti-CD122 M&A read-through). It is a
  *sympathy* trade, gapping to **above its 52-week high and at its consensus PT** — poor entry
  quality despite a real catalyst. Conditional/pass.
- **M&A is today's live theme**: argenx buying Forte (FBRX) at $77/sh cash, ~86% premium, for
  anti-CD122. Watch for further immunology read-throughs.
- **Premarket gainer tape is mostly junk** — reverse-split shells and sub-$3 names (LGHL,
  BIYA, DFNS, MTNB, SXTC, OMH, GMEX). All fail universe filters. Do not screen-chase.
- **Zero small-cap analyst initiations or PT raises** dated 7/24 or 7/27. No verifiable
  short-squeeze setup (>15% short float + fresh catalyst) found.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently ~17.6, clear).
- **Scanner is BROKEN again** — single-letter symbol truncation, $0.00 and wildly wrong prices
  (MRAM "$1572", GBX "+52.9%"). Treat output as unusable; verify every name via
  `market_data.py` + web before sizing. This is now 4+ consecutive sessions.
- Chase rule: no entry >20% above prior close except gap-and-go on a 9:45–9:50 base.
- Dilution rule: skip active S-1/ATM/convertible names. TRAX carries a ~10.5M-share resale
  overhang (not a hard disqualifier, but a real seller risk).
- Oil headline risk is now two-sided in the *other* direction — a collapse of the Iran pause
  would re-spike crude and hit the tape.

---

> Older snapshots archived to `memory/archive/market_context_history.md`.
