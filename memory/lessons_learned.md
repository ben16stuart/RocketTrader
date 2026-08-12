# Rocket Lessons Learned

Rules derived from real trades. Read every session.
Full-text versions and older observations: `memory/archive/lessons_history.md`.

---

## Standing Rules — Trading

1. **No catalyst = no trade.** Volume alone is never enough.
2. **Gap 20–35% on a confirmed catalyst = gap-and-go, not a chase** — enter the 9:45–9:50 base. **Gap >35% = second-day only.**
3. **Second-day rule**: gapped >25% yesterday + **closed above the day's midpoint** → today's open IS the entry, within 10% of prior close. Do not wait for a pullback that won't come.
4. **Close-position-in-range is the tiebreaker** (2026-08-07). Below the midpoint on heavy volume = distribution = dead, catalyst regardless. ASPN (+37.5% → 28% of range) and EVH (+16.6% → 9%) both had real news and both died; QNST/RCEL/CRSR closed 86–92% and held. **Validating the catalyst is no longer the hard part — surviving day one is.**
    - **4a. The rule also applies to same-day entries, not just carry-overs — 3-for-3** (2026-08-12). VELO's beat-and-raise was genuinely uncapped (ladder, squeeze float, dated dilution all checked out per lesson 6a) but the stock closed at ~25% of its post-entry range after a violent open-spike-and-fade. Closed same day for −1.18% instead of holding into a likely gap-down. A great catalyst write-up does not buy an exemption from weak day-one price action — run the range check at market_close on every satellite, even ones bought that same morning.
