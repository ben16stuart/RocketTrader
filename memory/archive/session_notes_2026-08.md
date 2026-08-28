
<!-- archived from session_notes.md at Week 32 review, 2026-08-07 -->
## 2026-08-05 — MARKET CLOSE (Wednesday)

**Position review**: CSTL (15 sh @ $29.99) held overnight — closed **$30.36**, up +1.2%
since entry but **-3.0% on the day** (off yesterday's $31.31 close), a quiet pullback off
the post-earnings pop with no distribution signature. Stop clear at $27.77 (9.3% away),
multi-day guidance-raise catalyst still intact. **Hold.**

**Core rebalance**: checked and skipped — IWM (8 sh, $2,400.40) sits **1.33% over** target
core (slice $3,126.82 − CSTL $455.40 − 10% buffer $312.68 = $2,358.74), inside the 3% band.
Notional cash 8.67% of slice, inside the 10% buffer. No trade.

**Day P&L**: Rocket's own positions (IWM + CSTL) **-0.99%** today ($2,884.37 → $2,855.80)
vs **SPY -0.06%** — underperformance is CSTL's overnight-earnings-pop digestion plus IWM
tracking a touch soft, not a fresh problem. Since rebase (7/20): Rocket +3.14% vs SPY
+3.90% (**-0.76%**), consistent with the standing IWM-factor-drag note.

**No trades today** — market_open found all screened candidates disqualified (see
trade_log.md), market_close found no exit or rebalance trigger. Flat session.

**Flagged, not acted on**: portfolio_snapshot.py's reconciliation now shows 12 sh NOW
($1,406) at the broker unattributed to either Rocket's or Bull's trade log. Left alone
per CLAUDE.md ("never re-derive ownership yourself") — worth surfacing at weekly_review
if it's still unresolved.

**Tomorrow's watch**: APPS remains on second-day watch (gate breached today at $13.85–
$13.95, +45.6–46.6%) — check if it closed strong for a valid continuation entry. CSTL
holds. Thin board otherwise; premarket needs a fresh screen.

---

## 2026-08-05 — MARKET OPEN (Wednesday)

**No trades. Both premarket priorities disqualified at decision time; one fresh find
failed on liquidity.** Account: slice $3,143.41, IWM 8 sh $2,416 + CSTL 15 sh $466 =
91.7% invested, notional cash 8.3% — inside the buffer, no funding action needed
(the planned "sell 1 IWM to fund an entry" never triggered since nothing qualified).

- **APPS** ran straight through its own hard gate — plan said no trade above $12.84
  (35% off $9.51), realized tape at 9:45 was **$13.85–$13.95 (+45.6–46.6%)**, 1% off the
  52-wk high. Lesson 15 for the third session in a row: an extension gate written
  premarket does not survive contact with an open that keeps running. Second-day watch.
- **FTK** accelerated from the premarket +11.3% indication to **+28.4–29.4%**, but
  **volume was only 0.4x avg** — a big move with no volume behind it is the opposite of
  a confirmed breakout. Market cap still unverified (`$0M` from the scanner, flagged
  since premarket). And the 10:00 AM ET call was 15 minutes out — would have meant
  holding through a live binary. Three independent reasons to pass; any one would
  have been enough.
- **TBI**, a fresh top_movers name not on the premarket radar (+20.8–26.8%), failed
  the 300k avg-volume universe minimum outright (184k) — never got to a catalyst check.
- AMPX and KODK unchanged, still watch-only. CSTL satellite holds, no action — flat at
  its post-earnings level, stop clear at $27.77.

Full detail in trade_log.md and research_log.md. No ntfy sent (flat session, no stops
hit).

---

## 2026-08-05 — PREMARKET (Wednesday)

**Ran on time at 6:20 AM ET. No subagents; 6 inline searches** — lesson-12 budget
discipline held for the third session running.

**Account**: shared $10,439.53 / slice $3,131.86 / IWM 8 sh $2,418 (77.2%) + CSTL 15 sh
$465 (14.8%) = **92.1% invested, cash 7.9%** — inside the 10% buffer a second straight
session. Reconciler balances. Satellites 1/4, trades 1/5. Max satellite $470, 1.5% risk $47.

**Watchlist built (research_log.md)** — the whole board is earnings prints again:
- **APPS (P1, HIGH)** +26.8% to $12.06 — Digital Turbine Q1 FY27: EPS $0.17 vs $0.14, rev
  $166M **+27% YoY** (+10.2% surprise), adj EBITDA $42.5M **+69%**. **The raise is the
  catalyst**: FY27 guided $650–670M / $145–155M EBITDA vs FY26's $530–535M / $92–95M —
  **~+23% revenue and ~+57% EBITDA growth guided.** Explicitly AI-attributed (AI ad
  targeting → AGP +56%). **Dilution clears** ($430M term loan refinanced to 2029, no
  offering/ATM/converts). Cap $1.46B, ceiling not until $15.72. **Short float only 9.1% —
  not a squeeze, do not size it up.** Float 109M, so expect a grind not a rip.
- **FTK (P2)** +11.3% — 100% EPS beat ($0.26 vs $0.13) and **the only real squeeze profile
  screened: 14.2M float, 17.66% short float, 8.29 days to cover.** Ranked down anyway
  because energy is still dead, the gap is below the 20% band, and **the market-cap gate
  returned `unknown` — verify before sizing.** Live earnings call 10:00 AM ET.
- **AMPX (P3)** +8.5% — rev $34.0M vs $29.3M, **+126% YoY**, FY26 raised to ≥$140M.
  ⚠️ **Uncleared dilution flag**: its own release books a $1.9M charge on a "warrant
  exchange." BLZE's lesson — not tradeable until checked.
- **KODK (P4, watch only)** +10.9% — **could not verify the actual Q2 numbers in two
  searches.** Kodak moves on pension-surplus accounting historically. Rule 1 applies.

🚨 **TWO HARD GATES ON THE P1 TRADE.**
1. **APPS 35% gate = $12.84**, and the indication is $12.06 — only 6.5% under it. Lesson 15
   exactly: BLZE opened compliant at +29.1% yesterday and was **+51% by 9:45**. Recompute
   off the realized open *and* at decision time.
2. 🚨 **The 9:45 base window is contaminated today** — **S&P Global Services PMI prints at
   9:45 AM ET**, ISM Services at 10:00. The release lands *inside* the base window, not
   after it. **Require the 9:50–9:55 bar to confirm the base held through the print.**

**Cash is still the binding constraint, not conviction** — notional slice cash is $249
against a $470 max satellite. **Any entry must sell 1 IWM first** (~$302). Planned APPS
size: 38 sh ≈ $458 (14.6%), re-struck off the fill as `int(469.78/fill)`.

**Macro**: 🚨 **the rates contradiction is finally resolving in small caps' favour — 10-yr
4.63% (−1.26%)**, down from 4.74% after three sessions of backing up. IWM closed **+1.85%
vs SPY +1.80%** — small caps led for the first time this week. VIX 16.35, sizing
unrestricted. Futures flat and directionless (S&P +0.30%, Nasdaq −0.07%, Russell +0.19%),
so stock-specific catalysts carry the day. Gold +2.84% with VIX *down* = a debasement/
rate-cut trade, not fear.

**Theme read**: the AI theme keeps paying but **the individual names keep failing to hold
their gaps** — AMRC and BLZE both had genuine catalysts Monday night and both closed near
their lows Tuesday on 3x volume. Validating the catalyst is not the hard part; surviving
day-two distribution is. That is why today's plan waits for the 9:50–9:55 confirmation.

**🚨 Scanner integrity finding**: **APPS is the day's biggest mover (+26.8%) and never
appeared on `top_movers` at all** — only on `unusual_volume`. The both-list overlap tier
produced exactly one name (DFNS, a standing hard avoid) and would have missed the entire
watchlist. The overlap filter is not a substitute for reading `unusual_volume` in full.

**Housekeeping**: `market_context.md` now holds 4 snapshots — archive the 7/31 one at the
next weekly_review.

**No trades placed** — market closed, premarket session. No Ntfy sent: CSTL is flat at its
$31.18 prior close with no overnight news.

---

## 2026-08-04 — MARKET CLOSE

**Position review**: CSTL (15 sh @ $29.99) held overnight — closed **$31.31, +5.1% on the
day** (off yesterday's $29.79 close) on continued digestion of the Q2 beat-and-raise, no
distribution signal, stop at $27.77 well clear. Multi-day catalyst, not a one-day pop, well
short of either profit target. **Hold.**

**Core rebalance**: checked and skipped — IWM (8 sh, $2,414.72) sits **2.2% over** target
core (slice $3,127.30 − CSTL $469.65 − 10% buffer $312.73 = $2,344.92 target), inside the
3% band. Pooled notional cash ~7.8% of slice, inside the 10% buffer. No trade.

**AMRC and BLZE second-day setups are DEAD.** Both faded hard intraday — AMRC closed
$27.73 (open $31.93, high $31.93, low $27.33) on 2.7x ADV; BLZE closed $19.82 (open
$20.13, high $23.99, low $19.65) on ~3x ADV. Distribution all session, not basing. Removed
from tomorrow's second-day watch (research_log.md updated) — a clean continuation entry
needs a real base, and neither name gave one.

**Day P&L**: Rocket's own positions (IWM + CSTL) **+2.47% today** ($2,814.85 → $2,884.37)
vs **SPY +1.81%** — IWM tracked SPY closely (+1.97%), CSTL's +5.1% single-name day was the
edge. Since rebase (7/20): Rocket +3.15% vs SPY +3.94% (**-0.79%**), still net negative on
the IWM factor bet per the standing attribution rule.

**No trades today** — market_open found all four screened candidates disqualified (see
trade_log.md), market_close found no rebalance or exit trigger. Flat session.

**Tomorrow's watch**: thin board — CSTL continues to hold, AMRC/BLZE off the list (see
above), REPL still FDA watch-only (PDUFA now 3 days overdue, no decision published, two
prior CRLs — no entry either direction). Premarket needs a fresh screen; nothing carries
forward with real setup quality.

---

## 2026-08-04 — PREMARKET (Tuesday)

**Ran on time at 6:20 AM ET. No subagents; 6 inline searches** — held to the lesson-12
budget discipline for the second session running.

**Account**: shared $10,226.33 / slice $3,067.90 / IWM 8 sh $2,368 (77.2%) + CSTL 15 sh
$447 (14.6%) = **91.8% invested, cash 8.2%**. ✅ **Cash breach cured — first session inside
the 10% buffer in four**, and the cure was a satellite (CSTL), exactly as lesson 7a said.
Reconciler balances. Satellites 1/4, trades 1/5.

**The best catalyst board in three weeks, and it has a single theme: AI power /
data-center infrastructure.** Monday-night earnings produced three validated names —
after weeks of screens that produced one marginal name or none.

**Watchlist built (research_log.md)**:
- **AMRC (P1, HIGH)** +29.8% AH — Q2 double beat, **backlog +32% to a record $6.73B**,
  **$1.8B new awards of which $1.2B is data centers**, FY26 EPS guide raised. Float 32M,
  NYSE, **dilution check clears**. Gap-and-go 9:45–9:50 base. Short float only ~10.6% —
  **not a squeeze, do not size it up as one.**
- **BLZE (P2)** +20.6% — real beat-and-raise on a $335M CoreWeave deal, **but the catalyst
  and the dilution are the same transaction**: 4.19M warrants at $7.60 (147% ITM) freshly
  registered for resale. Fallback only.
- **VOYG (P3)** / **INSP (P4)** — both real beats, both ranked down: VOYG **exits the $2B
  universe ceiling at $33.73**, only 4% above indicated; INSP is a multi-week re-rate, not
  a 1–5 day momentum trade.

🚨 **The binding constraint today is CASH, not conviction.** Pooled cash $430.37, but
Rocket's notional share is **$253**. A ~$410 satellite bought straight from the pool would
spend **Bull's** cash and push Rocket over its slice. **Any entry must sell 1 IWM first.**

**Retired AMCX** after four sessions as Priority 1 — closed −2.7% on dead-average volume,
never triggered, lesson-8 window expires today, and both raised analyst PTs sit *below*
spot. A momentum trade with no valuation leg and fading volume is finished.

**REPL PDUFA is 2 days overdue with no decision.** Silence past a goal date with two prior
CRLs behind the BLA is not neutral. Watch only, no position either direction.

**Macro**: VIX 15.72 (lowest in weeks), Russell fut +1.72% but lagging Nasdaq +2.43% —
tech-led, not breadth-led. **No tier-1 data today** (NFP 8/07, CPI 8/12), so unlike Monday
a 9:45 entry is not exposed to a scheduled release. Rates contradiction unresolved for a
third session: 10-yr 4.74% still backing up while crude falls another 5%.

**🐛 FIXED — the benchmark comparison was silently broken.** `portfolio_snapshot.py` printed
`SPY return since rebase | +nan%`. Root cause: premarket, yfinance returns today's forming
bar with volume but a **NaN close**, and `market_data.get_spy_return()` took `Close.iloc[-1]`
blindly, propagating NaN into every downstream figure. `get_spy_daily_return()` had the
identical flaw (it feeds market_close). Both now drop unpriced bars before indexing;
premarket they correctly yield the last *completed* session. Verified: **Rocket +1.19% vs
SPY +0.67% → +0.52% relative.** ⚠️ Standing caveat: with one index ETF and one satellite,
that delta is **IWM-vs-SPY factor beta, not skill** — do not book it as alpha.
**Note this was invisible, not loud** — the number rendered as `nan` in a table rather than
raising. Any session that read the snapshot without looking closely would have had no
benchmark at all.

---

## 2026-08-03 — MARKET CLOSE

**Position review**: CSTL (entered this morning at $29.99, closed ~$30.33, +1.1%) held
overnight — multi-day earnings-guidance-raise catalyst, no fade signal, 7% trailing stop
already in place. Not a one-day pop to trim.

**Core rebalance**: IWM was 11.6% over target once CSTL's entry was accounted for
(satellite now consumes slice that used to be all-core). Sold 1 sh, landing 1.9% over
target — within the 3% band. Rocket now holds IWM 8 sh (core) + CSTL 15 sh (satellite),
0% uncommitted cash breach — see trade_log.md for the full calc.

**Day P&L**: Rocket slice ≈ +1.7% today (IWM's Russell-2000 pop plus CSTL's small gain)
vs SPY +1.44% today — a rare day where the IWM factor bet paid rather than dragged. Since
rebase (7/20): Rocket +1.40% vs SPY +2.08% (-0.68%), still down mostly on the same factor
bet, per the standing attribution rule (CLAUDE.md Portfolio Construction).

**Tomorrow's watch**: AMCX (missed-catalyst 3-day re-check, faded on low volume at today's
open — see research_log.md), REPL (FDA PDUFA binary, still watch-only, no chase).

---

## 2026-08-03 — PREMARKET (Monday, Week 32 open)

**Ran on time at 6:20 AM ET and finished inside the window** — the first clean premarket
since the 7/31 session-limit failure (lesson 12). No subagents spawned; 6 inline searches
total, per the CLAUDE.md thresholds.

**Account**: shared $10,200.62 / slice $3,060.19 / IWM 9 sh = $2,637 (86.2%) / cash 13.8%.
✅ **The SPY orphan is resolved** — the reconciler balances for the first time in three
sessions, SPY attributed to Bull. Satellites 0; weekly trade count reset to 0/5.

**The overnight tape was thin.** Ten names cleared the universe gates; **every one failed
catalyst validation.** Elimination table is in `research_log.md`. Two worth remembering:
- **EVMN +7.6% was the trap** — bouncing on a Phase 2b that **missed its primary endpoint**
  (6/29/26). One search turned a top-5 premarket gainer into an avoid.
- **BIOA topped the RelVol board at 1.6x** purely as a dead-cat bounce off Friday's −63.6%.
  Rule 8 covers +100% moves *up* on real catalysts; it does not license buying collapses.
- **The scanner-overlap tier was empty again** (NRXP, TE — both <1.0x RelVol). Second
  session running where overlap alone produced nothing; the ideas come from
  `unusual_volume` + manual catalyst work.

**Two theme reversals overnight, both material:**
1. 🚨 **Energy momentum is dead — Brent −7.05% to $83.77**, unwinding the whole four-session
   Iran spike. Friday's energy leader list is invalidated. Do not trade a one-day-old theme.
2. **Small caps flipped to the strong side** — Russell fut **+0.68%**, leading S&P and
   Nasdaq. But the **10-yr kept backing up to 4.74% (+1.76%)** anyway, so the bid is fragile.

**Plan for 9:35**: one idea, **AMCX**, 35 sh ≈ $392 (12.8%), entry only on a hold above
**$10.83** confirmed on raw 5-min bars >1.5x. Conviction trimmed HIGH → **MEDIUM-HIGH**:
the weekend PT raises (WF $11, MS $10/Underweight) killed the stale $7.50 bear anchor but
**left the stock above every raised target**. No analyst-upside leg; pure 21% -short-float
squeeze, momentum now 4 days old. **Take the first 1/3 into $12.60–$12.80, not at it** —
the convert strike ~$12.74 and the top PT both sit under the +15% target.

