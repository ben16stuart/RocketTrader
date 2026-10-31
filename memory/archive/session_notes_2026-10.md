# Session Notes Archive — October 2026

<!-- archived at W41 weekly review 2026-10-10 -->
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

## 2026-10-06 — MIDDAY (Tuesday, Week 41 day 2) — no satellites, no action

- Book: IWM core only (≈9.98 sh after this morning's 10:23 ET buy; snapshot display shows stale 10 sh/rounded). SPY 9 sh is Bull's. No satellite positions → nothing to cut/tighten, no holdings news check needed.
- Scanner (name source only, rule 17): ITG +19.3% (same-day gap, rule 2: day-2 only), BRUN +9.1%, CGEM +7.6%, PRME +9.3% (closed on Gate A 9/25). No dated catalyst verified for any; no entry. Others were big decliners (AVBP −49%, XRPN −52%, DNA −17%).
- Satellite floor still breached (0%); breach is a research gap. ITG/BRUN are candidates for tomorrow's premarket catalyst check if a dated catalyst exists.

## 2026-10-07 — MIDDAY (Wednesday, Week 41 day 3) — no satellites, no action

- Book: IWM core only (~9.98 sh). The snapshot's AMD/BNY/DELL/NUE/SPY rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): XRPN +25% (SPAC, Armada Acquisition II; no operating catalyst), PRME +9.1% (closed on Gate A 9/25), AVBP/CBIO/ACRS/DNA/PRG/BETR/MNTS/EARN have no dated catalyst checked. No entry. No searches run, to save tokens.
- Satellite floor still 0% vs 50%. Breach is a research gap, not a bearish call. Idle money is in IWM. No trades, no ntfy.



---

# Archived 2026-10-17 (W42 weekly review): 10/07 – 10/15

## 2026-10-07 — MARKET CLOSE (Wednesday, Week 41 day 3)
- Satellite floor breached 13 sessions running (0.0%) — research gap; rule 8 escalation binding tomorrow.
- IWM core only (10 sh, 89.1%, cash 10.9%). Target core ~$2,797 vs $2,777: in band, no rebalance. IWM -1.31%; core -$36.76. Rocket vs IWM +7.29%. No trades. ntfy sent.

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

## 2026-10-08 — MIDDAY (Thursday, Week 41 day 4) — no satellites, no action

- Book: IWM core only. AMD/BNY/DELL/NUE/SPY rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): PCRX +44% on 77.8× ($1.45B cap, in universe by size). One search found no dated catalyst for today's move (only old patent-settlement stories). Same-day >35% is day-2 only (rule 2c), and a catalyst can't be confirmed from a search result (57). No entry. Candidate for 10/09 premarket: find the 8-K/PR first. BYRN +9.9% and HNRG +11% have no dated catalyst checked. ANGO −21% and the rest are decliners.
- Satellite floor still 0% vs 50%, a research gap and not a bearish call. Idle money is in IWM. No trades, no ntfy.

## 2026-10-08 — MARKET_CLOSE (Thursday, Week 41 day 4) — no session note written [backfilled at W41 review]

