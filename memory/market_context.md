# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-16 Wednesday premarket (Week 38 day 3 — **FOMC DECISION DAY**)  ← CURRENT

All "last close" figures are **Tuesday 2026-09-15's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **FOMC DECISION TODAY, 2:00 PM ET — ~90% odds of a HIKE** | 🚨 **Rule 29 at maximum force: day 1 of any hold opened today IS the event.** There is no configuration — no catalyst, no size, no stop — that makes a satellite entry legal this session. Every other line on this page is subordinate to this one |
| **VIX** | **17.00** (**−1.16%**) | **Well below the 22 brake.** 18.03 → 17.10 → 17.20 → **17.00** — ⚠️ **the VIX has now drifted DOWN for three sessions into a ~90%-priced hike decision.** Either the event is genuinely pre-priced or this is complacency; **on the morning of the print there is no way to tell, and no trade depends on it.** Noted, not resolved |
| 🚨 **10-yr** | **5.00%** (**+0.71%**) | 🚨 **ELEVENTH consecutive session through the 4.75% trigger, and a new run high ON A ROUND NUMBER** (4.78 → 4.81 → 4.84 → 4.94 → 4.97 → 4.96 → **5.00**). Lesson 34's "trend, not one print" bar was met eight sessions ago. **Still the cleanest, best-corroborated macro signal on the board — and it goes into the decision at its high** |
| **FUTURES** | **ES +0.23% · NQ +0.45% · RTY +0.17%** | ✅ **Mildly risk-on, and the roll correction fired again**: ES/NQ/RTY all re-read off the **Z26** contracts. Naive vs true: ES **+1.11% → +0.23%**, NQ **+1.46% → +0.45%**, RTY **+0.92% → +0.17%**. 🚨 **Unpatched, this table would have overstated every equity future by ~0.8 points on FOMC morning.** Second consecutive session the patch has done real work (lesson 50) |
| ⚠️ **Russell vs the others** | **RTY +0.17%, the WEAKEST of the three again** | Small caps lag on the pre-decision tape for a second straight session. **Lesson 28: one session carries no information — and two is not much more.** Flagged, not booked |
| SPY / IWM | **757.39 (−0.46%)** / **285.14 (−0.70%)** | Tuesday's settled closes. 🚨 **Factor −0.24% AGAINST Rocket**, carried at 93.6% core weight ≈ **−0.22% on the book** — Rocket's whole day, since there are no satellites. ⚠️ **IWM's recorded 9/14 close disagrees with `macro`'s read of that same bar (287.91 recorded vs 287.16 now) — a 0.26% gap, plausibly an ex-dividend adjustment. Flagged, not scored** (lesson 38) |
| **Brent / WTI** | **107.73 (−0.94%)** / **103.84 (−1.88%)** | ✅ **The Brent-below-WTI inversion flagged yesterday has RESOLVED** — Brent is back above WTI at a normal spread, and both levels now reconcile with the 9/14 readings (107.43 / 102.71). **The 9/15 file's caution against asserting a Brent level across the roll was correct and the distortion has washed out.** Crude remains elevated, both legs off their highs |
| Gold / Dollar | 4,387.00 (+1.25%) / 99.68 (+0.03%) | Gold at a run high into the decision; dollar flat after firming for a week. Both cross-check cleanly for the first time in several sessions |

### The macro thesis is unchanged and today it gets settled

Rates remain the signal — **an eleventh session through trigger, at a 5.00% run high, into a
decision that is hours away.** Energy elevated, gold at a high, dollar firm: the same four legs
this file has tracked for two weeks, all still pointing at a hike. **Nothing about the setup is
ambiguous. What is ambiguous is the reaction**, and rule 29 exists precisely because a 7% trail
cannot price a policy gap — it fills at the open, wherever the open is.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design** — recorded as a decision, not an
omission. **For satellites the answer is simply no, today.**

### Factor watch

🚨 **IWM −0.70% vs SPY −0.46% = −0.24% of factor Tuesday**, ≈ **−0.22% on the book** at 93.6%
core weight. Reverses Monday's +0.11%. **Lesson 28 bars booking either as information** — this
belongs in `weekly_review`, where the ~93.6% core weight is what actually decides Rocket's year.

🚨 **`weekly_review` W36 (due 9/04) AND W37 (due 9/11) BOTH remain unrun — SEVENTH session
flagging W36.** `memory/weekly_reviews/` still ends at **2026-W35**; the hand-built
Rocket-vs-SPY chain is **thirteen sessions stale** (last good 8/28 W35, −2.51%).
Lesson 47c / [[launchd-quota-contention]].

### Instrument health

🚨 🥇 **THE BIG ONE TODAY IS NOT AN INSTRUMENT — IT IS A STATISTIC. Lesson 48's stop-fit
diagnostic was falsified.** Eight sessions of this file have asserted, from `daily range ÷ 7%`,
that no small-cap catalyst day can be held with a 7% trail. **A trailing stop keys on drawdown
from the running high, not on daily range** — the same number only on a round-trip bar.
Re-measured on 5-minute bars across all eleven names lesson 48 counted: **the trail SURVIVED 6
and was HIT 5**, and **KMTS — the best catalyst on the board — would have held and paid +15.49%.**
✅ **The ELMT kill is vindicated by the same test** (15.66% drawdown). ❌ **The universal claim is
not.** Escalated to the user as a proposed change of statistic; **no gate rewritten** (rule 42).
✅ **`macro` populated every field for a TWELFTH straight session**, and the **futures-roll patch
corrected three rows again** (ES/NQ/RTY → Z26), tagging naive-vs-true as designed (lesson 50d).
✅ **Brent/WTI levels reconciled** for the first time since the roll — the flagged inversion is gone.
⚠️ **IWM's 9/14 close differs between this file (287.91) and `macro` (287.16)** — 0.26%, likely
ex-dividend. **Flagged, not scored** (38).
✅ **`eligibility`: 12 requested → 12 returned** (lesson 43 count held, on full output per 43b).
🚨 **`unusual_volume`'s RelVol column is garbage for a THIRD straight session** — **19 of 20 rows
below 1.0×**, on a day its own top name (FTFT) gapped +20%. `top_movers` gave **9 of 20 rows
`—` or `0.0x`.** ✅ **`Change %` correct for a FOURTH consecutive session** — DTIL, RCKT and FTFT
all reconcile exactly off Tuesday's settled closes. **Same split as 17f/17g: price usable, RelVol
uncorrelated.** Medians pulled on every survivor regardless (rule 46).
✅ **EDGAR delivered decisively** — it produced KMTS's **undrawn S-3ASR** (gate C), the **Bermuda
incorporation** that opened escalation 4, and the **10b5-1 plan adoption dates** that reversed an
apparent "insiders dumping into the print" read into scored-as-noise. 🥇 **Three separate
findings, none available from any secondary source.**
📌 **Nasdaq earnings calendar: 15 reporters for 9/15 + 23 for 9/16 = 38 screened, ZERO survivors.**
Lesson 41d honest tally now **3-for-5** — calendar and screener are complements, not a hierarchy.

---

## Snapshot — 2026-09-15 Tuesday premarket (Week 38 day 2 — FOMC IS TOMORROW)

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
