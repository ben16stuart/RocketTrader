# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-22 Tuesday premarket (Week 39 day 2 — **floor breached, MEDIUM bar active**)  ← CURRENT

All "last close" figures are **Monday 2026-09-21's settled closes**.

| Metric | Level | Read |
|---|---|---|
| **VIX** | **14.80** (**−0.47%**) | ✅ **Well below the 22 brake — no size restriction, and a NEW low for this table.** 16.04 → 15.36 → 14.87 → **14.80.** The post-FOMC vol crush is now three weeks old and still grinding lower. ⚠️ **A low VIX is the absence of an event, not a bullish signal** |
| **10-yr** | **4.96%** (**−0.70%**) | 🚨 **Still ~21bp THROUGH the 4.75% trigger — but the run has now rolled over: 5.01 → 4.95 → 5.00 → 4.96.** Lesson 34 governs and cuts **both** ways: two down-prints in four sessions is a wobble, not a resolution, and the flag stands. **But it is no longer making new highs, which is the first genuine change in this signal in three weeks** |
| **FUTURES** | **ES +0.08% · NQ +0.17% · RTY +0.49%** | ⚠️ **Flat-to-mildly-positive overall — but read the ORDER.** 🥇 **RTY is the STRONGEST of the three for the first time in weeks**, after being the weakest or mid-pack in five of the last seven sessions. **Lesson 28: one session carries no information. Flagged, NOT booked** — this exact read has reversed sign repeatedly |
| **WTI roll** | **🔄 ROLLED → CLX26.NYM** | 🚨 **The patch fired again: naive −6.60% → true −3.15%.** Unpatched, this table would have reported crude down 6.6% on a calendar spread. **Sixth session the roll patch has done real work** (lesson 50) |
| **Brent / WTI** | **97.76 (−2.57%)** / **89.46 (−3.15%)** | 🚨 **Crude is breaking down, and this is the clearest trend on the board.** WTI **through $90** for the first time in this file's history; Brent under $98. Both legs now ~15–18% off their highs. ✅ Spread ordering normal (Brent above WTI) though wide at ~$8.3 |
| **SPY / IWM** | **773.50 (+1.55%)** / **285.58 (+0.52%)** | Monday's settled closes. Both reconcile exactly against Friday (761.69 → 773.50 ✓; 284.10 → 285.58 ✓) |
| Gold / Dollar | 4,371.00 (−0.29%) / 100.35 (−0.08%) | Both essentially flat; dollar holding above 100, gold easing off its run high. Cross-check cleanly |

### 🚨 The cost of the floor breach is now measurable, and the old "factor watch" framing is obsolete

**Stop reporting IWM-vs-SPY as a drag on Rocket. Since 2026-09-17 the benchmark IS IWM**, so
the core contributes **exactly zero excess return by construction** — SPY's outperformance is
no longer Rocket's problem in any measured sense.

🥇 **What replaces it is sharper and it is the satellite floor.** Rocket holds **~49.6% IWM and
~50% idle cash against a 100% IWM benchmark.** So the arithmetic of the breach is simply:
**every 1% IWM gains costs Rocket ≈0.5% of relative performance.** Monday IWM closed
**+0.52% → the idle cash cost ≈ −0.26% vs benchmark, in a single session.**

**That is the honest price of the research gap, and it is not a market call** — there is no
bearish thesis on file and none applies. **It is a stock-picking gap being paid for daily.**

### The tape is permissive — rule 29 blocks nothing

VIX at a multi-week low, futures mildly green with the Russell leading, crude falling hard,
the 10-yr off its highs. **There is no macro reason not to trade today.** Today's zero-entry
is therefore a **supply/measurement** result, not a calendar one — see the research log.
📌 **One forward item: MLKN reports BMO today**, the session's only live candidate.

### Instrument health

