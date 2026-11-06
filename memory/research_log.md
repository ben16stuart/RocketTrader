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
> The Week 44 board (10/26–10/30 daily notes) was archived to `archive/research_log_history.md` on 2026-10-31.

## Watchlist — Week 45 (Mon 11/02 – Fri 11/06), built at the W44 review Sat 10/31  ← CURRENT

Book (10/30 close): 8 satellites ≈ 101.7% of a $2,997 slice, IWM 0, Rocket cash ≈ 0. The 12.5% cap ≈ **$375**. The weekly entry cap resets to **5**.
Ranking data as of 10/30 (740 eligible): TXG #1, REPL #2, QMCO #5, NSIT #7, CLDT #20, GTLB #23, **KELYA #26, NEO #27** → both replaced.
After the swap: HC = TXG/REPL/OABI (full). Tech = QMCO/NSIT/GTLB (full).

### Mon 11/02 — 2 replacements → premarket confirms on fresh data, market_open executes
**Order at 9:35:** (1) cancel NEO's and KELYA's trailing stops, `sell NEO 21`, `sell KELYA 22`. Log
`candidate_ledger.py log NEO EXIT "rank decay 27 > 25 at W44 review" --rank 27` and `... KELYA EXIT "rank decay 26 > 25 at W44 review" --rank 26`.
(2) Proceeds ≈ $730 cover both buys (≈ $696), so no IWM funding sale is needed. (3) BUY OABI and CAKE at market. (4) Place 25% trailing stops. (5) Log the BUYs.
Re-run `size` at the live price. Skip a name that opens >8% above Friday's close on no news (OABI $5.11, CAKE $112.64).
If Monday's premarket ranking puts NEO or KELYA back ≤25, **still replace them**: rank decay is judged weekly on Saturday's data.

### OABI — OmniAb, Inc.   (rank 3, Healthcare)  — replaces NEO
- Why it ranks: 6-1 +256%, vol 76%, 89% above 200d. Cap $745M, short 6.4%. YTD +268%.
- Checked 10/31: **DE incorporated** (EDGAR). Filings since 8/15 are only the 10/30 8-K 2.02 and the 10-Q. **No S-1/S-3/424B.** Q3 printed 10/30: EPS −$0.14 in line, **revenue $2.2M vs $5.6M est (a miss)**. The stock held: week range $4.61–5.28, Friday close $5.11, above the 50d ($4.65). The earnings gate is now clear.
- Judgment flag, not a veto: lumpy royalty/milestone revenue, so one quarter's miss is not a guide cut. **Premarket must read the 10-Q for going-concern language** before the order.
- What would break it: going-concern doubt, an ATM/shelf takedown, or a partner program discontinued.
- Size: `alpaca_client.py size OABI 5.11 3.83` → **69 sh ≈ $353 (11.8%)** (re-run 11/02)
- ✅ **11/02 premarket: 10-Q read (0001846253-26-000051).** Going concern appears only as the basis-of-presentation boilerplate, with **no substantial doubt**. Cash + ST investments are **$64.2M**, "sufficient … at least the next 12 months". The $100M ATM (Dec 2023) has **zero sales YTD**. Grade: undrawn ATM with roughly 12+ months of runway, a flag not a veto (rule 8). EDGAR: DE, no S-1/S-3/424B since the 10-Q. Rank #3 on fresh 10/30 data.
- Status: WATCHING (added 2026-10-31, confirmed 2026-11-02)

### CAKE — The Cheesecake Factory   (rank 15, Consumer Cyclical)  — replaces KELYA
- Why it ranks: 6-1 +81%, vol 39%, 42% above 200d. Cap $5.6B, **short 40%** (a squeeze flag, not a veto).
- Checked 10/31: **DE incorporated**. Filings since 8/15: only the 10/27 8-K (2.02/7.01/8.01). Q3 (10/27): revenue $1,033M (+14%), comps **+15.2%**, adj EPS $1.02, a beat. No specific comp/EPS guide ("will not be providing"). 26 openings FY26, 27 FY27. The stock dipped on the print and then recovered: Friday close $112.64, above the 50d ($108.02).
- It is the best-ranked non-HC, non-Tech name that passes. UTZ #13 is a take-private (vetoed 10/24) with EARNINGS in 4d.
- What would break it: a comp slowdown or a margin hit, a dividend cut, or an equity issuance.
- Size: `alpaca_client.py size CAKE 112.64 84.48` → 3 sh ≈ $338 (11.3%) (re-run 11/02)
- ✅ **11/02 premarket:** a web result claimed "earnings 11/02 AMC". **EDGAR falsifies it**: the 8-K 2.02 was filed 10/27, so Q3 is already out (rule 33/39: a calendar estimate is not a date). Filings since then are only Form 144 ×3 (10/29) and Form 4 ×3 (10/30). That is insider selling, not issuance: a note, not a veto. DE. Rank #15 on fresh 10/30 data. Ranks 9–14 are all EARNINGS ≤5d or non-US.
- Status: WATCHING (added 2026-10-31, confirmed 2026-11-02)

