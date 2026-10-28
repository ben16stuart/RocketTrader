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

### Mon 10/26 — CONFIRMED at premarket (ranking data 10/23, 712 eligible; ranks unchanged from Saturday) → market_open executes
**Order of operations at 9:35:** (1) cancel DK's trailing stop, `sell DK 4`, and log
`candidate_ledger.py log DK EXIT "rank decay 75 > 25 at W43 review" --rank 75`; (2) CORE FUNDING: sell IWM ≈ (≈$1,041 of BUYs − DK
proceeds ≈$298 − cash above the 10% buffer, ≈$0) ≈ **$740**; (3) BUY the 3 names below; (4) place 25% trailing stops; (5) log BUYs.
Re-run `size` at the live price. Skip any name that opens >8% above Friday's close on no news (wait a session).

### QMCO — Quantum Corporation   (rank 5, score 0.994)  — replaces DK
- Why it ranks: 6-1 +311%, vol 117%, 38% above 200d. Short interest 59.6%: a squeeze flag, not a veto.
- Catalyst / story: turnaround after the balance-sheet repair. The $54.7M term debt became converts on 12/18/2025, and Dialectic converted
  all of it (~$57.2M) into stock in June 2026. **Both are outside 30d, so this is not fresh dilution.** 10-Q (8/11) has **no** "substantial
  doubt" language. EDGAR since 8/1: no S-1/S-3/424B. The S-8 on 9/25 (employee plan) is not a veto. DE incorporated. Earnings 11/09.
- ⚠️ Judgment flag, not a veto: **CFO William White was terminated "effective immediately" on 10/09 (8-K 5.02).** The CAO (joined 9/2026)
  is now PFO. The COO moved over 9/28, plus 5.02s on 8/14 and 9/01. That is heavy C-suite churn at a company with a restatement history.
- What would break it: a restatement, NT 10-Q, or auditor change; an equity raise; a Q3 guide cut on 11/09.
- Entry: market at 9:35 | Stop: 25% trailing | Size: `alpaca_client.py size QMCO 17.62 13.22` → 20 sh ≈ $352 (11.6%)
- Status: WATCHING (added 2026-10-24, confirmed 2026-10-26)

### GTLB — GitLab Inc.   (rank 17, score 0.978)
- Why it ranks: 6-1 +126%, vol 59%, 68% above 200d.
- Catalyst / story: none fresh. Q2 (9/01 8-K 2.02/5.02) and a Strong Buy consensus. DE incorporated. Since 8/15, filings are only that 8-K and the 9/02 10-Q:
  no S-1/S-3. Earnings 12/01.
- What would break it: a guide cut, an exec departure that signals trouble, or a disclosed AI-disruption hit to seat growth.
- Entry: market at 9:35 | Stop: 25% trailing | Size: `alpaca_client.py size GTLB 56.28 42.21` → 6 sh ≈ $338 (11.1%)
- Status: WATCHING (added 2026-10-24, confirmed 2026-10-26)

### CLDT — Chatham Lodging Trust   (rank 25, score 0.966)
- Why it ranks: 6-1 +57%, vol 31% (low vol drives the score), 32% above 200d.
- Catalyst / story: none found. MD (US). The only filing since 8/15 is the 9/14 8-K (5.02/7.01). Earnings 11/04–11/05 (7–8 td), outside the 5-td gate.
  (The $19.45 price in the search was the CLDT-PA preferred; the common is $14.03.)
- Risk: it sits **exactly at the exit edge (25)**. A one-place slip by Sat 10/31 makes it a replacement. Accepted: it is the only non-HC,
  non-Tech name ≤25 that passes.
- What would break it: a Q3 RevPAR/guide cut, a dividend cut, or an equity issuance.
- Entry: market at 9:35 | Stop: 25% trailing | Size: `alpaca_client.py size CLDT 14.03 10.52` → 25 sh ≈ $351 (11.6%). ADV is 342k: thin, so use a market order at 9:35, not the first print.
- Status: WATCHING (added 2026-10-24, confirmed 2026-10-26)

- **VETOs logged 10/26:** OABI #3 (EARNINGS 10/30 + HC cap), XGN #4 (HC cap), CDNA #6 (EARNINGS 10/29 + HC cap), TWST #7 (HC cap),
  APPS #16 (EARNINGS 11/02), QLYS #20 (Tech cap). UTZ #18 was logged 10/24 (cash take-private). SMWB #10 and ABCL #12 FAIL non-US HQ (not top-8).
- **Slot 8 stays empty.** Nothing else ≤25 passes: TKNO, SDGR, ATRC, ETON, IOVA, PSNL, HNGE, CORT and CON are all HC (cap full).
  Projected satellites ≈ **82%** (4 held ≈ $1,427 + 3 ≈ $1,041, out of a $3,035 slice). IWM ≈ $285 after funding.
- Weekly entry count after Monday: 3/5. No entries Wed 10/28 (**FOMC**, statement 2:00 PM ET).

