# Rocket Trade Log

Append-only record of all Rocket trades. Never delete entries.

---

## 2026-08-07 — NO TRADE (market_close) — no satellites to review, core in band

**Position review**: 0 satellites open — nothing to review. Core (IWM 9 sh) is the
only holding.

**Core rebalance check**: slice $3,152.62, satellite value $0, 10% buffer $315.26 →
target_core $2,837.36. IWM 9 sh @ $301.57 = $2,714.13 — **3.91% short of target,
outside the 3% band.** Per lesson 7a, only trade a breach if the nearest whole-share
move lands closer to target than doing nothing: buying 1 sh (@~$301.57) would push
IWM to $3,015.70, **5.66% over target** — a bigger deviation than the current 3.91%
short. **No trade** — share-granularity remainder, not actionable. Notional slice
cash $438.49 (13.9%), same known remainder flagged the last several sessions.

**Day P&L**: Rocket's book (IWM + notional cash) **+1.51%** ($3,105.58 → $3,152.62)
vs **SPY +0.66%** today — IWM itself moved +1.13% ($298.25→$301.61), small caps
outperforming large caps today; the extra lift in the slice figure reflects the
shared-account cash split, not incremental Rocket P&L. Since rebase (7/20): Rocket
+3.99% vs SPY +4.20% (**-0.21%**).

**No new trades placed today** — market_open found both ranked ideas (QNST, STLN)
disqualified and no fresh mover had a validated catalyst; no midday session ran;
market_close core rebalance is inside the actionable range (see above).

---

## 2026-08-07 — NO TRADE (market_open) — both ranked ideas disqualified at the open

**QNST (P1)** — extension gate essentially exhausted: intraday high $20.50 (+34.8%) vs the
$20.55 (35%) gate, and spot ($20.21) already above the $19.00 mean analyst target with no
revision confirmed. Base held (higher lows, strong relative volume) but risk/reward broken
— capped upside, full stop-out downside. Skipped.

**STLN (P2)** — premarket-flagged dilution risk (unverified, SEC 403'd) confirmed via
web search: active $15M ATM facility (424B5) on a company with a 0.1% EBITDA margin and
$41.1M cash. Same structural flaw that killed SOC and SVCO this month. Skipped.

**Fresh movers** (`unusual_volume`/`top_movers`) — none carried a validated catalyst;
declined to chase unvetted names late in the entry window. Full detail in session_notes.md
and research_log.md.

No positions opened or closed. Rocket unchanged: IWM 9 sh (core), 0 satellites.

---

## 2026-08-06 — CSTL trailing stop hit + core rebalance (market_close)

**CSTL — STOPPED OUT.** Trailing 7% stop filled intraday at **18:32 UTC (2:32 PM ET)**,
discovered at end-of-day sync (not caught live — no midday session ran today). Not a
market_close decision; the broker closed it automatically.
- Entry: 15 sh @ $29.99 (2026-08-03)
- Exit: **$29.94 on 2026-08-06** (stop: 7% trail off $31.73 high-water mark → trigger
  $29.5089, filled slightly better at $29.94)
- P&L: **-$0.75 (-0.17%)** — essentially breakeven, not a thesis failure
- Reason for exit: trailing stop, not a decision — the post-earnings pop's high-water
  mark ($31.73, set 8/03–8/04) pulled the 7% trail up with it, and today's session round-
  tripped through it. Catalyst (Q2 beat-and-raise) was never invalidated; this is the
  ordinary cost of a trailing stop giving back gains after a high print.
- Lesson: nothing actionable — stop worked exactly as designed, protected the post-pop
  high-water mark, exited at essentially cost. No open Rocket satellites remain (0/4).

**CORE REBALANCE — BUY IWM 1 sh.** CSTL's exit returned its proceeds to cash instead of
core per the same-session rule, opening a large gap: slice $3,105.58, satellite value
$0 (no open satellites), 10% buffer $310.56 → target_core $2,795.02. Pre-trade IWM (8 sh)
= $2,387.36 (13.1% short of target — outside the 3% band). Bought **1 sh @ $298.27**,
IWM now **9 sh, avg entry $292.90 ≈ $2,684**. Residual gap ~$111 (3.6% of slice) is a
whole-share rounding remainder, not further actionable — IWM trades in ~$298 increments
against a ~$111 gap, so 1 share is the closest achievable fit; buying a 2nd share would
overshoot to -6.1%. Notional slice cash after: ~$422 (13.6%), expected to normalize as
this residual works itself into future rebalances.

**Day P&L**: Rocket's total book (positions + notional cash) **-0.68%** ($3,126.82 →
$3,105.58) vs **SPY -0.15%** today — underperformance driven by the CSTL stop-out
(-1.38% intraday move that triggered the trail) plus IWM tracking slightly soft, not a
fresh problem. Since rebase (7/20): Rocket +2.44% vs SPY +3.59% (**-1.15%**), the widest
gap yet — consistent with the standing IWM-factor-drag note plus today's CSTL exit.

