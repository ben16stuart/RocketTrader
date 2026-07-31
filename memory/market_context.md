# Rocket Market Context

Last updated: 2026-07-31 (Week 31 weekly review — post-close)
Older snapshots: `memory/archive/market_context_history.md`

---

## Snapshot — 2026-07-31 Friday  ← CURRENT

### ✅ RESOLVED — the premarket delay was a session limit, not a schedule bug
Diagnosed at the Week 31 review. **The launchd schedule is correct**:
`com.benstuart.rocket.premarket` fires at 4:20 AM MDT = **6:20 AM ET**, three hours before
the open. `premarket.log` shows it fired on time and then hit
`You've hit your session limit · resets 9am (America/Denver)` on **opus and again on the
sonnet fallback**, only finishing at ~10:05 AM ET — after the 9:45–9:50 base window.
**Cost: the AMCX entry.** See lesson 12 — token budget is a trading risk.

### 🚨 SEPARATE FINDING — the midday routine has NEVER run
`com.benstuart.rocket.midday.plist` exists (authored 7/22, scheduled 12:15 PM ET) but is
**not loaded in `launchctl` and has never written a log line.** Every "re-check at midday"
plan of the last 9 days silently did nothing. Needs the user to load it (lesson 13).

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
