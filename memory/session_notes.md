# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-08-27 — MARKET_CLOSE (Thursday, Week 35 day 4) — no trades, core in band

Clean no-op day: 0 satellites open (unchanged since the 8/26 OMER stop-out), no
overnight fills, no stops hit. Core rebalance check: IWM (9.4932 sh, $2,846.44) is
1.07% of slice short of target — inside the 3% band, no trade. Day P&L: IWM
+0.29%/+$8.26 vs SPY +0.66% — Rocket trailed SPY by ~0.37% today, pure factor drag
(small-cap IWM lagging large-cap SPY), no satellites to attribute it to. Full detail
in `trade_log.md`. ntfy daily summary sent and confirmed. Since-rebase figure still
not recomputed daily (lesson 23a) — carries to weekly_review.

**Open thread for tomorrow (Fri 8/28, last session of Week 35)**: Warsh's Jackson
Hole keynote ~10:00 AM ET is the day's dominant event — per premarket's own note, a
7% trail fills at the open wherever the open is, so any fresh entry timed around it
carries that data-gap risk. Watchlist is still empty (LTRX killed, CAPR/ARCT/OI dead
threads) — a fresh scan is the priority, not a nice-to-have, since Rocket closes the
week with zero satellite attempts if nothing changes.

---

## 2026-08-27 — MARKET_OPEN (Thursday, Week 35 day 4) — no trade, confirmed premarket decision

Synced live account: **IWM 9 sh ($2,840), no satellites, no overnight fills or stops**.
Cash $411.48 pooled, unchanged. Weekly satellite count still 0/5.

Ran `unusual_volume` and `top_movers` fresh at the open — board is essentially
unchanged from premarket: **BBW** is down **−19.5% on 15.1x** (the print already hit,
a miss reaction, not a beat — not a candidate). LTRX and OOMA reappear at the same
levels already triple/single-killed in premarket. Everything else new (BNC, XHLD,
METC, REAX, IGR, BETR, SVV, TE) is sub-3x RelVol or <6% change with no named catalyst
(rule 1), or is the same mandate-excluded crypto-treasury tier (DFDV, FWDI, ASST,
HYPD, USDE, SECZ, BKKT — rule 31). No new candidate clears the bar.

**Decision: no trade. Hold 100% IWM core**, consistent with premarket. Nothing to
log to trade_log.md. No notification sent (flat session).

---

## 2026-08-27 — PREMARKET (Thursday, Week 35 day 4) — NO SATELLITE, hold 100% IWM

**Book (hand-built, lesson 23a): $3,138.95** = IWM 9.4932 sh ($2,838.05, 90.4%) +
notional cash $300.90 (9.6%). **Inside the 10% buffer — no bearish thesis required.**
Satellites 0/4 · weekly count 0/5. **Decision: no satellite. This is a calendar
timing call, not a market call.**

- 🚨 **CORRECTED A TWO-SESSION ERROR IN ROCKET'S OWN FILES: the Jackson Hole keynote
  is KEVIN WARSH, not Powell** — and it is **Fri 8/28 ~10:00 AM ET, his first as
  chair.** Both `research_log.md` and `market_context.md` said "Powell" in bold on
  8/25 and 8/26 as the top-cited risk. The risk call survived by luck; it was right
  about the date, wrong about the event. **New lesson 39** — memory files get re-read
  every session and never re-sourced, and the two mechanical-close days that skipped
  research still inherited the claim. Ties to [[launchd-quota-contention]].
- 🚫 **LTRX was the only genuine fresh catalyst and it was TRIPLE-KILLED.** FY26 Q4
  after the 8/26 close, **$5.66 → $6.50 premarket (+14.8%)**. It *passed* the gates
  that usually kill: universe, rule 13 ($290M), **rule 37a (ranges 4.8–6.7%, the 7%
  stop actually fits)**, and **rule 11 uncapped** ($6.50 vs $10.33 mean, low $8.00).
  Died on: **(1) rule 5** — EPS $0.04 vs $0.03 is a *one-cent* beat, revenue +8% YoY
  is not acceleration, and Q1 FY27 guidance **$31–33M midpoints +2.6% QoQ with the
  low end BELOW the quarter just reported** = beat without a raise; **(2) rule 8a** —
  **424B5 takedowns 5/8 and 6/1/2026**, shelf drawn twice this year and still live;
  **(3) calendar** — lesson 2 makes tomorrow's open the earliest valid entry, i.e.
  **30 minutes before Warsh's keynote.** Tell: 8/26 into the print was **−3.4% at 29%
  of range on 2.8x volume.**