🚨 🥇 **THE FINDING OF THE SESSION — LESSON 55b PASSED 8-FOR-8 AND THE BOARD WAS STILL
FICTION. New lesson 59.** Every `top_movers` row reconciled exactly under 55b's arithmetic
check (EVMN 10.13/9.45 ✓, BBW 26.03/24.75 ✓, FBRT 8.18/7.71 ✓, GOSS ✓, QUIK ✓, SIGA ✓,
ACCO ✓, QTRX ✓). **Then the actual tape: six of the eight had ZERO premarket trades**,
EVMN's "+7.2%" is a **single 202-share print (306 shares / $3,081 all session)**, and **BBW —
printed at $26.03/+5.2% — actually traded 500 shares at $24.74, −0.0%.** 55b validates the
scanner's *arithmetic*, never the *liquidity behind the numerator*.
🚨 **AND THE CHECK ITSELF NEARLY FAILED ON A BROKEN FEED.** Alpaca's **`iex` feed returns
ZERO premarket bars even for SPY, AAPL and IWM.** Had the control not been run (lesson 38),
"zero volume everywhere" would have been written up as a finding when it was the wrong feed.
**`sip` is the only usable premarket feed; `iex` silently returns an empty, plausible blank.**
✅ **`macro` populated every field for an 18th straight session**; roll patch corrected WTI.
⚠️ **`unusual_volume` RelVol unusable for a SIXTH straight session — 19 of 20 rows below
1.0×**, its only >1.0× row (USDE 2.5×) a standing mandate kill. `breakouts` **errored on the
Finviz query** and returned 3 rows. `top_movers` gave 11 of 20 rows `—` or `0.0x`.
✅ **`eligibility`: 8 requested → 8 returned, twice** (lesson 43 count held, full output).
⚠️ **EDGAR's ticker lookup resolved `CURR` to Avenir Wellness Solutions (DE) — the wrong
company.** Currenc Group is a separate issuer. **Flagged and the name dropped on rule 38**,
not scored. A ticker-to-CIK lookup is not authoritative; verify the returned `name`.
📌 **Nasdaq earnings calendar: 8 reporters 9/21 + 19 for 9/22 = 27 screened, ONE survivor
(MLKN)** — and it came from the calendar, not from any screener. Lesson 41d tally now **4-for-8.**

---

## Snapshot — 2026-09-18 Friday premarket (Week 38 day 5 — **1 breach recorded; today's close would be #2**)

All "last close" figures are **Thursday 2026-09-17's settled closes**.

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.36** (**−0.52%**) | ✅ **Well below the 22 brake — no size restriction.** 17.71 → 16.04 → **15.36.** The post-FOMC vol crush is holding and extending, now at the lowest level on this table in weeks |
| 🥇 **10-yr** | **4.95%** (**−1.18%**) | 🚨 **THIRTEENTH consecutive session above the 4.75% trigger — but the FIRST DECLINE of the entire run** (4.94 → 4.97 → 4.96 → 5.00 → 5.01 → **4.95**). ⚠️ **Lesson 34 governs exactly here: flags near a threshold stand down on a TREND, never on one print.** One down-tick off a run high after twelve up-sessions is **not** a resolution. **Still flagged, not cleared** |
| **FUTURES** | **ES +0.13% · NQ +0.37% · RTY −0.06%** | ⚠️ **Flat-to-mildly-positive — the relief tape has stalled.** 🚨 **The roll patch fired on FIVE rows** (ES/NQ/RTY → Z26, Brent → BZZ26, **WTI → CLX26**) **and produced a SIGN FLIP on the Russell: naive +0.67% → true −0.06%.** Also ES +1.01%→+0.13%, NQ +1.38%→+0.37%, Brent −5.87%→−1.26%, WTI −5.56%→−1.02%. **Unpatched, this table would have read "small caps up 0.67%" on a tape where they are flat-to-down** — fourth consecutive session the patch has done real work (lesson 50) |
| **Russell vs the others** | **RTY −0.06%, the WEAKEST of the three** | Small caps lag again, and are the only negative equity row. **Lesson 28: one session carries no information** — and this specific read has now reversed sign in five of the last seven sessions. **Flagged, not booked** |
| 🚨 **SPY / IWM** | **762.60 (+1.13%)** / **285.43 (+0.53%)** | Thursday's settled closes. 🚨 **Factor −0.60% AGAINST Rocket** — the widest adverse single-session factor gap in over a week, and it lands on the session Rocket's core was cut to 50%. ✅ **Silver lining that is worth stating plainly: at the NEW 50% core weight that is ≈ −0.30% on the book, not −0.56%. The IWM cap halved the damage from an adverse factor day** — the first concrete benefit of the 9/17 rule change |
| **Brent / WTI** | **98.67 (−1.26%)** / **96.24 (−1.02%)** | ✅ **Spread normal** (Brent above WTI by ~$2.4, both legs off the new contracts). **Crude continuing to ease — WTI now below $100 as well**, both legs ~10% off their highs |
| Gold / Dollar | 4,419.10 (+0.44%) / 100.35 (+0.13%) | Gold firming back toward its run high; dollar flat and holding above 100. Both cross-check cleanly against yesterday's recorded levels |

