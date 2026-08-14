# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-08-14 — MARKET CLOSE (Friday, Week 33)

**OMER held overnight — closed 60% of today's range, thesis intact.** Day-2 entry $17.14,
closed $17.19 (+0.3%). Raw 5-min bars: today's range $16.54–$17.61, last print $17.18 →
59.8% of range, above the midpoint (lesson 4 tiebreaker — this is the QNST/RCEL/CRSR
pattern, not the ASPN/EVH bottom-quartile one). Volume faded hard from yesterday's 13.4M
to ~3.2M today (expected day-2 cooldown, not a red flag on its own given the range close).
Catalyst (NTAP reimbursement effective 10/01) is multi-day and unplayed — no reason to
exit early. Known, accepted risk: Friday fill = weekend gap with no stop protection,
flagged at entry, not new information. **Hold.**

**Core rebalance — SELL, band breached.** OMER's entry (funded partly by an IWM sale)
plus the day's drift left IWM at $2,720.61, 10.3% of slice over `target_core` — well
outside the 3% band. Sold 1.073 sh IWM @ $304.96 ($327.22), landing IWM at $2,393.57 vs a
$2,393.39 target (within $0.18, no granularity remainder — lesson 18 holding). Logged as
CORE REBALANCE, not a conviction trade.

**Day P&L**: IWM +$13.24 intraday (realized + unrealized) + OMER +$1.35 (day-1) ≈ **+$14.59,
+0.46% of slice**, vs SPY **−0.22%** today → Rocket beat SPY by **+0.68% today**, on IWM
positive divergence (small-cap factor up while SPY was down) plus OMER holding flat-to-up.
Since rebase (7/20, script-verified): Rocket +4.76%, SPY +4.61%, Rocket vs SPY **+0.15%**.

**Weekly trade count (hand count, lesson 25): still 3/5** — FF (8/11), VELO (8/12), OMER
(8/14). The IWM rebalance is not a new position and does not count against the cap.

---

## 2026-08-14 — MARKET OPEN (Friday, Week 33)

**TRADE PLACED — OMER, 27 sh @ $17.14. Lesson 24 closed out clean: the GO/NO-GO was made
and logged explicitly at 9:45 AM, not deferred to a monitor.** 9:40–9:45 raw 5-min bar (O
$17.02 / H $17.38 / L $16.92 / C $17.33 on 58,327 sh, ~1.6x avg 5-min volume) held cleanly
above the $16.85 GO threshold and never touched Thursday's $16.27 low — confirmed GO. Filled
$17.14, stop $15.84 (7% trail), 14.6% of slice. Funded by selling 0.5822 sh IWM (core stayed
IWM-only, no pooled-cash draw) rather than the higher, easier route of just using the $549
pooled cash sitting free — kept Rocket's own core/satellite book clean instead. CURI (P2) was
correctly passed — it was the explicit alternate, not a second position, and OMER hit GO.

**Step 4 scan found two new names, both correctly passed.** ETON: real beat-and-raise
(revenue +99%, EBITDA margin 43% from 16%, guidance raised to $145M+, PT raised to $65) but
**+37.6% intraday — a >35% gap, second-day only per rule 2.** Added to watchlist for Monday
8/17; re-verify the $2B cap clearance at a ~$70 second-day entry before sizing. NMAX: Q2 EPS
beat but **guidance reiterated, not raised** — beat-without-raise, the exact pattern that
stopped out FF — plus thin, undated 2-analyst coverage. Passed, not researched further.

**Weekly trade count (by hand, lesson 25 — script still misreports): FF (8/11), VELO (8/12),
OMER (8/14) = 3/5.** Two slots remain this week.

---

## 2026-08-14 — PREMARKET (Friday, Week 33)

**No trades — market closed. Today's board is carry-overs, not new names, and that is the
honest read: the earnings pipeline is spent.** 6 web searches, all inline, no subagent
(lesson 20).

