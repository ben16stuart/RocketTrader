# Session Notes

Running log of recent sessions. Keep the last 3–5 entries here.
Archive entries older than 7 days to `memory/archive/session_notes_YYYY-MM.md` during weekly_review.

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

## Session Archives

- `memory/archive/session_notes_2026-08.md` — August 2026
- `memory/archive/session_notes_2026-07.md` — July 2026
- `memory/archive/session_notes_2026-06.md` — June 2026
- `memory/archive/session_notes_may2026.md` — May 2026
