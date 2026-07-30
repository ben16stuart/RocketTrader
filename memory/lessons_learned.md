# Rocket Lessons Learned

Rules derived from real trades. Read every session.

---

## Standing Rules

1. No catalyst = no trade. Period. Volume alone is not enough.
2. Gap 20–35% on confirmed catalyst = gap-and-go, NOT a chase. Enter on 10-min base (9:45–9:50). Gap >35% = wait for second-day entry.
3. Second-day rule: stock gapped >25% yesterday on real catalyst + closed strong → today's open IS the entry. Do not wait for a 20%+ pullback that will not come.
4. Small caps go quiet fast after a pop. Exit when volume fades, not when price falls.
5. Sub-$3 stocks are traps — bid-ask spreads too wide to trade profitably.
6. If short float >15% AND catalyst hits, size UP — squeeze moves are violent and fast.
7. **Missing real catalysts has a cost too.** Standing flat for a full week while APPS +78%, UMAC +52%, RCAT +33% all moved on confirmed catalysts = missed alpha. The goal is NOT to avoid all risk. Apply discipline on entry price, not on whether to trade at all.
7a. **Core rebalance band vs. whole-share granularity (2026-07-28).** With Rocket's slice at ~$3,044 and IWM at ~$293/share, one share is ~9.6% of the slice — more than 3x the rebalance band. When the shortfall (3.24%) is just outside the band but the nearest whole-share trade would overshoot in the other direction by more (6.4%), skip the trade — the untraded state is closer to target. Don't mechanically "fix" a small band breach with a move that makes tracking error worse. Raised for weekly_review: widen the core band or use fractional IWM orders.
8. **Extreme moves (+100%+) with REAL catalysts are NOT noise.** XOS +172% on AI data center power hub launch = major theme, not pump. LASE +300% on U.S. Army anti-drone selection = real defense catalyst. BUT: Never chase the spike. Add to watchlist, wait for pullback/consolidation (1-3 days). The best catalysts often give second entries.
9. **Log exits the same day they happen — no exceptions.** CAMP (entered 2026-06-16, $4.85, 3,093 sh) shows OPEN in trade_log.md but was actually closed at some point before the 2026-07-20 account merge — no exit price, date, or reason was ever recorded, and it's now unrecoverable from memory alone. Also market_context.md and research_log.md went stale for over a month (last real update 6/16) through the 7/20 Bull-account merge and a research gap on 7/21–7/22. **Rule: every close_position call must be paired with a trade_log.md exit entry in the same session, and premarket/midday routines must run (or explicitly log a skip reason) every trading day** so gaps like this don't recur. Follow-up: pull Alpaca order history for CAMP to backfill the exit record during the next weekly_review.
11. **`alpaca_client.py close SYMBOL` always fully liquidates — it has no `--qty` flag
and silently ignores one if passed.** 2026-07-30 market_close: tried `close IWM --qty 1`
to trim 1 share off an oversized core position; it closed all 10 shares instead (DELETE
`/v2/positions/{symbol}` under the hood, per `close_position()` in alpaca_client.py).
Caught immediately via `positions` and corrected with a `buy IWM 9` rebuy, but for a few
minutes the core was at 0% invested with no bearish thesis — an unintended mandate
breach. **Rule: for any partial position reduction, use `sell SYMBOL QTY`. Reserve
`close` for intentional full exits only** (e.g. closing a satellite entirely). Verify
the resulting `qty` in the order JSON before assuming a partial trim worked.

10. **Pull raw 5-min bars (`yfinance` `interval="5m"`) to judge a 9:45-9:50 base — don't trust the scanner's single daily-change/RelVol number.** 2026-07-30: `smallcap_scanner.py detail BOOM` and `unusual_volume BOOM` reported wildly different RelVol (1.4x vs 14.8x) for the same stock at the same moment — a repeat of the 2026-05-26 finding. Only the raw bars showed the real story: BOOM opened with a spike to +35% then broke *below* the required $6.40 base level on rising (distribution) volume — a failed base the scanner's one-line summary would not have caught. Same technique caught CMCO and XRX opening spikes that briefly exceeded the 35% chase ceiling before settling into their reported daily-change %. Make this the default check before any gap-and-go entry, not just when scanner numbers look suspicious.