- The routine ran (log: no trades, IWM in band, breach #14 logged in lessons, ntfy sent). No session note was written.

## 2026-10-09 — PREMARKET (Friday, Week 41 day 5) — board EMPTY after widened search; KOPN conditional for 10/12

- **Satellite floor breached 14 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM ~89.5% · cash ~10.5% · slice $3,109.14 · shared cash $1,045.19.
- Funnel: calendar (14 rows) → Alpaca news tape (275 headlines + premarket movers) → 3 web searches → 2 scanners →
  26 settled bars → 7 eligibility (7/7) → 4 survivors (ALMS, ACRS, KOPN, TRIN) → **0 entries**.
- **PCRX CLOSED:** +44% was a $36.50 cash takeover (pinned, 27). **TLRY CLOSED:** beat on EPS, sales miss, no raise.
- ALMS pass (data presentation, 0/4 category; reopen on NDA-submission PR). ACRS pass (bounce, no cause). PKE beat but ADV 268k.
- **KOPN conditional (MEDIUM):** +$18.6M Army IBAS award PR 10/08 AMC. Day-2 Mon 10/12 only if 10/09 closes upper half
  on ≥1.5× and >$4.19; read the shelf for an ATM first. Kill on a lower-half close or <$4.00.
- IRD no trigger ($4.45). UNCY sliding (14% of range, 1.4×) → one more ≥1.5× low close kills it.
- Macro: VIX 15.41 close / 15.21 LIVE; RTY +0.35% LIVE; 10Y 5.23% (off highs); Brent 104.28 close, −1.2% LIVE.
  No major data found for today (thin source). Hurricane Isaias (Cat 2, Gulf) = energy/airline headline risk.
- Cash ~10.5% is ~0.5 pts over the buffer with no bearish thesis → sweep to IWM at the close (rule 4/5).
- No trades (market closed). No ntfy (no held satellites).

## 2026-10-09 — MIDDAY (Friday, Week 41 day 5) — no satellites, no action

- Book: IWM core only. Other snapshot rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): PCRX flat (-0.2%, no day-2 follow-through on the 10/08 +44%), CABO -34%, ALHC -15%, DNA +12.8% and PRME +12.1% (no dated catalyst checked; PRME closed on Gate A 9/25). No entry. No searches run.
- KOPN day-2 plan is a close check only (upper half on ≥1.5× median, above $4.19), handled at market_close. Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

## 2026-10-09 — MARKET_CLOSE (Friday, Week 41 day 5) — no session note written [backfilled at W41 review]

