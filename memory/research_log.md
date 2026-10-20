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
> **Tue 10/20 premarket:** all 5 picks HELD (filled 10/19). Rank as of 10/19 close: REPL #1, TXG #2, NEO #4, NSIT #7, DK #18 (all ≤25).
> Holdings news check is clean. **REPL resolved:** FDA granted Accelerated Approval for TUDRIQEV (RP1) + nivolumab in Aug 2026, so the CRL risk is gone.
> Dates: REPL Q3 10/29 (search) vs 11/05 (screener); TXG Q3 **11/05 AMC** (company PR 10/13, not 11/04); NEO **10/28 AMC** confirmed (±16% implied, held through it, no time stops).
> Weekly entry cap 5/5 is used, so 0 open slots until Mon 10/26. Next in line by rank: OABI #6 (HC; would be the 4th HC, HC cap is 3), ATRC #8 (HC, same cap), UTZ #11, QMCO #12, GTLB #13.
> **DONE Mon 10/19 premarket:** 5 WATCHING picks (REPL, TXG, NEO, DK, NSIT). The 4 top-8 skips are logged as VETOs. The Week 42 board below (RAPP/EIKN/HAWK/CODI…) is **history, not a to-do list**; a name
> from it is bought only if it ranks.

## Watchlist — Week 43 (Mon 10/19 – Fri 10/23), built at W42 review Sat 10/17  ← CURRENT

**The first week under rank → judge.** Satellites **0%** (floor 50%, breached at 20 straight closes). Weekly entry cap: **5**. Healthcare cap: 3.
Book (10/16 close): IWM 9.9763 sh × $270.44 = $2,697.99. Slice $2,988.05 → 12.5% cap ≈ **$373** per satellite. Every BUY needs a
**CORE FUNDING** IWM sale right before it (rule 3). The W42 board (RAPP/EIKN/HAWK/CODI/OIG/TRAX/VSTM) was archived 2026-10-17. It is history.

