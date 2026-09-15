# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-15 Tuesday premarket (Week 38 day 2 — FOMC IS TOMORROW)  ← CURRENT

All "last close" figures are **Monday 2026-09-14's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **FOMC decision TOMORROW, Wednesday 9/16 — ~90% odds of a HIKE** | 🚨 **Binding on the entire board, and TIGHTER than yesterday.** A 1–5 day hold opened today runs 9/15 · **9/16** · 9/17 · 9/18 · 9/21 — the decision is now on **day 2**, not day 3. Rule 29: a 7% trail cannot protect against a policy gap; it fills at the open, wherever the open is |
| 🚨🆕 **FUTURES — THE INSTRUMENT DEFECT IS THE STORY** | **ES −0.33% · NQ −0.36% · RTY −0.40% (TRUE, post-roll)** | 🚨 **FOUR futures rows ROLLED CONTRACT TODAY (ES/NQ/RTY Sep→Dec quarterly, BZ Nov→Dec) and the naive continuous-symbol read printed the WRONG SIGN on all four**: ES naive **+0.55%** → true **−0.33%**; NQ **+0.66%** → **−0.36%**; RTY **+0.36%** → **−0.40%**; Brent **−3.15%** → **+1.35%**. ✅ **Caught and corrected by the `_resolve_futures_contract` patch to `market_data.py`** (the roll re-reads BOTH legs off the named contract, e.g. `RTYZ26.CME`). **Unpatched, this table would have read "risk-on into the FOMC" on the day before the decision, when futures are in fact broadly DOWN and Brent is UP.** See instrument health |
| ⚠️ **Russell vs the others** | **RTY −0.40%, the WORST of the three** | 🚨 **Yesterday's "first genuine counter-signal in three sessions" (RTY +0.42% vs NQ −1.72%) did NOT persist — one session later the Russell is the laggard again.** ✅ **Yesterday's file explicitly refused to book it as a turn, citing lesson 28. That restraint is vindicated in a single session** — and it is a live demonstration of why 28 exists. **Still not booked as information in either direction** |
| **VIX** | **17.48** (**+2.22%**) | **Below the 22 brake — no size restriction.** Friday 18.03 → Monday **17.10** (−5.2%) → live 17.48. **The FOMC-pricing spike of 9/14 gave most of itself back**, which is the opposite of what a 90%-hike-odds decision one day out would suggest. Noted, not resolved |
| 🚨 **10-yr** | **4.96%** (−0.28%) | 🚨 **TENTH consecutive session through the 4.75% trigger**, one basis point off the run high (4.78 → 4.81 → 4.84 → 4.94 → 4.97 → **4.96**). Lesson 34's "trend, not one print" bar was met seven sessions ago. **Still the cleanest, best-corroborated macro signal on the board** |
| SPY / IWM | **760.88 (−0.45%)** / **287.91 (−0.34%)** | Monday's settled closes. ✅ **Both cross-check EXACTLY against this file's recorded prior closes** (764.29 → 760.88 = −0.45%; 288.89 → 287.91 = −0.34%). ✅ **Factor +0.11% IN ROCKET'S FAVOUR — first favourable session after three adverse ones.** Lesson 28: **one session carries no information.** Flagged, not booked |
| ⚠️ **Brent / WTI** | **102.35 (+1.35%)** / **103.58 (+2.16%)** | ⚠️ 🆕 **Brent is printing BELOW WTI** — the spread is normally the other way round. The BZ Nov→Dec roll is corrected for the *change* but the **level inconsistency across sessions persists** (this file recorded Brent 107.43 on 9/14; `macro` now reads its 9/14 close as 100.99). **Safe to assert: crude is ~$100–104 and elevated. Do not quote a Brent level or % to the decimal, and do not assert a direction from the cross-session delta** |
| Gold / Dollar | 4,314.80 (−0.85%) / 99.60 (+0.14%) | Dollar cross-checks clean and is still firming. Gold's cross-session level disagreement persists — **flagged, not scored** (lesson 38) |

### The macro thesis is unchanged; the instrument that reports it nearly inverted

