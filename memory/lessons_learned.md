# Rocket Lessons Learned

Rules derived from real trades. Read every session.
Full-text versions and older observations: `memory/archive/lessons_history.md`.

⚠️ **Renumbered 2026-08-14 (Week 33 review).** Archived notes before this date use the old
scheme, where old-24 = "a deferred intraday decision needs a completion check" (now **25**)
and old-25 = "the weekly trade counter is broken" (now **26**). Cite by text, not by number,
when writing anything that will be read after a future renumber.

---

## Standing Rules — Trading

1. **No catalyst = no trade.** Volume alone is never enough.
2. **🥇 ENTER ON THE SECOND DAY.** Same-day entries are **0-for-3** (CSTL, FF, VELO); second-day continuations are **2-for-2** (MRLN, OMER). Both same-day losses failed identically — Rocket bought the retrace of a failed opening spike and called it a base.
    - **2a. Opening-range gate (2026-08-14):** if the **9:30–9:45 range exceeds 10% of price**, there is no tradeable 9:45 base — **defer to day 2.** VELO ran $17.61→$14.35 (22.7%) in ten minutes; the "base" at $15.27 was the middle of a range. Deferring would have bought 8/13's $14.95 open, now $16.16 (**+8.1%**).
    - **2b. The 9:45–9:50 bar must close in the upper half of its own range.** OMER's did ($17.02/$17.38/$16.92/**$17.33**, 1.6x 5-min volume). That is what a base looks like.
    - **2c.** Gap 20–35% = gap-and-go, not a chase. **Gap >35% = second-day only.**
3. **Second-day rule**: gapped >25% yesterday + **closed above the day's midpoint** → today's open IS the entry, within 10% of prior close. Do not wait for a pullback that won't come.
4. **Close-position-in-range is the tiebreaker** (2026-08-07). Below the midpoint on heavy volume = distribution = dead, catalyst regardless. ASPN (28% of range) and EVH (9%) both had real news and both died; QNST/RCEL/CRSR closed 86–92% and held. **Validating the catalyst is no longer the hard part — surviving day one is.**
    - **4a. Applies to same-day entries too, and it beat Rocket's own stop** (2026-08-12, re-verified 8/14). VELO closed at ~25% of its post-entry range; Rocket closed it same-day at $15.09 for −$5.40. The 7% trail sat at **$14.72** and **8/13's low was $14.65** — holding would have stopped out for **−$16.50**. The discretionary close won by $11.10 *even though VELO later recovered to $16.16.* Run the range check at market_close on every satellite.
    - **4b. Corollary — a 7% trail is inside the noise band of a 20%-range stock.** On such a name the stop is a coin flip, not risk management. That is an argument against entering, not for a wider stop.
5. **🚫 A beat WITHOUT a raise is a DISQUALIFIER, not a demotion** (2026-08-14). 3-for-3 as a fader: SVCO, CVRX, FF. FF closed day one at 30% of range and went $6.37→$5.85→$5.68→$5.59.
6. **🚫 P2 is not a substitute for a failed P1** (2026-08-14). If the P1 fails its gate at the open, the default is **no satellite**, not the next name down. FF was ranked P2 in premarket *for the exact reason it lost* (no raise, no coverage) and was entered only because APEI failed and a slot was open. **A slot being open is not a thesis.**
7. **Rank on the BALANCE SHEET, not the growth rate.** Growth makes a stock gap; funding structure decides whether it holds the gap over a 1–5 day hold.
    - **7a. 🆕 Score the announcement-to-balance-sheet ratio** (2026-08-18). When a contract/partnership catalyst is **orders of magnitude larger than the company's cash**, the catalyst *is* the dilution event — delivering it requires capital the company does not have. **AGPU: $21.9M cash and falling equity against $1.3B of announced contracts (~60x), with an S-3 effective three weeks earlier.** DUOT: $2.7M quarterly revenue against a $500M contract needing a 55 MW build. **Both had strong price action; both were uninvestable.** Divide the announcement by cash before believing it.
    - **7b. 🆕 A circular counterparty voids the contract as evidence.** AGPU pays DUOT to host **while contemplating minority equity in the DUOT SPEs it is paying** — each books the other's side as a headline win. **When a contract's counterparty is also its financier, the revenue is not independent.** Skip both sides, never just the weaker one.