### The tape is quiet and the constraint is elsewhere

VIX at a multi-week low, futures flat, crude easing, and the 10-yr finally ticking down.
**There is no macro reason not to trade today** — rule 29 blocks nothing, the VIX brake is
far away, and the FOMC is behind us. **That is precisely why today's zero-entry result is a
research/supply finding rather than a calendar one.** See the research log: the binding
kills were **a falsified catalyst (PAAI), a 17.4×-float resale overhang (SECZ), and plain
catalyst absence** on everything else.

⚠️ **The one live macro caution is the 10-yr.** It declined for the first time in thirteen
sessions, and lesson 34 exists to stop exactly that print being read as the turn. Twelve
sessions up, one session down, still 20bp through trigger — **nothing has stood down.**

### 🚨 The stop-width escalation weakened for a SECOND consecutive session

53a (written 9/17) held that stop width and catalyst quality are separable and that which
one binds **must be re-measured each session**. Re-measured today on the **corrected**
MDD-from-HWM statistic (54c, approved 9/17): **SECZ median MDD 5.44% = 0.78× the trail ·
ASPN 0.70× · HDSN 0.50× · AHRT 0.26× · GSIT 0.86× · ATOM 0.98×.** **Six of seven in-universe
names fit inside a 7% trail, and the board still produced zero entries.**

🥇 **And the new statistic's first live use went the honest way: it PASSED SECZ's stop fit**
(the old `range ÷ trail` test would have killed it on a 9.42% median range) **— and SECZ
then died on supply structure anyway.** That is lesson 54a demonstrated in a live session:
**an accuracy fix removes a false veto; it does not supply an edge.** Recorded against
Rocket's own standing escalation (48c), per 53b.

### Factor watch

🚨 **IWM +0.53% vs SPY +1.13% = −0.60% of factor Thursday** — carried at the **new 50% core
weight ≈ −0.30% on the book.** Lesson 28 bars booking a one-session move as information.
It belongs in `weekly_review`, where the core weight decides Rocket's year — **and note that
weight is now 50%, not ~93%, so factor drift matters materially less from here.**

🚨 **`weekly_review` W36 (9/04), W37 (9/11) AND W38 (due TODAY 9/18) — THREE now owed.**
`memory/weekly_reviews/` still ends at **2026-W35**; the hand-built chain is **fifteen
sessions stale** (last good 8/28 W35, −2.51%). **NINTH session flagging W36.**
Lesson 47c / [[launchd-quota-contention]].

### Instrument health

