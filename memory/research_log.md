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
> The Week 45 board (11/02–11/06 daily notes) was archived to `archive/research_log_history.md` on 2026-11-07.

## Watchlist — Week 46 (Mon 11/09 – Fri 11/13), built at the W45 review Sat 11/07  ← CURRENT

Book (11/06 close): 8 satellites ≈ 104% of a $2,878 slice. IWM 0. The 12.5% cap ≈ **$360**. The weekly entry cap resets to **5**.
Ranking data as of 11/06 (739 eligible): CDNA 2, OABI 5, NSIT 14, CAKE 16, GTLB 20, REPL 24, **PD 26, CLDT 58** → both replaced.
After the swap: HC = CDNA/OABI/REPL (full). Tech = NSIT/GTLB/AMPL (full). Energy = PBF. Consumer = CAKE.

### Mon 11/09 — 2 replacements → premarket confirms on fresh data, market_open executes
**Order at 9:35:** (1) cancel PD's and CLDT's trailing stops, `sell PD 21`, `sell CLDT 25`. Log
`candidate_ledger.py log PD EXIT "rank decay 26 > 25 at W45 review" --rank 26` and `... CLDT EXIT "rank decay 58 > 25 at W45 review" --rank 58`.
(2) Proceeds ≈ $716 cover both buys, so no IWM funding sale. (3) BUY AMPL and PBF at market. (4) Place 25% trailing stops. (5) Log the BUYs.
**Size:** VIX closed 25.64 on 11/06 (>25 reduce-size line). If VIX is still >25 at premarket, buy **half: AMPL 10 / PBF 2**. If it is ≤25, buy full size: **AMPL 20 / PBF 5**
(re-run `size` at the live price). If VIX >30, no new longs: still sell PD/CLDT, and the proceeds sweep to IWM at the close.
Skip a name that opens >8% above Friday's close on no news (AMPL $16.70, PBF $67.27). If PD/CLDT re-rank ≤25 Monday, **still replace them** (decay is judged on Saturday's data).

