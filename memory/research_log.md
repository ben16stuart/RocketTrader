# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Wed 2026-09-09 market_open update  ← CURRENT

### 🆕 IRD — Opus Genetics. Positive BEST1 Phase 1/2 data, the binary flagged 9/02 as anticipatory now resolved. **Too extended for today — pre-committed as a day-2 candidate.**

9/02 midday logged IRD's then +12.5% move as "anticipatory, tied to a September 9 data
webcast announcement... kill, not a today catalyst" (rule 29 shape). Today IS that date:
BIRD-1 trial (OPGx-BEST1 gene therapy) reported **positive 3- and 6-month Cohort 1 data**,
safety + proof-of-concept clean enough to advance to the higher-dose Cohort 2. Real,
dated, positive regulatory/trial catalyst — not hype.

| Gate | Reading |
|---|---|
| Universe (`market_data.py eligibility`) | ✅ price $6.56, cap $546M, **avg volume 1,128,759 — passes by 276%**, NASDAQ, next earnings +63d (no interference) |
| 🚨 **Extension** | **+49.6% TODAY ALONE**, on top of **+45.9% over the prior 5 days** and **+77.4% over the month** — **-0.9% from the 52-wk high.** Same-day gap-size framework: **>35% = second-day only** (rule 2c). Not a today entry regardless of catalyst quality. |
| Rule 13 (cap ladder) | ✅ Cleanest read yet — even +25% off today's price is ~$682M, nowhere near the $2B lid |
| Float / short | 65.2M float (above the <50M preference, not a hard gate); short 14.2% — below the 15% squeeze bar |

#### 🔒 Pre-committed gates for a 2026-09-10 day-2 entry (rule 42) — write BEFORE tomorrow's open

| # | Gate | Kill condition |
|---|---|---|
| **A** | Rule 2b | 9/09 must close in the **upper half of today's range**. Below the midpoint = distribution, not continuation — kill regardless of the catalyst. |
| **B** | Rule 46 | Re-verify ADV on the **median**, not the mean — today's volume bar will contaminate the trailing average exactly like TLYS/OCC did. |
| **C** | Rule 45 | Pull IRD's own 2y catalyst-day history for a range multiple **before** sizing any stop — a name that just moved 49.6% in a day is a live rule-45 candidate for blowing through a 7% trail on day 2 as well. |
| **D** | 🚨 **Rule 29** | Entry Thursday 9/10 on a 1–5 day hold can run into **FOMC 9/16** — the same calendar shape that killed CAL's day-2 this session. Check explicitly; do not assume it's clear because the catalyst already resolved. |
| **E** | Rule 3 | Entry zone = within 10% of 9/09's close, only if gate A holds. |

**Honest prior**: this is a real catalyst that was correctly anticipated a week ago and
correctly not chased today. Whether it clears day 2 depends on tomorrow's close shape
and gates B–D — not asserted here.