### Tue 10/27 — premarket (ranking data 10/26, 714 eligible) → market_open executes
Held 7 (TXG #1, QMCO #2, REPL #4, NSIT #8, NEO #13, GTLB #21, CLDT #23). **1 open slot**, weekly entries 3/5 → 1 pick.
HC cap full (TXG/REPL/NEO), Tech cap full (NSIT/QMCO/GTLB). The only non-HC, non-Tech name ≤25 that passes is KELYA. UTZ #19 = take-private (vetoed 10/24); CON #22 and CORT #24 = HC.
**Order at 9:35:** (1) CORE FUNDING: sell IWM ≈ **$365** (≈1.32 sh; Rocket has ≈$0 own cash above buffer). (2) BUY KELYA at market. (3) 25% trailing stop. (4) `candidate_ledger.py log KELYA BUY ... --rank 25`.
Re-run `size` at the live price. Skip it if it opens >8% above the 10/26 close ($16.58) on no news. Projected satellites ≈ **95%**, IWM ≈ $180.

### KELYA — Kelly Services, Inc.   (rank 25, score 0.966)
- Why it ranks: 6-1 +74%, vol 41%, 35% above 200d. Cap $576M, float 29.5M (94%).
- Catalyst / story: none fresh. A staffing turnaround with FY25 FCF of $114M (6× the prior year), and it pays a dividend. Class A (non-voting) shares. **DE incorporated** (EDGAR).
  EDGAR since 5/13: only Form 4s, the 8-K 2.02 and 10-Q (8/06), and a 13D/A + 13G (5/19). **No S-1/S-3/424B, no going concern.**
  Earnings: 11/05 (screener) vs 11/09 (search). Both are outside the 5-td gate (11/05 = 7 td).
- Risk: **ADV 313k is just over the 300k gate**, so it is thin. Use a market order at 9:35, not the first print. Like CLDT, it sits **exactly at the exit edge (25)**: a one-place slip by Sat 10/31 makes it a replacement. Accepted: it is the only eligible name in a sector with room.
- What would break it: a Q3 revenue/guide cut on 11/05–09, a dividend cut, or an equity issuance.
- Entry: market at 9:35 | Stop: 25% trailing | Size: `alpaca_client.py size KELYA 16.58 12.44` → 22 sh ≈ $365 (11.9%)
- Status: WATCHING (added 2026-10-27)

- **VETOs logged 10/27:** OABI #3 (EARNINGS 10/30 + HC cap), CDNA #5 (EARNINGS 10/29 + HC cap), XGN #6 and TWST #7 (HC cap).
- Holdings check (7 searches): **no thesis breaks.** REPL Q2 FY27 call is 10/28 8:00 AM, NEO reports 10/28, TXG reports 11/05 AMC. ⚠️ GTLB has a **maximum-severity CVE (CVE-2026-85706) under active exploitation** in CE/EE. It is a product-security flag, not a defined break. Watch for disclosed customer churn or a guide hit.

### Wed 10/28 — premarket (ranking data 10/27, 748 eligible) — 8 held, **0 open slots**, no entries (FOMC 2:00 PM ET)
Held ranks: TXG #1, QMCO #2, REPL #4, NSIT #8, NEO #16, GTLB #24, **CLDT #28 ⚠️, KELYA #34 ⚠️**. Weekly entries 4/5. No picks and no VETOs owed (0 slots).
- Holdings check (8 searches): **no thesis breaks.** The results were old items: TXG FY26 guide backed and the Proteintech deal, QMCO material weakness (known), REPL's $150M offering (Aug, >30d, known), NSIT Q2 beat, NEO Q2 raise + convert (June, known), GTLB Q2 beat, CLDT reports 11/04 BMO, KELYA rights plan (Jan).
- **REPL and NEO report today (10/28).** Both held through with stops in place. Read the prints at market_close/Thu premarket for a guide cut (thesis break) vs noise.
- **For the Sat 10/31 weekly_review:** (a) CLDT 28 and KELYA 34 are past the 25 exit rank. Rank decay is weekly, so replace them only if they are still >25 Saturday. (b) 🆕 **TXG's gate now reads `FAIL cap $10.2B`**, over the $10B universe ceiling, while it ranks #1. CLAUDE.md's exit triggers are stop / thesis break / rank >25 / below 200d, so cap drift is **not** an exit by rule. Decide at the review whether the cap gate is entry-only (it should be: exiting the #1 name for growing is selling a winner for winning). Hold it until then.

### Held satellites — thesis cards (break = specific news, never price)
- **QMCO** (20 @ $17.53, Tech): turnaround after the debt-to-equity conversion. CFO terminated 10/09 (flag). Break: a restatement, NT 10-Q, equity raise, or guide cut 11/09.
- **GTLB** (6 @ $56.75, Tech): Q2 beat + raise. Break: a guide cut, an exec exit, or a seat hit (incl. fallout from the CVE).
- **CLDT** (25 @ $14.30, REIT): pure rank. Break: a RevPAR/guide cut, a dividend cut, or an issuance. Earnings 11/04–05.
- **TXG** (5 @ $69.59, HC): Q2 beat + raised FY outlook, Atera demand. Break: a Q3 (11/05 AMC) guide cut. Cap $9.3B, near the $10B line.
- **REPL** (32 @ $10.99, HC): RP1 Accelerated Approval (Aug). Break: a 424B takedown off the 8/14 S-3ASR, a weak launch, FDA safety action. **Earnings 10/28.**
- **NEO** (21 @ $16.83, HC): Q2 beat + raise, prelim Q3 ~$209M, FY guide up. Break: a guide cut. **Earnings 10/28 AMC** (±16% implied, held through it).
- **NSIT** (2 @ $162.53, Tech): Q2 beat, FY26 EPS guide raised to $12.20–12.70. Break: a guide cut. Earnings 11/05.
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
