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
> The Week 47 board (11/16–11/19 daily notes, TXG/IOVA/PAYS/CBRL entry cards) was archived to `archive/research_log_history.md` on 2026-11-21.


## Watchlist — Week 48 (Mon 11/23 – Fri 11/27, Thanksgiving Thu closed, Fri half day), built at the W47 review Sat 11/21  ← CURRENT

Book (11/20 close): 8 satellites ≈ 92.4% of a $2,779 slice. IWM 0. The 12.5% cap ≈ **$347**. The weekly entry cap resets to **5**.
Ranking (11/20 data, 546 eligible): CDNA 1, TXG 3, AMPL 5, IOVA 8, APPN 9, CAKE 12, CBRL 17, **PAYS 29** → PAYS is replaced.
After the swap: HC = CDNA/TXG/IOVA (full). Tech = AMPL/APPN/INTA. Consumer Cyclical = CAKE/CBRL.

### Mon 11/23 — REPLACE PAYS → INTA (rank 10). Status: WATCHING (added 2026-11-21)
**🚦 VIX gate first (premarket.md: >25 reduce size, >30 no new longs). VIX CLOSED 35.89 on Fri 11/20.**
- VIX > 30 at 9:35: **still sell PAYS** (rank decay is decided on Saturday's data), put the proceeds in IWM, and **do not buy INTA**. Carry INTA forward. The first session with VIX ≤ 30 sells IWM as a CORE FUNDING sale and buys INTA.
- VIX 25–30: INTA **3 sh** (half). VIX < 25: INTA **7 sh** (`size INTA 43.45 32.59` → 7; re-run at the live price, STOP = ENTRY × 0.75).
**Order:** cancel PAYS's trailing stop, `sell PAYS 37` (raw qty from `GET /v2/positions`), log `candidate_ledger.py log PAYS EXIT "rank decay 29 > 25 at W47 review" --rank 29` and a `PAYS SELL` header in trade_log. Then BUY INTA if the VIX allows, place the 25% trailing stop, log the BUY (rank 10). Skip it if it opens >8% above Friday's $43.45 close on no news.
1. **INTA #10 (Tech)**: Intapp, **DE** (EDGAR `stateOfIncorporation`), HQ CA. Q3 8-K 2.02 + 10-Q 10/27. Since 10/20 the only non-insider filing is an 8-K 5.07 on 11/20 (shareholder vote results). **No S-1/S-3/424B**, no takeover or going-concern found. Next earnings early Feb. One news search (11/21) returned stale, misdated items only (rule 33). **Premarket owes:** one dated news check. Break: guide cut, dilution, an exec exit.
2. Backups in order: **ELF #11** (DE; earnings 2027-02-03; **8-K 5.02 dated 11/16 unread, so read it first**), **VIA #13** (DE, Q3 11/09; check for IPO lock-up expiry or a resale S-1).
- **VETOs owed Monday** (top 8 not held): SLN #2 (FAIL non-US HQ), RCEL #4 and ATRC #6 (HC cap), UTZ #7 (pinned going-private).
- **Binary events, held names, W48:** none inside the window. **CBRL earnings: the ranker says 12/02, the W46 board said 12/09.** Premarket confirms the date (it's not an exit trigger).
- **The weekly entry cap is reset to 5.** W47 used 5/5 (TXG, IOVA, PAYS, CBRL, APPN). The 11/20 midday's "1/5" was wrong.

**✅ Premarket 11/23 (Mon) confirmed the swap.** Ranking still on 11/20 data (same as the review): PAYS 29, INTA 10. INTA owed checks DONE: EDGAR (CIK 1565687, **DE**) since 11/10 shows only Form 4 / 144 insider sales and the 11/20 8-K 5.07, so **no S-1/S-3/424B**. News: FQ1 FY27 results 10/27, nothing thesis-breaking, and no fresh dated item. Earnings early Feb → gate OK. Tech after the swap = AMPL/APPN/INTA (3, at cap).
**VIX at 11/23 premarket: 29.67 LIVE (close 35.89 on 11/20).** If it is in 25–30 at 9:35, buy **INTA 3 sh (half)**. Above 30, sell PAYS into IWM and skip INTA. Below 25, buy 7 sh. Re-read the VIX at the open.
**CBRL earnings confirmed 2026-12-02** (`eligibility`). That is 6 trading days out, outside the 5-day entry gate. It is not an exit trigger (held name).
**Top-8 VETOs logged 11/23:** SLN 2, RCEL 4, ATRC 6, UTZ 7.

**Premarket Tue 11/24: 8 held, 0 open slots, no picks owed.** Weekly entries 1/5 (INTA). Ranking (11/23 data, 620 eligible): CDNA 1, TXG 4, AMPL 6, INTA 7, IOVA 9, APPN 10, CBRL 21, **CAKE 33**. CAKE is over the exit line on one day's data. Rank decay is decided at Saturday's review only, so there is **no action today**. Watch it for the W48 review. Unheld top 8: RCEL 2 / UTZ 3 / SLN 5 (FAIL) / VIA 8. No slots were skipped, so no VETOs are owed.
- Holdings check (8 searches): no thesis breaks. Only Q3 recaps, CAKE's 11/24 dividend payment, and TXG's 11/16 collaborations. The INTA "CFO sold 10,000 sh on Mon Nov 24" hit links to a **2025-11-27** URL, so it is a stale item misdated (rules 39, 62). The CDNA appeal still has no ruling found.
- **If a stop opens a slot, refill in rank order:** VIA #8 (Tech is at cap 3, so VETO), then ATRC #11 (HC is at cap), HNGE #12 (HC cap), PD #13 (Tech cap; earnings 12/03), ELF #14 (Consumer Defensive; 8-K 5.02 11/16 still unread). **VIX 28.58 live → half size.**

**Premarket Wed 11/25: 8 held, 0 open slots, no picks owed.** Weekly entries 1/5 (INTA). Ranking (11/24 data, 648 eligible): CDNA 1, TXG 5, INTA 6, AMPL 8, APPN 11, IOVA 17, **CBRL 27, CAKE 31**. Both are over the 25 exit line now (CAKE on 2 straight days). Rank decay is decided at Saturday's W48 review only, so there is **no action today**. Both are prime replacement candidates Saturday. CBRL earnings 12/02 is now inside the 5-day gate. That blocks entries, not holds, and it is not an exit trigger. Unheld top 8: RCEL 2 / ATRC 3 (HC cap), UTZ 4 (going-private pin), SLN 7 (FAIL). No slots were skipped, so no VETOs are owed.
- Holdings check (8 searches): no thesis breaks. Same Q3 recaps. The INTA "CFO sale 11/24" is again the **2025-11-27** item (rule 39). The CDNA appeal still has no ruling found.
- **If a stop opens a slot today, the top 20 has NO clean refill.** HC is at cap (RCEL, ATRC, XNCR, HNGE). Tech is at cap (VIA, QLYS, PD, RSKD; BOX also earnings 4d). UTZ is pinned. SLN / BUUU / ECO FAIL non-US. NIQ is VERIFY (no company data). Go past 20 in `ledger/ranks/2026-11-24.csv` for the first non-HC, non-Tech name, and run the full veto checks. **VIX 29.23 live → half size, and none if > 30 at the open.**

**Premarket Thu 11/26 (THANKSGIVING, market closed; next session Fri 11/27, 1:00 PM ET close): 8 held, 0 open slots, no picks owed.** Weekly entries 1/5 (INTA). Ranking (11/25 data, 673 eligible): CDNA 1, TXG 5, AMPL 6, IOVA 9, APPN 16, CBRL 23, INTA 24, **CAKE 30** (3rd straight day > 25). CBRL is back under the line. INTA (24) is now near it. Rank decay is decided at Saturday's W48 review only, so there is **no action Friday**. Unheld top 8: RCEL 2, ATRC 3, XNCR 8 (HC cap), UTZ 4 (going-private pin), SLN 7 (FAIL). No slots were skipped, so no VETOs are owed.
- Holdings check (8 searches): no thesis breaks, only Q3 recaps. The INTA "CFO sale 11/24" is the **2025-11-27** insidertrades URL again (rule 39). IOVA's −35% lung-data drop is dated 10/29 (old). Still no ruling found on the CDNA appeal.
- **If a stop opens a slot Friday:** HC is at cap (RCEL/ATRC/XNCR/HNGE/CON/HAE/AMRX). Tech is at cap (VIA/QLYS; PD has earnings in 5d). UTZ is pinned. SLN/ECO/BUUU FAIL. NIQ is VERIFY. **No clean refill in the top 20.** Go past 20 in `ledger/ranks/2026-11-25.csv` for the first non-HC, non-Tech name, with full veto checks. Note the half day: no entries after 12:30 ET. **VIX 27.36 live → half size.**

**Premarket Fri 11/27 (half day, 1:00 PM ET close): 8 held, 0 open slots, no picks owed.** Weekly entries 1/5 (INTA). Ranking is **still on 11/25 data** (Thursday closed; 672 eligible, same order as Thursday's run): CDNA 1, TXG 5, AMPL 6, IOVA 9, APPN 16, CBRL 23, INTA 24, **CAKE 30** (4th run > 25, on 3 distinct data days). **W48 review Saturday: CAKE is the prime replacement**, and INTA (24) sits on the line. Unheld top 8: RCEL 2 / ATRC 3 / XNCR 8 (HC cap), UTZ 4 (pin), SLN 7 (FAIL). No slots were skipped, so no VETOs are owed.
- Holdings check (8 searches + 2 dating checks): no thesis breaks. **AMPL "President departure" is the 2026-02-24 8-K** (Hansen, effective 3/31; guide reaffirmed), so it is stale. **IOVA "$350M offering / −14.9% governance" is a 2025 item** (Zacks id 2742764, ~$915M cap at the time vs ~$3.3B now), stale (rule 33). There is still no CDNA appeal ruling. INTA: $150M buyback, new CMO. TXG/APPN/CAKE/CBRL only had Q3/old recaps.
- **If a stop opens a slot today:** the first non-HC, non-Tech, non-FAIL name past 20 is **ELF #25** (Consumer Defensive; 8-K 5.02 from 11/16 is still unread, and it needs the full veto check). TBBB #26 is Mexican (check the gate). **VIX 24.93 live (< 25) → full size**, but re-read it at the open.

### Held satellites — thesis cards (break = specific news, never price)
- **CDNA** (4 @ $86.10, HC): Q3 rev +39%, 3rd straight guide raise. Patent appeal heard 11/09 (≈$96M): no ruling found yet. Break: guide cut, Medicare/LCD hit, equity raise.
- **TXG** (6 @ $55.86, HC): Q3 filed, 2 directors added. Break: guide cut, dilution.
- **IOVA** (44 @ $7.70, HC): ATM used up and terminated 9/30. A new ATM/S-3 is likely and would be a thesis break. Break: new ATM/offering, failed readout.
- **AMPL** (20 @ $17.15, Tech): Q3 rev +25%, FY guide +1.9%. Break: guide cut, equity raise.
- **APPN** (6 @ $51.73, Tech): Q3 beat + FY raise (8-K 2.02 11/05). **DE, verified 11/21 on the 10-Q cover** (EDGAR JSON field blank). Break: dilution, guide cut. (Bought at full size with VIX > 30. See W47 review.)
- **CAKE** (3 @ $117.25, Consumer): Q3 comps +15.2%, short 36%. Break: comp slowdown, margin hit, issuance.
- **CBRL** (5 @ $67.16, Consumer): 11/19 meeting uncontested. Earnings **12/02** (confirmed 11/23). Break: guide cut, issuance, contested-control event.
- Exiting Mon 11/23: **PAYS** (37 @ $9.38, rank 29).
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
