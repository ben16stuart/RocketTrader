# Rocket Lessons Learned

Read every session. **Compressed 2026-09-26 (W39). Full text, worked examples and tallies for
every rule number are in `memory/archive/lessons_history.md`.** Rule numbers are kept so
old references still resolve. **New lessons must replace a check or state what they let
through.** Tool defects go under Instruments.

## Standing Rules — Trading
1. **No named, dated catalyst = no trade.** Volume alone is the pump shape (rule-1 AVOID).
2. **Enter on day 2** (same-day 0-for-3, day-2 2-for-3). 2a: 9:30–9:45 range >10% → defer. 2b: the 9:45–9:50 bar must close in its upper half. 2c: gap 20–35% = gap-and-go, >35% = day 2 only. 3: gapped >25% and closed above the midpoint → the open is the entry (within 10% of the prior close).
4. **Close below the midpoint on heavy volume = distribution = dead**, whatever the catalyst.
5. **A beat without a raise disqualifies.** 5a: size the raise as a %; <1% is cosmetic (PD, CHPT, SWBI, AVO). 5c: check the guide against the quarter just reported. 5d: check pass-through against the company's own prior guide. 5e: a one-off bigger than net income IS the beat. 5f: a reaffirmed or reinstated guide is a 0% change. 5g: KMTS (+2.9%, 284% pass-through) shows what a real raise looks like.
6. **P2 is not a substitute for a failed P1.** An open slot is not a thesis.
7. **Rank on the balance sheet.** A contract far larger than the company's cash means the catalyst is a dilution event. 7b: a circular counterparty voids it.
8. **Dilution check runs first.** A 403 is not clean. Grade the structure (VWAP converts are a kill; an undrawn shelf with <1yr runway is a risk). 8b: an S-8 is not an offering. 8e: a "cash-rich" PR can be advertising the dilution that created the cash.
9/10. **Short float >15% + catalyst = squeeze flag.** Sub-$3 = trap; watch names within 5% of the floor.
11. **Analyst ladder:** strike +15% and +25% against a **dated** consensus. If the Street's highest target is below +15%, it's the strongest kill signal on the book. An un-runnable ladder = FAIL.
27. **A tiny range on huge volume means a pinned deal price** (tender, merger-of-equals). Check high−low first.
28. **A one-session factor move carries no information**; read it weekly.
29. **The event calendar is a gate.** A trailing stop can't protect against a data gap. No entries into a binary readout, or on FOMC day.
30. **Read the transaction code and size, then the 10b5-1 flag** (read the raw Form 4 XML). A Form 144 is supply, not dilution.
31. **Mandate exclusions** (crypto treasuries, etc.): check the mandate before the chart.
32. **Only override a trailing stop >2% away** (32a). Grade counterfactuals against the actual stop and the actual low (32c).
33/34. **Date the news against the bars** (a search result is not a date). Flags near a threshold stand down on a trend, never on one print.
35. **A correct rule can cost money for a while.** Record the tally and don't relax it on one outcome.
36/53. **Name which constraint bound the board on this session:** board quality, stop fit, or mandate. Re-measure it every session; don't carry it over.
37/40/45/51/54c. **Stop fit = max drawdown from the running high on 5-min bars**, not range ÷ 7%. Forecast catalyst-day range from the name's own history (45), and grade the forecast (tally so far: 5 right, 3 misses in both directions). A range kill converts to a date (day 2); a price-action kill closes the name (42d/45e).
38. **"Could not confirm" = FAIL.** Prove the source isn't broken (run a control) before believing a blank.
39. **Rocket's own notes are claims, not facts.** Re-verify anything copied forward.
41. **Source rung-1 from the earnings calendar before the screeners**, and from the FDA/regulatory tape. A blank board built on a degraded instrument is not a real absence (41b).
42. **Pre-commit kill/pass conditions as SHAPES, not levels, before the evidence arrives.** Independent gates don't net out (42a). Validated on IRD, ELMT and PRME (68).
46. **Use median ADV, never the mean.** Any catalyst, IPO or atypical window contaminates the mean. Read the last 5 sessions. A wide premarket spread only counts if the median also fails.
48f/54b. **Say which claim a kill makes:** "can't hold it" or "it will fall." Say which claim a correction supports: "number was wrong" or "fixing it makes money."
49. **Undisclosed deal terms = FAIL.** Headline size ≠ committed size (an IDIQ is a ceiling; an MOU is $0). Grade dilution against the float.
57. **Only the issuer's filing confirms a catalyst's CONTENT.** Check the 8-K Item: 7.01 (furnished) vs 1.01 (material agreement).
60. **A blank `stateOfIncorporation` on a recently renamed shell = FAIL.** Serial rebrands into a hot story are a second kill.
62. **Law-firm "investor alerts" are ads.** Date the underlying event.
65. **The Nasdaq calendar's eps fields can turn a miss into a beat.** Always read the 8-K exhibit for revenue, EPS basis and the guidance verb.
67. **(open)** The midday "−5% = cut" rule conflicts with 32a when the stop is <2% away. Escalated. Held RARE 9/25 under 32a.
🆕 70. **Name the prior SETTLED close in the entry log line and quote today's % against it** (2026-09-26, RARE). Market_open 9/23 logged "$15.06, +2.8%, fresh weekly high" against 9/21's close ($14.65). The real prior close was 9/22's $15.615 (high $16.12), so the entry was **−3.6% on the day, into the fade after the breakout**. It then closed at 35% of range. Premarket had the right number; the next session didn't carry it. **This check makes a good day-2 entry easier to see, as well as blocking a bad one.**

