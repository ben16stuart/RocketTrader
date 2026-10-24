# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-10-24 — WEEKLY REVIEW (Week 43, Saturday) — Grade B−; satellites 56.8% avg; DK → QMCO Monday

- Book **+1.79%** vs IWM +1.96% (**−0.18 pts**, ≈ +$54). Satellites ≈ IWM from entry. The gap is the ~9% cash buffer in an up week. 0 closed trades.
- Floor met at **5/5 closes** (56–57.5%). The 20-close breach streak is over. 20/20 routines ran.
- Ledger: 5d only, n tiny (top 8 +0.16%/8, BUY +1.02%/5 vs VETO +1.10%/4). **No rule change.**
- Rank (10/23): TXG #1, REPL #2, NSIT #8, NEO #9, **DK #75 → EXIT Mon**. Monday: QMCO #5 (replaces DK), GTLB #17, CLDT #25. UTZ #18 VETO logged (cash take-private). APPS #16 is an earnings veto.
  Premarket owes the QMCO 8-K 8.01 and convert-exchange date check. See research_log.
- Lesson: an owed pre-entry check (REPL FDA outcome) was skipped at the 10/19 open. A check handed to market_open must be done before the order.
- REPL and NEO report 10/28 (held through). FOMC 10/28: no entries that day. HPE/STT are still unattributed (Bull's).

---

## 2026-10-23 — PREMARKET (Friday, Week 43 day 5) — 5 satellites held, 0 open slots, DK rank 46

- Book: satellites ≈57% (DK, NEO, NSIT, REPL, TXG), IWM ≈34%, cash ≈9%. Slice $3,022.62. **Floor met.** Own book this week +1.62% vs IWM +1.86% (−0.24 pts). Since 10/6: +0.16 pts.
- Weekly entry cap 5/5 used (all on 10/19), so **0 open slots** until Mon 10/26. No picks and no VETOs owed.
- Holdings check (5 searches): no thesis breaks. Results were older items: REPL BLA history, TXG Q2 raise, NEO Q2 raise and the 6/22 convert (not fresh), NSIT product launches, DK analyst PTs.
- `rank_screen.py` (10/22 data, 730 eligible): TXG #1, REPL #3, NSIT #6, NEO #8, **DK #46** (33 → 36 → 46). Saved `ledger/ranks/2026-10-22.csv`.
  REPL's screener earnings date moved to **10/28** (gate "EARNINGS in 3d"). It is held, so the gate is entry-only and REPL is held through the print.
  **For the Sat 10/24 weekly_review:** DK is far beyond 25, so replace it Mon 10/26 unless something changes. HC is full (REPL/TXG/NEO). Non-HC candidates: APPS #12, GTLB #14, QMCO #15 (Tech, 2 slots left under the cap), UTZ #16.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.
- Macro: VIX 19.68 live, RTY −0.47%, ES −0.19%, Brent 109.73 (rolled to BZF27). 10Y printed 4.95% (−20bp, unverified). No event search (flash PMIs known from the calendar). No trades. No ntfy.

---

## 2026-10-22 — PREMARKET (Thursday, Week 43 day 4) — 5 satellites held, 0 open slots, DK rank 36

- Book: satellites **57.6%** (DK, NEO, NSIT, REPL, TXG), IWM 33.5%, cash 8.9%. Slice $3,038.32. **Floor met.** Own book this week +2.47% vs IWM +1.36% (+1.11 pts).
- Weekly entry cap 5/5 used (all on 10/19, per trade_log; the snapshot's counter is still broken, rule 24), so **0 open slots** until Mon 10/26. No picks and no VETOs owed.
- Holdings check (5 searches + 1 EDGAR pull): no thesis breaks. The NEO search surfaced a "$275M convertible notes offering". EDGAR dates it to the **6/22 8-K** (items 1.01/2.03/3.02), outside 30d, so it is not fresh dilution. NEO is incorporated in NV (US).
  NEO's 10/05 8-K (2.02/5.02/5.03) predates the 10/19 entry. NEO Q3 is 10/28 (EARNINGS gate in 4d: entry rule only, held through).
- `rank_screen.py` (10/21 data, 708 eligible): REPL #1, TXG #2, NEO #7, NSIT #12, **DK #36** (was #33). Saved `ledger/ranks/2026-10-21.csv`.
  **For the Sat 10/24 weekly_review:** DK is >25 for the 2nd straight day. If it is still >25 Saturday, replace it Mon 10/26. HC already holds 3 (REPL/TXG/NEO), so the HC names OABI #3 / XGN #6 / ATRC #8 are blocked by the sector cap. Next eligible non-HC names: **APPS #11, QMCO #13, BLZE #16** (Tech: NSIT + 2 = 3, at the cap).
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's 10/19 buys). Not Rocket's, not touched.
- Macro: VIX 18.43 live (+10.5%), **NQ −1.74%, RTY −0.83%**, ES −1.01%, Brent 111.76 (+2.7%), 10Y 5.15%. Tech-led risk-off, under the VIX 22 brake. 1 event search (undated result, not relied on). No trades (market closed). No ntfy (no breaking news).

---

## 2026-10-21 — PREMARKET (Wednesday, Week 43 day 3) — 5 satellites held, 0 open slots, DK rank 33

- Book: satellites **56.6%** (DK, NEO, NSIT, REPL, TXG), IWM 33.9%, cash 9.5%. Slice $3,017.10. **Floor met.** Own book this week +1.18% vs IWM +1.67% (−0.49 pts).
- Weekly entry cap 5/5 used (snapshot's "0/5" counter is still broken, rule 24), so **0 open slots** until Mon 10/26. No picks and no VETOs owed.
- Holdings check (5 searches): no thesis breaks. Only scheduled-earnings PRs (TXG 11/05 AMC, NEO 10/28 AMC, DK 11/06 BMO). REPL's $150M raise at $12.06 is the August 424B5 (outside 30d).
  REPL Q3 date still conflicts: 10/29 (search) vs 11/05 (screener). Held either way.
- `rank_screen.py` (10/20 data, 708 eligible): REPL #1, TXG #2, NEO #5, NSIT #11, **DK #33**. Saved `ledger/ranks/2026-10-20.csv`.
  **For the Sat 10/24 weekly_review:** DK is >25. If it is still >25 Saturday, replace it Monday 10/26. Next eligible non-HC names: QMCO #9, APPS #10 (Tech: would be the 2nd/3rd Tech with NSIT).
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's 10/19 buys; Bull's log header parses only the first ticker). Not Rocket's, not touched.
- Macro: VIX 17.50 live, RTY −0.23%, 10Y 5.12%, Brent 110.76. 6 searches. No trades (market closed). No ntfy (no breaking news).

---

## 2026-10-20 — PREMARKET (Tuesday, Week 43 day 2) — 5 satellites held, 0 open slots, books fixed

- **Reconciler fix:** the snapshot was reporting **0 satellites (floor breached)** because the 10/19 trade_log headers ("Satellite BUYS…", "CORE FUNDING — IWM SELL for …") weren't in a format `position_reconciler.py` parses. I reworded both headers (same content). Now: satellites **56.3%** (DK, NEO, NSIT, REPL, TXG), IWM 33.9%, cash 9.8%. **Floor met.**
  For future logs: one `SYM ENTRY` per `+` segment, and core trades as `IWM — SELL (CORE REBALANCE …)`.
- **For Bull:** HPE and STT show as UNATTRIBUTED. They are Bull's 10/19 buys, but Bull's header "DELL / FTNT / HPE / STT — BUY" only parses the first ticker. That fix belongs in Bull's log; I did not edit it.
- Snapshot "Weekly Trade Count 0/5" is wrong too: per trade_log, **5/5 entries are used** this week, so 0 open slots until Mon 10/26. No picks and no VETOs needed today.
- Holdings check (5 searches): no thesis breaks. **REPL:** FDA Accelerated Approval of TUDRIQEV (RP1) in Aug, which settles the open item. NEO Q3 is 10/28 AMC (held through it). TXG Q3 is 11/05 AMC.
- `rank_screen.py` (10/19 data): REPL #1, TXG #2, NEO #4, NSIT #7, DK #18. All ≤25. Saved `ledger/ranks/2026-10-19.csv`.
- Macro: VIX 18.73 live, RTY +0.06%, 10Y 5.14%, Brent 111. No trades (market closed). No ntfy (no breaking news).

---

## 2026-10-19 — PREMARKET (Monday, Week 43 day 1) — first rank → judge board: 5 WATCHING, 4 VETOs logged

- Satellites 0.0% (floor breached at 20 straight closes). Slice $2,997.62. IWM core 9.9763 sh. Shared cash $986.15. Open slots = 5 (weekly cap).
- `rank_screen.py`: 651 eligible of 1,830. Data as of the 10/16 close, saved to `ledger/ranks/2026-10-16.csv`.
- **Picks (WATCHING):** REPL #1 (33 sh), TXG #3 (5), NEO #4 (21), DK #8 (4), NSIT #9 (2). Total ≈ $1,685 ≈ **56% of slice**.
- **VETOs logged:** SMWB #2 and ABCL #5 (non-US HQ), OABI #6 and SDGR #7 (HC cap).
- EDGAR worked from a script today (`data.sec.gov/submissions` with a UA header). One call gives both incorporation and recent filings, so it covers
  the filings look for 8 names in one shot. All US-incorporated. Of the 8, only REPL has an offering (424B5 8/10, outside 30d) plus an S-3ASR shelf.
- **market_open owes:** (1) verify REPL's August RP1 FDA outcome before buying it; (2) one CORE FUNDING IWM sale, then 5 market buys,
  then 25% trailing stops; (3) **NEO is Monday-only**: if it doesn't fill 10/19, log a VETO (earnings 10/27 ≤5 td); (4) log each fill with
  `candidate_ledger.py log SYM BUY ... --rank N`. Next in line: GTLB #11, UTZ #12.
- Macro: VIX 18.63 live, RTY +0.45% live. FOMC 10/27–28. 7 searches used. No trades (market closed). No ntfy (no held satellites).

---

## 2026-10-17 — WEEKLY REVIEW (Week 42, Saturday) — Grade F; satellites 0.0% avg; rank → judge starts Monday

- Book **−2.75%** vs IWM −3.05% (**+0.30 pts**, all cash buffer). −$84.80, the IWM mark only. 0 trades. Satellites **0.0% at 5/5 closes** (breaches #16–#20, all logged).
- Rule 8 searched daily: 7 conditional plans (TRAX/OIG/CODI/VSTM/HAWK/RAPP/EIKN), **0 entries**. Kill counterfactual 3 up / 3 down / 1 flat vs IWM −3%: the gates were a coin flip.
- Ledger empty (n = 0), so no learning-loop change. The rebuild was Ben's structural call (10/16).
- **Mon 10/19 premarket:** run `rank_screen.py`, fill up to 5 slots (3 HC max). Top 8 as of 10/16: REPL, SMWB (FAIL, Israel), TXG, NEO, ABCL (FAIL, Canada), OABI, SDGR, DK; then NSIT, HNGE, GTLB. Log every top-8 skip as a VETO. Check VIX first: it closed 19.99 (+21%), and the brake is 22.
- 20/20 routines ran. Session-note gaps: 10/13 open, 10/14 close.

---

## Session Archives

- `memory/archive/session_notes_2026-10.md` — October 2026 (through 10/15)
- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

---

## 2026-10-19 — MIDDAY (Monday, Week 43 day 1) — 5 satellites held, no action
- Mine: REPL, TXG, NEO, DK, NSIT (all bought at open, ~56% of slice). Trailing stops live on all five (snapshot open-orders). No stop fired. Prices: REPL -1.4%, TXG +2.0%, NEO -1.1%, DK -4.1%, NSIT +1.2% vs entry. Price is the stop's job; no cuts.
- News: nothing thesis-breaking. NEO: prelim Q3 rev ~$209M, FY guide to rise at midpoint, CEO succession 1/4/27 (not a break; earnings 10/27-28 still ahead). REPL: search returned only the old adcom/Aug-2 PDUFA items, FDA outcome still unverified (carried from open). TXG, DK, NSIT: no fresh news found (results stale).
- Snapshot reconciliation lists DK/NEO/NSIT/REPL/TXG as "unattributed" (trade_log entries 10/19 lack the format the reconciler parses) and HPE/STT as unattributed too (not Rocket buys; presumably Bull's). Needs a reconciler fix / attribution check, not a trading action.
- No open slot, no new entries (5/5 weekly cap used). No ntfy.

## 2026-10-20 midday (sonnet)
- Satellites REPL +4.1%, TXG +4.3%, NSIT +2.3%, NEO 0.0%, DK -4.1%. All 5 have live 25% trailing stops. No stops fired, no exits, no new entries (no slot opened).
- News: REPL no new filing seen (RP1 adcom positive reaction is older news; 424B takedown still unverified). NEO pre-announced Q3 rev ~$209M, FY guide up at midpoint, CEO succession (Stone CEO 1/4/27) -- not a thesis break, and the pre-announcement may soften the 10/27-28 earnings gate. TXG, DK, NSIT: nothing new.

## 2026-10-21 midday (Rocket)
- All 5 satellites (REPL +7.8%, TXG +10.8%, NEO +1.6%, DK -1.7%, NSIT +3.8%) hold live trailing stops per snapshot. No stop fired, no exits, no trades.
- News: NEO DOJ civil settlement finalized + PT raises (not a thesis break; earnings 10/27-28 still ahead). REPL: positive adcom/upgrades. TXG/DK/NSIT not searched (no signal). No slot opened, so no fill.
- HPE/STT still unattributed at broker; untouched.

## 2026-10-22 — midday
- All 5 satellites (DK, NEO, NSIT, REPL, TXG) hold live 25% trailing stops; none fired. No thesis breaks in news (NEO: CEO succession 1/4/27 + prelim Q3 rev ~$209M, FY guide up at midpoint; REPL earnings 10/29; no dilution/going-concern headlines found). No trades, no slot opened. HPE/STT still unattributed.

## 2026-10-23 — midday
- No trades. All 5 satellites (DK -4.5%, NEO -2.0%, NSIT +7.5%, REPL +6.1%, TXG +2.6%) hold live 25% trailing stops (verified in open orders). No stop fired.
- News check (5 inline searches): no thesis break. NEO: prelim Q3 rev ~$209M, FY guide to rise at midpoint, CEO succession 1/4/27 (BTIG upgrade) — thesis intact; NEO earnings 10/27–28 still inside hard-veto window of entry, already held. Other searches returned stale/undated results, nothing new on dilution/going concern.
- No slot opened; no fill step. HPE/STT still UNATTRIBUTED (have 15% stops; untouched).
