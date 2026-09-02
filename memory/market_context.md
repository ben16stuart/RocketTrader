# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-02 Wednesday premarket (Week 36 day 3)  ← CURRENT

| Metric | Level | Read |
|---|---|---|
| 🚨 **10-yr** | **4.80%** (+0.80%) | **Second session THROUGH the 4.75% trigger**, and it kept going (4.76% → 4.80%). Six straight sessions grinding up. Lesson 34: a flag stands down on a *trend*, never one print — this is now a trend, in the wrong direction |
| **VIX** | **16.81** (+2.88%) | Third consecutive up day off the two-week low, but **still far below the 22 brake.** No size restriction |
| Russell fut | 2,916.90 (−0.27%) | Risk-off but **orderly, and no longer the worst leg** — Nasdaq −0.59%, S&P −0.27% |
| SPY / IWM | 761.78 (−0.69%) / **290.57 (−1.14%)** | Tuesday's settled closes. **Factor −0.45% on the day** |
| Brent / WTI | 95.15 (+0.53%) / 90.51 (+0.32%) | Both up together again — **second straight confirmed session.** Brent has run $92.33 → $95.15 in one day |

### The rates story is now the whole tape, and it is compounding

The 4.75% flag breached Tuesday at 4.76% and is **4.80% today** — it did not mean-revert.
Simultaneously **Brent is up ~$3 in a session with WTI confirming**, which is inflation
pressure arriving underneath a chair who has already refused forward guidance. **Neither
of these is a one-print artifact any more**, which is exactly the condition lesson 34 set
for taking a flag seriously.

**The designed response for the core remains no action** — the core carries no trailing
stop, backed by 33 years of SPY testing in which every stop configuration lost to
buy-and-hold. **A breached flag is not a licence to override a tested design.** What it
does change: any satellite entered now is entered into a tape where the dominant variable
is rates, not the stock's own catalyst — and today's calendar is dense.

### 🚨 Today's calendar is a three-event day

**ADP 8:15 AM ET** (48K expected vs 44K prior) — lands *before* the open, so it resolves
ahead of any 9:35 decision, which is the good case. Then **Factory Orders AND Durable
Goods at 10:00 AM** — 25 minutes after the decision window — and the **Fed Beige Book at
2:00 PM**, the first since Warsh's hawkish Jackson Hole debut. Then **ISM Services** and
the **August jobs report Friday 9/4**.

### Factor watch

IWM −1.14% vs SPY −0.69% = **−0.45% of factor Tuesday**, carried at 93.7% core weight.
Small on its own (lesson 28: a one-session move carries no information), but it is the
**seventh consecutive week** pointing the same way as the −2.50% since-rebase drift already
escalated to the user. Read it properly in `weekly_review` Friday, not here.

✅ **`market_data.py macro` clean for a third straight session** — every field populated.
🔧 **The scanners degraded to a new worst**: `top_movers` returned **zero usable RelVol
across all 20 names**, and `unusual_volume` had **19 of 20 rows below 1.0× with a
mandate-excluded decliner on top.** See `research_log.md`.

---

## Snapshot — 2026-09-01 Tuesday premarket (Week 36 day 2)

| Metric | Level | Read |
|---|---|---|
| 🚨 **10-yr** | **4.76%** (+1.84%) | **THE 4.75% TRIGGER HAS BREACHED.** Flagged four straight sessions at 8bp → 3bp cushion; today it is **through, by 1bp, on the largest single-session move of the run.** Fifth session grinding up |
| **VIX** | **15.89** (+6.50%) | Second straight +5%+ day off the two-week low, but **still far below the 22 brake.** No size restriction |
| Russell fut | 2,942.20 (**−0.56%**) | Risk-off, but **not the worst leg** — Nasdaq −1.03%, S&P −0.60% |
| SPY / IWM | 767.05 (−0.30%) / **293.93 (−1.96%)** | Monday's closes |
| Brent / WTI | 92.33 (**+2.03%**) / 88.02 (**+2.64%**) | 🆕 **CONFIRMED this time — both up together.** Monday's WTI-only spike was correctly left unconfirmed; the divergence has resolved to the upside |

### 🚨 The trigger fired. The designed response is "no action" — say that out loud

The 4.75% flag was carried for four sessions precisely so it would not be discovered
inside an attribution. It has now breached at **4.76%**, and **energy is confirming**
(Brent *and* WTI up together for the first time in the run) — inflation pressure into a
chair who has already refused forward guidance.

**There is nothing to do, and that is by design, not by neglect.** The core carries no
trailing stop; that choice is backed by 33 years of SPY testing in which every stop
configuration lost to buy-and-hold. **A breached flag is not a licence to override a
tested design.** What it does change: any satellite entered today is entered into a
tape where the dominant variable is rates, not the stock's own catalyst.

### The factor cost 1.5% of the book on Monday alone

