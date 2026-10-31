# Rocket Lessons Learned

Read every session. Full text for every rule number (incl. those retired at W44): `memory/archive/lessons_history.md`.
**New lessons must replace a check or state what they let through.** Tool defects go under Instruments.

> 🔁 **2026-10-17 — REBUILT AS RANK → JUDGE (Ben: "rebuild rocket tonight").** Read CLAUDE.md
> "How Rocket Picks Stocks" before anything else. Selection = `scripts/rank_screen.py` (6-1 month
> momentum ÷ vol, ~1,800 small caps $150M–$10B) → your judgment → up to 8 satellites at ~12%, 25%
> trailing stop, no profit ladders, exits on stop / thesis break / weekly rank > 25. Every BUY, top-8
> VETO and non-stop EXIT is logged with `scripts/candidate_ledger.py` and scored vs IWM.
> Why: 22 straight sessions below the 50% floor (9/17–10/16), 0% in stocks after 10/5. The checklist
> below rejected nearly everything and nothing measured what it rejected.
> - **Data-integrity rules stay BINDING** (date every bar, verify the settled close, scanner % is not data,
>   instruments section).
> - **Selection rules are ADVISORY** (1 named-dated catalyst, 2 day-2 entry, 4, 5, 13 cap math, 14 ADV,
>   stop-fit 54c, 67 midday cut, and any rule that rejects a candidate). They may inform a logged, scored
>   VETO; one regains hard-veto power only if the ledger shows its vetoes underperformed the BUYs (n ≥ 10).
> - Stops: **25% trailing, never tightened**. Rules citing 7%/5%/3% stops or −5% cuts are superseded.
> - Hard vetoes that remain: non-US incorporation (52c), binary event ≤10 trading days, earnings ≤5,
>   fresh dilution / going concern / pinned takeover / reverse split / pump (judgment, logged).

## Standing Rules — Trading
5. **A beat without a raise disqualifies.** 5a: size the raise as a %; <1% is cosmetic (PD, CHPT, SWBI, AVO). 5c: check the guide against the quarter just reported. 5d: check pass-through against the company's own prior guide. 5e: a one-off bigger than net income IS the beat. 5f: a reaffirmed or reinstated guide is a 0% change. 5g: KMTS (+2.9%, 284% pass-through) shows what a real raise looks like.
8. **Dilution check runs first.** A 403 is not clean. Grade the structure (VWAP converts are a kill; an undrawn shelf with <1yr runway is a risk). 8b: an S-8 is not an offering. 8e: a "cash-rich" PR can be advertising the dilution that created the cash.
27. **A tiny range on huge volume means a pinned deal price** (tender, merger-of-equals). Check high−low first.
29. **The event calendar is a gate.** A trailing stop can't protect against a data gap. No entries into a binary readout, or on FOMC day.
31. **Mandate exclusions** (crypto treasuries, etc.): check the mandate before the chart.
33/34. **Date the news against the bars** (a search result is not a date). Flags near a threshold stand down on a trend, never on one print.
35. **A correct rule can cost money for a while.** Record the tally and don't relax it on one outcome.
38. **"Could not confirm" = FAIL.** Prove the source isn't broken (run a control) before believing a blank.
39. **Rocket's own notes are claims, not facts.** Re-verify anything copied forward.
46. **Use median ADV, never the mean.** Any catalyst, IPO or atypical window contaminates the mean. Read the last 5 sessions. A wide premarket spread only counts if the median also fails.
57. **Only the issuer's filing confirms a catalyst's CONTENT.** Check the 8-K Item: 7.01 (furnished) vs 1.01 (material agreement).
60. **A blank `stateOfIncorporation` on a recently renamed shell = FAIL.** Serial rebrands into a hot story are a second kill.
62. **Law-firm "investor alerts" are ads.** Date the underlying event.
65. **The Nasdaq calendar's eps fields can turn a miss into a beat.** Always read the 8-K exhibit for revenue, EPS basis and the guidance verb.
70. **Name the prior SETTLED close in the entry log line and quote today's % against it** (2026-09-26, RARE: logged "+2.8%, fresh high" vs the wrong close; it was −3.6%, a day-2 fade). Applied cleanly on AGEN 9/29. It makes a good day-2 entry easier to see, as well as blocking a bad one.

