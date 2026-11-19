# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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

## Session Archives

- `memory/archive/session_notes_2026-11.md` — November 2026 (11/02–11/06)
- `memory/archive/session_notes_2026-10.md` — October 2026 (through 10/31 review)
- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

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


## 2026-11-16 — midday (sonnet)
- No trades. All 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG) hold live trailing stops per open orders; none fired, no slot opened, so no refill. Own book -2.36% vs IWM -1.17% (loss cap $144: OK).
- News check (GTLB, CDNA, CAKE inline): results stale/undated, nothing dated today. No dilution, going-concern, guidance-cut or takeover found. No thesis break. GTLB -16.5% and CDNA -12.9% vs entry are price moves; the stop's job.
- STT still UNATTRIBUTED at broker (Bull's). Not touched.