**✅ Premarket 11/09 confirmed — GO, FULL SIZE.** `rank_screen.py` data is still as of 11/06 (unchanged: AMPL #8, PBF #18, PD 26, CLDT 58).
VIX **23.54 live** (25.64 close 11/06), under the 25 line → **AMPL 20 / PBF 5** (`size` at Fri closes: 11.6% each). market_open: re-read VIX; if >25 at 9:35, use half size.
Owed checks are done: both 5.02s are benign (AMPL 10/15 = **added** director Vijaye Raji, board 8→9, nobody left; PBF 10/30 = routine exec LTI grants).
AMPL FY guide **raised 1.9%** (midpoint $409.2M after Q2 → $417.0M after Q3), a real raise under rule 5a. EDGAR (11/09): no new filings since 11/06 for either name, no S-1/S-3/424B.
Top-8 VETOs **logged 11/09**: TXG #1, IOVA #4, RCEL #6, HAE #7 (HC cap), UTZ #3 (going-private; DEFM14A 10/02 + SC 13E3/A 10/30 verified on EDGAR).

### AMPL — Amplitude, Inc.   (rank 8, Technology)  — replaces PD
- Why it ranks: 6-1 +139%, vol 65%, 71% above 200d. Cap $2.1B, short 8.3%.
- Checked 11/07: **DE** (EDGAR). Q3 (11/04 8-K ex-99.1): revenue $110.6M +25%, ARR $431M +24%, RPO +27%, record non-GAAP op margin, FCF $5.8M. FY26 guide revenue $415.8–418.2M.
  10-Q 11/05. After that, only Form 4/144 (insider sales, a note). **No S-1/S-3/424B.** The earnings gate is clear (next print ~Feb).
- **Premarket owes:** (a) the 10/15 8-K 5.02 (an exec change: who left?); (b) whether the FY guide was raised versus Q2's guide (rule 5, advisory: log it).
- Break: guide cut, a seat/AI-disruption hit, an equity raise.
- Status: WATCHING (added 2026-11-07)

### PBF — PBF Energy Inc.   (rank 18, Energy)  — replaces CLDT
- Why it ranks: 6-1 +122%, vol 66%, 24% above 200d. Cap $8.0B, short 12.5%.
- Checked 11/07: **DE** (EDGAR). Q3 (10/29 8-K): net income $1.54B, EPS $12.54 vs $1.45, cash $2.5B vs debt $2.1B (net debt cut >$1.2B), **dividend +18%** to $0.325. Martinez is back at full rate, and the turnarounds are done.
  Since then: 8-K 5.02 (10/30), Form 4s, two 144s. **No S-1/S-3/424B.**
- **DK TESTING check:** a refiner, but the thesis is realized cracks plus deleveraging, not "crude is up". Crude has fallen (Brent 117 → 98). It does not match the DK pattern. Flag only.
- **Premarket owes:** the 10/30 8-K 5.02 (who left?).
- Break: a crack-spread collapse with a guide cut, a refinery outage, a dividend cut, an equity raise.
- Status: WATCHING (added 2026-11-07)

- **VETOs to log Mon (if the 11/06 ranks hold):** UTZ #3 (take-private), IOVA #4, RCEL #6, HAE #7 (HC cap: CDNA/OABI/REPL).
  Between #8 and #18 (no log needed beyond the top 8): ATRC, PSNL, TWST (HC), PAYS/QLYS (EARNINGS 11/09), SMWB/ECO (non-US), NSIT/CAKE held.
- **Earnings this week (held):** none in the gate. GTLB 12/01.
- **Closed 11/07:** the CDNA "11/05 8-K" and REPL "FQ2 11/06" claims were false (EDGAR: a Form 144, and a 10-Q/A adding exec 10b5-1 plans). No thesis break.

### Tue 11/10 premarket — 8 held, **0 open slots** (no picks, no VETOs owed)
- `rank_screen.py` (11/09 data, 810 eligible): CDNA 5, OABI 6, AMPL 9, REPL 15, CAKE 16, GTLB 18, NSIT 24, **PBF 44 ⚠️** (>25).
  PBF was rank 18 on 11/06 data and was bought 11/09; rank decay is judged **weekly** → re-check at the Sat 11/14 W46 review, no action before.
  NSIT 24 is on the edge. Top 8 not held: TXG 1, HAE 2, IOVA 3, UTZ 4 (going-private), SMWB 7 (FAIL Israel), ATRC 8. No slot is open, so these are not decisions.
- Holdings check (8 searches): **no thesis breaks.** Results were stale or undated. CDNA search again returned CRBU (wrong company). The GTLB "Q3 drop" is the Dec 2025 print.
  The OABI "earnings 11/09" and REPL "11/05" are projected calendar dates (rule 39); the ranker shows 10/30 and 10/28 already printed. PBF's dividend record date is 11/12.

### Wed 11/11 premarket — 8 held, **0 open slots** (no picks, no VETOs owed)
- `rank_screen.py` (11/10 data, 791 eligible): CDNA 4, GTLB 6, AMPL 9, OABI 11, CAKE 15, NSIT 19, **REPL 30 ⚠️, PBF 40 ⚠️** (both >25).
  Two held names are now past the exit rank. Rank decay is weekly → the **Sat 11/14 W46 review** decides on Friday's data, no action before. If both still rank >25, that review replaces 2 (entries used this week: 2/5).
  Top 8 not held: TXG 1, HAE 2, IOVA 3, UTZ 5 (going-private), ATRC 7, SMWB 8 (FAIL Israel). HC already holds 3 (CDNA/OABI/REPL). No slot is open, so these are not decisions.
- Holdings check (8 searches + EDGAR filing lists for all 8): **no thesis breaks.** No S-1/S-3/424B on any name.
  New filings since 11/09: CAKE 8-K 5.02 (11/10) = the **bakery subsidiary president is retiring** in Q1 2027 (read on EDGAR; benign). Otherwise only Form 4/144 and 13G/13G/A.
  OABI: the ticker lookup came back blank, so I re-ran it by CIK 1846253 (rule 38). Last filing is a Form 4 on 11/02; nothing new. OABI is presenting at Stifel today and Truist 11/12.
  CDNA: news mentions a patent **appeal hearing on 11/09** with ≈$96M + interest at stake from a prior jury award. This is a known contingency, not a break. **A ruling against CDNA would be checked against its cash and buyback.**
  REPL: earningswhispers shows "earnings 11/13 BMO". That is a projected date and unverified (rule 39). The FQ2 10-Q/A was filed 11/06. Held names don't exit on earnings; it is a note only.
  GTLB news is still the Dec 2025 FQ3 print; the next print is 12/01.

### Thu 11/12 premarket — 8 held, **0 open slots** (no picks, no VETOs owed)
- `rank_screen.py` (11/11 data, 813 eligible): CDNA 2, CAKE 7, AMPL 8, GTLB 10, NSIT 17, PBF 22, **OABI 29 ⚠️, REPL 134 ⚠️** (both >25).
  REPL's drop (30 → 134) is the 6-1 window rolling: its m61 fell 2.20 → 1.28 while price moved only 23.28 → 21.78. That is a mechanical
  re-base, not news. PBF recovered to 22. Rank decay is weekly → the **Sat 11/14 W46 review** decides on Friday's data, no action before.
  Top 8 not held: TXG 1, UTZ 3 (going-private), HAE 4, IOVA 5, SMWB 6 (FAIL Israel). No slot is open, so these are not decisions.
- Holdings check (8 searches + EDGAR filing lists for all 8; OABI by CIK 1846253): **no thesis breaks.** No S-1/S-3/424B on any name.
  New filings since 11/11: REPL Form 4 + SC 13G (11/10), CDNA 144 + SC 13G (11/10). Nothing else. Search results were stale or undated.
  REPL: earningswhispers again shows "earnings 11/13 BMO" (projected, unverified, rule 39). Held names don't exit on earnings; a note only.
  PBF snippets (Morgan Stanley downgrade, Scotiabank PT $28) are undated and the PT doesn't match a ~$70 stock: old (rule 33).

### Held satellites — thesis cards (break = specific news, never price)
- **CDNA** (4 @ $86.10, HC): Q3 rev +39%, 3rd straight guide raise. Break: a guide cut, a Medicare/LCD reimbursement hit, an equity raise.
- **OABI** (70 @ $5.08, HC): pure rank. No going-concern doubt, $64.2M cash, ATM undrawn. Break: going-concern, an ATM draw, a partner program dropped.
- **REPL** (32 @ $10.99, HC): RP1 Accelerated Approval. Going-concern doubt alleviated. 10-Q/A (11/06) added exec 10b5-1 plans (insider-selling note). ≈ 24% of slice; no trims by rule. Break: a 424B takedown off the S-3ASR, a weak launch, an FDA safety action.
- **NSIT** (2 @ $162.53, Tech): Q3 adj EPS +34%. Break: a guide cut.
- **GTLB** (6 @ $56.75, Tech): Q2 beat + raise. Earnings 12/01. Break: a guide cut, an exec exit, a seat hit (CVE fallout).
- **CAKE** (3 @ $117.25, Consumer): Q3 comps +15.2%. Short 40%. Break: a comp slowdown, a margin hit, an issuance.
- **AMPL** (20 @ $17.15, Tech): Q3 rev +25%, ARR +24%, FY guide +1.9%. Break: a guide cut, an equity raise.
- **PBF** (5 @ $70.54, Energy): Q3 EPS $12.54, dividend +18%, net debt cut. Break: a crack collapse with a guide cut, an outage, a dividend cut, an equity raise. Rank 44 on 11/09 data (weekly check).
- ~~PD~~ / ~~CLDT~~ (rank decay 11/09), ~~TXG~~ (stop 11/02), ~~QMCO~~ (stop 11/05), ~~NEO~~ / ~~KELYA~~ (rank decay 11/02), ~~DK~~ (rank decay 10/26).


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
