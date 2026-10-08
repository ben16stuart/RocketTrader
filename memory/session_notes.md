# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-10-08 — PREMARKET (Thursday, Week 41 day 4) — board EMPTY after widened search; no entry today

- **Satellite floor breached 13 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM 88.9% · cash 11.1% · slice $3,088.34 · shared cash $1,045.19.
- Funnel: calendar (14 rows) → Alpaca news tape (~200 headlines) → 2 scanners → 16 eligibility (16/16) → 7 survivors → **0 entries**.
- **ANGO CLOSED (5f):** beat, but FY27 guide affirmed (0% raise) + CEO change. **RGP CLOSED:** Q2 guide well below consensus, −13% AH.
- **WOLF OUT (13/49):** $1.5B *conditional* DoD loan, +17–27% AH, but ~$1.94B cap at the price paid → +15% breaches $2B.
- ELMT stays closed (PT raises ≠ upgrade; 42d). VSTM no dated cause (1). TRAX/OSUR/EVC no catalyst.
- Watch: **TLRY** BMO today → day-2 10/09 only on a beat + >1% FY raise on the 8-K + upper-half close. IRD/UNCY: no trigger.
- Macro: VIX 15.08 close / 15.72 LIVE; **RTY −0.84% LIVE**; Brent +4.3% (Iran-strike reports); 10Y 5.28%. Fed speakers 8:30–1:00.
- Cash 11.1% is 1.1 pts over the buffer with no bearish thesis — flag for the close sweep (rule 4/5), not a market call.
- No trades (market closed). No ntfy (no held satellites).

---

## 2026-10-07 — PREMARKET (Wednesday, Week 41 day 3) — board EMPTY after widened search; no entry today

- **Satellite floor breached 12 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM 89.8% · cash 10.2% · slice $3,118.41 · shared cash $1,048.98.
- Funnel: calendar (15 rows → 1 in universe, RGP AMC tonight) → Alpaca news tape (~50 headlines + premarket-movers list)
  → 3 web searches (FDA/initiations/movers: nothing dated) → 4 screeners → 21 settled bars → 7 eligibility (7/7) → **0 entries**.
- Real catalysts all **>$2B (13)**: NEOG beat+raise, PENG beat+guide, NLST patent deal. Escalation #4 is binding again.
- Scanner Change % wrong for every checked mover (17). Breakouts Finviz query empty (64, 7th session).
- ANGO −7.2%/1.6× closed at 13% of range into 10/08 BMO (distribution flag). BYRN dropped: median ADV 265k (46).
- Macro: VIX 15.01 close / 15.50 LIVE; RTY −0.48% LIVE; 10Y 5.27%; Brent 101.9. **FOMC minutes 2:00 PM ET today (29).**
- Ahead: ANGO 10/08 BMO (day-2 10/09), RGP 10/07 AMC (day-2 10/09), IRD trigger window to 10/13, UNCY NDA PR.
- No trades (market closed). No ntfy (no held satellites).

---

## 2026-10-06 — MARKET CLOSE (Tuesday, Week 41 day 2)

- **Satellite floor breached 12 sessions running** (0.0% of slice) — research gap, not a bearish call. Under rule 8 the next premarket's #1 job is widening the scan.
- Rocket holds IWM core only (10 sh, 89.8% of slice, cash 10.2%). Target core $2,813 vs actual $2,813: in band, **no rebalance needed**. No satellites, so no stop review.
- IWM today -0.75%; Rocket core -$20.80. Rocket vs IWM +6.61% since rebase. Only trade today was the Ben-ordered IWM buy (already logged). ntfy sent (confirmed).

## 2026-10-06 — PREMARKET (Tuesday, Week 41 day 2) — board EMPTY after widened search; no entry today

- **Satellite floor breached 11 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM 49.7% (at cap) · slice $3,122.03 · shared cash $1,870.56. Breach #11 = 10/05 close (fallback didn't log it).
- 10/05 fallback close: rebalance flagged "in band" (IWM $1,550 vs $1,558 target), so **no rebalance is owed**. RARE stop fill already logged at midday.
- Funnel: earnings calendar (14 rows → 0 tradeable; WS/SAR fail ADV) → FDA tape (nothing dated) → initiations (Benzinga 403,
  source down) → 4 screeners (~60 rows) → 11 eligibility (11/11) → settled bars → **1 real mover (CRVO) → 0 live**.
