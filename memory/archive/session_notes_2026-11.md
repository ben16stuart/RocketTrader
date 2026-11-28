# Rocket Session Notes — November 2026 (archived)

## 2026-11-06 — PREMARKET (Friday, Week 45 day 5) — 8 held, 0 open slots, VIX 28

- Book: 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, PD, REPL) ≈ 103% of the $2,849 slice. IWM 0. **Floor met.** Weekly entries 4/5. Own book this week −5.47% vs IWM −2.98% (−2.49 pts). Since 10/6: +3.33 pts.
- Holdings check (9 searches + 1 EDGAR): no thesis breaks. CLDT Q3 strong (RevPAR +8%, AFFO/sh +27%). NSIT Q3 strong (adj EPS +34%). CDNA's "$91 offering" is old: EDGAR shows only Form 4s and a 144 since the 10-Q. Searching "Caribou CDNA" returns CRBU, a different company.
- `rank_screen.py` (11/05 data, 726 eligible): OABI 2, NSIT 3, CDNA 4, REPL 7, CAKE 14, GTLB 21, **PD 29, CLDT 59**. These are for the Sat W45 review; rank decay is weekly. 0 open slots, so no picks and no VETOs owed.
- Macro: **11/05 was a −4.4% day (SPY −4.41%, IWM −4.59%).** VIX closed at 28.18 (26.88 live). That is above the 25 reduce-size line, below the 30 no-longs line. RTY flat live, NQ +1.31%. Search found no cause for 11/05 (results were 2025 articles). October payrolls are likely today at 8:30 ET (unconfirmed). No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-05 — PREMARKET (Thursday, Week 45 day 4) — 8 held, 0 open slots, NSIT/CLDT print today

- Book: 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL) ≈ 102% of the $3,018 slice. IWM 0. **Floor met.** Weekly entries 3/5. Own book this week +1.72% vs IWM +1.82% (−0.10 pts). Since 10/6: +6.14 pts.
- Holdings check (8 searches + 1 EDGAR): no thesis breaks. A QMCO "equity financing" headline is the June raise; EDGAR shows nothing since 10/09. Note that `data.sec.gov/submissions` JSON **worked via curl with a contact User-Agent** this session.
- `rank_screen.py` (11/04 data, 821 eligible): NSIT 2, OABI 3, CDNA 4, REPL 6, CAKE 10, QMCO 12, GTLB 18, CLDT 20. All ≤25. 0 open slots, so no picks and no VETOs owed.
- Macro: VIX 16.61 close 11/04 (16.83 live). RTY +0.63% live, NQ −0.54%. IWM 284.02 (+1.51%). Under the 22 brake. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-04 — PREMARKET (Wednesday, Week 45 day 3) — 8 held, 0 open slots, post-midterms

- Book: 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL) ≈ 103% of the $3,016 slice. IWM 0. **Floor met.** Weekly entries 3/5. Own book this week +1.94% vs IWM +0.05% (+1.90 pts). Since 10/6: +8.14 pts.
- Holdings check (8 searches): no thesis breaks. Unverified calendar claims: CDNA 11/04 AMC (already printed 10/29), OABI 11/03/11/09 (printed 10/30), REPL 11/09 BMO (ranker says 10/28). Held through either way.
- `rank_screen.py` (11/03 data, 759 eligible): OABI 2, CDNA 4, REPL 5, NSIT 6, QMCO 7, CAKE 18, CLDT 25, **GTLB 27** (Sat review; needs a non-HC replacement). Saved `ledger/ranks/2026-11-03.csv`. 0 open slots, so no picks and no VETOs owed.
- Macro: VIX 20.83 close 11/03 (18.24 live, −12%). **RTY +1.37%** live, ES +1.07%, NQ +1.01%: a post-election relief bid. Gold +2.8%. Brent 103.60 close. ADP 8:15, ISM Services 10:00 ET. Under the 22 brake. Earnings Thu 11/05: NSIT BMO, CLDT BMO. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-03 — PREMARKET (Tuesday, Week 45 day 2) — 8 held, 0 open slots, midterms