🆕 **Midday update (10:15 ET)**: IRD has faded hard intraday — $5.57–5.59, +28.4% on the
day per the scanner, **down from the $6.56 level this morning's gate table was struck
against** (≈−15%). Still well up on the day, but the trajectory is now a fade, not a
hold-and-base. This raises real doubt on **Gate A (rule 2b, close in upper half of
today's range)** — flagged for whoever runs `market_close` to check the actual OHLC
before writing the close-shape verdict, not carried forward as an assumption.

---

## Watchlist — Wed 2026-09-09 premarket (Week 37 day 2)

**Book (hand-built — BASE NAMED, lesson 23a/44)**: **$3,098.52** = IWM **9.8636 sh**
($2,906.51 @ $294.67 *settled* close, **93.80%**) + notional cash **$192.01 (6.20%)**.
✅ **Inside the 10% buffer — no bearish thesis required or written.**
Satellites **0/4** · weekly count **0/5** (counted by hand — lesson 24) · max satellite
**$464.78** (15%) · 1.5% risk **$46.48** · shared cash $427.02 (pooled with Bull —
**fund from core, not cash**).

## 🚩 VERDICT: NO ENTRY TODAY. Hold IWM. **The board was NOT empty — it was the fullest in a week, and all four survivors died on named gates.**

This is the opposite failure mode from 9/08. The earnings calendar produced **four
in-universe names with real dated catalysts**, and every one was killed on a gate, not on
an absence of evidence. Two of the four (AVO, INNV) had already printed and were gapping.

---

### 🥇 The earnings calendar ran FIRST (lesson 41) — and this time it delivered

Nasdaq earnings-calendar API (`api.nasdaq.com/api/calendar/earnings?date=…`), the source
adopted 9/08. Tradeable slate = **9/08 AMC reporters** (gap today) + **9/09 BMO reporters**.

| Slate | Reporters | Screened in-universe |
|---|---|---|
| **Tue 9/08 AMC** | 24 | INNV, AVO, CSHR, ALPS |
| **Wed 9/09 BMO** | 45 | CAL, JILL, PPIH, OCC, HTT, NBP, ANIX |

**`eligibility` on all 11: 11 requested → 11 returned** ✅ (lesson 43 count held; no
truncation, counted against full output per 43b).

| Killed on a hard gate — zero research spent | Kill |
|---|---|
| **JILL** | ADV **76,785** — 26% of the gate |
| **PPIH** | ADV **107,613** |
| **CSHR** | ADV **203,298** (also CoinShares — crypto proxy, rule 31 independently) |
| **HTT** | **$2.65** under the $3 floor · ADV 217,254 |
| **NBP** | **$1.78** |
| **ANIX** | **$2.90** · ADV 278,140 |
| **ALPS** | **$0.39** · ADV 124,491 |
| **SIG $3.35B · ASO $2.79B** | Cap (SIG also Bermuda) |
| **ODD · CGNT · NNOX** | Israel-domiciled — mandate |
| **COE · AACG** | China-domiciled — mandate |
| **ANAB** | Standing rule-13 kill ($1.68B → +25% = $2.10B, through the $2B lid) |

**Survivors: CAL, OCC, INNV, AVO.** All four screened below.

---

### ❌ AVO — Mission Produce. Reported AMC 9/08, +5.8% premarket. **Beat-without-a-raise, and the raise that WAS announced never reached the guide.**

| Gate | Reading |
|---|---|
| Universe | ✅ **The cleanest liquidity on the board** — median ADV **865,900** (passes by 189%), cap $1.14B, US (Oxnard CA) |
| 9/08 bar | **+1.50% at 81% of range** on 990,200 (1.14× median) — a firm bar into the print |
| 🚫 **Rule 5 / 5f** | Q3 adj EBITDA **$32.4M** beat the high end of its own $28–32M guide by **$0.4M = +1.25%** — then **REAFFIRMED** the second-half range at **$84–88M. A 0% change.** Q4 guided $52–55M, which simply absorbs the Q3 beat. **Rule 5d's pass-through diagnostic: beat your own quarter, raise the half by zero → the beat was not run-rate.** |
| 🚨 **Rule 5e** | **Read the composition and the beat inverts.** Revenue $450.0M on **+38% avocado volume** — but **gross profit FELL** ($44.7M vs $45.1M), **gross margin −270bps to 9.9%**, **adjusted net income −18%** ($15.0M/$0.18 vs $18.2M/$0.26), and GAAP was a **net loss of $6.5M (−$0.08)**. Volume bought with acquisition (Calavo) that earned *less money than last year*. |
| ⚠️ The headline raise | "Annualized Calavo synergy target raised to **>$30M**" is a **forward promise, not a delivered result** — and the tell is that it did **not** flow into guided EBITDA. If the synergies were real and near, H2 would have moved. It didn't. |

**Rule 5 stands 5-for-5 as a fader on beat-without-a-raise.** Killed. Not re-openable on
this print.

---

### ❌ INNV — InnovAge. Reported AMC 9/08, **+14.2% premarket** ($10.52 → $12.01). Dies FOUR ways.

The largest gap on the board, and the most seductive name of the session.

1. 🚫 **Rule 5a — guidance is explicitly IN-LINE (0% raise).** FY26 was genuinely strong
   (revenue $989.7M **+15.9%**, adj EBITDA $94.6M vs $34.5M **+175%**, net loss $35.3M →
   $0.7M). But FY27 guides revenue **$1.05–1.085B, midpoint $1.0675B = +7.9%** — against
   an FY26 that just delivered **+15.9%**. **The company guided its own growth rate to
   roughly half.** Adj EBITDA $105–115M (mid $110M) = +16.3% after +175%. Management also
   flagged a *moderating* rate environment (Medicare +1.5–2% incl. V28, low-single-digit
   Medicaid). Rule 5c: growth decelerating hard against the year just reported.
2. 🚨 ❌ **Rule 13 — the second rung is THROUGH the $2B lid.** At the $12.01 premarket
   price on 135.736M shares out: entry cap **$1.63B**, +15% → $13.81 = $1.87B (clears),
   **+25% → $15.01 = $2.04B — through the lid.** A one-rung name at best, priced *after*
   a 14% gap has already been paid for.
3. ❌ **Lesson 46 — mean passes, MEDIAN fails.** `eligibility` read ADV **313,314, a PASS
   by 4.4%** — inside lesson 14's ±10% re-verify band, so it was re-verified:

   | Measure (63d) | Value | vs 300k gate |
   |---|---|---|
   | Mean, as-is | 320,840 | ✅ passes by 6.9% |
   | Mean, ex-max bar | 304,647 | ✅ passes by 1.5% |
   | **Median** | **288,500** | ❌ **fails by 3.8%** |

   Recent sessions: 249,800 · 184,800 · 232,400 · **122,600** · 161,400 — then 535,200 on
   earnings eve. **The one contaminated bar is doing the work again** (46b).
4. ❌ **Rule 45 — predicted catalyst-day range 25.2% = 3.6× the 7% trail.** 2y median
   range 5.77%, own top-5 catalyst multiple **4.37×** (widest 6.02×). Its ten widest days:
   **15.4, 16.2, 16.5, 18.2, 18.3, 19.0, 20.9, 24.3, 27.0, 34.7%.** *Every single one*
   blows through a 7% trail.

---

### 🚨 ❌ OCC — Optical Cable. **Tops BOTH scanners (+12.5%, 4.3–4.4× RelVol) AND reports BMO today — the single most tempting row of the session. Dead three ways before the print even landed.**

1. 🚨 **Lesson 46e — the live book is the whole argument. Bid $11.47 / ask $20.01 = an
   $8.54 spread, 55% of price.** Worse than BBCP's 44%, which is the precedent that made
   this a one-call kill.
2. ❌ **Lesson 46 — the widest mean/median split yet recorded.** `eligibility` read ADV
   **380,424 — a PASS by 26.8%**, comfortably *outside* the ±10% band that would normally
   trigger a re-verify. Raw bars:

   | Measure (63d) | Value | vs 300k gate |
   |---|---|---|
   | Mean, as-is | **380,424** | ✅ passes by 26.8% |
   | Mean, ex-max bar | 342,985 | ✅ passes by 14.3% |
   | **Median** | **236,900** | ❌ **fails by 21%** |

   Its last five normal sessions: **70,300 · 95,300 · 87,000 · 123,000 · 201,500.**
   🚨 **46g (new): the median must be pulled even when the mean passes by a wide margin.**
   Lesson 14's ±10% band would NOT have triggered here — 26.8% is nowhere near it — and
   the name still trades at 79% of the gate on a typical day. **The ±10% trigger is a
   floor for re-verification, not a ceiling.**
3. ❌ **Rule 37a — median daily range 9.13%, LARGER than the entire 7% trail.** Predicted
   catalyst-day range **~50%** (top-5 multiple 5.98× on an 8.49% 2y median). Float **5.9M
   shares** — lesson 46c: the low float is precisely *why* it moves 12% and precisely why
   a 7% stop cannot be filled.

---

### ⏳ CAL — Caleres. The only clean instrument on the board. Print lands BMO today. **Gates pre-committed BELOW, before the evidence (rule 42).**

| Gate | Reading |
|---|---|
| Universe | ✅ Passes everything, and **the liquidity is genuinely good**: median ADV **490,700** (passes by 64%), mean 536,437, ex-max 518,063 — **all three agree**, no lesson-46 split. Cap $404M, $12.03, 31.8M float (95%), NYSE, US (St. Louis) |
| Short float | **12.8%** — below the 15% squeeze bar, no kicker |
| Rule 37a | ✅ Median daily range **4.82%** — inside the 7% trail on normal days |
| 🚨 **Rule 45** | ❌ **2y median range 4.41%, top-5 catalyst multiple 3.64× → predicted catalyst-day range 16.1%** (widest 4.32× → 19.0%) = **2.3–2.7× the trail.** Its ten widest days: **13.0–19.0%. Every one blows a 7% trail.** |
| 🚨 **Rule 4** | ❌ 9/08 closed **−3.22% at 3% of its range** on 765,900 (**1.56× median**) — heavy volume, dead-bottom close. **Distribution shape going INTO the print.** |
| ⚠️ Timing | Release moved **UP one day** (was 9/10). Call at **10:00 AM ET — 25 minutes AFTER the 9:35 decision window.** Same hostile shape as ISM has had all week. |

**Ladder off the $12.03 settled close: +15% = $13.83 · +25% = $15.04 · 7% stop = $11.19.**

⚠️ **Pre-print consensus is LOW-CONFIDENCE and conflicting** (rule 11a/33): one source gave
consensus EPS **$0.31** / revenue **$664.17M**, another **$0.37** / **$702.5M**; price
targets came back **$14.00 (consensus rating "Reduce")** and **$15.30 average** — the
latter struck against "a current price of $14.06," **which is not CAL's price** ($12.03
settled). **Undated and internally inconsistent — recorded as unresolved, not asserted.**
Note $14.00 clears the +15% rung by only **$0.17 (1.2%)** and fails the +25% rung outright.

