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
> The Week 46 board (11/09–11/13 daily notes, AMPL/PBF entry cards) was archived to `archive/research_log_history.md` on 2026-11-14.


## Watchlist — Week 47 (Mon 11/16 – Fri 11/20), built at the W46 review Sat 11/14  ← CURRENT

Book (11/13 close): 8 satellites ≈ 103% of a $2,925 slice. IWM 0. The 12.5% cap ≈ **$365**. The weekly entry cap resets to **5**.
Ranking data as of 11/13 (757 eligible): CDNA 2, AMPL 6, CAKE 8, GTLB 11, **NSIT 41, PBF 42, OABI 50, REPL 157** → all four replaced.
After the swap: HC = CDNA/TXG/IOVA (full). Tech = AMPL/GTLB/PAYS (full). Consumer Cyclical = CAKE/CBRL.

### Tue 11/17 premarket — no slots open, no picks
Ranking (11/16 data, 716 eligible): TXG 1, CDNA 2, IOVA 3, CBRL 6, CAKE 7, PAYS 10, AMPL 12, GTLB 18. All 8 are ≤ 25. Unheld top-8 names: HAE 4, UTZ 5, RCEL 8. With 0 slots open (and 4/5 entries used), nothing to pick or veto.
Holdings check: 8 searches turned up only stale or undated items. IOVA "equity raise" is old: EDGAR since 11/05 shows only Form 4 and 13G filings. No thesis breaks.

### Mon 11/16 — 4 replacements → premarket confirms on fresh data, market_open executes
**Order at 9:35:** (1) cancel the trailing stops on NSIT, PBF, OABI and REPL. Then `sell NSIT 2`, `sell PBF 5`, `sell OABI 70`, `sell REPL 32` (raw qty from `GET /v2/positions`, rule 24).
Log the EXITs: `candidate_ledger.py log NSIT EXIT "rank decay 41 > 25 at W46 review" --rank 41`, likewise PBF --rank 42, OABI --rank 50, REPL --rank 157.
Join the four sales in one trade_log header with **`+`** (rule 20b).
(2) Proceeds ≈ $1,738 cover all four buys (≈ $1,376), so no IWM funding sale. (3) BUY at market. (4) Place 25% trailing stops. (5) Log the BUYs. (6) market_close sweeps the ≈ $360 leftover into IWM.
**Size (re-run `size SYM ENTRY STOP` at the live price, STOP = ENTRY × 0.75):** TXG 6 · IOVA 45 · PAYS 36 · CBRL 5 (11/13: $58.19 / $7.76 / $9.52 / $66.95).
VIX 19.30 close 11/13. Over 25 means half size; over 30 means no new longs (the exits still happen and the proceeds go to IWM).
Skip a name that opens >8% above Friday's close on no news. If NSIT/PBF/OABI/REPL re-rank ≤25 Monday, **still replace them** (decay is judged on Saturday's data).

1. **TXG #1 (HC)** — DE. Q3 8-K 2.02 11/05, 10-Q 11/06. The 8-K 5.02 (11/02) **adds** 2 directors (read). No S-1/S-3/424B. Prior trade: stopped 11/02 @ $65.91; now $58.19. GO.
2. **IOVA #3 (HC)** — DE. Q3 11/05. 8-K 8.01: 10/29 Phase 2 lung data (already out); 11/05 corporate deck. Interim CEO (GC acting) is a note.
   **Premarket owes, before the order:** (a) ATM draws in the 11/05 10-Q's subsequent-events/equity note (a draw in the last 30 days = dilution VETO); (b) no PDUFA, AdCom or readout within 10 trading days (hard VETO). Fails → **HAE #4** (MA, earnings 2027-02-04, clean; 2 shares, whole-share cap).
3. **PAYS #9 (Tech)** — NV. Q3 8-K 2.02 11/09, 10-Q 11/10. No S-1/S-3/424B. Cap $541M, rev growth +43%. **Premarket owes:** read ex-99.1 and log whether the guide was raised (rule 5, advisory).
4. **CBRL #15 (Consumer Cyclical)** — TN. Earnings 12/09. Short 27%. DEFA14A 11/09 = proxy supplement on "blank check" preferred provisions.
   **Premarket owes:** one news search. Is there an activist fight, and is the meeting vote inside 10 trading days? This is judgment: log it either way. If vetoed: ELF #22, then LIND #35.