- Book: 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL) ≈ 102% of the $2,959 slice. IWM 0. **Floor met.** Weekly entries 3/5. Own book this week −1.02% vs IWM 0.00%. Since 10/6: +5.06 pts.
- Holdings check (8 searches): no thesis breaks. CAKE's $500M convert is old (≈2024). A web claim of "QMCO reports 11/03" conflicts with the ranker's 11/09; treat it as unverified.
- `rank_screen.py` (11/02 data, 769 eligible): OABI 2, QMCO 3, CDNA 4, NSIT 6, REPL 7, CAKE 12, CLDT 18, **GTLB 30** (for the Sat review; it needs a non-HC replacement). Saved `ledger/ranks/2026-11-02.csv`. 0 open slots, so no picks and no VETOs owed.
- 🛠️ **The KELYA "MISSING" flag was a log-format bug, not a lost position.** The 11/02 header read "NEO SELL / KELYA SELL", but `position_reconciler.py` splits multi-trade headers on **`+`** only, so KELYA's sale was never replayed. The header is fixed to `+`, and the replay now equals the 8 held. **Use `+` to join trades in one header.**
- Macro: VIX 21.15 close 11/02 (21.29 live), **close to the 22 brake**. RTY flat. Midterm election today plus JOLTS 10:00, so expect overnight headline risk into Wed. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-02 — PREMARKET (Monday, Week 45 day 1) — 8 held, 2 rank-decay swaps confirmed: NEO → OABI, KELYA → CAKE

- Book: 8 satellites ≈ 100% of the ≈$2,975 slice. IWM 0. **Floor met.** Weekly entries 0/5.
- Holdings check (keepers): no thesis breaks. TXG, QMCO, NSIT, CLDT and GTLB results were old or known. **REPL: a 424B5 surfaced, but EDGAR dates it 2026-08-10** (the known post-approval raise, before entry), so it is not a takedown.
- `rank_screen.py` (10/30 data, 738 eligible): **identical to the W44 review.** TXG 1, REPL 2, OABI 3, QMCO 5, NSIT 7, CLDT 20, GTLB 23, KELYA 26, NEO 27. Saved `ledger/ranks/2026-10-30.csv`.
- 🛠️ **Ranker "hangs" were the Mac deep-idling on battery** (pmset: DarkWake from Deep Idle), not a code bug. Two runs were killed at the time limits with zero output. Fixed by running under `caffeinate -i`. If launchd premarkets are going silent, check sleep before debugging the script.
- Picks confirmed: **OABI #3** (10-Q has no substantial doubt, $64.2M cash, ≥12mo runway, ATM undrawn) and **CAKE #15** (a web claim of "earnings 11/02 AMC" was falsified by the 10/27 8-K 2.02; insider Form 144/4s are a note).
- VETOs logged: IOVA #4 (EARNINGS 11/05), CDNA #6 (HC cap), ABCL #8 (FAIL non-US HQ).
- market_open: sell NEO 21 / KELYA 22 (cancel stops first, log EXITs with rank decay), buy OABI 69 / CAKE 3, place 25% trails, log BUYs. No IWM funding needed (≈$730 proceeds vs ≈$690). Skip a name that opens >8% above Fri close (OABI $5.11, CAKE $112.64) on no news.
- Macro: VIX 18.92 live, RTY +0.76%, ES +0.53%, Brent 108.41 (−4.4% roll-corrected). ISM Mfg 10:00 ET. **Midterms Tue 11/03.** No trades. No ntfy.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-02 — midday (sonnet)
- TXG's 25% trailing stop filled 10:51 ET at $65.91 (hwm $87.82); logged. Slot refilled with CDNA (rank 6, 4 sh @ $86.10, 25% stop placed). 8 satellites: CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL; all with live stops.
- Only one news search (CDNA); others not searched. HPE/STT still UNATTRIBUTED; not touched. Note: no 11/02 rank file yet; used 10/30 ranking.

---

