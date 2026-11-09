# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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

## 2026-10-31 — WEEKLY REVIEW (Week 44, Saturday) — Grade A−; satellites 96.1% avg; NEO → OABI, KELYA → CAKE Monday

- Book **+7.32%** vs IWM +1.30% (**+6.02 pts**, ≈ +$220). Almost all of it is REPL (+≈$197, ≈ +6.5 pts of slice). Without REPL the book ≈ IWM. Fri −4.39% vs IWM −1.65%, so the book runs at high beta.
- Floor met at **5/5 closes** (82.7 → 101.6%, avg 96.1%). 1 closed trade (DK −2.6%, rank-decay exit). 4 entries.
- Ledger: Signal is monotone at 5d (top 8 +7.43%/48, 9–25 +2.60%/102, 26+ −0.07%/3991) and at 10d. Judgment 5d: VETO +4.72% (11) > BUY +0.76% (8). It is spread over categories (HC cap n=6), so no category reaches n ≥ 10. **No rule change.**
- Rank (10/30): TXG 1, REPL 2, QMCO 5, NSIT 7, CLDT 20, GTLB 23, **KELYA 26, NEO 27 → replace Mon**. **OABI #3** (HC slot freed by NEO) and **CAKE #15** (non-HC, non-Tech). See research_log W45.
- TXG cap ruling: the cap gate is **entry-only**. It has drifted back under anyway ($9.1B).
- HPE/STT are still UNATTRIBUTED (Bull's). Not touched.

---

## Session Archives

- `memory/archive/session_notes_2026-10.md` — October 2026 (through 10/30)
- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

---

## 2026-11-02 — midday (sonnet)
- TXG's 25% trailing stop filled 10:51 ET at $65.91 (hwm $87.82); logged. Slot refilled with CDNA (rank 6, 4 sh @ $86.10, 25% stop placed). 8 satellites: CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL; all with live stops.
- Only one news search (CDNA); others not searched. HPE/STT still UNATTRIBUTED; not touched. Note: no 11/02 rank file yet; used 10/30 ranking.

## 2026-11-04 — midday (sonnet)
- All 8 satellites (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, QMCO, REPL) hold live 25% trailing stops; none fired, no exits, no slot opened, no entries.
- News check (REPL, QMCO, OABI): results stale/undated; no offering, going-concern, guide cut or takeover found. No thesis break. Upcoming: QMCO and OABI earnings ~11/09 (held under stops).
- STT still UNATTRIBUTED at broker; not touched.

## 2026-11-05 — market_open (sonnet)
- QMCO 25% stop filled 10:36 ET @ $15.36 (logged). Bought PD 21 @ ~$16.53 (rank 23), 25% stop placed. QLYS (earnings 11/09) and ATRC (HC full) logged VETO. 8 slots: CAKE, CDNA, CLDT, GTLB, NSIT, OABI, REPL, PD. Weekly entries 4/5.
- Bull's HPE/CRWD stops also fired and DELL bought (not mine). STT still UNATTRIBUTED.

## 2026-11-05 — market_close
- No trades at close. 8 satellites held (CAKE, CDNA, CLDT, GTLB, NSIT, OABI, PD, REPL), 103.4% of slice, floor met; no IWM rebalance. IWM -4.44% today. Earlier: QMCO stop fired, PD refilled.
- STT still UNATTRIBUTED. Not touched.

## 2026-11-09 — market_open (sonnet)
- Sold PD and CLDT (rank decay), bought AMPL 20 @ $17.15 and PBF 5 @ $70.54, both with 25% trailing stops verified. Weekly entries 2/5. VIX 23.2, full size.
- Mistake: PBF stop was first placed at 5% by typo; caught on the next call, cancelled and replaced at 25% before any trigger.
- Search snippets for AMPL/PBF were stale; no fresh red flag. STT still UNATTRIBUTED.