#### 🔒 Pre-committed gates for CAL — written BEFORE the print (rule 42)

| # | Gate | Kill condition |
|---|---|---|
| **A** | Rule 5a/5d | FY26 guide must be raised **>2% at the midpoint** vs Caleres' **own prior guide** (it raised on 6/04, so a prior number exists — diff against *that*, not consensus). **Reaffirmation or sub-1% nudge = KILL.** State the % in the log or the label does the reasoning. |
| **B** | Rule 5c | The new guide must not sit **below the quarter just reported**. |
| **C** | Rule 11/42b | **Dated post-print** consensus must clear the **+15% rung ($13.83)**. If the Street's **highest** target lands below it → the OOMA/PD configuration, the strongest kill on the book. |
| **D** | 🚨 **Rule 45** | **BINDING REGARDLESS OF A–C: a 16.1% predicted catalyst-day range is 2.3× the trail → NO SAME-DAY ENTRY.** Per 45c this converts the kill to a *date*: earliest valid entry is **day 2, Thursday 9/10**. |
| **E** | 🚨 **Rule 29** | A Thursday **9/10** entry on a 1–5 day hold runs to **9/16 — FOMC decision day.** The calendar gate argues against the day-2 entry too. |

🚩 **Honest read: D and E together mean CAL cannot be entered today, and its only valid
entry date collides with the FOMC.** This is recorded as a near-certain no-trade, not as an
open thread — leaving it vague would let a gate be re-specified after the data arrives,
which rule 42 exists to prevent. Midday may confirm the print against gates A–C for the
*record* (grading, lesson 32c), not to re-open the entry.