- The routine ran (log: IWM in band, breach #15 logged in lessons, ntfy sent) but did not write this entry, and it **did not run the KOPN close check** it had been handed. Backfilled: KOPN 10/09 closed $4.47 at **37% of range** (lower half) → the pre-committed kill fired → **CLOSED** for 10/12.

## 2026-10-10 — WEEKLY REVIEW (Week 41, Saturday) — Grade D−; satellites 0.0% avg; W42 board built

- Book **−$54.40 / −1.83%** vs IWM −0.92% (281.52 → 278.94) = **−0.91%**. All of it came from RARE (stopped $14.42 on 10/05, then closed $15.49 on 10/09) plus a little idle-cash drag. No new entries; 0/1 closed (RARE −0.63R).
- Satellites **0.0% at all 5 closes** (breaches #11–#15). Rule 8 was acted on in the search (the Alpaca news tape was added as a source; KOPN was boarded at the MEDIUM bar) but produced **0 entries**.
- Gate counterfactual: all 9 graded W41 in-universe kills or passes were flat-to-down by 10/09 (best +2.7%) (ANGO −26%, RGP −25%, FEAM −7%). The filters are not the leak. Catalyst supply inside $50M–$2B is.
- **Reporting error:** every daily ntfy said "Rocket vs IWM +6.6–7.3%". That snapshot figure is 30% of the *shared* account, so Bull's gains are in it. Hand-built: **+0.93%** since rebase (−3.65% vs −4.57%). Escalated.
- Process slips: the 10/08 and 10/09 market_close wrote no session note. The 10/09 close skipped the KOPN close check (done here: **kill fired**, 37% of range). The 10/06 breach was never put in lessons.
- **W42:** KOPN CLOSED. IRD run-up plan, **exit moved up to the 10/14 close** (PDUFA 10/17 is a Saturday, so the FDA can act on Fri 10/16 or earlier). UNCY/ALMS conditional. SVC/KLRA unverified (premarket must read the filing first). The earnings calendar is thin (regional banks) and must be re-pulled daily.

## 2026-10-12 — PREMARKET (Monday, Week 42 day 1, Columbus Day) — no entry today; TRAX conditional for 10/13

- **Satellite floor breached 15 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM ~89.5% · cash ~10.5% · slice $3,107.30 · shared cash $1,045.19.
- Funnel: calendar (0 in-universe BMO) → Alpaca tape (275) → 3 searches → all 4 scanners → 15 eligibility (15/15) →
  13 in universe → **0 entries today**. **Binding constraint (53): board quality.** No in-universe earnings before the 10/13 banks.
- **TRAX (MEDIUM, conditional for 10/13):** Phase 1b ANB033 celiac topline due today. Binary event, so no entry today (29). Day-2
  only on a primary-endpoint hit read on the PR, an upper-half close on ≥1.5×, and no AH offering. Clinical day-2 plans are 0/4.
- HUBG CLOSED (upgrade PT under +15%, delinquent filer, distribution). SVC LOW (non-binding TKO proposal for an asset, no 8-K yet).
  QNRX/ASBH fail the gates. IRD/UNCY no trigger. IRD exit-by-10/14 plan unchanged.
- Macro: VIX 14.84 close 10/09 / 15.47 LIVE; RTY +0.04% LIVE; 10Y 5.24%; Brent 104.72 close, +0.8% LIVE. Bond market closed
  (Columbus Day), so volume is thin. CPI/inflation data is due this week (date not confirmed).
- No trades (market closed). No ntfy (no held satellites).

## 2026-10-12 market_open — no trade
- Snapshot: satellites 0.0% (breach, no new data point beyond premarket); book = IWM core only; no stops hit, no overnight fills.
- TRAX: $37.72 / +18.4% vs 10/09 settled $31.85 (70), 1.9× avg early, cap $1.35B. Same-day entry barred (rule 2 day-2, rule 29). Day-2 plan for 10/13 unchanged: needs primary-endpoint hit on the PR/8-K, upper-half close ≥1.5× median, no AH offering.
- Fresh scan (unusual_volume/top_movers): CTNM −19.5% on 43× (decline, no entry); GRML pump (standing kill); rest fails or no catalyst. Funnel: 2 scanners → 0 qualifying → 0 entries. No CORE FUNDING sale made.

## 2026-10-12 — MIDDAY (Monday, Week 42 day 1) — no satellites, no action
- Book: IWM core only; other snapshot rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): TRAX +6.8% on 15.2× at $34.01 (faded from +18.4% at the open; same-day entry still barred, day-2 plan for 10/13 unchanged — a fade from the open is a point against the upper-half-close condition). CTNM −28%, SRZN −22%, SVC −15% are decliners. Rest are funds/no catalyst. No searches, no entry.
- Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

## 2026-10-12 — MARKET_CLOSE (Monday, Week 42 day 1)
- Satellites 0.0% (breach, escalated). IWM core 89.6%, within band, no rebalance. No trades. IWM -0.38%; Rocket +2.06% vs IWM -4.69% since rebase (+6.75%).
- 10/13 premarket: rule-8 gap closing; TRAX day-2 plan (primary-endpoint on PR/8-K, upper-half close, no AH offering — note it faded from +18.4% to +6.8%).

## 2026-10-13 — PREMARKET (Tuesday, Week 42 day 2) — no entry today; OIG conditional for 10/14

- **Satellite floor breached 16 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM ~89.6% · cash ~10.4% · slice $3,097.28 · shared cash $1,042.66.
- The 10/12 market_close wrote **no session note** (breach line in lessons only). Second skip in four closes (47c).
- Handed-off checks done first: **TRAX killed** (10/12 closed at 14% of range on 11.2×, rule 4). **IRD CLOSED** (no trigger,
  window exhausted). **SVC CLOSED** (12% of range on 5×). UNCY no trigger. ALMS parked.
- Funnel: calendar (1 in universe, UNTY ADV 59k) → Alpaca tape (261) → 4 scanners (stale) → 10 eligibility (10/10) →
  2 in universe → **0 entries**. **Binding constraint (53): board quality.**
- **OIG (MEDIUM, conditional for 10/14):** Goldman Buy $13 initiation. This is the underwriter quiet-period wave on a busted IPO
  ($12 → $8.95). Day-2 only on an upper-half 10/13 close on ≥1.5× (~960k) and ≥$9.20. **market_close: grade the OIG 10/13 bar
  and write the result here (handed-off check).**
- Macro: VIX 15.21 close / 15.28 LIVE; RTY +0.47% LIVE; 10Y 5.24%; Brent 106.65 close, −2.1% LIVE. **CPI Wed 10/14 8:30 ET.**
- No trades (market closed). No ntfy (no held satellites).

## 2026-10-13 — MIDDAY (Tuesday, Week 42 day 2) — no satellites, no action
- Book: IWM core only (10 sh, -5.0% vs Bull-shared entry basis; core has no stop). Other snapshot rows are Bull's. No satellites, so nothing to cut or tighten and no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): BMBL +56.3% on 59.7x at $5.94 ($784M cap). Same-day >35% is day-2 only (rule 2c); catalyst not yet confirmed from a primary source (57). Candidate for 10/14 premarket: find the 8-K/PR first. ZURA +2.2% on 21.7x, no catalyst checked. FUN/SNDX/GLAS/CEPL are decliners. Rest are funds/no catalyst. No searches, no entry.
- Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

## 2026-10-13 — MARKET_CLOSE (Tuesday) — no trades; floor breached 17th session

- Satellites 0.0% · IWM 89.7% ($2,761 vs target ~$2,771, inside 3% band, no rebalance) · cash 10.3%. Rocket +1.57% vs IWM -5.08% since rebase.
- **OIG graded: FAILED** the 10/13 bar. Last $9.13 < $9.20 floor. Day-2 entry off for 10/14 unless it re-qualifies.
- IWM today -0.41%. CPI Wed 10/14 8:30 ET. Premarket: widen scan per rule 8.

## 2026-10-14 — PREMARKET (Wednesday, Week 42 day 3) — CODI MEDIUM tape-confirmed candidate; VSTM/OIG conditional for 10/15

- **Satellite floor breached 17 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM 90.0% · cash ~10% · slice $3,077.08 · shared cash $1,311.02.
- Handed-off checks: OIG failed the 10/13 bar (done at the close) and re-qualifies only on a 10/14 close. BMBL (midday flag) → $6.05 cash deal, **CLOSED**.
- Funnel: Alpaca tape (869) → 2 scanners (stale) → 16 eligibility (16/16) → 10 in universe → **1 candidate (CODI)**. Binding constraint (53): board quality.
- **CODI (MEDIUM):** Ladenburg Buy, $17 PT, 10/13 AMC. Entry only on a break of $11.20 with an upper-half 9:45–9:50 bar and ≥1.5× volume pace.
  40 sh, stop $10.51, CORE FUNDING sale first. Risk: lender restrictions from Lugano.
- **market_close owes:** the VSTM 10/14 close check (≥$8.00, upper half, ≥1.5×) and the OIG re-qualify check (≥$9.20, upper half, ≥1.5×).
- Macro: VIX 15.27 close / 15.25 LIVE; RTY +0.30% LIVE; 10Y 5.22%; Brent 105.69 close. **CPI 8:30 ET.**
- No trades (market closed). No ntfy (no held satellites).

## 2026-10-14 MARKET_OPEN (Sonnet) — 0 entries
- CODI (Ladenburg initiation) at 9:45 ET: $10.95, −0.8% vs $11.05 settled close (rule 70), vol 9k, below MA20/MA50. Plan said no entry if open flat/red → **NO ENTRY**. Not a kill; initiation was a weak form anyway.
- Scanners stale (07:45 timestamps, rule 17); movers are GLND/GRML (pumps, out), AADX ($1.95B cap, +25% > $2B, rule 13). No fresh catalyst-backed mover.
- Conditionals VSTM / OIG remain owed a 10/14 close check at market_close. Satellite floor still 0% (breach continues; binding constraint = board quality).

## 2026-10-14 — MIDDAY (Wednesday, Week 42 day 3) — no satellites, no action
- Book: IWM core only (10 sh, no stop). Other snapshot rows are Bull's (AMD/DELL −10%+ are Bull's). Nothing to cut or tighten; no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): VSTM +11.3% on 22.7× at $8.28 (above the $8.00 offering price; conditional for 10/15 still needs an upper-half close ≥1.5× median — graded at market_close). GLND/GRML pumps (out). BMBL flat (−0.2%) after yesterday's +56%, no day-2 follow-through. Rest decliners/no catalyst. No searches, no entry.
- Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

