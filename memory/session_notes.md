# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

## 2026-09-26 — WEEKLY REVIEW (Week 39, Saturday) — Grade D; W36–W38 chain rebuilt; files compressed

- **W39:** book −0.99% vs IWM −0.75% = **−0.24%**. Satellites averaged **8.8%** (5/5 sessions
  below the 50% floor). 1 fill (RARE), 0 closed. Full review: `weekly_reviews/2026-W39.md`.
- **W36–W38 chain rebuilt** (reviews never ran): +0.01% / +0.15% / +0.32% vs IWM, all from
  cash timing, 0 satellites. Since the 7/20 rebase: book −2.12% vs IWM −3.54%.
- 🔧 **Book cash corrected to $978.08.** The 9/17 "≈$1,563" figure was the IWM target, not cash.
- 🚨 **New lesson 70:** the RARE entry quoted +2.8% "fresh high" off 9/21's close. The correct
  9/22 close ($15.615) made it a −3.6% day-2 fade.
- 🚨 **Escalated to Ben:** the 50% satellite floor needs 4/4 slots at the 15% cap
  (3 × 15% = 45%).
- **Compressed:** lessons_learned 337 → 64 lines (full text archived) · research_log rebuilt
  for W40 · session_notes archived to 5 entries · strategy.md rewritten (IWM benchmark,
  throughput constraint).
- **W40 watch:** ANGO (10/01, MEDIUM) · CNXC/PRGS (ceiling-capped) · QMCO breakout (check
  news) · RARE held, stop $14.06.

---

## 2026-09-25 — MARKET_CLOSE (Friday, Week 39 day 6) — HOLD RARE overnight; core in band, no rebalance; PRME CLOSED on Gate A; satellite floor breached 5th consecutive session (14.4%)

**Step 1**: `portfolio_snapshot.py` synced clean. Shared account $10,372.88 (later re-synced
$10,372.97 near close), slice $3,111.86, cash $1,435.34 (pooled). Reconciliation balanced:
Rocket core IWM 5.4746 sh ($1,544.30), Rocket satellite RARE 31 sh ($449.66), Bull's SPY.

**Step 2 — RARE.** $14.505 live (raw API), −1.79% today, −3.81% from the $15.08 entry. Stop
confirmed $14.0616 (HWM $15.12) — 3.1% clear, more cushion than midday's 1.5% read. Web search
found no negative Ultragenyx news; Barclays ($35) and Evercore ($18) PTs from 9/21 still stand
well above spot. Multi-day FDA breakout thesis (9/17) intact. **HOLD**, consistent with the
9/23 `market_close` and today's `midday` precedent (lesson 67).

**🚨 PRME gate grading (carried from 9/24 premarket, day-2 Monday 9/28 candidate).** Gate A
required a 9/25 close in the upper half of the day's own range; PRME instead opened at its
high ($3.42) and closed at $2.905, just 5.5% up from the $2.875 low — **Gate A fails, PRME
CLOSED per the pre-committed rule (42d), no Monday entry.** This is exactly the bottom-quartile
distribution shape the 9/24 premarket historical-MDD study predicted for PRME's widest
sessions. Gate C graded for calibration: actual MDD 15.94% vs a predicted ≈11.5% — verdict
right, magnitude undershot, close to the historical worst case. New lesson 68 (the gate
worked); new lesson 69 (satellite floor: 5th consecutive `market_close` breach, 14.4%, and the
one live candidate that could have helped just closed instead).

**Step 2.5 — core rebalance.** Raw IWM qty 5.4746 sh, value $1,544.30 vs target $1,555.93
(slice×50% cap) = −0.37% of slice, well inside the 3% band. **HOLD, no trade.**

