# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-14 Monday premarket (Week 38 day 1 — FOMC WEEK)  ← CURRENT

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

## Snapshot — 2026-09-11 Friday premarket (Week 37 day 4 — CPI MORNING)

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
