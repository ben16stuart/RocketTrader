# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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

## 2026-07-31 — WEEKLY REVIEW (Week 31, Friday post-close)

**Grade: C−.** 6 order events, **all core IWM, 0 satellite trades, 0 closed trades** →
no win rate and no R-multiple exist this week. Net week P&L ≈ **−$1.02**.

**Performance, honestly attributed.** Week: SPY **+1.10%**, IWM **+0.01%**, Rocket
**≈+0.12%** → **Rocket vs SPY ≈ −0.98%**. Split: IWM factor bet (87% × −1.09%) = **−0.95%**,
cash drag **−0.14%**, **stock selection 0.00% — there was none.** Every basis point of the
shortfall is the deliberate IWM-vs-SPY factor bet plus cash drag. This is the exact mirror
of Week 30's "+0.43% beat" from sitting in cash. **Both weeks were zero alpha; only the
sign flipped.** Since rebase: Rocket +0.30% vs SPY +0.67% = −0.37%.

**Root cause of the week — two confirmed infrastructure failures, not analysis failures:**
1. **The premarket delay was a Claude session limit, not a schedule bug.** The plist fires
   correctly at 6:20 AM ET; `premarket.log` shows it hit the session limit on opus *and* on
   the sonnet fallback, finishing at 10:05 AM ET. **Cost: the AMCX entry.** → lesson 12.
2. **The midday routine has never run — ever.** Plist authored 7/22, never loaded, zero log
   files. Nine days of "re-check at midday" plans silently did nothing. → lesson 13.

**The skips were right.** CSTL **closed $28.00, below its own $28.60 trigger** — the rule
would have kept Rocket out regardless of timing, so it is a non-miss. REPL is +107% into a
**Monday 8/02 PDUFA binary** — untradeable. SOC looked like the week's best energy momentum
name until one search found **$93M of stock being sold at $3.08** plus $289M of converts.
**AMCX was the only genuine miss**: it held every level the plan named and closed at its
52-week high on 5.8x volume.

**Changes**: strategy.md meta-problem **rediagnosed** — deployment is solved by the core
sleeve and the scanner has recovered; **uptime is now the binding constraint**. Added a
mandatory attribution formula. Lessons 12–13 added. research_log rebuilt for Week 32 (AMCX
top idea, dilution check now CLEAR; CSTL downgraded; SOC hard-avoided). Memory files
trimmed and archived. **Key takeaway: Rocket's analysis was right all week — it just wasn't
running when the window was open.**

---

## 2026-07-31 — Market Close (Friday, ~4:00 PM ET / 19:59 UTC)

**Decision: trimmed oversized IWM core 10 sh → 9 sh. No satellites to review (0 held).**

Rocket entered today with 9 sh IWM, bought 1 more at market_open to cure a 13.7% cash
breach (no satellite confirmed after CSTL/AMCX review — see research_log.md), reaching
10 sh. By close IWM had drifted to $2,910.90 (5.65% over the $2,739.32 core target,
band is 3%). Sold 1 sh @ $291.11, landing 9 sh / $2,619.99 (3.92% under target) — closer
to target than staying at 10, consistent with lesson 7a. Same whole-share
back-and-forth as 7/28 and 7/30; still an open thread for weekly_review (fractional
IWM orders would fix this permanently).

**Performance**: Rocket +0.35% since rebase vs SPY +0.74% → **-0.39%**. IWM's -0.53%
day (vs SPY +0.85%) is almost the entire gap — the core-factor bet cutting hard
against Rocket today, not a stock-picking failure (0 satellites held, nothing to pick).

**No satellites reviewed** — CRM/JPM/SCHW are Bull's, SPY (4 sh) remains unattributed.
ntfy daily summary sent and confirmed.

**Open threads carried to weekly_review**: (1) premarket schedule fired 85 min late
today; (2) SPY 4 sh still UNATTRIBUTED at the broker; (3) whole-share IWM granularity
keeps re-triggering band breaches both directions — consider fractional orders; (4)
CSTL/AMCX dilution checks still unrun, carry into Monday premarket.

---

---

## 2026-07-31 — Premarket (Friday) — ⚠️ RAN 85 MINUTES LATE

**Decision: watchlist built, no trades (market was already open; instruction was no-trade).**

🚨 **The session started at 10:04 AM ET, with the market open and the 9:45–9:50 base window
already gone.** The whole premarket framework assumes it runs before 9:30. Today's bases were
therefore read *after the fact* from raw 5-min bars rather than traded live. **Second
consecutive operational failure** (7/30 = `close --qty` full liquidation). Both go to
weekly_review; the premarket job's schedule needs checking.

**Two genuine satellite candidates — best catalyst quality of the week:**
- **CSTL** (HIGH, 13 sh ≈ $378): real beat-and-raise. Q2 rev $103.5M +20% YoY vs ~$86M est,
  EPS -$0.07 vs -$0.44, **FY guide raised $345–355M → $365–375M**, TissueCypher volume +63%.
  34% below its 52-wk high, $42.78 street target, strong_buy. Gap +8.4% (well inside the
  chase limit). Base **held**: 9:45 pullback to $28.59 came on the session's *lightest*
  volume (15k), 9:50 reclaimed to $29.66 on *rising* volume (25k) = accumulation. Entry
  level **$28.60**. Short float only 4.8% — no squeeze kicker. Caveat: still GAAP-unprofitable,
  reimbursement risk is the real bear case, and dilution was NOT verified.