**No new trades placed today** beyond the stop-driven exit and its core rebalance —
market_open found all three ranked candidates disqualified; no midday session ran.

---

## 2026-08-05 — NO TRADE (market_close) — CSTL held, core in band

**CSTL position review**: 15 sh, entry $29.99, closed **$30.36 (+1.2% since entry)** but
**down from yesterday's $31.31 close (-3.0% on the day)** — a pullback off the post-earnings
pop, not a break. Still comfortably above entry and 9.3% clear of the $27.77 stop, MA50
$23.29 well below, week range $26.79–$31.18 (near the top, not breaking down). Catalyst
(Q2 beat-and-raise, guidance raise) is multi-day per the 8/03 entry thesis and confirmed
again 8/04 — no distribution signal (this is a single quiet red day, not fading on volume).
**Hold overnight.**

**Core rebalance**: IWM 8 sh = $2,400.40 vs target_core = slice $3,126.82 − CSTL $455.40 −
10% buffer $312.68 = $2,358.74. **1.33% over target — inside the 3% band. No trade.**
Notional slice cash $271.02 (8.67%), inside the 10% buffer.

**Day P&L**: Rocket's own positions (IWM + CSTL) **-0.99%** ($2,884.37 → $2,855.80) vs
**SPY -0.06%** today — underperformance driven by CSTL's pullback (-3.0%) plus IWM tracking
slightly softer than SPY, not a stock-specific problem. Since rebase (7/20): Rocket +3.14%
vs SPY +3.90% (**-0.76%**).

**No trades placed today** — market_open found all screened candidates disqualified, market
close found no exit or rebalance trigger. Flat session, no ntfy stops hit independently of
the scheduled EOD summary.

**Note**: portfolio_snapshot.py flags 12 sh NOW ($1,406) as unattributed — held at the broker
but absent from both Rocket's and Bull's trade logs. Not sized against or acted on; this is a
reconciliation gap for weekly_review, not a Rocket position.

---

## 2026-08-05 — NO TRADE (market_open) — both priority candidates disqualified

No fills or stops overnight. Cash unchanged at $430.37 pooled; Rocket notional cash
$261.41 (8.3% of $3,143.41 slice) — inside the 10% buffer, no action needed. IWM 8 sh
+ CSTL 15 sh unchanged, 91.7% invested. Checked both pre-market priorities plus fresh
scans (`unusual_volume`, `top_movers`); no candidate qualified.

- **APPS (Priority 1)** — hard-gated, lesson 15 for the third session running.
  Premarket plan set an explicit gate: 35% off the $9.51 Tuesday close = $12.84, no
  trade above it at decision time. Realized 9:45 AM tape: **$13.85–$13.95, +45.6% to
  +46.6%**, only 1% off the 52-week high. The gate was breached before the session even
  opened. **No entry.** Added to second-day watch (lesson 8) — valid continuation entry
  tomorrow if it closes strong on the print.
- **FTK (Priority 2)** — no entry, three independent reasons. Volume is only 0.4x avg
  (167k vs 361k avg) on a +29% move — the opposite of the >1.5x confirmation lesson 10
  requires. Market cap still returns `$0M`/unverified from the scanner (flagged
  premarket, never cleared). And the 10:00 AM ET earnings call was 15 minutes away at
  decision time — entering would mean holding through a live unscheduled binary.