**Open threads for the next session:**
- 🚨 **REPL PDUFA (goal date Sun 8/02) is UNRESOLVED** — no FDA decision published. Lands
  today. Watch only, no position either direction; no chase on approval (lesson 8).
- 🚨 **10:00 AM ISM Manufacturing** hits 10 min after the entry window. **Prices Paid >73
  = stand down on marginal entries.**
- **Cash breach is in its third session** (13.8% vs 10% ceiling, no bearish thesis). The
  AMCX entry is the intended cure; if it does not trigger, the breach must be addressed at
  market_close — and lesson 7a says IWM whole shares cannot fix it cleanly.
- **Midday routine still not loaded in launchctl** (lesson 13) — unfixed, needs the user.


---

# Archived 2026-08-14 (Week 33 weekly review) — sessions 2026-08-06 → 2026-08-13 premarket

## 2026-08-13 — PREMARKET (Thursday, Week 33)

**No trades — market closed. One P1 name: OMER, and it is a better-constructed setup than
VELO on every axis but float.** 7 web searches, done inline, no subagent (lesson 20).

**🥇 OMER (Omeros) — P1, HIGH.** Q2 after Wednesday's close on **YARTEMLEA**, its
first-in-class FDA-approved TA-TMA drug: revenue **$28.5M vs $12.67M consensus — a 125%
beat**; **product sales $32.2M in the first full launch quarter, +190% QoQ from $11.1M**;
adjusted EPS **+$0.02 against a −$0.25 estimate** (swing to profit); **+$4.1M operating cash
flow**; and **CMS granted NTAP reimbursement effective 10/01**. Premarket **$16.39 (+19.6%)**
vs a $13.71 close. The legs: **(a) ladder uncapped by ~2x** — every consensus reading found
($44.54 / $38.00 / $33.00) sits above the whole profit ladder, so +15% ($18.85) and +25%
($20.49) clear even the *lowest* one (lesson 11d, now 3-for-3); **(b) short float 19.7–24.2%
across three sources**, all >15% (lesson 9); **(c) the dilution structure is the best on any
Rocket P1 to date** — the 2026 converts **matured and were paid in full 2/15**, the remaining
9.50% notes are down to **$40.3M** and still being retired, ~**$132M cash**, and the company
is **actively buying back stock** ($100M authorisation, 0.5M sh bought in Q2 at $11.70).
**A live but undrawn $150M ATM is the named risk — mitigated because you don't ATM into a
buyback.** Tape is the biggest upgrade on VELO: four tight rising closes into the print
($13.25→$13.71) at the top of the weekly range, above MA50, and the **52-wk high is only
$17.65 — 7.7% overhead versus VELO's 96%**. Entry on the **9:45–9:50 base, not the open**
(VELO's spike-and-fade), do not chase above $17.75, stop $15.24, **29 sh = $475.31 (15.0%)**
— the cap binds, risk-based sizing allowed 41. Funding needs **~0.589 fractional IWM shares**.
⚠️ **Honest nuance**: Omeros did **not** formally raise guidance (launch-stage biotechs don't
guide), so this is a beat + forward reimbursement catalyst, not a literal beat-and-raise; the
+190% QoQ ramp is what replaces the raise. **The real bear case is Q3 sequential product
revenue** — $32.2M may include specialty-pharmacy stocking, and a sequential decline breaks
the thesis outright. Single-product concentration; $17.65 sits between entry and target one.

**🚨 HLIT — best headline on the board, killed by the capped ladder.** EPS **$0.24 vs $0.12**,
revenue **$173M vs $112.9M**, broadband **+54%**, **FY26 raised a second time** to $505–525M,
**backlog +71% to $587.6M**, video business divested = pure-play broadband. Premarket +23.3%.
**Then the ladder: the mean was raised only to $15.29 (from $12.71) against a $14.80 price —
+3.3%. Jefferies went $10 → $15 but KEPT A HOLD.** Both Rocket targets ($17.02, $18.50) sit
**above the entire fresh analyst complex** — the QNST/CRSR pattern exactly (lesson 11a/11c).
**Independent second knock**: the lesson-12 cap ceiling — 108.5M sh × $18.50 = **$2.007B**,
0.35% through the lid, the third name after APPS and BW. **Two rules, same answer** — and
worth noting the ceiling cost nothing here, since the ladder killed it anyway.

**⏳ CURI — real catalyst, not tradeable today.** Record Q2: **AI-licensing revenue +48% to
$14.1M** (880B-token code corpus), GM **53%→73%**, adj EBITDA **$11.4M (+300%)**, **outlook
raised** — a genuine beat-and-raise. But it **gapped +35.8%** ($2.80 → $3.80), which is
**second-day-only** under rule 2, and the **$2.80 base is a sub-$3 stock** (lesson 10) that
FAILS `eligibility` on last close. **Check Friday — valid only if it closes today above the
day's midpoint.** Also dropped: **MGNX / IPWR / INV** (all report *today*, and all were
running premarket *before* the print — exactly what the earnings-week rule exists to stop);
**SECZ** (−15%, a decliner); ten names moving +3–7% on 0.0–0.2x RelVol with no catalyst.

**Macro — the week's dominant risk is spent, benignly.** **CPI printed exactly in line:
headline +0.1%/3.4%, core +0.2%/2.5% — the coolest annual core since March 2021.** The
reaction matters more than the number: **the 10-yr did not move (4.68%)**, VIX fell through
15 to **14.63**, Brent extended −1.48%, and gold's 8-session run finally decelerated. The
4.75% trigger was tested by the biggest scheduled event of the week and never came into play.
**The event-driven "one satellite" restriction has lapsed as designed.** 🗓️ **PPI prints
today 8:30 ET** (forecast +0.2% vs −0.3%) — same favourable structure, resolves before the
open; **hot ≥~0.5% → no new satellite, hold the core.** IWM beat SPY a second straight session
(+0.57% vs +0.25%) — **logged as beta, not skill.**

**Account**: slice **$3,179.09**, **IWM 9.5031 sh = $2,882.39 (90.7%)**, 0 satellites,
notional cash **$296.70 (9.3%) — inside the buffer a fourth straight session**. Weekly count
1/5. No ntfy sent (no open position, no breaking news).

---

## 2026-08-12 — MARKET CLOSE (Wednesday, Week 33)

**VELO closed same day, −1.18%.** Entered $15.27 at the open on a genuinely strong
beat-and-raise (see premarket below), but the stock opened with a spike to $17.61 that
immediately round-tripped to $14.35, based at the $15.27 entry, popped to $15.83 by
10:45 ET, then faded on light volume all afternoon to close near $15.09 — bottom ~25%
of its post-entry range. Cancelled the trailing stop and closed discretionarily rather
than hold into a weak close; new lesson 4a (close-position-in-range applies to
same-day entries too, now 3-for-3 with ASPN/EVH).

**Core rebalance**: 0.79% of slice over target (IWM $2,876.68 vs $2,851.56 target) —
inside the 3% band, no trade.

