# Rocket Lessons Learned

Rules derived from real trades. Read every session.
Older observations: `memory/archive/lessons_history.md`.

---

## Standing Rules

1. No catalyst = no trade. Period. Volume alone is not enough.
2. Gap 20–35% on confirmed catalyst = gap-and-go, NOT a chase. Enter on 10-min base (9:45–9:50). Gap >35% = wait for second-day entry.
3. Second-day rule: stock gapped >25% yesterday on real catalyst + closed strong → today's open IS the entry. Do not wait for a 20%+ pullback that will not come.
4. Small caps go quiet fast after a pop. Exit when volume fades, not when price falls.
5. Sub-$3 stocks are traps — bid-ask spreads too wide to trade profitably.
6. If short float >15% AND catalyst hits, size UP — squeeze moves are violent and fast.
7. **Missing real catalysts has a cost too.** Standing flat while APPS +78%, UMAC +52%, RCAT +33% all moved on confirmed catalysts = missed alpha. The goal is NOT to avoid all risk. Apply discipline on entry price, not on whether to trade at all.
7a. **Core rebalance band vs. whole-share granularity (2026-07-28).** IWM at ~$292 against a ~$3,040 slice makes one share **9.6% of the slice vs a 3% band** — the band is unsatisfiable by any whole-share move. Only trade a band breach if the nearest whole-share move lands *closer* to target than doing nothing. Root fix is fractional orders; `alpaca_client.py:68` sends integer `qty` only, so this needs a code change.
8. **Extreme moves (+100%+) with REAL catalysts are NOT noise** (XOS +172% AI power hub; LASE +300% Army anti-drone; REPL +107% FDA AdCom). BUT never chase the spike — watchlist it and wait 1–3 days for a pullback. The best catalysts often give second entries.
9. **Log exits the same day they happen — no exceptions.** CAMP was closed pre-merge with no exit price, date or reason ever recorded, and is now unrecoverable. **Every close must be paired with a same-session trade_log.md entry, and every routine must run or log an explicit skip reason.**
10. **Pull raw 5-min bars (`yfinance` `interval="5m"`) to judge a 9:45–9:50 base — never trust the scanner's one-line RelVol.** 2026-07-30 the scanner reported 1.4x and 14.8x for BOOM at the same moment. Only the raw bars showed it breaking *below* its base on rising distribution volume. Same technique caught CMCO and XRX opening spikes that exceeded the 35% ceiling before settling back. Default check before any gap-and-go entry.
11. **`alpaca_client.py close SYMBOL` always fully liquidates — it has no `--qty` flag and silently ignores one.** 2026-07-30: `close IWM --qty 1` sold all 10 shares (it calls `DELETE /v2/positions/{symbol}`), leaving the core at 0% invested with no bearish thesis. **For any partial reduction use `sell SYMBOL QTY`; reserve `close` for intentional full exits.** Verify `qty` in the order JSON before assuming a trim worked.
12. **🚨 Token budget is a TRADING risk, not a housekeeping concern (2026-07-31).** Rocket's premarket fired on time at 6:20 AM ET, then hit `You've hit your session limit` on opus **and again on the sonnet fallback**, finishing at 10:05 AM ET — after the base window. **Cost: the AMCX entry** (closed +15.3% at its 52-week high, above its stated trigger). Rocket and Bull share one Claude quota across 10 launchd routines. **Spend tokens like they are the trading day, because they are.** Obey the subagent rules in CLAUDE.md literally: <5 searches → inline, never a subagent (measured overhead ~171k tokens *each*).
13. **A launchd plist that exists is not a job that runs — verify it is LOADED (2026-07-31).** `com.benstuart.rocket.midday.plist` was authored 7/22 and scheduled for 12:15 PM ET, but never appeared in `launchctl list` and **never wrote a single log line.** The midday routine has never executed. Nine days of "re-check at midday" plans silently did nothing. **Check `launchctl list | grep rocket` against `ls ~/Library/LaunchAgents/` whenever a routine's output seems missing** — absence of a log file is the tell.

14. **A metric that renders as `nan` is a silent failure — treat any non-numeric output as a
    broken instrument, not a cosmetic glitch (2026-08-04).** `portfolio_snapshot.py` printed
    `SPY return since rebase | +nan%`, i.e. **Rocket had no benchmark comparison at all** —
    the one number that measures whether it is doing its job. Cause: premarket, yfinance
    returns today's forming bar with volume but a **NaN close**, and `get_spy_return()`
    indexed `Close.iloc[-1]` blindly. `get_spy_daily_return()` (used by market_close) had the
    same flaw. Fixed by dropping unpriced bars. **Two generalisations**: (a) *any* yfinance
    `.iloc[-1]` close read premarket is suspect — the same NaN appeared on all 7 tickers
    checked that morning; (b) this failed **quietly, in a table cell**, exactly like the
    never-loaded midday plist in lesson 13. **Silent degradation is the failure mode that
    actually costs Rocket money — loud errors get fixed.**

15. **The 35%-extension gate is checked against the tape at decision time, not just the
    opening tick (2026-08-04).** AMRC's premarket plan set an explicit gate: open >$30.69
    (35% off prior close) = too extended, wait for second-day. Raw 5-min bars showed the
    *actual* open print was $31.93 (+40.5%) — the gate had already been breached before the
    plan's own 9:45–9:50 base window even started, and it then faded on heavy volume (84%
    of full-day avg in 15 min) rather than basing. Separately, BLZE opened at a compliant
    +29.1% but kept climbing to **+51.0%** by 9:45 — inside-the-band math at the open tick
    does not mean inside-the-band at the moment you actually decide. **Always compute the
    gap/extension off the realized open print (and current price if the tape kept moving),
    never the premarket-indicated price used to write the plan.** Zero trades resulted, but
    both names are legitimate second-day watches if they close strong.

16. **`smallcap_scanner.py` is a NAME SOURCE ONLY — never read a price or a percentage off
    it (2026-08-07).** Both `top_movers` and `unusual_volume` returned **`+0.0%` for every
    single row**, so `top_movers` was a ranked list of zeros and the both-list overlap tier
    produced nothing for a fourth straight session. Worse, several *prices* were wrong
    against raw daily bars — it quoted **STLN $6.67 against a $4.99 close** and **CVRX $3.41
    against $5.94**. A number that is merely *wrong* is more dangerous than one that errors,
    because it renders as a plausible cell (lesson 14, same failure mode). **The entire
    tradeable board that day came from (a) raw yfinance daily bars on carry-over names and
    (b) the live premarket gainers page** — neither of which is the scanner. Standing
    procedure: pull raw daily bars for carry-overs and read the live premarket gainers list;
    use the scanner only to surface tickers worth checking.

17. **Rank on the BALANCE SHEET when the board is all earnings prints (2026-08-07).** Six
    fresh prints screened; **three died on funding structure** (SVCO's undisclosed $10M
    convertible on $13.0M cash, STLN's 0.1% EBITDA margin on $41.1M cash, NNBR's $3.06 PIPE)
    and one on a **guide cut** (CVRX). QNST won Priority 1 not because its growth was
    highest but because **$130.9M of operating cash flow makes the dilution question moot by
    construction.** Growth rate is what makes a stock gap; funding structure is what decides
    whether it holds the gap over a 1–5 day hold. **A GAAP-profitable small cap with real
    cash flow is a structurally different — and rarer — bet than a fast-growing one that
    still needs the equity market.**

18. **Compute the $2B universe ceiling against the PREMARKET price, not the prior close
    (2026-08-07).** `eligibility` passed **FIGS** at a $1,878M cap — but that is the cap at
    its $11.24 *close*; at its **$14.25 premarket print it is ~$2.38B, out of universe before
    the bell.** The command reads the last close, so on a gapper the gate it reports is stale
    by exactly the size of the gap. Same arithmetic retired **APPS** as untradeable despite
    the best chart on the board: a $1,727M cap puts ejection at ~$16.55, so its **+25% target
    sits outside the universe** — a position that cannot be held to its own plan is not a
    position worth opening. **Always re-derive cap at the price you would actually pay, and
    check that the +25% target still clears the ceiling.**

19. **"Unverified-but-no-flag" is a to-do, not a pass — close it before the open, not
    after (2026-08-07).** Premarket left STLN's dilution check half-run (SEC 403'd the
    8-K). One search at market_open found an active **$15M ATM facility (424B5)** — live
    authorization to sell stock into exactly the kind of spike STLN was having. Same
    structural pattern as SOC and SVCO, both HARD AVOIDs. **A 403 or a paywall is not a
    clean bill of health; it just means the check moved to the next session.** If a
    dilution check is still open when a session ends, it must be the first thing resolved
    at the next session before any order — it very nearly got skipped because the stock's
    tape looked strong.

## Rules From Real Trades

### 2026-08-07 — Week 32: NFP day, both ranked ideas broke on contact with the open
- ✅ **The dilution check paid for itself a second time.** STLN's unverified ATM flag from
  premarket resolved to CONFIRMED with one search at the open — see lesson 19. Passing
  cost nothing; trading it risked a live equity raise into the position.
- ✅ **Extension gates keep doing their job even when barely breached.** QNST never
  technically closed above its 35% gate, but tapping it intraday while the analyst target
  was already exceeded was enough to kill the trade on risk/reward alone — the gate does
  not need to be breached to be disqualifying, just exhausted.
- **Net result**: flat session, IWM core unchanged. Zero satellites for a second straight
  session — not from lack of catalysts, but from both of this week's best-screened ideas
  failing a structural check (balance sheet, extension) rather than a catalyst check.

### 2026-07-31 — Week 31: zero satellites, and the skips were right
- ✅ **Entry triggers work even when the session doesn't.** CSTL's trigger was a hold above $28.60; it **closed $28.00**. The base broke, so the rule would have kept Rocket out regardless of the late session. A missed *setup* is not automatically a missed *trade* — check where it actually closed before calling it a miss.
- ✅ **The dilution rule keeps paying.** SOC looked like the week's cleanest energy momentum name (+18.1%, 1.9x RelVol) until a single search found $93M of stock being sold **at $3.08** plus $289M of converts. One lookup, one disaster avoided.
- ❌ **The only real miss was AMCX** — it held every level the plan named and closed at its 52-week high. Lost to infrastructure (lesson 12), not analysis.

### 2026-06-05 — MRLN (+$33.40, +0.23% position, Rocket's first trade)
- ✅ **Second-day entry framework WORKS**: gapped +32% after-hours on a USSOCOM defense milestone; entered next morning at $8.88 within 10% of prior close; hit $10.25 (+15%).
- ✅ **Defense catalysts are reliable** — government milestones on aerospace/defense small caps deserve full size.
- ❌ **PROFIT-TAKING DISCIPLINE**: hit the +15% target and was NOT scaled, then round-tripped to a $8.90 exit while the stock closed $9.10. **Sell 1/3 at +15% and 1/3 at +25%, immediately, per plan.** Targets exist to be used.