- **VETOs LOGGED 11/02 06:25 (top 8, not held):** IOVA #4 (EARNINGS 11/05), CDNA #6 (HC cap once OABI fills), ABCL #8 (FAIL non-US HQ). Also skipped between OABI and CAKE: SDGR #9, HNGE #10, PSNL #12 (EARNINGS and HC), APPS #11 (EARNINGS and Tech), UTZ #13, SMWB #14 (non-US).
- **Earnings this week (held, entry-gate only, held through with stops):** TXG, NSIT and CLDT 11/05. QMCO 11/09.

### Tue 11/03 premarket — 8/8 held, 0 open slots (weekly entries 3/5: OABI, CAKE, CDNA)
- Ranking (11/02 data, 769 eligible): OABI 2, QMCO 3, CDNA 4, NSIT 6, REPL 7, CAKE 12, CLDT 18, **GTLB 30 ⚠️** (a Sat W45 review item; rank decay is weekly, not daily). Saved `ledger/ranks/2026-11-02.csv`.
- Unheld top 8, for context only (no slot, so no VETO owed): TXG #1 (EARNINGS 11/05), TWST #5 (HC is full: OABI/CDNA/REPL), XRPN #8 (VERIFY earnings).
- Holdings check: no thesis breaks. CAKE's "$500M convert" hit is an old item (≈2024). A web claim that QMCO reports "11/03" conflicts with the ranker's 11/09. Treat it as unverified (rule 33). QMCO is held through either way.
- **Sat review watch:** GTLB needs a non-HC replacement (HC is full). Tech then holds QMCO/NSIT, so a Tech name is allowed.

### Wed 11/04 premarket — 8/8 held, 0 open slots (weekly entries 3/5: OABI, CAKE, CDNA)
- Ranking (11/03 data, 759 eligible): OABI 2, CDNA 4, REPL 5, NSIT 6, QMCO 7, CAKE 18, **CLDT 25** (at the edge), **GTLB 27 ⚠️** (second day >25; for the Sat W45 review). Saved `ledger/ranks/2026-11-03.csv`.
- Unheld top 8, context only (no slot, so no VETO owed): TXG #1 (EARNINGS 11/05), TWST #3 (OK gate, but HC is full: OABI/CDNA/REPL), XRPN #8 (VERIFY earnings). Note that the top 20 is 15/20 Healthcare.
- Holdings check (8 searches): no thesis breaks. Calendar conflicts, all unverified (rule 33): **CDNA "reports 11/04 AMC"** vs the 10/29 print already logged. OABI "11/03 or 11/09" vs the 10/30 8-K. **REPL "11/09 BMO"** vs the ranker's 10/28 (REPL's fiscal Q2, Sep qtr, is not on EDGAR in our notes yet). Held names keep their stops through any print. GTLB hits were FY26 items (Dec 2025 / Mar 2026), old.
- **Sat review watch:** GTLB (27) needs a replacement. HC is full, so the replacement must be non-HC. CLDT (25) is also borderline.

### Thu 11/05 premarket — 8/8 held, 0 open slots (weekly entries 3/5: OABI, CAKE, CDNA)
- Ranking (11/04 data, 821 eligible): NSIT 2, OABI 3, CDNA 4, REPL 6, CAKE 10, QMCO 12, **GTLB 18** (recovered from 27), **CLDT 20**. All 8 held are ≤25. Saved `ledger/ranks/2026-11-04.csv`.
- Unheld top 8, context only (no slot, so no VETO owed): TXG #1 (EARNINGS today), TWST #5 (EARNINGS 11/12 and HC full), SMWB #7 (FAIL non-US HQ), CON #8 (EARNINGS today).
- Holdings check (8 searches + 1 EDGAR): no thesis breaks. **QMCO "equity financing" headline = the known June 2026 $100M raise**: EDGAR shows no filing since the 10/09 8-K (5.02/8.01), no S-3/424B/NT 10-Q. OABI "reports 11/09 AMC" conflicts with the 10/30 8-K 2.02 (unverified, rule 33). GTLB "350 job cuts 9/26" is old. CAKE convert is the old ≈2024 item. **NSIT and CLDT report today BMO**, held through with stops.
- **Sat review watch:** GTLB and CLDT are no longer over 25 on today's data. Judge on Saturday's numbers only.