## 2026-11-04 — midday (sonnet)
- All 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL) hold live 25% trailing stops; none fired, no exits, no slot opened, no entries.
- News check (REPL, QMCO, OABI): results stale/undated; no offering, going-concern, guide cut or takeover found. No thesis break. Upcoming: QMCO and OABI earnings ~11/09 (held under stops).
- STT still UNATTRIBUTED at broker; not touched.

---

## 2026-11-05 — market_open (sonnet)
- QMCO 25% stop filled 10:36 ET @ $15.36 (logged). Bought PD 21 @ ~$16.53 (rank 23), 25% stop placed. QLYS (earnings 11/09) and ATRC (HC full) logged VETO. 8 slots: CAKE, CDNA, CLDT, GTLB, NSIT, OABI, REPL, PD. Weekly entries 4/5.
- Bull's HPE/CRWD stops also fired and DELL bought (not mine). STT still UNATTRIBUTED.

---

## 2026-11-05 — market_close
- No trades at close. 8 satellites held (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, PD, REPL), 103.4% of slice, floor met; no IWM rebalance. IWM -4.44% today. Earlier: QMCO stop fired, PD refilled.
- STT still UNATTRIBUTED. Not touched.


<!-- archived at W47 review 2026-11-21 -->
## 2026-11-13 — PREMARKET (Friday, Week 46 day 5) — 8 held, 0 open slots, OABI/REPL still past exit rank

- Book: 8 satellites (AMPL, CAKE, CDNA, GTLB, NSIT, OABI, PBF, REPL) ≈ 103% of the $2,930 slice. IWM 0. **Floor met.** Weekly entries 2/5. Own book this week +1.85% vs IWM +1.74% (+0.12 pts). Since 10/6: +5.17 pts.
- Holdings check (8 searches + EDGAR lists for CDNA/REPL/OABI): no thesis breaks, no dilution filings. CDNA search again matched Caribou (CRBU): no read. REPL "earnings 11/13 BMO" still unverified (no 8-K).
- `rank_screen.py` (11/12 data, 762 eligible): CDNA 2, CAKE 6, AMPL 7, GTLB 8, PBF 22, NSIT 24, **OABI 54, REPL 119**. Saved `ledger/ranks/2026-11-12.csv`. 0 open slots, so no picks and no VETOs owed. Sat W46 review: likely replace OABI + REPL; TXG/IOVA/HAE become eligible once HC frees 2 slots. NSIT at 24 is on the edge.
- Macro: VIX 18.70 close 11/12 (18.36 live). RTY +0.11%, ES +0.19% live. IWM 278.44 (−1.64% 11/12). 10-yr 5.10% (+10bp). October PPI 8:30 ET today. Under the 25 line. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-12 — PREMARKET (Thursday, Week 46 day 4) — 8 held, 0 open slots, OABI/REPL past exit rank

- Book: 8 satellites (AMPL, CAKE, CDNA, GTLB, NSIT, OABI, PBF, REPL) ≈ 103% of the $2,935 slice. IWM 0. **Floor met.** Weekly entries 2/5. Own book this week +1.90% vs IWM +3.43% (−1.53 pts). Since 10/6: +3.57 pts.
- Holdings check (8 searches + EDGAR lists, OABI by CIK): no thesis breaks, no dilution filings. New since 11/11: only Form 4/144/13G on REPL and CDNA.
- `rank_screen.py` (11/11 data, 813 eligible): CDNA 2, CAKE 7, AMPL 8, GTLB 10, NSIT 17, PBF 22, **OABI 29, REPL 134** (6-1 window roll, not news). Sat 11/14 review decides. Saved `ledger/ranks/2026-11-11.csv`. 0 open slots, so no picks and no VETOs owed.
- Macro: VIX 17.49 close 11/11 (18.32 live). RTY +0.02%, ES −0.35%, NQ −0.75% live. IWM 283.09 (+0.89% 11/11). 10-yr 5.00%. Under the 25 line. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-11 — PREMARKET (Wednesday, Week 46 day 3) — 8 held, 0 open slots, REPL/PBF past exit rank