---

### ✅ Yesterday's kills graded against the 9/08 settled bars (lesson 32c) — 8 of 10 confirmed in ONE session

| Name | 9/08 settled bar | Verdict |
|---|---|---|
| 🥇 **NX** | **−3.10%**, 41% of range | ✅ **Rule 5f's first graded validation.** Yesterday this was logged as "the strongest bar on the tape, and the kill still stands — an uncomfortable carry." One session later the reinstated-guide kill is paying. |
| 🥇 **CHPT** | **−5.26% at 6% of range** on 5.4M | ✅ **Rule 5a/5b (+0.6% guide midpoint) graded correct.** The 9/03 +49.3% spike is unwinding. The second uncomfortable carry, also resolved for the kill. |
| **EAF** | **+1.61% at 2% of range** on a **21.43% range** | ✅ Rule 1 (no dated catalyst) correct — and the 21.4% range would have blown a 7% trail **three times over** |
| **INSG** | +2.83%, 36% of range, **volume 254,100 — under the 300k gate** | ✅ The lesson-46 median kill confirmed by the very next session's raw volume |
| **HLF** | +0.40%, 11% of range | ✅ |
| **SG** | +1.61%, 45% of range | ✅ |
| **TROX** | −0.21%, 28% of range | ✅ |
| **NVA** | +5.87%, 51% of range | ✅ (mandate kill — moot either way) |
| ⚠️ **HYPD** | **+8.48% at 82% of range** | ⚠️ **The rule-31 mandate kill cost a real up-move — recorded, not rationalised.** Note its **13.97% range = 2× the trail**, so rule 45 kills it independently of the mandate. |
| ⚠️ **SWBI** | +2.64%, 84% of range | ⚠️ Bounced. The 5a/5d kill (+0.95% guide) is mildly uncomfortable again after grading correct on 9/04. Carried, not re-opened (rule 42a). |