### Fri 11/06 premarket — 8/8 held, 0 open slots (weekly entries 4/5: OABI, CAKE, CDNA, PD)
- Ranking (11/05 data, 726 eligible): OABI 2, NSIT 3, CDNA 4, REPL 7, CAKE 14, GTLB 21, **PD 29 ⚠️**, **CLDT 59 ⚠️**. Saved `ledger/ranks/2026-11-05.csv`. Rank decay is judged at Saturday's review, not today. CLDT fell 20 → 59 on the day it posted a strong beat, so check Saturday whether the 11/05 bar is clean before swapping it (rule 34: one print is not a trend).
- Unheld top 8, context only (no slot, so no VETO owed): TXG #1 (OK, but HC is full), IOVA #5 (HC full), AMPL #6 (OK; Tech has NSIT/GTLB/PD, 3/3), UTZ #8 (EARNINGS today; take-private).
- Holdings check (9 searches + 1 EDGAR): **no thesis breaks.**
  - **CLDT Q3 (11/05, from the EDGAR 8-K ex-99):** RevPAR +8% to $161, an all-time Q3 high. Occupancy 83% (+390bp), AFFO/sh +27%. A strong print.
  - **NSIT Q3 (11/05 8-K):** sales +22%, adj EPS $3.59 (+34%). Search didn't show the FY guide verb, so Saturday reads ex-99.1 for raise vs. reaffirm (rule 5f).
  - **CDNA:** a "$91 offering" hit is old (≈2021). **EDGAR (DE) since 10/29 shows only Form 4 ×2 and a 144 (11/05)**: insider selling, a note. **Search hazard:** the query "Caribou Biosciences CDNA" returned CRBU news. CDNA = **CareDx**.
  - GTLB, REPL, OABI, PD, CAKE: results stale or already known. OABI "11/09" earnings and CAKE "11/02" are the same calendar errors seen earlier this week; their 8-Ks are already filed.
- **Sat W45 review: VIX 28.18 at the 11/05 close.** Above the 22 brake and the 25 reduce-size line. If it is still >25 at the review, any CLDT/PD replacement goes in at reduced size, or waits.

### Held satellites — thesis cards (break = specific news, never price)
- **QMCO** (20 @ $17.53, Tech): turnaround after the debt-to-equity conversion. CFO terminated 10/09 (flag). Break: a restatement, NT 10-Q, equity raise, or guide cut 11/09.
- **GTLB** (6 @ $56.75, Tech): Q2 beat + raise. Break: a guide cut, an exec exit, or a seat hit (incl. fallout from the CVE).
- **CLDT** (25 @ $14.30, REIT): pure rank. Break: a RevPAR/guide cut, a dividend cut, or an issuance. Earnings 11/04–05.
- **TXG** (5 @ $69.59, HC): Q2 beat + raised FY outlook, Atera demand. Break: a Q3 (11/05 AMC) guide cut. Cap $9.1B. **The cap gate is entry-only (ruled at W44)**, so drifting over $10B is not an exit.
- **REPL** (32 @ $10.99, HC): RP1 Accelerated Approval (Aug). The 10-Q says going-concern doubt is alleviated, with no ATM sales. Now ≈ 19% of slice after the run to $17.61; there are no trims by rule. Break: a 424B takedown off the 8/14 S-3ASR, a weak launch, an FDA safety action.
- **NEO** (21 @ $16.83, HC): Q3 beat and raise 10/28. **EXITING Mon 11/02 on rank decay (27).**
- **NSIT** (2 @ $162.53, Tech): Q2 beat, FY26 EPS guide raised to $12.20–12.70. Break: a guide cut. Earnings 11/05.
- **KELYA** (22 @ $16.41, Industrials): pure rank. **EXITING Mon 11/02 on rank decay (26).**
- ~~DK~~: exited 10/26 on rank decay (75). Thesis lesson: a refiner is short crude (strategy.md TESTING).


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
