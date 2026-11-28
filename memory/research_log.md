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
> The Week 48 board was archived on 2026-11-28, and the Week 47 board (11/16–11/19 daily notes, TXG/IOVA/PAYS/CBRL entry cards) was archived to `archive/research_log_history.md` on 2026-11-21.


## Watchlist — Week 49 (Mon 11/30 – Fri 12/04), built at the W48 review Sat 11/28  ← CURRENT

Book (11/27 close): 8 satellites ≈ 86.7% of a $2,891 slice. IWM 0.33 sh (3.1%). Cash 10.2% (pooled). 12.5% cap ≈ **$361**. Weekly entry cap resets to **5**.
Ranking (`rank_screen.py --no-save`, **11/27 data**, 716 eligible): CDNA 2, TXG 5, IOVA 6, CBRL 13, APPN 15, AMPL 18, **CAKE 38, INTA 77** → both replaced.
INTA's score decayed on real data, not a download failure: m6-1 1.31 (11/20) → 1.08 (11/25) → 0.75 (11/27).
After the swaps: HC = CDNA/TXG/IOVA (full). Tech = AMPL/APPN/VIA (full). Consumer Cyclical = CBRL. Consumer Defensive = ELF.

### Mon 11/30 — REPLACE CAKE → ELF (#14) and INTA → VIA (#10). Status: WATCHING (added 2026-11-28)
**🚦 VIX gate (any routine that places the BUY applies it itself, per the W47 lesson). VIX CLOSED 23.81 on Fri 11/27.** < 25 → full size. 25–30 → half. > 30 → still sell CAKE and INTA (rank decay is never VIX-gated), put the proceeds in IWM, and carry the buys forward.
**Order:** cancel each exit's trailing stop, then `sell CAKE 3` and `sell INTA 3` (raw qty from `GET /v2/positions`). Log `candidate_ledger.py log CAKE EXIT "rank decay 38 > 25 at W48 review" --rank 38` and `... INTA EXIT "rank decay 77 > 25 at W48 review" --rank 77`. Write **one trade_log header per name** (rule 20b). Then make the BUYs, each with a 25% trailing stop and a logged BUY. Skip any name that opens >8% above its Friday close on no news.
1. **VIA #10 (Tech)**: Via Transportation. **DE** (EDGAR `stateOfIncorporation`), HQ NY. Q3 8-K 2.02 + 10-Q on 11/09: beat, Q4 guide initiated (platform rev $150–151.7M, +26–28%, which slows from Q3's +31%). Since 10/25 the only other filing is a passive SC 13G (11/16). **No S-1/S-3/424B.** IPO was 9/2025, so the lock-up is long expired. Earnings are next in early 2027. Fri close **$48.14** → `size VIA 48.14 36.11` = **7 sh** (11.7%). Break: guide cut, dilution, a secondary.
2. **ELF #14 (Consumer Defensive)**: e.l.f. Beauty. **DE**, HQ CA. FQ2 FY27 (8-K 2.02 11/04) beat and raised the FY outlook. **8-K 5.02 (11/16) read 11/28:** the CAO was named principal accounting officer and the CFO stays, so it is benign (✅ CLOSED). Only Form 144 insider filings since. **No S-1/S-3/424B.** The search's "−21% after-hours, guide disappoints" is the **Nov 2025** print (rule 33; ELF is +106% over 6 months). Earnings 2027-02-03. Fri close **$112.98** → `size ELF 112.98 84.74` = **3 sh** (11.7%). Break: guide cut, dilution, a tariff-driven margin reset.
- Backups (only if a check fails at premarket): every other non-held name in the top 20 is HC (cap full), FAIL (ECO 4 Greece, SLN 8 UK) or **NIQ #12, an Irish plc (L2 on EDGAR): hard VETO, non-US incorporation.** Go past 20 in Monday's rank file for the first non-HC, non-Tech name.
- **VETOs owed Monday** (top 8 not held, logged at premarket): RCEL 1, ATRC 3, XNCR 7 (HC cap); ECO 4, SLN 8 (FAIL non-US HQ).
- **Binary events, held names, W49:** **CBRL earnings Tue 12/02** (held; it is not an exit trigger, but a 30%+ gap goes through any stop). Nothing else in the window.
- **The weekly entry cap is reset to 5.** W48 used 1/5 (INTA).

### Held satellites — thesis cards (break = specific news, never price)
- **CDNA** (4 @ $86.10, HC): Q3 rev +39%, 3rd straight guide raise. Patent appeal heard 11/09 (≈$96M): no ruling found yet. Break: guide cut, Medicare/LCD hit, equity raise.
- **TXG** (6 @ $55.86, HC): Q3 filed, 2 directors added. Break: guide cut, dilution.
- **IOVA** (44 @ $7.70, HC): ATM used up and terminated 9/30. A new ATM/S-3 is likely and would be a thesis break. Break: new ATM/offering, failed readout.
- **AMPL** (20 @ $17.15, Tech): Q3 rev +25%, FY guide +1.9%. Break: guide cut, equity raise.
- **APPN** (6 @ $51.73, Tech): Q3 beat + FY raise (8-K 2.02 11/05). **DE, verified 11/21 on the 10-Q cover** (EDGAR JSON field blank). Break: dilution, guide cut. (Bought at full size with VIX > 30. See W47 review.)
- Exiting Mon 11/30: **CAKE** (3 @ $117.25, rank 38) and **INTA** (3 @ $43.65, rank 77).
- **CBRL** (5 @ $67.16, Consumer): 11/19 meeting uncontested. Earnings **12/02** (confirmed 11/23). Break: guide cut, issuance, contested-control event.
- ~~PAYS~~ (rank decay 11/23 @ $10.10, +7.7%; $11.15 by 11/27, so the exit cost ≈ 7 pts vs IWM).
- ~~GTLB~~ (stop 11/20 @ $43.365, −23.6%), ~~NSIT~~ / ~~PBF~~ / ~~OABI~~ / ~~REPL~~ (rank decay 11/16). Older exits: see archive.
- ✅ **CLOSED, do not carry forward (rule 39):** "CDNA 11/5 8-K" (a Form 144), "REPL FQ2 11/6" (a 10-Q/A), "REPL earnings 11/13 BMO" (no filing).


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