8. **The dilution check runs FIRST and is Rocket's most profitable rule** — one search. Kills: SVCO, STLN, NNBR, RCEL, NRGV — all then traded badly. **A 403 or paywall is not a clean bill of health.**
    - **8b. 🆕 An S-8 is NOT an offering — do not let it trip an exit trigger** (2026-08-18). OMER's 8/13 S-8 was reported as a "$142.67M ESOP-related shelf registration"; it registers **employee-benefit-plan shares** and does **not** draw the ATM. The offering trigger is a **424B5 or an announced deal**, not any filing with "registration" in the headline. **Cuts both ways: read the form type, not the headline.** A false positive sells a good position; a false negative holds a diluting one.
    - **8a. Grade the dilution *structure*, not its existence** (2026-08-12). Worst → best: **(i) converts struck at a VWAP-DISCOUNTED price** (holders are paid to short strength — automatic kill, e.g. NRGV); **(ii) a drawn shelf with <1yr runway** (RCEL — kill); **(iii) an undrawn ATM with multi-year runway** (VELO, OMER — a risk to size around, not a disqualifier); **(iv) a completed raise months old** (not an overhang at all). **Always date the raise.**
9. **Short float >15% + a catalyst = size up.** Run the check on **every** board candidate, not just the ones that look like squeezes — it is one field in data already being fetched.
10. **Sub-$3 stocks are traps.** Watch names sitting within ~5% of the floor.
11. **The analyst-ladder check is Rocket's best entry filter — now 4-for-4.** Strike both profit targets (+15%, +25%) against a **dated** consensus before the open, every name, every session. A capped ladder is close to sufficient for a skip; an uncapped one is necessary but not sufficient. Kills: QNST (−5.1%), CRSR (−4.5%), HLIT, **CURI (−11.0% on 8/14, closed at 4% of range)**.
    - **11a. An undated analyst headline is not evidence** — resolve it against a dated consensus page. "Barrington raised QNST to $29" was a prior period; the current page showed a $24 reiteration.
    - **11b. 🆕 An UN-RUNNABLE filter is a FAIL, not a pass** (2026-08-14). FF had **no analyst coverage at all**, so the ladder check could not run — and its absence was scored as an absence rather than as a skip. Same logic as rule 8's "a 403 is not a clean bill of health."
12. **Extreme moves (+100%+) with real catalysts are not noise** — but never chase the spike. Watchlist and wait 1–3 days. **Missing real catalysts has a cost too** — apply discipline to entry price, not to whether to trade at all.

## Standing Rules — Universe gates

13. **Compute market cap at the price you would PAY, and confirm the +25% target still clears $2B.** ⚠️ **Now costing real names**: APPS, BW, HLIT, ETON and UMAC were all killed or capped in two weeks, several the best catalyst of their day. **Escalated to the user as an open question — not overridden.**
14. **ADV within ±10% of the 300k gate → re-verify against raw data before rejecting** (RCEL read 295k; the real figure was 302,064). Also applies in reverse: VOGX's "382,500 ADV" was computed off a two-day sample against 81,000 real volume.

## Standing Rules — Instruments and tooling