- Book: 8 satellites (AMPL, CAKE, CDNA, GTLB, NSIT, OABI, PBF, REPL) ≈ 103% of the $2,949 slice. IWM 0. **Floor met.** Weekly entries 2/5. Own book this week +4.03% vs IWM +2.55% (**+1.48 pts**). Since 10/6: +6.60 pts.
- Holdings check (8 searches + EDGAR lists): no thesis breaks, no dilution filings. CAKE 8-K 5.02 (11/10) = bakery president retiring (benign, read). OABI EDGAR ticker lookup was blank; re-ran by CIK and found nothing new. CDNA patent appeal heard 11/09 (≈$96M at stake): watch for the ruling.
- `rank_screen.py` (11/10 data, 791 eligible): CDNA 4, GTLB 6, AMPL 9, OABI 11, CAKE 15, NSIT 19, **REPL 30, PBF 40** (both >25). The Sat 11/14 review decides on Friday's data. Saved `ledger/ranks/2026-11-10.csv`. 0 open slots, so no picks and no VETOs owed.
- Macro: VIX 19.46 close 11/10 (18.69 live). RTY +0.65%, ES +0.79%, NQ +1.80% live. IWM 280.58 (−0.68% 11/10). 10-yr 4.98% (+12bp on 11/10, after CPI). Veterans Day: bonds closed, stocks open. Under the 25 line. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-10 — PREMARKET (Tuesday, Week 46 day 2) — 8 held, 0 open slots, CPI 8:30 ET

- Book: 8 satellites (AMPL, CAKE, CDNA, GTLB, NSIT, OABI, PBF, REPL) ≈ 103% of the $2,973 slice. IWM 0. **Floor met.** Weekly entries 2/5. Own book this week +3.65% vs IWM +3.15% (+0.50 pts). Since 10/6: +5.63 pts.
- Holdings check (8 searches): no thesis breaks. Results stale or undated. CDNA search returns CRBU (wrong company).
- `rank_screen.py` (11/09 data, 810 eligible): CDNA 5, OABI 6, AMPL 9, REPL 15, CAKE 16, GTLB 18, NSIT 24, **PBF 44** (bought 11/09 at rank 18). Rank decay is weekly → Sat 11/14 review decides. Saved `ledger/ranks/2026-11-09.csv`. 0 open slots, so no picks and no VETOs owed.
- Macro: VIX 19.92 close 11/09 (20.18 live). RTY +0.04%, ES +0.08%, NQ −0.26% live. IWM 282.51 (+3.23% 11/09). Brent 92.57 close. **October CPI today at 8:30 ET** (thriveinmarkets/fxnx calendars). Under the 25 line. No trades. No ntfy.
- Correction: the 11/09 market_close note "CDNA 11/5 8-K and REPL FQ2 still unread" was copied forward after the W45 review had already closed both as false (rule 39). Do not carry it further.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-09 — PREMARKET (Monday, Week 46 day 1) — 8 held, 2 replacements confirmed (PD → AMPL, CLDT → PBF), full size

- Book: 8 satellites ≈ 104% of the $2,888 slice. IWM 0. **Floor met.** Weekly entries 0/5 (2 planned today).
- Holdings check (6 searches: CDNA, OABI, REPL, NSIT, GTLB, CAKE; PD/CLDT skipped as exiting): no thesis breaks. Results stale or undated. "OABI/REPL earnings 11/09" are projected calendar dates; the ranker shows 10/30 and 10/28 already printed (rule 39). GTLB's "soft FY27 guide" is the old Q4 print. OABI presents at Stifel 11/11, Truist 11/12 and Jefferies London 11/16–19.
- `rank_screen.py` (still 11/06 data, 741 eligible): identical to the W45 review. AMPL #8, PBF #18 confirmed. **Logged 5 top-8 VETOs:** TXG/IOVA/RCEL/HAE (HC cap) and UTZ (going-private, verified on EDGAR). TXG #1 was missing from Saturday's VETO list.
- Owed checks done (EDGAR curl worked): AMPL 5.02 = a director added; PBF 5.02 = LTI grants. AMPL guide +1.9%. No dilution filings. **Full size: AMPL 20 / PBF 5** because VIX is 23.54 live; market_open re-checks against 25.
- Macro: RTY +1.27% live, ES +0.52%. Brent 96.37. CPI/PPI this week (day unconfirmed). Note: `market_data.py`'s footer still prints a "VIX >22 = pause" line that no rule file contains; the 25/30 lines govern. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-07 — WEEKLY REVIEW (Week 45, Saturday) — Grade B−; satellites 103.0% avg; PD → AMPL, CLDT → PBF Monday