🥇 **THE FINDING OF THE SESSION IS A DATA-INTEGRITY ONE AND IT WAS IN ROCKET'S OWN FILES.**
The 9/17 research log recorded PAAI's catalyst as a *"$1B deal plus an $89M investment,
confirmed via web search."* **The 8-K filed this morning says the company receives ZERO
proceeds, is NOT a party to the equity transaction, states no dollar value anywhere, and
furnished the whole thing under Item 7.01 rather than filing it under Item 1.01.** Lesson
39a: a dated entry read twice is one unchecked claim — **this is the second reading, and it
caught it.** Secondary coverage supplied a number the issuer never printed.
✅ **`macro` populated every field for a FOURTEENTH straight session**, and the futures-roll
patch corrected **five** rows (ES/NQ/RTY → Z26, BZ → BZZ26, **CL → CLX26**), **including a
sign flip on the Russell** — tagged naive-vs-true as designed (50d).
✅ 🥇 **Scanner `Change %` correct on TWELVE of twelve checkable rows — a FIFTH consecutive
clean session.** Every row reconciles exactly as a 9/18 premarket quote against the 9/17
settled close: SECZ 9.63/8.93 ✓, AHRT 6.68/6.23 ✓, ASPN 5.48/5.13 ✓, ATOM 4.16/3.98 ✓,
GSIT 5.33/5.22 ✓, HDSN 5.25/5.15 ✓, TTI 6.34/6.15 ✓, NRGV 4.34/4.23 ✓, ALIT 12.68/12.29 ✓,
UAMY 4.70/4.61 ✓. **Lesson 55b's one-line check, run before writing any defect.**
⚠️ **`unusual_volume`'s RelVol column unusable for a FIFTH straight session** — 17 of 20 rows
below 1.0×. `top_movers` gave **9 of 20 rows `—`.** Medians pulled on every survivor (rule 46).
🚨 🥇 **RULE 46 PRODUCED ITS WIDEST CONTAMINATION MARGIN EVER RECORDED — PAAI.**
`eligibility` mean ADV **441,426 (PASS)**; 63-day **MEDIAN 84,400 (FAILS by 72%)** —
**a 5.2× mean/median ratio**, past TLYS (2.4×) and BBCP (1.7×). **One 31.76M-share bar
carried the mean through the gate by itself**, and all five prior sessions traded under it.
✅ **`eligibility`: 8 requested → 8 returned** (lesson 43 count held, on full output per 43b).
🚨 **Lesson 24a/24d RECURRED A FIFTH TIME:** `portfolio_snapshot.py` printed IWM as **"5"**;
raw `GET /v2/positions/IWM` says **5.4746** — a **9.5% error**, the largest yet. Standing
property of the tool; raw qty pulled from the API for every calculation here.
📌 **Nasdaq earnings calendar: 15 reporters for 9/17 + 7 for 9/18 = 22 screened, ZERO
survivors** — every one dead on a named gate. Lesson 41d honest tally now **3-for-7**.

---

## Snapshot — 2026-09-17 Thursday premarket (Week 38 day 4 — **FIRST POST-FOMC SESSION**)

All "last close" figures are **Wednesday 2026-09-16's settled closes**.

