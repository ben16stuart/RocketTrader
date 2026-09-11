# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-11 Friday premarket (Week 37 day 4 — CPI MORNING)  ← CURRENT

All "last close" figures are **Thursday 2026-09-10's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **CPI PRINTED 8:30 ET · FOMC decision 9/16 (2 trading days out)** | 🚨 **Update, midday**: actual print **headline +0.4% m/m / 3.4% y/y — in line**; **core +0.3% m/m, 0.1pt HOTTER than the +0.2% consensus** (core y/y 2.4%, in line). Stocks rallied on the print (yields eased), but **Fed funds futures moved to ~90% odds of a hike at 9/16** — up from earlier in the week. Rally + higher hike odds is not a contradiction the market has resolved for us; it sharpens rule 29's calendar gate rather than closing it. FOMC still sits in the MIDDLE of any 1–5 day hold opened today (9/11 · 9/14 · 9/15 · **9/16** · 9/17) |
| 🚨 **10-yr** | **4.94%** (**+2.21%**) | 🚨 **EIGHTH session through the 4.75% trigger and the BIGGEST single-session jump of the run: 4.78 → 4.81 → 4.84 → 4.94, +10bps in a day.** Lesson 34's "trend, not one print" bar was met five sessions ago. **This is the cleanest, best-corroborated macro signal on the board** |
| **VIX** | **17.09** (**−4.20%**) | Below the 22 brake — **no size restriction.** ⚠️ **But note the direction: VIX FELL 4.2% INTO CPI day.** After a week of this file flagging the CPI/FOMC pair, the options market is pricing the print as routine. Either the flag is overdone or the tape is complacent; **one print will not settle it (rule 34)** |
| **Russell fut** | 2,911.20 (**+0.62%**) | ⚠️ **The same pattern as yesterday: a positive change print on a LOWER level** (2,925.50 → 2,911.20, −0.5% overnight). S&P +0.59%, Nasdaq +0.67% — **Russell is the laggard of the three for a third straight session** |
| SPY / IWM | **757.83 (−0.60%)** / **287.70 (−1.01%)** | Thursday's settled closes. 🚨 **Factor −0.41% against Rocket** — second consecutive adverse session (−0.91% Wednesday) |
| Gold / Dollar | 4,385.30 (+0.48%) / 99.15 (+0.06%) | ⚠️ **Level/change inconsistent — see instrument health.** Dollar flat and cross-checks clean |
| ⚠️ **Brent / WTI** | **103.95 (−3.42%)** / **99.22 (−3.18%)** | ⚠️ **DO NOT ASSERT A DIRECTION FROM THIS — the print is internally inconsistent** (below). What is safe to say: **Brent is ~$104 and still clearly above $100**, up from 92.33 at the start of the run |

### The rates leg is now the signal; the energy leg is unreadable this session

For a week this file tracked energy + rates + gold as three independent inputs pointing at
a September hike. **Today only the rates leg is trustworthy, and it is the strongest it has
been: the 10-yr jumped 10bps to 4.94%, an eighth session through trigger.** The energy and
gold prints disagree with their own levels (below), so **they are recorded as unresolved
rather than folded into the thesis.** Honest position: one clean confirming input, one
broken instrument, and a VIX that has stopped caring — **not the three-for-three alignment
this file claimed yesterday.** Lesson 39a: a dated entry copied forward three times is one
unchecked claim read three times.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design** — recorded as a decision, not
an omission.

**For satellites it is the opposite**, and today rule 29 is the binding kill on the whole
board: CPI in 2 hours, FOMC inside the hold window.

### Factor watch

🚨 **IWM −1.01% vs SPY −0.60% = −0.41% of factor Thursday**, carried at 93.66% core weight
≈ **−0.38% on the book** — Rocket's whole day, since there are no satellites. **Second
consecutive adverse session** (−0.91% Wednesday). Lesson 28 bars booking a one-session
move as information and that is honored here; but the *direction* matches the six-week
drift (−2.50% since rebase), which is the figure that matters and it belongs in
`weekly_review`.

