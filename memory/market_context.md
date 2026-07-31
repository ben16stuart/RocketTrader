# Rocket Market Context

Last updated: 2026-07-31 (Friday, 10:05 AM ET — session ran late, see below)

---

## Snapshot — 2026-07-31 Friday  ← CURRENT

### 🚨 Operational — the premarket routine fired ~85 minutes late
Session started **10:04 AM ET with the market already open**. The 9:45–9:50 base-confirmation
window had passed before any analysis existed, so today's bases were read *after the fact*
rather than traded live. No trades placed (per instruction). This is the **second consecutive
session with an operational failure** — 7/30's was the `close --qty` full liquidation
(lesson 11). **Both belong in weekly_review; check the premarket job's schedule.**

### Account structure
- Shared account **$10,078.66**; Rocket slice (30%) = **$3,023.60**. Pooled cash $1,138.86.
  **Rocket holds IWM 9 sh = $2,607 (86.3%).** JPM + SCHW are Bull's.
- ⚠️ **Reconciler does NOT balance**: **SPY (5 sh, $3,705) is UNATTRIBUTED** — in neither
  agent's trade log. Do not size against it. Resolve at weekly_review.
- Max satellite = **$453** (15%); 1.5% risk = **$45**. Satellite trades this week: **0 / 5**.
- **Rocket -0.27% since rebase vs SPY -0.15% → -0.12% relative.** The +0.61% edge on 7/30 has
  fully reversed and flipped negative in one session — because **IWM fell -1.02% while SPY
  fell -0.10%**. This is the IWM-vs-SPY factor bet the mandate warned about, working against
  Rocket now exactly as it worked for it last week. It was never skill in either direction.
- ⚠️ **Cash back to 13.7% — above the 10% ceiling, no bearish thesis.** Cured Thursday
  morning (10 IWM sh), re-opened Thursday afternoon when the market_close rebalance landed
  on 9 shares and IWM then drew down. Whole-share granularity keeps regenerating this
  (lesson 7a) — **a satellite is the correct cure, not another IWM top-up.**

### Macro — VIX calm, but rates backed up and the Russell is the weak side
- **VIX 17.54 (+2.63%)** — well under the 22 pause threshold. Sizing unrestricted.
- **10-yr 4.73% (+1.42%)** — up from 4.62% on 7/30. This is the meaningful move: the hawkish
  read of Thursday's PCE showing up in the long end.
- Futures: S&P **-0.05%**, Nasdaq **+0.27%**, **Russell 2,934.20 -0.68%** — small caps are
  clearly the weak side today, which is the direct consequence of the rate back-up.
- **Thursday closes: SPY 740.96 -0.10%, IWM 289.62 -1.02%.** Small caps underperformed large
  by ~0.9% in a single session.
- ⚠️ **Brent $90.16 (+1.27%), WTI $85.43 (+2.20%)** — the Iran-driven crude re-spike is
  **still extending for a fourth session** ($86.97 → $91.41 → $90.16 area). The inflation
  impulse behind hike pricing has not faded.
- **Gold $4,082.40 (-0.43%)** — the panic hedge bid from 7/30 came *off*. Dollar 100.39
  (+0.38%). So: no fear in vol or gold, but rates and crude are doing the tightening.
- **Net read**: this is a rates-driven small-cap headwind, not a risk-off event. The IWM
  core will feel it; it is not stopped, by mandate.

### Calendar
- **8:30 AM ET — Employment Cost Index** (already out at session start).
- **10:00 AM ET — Michigan Consumer Survey, final.** No tier-1 event remaining today.
- **🚨 Mon 2026-08-02 — REPL PDUFA decision.** The biggest small-cap binary on the calendar.

