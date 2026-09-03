# Rocket Trade Log

Append-only record of all Rocket trades. Never delete entries.

---

## 2026-09-03 — NO TRADE (market_close, Thursday, Week 36 day 4) — core diverges by basis (3rd straight session), no satellites

**No fills today.** No satellites open to review (0/4, unchanged since the 8/26 OMER
stop-out). Premarket screened and killed ten names (GIII/DAKT gate-3 price-action
fails, CHPT beat-without-a-raise, TLYS liquidity-median fail, ANAB/NEOV/PHR/MEI/RARE/
PSQL/LE/MTRX/GCO/DLTH/WLY/AGX all killed on named gates). Market_open and midday
confirmed the same kills on fresh price action (CHPT +49.3%/116x, TLYS +21.5%/191x —
both moves confirm rather than reopen their kills) and checked two new names (BNC
crypto-treasury mandate-excl., JFB SPAC-merger-closing, CBIO no named catalyst) — all
killed. Board stayed IWM-only all session. See `research_log.md`/`session_notes.md`.

**Core rebalance check — SLICE basis** (documented CLAUDE.md procedure): slice
**$3,209.93** (portfolio_value $10,699.78 × 30%), satellite value $0, 10% buffer
$320.99 → target_core **$2,888.94**. Live IWM (raw qty **9.8636 sh**) × $294.97 =
**$2,909.47 — $20.53 / 0.64% of slice over target, well within the 3% band.** No trade.

🚩 **44/44a/44c divergence recurs a THIRD straight session, still unresolved.** On the
**BOOK basis** (lesson 23a: prior book $3,092.00 + today's script-verified IWM gain
+$9.86 = **$3,101.86**), target_core = book − $0 − 10% buffer ($310.19) = **$2,791.67**.
IWM is **$117.79 over** that target = **3.80% of book — outside the 3% band, book basis
says SELL ~$118 of IWM.** Slice basis says hold. This is essentially the same dollar gap
as 9/02 ($117.18) — it has not resolved itself, it has stabilized as a standing error.
**Followed the documented CLAUDE.md procedure (slice) again, did NOT self-resolve toward
book.** Per lesson 44c's own warning ("if this keeps recurring it needs a user decision
... not another session noting it"), this is now flagged as needing an explicit user
call on which basis governs core rebalancing — not deferred again by default.

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book): IWM
**+0.34% / +$9.86** today vs **SPY +1.01%** — Rocket trailed SPY by ~0.67% today,
entirely factor drag (small-cap IWM lagging large-cap SPY on today's tape; no
satellites to select). Hand-built book (lesson 23a): $3,092.00 → **$3,101.86** (+0.32%).
- Since-rebase figure **not recomputed here** — stands at the 8/28 weekly-review chain
  (Rocket vs SPY **−2.51%**, W35 review, grade C) until tomorrow's `weekly_review`
  (due Friday 9/04) chains it forward, per the lesson 23a discipline.
- Weekly count: **0/5** — Week 36 day 4 closes with zero new satellites, board-quality
  problem (all ten screened names killed cleanly on their own numbers), not a
  discipline gap.

---

## 2026-09-02 — NO TRADE (market_close, Wednesday, Week 36 day 3) — core diverges by basis, no satellites

**No fills today.** No satellites open to review (0/4, unchanged since the 8/26 OMER
stop-out). GIII/DAKT were both killed for a same-day entry at premarket (rule 37a/40a,
catalyst-day multiple 4.4–4.7x through the 7% trail); GIII carries pre-committed
second-day gates for 9/03 in `research_log.md`. Afternoon screens killed ALMS/EOSE/OABI
(no fresh dated catalyst / dilution) and IRD (rule 29 — binary readout Sept 9, 7% trail
can't protect a gap). Board stayed IWM-only all session — see `session_notes.md`.

**Core rebalance check — SLICE basis** (per CLAUDE.md's written procedure, named per
lesson 44): slice **$3,183.08** (portfolio_value $10,610.28 × 30%), satellite value $0,
10% buffer $318.31 → target_core **$2,864.77**. Live IWM (raw qty **9.8636 sh**) ×
$294.00 = **$2,899.90 — 1.10% of slice over target, within the 3% band.** No trade.

🚩 **44/44a divergence resurfaces, and today it crosses the band.** On the **BOOK basis**
(hand-built, lesson 23a: $3,091.91 = IWM $2,899.90 + notional cash $192.01),
target_core = book − $0 − 10% buffer ($309.19) = **$2,782.72**. IWM is **$117.18 over**
that target = **3.79% of book — outside the 3% band, book basis says SELL ~$117 of
IWM.** Slice basis says hold. Same disagreement flagged 9/01 (lesson 44): Bull's P&L
(JPM +13.6%, SCHW +4.3% today) inflates the slice; book does not. **Followed the
documented CLAUDE.md procedure (slice) and did NOT self-resolve toward book — no trade
taken, escalating the divergence to the user again rather than picking a side.**

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book): IWM
**+1.21% / +$34.62** today vs **SPY +0.42%** — Rocket beat SPY by ~0.79% today, entirely
factor tailwind (small-cap IWM outperforming large-cap SPY broadly; no satellites to
select). Hand-built book (lesson 23a): $3,058.08 → **$3,091.91** (+1.11%).
- Since-rebase figure **not recomputed here** — stands until the next `weekly_review`
  (due Friday 9/04) chains it forward, per the lesson 23a discipline.
- Weekly count: **0/5** — Week 36 day 3 closes with zero new satellites, board-quality
  problem (GIII/DAKT/ALMS/EOSE/OABI/IRD all killed cleanly on their own numbers), not a
  discipline gap.

---

## 2026-09-01 — NO TRADE (market_close, Tuesday, Week 36 day 2) — core in band, no satellites, YEXT killed

**No fills today.** No satellites open to review (0/4, unchanged since the 8/26 OMER
stop-out). YEXT (the one live candidate) was killed at market_open on gate 1 —
Q2 revenue missed consensus and no FY27 guidance raise was found, despite an EPS
beat (lesson 5's beat-without-a-raise shape). No fresh mover carried a validated
catalyst. Board stayed IWM-only all session. See `research_log.md` market_open entry.

**Core rebalance check**: slice **$3,179.36** (portfolio_value $10,597.88 × 30%),
satellite value $0, 10% buffer $317.94 → target_core **$2,861.43**. Live IWM (raw qty
**9.8636 sh**) × $290.295 = **$2,863.35 — 0.06% of slice over target, well within the
3% band.** No trade.

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book):
IWM **−1.20% / −$34.72** today vs **SPY −0.80%** — Rocket trailed SPY by ~0.40% today,
entirely factor drag (small-cap IWM underperforming large-cap SPY on a broad
risk-off Tuesday; no satellites to select). Hand-built book (lesson 23a): $3,081.26
→ **$3,046.54** (−1.13% cash-chain estimate; script's −1.20%/−$34.72 IWM figure is
authoritative for the day-P&L number itself).
- Since-rebase figure **not recomputed here** — the 8/28 weekly-review chain
  (**Rocket vs SPY: −1.27%**, W35 review) stands until the next `weekly_review`
  (due Friday 9/04) chains it forward properly, per the lesson 23a discipline. Do
  **not** cite `portfolio_snapshot.py`'s own since-rebase figures (+4.83%/+2.31% today)
  — that calc method mixes in Bull's P&L and is known to diverge from the
  weekly-review reconstruction.
- Weekly count: **0/5** — Week 36 day 2 closes with zero new satellites, board-quality
  problem (YEXT killed cleanly on its own numbers), not a discipline gap.

---

## 2026-08-31 — CORE REBALANCE, IWM BUY (market_close, Monday, Week 36 day 1)

**No satellites open to review** (0/4, unchanged since the 8/26 OMER stop-out).
Board stayed IWM-only all session per premarket/market_open's "no satellite, hold
IWM core" call — NEOV was the only name of substance and is gated by the 9/02
earnings-week rule; PD and RMNI remain killed. See `research_log.md` and
`session_notes.md` for full detail.

**Core rebalance, IWM BUY**: bought **0.3704 sh @ $293.958 = $108.89**, filled
19:58:56 UTC. Reason: slice **$3,221.73** (portfolio_value $10,739.11 × 30%),
satellite value $0, 10% buffer $322.17 → target_core **$2,899.56**. Live IWM
(raw qty **9.4932 sh**) × $293.965 = **$2,790.67 — 3.38% of slice short**,
just outside the 3% band. New IWM qty **9.8636 sh** (≈$2,900.14 at fill),
landing on target. Not a conviction trade — core rebalance only, funded from
pooled cash per rule "fund satellites/core from proceeds, never cash starvation."

**Portfolio now**: 100% core (IWM, 9.8636 sh), 0 satellites, 0/4 open satellite
slots used, 0/5 new-satellite count this week.

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book):
IWM **−0.55% / −$16.13** today vs **SPY −0.47%** — Rocket trailed SPY by ~0.08%
today, entirely factor drag (small-cap IWM lagging large-cap SPY on a broad
risk-off Monday; no satellites to select). Hand-built book (lesson 23a):
$3,106.43 → **$3,090.30** (−0.52%) before the rebalance trade; the $108.89
cash→IWM transfer is a reallocation, not a P&L event.
- Since-rebase figure **not recomputed here** — the 8/28 weekly-review chain
  (**Rocket vs SPY: −1.27%**, W35 review, IWM vs SPY raw −2.50% since rebase)
  stands until the next `weekly_review` chains it forward properly, per the
  lesson 23a discipline. Do **not** cite `portfolio_snapshot.py`'s own
  since-rebase figures (+6.20%/+2.80% today) — that calc method is known to
  diverge from the weekly-review reconstruction; the script's live account
  totals are authoritative for sizing trades, not for the since-rebase narrative.
- Weekly count: **0/5** — Week 36 opens with zero new satellites, board-quality
  problem (no genuine catalyst signal today), not a discipline gap.