🚨 **`weekly_review` W36 (due Fri 9/04) STILL has not run — FOURTH session flagging it.**
`memory/weekly_reviews/` ends at **2026-W35**; no 9/04 `market_close` entry in
`trade_log.md`. **W37's is due TODAY — two reviews now owed**, and three open escalations
(rebalance basis, stop width, ADV-gate-vs-account-size) need one of them. The hand-built
Rocket-vs-SPY chain is **ten sessions stale** (last good: 8/28 W35, −2.51%). Lesson 47 /
[[launchd-quota-contention]].

### Instrument health

✅ **`macro` populated every field for a NINTH straight session** — but see the caveat below;
populated is not the same as correct.
⚠️ 🆕 **NEW — `macro` level-vs-change inconsistency on TWO commodity fields.** Brent prints
**103.95 with −3.42%**, which implies a prior close of **107.63** — but this file recorded
Brent at **102.11** yesterday. Gold prints **4,385.30 with +0.48%** against yesterday's
recorded **4,435.40**, which is **−1.13%**, not +0.48%. **Either yesterday's readings were
intraday prints rather than settles, or the continuous futures contract rolled.** Per lesson
15 this is a broken instrument, not a cosmetic glitch, and per lesson 38 the gap is
**resolved-or-flagged, never scored**. 📌 **The equity and rates fields cross-check clean
against yesterday's recorded closes (SPY 762.40 → 757.83 = −0.60% ✅, IWM 290.64 → 287.70 =
−1.01% ✅), so the defect is confined to the commodity rows.**
✅ **`eligibility`: 13 requested → 13 returned** (lesson 43 count held, run against full output).
⚠️ 🆕 **`market_data.py price REF LPTH ACVA` returned ONE row for three tickers, exit 0** —
lesson 43's silent-omission defect, now observed on a **second** command. Re-run one ticker
at a time, all three returned. **Count rows on every multi-ticker call, not just `eligibility`.**
✅ **Nasdaq earnings-calendar API delivered on its fourth use** — 38 reporters for 9/10, 14
for 9/11, with cap and BMO/AMC in one call. It sourced **three of the four survivors**
(REF, FEIM, LPTH); the scanner sourced one (ACVA), and ACVA turned out to be a cash tender
offer with the upside pinned.
🚨 **Lesson 17a — THIRTEENTH straight demonstration, and `unusual_volume` is now useless.**
`top_movers` gave **12 of 20 rows** a RelVol of `—` or `0.0x`; **`unusual_volume` had 19 of
20 rows below 1.0×, and its top row (ACVA) printed 1.7× against a real 9/10 volume of
19,410,000 = 6.5× median.** A list sorted by relative volume whose highest entry is 1.7×,
on a day one of its names traded 6.5× median, is not measuring relative volume at all.
⚠️ **ACVA is the reverse of the "right by accident" case**: the scanner's **+43.9%** was a
**real** premarket move off the settled close — the only time in thirteen sessions the
`Change %` column has been correct — **and the name was still a kill** (rule 27, cash
tender). Accuracy on the price column does not make the row tradeable.

---

## Snapshot — 2026-09-10 Thursday premarket (Week 37 day 3)

All "last close" figures are **Wednesday 2026-09-09's settled closes**.

| Metric | Level | Read |
|---|---|---|
| 🚨 **THE CALENDAR** | **PPI today 8:30 ET · CPI tomorrow 8:30 ET · FOMC decision 9/16** | 🚨 **The single most important line in this file.** Friday's CPI is the **last inflation print before the decision**, and it lands 60 minutes before the open — a gap a 7% trail cannot protect against (lesson 29). **This closes Friday as an entry date**, which is exactly where rule 45's day-2 conversions land |
| 🚨 **Brent / WTI** | **102.11 (+0.89%)** / **97.46 (+1.47%)** | **A new run high, and now clearly through $100.** 92.33 → 95.15 → 97.10 → 95.44 → 98.53 → 100.50 → **102.11 = +10.6% across the run.** WTI confirmed every leg. **This is the input that makes tomorrow's CPI dangerous rather than routine** |
| 🚨 **10-yr** | **4.84%** (**+0.65%**) | **SEVENTH session through the 4.75% trigger, and still rising** (4.78 → 4.81 → 4.84). Lesson 34's "trend, not one print" bar was met three sessions ago |
| **VIX** | **16.47** (+0.06%) | Flat, fourth session up off the 14.21 low, far below the 22 brake. **No size restriction.** ⚠️ Note it is *not* pricing the CPI/FOMC pair |
| **Russell fut** | 2,925.50 (**+0.09%**) | Off yesterday's 2,950.90 — **the level fell 0.9% overnight even though the change print is flat.** S&P +0.09%, Nasdaq −0.19% |
| SPY / IWM | **762.40 (−0.46%)** / **290.64 (−1.37%)** | Wednesday's settled closes. 🚨 **Factor −0.91% — the largest single-session drag against Rocket in two weeks** |
| Gold / Dollar | 4,435.40 (+0.44%) / 98.78 (+0.01%) | Gold bid, dollar flat — the inflation trade intact on all three legs |