Rates remain the signal — a tenth session through trigger, at the run high, into a decision
that is now **one day away**. What changed today is not the thesis but **the reliability of the
table it is read from**: a quarterly futures roll silently flipped the sign on three equity
index rows and one energy row at once. **The naive read was not noisy — it was plausible and
backwards**, which is the dangerous kind (lesson 15). It was caught only because the script
now resolves the continuous `=F` symbol to the actual contract it is quoting.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design** — recorded as a decision, not
an omission.

**For satellites it is the opposite**, and rule 29 is today the binding kill on the whole
board — including on **KMTS**, a clean rung-1 beat-and-raise (FY guide +2.92%, 284% pass-through).

### Factor watch

✅ **IWM −0.34% vs SPY −0.45% = +0.11% of factor Monday**, carried at 93.67% core weight
≈ **+0.10% on the book** — Rocket's whole day, since there are no satellites. **First
favourable session after three adverse ones** (−0.41% Thu, −0.44% Fri, −0.91% Wed).
Lesson 28 bars booking a one-session move as information and that is honored. It belongs in
`weekly_review`, where the ~93.7% core weight makes it matter.

🚨 **`weekly_review` W36 (due 9/04) AND W37 (due 9/11) BOTH remain unrun — SIXTH session
flagging W36.** `memory/weekly_reviews/` still ends at **2026-W35**. The hand-built
Rocket-vs-SPY chain is **twelve sessions stale** (last good: 8/28 W35, −2.51%). Per lesson
47c this was escalated **directly to the user in this session's response.**
Lesson 47 / [[launchd-quota-contention]].

### Instrument health

🚨 🆕 **THE BIG ONE — `macro`'s futures rows silently changed instrument underneath the series.**
A `=F` symbol is **continuous front-month**: on roll day `last/prev` compares two *different*
contracts and reports the **calendar spread** as a price move. **Four of seven futures rows
rolled at once on 2026-09-15 and three printed the wrong sign.** ✅ Fixed in code
(`_resolve_futures_contract`), which resolves the contract from `.info` and re-reads **both
legs** off it — no hand-maintained roll calendar, because a hand-maintained calendar is just
a slower version of the same defect. 📌 **Prior art: the same bug class hit `ZQ=F` one session
earlier (9/14) and corrupted the magnitude of a live thesis test.** The output now tags rolled
rows `🔄 ROLLED` and prints naive-vs-true. **This is lesson 15 at full strength: a populated,
plausible field that was simply wrong.**
✅ **`macro` populated every field for an ELEVENTH straight session**; equity and rates rows
cross-check **exactly** against recorded prior closes.
✅ **`eligibility`: 11 requested → 11 returned, and 3 → 3 on the re-run** (lesson 43 count held,
run against full output not a truncated view, per 43b).
✅ **Nasdaq earnings-calendar API delivered on its sixth use** — 15 reporters for 9/14, 17 for
9/15, with cap and BMO/AMC in one call. 🥇 **It sourced the session's ONLY real catalyst (KMTS),
which appeared on NEITHER scanner list.** Lesson 41d now **3-for-4**.
🚨 🆕 **LESSON 17f CONFIRMED AGAIN — `Change %` correct on EVERY checkable row for a THIRD
consecutive session**, and `RelVol` still garbage. Reconciled against Monday's settled closes:
ELMT 21.50→21.41 = −0.42% ✓, PLAY 8.47→7.50 = −11.45% ✓, SOC 4.82→5.08 = +5.39% ✓,
FTK 26.34→28.00 = +6.30% ✓, EAF 6.66→6.99 = +4.95% ✓ — **five for five, exact.**
⚠️ **Meanwhile `unusual_volume` printed ELMT at 1.3× RelVol against a Monday bar of 13,965,600
shares = 46.6× its 299,600 median** — and **yesterday the same column printed ELMT at 44.0× on
a 0.48× day.** 🚨 **The column is not biased, it is UNCORRELATED**: the same ticker, two
sessions running, with the error in opposite directions. `top_movers` gave 14 of 20 rows `—`
or `0.0x`. **Treat `Change %` as provisionally usable off settled closes; treat `RelVol` as
pure noise and pull the median on every survivor** (rule 46).
✅ **`portfolio_snapshot.py` ran clean today** — the `/v2/orders` timeout of 9/14 (lesson 25)
did not recur.
🚨 **Lesson 24a RECURRED A THIRD TIME: the snapshot table printed IWM as "10"; the raw
`GET /v2/positions/IWM` says 9.8636.** A 1.4% error, and it has already inverted a rebalance
verdict once. **Pull raw qty from the API in the rebalance step itself, never from a formatted
table.**
📌 **Alpaca's quote/trade endpoints returned only 2026-09-14T20:00 timestamps at 06:20 ET** —
no premarket book available, so KMTS's premarket had to be read from yfinance 5-min prepost
bars (2 bars, **zero reported volume**). **Flagged, not scored** (lesson 15).

