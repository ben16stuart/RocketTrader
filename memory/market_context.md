# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-08-28 Friday close (end of Week 35)  ← CURRENT

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