- Book **−3.02%** vs IWM −2.03% (**−0.99 pts**, ≈ −$90). Since 10/6 +4.96 pts. Thu 11/05: book ≈ −7.1% vs IWM −4.6% (beta). Floor met 5/5 (avg 103.0%).
- 4 closed trades (2/4 wins, realized ≈ −$55): TXG and QMCO stops, NEO and KELYA rank decay. **All four exits beat holding** (KELYA −16% since).
- Ledger: Signal monotone at 5d/10d. **HC-cap VETO 5d +7.79% (n=11, 6 names) > BUY −0.33%**, but behind BUY at 10d. Hard Guardrail, so **escalated to Ben, no change.**
- Rank (11/06): CDNA 2, OABI 5, NSIT 14, CAKE 16, GTLB 20, REPL 24, **PD 26, CLDT 58 → replace Mon** with **AMPL #8 (Tech)** and **PBF #18 (Energy)**. Both DE, no dilution filings. **VIX 25.64: half size if still >25 at premarket** (AMPL 10 / PBF 2; full 20 / 5). Premarket reads both 8-K 5.02s. See research_log W46.
- Closed: the 11/06 midday's "CDNA 8-K 11/05" and "REPL FQ2" claims were false (Form 144; a 10-Q/A adding 10b5-1 plans). No thesis break.
- STT still UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-09 — market_open (sonnet)
- Sold PD and CLDT (rank decay), bought AMPL 20 @ $17.15 and PBF 5 @ $70.54, both with 25% trailing stops verified. Weekly entries 2/5. VIX 23.2, full size.
- Mistake: PBF stop was first placed at 5% by typo; caught on the next call, cancelled and replaced at 25% before any trigger.
- Search snippets for AMPL/PBF were stale; no fresh red flag. STT still UNATTRIBUTED.

## 2026-11-10 — midday: no trades
- All 8 satellites (AMPL, CAKE, CDNA, GTLB, NSIT, OABI, PBF, REPL) hold live 25% trailing stops (verified via open orders); none fired, no slot opened, so no refill.
- News check (GTLB, PBF, AMPL inline): results stale/undated, nothing dated today. No dilution, going-concern, guidance-cut or takeover found. No thesis break. GTLB -17.7% and PBF -5.4% vs entry are price moves; the stop's job.
- CDNA 11/5 8-K and REPL FQ2 print still unread (rule 57: needs EDGAR row). STT still UNATTRIBUTED at broker. Not touched.

## 2026-11-13 — market_open: no trades
- No WATCHING picks and 0 open slots (8/8 satellites, 102.4% of slice). The OABI (54) and REPL (119) rank decay is weekly, so the Sat 11/14 W46 review decides. No action before then.
- All 8 satellites still hold live 25% trailing stops; none fired. Own book -1.37% today vs IWM -0.25% (cap $145: OK). No ntfy (flat session).
- STT still UNATTRIBUTED at the broker; not touched.

## 2026-11-13 — midday (sonnet)
- No trades. All 8 satellites hold live trailing stops; none fired, no slot opened. Own book -0.78% vs IWM -0.71%; satellites 102.9% (floor met).
- News searches on REPL and GTLB returned stale/mismatched results (REPL snippet $12.86 vs broker $21.91). Nothing dated today, no thesis break.
- ~~Still owed: REPL 11/13 BMO earnings unverified; CDNA 11/5 8-K and REPL FQ2 print unread.~~ **All three CLOSED as false at the W46 review (EDGAR). Do not carry forward.** STT UNATTRIBUTED at broker, not touched.