- ✅ **PREMARKET 11/16 CONFIRMED all four. Status: WATCHING (added 2026-11-16).** `rank_screen.py` is still on 11/13 data: TXG 1, IOVA 3, PAYS 9, CBRL 15, identical to the review. VIX 19.91 live means full size.
  - **IOVA**: the 10-Q shows the 2025 Jefferies ATM sold 8.67M sh for $87.9M net at $10.34 in Q3, and the agreement **terminated at 9/30 (fully used)**. No 424B/S-3 since 10/15, so no draw in the last 30 days and no fresh-dilution veto. The 10-Q says "no assurance" funds cover 12 months but then "we believe we have sufficient capital" with no "substantial doubt", so this is **not** a going concern. **Risk: a new ATM or offering is likely**, and if one is filed that is a thesis break. No PDUFA, AdCom or readout found within 10 trading days (the search's "PDUFA 11/25" is the 2023–24 lifileucel item, now approved). Break: a new ATM, S-3 or offering, or a failed readout.
  - **PAYS**: per ex-99.1 (11/09), the FY26 revenue guide of $114–117M is **reaffirmed (0%, rule 5f)**. Gross margin, net income, EPS and adj. EBITDA guides are **raised**. 113 plasma centers move to another provider in Q4. Rule 5 is advisory: logged as a note, not a veto. Break: a revenue-guide cut, or more center losses.
  - **CBRL**: the 2026 annual meeting is **Thu 11/19** (DEFA14A). It is a 9-director slate plus a shareholder (TAB) proposal on "blank check" preferred. **No 2026 Biglari contest on EDGAR** (no DFAN14A). The search's ISS/Glass Lewis/Egan-Jones withhold stories are the 2025 meeting (rule 33: date the news). This is not a binary price event, so PICK. Break: a guide cut at 12/09, an issuance, or a contested-control event.
  - **TXG**: no new filings since the review except a Form 4. GO.
- **VETOs LOGGED 11/16** (top 8 not held/bought): HAE #4 (HC cap), UTZ #5 (going-private pending; 8-K 8.01 11/13), ABCL #7 (FAIL, non-US HQ).
- ~~VETOs to log Mon (top 8 not held/bought):~~ HAE #4 (HC cap, if IOVA is bought), UTZ #5 (going-private, pinned), ABCL #7 (FAIL non-US HQ).
- **Binary events, held names, W47:** none. GTLB reports 12/01.

### Held satellites — thesis cards (break = specific news, never price)
- **CDNA** (4 @ $86.10, HC): Q3 rev +39%, 3rd straight guide raise. Patent appeal heard 11/09 (≈$96M at stake): check a ruling against its cash. Break: a guide cut, a Medicare/LCD reimbursement hit, an equity raise.
- **GTLB** (6 @ $56.75, Tech): Q2 beat + raise. Earnings 12/01. Break: a guide cut, an exec exit, a seat hit (CVE fallout).
- **CAKE** (3 @ $117.25, Consumer): Q3 comps +15.2%. Short 40%. 8-K 5.02 11/10 = bakery president retiring (benign). Break: a comp slowdown, a margin hit, an issuance.
- **AMPL** (20 @ $17.15, Tech): Q3 rev +25%, ARR +24%, FY guide +1.9%. Break: a guide cut, an equity raise.
- Exiting Mon 11/16 (rank decay): **NSIT** (2 @ $162.53), **PBF** (5 @ $70.54), **OABI** (70 @ $5.08), **REPL** (32 @ $10.99, +99%).
- ~~PD~~ / ~~CLDT~~ (rank decay 11/09), ~~TXG~~ (stop 11/02), ~~QMCO~~ (stop 11/05), ~~NEO~~ / ~~KELYA~~ (rank decay 11/02), ~~DK~~ (rank decay 10/26).
- ✅ **CLOSED, do not carry forward (rule 39):** "CDNA 11/5 8-K" (a Form 144), "REPL FQ2 11/6" (a 10-Q/A for 10b5-1 plans), "REPL earnings 11/13 BMO" (no 11/13 filing on EDGAR).


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
8. 🆕 **HC sector cap vs the ledger (W45).** It is the first veto category with n ≥ 10: HC-cap VETO 5d **+7.79% (n=11, only 6 distinct names)** vs BUY −0.33% (12).
   At 10d it reverses: +2.59% (6) vs BUY +4.31% (8). OABI and CDNA were bought after the vetoes and are −1% / −9% since. It is a Hard Guardrail, so Ben decides.
   Recommendation: **no change yet.** Re-test at 20d with ≥10 distinct names.
   **RULED 2026-11-11 (desktop review, delegated): KEEP the 3-per-sector cap.** 6 distinct names over one window is
   not evidence (RESEARCH_GATES §1); the rule now needs ≥ 10 distinct vetoed names with 20-day results. The
   cap is also doing its risk job: on 11/5 the HC/Tech-heavy book fell ~7.1% vs IWM −4.6%. Revisit with the new
   scorecard (`w`/`names` columns) once the 20d cell has ≥ 10 names.

### Standing category kills (full detail in archive)
Crypto/treasury (31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI, BKKT, UPXI, HSDT.
Non-US-incorporated (52c): KMTS, GLAS, NB, ADNT, DAVA. Liquidity: GLOO, TLYS, REF, OPTX,
SRZN, TTRX, IDT, TRAK, BSET. Pump/shell: GLND, GRML. **CLOSED:** PAAI (catalyst
falsified), PRTH (pinned deal), NUAI (mandated ATM), SCHL (miss + affirmed guide), PRME
(Gate A 9/25), MLKN (guide cut 9/22), XTND (undisclosed contract value, SPAC ADV).