## 2026-10-15 — PREMARKET (Thursday, Week 42 day 4) — HAWK MEDIUM candidate (tape-confirmed today / day-2 Fri)

- **Satellite floor breached 18 sessions running — searched at MEDIUM-conviction bar per rule 8.**
  Satellites 0.0% · IWM ~89.6% · cash ~10.4% · slice $3,023.40 · shared cash $1,016.95.
- **The 10/14 market_close skipped its handed-off checks again** (47c; it logged only the breach line). Done here first: **VSTM CLOSED** ($7.71 < $8.00, the kill fired),
  **OIG CLOSED** ($9.05 < $9.20, second fail), **CODI CLOSED** (10/14 closed 9% of range, initiation sold).
- Funnel: Alpaca tape (223) + Nasdaq calendar → 2 scanners (stale, 17) → 12 eligibility (12/12) → 9 in universe → **1 candidate (HAWK)**. Binding constraint (53): board quality.
- **HAWK (MEDIUM):** Piper Overweight $22 initiation, independent of the IPO syndicate, at $12.38 (a busted IPO, −64%). The tape-confirmed entry needs the 9:45–9:50 bar upper half and >$12.99 at ≥1.5× pace.
  Fallback: day-2 on 10/16 if 10/15 closes ≥$12.99 in the upper half. 34 sh, stop $12.14, CORE FUNDING first. Risk: space sector (RKLB −10% PM), post-lock-up insider supply.