| Metric | Level | Read |
|---|---|---|
| ✅ **THE CALENDAR** | **FOMC DELIVERED 9/16: 25bp HIKE, as priced (~90% odds)** | ✅ **Rule 29's board-wide block is LIFTED** — the event that closed the last three sessions has passed and resolved as expected. 🚨 **And the board still produced nothing**, on catalyst quality rather than on the calendar. **That is today's real result: the constraint was never only the calendar** |
| **VIX** | **16.04** (**−9.43%**) | ✅ **Well below the 22 brake, and the single biggest one-day drop on this table in weeks.** 17.20 → 17.00 → 17.71 → **16.04**. **Textbook post-event vol crush** — the decision was pre-priced and the hedges came off. ⚠️ **A vol crush is not a bullish signal, it is the absence of an event**; no size restriction either way |
| **FUTURES** | **ES +0.82% · NQ +1.08% · RTY +0.79%** | ✅ **Broadly risk-on — post-decision relief.** 🚨 **The roll patch fired again and on ALL FOUR rows**: ES/NQ/RTY → **Z26**, Brent → **BZZ26**. Naive vs true: ES **+1.71% → +0.82%**, NQ **+2.10% → +1.08%**, RTY **+1.53% → +0.79%**, Brent **−6.01% → −1.28%**. **Unpatched, this table would have overstated every equity future by ~0.8pts and reported Brent down 6% on the morning after an FOMC.** Third consecutive session the patch has done real work (lesson 50) |
| **Russell vs the others** | **RTY +0.79%, between ES and NQ** | ⚠️ **The two-session "Russell is the laggard" flag did NOT persist** — small caps are mid-pack on the relief tape. **Lesson 28: this is the fifth-plus one-session macro read to reverse inside 24 hours.** Flagged, not booked, in either direction |
| 🚨 **10-yr** | **5.01%** (**+0.20%**) | 🚨 **TWELFTH consecutive session through the 4.75% trigger, and a NEW RUN HIGH — the day AFTER the hike was delivered** (4.84 → 4.94 → 4.97 → 4.96 → 5.00 → **5.01**). 🥇 **This is the line worth reading twice: equities are celebrating a hike that the long end did not price as the end of anything.** The 10-yr rose *through* the decision. **Still the cleanest, best-corroborated macro signal on the board — and the relief rally is happening above it, not because of it** |
| SPY / IWM | **754.05 (−0.44%)** / **283.92 (−0.43%)** | Wednesday's settled closes. ✅ **Factor +0.01% — dead flat, the first genuinely neutral session in weeks.** At 93.58% core weight that is ≈ **+0.01% on the book** — Rocket's whole day, since there are no satellites. **Lesson 28 bars booking it as information; at this magnitude there is nothing to book anyway** |
| **Brent / WTI** | **99.47 (−1.28%)** / **100.75 (−1.64%)** | ✅ **Spread normal (Brent below WTI by ~$1.3 — both legs now read off Dec contracts).** Crude **broke below $100 on Brent** for the first time in this file's recent history, off ~8% from the highs. ⚠️ **Do not over-read a cross-roll level comparison** (50d) — safe to assert: crude is easing, both legs off their highs |
| Gold / Dollar | 4,348.80 (−0.88%) / 100.17 (−0.14%) | Gold off its run high after the hike landed; dollar essentially flat and **back above 100**. Both cross-check cleanly against yesterday's recorded levels |

### The event resolved as priced — and the interesting part is what did NOT move

The hike was delivered, the VIX collapsed **−9.4%**, futures went risk-on, and **the 10-yr
went UP to a new run high of 5.01%.** Equities are trading the removal of uncertainty; the
bond market is not trading a peak. **Those are compatible for one session and not much
longer.** Energy easing and gold off its high are the only two legs that softened.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**For satellites, rule 29 no longer blocks anything — and seven in-universe names were
screened and killed on their own merits instead.** See the research log: **the binding
constraints today were catalyst quality (rule 1/7a), dilution (rule 8) and rule 13's cap
ceiling — not stop width.**

### 🚨 The stop-width argument weakened today, on Rocket's own evidence

Yesterday this file recorded lesson 51: a trailing stop keys on **drawdown from the running
high**, not daily range, and KMTS's 9/15 catalyst bar had an MDD of **6.18%** — the trail
survived and would have paid **+15.49%.** **Run the identical measurement on the next bar:
KMTS 9/16 MDD from HWM = 5.80%. The trail survived again — and the trade lost 4.44%.**

🥇 **Lesson 51's correctness is untouched; the claim attached to it is not.** MDD-from-HWM
**removes a false veto. It does not supply an edge** — a gate that stops vetoing bad trades
along with good ones is an accuracy fix, not a profit case. **Escalation 2 re-stated on
accuracy grounds only.** Recorded against Rocket's own argument (45h/51e).

