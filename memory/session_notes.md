# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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