---

## 2026-08-28 — NO TRADE (market_close, Friday, Week 35 day 5) — core in band, no satellites, Warsh hawkish

**No fills today.** No satellites open to review (0/4, unchanged since the 8/26 OMER
stop-out). Board stayed IWM-only all session per premarket's "no satellite, hold
100% IWM core" call — the overlap screen was zero names and every top_movers print
falsified against raw bars (seventh/eighth straight lesson-17a demonstration). See
`research_log.md` and `session_notes.md` premarket/market_open entries.

**Macro**: Kevin Warsh's first Jackson Hole keynote as Fed chair (10:00 AM ET) ran
hawkish — inflation "still too high," refused forward guidance, majority of investors
now pricing a September hike. Small caps (IWM) sold off harder than large caps (SPY)
into the print, consistent with rate-sensitive small-cap reaction to hawkish Fed talk.

**Core rebalance check**: slice $3,219.64 (portfolio_value $10,732.12 × 30%),
satellite value $0, 10% buffer $321.96 → target_core $2,897.67. Live IWM (raw qty
**9.4932 sh**) × $295.76 = **$2,807.80 — 2.79% of slice short, inside the 3% band.**
No trade (close call — nearest to the band edge yet without crossing it).

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book):
IWM **−1.35% / −$38.40** today vs **SPY −0.18%** — Rocket trailed SPY by ~1.17% today,
entirely factor drag from the hawkish Warsh reaction (small-cap IWM sold off harder
than large-cap SPY; no satellites to select). Hand-built book (lesson 23a): $3,147.21
→ **$3,108.81** (−1.22%), notional cash unchanged at $300.90 (9.68% — no trades to
move it).
- Since-rebase figure **not recomputed here** — 8/21 weekly-review reading (+4.53%
  vs SPY +3.18% = +1.35%) stands until the next `weekly_review` chains it forward
  properly, per the 8/21–8/27 precedent (lesson 23a discipline).
- Weekly count: **0/5** — Week 35 closes with zero new satellites opened, entirely
  a board-quality problem (no genuine catalyst signal all week), not a discipline gap.

---

## 2026-08-27 — NO TRADE (market_close, Thursday, Week 35 day 4) — core in band, no satellites

**No fills today.** No satellites open to review (0/4, unchanged since the 8/26 OMER
stop-out). Board stayed IWM-only all session per premarket's "no satellite, hold
100% IWM core" call — LTRX was the only fresh catalyst and it was triple-killed
(beat without a raise, shelf drawn twice in 2026, Warsh's Jackson Hole keynote
landing inside any hold). See `research_log.md` and `session_notes.md` premarket/
market_open entries for full detail.

**Core rebalance check**: slice $3,200.83 (portfolio_value $10,669.43 × 30%),
satellite value $0, 10% buffer $320.08 → target_core $2,880.75. Live IWM (raw qty
**9.4932 sh**) × $299.84 = **$2,846.44 — 1.07% of slice short, inside the 3% band.**
No trade.