**🥇 OMER — P1, HIGH. Same trade as yesterday, one day later, and it is fading premarket.**
Thursday's catalyst work stands unchanged (125% revenue beat, +190% QoQ product ramp, swing
to profit, NTAP effective 10/01) — it is on the board today only because **lesson 24**: the
monitor died, no midday exists, and it ran untraded. Raw bars: **O $16.65 H $18.14 L $16.27
C $17.35 on 13.4M sh (6.4x ADV), closing at 58% of range** — above the midpoint, so the
second-day rule is live, but it gave back 43% of the intraday range and that is not QNST's
90% conviction close. **Premarket $16.92, −2.5% — which makes the entry better, not worse**,
pulling it back toward Thursday's planned $16.39 instead of forcing a chase through $18.14.
Ladder re-struck at $17.00: **+15% $19.55 / +25% $21.25 vs a LOWEST analyst reading of
$33.00 — uncapped by ~55%** (lesson 11d). Short float 19.7–24.2% ✓. Dilution re-checked:
**no offering announced 8/13–8/14**, the named trigger has not fired; ~$132M cash, buyback
live, $150M ATM still undrawn. Cap at target two **$1,538M**, clears the lid by 23%.
**Entry 9:45–9:50: GO above $16.85 on >0.75x 5-min volume; NO-GO below $16.27; never chase
above $18.14.** Stop **$15.81** (below Thursday's entire range). **28 sh = $476.00 (14.9%)**,
funded by selling **~0.565 sh of IWM**. ⚠️ Honest marks against it: the entry is 3.4% worse
than yesterday's, the $17.65–$18.14 band now sits between entry and target one, and a Friday
fill is a weekend hold on a single-product biotech.

**🚨 The binding rule today is lesson 24, not a market rule.** `market_open` must log an
explicit **GO or NO-GO with the observed 9:45–9:50 bar**. No monitor deferral. Two
consecutive sessions of this flaw would cost the same trade twice.

**🥈 CURI — P2, MEDIUM, and the ALTERNATE not a second position.** It passed the exact gate
set for it Thursday: closed **$3.99 at 57% of range** on 20.3M shares, above the midpoint,
and now **clears the $3 price gate on its own close** rather than only on the gap. Real
beat-and-raise (licensing +48% to $14.1M, GM 53%→73%, net income $8.9M, outlook raised).
Dilution clean and the good kind — **no debt, dividend + buyback**. ⚠️ Two real knocks:
**the ladder is half-capped** — a *fresh, dated, post-print* analyst **CUT to $5.00 from
$5.50 citing "lumpy" licensing**, so +15% ($4.66) clears but **+25% ($5.06) sits on top of
the lowest target**; and **$10.9M cash against a ~$20M/yr dividend** is the mechanism that
turns a licensing miss into dilution. Short interest only 4.3%, falling — no squeeze leg.
**OMER and CURI are the same structural trade** (day-2 continuation on a post-earnings gap
that closed mid-range), so taking both is one correlated bet at double size into an
unresolved 10:00 print. **Take CURI only if OMER hits its $16.27 no-go.**

**Dropped, with the two worth naming.** **CAPR** was the biggest thing on the tape (+98% →
$8.34, 60x RelVol, now $8.70) on the FDA signalling it will accept an amended deramiocel
application — and it is a **hard no on three independent grounds**: a >35% gap is
second-day-only (rule 2); **the PDUFA is 8/22, inside a 1–5 day hold, after a 9–3 AdCom vote
against efficacy** — a coin flip no stop protects through a halt; and a doubled clinical-stage
biotech with securities-fraud class actions will raise into the strength. **Rocket trades
continuation, not binaries.** **IMXI** (+25%, 11.9x) is real news — NYDFS cleared the Western
Union deal — but it is **all-cash at $16.00/share**, so **Rocket's +15% target ($16.82) sits
above the deal consideration**: the capped-ladder logic in its purest form, where the "target"
is a contract. Added to the merger-arb skip list beside HZO. Also resolved cleanly: **MGNX /
IPWR / INV / SPRY** all printed 8/13 and **all four failed the day-one range check** (25% /
**11%** — IPWR round-tripped $4.76→$5.25→$4.26 / 36% / didn't move) — the earnings-week bar
saved the work and the range check finished them. **VOGX** has the board's best float (3.4M,
24%) but is a two-day-old listing whose "382,500 ADV" is computed off a two-day sample while
**Thursday's real volume was 81,000** — lesson 13 in reverse, the gate reads PASS off bad
data. Sixteen more names moved +2.5–5.8% on 0.0–0.6x RelVol with no catalyst (lesson 1).

**Macro — both of the week's big prints are spent, benignly, but today's structure is the
week's worst.** **PPI resolved without a search**: the **10-yr rallied 4bp to 4.64%** and VIX
fell to 14.57 — a hot producer print does not produce a bond rally, so the "no new satellite"
brake never fired. The 4.75% trigger is now **11bp away, the widest cushion of the week**,
after being tested twice. 🚨 **But UMich prelim lands 10:00 ET — AFTER the open**, ~10 minutes
past the entry window, and it is the first entry this week placed into an unresolved print
(forecast 54.1 vs 55.2; the 4.2%/3.3% inflation-expectation legs matter more than the
headline). **Do not widen the stop for it; do have the stop working by 10:00.** ⚠️ Also
logged honestly: **SPY beat IWM by 0.44% Thursday**, ending the two-session small-cap streak,
and Russell futures are **−0.01%** against green S&P/Nasdaq — the "Russell red" trigger is
**grazing for the first time but not fired**. Mon–Thu the factor bet ran −0.52% → +0.66% →
+0.32% → −0.44%, about a wash. **Booked as beta in both directions, not skill** — the same
discipline applied to Wednesday's outperformance applies to Thursday's drag.

---

## 2026-08-13 — MARKET CLOSE (Thursday, Week 33)

**No trades. 0 satellites, core (IWM) within band — but the real story is OMER never
got evaluated.** Premarket flagged OMER (P1, HIGH — 125% revenue beat, uncapped
ladder ~2x, 19.7–24.2% short float) as the best-constructed setup Rocket has
screened. The 07:45 market_open log shows it set up a monitor to wait for the
9:45–9:50 base and then... nothing — no midday log (dead since 6/15, lesson 21), no
follow-up decision anywhere, no trade. **New lesson 24: this is an infra failure, not
a discretionary skip** — every prior "no trade" session logged an explicit reason at
decision time; today just went silent. OMER closed the gap further to **$17.35**
(+5.9% over the $16.39 premarket read that framed the entry, would already be
approaching the +15% target at $18.85 had it been entered). Per the spirit of the
missed-catalyst rule, **check OMER again tomorrow premarket** for a pullback or
continuation entry if the thesis (dilution structure, ladder) still holds.

**Position review**: 0 satellites open — nothing to hold/close.

**Core rebalance check**: slice $3,188.02 (live portfolio_value $10,626.74 × 30%),
satellite value $0, 10% buffer $318.80 → target_core $2,869.22. IWM (raw qty
**9.5031 sh**, per lesson 23) × $303.54 = **$2,884.57 — 0.50% of slice over target,
well within the 3% band.** No trade.

**Day P&L (hand-built, per lesson 22 — snapshot table mixes in Bull's P&L)**: no
satellite trades, IWM intraday unrealized **+$7.89 (+0.25% of slice)** vs **SPY
+0.69%** today — Rocket underperformed SPY today by ~0.44%, small-cap factor drag,
not a stock-picking loss (no picks were made). Since rebase (7/20): SPY **+4.82%**
(script-verified). Rocket hand-built, chained from 8/12's ~+4.65% base compounded
with today's core return: **≈+4.91%** → Rocket vs SPY **≈+0.09%** since rebase. Flag
per lesson 22: this chained figure carries rounding drift session to session: treat
as directional, reconcile precisely at the next weekly review.

**Also found**: lesson 25 — the weekly trade counter (`portfolio_snapshot.py`) shows
"0 / 3 max" despite VELO trading this week; the `—` split-count bug undercounts to
zero and the hardcoded cap (3) doesn't match CLAUDE.md's real 5/week guardrail.
Flagged, not fixed (script change out of scope for market_close).

---

## 2026-08-13 — PREMARKET (Thursday, Week 33)

**No trades — market closed. One P1 name: OMER, and it is a better-constructed setup than
VELO on every axis but float.** 7 web searches, done inline, no subagent (lesson 20).

**🥇 OMER (Omeros) — P1, HIGH.** Q2 after Wednesday's close on **YARTEMLEA**, its
first-in-class FDA-approved TA-TMA drug: revenue **$28.5M vs $12.67M consensus — a 125%
beat**; **product sales $32.2M in the first full launch quarter, +190% QoQ from $11.1M**;
adjusted EPS **+$0.02 against a −$0.25 estimate** (swing to profit); **+$4.1M operating cash
flow**; and **CMS granted NTAP reimbursement effective 10/01**. Premarket **$16.39 (+19.6%)**
vs a $13.71 close. The legs: **(a) ladder uncapped by ~2x** — every consensus reading found
($44.54 / $38.00 / $33.00) sits above the whole profit ladder, so +15% ($18.85) and +25%
($20.49) clear even the *lowest* one (lesson 11d, now 3-for-3); **(b) short float 19.7–24.2%
across three sources**, all >15% (lesson 9); **(c) the dilution structure is the best on any
Rocket P1 to date** — the 2026 converts **matured and were paid in full 2/15**, the remaining
9.50% notes are down to **$40.3M** and still being retired, ~**$132M cash**, and the company
is **actively buying back stock** ($100M authorisation, 0.5M sh bought in Q2 at $11.70).
**A live but undrawn $150M ATM is the named risk — mitigated because you don't ATM into a
buyback.** Tape is the biggest upgrade on VELO: four tight rising closes into the print
($13.25→$13.71) at the top of the weekly range, above MA50, and the **52-wk high is only
$17.65 — 7.7% overhead versus VELO's 96%**. Entry on the **9:45–9:50 base, not the open**
(VELO's spike-and-fade), do not chase above $17.75, stop $15.24, **29 sh = $475.31 (15.0%)**
— the cap binds, risk-based sizing allowed 41. Funding needs **~0.589 fractional IWM shares**.
⚠️ **Honest nuance**: Omeros did **not** formally raise guidance (launch-stage biotechs don't
guide), so this is a beat + forward reimbursement catalyst, not a literal beat-and-raise; the
+190% QoQ ramp is what replaces the raise. **The real bear case is Q3 sequential product
revenue** — $32.2M may include specialty-pharmacy stocking, and a sequential decline breaks
the thesis outright. Single-product concentration; $17.65 sits between entry and target one.

**🚨 HLIT — best headline on the board, killed by the capped ladder.** EPS **$0.24 vs $0.12**,
revenue **$173M vs $112.9M**, broadband **+54%**, **FY26 raised a second time** to $505–525M,
**backlog +71% to $587.6M**, video business divested = pure-play broadband. Premarket +23.3%.
**Then the ladder: the mean was raised only to $15.29 (from $12.71) against a $14.80 price —
+3.3%. Jefferies went $10 → $15 but KEPT A HOLD.** Both Rocket targets ($17.02, $18.50) sit
**above the entire fresh analyst complex** — the QNST/CRSR pattern exactly (lesson 11a/11c).
**Independent second knock**: the lesson-12 cap ceiling — 108.5M sh × $18.50 = **$2.007B**,
0.35% through the lid, the third name after APPS and BW. **Two rules, same answer** — and
worth noting the ceiling cost nothing here, since the ladder killed it anyway.

**⏳ CURI — real catalyst, not tradeable today.** Record Q2: **AI-licensing revenue +48% to
$14.1M** (880B-token code corpus), GM **53%→73%**, adj EBITDA **$11.4M (+300%)**, **outlook
raised** — a genuine beat-and-raise. But it **gapped +35.8%** ($2.80 → $3.80), which is
**second-day-only** under rule 2, and the **$2.80 base is a sub-$3 stock** (lesson 10) that
FAILS `eligibility` on last close. **Check Friday — valid only if it closes today above the
day's midpoint.** Also dropped: **MGNX / IPWR / INV** (all report *today*, and all were
running premarket *before* the print — exactly what the earnings-week rule exists to stop);
**SECZ** (−15%, a decliner); ten names moving +3–7% on 0.0–0.2x RelVol with no catalyst.

**Macro — the week's dominant risk is spent, benignly.** **CPI printed exactly in line:
headline +0.1%/3.4%, core +0.2%/2.5% — the coolest annual core since March 2021.** The
reaction matters more than the number: **the 10-yr did not move (4.68%)**, VIX fell through
15 to **14.63**, Brent extended −1.48%, and gold's 8-session run finally decelerated. The
4.75% trigger was tested by the biggest scheduled event of the week and never came into play.
**The event-driven "one satellite" restriction has lapsed as designed.** 🗓️ **PPI prints
today 8:30 ET** (forecast +0.2% vs −0.3%) — same favourable structure, resolves before the
open; **hot ≥~0.5% → no new satellite, hold the core.** IWM beat SPY a second straight session
(+0.57% vs +0.25%) — **logged as beta, not skill.**

**Account**: slice **$3,179.09**, **IWM 9.5031 sh = $2,882.39 (90.7%)**, 0 satellites,
notional cash **$296.70 (9.3%) — inside the buffer a fourth straight session**. Weekly count
1/5. No ntfy sent (no open position, no breaking news).

---

## 2026-08-12 — MARKET CLOSE (Wednesday, Week 33)

**VELO closed same day, −1.18%.** Entered $15.27 at the open on a genuinely strong
beat-and-raise (see premarket below), but the stock opened with a spike to $17.61 that
immediately round-tripped to $14.35, based at the $15.27 entry, popped to $15.83 by
10:45 ET, then faded on light volume all afternoon to close near $15.09 — bottom ~25%
of its post-entry range. Cancelled the trailing stop and closed discretionarily rather
than hold into a weak close; new lesson 4a (close-position-in-range applies to
same-day entries too, now 3-for-3 with ASPN/EVH).

**Core rebalance**: 0.79% of slice over target (IWM $2,876.68 vs $2,851.56 target) —
inside the 3% band, no trade.

**Day**: Rocket ≈+0.35% vs SPY +0.25% (beat by ~0.10%). Since rebase (7/20), hand-built
Rocket ≈+4.65% vs SPY +4.12% → **Rocket vs SPY ≈+0.53%**. Weekly trade count: 1/5
(VELO buy+sell counts as the week's one entry).

---

## 2026-08-12 — PREMARKET (Wednesday, Week 33) — CPI DAY

**No trades — market closed. One P1 name, VELO, and it is the best-constructed setup in weeks.**
7 web searches, done inline, no subagent (lesson 20).

**Yesterday's board fully resolved, and every skip was validated by the tape**: APEI closed
**$45.72 (−3.5%, 27% of range)** — the sub-consensus EPS guide knock written into its own P1
writeup is exactly what killed it. QNST closed **$20.90 (−5.1%, 35%)**, straight back through
the $22.40 consensus it had just reached — **lesson 11c is now 3-for-3**. FF stopped out
(−$12.24); its P2 knocks (no raise, no coverage) were the right knocks.

**🥇 VELO — P1, HIGH.** Q2 after Tuesday's close: revenue **$20.7M +52.3%**, GAAP gross margin
swung **−11.7% → +21.5%**, **FY26 guidance RAISED** to $65–75M, H2 GM guided >30%, positive
EBITDA projected H2, **backlog nearly doubled to $31M**. The three legs that matter all point
the same way: (a) **beat AND raise** — the only version that works per the standing theme;
(b) **uncapped ladder** — consensus **$23.75** (high $33) vs a $16.20 entry, so **both +15%
($18.63) and +25% ($20.25) sit below the mean**, with targets *rising* post-print;
(c) **short float >15% on a 13.8M float** — squeeze leg live (sources disagree, 18.6% of
shares out vs 35%+ of float; every reading clears the bar). Entry $16.20 on the 9:45 base,
**do not chase above $17.50**, stop $15.07, **29 sh = $469.80 (14.9%)**.
🚨 **Honest knock recorded**: a **live, undrawn $100M ATM** (S-3 effective 4/08, agreement
5/15) — an 18% gap is exactly when a company uses one. Also still GAAP-unprofitable, and the
6-mo high of $31.75 means this is a *recovery*, not clean-air breakout. Funding needs ~0.58
fractional IWM shares sold.

**🚨 NRGV — best headline on the board, killed by the balance sheet.** Revenue +104%, backlog
**~$2B**, a **1.25 GW AI data center** deal, FY26 guidance raised to $270–310M. Then: **$29.7M
GAAP loss in one quarter against $80.5M equity**, $150M converts, a $300M shelf, and an amended
debenture convertible into **33.25M shares at a VWAP-DISCOUNTED price** — holders paid to short
any pop. Added to the HARD AVOID list. **This produced new lesson 6a**: grade the dilution
*structure* and **date the raise** — VWAP-discounted converts (kill) ≠ drawn shelf (kill) ≠
undrawn ATM with runway (risk to size around) ≠ a completed raise months old (not an overhang).
That distinction is what separated NRGV's kill from VELO's pass; the same search returns both.

**Also dropped**: HYLN → watch-only (real $41.7M Navy ONR contract, but **EPS only in line**, an
active **Pelican Way short report** contesting its $133M LOI, 125M float, and NYSE American
listing); LENZ (beat-without-raise — product revenue just **+9% QoQ**, the SVCO pattern); JFB
(**no catalyst** despite being the only name on both scans with real RelVol — a 5.7M-float IPO
on unexplained volume is the manipulation profile); MGNX/TE (earnings-week bar).

**Macro — three of yesterday's four worries resolved favourably.** VIX 15.38 (no brake).
**Russell futures GREEN, breaking the two-session red streak** — and Tuesday inverted the drag:
**IWM +0.34% vs SPY −0.32%**. **10-yr backed off to 4.68%** (7bp from trigger, was 5bp).
**Brent got no second leg** ($88.74, −0.19%). Only gold still leans inflationary — 8 straight up
sessions, +2.16%. **The key structural point: CPI prints 8:30 ET, an hour BEFORE the open**, so
today's entries trade a *known* number rather than carrying it as day-2 risk. Consensus headline
+0.1% M/M / 3.4% Y/Y, core +0.2% / 2.5% Y/Y. **The "one satellite" restriction was event-driven
and lapses with the print — but confirm the actual number at 8:30 before sizing. A hot print
(≥~0.3% M/M) → no new satellite, hold the core, re-screen tomorrow.**

**Account**: slice **$3,162.74**, **IWM 9.5031 sh = $2,866.80 (90.6%)**, 0 satellites, notional
cash **$295.94 (9.4%) — inside the buffer a third straight session**. Weekly count 1/5. No ntfy
sent (no breaking news on an open position).

---

## 2026-08-11 — MARKET CLOSE (Tuesday, Week 33)

**FF stopped out mid-morning** (72 sh, $6.61 → $6.44, −2.57%, −$12.24) — clean stop
fill, one session, small loss. Zero satellites open into the close. **IWM core within
band** (0.29% of slice off target) — no rebalance trade. Day: Rocket ≈−0.10% vs SPY
−0.36% (+0.26% today, +0.52% since 7/20 rebase, hand-built per lesson 22). New lesson
23: `positions`/`portfolio_snapshot.py` round share counts for display (IWM showed
"10" vs actual 9.5031) — pull raw positions before rebalance math. ntfy sent,
confirmed. Full detail in `trade_log.md`.

## 2026-08-11 — PREMARKET (Tuesday, Week 33)

**No trades — market closed. Board fully rebuilt: Monday's entire watchlist is dead, and
three fresh names printed Q2 after Monday's close.** 5 web searches, done inline, no subagent.

**Monday's board was wiped out by the tape** — CRSR closed **8% of range (−4.5%)**, ARCT
**25% (−4.9%)**. The lesson-11c capped-ladder call on CRSR was right in real time. QNST is
the only survivor (new 52-wk high, 83% of range) but spot **$22.02 has now reached the $22.40
consensus** — the cap problem is worse, so it stays a watch, not a position.

**New board (all three reported AFTER Monday's close, so today is their day one):**
1. 🥇 **APEI — P1, HIGH.** EPS **$0.52 vs $0.36** (+44% beat), revenue $171.7M, adj EBITDA
   +36.8%, **FY26 guidance raised on all four metrics**. Net cash, GAAP profitable, **float
   just 13.87M**. The differentiator: **its profit ladder fits *under* the street's targets**
   (+15% = $61.53 vs a $62.17 mean; +25% = $66.88 vs a $68 high) — the exact inverse of QNST
   and CRSR, which both stalled on capped ladders. Entry $53.50 on the 9:45 base, stop
   $49.76, **8 sh = $428**. Honest knock recorded: the raised FY EPS guide ($2.48–2.79) still
   lands **below** the $2.93 street consensus.
2. 🥈 **FF — P2, MEDIUM.** Revenue **+120.6%**, swing to **+$11.4M GAAP net income**,
   **zero total debt**, opening ~15% above its 52-wk high with no overhead supply. Held to P2
   because there is **no raise** (soft "positive adj EBITDA" guide), no analyst coverage, and
   biofuel is credit-timing-driven. 76 sh = $471.
3. ❌ **BW — the best catalyst on the board, excluded by the universe ceiling.** Revenue +130%,
   **backlog +533%**, +34.9% premarket, analyst mean $24.67 vs $11.98. But 148.8M sh × $11.98
   = $1.78B, so **even the +15% target implies $2.05B — outside the $2B cap** (lesson 12).
   Not traded. **Second time in two weeks the ceiling killed the best name (after APPS) —
   flagged for `weekly_review`, not overridden today.**
4. ❌ **HZO resolved and permanently skipped** — Monday's +45.8% was an **all-cash $53.00
   Blackstone/Safe Harbor buyout**, price pinned at a 1.7% arb spread. Rule 2's second-day
   entry does not apply to merger arb. Closes yesterday's open item.

**Process wins worth keeping**: (a) **lesson 13 paid again** — APEI's ADV came back a FAIL at
298,467, and raw bars put the 3-mo at **300,406 (pass)** and 1-mo at 362,200; re-verifying the
borderline gate saved the P1 name. (b) **lesson 16 paid again** — the scanner's prices were
premarket quotes and its `Change %` was premarket-vs-close; every number was re-derived from
raw daily bars, which is what revealed BW/FF/APEI as after-close prints rather than Monday
movers.

**Macro**: VIX 15.53 (no brake). **10-yr 4.70%, now 5bp from the 4.75% trigger.** Russell
futures red a **second** straight session — that trigger has fired, and Monday delivered
**IWM −0.52% vs SPY −0.03%**. **Brent +6.2% in one session to $89.60**, 24h before CPI.
**CPI is tomorrow 8:30 ET** — anything entered today is open through it on **day 2**, so the
standing call is **one satellite, not two**, first third taken promptly at +15%.

**Account**: slice $3,164.68, **IWM 9.5031 sh ≈ $2,851 (90.1%)**, 0 satellites, notional cash
**$314 (9.9%) — inside the 10% buffer for the first time in nine sessions**, closing the
lesson-15 verification loop. A full-size satellite needs ~0.39 sh of fractional IWM sold to
fund it. No ntfy sent (no breaking news on an open position).

---

## 2026-08-10 — MARKET CLOSE (Monday, Week 33)

**0 satellites open — nothing to review.** Only Rocket holding is the IWM core (9 sh
entering the session). No positions to hold/close decisions today.

**Core rebalance**: slice $3,164.97, target_core $2,848.47 (10% buffer $316.50). IWM
9 sh @ $299.74 = $2,697.66 — **4.77% short, outside the 3% band.** Bought fractional
**0.5031 sh @ $299.74** ($150.81 notional). Filled ~19:58 UTC; position now **9.5031
sh, mkt value $2,848.65** — within $0.18 of target. First rebalance since the
fractional-order fix (lesson 15/18) to close the band exactly rather than stall on a
whole-share remainder — confirms the fix works live.

**Day P&L**: Rocket's book (≈ slice) **+0.39%** ($3,152.62 Fri close → $3,164.97) vs
**SPY −0.07%** today. Since rebase (7/20): Rocket **+4.40%** vs SPY **+4.12%**
(**+0.28%**), chained from the 8/07 weekly-review baseline (lesson 22 caveat: hand-
built proxy, not `portfolio_snapshot.py`'s figure, though they currently agree since
Rocket is 100% IWM with no satellites live).

**No satellite trades today** — market_open found all three ranked ideas (CRSR, QNST,
ARCT — see below) failed at decision time; no second-day candidates worked either.
ntfy daily summary sent and confirmed.

---

## 2026-08-10 — MARKET OPEN (Monday, Week 33)

**No trades. All three ranked ideas failed at decision time; three fresh movers lacked a
confirmed catalyst.** Checks done inline (3 web searches + 2 scanner re-pulls), no subagent.

- **CRSR (P1) — the flagged open check resolved NO-GO, and price confirmed it.** Real
  post-print analyst raises exist (Baird $12, Craig-Hallum $12, Wedbush $13, Roth $16) — not
  stale as hoped, but the resulting $12–16 spread means spot ($13.98) is already above 3 of 4
  targets. Same "no upside leg" signature that demoted QNST last week (lesson 11a), now seen
  twice — logged as lesson 11c. Opened **-2.6% on 0.1x avg volume**, a red/thin fade rather
  than a base. **Not entered.**
- **QNST (P2)** confirmed real strength — **+4.9%, new 52-wk high** — but the pre-registered
  cap-check verdict (own +15% target sits above the street high) doesn't change on a green
  tape alone. Held to its own plan: **watch, not traded.**
- **ARCT (P3)** opened **-2.4%** on thin volume — weakest catalyst on the board, no confirmation. Skipped.
- **Fresh movers**: **HZO** (+45.8%, 104.8x RelVol) is a >35% gap, second-day-only per rule 2
  — watchlist for tomorrow. **MVIS** (+22.1%) had no dated catalyst for today (stale 7/15
  print + a reverse split, itself a mild red flag) — classic pump-prone name, skipped per
  lesson 1. **TNXP** (+12.1%, 5.7x RelVol) reports today but results weren't out yet at
  check time — pre-print move, barred by the earnings-week rule.

**Account unchanged**: slice $3,155.56, IWM 9 sh ($2,707, ~85.8%), 0 satellites, pooled cash
$719.86. No overnight fills or stops. No ntfy sent (flat session).

---

## 2026-08-10 — PREMARKET (Monday, Week 33)

**No trades — market closed. Watchlist rebuilt; Friday's two open checks closed and both
flipped the ranking.**

**The overnight scan produced nothing.** Screeners returned only thin-RelVol extended-hours
quotes (STI +14.7% — standing hard-avoid; NMAD/AMPG/INGN — no catalyst). **Every idea on
the board is a Friday carry-over.** Correctly did not manufacture a new name to fill a slot.

**Both open checks resolved — and the ranking inverted:**
1. ⬆️ **CRSR P2 → P1.** Dilution check came back **clean and then some**: $192.2M cash vs
   $118.3M debt = **~$75M net cash**, GAAP net income **+$9.1M**, operating cash flow **+148%
   to $74.8M**. It does not need the equity market. Then the bigger find — **short float
   21.94%, above the 15% squeeze bar, which Friday's board never checked at all** (lesson 9
   is live). With a 47.4M float (44% of shares out) and a 92%-of-range close, it has the best
   structure on the board.
2. ⬇️ **QNST P1 → P2, on its own pre-registered rule.** Friday's bar was *"if consensus has
   not been raised above ~$24, the upside leg is missing."* Revisions **did** land — four
   raises on 8/07, all Buy — but consensus is only **$22.40 with a street high of $24.00**
   against a $21.08 close. **Rocket's +15% first scale-out ($24.24) sits above every price
   target on the street.** Balance sheet is still the cleanest on the board, so it's a smaller
   trade, not a skip — but the rule was written in advance and was not rationalised away.
3. 🆕 **ARCT promoted to P3** off the secondary board: $191.5M cash / 2.5-yr runway is clean
   for clinical-stage, and **short float 30.65% on a 26.0M float** is the most explosive
   structure available. Held back to P3 because the catalyst is a rights-reversion from CSL,
   not a beat-and-raise, and **revenue collapsed to $2.96M from $28.3M YoY**.

**A search nearly misled the QNST call.** A "Barrington raised PT to $29" headline surfaced
with no date; verifying against the current consensus page showed Barrington **reiterating
$24 on 8/07** — the $29 was a prior period. Taking that at face value would have kept QNST
at P1 on a fabricated upside leg.

**Dropped with reasons**: PUBM (52% range close, −1.0% pre — fade confirmed), EMBC, OABI
(2.7% off the $3 floor, 4.45% short float — no edge), TBCH (**no catalyst ever identified**),
GTN (**retired** — cap gate still `unknown`, an unchecked gate is not a pass), RCEL (standing
avoid; **−4.0% premarket is validating the skip in real time**).

**Macro — two things changed.** 🚨 **Russell futures flipped to −0.27%** after Friday's
+1.04%; they are the only red future while S&P/Nasdaq are green, so small-cap leadership did
not survive the weekend. Notably **CRSR and QNST both held their gaps flat overnight anyway**
— name-specific strength intact while the group softens. 🗓️ **CPI lands Wednesday 8:30 ET**,
so anything bought today is open through it with the 10-yr just 9bp under the 4.75% trigger.
**Argues for one satellite today, not two, and taking the first third promptly.**

**Open for market_open**: (a) verify **CRSR post-print PT revisions** — consensus reads
$12.33, below spot, almost certainly stale, and lesson 6 says an unresolved check is a to-do;
(b) re-derive the **lesson-18 cap check at the actual fill** — a CRSR fill above **~$14.79**
puts the +25% target outside $2B; (c) confirm the base on **raw 5-min bars**, not the scanner.

**Funding**: only ONE full-size satellite (~$459–467) is fundable from ~$444 notional cash —
**fund it by selling a fractional IWM slice**, satellites stay whole-share. If no entry
happens, `market_close` must still top the core up fractionally. **Either path finally
exercises the fractional fix, which has never run against a live order** (lesson 15).

---

## 2026-08-07 — WEEKLY REVIEW (Week 32, Friday post-close)

**Grade: C.** Rocket vs SPY **−0.54%** for the week (+2.97% vs +3.51%). One satellite
closed (CSTL, −$0.75, −0.17%, −0.02R) — a scratch, well executed. **Real alpha −0.13%.**

**The finding: this was an infrastructure week, not an analysis week.** Attribution splits
to factor **+0.04%** (IWM − SPY was only +0.05% — the usual drag excuse was unavailable),
cash drag **−0.49%**, satellite **−0.13%**. Nearly all of the miss was idle cash.

**Two root causes found and FIXED today:**
1. **Fractional orders** (`alpaca_client.py`). IWM at ~$300 vs a ~$3,150 slice makes one
   share 9.6% of the book against a 3% band — unsatisfiable, so ~14% sat in cash every
   session for eight sessions. `buy`/`sell` now take fractional qty; trailing stops reject
   it loudly (satellites stay whole-share). **Untested against a live order — Monday's
   market_close must run the first fractional top-up and verify the fill.**
2. **Scanner `Change` column** (`smallcap_scanner.py`). Finviz renamed the header
   `Change` → `Change %`; the code read the old key and `_safe_float("")` returned 0.0.
   Five sessions of `+0.0%` on every row. Fixed and verified live. **This also retires the
   over-broad half of lesson 16 — the scanner's prices were fine all along.**

**Two defects still open:**
3. 🔴 **Midday has not run since 2026-06-15** — plist is valid and on disk but absent from
   `launchctl list`; last log ends in a 429. Cost visibility on CSTL's 2:32 PM stop fill.
   **Deliberately NOT reloaded — escalated to the user**, because a 5th Rocket job competes
   for the shared Claude quota with premarket/market_open (lesson 20).
4. 🔴 **NEW — Rocket cannot measure its own return.** `portfolio_snapshot.py` derives it
   from a fixed 30% of the *shared* account, which is algebraically the whole account's
   return — Bull's P&L included, and Bull holds 5 of 6 positions. Reported −0.25% vs SPY;
   real figure −0.54%. **Priority 1 for Week 33.**

**Skips were right, with one nuance.** ASPN, EVH, NNBR, MRAM, SVCO, CVRX, STLN, FIGS and
REPL all faded or died. **QNST** was the one questionable pass — skipped at $20.21 partly
on a *pre-print* $19.00 analyst target, then closed $21.08 at 91% of range. **RCEL** was
rejected on a stale 295k ADV reading (real: 302,064, it passes) and ran +63.6% — but it
carries an active $200M shelf with <1yr runway, so the skip was right for a reason Rocket
never reached. Right outcome, wrong gate.

**Memory trimmed**: session_notes 661→~230, research_log 239→~155, market_context 217→81,
lessons_learned 113→56.

**Week 33 board**: P1 **QNST** (rule-3 continuation, GAAP profitable, zero dilution risk,
cap headroom fine — but verify post-print PT revisions). P2 **CRSR** (record margins, low
float, but revenue −2% YoY and the +25% target is only ~4% inside the $2B ceiling; dilution
check not yet run). **RCEL → standing avoid list.**

---

## 2026-08-07 — MARKET CLOSE (Friday)

**No trades.** 0 satellites open, nothing to review. Core rebalance checked and
skipped: IWM 9 sh is 3.91% short of target_core (share-granularity remainder per
lesson 7a — buying 1 sh would overshoot to 5.66% over, worse than doing nothing).

**Day P&L**: book +1.51% ($3,105.58 → $3,152.62) vs SPY +0.66% — IWM itself +1.13%,
small caps outperforming large caps today. Since rebase: Rocket +3.99% vs SPY
+4.20% (-0.21%).

**Week summary**: 1 trade this week (CSTL stop-out 8/06, not a decision), 0 new
entries — QNST and STLN both had real catalysts but failed at entry gates (extension/
target exhausted, confirmed dilution risk). No satellites open into the weekend.

---

## 2026-08-07 — MARKET OPEN (Friday)

**No trades. Both ranked ideas failed at decision time; no fresh mover had a confirmed
catalyst.** Checks done inline (1 web search + raw 5-min bars), no subagent.

- **QNST (P1)** ran from premarket +22.6% to **+32.8% ($20.21) by 9:45**, tapping an
  intraday high of **$20.50 (+34.8%)** in the opening 5-min bar — a hair under the **$20.55
  (35%) extension gate**, with essentially no room left. Worse, **spot is now above the
  $19.00 mean analyst target** with no revision confirmed — the exact "no upside leg"
  problem flagged in the premarket note, now realized rather than hypothetical. Base
  structure itself was fine (higher lows $19.22→$19.74→$20.02, volume already ~0.7x full-day
  average in 15 minutes), but risk/reward is broken: capped upside, full stop-out downside.
  **Passed.**
- **STLN (P2)** held up better technically — **+28.3% ($6.40), 5% under its $6.74 gate**,
  higher lows ($6.02→$6.27→$6.40), volume already ~1.0x full-day average in 15 minutes,
  analyst target $8.40 still +31% above spot. **But the dilution flag the premarket note
  left unverified (SEC 403'd) is now CONFIRMED**: one search found an active **$15M ATM
  facility** (424B5) — live authorization to sell stock into exactly this kind of spike, on
  a company with a **0.1% EBITDA margin and only $41.1M cash**. Same pattern that killed
  SOC and SVCO this month. **Passed** — the dilution check did its job a second time.
- **Fresh movers** (`unusual_volume`/`top_movers`): BZH, XPOF, PUBM, INVX, NRXP, FNKO,
  ARDX, SERV, LZ, CRSR, SSP, EMBC, TALK, INGN, BETR, WHWK, PBYI — none carried a validated
  catalyst from premarket screening, and chasing any of them fresh would mean 5+ new
  searches on unvetted names late in the entry window. Declined per rule 1 (no catalyst,
  no trade) rather than force a trade to avoid a flat session.

**Account unchanged**: slice $3,142.77, IWM 9 sh ($2,707, 86.1%), notional cash 13.9% —
still outside the 10% buffer (the same share-granularity remainder flagged premarket), but
no satellite qualified so no funding trade was triggered. No overnight fills or stops. No
ntfy sent (flat session).

---

## 2026-08-07 — PREMARKET (Friday)

**Ran on time at 6:20 AM ET. No subagents; 8 inline searches + 3 fetches** — lesson-12
budget discipline held for the fifth session running.

**Account**: shared $10,435.72 / slice $3,130.72 / **IWM 9 sh $2,691 (85.9%), 0 satellites**.
✅ Reconciler balances. Satellites 0/4, trades 1/5. Max satellite $469.61, 1.5% risk $46.96.
⚠️ Notional cash **$439.72 = 14.0%, outside the buffer** (share-granularity remainder) —
**any full-size entry must sell 1 IWM first**, which also cures the breach. Rocket vs SPY
improved to **−0.30%** from −1.15% as IWM recovered and CSTL stopped dragging.

🚨 **BOTH SCANNERS WERE OUTRIGHT BROKEN — every row returned `+0.0%`**, so `top_movers` was
a ranked list of zeros and the overlap tier produced nothing for a fourth straight session.
Several scanner *prices* were also wrong vs raw bars (STLN $6.67 vs a $4.99 close; CVRX
$3.41 vs $5.94). **The whole board came from raw yfinance daily bars on carry-overs plus the
live premarket gainers page.** Logged as lesson 16.

**Watchlist built (4 ranked, from 6 fresh prints screened):**
- **P1 QNST (HIGH)** — QuinStreet Q4 FY26 (8/06 post-close): revenue **$373.9M +43%, above
  the top of its own $350–370M guide**; adj EBITDA $41.4M **+87%**; **GAAP EPS $0.33**; FY26
  op cash flow **$130.9M**; **FY27 guided to $1.45–1.55B / $150–160M EBITDA (+33–42%)**.
  Premarket **+22.6% to $18.66 — inside the 20–35% gap-and-go band**, 35% gate $20.55.
  $874M cap, **$2B ceiling ~87% away**. Short float 11.34%, 6.48 DTC. ✅ **Chosen P1 mainly
  because it is GAAP profitable with real cash flow — dilution risk is absent by
  construction**, and dilution killed three of this week's ideas.
- **P2 STLN (MED-HIGH)** — Starling Oncology (renamed from TOI 8/04) Q2: revenue **$161.3M
  +34.6%**, gross profit **+55.2%**, **adj EBITDA positive for the first time**, **FY26
  raised to $650–670M**. Best upside math on the board — **blue sky 24.6% above its 52-wk
  high**, mean target **$8.40 (+26.7%)**. 🚨 Capped at P2: **0.1% EBITDA margin on $41.1M
  cash** = live dilution risk, **unverified** (SEC 403'd the 8-K). And **its 35% gate is
  $6.74 vs a $6.63 premarket print — 1.7% of room, the likeliest disqualification today.**
- **P3 APPS (WATCH)** — closed **$14.27 +8.4% at 96% of range**, new 52-wk high, Craig-Hallum
  PT $10→$18. **Cannot be traded**: $1,727M cap puts the $2B ejection ceiling at ~$16.55, so
  the +25% target is outside the universe. Day 3, +50% off the base. Pullback only.
- **P4 HNST (MED-LOW)** — valid rule-3 second-day (closed above midpoint, zone ceiling
  $5.96), but revenue −10.9% and **mean target $4.81 is BELOW the $5.42 close** (AMCX
  signature). Fallback only.

**Eliminated**: **RCEL/VATE/FRD/SRZN** — four premarket gappers of +17–34%, **all fail the
300k ADV gate, killed in one `eligibility` call with zero searches**. **FIGS** out of
universe at its premarket price ($1,878M cap → ~$2.38B at $14.25). **SVCO** revenue missed
consensus and **Q3 guided BELOW the quarter just delivered** + undisclosed Micron
convertible. **CVRX guidance CUT**. **ASPN** failed rule 3 — closed at **28% of range** on
13.3x volume (distribution). **EVH** closed at 9% of range. **NNBR** PIPE thesis played out
exactly as written. **REPL** — **FDA approved RP1 (TUDRIQEV) 8/06**, but priced in by the
AdCom and **barred by earnings 8/11**; binary closed, removed from rotation.

**Macro**: 🚨 **NFP 8:30 AM ET** — fcst ~80–120k vs 57k prior, U3 4.2%, AHE +3.5%. Pre-open,
so the 9:45–9:50 base window is clean, but it is the month's biggest whipsaw. **VIX 15.28**
(clear). 🚨 **10-yr 4.67% (+1.15%) — the rates tailwind reversed after exactly one session**;
**IWM −0.51% vs SPY −0.16%** again. Gold $4,373 (+3.09%), 4th straight up session with VIX
low = rate-cut positioning, not fear. Energy dead (Brent $82.14).

**Open threads**: (1) **STLN dilution check unrun** — close before any order; (2) **FTK cap
gate `unknown` a 4th session** — verify or retire; (3) scanner numeric columns broken.

**No trades placed — market closed. No ntfy sent (no breaking news on a held position).**

---

## 2026-08-06 — MARKET CLOSE (Thursday)

**CSTL stopped out intraday (2:32 PM ET), discovered at EOD sync — not a market_close
decision.** Trailing 7% stop off the $31.73 high-water mark filled at $29.94 vs $29.99
entry: -$0.75 (-0.17%), essentially breakeven. Catalyst was never invalidated; this is
just the trail giving back the post-earnings pop. **0/4 satellites open now.**

**Core rebalance**: CSTL's proceeds returned to cash, not core, opening a 13.1%-of-slice
gap vs target. Bought **1 sh IWM @ $298.27** (closest whole-share fit to the $408 gap;
2 shares would have overshot further). IWM now **9 sh ≈ $2,684**. Residual ~3.6%-of-slice
gap is a share-granularity remainder, not an actionable miss — flagged for premarket to
watch, not re-traded today.

**Day P&L**: Rocket's total book **-0.68%** ($3,126.82 → $3,105.58) vs **SPY -0.15%** —
the CSTL stop-out (-1.38% intraday) drove the gap. Since rebase: Rocket +2.44% vs SPY
+3.59% (**-1.15%**, widest yet).

No midday session ran today; market_open found all three ranked ideas disqualified (see
below). ntfy summary sent for today's close.

---

## 2026-08-06 — MARKET OPEN (Thursday)

**No trades. All three ranked ideas failed confirmation at 9:45 AM ET; two fresh movers
were too extended to enter same-day.** Checks done inline (2 web searches), no subagent.

- **MRAM** flipped from premarket +8.4% to **-7.3% at $16.14** on 1.5x volume, now below
  its MA50 — a broken base with confirming volume, not just weak confirmation. Removed
  from active watch.
- **APPS** -4.6% to $12.57 on only **0.2x avg volume** — nowhere near the 1.5x bar, no
  confirmed base either direction.
- **NNBR** +6.8% to $4.16 but also only **0.7x avg volume**; already capped MEDIUM on the
  PIPE overhang, so this was the fallback and it didn't confirm either.
- **Fresh finds**: **HNST** (catalyst-validated, 8/05 EPS beat) is +50.3% today on 2.5x
  volume — 29.6% past its own second-day entry zone ceiling, too extended. **ASPN**
  reported a genuine beat-and-raise this morning (Q3 guided $65-80M vs $49.8M delivered)
  but is +54.3% same-day, over the 35% ceiling. Both watchlisted for a second-day/pullback
  check tomorrow, neither enterable today per Rule 2.

**Account unchanged**: slice $3,105.89, IWM 8 sh ($2,396) + CSTL 15 sh ($453) = 91.8%
invested, notional cash 8.2% — inside the buffer, no funding action needed since nothing
qualified. No overnight fills or stops triggered. No ntfy sent (flat session).

---

## 2026-08-06 — PREMARKET (Thursday)

**Ran on time at 6:20 AM ET. No subagents; 8 inline searches + 1 fetch (timed out)** —
lesson-12 budget discipline held for the fourth session running.

**Account**: shared $10,380.36 / slice $3,114.11 / IWM 8 sh $2,404 (77.2%) + CSTL 15 sh
$456 (14.6%) = **91.8% invested, cash 8.2%** — inside the 10% buffer a third straight
session. ✅ **Reconciler balances and yesterday's unattributed NOW (12 sh, $1,369) is
resolved to Bull.** Satellites 1/4, trades 1/5. Max satellite $467, 1.5% risk $47.

**Watchlist built (5 ranked):**
- **P1 MRAM (HIGH)** — Everspin's **highest-revenue quarter ever**: $18.7M **+42% YoY**,
  **13% above the top of its own guide**; non-GAAP EPS $0.11 vs $0.00–0.03 guided (~4x);
  **Q3 guided UP to $19.5–20.5M**. Driven by the $40M US prime-contractor deal converting
  to revenue. Best structure on the board — **18.7M float, 16.53% short float (squeeze bar
  cleared), $378M cap (no ceiling risk), 3.37M ADV**. +8.4% = below the 20% band, so
  conventional base, not gap-and-go. ⚠️ **The muted reaction is the open question** — +8.4%
  merely round-trips yesterday's −7.3%. Volume at 9:45 separates opportunity from tell.
- **P2 APPS (MED-HIGH)** — second-day continuation, and **rule 3 fits cleanly for the first
  time this week**: gapped +38.5%, closed above the midpoint (58% of range) on 3.5x ADV,
  premarket $13.06 **inside** the 10% zone (ceiling $14.49). Catalyst + dilution already
  validated 8/05. No squeeze (109M float); yesterday's high $14.10 is also the 52-wk high.
- **P3 NNBR (MED)** — real beat-and-raise (+19.3% sales, +36.1% EBITDA, FY raised) plus a
  $12–15M firearms contract and a $50M+ datacenter pipeline. 🚨 **Dilution demoted it:** the
  "$124M deleveraging" is funded by a **$75M PIPE at $3.06 (~24.5M sh vs a 31.1M float)** —
  BLZE again, headline and overhang are the same transaction.
- **P4 HNST (MED-LOW)** — 100% EPS beat + raised FY + buyback, but **revenue −10.9% YoY**;
  a margin story, not a growth story. **P5 FTK** — best close on the board (72% of range,
  4.3x ADV) and best squeeze math, but the **market-cap gate has returned `unknown` for a
  third session** and energy is still dead. Not tradeable until verified.

**Eliminated**: **GCT** — best print screened all week (revenue $411.6M +27.6%, EPS $1.16,
19.87% short float) but it is a **Cayman holdco operating through mainland-China
subsidiaries → fails the US-domicile gate**; added to the standing avoid list so it is not
re-screened on catalyst quality. **AEVA** — $115M follow-on offering, $79.6M quarterly loss
on $6.1M revenue, deployment 2H2027, CFO exiting. **ASYS** — reaction already failed
(closed −8.2% at 3% of range). EVH/SPIR/LENZ barred by the earnings-week rule.

**Theme**: earnings are the whole board a third session, but **the new theme is DEFENSE** —
MRAM and NNBR both printed on defense revenue the same night. Rocket's best-ever trade
(MRLN) was a defense catalyst.

**Process flags**: (1) ✅ **the entry window is clean today** — all data is pre-open, the
first uncontaminated 9:45 base window this week; (2) 🚨 **the both-list scanner overlap
produced one worthless name (HDSN, +3.4% at 0.1x) for the third session running** and would
have missed the entire watchlist — every idea came from `unusual_volume` or carry-over
second-day watch; (3) **Rocket can fund exactly ONE satellite** and any entry requires
selling 1 IWM first; (4) **NFP tomorrow** — do not carry a marginal name into it.

**Performance**: Rocket **+2.72%** since rebase vs SPY **+3.73%** → **−1.01%**, wider than
yesterday's −0.76%. IWM −0.64% vs SPY −0.20% yesterday: the gap is the IWM factor drag, not
stock selection. No trades placed (market closed). No ntfy sent — no breaking news on CSTL.

---


---

## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