**IWM −1.96% vs SPY −0.30% = −1.66% of factor in ONE session**, carried at **93.8%**
core weight ≈ **−1.55% on the book**. Lesson 28 says a one-session factor move carries
no information — **but this one lands on top of the six-week −2.50% drift already
escalated to the user, and in the same direction.** It is not a new signal; it is the
existing signal getting more expensive. Read it properly in `weekly_review`, not here.

**Today: ISM Manufacturing AND JOLTS, both 10:00 AM ET** — 25 minutes after the 9:35
decision window. Then ADP, ISM Services, and the **August jobs report Friday 9/4**.
*(Labor Day 2026 is Mon 9/7 — this is a full trading week.)*

✅ **`market_data.py macro` clean for a second straight session** — every field
populated. 🔧 **The scanners degraded further**: `top_movers` RelVol unusable for **18 of
20** names (14 → 17 → 18 across three sessions), and `unusual_volume` returned **16 of 20
rows below 1.0x with a decliner at the top.** See `research_log.md`.

---

## Snapshot — 2026-08-28 Friday close (end of Week 35)

### 🚨 The week's event: Warsh's Jackson Hole debut ran HAWKISH

Kevin Warsh's **first keynote as Fed chair** (Fri 8/28, 10:00 AM ET) was not the
non-event the tape was priced for: **inflation "still too high," refused forward
guidance, and a majority of investors now price a September HIKE.** He also called for
a "quieter" Fed, telling investors not to look to it for their next trade — itself a
stance.

🥇 **Premarket's read was correct and is the transferable lesson**: VIX at a two-week
low (**14.48**) with **Russell futures printing a 0.3% overnight range on 0.1x volume**
meant *nobody was positioned* — and a debut chair has **no established reaction
function to price against.** That combination was flagged as **the risk, not the
comfort**, and it paid.

**Small caps took it ~7x harder than large caps: IWM −1.35% vs SPY −0.18% on the day.**
Rate-sensitive small caps repricing a hawkish Fed is the direct mechanism.

### Where things stand into Week 36

| Metric | 8/28 close | Read |
|---|---|---|
| **SPY** | **769.35** (−0.23%) | +0.47% on the week |
| **IWM** | **295.75** (−1.40%) | **−1.40% on the week — trailed SPY by 1.88%** |
| **VIX** | 14.48 area, pre-keynote | No brake (22 threshold), but it was **wrong-footed** by Warsh — treat a low VIX into an event as positioning, not calm |
| **10-yr** | **4.67%**, cushion **8bp** to the 4.75% trigger | Third session grinding up, **now with a hawkish chair behind it. Flag stays live and is the number to watch Monday** |

### 🚨 The factor is no longer noise — this is the weekly read lesson 28 asks for

Lesson 28/34 says read IWM−SPY **weekly in the attribution**, never daily. Doing that:

> **Since the 7/20 rebase: IWM +1.18% vs SPY +3.67% = −2.50%**, carried at ~90% weight.

That is **six weeks of drift in one direction**, not a one-session reversal — a
different object from the daily flip-flopping that lesson 28 warns against (the factor
changed sign five times in six sessions in August). **It is Rocket's entire cumulative
deficit to SPY**, while stock selection is **+0.68% and positive**. Escalated to the
user in `strategy.md`; **not self-approved.**

### 🔧 Instrument status — worst degradation on record (lesson 15)

- **`market_data.py macro`** returned mostly `n/a` on **three consecutive calls**
  (yfinance "possibly delisted" for ES/NQ/RTY/SPY/IWM/VIX/TNX/gold/Brent — rate
  limiting). ✅ Gold and Brent were left **unrecorded rather than assumed**.
- **`unusual_volume` returned completely EMPTY output twice** before printing — reads
  identically to "no candidates," the exact lesson-38 blank trap. Re-run until it proved
  it could print.
- **`top_movers`** printed RelVol as `0.0x`/`—` for **17 of 20** names (11 of 20 the day
  before — worsening).
- **`portfolio_snapshot.py`** timed out on the Alpaca clock endpoint twice this week.
- ✅ **Raw daily bars carried every session** and disagreed with the scanner on
  essentially every name — **eight** straight lesson-17a demonstrations.

🚨 **Instrument health is a first-order trading risk now.** A screener this degraded
feeding an "empty board" conclusion is how **PD** — the week's one real beat-and-raise —
never reached the board. See `strategy.md` → SOURCING.

### Carried forward (still current)

- ✅ **Beat-AND-RAISE is the only version that trades.** Beat-without-a-raise **5-for-5**
  as a fader (SVCO, CVRX, FF, LTRX ×2, confirmed by tape).
- ✅ **The analyst ladder is 5-for-5.** OOMA spiked *through* the Street's highest target
  ($24.00 → $26.19) and closed **$23.04, within $0.04 of the consensus mean.**
- ✅ **ARCT's calendar gate paid.** 8/28 −6.1% at 50% of range on 0.6x — first red day,
  volume exhausted 2.1x → 0.6x, readout still undated.
- ⚠️ **The $2B ceiling remains binding** — APPS, BW, HLIT, ETON, UMAC, IE. **Escalated
  to the user; not overridden.**

---