## Rules From Real Trades

### 2026-06-05 — MRLN (+$33.40, +0.23% position, Rocket's first trade)
- ✅ **Second-day entry framework WORKS**: MRLN gapped +32% after-hours on USSOCOM defense milestone. Entered next morning at $8.88 (within 10% of prior close per second-day rule). Stock hit $10.25 (+15% profit target). Entry framework validated.
- ✅ **Defense catalysts are reliable**: USSOCOM autonomy program milestone = hard catalyst with volume confirmation. Aerospace/defense small caps with government milestones deserve full position size (entered 14.8% vs 15% max).
- ❌ **PROFIT-TAKING DISCIPLINE NEEDED**: Stock hit first profit target ($10.25, +15%) but position was NOT scaled (no 1/3 sold at target). Position then pulled back to $8.90 exit (+0.23% captured) while stock closed at $9.10 (+22% available). **New rule: When position hits profit targets ($10.21 = +15%, $11.10 = +25%), IMMEDIATELY sell 1/3 at each target per plan. Lock in gains. Let final 1/3 ride with trailing stop.** Profit targets exist for a reason — use them.
- ❌ **Real-time exit logging is CRITICAL**: Position closed at $8.90 (12:09 PM) but exit was not manually recorded — likely trailing stop triggered during midday volatility. On future trades, monitor positions actively during first hour and log exits immediately when they happen.
- ✅ **Discipline after wins**: Closed first trade profitably (+$33.40). No forced afternoon trades. Cash is a position even after a win. Rocket +2.47% vs SPY -2.44% today = outperformance on first trade.

---

## Pre-Trade Observations (Standing Flat)

- **2026-06-10 midday**: Afternoon scanner showed movers (APPS +8.6%, ALTO +9.1%, HYLN +8.1%) but ALL were continuation plays from catalysts 3-7 days old (early June news). APPS already +139% over 30 days on Launchpad launch. ALTO on June 4 analyst upgrade. HYLN on early June Navy testing. **Lesson: Multi-day continuation without fresh catalyst = not a Rocket setup.** The "named catalyst" rule applies to timing — need FRESH catalysts (same-day or prior-day), not week-old news with residual momentum. Momentum ≠ catalyst. Standing flat on low-conviction continuation tape = correct discipline.
- **2026-06-09 close**: ABAT volume discipline decision VALIDATED. Stood flat at 9:35 AM when ABAT was $3.42 in perfect entry zone ($3.50-$3.80) but volume was only 0.2x avg (vs 1.5x required). Stock closed at $3.06 (-19.5% from prior high, below week lows). **Lesson reinforced: Volume confirmation is MANDATORY.** Even with intact catalyst (DOE grant + earnings beat still real), price without volume = distribution, not accumulation. Standing flat on failed volume check saved -10.5% loss from $3.42 entry to $3.06 close. Volume discipline is NOT optional.
- **2026-06-09 midday**: Two observations from afternoon scan:
  - **ABAT falling knife**: Yesterday +33% on dual catalyst (DOE grant + earnings beat). Today -19.5% to $3.06 (week lows, below MA50). **Lesson: Real catalyst ≠ automatic entry. Price action must confirm.** Even with intact catalyst (DOE grant still there, earnings still beat), if stock is at week lows with heavy selling pressure = falling knife. Wait for stabilization and base formation above key levels ($3.20-$3.40) before entry. Distribution vs accumulation matters.
  - **FCEL +21% same-day analyst upgrade**: Canaccord upgrade to BUY, PT $30 (from $12), data center catalyst thesis. Fresh catalyst TODAY. **Discipline reinforced AGAIN: "Never chase >20% gap" applies to same-day fresh-catalyst moves.** Added to watchlist for pullback entry. Patience > FOMO, even on hot AI data center theme.