### The inflation trade is now three-for-three going into the print that tests it

Energy at a run high, the 10-yr through its trigger for a seventh session, gold bid, dollar
flat — every leg this file tracks points the same way, and the **August CPI lands tomorrow
at 8:30 ET as the last data the FOMC sees before 9/16.** For a week the setup has been
"three inputs pointing at a September hike"; tomorrow is when the market gets to reprice it
in one 30-second gap.

**The designed response for the core remains no action.** The core carries no trailing stop,
backed by 33 years of SPY testing in which every stop configuration lost to buy-and-hold.
**A live flag is not a licence to override a tested design**, and this is recorded as a
decision, not an omission.

**For satellites it is the opposite** — this is precisely rule 29's gate, and it did real
work today: it is one of the two binding kills on DBI (the only live name on the board) and
it independently closed IRD's day-2 window.

### Factor watch

🚨 **IWM −1.37% vs SPY −0.46% = −0.91% of factor on Wednesday**, carried at 93.7% core
weight ≈ **−0.85% on the book** — Rocket's whole day, since there are no satellites.
**Lesson 28 bars booking a one-session move as information**, and it is being honored here
in the unfavourable direction exactly as it was honored on 9/08 in the favourable one. But
note the *direction* is the same as the six-week drift (−2.50% since rebase), and that
figure is the one that matters. It belongs in `weekly_review`.

🚨 **`weekly_review` for W36 (due Fri 9/04) STILL has not run — THIRD session flagging it.**
No `memory/weekly_reviews/2026-W36.md`; no 9/04 `market_close` entry in `trade_log.md`.
W37's review is due **tomorrow, Fri 9/11**. The hand-built Rocket-vs-SPY chain is now
**nine sessions stale** (last good number: 8/28 W35, −2.51%). Lesson 47 /
[[launchd-quota-contention]].

### Instrument health

✅ **`market_data.py macro` clean for an EIGHTH straight session** — every field populated.
✅ **`eligibility`: 15 requested → 15 returned** (lesson 43 count held, run against full output).
✅ **Nasdaq earnings-calendar API delivered on its third use** — **41 reporters for 9/09,
39 for 9/10**, with market cap and BMO/AMC in one call. It produced **three in-universe
survivors** on a session where the scanner's overlap tier was **zero usable names**
(BNC = crypto-treasury mandate kill, LPA = Costa Rica domicile mandate kill).
🚨 **Lesson 17a, TWELFTH straight demonstration — two sign flips.** `top_movers` printed
**QUIK "$11.35, +5.8%"** against a real settled bar of **$10.73, −2.01% at 26% of range on
216,600**, and **NMAD "$4.00, +7.8%"** against **$3.71, −3.89% at 0% of range on 188,800**.
**Both names also fail the 300k volume gate outright.** 12 of 20 `top_movers` rows carried
RelVol `—` or `0.0x`; **19 of 20 `unusual_volume` rows were below 1.0×.**
⚠️ **SHOE is the "right by accident" case**: the scanner's −13.1% *is* a real move (a 6:10 AM
guidance cut), but it is still an extended-hours quote in a `Change %` column.
🚨 **NEW — `positions` / `portfolio_snapshot.py` rounding cost a wrong rebalance verdict.**
9/09's `market_close` struck its band check on **"raw qty 10 sh"**; the broker API returns
**9.8636**. Corrected, IWM was **2.01% over target — inside the band**, not 3.28% outside.
**This is lesson 24 exactly, firing on the same field it was written about.** See
`research_log.md`; the deferred SELL is withdrawn.

---
