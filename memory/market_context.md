# Rocket Market Context

Last updated: 2026-07-29 (Wednesday EOD)

---

## Snapshot — 2026-07-29 Wednesday EOD  ← CURRENT

### FOMC Outcome
**Fed HELD at 3.50-3.75%** — priced at 62% pre-session. No surprise. Statement language neutral; no new hawkish signals. Chair Warsh's presser acknowledged Iran oil re-spike but signaled patience on hiking. Market held gains into close. Small caps down -1.1% with broad retreat.

### End-of-Day Account State
- Rocket slice: $2,990.98 (down from $3,051.49 pre-market — lost ~$60, matching IWM -1.1% drawdown)
- IWM 9 sh: $2,594 (-1.1% / -$29.17 on day)
- Cash buffer: $397 (13.3% — still above 10% mandate ceiling)
- **Rocket vs SPY: +0.35%** (outperforming despite flat-to-down day)

### Sessions Today
- No satellites triggered (NEO and VRRM both failed to confirm on 9:45-9:50 base with >1.5x volume)
- No new entries
- Trades this week: 1 (IWM core from 7/28) / 5 max
- **Core rebalance DEFERRED** (market closed at 4:01 PM ET; buffer deployment pushed to tomorrow premarket)

### Tomorrow's Agenda
🚨 **PRIORITY 1**: Buy 1 IWM share (~$288-290) at premarket open to deploy buffer and cure 13.3% cash mandate breach. Target: 96% core / 4% cash. This is non-discretionary.

---

## Snapshot — 2026-07-29 Wednesday Pre-Open  ← PREVIOUS

### Account structure
- SHARED Alpaca account with Bull. Shared value **$10,171.64**; Rocket slice (30%) =
  **$3,051.49**. Pooled cash **$916.64**. **Rocket holds IWM 9 sh = $2,648 (86.8% of slice).**
  JPM + SPY are Bull's (reconciler ✅ balanced).
- Position math: 15% max satellite ≈ **$458**; 1.5% risk ≈ **$46**.
- ⚠️ **Cash 13.2% — above the 10% ceiling with no written bearish thesis.** Live mandate
  breach carried over from 7/28. Cure it today: half-size satellite (→5.8%) or +1 IWM (→3.6%).

### 🚨 Event risk — FOMC TODAY is a live coin-flip
- **Wed 7/29 2:00 PM ET — FOMC decision + Warsh presser.** ~**62% hold** (3.50–3.75%) /
  ~**38% HIKE** (3.75–4.00%). Pricing essentially unchanged from 7/28. **No SEP / no dot
  plot** — statement language and the presser are the entire event. Two hawkish dissents
  expected (Logan, Hammack). Economists polled unanimously expect a hold; the market does not
  fully agree, which is what makes it tradeable risk.
- **A hike surprise hits small caps harder than large.** Half-size any satellite; **no new
  satellite entries after 1:30 PM ET.** The IWM core is a separate question — it is the
  neutral benchmark position and is explicitly **not market-timed**.
- **Thu 7/30 8:30 AM — Q2 GDP advance + June PCE/Core PCE.** Consensus core PCE +0.1% m/m.
- **MSFT + META report tonight (Wed AMC); AAPL + AMZN Thu AMC.** Heavy tape risk into Friday.

### Macro — calm surface, hawkish undercurrent
- **VIX 18.24**, roughly flat vs 18.67. Under the 22 pause threshold → sizing not restricted
  by VIX (FOMC is the reason to halve size, not VIX).
- Futures: S&P +0.2%, Nasdaq-100 slightly red (chip weakness persists), **Russell 2000
  2,971.60 +0.24%** — small caps again the marginally stronger side.
- Tue 7/28 closes: S&P 500 **7,428.78 (+0.21%)**, Dow **52,747.32 (+1.03%)**, Nasdaq
  **24,876.91 (-0.22%)**, R2K **~2,953 (+0.19%)**. Rotation into value/cyclicals, tech soft.
- 10-yr Treasury **4.63%**.

### ⚠️ NEW — the Iran pause has BROKEN
- **Iran resumed strikes overnight**: IRGC ballistic missiles at US Mideast forces; US/Saudi
  retaliatory strikes in eastern Iraq. The fragile pause noted on 7/27–7/28 is over.
- **Brent +3.4% to $86.97; WTI +3.6% to $82.09** — reversing part of the ~16% three-session
  slide into 7/28 (largest since 2020).
- **Why this matters today specifically**: the oil re-spike is the exact inflation impulse
  that tripled hike odds (10.7% on 7/15 → 34.7% on 7/22 → ~38% now). Risk into the 2:00 PM
  print is skewed **more hawkish** than yesterday, not less. Energy names catch a bid;
  rate-sensitive small caps carry more downside tail.

### THEME READ (7/29)
- **Catalyst breadth improved but quality is still MEDIUM.** Two names clear every universe
  filter with a dated 7/28 catalyst: **NEO** (Q2 revenue beat, +11.9% pm) and **VRRM** (Avis
  7-year contract framework, +20.3% pm, 1.4x RelVol — top volume reading in the scan).
  Neither is high conviction: NEO's guide was **in-line, not raised**, and it carries a
  ~$14.16 convertible strike acting as an overhead ceiling; VRRM is a **relief bounce on
  explicitly worse contract terms**, with no CEO and an 8/4 class-action deadline.
- **Liquidity floor did real work today**: RCKY posted the cleanest earnings blowout of the
  session (EPS $1.90 vs $0.35 est) but averages only ~67k shares/day — untradeable. Correctly
  skipped on rules, not on judgment.
- **Zero small-cap FDA approvals and zero fresh analyst initiations** dated 7/28–7/29.
- Premarket gainer tape again dominated by sub-$3 names, sub-$50M shells and SPACs (BCAR,
  DFNS, LGHL, AIIO, ONMD et al). Do not screen-chase.

### ✅ Scanner FIXED — after 7 broken sessions
Root cause: finviz added a **logo cell before the ticker**, shifting every value one column in
the `finviz` library's header map (hence single-letter symbols, $0.00 prices, blank RelVol;
the trailing `Volume` column was dropped entirely). Fixed in `scripts/smallcap_scanner.py` via
a self-disabling `_unshift()` plus a merge of the Overview + Performance + Ownership views.
**RelVol and short float are live for the first time in weeks** — `short_squeeze` now returns
real data (WOLF 71.97%, WYFI 61.12%, LENZ 43.35%, VELO 40.21%). Idea flow is restored.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently 18.24, clear).
- **2:00 PM FOMC** — no new satellite entries after 1:30 PM. A hike print = do not chase the
  knife down; a dovish hold = small caps should lead, but that is a next-session entry.
- Chase rule: no entry >20% above prior close except gap-and-go on a 9:45–9:50 base.
- Volume gate is mandatory: >1.5x avg in the 9:45–9:50 window or no entry (ABAT precedent).
- Oil headline risk now skewed one way — further Iran escalation re-spikes crude and pressures
  the tape and the IWM core. The core is not stopped; that is accepted by mandate.

---

## Snapshot — 2026-07-28 Tuesday Pre-Open (superseded)

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