📌 **Missed-catalyst rule check**: nothing in-universe has run **>35%** in the last 3
sessions. EAF's +21.9% was the largest and it closed at 2% of its range. CHPT's 9/03 +49.3%
is now **day 4 — the 3-day recheck window has expired**, and it is under a standing
guidance kill besides.

---

### 🚩 Rebalance-basis divergence — carried, narrowed again, **SIXTH** session (lesson 44/44c)

| Basis | Value | Divergence |
|---|---|---|
| **Book** (hand-built, lesson 23a — **the base used above**) | **$3,098.52** | — |
| **Slice** (30% of live shared equity $10,558.82) | $3,167.65 | **slice +$69.13 richer** |

**Narrowed for a second straight session: $106.66 → $88.16 → $69.13.** Consistent with
lesson 44b's mechanism running in reverse — Bull's JPM gave back (+13.3% → +12.6%) while
IWM held, so the gap Bull's P&L opens has partly closed. **It is closing for the same
reason it opens — not because anything was fixed.** 🚨 **Sixth consecutive session.
Escalated 9/01, 9/02, 9/03, 9/04, 9/08; still awaiting a user decision on which basis
governs.** No action here — rebalancing is `market_close` only (rule 6).

---

### 🚨 Instrument health — lesson 17a, ELEVENTH straight demonstration

- **OCC**: `top_movers` printed **"$15.41, +12.5%"** against a real settled 9/08 close of
  **$13.70, −1.08% at 11% of range.** The scanner ran at **04:22 ET — hours before any BMO
  release** — so that is a thin premarket print reported as both the price and the day's
  change.
- **INNV**: scanner "+14.2%" **is** a real earnings gap (corroborated by `preMarketPrice`
  $12.01) — but it is still an extended-hours quote in a column labelled `Change %`.
  **Right by accident is not right.**
- `top_movers` gave **11 of 17 rows** a RelVol of `—` or `0.0x`. `unusual_volume` had
  **18 of 20 below 1.0×**, i.e. below average volume.
- Overlap tier (both lists): **OCC** and **USDE** (stablecoin proxy — standing rule-31
  mandate kill). Effectively **one real overlap name, and it had a 55% spread.**

### 🆕 46g — a wide premarket book is only evidence when the median ADV independently fails

**AVO is the control case that proves it.** At 06:25 ET its book read **bid $9.13 / ask
$16.12 — a 55% spread, identical to OCC's** — yet AVO's **median ADV is 865,900, passing
the gate by 189%.** INNV read 48% wide on a median that fails by 3.8%.

