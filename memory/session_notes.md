# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-09-23 — MARKET_CLOSE (Wednesday, Week 39 day 4) — HOLD RARE overnight, core in band, satellite floor breached 4th consecutive `market_close` session

**Step 1/2**: `portfolio_snapshot.py` synced clean. RARE (31 sh @ $15.08, day-1) at
$14.895, -1.23% from entry, well clear of the $14.00 trailing stop. FDA-approval
catalyst is explicitly multi-day (breakout thesis) — held overnight per the
close-rule's multi-day exception, same conclusion midday already reached. IWM core
5.4746 sh, -5.2%/-$84.79 all-time, no stop by design.

**Step 2.5**: Core rebalance check — IWM $1,544.08 vs target $1,552.08 (new-cap
formula), -0.26% of slice, well within the 3% band. **HOLD, no trade.** Satellite
floor: 14.9% < 50%, **4th consecutive actual `market_close` breach** (9/17, 9/21,
9/22, 9/23). Rule 8's MEDIUM bar has been active since 9/21 and stays active. Logged
as lesson 63 — cash above the 10% buffer (~35% of slice) is the mechanical byproduct
of IWM at its cap with only 1/4 satellite slots filled, not a bearish call.

**Step 3**: No new fills to log — RARE already logged at this morning's `market_open`.

**Step 4**: Day P&L (`position_table.py`) IWM -1.82%/-$28.58, RARE -1.39%/-$6.51,
book total -$35.09/-1.13% of slice, vs IWM benchmark today -1.80%. Weekly count 1/5.

---

## 2026-09-23 — MIDDAY (Wednesday, Week 39 day 4) — HOLD RARE, no cuts, no afternoon entries

**Step 1**: `portfolio_snapshot.py` synced clean. Rocket holds IWM core (5 sh, -4.9%,
no stop by design) and RARE satellite (31 sh @ $15.08, now $14.91/-1.1%). Satellite
floor still 14.9% (breached, unchanged since this morning's buy — one satellite can't
close a 50% floor alone).

**Step 2**: RARE reviewed against the cut/tighten/hold criteria — down only 1.1% from
entry (well inside the 5% cut threshold), FDA approval catalyst (UX111/Fayuvi, 9/17)
unchanged, not up enough to tighten the trail. **HOLD**, stop unchanged at $14.00 (7%
trail, HWM $15.055).

**Step 3**: News check on RARE surfaced a Pomerantz Law Firm "investor alert" dated
9/22–9/23 and stale coverage of the Phase 3 Aspire trial miss for **apazunersen**
(Angelman syndrome) — an **unrelated drug program** that crashed the stock 44% on
9/2–9/3, three weeks before Rocket's entry and already fully priced into the base the
9/17 breakout traded off. The "investigation" is a plaintiff-firm solicitation ad
referencing that same stale trial miss, not new information, and does not bear on the
UX111 catalyst. **Assessed as noise, not a negative-news cut trigger** — new lesson 62.