### Mon 10/19 PREMARKET picks — 5 WATCHING (first rank → judge board; ranking data as of 10/16 close)
Slots: 8 − 0 held = 8, capped by the weekly limit at **5**. Picks total ≈ **$1,685 ≈ 56% of slice → clears the 50% floor**.
**CORE FUNDING at market_open:** sell ≈ the BUY total minus free cash above the 10% buffer, as IWM (fractional market) right before the
buys; log `CORE FUNDING`. EDGAR `stateOfIncorporation` checked via data.sec.gov for all 8 top names (DE ×7, NEO = NV): all US.
**Top-8 VETOs logged:** SMWB #2 (FAIL Israel HQ), ABCL #5 (FAIL Canada HQ), OABI #6 + SDGR #7 (HC cap: 3 HC picked at ranks 1/3/4).
NSIT (#9) fills the 5th slot, after DK (#8).

### REPL — Replimune Group   (rank 1, score 1.000)
- Why it ranks: 6-1 +493%, vol 127%, 20% above 200d
- Catalyst / story: RP1 (vusolimogene) in melanoma. The 4/10 PDUFA ended in a CRL. It was resubmitted in June with a ~8/2 PDUFA (search result). The
  **outcome is NOT verified**: a run of 8-Ks from 7/30 to 8/11 plus the raise suggests approval. Confirm in the first 2 minutes of market_open; a second CRL would be a thesis break. Raised money on a **424B5 dated 8/10** (70 days ago: outside the 30-day window). 9/16 8-K = annual meeting (5.03/5.07).
- What would break it: a takedown off the **S-3ASR automatic shelf (8/14)**, which needs no new registration (watch for a 424B); a weak launch print at
  FQ2 earnings 11/05; any FDA labeling or safety action. 127% vol, so expect 25% swings. That is the stop's job.
- Entry: market at 9:35 | Stop: 25% trailing | Size: 33 sh ≈ $358 (12.0%) at $10.86 / stop basis $8.15
- Status: HELD (bought 2026-10-19; 25% trail live)

### TXG — 10x Genomics   (rank 3, score 0.997)
- Why it ranks: 6-1 +195%, vol 75%, 85% above 200d
- Catalyst / story: Q2 (8/6) beat with a **raised FY revenue outlook** + early Atera demand; +67% post-earnings drift since. No offerings (13G/As only).
- What would break it: Q3 (11/04 AMC) guide cut or Atera demand stalling. Insiders: 30 sales / 0 buys in 6 months (supply, not a veto).
  Cap $9.1B: a ~10% move takes it over IWM's $10B line (in-universe at entry, so the weekly rank decides, not the cap).
- Entry: market at 9:35 | Stop: 25% trailing | Size: 5 sh ≈ $349 (11.7%) at $69.86 / stop basis $52.40
- Status: HELD (bought 2026-10-19; 25% trail live)

### NEO — NeoGenomics   (rank 4, score 0.995)
- Why it ranks: 6-1 +138%, vol 54%, 33% above 200d
- Catalyst / story: Q2 beat and **raised FY26 revenue guide ($802–806M) and EBITDA**, +260bp gross margin, DOJ probe resolved, Medicare coverage for RaDaR ST.
- What would break it: Q3 on **10/27 (search) / 10/28 (screener)**, ±16% implied. ⚠️ **Monday-only entry:** a buy today is 6 trading days ahead of
  10/27. From Tue 10/20 it is 5 days out, which is a hard veto. If it does not fill 10/19, VETO it ("earnings ≤5 td") and move to the next rank.
  S-8 on 8/25 (not an offering).
- Entry: market at 9:35 | Stop: 25% trailing | Size: 21 sh ≈ $350 (11.7%) at $16.65 / stop basis $12.49
- Status: HELD (bought 2026-10-19; 25% trail live)

### DK — Delek US Holdings   (rank 8, score 0.989)
- Why it ranks: 6-1 +121%, vol 54%, 52% above 200d
- Catalyst / story: refining margins with Brent ~$109 under the Iran export blockade. Q2 revenue +48%. Street mixed (5 Buy / 5 Hold / 1 Sell;
  TD Cowen Buy $85 10/1, Freedom Hold $86 10/6). No offering filings.
- What would break it: the blockade ending or a crude collapse (the headline risk is the thesis itself); a crack-spread squeeze. Q3 on 11/06.
- Entry: market at 9:35 | Stop: 25% trailing | Size: 4 sh ≈ $306 (10.2%) at $76.59 / stop basis $57.44
- Status: HELD (bought 2026-10-19; 25% trail live)

### NSIT — Insight Enterprises   (rank 9, score 0.988)
- Why it ranks: 6-1 +102%, vol 46%, 48% above 200d
- Catalyst / story: Q2 (8/6) EPS $3.86 vs $2.93, revenue +14.7%, **FY26 EPS guide raised to $12.20–12.70** (AI infrastructure / cybersecurity). No filings since 8/15.
- What would break it: Q3 guide cut. ⚠️ Earnings date conflict: **10/29 (search) vs 11/05 (screener)**. 10/29 is 8 td out, so the entry is fine either way.
- Entry: market at 9:35 | Stop: 25% trailing | Size: 2 sh ≈ $321 (10.7%) at $160.47 / stop basis $120.35
- Status: HELD (bought 2026-10-19; 25% trail live)

**Next in line if a pick is skipped at the open:** GTLB #11 (Tech), UTZ #12 (Consumer Defensive; earnings 10/29 = 8 td). HNGE #10 is HC, blocked by the cap.
**Open-rule reminder:** if a name opens >8% above its 10/16 close on no news, wait one session (except NEO, which becomes a veto instead).
**Rank-decay replacements:** none (no held satellites).
**Calendar:** FOMC **10/27–28** (statement 10/28 2:00 PM ET) is next week. This week: housing starts and flash PMIs (10/23).
VIX 18.63 live (10/16 close 19.99), under the 22 brake.

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