**At this hour essentially every small cap shows a broken-looking book**, so lesson 46e's
spread check **cannot stand alone as a kill** — it corroborates a median-ADV failure and is
noise without one. Read the other way it would kill every name every premarket, which is
lesson 38's blank-result trap wearing the opposite sign: **a check that always fires
carries no information.** OCC's and BBCP's spreads were decisive *because* their medians
had already failed; AVO's identical spread is discarded.

---

### Scheduled catalysts

- 🚨 **FOMC September 15–16, decision Wednesday 9/16 — 5 trading days out.** A satellite
  opened **today** on a 1–5 day hold reaches 9/16 at the far end; **anything opened
  Thursday or later carries into it.** Live rule-29 gate for the rest of the week, and it
  is the gate that closes CAL's day-2 entry.
- **Today**: CAL earnings call **10:00 AM ET** (25 min after the decision window); wholesale
  inventories 10:00 AM. No tier-1 macro print before the open.
- **Thu 9/10**: the week's next real slate — screen from the calendar at premarket, not the
  scanner.

### Re-open conditions for killed names (everything else needs a new dated catalyst)

| Name | What would have to change |
|---|---|
| **AVO** | A **sized** raise to the H2/FY EBITDA guide (>2% at the midpoint), **and** gross margin stabilising — the −270bps with volume +38% is the actual problem |
| **INNV** | ⚠️ **Not re-openable on this print.** Needs a sustained **median** volume above 300k **and** a price low enough that the +25% rung clears the $2B lid (≤$14.73 entry) |
| **OCC** | ⚠️ **Not re-openable on a catalyst** — only a sustained **median** volume above 300k and a normal spread. A 9.13% median range exceeds the whole trail regardless |
| **CAL** | Gates A–E above. **D and E are the binding ones and neither is a research question** |
| **NX** | A **sized** raise against the **pre-withdrawal** March guide (5f), not a reinstatement |
| **SWBI** | A **sized** raise (>2% on revenue) **and** dated post-print targets. The Q2 +10% guide must be beaten and passed through |
| **CHPT** | A **sized** raise (>2% at the midpoint) **and** a dated post-print consensus above 1.15× entry |
| **INSG** | A **dated** catalyst **and** a sustained *median* volume above 300k **and** the S-3 graded (8a) |
| **EAF** | A **dated** catalyst. The "Defense Dept partnership speculation" headline was undated and explicitly speculative (rule 33) |
| **BBCP · TLYS · JILL · PPIH · CSHR** | ⚠️ **Not re-openable on a catalyst** — only a sustained **median** volume above 300k, or a user decision on the ADV gate |
| **CAPR** | In universe but the **PDUFA was EXTENDED Aug 22 → Nov 22** — lesson 37c: an extension is a delay repriced as optionality, **not a catalyst delivered** |
| **HLF · SG · TROX · AMRC · WTI · ENOV · UPB** | Earnings **11/02–11/05**. No dated catalyst inside any tradeable horizon |
| **ALMU** | Earnings **9/16** — re-screen after the print (note it collides with FOMC day) |
| **PHR** | ⚠️ **Resolve the earnings date first** (two sources disagreed 9/03) |
| **ARCT** | ARCT-810 Phase 2 **date becomes a fact** |
| **BNC · USDE · DFDV · ABTC · HYPD · CSHR** | Crypto/stablecoin proxies — **mandate-excluded, lesson 31**. Standing, not re-researched |
| **ANAB · NVA · HTT · NBP · ANIX · ALPS · SIG · ASO · ODD · CGNT · NNOX · COE · AACG** | Killed on a hard gate or mandate this session / standing |
| **GIII · DAKT · NEOV · YEXT · PD · RMNI · MEI · CBIO · TYRA · PYXS · RARE · GOLD** | Killed on the tape or a hard gate. New dated catalyst only |
| **IRD** | ⚠️ **Not a stale kill anymore — see the 9/09 market_open entry above.** Real dated catalyst delivered, pre-committed day-2 gates A–E written for 2026-09-10 |
| **LTRX · OOMA · FRNM · SSTK · BBW · OSG · XHLD · NABL · LENZ · ALMS · EOSE · OABI** | Killed W35–W36, reasons in `archive/research_log_history.md` |