- **market_close owes:** grade HAWK's 10/15 close against the day-2 bar and write the result in this file.
- Macro: VIX 16.87 close / 17.60 LIVE; RTY +0.28% LIVE, NQ −1.10%; 10Y 5.19%; IWM −1.93% on 10/14. PPI/retail sales/claims/Philly Fed at 8:30 ET. Hammack 16:30, Warsh 23:30.
- No trades (market closed). No ntfy (no held satellites).

## 2026-10-15 market_open (Rocket) — 0 entries
HAWK: at ~9:45 ET $12.36 (−0.2% vs $12.38 settled 10/14 close, rule 70), 99k vol (0.1× avg). Plan said no entry if open is flat/red (note being ignored) → PASS; fallback is day-2 Fri 10/16 only on a 10/15 close ≥ $12.99, upper half, ≥1.5× median. Scanners stale (07:45, rule 17); no fresh in-universe mover with a dated catalyst (BETR/DFH/BRBR no catalyst checked → out). No IWM funding sale, no orders. Floor still 0.0% (19th breach at close). Binding constraint: board quality.

## 2026-10-15 — MIDDAY (Thursday, Week 42 day 4) — no satellites, no action
- Book: IWM core only (10 sh, no stop). Other snapshot rows are Bull's. Nothing to cut or tighten; no holdings news check.
- Scanner `unusual_volume` (name source only, rule 17): VSTM +10.6% on 3.9× at $8.53 (conditional graded at market_close: upper-half close ≥1.5× median). DFH +14.1% on 5.3× at $8.47 ($766M cap), no catalyst checked. FMC −31.9% decliner. Rest funds/no catalyst. No searches, no entry.
- Floor still 0% vs 50%, a research gap and not a bearish call. No trades, no ntfy.

## 2026-10-15 — MARKET_CLOSE (Thursday, Week 42 day 4)
- Satellites 0.0% (19th breach). IWM core 90.6%, within band, no rebalance. No trades. IWM +1.39% today; Rocket own book -4.94% vs IWM -5.88% since 7/20 (+0.93 pts).
- HAWK closed $12.82 < $12.99 → day-2 plan for 10/16 dead. VSTM closed $9.20 on 10/15 (kill fired 10/14, not a position; not re-opened without a fresh check).
- 10/16 premarket: rule-8 gap closing, widen scan, MEDIUM bar OK; catalyst still required.

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



<!-- archived at W44 review 2026-10-31: 10/17–10/24 -->

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