## Standing Rules — Satellite floor
56–69 (breach logs). **One line per breach in session notes; a breach isn't a lesson.** The design problem is escalated (W39 §6): 3 × 15% = 45% < 50%, so the floor needs all 4 slots full at max size. **Rule 8 relaxes catalyst quality, which is rarely what binds.** Widen the SOURCES (calendar, FDA, analyst), not only the screeners. A missing session is not a confirming data point (58).

## Standing Rules — Universe gates
13. **Compute cap at the price you'd pay, and check the +25% target vs $2B** (escalated; this blocks names near the ceiling). 14. ADV near the gate → re-verify on the median. 52c. **Domicile = state of incorporation** (EDGAR `stateOfIncorporation`), ruled 9/17.

## Standing Rules — Instruments and tooling
15. `nan` / `0.0x` / blank = a broken instrument. 16. Verify a fix on a live artifact. 17. **The scanner is a name source only.** Its price, Change % and RelVol fields break without warning and uncorrelated (17f/17g/64). Reconcile against settled bars and `detail`. 55b/59: arithmetic that reconciles doesn't prove a trade happened. 66: `sip` returns 403 on this plan, so premarket quotes are indicative only.
18–20. `close` fully liquidates; use `sell SYMBOL QTY` for partials. Trailing stops need whole shares. Log exits the same day.
21/47. **Token budget is a trading risk.** Fewer than 5 searches → do them inline. A starved routine leaves a silent gap: grep for the expected dated entry, and fix the gap rather than just flagging it (47c).
23. **Rocket can't measure Rocket from the snapshot.** Use the hand-built book (23a), carried forward by fills.
24. **Display share counts are rounded.** Pull the raw qty from `GET /v2/positions` for any arithmetic. The snapshot's weekly trade counter is broken; count trades from `trade_log.md`.
25. If the snapshot fails on one endpoint, curl that path; don't write the session off.
43. **Count output rows against tickers requested** on every multi-ticker call. `eligibility`/`price` silently drop rows and still exit 0.
44. **Name the rebalance basis** (slice vs book). Escalated.
50. **Continuous futures roll**, so a naive % is a calendar spread. `macro` corrects it and prints naive vs true.

## Rules From Real Trades — 5 most recent
- **W39 (9/21–25):** D. Book −0.99% vs IWM −0.75%. Satellites averaged 8.8% (5/5 sessions below the floor). RARE was entered on a stale reference close (70). PRME Gate A and the SCHL 8-K check each kept a loser out.
- **W36–W38:** No satellites. The chain was rebuilt in W39 (+0.48% vs IWM combined, all from cash timing). The reviews never ran.
- **W35 (8/24–28):** −2.51% vs SPY, 65% of it factor. PD (a beat-and-raise) was never on the board, which is why rule 41 exists.
- **W34 (8/17–21):** +2.03% vs SPY, all from OMER. ETON lost $25.83 on a discretionary exit ahead of an untouched stop, which is why rule 32 exists.
- **W33 (8/10–14):** Research 4/4. The losses were execution (OMER monitor miss, FF P2, VELO same-day).