## Standing Rules — Satellite floor
56–69 (breach logs). **The IWM cap was lifted 2026-10-06 (Ben).** An unfilled floor sits in IWM, never in cash. The 50% floor is still a guardrail: it is measured, flagged every session and escalated under rule 8. To fund a satellite, SELL the IWM shortfall right before the BUY (log it as `CORE FUNDING`). Log one line per breach in the session notes; a breach is not a lesson. A missing session is not a confirming data point (58). (The 3 × 15% < 50% design note was retired 10/17: 8 slots at 12.5%.)

## Standing Rules — Universe gates
13. Universe is $150M–$10B since 10/17; **the cap gate is entry-only** (W44: TXG drifted over $10B while #1; growth is not an exit). 14. ADV near the gate → re-verify on the median. 52c. **Domicile = state of incorporation** (EDGAR `stateOfIncorporation`), ruled 9/17.

## Standing Rules — Instruments and tooling
15. `nan` / `0.0x` / blank = a broken instrument. 16. Verify a fix on a live artifact. 17. **The scanner is a name source only.** Its price, Change % and RelVol fields break without warning and uncorrelated (17f/17g/64). Reconcile against settled bars and `detail`. 55b/59: arithmetic that reconciles doesn't prove a trade happened. 66: `sip` returns 403 on this plan, so premarket quotes are indicative only.
18–20. `close` fully liquidates; use `sell SYMBOL QTY` for partials. Trailing stops need whole shares. Log exits the same day.
21/47. **Token budget is a trading risk.** Fewer than 5 searches → do them inline. A starved routine leaves a silent gap: grep for the expected dated entry, and fix the gap rather than just flagging it (47c).
23. **Rocket can't measure Rocket from the snapshot.** Use the hand-built book (23a), carried forward by fills.
24. **Display share counts are rounded.** Pull the raw qty from `GET /v2/positions` for any arithmetic. The snapshot's weekly trade counter is broken; count trades from `trade_log.md`. 25: if the snapshot fails on one endpoint, curl that path.
43. **Count output rows against tickers requested** on every multi-ticker call. `eligibility`/`price` silently drop rows and still exit 0.
44. **Name the rebalance basis** (slice vs book). Escalated.
50. **Continuous futures roll**, so a naive % is a calendar spread. `macro` corrects it and prints naive vs true.

## Rules From Real Trades — 5 most recent
- **W44 (10/26–10/30):** A−. Book **+7.32%** vs IWM +1.30% (**+6.02 pts**). Satellites **96.1%**, 0/5 breaches. REPL alone ≈ +6.5 pts. **One winner made the week, so grade the process, not the P&L.** Without REPL the book ≈ IWM, and the book fell 2.7× IWM on Friday (−4.39% vs −1.65%). Ledger 5d: VETO +4.72% (11) > BUY +0.76% (8), but it is spread across categories (HC cap n=6), so no category reaches n ≥ 10 and there is no change. **Watch the HC sector cap first:** if its vetoes still beat the BUYs with n ≥ 10 at 10d/20d, escalate to Ben (it is a Hard Guardrail, not the ledger's to loosen alone). Lets through: nothing new; it names the next test.
- **W43 (10/19–10/23):** B−. Book +1.79% vs IWM +1.96% (−0.18 pts, the cash buffer in an up week). Satellites **56.8%**, 0/5 breaches. The first rank → judge week: 5 buys, 0 exits. **A pre-entry check handed to market_open is done BEFORE the order, or the name is skipped** (REPL was bought 10/19 with its FDA outcome "not verified"; it was approved, so no harm, but the check was skipped). This extends the handed-off-check rule below to entries. Lets through: every ranked name with no open check.
- **W42 (10/12–10/16):** F. Book −2.75% vs IWM −3.05% (+0.30 pts, all cash buffer). Satellites **0.0%** at 5/5 closes. Rule 8 boarded 7 conditional plans and filled 0. **The kill counterfactual went 3 up / 3 down / 1 flat vs a −3% IWM week, so the shape gates were a coin flip, not an edge.** That overturns the W40/W41 "filters aren't the leak" read and is the evidence behind the rank → judge rebuild. Lets through: everything the ranking surfaces that clears the hard vetoes.
- **A handed-off check is owed by the routine it was handed to** (10/09: market_close was told to grade KOPN's close and didn't). If a plan says "checked at close", that close's session note must show the result. If it doesn't, the next session does the check first.
- Breach log: 20 consecutive breaches through 10/16 (archived). The streak ended 10/19. W43 and W44 met the floor at 10/10 closes. Append one line per new breach below.