- **CRVO PASS:** +9.6% / 4.1× on 10/05 with no dated cause; $3.31 near the price floor, $50M on the cap floor; offering in recent news.
- Scanner Change % wrong for 8 of 9 checked names (17). Breakouts Finviz query empty again (64).
- IRD closed $4.38 (<$4.40 kill level) on 1.3×, under the 1.5× heavy bar → kill shape not met; one more such close on ≥1.5× kills it.
- Macro: VIX 15.52 close / 15.43 LIVE; RTY +0.05% LIVE; 10Y 5.31%; oil −1.8%. Not FOMC. **Binding: board quality.**
- Ahead: RGP 10/07 AMC (day-2 10/09), ANGO 10/08 BMO (day-2 10/09), BYRN 10/08; IRD run-up trigger; UNCY NDA PR.
- No trades (market closed). No ntfy (no held satellites).

---

## 2026-10-05 — MARKET_CLOSE — DID NOT RUN [automated fallback, no LLM]

The market_close routine produced no output: Claude session limit (resets 3pm (America/Denver)). It failed before doing any work: nothing was executed.
A no-LLM fallback (`scripts/degraded_close.py`) ran instead. It placed **no orders** and touched no file except this note and `portfolio_state.md`.

- **Done by the fallback:** portfolio snapshot synced, books reconciled, automated ntfy summary sent, memory commit and push attempted (the ntfy states the result).
- **NOT done today:** stop review, core rebalance, fill logging in `trade_log.md`, lessons, and tomorrow's research priorities. Broker-side stops were unaffected.
- Day (as of 13:58 MDT): +0.27% (+$8) vs IWM +0.54%. Satellites 0.0% (floor 50% 🚨 breached) | Core 49.7% | Cash 50.3% of slice.
- Books vs broker: ✅ Balanced.
- Orders today: none.
- Stops armed: none needed (no satellites).
- Rebalance drift, informational and NOT executed: IWM $1,550 vs target $1,558 -> in band. The core rebalance only runs at `market_close`, so it is still owed if outside the band.

---
## 2026-10-05 — MIDDAY (Monday, Week 41 day 1) — RARE STOPPED OUT (−4.4%); no new entry; satellites 0%

- **RARE** stop filled 10:26 ET @ $14.42 (stop $14.4336) → −$20.46 / −4.4% vs $15.08. Detected at midday via snapshot ("MISSING: RARE") + `/v2/orders` closed. RARE $14.57 at midday (above fill); no new negative news (only the old Pomerantz ad). Logged in trade_log. No ntfy (routine stop fill, not a forced cut).
- Scan (`unusual_volume`, 10:15 stamp): DNA +19.2% (already FAIL at open: no dated catalyst, ladder fails), MNTK +10.9% at $3.18 (floor trap, no catalyst), SDEV/XRPN/BEAG/PUSA crypto/SPAC/floor (31, 10), VELO/CWH/FDMT/PCT negative. Nothing clears rule 1. No entry.
- Satellites **0%** of slice, IWM ≈49.7%, cash above buffer ≈ $1,100+ with no bearish thesis: research gap, not a market call. 11th breach pending at close; rebalance/IWM check at close (rule 7). Binding constraint: board quality. Next catalysts: RGP 10/07, ANGO/BYRN 10/08.

---

## 2026-10-05 — MARKET_OPEN (Monday, Week 41 day 1) — no entry; RARE held; board still empty