- **TBI (fresh find, top_movers)** — +20.8–26.8%, inside the gap-and-go band, but avg
  daily volume 184k fails the 300k universe minimum outright. Disqualified on liquidity
  before any catalyst check.
- **AMPX / KODK** — unchanged from premarket, both remain watch-only (uncleared
  dilution flag on AMPX; unverified catalyst on KODK).
- **Result**: flat session, no trades placed. Per Portfolio Construction rule 7, "no
  qualifying catalyst" means hold IWM, not go flat — Rocket is already ~92% invested
  via core + CSTL, so no action was needed to stay compliant. No notification sent
  (flat session, no stops hit).

---

## 2026-08-04 — NO TRADE (market_open) — all four candidates disqualified

No fills or stops overnight. Cash unchanged at $430.37 pooled / ~$253 Rocket notional.
IWM core + CSTL satellite unchanged, 91.6% invested. Checked both pre-market priorities
plus fresh scans; every candidate failed on its own numbers.

- **AMRC (Priority 1)** — hard-gated. Pre-market plan set an explicit gate: gap >35% off
  the $22.73 Monday close (= $30.69) means wait for second-day entry, not chase. Raw 5-min
  bars show the actual **opening print was $31.93 = +40.5%**, breaching the gate before
  the first bar even closed. It then faded to a $28.97 low by 9:40 on ~443k shares (84% of
  full-day avg volume in 15 minutes) — high-volume chop after an over-extended gap, not a
  base. **No entry.** Added to second-day watch: if it closes strong today, tomorrow's open
  or first 10-min base is a valid entry per the second-day continuation rule.
- **BLZE (Priority 2)** — same failure mode, worse. Opened $20.13 (+29.1%, inside the
  gap-and-go band) but kept climbing through the first 15 minutes to a $23.99 high, last
  ~$23.54 = **+51.0%** off the $15.59 prior close — the *current* move is now more than 35%
  even though the opening print was not. Rule 2's "too extended, do not chase" applies to
  the state of the tape at decision time, not just the open tick. Combined with the known
  CoreWeave-warrant dilution overhang (research_log.md), this is a clean skip. Added to
  second-day watch, dilution caveat carries forward.
- **XGN (fresh find)** — Exagen Q2 2026 beat: revenue $19.94M vs $17.81M est (+16% YoY,
  record), EPS -$0.13 vs -$0.19 est, gap +32.7–34.6% (inside the gap-and-go band, unlike
  AMRC/BLZE). Real catalyst, but **fails the hard universe gate**: avg daily volume 229k,
  under the 300k minimum in CLAUDE.md's Investment Universe rule. Disqualified regardless
  of catalyst quality — thin-float healthcare name, no exception made.
- **BWEN** — appeared on both `unusual_volume` and `top_movers` (+14–15%, 3.4–3.6x RelVol),
  same overlap signature that found AMRC pre-market. Checked: **no catalyst**. Q2 earnings
  aren't until 8/11; the only recent news is a May wind-market exit, already stale. Rule 1
  (no catalyst = no trade) applies. Skip.
- **Result**: flat session, no trades placed. Per Portfolio Construction rule 7, "no
  qualifying catalyst" means hold IWM, not go flat — Rocket is already ~92% invested via
  core + CSTL, so no action was needed to stay compliant. No notification sent (flat
  session, no stops hit).

---

## 2026-08-03 — IWM CORE REBALANCE (market_close) — SELL 1 sh

- **Shares**: sold 1 @ ~$296.30 (filled 19:58:49 UTC), IWM position now 8 sh (avg cost
  basis unchanged $292.28)
- **Catalyst**: N/A — core rebalance, not a satellite trade. Satellites now hold CSTL
  (15 sh, opened this session at market_open, ~$456.60). target_core = slice − satellite
  − 10% buffer = $3,075.03 − $456.60 − $307.50 = $2,310.93. Pre-trade IWM value was
  9 sh × $296.33 ≈ $2,666.97, **11.6% over** target (band is 3%). Post-trade 8 sh ×
  $296.30 ≈ $2,370.64, **1.9% over** target — within band. Selling 2 sh would have landed
  7.7% under, a worse miss, so 1 share was the correct whole-share fix (lesson 7a).
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket now 8 sh IWM + CSTL (15 sh) satellite. Cash breach from premarket
  is resolved by the CSTL entry; this trade brings core back inside the rebalance band.

