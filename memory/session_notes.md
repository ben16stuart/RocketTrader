# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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


## Session Archives

- `memory/archive/session_notes_2026-11.md` — November 2026 (11/02–11/13)
- `memory/archive/session_notes_2026-10.md` — October 2026 (through 10/31 review)
- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

---

## 2026-11-16 — midday (sonnet)
- No trades. All 8 satellites (AMPL, CAKE, CBRL, CDNA, GTLB, IOVA, PAYS, TXG) hold live trailing stops per open orders; none fired, no slot opened, so no refill. Own book -2.36% vs IWM -1.17% (loss cap $144: OK).
- News check (GTLB, CDNA, CAKE inline): results stale/undated, nothing dated today. No dilution, going-concern, guidance-cut or takeover found. No thesis break. GTLB -16.5% and CDNA -12.9% vs entry are price moves; the stop's job.
- STT still UNATTRIBUTED at broker (Bull's). Not touched.

## 2026-11-20 midday
- GTLB stopped out at $43.365 (about -$80). Filled slot with APPN (rank 9, 6 sh @ $51.73, 25% trail). Weekly trades 1/5. No thesis breaks among others (news searches found nothing fresh). 11/20 premarket rank file did not exist; midday ran rank_screen.py.