15. **A metric that renders as `nan`, `0.0%`, or `unknown` is a broken instrument, not a cosmetic glitch.** Silent degradation is the failure mode that costs money; loud errors get fixed.
16. **Verify a fix against a live artifact before declaring the problem solved.** The core sleeve was declared to have fixed idle cash on 7/28, before one rebalance had run. Cost: −0.49% in Week 32. ✅ **Closed 8/10–8/14**: three fractional rebalances, all within $0.20 of target, cash drag down to −0.04%.
17. **Pull raw 5-min bars to judge a base; raw daily bars for carry-overs. The scanner is a NAME SOURCE**, and its prices/`Change %` are extended-hours quotes.
18–19. **`alpaca_client.py close SYMBOL` always fully liquidates** — no `--qty`, and it silently ignores one. Use `sell SYMBOL QTY` for partial reductions; verify `qty` in the returned order JSON. **Fractional orders work; trailing stops reject fractional qty by design** — size satellites in whole shares, only the stopless IWM core may be fractional.
20. **Log exits the same day they happen.** CAMP was closed pre-merge with no price, date or reason and is permanently unrecoverable.
21. **🚨 Token budget is a TRADING risk.** Bull and Rocket share one Claude quota across 10 launchd jobs. **<5 searches → inline, never a subagent** (~171k tokens of overhead each).
22. **A plist that exists is not a job that runs — check `launchctl list`, not `ls`.** Midday has not executed since **2026-06-15**.
23. **🔴 Rocket cannot measure Rocket.** `portfolio_snapshot.py` derives Rocket's return from a fixed 30% of the *shared* account — algebraically the whole account's return, Bull's P&L included. Snapshot reads **+0.10% vs SPY since rebase; the truth is −0.78%.** The error grew 67bp → **88bp** in one week. **Trust only the hand-built weekly attribution.**
    - **23a. 🆕 The hand-built BOOK, not the slice, is the valid daily base** (2026-08-14). Every daily note Mon–Fri chained off the contaminated slice ($3,152.62) instead of the W32 review's hand-built book ($3,135.02), and so reported +0.09%→+0.53% all week against a true −0.78%. **Carry the hand-built book forward transaction by transaction.**
24. **`positions` and `portfolio_snapshot.py` round share counts for display** (IWM printed "10" against a real 9.5031). Pull the raw position before computing the rebalance band.
25. **🚨 A deferred intraday decision needs its own completion check** (2026-08-13). `market_open` handed OMER (P1/HIGH) to a monitor that died silently; no midday exists to catch it, and it ran **+26.6% untraded — ≈−0.70% of book, more than both losing trades combined.** **Absence of a session_notes entry between market_open and market_close on a P1 name is itself the failure signal.** ✅ Closed out 8/14: the GO/NO-GO was made and logged explicitly at 9:45 off raw bars.
26. **`portfolio_snapshot.py`'s weekly trade counter is broken and undercounts to zero** — `count_weekly_trades()` needs `line.split("—")` to yield ≥3 parts but trade_log headers contain one em-dash. The hardcoded cap (**3**) also doesn't match the real guardrail (**5**/week). **Count trades from `trade_log.md` by hand.**

## Rules From Real Trades

### 2026-08-14 — Week 33: beat SPY on pure beta, lost −0.52% on stock selection
- ❌ **The +0.15% headline was 100% IWM factor.** Real alpha **−0.52%**, the worst satellite week yet, on an **0-for-2** record. Cumulative real alpha since rebase: **−0.65%** — never yet positive.
- ✅ **Research quality is now a strength** — 4/4 skips validated (CURI −11%, HLIT, CAPR, IMXI), ladder filter 4-for-4. **The losses were execution, not analysis. Do not loosen the research bar.**
- ❌ **Ranked by cost**: the 8/13 OMER miss (≈−0.70%, infrastructure) > FF (−0.39%, discipline) > VELO (−0.17%, entry timing).

### 2026-08-12 — VELO (−$5.40, −1.18%): right research, wrong day
- ❌ Beat-and-raise, uncapped ladder, 33% short float, dilution graded clean — and it still lost, because the entry was into a 22.7% opening whipsaw. **See rules 2a and 4b.**
- ✅ The same-day close beat Rocket's own trailing stop by **$11.10**.

### 2026-08-11 — FF (−$12.24, −2.57%): the P2 that should never have been entered
- ❌ Entered as a **substitute** for a failed P1, with a known-second-tier catalyst (no raise) and an un-runnable ladder check. **See rules 5, 6 and 11b.**
- ✅ **The 7% trail did its job perfectly** — out at $6.44, and FF is **−13.2% below the exit** three sessions later.
