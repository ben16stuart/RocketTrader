# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-08-28 Friday premarket (Week 35 day 5)  ← CURRENT

### 🚨 TODAY IS THE EVENT: Warsh keynote 10:00 AM ET — confirmed by search

**Kevin Warsh's first Jackson Hole keynote as Fed chair**, Friday 8/28 **10:00 AM ET**
— thirty minutes after the open. Theme: *"Financial Innovation: Implications for
Payments and Policy."* ✅ **Independently re-verified this session** rather than
inherited from yesterday's file (lesson 39a: a claim copied forward three times is one
unchecked claim read three times).

**PCE is already out** — released **Wed 8/26**, Core PCE **3.3%**. It is not a Friday
event. The keynote is the *only* thing on today's calendar.

### Where things stand

⚠️ **`market_data.py macro` was BADLY degraded this session — see instrument note
below. These levels were assembled from three partial calls plus direct bar pulls,
not from one clean snapshot.**

| Metric | Level | Read |
|---|---|---|
| ✅ **VIX** | **14.48** (−0.21%) | **No brake — 7.5 points under the 22 threshold, and LOWER than yesterday's 14.94.** 🚨 **The tape is priced for a debut Fed chair to say nothing surprising.** That is the risk, not a comfort |
| ⚠️ **10-yr** | **4.67%** (+0.17%) | Cushion to the 4.75% trigger **8bp**, narrowed from 9bp. Third session of grinding back up. **Flag stays live** |
| **S&P fut** | **7738.25** (−0.05%) | Flat |
| 🆕 **Nasdaq fut** | **29603.25** (−0.31%) | **The weakest of the three today — a clean reversal of yesterday, when it was strongest at +1.07%** |
| 🆕 **Russell fut** | **3019.00** (**0.00%**) | **Dead flat. Overnight range 0.3% on 0.1x volume** |
| **WTI** | **83.12** (−0.49%) | Steady after the 8/27 reversal |
| **Dollar** | **99.22** (+0.06%) | Firm, unchanged in character |
| **SPY / IWM (8/27 close)** | **771.10** (+0.66%) / **299.81** (+0.29%) | IWM trailed SPY by 0.37% — the factor drag booked in yesterday's close |

### ✅ Yesterday's "Russell lagging" flag has already reversed — as lesson 28 predicted

On 8/27 this file flagged **"Russell the ONLY red index, second straight −0.11%, while
Nasdaq runs +1.07%"** and correctly declined to trade it. **Today the ordering is
inverted: Nasdaq is the weakest (−0.31%) and Russell is flat (0.00%).**

🥇 **This is now the fourth consecutive one-session macro read that reversed inside 24
hours** (8/20 the 10-yr, 8/26 the crypto theme, 8/27 crude, 8/28 the Russell factor).
**Lesson 28/34 is the most-confirmed rule in this file, and the restraint keeps paying
by not costing anything.** Read the factor weekly in the attribution, never daily.

### 🚨 What the tape is actually saying into the keynote

**Nobody is positioned.** Russell futures printed a **0.3% overnight range on 0.1x
volume**; ES 0.3%; VIX at a two-week low. Every instrument is coiled and flat ahead of
a speaker with **no established reaction function** — a debut chair has never set
policy tone from that podium, so there is no prior to price against.

**Implication for Rocket:** a 7% trailing stop fills at the open, wherever the open is
(lesson 29 mechanics, macro version). It cannot protect against a 10:00 AM repricing.
**Combined with Friday's weekend risk on a 1–5 day hold, the calendar closes the door
on both a same-day and a second-day entry — the same conclusion as yesterday, reached
independently.**

### 🥇 LTRX proved the gap-entry failure mode one day EARLY, with no macro shock needed

Yesterday's kill was graded against the bars (lesson 32c). LTRX **opened $6.68, ran to
$7.07, reversed to $5.80, closed $6.03 — 21.1% range, 18% of range, 2.3x volume.** A
7% trail from that open sits at **$6.21** and the low went straight through it.
**That is the whole argument for the calendar gate, demonstrated on a quiet day.**

### 🔧 Scanner + macro instrument status — WORST degradation recorded (lesson 15)

- **`macro` returned mostly `n/a` on three consecutive calls**, with yfinance reporting
  *"possibly delisted"* for ES/NQ/RTY/SPY/IWM/VIX/TNX/gold/Brent — rate-limiting, not
  delisting. Levels above were reconstructed from **three partial calls with different
  fields succeeding each time**, plus a direct daily-bar pull for the futures.
  ⚠️ **Gold and Brent are still missing and are NOT recorded above** — absent, not zero.
- **`unusual_volume` returned completely EMPTY output twice** before succeeding on the
  third call. An empty screen reads identically to "no candidates" — **exactly the
  lesson-38 blank-result trap.** It was re-run until it proved it could print.
- **`top_movers`** printed RelVol as `0.0x`/`—` for **17 of 20** names (worse than
  yesterday's 11 of 20).
- **`portfolio_snapshot.py`** timed out on the Alpaca clock endpoint on the first call.
- ✅ **Raw daily bars again carried the entire session** and again disagreed with the
  scan on every single name.

### 🔴 market_close UPDATE — Warsh was NOT "nothing surprising"; the coiled-tape flag paid off

Confirmed via search: Warsh's debut ran **hawkish** — inflation "still too high,"
refused forward guidance, and a majority of investors now price a **September hike**.
He also called for a "quieter" Fed, telling investors not to look to it for their next
trade — itself a stance, not the no-news outcome VIX (14.48, two-week low) was priced
for. **IWM sold off −1.35% on the day vs SPY −0.18%** — small caps took the hawkish
repricing harder than large caps, exactly the asymmetric reaction the premarket
"nobody is positioned" note flagged as the risk, not the comfort. No satellite was
open to be hurt by the gap-through-stop mechanics LTRX demonstrated yesterday — the
calendar gate's caution was reinforced, not tested, since the board was already empty
for catalyst-quality reasons.

### Carried forward (still current)

- 🚨 **ARCT** — readout still **"Q3 2026," undated.** Gate held five times; skip cost
  now ≈**+45%**. But volume is exhausting (**1.3x → 0.5x**). Lesson 35 holds.
- ✅ **Beat-AND-RAISE is the only version that trades.** Beat-without-a-raise now
  **5-for-5** as a kill (SVCO, CVRX, FF, LTRX — LTRX confirmed by the tape).
- ✅ **The analyst ladder is 5-for-5.** OOMA spiked *through* the Street's highest
  target ($24.00 → $26.19) and closed at **$23.04, within $0.04 of the consensus mean.**
- ⚠️ **The $2B ceiling remains binding** — APPS, BW, HLIT, ETON, UMAC, IE.
  **Escalated to the user; not overridden.**

---
