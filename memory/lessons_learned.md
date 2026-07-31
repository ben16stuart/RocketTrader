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

## Rules From Real Trades

### 2026-07-31 — Week 31: zero satellites, and the skips were right
- ✅ **Entry triggers work even when the session doesn't.** CSTL's trigger was a hold above $28.60; it **closed $28.00**. The base broke, so the rule would have kept Rocket out regardless of the late session. A missed *setup* is not automatically a missed *trade* — check where it actually closed before calling it a miss.
- ✅ **The dilution rule keeps paying.** SOC looked like the week's cleanest energy momentum name (+18.1%, 1.9x RelVol) until a single search found $93M of stock being sold **at $3.08** plus $289M of converts. One lookup, one disaster avoided.
- ❌ **The only real miss was AMCX** — it held every level the plan named and closed at its 52-week high. Lost to infrastructure (lesson 12), not analysis.

### 2026-06-05 — MRLN (+$33.40, +0.23% position, Rocket's first trade)
- ✅ **Second-day entry framework WORKS**: gapped +32% after-hours on a USSOCOM defense milestone; entered next morning at $8.88 within 10% of prior close; hit $10.25 (+15%).
- ✅ **Defense catalysts are reliable** — government milestones on aerospace/defense small caps deserve full size.
- ❌ **PROFIT-TAKING DISCIPLINE**: hit the +15% target and was NOT scaled, then round-tripped to a $8.90 exit while the stock closed $9.10. **Sell 1/3 at +15% and 1/3 at +25%, immediately, per plan.** Targets exist to be used.