5. **Rank on the BALANCE SHEET, not the growth rate.** Growth makes a stock gap; funding structure decides whether it holds the gap over a 1–5 day hold. A GAAP-profitable small cap with real operating cash flow is a structurally different and rarer bet than a fast grower that still needs the equity market.
6. **The dilution check runs FIRST and is Rocket's most profitable rule** — one search. Kills in six sessions: SVCO, STLN, NNBR, RCEL, NRGV. All then traded badly. **A 403 or paywall is not a clean bill of health** — an unresolved check is a to-do that must be closed before the next order, not a pass.
    - **6a. Grade the dilution *structure*, not just its existence** (2026-08-12). Not all overhangs are equal, and treating them as one bucket both misses kills and rejects tradeable names. Worst → best: **(i) converts struck at a VWAP-DISCOUNTED price** — holders are structurally paid to short strength, so the pop itself funds the selling (NRGV: up to 33.25M sh ≈ 18% of shares out, on top of $150M converts and a $300M shelf, against $80.5M equity and a $29.7M quarterly loss — an automatic kill regardless of a +104% revenue print and a $2B backlog); **(ii) a drawn shelf with <1yr runway** (RCEL — kill); **(iii) an undrawn ATM with multi-year runway** (VELO: $100M ATM live but $91.1M cash vs $53.6M liabilities — a named risk to size around, *not* a disqualifier); **(iv) a completed raise months old** (VELO's $50M at $14.00 closed 4/28 — not an overhang at all). **Always date the raise.** A finished offering and a live facility are different facts that the same search returns together.
7. **Extreme moves (+100%+) with real catalysts are not noise** — but never chase the spike. Watchlist and wait 1–3 days.
8. **Missing real catalysts has a cost too.** Apply discipline to entry price, not to whether to trade at all.
9. **Short float >15% + a catalyst = size up.** Squeeze moves are violent and fast. **Run the check on EVERY board candidate, not just the ones that look like squeezes** (2026-08-10): Friday's board recorded QNST's 11.34% but never pulled CRSR's, which is **21.94%** — a whole tier of the thesis was missing from the #2 name. It is one field in the data already being fetched; not running it is free information discarded.
10. **Sub-$3 stocks are traps** — spreads too wide. Watch names sitting within ~5% of the floor.
11. **Analyst price targets are stale on a print day** (2026-08-07). A breached mean target is a prompt to check for revisions, **not** a disqualification. Rocket passed QNST at $20.21 partly on a pre-print $19.00 consensus; it closed $21.08 at 91% of range.
    - **11a. Check the revised target against your own profit ladder, not just against spot** (2026-08-10). QNST's revisions were real (4 raises, all Buy) but landed at a **$22.40 consensus / $24.00 street high** — so Rocket's standard **+15% scale-out ($24.24) sat above every target on the street.** A raise that still caps the trade below your first target is not an upside leg. It demoted QNST from P1 to P2.
    - **11b. An undated analyst headline is not evidence — resolve it against a dated consensus page** (2026-08-10). A search surfaced "Barrington raised QNST to $29"; the current page showed Barrington **reiterating $24 on 8/07**. The $29 was a prior period. Taking it at face value would have kept QNST at P1 on an upside leg that does not exist.
    - **11d. 🏆 The ladder check is now 3-for-3 and is Rocket's best-performing entry filter** (2026-08-12). Every name demoted or skipped on a capped ladder has since died: CRSR (−4.5%, 8% of range), QNST (demoted at $22.02 against a $22.40 consensus → closed $20.90, −5.1%), and the inverse also held — APEI, promoted to P1 *on* an uncapped ladder, still died, but on its own separate flaw (a sub-consensus EPS guide), not on the ladder. **Read: an uncapped ladder is necessary, not sufficient. A capped ladder is close to sufficient for a skip.** Run it before the open, every name, every session.
    - **11c. A capped analyst ladder is a leading indicator, not a footnote — confirmed twice in one week** (2026-08-10). QNST's capped upside (11a) predicted a stall; CRSR's post-print raises ($12–$16, spot already $13.98) showed the identical pattern, and CRSR then opened red and thin the same morning. When fresh, dated analyst targets cluster at or below spot, price weakness at the next session is not a coincidence — check the ladder BEFORE the open, not as a tiebreaker after.

## Standing Rules — Universe gates

12. **Compute market cap at the price you would PAY, and confirm the +25% target still clears $2B** (lesson 18 orig.). FIGS was already out of universe at its gapped price; APPS's +25% target sat outside the ceiling, so it could not be held to its own plan.
13. **ADV within ±10% of the 300k gate → re-verify against raw data before rejecting** (2026-08-07). RCEL was rejected at a 295k reading; the real figure is 302,064. It then ran +63.6%. It was still the right call — an active $200M shelf disqualifies it — but **the right outcome via the wrong gate is luck, not process.**

## Standing Rules — Instruments and tooling

14. **A metric that renders as `nan`, `0.0%`, or `unknown` is a broken instrument, not a cosmetic glitch.** Silent degradation is the failure mode that actually costs money; loud errors get fixed. Two confirmed cases: `portfolio_snapshot.py` printing `SPY return +nan%` (premarket yfinance bars have volume but a NaN close), and the scanner zeroing every `Change` cell for five sessions.
15. **Verify a fix against a live artifact before declaring the problem solved** (2026-08-07). The core sleeve was declared to have solved idle cash on 7/28 — the day it was created, before one rebalance had run against a real band. All three subsequent rebalances failed on share granularity and each was logged as a one-off "remainder" rather than the recurring defect it was. **Cost: −0.49% in Week 32 alone.**
16. **Pull raw 5-min bars to judge a base; pull raw daily bars for carry-overs. The scanner is a NAME SOURCE.** Its RelVol one-liner has contradicted itself in the same session (BOOM: 1.4x and 14.8x). *Corrected 8/07: its **prices** are fine — the "wrong price" reading was extended-hours quoting. Do not distrust the whole tool.*
17. **`alpaca_client.py close SYMBOL` always fully liquidates** — no `--qty`, and it silently ignores one. Use `sell SYMBOL QTY` for any partial reduction. Verify `qty` in the returned order JSON.
18. **Fractional orders now work** (added 2026-08-07). `buy`/`sell` accept fractional quantities so the core can hit its target exactly. **Trailing stops reject fractional qty by design** — size satellites in whole shares; only the stopless IWM core may be fractional. **Confirmed live 2026-08-10**: bought 0.5031 sh to close a 4.77%-of-slice gap, landed within $0.18 of target — the first rebalance since the fix that didn't leave a share-granularity remainder (lesson 15 verification closed out).
19. **Log exits the same day they happen.** CAMP was closed pre-merge with no price, date or reason recorded, and is permanently unrecoverable.
20. **🚨 Token budget is a TRADING risk.** Bull and Rocket share one Claude quota across 10 launchd jobs. A 7/31 session limit finished premarket at 10:05 AM and cost the AMCX entry outright. **<5 searches → inline, never a subagent** (measured overhead ~171k tokens each).
21. **A plist that exists is not a job that runs — check `launchctl list`, not `ls`.** Midday has not executed since **2026-06-15**, when it died on a 429. Absence of a recent log file is the tell.
22. **🔴 Rocket cannot currently measure its own return** (2026-08-07). `portfolio_snapshot.py` derives Rocket's return from a fixed 30% of the *shared* account, which is algebraically the whole account's return — **Bull's P&L included**, and Bull holds 5 of 6 positions. **Trust only the hand-built attribution in the weekly review, never the snapshot table**, until this is fixed.
23. **`alpaca_client.py positions` and `portfolio_snapshot.py` display share counts rounded to the nearest whole number** (2026-08-11) — IWM's real qty was 9.5031 but both printed "10". Cosmetic only (the underlying fill was correct), but the core-rebalance math depends on the exact fractional qty, so **pull the raw position (`_get('/v2/positions/SYMBOL')`) before computing the rebalance band**, don't eyeball the table.

## Rules From Real Trades

### 2026-08-07 — Week 32: a scratch trade and a −0.49% plumbing leak
- ❌ **The week's entire underperformance was infrastructure, not analysis.** Idle cash from whole-share-only rebalancing cost −0.49%; the factor bet was ~nil (IWM − SPY = +0.05%) and the only satellite cost −0.13%. **Every skip was validated by the tape.**
- ✅ **Two root causes found and fixed**: Finviz renamed `Change` → `Change %` (five sessions of zeroed screens), and fractional orders now close the rebalance band.
- ⚠️ **CSTL's stop filled at 2:32 PM and was not seen until EOD** — the midday routine has been dead since June 15.

### 2026-08-06 — CSTL (−$0.75, −0.17%, Rocket's third closed trade)
- ✅ **Entry discipline worked perfectly.** Held on ice from 7/31 when it closed *below* its own $28.60 trigger; bought only on the 8/03 reclaim on ~3x volume with a rising base. Dilution check run and cleared pre-entry.
- ➖ **Neutral outcome, no rule change.** The +15% target was never reachable (high +5.8%), so there was nothing to scale. The trail did exactly its job after a post-earnings high.

### 2026-07-31 — Week 31: zero satellites, and the skips were right
- ✅ **A missed setup is not automatically a missed trade** — CSTL's trigger was a hold above $28.60 and it closed $28.00. The rule would have kept Rocket out regardless of the late session.
- ❌ **The only real miss was AMCX** — it held every level the plan named and closed at its 52-week high. Lost to infrastructure, not analysis.

### 2026-06-05 — MRLN (+$33.40, +0.23% position, Rocket's first trade)
- ✅ **Second-day entry framework WORKS**, and **defense/government milestones deserve full size.**
- ❌ **PROFIT-TAKING DISCIPLINE**: hit +15% and was not scaled, then round-tripped. **Sell 1/3 at +15% and 1/3 at +25%, immediately, per plan.**