### THEME READ (7/31)
- **Catalyst quality is the best all week — two genuine names, not one marginal one.**
  - **CSTL (Castle Biosciences)**: a real **beat-and-raise** — Q2 revenue $103.5M +20% YoY vs
    ~$86M est, EPS -$0.07 vs -$0.44, **FY guide raised $345–355M → $365–375M**, TissueCypher
    volume +63%. Trades 34% below its 52-wk high with a $42.78 street target. Base held the
    9:45 pullback on the lightest volume of the session and reclaimed on rising volume.
  - **AMCX (AMC Global Media)**: the quarter **missed both lines**, but a **$500M / 5-year
    Netflix Walking Dead licensing deal** plus a raised FY guide re-rated it. **21.1% short
    float** — above the squeeze bar — breaking to a **52-week high** on six straight bars of
    accumulation. Caveat: revenue -8.8% YoY, street target $7.50 vs $11.13 spot, consensus
    `underperform`. It is a momentum/squeeze trade, not an investment.
- **The chase rule got its hardest test yet and held: REPL.** FDA AdCom voted **10–3 in
  favor** of RP1 in advanced melanoma on 7/30, overruling FDA staff and reversing two prior
  rejections — a top-tier catalyst. Stock was **halted all day Thursday**, opened **+98%**,
  and has a **PDUFA on 8/02**. Triple disqualifier: 2.8x the chase ceiling, a two-day binary,
  and already fading below its own open. Untradeable at any price today.
- **Small-cap healthcare was violently two-sided.** The four largest volume prints on the
  board were all big *declines* — BIOA -60.6%, MYGN -42.0%, GLUE -31.8%, FLGT -18.4%. That
  is a live caveat on CSTL: its own sector is being repriced hard around it.
- **Scanner overlap did real work again**: JFB and CAPR were the only both-list names, and
  **both failed on inspection** — JFB's "catalyst" is a progress update on a de-SPAC signed
  back in February (issuance risk, opened near the high and distributed every bar), CAPR is
  a bounce off a -36% two-day collapse. The both-scanner filter finds candidates; it does
  not validate them.
- Neither of today's two real catalysts came from the scanner overlap — both came from the
  unusual_volume list plus catalyst validation. Worth noting for screening process.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently 17.54, clear).
- **CSTL entry level $28.60** (9:45 base low) — lost on volume = no trade.
- **AMCX entry level $10.83** (9:40–9:55 floor) — a 52-wk-high breakout; back under = failed.
  Air pocket below to the MA20 at $10.20.
- **Dilution NOT verified on either name.** Run that check before any entry.
- Chase rule: both names are inside the 20% limit but **extended off their bases as of
  10:05 AM** — do not chase into midday.
- Rates are the driver: a further 10-yr back-up pressures the Russell and the IWM core
  directly. Accepted by mandate; the core is not stopped.

---

## Snapshot — 2026-07-30 Thursday Pre-Open  ← PREVIOUS

### Account structure
- Shared account **$9,995.24**; Rocket slice (30%) = **$2,998.57**. Pooled cash $916.64.
  **Rocket holds IWM 9 sh = $2,606 (86.9%).** JPM + SPY are Bull's (reconciler ✅ balanced).
- Max satellite = **$450** (15%); 1.5% risk = **$45**. Trades this week: 1 / 5.
- **Rocket -1.09% since rebase vs SPY -1.70% → +0.61% relative.** Caveat per mandate: this is
  now an *invested* book, and the outperformance is IWM-vs-SPY factor drift, not stock
  selection. `weekly_review` must split beta from skill — do not book this as alpha.
- ⚠️ **Cash 13.1% — above the 10% ceiling, no bearish thesis. Third straight session.**
  Deferred 7/28 (whole-share granularity) and 7/29 (market closed first). **Cure today.**

### 🚨 Event risk — inflation data prints ONE HOUR before the open
- **Thu 7/30 8:30 AM ET — Q2 advance GDP + June PCE/Core PCE.** Consensus GDP **+2.3%**
  (prior +2.1%); **Core PCE +0.1–0.2% m/m, ~3.3% y/y**, easing from a 3-year-high 3.4%.
- **Why it matters more than usual**: the Fed held Wednesday at 3.50–3.75% and Warsh signaled
  patience *despite* the Iran oil re-spike. This is the first inflation read priced against
  that choice. **A hot core PCE reignites hike odds**, and small caps carry the larger tail.
- Because the print lands pre-open, Rocket's 9:45–9:50 base rule resolves it naturally — the
  data is fully digested before any entry is made. No need to alter the entry framework.