**Day**: Rocket ≈+0.35% vs SPY +0.25% (beat by ~0.10%). Since rebase (7/20), hand-built
Rocket ≈+4.65% vs SPY +4.12% → **Rocket vs SPY ≈+0.53%**. Weekly trade count: 1/5
(VELO buy+sell counts as the week's one entry).

---

## 2026-08-12 — PREMARKET (Wednesday, Week 33) — CPI DAY

**No trades — market closed. One P1 name, VELO, and it is the best-constructed setup in weeks.**
7 web searches, done inline, no subagent (lesson 20).

**Yesterday's board fully resolved, and every skip was validated by the tape**: APEI closed
**$45.72 (−3.5%, 27% of range)** — the sub-consensus EPS guide knock written into its own P1
writeup is exactly what killed it. QNST closed **$20.90 (−5.1%, 35%)**, straight back through
the $22.40 consensus it had just reached — **lesson 11c is now 3-for-3**. FF stopped out
(−$12.24); its P2 knocks (no raise, no coverage) were the right knocks.

**🥇 VELO — P1, HIGH.** Q2 after Tuesday's close: revenue **$20.7M +52.3%**, GAAP gross margin
swung **−11.7% → +21.5%**, **FY26 guidance RAISED** to $65–75M, H2 GM guided >30%, positive
EBITDA projected H2, **backlog nearly doubled to $31M**. The three legs that matter all point
the same way: (a) **beat AND raise** — the only version that works per the standing theme;
(b) **uncapped ladder** — consensus **$23.75** (high $33) vs a $16.20 entry, so **both +15%
($18.63) and +25% ($20.25) sit below the mean**, with targets *rising* post-print;
(c) **short float >15% on a 13.8M float** — squeeze leg live (sources disagree, 18.6% of
shares out vs 35%+ of float; every reading clears the bar). Entry $16.20 on the 9:45 base,
**do not chase above $17.50**, stop $15.07, **29 sh = $469.80 (14.9%)**.
🚨 **Honest knock recorded**: a **live, undrawn $100M ATM** (S-3 effective 4/08, agreement
5/15) — an 18% gap is exactly when a company uses one. Also still GAAP-unprofitable, and the
6-mo high of $31.75 means this is a *recovery*, not clean-air breakout. Funding needs ~0.58
fractional IWM shares sold.

**🚨 NRGV — best headline on the board, killed by the balance sheet.** Revenue +104%, backlog
**~$2B**, a **1.25 GW AI data center** deal, FY26 guidance raised to $270–310M. Then: **$29.7M
GAAP loss in one quarter against $80.5M equity**, $150M converts, a $300M shelf, and an amended
debenture convertible into **33.25M shares at a VWAP-DISCOUNTED price** — holders paid to short
any pop. Added to the HARD AVOID list. **This produced new lesson 6a**: grade the dilution
*structure* and **date the raise** — VWAP-discounted converts (kill) ≠ drawn shelf (kill) ≠
undrawn ATM with runway (risk to size around) ≠ a completed raise months old (not an overhang).
That distinction is what separated NRGV's kill from VELO's pass; the same search returns both.

**Also dropped**: HYLN → watch-only (real $41.7M Navy ONR contract, but **EPS only in line**, an
active **Pelican Way short report** contesting its $133M LOI, 125M float, and NYSE American
listing); LENZ (beat-without-raise — product revenue just **+9% QoQ**, the SVCO pattern); JFB
(**no catalyst** despite being the only name on both scans with real RelVol — a 5.7M-float IPO
on unexplained volume is the manipulation profile); MGNX/TE (earnings-week bar).

**Macro — three of yesterday's four worries resolved favourably.** VIX 15.38 (no brake).
**Russell futures GREEN, breaking the two-session red streak** — and Tuesday inverted the drag:
**IWM +0.34% vs SPY −0.32%**. **10-yr backed off to 4.68%** (7bp from trigger, was 5bp).
**Brent got no second leg** ($88.74, −0.19%). Only gold still leans inflationary — 8 straight up
sessions, +2.16%. **The key structural point: CPI prints 8:30 ET, an hour BEFORE the open**, so
today's entries trade a *known* number rather than carrying it as day-2 risk. Consensus headline
+0.1% M/M / 3.4% Y/Y, core +0.2% / 2.5% Y/Y. **The "one satellite" restriction was event-driven
and lapses with the print — but confirm the actual number at 8:30 before sizing. A hot print
(≥~0.3% M/M) → no new satellite, hold the core, re-screen tomorrow.**

**Account**: slice **$3,162.74**, **IWM 9.5031 sh = $2,866.80 (90.6%)**, 0 satellites, notional
cash **$295.94 (9.4%) — inside the buffer a third straight session**. Weekly count 1/5. No ntfy
sent (no breaking news on an open position).

---

## 2026-08-11 — MARKET CLOSE (Tuesday, Week 33)

**FF stopped out mid-morning** (72 sh, $6.61 → $6.44, −2.57%, −$12.24) — clean stop
fill, one session, small loss. Zero satellites open into the close. **IWM core within
band** (0.29% of slice off target) — no rebalance trade. Day: Rocket ≈−0.10% vs SPY
−0.36% (+0.26% today, +0.52% since 7/20 rebase, hand-built per lesson 22). New lesson
23: `positions`/`portfolio_snapshot.py` round share counts for display (IWM showed
"10" vs actual 9.5031) — pull raw positions before rebalance math. ntfy sent,
confirmed. Full detail in `trade_log.md`.

## 2026-08-11 — PREMARKET (Tuesday, Week 33)

**No trades — market closed. Board fully rebuilt: Monday's entire watchlist is dead, and
three fresh names printed Q2 after Monday's close.** 5 web searches, done inline, no subagent.

**Monday's board was wiped out by the tape** — CRSR closed **8% of range (−4.5%)**, ARCT
**25% (−4.9%)**. The lesson-11c capped-ladder call on CRSR was right in real time. QNST is
the only survivor (new 52-wk high, 83% of range) but spot **$22.02 has now reached the $22.40
consensus** — the cap problem is worse, so it stays a watch, not a position.

**New board (all three reported AFTER Monday's close, so today is their day one):**
1. 🥇 **APEI — P1, HIGH.** EPS **$0.52 vs $0.36** (+44% beat), revenue $171.7M, adj EBITDA
   +36.8%, **FY26 guidance raised on all four metrics**. Net cash, GAAP profitable, **float
   just 13.87M**. The differentiator: **its profit ladder fits *under* the street's targets**
   (+15% = $61.53 vs a $62.17 mean; +25% = $66.88 vs a $68 high) — the exact inverse of QNST
   and CRSR, which both stalled on capped ladders. Entry $53.50 on the 9:45 base, stop
   $49.76, **8 sh = $428**. Honest knock recorded: the raised FY EPS guide ($2.48–2.79) still
   lands **below** the $2.93 street consensus.
2. 🥈 **FF — P2, MEDIUM.** Revenue **+120.6%**, swing to **+$11.4M GAAP net income**,
   **zero total debt**, opening ~15% above its 52-wk high with no overhead supply. Held to P2
   because there is **no raise** (soft "positive adj EBITDA" guide), no analyst coverage, and
   biofuel is credit-timing-driven. 76 sh = $471.
3. ❌ **BW — the best catalyst on the board, excluded by the universe ceiling.** Revenue +130%,
   **backlog +533%**, +34.9% premarket, analyst mean $24.67 vs $11.98. But 148.8M sh × $11.98
   = $1.78B, so **even the +15% target implies $2.05B — outside the $2B cap** (lesson 12).
   Not traded. **Second time in two weeks the ceiling killed the best name (after APPS) —
   flagged for `weekly_review`, not overridden today.**
4. ❌ **HZO resolved and permanently skipped** — Monday's +45.8% was an **all-cash $53.00
   Blackstone/Safe Harbor buyout**, price pinned at a 1.7% arb spread. Rule 2's second-day
   entry does not apply to merger arb. Closes yesterday's open item.

**Process wins worth keeping**: (a) **lesson 13 paid again** — APEI's ADV came back a FAIL at
298,467, and raw bars put the 3-mo at **300,406 (pass)** and 1-mo at 362,200; re-verifying the
borderline gate saved the P1 name. (b) **lesson 16 paid again** — the scanner's prices were
premarket quotes and its `Change %` was premarket-vs-close; every number was re-derived from
raw daily bars, which is what revealed BW/FF/APEI as after-close prints rather than Monday
movers.

**Macro**: VIX 15.53 (no brake). **10-yr 4.70%, now 5bp from the 4.75% trigger.** Russell
futures red a **second** straight session — that trigger has fired, and Monday delivered
**IWM −0.52% vs SPY −0.03%**. **Brent +6.2% in one session to $89.60**, 24h before CPI.
**CPI is tomorrow 8:30 ET** — anything entered today is open through it on **day 2**, so the
standing call is **one satellite, not two**, first third taken promptly at +15%.

**Account**: slice $3,164.68, **IWM 9.5031 sh ≈ $2,851 (90.1%)**, 0 satellites, notional cash
**$314 (9.9%) — inside the 10% buffer for the first time in nine sessions**, closing the
lesson-15 verification loop. A full-size satellite needs ~0.39 sh of fractional IWM sold to
fund it. No ntfy sent (no breaking news on an open position).

---

## 2026-08-10 — MARKET CLOSE (Monday, Week 33)

**0 satellites open — nothing to review.** Only Rocket holding is the IWM core (9 sh
entering the session). No positions to hold/close decisions today.

**Core rebalance**: slice $3,164.97, target_core $2,848.47 (10% buffer $316.50). IWM
9 sh @ $299.74 = $2,697.66 — **4.77% short, outside the 3% band.** Bought fractional
**0.5031 sh @ $299.74** ($150.81 notional). Filled ~19:58 UTC; position now **9.5031
sh, mkt value $2,848.65** — within $0.18 of target. First rebalance since the
fractional-order fix (lesson 15/18) to close the band exactly rather than stall on a
whole-share remainder — confirms the fix works live.

**Day P&L**: Rocket's book (≈ slice) **+0.39%** ($3,152.62 Fri close → $3,164.97) vs
**SPY −0.07%** today. Since rebase (7/20): Rocket **+4.40%** vs SPY **+4.12%**
(**+0.28%**), chained from the 8/07 weekly-review baseline (lesson 22 caveat: hand-
built proxy, not `portfolio_snapshot.py`'s figure, though they currently agree since
Rocket is 100% IWM with no satellites live).

**No satellite trades today** — market_open found all three ranked ideas (CRSR, QNST,
ARCT — see below) failed at decision time; no second-day candidates worked either.
ntfy daily summary sent and confirmed.

---

## 2026-08-10 — MARKET OPEN (Monday, Week 33)

**No trades. All three ranked ideas failed at decision time; three fresh movers lacked a
confirmed catalyst.** Checks done inline (3 web searches + 2 scanner re-pulls), no subagent.

- **CRSR (P1) — the flagged open check resolved NO-GO, and price confirmed it.** Real
  post-print analyst raises exist (Baird $12, Craig-Hallum $12, Wedbush $13, Roth $16) — not
  stale as hoped, but the resulting $12–16 spread means spot ($13.98) is already above 3 of 4
  targets. Same "no upside leg" signature that demoted QNST last week (lesson 11a), now seen
  twice — logged as lesson 11c. Opened **-2.6% on 0.1x avg volume**, a red/thin fade rather
  than a base. **Not entered.**
- **QNST (P2)** confirmed real strength — **+4.9%, new 52-wk high** — but the pre-registered
  cap-check verdict (own +15% target sits above the street high) doesn't change on a green
  tape alone. Held to its own plan: **watch, not traded.**
- **ARCT (P3)** opened **-2.4%** on thin volume — weakest catalyst on the board, no confirmation. Skipped.
- **Fresh movers**: **HZO** (+45.8%, 104.8x RelVol) is a >35% gap, second-day-only per rule 2
  — watchlist for tomorrow. **MVIS** (+22.1%) had no dated catalyst for today (stale 7/15
  print + a reverse split, itself a mild red flag) — classic pump-prone name, skipped per
  lesson 1. **TNXP** (+12.1%, 5.7x RelVol) reports today but results weren't out yet at
  check time — pre-print move, barred by the earnings-week rule.

**Account unchanged**: slice $3,155.56, IWM 9 sh ($2,707, ~85.8%), 0 satellites, pooled cash
$719.86. No overnight fills or stops. No ntfy sent (flat session).

---

## 2026-08-10 — PREMARKET (Monday, Week 33)

**No trades — market closed. Watchlist rebuilt; Friday's two open checks closed and both
flipped the ranking.**

**The overnight scan produced nothing.** Screeners returned only thin-RelVol extended-hours
quotes (STI +14.7% — standing hard-avoid; NMAD/AMPG/INGN — no catalyst). **Every idea on
the board is a Friday carry-over.** Correctly did not manufacture a new name to fill a slot.

**Both open checks resolved — and the ranking inverted:**
1. ⬆️ **CRSR P2 → P1.** Dilution check came back **clean and then some**: $192.2M cash vs
   $118.3M debt = **~$75M net cash**, GAAP net income **+$9.1M**, operating cash flow **+148%
   to $74.8M**. It does not need the equity market. Then the bigger find — **short float
   21.94%, above the 15% squeeze bar, which Friday's board never checked at all** (lesson 9
   is live). With a 47.4M float (44% of shares out) and a 92%-of-range close, it has the best
   structure on the board.
2. ⬇️ **QNST P1 → P2, on its own pre-registered rule.** Friday's bar was *"if consensus has
   not been raised above ~$24, the upside leg is missing."* Revisions **did** land — four
   raises on 8/07, all Buy — but consensus is only **$22.40 with a street high of $24.00**
   against a $21.08 close. **Rocket's +15% first scale-out ($24.24) sits above every price
   target on the street.** Balance sheet is still the cleanest on the board, so it's a smaller
   trade, not a skip — but the rule was written in advance and was not rationalised away.
3. 🆕 **ARCT promoted to P3** off the secondary board: $191.5M cash / 2.5-yr runway is clean
   for clinical-stage, and **short float 30.65% on a 26.0M float** is the most explosive
   structure available. Held back to P3 because the catalyst is a rights-reversion from CSL,
   not a beat-and-raise, and **revenue collapsed to $2.96M from $28.3M YoY**.

**A search nearly misled the QNST call.** A "Barrington raised PT to $29" headline surfaced
with no date; verifying against the current consensus page showed Barrington **reiterating
$24 on 8/07** — the $29 was a prior period. Taking that at face value would have kept QNST
at P1 on a fabricated upside leg.

**Dropped with reasons**: PUBM (52% range close, −1.0% pre — fade confirmed), EMBC, OABI
(2.7% off the $3 floor, 4.45% short float — no edge), TBCH (**no catalyst ever identified**),
GTN (**retired** — cap gate still `unknown`, an unchecked gate is not a pass), RCEL (standing
avoid; **−4.0% premarket is validating the skip in real time**).

**Macro — two things changed.** 🚨 **Russell futures flipped to −0.27%** after Friday's
+1.04%; they are the only red future while S&P/Nasdaq are green, so small-cap leadership did
not survive the weekend. Notably **CRSR and QNST both held their gaps flat overnight anyway**
— name-specific strength intact while the group softens. 🗓️ **CPI lands Wednesday 8:30 ET**,
so anything bought today is open through it with the 10-yr just 9bp under the 4.75% trigger.
**Argues for one satellite today, not two, and taking the first third promptly.**

**Open for market_open**: (a) verify **CRSR post-print PT revisions** — consensus reads
$12.33, below spot, almost certainly stale, and lesson 6 says an unresolved check is a to-do;
(b) re-derive the **lesson-18 cap check at the actual fill** — a CRSR fill above **~$14.79**
puts the +25% target outside $2B; (c) confirm the base on **raw 5-min bars**, not the scanner.

**Funding**: only ONE full-size satellite (~$459–467) is fundable from ~$444 notional cash —
**fund it by selling a fractional IWM slice**, satellites stay whole-share. If no entry
happens, `market_close` must still top the core up fractionally. **Either path finally
exercises the fractional fix, which has never run against a live order** (lesson 15).

---

## 2026-08-07 — WEEKLY REVIEW (Week 32, Friday post-close)

**Grade: C.** Rocket vs SPY **−0.54%** for the week (+2.97% vs +3.51%). One satellite
closed (CSTL, −$0.75, −0.17%, −0.02R) — a scratch, well executed. **Real alpha −0.13%.**

**The finding: this was an infrastructure week, not an analysis week.** Attribution splits
to factor **+0.04%** (IWM − SPY was only +0.05% — the usual drag excuse was unavailable),
cash drag **−0.49%**, satellite **−0.13%**. Nearly all of the miss was idle cash.

**Two root causes found and FIXED today:**
1. **Fractional orders** (`alpaca_client.py`). IWM at ~$300 vs a ~$3,150 slice makes one
   share 9.6% of the book against a 3% band — unsatisfiable, so ~14% sat in cash every
   session for eight sessions. `buy`/`sell` now take fractional qty; trailing stops reject
   it loudly (satellites stay whole-share). **Untested against a live order — Monday's
   market_close must run the first fractional top-up and verify the fill.**
2. **Scanner `Change` column** (`smallcap_scanner.py`). Finviz renamed the header
   `Change` → `Change %`; the code read the old key and `_safe_float("")` returned 0.0.
   Five sessions of `+0.0%` on every row. Fixed and verified live. **This also retires the
   over-broad half of lesson 16 — the scanner's prices were fine all along.**

**Two defects still open:**
3. 🔴 **Midday has not run since 2026-06-15** — plist is valid and on disk but absent from
   `launchctl list`; last log ends in a 429. Cost visibility on CSTL's 2:32 PM stop fill.
   **Deliberately NOT reloaded — escalated to the user**, because a 5th Rocket job competes
   for the shared Claude quota with premarket/market_open (lesson 20).
4. 🔴 **NEW — Rocket cannot measure its own return.** `portfolio_snapshot.py` derives it
   from a fixed 30% of the *shared* account, which is algebraically the whole account's
   return — Bull's P&L included, and Bull holds 5 of 6 positions. Reported −0.25% vs SPY;
   real figure −0.54%. **Priority 1 for Week 33.**

**Skips were right, with one nuance.** ASPN, EVH, NNBR, MRAM, SVCO, CVRX, STLN, FIGS and
REPL all faded or died. **QNST** was the one questionable pass — skipped at $20.21 partly
on a *pre-print* $19.00 analyst target, then closed $21.08 at 91% of range. **RCEL** was
rejected on a stale 295k ADV reading (real: 302,064, it passes) and ran +63.6% — but it
carries an active $200M shelf with <1yr runway, so the skip was right for a reason Rocket
never reached. Right outcome, wrong gate.

**Memory trimmed**: session_notes 661→~230, research_log 239→~155, market_context 217→81,
lessons_learned 113→56.

**Week 33 board**: P1 **QNST** (rule-3 continuation, GAAP profitable, zero dilution risk,
cap headroom fine — but verify post-print PT revisions). P2 **CRSR** (record margins, low
float, but revenue −2% YoY and the +25% target is only ~4% inside the $2B ceiling; dilution
check not yet run). **RCEL → standing avoid list.**

---

## 2026-08-07 — MARKET CLOSE (Friday)

**No trades.** 0 satellites open, nothing to review. Core rebalance checked and
skipped: IWM 9 sh is 3.91% short of target_core (share-granularity remainder per
lesson 7a — buying 1 sh would overshoot to 5.66% over, worse than doing nothing).

**Day P&L**: book +1.51% ($3,105.58 → $3,152.62) vs SPY +0.66% — IWM itself +1.13%,
small caps outperforming large caps today. Since rebase: Rocket +3.99% vs SPY
+4.20% (-0.21%).

**Week summary**: 1 trade this week (CSTL stop-out 8/06, not a decision), 0 new
entries — QNST and STLN both had real catalysts but failed at entry gates (extension/
target exhausted, confirmed dilution risk). No satellites open into the weekend.

---

## 2026-08-07 — MARKET OPEN (Friday)

**No trades. Both ranked ideas failed at decision time; no fresh mover had a confirmed
catalyst.** Checks done inline (1 web search + raw 5-min bars), no subagent.

- **QNST (P1)** ran from premarket +22.6% to **+32.8% ($20.21) by 9:45**, tapping an
  intraday high of **$20.50 (+34.8%)** in the opening 5-min bar — a hair under the **$20.55
  (35%) extension gate**, with essentially no room left. Worse, **spot is now above the
  $19.00 mean analyst target** with no revision confirmed — the exact "no upside leg"
  problem flagged in the premarket note, now realized rather than hypothetical. Base
  structure itself was fine (higher lows $19.22→$19.74→$20.02, volume already ~0.7x full-day
  average in 15 minutes), but risk/reward is broken: capped upside, full stop-out downside.
  **Passed.**
- **STLN (P2)** held up better technically — **+28.3% ($6.40), 5% under its $6.74 gate**,
  higher lows ($6.02→$6.27→$6.40), volume already ~1.0x full-day average in 15 minutes,
  analyst target $8.40 still +31% above spot. **But the dilution flag the premarket note
  left unverified (SEC 403'd) is now CONFIRMED**: one search found an active **$15M ATM
  facility** (424B5) — live authorization to sell stock into exactly this kind of spike, on
  a company with a **0.1% EBITDA margin and only $41.1M cash**. Same pattern that killed
  SOC and SVCO this month. **Passed** — the dilution check did its job a second time.
- **Fresh movers** (`unusual_volume`/`top_movers`): BZH, XPOF, PUBM, INVX, NRXP, FNKO,
  ARDX, SERV, LZ, CRSR, SSP, EMBC, TALK, INGN, BETR, WHWK, PBYI — none carried a validated
  catalyst from premarket screening, and chasing any of them fresh would mean 5+ new
  searches on unvetted names late in the entry window. Declined per rule 1 (no catalyst,
  no trade) rather than force a trade to avoid a flat session.

**Account unchanged**: slice $3,142.77, IWM 9 sh ($2,707, 86.1%), notional cash 13.9% —
still outside the 10% buffer (the same share-granularity remainder flagged premarket), but
no satellite qualified so no funding trade was triggered. No overnight fills or stops. No
ntfy sent (flat session).

---

## 2026-08-07 — PREMARKET (Friday)

**Ran on time at 6:20 AM ET. No subagents; 8 inline searches + 3 fetches** — lesson-12
budget discipline held for the fifth session running.

**Account**: shared $10,435.72 / slice $3,130.72 / **IWM 9 sh $2,691 (85.9%), 0 satellites**.
✅ Reconciler balances. Satellites 0/4, trades 1/5. Max satellite $469.61, 1.5% risk $46.96.
⚠️ Notional cash **$439.72 = 14.0%, outside the buffer** (share-granularity remainder) —
**any full-size entry must sell 1 IWM first**, which also cures the breach. Rocket vs SPY
improved to **−0.30%** from −1.15% as IWM recovered and CSTL stopped dragging.

🚨 **BOTH SCANNERS WERE OUTRIGHT BROKEN — every row returned `+0.0%`**, so `top_movers` was
a ranked list of zeros and the overlap tier produced nothing for a fourth straight session.
Several scanner *prices* were also wrong vs raw bars (STLN $6.67 vs a $4.99 close; CVRX
$3.41 vs $5.94). **The whole board came from raw yfinance daily bars on carry-overs plus the
live premarket gainers page.** Logged as lesson 16.

**Watchlist built (4 ranked, from 6 fresh prints screened):**
- **P1 QNST (HIGH)** — QuinStreet Q4 FY26 (8/06 post-close): revenue **$373.9M +43%, above
  the top of its own $350–370M guide**; adj EBITDA $41.4M **+87%**; **GAAP EPS $0.33**; FY26
  op cash flow **$130.9M**; **FY27 guided to $1.45–1.55B / $150–160M EBITDA (+33–42%)**.
  Premarket **+22.6% to $18.66 — inside the 20–35% gap-and-go band**, 35% gate $20.55.
  $874M cap, **$2B ceiling ~87% away**. Short float 11.34%, 6.48 DTC. ✅ **Chosen P1 mainly
  because it is GAAP profitable with real cash flow — dilution risk is absent by
  construction**, and dilution killed three of this week's ideas.
- **P2 STLN (MED-HIGH)** — Starling Oncology (renamed from TOI 8/04) Q2: revenue **$161.3M
  +34.6%**, gross profit **+55.2%**, **adj EBITDA positive for the first time**, **FY26
  raised to $650–670M**. Best upside math on the board — **blue sky 24.6% above its 52-wk
  high**, mean target **$8.40 (+26.7%)**. 🚨 Capped at P2: **0.1% EBITDA margin on $41.1M
  cash** = live dilution risk, **unverified** (SEC 403'd the 8-K). And **its 35% gate is
  $6.74 vs a $6.63 premarket print — 1.7% of room, the likeliest disqualification today.**
- **P3 APPS (WATCH)** — closed **$14.27 +8.4% at 96% of range**, new 52-wk high, Craig-Hallum
  PT $10→$18. **Cannot be traded**: $1,727M cap puts the $2B ejection ceiling at ~$16.55, so
  the +25% target is outside the universe. Day 3, +50% off the base. Pullback only.
- **P4 HNST (MED-LOW)** — valid rule-3 second-day (closed above midpoint, zone ceiling
  $5.96), but revenue −10.9% and **mean target $4.81 is BELOW the $5.42 close** (AMCX
  signature). Fallback only.

**Eliminated**: **RCEL/VATE/FRD/SRZN** — four premarket gappers of +17–34%, **all fail the
300k ADV gate, killed in one `eligibility` call with zero searches**. **FIGS** out of
universe at its premarket price ($1,878M cap → ~$2.38B at $14.25). **SVCO** revenue missed
consensus and **Q3 guided BELOW the quarter just delivered** + undisclosed Micron
convertible. **CVRX guidance CUT**. **ASPN** failed rule 3 — closed at **28% of range** on
13.3x volume (distribution). **EVH** closed at 9% of range. **NNBR** PIPE thesis played out
exactly as written. **REPL** — **FDA approved RP1 (TUDRIQEV) 8/06**, but priced in by the
AdCom and **barred by earnings 8/11**; binary closed, removed from rotation.

**Macro**: 🚨 **NFP 8:30 AM ET** — fcst ~80–120k vs 57k prior, U3 4.2%, AHE +3.5%. Pre-open,
so the 9:45–9:50 base window is clean, but it is the month's biggest whipsaw. **VIX 15.28**
(clear). 🚨 **10-yr 4.67% (+1.15%) — the rates tailwind reversed after exactly one session**;
**IWM −0.51% vs SPY −0.16%** again. Gold $4,373 (+3.09%), 4th straight up session with VIX
low = rate-cut positioning, not fear. Energy dead (Brent $82.14).

**Open threads**: (1) **STLN dilution check unrun** — close before any order; (2) **FTK cap
gate `unknown` a 4th session** — verify or retire; (3) scanner numeric columns broken.

**No trades placed — market closed. No ntfy sent (no breaking news on a held position).**

---

## 2026-08-06 — MARKET CLOSE (Thursday)

**CSTL stopped out intraday (2:32 PM ET), discovered at EOD sync — not a market_close
decision.** Trailing 7% stop off the $31.73 high-water mark filled at $29.94 vs $29.99
entry: -$0.75 (-0.17%), essentially breakeven. Catalyst was never invalidated; this is
just the trail giving back the post-earnings pop. **0/4 satellites open now.**

**Core rebalance**: CSTL's proceeds returned to cash, not core, opening a 13.1%-of-slice
gap vs target. Bought **1 sh IWM @ $298.27** (closest whole-share fit to the $408 gap;
2 shares would have overshot further). IWM now **9 sh ≈ $2,684**. Residual ~3.6%-of-slice
gap is a share-granularity remainder, not an actionable miss — flagged for premarket to
watch, not re-traded today.

**Day P&L**: Rocket's total book **-0.68%** ($3,126.82 → $3,105.58) vs **SPY -0.15%** —
the CSTL stop-out (-1.38% intraday) drove the gap. Since rebase: Rocket +2.44% vs SPY
+3.59% (**-1.15%**, widest yet).

No midday session ran today; market_open found all three ranked ideas disqualified (see
below). ntfy summary sent for today's close.

---

## 2026-08-06 — MARKET OPEN (Thursday)

**No trades. All three ranked ideas failed confirmation at 9:45 AM ET; two fresh movers
were too extended to enter same-day.** Checks done inline (2 web searches), no subagent.

- **MRAM** flipped from premarket +8.4% to **-7.3% at $16.14** on 1.5x volume, now below
  its MA50 — a broken base with confirming volume, not just weak confirmation. Removed
  from active watch.
- **APPS** -4.6% to $12.57 on only **0.2x avg volume** — nowhere near the 1.5x bar, no
  confirmed base either direction.
- **NNBR** +6.8% to $4.16 but also only **0.7x avg volume**; already capped MEDIUM on the
  PIPE overhang, so this was the fallback and it didn't confirm either.
- **Fresh finds**: **HNST** (catalyst-validated, 8/05 EPS beat) is +50.3% today on 2.5x
  volume — 29.6% past its own second-day entry zone ceiling, too extended. **ASPN**
  reported a genuine beat-and-raise this morning (Q3 guided $65-80M vs $49.8M delivered)
  but is +54.3% same-day, over the 35% ceiling. Both watchlisted for a second-day/pullback
  check tomorrow, neither enterable today per Rule 2.

**Account unchanged**: slice $3,105.89, IWM 8 sh ($2,396) + CSTL 15 sh ($453) = 91.8%
invested, notional cash 8.2% — inside the buffer, no funding action needed since nothing
qualified. No overnight fills or stops triggered. No ntfy sent (flat session).

---

## 2026-08-06 — PREMARKET (Thursday)

**Ran on time at 6:20 AM ET. No subagents; 8 inline searches + 1 fetch (timed out)** —
lesson-12 budget discipline held for the fourth session running.

**Account**: shared $10,380.36 / slice $3,114.11 / IWM 8 sh $2,404 (77.2%) + CSTL 15 sh
$456 (14.6%) = **91.8% invested, cash 8.2%** — inside the 10% buffer a third straight
session. ✅ **Reconciler balances and yesterday's unattributed NOW (12 sh, $1,369) is
resolved to Bull.** Satellites 1/4, trades 1/5. Max satellite $467, 1.5% risk $47.

**Watchlist built (5 ranked):**
- **P1 MRAM (HIGH)** — Everspin's **highest-revenue quarter ever**: $18.7M **+42% YoY**,
  **13% above the top of its own guide**; non-GAAP EPS $0.11 vs $0.00–0.03 guided (~4x);
  **Q3 guided UP to $19.5–20.5M**. Driven by the $40M US prime-contractor deal converting
  to revenue. Best structure on the board — **18.7M float, 16.53% short float (squeeze bar
  cleared), $378M cap (no ceiling risk), 3.37M ADV**. +8.4% = below the 20% band, so
  conventional base, not gap-and-go. ⚠️ **The muted reaction is the open question** — +8.4%
  merely round-trips yesterday's −7.3%. Volume at 9:45 separates opportunity from tell.
- **P2 APPS (MED-HIGH)** — second-day continuation, and **rule 3 fits cleanly for the first
  time this week**: gapped +38.5%, closed above the midpoint (58% of range) on 3.5x ADV,
  premarket $13.06 **inside** the 10% zone (ceiling $14.49). Catalyst + dilution already
  validated 8/05. No squeeze (109M float); yesterday's high $14.10 is also the 52-wk high.
- **P3 NNBR (MED)** — real beat-and-raise (+19.3% sales, +36.1% EBITDA, FY raised) plus a
  $12–15M firearms contract and a $50M+ datacenter pipeline. 🚨 **Dilution demoted it:** the
  "$124M deleveraging" is funded by a **$75M PIPE at $3.06 (~24.5M sh vs a 31.1M float)** —
  BLZE again, headline and overhang are the same transaction.
- **P4 HNST (MED-LOW)** — 100% EPS beat + raised FY + buyback, but **revenue −10.9% YoY**;
  a margin story, not a growth story. **P5 FTK** — best close on the board (72% of range,
  4.3x ADV) and best squeeze math, but the **market-cap gate has returned `unknown` for a
  third session** and energy is still dead. Not tradeable until verified.

**Eliminated**: **GCT** — best print screened all week (revenue $411.6M +27.6%, EPS $1.16,
19.87% short float) but it is a **Cayman holdco operating through mainland-China
subsidiaries → fails the US-domicile gate**; added to the standing avoid list so it is not
re-screened on catalyst quality. **AEVA** — $115M follow-on offering, $79.6M quarterly loss
on $6.1M revenue, deployment 2H2027, CFO exiting. **ASYS** — reaction already failed
(closed −8.2% at 3% of range). EVH/SPIR/LENZ barred by the earnings-week rule.

**Theme**: earnings are the whole board a third session, but **the new theme is DEFENSE** —
MRAM and NNBR both printed on defense revenue the same night. Rocket's best-ever trade
(MRLN) was a defense catalyst.

**Process flags**: (1) ✅ **the entry window is clean today** — all data is pre-open, the
first uncontaminated 9:45 base window this week; (2) 🚨 **the both-list scanner overlap
produced one worthless name (HDSN, +3.4% at 0.1x) for the third session running** and would
have missed the entire watchlist — every idea came from `unusual_volume` or carry-over
second-day watch; (3) **Rocket can fund exactly ONE satellite** and any entry requires
selling 1 IWM first; (4) **NFP tomorrow** — do not carry a marginal name into it.

**Performance**: Rocket **+2.72%** since rebase vs SPY **+3.73%** → **−1.01%**, wider than
yesterday's −0.76%. IWM −0.64% vs SPY −0.20% yesterday: the gap is the IWM factor drag, not
stock selection. No trades placed (market closed). No ntfy sent — no breaking news on CSTL.

---


---

# Archived 2026-08-21 (Week 34 review) — sessions through 2026-08-18

## 2026-08-18 — MARKET CLOSE (Tuesday, Week 34 day 2)

**No trades. Both satellites held overnight. Core rebalance checked — within band, no action.**

- ✅ **ETON HOLD** — up on the day (Mon close $61.66 → today's close $63.17, **+2.45%**,
  +$10.57 on the position). Multi-day beat-and-raise thesis unchanged, no fresh EDGAR
  filings, stop (trailing from the new $63.26 intraday high) well clear. One-day catalyst
  test does not apply — this is a multi-session breakout story.
- ✅ **OMER HOLD** — essentially flat (Mon close $17.36 → today's close $17.175, **−1.07%**,
  −$5.00 on the position). CMS NTAP reimbursement (effective 10/1) still unplayed; insider
  144 (8/13) / Form 4 (8/17) remain unresolved but not actionable alone. No offering trigger
  fired (S-8 correctly not treated as a raise per lesson 8b). Not down enough, and thesis
  hasn't degraded — holds.
- ➖ **Core rebalance — within band, no trade.** Slice $3,146.79 (shared $10,489.29 × 30%),
  satellite value ETON $442.23 + OMER $463.86 = $906.09, 10% buffer $314.68 → target_core
  **$1,926.02**. Current IWM (raw qty **6.1976 sh**, unchanged since Monday) = **$1,860.21**.
  Gap = **$65.81 short**, under the 3% band (**$94.40**) → **no action**, per rule 5 (avoid
  daily churn).
- 📊 **Today, price-only (prior close → today's close)**: ETON +$10.57, OMER −$5.00,
  IWM −$24.17 (6.1976 sh × $304.05→$300.15) ≈ **−$18.60 net (~−0.59% of slice)**. SPY today
  **−0.69%**. Rocket's book beat the tape today by **≈+0.11%**, on ETON's gain outweighing
  IWM's Russell-led drag and OMER's small pullback. (Cross-checked via a second book
  reconstruction — IWM+OMER+ETON+flat cash — Mon-close→Tue-close: **−$18.40**, consistent
  within rounding.)
- ⚠️ **Slice-vs-book caveat stands (lesson 23a/23)**: `portfolio_state.md`'s since-rebase
  figures (+3.77% Rocket vs +3.38% SPY) are the contaminated slice, not the hand-built book.
  Did not reconstruct the full cumulative hand-built book this session — that's
  premarket/weekly_review work — flagging so today's +0.11%-vs-SPY read isn't extrapolated
  into a since-rebase claim.
- No new fills today (pre-committed no-trade day, per premarket/market_open notes). Weekly
  trade count unchanged: **1/5**. Satellites unchanged: **2/4** (OMER, ETON).
- Next entry day: **Thu 8/20**, post-FOMC-minutes, on a fresh board.

## 2026-08-18 — MARKET OPEN (Tuesday, Week 34 day 2)

**No trade — pre-commitment held. Both satellites confirmed healthy at the open.**

- ✅ **OMER open-check**: $17.16, essentially flat, 22.1% short float, no new EDGAR filings
  since premarket. $0.79 clear of the ~$16.37 stop. Volume light (0.0x avg by open) — normal
  for a name with no fresh catalyst today.
- ✅ **ETON open-check**: $61.59, **+4.6% on the day**, above Monday's $61.67 close read at the
  premarket check. Comfortably above the $58.47 trailing-stop trigger. No EDGAR filings.
- 🚫 **NO NEW SATELLITE — held the pre-commitment.** Fresh-mover scan surfaced **WEAV** (+31.9%,
  123.6x RelVol, $584M cap, healthcare) — not yet screened, but entering a third satellite
  ahead of Wednesday's 2:00 PM FOMC minutes was explicitly ruled out in writing at premarket
  (slot budget already spent on ETON Monday). Not chasing a fresh name against a same-day
  written pre-commitment — lesson 6 exists for exactly this. **Worth a one-search catalyst
  check premarket Wednesday if still elevated**, alongside the standing XOS/DUOT/AGPU/OABI/CAPR
  skips (all re-confirmed on the scan, no new evidence to revisit any of them).
- ➖ **Unusual volume / top movers scan**: nothing else new or actionable. Rest of the list is
  either already-killed names or sub-1x RelVol movers with no catalyst (lesson 1).
- 💵 **Bull sold CRM overnight/premarket** (not a Rocket position) — shared cash rose
  $667.77 → $1,249.80. No action needed on Rocket's side.
- Rocket satellites unchanged: **2/4** (OMER, ETON). Weekly trade count: **1/5**. Next entry
  day remains **Thu 8/20**, post-FOMC-minutes, on a fresh board.

## 2026-08-18 — PREMARKET (Tuesday, Week 34 day 2)

**No new satellite today — pre-committed AND the board is independently empty. Two open
positions both held their gates. Next entry day is Thu 8/20.**

- 🚨 **NO TRADE TODAY, for two independent reasons that agree.** (1) The Mon/Tue satellite slot
  was **spent on ETON Monday**; Rocket already carries **two** satellites into Wednesday's
  2:00 PM FOMC minutes against a standing call of **one**. (2) Every fresh name failed a hard
  gate. **Lesson 6 exists because Rocket once entered a name simply because a slot looked open
  — this is the opposite of that, and it was pre-committed in writing before the tape opened.**
- ❌ **OABI DROPPED — the rule-4 gate fired and Monday's deferral is now measurable.** Required
  ≥50% close-in-range; **closed at 18%** (O $4.18 H $4.29 L $3.71 **C $3.82**, 18.1M sh). It
  opened at its high and gave the entire Lilly gap back intraday. **A day-1 entry near the
  $4.47 premarket would be −14.5%.** The catalyst was real, the ladder uncapped, rule 13 a
  non-issue — **best-structured idea in a month, and it still died on day one.** Same-day
  entries stay 0-for-3. Not deferred to Thu/Fri; **dropped**, because the day-2 case was
  conditional on Monday's close and the condition failed.
- ❌ **AGPU KILLED on rule 8 — and it had the best price action on the tape.** +28.4%, **closed
  at 92% of range** on 6.4x volume, **8.5M float**, uncapped on rule 13, passes every universe
  gate. Real catalyst (>$1.3B AI-infrastructure contracts). **EDGAR killed it anyway: S-3
  EFFECTIVE 7/27, 424B3 in use 7/29, 424B5 drawn 5/15 — and $21.9M of cash with equity
  *falling* $40.3M→$34.0M against $1.3B of announced contracts (~60x).** Delivering the
  catalyst *requires* massive dilution and the shelf is already live. SIC code is **"Finance
  Services," not technology.** Lesson 7 in its purest form.
- ❌ **DUOT KILLED twice.** It filed an **NT 10-Q — a LATE FILING notice — on 8/17, the same day
  as its $500M contract PR.** Plus 424B5 drawn 6/17, and **$2.7M quarterly revenue against a
  $500M contract** requiring a 55 MW build. 🚩 **AGPU and DUOT are a circular pair** — AGPU pays
  DUOT to host while contemplating minority equity in the DUOT SPEs it is paying.
- ❌ **XOS dropped on universe gates in one search.** +98.2% at 101x RelVol, the day's biggest
  mover — but **$2.09 close (<$3) and $30M cap (<$50M)**, 7.4M float, and its Q2 print on 8/13
  was followed by **−18.6% on 8/14**, so earnings are not the catalyst. Rule 10 pump profile.
- ✅ **OMER HOLD — and a near-miss on the exit trigger worth recording.** A headline framed
  OMER's **8/13 S-8** as a "$142.67M ESOP-related shelf." **An S-8 is an employee-plan
  registration, not a capital raise; the $150M ATM is still undrawn (no 424B5).** The trigger
  did not fire and should not have. Closed Monday at **73% of range**; premarket $17.01, $0.64
  clear of the ~$16.37 stop. Wainwright reiterated Buy **$33**. ⚠️ Carry forward: a **144 (8/13)
  and a Form 4 (8/17)** — insider intent unresolved after a +27% run.
- ✅ **ETON HOLD.** Closed Monday at **81% of range** ($61.67), premarket $60.96, +0.5% on the
  position. **EDGAR still shows no S-3/424B5/S-1 at all.** Stop trails from the $62.87 HWM →
  ≈$58.47. ⚠️ Monday's intraday range was **10.5% of price** — wider than the 2% opening base
  implied; the 7% trail is nearer the noise band than it looked (lesson 4b).
- 🔢 **Book correction — the raw IWM qty is 6.1976 sh**, matching the hand-built chain exactly
  (7.8479 − 1.6503). **Monday's `market_close` note recorded "≈6.3497 sh" — an arithmetic
  error of 0.152 sh (~$46).** Lesson 24 warns that the *display* rounds; this time the *note*
  was wrong. Book **$3,135.79** (IWM $1,878.93 + OMER $459.27 + ETON $426.72 + cash $370.87);
  slice reads $3,144.14 and is ignored per lesson 23a. Satellites **2/4**, weekly **1/5**.
- 💵 **Cash is 11.8% — just above the 10% buffer.** IWM sits **$57.29 under** target_core
  ($1,936.22), fractionally inside the 3% band ($58.09). **Flagged for `market_close`, not
  acted on** — rebalancing is a close-only action.
- ⚠️ **Macro: VIX jumped +11.79% to 15.93** (second straight rise, still 6 pts under the 22
  brake). **10-yr unchanged at 4.70%, still only 5bp from the 4.75% trigger.** 🟢 **The
  "Russell red while S&P green" flag has REVERSED** — Russell fut −0.22% vs S&P −0.48% vs
  **Nasdaq −1.20%**: a tech-led selloff with small caps the best leg. One session, not a trend.
- ✅ **Today's calendar is clean** — permits/starts/import prices 8:30, industrial production
  9:15, all pre-open. **Wednesday's 2:00 PM minutes are the week's only intraday risk.**

## 2026-08-17 — PREMARKET (Monday, Week 34 day 1)

**Board: ETON P1 today, OABI P2 tomorrow, and only ONE of them gets taken.**

- ✅ **OMER weekend gap check passed** — premarket $17.00, −1.11%, $0.63 clear of the ~$16.37
  stop. No offering/ATM news overnight; standing exit trigger unfired. **Hold.**
- ✅ **ETON cleared Friday's binding gate.** The ladder was re-struck on **dated post-print**
  data: consensus **$71** (was a stale $62.33 struck at a $41.58 price), after H.C. Wainwright
  $65→$70 on 8/14 and Craig-Hallum $62→$76 on 8/13. Friday's condition was "GO only if
  consensus clears ~$68" — it does. Rule 8 cleared on **hard EDGAR evidence**: no S-3, no
  424B5, no S-1 on file at all, plus operating CF +$15.1M and FCF +$3.3M.
- 🚨 **ETON's real no-chase ceiling is $60.80, not the rule-3 $64.75.** Rule 13 binds first
  (28.6M sh → $2B at $69.93), so entry must be ≤$60.80 for even the **+15%** target to clear
  the lid. Premarket $59.33 is inside by 2.5%. **Above $60.80 the name is untradeable.**
  Plan: 7 sh ≈ $415 (13.2%), stop $55.18, **sell 4 at $68.23 (+15%), trail 3 — no +25% limit**,
  because $74.16 fails both the ladder ($71) and the ceiling ($2.12B). A one-rung name.
- 🥈 **OABI is the best-shaped idea on the board and is deliberately NOT being traded today.**
  Eli Lilly licence signed 6:01 AM (**up to $370M milestones + royalties**) with a hard cash
  guidance raise to $49–53M from $37–41M. **Ladder wide open** (consensus $7.33 vs a $5.59
  +25% target) and **rule 13 is a non-issue** ($813M against a $2B lid) — the first uncapped
  name in a month. But premarket printed **+45.6%** on a **31%-of-price range**, so rule 2c
  and rule 2a both say day-2. **Entry is Tuesday**, conditional on today's close ≥50% of range.
- 🚫 **Explicitly pre-committed (rule 6): OABI is NOT the fallback if ETON fails at 9:45.**
  A failed P1 means no satellite. This is the exact error that produced FF.
- 🚩 **Slot budget resolved up front: Mon and Tue share ONE new satellite**, since OMER already
  fills the "one satellite into Wednesday" call. Runner-up defers to Thu/Fri.
- 🔴 **Calendar correction: Jackson Hole is Aug 27–29, not this Friday.** Friday's Week-34
  table had it wrong. Week 34's only scheduled risk is **Wed 2:00 PM FOMC minutes**; Thu and
  Fri are clean, which is what makes the deferral above cheap.
- ⚠️ **Macro deteriorated over the weekend without triggering anything.** VIX 14.98 (no brake),
  but **10-yr 4.70% is 5bp from the 4.75% trigger** (was 11bp), Brent round-tripped to $89.51,
  gold +1.62%, and **Russell futures are red while S&P futures are green** for a second
  session. Nothing blocks a trade; it argues against taking two.
- ➖ **The scanners were empty of catalysts** — best top-mover +6.5% on 0.9x RelVol, 16 of 20
  under 0.5x. OABI (39.6x) was the only real event on the tape. UMAC dropped (−3.5% premarket,
  confirming the "most-chased name in a sector policy move" read).
- **Book carried at Friday's hand-built $3,152.16** per lesson 23a; the slice reads $3,165.91
  and is ignored. Satellites 1/4, weekly count 0/5.

## 2026-08-17 — MARKET OPEN (Monday, Week 34 day 1)

**ETON bought. Slot budget resolved — OABI now firmly deferred to Thu/Fri.**

- ✅ **ETON filled 7 sh @ $60.65 at 9:47 AM ET**, inside the $60.80 no-chase ceiling by $0.15.
  Opening range held inside ~2% of price from premarket $59.33 through the 9:45–9:50 base,
  no whipsaw, volume pace ~6x normal by 9:45 (153k of a 643k ADV in the first 15 min).
  Stop set immediately: 7% trailing, initial trigger $56.24. Full writeup in `trade_log.md`.
- ✅ **OMER unchanged overnight** — no stop trigger, no fills. Still holding per premarket plan.
- ✅ **OABI confirmed fading as predicted** — premarket peaked +45.6%, now +18.2% at 9:48 AM
  (169.9x RelVol). Validates the day-1 whipsaw read; stays parked for Thu/Fri, not Tuesday —
  the Mon/Tue slot is now spent on ETON.
- ➖ Fresh-mover scan turned up AGPU (+10.3%, 22.9x) and DUOT (+9.3%, 9.0x), neither with a
  catalyst check run yet. No capacity today (slot spent); worth a one-search look pre-market
  tomorrow if still elevated.
- Rocket satellites after this trade: **2/4** (OMER, ETON). Weekly trade count: **1/5**.

---

## 2026-08-17 — MARKET CLOSE (Monday, Week 34 day 1)

**Both satellites held overnight. Core rebalanced down after ETON entry pushed IWM 15.9% over target.**

- ✅ **ETON held** — up +1.7% on its first day ($60.65→$61.71), clean opening base with no
  afternoon fade, one-rung stop at $56.24 untouched. Catalyst (beat-and-raise, dated ladder
  re-strike) is a multi-day story, not a one-day pop — holds overnight per the multi-day
  catalyst rule.
- ✅ **OMER held** — up on the day ($17.19→$17.36, +0.99%), stop untouched, NTAP reimbursement
  catalyst (effective 10/1) still unplayed. No offering/dilution news. Multi-day thesis intact.
- ✅ **Core rebalance executed** — sold 1.6503 sh IWM @ $304.04 ($501.68), pulling IWM from
  $2,431.04 (8 sh, 15.9% over target_core) down to ≈$1,930 (within $0.82 of target). Full
  math in trade_log.md. This was the only satellite-funding gap left over from this morning's
  ETON buy, which was paid straight from cash rather than a same-session IWM sale.
- 📊 **Today, price-only**: OMER +$4.59, IWM −$8.40 (8 sh × Fri $305.09 → today $304.04),
  ETON +$7.35 (first-day mark) ≈ **+$3.54 net (~+0.11% of slice)** — flat day. SPY −0.47%
  today, so Rocket's book beat the tape today, mostly on ETON's clean first session with OMER
  also positive while IWM gave back less than SPY.
- ⚠️ **Slice-vs-book caveat stands (lesson 23a)**: `portfolio_state.md`'s +3.70%/−0.43% vs
  SPY since-rebase figures are the contaminated slice, not the hand-built book. Did not
  reconstruct the hand-built book this session (that reconciliation is premarket/weekly_review
  work); flagging so it isn't mistaken for validated attribution.
- Rocket satellites unchanged: **2/4** (OMER, ETON). Weekly trade count: **1/5**.

## 2026-08-14 — WEEKLY REVIEW (Week 33, Friday post-close)

**Grade C−. Rocket beat SPY by +0.15% and every basis point of it was IWM beta. Real alpha
−0.52% — the worst satellite week since the core sleeve existed.** Full write-up in
`weekly_reviews/2026-W33.md`.

- **Book $3,135.02 → $3,152.16 (+0.55%)** vs SPY +0.40%, IWM +1.17%. Attribution: factor
  **+0.70%**, cash drag **−0.04%**, satellite **−0.52%**.
- **3 satellites opened (FF, VELO, OMER), 2 closed, 0 winners.** Realized −$17.64, avg
  **−0.25R**. Under the core/satellite regime Rocket is now **0-for-3 all-time**.
- ✅ **Week 32's problem is genuinely fixed** — three fractional rebalances all landed within
  $0.20 of target; cash drag −0.49% → **−0.04%**.
- 🔴 **Since-rebase truth: Rocket +3.84% vs SPY +4.62% = −0.78%.** The snapshot says +0.10%
  — **88bp of flattery, up from 67bp.** New **lesson 23a**: the daily notes drifted back onto
  the contaminated slice all week; the hand-built *book* is the only valid daily base.
- 🥇 **The finding of the week: same-day entries are 0-for-3, second-day are 2-for-2.** Both
  same-day losses bought the retrace of a failed opening spike and called it a base.
- **Rules shipped**: beat-without-raise is now a **disqualifier**; **P2 is not a substitute
  for a failed P1**; an **un-runnable filter is a FAIL**; new **opening-range gate** (>10%
  9:30–9:45 range → defer to day 2); the 9:45–9:50 bar must close in its upper half.
- **Ranked by cost**: the 8/13 OMER miss (**≈−0.70%**, infrastructure) > FF (−0.39%,
  discipline) > VELO (−0.17%, timing). **None of it was bad analysis** — 4/4 skips were
  validated (CURI −11%) and the ladder filter is 4-for-4. Do not loosen the research bar.
- **Week 34 board**: ETON P1 (day-2 continuation, 87.6% close — gated on a *dated* post-print
  ladder re-strike; currently reads capped), UMAC P2 (drone-tariff sector move), BW watch
  (ceiling cleared, dilution check is the gate). **OMER held over the weekend.**
- ⚠️ **Escalated to the user**: the $2B ceiling has killed or one-rung-capped five names in
  two weeks (APPS, BW, HLIT, ETON, UMAC). Not overridden.

---

## 2026-08-14 — MARKET CLOSE (Friday, Week 33)

**OMER held overnight — closed 60% of today's range, thesis intact.** Day-2 entry $17.14,
closed $17.19 (+0.3%). Raw 5-min bars: today's range $16.54–$17.61, last print $17.18 →
59.8% of range, above the midpoint (lesson 4 tiebreaker — this is the QNST/RCEL/CRSR
pattern, not the ASPN/EVH bottom-quartile one). Volume faded hard from yesterday's 13.4M
to ~3.2M today (expected day-2 cooldown, not a red flag on its own given the range close).
Catalyst (NTAP reimbursement effective 10/01) is multi-day and unplayed — no reason to
exit early. Known, accepted risk: Friday fill = weekend gap with no stop protection,
flagged at entry, not new information. **Hold.**

**Core rebalance — SELL, band breached.** OMER's entry (funded partly by an IWM sale)
plus the day's drift left IWM at $2,720.61, 10.3% of slice over `target_core` — well
outside the 3% band. Sold 1.073 sh IWM @ $304.96 ($327.22), landing IWM at $2,393.57 vs a
$2,393.39 target (within $0.18, no granularity remainder — lesson 18 holding). Logged as
CORE REBALANCE, not a conviction trade.

**Day P&L**: IWM +$13.24 intraday (realized + unrealized) + OMER +$1.35 (day-1) ≈ **+$14.59,
+0.46% of slice**, vs SPY **−0.22%** today → Rocket beat SPY by **+0.68% today**, on IWM
positive divergence (small-cap factor up while SPY was down) plus OMER holding flat-to-up.
Since rebase (7/20, script-verified): Rocket +4.76%, SPY +4.61%, Rocket vs SPY **+0.15%**.

**Weekly trade count (hand count, lesson 25): still 3/5** — FF (8/11), VELO (8/12), OMER
(8/14). The IWM rebalance is not a new position and does not count against the cap.

---

## 2026-08-14 — MARKET OPEN (Friday, Week 33)

**TRADE PLACED — OMER, 27 sh @ $17.14. Lesson 24 closed out clean: the GO/NO-GO was made
and logged explicitly at 9:45 AM, not deferred to a monitor.** 9:40–9:45 raw 5-min bar (O
$17.02 / H $17.38 / L $16.92 / C $17.33 on 58,327 sh, ~1.6x avg 5-min volume) held cleanly
above the $16.85 GO threshold and never touched Thursday's $16.27 low — confirmed GO. Filled
$17.14, stop $15.84 (7% trail), 14.6% of slice. Funded by selling 0.5822 sh IWM (core stayed
IWM-only, no pooled-cash draw) rather than the higher, easier route of just using the $549
pooled cash sitting free — kept Rocket's own core/satellite book clean instead. CURI (P2) was
correctly passed — it was the explicit alternate, not a second position, and OMER hit GO.

**Step 4 scan found two new names, both correctly passed.** ETON: real beat-and-raise
(revenue +99%, EBITDA margin 43% from 16%, guidance raised to $145M+, PT raised to $65) but
**+37.6% intraday — a >35% gap, second-day only per rule 2.** Added to watchlist for Monday
8/17; re-verify the $2B cap clearance at a ~$70 second-day entry before sizing. NMAX: Q2 EPS
beat but **guidance reiterated, not raised** — beat-without-raise, the exact pattern that
stopped out FF — plus thin, undated 2-analyst coverage. Passed, not researched further.

**Weekly trade count (by hand, lesson 25 — script still misreports): FF (8/11), VELO (8/12),
OMER (8/14) = 3/5.** Two slots remain this week.

---

## 2026-08-14 — PREMARKET (Friday, Week 33)

**No trades — market closed. Today's board is carry-overs, not new names, and that is the
honest read: the earnings pipeline is spent.** 6 web searches, all inline, no subagent
(lesson 20).

**🥇 OMER — P1, HIGH. Same trade as yesterday, one day later, and it is fading premarket.**
Thursday's catalyst work stands unchanged (125% revenue beat, +190% QoQ product ramp, swing
to profit, NTAP effective 10/01) — it is on the board today only because **lesson 24**: the
monitor died, no midday exists, and it ran untraded. Raw bars: **O $16.65 H $18.14 L $16.27
C $17.35 on 13.4M sh (6.4x ADV), closing at 58% of range** — above the midpoint, so the
second-day rule is live, but it gave back 43% of the intraday range and that is not QNST's
90% conviction close. **Premarket $16.92, −2.5% — which makes the entry better, not worse**,
pulling it back toward Thursday's planned $16.39 instead of forcing a chase through $18.14.
Ladder re-struck at $17.00: **+15% $19.55 / +25% $21.25 vs a LOWEST analyst reading of
$33.00 — uncapped by ~55%** (lesson 11d). Short float 19.7–24.2% ✓. Dilution re-checked:
**no offering announced 8/13–8/14**, the named trigger has not fired; ~$132M cash, buyback
live, $150M ATM still undrawn. Cap at target two **$1,538M**, clears the lid by 23%.
**Entry 9:45–9:50: GO above $16.85 on >0.75x 5-min volume; NO-GO below $16.27; never chase
above $18.14.** Stop **$15.81** (below Thursday's entire range). **28 sh = $476.00 (14.9%)**,
funded by selling **~0.565 sh of IWM**. ⚠️ Honest marks against it: the entry is 3.4% worse
than yesterday's, the $17.65–$18.14 band now sits between entry and target one, and a Friday
fill is a weekend hold on a single-product biotech.

**🚨 The binding rule today is lesson 24, not a market rule.** `market_open` must log an
explicit **GO or NO-GO with the observed 9:45–9:50 bar**. No monitor deferral. Two
consecutive sessions of this flaw would cost the same trade twice.

**🥈 CURI — P2, MEDIUM, and the ALTERNATE not a second position.** It passed the exact gate
set for it Thursday: closed **$3.99 at 57% of range** on 20.3M shares, above the midpoint,
and now **clears the $3 price gate on its own close** rather than only on the gap. Real
beat-and-raise (licensing +48% to $14.1M, GM 53%→73%, net income $8.9M, outlook raised).
Dilution clean and the good kind — **no debt, dividend + buyback**. ⚠️ Two real knocks:
**the ladder is half-capped** — a *fresh, dated, post-print* analyst **CUT to $5.00 from
$5.50 citing "lumpy" licensing**, so +15% ($4.66) clears but **+25% ($5.06) sits on top of
the lowest target**; and **$10.9M cash against a ~$20M/yr dividend** is the mechanism that
turns a licensing miss into dilution. Short interest only 4.3%, falling — no squeeze leg.
**OMER and CURI are the same structural trade** (day-2 continuation on a post-earnings gap
that closed mid-range), so taking both is one correlated bet at double size into an
unresolved 10:00 print. **Take CURI only if OMER hits its $16.27 no-go.**

**Dropped, with the two worth naming.** **CAPR** was the biggest thing on the tape (+98% →
$8.34, 60x RelVol, now $8.70) on the FDA signalling it will accept an amended deramiocel
application — and it is a **hard no on three independent grounds**: a >35% gap is
second-day-only (rule 2); **the PDUFA is 8/22, inside a 1–5 day hold, after a 9–3 AdCom vote
against efficacy** — a coin flip no stop protects through a halt; and a doubled clinical-stage
biotech with securities-fraud class actions will raise into the strength. **Rocket trades
continuation, not binaries.** **IMXI** (+25%, 11.9x) is real news — NYDFS cleared the Western
Union deal — but it is **all-cash at $16.00/share**, so **Rocket's +15% target ($16.82) sits
above the deal consideration**: the capped-ladder logic in its purest form, where the "target"
is a contract. Added to the merger-arb skip list beside HZO. Also resolved cleanly: **MGNX /
IPWR / INV / SPRY** all printed 8/13 and **all four failed the day-one range check** (25% /
**11%** — IPWR round-tripped $4.76→$5.25→$4.26 / 36% / didn't move) — the earnings-week bar
saved the work and the range check finished them. **VOGX** has the board's best float (3.4M,
24%) but is a two-day-old listing whose "382,500 ADV" is computed off a two-day sample while
**Thursday's real volume was 81,000** — lesson 13 in reverse, the gate reads PASS off bad
data. Sixteen more names moved +2.5–5.8% on 0.0–0.6x RelVol with no catalyst (lesson 1).

**Macro — both of the week's big prints are spent, benignly, but today's structure is the
week's worst.** **PPI resolved without a search**: the **10-yr rallied 4bp to 4.64%** and VIX
fell to 14.57 — a hot producer print does not produce a bond rally, so the "no new satellite"
brake never fired. The 4.75% trigger is now **11bp away, the widest cushion of the week**,
after being tested twice. 🚨 **But UMich prelim lands 10:00 ET — AFTER the open**, ~10 minutes
past the entry window, and it is the first entry this week placed into an unresolved print
(forecast 54.1 vs 55.2; the 4.2%/3.3% inflation-expectation legs matter more than the
headline). **Do not widen the stop for it; do have the stop working by 10:00.** ⚠️ Also
logged honestly: **SPY beat IWM by 0.44% Thursday**, ending the two-session small-cap streak,
and Russell futures are **−0.01%** against green S&P/Nasdaq — the "Russell red" trigger is
**grazing for the first time but not fired**. Mon–Thu the factor bet ran −0.52% → +0.66% →
+0.32% → −0.44%, about a wash. **Booked as beta in both directions, not skill** — the same
discipline applied to Wednesday's outperformance applies to Thursday's drag.

---

## 2026-08-13 — MARKET CLOSE (Thursday, Week 33)

**No trades. 0 satellites, core (IWM) within band — but the real story is OMER never
got evaluated.** Premarket flagged OMER (P1, HIGH — 125% revenue beat, uncapped
ladder ~2x, 19.7–24.2% short float) as the best-constructed setup Rocket has
screened. The 07:45 market_open log shows it set up a monitor to wait for the
9:45–9:50 base and then... nothing — no midday log (dead since 6/15, lesson 21), no
follow-up decision anywhere, no trade. **New lesson 24: this is an infra failure, not
a discretionary skip** — every prior "no trade" session logged an explicit reason at
decision time; today just went silent. OMER closed the gap further to **$17.35**
(+5.9% over the $16.39 premarket read that framed the entry, would already be
approaching the +15% target at $18.85 had it been entered). Per the spirit of the
missed-catalyst rule, **check OMER again tomorrow premarket** for a pullback or
continuation entry if the thesis (dilution structure, ladder) still holds.

**Position review**: 0 satellites open — nothing to hold/close.

**Core rebalance check**: slice $3,188.02 (live portfolio_value $10,626.74 × 30%),
satellite value $0, 10% buffer $318.80 → target_core $2,869.22. IWM (raw qty
**9.5031 sh**, per lesson 23) × $303.54 = **$2,884.57 — 0.50% of slice over target,
well within the 3% band.** No trade.

**Day P&L (hand-built, per lesson 22 — snapshot table mixes in Bull's P&L)**: no
satellite trades, IWM intraday unrealized **+$7.89 (+0.25% of slice)** vs **SPY
+0.69%** today — Rocket underperformed SPY today by ~0.44%, small-cap factor drag,
not a stock-picking loss (no picks were made). Since rebase (7/20): SPY **+4.82%**
(script-verified). Rocket hand-built, chained from 8/12's ~+4.65% base compounded
with today's core return: **≈+4.91%** → Rocket vs SPY **≈+0.09%** since rebase. Flag
per lesson 22: this chained figure carries rounding drift session to session: treat
as directional, reconcile precisely at the next weekly review.

**Also found**: lesson 25 — the weekly trade counter (`portfolio_snapshot.py`) shows
"0 / 3 max" despite VELO trading this week; the `—` split-count bug undercounts to
zero and the hardcoded cap (3) doesn't match CLAUDE.md's real 5/week guardrail.
Flagged, not fixed (script change out of scope for market_close).

---


## 2026-08-20 — PREMARKET (Thursday, Week 34 day 4 — post-minutes, the pre-committed entry day)

**No new satellite — but a *researched* decline, not an empty board. Both carried insider
threads resolved, in opposite directions. ETON downgraded on a CEO sale; OMER's stop is now
above entry.**

- 🚫 **NO ENTRY.** Today was the day the week was built around, and the board did not cooperate:
  🆕 **the entire top tier of the tape is ONE theme — crypto-treasury proxies** (DFDV, HYPD,
  USDE, SBET, ASST, ABTC, FWDI, BKKT, SECZ). **Excluded on mandate**, not judgment: CLAUDE.md
  forbids crypto, their catalyst is "a token went up," and they are **ATM-financed by
  construction** — issuing stock to buy tokens *is* the model, so rule 8 applies by design.
  DFDV closed at **93% of range on 3.5x volume**, the best bar on the tape, and is still a hard
  skip → **new lesson 31.** Second time in three sessions the prettiest action was
  structurally uninvestable. **Default: hold IWM core + both satellites, ~100% invested, no
  rebalance until `market_close`** (core $54 / **1.7%** short — inside the 3% band).
- ❌ **ARCT SKIPPED — killed by the EVENT CALENDAR, a first.** The only name with a real volume
  event (**+25.2% on 5.63M vs ~0.5M ADV ≈11x**), and it **passed everything that normally
  kills**: uncapped dated ladder (**$18.29–$23.30 consensus, Canaccord $20** vs $10.28), rule
  13 irrelevant ($288M cap), and the **best balance sheet screened to date — $191.5M cash
  against a $288M market cap, runway to YE2028, S-3 undrawn** (the *inverse* of AGPU/DUOT).
  **Skipped anyway**: (1) 🚨 **rule 1 — the catalyst doesn't exist.** The move resolves to a
  Canaccord PT **CUT** ($21→$20) + a **conference fireside chat** + recirculated Aug-6 news;
  (2) 🚨 **the CAPR rule — ARCT-810 Phase 2 data is guided "later in Q3 2026," undated**, i.e.
  inside a 1–5 day hold, **and a 7% stop cannot protect against a data gap.** → **new lesson
  29: screen the calendar as its own gate.** Re-screen only once the readout is a fact.
- ✅ **OMER insider thread CLOSED — BENIGN, stop citing it.** Carried 4 sessions, resolved by
  opening the filings: 8/18 Form 4 = **code A, a GRANT** of 30k options to a director; 8/17
  Form 4 = **code M+S, a cashless exercise-and-sell** (5,000 @ $3.93 → $16.95, **~$85k against
  a 13.4M-share day**); Form 3 = a new insider's initial statement. Compensation mechanics.
- 🎉 **OMER — the stop is now ABOVE the entry.** 8/19: **+7.0% at 72% of range on 3.20M**,
  volume *expanded* 2.6x. Live stop verified **HWM $18.86 → $17.5398 vs $17.14 entry — the
  trade can no longer lose money** (worst case **+$10.79**). 🚨 **+15% rung is $19.71 and 8/19's
  high was $18.89 — within 4.3%. SELL 9 SHARES ON THE TOUCH.** MRLN round-tripped unscaled.
  ✅ No 424B5 → ATM undrawn, exit trigger has not fired.
- 🚨 **ETON — the founder is selling. Outlook downgraded, position held.** 🆕 **Form 144 filed
  8/19: CEO Sean Brynjelsen, 100,000 sh / $6,343,000**, sale date 8/19 — **16% of that day's
  610k volume.** ⚠️ **This falsifies yesterday's `market_close` conclusion**, which searched for
  a cause of the reversal (H $63.83 → **C $61.48 at 38% of range**), found none, and called it
  "an ordinary FOMC-day pullback." There *was* a seller. ✅ **But a 144 is NOT dilution** —
  secondary sale, shares out unchanged at 28,583,135, cap math and balance sheet untouched;
  **still no S-3/424B5/S-1 on file, dilution profile still the cleanest screened.** It is
  **supply overhang** → **honor the rung: sell 4 sh at $68.23.** Still a one-rung name. Stop
  cushion narrowed to **3.1%** ($59.3619), sitting **$1.29 below entry.** → **new lesson 30.**
- ✅ **10-yr resolved the right way: 4.71% → 4.65%**, widening the cushion to the 4.75% trigger
  from **4bp to 10bp**. VIX **15.20**, no brake. 🚨 **Brent $93.90 (+2.49%), fourth straight
  advance and accelerating — +4.9% in four sessions. Watch $95.** Gold $4,546 also making
  highs; yields falling — an inflation-tinged backdrop.
- ✅ **Lesson 28 vindicated one session after being written**: IWM +0.50% vs SPY +0.21% (+29bp)
  right after −58bp — **six sign changes in seven sessions.** Not booked, correctly.
- 🗓️ **Calendar clean for the entry window**: 8:30 AM claims + Philly Fed (pre-open), 10:00 AM
  Leading Indicators (minor). 🔧 **Correction: existing home sales is 8/25, not today.**
  **Jackson Hole Aug 27–29 (Week 35) is the next real event.** Earnings pipeline still empty —
  four straight sessions; nearest are **QMLS 8/25, LTRX 8/26** (carry LTRX forward).
- Book **$3,167.90** (hand-built, lesson 23a). Satellites **2/4**, weekly count **1/5**.

## 2026-08-20 — MARKET OPEN (Thursday, Week 34 day 4 — post-minutes, the pre-committed entry day)

**No trade — premarket's "no new satellite" call held. Clean overnight, one new name
checked and correctly passed.**

- ✅ **Snapshot confirms no surprises**: ETON 7 sh unchanged ($60.65→$60.87), OMER 27 sh
  unchanged ($17.14→$18.48), IWM 6 sh core unchanged, all five trailing stops still live
  (ETON, OMER, plus Bull's JPM/NOW/SCHW). Cash flat at $482.34. Nothing broke overnight.
- 🚫 **NO NEW SATELLITE — held the premarket call.** The top-tier tape was still the
  crypto-treasury theme (DFDV, USDE, BKKT, ABTC, SBET, FWDI, SECZ, plus **two new names
  in the same bucket**: PURR/Hyperliquid Strategies, GEMI/Gemini Space Station, BTGO/BitGo
  Holdings) — all excluded on mandate per lesson 31, none re-screened.
- ⚠️ **Fresh-mover scan surfaced PSNL** (Personalis, healthcare, $1.77B cap) — not on the
  premarket board, only genuinely new name outside the crypto theme and the existing kill
  list. One inline search + scanner detail killed it on three independent grounds: (1) real
  volume today is **0.9x avg**, not the 7.3x the premarket-timestamped scan showed — no
  confirmation; (2) the catalyst is **16-day-old Q2 earnings (8/4)**, already priced in via
  a +9.85% 7-day pop right after the print — stale, not fresh; (3) **analyst target
  ($13.875) sits BELOW the current price ($16.57)** — an inverted ladder, worse than merely
  capped, a hard fail on rule 11. Also flagged: insiders sold $7.1M in the last 3 months
  against widening losses (Q2 net loss $31.68M vs $17.20M revenue). Not traded.
- ➖ Rest of both scans: ARCT, OABI, QMLS, STI, BNAI, WOLF all re-appear and are already on
  the standing skip list, no new evidence to revisit any of them.
- Rocket satellites unchanged: **2/4** (OMER, ETON). Weekly trade count: **1/5**. Next
  fresh board Fri 8/21 per premarket note.

## 2026-08-20 — MARKET CLOSE (Thursday, Week 34 day 4 — post-minutes, the pre-committed entry day)

**ETON closed on the end-of-day rule; OMER held. Core rebalanced hard after the ETON exit
freed cash. First day-to-day move below zero this week.**

- 🚫 **ETON CLOSED** — 7 sh, $60.65 entry → **$59.78 fill (-1.43%, -$6.09)**. Continued sliding
  from 8/19's $61.48 close, crossed **below entry** for the first time, live trail down to a
  ~0.7% cushion, thesis already downgraded on the CEO's $6.34M Form 144 (lesson 30). Small-cap
  close rule fired cleanly: down on day + below entry + no thesis improvement → close, don't
  wait for the trail. **New lesson 32**: the exit beat where the 7% trail would have triggered.
- ✅ **OMER HELD** — $17.14 entry → $18.63 (+8.7% all-time, +1.3% today), new week high $18.62,
  stop still locked above entry (worst case remains positive). Multi-day beat-and-raise thesis
  intact, volume still constructive. No same-day catalyst, ordinary continuation — holds
  overnight per the multi-day-thesis criterion.
- ✅ **CORE REBALANCE — IWM BUY 1.8546 sh @ $297.53 ($551.79)**. Post-ETON-close core was
  **17.5% of slice short** of target (slice $3,156.19, satellite value $503.28 (OMER only),
  10% buffer $315.62 → target_core $2,337.29 vs live IWM $1,844.13) — outside the 3% band by a
  wide margin, funded from ETON's proceeds plus existing pooled cash headroom, not new cash.
  New IWM qty **8.0522 sh**.
- 📊 **Today (hand-built book, lesson 23a)**: $3,167.90 → **≈$3,137.93 (-0.95%)** vs **SPY
  -0.88%** → **Rocket ≈-0.07% vs SPY today** — small caps (IWM) underperformed SPY intraday,
  consistent with the beta-not-skill framing (core carried the loss, OMER partially offset it).
- 📊 **Since rebase (7/20)**: SPY **+2.79%** (script-verified, `market_data.py spy 2026-07-20`).
  Rocket hand-built ≈**+3.38%** (chained forward from 8/19's non-penny-precise ≈+4.37%,
  itself flagged for reconstruction at next weekly_review) → Rocket vs SPY **≈+0.6%**,
  directional only. `portfolio_state.md` slice reads **+4.04%/+2.79% = +1.25%** — the more
  flattering, contaminated figure per lesson 23; do not cite it as the true number.
- Satellites now **1/4** (OMER only). Weekly trade count unaffected (core rebalance + a
  close, no new entry) — still **1/5**. Next fresh board Fri 8/21 per premarket note.
- ✅ ntfy daily summary sent and confirmed (`Notification sent: [default] ...`).

## 2026-08-19 — MARKET CLOSE (Wednesday, Week 34 day 3 — FOMC MINUTES DAY)

**No trades. Both satellites held overnight — OMER strong, ETON pulled back on no news. Core checked, within band.**

- ✅ **OMER HOLD** — $17.14 entry → **$18.39 (+7.3% on the position)**, day's biggest mover.
  Checked for a same-day catalyst: nothing dated to 8/19 found — CHMP's negative opinion on
  narsoplimab is **stale June 2026 news** (EU-only, doesn't touch the US NTAP thesis) and the
  "profitable Q2" coverage recirculating today is the same 8/13 print already priced in. Read
  this as continued momentum off the beat-and-raise + insider-activity thread, not a fresh
  event. Insider thread (144 8/13, Form 4 8/17, Form 4 + Form 3 8/18) is now due for
  resolution **tomorrow** per the standing note — do not let it run a fourth session unresolved.
- ✅ **ETON HOLD** — $60.65 entry → **$61.48 (+1.4% on the position)**, but **down ~3.1% from
  yesterday's $63.43 close.** Checked for fresh bad news: none found. A search surfaced an
  8-K exhibit link that read as "new" in search results but resolves to the **6/8/2026** filing
  (stale, mis-surfaced by search recency bias, not a new dilution event) — EDGAR dilution
  profile is unchanged (still no S-3/424B5/S-1 on file). Read as ordinary FOMC-day pullback
  on a quiet macro tape, not thesis decay. Position remains above entry, so the close-rule
  ("down on day AND below entry") does not fire. Multi-day beat-and-raise thesis intact — holds.
- ✅ **Core rebalance checked, no action** — slice $3,174.13, satellite value $926.89 (ETON
  $430.36 + OMER $496.53), 10% buffer $317.41 → target_core $1,929.83. Live IWM (6.1976 sh)
  marked at $1,870.37 — short by $59.46, **1.9% of slice**, inside the 3% no-churn band.
- 📊 **Today (hand-built book, lesson 23a)**: $3,139.92 → **$3,168.13 (+0.90%)** vs **SPY
  +0.17%** → **Rocket +0.73% vs SPY today**, driven almost entirely by OMER.
- 📊 **Since rebase (7/20), hand-built book, chained forward from the 8/14 review's
  validated +3.84%/−0.78%)**: **Rocket ≈+4.37% vs SPY +3.60% ≈ +0.77%.** ⚠️ The 8/17 leg of
  this chain uses that session's approximate "+$3.54 net" price-only note rather than a
  reconstructed exact book, so treat the since-rebase figure as directionally right, not
  penny-precise — reconstruct exactly at the next weekly review. `portfolio_state.md`'s slice
  reads **+4.65%/+3.59% = +1.06%** — still the more-flattering, contaminated figure per lesson 23.
- Satellites unchanged **2/4** (OMER, ETON). Weekly trade count **1/5**. No new positions —
  board stays closed until **Thu 8/20**, post-minutes, fresh scan. Carry forward: OMER insider
  thread (resolve Thu), ETON Form 4/144 batch (resolve Thu), ARCT re-check if still elevated.

## 2026-08-19 — PREMARKET (Wednesday, Week 34 day 3 — FOMC MINUTES DAY)

**No new satellite — pre-committed, and the board is empty anyway. Two open threads that had
been deferred for days were both closed out this session.**

- 🚫 **NO ENTRY TODAY, three independent reasons agreeing**: (1) **2:00 PM ET FOMC minutes**,
  the week's only scheduled event, against a standing call of *one* satellite into it — Rocket
  carries two; (2) the board is **independently empty** (top scanner mover is **+5.8%, STI**, a
  permanent skip; nothing else clears +4.6%); (3) the sole deferred candidate resolved to a hard
  skip. **Next entry day remains Thu 8/20.**
- ✅ **WEAV closed out — merger-arb, not momentum.** Yesterday's flag (+31.9%, 123.6x RelVol) is
  a **$7.40/share all-cash take-private by Francisco Partners** ($650M, 34% premium, Q4 close).
  🔎 **The daily bar diagnosed it before the search did**: a **$0.04 range on 49.4M shares**
  cannot happen unless the price is pinned → **new lesson 27.** Passing yesterday cost nothing.
- ✅ **BW closed out — ran the gate instead of deferring a fifth time.** It had been carried
  **four sessions** with rule 8 unrun. **S-3ASR filed 5/21 = an automatic shelf, effective on
  filing with no SEC review** — the fastest takedown vehicle there is → **new lesson 8c**, a
  tier *above* "effective shelf." Its scary-looking **25-NSE (8/13) is benign** (matured 6.50%
  Senior Notes, not the common) → **lesson 8d**. **Dropped**, catalyst 9 days stale.
- ✅ **ETON HOLD — best close of the run.** $63.43, **+4.6% on the position**, at **96% of range**
  (86% → 82% → **96%**), a new closing high on *contracting* volume (2.32M → 1.28M → 0.87M).
  EDGAR clean, still **no shelf of any kind on file.** Stop verified live at the broker:
  **HWM $63.5591 → stop $59.11**, price $4.32 (6.8%) clear. ⚠️ Cap now **$1.81B** — the +15%
  target (~$1.95B) clears the $2B lid only just. **One-rung name; sell 4 sh at $68.23.**
- ✅ **OMER HOLD.** $17.19, +0.3%, second straight **74%-of-range** close on falling volume
  (13.4M → 3.7M → 2.5M → 1.2M) — quiet consolidation, not distribution. Stop verified live:
  **HWM $17.59 → stop $16.3587**, price $0.83 (4.8%) clear. **No 424B5 → ATM still undrawn**,
  exit trigger has NOT fired. ⚠️ Insider thread now **3 sessions old** and grew overnight
  (144 8/13, Form 4 8/17, **Form 4 + Form 3 8/18** — a Form 3 is a *new* insider's initial
  filing, normally an appointment). **Resolve Thursday or stop citing it.**
- 🚨 **Russell-lagging flag reversed BACK ON one session after reversing off** — IWM −1.26% vs
  SPY −0.68%, IWM closing at **4% of its range**. The factor has changed sign **five times in
  six sessions** → **new lesson 28: a one-session factor move carries no information.** Yesterday's
  refusal to book the green session was correct; do not now over-correct into a bearish read.
- 🚨 **10-yr at 4.71% — 4bp from the 4.75% trigger, tightest ever.** VIX 15.88, flat, no brake.
  Brent re-accelerating ($89.51 → $90.91 → **$91.90**). EIA inventories 9:30 AM.
- 🧹 Trimmed `research_log.md` 222 → ~180 lines (archived the OABI/AGPU/DUOT/XOS writeups to
  `archive/research_log_history.md`, kept one line each); archived the superseded Monday macro
  snapshot. Satellites **2/4**, weekly count **1/5**. Book **$3,139.92** (hand-built, lesson 23a).

## 2026-08-19 — MARKET OPEN (Wednesday, Week 34 day 3 — FOMC MINUTES DAY)

**No trade — pre-commitment held. Positions clean, no overnight fills or stops.**

- ✅ **Snapshot confirms no surprises**: ETON $62.56 (+3.1% on position), OMER $17.64 (+2.9%),
  IWM 6 sh core unchanged, all five trailing stops still live (ETON, OMER, plus Bull's
  JPM/NOW/SCHW). Nothing broke overnight.
- 🚫 **NO NEW SATELLITE — held the pre-commitment** written at premarket (2:00 PM ET FOMC
  minutes today; Rocket already carries 2 satellites against a standing 1-into-FOMC call;
  board was independently empty).
- ⚠️ **Fresh-mover scan surfaced ARCT** (+28.6%, 59.3x RelVol, $300M cap, healthcare) — not on
  the premarket board. Two inline searches found only a stale Aug 6 earnings beat and an
  already-priced-in Thermo Fisher collaboration; nothing dated to confirm a same-day catalyst.
  **Not traded — no clean catalyst, and would be a third satellite into FOMC minutes regardless.
  Added to watchlist for a cleaner look tomorrow (missed-catalyst rule) if still elevated.**
- ➖ Rest of unusual_volume/top_movers: FBRX (39.4x RelVol, +0.1% — likely pinned/deal per
  lesson 27, not investigated further), MRVI (+30.9%, $1.95B cap — brushes the Rule 13 lid,
  no catalyst check run), OABI/DUOT/WEAV all re-appear and are already on the skip list. Top
  movers list had nothing above 10x RelVol with a catalyst.
- Rocket satellites unchanged: **2/4** (OMER, ETON). Weekly trade count: **1/5**. Next entry
  day remains **Thu 8/20**, post-minutes, on a fresh board.



---

## Archived 2026-08-28 (W35 weekly review) — sessions 2026-08-21 through 2026-08-27

## 2026-08-27 — MARKET_CLOSE (Thursday, Week 35 day 4) — no trades, core in band

Clean no-op day: 0 satellites open (unchanged since the 8/26 OMER stop-out), no
overnight fills, no stops hit. Core rebalance check: IWM (9.4932 sh, $2,846.44) is
1.07% of slice short of target — inside the 3% band, no trade. Day P&L: IWM
+0.29%/+$8.26 vs SPY +0.66% — Rocket trailed SPY by ~0.37% today, pure factor drag
(small-cap IWM lagging large-cap SPY), no satellites to attribute it to. Full detail
in `trade_log.md`. ntfy daily summary sent and confirmed. Since-rebase figure still
not recomputed daily (lesson 23a) — carries to weekly_review.

**Open thread for tomorrow (Fri 8/28, last session of Week 35)**: Warsh's Jackson
Hole keynote ~10:00 AM ET is the day's dominant event — per premarket's own note, a
7% trail fills at the open wherever the open is, so any fresh entry timed around it
carries that data-gap risk. Watchlist is still empty (LTRX killed, CAPR/ARCT/OI dead
threads) — a fresh scan is the priority, not a nice-to-have, since Rocket closes the
week with zero satellite attempts if nothing changes.

---

## 2026-08-27 — MARKET_OPEN (Thursday, Week 35 day 4) — no trade, confirmed premarket decision

Synced live account: **IWM 9 sh ($2,840), no satellites, no overnight fills or stops**.
Cash $411.48 pooled, unchanged. Weekly satellite count still 0/5.

Ran `unusual_volume` and `top_movers` fresh at the open — board is essentially
unchanged from premarket: **BBW** is down **−19.5% on 15.1x** (the print already hit,
a miss reaction, not a beat — not a candidate). LTRX and OOMA reappear at the same
levels already triple/single-killed in premarket. Everything else new (BNC, XHLD,
METC, REAX, IGR, BETR, SVV, TE) is sub-3x RelVol or <6% change with no named catalyst
(rule 1), or is the same mandate-excluded crypto-treasury tier (DFDV, FWDI, ASST,
HYPD, USDE, SECZ, BKKT — rule 31). No new candidate clears the bar.

**Decision: no trade. Hold 100% IWM core**, consistent with premarket. Nothing to
log to trade_log.md. No notification sent (flat session).

---

## 2026-08-27 — PREMARKET (Thursday, Week 35 day 4) — NO SATELLITE, hold 100% IWM

**Book (hand-built, lesson 23a): $3,138.95** = IWM 9.4932 sh ($2,838.05, 90.4%) +
notional cash $300.90 (9.6%). **Inside the 10% buffer — no bearish thesis required.**
Satellites 0/4 · weekly count 0/5. **Decision: no satellite. This is a calendar
timing call, not a market call.**

- 🚨 **CORRECTED A TWO-SESSION ERROR IN ROCKET'S OWN FILES: the Jackson Hole keynote
  is KEVIN WARSH, not Powell** — and it is **Fri 8/28 ~10:00 AM ET, his first as
  chair.** Both `research_log.md` and `market_context.md` said "Powell" in bold on
  8/25 and 8/26 as the top-cited risk. The risk call survived by luck; it was right
  about the date, wrong about the event. **New lesson 39** — memory files get re-read
  every session and never re-sourced, and the two mechanical-close days that skipped
  research still inherited the claim. Ties to [[launchd-quota-contention]].
- 🚫 **LTRX was the only genuine fresh catalyst and it was TRIPLE-KILLED.** FY26 Q4
  after the 8/26 close, **$5.66 → $6.50 premarket (+14.8%)**. It *passed* the gates
  that usually kill: universe, rule 13 ($290M), **rule 37a (ranges 4.8–6.7%, the 7%
  stop actually fits)**, and **rule 11 uncapped** ($6.50 vs $10.33 mean, low $8.00).
  Died on: **(1) rule 5** — EPS $0.04 vs $0.03 is a *one-cent* beat, revenue +8% YoY
  is not acceleration, and Q1 FY27 guidance **$31–33M midpoints +2.6% QoQ with the
  low end BELOW the quarter just reported** = beat without a raise; **(2) rule 8a** —
  **424B5 takedowns 5/8 and 6/1/2026**, shelf drawn twice this year and still live;
  **(3) calendar** — lesson 2 makes tomorrow's open the earliest valid entry, i.e.
  **30 minutes before Warsh's keynote.** Tell: 8/26 into the print was **−3.4% at 29%
  of range on 2.8x volume.**
- 🆕 **New lesson 8e** from that #2: **LTRX's press release led with "$60 million in
  cash and no debt"** — which is the *proceeds of the two takedowns*. A PR touting
  cash can be advertising the dilution that created it. **Exact inverse of lesson 38**
  (there a blank search hid a *clean* name; here a company hid a *drawn* one).
- ❌ **OOMA killed on rule 11 in one call** — real +25% YoY print, but consensus mean
  $23.00 and **highest target $24.00 vs a +15% rung of $25.10.** Ladder capped below
  the first rung; also within 4% of its 52w high and its 8/21 run already faded.
- ❌ **CRBP** — best accumulation on the board (+14.8% in four sessions, 93/84/93% of
  range, 2.0x volume twice, short float 12.7%) but **rule 1**: the only news is a
  Phase 3 **initiation**, "not yet recruiting" — an undated forward binary (lesson
  29), with August PT **cuts**. Watch, don't trade.
- 🔧 **Lesson 17a held again**: **BKSY scanned +9.4%; its real 8/26 bar was −2.1% at
  20% of range**, mid-slide through −11% in three sessions. SPIR, HDSN, ATOM, AMPG,
  CEPL all falsified the same way. Bars before the board.
- ⚠️ **Crypto-treasury theme is back on top of both screens after ONE red session** —
  yesterday's file called it "stopped topping the scanner." Same one-print error as
  the 8/20 rate stand-down. **3 of 4 names in the overlap tier were unusable
  (lesson 36 board-quality problem is back, not eased).**
- ✅ **Yesterday's "crude has broken down" call half-reversed in one session** (Brent
  $84.84 → $87.28, +2.9%). The written restraint — *note it, don't trade it* — was
  correct. Third consecutive one-session macro read to reverse.
- **Open thread for market_open**: nothing to execute. Re-verify the book is ≥90%
  invested; if IWM has drifted outside the 3% band, that is a `market_close` job.
  **Do not reach into the weak tier to fill a slot — rule 6.**

---

## 2026-08-26 — MARKET_CLOSE (Wednesday, Week 35 day 3) — OMER stopped out, core rebalanced to 100%

**No premarket/market_open ran today** (same launchd quota gap as 8/24–8/25). First
session of the day was this market_close sync, which found OMER already gone from
the broker — the 7% trailing stop had filled intraday at 15:55 UTC, well before
market_close ran.

- **OMER stopped out**: 27 sh, entry $17.14 (8/14) → $18.270741 (7% trail off HWM
  $19.6497). **+$30.53 lifetime (+6.60%)**, but today's mark was −$27.25 — the stop
  won the race against the queued +15% profit rung ($19.71), which the 8/25 high
  ($19.65) never reached. Net: a real winner closed by the mechanism, not by
  judgment — nothing to second-guess here.
- **Core rebalanced to 100%**: satellite sleeve now $0, so bought 1.441 sh IWM
  ($430.75) to bring the core from 13.7%-short to on-target ($2,838, 90% of slice
  deployed, 10% buffer intact). Board is now IWM-only — first time since 8/14 with
  zero satellites open.
- **Full detail in `trade_log.md`** under "2026-08-26 — OMER STOPPED OUT + CORE
  REBALANCE". ntfy daily summary sent and confirmed.
- **Open thread for next premarket**: watchlist is empty. CAPR (volatility gate),
  ARCT (data-gap gate), OI (no catalyst) were all killed this week per the 8/26
  premarket notes below. Need a fresh scan — this is now the top priority, not a
  nice-to-have, since Rocket is carrying zero alpha attempts into Jackson Hole week.

---

## 2026-08-26 — PREMARKET (Wednesday, Week 35 day 3)

**First research session of the week** — no premarket/market_open has run since Fri 8/21.
All three tasks carried for two sessions (CAPR PDUFA outcome, OI catalyst, re-run screeners)
are **resolved and closed** below. **No trade recommended for the open.**

- 🚨 **JACKSON HOLE STARTS TOMORROW (Aug 27–29)** — Powell's keynote lands **inside** any
  1–5 day hold opened today, and a 7% trail fills at the open wherever the open is (lesson
  29's data-gap mechanic applied to a macro event). VIX **15.70** says the tape is not
  braced for it. **Direct argument for carrying the book, not adding to it.**
- ✅ **CAPR — the standing PDUFA question is ANSWERED: there was no decision.** FDA extended
  to **2026-11-22** to review a BLA amendment; the +58% (8/14) and +21.9% (8/25) moves are
  the **analyst reaction** (Oppenheimer PT **$54**, Cantor Overweight **$28 from $3.50**).
  Real, dated, on-list catalyst. It **cleared rules 8, 11, 13, 29** — including a **top-tier
  dilution profile: no S-3/S-3ASR/424B5 anywhere in 2026, $237.9M cash vs a $482M cap.**
  🚫 **Killed on rule 4b**: daily ranges of **18.6% / 26.7% / 35%** make the mandated 7%
  trail a coin flip. 🆕 **First kill this month from INSTRUMENT VOLATILITY rather than
  funding structure or calendar.** Also: **securities fraud class action filed 8/25** (the
  day of the move), a **9–3 negative AdCom** on the record, and eight sessions of chop
  ($6.01–$8.60) — **8/24 opened $8.03 and closed $6.80.** An FDA *extension* is a delay
  being repriced as optionality, not a catalyst delivered.
- ⚠️ **Rule 11b applied deliberately**: the dilution web search came back "could not confirm
  the shelf." **That is a FAIL, not a pass** — so I went to EDGAR directly, verified the
  submissions file was populated (961 filings, 56 in 2026) so a blank result couldn't be a
  broken instrument (lesson 15), and got a genuine clean read. **Search said unknown; EDGAR
  said clean.** Worth repeating: resolve the gap, don't score it.
- ❌ **ARCT — gate holds a FOURTH time. Skip cost now ≈+50%** ($10.28 → $15.44). It has run
  **+88% in five sessions** (5.1x → 2.6x → 2.0x volume, closing 54–98% of range daily) —
  **best price action on the board by a distance.** Re-checked: **no new information**, same
  Aug-6 material, readout still **"Q3 2026," undated**, inside any hold. **Lesson 35 says
  that exact profile — big momentum on zero new information — is a crowded chase and a
  reason for MORE caution.** Carry the cost to the weekly review; do not loosen the gate.
- 🔵 **OMER — both open threads closed, both benign. HOLD.** ✅ **ATM still undrawn — no
  424B5 anywhere in 2026** (EDGAR). ✅ **New Form 144s (8/20 $276,773, 8/21 $203,179)
  resolved BENIGN per lesson 30** — acquired-date = sale-date, paid **cash** = cashless
  exercise-and-sell; **0.90% and 0.41% of their days' volume**, 0.040% of shares out,
  *vs ETON's real one at 16% of a day's volume.* Compensation mechanics, **not an exit
  trigger (lesson 32b).** 🥇 **+15% rung $19.71 is 0.31% away — 8/25 high was $19.65.
  SELL 9 SH ON THE TOUCH; first thing to check at the open.** Volume drying (1.0x → 0.6x
  → 0.5x) but price holding $19.28 — a pause, not distribution.
- ❌ **Board otherwise fails rule 1 (no catalyst)**: **OI** killed after a third session with
  no catalyst *and below-average volume* (0.9x/0.8x) — stop carrying it. **IE** rule-13 kill
  ($1.90B → $2.19B at +15%). **THEO** rule-27 kill — a SPAC pinned in a **$0.01 range**.
  ANRO/ALIT/CPSH no catalyst or dead follow-through. ⚠️ **GNK is the one genuine puzzle —
  2.8x volume three straight sessions, closed 97% of range — but +1.4%/day is drift and
  there is no named catalyst. WATCH.**
- 🔧 **Scanners were a broken instrument (lesson 15).** `unusual_volume` **returned nothing
  above 0.7x RelVol** on a screen built for 3x+, its top name *down* 4.1%; `top_movers`
  printed RelVol as `0.0x`/`—` for **15 of 20** names; **zero overlap between the two**, so
  the routine's first-priority tier was empty. At 04:20 RelVol runs off partial premarket
  volume. **Raw daily bars carried the session** — THEO scanned **+10.8%** against a real
  bar of **−0.1% in a $0.01 range.**
- 🆕 **Crypto-treasury theme went RED after four sessions on top** (USDE −4.1%, DFDV −2.8%).
  Lesson 31 unchanged, but **lesson 36's board-quality problem has eased on its own** — the
  board is no longer crowded out by an untradeable theme, it is **simply thin on catalysts.**
  Different problem, and the distinction matters when grading a no-trade session.
- 🆕 **Macro: the inflation-tinged pattern BROKE, constructively — all three legs at once.**
  **Brent −4.22% to $84.84** (a −9.7% break from $93.96, the biggest move on the board),
  **gold decelerating** (+2.72% → +0.85%), **10-yr −6bp to 4.64%** (cushion to the 4.75%
  trigger widened 5bp → **11bp**). ⚠️ **Per lesson 34 this does NOT stand the rate flag
  down — that is the exact error made 8/20, reversed the next day.** And Jackson Hole is
  the event that will confirm or destroy it. **Note it; act only if it survives Powell.**
  ✅ VIX 15.70, no brake. Futures flat-to-red (Russell −0.11%, no information — lesson 28).
- Book **$3,167.56** (hand-built, lesson 23a) = IWM 8.0522 sh $2,409.46 (76.1%) + OMER
  $520.56 (16.4%) + cash $237.54 (**7.5% — inside the buffer, no bearish thesis needed**).
  **92.5% invested.** Satellites **1/4**, weekly count **0/5**. Core is ~2.4% of slice over
  target, **inside the 3% band — no rebalance, and `market_close` owns that call anyway.**

## 2026-08-26 — MARKET_OPEN (Wednesday, Week 35 day 3)

**No trade.** Premarket already killed everything actionable (CAPR on 4b, ARCT on
lesson 35); nothing new cleared the gate at the open either.

- **OMER $18.98, −1.6%, 0.1x volume (early).** Well off the $19.71 (+15%) rung —
  8/25's $19.65 high wasn't retested. No action; standing order stays live.
- **`unusual_volume`/`top_movers` re-scanned** — no new names. PLAB (+6.5%, 19.1x)
  is the one fresh print but **$1.84B cap → $2.3B at +25%, rule 13 kill**, no
  catalyst identified. ARCT (7.8x), CAPR (2.6x), AGPU, FWDI all already-killed
  names reappearing, not new signal.
- **Positions unchanged from 8/25 close** — no overnight fills, no stops triggered.
  Cash still $348.97 (pooled), satellites 1/4, weekly trades 0/5.
- 🚨 Jackson Hole (Aug 27–29) starts tomorrow — held the book rather than adding,
  per premarket's explicit call.

## 2026-08-25 — MARKET_CLOSE (Tuesday, Week 35 day 2)

**Second quiet day — no trades, no premarket/market_open sessions ran today either.**

- OMER held overnight (27 sh, $19.28, −0.2% today) — +15% rung untouched, catalyst
  multi-day and intact, a pause after five strong closes rather than a breakdown.
  IWM core (8.0522 sh) unchanged, within rebalance band (2.4% of slice over target,
  band is 3%).
- Day: book $3,158.25 → $3,168.91 = **+0.34%** vs **SPY +0.33%** → Rocket essentially
  matched SPY today (+0.01%); IWM led (+$11.88), OMER gave back a touch (−$1.22).
- No new satellite research happened this session (mechanical close only) — Week 35
  premarket board (OI needs a catalyst check, CAPR PDUFA outcome from 8/22, screeners
  re-run) is still outstanding, now two sessions running.

## 2026-08-24 — MARKET_CLOSE (Monday, Week 35 day 1)

**Quiet open to the week — no trades, no premarket/market_open sessions ran today either
(nothing in the log for 8/24 before this entry).**

- OMER held overnight (27 sh, $19.32, +0.3% today) — +15% rung untouched, catalyst
  multi-day and intact. IWM core (8.0522 sh) unchanged, within rebalance band (2.1% of
  slice over target, band is 3%).
- Day: book $3,173.17 → $3,158.25 = **−0.47%** vs **SPY −0.28%** → Rocket **−0.19%**
  vs SPY today (IWM lagged SPY on a small-cap-soft session — factor drag, not stock
  selection; one session, not a trend per lesson 28).
- No new satellite research happened this session (mechanical close only) — Monday's
  premarket board (OI needs a catalyst check, CAPR PDUFA outcome from 8/22, screeners
  re-run) is still outstanding from the Week 35 watchlist in research_log.md.

## 2026-08-21 — WEEKLY REVIEW (Week 34, Friday post-close)

**Grade B−. Best relative week of the regime (+2.03% vs SPY) — and none of it was earned
this week.**

- 📊 **Book $3,152.18 → $3,173.17 = +0.67%** vs **SPY −1.37%** → **+2.03%**. IWM −1.68%.
  Attribution: satellite **+2.18%**, cash **+0.10%**, factor **−0.24%** (the core *lost*
  to SPY). **Real alpha +2.18% — but 100% of it is OMER, opened 8/14.**
- ✅ **Since-rebase hand-built chain REBUILT** (the flagged task). Cash reconstructed
  transaction-by-transaction to **$237.54**, independently matching the 8/21 premarket log.
  Position P&L ties to the book change to the cent. **Since 7/20: Rocket +4.53% vs SPY
  +3.18% = +1.35% — first positive reading since the rebase.** Cumulative real alpha
  **+1.53%** (was −0.65%).
- ⚠️ `portfolio_state.md` now reads +1.28% — only 7bp off. **Coincidence, not a fix**:
  Bull's cumulative return happens to sit near Rocket's. Lesson 23 unchanged.
- 🚨 **THE FINDING: ETON was graded on a counterfactual nobody checked.** The 8/20 close
  claimed it beat where the trailing stop would have fired. **False** — HWM $63.83 → stop
  **$59.36**; 8/20 low $59.59, 8/21 low $59.76, **never touched**; ETON closed **$63.47**.
  Holding = **+$19.74**. The discretionary close **cost $25.83 = 0.82% of book.** It also
  violated **lesson 30a** (a Form 144 is not an exit trigger), written the day before.
  **Lesson 32 rewritten from a success into the error it was**; new rules 32a (only
  override a stop that is >2% away) and 32c (grade counterfactuals against the bars).
- ❌ **ARCT skip now costs +31%** ($10.28 → $13.45). Re-checked: **no new information**,
  readout still undated. **Gate held, per the lesson-35 pre-commitment.** Sizing — not the
  gate — escalated to the user.
- 🔧 **`position_reconciler.py` fixed** — three compounding parser bugs had it reporting
  Rocket's only satellite (OMER) as **UNATTRIBUTED**: `"CLOSE"` matched `(market_close)`;
  two-event headers dropped the second event; same-day round trips never closed because
  the log is written newest-first. **Now `✅ Balanced` for the first time**, and
  `position_table.py` includes OMER, which it had been silently omitting.
- 🗂️ Memory trimmed: research_log 191→103, market_context 241→88, session_notes 707→113,
  lessons 92→89. ⚠️ **lessons_learned is over its 60-line target and the overflow is all
  live standing rules** — flagged rather than cut.
- 📋 Week 35 watchlist built. **OMER's $19.71 rung (0.7% away) is the first check Monday.**
  ETON blocked by rule 13 at $63.47. Best fresh bar: **OI** (+12.5%, 98% of range) — needs
  a catalyst. **CAPR's PDUFA was Saturday 8/22 — check the outcome.**

## 2026-08-21 — MARKET_CLOSE (Friday, Week 34 day 5 — week close)

**OMER held overnight, core in band, no trades — cleanest close of the week.**

- 🟢 **OMER HELD.** Closed $19.24 at the week high, +3.3% on the day (8/20 close $18.63),
  fifth straight strong close. Stop still above entry; +15% rung ($19.71) 2.4% away,
  untouched — standing order to sell 9 sh on the touch carries into next week.
- ✅ **Core rebalance check: no trade.** IWM $2,416.79 vs target $2,333.15 — 2.64% of
  slice over, inside the 3% band.
- 📊 **Day**: hand-built book $3,137.45 → $3,169.89 = **+1.03%** vs **SPY +0.46%** →
  Rocket beat SPY by **+0.57%** today (script-verified position table: IWM +$19.29,
  OMER +$17.14, total +$36.43).
- ⚠️ **Since-rebase hand-built chain is stale** (last point 8/14, −0.78%) — flagged for
  reconstruction at the next weekly_review rather than guessed here. Do not quote
  `portfolio_state.md`'s +1.33% since-rebase figure as Rocket's own number (lesson 23).
- Week 34 summary: 1 satellite opened (ETON 8/17), closed 8/20 on the end-of-day rule
  (small loss). OMER (opened 8/14) carries into Week 35 still up double digits. Three
  straight no-entry sessions to close the week (8/19–8/21) — board quality problem
  (falsified scanner reads, crypto-treasury theme dominating), not a discipline lapse.

## 2026-08-21 — MARKET_OPEN (Friday, Week 34 day 5)

**No new satellite — the open confirmed the premarket call, and the board stayed weak.**

- 🚫 **NO ENTRY.** Portfolio synced clean: no overnight stops, IWM core and OMER both
  intact, no fills, weekly count still 1/5.
- Scanner at the open was still the same crypto-treasury sweep flagged premarket — USDE
  now **80.1x RelVol +33.5%**, plus GEMI/BKKT/ASST/ABTC/DFDV/HYPD/SBET/SECZ/BTGO, all
  mandate-excluded (lesson 31). ARCT +4.8% on 7.7x — standing skip, no new information.
  CAPR −0.9% — PDUFA is tomorrow 8/22, untouched either direction.
- 🆕 **ABUS checked and killed — new catalyst type to name explicitly.** +10.9% on a
  scanner-reported 11.4x RelVol, but `detail` showed real volume only **1.1x avg (2015k
  vs 1458k)** — another scanner/reality mismatch (lesson 17). One search found the actual
  driver: a **$230M Dutch-auction tender offer at $5.00–$5.75/share**, announced today.
  **A self-tender is not on the nine-catalyst list** — it's a capital-return event, and
  the band pins price toward the midpoint rather than a momentum breakout (same shape as
  lesson 27's pinned-price names, just self-imposed instead of a merger price). Rule 1:
  no catalyst = no trade.
- 🔵 **OMER unchanged** — $18.72, +15% rung ($19.71) still 5.2% away, untouched. Standing
  order to sell 9 sh on the touch stands.

## 2026-08-21 — PREMARKET (Friday, Week 34 day 5 — last session of the week)

**No new satellite, third straight session — but the board wasn't weak, it was FALSE. Raw
bars falsified all nine non-crypto "gainers." Two new rules: date your catalyst headlines,
and one session of rate relief is not a resolution.**

- 🚫 **NO ENTRY.** 🆕 **The scanner and the tape disagreed on EVERY non-crypto name.** The
  04:20 scan showed nine names +3.4% to +7.7%; raw daily bars showed all nine were
  **extended-hours quotes against red or flat 8/20 cash sessions**. UNCY closed at **15% of
  range**, **LFMD at 0%** (on the low, 0.3x volume), HDSN at **4%** (its real 3.5x event was
  8/17, four days stale), OSS at **10%** and **−16% in four sessions**, ALMU **−20% in
  three**; ENR/MAX had no catalyst inside 17/68 days; **BBW's open WAS its high** and it
  reports **8/27** (earnings-week rule). **Nine names, nine falsifications, one script call.**
  → **Lesson 17 at full strength: the scanner is a name source, never a signal.**
- 🆕 **APPS — new rule, and it nearly worked.** An overnight search returned *"Digital Turbine
  surges 22% after hours on a beat-and-raise, adj EPS $0.15 vs $0.05"* — the **exact** catalyst
  type that trades, on a name Rocket knows. **The article had no date.** Bars: 8/18 C 12.12 →
  8/19 C **11.23 (10% of range)** → 8/20 C **10.71 (6% of range)** on **0.5x** volume =
  **−11.6% in two sessions.** Weeks-stale print, fully faded. → **new lesson: extend rule 11a
  from analyst headlines to CATALYST headlines — date the news against the bars.**
- ⚠️ **ARCT — the skip is now costing money, and it still stands.** It ran a **second**
  volume-expansion day: **+6.9% at 66% of range on 2.9x** (after 8/19's +25% on 7.2x). One
  search re-tested the kill: **no new information entered the market** — same Aug-6 Q2/CSL
  material, same Canaccord PT **cut**, and the company re-confirmed **ARCT-810 Phase II data +
  regulatory path "Q3 2026," still undated**, inside any 1–5 day hold. **Lesson 29 intact; a
  7% stop fills at the open, wherever the open is.** 🚨 **Recording the cost (~−7% foregone
  and counting) for the weekly review — do NOT loosen the calendar gate because price went the
  other way.**
- 🆕 **Crypto-treasury theme topped the scanner a THIRD straight session** — **USDE +19.3% on
  26.1x RelVol**, the biggest print on the board, plus DFDV/ABTC/SBET/ASST/FWDI/SECZ/BKKT/
  GEMI/HYPD. All excluded on **mandate** (lesson 31); none re-screened. **Consequence worth
  naming: while tokens rally, the scanner's top tier is useless to Rocket and the real board
  must be built from the names beneath it — which is exactly where the bars-falsify-all
  problem bites. Three no-trade sessions is a board-quality problem, not a discipline one.**
- 🚨 **10-yr: yesterday's resolution was given back in ONE session — 4.65% → 4.70% (+5bp),
  cushion to the 4.75% trigger re-narrowed from 10bp to 5bp.** Thursday's "the standing rate
  flag stands down a notch" was **premature**. → **lesson 28's logic applies to rates too: one
  session of relief is not a resolution.** ✅ VIX **15.63**, no brake. ✅ Futures green across
  the board, **Russell +0.65% tied best.** ✅ **Brent's four-session ramp STALLED** (+0.19%,
  $93.96, still under the $95 watch). 🚨 **Gold is now the live trend: $4,639 (+2.72%),
  +5.1% in three sessions and accelerating.** **Gold making highs while yields RISE** is the
  more uncomfortable combination — flagged to the weekly review, not actionable at 1–5 days.
- 🔵 **OMER — best bar on the book. 8/20: O 18.30 H 18.73 L 18.07 C 18.63, +1.8% at 85% of
  range** on a day IWM fell −1.34%. **Four straight closes at 72–85% of range.** Stop ≈$17.57,
  **$0.43 ABOVE the $17.14 entry — cannot lose money.** 🚨 **+15% rung $19.71 is 5.2% away —
  SELL 9 SHARES ON THE TOUCH** (MRLN round-tripped unscaled). ⚠️ 🆕 Position has drifted to
  **16.0% of book, above the 15% max-satellite line** — pure appreciation, not a violation
  (the cap binds at entry), but a **second independent argument for taking the rung**, which
  returns it to ~10.7%. ATM still undrawn; ladder open ($33 PT).
- 🗓️ **Calendar clean today. Jackson Hole confirmed Aug 27–29 (Week 35)** — six days out, and
  it lands inside any position opened late next week. **Earnings pipeline empty FIVE straight
  sessions**, the longest drought recorded; nearest **QMLS 8/25, LTRX 8/26** (LTRX stabilised
  8/20 at **71% of range on 1.4x** — the best-defined event on the calendar, carry forward).
  🚨 **CAPR PDUFA is TOMORROW 8/22**; it closed 8/20 at **1% of range** — standing skip, do
  not touch in either direction.
- Book **$3,137.45** (hand-built, lesson 23a) = IWM 8.0522 sh $2,396.90 (76.4%) + OMER
  $503.01 (16.0%) + cash $237.54 (**7.6% — inside the buffer, no bearish thesis needed**).
  **92.4% invested.** 8/20: −0.96% vs SPY −0.84% (−12bp), IWM −1.34%. Core is **$76 / 2.4%
  OVER** target — **inside the 3% band, erring toward more invested. No rebalance until
  `market_close`.** Satellites **1/4**, weekly count **1/5**.

