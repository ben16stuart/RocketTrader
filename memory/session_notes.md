# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-09-01 — PREMARKET (Tuesday, Week 36 day 2) — ONE LIVE CANDIDATE: YEXT, gates pre-committed

Book **$3,081.26** = IWM 9.8636 sh @ $292.92 ($2,889.25, **93.8%**) + notional cash
$192.01 (**6.2%**, inside the buffer — no bearish thesis owed). Satellites 0/4, weekly 0/5.

- 🥇 **The earnings calendar produced a name this time.** Lesson 41's first step ran before
  any screener: today's reporters gated down to **YEXT (BMO today, in universe)** and
  **ANAB (AMC today, killed on rule 13 — +25% target = $2,111M, through the $2B lid)**.
  RGS (ADV 5,798) and SPWH ($1.19 / $46M cap) failed outright. **4 tickers requested, 4
  rows returned — counted (lesson 43).** Monday 8/31 after-close had exactly one reporter,
  CANG, China-domiciled — a second verifiably-empty overnight slate, not a missing one.
- 🔎 **YEXT confirmed BMO today from company IR** — so the print lands in the premarket
  window and it is a legitimate same-day candidate under the earnings-week guardrail.
  ✅ **Dilution is the cleanest tier on the book**: EDGAR file proven populated (1,000
  filings, 2018-06-22 → 2026-07-13), and the **only** offering-type filings in seven years
  are a **2019 S-3ASR + 424B5** — a shelf that lapsed in 2022. S-8s only since (lesson 8b).
- ⚠️ **But the ladder is already the binding gate before the print.** Dated 4-analyst page:
  mean **$7.50**, high $10.00 (Needham 8/18), Zacks cut to hold 8/21. At $6.77 the **+15%
  rung is $7.79 — above the mean.** ⇒ **zero-rung on the mean at today's price**, and any
  gap up moves the rungs while the pre-print mean stays put. Not the OOMA/PD shape (the
  high clears both rungs) — the softer failure. Also: **rule 40a puts the catalyst-day
  range at 7.8–12.6% against a 7% trail** (trailing mean 3.4% × PD/LTRX multiples), and
  8/31 **closed at 23% of range on ~1.9x volume** — mild distribution into the print.
- 🚨 **Four pass/kill conditions written BEFORE the print (lesson 42)**: (1) FY27 revenue
  guide raised **>2%**, stated as a %; (2) **dated post-print mean above 1.15 × actual
  entry** — requires a same-day Street markup, the test that killed PD; (3) rule 2a/2b at
  the open; (4) rule 2c gap size. **Honest prior: most likely a kill on gate 2.**
- 🚨 **The 10-yr trigger BREACHED — 4.76% vs the 4.75% flag carried for four sessions**,
  with **Brent and WTI confirming together** for the first time. The designed response is
  **no action** (core has no stop, backed by 33 years of testing) — recorded as a decision,
  not an omission. Monday's factor: **IWM −1.96% vs SPY −0.30% ≈ −1.55% on the book.**
- 🆕 **Rebalance-base divergence found — flagged to market_close, not acted on (rule 6).**
  Slice basis says IWM is **+0.30%** (in band, no trade); book basis says **+3.77%**
  (outside the 3% band, indicates a SELL). **Lesson 23a says the book is valid; 8/31's
  market_close used the slice and bought.** See new lesson 44.
- 🔧 Scanners degraded further: `top_movers` RelVol unusable for **18 of 20** (14→17→18),
  `unusual_volume` **16 of 20 rows below 1.0x with a decliner on top.** Overlap tier was
  NEOV alone at 0.2x — and NEOV reports 9/02, so it is barred regardless.

**No trades placed — market closed. No notification sent (no breaking news on an open
position; the only position is the stopless IWM core).**

---

## 2026-08-31 — MARKET_CLOSE (Monday, Week 36 day 1) — CORE REBALANCE, IWM BUY

No satellites to review (0/4). Core rebalance triggered for the first time since
8/26: slice **$3,221.73**, target_core **$2,899.56**, live IWM **$2,790.67 — 3.38%
of slice short**, just outside the 3% band → bought **0.3704 sh @ $293.958**
($108.89), landing on target at **9.8636 sh / $2,900.14**. Full detail and day P&L
in `trade_log.md`.

