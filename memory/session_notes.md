# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-10-16 — PREMARKET (Friday, Week 42 day 5) — RAPP #1 / EIKN #2, both MEDIUM tape-confirmed

- **Satellite floor breached 19 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM ~90.5% · cash ~9.5% · slice $3,039.26 · shared cash $994.89.
- Handed-off check: the 10/15 close **did** grade HAWK ($12.82 < $12.99 → CLOSED). VSTM's 10/15 reclaim to $9.20 doesn't reopen it (42d).
- Funnel: Alpaca tape (234) → 4 scanners (stale) → 15 eligibility (15/15) → 9 in universe → **2 candidates**. Binding constraint (53): board quality.
- **RAPP (MEDIUM):** the 3rd independent initiation in 10 days (UBS Buy $71, 10/15 AMC; Wolfe, Guggenheim). Entry: the 9:45–9:50 bar upper half and >$30.39 at ≥1.5× pace, no-chase above $31.50.
  14 sh, stop $28.37. Quote vs the $29.45 settled close.
- **EIKN (MEDIUM):** HCW Buy $23 (10/16) + IND submission (10/15); two upper-half closes into the note. Entry: >$7.63 with an upper-half 9:45 bar. 59 sh, stop $7.16.
  **The IPO lock-up date must be verified before entry** (~early Nov expiry inferred from the 13G dates).
- Passes: SLDB (unexplained −13% on 10/13), WVE (near the $3 floor), SRTA (activist stake, not a catalyst).
- **market_open owes:** run both triggers and do the CORE FUNDING IWM sale right before any BUY. **market_close owes:** grade both 10/16 closes against the day-2 fallback bars.
- Macro: VIX 16.46 close / 16.18 LIVE; RTY +0.28% LIVE; 10Y 5.09% (−10bp); IWM +1.37% on 10/15. No 8:30 data. Monthly opex.
- No trades (market closed). No ntfy (no held satellites).

---

## 2026-10-16 MARKET_OPEN (9:45 ET) — 0 entries
- RAPP opened/trading $28.29 (−4.3% vs 10/15 settled $29.45, 0.2× pace): the third note is being ignored → plan's no-entry/kill shape fired. CLOSED (day-2 fallback needs a 10/16 close ≥ $30.39, unlikely).
- EIKN $7.52 (−0.3% vs $7.54 settled), 0.2× pace → flat open, no entry per plan. Lock-up question moot. CLOSED.
- Fresh scan: SITC (liquidation, already out), FOXF/OMER/EBS decliners, SRTA (activist 13D, passed). Nothing with a dated catalyst + volume. Binding constraint: board quality. Floor still breached (20th close pending). No trades, no IWM sale.

---

## 2026-10-16 — MIDDAY (Friday, Week 42 day 5) — no satellites, no action
- Book: IWM core only (10 sh, no stop). Other snapshot rows are Bull's. Nothing to cut or tighten; no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): SITC liquidation (already out), FOXF -10.5% / CCOI -7.5% decliners, FMC +4.0% no catalyst checked, rest funds. No fresh dated-catalyst mover. No searches, no entry.
- Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

---

## 2026-10-16 — MARKET_CLOSE (Friday, Week 42 day 5)
- Satellites 0.0% (20th breach). IWM core 90.3%, within band, no rebalance. No trades. Rocket -1.54% vs IWM -1.70% today; own book -6.43% vs IWM -7.50% since 7/20 (+1.07 pts). ntfy sent.
- Next premarket: rule-8 widened scan, MEDIUM bar OK; catalyst still required.

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
