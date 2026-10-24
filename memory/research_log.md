# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines. Archive resolved or stale
entries to `memory/archive/research_log_history.md` (the W41 board was archived there 2026-10-10).

---

> 🔁 **2026-10-17 — REBUILT AS RANK → JUDGE (Ben: "rebuild rocket tonight").** Read CLAUDE.md
> "How Rocket Picks Stocks" before anything else. Selection = `scripts/rank_screen.py` (6-1 month
> momentum ÷ vol, ~1,800 small caps $150M–$10B) → your judgment → up to 8 satellites at ~12%, 25%
> trailing stop, no profit ladders, exits on stop / thesis break / weekly rank > 25. Every BUY, top-8
> VETO and non-stop EXIT is logged with `scripts/candidate_ledger.py` and scored vs IWM.
> Why: 22 straight sessions below the 50% floor (9/17–10/16), 0% in stocks after 10/5. The checklist
> below rejected nearly everything and nothing measured what it rejected.
> The Week 43 board and the daily notes from 10/19–10/23 were archived to `archive/research_log_history.md` on 2026-10-24.

## Watchlist — Week 44 (Mon 10/26 – Fri 10/30), built at W43 review Sat 10/24  ← CURRENT

Book (10/23 close): satellites 56.9% (5 held), IWM 3.7163 sh ≈ $1,025 (33.8%), cash 9.3%. Slice $3,029 → 12.5% cap ≈ **$379**.
The weekly entry cap resets to **5**. HC cap 3 (**full**: TXG/REPL/NEO). Tech cap 3 (NSIT + 2).
Ranking data as of 10/23 (713 eligible): TXG #1, REPL #2, NSIT #8, NEO #9, **DK #75**.

### Mon 10/26 — WATCHING (premarket confirms on Monday's ranking, then market_open executes)
1. **REPLACE DK → QMCO (rank 5, Tech).** First, market_open SELLs DK (4 sh): cancel its trailing stop, then `sell DK 4`.
   Log `candidate_ledger.py log DK EXIT "rank decay 75 > 25 at W43 review" --rank 75`.
   QMCO (Quantum Corp, DE): 6-1 +311%, vol 117%, short 59.6% (a squeeze flag, not a veto). Earnings 11/09.
   **Premarket owes:** (a) read the 8.01 items of the 10/09 and 9/28 8-Ks (5.02 exec changes); (b) date the "$54.7M term debt →
   senior secured convertible notes" exchange: inside 30d = fresh-dilution VETO; (c) going-concern language in the last 10-Q.
2. **FILL: GTLB (rank 17, Tech).** GitLab, DE, no filings ≤45d, earnings 12/01. The Strong Buy consensus is not a catalyst. Fine.
3. **FILL: CLDT (rank 25, Real Estate, hotel REIT).** MD (US). 8-K 9/14 (5.02/7.01). Earnings 11/04 BMO (7 td). At the exit-rank edge:
   if Monday's ranking pushes it past 25, skip it rather than buy next week's replacement.
- **VETOs:** UTZ #18 is LOGGED (pending $14.25 cash take-private, DEFM14A 10/02). APPS #16 (earnings 11/02 ≤5 td): premarket logs it.
  QLYS #20 is blocked by the Tech cap once QMCO and GTLB fill. HC names (OABI #3, XGN #4, CDNA #6, TWST #7, …) fail on the HC cap,
  and SMWB #10 and ABCL #12 FAIL non-US HQ. **Premarket must log every skipped top-8 name as a VETO** with Monday's rank.
- **Slot 8 stays empty.** Nothing ≤25 is left that passes. Projected satellites ≈ **83%** (4 held ~47% + 3 × ~12%).
  CORE FUNDING: sell ≈ (3 BUYs − DK proceeds − cash above the 10% buffer) of IWM right before the buys. IWM will be small after that. That is expected.
- No entries Wed 10/28 (**FOMC**, statement 2:00 PM ET).

### Held satellites — thesis cards (break = specific news, never price)
- **TXG** (5 @ $69.59, HC): Q2 beat + raised FY outlook, Atera demand. Break: a Q3 (11/05 AMC) guide cut. Cap $9.3B, near the $10B line.
- **REPL** (32 @ $10.99, HC): RP1 Accelerated Approval (Aug). Break: a 424B takedown off the 8/14 S-3ASR, a weak launch, FDA safety action. **Earnings 10/28.**
- **NEO** (21 @ $16.83, HC): Q2 beat + raise, prelim Q3 ~$209M, FY guide up. Break: a guide cut. **Earnings 10/28 AMC** (±16% implied, held through it).
- **NSIT** (2 @ $162.53, Tech): Q2 beat, FY26 EPS guide raised to $12.20–12.70. Break: a guide cut. Earnings 11/05.
- **DK** (4 @ $79.18, Energy): **EXITING Mon 10/26 on rank decay.** Thesis lesson: a refiner is short crude (strategy.md TESTING).


### Open escalations awaiting a user decision
**RESOLVED 2026-10-17 by the rank → judge rebuild:** #1 (8 slots at 12.5%: the floor needs 4–5 names, not
4/4 at max), #4 ($2B ceiling → $10B, IWM's range), #5 (midday −5% cut retired; 25% stop), #7 (the daily ntfy
now uses `agent_performance.py`, Rocket's own book from fills: +0.88 pts vs IWM since 7/20 on 10/16, which
matches the hand-built +0.93%). #2, #3 and #6 are advisory under the new process.
1. **Satellite floor arithmetic** — IWM cap LIFTED 2026-10-06 (Ben chose option 1). RULED 2026-10-06: per-slot cap (15%) and 50% floor stay UNCHANGED —
   no proven edge to size up (last 2 entries stopped out); revisit after >=8 closed satellite trades.
2. **Rebalance basis** (lesson 44). Now binding — IWM fills to the 90% line.
3. **ADV gate vs account size** (46f).
4. **$2B ceiling vs the +25% ladder** (13). It blocks CNXC and PRGS this week.
5. **Midday −5% cut vs stop distance** (67).
6. **`sip` data entitlement for premarket liquidity checks** (66).
7. 🆕 **Daily ntfy "Rocket vs IWM" is wrong (W41).** `portfolio_snapshot.py` computes it as 30% of the SHARED account vs
   the rebase, so it includes Bull's P&L. It printed +6.6–7.3% all week; the hand-built figure is **+0.93%**. Ask Ben whether
   to fix the script (a hand-built book carried by fills) or drop the line from the ntfy. Until then, never quote it.

### Standing category kills (full detail in archive)
Crypto/treasury (31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI, BKKT, UPXI, HSDT.
Non-US-incorporated (52c): KMTS, GLAS, NB, ADNT, DAVA. Liquidity: GLOO, TLYS, REF, OPTX,
SRZN, TTRX, IDT, TRAK, BSET. Pump/shell: GLND, GRML. **CLOSED:** PAAI (catalyst
falsified), PRTH (pinned deal), NUAI (mandated ATM), SCHL (miss + affirmed guide), PRME
(Gate A 9/25), MLKN (guide cut 9/22), XTND (undisclosed contract value, SPAC ADV).