- Open (13:45 UTC snapshot): RARE $14.96 LIVE vs 10/02 settled $15.22 (−1.7%), stop $14.4336 is 3.5% away → HOLD, 32a (no override >2% only applies when closer; not engaged). Floor 14.9% (breach #11 pending at close). IWM 49.4%.
- Scanner data stale (stamped 07:45, RARE RelVol 0.0x) → name source only (17). Unusual-volume list: crypto/SPAC/pinned (SDEV, XRPN, BEAG, USDE, GRML), VELO −18% (down), PUSA $3.11 (floor trap, no catalyst). Movers: only DNA +9.8%.
- **DNA FAIL (1):** one inline search — no dated catalyst; Q2 revenue −48%, TD Cowen Hold/PT $9, BTIG Sell/PT $5 (rule 11 ladder fails; analyst targets below price). "Curious rally" shape.
- FEAM 3.2× RelVol, −0.3% at $3.87 — plan closed premarket, stays closed (no resale filing seen).
- No trades. No ntfy. Binding constraint: board quality.

---

## 2026-10-05 — PREMARKET (Monday, Week 41 day 1) — board EMPTY after widened search; FEAM + TBCH closed; no entry today

- **Satellite floor breached 10 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 15.2% (RARE only) · IWM 49.6% (at cap) · slice $3,104.15 · shared cash $1,423.56.
- Funnel: earnings calendar (5 rows, 0 in universe) → FDA tape (nothing dated 10/02–10/04 in universe) → initiations
  (no 2026-dated small-cap results) → all 4 screeners → ~60 rows → 8 eligibility (8/8) → 7 in universe → **0 live**.
- **FEAM PASS:** the 9/15 8-K obliges registering the resale of 8.3M seller shares (37% of float) after the 10/01 close.
  Also a 270-day PIK bridge. 5-min stop fit: 37% of days >7% MDD. Closed unless the resale is filed and absorbed.
- **TBCH PASS:** the B. Riley "Buy/$21 Oct 2" item is from 2025 (dated at source). No 2026 catalyst.
- Scanner Change % is wrong again (PNNT/ESRT "+12–15%" had no settled move) (17).
- Held: RARE 10/02 settled $15.22, stop $14.4336 (re-read via `/v2/orders` at open). No news searched (no trigger).
- Macro: VIX 15.31 close / 16.30 LIVE; RTY −0.18% LIVE; 10Y 5.28%. ISM Services 10:00 ET; FOMC minutes this week. **Binding: board quality.**
- Rest of the week: RGP 10/07, ANGO 10/08 BMO (day-2 10/09), BYRN 10/08; IRD run-up trigger (exit by 10/15); UNCY NDA PR.
- No trades (market closed). No ntfy.

---

## 2026-10-03 — WEEKLY REVIEW (Week 40, Saturday) — Grade D+; floor 21.0% avg; W41 board built

- Book +0.27% vs IWM −0.16% (**+0.43%**, all RARE). AGEN 0/1 (−0.36R, clean entry, stop saved ~$57). Satellites avg **21.0%**, 5/5 closes below floor, all logged; rule 8 acted on (sources widened, MEDIUM bar used).
- Gate counterfactual: all 7 W40 shape kills would have lost by 10/02 → filters are not the leak; floor arithmetic escalation re-raised with two weeks' evidence.
- W41 board: **FEAM day-2 Mon 10/05** (MEDIUM, conditional: read 9/15 8-K + 5-min MDD first; $3.88–$4.27, dead < $3.585). ANGO 10/08 BMO; RGP 10/07 / BYRN 10/08 watch; IRD/UNCY conditional; TBCH unverified. NNBR, NEOV, HELE FAIL.
- Strategy: clinical-data readouts split from approvals (0/4); MEDIUM-bar dilution tiebreaker. Files trimmed (session notes archived through 9/30; research_log 83 lines; lessons 63 lines — 3 over, all standing rules).

---

## 2026-10-02 — MARKET_CLOSE (Friday, Week 40 day 5) — RARE HELD, IWM IN BAND, NO TRADES

- RARE $15.24 (+1.0% vs entry, +3.3% today), live stop $14.4336 (HWM $15.52, 5.3% clear, verified via `/v2/orders`). HOLD under 32a. IWM raw 5.4746 sh = $1,540.96 vs target $1,554.54 (slice $3,109.07, sat $472.44) → short 0.44% of slice, inside the 3% band, no trade.
- Satellites 15.2%, **10th consecutive breach**, research gap not a bearish call. ~$1,096 (35% of slice) is cash above the buffer with no bearish thesis, flagged not hidden. IWM at the 50% cap so it cannot fill the gap.
- Book +$28.53 today (+0.92% of slice) vs IWM +0.88%. ntfy sent (confirmed). Week-40 count 1/5. No fills today.
- Next premarket (W41): still #1 job is the satellite gap. Plans IRD (PDUFA 10/17 run-up, exit by 10/15). Still owed: W36–W40 weekly reviews, floor-arithmetic escalation.

---

## 2026-10-02 — MIDDAY (Friday, Week 40 day 5) — RARE HELD (+0.4% vs entry); no new entry; NNBR/AZTA PASS

- **RARE** $15.14 (+0.4% vs $15.08 entry, +2.6% vs $14.75 close), stop $14.4336 (HWM $15.52, 7%) = 4.7% clear, confirmed via `/v2/orders`. No cut or tighten trigger. News: EMA validated the UX111 MAA (10/2, positive, not a new catalyst); no negative news. HOLD.
- Scan (`unusual_volume`): **NNBR** (+14.7%, 4.9x) firearm-components contract manufacturing, undisclosed terms (49), same-day (2), and the search price ($3.52) conflicts with the scanner ($4.16) (17). **AZTA** (+13.1%) search result is a misdated earnings piece (33), and the +25% target (~$48.75) breaches the $2B cap (13). FEAM carried from open (PASS), SDEV (31), TH/THRM/IART/NKTR negative. Nothing clears rule 1.
- Satellites 15.1% of slice (RARE only), IWM 49.6%. 10th breach pending at close. Research gap, not a bearish call. Rebalance decision at close. Weekly count 1/5. No trades, no ntfy.

---

## 2026-10-02 — MARKET_OPEN (Friday, Week 40 day 5) — no entry; FEAM new name, PASS

- Snapshot 9:45 ET: slice $3,112.49, shared cash $1,423.56, satellites 14.8% (RARE only), IWM at cap. RARE stop order live (ca4a062c…). No overnight fills or stops.
- Scanned unusual_volume + top_movers. Only new in-universe name: **FEAM** ($3.56, +10% vs prior settled close ~$3.23, 0.7× avg vol at 9:45, cap $148M, +128% 1-month). Catalyst = Searles Valley acquisition CLOSED 10/2 (known deal; prior "$9.6M acquisition" sold off). PASS: same-day (rule 2), volume unconfirmed, extended, dilution/domicile unread (8, 52c). Not a W41 plan unless a day-2 base forms with dilution cleared.
- BETR +15% / 4.7× already PASS (1) at premarket; TH/THRM/LIME/QMCO negative; rest crypto/funds (31).
- Binding constraint: board quality (no dated catalyst with a live shape). Floor breach continues (10th at close unless changed) — research gap, not a bearish call.
- No trades, no ntfy.

---

## 2026-10-02 — PREMARKET (Friday, Week 40 day 5) — board EMPTY after widened search; no entry today; W41 plans IRD/UNCY

- **Satellite floor breached 9 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 14.8% (RARE only) · IWM 49.5% (at cap) · slice $3,096.55 · shared cash $1,423.56.
- Funnel: earnings calendar (19 rows, 0 in universe) → FDA/PDUFA tape → 10/01 initiations → all 4 screeners →
  PM movers. ~65 scanner rows → 9 eligibility (9/9) → 5 in universe → **0 live**. **Binding: price action (42d/4).**
- UNCY (NDA resubmitted 9/29) closed 10/01 at 2% of range on 1.5× → dead. LBRX (Needham init) 11%/1.0× → no
  reaction. IRD (PDUFA 10/17) closed at the lows 2 days → W41 run-up plan only, exit by 10/15 (29).
- ACHV (~$7.53 < $7.87 kill) and GLUE (sold the news) DEAD. RCKT fails price ($2.59) → dropped. SLS fails cap.
- Held: RARE 10/01 ~$14.77, stop $14.4336 (from `/v2/orders` on 10/01; re-read at open). No news searched today.
- Macro: VIX 16.00 LIVE, RTY +0.50% LIVE, 10Y 5.24%. **Payrolls 8:30 ET** (cons. +90k).
- No trades (market closed). No ntfy (no breaking news on held names).
- Still owed: the W36–W40 weekly reviews; the floor-arithmetic escalation (W39 §6).

---

## 2026-10-01 — MARKET_CLOSE (Thursday, Week 40 day 4) — RARE HELD, IWM IN BAND, NO TRADES

- RARE $14.78 (−2.0% vs entry, −1.66% today), live stop $14.4336 (2.4% clear). HOLD under 32a. IWM 5.4746 sh $1,527 vs target $1,543 (−0.5% of slice), in band, no trade.
- Satellites 14.8%, 9th consecutive breach, research gap not a bearish call. Book −0.06% vs IWM +0.39%. ntfy sent (confirmed). Week-40 count 1/5.
- Slip: ntfy quoted RARE stop as ~$14.06 (stale 9/25 value) instead of $14.4336 — verify stop via /v2/orders before writing it.
- Next premarket: still the #1 job is widening the scan for satellites; W36–W40 reviews still owed.

## 2026-10-01 — MIDDAY (Thursday, Week 40 day 4) — AGEN STOPPED OUT (−2.5%); RARE held; no new entries

- **AGEN** trailing stop filled 47 sh @ $9.56 at 9:49 ET (stop $9.5883, HWM $10.31), −$11.75. Snapshot flagged it MISSING; logged in trade_log. Live $9.03 (−9.1% vs $9.93 close) — stop saved ~$25. A web search showed $9.94 (stale); `market_data.py price` confirmed $9.03 (rule 17).
- **RARE** $14.88 (−1.3% vs entry, −1.0% vs $15.03 close), stop $14.4336 = 3.0% clear. No −5% cut trigger. News: only a Pomerantz alert (ad, rule 62) and the old Angelman failure. HOLD (32a).
- Scan (`unusual_volume`): SDEV (31), INSG (ADV), NKTR −21.8%, TDAY (no catalyst), GLAS/PUSA wrong direction, rest SPAC/closed-end funds. Nothing clears rule 1. No new entry.
- Satellites ≈15% of slice (RARE only), IWM 49.4%, cash above buffer. Research gap, not a bearish call. Rebalance decision at close. Weekly count 1/5. No ntfy (stop fill is routine, not a forced cut).

---

## 2026-10-01 — MARKET_OPEN (Thursday, Week 40 day 4) — NO TRADE; ACHV failed shape (b), GLUE sold the news

- Snapshot 13:45 UTC (9:45 ET). Slice $3,086.98, pooled cash $974.26. Satellites 30.0% (floor breached, 9th session pending close). No stops hit; AGEN $9.71 (-2.2% vs $9.93 close, stop $9.5883), RARE $15.11 (+0.5% vs $15.03, stop $14.4336). HOLD both (32a).
- **ACHV** (prior settled close $8.09): 9:30-9:45 bars $7.90-$7.97, closed $7.94 on ~1k shares (IEX), detail -1.6% / 0.1x. Fails pre-committed (b): can't hold the 9/30 close. Low $7.90 still above the $7.87 kill, but no entry. Re-grade at close; not carried as a maybe.
- **GLUE** (prior settled close $11.93): premarket +21.5% faded to $11.55 (-3.2%) by 9:45, after opening $12.04. Sell-the-news shape, the pre-committed kill. 10/02 plan DEAD unless 10/01 close reverses on heavy volume (unlikely).
- Fresh movers: TDAY (+11.9% scanner, search shows +2.9% to $7.04 - the scanner field conflicts, rule 17) and EFOR (+10.1% scanner, search +1.05%) - no dated catalyst found. PASS (1). SDEV stablecoin (31). INSG ADV fail (46). NKTR/ORN no catalyst checked.
- Funnel: 2 planned + ~20 scanner rows -> 0 entries. Binding: board quality (53a) + price action (42d).
- Trades 0. No ntfy (no trades, no stops).

---

## 2026-10-01 — PREMARKET (Thursday, Week 40 day 4) — board: ACHV (MEDIUM, conditional day-2 entry today) + GLUE (day-2 plan 10/02); CAPR/VNDA/QTTB dead

- **Satellite floor breached 8 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 30.0% (RARE + AGEN) · IWM 49.2% (at cap) · slice $3,091.06 · shared cash $974.26 · book cash ≈$517.
- **All 3 pre-committed 10/01 plans died on the 9/30 close (rule 4):** CAPR 5% of range on 7.6×, VNDA 3% on
  4.1×, QTTB 16% on 8.8×. Gate 42 kept three distribution days out of the book.
- Funnel: calendar (thin; PRGS/HUBG ceiling-bound) → FDA/clinical → 9/30 initiations → all 4 screeners →
  EDGAR. ~30 names → 13 eligibility (13/13 rows) → 9 in universe → 2 live → 1 enterable today.
  **Binding: board quality (53a).**
- **ACHV**: Stifel Buy/$18 (9/30). Day 1 +5.2%, 54% of range, 1.6× (weak). Short 15.6%, raise done 8/14,
  cash $187M, stop fits. Enter only if 2a ✓ and the 9:45–9:50 bar closes upper half AND ≥ $8.09, ≤ $8.90;
  dead below $7.87. 57 sh at cap.
- **GLUE**: GFORCE-1 data 8:00 AM today, premarket +21.5% vs $11.93. Day 1 + stop fit fails → 10/02 plan:
  issuer numbers + upper-half close on ≥2× median + no offering (S-3ASR auto-shelf live).
- PASS/FAIL: KURA (JPM init, no reaction), SRRK/TWST (cap), CVEO/INSG (ADV), SPIR/TARA/XRX/OSUR/DBI/FTK (no dated catalyst).
- Held: AGEN close $9.93, stop $9.5883 (HWM $10.31); RARE close $15.03, stop $14.4336 (HWM $15.52). No news.
- Macro: VIX 16.34, RTY −0.17% LIVE, 10Y 5.29% (bond rout). Claims 8:30, ISM 10:00, heavy Fedspeak.
- No trades (market closed). No ntfy (no breaking news on held names).

---

## Session Archives

- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026

## 2026-10-06 — MIDDAY (Tuesday, Week 41 day 2) — no satellites, no action

- Book: IWM core only (≈9.98 sh after this morning's 10:23 ET buy; snapshot display shows stale 10 sh/rounded). SPY 9 sh is Bull's. No satellite positions → nothing to cut/tighten, no holdings news check needed.
- Scanner (name source only, rule 17): ITG +19.3% (same-day gap, rule 2: day-2 only), BRUN +9.1%, CGEM +7.6%, PRME +9.3% (closed on Gate A 9/25). No dated catalyst verified for any; no entry. Others were big decliners (AVBP −49%, XRPN −52%, DNA −17%).
- Satellite floor still breached (0%); breach is a research gap. ITG/BRUN are candidates for tomorrow's premarket catalyst check if a dated catalyst exists.

## 2026-10-07 — MIDDAY (Wednesday, Week 41 day 3) — no satellites, no action

- Book: IWM core only (~9.98 sh). The snapshot's AMD/BNY/DELL/NUE/SPY rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): XRPN +25% (SPAC, Armada Acquisition II; no operating catalyst), PRME +9.1% (closed on Gate A 9/25), AVBP/CBIO/ACRS/DNA/PRG/BETR/MNTS/EARN have no dated catalyst checked. No entry. No searches run, to save tokens.
- Satellite floor still 0% vs 50%. Breach is a research gap, not a bearish call. Idle money is in IWM. No trades, no ntfy.

## 2026-10-07 — MARKET CLOSE (Wednesday, Week 41 day 3)
- Satellite floor breached 13 sessions running (0.0%) — research gap; rule 8 escalation binding tomorrow.
- IWM core only (10 sh, 89.1%, cash 10.9%). Target core ~$2,797 vs $2,777: in band, no rebalance. IWM -1.31%; core -$36.76. Rocket vs IWM +7.29%. No trades. ntfy sent.

## 2026-10-08 — MIDDAY (Thursday, Week 41 day 4) — no satellites, no action

- Book: IWM core only. AMD/BNY/DELL/NUE/SPY rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): PCRX +44% on 77.8× ($1.45B cap, in universe by size). One search found no dated catalyst for today's move (only old patent-settlement stories). Same-day >35% is day-2 only (rule 2c), and a catalyst can't be confirmed from a search result (57). No entry. Candidate for 10/09 premarket: find the 8-K/PR first. BYRN +9.9% and HNRG +11% have no dated catalyst checked. ANGO −21% and the rest are decliners.
- Satellite floor still 0% vs 50%, a research gap and not a bearish call. Idle money is in IWM. No trades, no ntfy.