- **2026-06-08 midday**: ABAT +33% on DOUBLE catalyst (DOE $115M grant reinstatement + Q3 earnings beat $7.8M vs $4.3M est, first positive gross margin). Highest quality catalyst of the week — government contract + earnings crush. But +33% = 1.65x the 20% chase limit. **Discipline reinforced: Even dual catalysts do not override the >20% chase rule.** Added to watchlist for pullback entry over next 1-3 days. Best catalysts often give second entries. Standing flat = correct.
- **2026-06-04 midday**: LODE +15.8% on valid insider buying catalyst (June 3), but already extended intraday = same-day fresh-catalyst chase. SKIP. PSNL/DNA/SPCE had no fresh catalysts (conference presentation/general momentum/meme volatility). Stood flat — no valid afternoon setups. Discipline reinforced: extended moves without proper entry setups = pass.
- **2026-06-02 ELMT miss**: Stood aside at 9:35 AM on weak volume (0.2x avg), but stock DID form valid 10-min base at $19.50-$20.00 zone (9:45-9:50) and ran to $21+ on volume (732.4K shares). Q1 beat + defense backlog catalyst was real. **Lesson: Early volume read (first 5 mins) is NOT final verdict. Market_open routine says "wait for 10-min opening base" — that means WAIT THE FULL 10 MINUTES, not dismiss at minute 5.** If plan says check at 9:50, check at 9:50. This was a valid missed entry, not a chase avoid.

---

## Observations From Standing Flat (Pre-Trade)

- **2026-05-29**: REPL +81.1% on FDA BLA resubmission path agreement (melanoma drug RP1, after TWO prior rejections in 2025-2026) = textbook major biotech catalyst. But +81.1% = 4x chase limit. Lesson reinforced FOUR TIMES now (ASPI Tue +19.6%, APPS Wed +54.9%, UMAC Thu +52.4%, REPL Fri +81.1%): **"Never chase >20% gap" applies to ALL intraday fresh-catalyst spikes, regardless of catalyst quality.** Even FDA reversals and Pentagon funding do not override the >20% rule. Wait for pullback/consolidation — the best catalysts often give second entries. Patience > FOMO.
- **2026-05-28**: UMAC +52.4% on WSJ Pentagon drone funding report (Trump admin direct funding, UMAC explicitly named, Powerus Phase II selection) = MAJOR fresh catalyst. But +52.4% = 2.6x chase limit. EXACT same pattern as APPS Wed (+54.9% earnings beat). Lesson reinforced THREE TIMES now (ASPI Tue +19.6%, APPS Wed +54.9%, UMAC Thu +52.4%): **"Never chase >20% gap" applies to same-day fresh-catalyst moves, not just overnight gaps.** Catalyst strength does NOT override entry discipline. Wait for pullback/consolidation — patience beats FOMO every time.
- **2026-05-27**: APPS Q4 earnings beat (EPS $0.16 vs $0.09 est) = textbook fresh catalyst. But stock +54.9% same-day = 2.7x the "never chase >20% gap" limit. Correct decision: skip today, add to watchlist for pullback. Even the best catalysts require discipline on entry price. Fresh earnings beats can consolidate/pull back for 1-3 days before next leg — patience pays.
- **2026-05-27**: ASPI held consolidation zone ($6.92 vs $6.64 Tue close) above $6.50 target, but dropped off unusual_volume scanner = volume faded. Lesson reinforced: "Small caps go quiet fast after a pop." Holding price without volume = not a valid entry. Volume confirmation is mandatory.
- **2026-05-26**: Scanner RelVol column unreliable two sessions running (Fri + Tue). Treat scanner as a starting universe filter only — must independently verify volume via news/quote source before sizing. Do not size up on a scanner row alone.
- **2026-05-26**: DXYZ pre-market mcap reading ($2.089B "above ceiling") was a scanner glitch. By midday the same scanner showed $987M, consistent with Fri close. Cross-check mcap with a second source before disqualifying on universe rules — but err on the side of skipping when in doubt (correct call this AM).
- **2026-05-26**: Fresh midday catalyst (ASPI Silicon-28 restart) at +19.6% intraday = NOT an entry. Same-day fresh-catalyst chases at extended price violate the "no chasing gaps >20%" spirit. Put on next-day watchlist for pullback setup instead.
