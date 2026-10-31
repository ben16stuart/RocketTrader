# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-10-31 — WEEKLY REVIEW (Week 44, Saturday) — Grade A−; satellites 96.1% avg; NEO → OABI, KELYA → CAKE Monday

- Book **+7.32%** vs IWM +1.30% (**+6.02 pts**, ≈ +$220). Almost all of it is REPL (+≈$197, ≈ +6.5 pts of slice). Without REPL the book ≈ IWM. Fri −4.39% vs IWM −1.65%, so the book runs at high beta.
- Floor met at **5/5 closes** (82.7 → 101.6%, avg 96.1%). 1 closed trade (DK −2.6%, rank-decay exit). 4 entries.
- Ledger: Signal is monotone at 5d (top 8 +7.43%/48, 9–25 +2.60%/102, 26+ −0.07%/3991) and at 10d. Judgment 5d: VETO +4.72% (11) > BUY +0.76% (8). It is spread over categories (HC cap n=6), so no category reaches n ≥ 10. **No rule change.**
- Rank (10/30): TXG 1, REPL 2, QMCO 5, NSIT 7, CLDT 20, GTLB 23, **KELYA 26, NEO 27 → replace Mon**. **OABI #3** (HC slot freed by NEO) and **CAKE #15** (non-HC, non-Tech). See research_log W45.
- TXG cap ruling: the cap gate is **entry-only**. It has drifted back under anyway ($9.1B).
- HPE/STT are still UNATTRIBUTED (Bull's). Not touched.

---

## 2026-10-30 — PREMARKET (Friday, Week 44 day 5) — 8 held, 0 open slots

- Book: 8 satellites ≈ 100% of the $3,055 slice. IWM 0. **Floor met.** Own book this week +11.30% vs IWM +3.00% (+8.31 pts). Since 10/6: +8.38 pts.
- Holdings check (8 searches): no thesis breaks. All results were old or known items.
- `rank_screen.py` (10/29 data, 791 eligible): TXG #1, REPL #3, QMCO #5, NSIT #8, GTLB #19, CLDT #23, NEO #24, **KELYA #31** (for the Sat review). Saved `ledger/ranks/2026-10-29.csv`.
- 0 open slots (8/8; weekly 4/5). No picks, no VETOs owed.
- Macro: VIX 18.46 live (17.20 close 10/29), **NQ −2.37%, ES −1.07%, RTY −0.67%** live. Brent 113.23 (+2.2%, roll-corrected). Bull's DELL/HPE/ILMN are weak after hours. The one event search found nothing specific dated today. Under the VIX 22 brake. No trades. No ntfy (no position-specific breaking news).
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-10-29 — PREMARKET (Thursday, Week 44 day 4) — 8 held, 0 open slots

- Book: 8 satellites (TXG, REPL, QMCO, NSIT, NEO, GTLB, CLDT, KELYA) ≈ 99% of the slice; IWM sold to 0 at the 10/28 close. **Floor met.** Own book this week +10.01% vs IWM +2.13% (+7.88 pts). Since 10/6: +7.97 pts.
- Holdings check: no thesis breaks. **NEO beat and raised** (FY26 revenue $802–806M). REPL's 10-Q has the going-concern doubt alleviated and no ATM sales. QMCO's "equity financing" hit is the June deal (known).
- `rank_screen.py` (10/28 data, 764 eligible): TXG #1, REPL #2, QMCO #4, NSIT #12, NEO #20, GTLB #23, **CLDT #27, KELYA #37** (both are for the Sat review). Saved `ledger/ranks/2026-10-28.csv`.
- 0 open slots (8/8; weekly 4/5). No picks, no VETOs owed. Sat review: replacing CLDT/KELYA will need a non-HC/non-Tech name, and none passes ≤25 today.
- Macro: VIX 17.02 live, RTY +0.57%, NQ −0.94%, 10Y 5.05%, Brent 110.28. No trades. No ntfy.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-10-28 — PREMARKET (Wednesday, Week 44 day 3) — 8 held, 0 open slots, FOMC day

- Book: 8 satellites (TXG, QMCO, REPL, NSIT, NEO, GTLB, CLDT, KELYA) ≈ 95% of the $3,156 slice. **Floor met.** Own book this week +6.26% vs IWM +1.37% (+4.89 pts). Since 10/6: +5.03 pts.
- Holdings check (8 searches): no thesis breaks. REPL and NEO report today and are held through.
- `rank_screen.py` (10/27 data, 748 eligible): TXG #1, QMCO #2, REPL #4, NSIT #8, NEO #16, GTLB #24, **CLDT #28, KELYA #34** (both past 25; for the weekly review, not a daily exit). Saved `ledger/ranks/2026-10-27.csv`.
- 🆕 TXG gate `FAIL cap $10.2B`: over the universe ceiling while #1. Cap drift is not an exit trigger. Flagged for the Sat review (see research_log).
- 0 open slots (8/8 held; weekly entries 4/5). No picks, no VETOs owed. FOMC 2:00 PM ET: no entries today anyway.
- Macro: VIX 17.51 live, RTY −0.21%, ES +0.08%, Brent 111.20 (+1.6% roll-corrected). No event search (FOMC already on the calendar). No trades. No ntfy.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-10-27 — PREMARKET (Tuesday, Week 44 day 2) — 7 held, 1 slot → KELYA #25

- Book: 7 satellites (TXG, QMCO, REPL, NSIT, NEO, GTLB, CLDT) ≈ 83% of the $3,069 slice. **Floor met.** Own book this week +2.65% vs IWM +0.29% (+2.36 pts). Since 10/6: +2.54 pts.
- Holdings check (7 searches): no thesis breaks. ⚠️ GTLB: an actively exploited max-severity CVE (CVE-2026-85706). Flagged, not a break.
- `rank_screen.py` (10/26 data, 714 eligible): TXG #1, QMCO #2, REPL #4, NSIT #8, NEO #13, GTLB #21, CLDT #23. All ≤25.
- 1 open slot (8−7). Weekly entries 3/5. HC and Tech caps both full. **Pick: KELYA #25** (staffing, DE, no dilution filings since May, earnings 11/05–09, ADV 313k thin). It sits at the exit edge, like CLDT.
- VETOs logged: OABI #3, CDNA #5 (EARNINGS + HC cap), XGN #6, TWST #7 (HC cap).
- market_open: sell IWM ≈$365 (CORE FUNDING), buy KELYA 22 sh, set the 25% trail, log the BUY. Projected satellites ≈95%, IWM ≈$180.
- Macro: VIX 18.29 live, RTY −0.13%, ES −0.04%, Brent 111.09. Conf. Board confidence + new home sales 10:00 ET. FOMC Wed: no entries 10/28. No trades. No ntfy.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## 2026-10-26 — PREMARKET (Monday, Week 44 day 1) — DK → QMCO; GTLB + CLDT fill; slot 8 empty

- Book: 5 satellites (DK, NEO, NSIT, REPL, TXG), floor met. Slice $3,034.78. Own book this week +0.05% vs IWM +0.24%. Since 10/6: +0.03 pts.
- Holdings check (4 searches; DK skipped because it is exiting): no thesis breaks. NSIT's earnings date conflicts: **10/29** (search) vs 11/05 (screener). It is held through either way.
- `rank_screen.py` (10/23 data again, 712 eligible): TXG #1, REPL #2, NSIT #8, NEO #9, DK #75. Picks unchanged from Saturday: **QMCO #5, GTLB #17, CLDT #25**.
- QMCO owed checks are DONE. The convert exchange (12/2025) and its conversion to stock (6/2026) are both outside 30d. The 10-Q has no substantial-doubt language. No S-1/S-3/424B.
  ⚠️ **The CFO was terminated "effective immediately" on 10/09.** It is flagged in the card, not vetoed.
- VETOs logged: OABI #3, XGN #4, CDNA #6, TWST #7 (HC cap, plus EARNINGS for OABI/CDNA), APPS #16 (EARNINGS), QLYS #20 (Tech cap).
- market_open: sell DK, fund ≈$740 from IWM, buy QMCO 20 / GTLB 6 / CLDT 25, set 25% trails, log the BUYs and the DK EXIT. Projected satellites ≈82%.
- Macro: VIX 19.27 live (under the 22 brake), RTY +0.33%, ES +0.30%, Brent 110.14 (−1.4%), 10Y 4.99%. No event search (FOMC 10/28 already on the calendar). No trades. No ntfy.
- Still unresolved: HPE / STT UNATTRIBUTED (Bull's). Not touched.

---

## Session Archives

- `memory/archive/session_notes_2026-10.md` — October 2026 (through 10/24)
- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

---

## 2026-10-26 — midday (sonnet)
- Satellites NEO, NSIT, REPL, TXG, QMCO, GTLB, CLDT all hold live 25% trailing stops; none fired. No price-based cuts (rule: price is the stop's job).
- News: NEO prelim Q3 rev ~$209M, FY guide up at midpoint, CEO succession (positive; earnings 10/27–28 still ahead). REPL post-adcom, no dilution seen. QMCO no thesis break found (search results stale/mixed; earnings 11/09). GTLB, CLDT, TXG, NSIT not searched (budget; no flags).
- No slot opened today after the DK exit was refilled at the open; no new entries. HPE/STT (and other 15% stops) remain unattributed/Bull's — not touched.

## 2026-10-27 — midday (sonnet)
- All 8 satellites (CLDT, GTLB, KELYA, NEO, NSIT, QMCO, REPL, TXG) have live trailing stops; no stop fired. All green except none red (CLDT +0.8%, GTLB +0.6%).
- News check (8 searches, mostly stale/low-quality results): no thesis break found (no offering, going-concern, guide cut). QMCO shows only law-firm class-action alerts (rule 62, ads; CFO flag already known). NEO earnings 10/27-28 held under stop.
- No exits, no new entries. HPE/STT still UNATTRIBUTED at broker (both have stops); not touched.

## 2026-10-28 midday
- All 8 satellites (CLDT, GTLB, KELYA, NEO, NSIT, QMCO, REPL, TXG) have live 25% trailing stops; no stops fired, no exits, no new entries.
- News check (NEO, QMCO, REPL, TXG): nothing dated today, no dilution/going-concern/guide-cut found. GTLB, KELYA, CLDT, NSIT not searched (no trigger).
- ⚠️ HPE/STT still UNATTRIBUTED at broker; untouched.

## 2026-10-29 midday (sonnet)
- All 8 satellites (CLDT, GTLB, KELYA, NEO, NSIT, QMCO, REPL, TXG) held, each with a live 25% trailing stop. No stops fired, no exits, no new entries (no slot opened).
- News check on REPL, QMCO, TXG, NEO, GTLB: search results were stale (no dated 10/29 items) and showed no offering, going-concern, guidance cut or takeover. CLDT, KELYA, NSIT not searched this session. No thesis break found.
- Still UNATTRIBUTED at broker: HPE, STT (and other non-Rocket positions); not touched.

## 2026-10-30 — midday: no trades
- All 8 satellites (CLDT, GTLB, KELYA, NEO, NSIT, QMCO, REPL, TXG) held, each with a live 25% trailing stop. No stop fired, no slot opened, so no STEP 4 fill.
- News check on REPL/NEO/GTLB/QMCO: nothing dated today and no thesis break found; results were stale (searches returned 2025/early-2026 items). KELYA/NSIT/TXG/CLDT not searched (no catalyst flagged).
- HPE and STT still UNATTRIBUTED at broker (15% stops, not mine). Not touched.