---

## 2026-08-03 — CSTL BUY (market_open) — Satellite #1

- **Shares**: 15 @ $29.99 (filled 13:51:42 UTC / 9:51 AM ET)
- **Catalyst**: Q2 2026 earnings beat-and-raise (reported 7/30): revenue $103.5M
  (+20% YoY), FY26 guidance raised $345–355M → $365–375M, core test volume +32% YoY,
  guided to positive Adjusted EBITDA Q3/Q4/FY26. Research log had this on ice since
  it closed 7/31 at $28.00, below its own $28.60 reclaim trigger — today it broke
  the trigger cleanly on ~3x 20-min volume (84,035 sh vs ~27,500 expected), price
  action monotonically higher through the 9:30–9:50 base (28.37 → 28.31 → 29.36 →
  29.94), no fade.
- **Dilution check** (run before entry, per standing rule): SEC EDGAR filings for
  CIK 0001447362 show no S-3/S-1/424B since a Feb 2024 shelf — clears.
- **Stop**: 7% trailing, placed immediately, hwm $29.86, initial stop $27.7698
- **Targets**: 1st 1/3 at +15% ≈ $34.49 | 2nd 1/3 at +25% ≈ $37.49 | trail final 1/3
- **Size**: 15 sh = $449.85 (14.6% of Rocket's $3,067 slice, under the 15%/$460 cap)
- **Thesis**: real earnings catalyst already validated over two prior sessions: today
  is a technical confirmation entry (base reclaim), not a fresh-news chase. Sector
  headwind noted — small-cap healthcare has been the weakest group this week — but
  this is an idiosyncratic guidance raise, not a sympathy bounce.
- **Skipped AMCX** same session: spiked to $11.50 on the open then fully round-tripped
  to $11.19–11.25 by 9:45–9:50 on only ~1.4x volume (61,439 sh vs ~44,100 expected) —
  a fade, not a base. Does not meet the >1.5x-volume hold-above-$10.83 entry rule as
  written. Watching for a cleaner base later in the week per the missed-catalyst rule.
- **REPL**: still no FDA decision confirmed as of this session; stayed flat per the
  standing no-entry-through-a-binary rule.

---

## 2026-07-31 — IWM CORE REBALANCE (market_close) — SELL 1 sh

- **Shares**: sold 1 @ $291.11 (filled 19:58:57 UTC), IWM position now 9 sh (avg cost
  basis unchanged $292.31)
- **Catalyst**: N/A — core rebalance, not a satellite trade. No satellites held (0
  open), so target_core = slice − 0 − 10% buffer = $3,043.69 − $304.37 = $2,739.32.
  Pre-trade IWM value was 10 sh × $291.09 = $2,910.90, **5.65% over** target (band is
  3%). Post-trade 9 sh × $291.11 ≈ $2,619.99, **3.92% under** target — closer to
  target than staying at 10 sh, so the trim was taken per lesson 7a (only skip a
  band-breach fix if the nearest whole-share trade would overshoot *worse* than doing
  nothing; here it doesn't).
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket now 9 sh IWM, no satellites. Whole-share granularity (1 sh ≈
  9.6% of slice) keeps causing this back-and-forth — same open thread as 7/28 and
  7/30, still worth a fractional-order fix at weekly_review.

---

## 2026-07-31 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 1 @ ~$289.64 (filled ~9:06 AM ET), IWM position now 10 sh (avg $292.31)
- **Catalyst**: N/A — core rebalance, not a satellite trade. Cures the cash breach: no
  premarket research ran today (research_log.md's watchlist is stale from 7/30), so
  market_open validated the two carryover names inline instead:
  - **CMCO** — real Q1 FY27 beat + 28.1% short float, but today -4.9% on 0.2x avg volume
    (drifting down on no volume, not a base). No entry.
  - **BOOM** — beat-and-raise catalyst still real, but flat today (+0.0%) on 0.1x avg
    volume, below MA50, 1-month move 0%. Dead. No entry.
  - Fresh scan (`unusual_volume` + `top_movers`) cross-referenced for names appearing on
    both: **JFB** (+13.5%, business-combination "momentum update" is not new dated news,
    plus a 1395% short-float reading that is almost certainly bad data — same red-flag
    profile as the DFNS hard-skip precedent) and **CAPR** (+4.8% but -81% over the last
    month, -37% over 5 days — a dead-cat bounce inside a freefall, no catalyst, skip).
  - **REPL** +100–130% on a real catalyst (FDA adcomm 10-3 favorable vote 7/30, PDUFA
    Aug 2) — but already 5x+ the 20% chase limit with a binary FDA decision imminent.
    Per lesson 8, added to watchlist for a pullback/consolidation entry, not tradeable
    today at any size.
  - No satellite confirmed → per CLAUDE.md Portfolio Construction rule 7 ("no qualifying
    catalyst means hold IWM, not go flat") and the cash-buffer rule (>10% cash requires
    a written bearish thesis, none exists), bought 1 more IWM share.
- **Stop**: NONE by design (core sleeve).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: Rocket slice ~13.9% cash pre-trade → ~4.3% post-trade. Rocket now 10 sh
  IWM, no satellites.

---

## 2026-06-05 — MRLN CLOSED (+0.033% account)

**ROCKET'S FIRST TRADE** — ENTRY @ $8.88, EXIT $8.90

### ENTRY (9:50 AM)
- **Shares**: 1,670 @ $8.88
- **Catalyst**: USSOCOM C-130J autonomy Critical Design Review completion (announced June 4 after-hours). Major defense milestone advancing Merlin's AI-powered autonomy stack from design to aircraft integration phase. $100M+ IDIQ contract ceiling value.
- **Entry rationale**: Second-day continuation after +32.71% after-hours gap on real catalyst. Entry zone $8.54-$10.44 (within 10% of $9.49 after-hours close). Filled at $8.88 with 2.4x avg volume confirmation. Aerospace & Defense, $867M mcap (in-universe).
- **Stop**: 7% trailing (~$8.26 initial)
- **Targets**:
  - 1st third @ $10.21 (+15%)
  - 2nd third @ $11.10 (+25%)
  - Trail final third with 7% stop
- **Position size**: $14,830 (14.8% of account)
- **Risk**: $1,044 (1.05% of account)
- **Thesis**: Defense tech autonomy program milestone with USSOCOM. Second-day entry on confirmed catalyst with strong volume. Low float aerospace name with analyst PT $13 (strong_buy). Risk = profit-taking after big move, but catalyst quality high and volume confirmed conviction.

### EXIT (12:09 PM ET / 16:09:52 UTC)
- **Exit price**: $8.90 (filled via Alpaca)
- **P&L**: +$33.40 (+0.23% on position, +0.033% on account)
- **Intraday action**: MRLN hit $10.25 high (+15.4% from entry, reached first profit target), pulled back to $8.31 low (just above $8.26 stop), then recovered to $9.10 close
- **Exit reason**: Position closed at $8.90 during afternoon pullback. Stop not hit ($8.26), but position exited during volatility. No manual exit record captured in real-time.
- **Outcome**: PROFITABLE but small (+$33.40). Thesis validated (defense catalyst was real, stock moved +15% intraday and closed +22% on day at $9.10), but exited too early during midday chop at $8.90 instead of holding through close ($9.10) or first target ($10.21). Lesson: Trail stop caught downside volatility, but position closed prematurely.

---

## 2026-07-30 — IWM CORE REBALANCE (market_close) — sell-then-rebuy due to tooling error

**Intent**: rebalance check at market_close found IWM 10 sh = $2,926.90, **6.5% over**
target core (90% of $3,032.74 slice, 0 satellites = $2,729.47). Plan: sell 1 share to
land closer to target (9 sh = $2,635, ~3.1% under — the nearest achievable given
whole-share granularity, same tradeoff as lesson 7a).

**Execution error**: ran `alpaca_client.py close IWM --qty 1`. The `close` command has
no `--qty` support — it always calls `DELETE /v2/positions/{symbol}`, which liquidates
the *entire* position regardless of any trailing flag. Order filled for the full 10 sh
(sell, ~$292.69), leaving Rocket's core at **0 sh / 0% invested** for a few minutes —
an unintended full-liquidation, not a 1-share trim.

**Correction**: immediately bought back 9 sh via `alpaca_client.py buy IWM 9` (correct
command for exact quantities), filled ~$292.79. Net result matches the original intent
(9 sh core, ~3.1% under target) but took two round-trip orders instead of one partial sell.

**Stop**: NONE by design (core sleeve).
**Does not count** against the 4-satellite cap or 5-trades/week cap.
**Lesson logged** in lessons_learned.md: use `sell SYMBOL QTY` for partial reductions,
never `close` (full-liquidation only, ignores extra flags silently).

---

## 2026-07-30 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 1 @ $291.49 (filled ~9:51 AM ET), IWM position now 10 sh
- **Catalyst**: N/A — core rebalance. Cures the cash breach flagged 3 consecutive
  premarket sessions (7/28, 7/29, 7/30): pooled cash had drifted to 13.1% of slice
  (no written bearish thesis), driven down further overnight when Bull bought SCHW
  and consumed most of the shared buffer. Per the premarket plan's explicit fallback
  ("if BOOM does not confirm → buy 1 IWM share"), executed after BOOM failed its base.
- **Satellite candidates rejected today** (see research_log.md for full detail):
  - **BOOM** — failed the required 9:45-9:50 base. Real 5-min bars (yfinance) showed
    a spike to $7.37 at the open (already brushing the >35% ceiling), fading on
    declining volume each bar, then a break BELOW the $6.40 confirmation level to a
    $6.27 low on rising (distribution) volume in the 9:45 bar. Not a valid entry —
    correctly stood aside per lesson "price without volume [holding] = distribution."
  - **CMCO** — fresh name, +33% on a real Q1 FY27 earnings beat (EPS $0.61 vs $0.27
    est) with 28.1% short float (squeeze fuel). But real intraday data showed a spike
    to +42% at the open (past the 35% ceiling) fading hard on declining volume, AND a
    10:00 AM ET earnings call still ahead — a live binary. Skipped; watch post-call
    and tomorrow for a cleaner second-day setup.
  - **XRX** — +24-25% on a genuine Q2 earnings beat (EPS $0.38 vs $0.03), but prior
    close was $2.64 — this is a sub-$3 stock crossing the floor only today (the exact
    "sub-$3 trap" the rules exist to avoid), AND intraday high $3.78 was already a
    +43% gap (past the 35% ceiling). Skipped on both universe and chase-limit grounds.
- **Stop**: NONE by design (core sleeve, see 7/28 entry below).
- **Does not count** against the 4-satellite cap or 5-trades/week cap.
- **Result**: cash breach cured — pooled cash $397.09 (13.1% implied via slice math)
  → $105.68 (~3.5% of slice) after the buy. Rocket now 10 sh IWM, no satellites.

---

## 2026-07-28 — IWM BUY (Core sleeve — not a satellite)

- **Shares**: 9 @ $291.50 (filled)
- **Cost basis**: $2,623.50 (~86.4% of Rocket's $3,037.22 allocated slice)
- **Catalyst**: N/A — this is the core/benchmark sleeve, not a catalyst trade. Per
  CLAUDE.md Portfolio Construction (adopted 2026-07-27), Rocket's default resting
  state is ~100% invested via IWM, not cash. Rocket had been flat 0 positions /
  ~100% cash with no written bearish thesis, violating the mandate.
- **Stop**: NONE by design. Backtested 1993-2026: buy-and-hold beats every trailing-stop
  configuration on the index (10.73% CAGR vs 7.98-8.48% stopped). Satellites keep 7% stops;
  the core does not.
- **Does not count** against the 4-satellite position cap or 5-trades/week cap.
- **Thesis**: Establish the benchmark-tracking core so idle cash stops acting as an
  unhedged short against equity drift. Attribution note: IWM is a small-cap factor bet
  vs the SPY benchmark — weekly_review must split IWM beta from stock-picking skill,
  not book factor drift as alpha.
- **Remaining slice buffer**: ~$413 (13.6%) left for a satellite (TRAX conditional
  reclaim watch) or operating buffer.

---

## 2026-06-16 — CAMP ENTRY — [SUPERSEDED 2026-07-27 — ORPHANED BY ACCOUNT MERGE]

> **SUPERSEDED.** CAMP is not held on the current shared account and never was.
> This position lived on Rocket's pre-merge account. See the correction entry
> dated 2026-07-27 below. Retained for audit trail only.

**ROCKET'S SECOND TRADE** — ENTRY @ $4.85

### ENTRY (9:45 AM ET)
- **Shares**: 3,093 @ $4.85
- **Catalyst**: JPMorgan upgraded CAMP from Neutral to Overweight with PT $9 (from $5) on CMP-002 (SYNGAP1-related disorder) probability-adjusted upside. Leerink also raised PT to $9 on CMP-002 GLP tox progress, IND filing targeted H2 2026. Two analyst actions clustering = fresh institutional attention on small cap biotech (catalyst type: analyst upgrade).
- **Entry rationale**: Gap-and-go setup. Pre-market +10.4% gap under 20% chase limit. Entry at 9:45 AM on confirmed 10-min base ($4.85) with 2.1x avg volume (316k vs 78k avg). $252M mcap (in-universe), NASDAQ clinical-stage biotech, price >$3, low float (26.5M shares). Fresh same-day catalyst (Jun 16).
- **Stop**: 7% trailing stop set immediately (~$4.51 initial)
- **Targets**:
  - 1st third @ $5.58 (+15%)
  - 2nd third @ $6.06 (+25%)
  - Trail final third with 7% stop
- **Position size**: $15,001 (15.0% of account, max position cap)
- **Risk**: $1,052 (1.05% of account)
- **Thesis**: Fresh dual-analyst PT raises (JPMorgan and Leerink) on clinical-stage biotech with CMP-002 (SYNGAP1 disorder) advancing to IND filing H2 2026. Analyst clustering on small cap = institutional attention catalyst. Entry gap (+10.4%) under chase limit with strong volume confirmation (2.1x avg). Low float (26.5M) supports price movement. Risk = no near-term binary (CMP-002 not in clinic until H2 2026), clinical-stage (no revenue), FOMC tomorrow adds event risk. Entry discipline followed: gap-and-go base, volume >1.5x, fresh catalyst.

### EXIT — UNRECOVERABLE (recorded 2026-07-24 weekly review)
- **Status**: CLOSED, but exit price/date/reason cannot be recovered.
- **Backfill attempt (2026-07-24)**: Queried Alpaca closed-order history for the live
  shared account. CAMP does not appear — the only closed orders on the shared account
  are Bull's (KO, V, GOOGL, HSY, COST, JPM), oldest 2026-05-05. CAMP was traded on
  Rocket's original standalone paper account, which was dissolved in the 2026-07-20 merge
  with Bull. That account's order history is gone; there is no API path to recover the fill.
- **Resolution**: Treat CAMP as closed at an unknown price with unknown P&L. It is NOT a
  live position (confirmed absent from portfolio_snapshot.py). This entry is closed for
  bookkeeping. Do not report CAMP as open again.
- **Root cause / prevention**: Exit was never logged in real time (see lessons_learned.md
  item 9). Standing rule reinforced: every close_position call must be paired with a
  same-session trade_log.md exit entry.


---

## 2026-07-27 — BOOK CORRECTION — CAMP orphaned by the account merge

**Correcting entry.** Posted after reconciling this log against the shared Alpaca
account's filled-order history.

Rocket's book carried CAMP (3,093 sh @ $4.85, entered 2026-06-16) as an open position.
It is not held on the shared account, and **the shared account has no CAMP orders in
its entire fill history** — the position was opened on Rocket's own pre-merge account,
which is no longer the account Rocket trades.

**Disposition: unknown.** Rocket cannot determine the exit price or date, because the
account holding it is not the account it now reads. It may still be open on the old
account, or have been stopped out. Final P&L is therefore **unrecorded**, and this
trade is excluded from win-rate and R-multiple statistics rather than being assumed
a win or a loss.

**Impact**: Rocket believed it held a ~$15k position it does not have. Any sizing or
exposure calculation trusting the book was overstating deployed capital.

**Lesson**: an account migration must be treated as a reconciliation event. Positions
do not follow the agent — open positions must be explicitly closed out or transferred
in the book at the moment the account changes, or they become permanent phantoms.