---

<!-- archived at W48 review 2026-11-28 -->

## 2026-11-23 — PREMARKET (Monday, Week 48 day 1) — PAYS → INTA confirmed; VIX 29.67 live → INTA half size (3 sh) if still 25–30 at the open

- Book: 8 satellites (AMPL, APPN, CAKE, CBRL, CDNA, IOVA, PAYS, TXG), ~92% of the $2,802 slice. IWM 0. **Floor met.** Weekly entries 0/5. 1 slot opens when PAYS exits (rank 29).
- Holdings check (7 searches; PAYS skipped as it is exiting): no thesis breaks. Only Q3 recaps (CDNA, TXG and APPN guide raises; IOVA record Q3; AMPL +25%), TXG's 11/16 collaborations, and CAKE's dividend. No dilution, going-concern, guide cut or takeover.
- `rank_screen.py` (11/20 data, 546 eligible; identical to the W47 review): CDNA 1, TXG 3, AMPL 5, IOVA 8, APPN 9, CAKE 12, CBRL 17, PAYS 29. Pick: **INTA #10** (DE; EDGAR shows only insider Form 4/144 and the 8-K 5.07, no dilution filings). **VETOs logged:** SLN 2 (non-US), RCEL 4 and ATRC 6 (HC cap), UTZ 7 (going-private pin).
- CBRL earnings **12/02** confirmed (not an exit trigger).
- Macro: **VIX 29.67 live** (35.89 close 11/20). RTY +2.37%, ES +2.92%, NQ +3.61% live. Gold +3.0%. 10-yr 4.91% (11/20). Thanksgiving week: closed Thursday, half day Friday. No trades. No ntfy.
- market_open: execute research_log "Mon 11/23" with the VIX gate at 9:35. Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-21 — WEEKLY REVIEW (Week 47, Saturday) — Grade B; satellites 92.4% avg; PAYS → INTA Monday (VIX-gated)

- Book **−5.80%** vs IWM −7.54% (**+1.74 pts**, ≈ −$170). Since 10/6 +6.65 pts. Since 7/20 +7.12 pts. Floor met 5/5 (avg 92.4%).
- 5 closed trades (1/5 wins, realized ≈ +$216, almost all REPL's earlier gain): REPL +96%, NSIT −4.6%, PBF −2.3%, OABI −5.3% (rank decay), GTLB −23.6% (stop). The Monday rotation paid: the 4 exits fell avg −7.1% by Friday, the 4 buys −2.0%.
- **Process failures:** (1) Fri premarket died after 3h15m (Mac slept), no note and no rank file. (2) Fri midday bought APPN at **full size with VIX > 30** (premarket close 28.44, premarket live 30.47, close 35.89). The VIX rule lives only in premarket.md. (3) APPN's EDGAR incorporation check was skipped (verified now: Delaware, 10-Q cover; the JSON field is blank). (4) Fri close ntfy prose said Rocket beat IWM on a day it lagged. (5) Midday logged "weekly trades 1/5"; the true count is 5/5.
- Ledger: Signal 5d top8−26+ +1.54% (w=5, t +0.49). BUY 20d +4.39% (8 names) vs VETO −6.97% (10 names); twins 20d 82nd pct. Vetoes helping, nothing at its bar. **No change.**
- Rank (11/20 data): CDNA 1, TXG 3, AMPL 5, IOVA 8, APPN 9, CAKE 12, CBRL 17, **PAYS 29 → replace Mon with INTA #10** (DE, no dilution filings). **VIX closed 35.89: if > 30 at the open, sell PAYS and park the proceeds in IWM, no INTA.** 25–30 → INTA 3 sh; < 25 → 7 sh.
- STT still UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-19 — PREMARKET (Thursday, Week 47 day 4) — 8 held, 0 open slots; CBRL missing from the ranking (download failure)

- Book: 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG), ~94% of the $2,867 slice. IWM 0. **Floor met.** Weekly entries 4/5. Own book this week −0.02% vs IWM −2.68% (+2.66 pts). Since 10/6: +7.86 pts.
- Holdings check (8 searches): no thesis breaks, only Q3 recaps and stale items.
- `rank_screen.py` (11/18 data, 677 eligible; it ran ~6 min): CDNA 1, IOVA 2, TXG 4, CAKE 6, AMPL 10, PAYS 12, GTLB 23. **CBRL "NOT ELIGIBLE" came from a yfinance failed download (12 tickers failed), not real data.** No action. The weekly review must confirm its real rank. Unheld top 8: SLN 3 (FAIL), HAE 5, UTZ 7, ELF 8. No slots, so no picks or VETOs owed. Saved `ledger/ranks/2026-11-18.csv` (CBRL is absent from it).
- Macro: VIX 24.56 close 11/18 (under 25), 21.94 live. RTY +0.72%, NQ +2.35% live (post-NVDA). IWM 270.12 (+0.40%). 10-yr 5.07%. Today: claims + Philly Fed 8:30, existing home sales 10:00. CBRL's annual meeting is today. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-18 — PREMARKET (Wednesday, Week 47 day 3) — 8 held, 0 open slots; VIX closed 25.46