**Step 4**: `unusual_volume` scan checked for afternoon setups. Two positive movers
with real volume: **NNBR** (+11.4%, upper-half-of-range guidance language, no hard
numeric raise, already up 190% YTD and extended intraday — soft-raise shape, not a
rung-1 catalyst) and **CBRL** (Q4 beat but FY revenue guide **0.8% below consensus** —
fails rule 5c's "guide below consensus is not a raise in any framing" outright). Both
killed. No new entries.

**Step 5**: No position changes to `portfolio_state.md` (already fresh from this
session's `portfolio_snapshot.py` sync). Lesson 62 added to `lessons_learned.md`.

---

## 2026-09-23 — MARKET_OPEN (Wednesday, Week 39 day 4) — RARE BUY; satellite floor breach closes from 4 consecutive sessions

**Step 1**: `portfolio_snapshot.py` synced clean. No overnight fills/stops on the IWM core
or Bull's SPY. Cash $1,902.82 pooled, market open, 0/5 weekly trades used.

**Step 2**: Premarket's sole candidate, **RARE** (Ultragenyx — FDA full approval of Fayuvi,
9/17, MEDIUM conviction, entry conditional on volume confirmation per lesson 59), checked at
the 9:45 ET checkpoint: price $15.06 (+2.8%), a fresh weekly high, holding cleanly above the
$14.51–$14.65 base; volume 278k vs ~259k expected pace by that point (~1.07x) — real
regular-hours trades, confirms it wasn't a premarket quote artifact. Cleared all universe/
guardrail checks (mcap $1,485M, price, ADV 6.725M avg, DE domicile already confirmed
pre-market).

**Step 3**: Sized at the 15% cap (31 sh, $466.86) via `alpaca_client.py size`. Bought 31 sh
@ $15.08 avg fill. 7% trailing stop live at $14.00 (HWM $15.055). Logged to `trade_log.md`.

**Step 4**: `unusual_volume`/`top_movers` rerun — only GRML crossed both lists again
(40.3x/+12.5%), reconfirmed as a standing kill (lesson 60, stale EDGAR domicile record,
further extended). INNV (-10.8%) not a long candidate. No second entry.

**Step 5**: Final `portfolio_snapshot.py` sync — satellite floor moves **0.0% → 14.9%** of
slice (still breached; one satellite at the 15% position cap cannot close a 50% floor alone,
more entries needed). Rocket positions 1/4 (RARE), combined account positions 2 (RARE, IWM)
+ Bull's SPY = 3/7. ntfy trade notification sent.

## 2026-09-22 — MARKET_CLOSE (Tuesday, Week 39 day 2) — NO TRADE; core in band, satellite floor breached 3rd consecutive `market_close` session (lesson 61)

**Step 1/2**: `portfolio_snapshot.py` synced clean. No satellite positions to review (0/4)
— Step 2 had no rows. Only position is IWM core, 5.4746 sh, -3.49%/-$56.84 all-time.

**Step 2.5**: Core rebalance check — IWM $1,572.09 vs new-cap target $1,565.70, +0.20% of
slice, well within the 3% band. **HOLD, no trade.** Satellite floor: 0% < 50%, **3rd
consecutive actual `market_close` breach** (9/17, 9/21, 9/22 — 9/18 never ran, lesson 58).
Rule 8's MEDIUM bar was already active all session (premarket/market_open/midday) and
carries unchanged into 9/23 premarket. Logged as lesson 61 — CLAUDE.md defines no
escalation past "2 consecutive," so this session's action was logging the pattern for
`weekly_review` to grade.

**Step 3**: No fills to log.

**Step 4**: Day P&L IWM +0.55%/+$8.60 vs IWM benchmark +0.53% (spread ~0 by construction,
no satellites). Weekly count 0/5.

**Step 5**: ntfy summary sent — see confirmation below.

**Step 6**: memory pushed to GitHub.

---

## 2026-09-22 — MIDDAY (Tuesday, Week 39 day 2) — NO TRADE; no Rocket satellites to review, 4 afternoon movers checked and killed (new lesson 60)

**Step 1/2**: `portfolio_snapshot.py` synced clean. Rocket owns only the IWM core (5 sh,
$1,569, 50.1% of slice, no stop by design) — zero satellites open, Step 2's position
review had **no rows**, no cuts, no stop changes. SPY confirmed Bull's.

**Step 3**: N/A — no Rocket satellite positions to news-check.

**Step 4**: `unusual_volume` re-run, four names checked inline (web search, <5 lookups,
no subagent). **GRML** (+73.6%, 44.7×) had a real catalyst (Sarfartoq rare-earth land
expansion + US-Denmark-Greenland security deal) but killed on two independent grounds:
EDGAR shows a **serial-rebrand shell** (Redwoods Acquisition Corp → ANEW Medical →
Klotho Neurosciences → Greenland Mines, 3 renames since 2022) with a **blank
`stateOfIncorporation`** and stale SIC code — an unconfirmable domicile gate, lesson 38
FAIL — and the stock is already **+474% over 4 sessions**, far past any fresh-setup
window. Written up as new **lesson 60**. **EAF** reconfirmed the standing no-catalyst
kill (scanner artifact — stock actually closed red today). **SVIA** (ticker rebrand,
BRR→SVIA) killed on rule 1 — a name change is not a catalyst type. **CYPH** reconfirmed
the standing rule 31 crypto-treasury mandate exclusion. **No new candidate found.**

**Step 5**: Satellite floor still breached at 0% — unchanged since 9/17. If still 0% at
today's `market_close`, that's the 3rd consecutive breach (escalation territory per rule
8 for tomorrow's premarket). No forced cuts made, no notification sent (routine only
requires one on a forced cut).

---

## 2026-09-22 — MARKET_OPEN (Tuesday, Week 39 day 2) — NO ENTRY; MLKN closed on Gate A (guide cut, not raised); widened board found nothing

**MLKN's Q1 FY27 print (8-K ex-99.1, primary source): revenue $923.4M missed BOTH consensus
($943.3M) AND MLKN's own guide floor ($928M); net sales −3.4% YoY organic; NA Contract
−5.2% organic, Intl Contract −6.2% organic.** GAAP EPS $0.38 beat $0.35 consensus — the
only clean beat. **FY27 guide: revenue range CUT $3.93–4.13B → $3.88–4.03B (≈−1.9% at
midpoint); adj EPS range UNCHANGED $1.85–2.15 (reaffirmation, lesson 5f = 0% change).**
Gate A ("guide must be RAISED >1.0%... a reaffirmation is a KILL") fails outright — this is
worse than a reaffirmation, it's a top-line cut. Stock +1.7%, below MA20/MA50 — the tape
confirms the weak print. **CLOSED**, gates B–F never reached.

**Widened per rule 8's MEDIUM bar** (satellite floor still 0%, 2 consecutive breaches):
checked `unusual_volume`/`top_movers` inline for anything with real volume + a named
catalyst. **MAZE** (+28.2%, biggest mover) had no dated catalyst — IR page's latest item is
9/02 investor-conference attendance; its one real data readout is 6 months stale. **VFF**
($3.09, CEO bought $101K/35k sh, +0.36% of his stake) — catalyst too thin, and real volume
is 0.9x avg despite the scanner's screener printing 4.5x RelVol (another RelVol/reality
mismatch, lesson 17g — real volume, not the RelVol column, is what's authoritative). **FOSL**
— no news since Q2, reiterated guidance, not a catalyst. All three killed on rule 1 (no
named catalyst) or volume-not-confirming. Macro context ruled out a beta explanation: SPY
+0.08%, IWM +0.61%, a mildly green tape, not a risk-on day.

**Verdict: NO ENTRY.** Satellites remain 0/4, 0% of slice. If still 0% at today's
`market_close`, that's the 3rd consecutive breach. Full detail: `research_log.md` MLKN
close-out + widen section.

## 2026-09-22 — PREMARKET (Tuesday, Week 39 day 2) — NO ENTRY; **the entire `top_movers` board was fiction and lesson 55b's check passed anyway** (new lesson 59); ONE live candidate queued (MLKN, BMO today)

**Satellite floor breached 2 sessions running (9/17, 9/21 `market_close`) — searched at the
MEDIUM-conviction bar per rule 8**: all four screeners run, pushed deeper down each list, plus
the earnings calendar ahead of any screener (41b). Satellites 0/4 · weekly 0/5 · no trades.

- 🥇 **THE FINDING — `top_movers` reconciled 8-for-8 under lesson 55b and every row was still
  built on a price at which nothing traded.** Actual tape (Alpaca `sip`, 08:00Z→10:23Z):
  **six of eight names had ZERO premarket trades** (FBRT, GOSS, QTRX, QUIK, SIGA, ACCO);
  **EVMN's "+7.2%" is a single 202-share print** (306 sh / $3,081 all session); and **BBW,
  printed at $26.03/+5.2%, actually traded 500 sh at $24.74 = −0.0%.** **55b tests the
  scanner's arithmetic, never the liquidity behind the numerator.** → **New lesson 59**, and
  **59b names it as the mirror of 55a: a false instrument PASS is more seductive than a false
  kill, because a passing check feels like evidence.**
- 🚨 **59c — the check nearly became its own opposite.** The first liquidity pull used Alpaca's
  **`iex` feed, which returns ZERO premarket bars for every name including SPY/IWM/AAPL.**
  Uncorrected, "zero volume everywhere" would have been a fabricated finding off the wrong
  feed — **lesson 38's blank-result trap occurring inside the check built to catch it.** The
  `sip` control exposed it in one call. **Always run a liquid control before believing a
  blank, especially when the blank is the answer you expected.**
- 📌 **59d — NOT load-bearing.** All eight independently failed a **named** gate anyway:
  EVMN a **FAILED Phase 2b** (EVO756 in AD missed every endpoint, 9/08 — the only dated news
  is bearish; the 9/15 item is a deck, per the ASPN precedent) · BBW a **guidance cut** at a
  fresh 52-wk low · FBRT a CEO shuffle + routine $0.20 dividend · **GOSS** real FDA progress
  but **up to $250M of structured financing against a $69M cap ≈3.6× the company** on a 3.8M
  float (rule 7a/49b) · CURR unresolved issuer identity (rule 38).
- 🎯 **THE ONE LIVE CANDIDATE: MLKN (MillerKnoll), Q1 FY27 BMO today** — sourced from the
  **earnings calendar, not a screener** (41d now 4-for-8). Gates cleared: domicile **MI** ✅ ·
  rule 13 (+25% → $1,746M, clears $2B) ✅ · **rule 46 median ADV 627,900, passes by 109%, all
  5 recent sessions above gate — clean on every cut** ✅ · **rule 8 dilution: NO live shelf, no
  ATM, no 424B5; last S-3ASR 2017, everything since is S-8 only (8b)** ✅ · **rule 11 ladder:
  +15% $23.37 / +25% $25.40 both clear a dated $35.00 target with room** ✅ (⚠️ only 1–2
  analysts, quoted avg/low internally inconsistent — thin, passes weakly).
- ⚠️ **What can kill MLKN, stated in advance**: (1) 🚨 **GAP risk, not range.** Its own 2-y
  earnings gaps include **−25.83%** and −9.45% — **a 7% trail cannot price that; it fills at
  the open** (45a/29). Predicted catalyst range 11.60% = **1.66× the trail** — the *closest to
  fitting* any catalyst name has come in weeks (cf. KMTS 2.70× · FTK 4.33× · EAF 6.89×), but
  the range figure is the optimistic half of the history. (2) 🚨 **Consensus is a LOWERED bar**
  — Street EPS **cut 14.6% in three months ($0.41 → $0.35)**, so rule 5c applies: **grade
  against MLKN's own Q1 guide ($928–968M), not consensus.**
- 📌 **Six gates pre-committed for `market_open` as SHAPES not levels** (42c/42e): A size the
  raise >1.0% vs MLKN's OWN prior FY27 guide · B pass-through · C **close in upper half of
  range or KILL** · D gap rules · E composition (5e) · F **open/unresolved**: four Form 144s
  and heavy Form 4 clusters post-10-K, **10b5-1 flag NOT yet read — flagged, not scored** (30b).
- 🥇 **The old "factor watch" framing is retired.** Since the benchmark became IWM (9/17), the
  core contributes **zero excess return by construction** — IWM-vs-SPY is no longer a drag.
  **What replaces it is the real cost of the breach: ~49.6% IWM + ~50% idle cash against a
  100% IWM benchmark, so every 1% IWM gains costs Rocket ≈0.5% of relative performance.
  Monday IWM +0.52% → ≈ −0.26% vs benchmark in one session.** Not a market call; a
  stock-picking gap being paid for daily.
- ✅ **Macro permissive, rule 29 blocks nothing**: VIX **14.80** (new low), futures mildly green
  with **RTY the strongest of the three for the first time in weeks** (lesson 28 — flagged, not
  booked), **crude breaking down hard, WTI through $90**, 10-yr 4.96% still ~21bp through
  trigger but no longer making highs. **No macro excuse for the zero — this was supply.**
- 🔧 Instruments: `macro` clean 18th session (WTI roll patch fired, naive −6.60% → true
  −3.15%). `eligibility` 8→8 twice (43 held). **RelVol unusable 6th straight session**;
  `breakouts` **errored on Finviz**. ⚠️ **EDGAR ticker lookup resolved `CURR` to the wrong
  company (Avenir Wellness, DE)** — verify the returned `name`, a ticker→CIK map is not
  authoritative.

**🚨 Open threads**: `weekly_review` **W36/W37/W38 all still owed** — 19+ sessions stale,
tenth session flagging W36 (lesson 47c). Two escalations unchanged (rebalance basis, ADV-vs-
account-size — **note MLKN does not raise the latter**; a ~$470 satellite fills trivially in a
628k-ADV name).

---

## 2026-09-21 — MARKET_CLOSE (Monday, Week 39 day 1) — NO TRADE; core in band, satellite floor breach logged (2nd real `market_close` session, corrected from a miscounted "2nd of 9/17,9/18")

**Step 2**: No Rocket satellite positions to review (0/4, unchanged since 8/26 OMER
stop-out) — no rows. IWM core (5.4746 sh) unchanged; JPM/SCHW/SPY reconciled to Bull.

**Step 2.5**: Core rebalance check — IWM $1,564.26 vs target $1,577.91 (min of the 10%
buffer formula and the new 50% cap) = -0.43% of slice, well inside the 3% band. **HOLD,
no trade.** Satellite floor still breached at 0% — flagged as lesson 58: this is only
the **2nd actual `market_close` session** to log the breach (9/17, now 9/21), not the
"9/17, 9/18" pair cited earlier today — **no `market_close` ran on 9/18** (quota gap).
The MEDIUM-conviction bar already active since this morning stands on its own merits
regardless of the off-by-one. Full detail in `trade_log.md`/`lessons_learned.md`.

**Step 3**: No fills to log.

**Step 4**: Day P&L (`position_table.py`): IWM +0.54% / +$8.38, matching the benchmark
(+0.57%, `market_data.py`) within timing noise — ~0% spread by construction, no
satellites. Since-rebase chain not recomputed (stale, three weekly_reviews owed:
W36/W37/W38).

**Step 5**: ntfy summary sent — see confirmation below.

---

## 2026-09-21 — MIDDAY (Monday, Week 39 day 1) — NO TRADE; no Rocket positions to review, afternoon scan found nothing new

**Step 1/2**: `portfolio_snapshot.py` synced clean. Rocket owns only the IWM core
(5.4746 sh, $1,566, 49.7% of slice, no stop by design) — zero satellites open, so
Step 2's position review had **no rows**. JPM/SCHW/SPY confirmed Bull's (reconciliation
balanced). No cuts, no stop changes.

**Step 3**: N/A — no Rocket satellite positions to news-check.

**Step 4**: Re-ran `unusual_volume`/`top_movers`. Overlap tier unchanged from
market_open (PRTH, NUAI, OPTX, SECZ — all already killed on hard gates this morning).
Scanned the rest of `top_movers` for a fresh RelVol-confirmed mover: only **EAF**
(+9.1%, 1.9x) had both a real move and volume; web search turned up no dated catalyst
for today, consistent with its standing no-catalyst kill history — not re-opened.
Everything else on the list moved on <1.5x RelVol (no volume confirmation). **No new
candidate found.** Full detail in `research_log.md`'s midday addendum.

**Step 5**: Satellite floor still breached at 0% (unchanged since 9/17, now the 2nd+
consecutive close under the MEDIUM-conviction bar). No forced cuts made — no
notification sent per routine (only required on a forced cut).

---

## 2026-09-21 — MARKET_OPEN (Monday, Week 39 day 1) — NO TRADE; **no premarket ran today**, 4 fresh names screened inline, all killed on hard gates

**Step 1**: `portfolio_snapshot.py` synced clean — no overnight fills, no stops
triggered. IWM core unchanged, JPM/SCHW/SPY confirmed Bull's. Shared account
$10,479.87 → $10,477.53 across the session, slice ~$3,143, cash $1,665.04 (pooled).
Satellites still 0/4 — **floor breached for the 2nd consecutive `market_close` (9/17,
9/18)**, so rule 8's MEDIUM-conviction bar is active for any new candidate today.

**⚠️ No `premarket` session exists for today** — `research_log.md`'s last entry was
Friday 9/18. Per [[launchd-quota-contention]]/lesson 47a this reads as a starved
session rather than "nothing to research." Did the discovery work inline here instead
of only validating a queued list, per Step 2/4 combined.

**Screened 4 names, killed all 4 on hard structural gates** (full gate detail in
`research_log.md`): **PRTH** — all-cash take-private at $8.05, live $7.78 = pinned
3.5% spread, rule 27. **OPTX** — Space Force optics order, but avg volume 258k fails
the 300k liquidity gate and the only quantified contract figure found ($1.9M) is
immaterial against the $340M cap (rule 49a). **NUAI** — real dated Vistra/Luminant PPA,
but a Macquarie waiver **mandates** New Era establish a $100M ATM within 60 days
(lender-forced, not discretionary — worse than any self-initiated shelf graded so far),
stacked with −82.5% revenue, non-cash consideration, 2027 delivery, and an already
+41.2%/5-day extended tape. **SECZ** (Friday's re-open candidate) — ran to $1.873B
market cap (+44% 5-day, +79.3% 1-month), now within ~6.8% of the $2B universe ceiling;
rule 13 kills it cleanly regardless of the still-unresolved lock-up question. Fresh-
mover scan overlap tier was entirely standing crypto/treasury mandate kills and
standing liquidity/tape kills — nothing else cleared a first read.

**Result: 0/4 satellites, 100% IWM core held, NO TRADE.** No notification — flat
session, no stops hit, no news on the core. The MEDIUM bar (rule 8) had nothing to
admit: every kill today was a hard gate (liquidity, pinned deal price, mandated
dilution, cap ceiling), not a conviction judgment call, so widening the bar changed
nothing. Floor breach carries to today's `market_close` for a 3rd-consecutive-session
count if unresolved by midday. `weekly_review` backlog now **three** owed (W36/W37/W38)
— unchanged, carried forward. Two open escalations (rebalance basis, ADV-gate-vs-
account-size) also carried forward; both unchanged since 9/17.

---

## 2026-09-18 — MIDDAY (Friday, Week 38 day 5) — NO ACTION; core-only book, no new candidates

**Step 2**: Rocket owns only the IWM core (5 sh, $1,548, 49.7% of slice, no stop by
design) — JPM/SCHW/SPY on the shared account confirmed Bull's via `position_reconciler`
(Position Reconciliation block). Nothing to cut, nothing to tighten. IWM is down modestly
intraday (prior settled close $285.43 → live $282.77, ≈-0.93%) with no news event behind
it — ordinary tape noise, no override.

**Step 4 (afternoon scan)**: `unusual_volume` + `top_movers`, inline. Overlap tier BNC ·
DFDV · USDE · HYPD · SECZ, plus new prints GLOO, CYPH, GEMI, ABTC, QMLS, FWDI, XTND, ALMU,
ARRY, FLNC — every one is either a standing crypto/treasury mandate kill (lesson 31: BNC,
DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI are all crypto exchanges/miners/treasury
proxies), a standing liquidity/tape kill already on today's premarket board (GLOO, XTND,
ALMU, ARRY, FLNC), an S&P 500 component (FMC — mandate-excluded regardless of the print),
or a closed-end fund (PML). **SECZ** (the one real catalyst on the board) is unchanged
from premarket — still blocked on the pre-committed re-open condition (lock-up schedule +
float reconciliation, `research_log.md`), neither leg resolved since this morning. No
genuinely new candidate.

**Result: 0/4 satellites, floor still breached (0% < 50%), NO TRADE.** No notification —
no stops hit, no forced cut, no news on the core. This is the 2nd session today (after
market_open) independently confirming nothing qualifies; the breach carries to
`market_close` for the 2nd-consecutive-session count, which per rule 8 opens Monday
9/21 premarket at the MEDIUM conviction bar if still breached at today's close.

---

## 2026-09-18 — MARKET_OPEN (Friday, Week 38 day 5) — NO TRADE, confirms premarket's NO ENTRY

**Step 1**: `portfolio_snapshot.py` synced clean — no overnight fills, no stops
triggered. IWM core unchanged (5 sh live, book raw qty carried from premarket),
JPM/SCHW/SPY confirmed Bull's. Shared account $10,387.37, slice $3,116.21, cash
$3,188.64 (pooled). Satellites still 0/4 — floor breach unresolved (0% < 50%).

**Step 2**: Nothing to validate — premarket's verdict was NO ENTRY on both live
candidates. PAAI is CLOSED (catalyst falsified at the primary source, lesson 57).
SECZ's re-open condition (lock-up schedule + float reconciliation) was not met
this morning — still pending, not re-checked here since nothing new arrived.

**Step 4 (fresh-mover scan)**: `unusual_volume` + `top_movers`, inline, 2 calls.
Every row is already accounted for: standing mandate kills (BNC, USDE, DFDV,
HYPD, QMLS, BKKT — crypto/treasury, lesson 31), standing tape/liquidity kills
(GLOO, CYPH, XTND, RARE, RCAT, ALMU, FLNC, LTRX, CHPT, PLAY), or today's own
premarket kills (SECZ, AHRT). **FWDI (+10.6%, 3.4x RelVol) was the one name not
already on a list** — checked inline (one search): it's a Solana-treasury
company (Forward Industries pivoted to a SOL treasury strategy), so it's the
same crypto/treasury mandate kill as BNC/USDE/DFDV before any chart is worth
reading (lesson 31). No genuinely new candidate on the board.

**Result: 0/4 satellites, 100% IWM core held, NO TRADE.** No notification —
flat session, no stops hit, no news on the core. Satellite floor breach carries
to today's market_close for the 2nd-consecutive-session count (research_log.md);
if still breached at close, Monday 9/21 premarket opens at the MEDIUM bar per
rule 8. Escalations (rebalance basis, ADV-gate-vs-account-size) and the
W36/W37/W38 `weekly_review` backlog are unchanged — carried forward.

---

## 2026-09-17 — MARKET_CLOSE (Thursday, Week 38 day 4) — CORE REBALANCE (IWM SELL), first session under the new 50% cap; satellite floor breached 0%, 1st session

No satellite positions to review (0/4, unchanged since 8/26). The real event: this
morning's CLAUDE.md rewrite (commit 348cc06) caps IWM core at <=50% of slice instead of
letting it absorb everything satellites don't use. With satellites at $0, IWM had drifted
to ~90% of slice over the last three weeks under the old rule — the new formula put target
at $1,563.34 vs a live $2,816.65, **40.1% of slice over, nowhere near the 3% band.** Sold
**4.389 sh IWM @ $285.585443 = $1,253.55**, landing core exactly on the new 50% cap
(confirmed via `portfolio_snapshot.py`'s Satellite Floor block). Proceeds went to pooled
cash — there's no satellite to fund it into — which pushed Rocket's book cash from ~6% to
**~50% of slice** in one session. No bearish thesis written; per CLAUDE.md this is the
stock-picking gap made visible on purpose, not a market call. Full arithmetic in
`trade_log.md`; new lesson 56 in `lessons_learned.md`.

Day P&L (hand-computed, book basis, since `position_table.py`'s post-sale qty understates
it): **IWM +$16.78 / +0.60%**, matching the benchmark exactly — the rebalance itself is
P&L-neutral. Satellite floor is breached (0% < 50%) but this is only the **1st session**
the guardrail has formally existed (it wasn't a named breach under the old rule) — no
escalation required yet. **If tomorrow's close is also <50%, Monday 9/21 premarket must
prioritize closing the gap.** PAAI (real, verified $1B deal, barred only by the >35%
same-day rule) is the live second-day candidate best positioned to close it first — carries
into tomorrow's premarket.

Notification sent — see `trade_log.md` for confirmation status.

---

## 2026-09-17 — MIDDAY (Thursday, Week 38 day 4) — NO ACTION; 0 satellites (core-only book), one real catalyst (PAAI) barred by the 35% same-day rule

Position review trivial: Rocket owns only the IWM core (no stop by design, exempt from
position limits) — JPM/SCHW/SPY on the shared account confirmed Bull's via
`position_reconciler`. Nothing to cut, nothing to tighten.

Re-scanned `unusual_volume` for afternoon setups. One name worth recording: **PAAI**
(Paradium.AI, fka The Arena Group) spiked **+271%** ($0.90 → $3.34) on a real, dated,
web-verified catalyst — a 10-year **$1B Roundtable MediaOS deal** plus an $89M/49%
minority investment. Ran the lesson-17/55 reconciliation before trusting it: raw yfinance
bars confirm the move is genuine (31.76M volume vs a 13.1M float — 2.4x turnover), not a
scanner artifact. **Not tradeable today** — CLAUDE.md's >35% rule requires a second-day
entry, and every close in the trailing 5 sessions was under $3.00 (today is the first bar
to clear the price floor, on the spike itself). Logged in research_log.md as a 3-day
missed-catalyst watch per the standing rule. Rest of the board was mandate-kills
(USDE, BRR — crypto/treasury), liquidity-locked (GLOO), or already-closed names
(ACVA, ALMU). No trade.

Satellite floor remains breached (0% < 50%, portfolio_state.md) — unchanged from premarket.

**Open thread for market_close**: no rebalance action expected beyond the usual core
band check; PAAI carries into tomorrow's premarket as a live second-day candidate.

---

## 2026-09-17 — PREMARKET (Thursday, Week 38 day 4 — **first post-FOMC session**) — NO ENTRY; **rule 29 lifted and the board died on catalyst quality instead**; KMTS gates B+E passed and rule 4 CLOSED it

**Book (hand-built, lesson 23a — BASE NAMED per rule 44): $2,992.32** = IWM **9.8636 sh**
($2,800.31 @ the settled 9/16 close of $283.92, **93.58%**) + notional cash **$192.01 (6.42%)**.
✅ **Inside the 10% buffer — no bearish thesis required.** Satellites 0/4 · weekly 0/5 ·
max satellite $469.25 · 1.5% risk $46.92. Raw fractional qty pulled from
`GET /v2/positions/IWM` per lesson 24a/24d — **the snapshot table printed "10" for a FOURTH time.**

- ✅ **FOMC delivered 25bp as priced. Rule 29's three-session board-wide block is LIFTED** —
  and **seven in-universe names were then screened and killed on their own merits.**
- 🥇 **THE FINDING: for the first time in nine sessions, stop width was NOT the binding
  constraint — and that is evidence AGAINST Rocket's own lesson 48a.** 48a/48e/48g reframed
  lesson 36 from a *board-quality* problem into a *mandate-quality* one: "the catalyst screen
  works and the stop width forbids everything it finds." Run 48d's diagnostic on today's
  survivors' **normal-day median ranges**: **UNCY 5.56% (0.79×), GLAS 5.61% (0.80×), KMTS
  6.30% (0.90×), DUOT 6.84% (0.98×), HAWK 6.87% (0.98×)** — **five of seven FIT inside a 7%
  trail.** The board still produced nothing, because the catalysts were **an MoU with zero
  committed dollars (HAWK), a $400,000 award against a $224M cap (OSS), an unexplained
  cannabis premarket print (GLAS), and a class-action-adjacent bounce off a CRL (UNCY).**
  **The two constraints are separable and today separated them. 48a was over-claimed.**
  Written against Rocket's own argument (45h/51e) → **new lesson 53.**
- 🚨 **THE SECOND FINDING: yesterday's MDD statistic now cuts AGAINST the change Rocket asked
  for.** Lesson 51 argued MDD-from-HWM should replace `range ÷ trail` on the evidence that
  KMTS's 9/15 bar had a **6.18% MDD** — trail survives, **+15.49%.** Measured identically on
  the next bar, **KMTS 9/16 MDD = 5.80% (77 five-min bars): the trail survived AGAIN and the
  trade lost 4.44% open-to-close.** 51's *correctness* is untouched; **the claim attached to
  it is not. MDD removes a false veto; it does not supply an edge.** Escalation 2 re-stated on
  **accuracy grounds only** → **new lesson 54.**
- ❌ **KMTS CLOSED — and it cleared two more gates on the session that killed it.** Gate **B**
  ✅ (9/16 range **6.10%** ≤10%, held exactly as written per 42/51d despite 51 proving it
  measures the wrong thing) and gate **E** ✅ (FOMC done). 🚨 **Rule 4 is the binding kill:
  9/16 closed −4.37% at 15.0% of its range on 825,000 sh = 2.58× the 63d median / 3.25× the
  2y median.** Distribution. **SPY −0.44% and IWM −0.43% do not explain a −4.37% day.** Also
  the day-2 continuation window is spent (catalyst 9/14 AMC → day 1 9/15 → day 2 9/16 gave it
  back; today is day 3). **CLOSED, not deferred** (42d/45e). Gate G (Bermuda) still owed.
  🥇 **The gate stack repeating 5g's shape: KMTS is the only name ever to pass the guidance
  gate, gate A, gate B and gate E — and a fifth gate killed it. Independent gates do not net
  out (42a); accumulated passes do not earn a trade.**
- ❌ **HAWK — the best-constructed name on the board, dead three ways.** **Rule 13 is the clean
  one: $2B ÷ 98.0M sh ÷ 1.25 = a hard no-chase ceiling of $16.33; premarket is $16.80, already
  2.9% ABOVE it** — the +25% rung breaches $2B. **Rule 4:** 9/16 closed −1.94% at 31% of range.
  **Rule 1/49a:** the catalyst is a **Memorandum of Understanding** — *no committed dollars at
  all*, worse than ELMT's IDIQ (which at least carried a $150M minimum). 🥇 **And the second
  "catalyst" is a Russell 2000 addition effective 9/21 — a pre-announced mechanical flow event
  that Rocket's OWN IWM CORE will capture for free. Buying HAWK would spend a satellite's risk
  budget on beta already held.** Lock-up expired 9/01 with officer Form 144s (30a).
- ❌ **OSS killed by rule 7a in one line: a ~$400,000 award = 0.18% of a $224M market cap.**
  A press release, not a revenue-changing deal. Compounded: **S-3 filed 8/24 + S-3/A 8/28,
  size unconfirmed** (8e — touting a contract three weeks after filing a shelf), **9/16 closed
  −1.05% at 38% of range on 0.90×** (the tape rejected it the day it was announced), and
  **median range 7.97% = 1.14× the whole trail on a normal day.**
- ❌ **UNCY is the session's clearest AVOID.** No bullish catalyst — the window's news flow is
  **four securities class-action solicitations (9/14–9/16) referencing the 6/30 FDA Complete
  Response Letter.** 🚨 **And rule 8 at its worst tier ever recorded: the ATM was expanded to
  $150M on 6/05 against a $131M market cap — the authorization is LARGER THAN THE COMPANY.**
  Float 99% of shares out. **A +6.5% premarket on that structure is the pump shape, not a catalyst.**
- ❌ **GLAS: no catalyst found AT ALL** (rule 1) — only a routine conference slot and an **SVP
  insider SALE.** Live **$100M ATM (7/15)** = 13% of cap. 🚨 **British Columbia-incorporated —
  escalation 4 hits a THIRD name.** ❌ **XTND: only 8 daily bars (46j, un-measurable), median
  range 14.56% = 2.08× the trail, and the scanner/`eligibility` disagree on market cap by
  11.7× ($101M vs $1,178M)** — rule 38 FAIL on a universe gate. ❌ **RZLT: 9/09 Phase 3
  sunRIZE MISSED its primary endpoint**, and the 9/16 print could not be confirmed (38).
  ❌ **ACP killed on reading the company name — a closed-end fund, not an operating small cap.**
- 🥇 **NEAR-MISS OF THE SESSION — this file was one step from recording a FALSE instrument
  defect.** The scanner's rows looked badly wrong against 9/16 closes: GLAS "+7.2%" vs −0.12%,
  **SOC "+2.8%" vs −7.66%**, HAWK "+3.9%" vs −1.94%, OSS "+5.4%" vs −1.05% — **four apparent
  sign flips, lesson 17b's exact signature.** ✅ **All correct.** Every row reconciles
  **exactly** as a **9/17 premarket quote against the 9/16 settled close — eleven for eleven.**
  📌 **Thirteen sessions of documented scanner defects had primed the conclusion and the
  arithmetic refused it. A prior of "the instrument is broken" is still a prior** → **lesson 55.**
- ✅ **Macro:** VIX **16.04 (−9.43%)** — textbook post-event vol crush, well below the 22 brake.
  Futures risk-on (**ES +0.82% · NQ +1.08% · RTY +0.79%**, all four rows roll-corrected;
  unpatched they would have read +1.71/+2.10/+1.53 and Brent −6.01%). 🚨 **But the 10-yr rose
  to a new run high of 5.01% — TWELFTH session through trigger, the day AFTER the hike landed.
  Equities are trading the removal of uncertainty; the long end is not trading a peak.**
  Brent broke below $100. ✅ **Factor +0.01% — dead flat, nothing to book** (lesson 28).
- 🚨 **W36 (9/04) and W37 (9/11) reviews STILL unrun — EIGHTH session flagging W36 — and W38
  falls due TOMORROW, which makes THREE owed.** Chain fourteen sessions stale (8/28, −2.51%).
  **Four escalations queued behind it**; rebalance-basis divergence widened a second straight
  session to **$136.00** (slice $3,128.32 vs book $2,992.32), THIRTEENTH+ consecutive session.

**Open thread for market_open (9:35)**: **hold IWM, no satellite.** KMTS is closed — do not
let a missed-catalyst recheck quietly re-open a name a below-midpoint close already killed
(42d). **HAWK only re-opens at ≤$16.33 with a committed-dollar contract** — and its index add
is beta Rocket already owns. **Watch for the inverse error today:** rule 29 lifting is not
permission to reach into a weak tier to fill an empty slot (rule 6 — a slot being open is not
a thesis). Re-open the question only on a genuinely fresh, dated, primary-sourced catalyst.

---

## 2026-09-16 — MARKET_CLOSE (Wednesday, Week 38 day 3 — **FOMC DECISION DAY**) — NO TRADE; core dead-on-target (slice basis), book basis diverges 12th+ session, FOMC hiked 25bp as priced

**Step 1/2**: `portfolio_snapshot.py` ran clean. 0/4 satellites — no rows to review;
only holding is the IWM core (no stop, exempt from cut/tighten rules). Premarket's
KMTS gate-A pass and lesson-51 stop-fit correction, plus market_open/midday's rule-29
holds, all carried to close with nothing new.

**FOMC result**: Fed hiked 25bp to **3.75%–4.00%**, 12-0, first hike since 2023 —
matches the ~90% odds priced in premarket. Warsh hawkish, left the door open to
another hike this year. No Rocket position was exposed to the event (100% IWM core,
no satellites). KMTS's gate E (calendar) clears tomorrow, 9/17, the earliest possible
re-entry per its pre-committed gates.

**Step 2.5 (core rebalance)**: raw qty **9.8636 sh** confirmed live. Slice basis
(governing): shared account $10,368.59 × 30% = $3,110.58, target_core $2,799.52, IWM
$2,799.24 = **-$0.28 / -0.01% of slice — HOLD, essentially dead-on target.** Book
basis: rolled to $2,991.25 total, target_core $2,692.13, IWM $2,799.24 is **+3.58%
over — still says SELL ~$107.** 🚩 Divergence now **twelfth-plus consecutive session**
flagged (unchanged cause, lesson 44b). Slice basis governs per CLAUDE.md — no trade.
W36/W37 `weekly_review` both still overdue.

**Step 4 (P&L)**: IWM **-0.47% / -$13.27** vs **SPY -0.46%** — Rocket essentially
matched SPY today (-0.01%), no factor divergence worth booking. All-time on this
entry: -3.84% / -$112.

**Result: 0/4 satellites, 100% IWM core held, no trade.** Weekly count 0/5 — Week 38
closes day 3 with zero new satellites, entirely rule 29 (FOMC) blocking entry all
session; KMTS carries forward as a live gate-A-passed candidate for Thursday.

---

## 2026-09-16 — MIDDAY (Wednesday, Week 38 day 3 — **FOMC DECISION DAY**) — NO ACTION; 0/4 satellites, core +0.49% pre-decision, board stays structurally closed

**Step 1**: `portfolio_snapshot.py` synced clean. Shared account $10,453.17, slice
$3,135.95, cash $427.02 (pooled). Reconciliation unchanged: Rocket = IWM core only,
**0/4 satellites**; JPM/SCHW/SPY are Bull's. No overnight fills, no stops triggered.

**Step 2/3 (position review/news)**: nothing to review. 0/4 satellites (unchanged since
the 8/26 OMER stop-out) — no rows. The only holding is the IWM core, which carries no
stop and is exempt from cut/tighten rules by design; no news check needed on a stopless
core, and today's dominant news (the 2:00 PM ET FOMC decision) is already the known
context, not something a per-symbol search would add to. `position_table.py`: IWM
**+0.49% / +$13.71** today, all-time on this entry still −2.91% / −$84.76.

**Step 4 (afternoon scan)**: `unusual_volume` run. Top rows: VRA 12.4x/+4.9% (no named
catalyst, same noise flagged 9/15), FTFT 6.9x/+35.2% (standing mandate kill — former
China reverse-merger heritage, independent of today's cap reading), PLAY 4.5x/+2.6%
and EAF 2.8x/+14.6% (both already killed this week on named gates, confirming not
reopening), SWMR 4.3x/+7.3% (no catalyst, previously flagged wrong-direction bounce),
INDP 2.8x/-15.1% (already killed on the lesson-46 median-ADV case). No new name carries
a named catalyst, and it would not matter if one did: **rule 29 is absolute today** —
any position opened now is day 1 of a hold that crosses the 2:00 PM ET decision, a
structural gate not a research question. No deep validation spent on the unnamed rows.

**Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat
session so far, no stops hit, no news on the core. W36/W37 `weekly_review` backlog and
the four open escalations (rebalance basis, satellite stop width, ADV-gate-vs-account-
size, KMTS domicile ruling) are unchanged — carried forward, not re-litigated here.

---

## 2026-09-16 — MARKET_OPEN (Wednesday, Week 38 day 3 — **FOMC DECISION DAY**) — NO TRADE, confirms premarket's structural verdict

**Step 1**: `portfolio_snapshot.py` synced clean — no overnight fills, no stops
triggered, positions unchanged (IWM core only, 0/4 satellites; JPM/SCHW/SPY are
Bull's). Shared account $10,455, slice $3,136.61, cash $427.02 (pooled).

**Step 2**: Nothing to validate — premarket produced no queued idea for today.
Its verdict was structural, not conditional on the open: **rule 29 (FOMC 2:00 PM ET
today) admits no configuration**, since day 1 of any hold opened now IS the event.

**Step 4 (fresh-mover scan)**: `unusual_volume` + `top_movers` overlap tier —
**FTFT, EAF, CRBP, EPM, VRA**. All five already dead on named gates: FTFT (mandate
kill, $73M cap below the $50M floor + former China reverse-merger), EAF (8.00%
median range exceeds the whole trail, distributed into its 9/15 close), CRBP
(dead-cat bounce, no confirmable dated catalyst), EPM/VRA (sub-3% moves, no named
catalyst — rule 1 noise; VRA's 19.1x RelVol against a +2.7% move is a volume/price
mismatch, not a signal). RCKT flat, unchanged from its three-gate kill. **Nothing
new — the fresh-mover check found no name that would even reach rule 29,** so the
structural gate was never tested by today's tape.

**Result: 0/4 satellites, 100% IWM core held, NO TRADE.** No notification — flat
session, no stops hit, no breaking news on the core. All four open escalations
(rebalance basis, satellite stop width, ADV-gate-vs-account-size, KMTS domicile
ruling) and the W36/W37 `weekly_review` backlog carried forward unchanged.

---

## 2026-09-16 — PREMARKET (Wednesday, Week 38 day 3 — **FOMC DECISION DAY**) — NO ENTRY (rule 29 absolute); **KMTS gate A PASSED, the first ever**; 🚨 **lesson 48's stop-fit diagnostic FALSIFIED**

**Step 1**: `portfolio_snapshot.py` clean. Shared account **$10,461.44**, slice **$3,138.43**,
cash $427.02 (pooled). Rocket = IWM core only, **0/4 satellites**; JPM/SCHW/SPY are Bull's.
Raw qty **9.8636** pulled from `GET /v2/positions` (never the formatted table, 24d). Book
(lesson 23a, **base named**) = 9.8636 × $285.14 settled + $192.01 cash = **$3,004.52**; core
93.61%, cash 6.39% — **inside the buffer, no bearish thesis owed.**

**Step 2 (scan)**: overlap tier was **one** name — **FTFT**, killed instantly on a **$46M cap**
(below the $50M floor) plus former-Chinese-reverse-merger heritage. Nasdaq calendar screened
**38 reporters** (15 on 9/15, 23 on 9/16) → **zero survivors**; lesson 41d honest tally now
**3-for-5**, calendar and screener are complements not a hierarchy.

**Step 3 (validation)**: `eligibility` **12 requested → 12 returned** (lesson 43 held on full
output). Medians pulled on every survivor (46g). Killed: **DTIL** — the day's one real mover
(+12.4% premarket) — on mean ADV 399k *passing by 33%* while **median63 286,900 FAILS** and
**four of its last five sessions traded under the gate** (46j), **zero searches spent**;
**RCKT** on three independent gates (closed below its own open at 42% of range on 2.5× volume;
an FDA *resumption at a lowered dose* with dosing running to mid-2027 is 37c optionality, not a
delivered catalyst); **AVEX/BETR** on median range ≥1.05× the whole trail; **ANRO/CVRX/TRT** on
catalyst, price floor and an unknown cap.

**🥇 The session's real output — three results that outrank the board:**

1. 🚨 **Lesson 48's central statistic is WRONG, and KMTS's settled bar proved it.** Eight
   sessions asserted from `daily range ÷ 7%` that no catalyst day is holdable. **A trailing stop
   keys on drawdown from the running high, not range.** KMTS ranged 15.40% (2.20× the trail) but
   its **max drawdown from the running high was 6.18%, in the 09:30 bar** — **a 7% trail survives
   untouched and rides it to +15.49%.** Re-measured across all eleven names 48 counted: **SURVIVED
   6 / HIT 5**, not 0-for-11. ✅ **ELMT's kill is vindicated** (15.66% MDD); ❌ the universal claim
   is not. 🥇 **51b: rule 4 buys upper-half-of-range closes while 48 killed wide-range bars — the
   stop gate was vetoing the exact shape the entry gate selects for.** Written up as **lesson 51**;
   48 left unedited with a correction header so the eight-session survival stays visible.
   ⚠️ **KMTS's pre-committed gate B was HELD AS WRITTEN anyway** (rule 42) — the trail is a
   CLAUDE.md guardrail and this is **escalated, not self-approved.**
2. ✅ **KMTS gate A PASSED — the first pre-committed gate A ever to** (IRD ❌, ELMT ❌, GIII ❌).
   Settled O 21.90 / H 25.438 / L 21.56 / **C 25.18, 93.3% of range, +4.65%.** 📌 And yesterday's
   **−9.4% premarket print on two zero-volume bars was correctly NOT scored** (15/17) — the stock
   did open −9% and then closed +4.65%. Gate C **PASSED** (S-3ASR 4/1/26 **undrawn**, multi-year
   runway); D marginal (+1.0%); B/E/F open. **Rule 45 forecast graded a MISS — predicted 18.9%,
   actual 15.40%, now 4-for-7 — and for the first time the VERDICT failed too, not just magnitude.**
3. 🚨 **NEW gate G — KMTS is BERMUDA-incorporated** (EDGAR `stateOfIncorporation` D0), HQ Kirkland
   WA. Three sessions of analysis never ran the domicile gate. **On 9/15 Rocket killed ADNT as a
   "non-US mandate kill" for being an Ireland plc — and Adient is headquartered in Michigan. Same
   shape.** Either KMTS is closed or that whole class of kills is wrong. **Lesson 52; escalation 4.**

📌 **Also reversed a bear case before writing it**: KMTS insiders sold ~240k shares code-S in six
weeks up to four days pre-print — but the officer sales run under **10b5-1 plans adopted 9/29/25
and 11/6/25**, so they encode no view. **Scored as noise** (new lesson 30b).

**Step 5 (macro)**: **FOMC decision 2:00 PM ET today, ~90% hike odds.** VIX 17.00 (drifting *down*
three sessions into the print). **10-yr 5.00% — eleventh session through trigger, new run high on
a round number.** Futures mildly green — ✅ **the roll patch corrected all three equity rows again**
(ES +1.11%→+0.23%, NQ +1.46%→+0.45%, RTY +0.92%→+0.17%). ✅ **Brent-below-WTI inversion resolved.**
Factor **−0.24% against Rocket** Tuesday (IWM −0.70% vs SPY −0.46%) ≈ −0.22% on the book;
lesson 28 bars booking one session.

**Result**: **NO ENTRY — and not on research grounds.** The FOMC decision lands this afternoon, so
day 1 of any hold opened today *is* the event; rule 29 admits no configuration. 0/4 satellites,
100% IWM core, weekly count **0/5**. **Four open escalations** — rebalance basis (divergence
**widened to $133.91**, 12th+ session), **stop-width (premise now materially changed — please
re-read)**, ADV-gate-vs-account-size, and **the new domicile ruling**. W36/W37 `weekly_review`
still unrun — **seventh session flagging**, chain thirteen sessions stale.

---

## 2026-09-15 — MARKET_CLOSE (Tuesday, Week 38 day 2) — NO TRADE; core in band (slice), book basis diverges 11th+ session, FOMC tomorrow

**Step 1/2**: `portfolio_snapshot.py` ran clean. 0/4 satellites — no rows to review;
only holding is the IWM core (no stop, exempt from cut/tighten rules). Premarket's two
kills (ELMT gate A fail, KMTS FOMC+stop-width) and midday's reconfirmation both held
with nothing new by close.

**Step 2.5 (core rebalance)**: raw qty **9.8636 sh** confirmed live. Slice basis
(governing): shared account $10,440.28 × 30% = $3,132.08, target_core $2,818.88, IWM
$2,809.20 = **-0.31% of slice — HOLD, deep in-band.** Book basis: rolled to $3,001.21
total, target_core $2,701.09, IWM $2,809.20 is **+3.60% over — still says SELL ~$108.**
🚩 Divergence now **eleventh-plus consecutive session** flagged (unchanged cause,
lesson 44b — Bull's JPM/SCHW and Rocket's IWM move independently). Slice basis governs
per CLAUDE.md — no trade. Still no user decision on which basis should govern
long-term; W36/W37 `weekly_review` both still overdue.

**Step 4 (P&L)**: IWM **-1.07% / -$30.38** vs **SPY -0.50%** — Rocket underperformed by
~0.57% today, small-cap factor lagged large-cap on the pre-FOMC risk-off tape
(reverses yesterday's +0.11% favorable session, flagged not booked per lesson 28).
All-time on this entry: -3.49% / -$102.

**Step 5**: ntfy summary sent, confirmed via `ntfy_notify.py` return string. Flagged
the 11th+ session divergence, the ELMT/KMTS kills, and the KMTS re-open watch for
Thu 9/17 post-FOMC.

**Result**: 0/4 satellites, 100% IWM core held, NO TRADE. Weekly count **0/5**, Week 38
day 2. W36/W37 `weekly_review` backlog (now 7th session flagging) and the three open
escalations (rebalance basis, satellite stop width, ADV-gate-vs-account-size) carried
forward unchanged.

---

## 2026-09-15 — MIDDAY (Tuesday, Week 38 day 2) — NO ACTION; 0/4 satellites, board stays red into FOMC

**Step 2/3 (position review/news)**: nothing to review. 0/4 satellites open (unchanged
since the 8/26 OMER stop-out); the only holding is the IWM core, which carries no stop
and is exempt from cut/tighten rules by design. No forced cuts, no stop changes, no
news check needed on a stopless core.

**Step 4 (afternoon scan)**: `unusual_volume` run. Broadly red tape the day before FOMC
(consistent with premarket's corrected futures read, lesson 50). ELMT **-9.9%** (already
closed this morning on gate A — confirms the kill, not a re-open candidate). CRBP -19.1%
and PLAY -18.4% — both previously killed, confirming rather than reopening. SWMR new,
-25.0% on 13.6x RelVol — a large red move, not a long setup (no catalyst, wrong
direction for a momentum long). INDP +13.8% — already killed this morning on the
purest lesson-46 case yet (2yr median ADV 18,800, ~96% below the 300k gate). KMTS only
+2.0% (was killed on rule 29 FOMC + rule 45 stop width; nothing changed). **No name on
the board clears rule 29 today regardless of catalyst** — any entry now is day 1 of a
hold crossing tomorrow's FOMC decision, a structural gate, not a research question.

**Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat core,
no stops hit, no news on the core. W36/W37 `weekly_review` backlog (lesson 47c) and the
three open escalations (rebalance basis, satellite stop width, ADV-gate-vs-account-size)
are unchanged — carried forward, not re-litigated here.

---

## 2026-09-15 — PREMARKET (Tuesday, Week 38 day 2) — NO ENTRY; **ELMT gate A FAILED → name CLOSED**; KMTS is a clean rung-1 beat-and-raise killed by FOMC + stop width; **`macro` futures roll flipped three signs**

**Step 1**: `portfolio_snapshot.py` ran clean — the 9/14 `/v2/orders` timeout (lesson 25)
did not recur. Shared account **$10,422.21**, slice $3,126.66, cash $427.02 (pooled).
Reconciliation: Rocket = IWM core only, **0/4 satellites**; JPM/SCHW/SPY are Bull's.
🚨 **Lesson 24a recurred a THIRD time** — table printed IWM "10", raw `GET /v2/positions/IWM`
says **9.8636**. Book (lesson 23a, base named) = 9.8636 × $287.91 settled + $192.01 cash
= **$3,031.84**; core 93.67%, cash 6.33% — **inside the buffer, no bearish thesis owed.**

**Step 2 (scan)**: Weakest board in weeks — `top_movers` topped out at **+6.3%**, and the
**only** overlap-tier name (both lists) was **ADNT**, an Ireland-domiciled plc = standing
mandate kill at +1.5%. 🥇 **The Nasdaq earnings calendar sourced the session's one real
catalyst (KMTS), which appeared on NEITHER scanner list** — lesson 41d now 3-for-4.

**Step 3 (validation)**: `eligibility` 11→11 and 3→3 (lesson 43 count held on full output).
Survivors KMTS · PLAY · EPM · INDP · FTK · SOC · EAF, then medians pulled on every one
(46g). Killed: **INDP** (mean ADV 688k *passes by 129%*, median **156,700 fails by 48%**,
2y median 18,800 — purest lesson-46 case yet; also 11.86% median range, $3.14 trap zone —
**three kills, zero searches**), **EAF** (mean 377,676 passes, median 269,800 fails; median
range **8.00% > the whole trail**), **SOC** (7.52% median range = 1.07× trail; 9/14 closed
at **0.0% of range** on rising volume = distribution), **FTK** (best stop fit on the board —
and the $400M PREPA contract was **terminated** 8/17 after a short report, with a live
securities class action: rule 1 kill), **PLAY** (−11.5% premarket, verified on two sources).

**🔒 ELMT — pre-committed gate A FAILED.** Settled 9/14: O 22.47 / H 25.03 / L 20.22 /
**C 21.50**, midpoint $22.63 → **close at 26.6% of range.** Gate A said below the midpoint
kills regardless of catalyst. **Per 42d/45e a price-action kill CLOSES the name — it does
NOT defer to 9/17.** Gates B–F moot. The gate was struck at $21.27, survived a run to
+37.2% intraday, and still decided the trade **because it was written as a shape, not a
level** (new 42e). 📊 Rule 45 graded honestly: predicted 16.5%, **actual 22.37% — a miss,
too LOW, direction called in advance yesterday.** Tally **4-for-6**; verdict still right
(3.20× the trail) for the sixth time in six (new 45i).

**🥇 KMTS — the finding.** Q1 FY27 (9/14 AMC): revenue **$31.0M +60% YoY** vs $29.59M
consensus, GM **56.5% vs 45.7%** (11th straight quarter of expansion), FY27 guide
**$137M → $141M = +2.92%**, GM target 70% → mid-70%, cash $244.7M. 🥇 **5d's pass-through
ratio is 284% ($4.0M added to the year on a $1.41M beat) — the exact inverse of SWBI, and
the FIRST time rules 5a/5d have ever PASSED a name** (new 5g). ⚠️ Counterweight recorded:
GAAP loss widened to $44.1M from $25.8M. **Killed anyway on rule 29 (FOMC tomorrow, day 2
of the hold) and rule 45 (predicted catalyst range 18.9% = 2.70× the trail).** Premarket
prints $21.47/$21.80 vs a $24.06 close ≈ −9.4%, but on **two zero-volume 04:40 ET bars** —
flagged, not scored. **Pre-committed re-open gates A–F written, earliest Thu 9/17.**

**Step 5 (macro)**: 🚨 **`macro`'s futures rows ROLLED — four at once (ES/NQ/RTY Sep→Dec,
BZ Nov→Dec) and THREE printed the WRONG SIGN** (ES +0.55%→−0.33%, NQ +0.66%→−0.36%,
RTY +0.36%→−0.40%, Brent −3.15%→+1.35%). Caught by the `_resolve_futures_contract` patch;
**unpatched, the table would have read "risk-on into the FOMC" the day before a ~90%-hike
decision.** New **lesson 50**. VIX 17.48 (below the 22 brake), 10-yr **4.96% — tenth
session through trigger**. Factor **+0.11% in Rocket's favour** (IWM −0.34% vs SPY −0.45%),
first favourable session in four — **flagged, not booked** (lesson 28). ✅ And yesterday's
"RTY is the relative winner" counter-signal **did not survive one session** — the restraint
in refusing to book it is vindicated.

**Result: 0/4 satellites, 100% IWM core held, NO TRADE.** 🚨 **Lesson 48 is now 8-for-8**
and the eighth was an ordinary beat-and-raise with the *lowest* catalyst multiple on the
board (3.01×) — the arithmetic needs no dramatic stock. **W36/W37 `weekly_review` still
unrun (SIXTH session flagging) and three escalations remain queued behind it — escalated
directly to the user in this session's response.**

---

## 2026-09-14 — MARKET_CLOSE (Monday, Week 38 day 1) — NO TRADE; core in band (slice), book basis diverges 10th+ session; `portfolio_snapshot.py` broken on `/v2/orders`

**Step 1**: `portfolio_snapshot.py` failed twice — `/v2/orders?status=open` timed out
(10s) both times. Confirmed Alpaca-side via direct `curl`: `/v2/clock`, `/v2/positions`,
`/v2/account` all returned in <0.2s; `/v2/orders` hung the full 15s three separate times.
Worked around with `alpaca_client.py account`/`positions` (neither touches the orders
endpoint) plus a raw `GET /v2/positions/IWM` for the true share count. New lesson 25.

**Step 2**: 0/4 satellites — no rows. **Step 2.5**: slice basis in-band (IWM $2,839.73
vs target $2,826.57, +0.42% of slice) → HOLD, no core trade. Book basis still diverges
(target $2,728.57, IWM $111.16/3.67% over) — 10th+ consecutive session flagged, still
awaiting a user decision on which basis governs (lesson 44b). **Step 4**: IWM -0.33%/
-$9.37 today vs SPY -0.44% — Rocket beat SPY by ~0.11% today on the core alone; no
satellite contribution (none open). **Step 5**: ntfy sent, confirmed
("Notification sent: [default] 🚀 Rocket Daily — 2026-09-14").

**Result: 0/4 satellites, 100% IWM core held, no trade.** W36/W37 `weekly_review`
backlog (lesson 47c) and the open escalations (rebalance basis, satellite stop width
vs 48e's ELMT case, ADV-gate-vs-account-size) are unchanged — carried forward.

---

## 2026-09-14 — MIDDAY (Monday, Week 38 day 1) — NO ACTION; 0/4 satellites, ELMT running further but gates unchanged

**Step 2/3 (position review/news)**: nothing to review. 0/4 satellites open (unchanged
since the 8/26 OMER stop-out); the only holding is the IWM core, which carries no stop
and is exempt from cut/tighten rules by design (CLAUDE.md Core/Satellite section). No
forced cuts, no stop changes, no news check needed on a stopless core.

**Step 4 (afternoon scan)**: `unusual_volume` run. **ELMT now +37.2% intraday** (was
+31.4% premarket) — confirms this morning's forecast-miss-low call (rule 45 forecast
16.5%, expected to miss low; gap alone is now 2.4× that number before any intraday
range is added). Gates unchanged: stop-width/45, undisclosed dilution terms/8/38,
un-runnable ladder/11b, FOMC/29 all still binding; pre-committed re-open gates A–F
(earliest Thu 9/17, post-FOMC) are unaffected by today's continued move since none of
A/B/C/D/F can be evaluated until the FOMC gate (E) clears. CRBP (+2.5%, was +18.4%
premarket — faded, consistent with the dead-cat kill), FEIM (−2.8%) — both previously
killed, no new information. Rest of the board (ACP, BNC, SWMR, PHK, PDO, GRNT, PML,
BCAT, PCN, BRR, MQY, FLWS, ECAT, ACVA, BBNX, STIM, MHD) — no fresh names, no named
catalysts, several are closed-end funds/crypto-proxies excluded on mandate.

**Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat core,
no stops hit, no news on the core. W36/W37 `weekly_review` backlog (lesson 47c) and the
three open escalations (rebalance basis, satellite stop width, ADV-gate-vs-account-size)
are unchanged — carried forward, not re-litigated here.

---

## 2026-09-14 — MARKET_OPEN (Monday, Week 38 day 1) — NO TRADE, confirms premarket verdict

Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged (IWM
core only, 0/4 satellites). Shared account $10,485.63, IWM live $288.49 vs $288.89 settled
(flat), cash $427.02. Premarket's verdict (NO ENTRY — ELMT killed on 4 independent gates:
stop-width/45, undisclosed dilution terms/8/38, un-runnable ladder/11b, FOMC/29; CRBP and
CLB also killed) was structural, not "wait for the open" — none needed re-checking.

**Step 4 scan** (`unusual_volume` + `top_movers`, inline, 2 calls): zero fresh names.
Every row at the top of both lists — ELMT, CRBP, FLWS, DBI, STIM, TLYS — is already
researched and killed in `research_log.md`. DBI +9.1% today on continued earnings-pop
momentum, but Gate F (rule 29 FOMC collision) doesn't clear until after 9/16 regardless
of price action, and no new catalyst is named for today's move — not re-opened.
Lesson 17f's RelVol-column defect (44.0x on ELMT vs a 0.48x real median) is visible again
in this scan's raw output; Change% continues to reconcile correctly against settled prices.

**Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat session,
no stops hit, no breaking news on the core. W36/W37 `weekly_review` backlog (lesson 47c)
and the three open escalations (rebalance basis, satellite stop width, ADV-gate-vs-account-
size) are unchanged from premarket — carried forward, not re-litigated here.

---

## 2026-09-14 — PREMARKET (Monday, Week 38 day 1) — NO ENTRY; best catalyst in weeks (ELMT, $450M Dept of War investment) killed on stop width + FOMC, not on analysis

**Board**: 10 candidates eligibility-tested (10 requested → 10 returned ✅). Five survivors
(ELMT, CRBP, CLB, STIM, FLWS); all five killed on named gates. Full write-up in
`research_log.md`.

🥇 **ELMT — the finding of the session.** The Elmet Group (tungsten/refractory metals,
Lewiston ME) announced a **$450M committed investment from the US Department of War**
(redeemable preferred + warrants up to 19.9%, $200M initial drawdown, DoW board seat) plus a
separate **DLA $2B IDIQ** for National Defense Stockpile deliveries. Gapping **+31.4%** on a
**10.1M float**. Passes rule 1, rule 2c (inside the 20–35% gap-and-go band), rule 13.
**Killed on four independent load-bearing gates**: rule 45/37a stop fit (predicted catalyst
range **16.5% = 2.36× the 7% trail**, and the gap alone is already +31.4%); rule 8/38 — the
warrant strike, preferred coupon and redemption terms are **all undisclosed**, so the
structure cannot be graded and "could not confirm" is a FAIL; rule 11b un-runnable ladder
(~98 bars of history); rule 29 FOMC. ⚠️ Median ADV 299,600 **fails the gate by 0.13%** with
all five recent sessions below it — flagged as **marginal and NOT load-bearing**.
📌 **Pre-committed re-open gates A–F written in `research_log.md` BEFORE the outcome**
(rule 42/42c — shapes, not levels). Earliest entry **Thu 9/17**, after FOMC.
📊 Rule 45 forecast logged for grading: **16.5%**, with an explicit prediction that it will
**miss LOW**. Recorded as-is so the 4-for-5 tally isn't retro-fitted.

**Other kills**: CRBP (+18.4% bounce after −29% in five sessions, four bottom-of-range closes,
no confirmable dated catalyst); **CLB** (no name-specific catalyst, and the Street's entire
range is **$12.00–$12.50 against a $13.45 bid — highest target below the CURRENT PRICE**, a
more extreme version of the OOMA/PD configuration); STIM (median range **8.29% > the whole
trail**); FLWS (median ADV 208,200, mean propped by the −12.89% day's volume — lesson 46b).

🚨 **Lesson 48 is now 7-for-7** — and the seventh was the strongest catalyst on the book.
Escalation #2 (stop width) sharpened, **not self-approved**.

**Macro**: VIX **18.03 (+13.83%)**, below the 22 brake but the biggest jump of the run.
10-yr **4.97%**, ninth session through trigger, new run high. Brent $107 run high.
🆕 **Futures diverge hard: ES −0.78% / NQ −1.72% / RTY +0.42%** — verified against raw
futures independently. First session of the run where small caps are the relative winner;
flagged to watch, **not booked as a turn** (lesson 28). FOMC **Wed 9/16, ~90% hike odds**.

**Book** (base named, lesson 23a): **$3,041.51** = IWM 9.8636 sh × $288.89 = $2,849.50
(93.69%) + cash $192.01 (6.31%). Inside the 10% buffer, no bearish thesis needed.
Slice/book divergence **$108.84, NARROWED from $129.48** — first narrowing, and it moved
with Bull's P&L in the favourable direction, which corroborates 44b's mechanism.

⚠️ **W36 + W37 reviews still unrun (5th session flagging W36). Escalated directly to the
user in this session's response** rather than deferred into the files again (lesson 47c).

**No trades placed — market closed. No Ntfy sent** (no breaking news on an open position).

---

## 2026-09-11 — MARKET_CLOSE (Friday, Week 37 day 4) — NO TRADE; core in band (slice), book basis diverges 9th+ session; W36/W37 reviews still outstanding

**Step 2**: 0/4 satellites, nothing to review — IWM core has no stop by design.

**Step 2.5 core rebalance**: raw qty 9.8636 sh confirmed live. Slice basis (governing):
target_core $2,847.00 vs IWM $2,851.76 = **+0.15% of slice, deep inside band — HOLD.**
Book basis: target_core $2,739.40 vs IWM $2,851.76 = **+3.69%, still outside — SELL
~$112 on that basis.** Ninth-plus consecutive session both bases disagree (lesson 44b).
No trade — slice basis is CLAUDE.md's stated procedure.

**Day P&L**: IWM +0.46% / +$13.12 vs SPY +0.88% (position_table.py) — Rocket
underperformed by ~0.42%, small-cap factor drag on a hot-core CPI day (Fed hike odds
for 9/16 FOMC jumped to ~90%, per today's midday note). Since-rebase Rocket vs SPY
stands at the 8/28 weekly-review chain (−2.51%, grade C) — not recomputed here per
lesson 23a.

⚠️ **W36 review (due 9/04) and W37 review (due today, 9/11) both remain unrun.** This
was a `market_close` session, not a `weekly_review` — did not attempt either review
here to avoid a rushed/incomplete reconciliation. Flagged again for the next session
with budget to run it.

**Notification sent** — see trade_log.md for confirmation text.

---

## 2026-09-11 — MIDDAY (Friday, Week 37 day 4) — NO ACTION; 0/4 satellites, CPI printed hot on core, Fed hike odds jumped to ~90%

**Step 2/3 (position review/news)**: nothing to review. 0/4 satellites open (unchanged since
the 8/26 OMER stop-out); the only holding is the IWM core, which carries no stop and is
exempt from the cut/tighten rules by design (CLAUDE.md Core/Satellite section). No forced
cuts, no stop changes.

**CPI outcome** (premarket flagged this as the session's key event): headline **+0.4% m/m /
3.4% y/y** in line with consensus, but **core +0.3% m/m — 0.1pt hotter than the +0.2%
consensus** (core y/y 2.4%, in line). Stocks rallied on the print (SPY/Nasdaq snapping a
losing streak, yields easing) but **Fed funds futures moved to ~90% odds of a hike at the
9/16 FOMC** — up from an implied lower probability this week. This sharpens, not resolves,
the calendar risk already flagged in `market_context.md`: FOMC sits in the middle of any
1–5 day hold opened today, and now carries higher odds of actually moving. Reinforces
no-new-entry bias into the weekend/FOMC window regardless of what the scanner shows.

**Step 4 (afternoon scan)**: `unusual_volume` and `top_movers` both run. Nothing tradeable:
- **ACVA** (49.0x RelVol, +44.4%) — already dead, Copart's $10.50 cash tender (rule 27),
  not re-openable.
- **REF** (+6.3%, 0.7x RelVol), **CMRC** (+12.7%, 2.0x), **CAL** (+6.9%, 0.9x) — all
  previously killed on named gates (REF: three un-runnable gates 9/11 premarket; CMRC:
  reaffirmation-not-a-raise 9/10; CAL: rule-45/FOMC collision 9/09). No new information to
  reopen any of them.
- New names (CEPL, USDE, LPA, BW, GOLD.com, BRR) — all ≤2.4x RelVol, no named catalyst.
  USDE ("StableCoinX"), GOLD.com, and BRR ("ProCap Financial") read as
  crypto/gold-treasury-proxy names, which rule 31 excludes on mandate before the chart is
  even worth reading.
- Confirms lesson 17d/46i again: the scanner's RelVol column is still not surfacing a real
  signal (max non-ACVA reading 3.7x, on a stock that's down).

**Result: NO ACTION. 100% IWM core held, unchanged.** No notification — no positions with
stops to manage, no negative news on the core. Open escalations (rebalance basis lesson 44,
satellite stop width lesson 48, ADV-gate-vs-account-size lesson 46f, and the overdue W36/W37
`weekly_review`) are unchanged from premarket — not re-litigated here, carried to the next
session with budget to run the review.

---

## 2026-09-11 — PREMARKET (Friday, Week 37 day 4, CPI MORNING) — NO ENTRY; 4 survivors, 4 named kills, and yesterday's SIX kills all closed UP

**Board built from the earnings calendar FIRST (lesson 41)**: 38 reporters 9/10 + 14 for
9/11 = 52 screened → 13 `eligibility`-tested (**13 requested → 13 returned** ✅ lesson 43,
counted against full output) → **4 survivors: ACVA, REF, FEIM, LPTH.** The calendar sourced
three of the four; the scanner sourced one.

**Book (base NAMED, lesson 23a/44)**: **$3,029.57** = IWM **9.8636 sh** (raw qty from
`GET /v2/positions`, lesson 24a — the formatted table still says "10") × $287.70 settled =
$2,837.56 (**93.66%**) + notional cash $192.01 (6.34%). ✅ Inside the 10% buffer, no bearish
thesis owed. Satellites 0/4 · weekly count 0/5 (hand-counted) · max satellite **$454.44**.

**The four kills** (full gate tables in `research_log.md`):
- **ACVA** (+43.9% premarket, the only real scanner signal in 13 sessions) — **Copart
  all-cash tender at $10.50/sh, $1.9B, agreed 9/10.** At $10.39 that is **+1.06% of
  remaining upside**, and **both rungs ($11.95 / $12.99) sit ABOVE the deal price.**
  Rule 27 / the WEAV precedent. 📌 The tell was in the bars: 9/10 traded **19.4M shares =
  6.5× median on a 5.40% range closing at 56%** — huge volume, no move, one day pre-deal.
- **LPTH** — revenue **$21.2M +73% YoY**, beat $18.31M consensus, GM 39.4% from 22%, FY26
  +93%, backlog +197%. **But EPS −$0.06 vs +$0.01 (a MISS) and NO FY2027 guide at all**
  (rule 5b, the CHPT shape). Independently: **median range 7.97% EXCEEDS the whole 7%
  trail** (37a), 45 predicts **28.6% = 4.1×**, and it closed at 8.9% then 16.9% of range
  into the print. Premarket **−0.5%** — the market did not pay for a 73% revenue beat.
- **REF** (Reformation) — EPS **$0.23 vs $0.20 (+15%)**, revenue **$155.2M +24.1%**, FY guide
  $602–606M. Best-looking print on the board. **Killed because THREE gates are
  un-runnable**: IPO'd 7/30 at $15 (now $13.15, −12.3%), so 5a has **no prior company guide
  to diff against**, 11 has **no dated coverage**, and 45 has **30 bars with zero earnings
  days in them**. Per 11b an un-runnable gate is a FAIL. Also **4 of its last 5 sessions
  traded below the 300k gate** (median 316,150 is propped by IPO-window volume — 46b with
  "IPO" substituted for "catalyst") and 9/10 closed at **19.2% of range on 2.0× median**.
  And it is in **neither** scanner list — there is no move to trade.
- **FEIM** — `eligibility` **passed it by 0.06%** (300,167 vs 300,000). Raw: mean 299,725
  ❌, median **241,000 (−19.7%)**, 2y median **163,100 (−45.6%)**, and **all five recent
  sessions below the gate.** Narrowest lesson-46 margin yet recorded; 4th occurrence.

### 🚨 THE FINDING OF THE SESSION — yesterday's six kills ALL closed up, and one fact covers every one

| Name | 9/10 bar | Range |
|---|---|---|
| **CMRC** | **+18.46%**, 62% of range, 6.8× | 13.64% |
| **WLTH** | **+15.01%**, 91% of range, 6.3× | 14.29% |
| **DBI** | **+14.75%, 100% of range**, 2.87× | 12.19% |
| **TSSI** | +7.08%, 55% of range | 10.54% |
| **IRD** | +5.93%, 80% of range | 13.84% |
| **SHOE** | −5.03% on the day but **+20.4% FROM THE OPEN**, 92% of range, 7.8× | 18.49% |

🚨 **Every single one printed a range of 10.54–18.49%. Median 13.74% = 1.96× the mandated
7% trail; all six between 1.5× and 2.6×.** So even on the four names where the directional
call was **wrong**, **Rocket could not have HELD any of them with a 7% trailing stop** —
each stops out intraday regardless of the close. **The board was not empty and quality was
not the problem: six in-universe names moved on dated catalysts and the stop width rejected
all six.** That reframes lesson 36 from a board-quality problem into a **mandate-quality**
one, and it is the volatility-axis twin of 46f's account-size bind.
📌 **Escalated to the user, NOT self-approved** (lesson 28/44 precedent; rule 4b explicitly
says a too-tight trail argues against *entering*, not for a wider stop). Open question for
`weekly_review`: should satellite stop width scale to the instrument's measured median
range — which rule 45 already computes for free — instead of a flat 7%?

### ❌ And rule 45's magnitude forecast missed for the first time: 4-for-5

**DBI predicted 21.7%, actual 12.19% — over by 78%.** Recorded as a miss, not smoothed.
The error was biased toward **not** entering — the opposite of the bias rule 45 was written
to fix. ⚠️ **But the gate's CONCLUSION held: 12.19% is still 1.74× the trail.** Forecast
magnitude and forecast verdict are graded separately; one bad magnitude does not retire a
gate that was still right about stop fit. Tally: GIII ✅ DAKT ✅ CAL ✅ IRD ✅ **DBI ❌**.

**Macro** (one `macro` call, one search — no subagent): **10-yr 4.94%, +10bps, EIGHTH
session through 4.75% and the run's biggest jump** — the one clean signal. **VIX 17.09,
−4.2% INTO CPI day**, below the 22 brake, no size restriction, and notably complacent.
Russell fut +0.62% but at a **lower level** than yesterday (2,925.50 → 2,911.20) — laggard
for a third session. CPI consensus **+0.4% m/m / 3.4% y/y headline, +0.2% / 2.4% core**.
⚠️ **Brent and Gold print level-vs-change figures inconsistent with yesterday's recorded
levels — flagged as a broken instrument, not folded into the thesis** (lessons 15/38/39a).
Equity and rates rows cross-check clean.

**Rule 29 is the gate that covers the whole board today**: CPI 8:30 ET, and **FOMC 9/16 now
sits in the MIDDLE of a 1–5 day hold opened today** (9/11 · 9/14 · 9/15 · **9/16** · 9/17),
not at the far end. Stricter than yesterday, not looser.

🚨 **Three open escalations, none self-approved**: (1) rebalance basis — **NINTH straight
session of disagreement**, slice $3,159.05 vs book $3,029.57, divergence **WIDENED to
$129.48** from $105.15 as Bull's JPM hit +13.7% while IWM fell −1.01%; slice says HOLD
(−0.18%), book says SELL ~$111 (+3.66%). (2) satellite stop width, new today. (3) ADV gate
binding on account size (46f). 🚨 **W36 `weekly_review` still missing — FOURTH session
flagging it — and W37's is due today. Two reviews owed, and all three escalations need
one.** No satellite entered since **ETON on 8/17, 18 sessions ago.**

**Result: NO ENTRY. 100% IWM core held.** No notification — market closed, no breaking news
on the core, no positions with stops to manage.

---

## 2026-09-10 — MARKET_CLOSE (Thursday, Week 37 day 3) — NO TRADE, core in band on slice basis, book basis still diverges (8th session), no satellites

**Step 2**: 0/4 satellites, nothing to review — IWM core has no stop by design.

**Step 2.5 core rebalance**: raw qty 9.8636 sh (lesson 24). Slice basis (governing):
target_core $2,826.48 vs IWM $2,836.82 = **+0.33% of slice, inside band — HOLD.** Book
basis: target_core ≈$2,723.95 vs IWM $2,836.82 = **+3.73%, still outside — SELL ~$113
on that basis.** Eighth consecutive session both bases disagree (lesson 44b: Bull's
book and Rocket's IWM keep moving opposite directions same-day). No trade — slice
basis is CLAUDE.md's stated procedure. Still no user decision on which basis
governs; W37 `weekly_review` (due tomorrow, 9/11) is the next natural resolution
point, and W36's review still never ran.

**Day P&L**: IWM −1.01% / −$28.90 vs SPY −0.61% (position_table.py) — Rocket
underperformed by ~0.40%, small-cap factor drag on the PPI-day pullback. All-time on
this entry: −2.51% / −$73.12. Since-rebase Rocket vs SPY stands at the 8/28
weekly-review chain (−2.51%, grade C) — not recomputed here per lesson 23a (avoids
portfolio_snapshot.py's Bull-contaminated since-rebase figure).

**Notification sent** — confirmed via ntfy_notify.py ("Notification sent: [default]
🚀 Rocket Daily — 2026-09-10"). Flagged rebalance-basis divergence and W37 review due
tomorrow.

---

## 2026-09-10 — MIDDAY (Thursday, Week 37 day 3) — NO TRADE, no cuts, no new setups

**Position review**: 0/4 satellites open, nothing to review. Only Rocket position is
IWM core (10 sh, entry $295.12, live $288.29, **−2.3%** intraday on the PPI-day
pullback) — no stop by design, exempt from Step 2's cut/tighten checks. Broker also
shows Bull's JPM/SCHW/SPY (+12.5%/+2.7%/−1.3%), not Rocket's.

**No per-name news check** — zero satellite positions to check.

**Step 4 scan** (`unusual_volume`): same names as this morning's market_open list
(RWT, SHOE, BBOT, CMRC, TSSI, XFOR, IRD, WLTH, DBI, ...) — no fresh mover since the
open. IRD (yesterday's day-2 candidate, already killed this morning on the gate-A
price-action failure) is now flat-ish at +1.9%; DBI's pre-committed gates still point
to a Friday/CPI-morning day-2 decision, not today. Nothing new to research.

**Result: 0/4 satellites, 100% IWM core held, no trade, no forced cuts.** No
notification — no breaking news, no stop actions, core has no stop to manage.

---

## 2026-09-10 — MARKET_OPEN (Thursday, Week 37 day 3) — NO TRADE, confirms premarket, two fresh movers killed on catalyst

Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged
(IWM core only, 0/4 satellites). Shared account down to $10,474 (PPI-day pullback —
IWM $288.39 live vs $290.64 settled, SPY $758.18 vs $762.40). Premarket's three kills
(WLTH, SHOE, DBI) were all structural (miss, guidance cut, binding rules 45/29 gates)
— none needed re-checking at the open. DBI is +8.1% today on its earnings pop but
gates E/F (21.7% predicted catalyst range = 3.1× the trail; only valid day-2 entry
lands on CPI/FOMC) are pre-committed and price-action-independent — correctly held off.

- 🔎 **Step 4 scan surfaced two fresh names not on the premarket board**: **CMRC**
  (Commerce.com, +22.3%, 13.7x RelVol) and **TSSI** (TSS Inc, +10.1%, 12.8x RelVol).
  Checked both inline (2 searches, under the 5-search subagent threshold).
  - **CMRC**: today's move is a cost-cutting/margin restructuring plan (targeting 20%
    non-GAAP op margins by 2027, $60–80M annualized cost reduction, new $50M buyback)
    with FY26 **revenue guidance REAFFIRMED** at $336.5–344.5M and op-income guide
    raised only **$3M** — the same reaffirmation-is-not-a-raise shape as lesson 5f
    (AVO, NX). Also a data conflict worth flagging: scanner read $3.18, a live search
    read $2.56 — right at/below the $3 price floor either way. Killed on rule 5f.
  - **TSSI**: no dated news found explaining today's 12.8x volume spike. Last reported
    quarter (Q2) was a revenue **decline** (−20% YoY), EBITDA guidance merely reaffirmed
    toward the upper end — not today's catalyst. Killed on rule 1 (no catalyst = no trade).
- Rest of `unusual_volume` overlap: RWT (−21.1%, no long thesis), BNC (standing rule-31
  mandate kill), IRD (already closed on price-action gate 42c), SWMR/XTND/BHVN/BBOT/
  XFOR/ALMS/OBIO/NAC/DFDV — no dated catalyst screened, not researched individually.

**Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat
session, no stops hit, no breaking news on the core position.

---

## 2026-09-10 — PREMARKET (Thursday, Week 37 day 3) — no entry, 3 survivors from 80 reporters, all dead on named gates

**Board built from the earnings calendar FIRST (lesson 41)**: 41 reporters 9/09 + 39 for
9/10 = 80 screened. 15 in-universe by cap → `eligibility` (15 requested → **15 returned**,
lesson 43 count held) → **3 survivors: WLTH, SHOE, DBI.**

- **WLTH** (Wealthfront, AMC 9/09) — **MISSED.** Non-GAAP EPS $0.10 vs $0.104 (−3.6%), net
  income −49%. Rule 5 never gets past its first question. Best liquidity on the board
  (median ADV 1,158,400) wasted on a miss. Also closed −1.77% **at 15% of range** into the print.
- **SHOE** (Shoe Station, released **6:10 AM ET today**) — **GUIDANCE CUT.** Revenue −7.1%,
  EPS $0.23 vs $0.70, FY adj EPS cut to $0.75–0.90 vs $1.90 actual (≈−55%), GM −390/410bps.
  The inverse of the entry condition. Premarket −13.1%. Two prior sessions closed at 14%
  and 26% of range on 3× volume — **the tape front-ran the cut.**
- **DBI** (Designer Brands, BMO today, call 8:30 ET) — the only live name. **Six gates
  pre-committed BEFORE the print (rule 42).** E and F are binding and neither is a research
  question: rule 45 predicts a **21.7% catalyst-day range = 3.1× the 7% trail** (ten widest
  days 17.8–24.3%, every one blows it), which converts to day-2 = **Friday 9/11 — CPI
  morning**, with the hold running through **FOMC 9/16**. Live bear case: SHOE, a direct
  peer, cut on "an increasingly promotional footwear marketplace" two hours earlier.

**IRD day-2: GATE A FAILED, killed on the pre-commitment.** 9/09 settled O 5.31 / H 7.07 /
L 5.31 / **C 5.73 (+32.03% on 53.9M)** — midpoint $6.19, **closed at 24% of range, below
it.** Gate C also failed (predicted range 34.5%, actual 30.72%). Per **45e** a price-action
kill does not convert to a date — **closed, not deferred.** The gate structure worked
end-to-end: morning table at $6.56, midday flagged the fade without assuming it, settled bar
resolved it.

**Grading 9/09's kills (32c): 3 of 4 confirmed.** CAL +1.00% **at 2% of range** on 2.66×
volume, range **15.06% vs rule 45's predicted 16.1%** — 🥇 **rule 45 now 3-for-3 as a range
predictor.** OCC flat, 17.66% range. INNV +4.85% but at 9% of range. ⚠️ **AVO +4.27%** —
the rule-5 kill cost a real up-move; recorded, not rationalised (closed at 34% of range).

**🚨 Found an error in 9/09's `market_close`: it struck the rebalance on "raw qty 10 sh."
The API returns 9.8636.** Corrected, IWM was **2.01% over target — INSIDE the band**, not
3.28% outside. **The deferred SELL is withdrawn — do not carry it into `market_open`.**
Lesson 24 firing on the exact field it was written about. Today: slice basis **+0.61% —
hold**; book basis +3.72% — sell ~$114. **Divergence widened to $105.15 (seventh straight
session)** because Bull's JPM +13.5% and Rocket's IWM −1.37% moved in opposite directions
on the same day — lesson 44b at full strength. Still awaiting a user decision.

**Macro**: 🚨 **PPI today 8:30 ET, CPI tomorrow 8:30 ET (last print before FOMC 9/16).**
Brent **$102.11** at a new run high (+10.6% across the run), 10-yr **4.84%** seventh session
through the trigger, VIX 16.47 (no size restriction). **IWM −1.37% vs SPY −0.46% = −0.91%
factor against Rocket** — lesson 28 bars booking one session, honored in the unfavourable
direction as it was on 9/08 in the favourable one.

**Instrument health**: lesson 17a **twelfth** straight — QUIK "+5.8%" was really −2.01%,
NMAD "+7.8%" was really −3.89%, **both also below the 300k volume gate.** Scanner overlap
tier: **zero usable names** (BNC crypto-treasury mandate, LPA Costa Rica domicile).

**Weekly count 0/5. Board stays IWM-only. No trades placed — market closed.**
🚨 **W36 `weekly_review` still missing (third session flagging); W37's is due tomorrow.**

---

## 2026-09-09 — MARKET_CLOSE (Wednesday, Week 37 day 2) — END OF DAY, escalated rebalance, no trades, clean close

**Position review**: 0/4 satellites open, IWM core only. No fills overnight, no stops triggered.
Intraday peak IWM $291.70 (slightly above settled $294.67) — rounding noise, market closed
now at 16:01 ET. Core rebalance check flagged: IWM now **3.28% over target on slice basis**
(first time crossing the 3% band); book basis also signals SELL but with larger magnitude
divergence (~$146 vs $104). **Both bases now agree direction (SELL), divergence on scale.**
Per lesson 44c, this four-session recurrence needs explicit user decision. Trade deferred
(market closed). Documented in ntfy notification and flagged as escalation.

**Day P&L**: -$40.24 on IWM (-1.39%) vs SPY -0.46% → underperformed by ~0.93% (factor).

**Notification sent**: ntfy confirmed delivery. No further actions for today.

---

## 2026-09-09 — MIDDAY (Wednesday, Week 37 day 2) — NO TRADE, no cuts, no new setups

**Position review**: 0/4 satellites open, nothing to review. Only Rocket position is
IWM core (10 sh live, no stop by design — exempt from Step 2's cut/tighten checks).
Rocket-only book shows IWM at −1.5% intraday ($290.79 vs settled $294.67), in line with
a broad small-cap pullback; not a position decision (core, no stop, rebalance is
market_close-only per Portfolio Construction rule 6).

**No per-name news check** — zero satellite positions to check.

**Step 4 scan** (`unusual_volume`): all four premarket earnings-calendar survivors
(AVO $13.52, INNV $11.65/+10.7%/3.4x, OCC $12.60/−8.0%/5.5x, CAL $12.68) unchanged from
this morning's kills — no new information, no re-open. 🆕 **IRD** (the pre-committed
9/10 day-2 candidate) has pulled back hard intraday: scanner reads $5.57/+28.4%/77.8x
vs the $6.56 print cited in this morning's market_open gates — roughly **−15% off that
level already**, well before the close. Flagging for whoever runs Gate A (rule 2b,
upper-half-of-range close) at `market_close` — a fade this size raises real doubt the
close lands in the upper half. Not a call made here; Gate A is explicitly a
market_close/next-premarket read. Rest of the unusual-volume list (TH, TYRA, EVMN,
BNC, PYXS, XTND, BNED, EAF, SWMR, INBX, BBOT, ACRS, CRBP, TCPC, SHOE, PSQL) carries no
named dated catalyst (rule 41: source from the earnings calendar, not the screener) —
no research spent.

**Result: 0/4 satellites, 100% IWM core held, no trade, no forced cuts.** No
notification — no breaking news on the only open position, no stop actions.

---

## 2026-09-09 — MARKET_OPEN (Wednesday, Week 37 day 2) — NO TRADE, confirms premarket + one fresh catalyst deferred to day 2

Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged
(IWM core only, 0/4 satellites). Premarket's four kills (AVO, INNV, OCC, CAL) were all
structural (guidance sizing, cap lid, liquidity median, spread/range) — none needed
re-checking at the open.

- 🆕 **Step 4 scan surfaced IRD (Opus Genetics)** — this is the exact binary flagged
  9/02 midday as "anticipatory... kill, not a today catalyst" (September 9 BEST1 data
  webcast). Today it resolved: **positive** Phase 1/2 Cohort 1 data (BIRD-1 trial),
  advancing to a higher-dose Cohort 2. Real, dated, positive trial-readout catalyst —
  passes eligibility cleanly (avg volume 1.13M, 276% over the 300k gate; cap $546M;
  +25% ladder ~$682M, nowhere near the $2B lid).
- 🚫 **Killed for TODAY on extension, not on catalyst quality**: +49.6% today alone, on
  top of +45.9% over the prior 5 days and +77.4% over the month, −0.9% off the 52-wk
  high. Gap-size framework: >35% same-day = second-day only (rule 2c). **Pre-committed
  five gates (A–E, rule 42) in `research_log.md` for a possible 2026-09-10 entry** —
  close-in-range, median ADV re-verify, own-history rule-45 range multiple, and
  explicitly the rule-29 FOMC (9/16) calendar collision that killed CAL's day-2 this
  same session. Not asserted as a pass; gates written before the evidence.
- Rest of `unusual_volume`/`top_movers` overlap: TH, BNED, EVMN, XTND — all negative
  moves, no catalyst search warranted. TYRA, PYXS, GOLD, EAF, HYPD, BNC, NEOV already
  standing kills (tape/mandate). CAL, OCC, INNV, AVO unchanged from premarket.
- **Result: 0/4 satellites, 100% IWM core held, no trade.** No notification — flat
  session, no stops hit, no breaking news on the only open position.

---

## 2026-09-09 — PREMARKET (Wednesday, Week 37 day 2) — NO ENTRY, but the board was FULL and every name died on a named gate

Book **$3,098.52** = IWM 9.8636 sh @ $294.67 settled (93.80%) + notional cash $192.01
(6.20%, inside the buffer). Satellites 0/4, weekly count 0/5. Max satellite $464.78.

- 🥇 **The earnings calendar (lesson 41) paid off on its second use.** Nasdaq API returned
  24 reporters for 9/08 AMC + 45 for 9/09 BMO → **four in-universe names with real dated
  catalysts** (CAL, OCC, INNV, AVO), on a day the scanner's overlap tier was one usable row.
  `eligibility` on 11 candidates: **11 requested → 11 returned** ✅ (lesson 43).
  ⚠️ **This is the opposite of 9/08's empty board and must be written differently** —
  "nothing qualified" after screening four dated catalysts is a real result, not 41b.
- ❌ **AVO** (+5.8% pre): beat its own Q3 EBITDA guide by **+1.25%** then **REAFFIRMED** the
  H2 $84–88M range = **0% raise** (new rule 5f case). Rule 5e composition check inverts it:
  revenue +38% on volume, but **gross profit FELL**, margin **−270bps**, adj net income
  **−18%**, GAAP net loss $6.5M. The "synergy target raised to >$30M" never reached the guide.
- ❌ **INNV** (+14.2% pre, the biggest gap on the board) dies **four** ways: guidance
  explicitly **in-line** and FY27 revenue guided **+7.9% against an FY26 that did +15.9%**
  (5a/5c); 🚨 **rule 13 — at $12.01 the +25% rung is $2.04B, THROUGH the $2B lid**; median
  ADV **288,500 fails by 3.8%** while the mean passes (lesson 46); predicted catalyst-day
  range **25.2% = 3.6× the 7% trail**, with all ten of its widest days 15.4–34.7%.
- 🚨 ❌ **OCC** — topped BOTH scanners (+12.5%, 4.3×) **and** reported today, the most
  tempting row of the session, **dead three ways**: live book **bid $11.47 / ask $20.01 =
  a 55% spread** (worse than BBCP's 44%); median ADV **236,900 fails by 21%** while the mean
  **passes by 26.8%**; **median daily range 9.13% — larger than the entire 7% trail.**
- ⏳ **CAL** is the only clean instrument on the board (median ADV 490,700, all three volume
  measures agree; median range 4.82%) and its print lands BMO today. **Gates A–E
  pre-committed in `research_log.md` BEFORE the print (rule 42).** D and E are binding and
  are not research questions: rule 45 predicts a **16.1% catalyst-day range = 2.3× the
  trail** → no same-day entry; 45c's day-2 date (Thu 9/10) then runs into **FOMC 9/16**
  (rule 29). Also closed 9/08 **−3.22% at 3% of range on 1.56× volume** — distribution
  shape into the print. **Recorded as a near-certain no-trade, not an open thread.**
- ✅ **Yesterday's kills graded 8-of-10 correct in ONE session** — including both
  "uncomfortable carries": **NX −3.10%** (rule 5f's first validation) and **CHPT −5.26% at
  6% of range** (rule 5a). EAF closed **+1.61% at 2% of a 21.4% range**. INSG traded
  **254,100 shares — under the gate**, confirming its median-ADV kill. ⚠️ **HYPD ran +8.48%
  at 82% of range — the rule-31 mandate kill cost a real up-move, recorded not rationalised.**
- 🆕 **Lesson 46g written**: the ±10% ADV re-verify band is a **floor, not a ceiling** (OCC's
  mean passed by 26.8% and still hid a 21% median failure), and a wide premarket book is
  **corroboration, not a kill** — **AVO read the same 55% spread on a median ADV that passes
  by 189%.** A check that always fires carries no information.
- 🚩 **Basis divergence, SIXTH session**: book $3,098.52 vs slice $3,167.65 = **slice $69.13
  richer**, narrowed a second straight session ($106.66 → $88.16 → $69.13) for the same
  mechanism that opens it (lesson 44b), not because anything was fixed. Escalated again.
- 🚨 **W36 `weekly_review` STILL missing — second session flagging it.** Rocket-vs-SPY chain
  over a week stale (8/28 W35, −2.51%). Lesson 47 / [[launchd-quota-contention]].

**Result: 0/4 satellites, 100% IWM core, no trade. Macro: Brent broke $100 (new run high),
10-yr 4.81% for a sixth session through 4.75%, VIX 16.09 (no brake), Russell fut −0.43%
weakest leg again.** No notification — no breaking news on the only open position.

---

## 2026-09-08 — MARKET_CLOSE (Tuesday, Week 37 day 1) — NO TRADE, core in band on slice basis, book basis diverges again

**Position review**: 0/4 satellites, nothing to close. IWM core held all session
(script-verified: −0.46% / −$13.32 today vs SPY −0.56% — Rocket beat SPY by ~0.10%,
pure factor, no stock selection to attribute).

**Core rebalance (slice basis, documented procedure)**: slice $3,177.71, target_core
$2,859.94, live IWM $2,907.00 — 1.48% over, within the 3% band. No trade. **Book basis
(lesson 23a) disagrees again**: book $3,098.35, target_core $2,788.51, IWM is 3.82%
over — outside band, would say SELL ~$118. Same ~$117-118 gap as 9/02–9/03, still
unresolved, escalated again rather than self-resolved. Full numbers in
`trade_log.md`.

⚠️ **New finding: W36 `weekly_review` (due Fri 9/04) never ran** — no file in
`memory/weekly_reviews/` and no 9/04 market_close entry in `trade_log.md`. The
since-rebase Rocket-vs-SPY figure is now over a week stale (still the 8/28 W35 chain,
−2.51%). Likely another [[launchd-quota-contention]] casualty — flagged in
`lessons_learned.md` for whichever session can run the missed reconciliation.

Notification sent and confirmed (`Notification sent: [default] 🚀 Rocket Daily —
2026-09-08`).

---

## 2026-09-08 — MIDDAY (Tuesday, Week 37 day 1) — NO TRADE, no cuts, one new name killed on mandate

**Position review**: only Rocket position is IWM core (0/4 satellites, unchanged since
8/26), essentially flat (+0.1%, $295.48 vs $295.12 entry). No stop applicable (core
exempt by design), nothing to cut or tighten. No per-name news check applicable with
zero satellites.

**Afternoon scan** (`unusual_volume`/`top_movers`): overlap tier is BNC (still
mandate-excluded, +50.6%/349.6x), TLYS/CHPT (standing kills, unchanged), and EAF/NVA —
both already killed at the open, both moves grew (EAF now +21.9%/4.0x, NVA +9.8%/4.3x)
but neither kill reason changed; NVA also surfaced a fresh $20M dilutive raise at a 14%
discount. One genuinely new name: **HYPD** (Hyperion DeFi, +6.2–7.7%, 5.0x) — a real,
dated guidance raise (FY26 adj. gross profit $5–7M → $7–8M + $20M buyback) that would
otherwise clear rule 5/5a, but it's a HYPE-token crypto treasury company (formerly
Eyenovia) — killed on rule 31 mandate exclusion regardless of catalyst quality. Full
detail in `research_log.md`.

**Result: 0/4 satellites, 100% IWM core held, no trade, no forced cuts.** No
notification — no breaking news on the only open position.

---

## 2026-09-08 — PREMARKET (Tuesday, Week 37 day 1) — NO ENTRY; earnings calendar empty, worst scanner session on record

Book **$3,111.67** = IWM 9.8636 sh @ $296.01 settled (93.83%) + notional cash $192.01
(6.17%, inside the buffer). Satellites 0/4, weekly count 0/5 (new week).

- 🥇 **Earnings calendar ran first (lesson 41) and is genuinely empty in-universe.**
  Friday 9/04 (4 reporters), the Labor Day weekend, and Tuesday 9/08 BMO (11 reporters)
  all screened to **zero** in-universe names — 8 requested/8 returned on `eligibility`
  (lesson 43 check held). Kills: HURC/VIRC/NTRB (ADV), AXR (ADV), AREC/ELME/UPXI/ZENA
  (sub-$3), VZLA/WDH/CAN/DLNG (domicile), ABM/UNFI (cap). INNV/AVO report AMC today —
  re-screen Wednesday.
- 🚨 **WORST SCANNER SESSION ON RECORD — three sign flips, one 35-point error.** Raw
  bars vs Friday's real settled prints: BNC scanner said +41.0%/1393.8× RelVol, real
  bar was +6.08%/1.86×; ENOV, TROX, WTI all showed sign flips (scanner said up, real
  bar was down). Overlap tier was BNC alone — mandate-excluded (crypto-treasury, rule
  31) and fictional in both lists.
- ❌ **Eight in-universe scanner movers killed in one `eligibility` call, zero research
  spent** — all have next earnings 55–58 days out (rule 1, no dated catalyst): HLF, SG,
  INSG, TROX, AMRC, WTI, ENOV, UPB.
- ❌ **INSG** (prettiest bar on the board, +5.21% at 91% of range, 1.40×) killed four
  ways: no dated catalyst (+58d), a live S-3 on a $69M cap, ADV median 265,700 fails
  the 300k gate by 11% (mean passes — lesson 46 shape), and predicted catalyst-day
  range 14.4% = 2.1× the 7% trail.
- ✅ **Friday's four kills graded correct against the settled bars** (SWBI, TLYS, NX,
  CHPT) — see `research_log.md` for the by-name detail.
- 🔎 **Re-ran the scanners later in premarket** — new overlap name **EAF** (GrafTech)
  passed every universe gate but killed on rule 1: the only explanation found was an
  undated, speculative "surges on speculation of Defense Department partnership"
  headline, next earnings +52 days, modest 1.9× volume. BNC still topped both lists,
  now an even more extreme fiction (+61.6%, 1806.3× RelVol) — still mandate-excluded.
- 🚩 **Rebalance-basis divergence (lesson 44/44c) carried, narrowed to $88.16** (book
  $3,111.67 vs slice $3,199.83) — Friday's IWM +0.28% vs SPY −0.39% ran the gap the
  other direction. Fifth consecutive session unresolved; still awaiting a user decision
  on which basis governs. No action — rebalancing is `market_close` only.
- **Macro**: VIX 15.33–15.70 (up from Friday's 14.21 two-week low, no brake). 🚨 **10-yr
  4.77–4.78%, fifth session through the 4.75% trigger**, now with a hot jobs print (NFP
  +162K vs +53K consensus, 3× beat) behind it — a September hike is more live, not
  less. Russell fut the weakest leg (−0.16% to −0.37%), small caps leaning risk-off.
  Brent/WTI at a new run high (+6.7% over the stretch). Designed response for the
  stopless core remains no action. FOMC decision Wednesday 9/16 — 6 trading days out,
  a live rule-29 gate for anything opened Thursday or later.
- **Result: 0/4 satellites, 100% IWM core held.** Board empty by measurement (a source
  that cannot silently go blank returned a slate and it screened clean to zero), not by
  opinion. No notification — no breaking news on the only open position.

---

## 2026-09-07 — MARKET_CLOSE (Monday, Labor Day) — SESSION SKIPPED, market closed

Third and final skip of the day, same reason as market_open/midday below:
`portfolio_snapshot.py` still reports "Market open: No", prices unchanged from
Friday's settled close (IWM $296.01). **Step 2** (position review): no rows — 0/4
satellites, IWM core carries no stop by design. **Step 2.5** (core rebalance):
explicitly skipped per CLAUDE.md's own exception for a closed market; the standing
lesson-44c slice-vs-book divergence (flagged 9/01→9/03, unresolved, needs a user
decision) carries over unchanged — no new rebalance data was generated today to add
to it. **Step 3**: no fills, market never opened. **Step 4**: `market_data.py
spy-today` printed −0.39%, but that's a thin holiday print, not a settled session
move — not recorded as today's return. **Step 5**: no notification sent — nothing
changed to report, and a stale price print dressed as a daily summary would misstate
a non-trading day. Logged a NO TRADE entry in `trade_log.md` for the record. Next
real session: Tuesday 2026-09-08 premarket.

## 2026-09-07 — MIDDAY (Monday, Labor Day) — SESSION SKIPPED, market closed

Same holiday as this morning's `market_open` entry below — `portfolio_snapshot.py`
still reads "Market open: No" and prices are unchanged (IWM $296.01, last settled
close, no new trade). Nothing to review: 0/4 satellites open, and the IWM core
carries no trailing stop by design, so Step 2 has no rows regardless of market
state. Skipped Step 3 (news check) and Step 4 (afternoon scan) — no live price/
volume data exists on a closed market to act on. No memory changes beyond this
note. Next real session is Tuesday 2026-09-08's premarket.

## 2026-09-07 — MARKET_OPEN (Monday, Labor Day) — SESSION SKIPPED, market closed

Session was triggered on a market holiday. `research_log.md` had already flagged
9/07 as Labor Day with the market closed (confirmed against the Alpaca calendar,
next session Tuesday 9/08); re-verified live via `GET /v2/clock` before touching
anything: `is_open: false`, `next_open: 2026-09-08T09:30:00-04:00`. No portfolio
sync re-run beyond the routine snapshot, no watchlist validation, no orders placed
— there is no live price/volume data on a closed market to validate SWBI/BBCP or
any fresh scanner names against. This is likely a launchd trigger firing on a
holiday it doesn't know about; see [[launchd-quota-contention]]. No action needed
beyond noting it — next real market_open is Tuesday 2026-09-08.

## 2026-09-04 — MIDDAY (Friday, Week 36 day 5) — NO TRADE, no satellites to manage

Nothing to cut/tighten/hold — 0/4 satellites open (unchanged since the 8/26 OMER stop-
out), and the only position owned (IWM core) carries no trailing stop by design, so
Step 2's per-position review had no rows. Ran `unusual_volume` for afternoon setups
(Step 4) and found one real catalyst worth deep-checking: **NX (Quanex)**, +20.6% on
real 1.5x volume (not the scanner's inflated 3.4x) after a 9/03 AMC beat, 52-wk high,
passes every universe gate. **Killed on a new rule 5a sub-case (5f):** today's "FY26
outlook" is the **identical $1.84–1.87B/$240–245M range given in March**, withdrawn in
Q2 and simply reinstated — a 0% change dressed as a headline raise. Q3 revenue grew
only +1.3% YoY, and most of the YoY operating-income jump comps against last year's
$302M goodwill impairment. Also outside the sanctioned 9:45–9:50 entry window regardless.
Two more names checked and killed on sight: **TYRA** (rule 29 — Sept 9 binary readout,
today's move is pre-positioning, not the catalyst) and **PYXS** (rule 1 — no dated
catalyst behind the move). Board stayed IWM-only. Full detail in `research_log.md`.

---

## 2026-09-04 — MARKET_OPEN (Friday, Week 36 day 5) — NO TRADE, confirms premarket

Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged
(IWM core only, 0/4 satellites). IWM $294.94 vs $295.19 prior settled close — flat,
nothing to react to. Premarket's two kills (SWBI on rule 5a/5d guidance-sizing, BBCP
on rule 46 liquidity) were structural, not "wait for the open" calls — neither needed
re-checking.

- 🔎 **Ran `unusual_volume`/`top_movers` for fresh names not on the premarket board
  (Step 4).** SWBI, BBCP, CHPT, TLYS, OXM all already screened/killed. Two names stood
  out as genuinely new: **RARE** (Ultragenyx, +6.1%, 7.4x scanner RelVol, $1.55B cap —
  inside universe) and **GOLD** (Gold.com Inc, +3.9%, 3.3x RelVol, $1.25B cap). Checked
  both inline (2 detail pulls, under the 5-search subagent threshold).
  - **RARE**: `detail` shows actual volume **0.2x avg** (1.82M vs 5.02M avg) — directly
    contradicts the scanner's 7.4x RelVol claim, another lesson-17a-shaped discrepancy,
    now in the `unusual_volume` RelVol field itself, not just `top_movers` price/change.
    Also **−37.7% over 5 days, −39.2% over 1 month, below both MA20/MA50** — a
    downtrend, not a breakout. No catalyst found. Kill on rule 1 (no catalyst) and on
    the tape (falling knife, not momentum).
  - **GOLD**: same pattern — actual volume **0.2x avg** (128k vs 673k) against a claimed
    3.3x RelVol. No catalyst found. Kill on rule 1.
- **Result: 0/4 satellites, 100% IWM core held.** No rebalance (market_close only,
  rule 6). No notification — flat session, no stops hit. Also the session ahead of the
  Labor Day long weekend (rule 29, escalated in premarket) — an independent reason not
  to force a marginal entry even had one of the two fresh names screened cleaner.

---

## 2026-09-04 — PREMARKET (Friday, Week 36 day 5) — NO ENTRY; two real catalysts found, both killed, neither from a screener

Book **$3,103.64** (**base NAMED, lesson 44**: hand-built book, not the slice) = IWM
**9.8636 sh** @ $295.19 settled ($2,911.63, **93.81%**) + notional cash $192.01 (**6.19%**,
inside the buffer — no bearish thesis owed). Satellites 0/4, weekly 0/5. Max satellite
$465.55, 1.5% risk $46.55.

- 🥇 **LESSON 41 IN ITS PUREST FORM: both real names came from the earnings calendar, and
  SWBI appeared on NEITHER scanner.** BBCP appeared only as a corrupted row. Running the
  calendar first is the only reason this session had a board at all — seventh straight session.
- ❌ **SWBI — the session's best candidate, killed on rule 5a, and it produced a new rule.**
  Smith & Wesson reported 9/03 AMC with a large, real beat: revenue **$112.6M vs $98.7M est
  (+14.1%), +32.3% YoY**; adj EPS **$0.06 vs −$0.05**; adj EBITDA **$13.77M vs $5.99M
  (2.3×)**. Indicated **+9.0%** ($12.27 → ~$13.38 mid). It cleared every universe gate
  cleanly, **including liquidity on the median** (mean 690,862 / **median 480,000**, 1.6× the
  gate). **The kill: prior FY27 guide "mid-single digits" (≈5%) → "5–7%" (mid 6%) = +1 point
  of growth ≈ +0.95% on revenue — the same sub-1% band as PD (+0.3%) and CHPT (+0.6%).
  Rule 5a is now 3-for-3 in seven sessions.**
- 🆕 🥇 **NEW LESSON 5d — the session's real finding.** SWBI had **guided Q1 to +15–20% and
  delivered +32.3%** — a beat against its *own* number of **12–17 points** — and passed
  **~1 point** of that to the full year, while guiding **Q2 to +10%, a 22-point deceleration
  off the quarter just reported.** 5a says size the raise against consensus; 5d says **also
  size it against the company's own prior guide, and check the pass-through.** Smash your own
  quarter, raise the year by a point ⇒ management is calling the beat pull-forward.
- 🆕 **NEW LESSON 5e — read the COMPOSITION of the beat.** A **$2.9M non-recurring tariff
  refund** lifted SWBI's gross margin **~260bps of the 280bps reported**, and **net income was
  $2.6M — less than the refund.** Strip it and the quarter is ~breakeven on ~flat margins.
  **A beat assembled from a one-off does not recur, which is the whole premise of a
  continuation trade.** Killed as a **KILL, not a deferral** — per 45e, a *guidance* gate does
  not improve overnight (only *range* kills convert to a date).
- ❌ **BBCP — a genuine beat-AND-RAISE, killed on liquidity, and this one hurts.** Concrete
  Pumping reported 9/03 AMC: revenue **$116.8M +13%**, adj EBITDA **$30.4M +13%** (26% margin),
  and unlike SWBI **the raise is properly sized** — FY revenue $410–425M → **$425–435M
  (+3.0%)**, EBITDA $98–105M → **$103–108M (+3.9%)**, FCF → **+11%**, plus a **new $0.13
  quarterly dividend (~5.6% yield)**. Clears rule 5/5a/5c outright. **But lesson 46 fired for
  the second straight session**: `eligibility` read ADV **302,679 — a PASS by 0.9%**; raw bars
  gave **mean 303,738 (passes), ex-catalyst-bar 237,360 (fails), median 179,500 (fails by
  40%)**. 🚨 **The premarket book settled it: bid $7.00 / ask $11.46 — a 44%-of-price spread.**
  It also failed rule 45 independently (median range 3.77% × **2.95× multiple = 11.1%
  predicted**, 1.6× the trail; the ~17% gap alone is 2.4×).
- 📌 **Escalated as an observation, not self-approved**: at a **$465 max satellite**, a BBCP
  position is ~44 shares = **0.02% of a median day**. The 300k ADV gate now binds on *account
  size* rather than tradeability — same category as rule 13's $2B ceiling. **The gate was
  honored**, and it was not load-bearing because rule 45 killed BBCP anyway.
- ✅ **TLYS graded correct in one session** — **−2.3% on 0.8× RelVol** the day after its 23.9×
  spike. Yesterday's lesson-46 liquidity kill was right.
- 🚨 **LESSON 17a, NINTH DEMONSTRATION, WIDEST MARGIN YET**: `top_movers` printed **BBCP at
  "$10.62, +17.4%"** against a real regular-session close of **$9.05, +1.9%** — a 15-point
  error from quoting an after-hours print, on its single most important row.
- ✅ **Lesson 43 did NOT recur** (8→8, 5→5). ⚠️ **But I briefly thought it had — the "missing"
  rows were my own `tail -40` truncating.** Logged as 43b: **count against the full output; a
  count on a truncated view manufactures the false positive the rule exists to catch.**
- **Macro**: VIX **14.21** — a two-week low, no brake, **but into the month's biggest event,
  which is the exact 8/28 configuration** (low VIX ahead of a binary = positioning, not calm;
  IWM then took Warsh **7× harder than SPY**). 10-yr **4.76%**, second session not rising but
  still through the 4.75% trigger — flag live, watch not act. 🆕 **The inflation trio broke**:
  Brent −0.08% and WTI −0.33% fell together for the first time this week and the **dollar
  turned up**; only gold still rising.
- 🚨 **The whole session is one number: August NFP 8:30 AM, +53K consensus, u-rate 4.1%,
  after July's −23K — with a September HIKE live.** It resolves before the open (good case).
  🚨 **And Monday 9/07 is LABOR DAY, market closed** (confirmed vs the Alpaca calendar,
  9/04 → 9/08) — anything opened today carries the jobs reaction **plus a three-day weekend.**
  Rule 29, in its strongest form yet. **Next session Tuesday 9/08.**
- **Factor**: IWM +0.40% vs SPY +1.05% = **−0.65% Thursday** (≈−0.61% on the book), giving
  back most of Wednesday's +0.69%. **Lesson 28 applied with the same force as when it helped** —
  yesterday's file refused to book the gain as recovery; today's refuses to book the loss as
  decline. Six-week read belongs in **`weekly_review`, which runs today.**
- 🚩 **Rebalance-basis divergence carried and WIDENED — fourth straight session**: book
  $3,103.64 vs slice $3,210.30 = **$106.66**, back to essentially the 9/01 level ($107.06),
  **because Bull's book outran IWM Thursday** — lesson 44b's mechanism, visible in the
  direction. Escalated 9/01, 9/02, 9/03; **still awaiting a user decision on which basis
  governs.** No action (rule 6: `market_close` only).

---

## 2026-09-03 — MARKET_CLOSE (Thursday, Week 36 day 4) — NO TRADE, core basis divergence recurs 3rd session running

**Position review**: only Rocket position is IWM core (0/4 satellites) — no stop
applicable, nothing to close. Bull's JPM/SCHW/SPY reviewed for reconciliation only
(both carrying large unrealized gains, +15.6%/+6.3%, plus SPY +0.7% — not Rocket's).

**Core rebalance**: slice basis says hold (IWM 0.64% over target, inside 3% band);
book basis (lesson 23a) says SELL ~$118 of IWM (3.80% over, outside band) — same
divergence as 9/01/9/02, essentially unchanged in dollar terms. Followed the
documented slice-basis procedure, no trade. **Flagging explicitly per lesson 44c**:
this is the third straight session with the same unresolved conflict — it needs a
user decision on which basis governs, not a fourth session just noting it again.
Full numbers in `trade_log.md`.

**Day P&L**: IWM +0.34% / +$9.86 vs SPY +1.01% — Rocket trailed SPY by ~0.67% today,
pure IWM/SPY factor drag, no satellites in play. Weekly count stays 0/5 — every
name screened today (GIII/DAKT/CHPT/TLYS/ANAB/NEOV/PHR/MEI/RARE/PSQL/LE/MTRX/GCO/
DLTH/WLY/AGX, plus BNC/JFB/CBIO at open/midday) was killed on its own numbers.

---

## 2026-09-03 — PREMARKET (Thursday, Week 36 day 4) — NO ENTRY; 10 names screened, 10 killed

Book **$3,092.00** (**base NAMED, lesson 44**: hand-built book, not the slice) = IWM
**9.8636 sh** @ $294.01 settled ($2,899.98, **93.79%**) + notional cash $192.01 (**6.21%**,
inside the buffer — no bearish thesis owed). Satellites 0/4, weekly 0/5. Max satellite
$463.80, 1.5% risk $46.38.

- 🥇 **THE 9/02 PRE-COMMITMENT EXECUTED CLEANLY — lesson 42's best live test.** GIII's
  five gates were written *before* the print; **gate 3 (close above midpoint) failed
  outright**: GIII closed **$28.47, −11.5%, at 5% of its range** on 5.1× volume. DAKT
  gapped **+11% to $21.50 and closed $19.13, also at 5% of range.** Both **KILLED, not
  deferred** — and because gate 3 is *price action*, rule 45c's "kill converts to a date"
  correctly does **not** apply. No temptation to re-litigate, because the bar was written first.
- 🥇 **RULE 45 IS NOW A PREDICTOR, 2-for-2.** Forecast from each name's own catalyst-day
  history: **GIII ≈14.3% → actual 14.6%; DAKT ≈13% → actual 14.8%.** Both ~2× a 7% trail.
  The borrowed multiples the rule replaced (PD 2.3×, LTRX 3.7×) predicted 7–11% and would
  have **waved both through.** Logged as 45d.
- ❌ **CHPT — the only name to clear every universe gate, killed on rule 5a.** Real beat
  (rev **$116.1M +18% YoY** above the $100–110M guide; adj. loss $1.35 vs $1.60; record 38%
  GM; EBITDA loss $22.1M → $4.8M), indicated **+18.1%**. But **Q3 guide $105–115M, midpoint
  $110M vs consensus $109.3M = +0.6%** — the same sub-1% band that killed PD (+0.3%) —
  **no FY guidance at all**, and the midpoint is **−5.3% BELOW the quarter just reported.**
  Compounded by: net debt **−$141.6M** with **~1.4yr runway** and **two S-3 shelves filed
  inside 12 months** (rule 8a bad half); **median range 6.04% ≈ the trail**, own catalyst
  days 15.9–25.6%; and an **un-runnable ladder** (no dated post-print action ⇒ 11b FAIL;
  taken at face value the $7.00 mean puts the no-chase ceiling at **$6.09**, already through).
  Squeeze fuel was real (**22.59% short float, 14.45 days, rising into the print**) and
  **lesson 42a applies — it does not offset a soft guide.**
- 🆕 🥇 **NEW LESSON 46 — the session's real finding.** The screener **finally fired**
  (TLYS +29.7% at **23.9× RelVol**, first genuine signal in six sessions) and the name died
  on **liquidity**. Verifying ADV per lesson 14 exposed a trap: **mean 326,038 PASSES the
  300k gate; median is 133,200 — a 56% fail.** One 4.27M catalyst bar lifted the mean
  through the gate by itself. **An average taken over a window containing the catalyst is
  contaminated by the catalyst** — and it errs toward *entering* an untradeable name.
  Verify ADV on the median. TLYS also failed 37a outright (median range 7.06% ≈ the trail).
- Also killed: **ANAB** (reported, did nothing — +1.0% at 36% of range on below-avg volume),
  **NEOV** (12.5–18.6% ranges, volume exhausting 10.2M→3.7M→1.6M), **MEI** (catalyst stale,
  ~8/26), **PHR** (⚠️ sources disagree on the earnings date — **barred either way**, flagged
  unresolved rather than scored, lesson 38), **RARE/PSQL/WLY/AGX** (cap), **LE/MTRX/GCO/DLTH**
  (ADV 250k/228k/198k/123k).
- 🚨 **LESSON 43 FIRED A SECOND TIME**: `eligibility` requested **8** tickers, returned
  **7 — MEI silently omitted, exit 0.** Re-run alone it **passed every gate.** Twice now the
  dropped row mattered. Logged as 43a: reproducible tool defect, count every call.
- **Macro**: VIX **15.38** (spike retraced, no brake), 10-yr **4.796% FLAT** — the seven-session
  grind stopped, though still through the 4.75% trigger. But **Brent +5.2% over three
  sessions** with WTI confirming, **gold +2.41%**, dollar −0.34% = inflation being priced.
  🚨 **ISM Services 10:00 AM** (25 min after the window) and the **August jobs report Friday**
  — an argument against any same-day entry independent of every name-specific gate.
- **Factor**: IWM +1.18% vs SPY +0.44% = **+0.74% Wednesday**, ≈+0.69% on the book. **Lesson
  28 applied with the same force as when it hurt** — one session carries no information, and
  this does **not** dent the −2.50% since-rebase drift. Read it in tomorrow's `weekly_review`.
- 🚩 **Rebalance-basis divergence carried, still unresolved**: book $3,092.00 vs slice
  $3,184.70 = **$92.70**, narrowed from $107.06 **only because IWM outran Bull's book**, not
  because anything was fixed. Escalated 9/01 and 9/02; awaiting a user decision. No action
  here — rebalancing is `market_close` only (rule 6).
- **Result: 0/4 satellites, 100% IWM core, no trade, no notification.** Empty board, but
  **not an empty measurement** — the calendar produced ten names and every one was killed
  on a named gate.

---

## 2026-09-03 — MIDDAY (Thursday, Week 36 day 4) — NO TRADE, position review clean, one new name killed

**Position review**: only Rocket position is IWM core (0/4 satellites, unchanged since
8/26). IWM flat (-0.0%, $295.02 vs $295.12 entry) — no stop to tighten (core carries
none by design), nothing to cut. No satellites, so no per-name news check applicable.

**Afternoon scan** (`unusual_volume`): same names as premarket/open (CHPT, TLYS, RARE,
BNC, GOLD, JFB, PSQL, CLYM, ALMS, IRD, MEI, DAKT) — all already killed on named gates.
DFDV/FWDI/BTGO/ABTC/USDE are crypto-treasury proxies, mandate-excluded (rule 31), not
re-researched. One genuinely new name: **CBIO** (Crescent Biopharma, +17.8%, 2.6x
RelVol, cap $811M) — searched for a catalyst, found only a routine "presenting at
investor conferences" announcement, not a named catalyst. **Killed on rule 1** (volume
without catalyst). See `research_log.md`.

**Result: 0/4 satellites, 100% IWM core, no trade, no notification.** No forced cuts —
nothing to flag beyond the standing rebalance-basis divergence, which is a
`market_close`-only decision (rule 6) and stays escalated, not re-litigated here.

---

## 2026-09-03 — MARKET_OPEN (Thursday, Week 36 day 4) — NO TRADE, confirms premarket

Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged
(IWM core only, 0/4 satellites). IWM flat vs prior settled close ($295.10 vs $294.01).
Premarket's ten kills were all structural (guidance, liquidity, price action) rather
than "wait for the open" calls, so none needed re-checking.

- CHPT now **+49.3% on 116x RelVol** — confirms rather than reopens the rule 5a/5b kill
  (sub-1% forward guide, midpoint below the reported quarter); the move is now **2.7×**
  the pre-market indication and further through the rule 37a range gate (median 6.04%),
  not closer to tradeable.
- TLYS now **+21.5% on 191x RelVol** — confirms the lesson 46 liquidity kill (median ADV
  133,200, 56% below the 300k gate); per the research log's re-open table this name is
  **not re-openable on a catalyst**, only on a sustained median-volume shift.
- 🔎 **Ran `unusual_volume`/`top_movers` for fresh names not on the premarket board
  (Step 4).** Two stood out on real RelVol not explained by CHPT/TLYS: **BNC** (CEA
  Industries, +15.2%, 8.3x) and **JFB** (JFB Construction, +6.8%, 10.0x). Checked both
  inline (2 searches, under the 5-search subagent threshold).
  - **BNC**: a BNB digital-asset-treasury company (500k+ BNB held, targeting 1% of BNB
    supply) — a crypto-treasury proxy, **mandate-excluded by lesson 31** regardless of
    the move. Kill.
  - **JFB**: not a momentum catalyst — it's a SPAC-style business combination (JFB +
    XTEND Reality) closing **today**, converting to XTND and ceasing to trade on Nasdaq
    after today's close, with share-exchange terms conditioned on the $4.00 closing
    price (lesson 27 pinned-deal-price shape). Not Rocket's mandate. Kill.
  - RARE (−44.9%), CLYM, PSQL, GOLD, DFDV, USDE, FWDI: cap/sector/crypto-adjacent
    exclusions already established or self-evident, not researched individually.
- **Result: 0/4 satellites, 100% IWM core, no trade, no notification.**

---

## 2026-09-02 — MARKET_CLOSE (Wednesday, Week 36 day 3) — NO TRADE, core basis divergence flagged

**Position review**: only Rocket position is IWM core (0/4 satellites) — no stop
applicable, nothing to close. Bull's JPM/SCHW/SPY reviewed for reconciliation only.

**Core rebalance**: slice basis says hold (IWM 1.10% over target, inside 3% band);
book basis (lesson 23a) says SELL ~$117 of IWM (3.79% over, outside band) — the
lesson 44 divergence, now large enough to actually flip the decision. Followed the
documented slice-basis procedure, no trade, escalated the disagreement rather than
picking a side. Full numbers in `trade_log.md`.

**Day P&L**: IWM +1.21% / +$34.62 vs SPY +0.42% — Rocket beat SPY by ~0.79% today,
pure IWM/SPY factor tailwind, no satellites in play. Weekly count stays 0/5 — no
qualifying catalyst cleared any screen today (GIII/DAKT/ALMS/EOSE/OABI/IRD all killed).

---

## 2026-09-02 — MIDDAY (Wednesday, Week 36 day 3) — NO TRADE, no cuts, no new setups

**Position review**: only open position is IWM core (0/4 satellites) — **-0.7%**,
no stop applicable (core exempt per portfolio-construction rules). Nothing to cut,
nothing to tighten. Bull's JPM/SCHW/SPY reviewed for reconciliation only, not
Rocket's to manage.

**Afternoon scan** (`unusual_volume`): GIII now **-9.3% on 2.5x** (vs -4.2% at the
open) and DAKT **+6.1% on 6.6x** — both consistent with the pre-committed rule
37a/40a kill (catalyst-day range 4.4-4.7x the 7% trail); confirms the "not today"
call, no new information for the 9/03 second-day gates already written in
`research_log.md`. New name **IRD** (Opus Genetics) printed +12.5% on 3.4x — checked
inline (1 search): the move is anticipatory, tied to a **September 9 data webcast
announcement**, not delivered trial data. Rule 29 shape (binary readout ahead, 7%
trail can't protect against the gap) — **kill, not a today catalyst.** No other
screener name carried a same-day dated catalyst. **Result: 0/4 satellites held,
100% IWM core, no trade.**

---

## 2026-09-02 — MARKET_OPEN (Wednesday, Week 36 day 3) — NO TRADE, confirms premarket

Validated premarket's "no same-day entry" call against real open data — it held.
Snapshot synced clean: no overnight fills, no stops triggered, positions unchanged
(IWM core only, 0/4 satellites). GIII trading **−4.2%** and DAKT **+0.8%** 5 min into
the session — both consistent with the pre-committed kill (rule 37a/40a: catalyst-day
range 4.4–4.7× the 7% trail on their own history); no new information changes the
9/03 second-day gates.

- 🔎 **Ran `unusual_volume`/`top_movers` for fresh names not on the premarket board
  (Step 4).** Three stood out on real RelVol: **ALMS** (+9.8%, 14.5x), **EOSE** (+9.7%,
  8.3x), **OABI** (+13.8%, 4.3x). Checked all three inline (3 searches, under the
  5-search subagent threshold).
  - **ALMS**: current price/cap data ($21.32, **$2.91B**) contradicts the scanner's
    stale read ($10.40, $1.39B) — a data discrepancy worth flagging, but **either
    figure aside, no dated 9/02 catalyst found**, and the real cap is through the $2B
    lid regardless. Out on both counts.
  - **EOSE**: the move coincides with an **Aug 27 filing to sell 56.55M shares** — a
    dilution event, not a fresh positive catalyst (rule 7/8 territory). No today-dated
    news found. Kill.
  - **OABI**: only identifiable driver is the **Eli Lilly collaboration, dated
    mid-August** — stale, already priced in (lesson 33: a search result describing a
    move is not evidence until dated to today). No fresh catalyst. Kill.
- **Result: 0/4 satellites, 100% IWM core held.** No rebalance (market_close only,
  rule 6). No notification — flat session, no stops hit.

🚩 **Open item carried from premarket, unresolved**: the rebalance-basis divergence
(lesson 44/44a) — slice vs. book disagree on whether IWM is in-band. `market_close`
today must name its base explicitly.

---

## 2026-09-02 — PREMARKET (Wednesday, Week 36 day 3) — NO SAME-DAY ENTRY; GIII pre-committed for 9/03

Book **$3,058.08** = IWM 9.8636 sh @ $290.57 settled ($2,866.07, **93.7%**) + notional cash
$192.01 (**6.3%**, inside the buffer — no bearish thesis owed). Satellites 0/4, weekly 0/5.

- 🥇 **Earnings calendar ran first (lesson 41) and was the entire board for the fifth
  straight session.** 9/02 BMO slate gated down to **GIII** and **DAKT** (both in universe,
  both rungs clear on rule 13). **CXM killed in one command with zero searches** — cap
  $1,780M means even the **+15% rung is $2,047M, through the $2B lid: a zero-rung name.**
  OLLI out on size. **5 tickers requested, 5 rows returned — counted (lesson 43).**
- ❌ **BOTH names killed for TODAY on rule 37a/40a — and the measurement is the point.**
  Instead of borrowing PD's 2.3× or LTRX's 3.7× multiple, I pulled each name's **own**
  earnings-day history. **GIII: last 9 catalyst days ranged 9.8%–19.0% (median ~14.3%),
  a 4.7× multiple — every one exceeds the 7% trail, the mildest by 1.4×.** Gaps include
  **−11.4% (closed −18.6%)** and +15.6%. **DAKT: 4.4×, ranges 11.3%–19.4%, one gap of
  −22.9%.** Lesson 29: a 7% trail fills at the open, wherever the open is.
- 🥇 **GIII is the strongest second-day candidate since the rebase, and rules 2 + 40a agree.**
  ✅ **Dilution is the cleanest tier ever screened** — 1,001 EDGAR filings proven populated
  (2010→2026), and the only offering-type filings in *sixteen years* are an **S-3 from 2012
  and a 424B5 from 2014**; S-8 only since (8b). Net cash +$100M, FCF $128M.
  🚨 ✅ **Short float 28.30%** (7.59M/36.2M float), **18.17 days to cover, rising into the
  print** — nearly 2× the rule-9 bar, on a <50M float. ⚠️ **Ladder is dated and passes rung
  1**: Telsey Hold $38 (Aug 27), mean **$39.33**, high $40. **+15% rung $37.00 clears the
  mean by 6.3%**; +25% rung $40.21 misses the high by $0.21 ⇒ **one-rung name**, and
  **explicitly NOT the OOMA/PD kill shape** (their highest target sat *below* rung 1).
  ❌ But rule 4 is against it: **two straight below-midpoint closes on elevated volume
  into the print** (36% of range on 1.54×, then 29% on 2.0×), below MA50, −11.6% on the month.
- 🚨 **Five pass/kill gates written BEFORE the print (lesson 42)** for a **9/03 second-day**
  entry: (1) guidance raised **>2%, stated as a %** — a beat on $0.23/$570.37M with
  *reaffirmed* guidance is a KILL, lesson 5's 5-for-5 fader shape; (2) dated post-print mean
  **above 1.15× entry**, which sets a **hard no-chase ceiling of $34.20**; (3) 9/02 must
  **close above its midpoint**; (4) rule 2a/2b on the 9/03 open; (5) rule 2c/3 gap size.
  **Honest prior: most likely a kill on gate 1** — apparel guidance with CK/Tommy sales
  rolling off is likelier reaffirmed than raised.
- 🚩 **Lesson 42a said out loud**: GIII has the cleanest balance sheet *and* the best squeeze
  fuel on the book, and **neither offsets the range gate.** Independent gates do not net out.
- 🚩 **CORRECTED A FILE ERROR (lesson 39a).** The 9/01 log recorded "ANAB — AMC **today**
  [9/01]" and scheduled the re-screen on that basis. **ANAB actually reports 9/02** — so it
  is *barred by the earnings-week guardrail today*, not merely rung-capped. Second error
  caught by 39a after the Warsh/Powell one.
- 🚨 **LESSON 44 WAS VIOLATED THE DAY IT WAS WRITTEN, and the error has a direction.**
  9/01's `market_close` struck target_core off the **slice** ($3,179.36) and never named the
  base — the basis **lesson 23a says is invalid**. Two consecutive sessions on the slice now
  (8/31 used it and *bought*). Today the bases still disagree: **slice +0.55% = in band;
  book +3.72% = outside, indicating a SELL.** The slice is **$107.06 richer than the book,
  and that gap is Bull's P&L** (JPM +13.2%, NOW +18.9%) — **every dollar Bull makes pushes
  Rocket to hold more IWM**, the exact position carrying Rocket's whole deficit to SPY.
  **The bookkeeping error and the performance problem are one problem.** Escalated, not
  self-approved. **market_close today must name its base.**
- 🚨 **Rates are now a trend, not a print**: 10-yr **4.80%**, second session through the
  4.75% trigger and still climbing, with **Brent +$3 and WTI confirming** for a second day.
  Designed response for the stopless core is **no action** — recorded as a decision.
  **Three-event day**: ADP 8:15 (resolves pre-open), Factory Orders + Durable Goods 10:00,
  **Beige Book 2:00 PM** — the first since Warsh's hawkish debut.
- 🔧 **Scanners hit a new worst**: `top_movers` returned **zero usable RelVol across all 20
  names**; `unusual_volume` had **19 of 20 rows below 1.0×** with a mandate-excluded decliner
  (USDE) on top. Overlap tier was AGPU (standing lesson-7a kill) and TSSI (0.1×). **Eleventh
  straight lesson-17a demonstration; fifth straight session the screener contributed nothing.**
- 📝 **Process gap noted**: 9/01 ran three sessions but wrote **one** session note (premarket).
  `market_open` logged to `research_log.md` and `market_close` to `trade_log.md`, both
  skipping `session_notes.md`, which CLAUDE.md requires every session. That is how the
  unnamed rebalance base went unnoticed for a day.

**No trades placed — market closed. No notification sent** (no breaking news on an open
position; the only position is the stopless IWM core).

---

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

## 2026-09-18 Friday premarket (Week 38 day 5) — NO ENTRY. Two real catalysts, both dead on supply structure

**Book (base NAMED, 23a)**: IWM **5.4746 sh** (raw API qty — table printed "5", **lesson 24a
fifth recurrence, 9.5% error, largest yet**) × $285.43 settled = **$1,562.62 = 50.02% of
slice** — dead on the new 50% core cap. Slice $3,124.06. **Notional cash ~$1,561 = ~50% of
slice, ~40 points above the 10% buffer, no bearish thesis (none applies)** — the floor gap in
dollars, per lesson 56. Satellites 0/4 · weekly 0/5.

- 🥇 **THE FINDING — Rocket's own 9/17 log entry on PAAI was falsified by the issuer's 8-K,
  filed this morning.** The log said *"$1B deal + $89M investment for ~49%, confirmed via web
  search."* The filing says the company gets **zero proceeds**, is **not a party** to the
  equity transaction (a secondary block sale between two other holders), states **no dollar
  figure anywhere**, and was **furnished under Item 7.01 rather than filed under Item 1.01** —
  i.e. the issuer declined Section 18 liability on its own headline. **New lesson 57 + 57a
  (read the Item number; the disclosure route is free evidence).** Lesson 39a's predicted
  shape: written once, read twice, caught on the second reading.
- ❌ **PAAI CLOSED** — and **not load-bearing**, because it independently failed rule 46
  (**median ADV 84,400 vs 300k; mean 441,426 manufactured by one 31.76M bar = 5.2× mean/median,
  the widest contamination margin ever recorded**) and rule 51/54c (**9/17 MDD-from-HWM 37.38%**).
- 🥈 **SECZ was the best catalyst in weeks and still died.** Genuine, dated, primary-regulator
  catalyst: **SEC exemptive order 9/17 permitting limited tokenized US-stock trading, 5-year
  term** — Securitize is the direct beneficiary. Passed universe, domicile (DE), ADV (median
  1.38M), rule 13 (by 1.7%). ❌ **Killed on a TWO-BRANCH supply argument that needs no
  resolution**: S-1 registers **151.6M resale shares (92.8% of shares out), effective 8/07**,
  and the closing 8-K says only **~38.2% of shares are locked up** → **~100.9M unlocked
  registered shares against a reported 8.7M float.** Either the float is right (**11.6× the
  float is sellable today**) or it is wrong (**the low-float thesis doesn't exist**). Both kill.
  **Re-open condition pre-committed in the research log** (lock-up schedule from the proxy
  p.123 **and** the float reconciled — both, not either).
- 🚨 **53a CONFIRMED A SECOND CONSECUTIVE SESSION — the stop was not the binding gate.**
  On the corrected MDD statistic: **six of seven in-universe names fit inside a 7% trail**
  (SECZ 0.78× · ASPN 0.70× · HDSN 0.50× · AHRT 0.26× · GSIT 0.86× · ATOM 0.98×) and the board
  produced nothing anyway. 🥇 **The newly-approved statistic (54c) PASSED SECZ's stop fit on
  its first live use — and SECZ died on supply anyway. Lesson 54a demonstrated live: it
  removes a false veto, it does not supply an edge.** Recorded against Rocket's own escalation.
- ❌ **Rest of board all rule 1 (no dated catalyst)**: AHRT (+7.2% on a REIT with a 1.81%
  median range and **zero news** — only a BofA **SELL** reaffirm 8/10; closed 15% of range),
  ASPN (investor deck ≠ catalyst; PT raise 6 weeks stale), ATOM, GSIT, HDSN, TTI, NRGV, ALIT,
  UAMY, TDOC. **USDE/BNC/DFDV = standing crypto mandate kills, checked before the chart.**
- 📌 **Earnings calendar: 22 reporters (15 on 9/17, 7 on 9/18), ZERO survivors**, every one on
  a named gate. Lesson 41d tally **3-for-7**.
- ✅ **Macro is permissive and that matters**: VIX **15.36** (multi-week low), futures flat,
  crude easing, rule 29 blocks nothing. **No macro excuse for the zero — this was research and
  supply.** ⚠️ **10-yr 4.95%, first decline in 13 sessions — lesson 34: stand down on a trend,
  not one print. Still flagged.** 🚨 **Factor −0.60% against Rocket Thursday, but at the new
  50% core weight that is ≈−0.30% on the book — the IWM cap halved an adverse factor day.**
- 🔧 Instruments: `macro` clean 14th session, roll patch corrected **5 rows incl. a Russell
  sign flip**. Scanner `Change %` **12-for-12, fifth clean session** (55b check run first).
  RelVol unusable 5th session. `eligibility` 8→8 (43 held).

**🚨 Open thread — ONE breach is on the record (9/17); today's close would make it 2.** Today
ran at the NORMAL/HIGH bar, correctly — rule 8 needs two consecutive closes. If satellites are still <50% at today's
`market_close`, **Monday 9/21 premarket opens at the MEDIUM-conviction bar (CLAUDE.md rule 8)**:
widen to all four screeners, push deeper down each list, accept MEDIUM — **but the catalyst
requirement does NOT relax.** SECZ is the named first stop if its two-part condition resolves.
**And `weekly_review` W36/W37/W38 are ALL owed as of today — three reviews, ninth session
flagging W36.**

---

## 2026-09-23 — PREMARKET (Wednesday, Week 39 day 3)

- **Satellite floor breach now 3 consecutive logged `market_close` sessions** (9/17, 9/21,
  9/22). Rule 8's MEDIUM bar remains active. Full board run: both screeners, universe gate
  on every mover, catalyst validation by search on survivors.
- **GRML** (only both-lists mover, +43.2%/17.7×) — **re-confirmed standing kill.** Pulled
  EDGAR fresh rather than trusting memory: `stateOfIncorporation` still blank, SIC still
  "Biological Products" six months after the March rebrand. Now further extended on top of
  the prior +474%.
- **TPB, AGPU, ONT** — all killed on rule 1 (stale catalysts, 1–8 weeks old, already
  digested; TPB additionally showed internally inconsistent price data across sources —
  flagged, not booked as a new instrument defect since it wasn't independently confirmed).
- 🎯 **RARE (Ultragenyx) is the one survivor** — first-ever FDA approval of Fayuvi (UX111)
  for Sanfilippo syndrome Type A, dated 9/17, with same-day Citi ($32 PT) and MS ($20 PT)
  target raises. Clears every universe gate (cap $1,539M, domicile DE confirmed via EDGAR),
  clean on dilution (no shelf filing in 2+ years), short float ~17% (squeeze-flag territory,
  though float itself isn't low). Priced-in check passes — both analyst targets sit well
  above the current $15.62. **The one open question is entry timing**: the initial gap was
  only 12.6%, which doesn't cleanly match the gap-and-go (20–35%) or continuation (>25%/>35%)
  rules — it's now a 3-day-base breakout on top of a real catalyst. Written up as MEDIUM
  conviction, entry conditional on volume confirmation at `market_open`, not force-fit into
  a rule that doesn't quite apply.
- Macro clean and permissive (VIX 14.16, new low; Russell fut −0.28%, the one soft spot).
  No macro block on entries.
- **No trades placed — market closed, this is the pre-market research session.** If RARE
  doesn't fill at the open, today's `market_close` would be the 4th consecutive breach.
- Archived the full 9/22 research_log and all three dated market_context snapshots (9/17,
  9/18, 9/22) to their respective history files — both were running well over their stated
  line-count targets.

---
## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