- 🆕 **New lesson 8e** from that #2: **LTRX's press release led with "$60 million in
  cash and no debt"** — which is the *proceeds of the two takedowns*. A PR touting
  cash can be advertising the dilution that created it. **Exact inverse of lesson 38**
  (there a blank search hid a *clean* name; here a company hid a *drawn* one).
- ❌ **OOMA killed on rule 11 in one call** — real +25% YoY print, but consensus mean
  $23.00 and **highest target $24.00 vs a +15% rung of $25.10.** Ladder capped below
  the first rung; also within 4% of its 52w high and its 8/21 run already faded.
- ❌ **CRBP** — best accumulation on the board (+14.8% in four sessions, 93/84/93% of
  range, 2.0x volume twice, short float 12.7%) but **rule 1**: the only news is a
  Phase 3 **initiation**, "not yet recruiting" — an undated forward binary (lesson
  29), with August PT **cuts**. Watch, don't trade.
- 🔧 **Lesson 17a held again**: **BKSY scanned +9.4%; its real 8/26 bar was −2.1% at
  20% of range**, mid-slide through −11% in three sessions. SPIR, HDSN, ATOM, AMPG,
  CEPL all falsified the same way. Bars before the board.
- ⚠️ **Crypto-treasury theme is back on top of both screens after ONE red session** —
  yesterday's file called it "stopped topping the scanner." Same one-print error as
  the 8/20 rate stand-down. **3 of 4 names in the overlap tier were unusable
  (lesson 36 board-quality problem is back, not eased).**
- ✅ **Yesterday's "crude has broken down" call half-reversed in one session** (Brent
  $84.84 → $87.28, +2.9%). The written restraint — *note it, don't trade it* — was
  correct. Third consecutive one-session macro read to reverse.
- **Open thread for market_open**: nothing to execute. Re-verify the book is ≥90%
  invested; if IWM has drifted outside the 3% band, that is a `market_close` job.
  **Do not reach into the weak tier to fill a slot — rule 6.**

---

## 2026-08-26 — MARKET_CLOSE (Wednesday, Week 35 day 3) — OMER stopped out, core rebalanced to 100%

**No premarket/market_open ran today** (same launchd quota gap as 8/24–8/25). First
session of the day was this market_close sync, which found OMER already gone from
the broker — the 7% trailing stop had filled intraday at 15:55 UTC, well before
market_close ran.

- **OMER stopped out**: 27 sh, entry $17.14 (8/14) → $18.270741 (7% trail off HWM
  $19.6497). **+$30.53 lifetime (+6.60%)**, but today's mark was −$27.25 — the stop
  won the race against the queued +15% profit rung ($19.71), which the 8/25 high
  ($19.65) never reached. Net: a real winner closed by the mechanism, not by
  judgment — nothing to second-guess here.
- **Core rebalanced to 100%**: satellite sleeve now $0, so bought 1.441 sh IWM
  ($430.75) to bring the core from 13.7%-short to on-target ($2,838, 90% of slice
  deployed, 10% buffer intact). Board is now IWM-only — first time since 8/14 with
  zero satellites open.
- **Full detail in `trade_log.md`** under "2026-08-26 — OMER STOPPED OUT + CORE
  REBALANCE". ntfy daily summary sent and confirmed.
- **Open thread for next premarket**: watchlist is empty. CAPR (volatility gate),
  ARCT (data-gap gate), OI (no catalyst) were all killed this week per the 8/26
  premarket notes below. Need a fresh scan — this is now the top priority, not a
  nice-to-have, since Rocket is carrying zero alpha attempts into Jackson Hole week.

---

## 2026-08-26 — PREMARKET (Wednesday, Week 35 day 3)