Day: IWM −0.55%/−$16.13 vs SPY −0.47% (~0.08% trail, factor drag on a broad
risk-off Monday). Since-rebase figure not recomputed here — the 8/28
weekly-review chain (**Rocket vs SPY: −1.27%**) stands until next `weekly_review`.
ntfy sent and confirmed. No new lesson — routine mechanical rebalance.

## 2026-08-31 — MARKET_OPEN (Monday, Week 36 day 1) — NO TRADE, confirms premarket

Validated premarket's "no satellite" call against real open data — it held. Overlap
tier (top_movers ∩ unusual_volume): **NEOV** (+25.1–25.6%, 11.1x scanner / 2.1x live
avg) was the only name of substance; everything else on both lists was either a
closed-end fund/large-financial (mandate-excluded by sector/size) or a sub-4% mover.

- 🔎 **NEOV re-checked on live bars, not Friday's** — this time the move is **real**
  (detail pull confirms +25.6%, 2.1x avg volume, not a scanner artifact). No confirmed
  same-day catalyst found by search (candidates: Georgia plant commissioning
  end-of-August target, an undated ~$200M BESS supply LOI) — neither pinned to today.
  **Moot regardless: earnings print 9/02 is 2 trading days out — earnings-week
  guardrail forbids entry before a confirmed print.** 🆕 Also surfaced an 8/11 filing
  to sell 4.5M shares — an ungraded rule-8 dilution flag for if NEOV is re-screened
  post-print.
- PD and RMNI: no new information since premarket: both remain killed (ladder /
  no dated catalyst respectively). Not re-checked at the open — nothing changed.

**Result: 0/4 satellites, 100% IWM core held.** No rebalance (market_close only,
rule 6). No notification — flat session. NEOV is the one name worth a same-time-next-
session look, but only *after* 9/02 and only after grading the dilution filing.

---

## 2026-08-31 — PREMARKET (Monday, Week 36 day 1) — NO SATELLITE, hold IWM

Board built, both named candidates killed on **dated** evidence. Book **$3,106.43** =
IWM 9.4932 sh (90.3%) + $300.90 cash (9.7%, inside the buffer — no bearish thesis owed).
Satellites 0/4, weekly 0/5. Core is **0.31% from target — well inside the 3% band**, and
rebalancing is market_close-only regardless. **No action for the 9:35 session.**

- ✅ **Lesson 41's new first step ran and worked.** Earnings calendar before any
  screener: Monday before-open is **LX, SAIC, SY** — LX/SY China-domiciled
  (mandate-excluded), **SAIC cap $5.3B (gate fail)**. **An empty slate from a source
  that cannot silently go blank** — the exact distinction 41b was written for.
- 🚫 **PD KILLED — the ladder gate was tested against Friday's own stated condition and
  REFUTED.** Dated 9-analyst page: **mean $12.64, 8.6% BELOW Friday's $13.83 close; high
  target $15.00 sits under the +15% rung ($15.90)**; rating **Hold**. The Street *did*
  revise up on 8/28 (Truist $13→$15, Canaccord $10→$15, BofA $8→$9.50 **Sell**) and
  **still landed at/below the high — marking up did not un-cap it.** This is the **OOMA
  shape**, lesson 11's cleanest case. **Ladder 6-for-6.**
- 🆕 **The research log's "$18.70 consensus" was undated and is off by 48%** vs a dated
  page. **Rule 11a paid again.**
- 🆕 **Rocket's own files over-graded the PD catalyst (lesson 39a).** Called "Rung 1, the
  only type that has made money" — but revenue was **FLAT YoY** and the FY guide moved
  **$492.5M → $494M = +0.3%.** ETON's was $120M+ → "exceed $145M." **A 0.3% nudge on flat
  revenue sits nearer lesson 5's beat-without-a-raise (5-for-5 fader) than beside ETON.**
  Label inherited across three sessions, never re-checked. Rung 1 needs a **size** bar.
- ✅ **PD's dilution check passed cleanest-tier** — EDGAR 688 filings (populated, lesson
  38), **no S-3/424B5/S-1 since Jan 2025**, only S-8s (8b). **A spotless balance sheet
  did not rescue a capped ladder** — the gates are independent, and that is the point.