**Day P&L** (script-verified `position_table.py`, IWM is 100% of Rocket's book):
IWM **+0.29% / +$8.26** today vs **SPY +0.66%** — Rocket trailed SPY by ~0.37% today,
entirely factor drag (small-cap IWM lagging large-cap SPY on today's tape, not a
stock-selection issue since there are no satellites to select). Hand-built book
(lesson 23a): $3,138.95 → **$3,147.21** (+0.29%), notional cash unchanged at $300.90
(9.6% — no trades to move it).
- Since-rebase figure **not recomputed here** — 8/21 weekly-review reading (+4.53%
  vs SPY +3.18% = +1.35%) stands until the next `weekly_review` chains it forward
  properly, per the 8/21/8/24/8/25/8/26 precedent (lesson 23a discipline).
- Weekly count: **0/5** — no new satellite opened this week yet, one session (Friday
  8/28, Warsh's keynote) left in Week 35.

---

## 2026-08-26 — OMER STOPPED OUT (market_close) + CORE REBALANCE, IWM BUY

**No premarket/market_open logged today either** — same quota-contention gap as
8/24–8/25, see [[launchd-quota-contention]]. First entry of the day is this
market_close sync.

**OMER exit**: 27 sh, entry $17.14 (8/14) → **7% trailing stop filled $18.270741**
(order submitted/filled 15:55:11 UTC intraday, well before this session started).
**P&L +$30.53 (+6.60%)**, held 12 calendar days.
- Reason for exit: trailing stop, not a discretionary close. HWM tracked up to
  **$19.6497** (8/25's $19.65 high), stop triggered at $18.274221 (7% below HWM).
  The **+15% profit rung ($19.71) was never touched** — the standing "sell 9 sh on
  the touch" order from premarket carried three sessions and never got the chance
  to fire; price rolled over from the high before reaching it.
- Today's mark-to-market piece of this exit (prior close $19.28 → exit $18.270741):
  **−$27.25** — the round-trip's lifetime P&L is positive, but today's session was a
  loser for the position.
- Lesson: a trailing stop and a profit rung are racing each other once a position is
  extended near a target — this is the first time the stop won that race outright
  (previously OMER's story was steady grinding gains). Still a net winner and still
  the correct exit mechanism; nothing to change about sizing or the trail width.

**Core rebalance, IWM BUY**: bought 1.441 sh @ $298.93 = $430.75, filled 19:58:56 UTC.
- Reason: OMER's closure left the satellite sleeve at $0, so the core fell far short
  of target. Slice $3,153.91 (portfolio_value $10,513.05 × 30%), satellite value $0,
  10% buffer $315.39 → target_core $2,838.52. Live IWM (8.0522 sh) marked at
  $2,407.04 — **13.7% of slice short**, outside the 3% band. New IWM qty **9.4932 sh**
  (≈$2,838 at fill), landing right on target.
- Not a conviction trade — core rebalance only, proceeds-funded per rule "fund
  satellites/core from proceeds, never cash."

**Portfolio now**: 100% core (IWM), 0 satellites, 0/4 open satellite slots used,
0/5 new-satellite count this week (OMER was opened week 33, not this week).

📊 **Day** (script-verified `position_table.py` for IWM's original 8.0522 sh + hand
calc for OMER's mark-to-market): IWM −$2.71, OMER −$27.25 (day-change portion only,
see above), **total −$29.96**. Hand-built book $3,168.91 → **$3,138.95 = −0.95%** vs
**SPY −0.02%** → Rocket **trailed SPY by −0.93%** today, entirely the OMER stop-out;
the new IWM tranche was bought at the close and contributed no day-change.
- Since-rebase figure **not recomputed here** — 8/21 weekly-review reading (+4.53%
  vs SPY +3.18% = +1.35%) stands until the next `weekly_review` chains it forward
  properly, per the 8/21/8/24/8/25 precedent (lesson 23a discipline).
- Weekly count: **0/5** — no new satellite opened this week yet. Board is empty of
  positions for the first time since 8/14; watchlist work is now the priority for
  the next premarket that actually runs.

---

## 2026-08-25 — MARKET_CLOSE (Tuesday, Week 35 day 2) — no trades, OMER held, core in band

**No fills today.** No premarket/market_open sessions ran today either (nothing logged
before this entry — same quota-contention gap as 8/24, see [[launchd-quota-contention]]).

- 🟢 **OMER HELD.** $19.28 (Friday's mkt-close snapshot $19.29), essentially flat, **−0.2%**
  today after five straight strong closes — a pause, not a breakdown. **+15% rung ($19.71)
  not approached** (today's action stayed well below it) — standing order to sell 9 sh on
  the touch carries into tomorrow. Stop still above entry; catalyst (CMS NTAP reimbursement
  2026-10-01, YARTEMLEA growth) is multi-day and intact — held overnight per the
  multi-day-catalyst rule.
- ✅ **Core rebalance check: no trade.** Slice $3,172.69, satellite value (OMER) $520.43,
  10% buffer $317.27 → target_core $2,334.99. IWM $2,410.75 is $75.76 (2.4% of slice)
  over target — inside the 3% band, no action per rule 6 of Portfolio Construction.
- 📊 **Day** (script-verified `position_table.py`): IWM +$11.88, OMER −$1.22, **total
  +$10.66**. Hand-built book $3,158.25 → $3,168.91 = **+0.34%** vs **SPY +0.33%** →
  Rocket essentially matched SPY today (+0.01%), core (IWM) leading on a small-cap-firm
  session while the satellite (OMER) gave back a touch.
- Since-rebase figure **not recomputed here** — 8/21 weekly-review reading (+4.53% vs
  SPY +3.18% = +1.35%) stands until the next `weekly_review` chains it forward properly,
  per the 8/21/8/24 precedent (lesson 23a discipline: don't guess it in a daily close).
- Weekly count: **0/5** — no new satellite opened this week yet.

---

## 2026-08-24 — MARKET_CLOSE (Monday, Week 35 day 1) — no trades, OMER held, core in band

**No fills today.** IWM 8.0522 sh and OMER 27 sh both carry over unchanged from Friday.

- 🟢 **OMER HELD.** Closed **$19.32**, +0.3% on the day — a flat/quiet session after five
  straight strong closes. **+15% rung ($19.71) not approached** (today's range stayed
  well below Friday's $19.58 high) — standing order to sell 9 sh on the touch carries
  into tomorrow. Stop still above entry; catalyst (CMS NTAP reimbursement 2026-10-01,
  YARTEMLEA growth) is multi-day and intact — held overnight per the multi-day-catalyst
  rule, not a one-day news bump.
- ✅ **Core rebalance check: no trade.** Slice $3,170.65, satellite value (OMER) $521.64,
  10% buffer $317.07 → target_core $2,331.95. IWM $2,398.91 is $66.97 (2.1% of slice)
  over target — inside the 3% band, no action per rule 6 of Portfolio Construction.
- 📊 **Day** (script-verified `position_table.py`): IWM −$16.27, OMER +$1.35, **total
  −$14.92**. Hand-built book $3,173.17 → **$3,158.25 = −0.47%** vs **SPY −0.28%** →
  Rocket **trailed SPY by −0.19%** today — IWM underperforming SPY on a small-cap-lag
  session (factor drag, see lesson 28 — one session is not a trend).
- Since-rebase figure **not recomputed here** — Friday's weekly-review reading
  (+4.53% vs SPY +3.18% = +1.35%) stands until the next `weekly_review` chains it
  forward properly, per the 8/21 precedent (lesson 23a discipline: don't guess it
  in a daily close).
- Weekly count: **0/5** — no new satellite opened this week yet.

---

## 2026-08-21 — WEEK 34 SUMMARY (weekly review) — 1 satellite opened and closed, 0 winners

**Satellite trades**: 1 opened (ETON 8/17), 1 closed (ETON 8/20). OMER (opened 8/14) still
open. **Win rate 0/1. Realized P&L −$6.09. Avg R −0.20R** (on $30.87 planned risk).
**Core rebalances: 2** (8/17 sell 1.6503 IWM; 8/20 buy 1.8546 IWM) — exempt from the
4-satellite and 5-trades/week caps. Weekly count **1/5**.

**Week performance (hand-built book, per lessons 23/23a — NOT the slice)**: $3,152.18 →
**$3,173.17 = +0.67%** vs **SPY −1.37%** (776.34 → 765.72). **Rocket vs SPY +2.03%** —
best relative week of the core/satellite regime. IWM −1.68% (305.09 → 299.96).

**Attribution** — satellite **+2.18%**, cash **+0.10%** (idle cash helped; SPY fell),
factor **−0.24%** (the core LOST to the benchmark this week). **Real alpha +2.18%.**
✅ **The entire margin is OMER, which was opened LAST week.** Nothing opened this week
contributed. Position P&L ties to the book change exactly: OMER +$56.16, IWM −$29.08,
ETON −$6.09 = **+$20.99**.

✅ **Hand-built since-rebase chain REBUILT this session** (flagged 8/21). Cash
reconstructed transaction-by-transaction from the W33 close and independently confirmed
against the 8/21 premarket research log: **$237.54**. **Since 7/20 rebase: Rocket +4.53%
vs SPY +3.18% = +1.35%** — first positive reading since the rebase. Cumulative real alpha
**+1.53%** (was −0.65%). ⚠️ `portfolio_state.md` reads +1.28%, only 7bp off — **a
coincidence, not a fix.** It still measures the whole shared account; it has converged
only because Bull's cumulative return currently sits near Rocket's. Lesson 23 stands.

🚨 **The week's real finding: ETON was graded on a counterfactual nobody checked.** The
8/20 close logged the exit as *"a materially better exit than where the 7% trailing stop
would have triggered."* **False.** HWM $63.83 → stop **$59.36**; 8/20 low **$59.59**,
8/21 low **$59.76** — **the stop was never touched**, and ETON closed 8/21 at **$63.47**.
Holding = **+$19.74**; the discretionary close **cost $25.83 (0.82% of book)**. It also
violated **lesson 30a**, written the day before, which says a Form 144 is *not* an exit
trigger. See the ETON correction entry below.

🔧 **Instrument fix**: `position_reconciler.py` had three parser bugs that were cancelling
each other out — it opened this session reporting Rocket's only satellite (OMER) as
**UNATTRIBUTED**. Fixed and verified balanced. Full write-up in `weekly_reviews/2026-W34.md`.

**Rules shipped this week**: (a) a discretionary close may only override a trailing stop
when the stop is **>2% away**; (b) every counterfactual in this log must cite the actual
stop level and the actual subsequent low; (c) lesson 2's second-day record corrected
**2-for-2 → 2-for-3**; (d) lesson 32 rewritten.

**Escalated to the user, NOT self-approved**: half-size sizing for lesson-29 binary-risk
names (ARCT skip cost +31%), and rule 13, which capped ETON's target and now blocks its
re-entry at $63.47.

---

## 2026-08-21 — ETON EXIT CORRECTION (weekly review) — the 8/20 close was WRONG

**Correcting entry.** The 8/20 `market_close` exit of ETON is unchanged as a *fact*
(7 sh sold @ $59.78, −$6.09, −1.43%). What is corrected is the **grading**.

The 8/20 entry justified the close as beating where the trailing stop would have fired.
Verified against raw daily bars this session:

| | |
|---|---|
| High-water mark (8/19 intraday high) | $63.83 |
| 7% trailing stop therefore at | **$59.36** |
| 8/20 low | **$59.59** — did not touch |
| 8/21 low | **$59.76** — did not touch |
| 8/21 close | **$63.47** |

**The stop would never have fired.** Holding through Friday = **+4.65%, +$19.74**.
**The discretionary close cost $25.83 — 0.82% of book, four times the realized loss.**

**The asymmetry was knowable at the time.** The 8/20 note itself recorded the stop as
"~0.7% cushion" below price. Closing early could therefore save at most 0.7% in the bad
case, against unlimited forfeited upside in the good case.

**Rule violated**: **lesson 30a** — "a Form 144 is NOT dilution… an argument to honor the
scale-out rung, **not an exit trigger**." The 144 was used as the exit trigger, one day
after that rule was written, on a name whose beat-**and**-raise catalyst was intact and
whose dilution profile was the cleanest screened to date.

**Root cause**: a counterfactual was asserted and never checked against the bars — the
same failure mode as lesson 33 (undated headline), turned inward on Rocket's own
self-grading. Lesson 32 has been rewritten; it previously enshrined this as a success.

---

## 2026-08-21 — OMER HELD OVERNIGHT, CORE IN BAND — NO TRADE (market_close, Week 34 day 5)

**OMER position review**: 27 sh, entry $17.14, closed **$19.24 (+3.3% on the day** vs
8/20's $18.63 close**, closing at the week high $17.19–$19.24)**. Fifth straight session
closing strong. Trailing stop remains above entry (HWM tracked up with today's high,
worst case still a gain). +15% rung ($19.71) not yet touched — closed 2.4% below it.
Catalyst (Q2 beat, CMS NTAP reimbursement) unchanged, ATM still undrawn. **Hold
overnight** — momentum sustained, multi-day thesis intact, stop protects the gain.

**Core rebalance check**: slice $3,169.89 (portfolio_value $10,566.30 × 30%), satellite
value (OMER) $519.75, 10% buffer $316.99 → target_core $2,333.15. IWM (raw qty 8.0522 sh)
× $300.14 = **$2,416.79 — 2.64% of slice over target, inside the 3% band.** No trade.

**Day P&L (hand-built book, per lesson 23a)**: 8/20 close $3,137.45 → 8/21 close
$3,169.89 = **+1.03%** vs **SPY +0.46%** today — Rocket beat SPY by ~0.57% today, driven
by OMER's +3.3% day plus IWM tracking with the broad small-cap tape. Position-level
detail (script-verified, `position_table.py`): IWM +0.80%/+$19.29, OMER +3.41%/+$17.14,
total **+$36.43** today.

⚠️ **Since-rebase hand-built chain has lapsed** — last verified point was the 8/14 W33
review (Rocket +3.84% vs SPY +4.62% = −0.78%, lesson 23). No daily note since has
carried the chain forward; `portfolio_state.md`'s auto figure (+1.33% vs SPY since
rebase) still mixes in Bull's P&L per lesson 23 and should not be trusted. **Rebuilding
the hand-built since-rebase chain transaction-by-transaction is flagged for the next
weekly_review** — not attempted here to avoid compounding a guess.

**No new satellite this session** — market_open/premarket found the board falsified by
raw bars (see research_log.md); weekly count stayed 1/5. Week 34 closes with 1 satellite
opened (ETON, since closed) and OMER still open.

---

## 2026-08-20 — ETON CLOSED (market_close) + CORE REBALANCE, IWM BUY

**ETON exit**: 7 sh, entry $60.65 → market close fill **$59.78** (filled 19:59:03 UTC,
trailing stop cancelled first). **P&L −$6.09 (−1.43%)**.
- Reason for exit: small-cap end-of-day rule — down further on the day (8/19 close
  $61.48 → $59.78, ≈−2.8%) and now **below entry** for the first time since the 8/17
  fill. Thesis already downgraded this week (CEO Form 144, 100,000 sh / $6,343,000,
  read as supply overhang not dilution) and the live trailing stop had narrowed to a
  ~0.7% cushion above the current price — closed rather than risk a stop-out at a
  worse level overnight.
- Lesson: the founder-sale overhang note from premarket (lesson 30) played out inside
  24 hours — a 144-driven downgrade with a thin stop cushion is worth closing into
  strength of the rule rather than waiting for the trail to fire.

**Core rebalance, IWM BUY**: bought 1.8546 sh @ $297.53 = $551.79, filled 19:59:43 UTC.
- Reason: post-ETON-close cash ($900.80 pooled) left the core far short of target.
  slice $3,156.19 (portfolio_value $10,520.63 × 30%), satellite value (OMER) $503.28,
  10% buffer $315.62 → target_core $2,337.29. Live IWM (6.1976 sh) marked at
  $1,844.13 — **17.5% of slice short**, outside the 3% band. New IWM qty 8.0522 sh.
- Not a conviction trade — core rebalance only, funded from ETON's proceeds plus
  existing pooled cash headroom, per rule "fund satellites/core from proceeds, never
  cash."

---

## 2026-08-14 — WEEK 33 SUMMARY (weekly review) — 3 satellites opened, 2 closed, 0 winners

**Satellite trades**: 3 opened (FF 8/11, VELO 8/12, OMER 8/14), 2 closed, 1 open.
**Win rate 0/2. Realized P&L −$17.64. Avg R −0.25R** (FF −0.34R on $36.00 planned risk;
VELO −0.16R on $34.20). No winners → no avg-winner figure. **Core rebalances: 3** (8/10 buy
0.5031 IWM; 8/14 sell 0.5822 to fund OMER; 8/14 sell 1.073 rebalance) — these do not count
against the 4-satellite or 5-trades/week caps.

**Week performance (hand-built book, per lessons 23/23a — NOT the slice)**: $3,135.02 →
**$3,152.16 = +0.55%** vs **SPY +0.40%** (773.26 → 776.34). **Rocket vs SPY +0.15%.**
IWM +1.17% (301.56 → 305.09).

**Attribution** — factor **+0.70%** (IWM − SPY +0.77% × ~90.7% core weight), cash drag
**−0.04%**, satellite **−0.52%**. **Real alpha −0.52%** — the worst satellite week since the
core sleeve existed. **The entire +0.15% headline was IWM beta, not skill.**

⚠️ **Since the 7/20 rebase: Rocket +3.84% vs SPY +4.62% = −0.78%.** The chained SPY figure
matches `market_data.py spy 2026-07-20` exactly (+4.62%), validating the hand-built chain.
`portfolio_state.md` reads **+0.10%** — **88bp of flattery, up from 67bp last week.**
Cumulative real alpha since rebase: **−0.65%**, never yet positive. See lesson 23a: the
*daily* notes also drifted back onto the contaminated slice all week.

**Rules shipped this week** (affect future orders):
- **Beat WITHOUT a raise is a DISQUALIFIER**, not a demotion (3-for-3 fader: SVCO, CVRX, FF).
- **P2 is not a substitute for a failed P1** — a failed P1 means no satellite, not the next
  name down. FF exists only because a slot was open.
- **An un-runnable filter is a FAIL, not a pass** — FF had no analyst coverage, so the ladder
  check could not run, and its absence was scored as an absence.
- **Opening-range gate**: if the 9:30–9:45 range exceeds 10% of price, defer to day 2.
- **The 9:45–9:50 bar must close in the upper half of its own range.**

**Under the core/satellite regime Rocket is 0-for-3 all-time** (CSTL, FF, VELO). Same-day
entries 0-for-3; second-day entries 2-for-2 (MRLN, OMER). Full write-up:
`weekly_reviews/2026-W33.md`.

---

## 2026-08-14 — CORE REBALANCE, IWM SELL (market_close)

- Sold 1.073 sh IWM @ $304.96 = $327.22, filled 19:59:28 UTC.
- Reason: post-OMER-entry IWM had drifted to $2,720.61 (10.3% of slice over target),
  outside the 3% band. slice $3,174.87 (portfolio_value $10,582.90 × 30%), satellite
  value (OMER) $464.00, 10% buffer $317.49 → target_core $2,393.39. New IWM qty 7.8479
  sh = $2,393.57 — within $0.18 of target, no share-granularity remainder (lesson 18).
- Not a conviction trade — core rebalance only.

---

## 2026-08-14 — OMER BUY (market_open)

- Shares: 27 @ $17.14
- Catalyst: Q2 beat (125% revenue beat, $28.5M vs $12.67M est), YARTEMLEA product sales
  $32.2M (+190% QoQ), adjusted EPS +$0.02 vs −$0.25 est, +$4.1M operating cash flow, CMS
  NTAP reimbursement effective 2026-10-01. Day-2 continuation entry — the catalyst work
  was done pre-market Thursday (8/13) but the trade was missed when a monitor-based
  market_open died silently without executing (lesson 24); this is day 2 of the 3-day
  missed-catalyst follow-up window.
- **GO/NO-GO call (lesson 24 — logged explicitly, not deferred)**: made at 9:45 AM ET off
  raw 5-min bars. 9:40–9:45 bar: O $17.02 / H $17.38 / L $16.92 / C $17.33 on 58,327 sh —
  ~1.6x the ~35.7k avg 5-min volume (2,787k avg daily / 78 bars). Held cleanly above the
  $16.85 GO threshold, never touched the $16.27 no-go floor (Thursday's low), stayed well
  under the $18.14 no-chase ceiling. Confirmed GO.
- Stop: 7% trailing, initial trigger $15.8379 (hwm $17.03)
- Target: 1st $19.71 (+15%) sell 1/3, 2nd $21.43 (+25%) sell 1/3, trail final 1/3
- Thesis: Uncapped analyst ladder (consensus $44.54/$38.00/$33.00 — lowest reading sits
  ~55% above entry, both profit targets clear it easily), short float 19.7–24.2% (>15%
  bar) against a 69.6M float, dilution re-checked clean (no offering announced 8/13–8/14,
  ~$132M cash, $100M buyback live, $150M ATM undrawn but not being drawn into strength).
  Primary risks: day-2 entry is 3.4% above Thursday's planned $16.39, launch-quarter
  revenue could prove lumpy (real bear case, not the balance sheet), single-product
  concentration, undrawn $150M ATM, $17.65–$18.14 resistance sits between entry and
  target one, and a Friday fill means a weekend hold with no stop protection overnight.
- CURI (P2, $3.99, beat-and-raise, ladder half-capped by a fresh analyst cut) was the
  named alternate — not taken, since OMER hit GO and both were flagged as one correlated
  day-2-continuation bet at double size.
- Position: 27 sh = $462.78 (14.6% of Rocket's slice). Funded by selling 0.5822 sh IWM
  @ $303.624 ($176.77) — notional slice cash ($288) alone was short of the $462.78 needed;
  pooled broker cash ($549.43) covered it too but was left untouched to keep Rocket's own
  core/satellite accounting clean rather than drawing on Bull's notional cash buffer.

---

## 2026-08-13 — No trades, core rebalance check (market_close)

**No fills today.** 0 satellites open (nothing to review). OMER (P1, HIGH from
premarket) was never actually evaluated — market_open logged only "waiting for the
monitor to fire" and no follow-up ever ran (midday has been dead since 2026-06-15).
New lesson 24. Not logged as a discretionary skip since no decision was made.

**Core rebalance check**: slice $3,188.02 (portfolio_value $10,626.74 × 30%),
satellite value $0, 10% buffer $318.80 → target_core $2,869.22. IWM (raw qty
9.5031 sh, per lesson 23) × $303.54 = $2,884.57 — 0.50% of slice over target, within
the 3% band. **CORE REBALANCE check, no trade.**

**Day P&L (hand-built, per lesson 22)**: IWM intraday +$7.89 (+0.25% of slice) vs
SPY +0.69% today. Since rebase (7/20): SPY +4.82% (script-verified), Rocket
hand-built ≈+4.91% (chained approximation) → Rocket vs SPY ≈+0.09% since rebase.

---

## 2026-08-12 — VELO CLOSED SAME DAY + core rebalance check (market_close)

**VELO exit**: 30 sh, entry $15.27 → market close fill **$15.09** (filled 19:59:37 UTC,
~4 hrs 20 min after the market_open entry). **P&L −$5.40 (−1.18%)**. Reason for exit:
discretionary same-day close, not a stop (trailing stop was cancelled first — the 7%
trail at $14.13 was never in danger). Intraday action: opened with a violent spike to
$17.61 (initial print $17.10) then round-tripped down to $14.35 within 10 minutes —
the 9:45 base that the entry was built on ($15.27) formed only after that whipsaw.
From there it never reclaimed much: intraday high after entry was $15.83 (10:45 ET),
then it faded on light, non-accumulating volume all afternoon to close in the
**bottom ~25% of its post-entry range** ($15.09 vs range $14.88–$15.83). Per lesson 4
(close-position-in-range tiebreaker — ASPN 28%-of-range and EVH 9%-of-range both died
despite real catalysts, both closed weak in the final hour), this is the same pattern
regardless of the beat-and-raise catalyst being real and multi-day. Applied the
market_close hold/close test: down on the day, below entry, closing near the day's low
with no thesis improvement intraday → closed rather than held overnight. **Lesson: a
strong beat-and-raise print does not override a bottom-quartile close — the ladder and
squeeze thesis were correct on paper, but day-one price action said sellers won the
session. Lesson 4 is now 3-for-3.**

**Position review**: 0 satellites open after the VELO close — nothing else to review.

**Core rebalance check**: slice $3,168.40 (live portfolio_value $10,561.34 × 30%,
snapshot taken post-VELO-settlement), satellite value $0, 10% buffer $316.84 →
target_core $2,851.56. IWM (raw qty **9.5031 sh**, per lesson 23 pulled from the raw
position endpoint) × $302.71 = **$2,876.68 — 0.79% of slice over target, well within
the 3% band.** No trade. **CORE REBALANCE, not a conviction trade** — logged as a
check, not an order.

**Day P&L (hand-built, per lesson 22 — do not trust the portfolio_snapshot.py auto
figure, it mixes in Bull's P&L)**: VELO realized −$5.40 (−0.17% of slice), IWM intraday
unrealized +$16.35 (+0.52% of slice) → Rocket book ≈ **+$10.95 on the day (+0.35%)**
vs **SPY +0.25%** today — Rocket beat SPY by ~0.10% today. Since rebase (7/20),
hand-built running total: Rocket **≈+4.65%** vs SPY **+4.12%** (script-verified) →
**Rocket vs SPY ≈+0.53%**.

---

## 2026-08-12 — VELO BUY (market_open)

- Shares: 30 @ $15.27
- Catalyst: Q2 beat-and-raise (revenue $20.7M +52.3% YoY, GAAP gross margin swung to
  +21.5% from −11.7%, FY26 guidance raised to $65–75M from $60–70M, backlog nearly
  doubled to $31M). Gap at open only +12.7% (Tuesday close $13.69 → $15.27 fill),
  smaller than the after-hours +18.3% print — a normal (not gap-and-go) entry.
- Stop: 7% trailing, initial trigger $14.13 (hwm $15.195)
- Target: 1st $17.56 (+15%) sell 1/3, 2nd $19.09 (+25%) sell 1/3, trail final 1/3
- Thesis: Beat+raise with an uncapped analyst ladder (consensus $23.33–23.75, both
  profit targets sit below it) and short float >18% into a low 13.8M float — a
  squeeze-eligible setup. Primary risk is the live $100M ATM into an 18%+ gap; not
  disqualifying (net cash, ~2yr runway, last raise 3.5mo old) but the thing to watch.
- Position: 30 sh = $458.10, 14.5% of Rocket's slice. Funded from pooled cash
  ($1,326.91 available) — no IWM trim needed.

---

## 2026-08-11 — FF STOPPED OUT + core rebalance check (market_close)

**FF exit**: 72 sh, entry $6.61 → trailing-stop fill **$6.44** (hwm $6.9715, trail 7%,
stop trigger $6.483495, filled 14:20:38 UTC, ~2.5 hrs after the 11:47 UTC entry). **P&L
−$12.24 (−2.57%)**. Reason for exit: stop hit, not a discretionary close — the 12:00 PM
ET earnings call apparently did not hold the base. Lesson: this was the P2 name (no
raise, no analyst coverage) flagged in premarket as the weaker of the two names; the
stop did its job cleanly, one session, small loss.

**Position review**: 0 satellites open after the FF stop — nothing else to review.

**Core rebalance check**: slice $3,167.34 (live portfolio_value $10,557.81 × 30%),
satellite value $0, 10% buffer $316.73 → target_core $2,850.61. IWM actual holding
**9.5031 sh** (not the "10" the `positions`/`portfolio_snapshot.py` display rounds
to — raw position pull confirms 9.5031) × $300.93 = **$2,859.77 — 0.29% of slice over
target, well within the 3% band.** No trade. **CORE REBALANCE, not a conviction
trade** — logged as a check, not an order.

**Day P&L**: FF realized −$12.24, IWM intraday unrealized +$9.03 → Rocket book
≈ −$3.21 on the day (**−0.10%**) vs **SPY −0.36%** today — Rocket beat SPY by ~0.26%
today, entirely because FF's small stop-loss was smaller than IWM's gain and both
beat the broad-market pullback. Since rebase (7/20), hand-built: Rocket **≈+4.30%**
vs SPY **+3.78%** (script-verified) → **Rocket vs SPY ≈+0.52%** (per lesson 22, the
`portfolio_state.md` auto figure mixes in Bull's P&L and is not trustworthy for
Rocket's own attribution).

---

## 2026-08-11 — FF BUY (market_open)

- Shares: 72 @ $6.61 avg fill ($475.92 cost, 15.0% of slice)
- Catalyst: Q2 earnings — revenue $78.7M (+120.6% YoY), GAAP net income $11.4M
  ($0.25/sh) vs a $14.2M loss a year ago, zero total debt. Reported after Monday's
  close; today is day one.
- Stop: 7% trailing, set at $6.11 (hwm $6.57 at time of order)
- Target: 1st $7.13 (+15%, sell 1/3) | 2nd $7.75 (+25%, sell 1/3) | trail final 1/3
- Thesis: Cleanest balance sheet on the board (zero debt) breaking to a new
  52-wk high on 1.5x avg volume within 15 min of the open, confirmed basing
  ~$6.55–6.60 after an opening spike to $6.96 — entered the 9:45 base, not the
  spike, per gap-and-go rule (20–35% gap). Risk: no analyst coverage, no forward
  raise (only qualitative "anticipates positive adj. EBITDA"), 12:00 PM ET call
  today is same-session event risk, CPI print tomorrow lands on day 2 of the hold.
- Skipped APEI (P1 in premarket research): round-tripped hard at the open — down
  1.3% on the day to $46.76 (vs. $53.50 premarket read), below both MA20/MA50 on
  just 0.2x avg volume. The soft EPS-guide risk flagged in research_log.md played
  out live; no gap-and-go base ever formed. Per "ONE satellite today, not two"
  (CPI tomorrow), FF was the only entry regardless.

## 2026-08-10 — IWM CORE REBALANCE (market_close) — fractional buy, band closed exactly

**Position review**: 0 satellites open — nothing to review. Core (IWM 9 sh) is the
only Rocket holding.

**Core rebalance check**: slice $3,164.97, satellite value $0, 10% buffer $316.50 →
target_core $2,848.47. IWM 9 sh @ $299.74 = $2,697.66 — **4.77% short of target,
outside the 3% band.** Bought fractional **0.5031 sh @ $299.74** (notional $150.81)
via `alpaca_client.py buy IWM 0.5031`. **CORE REBALANCE, not a conviction trade.**

- **Fill**: 0.5031 sh filled ~19:58 UTC. Position now **9.5031 sh, avg cost $293.26,
  market value $2,848.65** — landed within $0.18 of the $2,848.47 target. First
  fractional core rebalance to close the band exactly rather than leaving a
  whole-share remainder (contrast 8/07 and 8/03 entries, both blocked by
  share-granularity). Confirms lesson 15's fractional-order fix now works live.

**No satellite trades today** — no candidates worked this session; core-only day.

**Day P&L**: Rocket's book (IWM + notional cash, ≈ slice) **+0.39%** ($3,152.62 Fri
close → $3,164.97) vs **SPY −0.07%** today — IWM/small caps outperformed large caps.
Since rebase (7/20): Rocket **+4.40%** vs SPY **+4.12%** (**+0.28%**), chained forward
from the 8/07 weekly-review baseline (lesson 22 caveat still applies — this is a
hand-built proxy, not the raw `portfolio_snapshot.py` figure, though the two
currently agree since Rocket is ~100% IWM with no satellites live).

---

## 2026-08-07 — WEEK 32 SUMMARY (weekly review) — 1 satellite closed, 2 core rebalances

**Satellite trades**: 1 opened (CSTL 8/03), 1 closed (CSTL 8/06, stopped out).
**Win rate 0/1. P&L −$0.75 (−0.17%). R-multiple −0.02R** on $31.49 of planned risk —
a scratch, not a loss. **Core rebalances**: 2 (8/03 sell 1 IWM, 8/06 buy 1 IWM) — these
do not count against the 4-satellite or 5-trades/week caps.

**Week performance**: Rocket book $3,044.50 → $3,135.02 = **+2.97%** vs **SPY +3.51%**
(747.03 → 773.26). **Rocket vs SPY −0.54%.** IWM +3.56%.

**Attribution** — factor **+0.04%** (IWM − SPY was only +0.05%), cash drag **−0.49%**,
satellite **−0.13%**. **Real alpha −0.13%.** The week's underperformance was idle cash,
not stock selection.

⚠️ **The `portfolio_state.md` headline figures (−0.25% vs SPY) are WRONG and always have
been since the merge** — `portfolio_snapshot.py` derives Rocket's return from a fixed 30%
of the *shared* account, which is algebraically the whole account's return with Bull's
P&L included. The −0.54% above is hand-built from Rocket's own holdings and is the real
number. See `weekly_reviews/2026-W32.md` §5.

**Tooling changes shipped this session** (affect future orders):
- `alpaca_client.py buy/sell` now accept **fractional quantities**; trailing stops raise
  on fractional qty by design. The core can finally hit its rebalance target exactly.
  **UNTESTED against a live order — verify the `qty` in the first fill.**
- `smallcap_scanner.py` `Change %` column repaired (Finviz header rename).

---

## 2026-08-07 — NO TRADE (market_close) — no satellites to review, core in band

**Position review**: 0 satellites open — nothing to review. Core (IWM 9 sh) is the
only holding.

**Core rebalance check**: slice $3,152.62, satellite value $0, 10% buffer $315.26 →
target_core $2,837.36. IWM 9 sh @ $301.57 = $2,714.13 — **3.91% short of target,
outside the 3% band.** Per lesson 7a, only trade a breach if the nearest whole-share
move lands closer to target than doing nothing: buying 1 sh (@~$301.57) would push
IWM to $3,015.70, **5.66% over target** — a bigger deviation than the current 3.91%
short. **No trade** — share-granularity remainder, not actionable. Notional slice
cash $438.49 (13.9%), same known remainder flagged the last several sessions.

**Day P&L**: Rocket's book (IWM + notional cash) **+1.51%** ($3,105.58 → $3,152.62)
vs **SPY +0.66%** today — IWM itself moved +1.13% ($298.25→$301.61), small caps
outperforming large caps today; the extra lift in the slice figure reflects the
shared-account cash split, not incremental Rocket P&L. Since rebase (7/20): Rocket
+3.99% vs SPY +4.20% (**-0.21%**).

**No new trades placed today** — market_open found both ranked ideas (QNST, STLN)
disqualified and no fresh mover had a validated catalyst; no midday session ran;
market_close core rebalance is inside the actionable range (see above).

---

## 2026-08-07 — NO TRADE (market_open) — both ranked ideas disqualified at the open

**QNST (P1)** — extension gate essentially exhausted: intraday high $20.50 (+34.8%) vs the
$20.55 (35%) gate, and spot ($20.21) already above the $19.00 mean analyst target with no
revision confirmed. Base held (higher lows, strong relative volume) but risk/reward broken
— capped upside, full stop-out downside. Skipped.

**STLN (P2)** — premarket-flagged dilution risk (unverified, SEC 403'd) confirmed via
web search: active $15M ATM facility (424B5) on a company with a 0.1% EBITDA margin and
$41.1M cash. Same structural flaw that killed SOC and SVCO this month. Skipped.

**Fresh movers** (`unusual_volume`/`top_movers`) — none carried a validated catalyst;
declined to chase unvetted names late in the entry window. Full detail in session_notes.md
and research_log.md.

No positions opened or closed. Rocket unchanged: IWM 9 sh (core), 0 satellites.

---

## 2026-08-06 — CSTL trailing stop hit + core rebalance (market_close)

**CSTL — STOPPED OUT.** Trailing 7% stop filled intraday at **18:32 UTC (2:32 PM ET)**,
discovered at end-of-day sync (not caught live — no midday session ran today). Not a
market_close decision; the broker closed it automatically.
- Entry: 15 sh @ $29.99 (2026-08-03)
- Exit: **$29.94 on 2026-08-06** (stop: 7% trail off $31.73 high-water mark → trigger
  $29.5089, filled slightly better at $29.94)
- P&L: **-$0.75 (-0.17%)** — essentially breakeven, not a thesis failure
- Reason for exit: trailing stop, not a decision — the post-earnings pop's high-water
  mark ($31.73, set 8/03–8/04) pulled the 7% trail up with it, and today's session round-
  tripped through it. Catalyst (Q2 beat-and-raise) was never invalidated; this is the
  ordinary cost of a trailing stop giving back gains after a high print.
- Lesson: nothing actionable — stop worked exactly as designed, protected the post-pop
  high-water mark, exited at essentially cost. No open Rocket satellites remain (0/4).

**CORE REBALANCE — BUY IWM 1 sh.** CSTL's exit returned its proceeds to cash instead of
core per the same-session rule, opening a large gap: slice $3,105.58, satellite value
$0 (no open satellites), 10% buffer $310.56 → target_core $2,795.02. Pre-trade IWM (8 sh)
= $2,387.36 (13.1% short of target — outside the 3% band). Bought **1 sh @ $298.27**,
IWM now **9 sh, avg entry $292.90 ≈ $2,684**. Residual gap ~$111 (3.6% of slice) is a
whole-share rounding remainder, not further actionable — IWM trades in ~$298 increments
against a ~$111 gap, so 1 share is the closest achievable fit; buying a 2nd share would
overshoot to -6.1%. Notional slice cash after: ~$422 (13.6%), expected to normalize as
this residual works itself into future rebalances.

**Day P&L**: Rocket's total book (positions + notional cash) **-0.68%** ($3,126.82 →
$3,105.58) vs **SPY -0.15%** today — underperformance driven by the CSTL stop-out
(-1.38% intraday move that triggered the trail) plus IWM tracking slightly soft, not a
fresh problem. Since rebase (7/20): Rocket +2.44% vs SPY +3.59% (**-1.15%**), the widest
gap yet — consistent with the standing IWM-factor-drag note plus today's CSTL exit.

**No new trades placed today** beyond the stop-driven exit and its core rebalance —
market_open found all three ranked candidates disqualified; no midday session ran.

---

## 2026-08-05 — NO TRADE (market_close) — CSTL held, core in band

**CSTL position review**: 15 sh, entry $29.99, closed **$30.36 (+1.2% since entry)** but
**down from yesterday's $31.31 close (-3.0% on the day)** — a pullback off the post-earnings
pop, not a break. Still comfortably above entry and 9.3% clear of the $27.77 stop, MA50
$23.29 well below, week range $26.79–$31.18 (near the top, not breaking down). Catalyst
(Q2 beat-and-raise, guidance raise) is multi-day per the 8/03 entry thesis and confirmed
again 8/04 — no distribution signal (this is a single quiet red day, not fading on volume).
**Hold overnight.**

**Core rebalance**: IWM 8 sh = $2,400.40 vs target_core = slice $3,126.82 − CSTL $455.40 −
10% buffer $312.68 = $2,358.74. **1.33% over target — inside the 3% band. No trade.**
Notional slice cash $271.02 (8.67%), inside the 10% buffer.

**Day P&L**: Rocket's own positions (IWM + CSTL) **-0.99%** ($2,884.37 → $2,855.80) vs
**SPY -0.06%** today — underperformance driven by CSTL's pullback (-3.0%) plus IWM tracking
slightly softer than SPY, not a stock-specific problem. Since rebase (7/20): Rocket +3.14%
vs SPY +3.90% (**-0.76%**).

**No trades placed today** — market_open found all screened candidates disqualified, market
close found no exit or rebalance trigger. Flat session, no ntfy stops hit independently of
the scheduled EOD summary.

**Note**: portfolio_snapshot.py flags 12 sh NOW ($1,406) as unattributed — held at the broker
but absent from both Rocket's and Bull's trade logs. Not sized against or acted on; this is a
reconciliation gap for weekly_review, not a Rocket position.

---

## 2026-08-05 — NO TRADE (market_open) — both priority candidates disqualified

No fills or stops overnight. Cash unchanged at $430.37 pooled; Rocket notional cash
$261.41 (8.3% of $3,143.41 slice) — inside the 10% buffer, no action needed. IWM 8 sh
+ CSTL 15 sh unchanged, 91.7% invested. Checked both pre-market priorities plus fresh
scans (`unusual_volume`, `top_movers`); no candidate qualified.

- **APPS (Priority 1)** — hard-gated, lesson 15 for the third session running.
  Premarket plan set an explicit gate: 35% off the $9.51 Tuesday close = $12.84, no
  trade above it at decision time. Realized 9:45 AM tape: **$13.85–$13.95, +45.6% to
  +46.6%**, only 1% off the 52-week high. The gate was breached before the session even
  opened. **No entry.** Added to second-day watch (lesson 8) — valid continuation entry
  tomorrow if it closes strong on the print.
- **FTK (Priority 2)** — no entry, three independent reasons. Volume is only 0.4x avg
  (167k vs 361k avg) on a +29% move — the opposite of the >1.5x confirmation lesson 10
  requires. Market cap still returns `$0M`/unverified from the scanner (flagged
  premarket, never cleared). And the 10:00 AM ET earnings call was 15 minutes away at
  decision time — entering would mean holding through a live unscheduled binary.
- **TBI (fresh find, top_movers)** — +20.8–26.8%, inside the gap-and-go band, but avg
  daily volume 184k fails the 300k universe minimum outright. Disqualified on liquidity
  before any catalyst check.
- **AMPX / KODK** — unchanged from premarket, both remain watch-only (uncleared
  dilution flag on AMPX; unverified catalyst on KODK).
- **Result**: flat session, no trades placed. Per Portfolio Construction rule 7, "no
  qualifying catalyst" means hold IWM, not go flat — Rocket is already ~92% invested
  via core + CSTL, so no action was needed to stay compliant. No notification sent
  (flat session, no stops hit).

---

## 2026-08-04 — NO TRADE (market_open) — all four candidates disqualified

No fills or stops overnight. Cash unchanged at $430.37 pooled / ~$253 Rocket notional.
IWM core + CSTL satellite unchanged, 91.6% invested. Checked both pre-market priorities
plus fresh scans; every candidate failed on its own numbers.

- **AMRC (Priority 1)** — hard-gated. Pre-market plan set an explicit gate: gap >35% off
  the $22.73 Monday close (= $30.69) means wait for second-day entry, not chase. Raw 5-min
  bars show the actual **opening print was $31.93 = +40.5%**, breaching the gate before
  the first bar even closed. It then faded to a $28.97 low by 9:40 on ~443k shares (84% of
  full-day avg volume in 15 minutes) — high-volume chop after an over-extended gap, not a
  base. **No entry.** Added to second-day watch: if it closes strong today, tomorrow's open
  or first 10-min base is a valid entry per the second-day continuation rule.
- **BLZE (Priority 2)** — same failure mode, worse. Opened $20.13 (+29.1%, inside the
  gap-and-go band) but kept climbing through the first 15 minutes to a $23.99 high, last
  ~$23.54 = **+51.0%** off the $15.59 prior close — the *current* move is now more than 35%
  even though the opening print was not. Rule 2's "too extended, do not chase" applies to
  the state of the tape at decision time, not just the open tick. Combined with the known
  CoreWeave-warrant dilution overhang (research_log.md), this is a clean skip. Added to
  second-day watch, dilution caveat carries forward.
- **XGN (fresh find)** — Exagen Q2 2026 beat: revenue $19.94M vs $17.81M est (+16% YoY,
  record), EPS -$0.13 vs -$0.19 est, gap +32.7–34.6% (inside the gap-and-go band, unlike
  AMRC/BLZE). Real catalyst, but **fails the hard universe gate**: avg daily volume 229k,
  under the 300k minimum in CLAUDE.md's Investment Universe rule. Disqualified regardless
  of catalyst quality — thin-float healthcare name, no exception made.
- **BWEN** — appeared on both `unusual_volume` and `top_movers` (+14–15%, 3.4–3.6x RelVol),
  same overlap signature that found AMRC pre-market. Checked: **no catalyst**. Q2 earnings
  aren't until 8/11; the only recent news is a May wind-market exit, already stale. Rule 1
  (no catalyst = no trade) applies. Skip.
- **Result**: flat session, no trades placed. Per Portfolio Construction rule 7, "no
  qualifying catalyst" means hold IWM, not go flat — Rocket is already ~92% invested via
  core + CSTL, so no action was needed to stay compliant. No notification sent (flat
  session, no stops hit).

---

## 2026-08-03 — IWM CORE REBALANCE (market_close) — SELL 1 sh

- **Shares**: sold 1 @ ~$296.30 (filled 19:58:49 UTC), IWM position now 8 sh (avg cost
  basis unchanged $292.28)
- **Catalyst**: N/A — core rebalance, not a satellite trade. Satellites now hold CSTL
  (15 sh, opened this session at market_open, ~$456.60). target_core = slice − satellite
  − 10% buffer = $3,075.03 − $456.60 − $307.50 = $2,310.93. Pre-trade IWM value was
  9 sh × $296.33 ≈ $2,666.97, **11.6% over** target (band is 3%). Post-trade 8 sh ×
  $296.30 ≈ $2,370.64, **1.9% over** target — within band. Selling 2 sh would have landed
  7.7% under, a worse miss, so 1 share was the correct whole-share fix (lesson 7a).
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket now 8 sh IWM + CSTL (15 sh) satellite. Cash breach from premarket
  is resolved by the CSTL entry; this trade brings core back inside the rebalance band.

---

## 2026-08-03 — CSTL BUY (market_open) — Satellite #1

- **Shares**: 15 @ $29.99 (filled 13:51:42 UTC / 9:51 AM ET)
- **Catalyst**: Q2 2026 earnings beat-and-raise (reported 7/30): revenue $103.5M
  (+20% YoY), FY26 guidance raised $345–355M → $365–375M, core test volume +32% YoY,
  guided to positive Adjusted EBITDA Q3/Q4/FY26. Research log had this on ice since
  it closed 7/31 at $28.00, below its own $28.60 reclaim trigger — today it broke
  the trigger cleanly on ~3x 20-min volume (84,035 sh vs ~27,500 expected), price
  action monotonically higher through the 9:30–9:50 base (28.37 → 28.31 → 29.36 →
  29.94), no fade.
- **Dilution check** (run before entry, per standing rule): SEC EDGAR filings for
  CIK 0001447362 show no S-3/S-1/424B since a Feb 2024 shelf — clears.
- **Stop**: 7% trailing, placed immediately, hwm $29.86, initial stop $27.7698
- **Targets**: 1st 1/3 at +15% ≈ $34.49 | 2nd 1/3 at +25% ≈ $37.49 | trail final 1/3
- **Size**: 15 sh = $449.85 (14.6% of Rocket's $3,067 slice, under the 15%/$460 cap)
- **Thesis**: real earnings catalyst already validated over two prior sessions: today
  is a technical confirmation entry (base reclaim), not a fresh-news chase. Sector
  headwind noted — small-cap healthcare has been the weakest group this week — but
  this is an idiosyncratic guidance raise, not a sympathy bounce.
- **Skipped AMCX** same session: spiked to $11.50 on the open then fully round-tripped
  to $11.19–11.25 by 9:45–9:50 on only ~1.4x volume (61,439 sh vs ~44,100 expected) —
  a fade, not a base. Does not meet the >1.5x-volume hold-above-$10.83 entry rule as
  written. Watching for a cleaner base later in the week per the missed-catalyst rule.
- **REPL**: still no FDA decision confirmed as of this session; stayed flat per the
  standing no-entry-through-a-binary rule.

---

## 2026-07-31 — IWM CORE REBALANCE (market_close) — SELL 1 sh

- **Shares**: sold 1 @ $291.11 (filled 19:58:57 UTC), IWM position now 9 sh (avg cost
  basis unchanged $292.31)
- **Catalyst**: N/A — core rebalance, not a satellite trade. No satellites held (0
  open), so target_core = slice − 0 − 10% buffer = $3,043.69 − $304.37 = $2,739.32.
  Pre-trade IWM value was 10 sh × $291.09 = $2,910.90, **5.65% over** target (band is
  3%). Post-trade 9 sh × $291.11 ≈ $2,619.99, **3.92% under** target — closer to
  target than staying at 10 sh, so the trim was taken per lesson 7a (only skip a
  band-breach fix if the nearest whole-share trade would overshoot *worse* than doing
  nothing; here it doesn't).
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket now 9 sh IWM, no satellites. Whole-share granularity (1 sh ≈
  9.6% of slice) keeps causing this back-and-forth — same open thread as 7/28 and
  7/30, still worth a fractional-order fix at weekly_review.

---

## 2026-07-31 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 1 @ ~$289.64 (filled ~9:06 AM ET), IWM position now 10 sh (avg $292.31)
- **Catalyst**: N/A — core rebalance, not a satellite trade. Cures the cash breach: no
  premarket research ran today (research_log.md's watchlist is stale from 7/30), so
  market_open validated the two carryover names inline instead:
  - **CMCO** — real Q1 FY27 beat + 28.1% short float, but today -4.9% on 0.2x avg volume
    (drifting down on no volume, not a base). No entry.
  - **BOOM** — beat-and-raise catalyst still real, but flat today (+0.0%) on 0.1x avg
    volume, below MA50, 1-month move 0%. Dead. No entry.
  - Fresh scan (`unusual_volume` + `top_movers`) cross-referenced for names appearing on
    both: **JFB** (+13.5%, business-combination "momentum update" is not new dated news,
    plus a 1395% short-float reading that is almost certainly bad data — same red-flag
    profile as the DFNS hard-skip precedent) and **CAPR** (+4.8% but -81% over the last
    month, -37% over 5 days — a dead-cat bounce inside a freefall, no catalyst, skip).
  - **REPL** +100–130% on a real catalyst (FDA adcomm 10-3 favorable vote 7/30, PDUFA
    Aug 2) — but already 5x+ the 20% chase limit with a binary FDA decision imminent.
    Per lesson 8, added to watchlist for a pullback/consolidation entry, not tradeable
    today at any size.
  - No satellite confirmed → per CLAUDE.md Portfolio Construction rule 7 ("no qualifying
    catalyst means hold IWM, not go flat") and the cash-buffer rule (>10% cash requires
    a written bearish thesis, none exists), bought 1 more IWM share.
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket slice ~13.9% cash pre-trade → ~4.3% post-trade. Rocket now 10 sh
  IWM, no satellites.

---

## 2026-06-05 — MRLN CLOSED (+0.033% account)

**ROCKET'S FIRST TRADE** — ENTRY @ $8.88, EXIT $8.90

### ENTRY (9:50 AM)
- **Shares**: 1,670 @ $8.88
- **Catalyst**: USSOCOM C-130J autonomy Critical Design Review completion (announced June 4 after-hours). Major defense milestone advancing Merlin's AI-powered autonomy stack from design to aircraft integration phase. $100M+ IDIQ contract ceiling value.
- **Entry rationale**: Second-day continuation after +32.71% after-hours gap on real catalyst. Entry zone $8.54-$10.44 (within 10% of $9.49 after-hours close). Filled at $8.88 with 2.4x avg volume confirmation. Aerospace & Defense, $867M mcap (in-universe).
- **Stop**: 7% trailing (~$8.26 initial)
- **Targets**:
  - 1st third @ $10.21 (+15%)
  - 2nd third @ $11.10 (+25%)
  - Trail final third with 7% stop
- **Position size**: $14,830 (14.8% of account)
- **Risk**: $1,044 (1.05% of account)
- **Thesis**: Defense tech autonomy program milestone with USSOCOM. Second-day entry on confirmed catalyst with strong volume. Low float aerospace name with analyst PT $13 (strong_buy). Risk = profit-taking after big move, but catalyst quality high and volume confirmed conviction.

### EXIT (12:09 PM ET / 16:09:52 UTC)
- **Exit price**: $8.90 (filled via Alpaca)
- **P&L**: +$33.40 (+0.23% on position, +0.033% on account)
- **Intraday action**: MRLN hit $10.25 high (+15.4% from entry, reached first profit target), pulled back to $8.31 low (just above $8.26 stop), then recovered to $9.10 close
- **Exit reason**: Position closed at $8.90 during afternoon pullback. Stop not hit ($8.26), but position exited during volatility. No manual exit record captured in real-time.
- **Outcome**: PROFITABLE but small (+$33.40). Thesis validated (defense catalyst was real, stock moved +15% intraday and closed +22% on day at $9.10), but exited too early during midday chop at $8.90 instead of holding through close ($9.10) or first target ($10.21). Lesson: Trail stop caught downside volatility, but position closed prematurely.

---

## 2026-07-30 — IWM CORE REBALANCE (market_close) — sell-then-rebuy due to tooling error

**Intent**: rebalance check at market_close found IWM 10 sh = $2,926.90, **6.5% over**
target core (90% of $3,032.74 slice, 0 satellites = $2,729.47). Plan: sell 1 share to
land closer to target (9 sh = $2,635, ~3.1% under — the nearest achievable given
whole-share granularity, same tradeoff as lesson 7a).

**Execution error**: ran `alpaca_client.py close IWM --qty 1`. The `close` command has
no `--qty` support — it always calls `DELETE /v2/positions/{symbol}`, which liquidates
the *entire* position regardless of any trailing flag. Order filled for the full 10 sh
(sell, ~$292.69), leaving Rocket's core at **0 sh / 0% invested** for a few minutes —
an unintended full-liquidation, not a 1-share trim.

**Correction**: immediately bought back 9 sh via `alpaca_client.py buy IWM 9` (correct
command for exact quantities), filled ~$292.79. Net result matches the original intent
(9 sh core, ~3.1% under target) but took two round-trip orders instead of one partial sell.

**Stop**: NONE by design (core sleeve).
**Does not count** against the 4-satellite cap or 5-trades/week cap.
**Lesson logged** in lessons_learned.md: use `sell SYMBOL QTY` for partial reductions,
never `close` (full-liquidation only, ignores extra flags silently).

---

## 2026-07-30 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 1 @ $291.49 (filled ~9:51 AM ET), IWM position now 10 sh
- **Catalyst**: N/A — core rebalance. Cures the cash breach flagged 3 consecutive
  premarket sessions (7/28, 7/29, 7/30): pooled cash had drifted to 13.1% of slice
  (no written bearish thesis), driven down further overnight when Bull bought SCHW
  and consumed most of the shared buffer. Per the premarket plan's explicit fallback
  ("if BOOM does not confirm → buy 1 IWM share"), executed after BOOM failed its base.
- **Satellite candidates rejected today** (see research_log.md for full detail):
  - **BOOM** — failed the required 9:45-9:50 base. Real 5-min bars (yfinance) showed
    a spike to $7.37 at the open (already brushing the >35% ceiling), fading on
    declining volume each bar, then a break BELOW the $6.40 confirmation level to a
    $6.27 low on rising (distribution) volume in the 9:45 bar. Not a valid entry —
    correctly stood aside per lesson "price without volume [holding] = distribution."
  - **CMCO** — fresh name, +33% on a real Q1 FY27 earnings beat (EPS $0.61 vs $0.27
    est) with 28.1% short float (squeeze fuel). But real intraday data showed a spike
    to +42% at the open (past the 35% ceiling) fading hard on declining volume, AND a
    10:00 AM ET earnings call still ahead — a live binary. Skipped; watch post-call
    and tomorrow for a cleaner second-day setup.
  - **XRX** — +24-25% on a genuine Q2 earnings beat (EPS $0.38 vs $0.03), but prior
    close was $2.64 — this is a sub-$3 stock crossing the floor only today (the exact
    "sub-$3 trap" the rules exist to avoid), AND intraday high $3.78 was already a
    +43% gap (past the 35% ceiling). Skipped on both universe and chase-limit grounds.
- **Stop**: NONE by design (core sleeve, see 7/28 entry below).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: cash breach cured — pooled cash $397.09 (13.1% implied via slice math)
  → $105.68 (~3.5% of slice) after the buy. Rocket now 10 sh IWM, no satellites.

---

## 2026-07-28 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 9 @ $291.50 (filled)
- **Cost basis**: $2,623.50 (~86.4% of Rocket's $3,037.22 allocated slice)
- **Catalyst**: N/A — this is the core/benchmark sleeve, not a catalyst trade. Per
  CLAUDE.md Portfolio Construction (adopted 2026-07-27), Rocket's default resting
  state is ~100% invested via IWM, not cash. Rocket had been flat 0 positions /
  ~100% cash with no written bearish thesis, violating the mandate.
- **Stop**: NONE by design. Backtested 1993-2026: buy-and-hold beats every trailing-stop
  configuration on the index (10.73% CAGR vs 7.98-8.48% stopped). Satellites keep 7% stops;
  the core does not.
- **Does not count** against the 4-satellite position cap or 5-trades/week cap.
- **Thesis**: Establish the benchmark-tracking core so idle cash stops acting as an
  unhedged short against equity drift. Attribution note: IWM is a small-cap factor bet
  vs the SPY benchmark — weekly_review must split IWM beta from stock-picking skill,
  not book factor drift as alpha.
- **Remaining slice buffer**: ~$413 (13.6%) left for a satellite (TRAX conditional
  reclaim watch) or operating buffer.

---

## 2026-06-16 — CAMP ENTRY — [SUPERSEDED 2026-07-27 — ORPHANED BY ACCOUNT MERGE]

> **SUPERSEDED.** CAMP is not held on the current shared account and never was.
> This position lived on Rocket's pre-merge account. See the correction entry
> dated 2026-07-27 below. Retained for audit trail only.

**ROCKET'S SECOND TRADE** — ENTRY @ $4.85

### ENTRY (9:45 AM ET)
- **Shares**: 3,093 @ $4.85
- **Catalyst**: JPMorgan upgraded CAMP from Neutral to Overweight with PT $9 (from $5) on CMP-002 (SYNGAP1-related disorder) probability-adjusted upside. Leerink also raised PT to $9 on CMP-002 GLP tox progress, IND filing targeted H2 2026. Two analyst actions clustering = fresh institutional attention on small cap biotech (catalyst type: analyst upgrade).
- **Entry rationale**: Gap-and-go setup. Pre-market +10.4% gap under 20% chase limit. Entry at 9:45 AM on confirmed 10-min base ($4.85) with 2.1x avg volume (316k vs 78k avg). $252M mcap (in-universe), NASDAQ clinical-stage biotech, price >$3, low float (26.5M shares). Fresh same-day catalyst (Jun 16).
- **Stop**: 7% trailing stop set immediately (~$4.51 initial)
- **Targets**:
  - 1st third @ $5.58 (+15%)
  - 2nd third @ $6.06 (+25%)
  - Trail final third with 7% stop
- **Position size**: $15,001 (15.0% of account, max position cap)
- **Risk**: $1,052 (1.05% of account)
- **Thesis**: Fresh dual-analyst PT raises (JPMorgan and Leerink) on clinical-stage biotech with CMP-002 (SYNGAP1 disorder) advancing to IND filing H2 2026. Analyst clustering on small cap = institutional attention catalyst. Entry gap (+10.4%) under chase limit with strong volume confirmation (2.1x avg). Low float (26.5M) supports price movement. Risk = no near-term binary (CMP-002 not in clinic until H2 2026), clinical-stage (no revenue), FOMC tomorrow adds event risk. Entry discipline followed: gap-and-go base, volume >1.5x, fresh catalyst.

### EXIT — UNRECOVERABLE (recorded 2026-07-24 weekly review)
- **Status**: CLOSED, but exit price/date/reason cannot be recovered.
- **Backfill attempt (2026-07-24)**: Queried Alpaca closed-order history for the live
  shared account. CAMP does not appear — the only closed orders on the shared account
  are Bull's (KO, V, GOOGL, HSY, COST, JPM), oldest 2026-05-05. CAMP was traded on
  Rocket's original standalone paper account, which was dissolved in the 2026-07-20 merge
  with Bull. That account's order history is gone; there is no API path to recover the fill.
- **Resolution**: Treat CAMP as closed at an unknown price with unknown P&L. It is NOT a
  live position (confirmed absent from portfolio_snapshot.py). This entry is closed for
  bookkeeping. Do not report CAMP as open again.
- **Root cause / prevention**: Exit was never logged in real time (see lessons_learned.md
  item 9). Standing rule reinforced: every close_position call must be paired with a
  same-session trade_log.md exit entry.


---

## 2026-07-27 — BOOK CORRECTION — CAMP orphaned by the account merge

**Correcting entry.** Posted after reconciling this log against the shared Alpaca
account's filled-order history.

Rocket's book carried CAMP (3,093 sh @ $4.85, entered 2026-06-16) as an open position.
It is not held on the shared account, and **the shared account has no CAMP orders in
its entire fill history** — the position was opened on Rocket's own pre-merge account,
which is no longer the account Rocket trades.

**Disposition: unknown.** Rocket cannot determine the exit price or date, because the
account holding it is not the account it now reads. It may still be open on the old
account, or have been stopped out. Final P&L is therefore **unrecorded**, and this
trade is excluded from win-rate and R-multiple statistics rather than being assumed
a win or a loss.

**Impact**: Rocket believed it held a ~$15k position it does not have. Any sizing or
exposure calculation trusting the book was overstating deployed capital.

**Lesson**: an account migration must be treated as a reconciliation event. Positions
do not follow the agent — open positions must be explicitly closed out or transferred
in the book at the moment the account changes, or they become permanent phantoms.

---

## 2026-08-17 — ETON BUY (market_open) — Satellite #2

- **Shares**: 7 @ $60.65 (filled ~13:47 UTC / 9:47 AM ET)
- **Catalyst**: Q2 earnings beat-and-raise reported 8/13 — EPS $0.35 vs $0.12, revenue
  $37.59M vs $27.66M (+99% YoY), adj EBITDA margin 43% from 16%, FY26 raised to
  "exceed $145M" (from $120M+). Friday closed +44.3% at 86% of range on 4.6x volume.
  **Second-day continuation entry** per lesson 2/rule 3 (gapped >25%, closed far above
  midpoint) — today's open is the entry, not a fresh spike chase.
- **Gate checks at entry**: opening range from premarket $59.33 through the 9:45–9:50
  window stayed inside ~2% of price (well under the 10% rule-2a ceiling), price
  climbing steadily into the print with no whipsaw — a clean base, not a fade
  (rule 2b). Volume pace ~24% of ADV inside the first 15 minutes, consistent with a
  confirming surge once annualized against normal opening-minute pace.
- **Hard no-chase ceiling**: $60.80, derived from the $2B market-cap lid at 28.6M
  shares out (rule 13) — a +15% target only clears $2B if entry ≤ $60.80. Filled at
  $60.65, inside the ceiling by $0.15.
- **Analyst ladder**: dated post-print consensus $71.00 (4 analysts, H.C. Wainwright
  $70 and Craig-Hallum $76 both raised after the print) — clears rule 11.
- **Dilution check**: EDGAR shows no S-3/424B5/S-1 in ETON's recent filing history;
  operating CF +$15.1M, FCF +$3.3M, cash $26.8M vs debt $29.0M — cleanest dilution
  profile screened to date (rule 8).
- **Short float**: 6.7% — below the 15% squeeze bar, sized normally, no squeeze kicker.
- **Stop**: 7% trailing, placed immediately, hwm $60.475, initial stop $56.24
- **Targets**: sell 4 sh at $68.23 (+15%), trail the remaining 3 sh — **no +25% target
  set**. $74.16 fails both the $71 consensus and the $2.12B cap lid (rule 13), so the
  second rung is capped; this is a one-rung name.
- **Size**: 7 sh = $424.55 (13.4% of Rocket's $3,158 slice) — cap-bound (max 7 vs
  risk-based 11), risk ≈$30.87 (0.98% of allocated equity)
- **Risk / what kills it**: (1) the capped upper rung caps expected payoff versus a
  normal setup; (2) unresolved insider Form 4/144 activity (8/4, 6/23–6/26) — likely
  routine but not verified; (3) open through Wednesday 8/19 2:00 PM FOMC minutes;
  (4) no squeeze fuel at 6.7% short float.
- **Slot budget note**: this fills the one Mon/Tue satellite slot per the W33-review
  standing call — OABI (Tuesday's second-day setup) is deferred to Thu 8/20 or Fri
  8/21 per the research log.

---

## 2026-08-17 — CORE REBALANCE, IWM SELL (market_close)

- Sold 1.6503 sh IWM @ $304.04 = $501.68, filled 19:58:57 UTC.
- Reason: post-ETON-entry IWM had drifted to $2,431.04 (8 sh), 15.9% of slice over
  target and well outside the 3% band. Shared account $10,479.31 → slice $3,143.79,
  satellite value (ETON $431.69 + OMER $468.18) $899.87, 10% buffer $314.38 →
  target_core $1,929.54. New IWM qty ≈6.3497 sh ≈ $1,930.36 — within $0.82 of target.
- Not a conviction trade — core rebalance only.