- Book: 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG), 91.8% of the $2,855 slice. IWM 0. **Floor met.** Weekly entries 4/5. Own book this week −1.63% vs IWM −3.09% (+1.46 pts). Since 10/6: +6.59 pts.
- Holdings check (8 searches): no thesis breaks. Everything was Q3 recaps or stale (CDNA appeal: no ruling found; PAYS plasma loss is the known 11/09 item; GTLB CFO story is prior-year).
- `rank_screen.py` (11/17 data, 672 eligible): CDNA 1, IOVA 3, TXG 4, CAKE 6, CBRL 7, PAYS 12, AMPL 13, GTLB 21, all ≤ 25. Unheld top-8 names: SLN 2 (FAIL), HAE 5, UTZ 8. 0 slots, so no picks and no VETOs owed. Saved `ledger/ranks/2026-11-17.csv`.
- Macro: **VIX closed 25.46 on 11/17** (above the 25 line), 23.77 live. IWM 269.05 (−1.43%). RTY flat live, NQ +0.95%. FOMC minutes 2 PM. NVDA after the close. If a stop opens a slot, the VIX rule pauses or reduces any refill. No trades. No ntfy.
- Watch: GTLB at rank 21 is near the >25 exit line for Saturday's review. Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-17 — PREMARKET (Tuesday, Week 47 day 2) — 8 held, 0 open slots; reconciler MISSING fixed

- Book: 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG), 91.3% of the $2,868 slice. IWM 0. **Floor met.** Weekly entries 4/5. Own book this week −2.34% vs IWM −1.64% (−0.70 pts). Since 10/6: +4.42 pts.
- **Fixed:** the snapshot flagged NSIT/PBF/OABI MISSING. Cause: the 11/16 header "NSIT + PBF + OABI + REPL SELL" had its verb only in the last `+` segment. I appended per-name SELL headers to trade_log, which cleared MISSING, and tightened rule 20b (each segment needs its own verb).
- Holdings check (8 searches): nothing dated or thesis-breaking. IOVA "equity raise" is old. EDGAR shows only Form 4 and 13G filings since 11/05.
- `rank_screen.py` (11/16 data, 716 eligible): TXG 1, CDNA 2, IOVA 3, CBRL 6, CAKE 7, PAYS 10, AMPL 12, GTLB 18, all ≤ 25. Unheld top-8 names: HAE 4, UTZ 5, RCEL 8. 0 slots open, so no picks and no VETOs owed. Saved `ledger/ranks/2026-11-16.csv`.
- Macro: VIX 22.91 close 11/16 (23.40 live), under 25. RTY −0.52% live. IWM 272.94 (−1.66% 11/16). 10-yr 5.12%. Retail sales and import prices at 8:30 ET, industrial production at 9:15. No trades. No ntfy.
- Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-16 — PREMARKET (Monday, Week 47 day 1) — 4 rank-decay swaps confirmed: TXG, IOVA, PAYS, CBRL at full size