- 🚫 **RMNI killed on rule 1 for the second session.** Still no dated 8/27–8/28 catalyst;
  only "hit a 52-week high" (**a description of the move, lesson 33**) + Roth $6.50
  (7/30) and an 8/01 upgrade, both stale. Ladder capped too: **+15% = $6.50 = exactly
  Roth's target.**
- 🚫 **NEOV/FLWS/SPIR killed on raw bars before any research spend** — ninth straight
  lesson-17a demonstration. Scanner's NEOV "+11.8%, 1.9x" was really **−5.9%, 4% of
  range, on its lowest volume in 8 sessions**, and it **reports 9/02 (+2d)** — the
  earnings-week guardrail forbids entry before a print.
- 🔧 **New instrument failure: `eligibility` silently omitted PD from a 6-ticker call**,
  printed the other five, exited 0. **A missing row is indistinguishable from a clean
  run (lesson 38).** Re-run alone it worked. **Count rows against tickers requested.**
  `top_movers` RelVol still broken (14 of 20).
- 🚨 **10-yr 4.72% — cushion to the 4.75% trigger is 3bp, down from 8bp.** Fourth session
  up, hawkish Warsh behind it, **IWM at ~90% weight**, and a four-event macro week (ISM,
  JOLTS, ADP, **jobs report 9/4**). Nothing to do — the core is stopless by design — but
  named now rather than discovered in an attribution later.

---

## 2026-08-28 — WEEKLY REVIEW (Week 35, Friday post-close) — Grade C

**Book $3,173.17 → $3,108.52 = −2.04% vs SPY +0.47% → Rocket vs SPY −2.51%**, worst
relative week of the core/satellite regime. **Since rebase: Rocket +2.40% vs SPY +3.67%
= −1.27%** — back negative from +1.35% last Friday. Full detail: `weekly_reviews/2026-W35.md`.

- 🚨 **Not one basis point of the −2.51% came from a decision made this week.**
  Attribution: **factor −1.63%** (the IWM core), **OMER's within-week giveback −0.85%**
  (opened 8/14, stop fired correctly), cash −0.04%. **New satellite decisions: 0,
  contributing exactly 0.00%.**
- 🚨 **THE PROBLEM INVERTED.** Real alpha is **+0.68% and positive** since the rebase;
  the entire deficit is the core instrument — **IWM +1.18% vs SPY +3.67% = −2.50%** at
  ~90% weight. W33's "beat" was booked as 100% factor; **the same honesty applies now
  that it hurts.** Escalated to the user in `strategy.md`, **not self-approved** — and
  note the non-negotiable constraint: Bull holds SPY in the same pooled account, so any
  alternative core must preserve distinct tickers for attribution.
- ❌ **THE ONE REAL FAILURE — NEW LESSON 41.** **PagerDuty (PD)** reported a **beat AND
  raise** 8/27 after the close (FY rev → $494M, FY adj EPS → $1.35) and traded 8/28
  **+9.5%, 69% of range, 2.7x volume.** **It appears in none of Friday's three session
  notes.** Rung 1 — the only catalyst type that has ever made money — and Rocket was
  waiting for it to surface through a screener that reports extended-hours quotes as
  prices, printed `0.0x` RelVol for 17 of 20 names, and **returned empty output twice.**
  **Coverage gap, not discipline gap.** New mandatory premarket step: **pull the
  overnight earnings calendar and ask "was guidance RAISED?" BEFORE any screener.**
- ✅ **Five skips graded against the bars, five correct** (lesson 32c): LTRX (21.1% range,
  blew through a 7% trail), OOMA (spiked through the Street's high target, closed within
  $0.04 of the mean — **ladder 5-for-5**), BBW (8/27 −27.3% guidance cut, 8/28 is the
  dead-cat), OSG (39% of range on 3.8x = distribution), **ARCT (first red day, −6.1% at
  50% of range on 0.6x, volume exhausted 2.1x → 0.6x — the gate that cost ≈+45% has
  paid; lesson 35 vindicated).**
- ✅ **OMER: +$30.53 / +6.60% / +0.87R, 12 days, exited mechanically with zero
  discretionary intervention** — lesson 32a's first live test, passed by not being taken.
  Win rate 1/1. Weekly count 0/5.
