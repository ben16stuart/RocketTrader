# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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
## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