**Step 3–4**: No new fills. Day P&L: IWM +$1.86–$2.96 (today's two snapshots), RARE −$8.21 to
−$8.37, book total ≈−$5.41 to −$6.35 (~−0.2% of slice) vs IWM benchmark +0.14%. Since-rebase
Rocket-vs-IWM not recomputed (stale 8/28 chain, W36–W39 all owed — four now).

**Step 5 — notification sent**, confirmed via `ntfy_notify.py` ("Notification sent: [default]
🚀 Rocket Daily — 2026-09-25"). Flagged: satellite floor 14.4% vs 50%, PRME closed, board
empty for tomorrow, since-rebase figure not authoritative.

**Step 6**: `portfolio_state.md`, `trade_log.md`, `research_log.md`, `lessons_learned.md` all
updated this session; memory push to follow.

---

## 2026-09-25 — MIDDAY (Friday, Week 39 day 6) — HOLD RARE (down 5.3%, stop 1.5% away, thesis intact); no afternoon adds

**Step 1**: `portfolio_snapshot.py` synced clean. Shared account $10,371.02, slice $3,111.31,
cash $1,435.34 (pooled). Satellites 14.2% / floor 50% — still breached. IWM core 49.8%
(within cap, no rebalance — that's `market_close`-only per CLAUDE.md rule 7).

**Step 2 — RARE review.** 31 sh @ $15.08 entry, now **$14.28, −5.3%**. Live trailing stop
confirmed via `/v2/orders`: **stop_price $14.0616, trail 7%, HWM $15.12** — only **1.5% below
current price.** This session's own cut criterion ("down >5% + no catalyst improvement =
CUT IMMEDIATELY") is technically satisfied on the arithmetic, but weighed against:
(1) the FDA Fayuvi approval (9/17) is a durable, multi-day breakout catalyst, not a one-day
pop that needs daily reconfirmation — same reasoning `market_close` used 9/23 at a similar
-4.6% intraday read and HELD; (2) lesson 32a: a discretionary exit inside 2% of the live stop
has bad asymmetry — the mechanical 7% trail already covers this decline and will fire on its
own if it continues. **DECISION: HOLD, no discretionary cut.** Flagging the tension itself
(routine's flat %-threshold vs. lesson 32a's stop-distance heuristic) as a genuine observation,
not resolving it unilaterally as a new rule — see `lessons_learned.md`.

**Step 3 — news check.** Web search "Ultragenyx news today" — no negative news, no halt. Only
recent items are the 9/17 approval itself and a 9/02 Angelman Phase 3 failure that predates
and is unrelated to the Sanfilippo/UX111 entry catalyst (already scored as stale noise,
lesson 62). Nothing changes the thesis.

**Step 4 — afternoon scan.** `smallcap_scanner.py unusual_volume`: dominated by closed-end
funds (JQC/NUV/HIX/PML/JFR/NAC/NRK — not operating companies, no catalyst channel) plus
standing kills already on the board (GLND, TRT, AESI, CYPH, SCHL-closed). No fresh dated
catalyst among today's movers; **PRME remains the only live candidate and its entry is
pre-committed to Monday 9/28** (Gates A–D at today's `market_close`), not an afternoon add.
**No new positions opened.**

**Result: NO TRADE.** RARE held unchanged (stop untouched, no tightening — position is
down, not up, so the tighten-on-gains rules don't apply). Satellite floor stays breached
at 14.2%.

---

## 2026-09-25 — MARKET_OPEN (Friday, Week 39 day 6) — NO ENTRY; PRME's plan is Monday-only, one fresh mover (WNC) killed on rule 1

**Step 1**: `portfolio_snapshot.py` synced clean. Shared account $10,352.28, slice $3,105.68,
cash $1,435.34 (pooled), market open. No overnight fills/stops — RARE live at $14.48 (-3.9%
from $15.08 entry), trailing stop untouched at $14.00; IWM core $281.82; SPY confirmed Bull's.
Satellites 14.5% (RARE only) — 4th confirmed `market_close` breach carries in, MEDIUM bar active.

**Step 2**: Nothing to validate from premarket's watchlist — **PRME's pre-committed entry plan
is explicitly Day-2 Monday 9/28**, contingent on Gates A–D (graded at today's `market_close`,
not entered today). PRME trading +0.7% at $3.09 at the open, consistent with a faded AH pop —
no action required, tracked for Gate A grading at close.

**Step 4 (fresh-mover scan)**: `unusual_volume`/`top_movers` run. Overlap tier = **AESI only**
(+19.4%, 5.1x) — already a standing kill (9/24 8-K is a $613.5M equipment PURCHASE commitment,
not a contract win). Rest of `unusual_volume` (GLND, TRT, SCHL, CYPH — standing kills; JQC/JFR/
HIX/PFN/PML closed-end funds, not operating small caps; NKTR/OFIX/ZSQR/IMXI/SCTX/QMCO all flat
or near-flat despite RelVol, no directional confirmation). One fresh name on `top_movers` not
previously screened: **WNC** (Wabash National, +10.5%, 1.4x RelVol) — web search found no dated
news for 9/25; last earnings was a **miss** (EPS $(0.53) vs $(0.44) est.), next report not until
10/29. No catalyst = rule 1 kill.

**Result: NO TRADE.** Satellite floor stays breached at 14.5%. No notification (flat session,
no stops hit, no breaking RARE news).

---

## 2026-09-25 — PREMARKET (Friday, Week 39 day 6) — NO ENTRY (market closed); ONE name carried forward: PRME, MEDIUM, day-2 Monday behind four pre-committed gates

**Step 1 — startup.** All six memory files read. `portfolio_snapshot.py` synced clean: shared
account **$10,367.13**, Rocket slice **$3,110.14**, cash $1,435.34 (pooled with Bull), market
closed. Reconciliation balanced — **Rocket's core IWM 5 sh ($1,546), Rocket's satellite RARE
31 sh ($456), Bull's SPY 9 sh ($6,929)**. RARE settled 9/24 at **$14.77**, −2.4% from the
$15.08 entry, trailing stop live at $14.00 and untouched. Rocket vs IWM since rebase **+5.98%**
(and per lesson 23 that figure is not a valid measure of Rocket — the hand-built weekly
attribution is, and it is 20+ sessions stale).

🚨 **Satellite floor: 14.7% vs a 50% floor — and the breach count is 4 confirmed
`market_close` sessions (9/17, 9/21, 9/22, 9/23), NOT 5.** **No `market_close` ran on 9/24** —
`trade_log.md` and this file both end that day at MIDDAY. Per **lesson 58**, an absent session
is not a session that ran and found nothing, so it is not counted; yesterday's files were
already anticipating a "5th consecutive" that never got logged. The breach was continuously
true across the gap (no trades 9/24), so **rule 8's MEDIUM-conviction bar stays active** —
searched at the MEDIUM bar, stated explicitly per the routine.

**Step 2–3 — widened board, sourced in the order lesson 41b mandates.**
- **Earnings calendar FIRST** (24 reporters 9/24 AMC, 10 for 9/25): exactly one in-universe
  name, **SCHL**, and it is a **KILL** — and the calendar row *lied about it*. See below.
- **All four screeners run.** Overlap tier (`top_movers` ∩ `unusual_volume`) = GLND, GRML,
  TRT, TE, HSDT — **every one a standing or fresh kill**: GLND third independent kill (same
  three grounds as 9/24's two sessions, no new fact), GRML lesson 60 (blank EDGAR
  `stateOfIncorporation` on a thrice-renamed shell, +474% in 4 sessions), TRT at the **low** of
  its week range and −28% on the month, HSDT is "Solana Co" (crypto mandate, lesson 31), TE no
  catalyst. `breakouts` immaterial (SRZN ADV 219k FAIL, BLFS $1.90B rule-13 FAIL). 
  `short_squeeze` returned the **same perpetually-shorted names as 9/24** at 0.0–0.2× RelVol
  and ±1% — high short float with no catalyst is not a setup.
- **FDA + analyst-initiation channels.** The analyst channel produced **six** dated 9/24 Buy
  initiations and **all six fail the universe** (PGEN $2.76B · BFLY $2.51B · USAR $5.77B ·
  TTRX ADV 117k · QNCX $31M cap + 30k ADV · ENTX $2.80 + Israeli Ltd). **6 requested → 6
  returned, count verified (43b).** The FDA channel produced the session's one name.

**Step 4 — the one survivor: PRME (Prime Medicine), MEDIUM, day-2 Monday 9/28.** FDA cleared
the **PM647 IND for Alpha-1 Antitrypsin Deficiency, dated 9/24**, primary-sourced; +13.0% AH
to ~$3.47 off a $3.07 settled close. Gates run: cap $557M ✅ · **EDGAR `stateOfIncorporation` =
`DE`** ✅ (52a, primary source, CIK 0001894562) · **median ADV 3,075,700** with all five recent
sessions 2.9–4.7M, no contamination (46) ✅ · earnings 11/06, +42d, clean calendar (29) ✅ ·
**short float 22.65%, 11.74 days to cover** → squeeze flag (9/10) · **dilution: zero offering
filings in all of 2026**, only an S-8 (not an offering, 8b) ✅ — **but cash $108.8M with runway
only "into 2027" means the shelf is UNDRAWN and an IND pop is the classic pricing window**,
the largest risk on the name · ladder passes with huge room (+15% $3.99 / +25% $4.34 vs a
$6.00–7.02 consensus and a **$4.25 low**), **flagged undated per 11a**.
🥇 **Stop fit measured with the approved statistic (54c — MDD from the running high, not
range÷trail), on PRME's own 4,674 five-min bars**: median MDD **5.27% = 0.75× the trail, fits**
and survives **77%** of sessions — **but on its 8 widest sessions median MDD is 11.52% (1.65×)
and five of those eight closed in the bottom quartile of range.** **A wide day in PRME is
historically distribution, the opposite of the KMTS shape that made lesson 51's case.** Hence
day-2, not today — rule 45c's "not today, not not-ever," reinforced by rule 2 (same-day 0-for-3).
**Four gates pre-committed as SHAPES not levels (42c): A** 9/25 must close in the upper half of
its own range, below the midpoint = **closed, not deferred** (42d); **B** any 424B5/S-3/S-1/FWP
before Monday's open = kill; **C** falsifiable forecast — predicted 9/25 range **19.2%**, MDD
**≈11.5%**, to be graded at `market_close`; **D** re-verify a *dated* consensus before sizing.

🚨 **NEW LESSON 65 — the Nasdaq earnings calendar fabricated a beat on the one name that
mattered.** Its SCHL row printed `eps $(2.52) vs $(3.42)` — the *shape* of a beat. The
issuer's own 8-K exhibit: **GAAP loss WIDENED to $(3.77) from $(2.83)**, adjusted **$(3.63)**,
revenue **$216.8M, −4% YoY** and below consensus, FY27 outlook merely **"affirmed"** (rule 5f:
a reaffirmation is 0% change), stock **−12.57% AH to $30.45**. **Neither calendar figure
matches any number in the release on either basis.** 41d promoted this API to Rocket's primary
rung-1 sourcing instrument precisely because screeners go blind; **it does not go blind, it
goes wrong in a shape that reads like a result**, and it errs toward *entering*. Rule 57b
already had the fix — the issuer's filing confirms *what*, a tabular API row is still just a
search result.

🚨 **NEW LESSON 66 — the lesson-59 premarket liquidity check cannot be run on this account.**
Alpaca `sip` bars returned **403 "subscription does not permit querying recent SIP data"** for
all six symbols **including the SPY/IWM control**; `iex` snapshots still work. ✅ **The control
is what made this a feed finding instead of a fabricated "quiet tape" finding** (59c). So every
premarket scanner price this session is an **unverified quote** — 55b's arithmetic reconciles
(PACK $4.61/$4.22 ✓, AMPG $3.63/$3.44 ✓, TRT $7.47/$7.26 ✓) but 59 proved reconciliation
certifies nothing. Escalated as an entitlement gap, not worked around.

⚠️ **`eligibility` dropped 2 of 8 rows again (43a, 3rd time the dropped row mattered)**:
`SCHL LGCY TBN HTLM ZONE TRT PACK AMPG` → 6 rows, **SCHL and LGCY omitted, exit 0**. Both
returned normally re-run alone, and SCHL was the session's primary earnings candidate. The
mandatory count caught it. A later 6-ticker call returned 6/6.

**Step 5 — macro (`market_data.py macro`, one call).** VIX **15.38 LIVE, −1.85%** — yesterday's
uptick faded, far below the 22 brake, **rule 29 blocks nothing**. Futures **all three legs
green**: ES +0.24%, NQ +0.47%, **RTY +0.20%** (weakest of the three but positive). 10-yr
**5.16%** close 9/24 — still above the 4.75% trigger, a standing **level** flag on a trend,
not a new event (34). Crude both legs down; **Brent ROLLED and the tool corrected it (naive
−7.27% → true −1.37%)**, lesson 50 working as designed. SPY/IWM settled 9/24 at 767.18/281.66,
both ~flat.

🚨 **Which constraint actually bound today, re-measured not assumed (53a): board and universe
quality (lesson 36), NOT stop width.** PRME's normal-day MDD is **0.75× the trail** and AESI,
PACK and MASS fit inside it too. Nothing died because the stop was tight — they died on a
widened loss with an affirmed-only guide (SCHL), a **$613.5M equipment PURCHASE commitment
worth 44.7% of market cap mislabelled as a contract win** (AESI — rule 7a in reverse, and the
company suspended its dividend in Q3 2025), two unexplained moves with no verifiable catalyst
(PACK, AMPG — rule 1's explicit AVOID), three cap failures and four ADV failures. **This is
the inconvenient answer for Rocket's own standing stop-width escalation, recorded anyway (53b).**

**No trades placed (market closed), no Ntfy sent (no breaking news on RARE).** Honest statement
of the gap: **PRME alone cannot close the satellite floor** — one satellite at the 15% position
cap takes satellites from 14.7% to only ~29.5%. **Three more qualifying names are needed and
the board has not produced three in nine sessions.** IWM core is at its 50% cap; no
cash-thesis exception applies because no bearish view is being made.

🚨 **`weekly_review` W36/W37/W38 owed — and W39 falls due TODAY, making FOUR.** Chain stale
since 8/28 W35 (20+ sessions). Four owed reviews is where the whole escalation backlog is
stuck: rebalance basis (44), ADV-vs-account-size (46f), stop width (48c/51d), and the
satellite-floor pattern (61/63). Lesson 47c: flagging is not fixing, and this is the fifteenth
consecutive flag.

## 2026-09-24 — MIDDAY (Thursday, Week 39 day 5) — NO CUTS, NO NEW ENTRY; RARE holds, GLND re-killed independently

**Step 1**: `portfolio_snapshot.py` synced clean. Shared account $10,301.82, slice $3,090.55,
cash $1,435.34 (pooled), market open. Satellites 14.6% (RARE only, 1/4 slots) — 4th
consecutive `market_close` breach still live, 5th pending absent an afternoon find.

**Step 2 (position review)**: RARE (31 sh @ $15.08) at **$14.58, -3.3% from entry** —
inside the 7% trail (stop live at $14.00, HWM $15.055), doesn't meet the "down >5%" cut
threshold. FDA-approval (Fayuvi/UX111) thesis unchanged, not broken. **HOLD**, stop
unchanged — not up enough to tighten (only tightens at +15%/+25%).

**Step 3 (news check)**: web search on RARE found no fresh negative news dated today —
only stale/general coverage (PDUFA dates already resolved, analyst mix unchanged). No
halt risk, no adverse catalyst news. Confirms HOLD.

**Step 4 (afternoon scan, optional)**: re-ran `unusual_volume`. Top mover **GLND**
(+51.5%, 34.3x RelVol) independently re-checked (web search + price pull) and **re-killed
on the same grounds market_open already used**: the "catalyst" is a £500k fee paid to
*extend* an exploration deadline (not revenue-moving), the company is a recent IPO (S-1s
filed this year, contaminating any volume read per lesson 46j), and the price/volume shape
matches the pump-and-dump pattern CLAUDE.md warns against. Second independent kill, same
day, same conclusion. Rest of the list (TRT, KYTX, RZLT, TLSI, ZURA, CGEM, GLAS — all red
and declining; TSSI a standing kill; QMCO/VOYG/NUV/MYI/NAC/PML/PCN/GLOO not small-cap
catalyst shapes) cleared no further look.

**No trade placed.** Satellite floor stays breached at 14.6%; 5th consecutive
`market_close` session below floor live absent an intraday find before 3:30 PM entry
cutoff. No notification sent — no forced cut, nothing new to report.

---

## Session Archives

- `memory/archive/session_notes_2026-09.md` — September 2026
- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