---

## Snapshot — 2026-09-14 Monday premarket (Week 38 day 1 — FOMC WEEK)

All "last close" figures are **Friday 2026-09-11's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **FOMC decision WEDNESDAY 9/16 — 2 trading days out, ~90% odds of a HIKE** | 🚨 **The binding gate on the entire board.** A 1–5 day hold opened today runs 9/14 · 9/15 · **9/16** · 9/17 · 9/18 — **the decision sits dead in the middle, not at the far end.** Friday's core CPI came in **+0.3% m/m against a +0.2% consensus** and futures repriced to ~90% hike odds. Rule 29: a 7% trail cannot protect against a policy gap; it fills at the open, wherever the open is |
| 🚨 **VIX** | **18.03** (**+13.83%**) | **Still below the 22 brake — no size restriction.** But this is **the largest single-session VIX jump of the run** (15.84 → 18.03), and it is the first session in which the options market has actually priced the FOMC it has been ignoring for a week. ⚠️ Last week this file flagged that a *falling* VIX into CPI was either complacency or an overdone flag — **the tape has now answered in favour of the flag** |
| 🚨 **10-yr** | **4.97%** (**+0.63%**) | 🚨 **NINTH consecutive session through the 4.75% trigger, and a new run high** (4.78 → 4.81 → 4.84 → 4.94 → **4.97**). Lesson 34's "trend, not one print" bar was met six sessions ago. **Still the cleanest, best-corroborated macro signal on the board** |
| 🚨 **FUTURES — READ THIS ONE** | **ES −0.78% · NQ −1.72% · RTY +0.42%** | 🚨 🆕 **A LARGE-CAP TECH SELLOFF WITH SMALL CAPS HOLDING UP — the first session of the run where the Russell is the relative WINNER.** ✅ **Independently verified against raw futures** (ES=F 7,600.00, NQ=F 28,881.00, RTY=F 2,916.80) rather than trusted from `macro` alone — the two agree. **A 2.1-point NQ-vs-RTY spread is not noise**, and it is the exact inverse of the three-session factor drag below |
| SPY / IWM | **764.29 (+0.85%)** / **288.89 (+0.41%)** | Friday's settled closes. ✅ **Both cross-check EXACTLY against this file's recorded prior closes** (757.83 → 764.29 = +0.85%; 287.70 → 288.89 = +0.41%). 🚨 **Factor −0.44% against Rocket — THIRD consecutive adverse session** |
| ⚠️ **Brent / WTI** | **107.43 (+2.70%)** / **102.71 (+2.66%)** | **New run highs on both legs** — Brent 92.33 → 107.43 = **+16.4% across the run**, WTI confirming every leg. ⚠️ The level/change inconsistency flagged Friday **persists but has NARROWED** (implied prior 104.61 vs recorded 103.95 = 0.6%, in from ~3.5%). **Safe to assert: Brent is ~$107 and clearly at a run high.** Do not quote the % to the decimal |
| ⚠️ Gold / Dollar | 4,325.20 (−0.94%) / 99.57 (+0.46%) | ⚠️ Gold's print still disagrees with its own level (implied prior 4,366 vs recorded 4,385.30 = −1.37% actual). **Flagged, not scored** (lesson 38). Dollar cross-checks clean and is firming |

### The rates leg is now NINE sessions old, and the VIX has finally joined it

