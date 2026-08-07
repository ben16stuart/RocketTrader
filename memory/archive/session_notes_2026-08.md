
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