- Book: 8 satellites ≈ 103% of the $2,920 slice. IWM 0. **Floor met.** Weekly entries 0/5 (4 planned). The snapshot's "−1.02% today" is from thin premarket prints. Ignore it.
- Holdings check (4 searches: CDNA, GTLB, CAKE, AMPL; the 4 exits skipped): no thesis breaks. Results were Q3 recaps or older (GTLB's "CFO transition / −14%" is the FY26 Q3 story). CDNA patent-appeal ruling: none found.
- `rank_screen.py` (still 11/13 data, 758 eligible): identical to the W46 review. Saved `ledger/ranks/2026-11-13.csv`. Exits stay NSIT 41, PBF 42, OABI 50, REPL 157.
- Owed checks done (EDGAR curl): IOVA ATM fully used and terminated 9/30, nothing in the last 30 days, no binary within 10 trading days, not a going concern. PAYS revenue guide reaffirmed, profit guides raised. CBRL 11/19 meeting is uncontested (the 2025 Biglari fight was misdated by search). **Logged VETOs:** HAE 4, UTZ 5, ABCL 7.
- Macro: VIX 19.91 live (19.30 close 11/13). RTY −0.41%, ES −0.32%, NQ −0.87% live. 10-yr 5.15% (11/13). Under the 25 line, so full size. No trades. No ntfy.
- market_open: execute research_log "Mon 11/16" as written. Still unresolved: STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-11-14 — WEEKLY REVIEW (Week 46, Saturday) — Grade B; satellites 103.2% avg; 4 rank-decay swaps Monday

- Book **+1.61%** vs IWM +1.41% (**+0.20 pts**, ≈ +$46). Since 10/6 +5.24 pts. Since 7/20 +5.80 pts. Floor met 5/5 (avg 103.2%).
- 2 closed trades (1/2 wins, realized ≈ +$28): CLDT +12.3% and PD −4.5%, both rank-decay exits. Both were about neutral vs IWM afterwards. No stops fired.
- Ledger (now `w`/names): Signal 5d top8−26+ +1.98% (w=4, t +0.49). BUY 20d +12.59% (5 names, 97th-pct twin) vs VETO +4.99% (4). No cell clears its bar. **No change.**
- Rank (11/13): CDNA 2, AMPL 6, CAKE 8, GTLB 11, **NSIT 41, PBF 42, OABI 50, REPL 157 → replace Mon** with **TXG #1, IOVA #3 (or HAE #4), PAYS #9, CBRL #15**. See research_log W47 for the owed checks.
- **Rule 39 failure:** midday/close repeated the closed "CDNA 8-K / REPL FQ2" claims plus a false "REPL earnings 11/13" 9 times. The CLOSED line is now in trade_log, which is what those routines copy.
- STT still UNATTRIBUTED (Bull's). Not touched.

---


## 2026-11-16 — midday (sonnet)
- No trades. All 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG) hold live trailing stops per open orders; none fired, no slot opened, so no refill. Own book -2.36% vs IWM -1.17% (loss cap $144: OK).
- News check (GTLB, CDNA, CAKE inline): results stale/undated, nothing dated today. No dilution, going-concern, guidance-cut or takeover found. No thesis break. GTLB -16.5% and CDNA -12.9% vs entry are price moves; the stop's job.
- STT still UNATTRIBUTED at broker (Bull's). Not touched.

## 2026-11-20 midday
- GTLB stopped out at $43.365 (about -$80). Filled slot with APPN (rank 9, 6 sh @ $51.73, 25% trail). Weekly trades 1/5. No thesis breaks among others (news searches found nothing fresh). 11/20 premarket rank file did not exist; midday ran rank_screen.py.