For two weeks this file has tracked energy + rates + gold as inputs pointing at a September
hike. Today **three of the four legs corroborate and the fourth has stopped contradicting**:
the 10-yr at a run high for a ninth session, Brent at a run high, the dollar firming — and
**VIX +13.8%, the first session it has priced the event.** The gold row remains broken and is
recorded as unresolved rather than folded in (lesson 38: resolve or flag, never score).

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design** — recorded as a decision, not
an omission.

**For satellites it is the opposite**, and rule 29 is today the binding kill on the whole
board — including on ELMT, the strongest catalyst screened in weeks.

### Factor watch — and the first genuine counter-signal in three sessions

🚨 **IWM +0.41% vs SPY +0.85% = −0.44% of factor Friday**, carried at 93.69% core weight
≈ **−0.41% on the book** — Rocket's whole day, since there are no satellites. **Third
consecutive adverse session** (−0.41% Thu, −0.44% Fri, −0.91% Wed).

⚠️ **But Monday's futures point the other way, hard: RTY +0.42% against NQ −1.72%.** Lesson 28
bars booking a one-session move as information and that is honored — **this is flagged as a
thing to watch across the week, NOT booked as a turn.** It is the first evidence in six weeks
running counter to the −2.50%-since-rebase drift, and the honest read is that one premarket
futures print is exactly the kind of thing lesson 28 was written to stop Rocket over-reading.
**It belongs in `weekly_review`, where the ~90% core weight makes it matter.**

🚨 **`weekly_review` W36 (due 9/04) AND W37 (due 9/11) BOTH remain unrun — FIFTH session
flagging W36.** `memory/weekly_reviews/` still ends at **2026-W35**. The hand-built
Rocket-vs-SPY chain is **eleven sessions stale** (last good: 8/28 W35, −2.51%). Per lesson
47c this was escalated **directly to the user in this session's response** rather than
deferred into the files a sixth time. Lesson 47 / [[launchd-quota-contention]].

### Instrument health

✅ **`macro` populated every field for a TENTH straight session**, and the equity/rates rows
cross-check **exactly** against recorded prior closes. The commodity rows remain internally
inconsistent but **the discrepancy narrowed** (Brent 3.5% → 0.6%).
✅ **Futures independently verified against `yfinance` raw** — ES/NQ/RTY all agree with `macro`
to within 0.05%. Given the commodity defect, cross-checking the row the session actually
depends on was worth one call.
✅ **`eligibility`: 10 requested → 10 returned** (lesson 43 count held, run against full output).
✅ **Nasdaq earnings-calendar API delivered on its fifth use** — 14 reporters for 9/11, 16 for
9/14, with cap and BMO/AMC in one call. ⚠️ **But today it sourced ZERO survivors**: every
9/11 and 9/14 reporter died on cap, price, domicile or ADV. **The scanner sourced the one real
catalyst (ELMT).** Recording this honestly — lesson 41d's claim that the calendar out-sources
the screener is **now 2-for-3, not universal**; the two instruments are complements.
🚨 🆕 **LESSON 17 INVERTS: the `Change %` column was CORRECT ON EVERY ROW, and `RelVol` is
the broken one.** All six top rows reconcile *exactly* to Friday's settled closes (ELMT
16.19→21.27 = +31.4% ✓, CRBP 8.12→9.61 = +18.4% ✓, CLB 12.50→13.45 = +7.6% ✓, STIM
3.03→3.23 = +6.6% ✓, FLWS 3.02→3.27 = +8.3% ✓). **Second consecutive session the price column
has been right** (ACVA 9/11). ⚠️ **Meanwhile `unusual_volume` printed ELMT at 44.0× RelVol
against a Friday bar of 142,900 shares = 0.48× its own median** — the single widest RelVol
error yet recorded, and **ELMT never appeared in `top_movers` at all despite being the day's
biggest gapper.** Net: **treat `Change %` as provisionally usable off settled closes; treat
`RelVol` as pure noise and pull the median on every survivor** (rule 46).
📌 **`GET /v2/positions` `current_price` (IWM 288.17 / SPY 758.68) does NOT match the settled
closes (288.89 / 764.29).** Delayed or premarket quotes. **Use `macro` closes for the book,
the positions endpoint only for raw `qty`** (lesson 24a — qty 9.8636 confirmed, table says "10").

---