- ⚠️ **Cash residual $0.81** between the recomputed fills ($300.09) and the carried
  notional ($300.90). Recorded, not swept; correct at the next fill.
- 🔧 **Worst instrument degradation on record** — `macro` `n/a` on three consecutive
  calls, `unusual_volume` empty twice, `top_movers` RelVol broken 17/20, snapshot timed
  out twice. **Instrument health is now a first-order trading risk (lesson 41b).**
- 📁 Memory trimmed: research_log 117→~110, market_context 108→~70, lessons 106→~60,
  session_notes 474→~110. All prior content archived.

**Open thread for Monday (8/31, Week 36 day 1)**: **PD is the only named catalyst on the
board and it is MEDIUM, not HIGH** — rule 11's ladder is **capped on the dated evidence**
(rungs $15.90/$17.29 vs Canaccord $15 post-print, Truist $13, RBC $12; the $18.70
"consensus" is undated → rule 11a). Premarket must, in order: ① re-run the ladder against
a dated page (post-print revisions could un-cap it), ② EDGAR dilution check, ③ measure
Monday's range against the 7% trail (8/28 printed 8.5% — rule 37a/40a marginal). **RMNI
has the prettiest bar on the board (98% of range, 2.2x, and a range the 7% stop actually
fits) and ZERO catalyst — rule 1 kills it unless a dated catalyst appears.**

---

## 2026-08-28 — MARKET_CLOSE (Friday, Week 35 day 5) — NO TRADE, core in band, Warsh hawkish

Clean close. 0/4 satellites open (unchanged since 8/26 OMER stop), nothing to review.
Core rebalance: short by 2.79% of slice — inside the 3% band, no trade (closest to the
edge of any session this stretch, but did not cross it). IWM **−1.35% / −$38.40**
today vs **SPY −0.18%**, trailing by ~1.17%, 100% factor drag.

Warsh's Jackson Hole debut (10 AM ET) ran hawkish: inflation "still too high," no
forward guidance, majority now pricing a September hike. Small caps sold harder than
large caps into it — explains today's IWM/SPY gap directly. See `trade_log.md` for
full numbers. Week 35 closes 0/5 satellites — a board-quality week (zero overlap-tier
signal every session), not a discipline lapse; see `research_log.md` premarket entries
40/17a chain. Full P&L attribution deferred to weekly_review per lesson 23a.

---

## 2026-08-28 — MARKET_OPEN (Friday, Week 35 day 5) — NO TRADE, confirms premarket

Validated premarket's "board is empty" call against real open data — it held. The
overlap tier (top_movers ∩ unusual_volume) which was **zero names in premarket** was
**three names 5 min into the open**: NABL (+12.2%, 2.7x), OSG (+6.1%, 5.2x), BBW
(+4.5%, 6.3x). All three killed on catalyst, not technicals:
- **NABL**: no positive catalyst found — N-able just **cut** Q3/FY26 revenue guidance
  below consensus and announced a reorg today. Unexplained rally against bad news.
- **BBW**: yesterday's print was a guidance **cut** (FY26 slashed, stock −15.6% in
  premarket 8/27). Today's bounce is relief after a rout, not a fresh positive
  catalyst — worse than lesson 5's beat-without-a-raise pattern.
- **OSG**: only news is Q2 earnings from **Aug 6 — 22 days stale**, does not explain
  today's move (lesson 33).
- Also noted: scanner RelVol (2.7x–6.3x) vs. `detail`'s live volume/avg (0.2x–0.7x) on
  all three, 5 min into the session — expected this early (cumulative volume vs
  full-day average), not scored either way since catalyst killed all three first.

**Result: 0/4 satellites, 100% IWM core held.** No rebalance (rebalance is
market_close only per Portfolio Construction rule 6). No notification — flat session.
Warsh's debut keynote at 10:00 AM ET is still 30+ min out; nothing to add pre-event.

---

## 2026-08-28 — PREMARKET (Friday, Week 35 day 5) — NO SATELLITE, hold 100% IWM

**Book (hand-built, lesson 23a): $3,147.91** = IWM **9.4932 sh** ($2,847.01 @ $299.90,
90.4%) + notional cash $300.90 (9.6%). **Inside the 10% buffer — no bearish thesis
required.** Satellites 0/4 · weekly count 0/5. Raw fractional qty pulled per lesson 24
(display rounds it to "9").