- **MSFT/META reported Wed AMC; AAPL + AMZN report tonight (Thu AMC)** — heavy tape risk
  into Friday.

### Macro — calm VIX, but the inflation hedges are bid
- **VIX 19.70 (-4.65%)** — up from 18.24 on 7/29, still comfortably under the 22 pause
  threshold. Sizing not restricted by VIX.
- Futures: S&P **+0.40%**, Nasdaq **+0.78%**, **Russell 2,922.40 +0.24%** — a modest bounce.
- **Wednesday closed red: SPY 729.46 -1.54%, IWM 288.57 -1.64%.** Small caps lagged again on
  the FOMC session, contradicting the 7/29 EOD read that the market "held gains into close."
- 10-yr **4.62%**. Dollar 100.76 (flat).
- ⚠️ **Brent $91.41 (+0.74%)** — the Iran-driven re-spike is **still extending** (was $86.97
  on 7/29, $86 area on 7/28). WTI $84.48. The geopolitical premium is rebuilding, not fading.
- ⚠️ **Gold +2.38% to $4,130.90** — the largest single-day cross-asset move on the board and a
  clear inflation/risk hedge bid the day before core PCE. Read this as the market positioning
  for a hawkish tail, not as risk-on.
- **Net read**: futures green and VIX down look benign, but crude extending + gold spiking is
  the hawkish undercurrent. Treat the surface calm with suspicion until 8:30 clears.

### THEME READ (7/30)
- **Catalyst breadth is NARROW but quality is UP.** Exactly one name — **BOOM (DMC Global)** —
  appears in *both* scanners with a real dated catalyst: Q2 sales $157.0M vs $149.1M est, EPS
  $0.10 vs a forecast loss, **and a raised Q3 guide ($158–168M)**. This is the first genuine
  **beat-and-raise** of the week; NEO's guide on 7/29 was in-line, which is why it failed.
- **Caveat on BOOM**: the beat is *sequential*. Sales were flat YoY and adj. EBITDA fell 21%
  YoY. Net margin is 0.3%. It's a recovery, not growth, and the raise rests entirely on
  Arcadia — a housing/construction-levered unit that a hawkish PCE repricing hits directly.
- **The other both-scanner name, DFNS (+71%, 5.7x RelVol), is a textbook trap** and went on
  the standing avoid list: 1-for-125 reverse split executed purely to hold the Nasdaq listing
  (139.8M shares → 1.12M), leaving a **0.3M float that turns over ~8x a day**; $27.1M net loss
  on $3.65M revenue; and a **$20M private placement** = active dilution. The rules rejected
  this in one `eligibility` call plus one search. Good example of the filters doing real work.
- **Volume gate did the rest of the screening**: ACH, ARCT, TARA and SPIR all *pass* every
  universe gate but print RelVol ≤0.1x. Passing the gates is not a catalyst.
- **Zero small-cap FDA approvals and zero fresh analyst initiations dated 7/29–7/30.** RGNX
  and OFIX are cited as strong July performers but both catalysts are weeks old — month-long
  moves are momentum, not catalysts.
- Premarket gainer tape again dominated by shells and SPACs (BCAR, BTGO, SECZ). Do not chase.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently 19.70, clear).
- **8:30 AM core PCE** — a hot print pressures rate-sensitive small caps and specifically the
  BOOM/Arcadia thesis. It resolves before the open, so no entry rule changes; just read it.
- Chase rule: BOOM at +21.8% is in the 20–35% gap-and-go band → **base entry only**, no spike.
  If it opens >35% above $5.47 (~$7.39+), it converts to a second-day setup.
- Volume gate mandatory: >1.5x avg in the 9:45–9:50 window or no entry.
- Oil headline risk is one-directional right now — further Iran escalation re-spikes crude,
  pressures the tape and the IWM core. The core is not stopped; that is accepted by mandate.
- **AAPL + AMZN tonight AMC** — do not carry oversized satellite risk into Friday's open.

---

## Snapshot — 2026-07-29 Wednesday EOD  ← PREVIOUS

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

## Snapshot — 2026-07-29 Wednesday Pre-Open (superseded)

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

> Older snapshots archived to `memory/archive/market_context_history.md`.