**First research session of the week** — no premarket/market_open has run since Fri 8/21.
All three tasks carried for two sessions (CAPR PDUFA outcome, OI catalyst, re-run screeners)
are **resolved and closed** below. **No trade recommended for the open.**

- 🚨 **JACKSON HOLE STARTS TOMORROW (Aug 27–29)** — Powell's keynote lands **inside** any
  1–5 day hold opened today, and a 7% trail fills at the open wherever the open is (lesson
  29's data-gap mechanic applied to a macro event). VIX **15.70** says the tape is not
  braced for it. **Direct argument for carrying the book, not adding to it.**
- ✅ **CAPR — the standing PDUFA question is ANSWERED: there was no decision.** FDA extended
  to **2026-11-22** to review a BLA amendment; the +58% (8/14) and +21.9% (8/25) moves are
  the **analyst reaction** (Oppenheimer PT **$54**, Cantor Overweight **$28 from $3.50**).
  Real, dated, on-list catalyst. It **cleared rules 8, 11, 13, 29** — including a **top-tier
  dilution profile: no S-3/S-3ASR/424B5 anywhere in 2026, $237.9M cash vs a $482M cap.**
  🚫 **Killed on rule 4b**: daily ranges of **18.6% / 26.7% / 35%** make the mandated 7%
  trail a coin flip. 🆕 **First kill this month from INSTRUMENT VOLATILITY rather than
  funding structure or calendar.** Also: **securities fraud class action filed 8/25** (the
  day of the move), a **9–3 negative AdCom** on the record, and eight sessions of chop
  ($6.01–$8.60) — **8/24 opened $8.03 and closed $6.80.** An FDA *extension* is a delay
  being repriced as optionality, not a catalyst delivered.
- ⚠️ **Rule 11b applied deliberately**: the dilution web search came back "could not confirm
  the shelf." **That is a FAIL, not a pass** — so I went to EDGAR directly, verified the
  submissions file was populated (961 filings, 56 in 2026) so a blank result couldn't be a
  broken instrument (lesson 15), and got a genuine clean read. **Search said unknown; EDGAR
  said clean.** Worth repeating: resolve the gap, don't score it.
- ❌ **ARCT — gate holds a FOURTH time. Skip cost now ≈+50%** ($10.28 → $15.44). It has run
  **+88% in five sessions** (5.1x → 2.6x → 2.0x volume, closing 54–98% of range daily) —
  **best price action on the board by a distance.** Re-checked: **no new information**, same
  Aug-6 material, readout still **"Q3 2026," undated**, inside any hold. **Lesson 35 says
  that exact profile — big momentum on zero new information — is a crowded chase and a
  reason for MORE caution.** Carry the cost to the weekly review; do not loosen the gate.
- 🔵 **OMER — both open threads closed, both benign. HOLD.** ✅ **ATM still undrawn — no
  424B5 anywhere in 2026** (EDGAR). ✅ **New Form 144s (8/20 $276,773, 8/21 $203,179)
  resolved BENIGN per lesson 30** — acquired-date = sale-date, paid **cash** = cashless
  exercise-and-sell; **0.90% and 0.41% of their days' volume**, 0.040% of shares out,
  *vs ETON's real one at 16% of a day's volume.* Compensation mechanics, **not an exit
  trigger (lesson 32b).** 🥇 **+15% rung $19.71 is 0.31% away — 8/25 high was $19.65.
  SELL 9 SH ON THE TOUCH; first thing to check at the open.** Volume drying (1.0x → 0.6x
  → 0.5x) but price holding $19.28 — a pause, not distribution.
- ❌ **Board otherwise fails rule 1 (no catalyst)**: **OI** killed after a third session with
  no catalyst *and below-average volume* (0.9x/0.8x) — stop carrying it. **IE** rule-13 kill
  ($1.90B → $2.19B at +15%). **THEO** rule-27 kill — a SPAC pinned in a **$0.01 range**.
  ANRO/ALIT/CPSH no catalyst or dead follow-through. ⚠️ **GNK is the one genuine puzzle —
  2.8x volume three straight sessions, closed 97% of range — but +1.4%/day is drift and
  there is no named catalyst. WATCH.**
- 🔧 **Scanners were a broken instrument (lesson 15).** `unusual_volume` **returned nothing
  above 0.7x RelVol** on a screen built for 3x+, its top name *down* 4.1%; `top_movers`
  printed RelVol as `0.0x`/`—` for **15 of 20** names; **zero overlap between the two**, so
  the routine's first-priority tier was empty. At 04:20 RelVol runs off partial premarket
  volume. **Raw daily bars carried the session** — THEO scanned **+10.8%** against a real
  bar of **−0.1% in a $0.01 range.**
- 🆕 **Crypto-treasury theme went RED after four sessions on top** (USDE −4.1%, DFDV −2.8%).
  Lesson 31 unchanged, but **lesson 36's board-quality problem has eased on its own** — the
  board is no longer crowded out by an untradeable theme, it is **simply thin on catalysts.**
  Different problem, and the distinction matters when grading a no-trade session.
- 🆕 **Macro: the inflation-tinged pattern BROKE, constructively — all three legs at once.**
  **Brent −4.22% to $84.84** (a −9.7% break from $93.96, the biggest move on the board),
  **gold decelerating** (+2.72% → +0.85%), **10-yr −6bp to 4.64%** (cushion to the 4.75%
  trigger widened 5bp → **11bp**). ⚠️ **Per lesson 34 this does NOT stand the rate flag
  down — that is the exact error made 8/20, reversed the next day.** And Jackson Hole is
  the event that will confirm or destroy it. **Note it; act only if it survives Powell.**
  ✅ VIX 15.70, no brake. Futures flat-to-red (Russell −0.11%, no information — lesson 28).
- Book **$3,167.56** (hand-built, lesson 23a) = IWM 8.0522 sh $2,409.46 (76.1%) + OMER
  $520.56 (16.4%) + cash $237.54 (**7.5% — inside the buffer, no bearish thesis needed**).
  **92.5% invested.** Satellites **1/4**, weekly count **0/5**. Core is ~2.4% of slice over
  target, **inside the 3% band — no rebalance, and `market_close` owns that call anyway.**

## 2026-08-26 — MARKET_OPEN (Wednesday, Week 35 day 3)

**No trade.** Premarket already killed everything actionable (CAPR on 4b, ARCT on
lesson 35); nothing new cleared the gate at the open either.

- **OMER $18.98, −1.6%, 0.1x volume (early).** Well off the $19.71 (+15%) rung —
  8/25's $19.65 high wasn't retested. No action; standing order stays live.
- **`unusual_volume`/`top_movers` re-scanned** — no new names. PLAB (+6.5%, 19.1x)
  is the one fresh print but **$1.84B cap → $2.3B at +25%, rule 13 kill**, no
  catalyst identified. ARCT (7.8x), CAPR (2.6x), AGPU, FWDI all already-killed
  names reappearing, not new signal.
- **Positions unchanged from 8/25 close** — no overnight fills, no stops triggered.
  Cash still $348.97 (pooled), satellites 1/4, weekly trades 0/5.
- 🚨 Jackson Hole (Aug 27–29) starts tomorrow — held the book rather than adding,
  per premarket's explicit call.

## 2026-08-25 — MARKET_CLOSE (Tuesday, Week 35 day 2)

**Second quiet day — no trades, no premarket/market_open sessions ran today either.**

- OMER held overnight (27 sh, $19.28, −0.2% today) — +15% rung untouched, catalyst
  multi-day and intact, a pause after five strong closes rather than a breakdown.
  IWM core (8.0522 sh) unchanged, within rebalance band (2.4% of slice over target,
  band is 3%).
- Day: book $3,158.25 → $3,168.91 = **+0.34%** vs **SPY +0.33%** → Rocket essentially
  matched SPY today (+0.01%); IWM led (+$11.88), OMER gave back a touch (−$1.22).
- No new satellite research happened this session (mechanical close only) — Week 35
  premarket board (OI needs a catalyst check, CAPR PDUFA outcome from 8/22, screeners
  re-run) is still outstanding, now two sessions running.

## 2026-08-24 — MARKET_CLOSE (Monday, Week 35 day 1)

**Quiet open to the week — no trades, no premarket/market_open sessions ran today either
(nothing in the log for 8/24 before this entry).**

- OMER held overnight (27 sh, $19.32, +0.3% today) — +15% rung untouched, catalyst
  multi-day and intact. IWM core (8.0522 sh) unchanged, within rebalance band (2.1% of
  slice over target, band is 3%).
- Day: book $3,173.17 → $3,158.25 = **−0.47%** vs **SPY −0.28%** → Rocket **−0.19%**
  vs SPY today (IWM lagged SPY on a small-cap-soft session — factor drag, not stock
  selection; one session, not a trend per lesson 28).
- No new satellite research happened this session (mechanical close only) — Monday's
  premarket board (OI needs a catalyst check, CAPR PDUFA outcome from 8/22, screeners
  re-run) is still outstanding from the Week 35 watchlist in research_log.md.

## 2026-08-21 — WEEKLY REVIEW (Week 34, Friday post-close)

**Grade B−. Best relative week of the regime (+2.03% vs SPY) — and none of it was earned
this week.**

- 📊 **Book $3,152.18 → $3,173.17 = +0.67%** vs **SPY −1.37%** → **+2.03%**. IWM −1.68%.
  Attribution: satellite **+2.18%**, cash **+0.10%**, factor **−0.24%** (the core *lost*
  to SPY). **Real alpha +2.18% — but 100% of it is OMER, opened 8/14.**
- ✅ **Since-rebase hand-built chain REBUILT** (the flagged task). Cash reconstructed
  transaction-by-transaction to **$237.54**, independently matching the 8/21 premarket log.
  Position P&L ties to the book change to the cent. **Since 7/20: Rocket +4.53% vs SPY
  +3.18% = +1.35% — first positive reading since the rebase.** Cumulative real alpha
  **+1.53%** (was −0.65%).
- ⚠️ `portfolio_state.md` now reads +1.28% — only 7bp off. **Coincidence, not a fix**:
  Bull's cumulative return happens to sit near Rocket's. Lesson 23 unchanged.
- 🚨 **THE FINDING: ETON was graded on a counterfactual nobody checked.** The 8/20 close
  claimed it beat where the trailing stop would have fired. **False** — HWM $63.83 → stop
  **$59.36**; 8/20 low $59.59, 8/21 low $59.76, **never touched**; ETON closed **$63.47**.
  Holding = **+$19.74**. The discretionary close **cost $25.83 = 0.82% of book.** It also
  violated **lesson 30a** (a Form 144 is not an exit trigger), written the day before.
  **Lesson 32 rewritten from a success into the error it was**; new rules 32a (only
  override a stop that is >2% away) and 32c (grade counterfactuals against the bars).
- ❌ **ARCT skip now costs +31%** ($10.28 → $13.45). Re-checked: **no new information**,
  readout still undated. **Gate held, per the lesson-35 pre-commitment.** Sizing — not the
  gate — escalated to the user.
- 🔧 **`position_reconciler.py` fixed** — three compounding parser bugs had it reporting
  Rocket's only satellite (OMER) as **UNATTRIBUTED**: `"CLOSE"` matched `(market_close)`;
  two-event headers dropped the second event; same-day round trips never closed because
  the log is written newest-first. **Now `✅ Balanced` for the first time**, and
  `position_table.py` includes OMER, which it had been silently omitting.
- 🗂️ Memory trimmed: research_log 191→103, market_context 241→88, session_notes 707→113,
  lessons 92→89. ⚠️ **lessons_learned is over its 60-line target and the overflow is all
  live standing rules** — flagged rather than cut.
- 📋 Week 35 watchlist built. **OMER's $19.71 rung (0.7% away) is the first check Monday.**
  ETON blocked by rule 13 at $63.47. Best fresh bar: **OI** (+12.5%, 98% of range) — needs
  a catalyst. **CAPR's PDUFA was Saturday 8/22 — check the outcome.**

## 2026-08-21 — MARKET_CLOSE (Friday, Week 34 day 5 — week close)

**OMER held overnight, core in band, no trades — cleanest close of the week.**

- 🟢 **OMER HELD.** Closed $19.24 at the week high, +3.3% on the day (8/20 close $18.63),
  fifth straight strong close. Stop still above entry; +15% rung ($19.71) 2.4% away,
  untouched — standing order to sell 9 sh on the touch carries into next week.
- ✅ **Core rebalance check: no trade.** IWM $2,416.79 vs target $2,333.15 — 2.64% of
  slice over, inside the 3% band.
- 📊 **Day**: hand-built book $3,137.45 → $3,169.89 = **+1.03%** vs **SPY +0.46%** →
  Rocket beat SPY by **+0.57%** today (script-verified position table: IWM +$19.29,
  OMER +$17.14, total +$36.43).
- ⚠️ **Since-rebase hand-built chain is stale** (last point 8/14, −0.78%) — flagged for
  reconstruction at the next weekly_review rather than guessed here. Do not quote
  `portfolio_state.md`'s +1.33% since-rebase figure as Rocket's own number (lesson 23).
- Week 34 summary: 1 satellite opened (ETON 8/17), closed 8/20 on the end-of-day rule
  (small loss). OMER (opened 8/14) carries into Week 35 still up double digits. Three
  straight no-entry sessions to close the week (8/19–8/21) — board quality problem
  (falsified scanner reads, crypto-treasury theme dominating), not a discipline lapse.

## 2026-08-21 — MARKET_OPEN (Friday, Week 34 day 5)

**No new satellite — the open confirmed the premarket call, and the board stayed weak.**

- 🚫 **NO ENTRY.** Portfolio synced clean: no overnight stops, IWM core and OMER both
  intact, no fills, weekly count still 1/5.
- Scanner at the open was still the same crypto-treasury sweep flagged premarket — USDE
  now **80.1x RelVol +33.5%**, plus GEMI/BKKT/ASST/ABTC/DFDV/HYPD/SBET/SECZ/BTGO, all
  mandate-excluded (lesson 31). ARCT +4.8% on 7.7x — standing skip, no new information.
  CAPR −0.9% — PDUFA is tomorrow 8/22, untouched either direction.
- 🆕 **ABUS checked and killed — new catalyst type to name explicitly.** +10.9% on a
  scanner-reported 11.4x RelVol, but `detail` showed real volume only **1.1x avg (2015k
  vs 1458k)** — another scanner/reality mismatch (lesson 17). One search found the actual
  driver: a **$230M Dutch-auction tender offer at $5.00–$5.75/share**, announced today.
  **A self-tender is not on the nine-catalyst list** — it's a capital-return event, and
  the band pins price toward the midpoint rather than a momentum breakout (same shape as
  lesson 27's pinned-price names, just self-imposed instead of a merger price). Rule 1:
  no catalyst = no trade.
- 🔵 **OMER unchanged** — $18.72, +15% rung ($19.71) still 5.2% away, untouched. Standing
  order to sell 9 sh on the touch stands.

## 2026-08-21 — PREMARKET (Friday, Week 34 day 5 — last session of the week)

**No new satellite, third straight session — but the board wasn't weak, it was FALSE. Raw
bars falsified all nine non-crypto "gainers." Two new rules: date your catalyst headlines,
and one session of rate relief is not a resolution.**

- 🚫 **NO ENTRY.** 🆕 **The scanner and the tape disagreed on EVERY non-crypto name.** The
  04:20 scan showed nine names +3.4% to +7.7%; raw daily bars showed all nine were
  **extended-hours quotes against red or flat 8/20 cash sessions**. UNCY closed at **15% of
  range**, **LFMD at 0%** (on the low, 0.3x volume), HDSN at **4%** (its real 3.5x event was
  8/17, four days stale), OSS at **10%** and **−16% in four sessions**, ALMU **−20% in
  three**; ENR/MAX had no catalyst inside 17/68 days; **BBW's open WAS its high** and it
  reports **8/27** (earnings-week rule). **Nine names, nine falsifications, one script call.**
  → **Lesson 17 at full strength: the scanner is a name source, never a signal.**
- 🆕 **APPS — new rule, and it nearly worked.** An overnight search returned *"Digital Turbine
  surges 22% after hours on a beat-and-raise, adj EPS $0.15 vs $0.05"* — the **exact** catalyst
  type that trades, on a name Rocket knows. **The article had no date.** Bars: 8/18 C 12.12 →
  8/19 C **11.23 (10% of range)** → 8/20 C **10.71 (6% of range)** on **0.5x** volume =
  **−11.6% in two sessions.** Weeks-stale print, fully faded. → **new lesson: extend rule 11a
  from analyst headlines to CATALYST headlines — date the news against the bars.**
- ⚠️ **ARCT — the skip is now costing money, and it still stands.** It ran a **second**
  volume-expansion day: **+6.9% at 66% of range on 2.9x** (after 8/19's +25% on 7.2x). One
  search re-tested the kill: **no new information entered the market** — same Aug-6 Q2/CSL
  material, same Canaccord PT **cut**, and the company re-confirmed **ARCT-810 Phase II data +
  regulatory path "Q3 2026," still undated**, inside any 1–5 day hold. **Lesson 29 intact; a
  7% stop fills at the open, wherever the open is.** 🚨 **Recording the cost (~−7% foregone
  and counting) for the weekly review — do NOT loosen the calendar gate because price went the
  other way.**
- 🆕 **Crypto-treasury theme topped the scanner a THIRD straight session** — **USDE +19.3% on
  26.1x RelVol**, the biggest print on the board, plus DFDV/ABTC/SBET/ASST/FWDI/SECZ/BKKT/
  GEMI/HYPD. All excluded on **mandate** (lesson 31); none re-screened. **Consequence worth
  naming: while tokens rally, the scanner's top tier is useless to Rocket and the real board
  must be built from the names beneath it — which is exactly where the bars-falsify-all
  problem bites. Three no-trade sessions is a board-quality problem, not a discipline one.**
- 🚨 **10-yr: yesterday's resolution was given back in ONE session — 4.65% → 4.70% (+5bp),
  cushion to the 4.75% trigger re-narrowed from 10bp to 5bp.** Thursday's "the standing rate
  flag stands down a notch" was **premature**. → **lesson 28's logic applies to rates too: one
  session of relief is not a resolution.** ✅ VIX **15.63**, no brake. ✅ Futures green across
  the board, **Russell +0.65% tied best.** ✅ **Brent's four-session ramp STALLED** (+0.19%,
  $93.96, still under the $95 watch). 🚨 **Gold is now the live trend: $4,639 (+2.72%),
  +5.1% in three sessions and accelerating.** **Gold making highs while yields RISE** is the
  more uncomfortable combination — flagged to the weekly review, not actionable at 1–5 days.
- 🔵 **OMER — best bar on the book. 8/20: O 18.30 H 18.73 L 18.07 C 18.63, +1.8% at 85% of
  range** on a day IWM fell −1.34%. **Four straight closes at 72–85% of range.** Stop ≈$17.57,
  **$0.43 ABOVE the $17.14 entry — cannot lose money.** 🚨 **+15% rung $19.71 is 5.2% away —
  SELL 9 SHARES ON THE TOUCH** (MRLN round-tripped unscaled). ⚠️ 🆕 Position has drifted to
  **16.0% of book, above the 15% max-satellite line** — pure appreciation, not a violation
  (the cap binds at entry), but a **second independent argument for taking the rung**, which
  returns it to ~10.7%. ATM still undrawn; ladder open ($33 PT).
- 🗓️ **Calendar clean today. Jackson Hole confirmed Aug 27–29 (Week 35)** — six days out, and
  it lands inside any position opened late next week. **Earnings pipeline empty FIVE straight
  sessions**, the longest drought recorded; nearest **QMLS 8/25, LTRX 8/26** (LTRX stabilised
  8/20 at **71% of range on 1.4x** — the best-defined event on the calendar, carry forward).
  🚨 **CAPR PDUFA is TOMORROW 8/22**; it closed 8/20 at **1% of range** — standing skip, do
  not touch in either direction.
- Book **$3,137.45** (hand-built, lesson 23a) = IWM 8.0522 sh $2,396.90 (76.4%) + OMER
  $503.01 (16.0%) + cash $237.54 (**7.6% — inside the buffer, no bearish thesis needed**).
  **92.4% invested.** 8/20: −0.96% vs SPY −0.84% (−12bp), IWM −1.34%. Core is **$76 / 2.4%
  OVER** target — **inside the 3% band, erring toward more invested. No rebalance until
  `market_close`.** Satellites **1/4**, weekly count **1/5**.

## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