- 🚨 **The board is empty by MEASUREMENT, not opinion.** The **overlap tier
  (top_movers ∩ unusual_volume) contained ZERO names — first time recorded.**
  `unusual_volume`'s #1/#2 are mandate-excluded crypto and **rank 3 onward is ≤0.7x,
  i.e. BELOW average volume** — the screen has no signal at all. Raw bars then
  falsified every non-crypto top_mover (**max real move +1.0%, max real RelVol 1.1x**):
  MGNX scanned +5.9% and really closed +1.0% at 27% of range; INSG scanned +5.0% and
  really closed **−2.7% at 20% on 0.5x**. Seventh straight lesson-17a demonstration,
  run **before** any research was spent. This is lesson 36's board-quality problem in
  its purest form.
- 🥇 **Both of yesterday's kills graded CORRECT against the bars (lesson 32c).**
  **LTRX** (triple-killed) opened $6.68, ran $7.07, **reversed to $5.80**, closed $6.03
  — **21.1% range, 18% of range**; a 7% trail from that open sat at $6.21 and the low
  blew through it. **OOMA** (rule 11 ladder kill) **spiked to $26.19 — through the
  Street's highest target of $24.00 — and closed $23.04, within $0.04 of the $23.00
  consensus mean.** The ladder named the closing price. **Rule 11 → 5-for-5;
  beat-without-a-raise → 5-for-5.**
- 🆕 **NEW LESSON 40 — rule 37a was the axis that MIS-scored LTRX.** It passed the
  stop-fit gate on trailing ranges of 4.8–6.7% (typical 5.7%) and then printed a
  **21.1% catalyst-day range — 3.7x.** Pre-catalyst bars are a *floor* on post-catalyst
  range, never an estimate. **A name saved by two other rules while a third mis-scored
  it is a rule failure, not a win.** 40b: this makes the gate stricter for quiet names,
  it does not loosen it for loud ones.
- 🚨 **Calendar closes the door for the second straight session — and LTRX proved the
  mechanism one day early with no macro shock required.** Warsh's debut keynote
  **re-verified by search: today 10:00 AM ET**, 30 min after the open (PCE already
  landed 8/26, Core 3.3%). **VIX 14.48 — lower than yesterday.** Nobody is positioned:
  **Russell futures printed a 0.3% overnight range on 0.1x volume, dead flat (0.00%).**
  Friday + weekend + a 1–5 day hold + a stop that fills at the open = no entry.
- ✅ **Yesterday's "Russell lagging" flag already reversed** — Nasdaq is today's
  *weakest* (−0.31%) after being the strongest (+1.07%). **Fourth consecutive
  one-session macro read to reverse inside 24 hours.** Lesson 28/34 confirmed again.
- ⚠️ **ARCT skip cost now ≈+45%** ($11.13 → $16.17) and the gate held anyway — still no
  new information, readout still undated. **But volume is finally exhausting: 1.3x →
  1.1x → 1.0x → 1.0x → 0.5x.** Lesson 35: carry the cost to the weekly review.
- 🔧 **Worst instrument degradation recorded (lesson 15).** `macro` returned mostly
  `n/a` on **three** consecutive calls (yfinance "possibly delisted" for
  ES/NQ/RTY/SPY/IWM/VIX/TNX/gold/Brent); levels were reconstructed from three partial
  calls plus direct bar pulls. **Gold and Brent are still missing and were left
  unrecorded rather than assumed.** `unusual_volume` **returned empty output twice** —
  which reads identically to "no candidates," the exact lesson-38 blank trap — and was
  re-run until it proved it could print. `portfolio_snapshot.py` timed out once.

**Open thread for market_open (9:35)**: decision is **no satellite, hold IWM**. Rocket
closes Week 35 with **zero satellite attempts** — name it in the weekly review as a
board-quality outcome (lesson 36), and watch for the opposite failure, reaching into
the weak tier to fill a slot (rule 6). Only re-open the question if a genuinely fresh,
dated catalyst appears at the open *and* clears the Warsh timing problem — which
realistically means Monday, not today.

---
## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