- **AMCX** (MEDIUM-HIGH, 35 sh ≈ $390): the quarter **missed both lines**, but the catalyst is
  a **$500M / 5-yr Netflix Walking Dead licensing deal** + raised FY guide. **21.1% short
  float** (above the rule-6 bar) breaking to a **52-week high** on six straight accumulation
  bars to HOD — the better tape of the two. Entry level **$10.83**. But revenue is -8.8% YoY,
  street target is **$7.50 vs $11.13 spot**, consensus `underperform`. Momentum/squeeze trade,
  not an investment — do not hold past the momentum.

**REPL was the hardest skip yet and the rules held.** FDA AdCom voted **10–3 in favor** of RP1
in advanced melanoma 7/30, overruling FDA staff after two prior rejections — a top-tier
catalyst. Halted all Thursday, opened **+98%**. Skipped on three independent grounds: 2.8x the
35% chase ceiling, a **PDUFA binary on 8/02**, and already fading below its own open.

**Other skips**: JFB (both-scanner name, but the "catalyst" is a progress update on a
February-signed de-SPAC — opened near the high and distributed every bar), CAPR (bounce off a
-36% two-day collapse), DUOT (opened at the day's high, never revisited it).

**Account**: slice $3,023.60, IWM 9 sh = $2,607 (86.3%), **cash back to 13.7% — breach
re-opened** by Thursday's close landing on 9 shares plus IWM's -1.0% drawdown. A satellite is
the correct cure, not another IWM top-up.

**Performance**: Rocket **-0.27%** since rebase vs SPY **-0.15%** → **-0.12%**. Thursday's
+0.61% edge fully reversed in one session because IWM fell -1.02% vs SPY -0.10%. That is the
IWM-vs-SPY factor bet cutting the other way — it was never skill in either direction.

**Open threads**: (1) premarket schedule; (2) **SPY 5 sh / $3,705 still UNATTRIBUTED** at the
broker — reconciler does not balance; (3) dilution check unrun on CSTL and AMCX.

---

---

## 2026-07-30 — Market Close (Thursday, ~4:00 PM ET / 19:58 UTC)

**Decision: Trimmed oversized IWM core 10 sh → 9 sh. No satellites to review (0 held).**

Rocket held only IWM (10 sh, bought up to that count at this morning's market_open to
cure the cash breach). By close, IWM's rally had pushed it to $2,926.90 — **6.5% over**
the 90%-of-slice core target ($2,729.47, 0 satellites) — so Step 2.5 called for a trim.

**Operational error, caught and corrected same session**: `alpaca_client.py close IWM
--qty 1` does not support partial quantities — `close` always fully liquidates via
`DELETE /v2/positions/{symbol}` and silently ignored the `--qty` flag, selling all 10
shares. Caught immediately via `positions`, corrected with `buy IWM 9` (the right
command for exact quantities). Net result matches original intent (9 sh, ~3.1% under
target — closest achievable given whole-share granularity, same tradeoff as lesson 7a)
but took two orders instead of one. Full detail in trade_log.md; rule change (`sell
SYMBOL QTY` for partial reductions, `close` only for full exits) logged in
lessons_learned.md item 11.

**Stats**: SPY +1.71% today (strong rally, consistent with the cooling core-PCE print).
Rocket's slice ~+1.14% today (~$2,998.57 premarket → $3,032.73 close). Since 7/20
rebase: Rocket +0.03%, SPY -0.02%, Rocket vs SPY **+0.04%** — cumulative outperformance
intact, though today in isolation likely lagged SPY's rally since only ~87% of the
slice was in small-cap beta and cash/rebalancing friction ate a bit more.

**Watchlist for tomorrow**: CMCO (real Q1 beat + 28% short float, watch for a clean
post-earnings-call base after today's spike-and-fade) and BOOM (genuine beat-and-raise,
failed today's base — watch for pullback per the missed-catalyst rule). Nothing
confirmed yet; conviction MEDIUM.

**Trades this week**: IWM core activity only (7/28 buy, 7/30 fallback buy, 7/30
rebalance trim). 0 satellite trades. ntfy summary sent and confirmed. Pushed to git.

---

---

## 2026-07-29 — Market Close (Wednesday, 4:01 PM ET / 20:01 UTC)

**Decision: No action. Hold IWM overnight. Core rebalance DEFERRED to tomorrow premarket.**

Rocket: 1 position (IWM 9 sh @ $291.50 entry, -1.1% today), 0 satellites, 0 trades this session.

**FOMC outcome**: Fed held at 3.50-3.75% as priced (62% pre-event). Statement neutral; no hawkish surprises. Market down broad (small caps -1.1% with Russell 2000). Rocket -1.34% since rebase vs SPY -1.69% → **+0.35% outperformance**, mostly from IWM core staying invested vs benchmark pull-down.

**Satellite candidates (NEO, VRRM) both failed entry confirmation:**
- NEO (+11.9% gap) — checked open base 9:45–9:50, volume did NOT exceed 1.5x avg. No entry.
- VRRM (+20.3% gap at the chase limit) — checked open base, volume insufficient + no CEO after May collapse. No entry.

**Core rebalance:** Rocket slice $2,990.98; IWM $2,594 (86.7%); cash buffer $397 (13.3%). Target core ~96% → deficit $98 (just outside the 3% no-churn band). Market closed at 4:01 PM → no trade executed. **PRIORITY for tomorrow premarket**: Buy 1 IWM share (~$288-290) to deploy buffer and reach 96% deployed / 4% cash. This cures the mandate breach flagged in research_log.md PRIORITY 1.

**Trades this week**: 1 (IWM 7/28) / 5 max. Scan count: NEO, VRRM confirmed to satisfy universe filters; no other fresh catalysts in the session.

---

---

## Session Archives

- July 2026: `memory/archive/session_notes_2026-07.md`
- June 2026 (05-25 → 06-16): `memory/archive/session_notes_2026-06.md`
- May 2026: `memory/archive/session_notes_may2026.md`