### Factor watch

✅ **IWM −0.43% vs SPY −0.44% = +0.01% of factor Wednesday** — **flat to two decimal places**,
after Tuesday's −0.24%. Carried at 93.58% core weight ≈ **+0.01% on the book.** Lesson 28
bars booking a one-session move and there is nothing here to book. It belongs in
`weekly_review`, where the ~93.6% core weight is what actually decides Rocket's year.

🚨 **`weekly_review` W36 (due 9/04) AND W37 (due 9/11) BOTH remain unrun — EIGHTH session
flagging W36 — and W38 falls due TOMORROW (Friday 9/18), which would make THREE owed.**
`memory/weekly_reviews/` still ends at **2026-W35**; the hand-built Rocket-vs-SPY chain is
**fourteen sessions stale** (last good 8/28 W35, −2.51%).
Lesson 47c / [[launchd-quota-contention]].

### Instrument health

🚨 🥇 **THE NEAR-MISS OF THE SESSION: this file almost recorded a false instrument defect.**
The scanner's premarket rows looked badly wrong against 9/16's settled closes — GLAS "+7.2%"
against a −0.12% close, SOC "+2.8%" against **−7.66%**, HAWK "+3.9%" against −1.94%, OSS
"+5.4%" against −1.05% — **four apparent sign flips, exactly lesson 17b's signature.**
✅ **They are all correct.** Every row reconciles **exactly** as a **9/17 premarket quote
against the 9/16 settled close**: GLAS $8.61/$8.03 ✓, ACP $4.96/$4.65 ✓, UNCY $5.09/$4.78 ✓,
XTND $5.00/$4.73 ✓, DUOT $8.75/$8.30 ✓, OSS $8.98/$8.52 ✓, ANRO $31.44/$30.00 ✓,
HAWK $16.80/$16.17 ✓, SOC $4.71/$4.58 ✓, FLNC $7.27/$9.05 ✓, ALMU $11.47/$13.43 ✓ —
**eleven for eleven.** 📌 **Thirteen sessions of documented scanner defects had primed the
conclusion, and the arithmetic refused it.** Lesson 39's discipline running in the
unfamiliar direction: **a prior of "the instrument is broken" is still a prior, and it must
be checked against the bars before it reaches a finding.**
✅ **`macro` populated every field for a THIRTEENTH straight session**, and the futures-roll
patch corrected **all four** futures rows (ES/NQ/RTY → Z26, BZ → BZZ26), tagging naive-vs-true
as designed (lesson 50d).
✅ **`eligibility`: 8 requested → 8 returned** (lesson 43 count held, on full output per 43b).
🚨 **`eligibility` and the scanner disagree on XTND's market cap by 11.7×** — scanner
**$101.15M**, eligibility **$1,178M** (249.1M sh × $4.73). **A universe gate with two answers
is rule 38's unresolved-gap FAIL**, and the name was dropped on it rather than scored.
⚠️ **`unusual_volume`'s RelVol column remains unusable for a FOURTH straight session** —
**18 of 20 rows below 1.0×** on a broadly green tape. `top_movers` gave **5 of 20 rows `—`**.
Medians pulled on every survivor regardless (rule 46).
✅ **Nasdaq earnings calendar delivered 22 reporters for 9/16 + 15 for 9/17 = 37 screened,
ZERO survivors.** Lesson 41d honest tally now **3-for-6**.
🚨 **Lesson 24a/24d RECURRED A FOURTH TIME:** `portfolio_snapshot.py` printed IWM as "10";
raw `GET /v2/positions/IWM` says **9.8636**. **Treated as a standing property of the tool —
the raw qty was pulled from the API in the book calculation itself, never from the table.**
✅ **`portfolio_snapshot.py` ran clean** — the 9/14 `/v2/orders` timeout (lesson 25) has not
recurred in three sessions.
