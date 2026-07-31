# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Friday 2026-07-31  ← CURRENT

🚨 **THIS SESSION RAN LATE — 10:04 AM ET, market already open.** The premarket routine
fired ~85 minutes behind schedule and the **9:45–9:50 base window had already passed**
before any analysis existed. Per instruction no trades were placed. This is the second
consecutive session with an operational failure (7/30 was the `close --qty` full
liquidation). **Raise at weekly_review: check the cron/schedule for the premarket job.**
All price action below is therefore *observed*, not *anticipated* — the bases were read
after the fact, which is a weaker form of the same test.

**Tape**: **VIX 17.54 (+2.63%)** — low, no sizing restriction. **10-yr 4.73% (+1.42%)** —
a real jump, the hawkish read of Thursday's PCE showing up in rates. Futures: S&P -0.05%,
Nasdaq +0.27%, **Russell 2,934.20 -0.68% — small caps are the weak side today.** Thursday
closed **IWM 289.62 -1.02%** vs **SPY 740.96 -0.10%**: small caps underperformed large by
~0.9% in a single session, which is what a rate back-up does to the Russell. **Brent
$90.16 (+1.27%), WTI $85.43 (+2.20%)** — crude still extending. Gold -0.43% (hedge bid
came off). Dollar 100.39 (+0.38%). Today's calendar: **Employment Cost Index 8:30 AM**
(already out), **Michigan Consumer Survey final 10:00 AM**. No tier-1 event left.

**Positions**: Rocket holds **IWM 9 sh = $2,607 (86.3% of slice)**. Slice **$3,023.60**.
Free cash **$414 (13.7%)**. JPM + SCHW are Bull's. ⚠️ **SPY (5 sh, $3,705) is still
UNATTRIBUTED** at the broker — reconciler does not balance; do not size against it.
Pooled cash $1,138.86. Max satellite = $453 (15%), 1.5% risk = $45. Satellite trades this
week: **0 / 5** (the IWM prints are core, they don't count).

⚠️ **Cash breach is BACK at 13.7%.** It was cured Thursday morning (10 IWM sh) and then
re-opened Thursday afternoon by the market_close rebalance landing on 9 shares, plus
IWM's -1.0% drawdown shrinking the core. Whole-share granularity keeps re-creating this
(lesson 7a). **A satellite entry cures it properly — that is the point of the sleeve.**

---

### PRIORITY 1 — Satellite candidates. Two real ones, first time this week.

Both names cleared **every universe gate in one `eligibility` call** and both carry a
dated, verifiable 7/30 catalyst. Neither is a scanner artifact — both were confirmed
against raw yfinance 5-min bars (lesson 10).

## CSTL — Castle Biosciences — Q2 beat AND raised FY guidance, 7/30
- **Catalyst**: Q2 2026 reported 7/30. Revenue **$103.5M, +20% YoY vs ~$86M consensus**;
  EPS **-$0.07 vs -$0.44 est** (beat by $0.37); adj. EBITDA **+$12.4M** (vs $10.4M PY).
  **FY26 revenue guide RAISED to $365–375M from $345–355M.** TissueCypher test volume
  **+63% YoY**, FY volume-growth guide lifted to 50–52%. This is a genuine **beat-and-raise
  on an accelerating growth business** — not a recovery off a low base like BOOM.
- **Market cap**: $881M ✓ | **Float 27.0M** ✓ | **Short float 4.8%** — no squeeze fuel
- Avg vol 383–408k ✓ (thin, but $400 of size is a non-issue) | NASDAQ ✓ | US (Friendswood, TX) ✓
- Above **MA20 $24.52** and **MA50 $22.69**. **-34.4% from the 52-wk high $44.28**;
  analyst target **$42.78 (+47%)**, consensus **strong_buy**. **Not priced in.**
- **Observed price action**: prior close $26.79. Opened **$28.75 (+7.3%)**, spiked to
  **$30.81 (+15%)** on the 9:35 bar, sold back to a **$28.59 low on the 9:45 bar (15k, the
  lightest volume of the session)** — then the **9:50 bar reclaimed to $29.66 on rising
  volume (25k)**. Light-volume pullback, higher-volume reclaim = **accumulation, base
  HELD.** 192k traded in the first 35 min against a 408k daily average (~4x pace).
- **Entry plan**: +8.4% is comfortably under the 20% chase limit — clean gap-and-go.
  Valid entry on a hold above **$28.60** (the 9:45 base low). A break below $28.60 on
  volume kills it.
- **Stop**: **$27.01** (7% below $29.04)
- **Target**: +15% ≈ **$33.40** (sell 1/3) | +25% ≈ **$36.30** (sell 1/3) | trail final 1/3
- **Size**: `alpaca_client size` returns 15 sh / $436 / 14.4%, but that exceeds the $414
  free buffer. **Take 13 sh ≈ $378 (12.5%)** — no IWM sale needed, cash 13.7% → **1.2%.**
- **Conviction: HIGH** — the best-quality satellite setup Rocket has seen since the core
  went on. Beat, raise, growth acceleration, room to the 52-wk high, and a base that held.
- **Risk / what kills it**:
  ⚠️ **Still unprofitable on a GAAP basis** (-$0.07 EPS, forward P/E -30.4). The beat is a
  smaller loss, not a profit.
  ⚠️ **Diagnostics = reimbursement risk.** A single adverse CMS/MolDX coverage decision on
  TissueCypher or DecisionDx re-rates this name overnight. That is the specific bear case.
  ⚠️ **383k avg volume is the thinnest name Rocket would hold.** Fine at $378; would not be
  fine at 5x that.
  ⚠️ Already +18.8% over 5 days and +17.5% on the month — some of the move predates the print.
  ⚠️ **Dilution not verified** — no offering/ATM search was run before the window closed.
  **Verify before any entry.**

## AMCX — AMC Global Media — $500M Netflix licensing deal + raised FY guide, 7/30
- **Catalyst**: Q2 reported 7/30. The quarter itself **MISSED both lines** (EPS -$0.28 vs
  -$0.07 est; revenue $547.5M vs $555.7M est). The catalyst is the deal announced with it:
  a **five-year, co-exclusive global Netflix licensing agreement for the entire Walking
  Dead universe — all 7 series, 371 episodes, $500M in contracted fees**, ~$200–225M
  recognized in *each* of 2026 and 2027. **FY26 guide raised**: revenue $2.4–2.45B, adj.
  operating income $410–420M, FCF ~$220M.
- **Market cap**: $489M ✓ | **Float 29.6M** ✓ | **Short float 21.1%** ✓✓ — **above the 15%
  bar. This is the squeeze candidate** (standing rule 6).
- Avg vol 589k ✓ | NASDAQ ✓ | US ✓ | above MA20 $10.20 and MA50 $9.94
- **52-wk range $5.41–$11.20 — it is trading at $11.13, 0.6% off the 52-week HIGH.**
  A 21% short base watching a breakout to new highs is real squeeze fuel: **no overhead
  supply above.**
- **Observed price action** — the better tape of the two. Prior close $9.71. Opened
  **$9.93**, then **six consecutive bars of accumulation** into the high: 10.65 → 10.87 →
  10.95 → 11.02 → 10.98 → 11.02 → **11.11**, on *heavy, sustained* volume (73k / 65k / 50k /
  42k / 27k). **No spike, no fade — a stair-step to HOD.** 350k in 35 min vs 589k avg.
  Note Thursday's shape: it **gapped DOWN to $8.97 on the miss and closed $9.71** — the
  market sold the quarter, then re-read the deal. Today is that re-rate.
- **Entry plan**: +14.6% is under the 20% chase limit. Valid entry on a hold above
  **$10.83** (the 9:40–9:55 consolidation floor). This is a 52-wk-high breakout — a close
  back under $10.83 is the failure signal.
- **Stop**: **$10.35** (7% below $11.13)
- **Target**: +15% ≈ **$12.80** (sell 1/3) | +25% ≈ **$13.91** (sell 1/3) | trail final 1/3
- **Size**: max is 40 sh / $445 / 14.7%, above the free buffer. **35 sh ≈ $390 (12.9%)**
  standalone. Taking **both** CSTL and AMCX requires selling **2 IWM shares (~$579)** —
  explicitly permitted ("fund satellites by selling core"), and the cleanest use of the
  sleeve all week.
- **Conviction: MEDIUM-HIGH** — ranked below CSTL on business quality, above it on tape.
- **Risk / what kills it**:
  ⚠️ **The quarter missed both lines and revenue is -8.8% YoY.** This is a secularly
  declining cable-network business; the Netflix deal is a **one-time licensing windfall,
  not growth.** Strip the ~$200M of Netflix revenue recognition and the raise mostly
  disappears.
  ⚠️ **Analyst target is $7.50 — 33% BELOW spot — and consensus is `underperform`.** Read
  one way this is squeeze fuel (bears are positioned into a breakout). Read the other way,
  the street thinks fair value is $7.50 and this is an $11 stock. **Both readings are true;
  that is what makes it a trade and not an investment. Do not hold it past the momentum.**
  ⚠️ **At the 52-week high with no support beneath** — if the breakout fails there is
  nothing until the MA20 at $10.20, an 8% air pocket that clips the stop.
  ⚠️ AMC-family balance sheets carry real leverage; verify no refinancing/offering pending.

---

### Hard skips today

- **REPL +98%, 15.4x RelVol — NO ENTRY AT ANY PRICE, despite a genuinely major catalyst.**
  FDA Cellular/Gene Therapies AdCom voted **10–3 in favor** of RP1+nivolumab efficacy in
  advanced melanoma on 7/30, overruling FDA staff and reversing two prior rejections.
  Stock was **halted all day Thursday** (0 volume, $5.41) and opened today at **$11.38**.
  Three independent disqualifiers: (1) **+98% is 2.8x the 35% chase ceiling**; (2) the
  **PDUFA decision is 2026-08-02 — a hard binary in 2 days**, and Rocket does not hold
  through binaries; (3) it is already **fading below its own open** ($11.38 → $10.73).
  This is the fifth time the >20% chase rule has been tested by a top-tier catalyst and it
  holds. Re-examine only after the PDUFA resolves and a real base forms.
- **JFB +13.5%, 5.9x RelVol — SKIP. Appeared in both scanners; the catalyst does not
  survive inspection.** The 7/30 release is a *business-combination progress update* with
  XTEND (drone/robotics), a deal signed back on **2026-02-17** and not closing until Q3.
  The headline numbers ($27M of XTEND defense orders, a "$500M+ pipeline", the DoW drone
  program) belong to the **target, not to JFB**, and a de-SPAC-style close means share
  issuance. Price action confirms: opened $4.03, spiked **$4.48 on the 9:35 bar, then faded
  every bar to $4.08** on declining volume (124k → 42k → 40k → 49k → 41k → 14k → 8k).
  **Opened near the high and distributed — failed base.** Merger-progress PR is not a
  dated catalyst.
- **DUOT +8.4% — SKIP on price action alone.** **Opened at $9.34, which was the high of the
  entire day**, and immediately broke to $8.67. Never traded above the open again. Textbook
  failed gap; no catalyst research spent.
- **CAPR +4.3%, 6.0x RelVol — SKIP, falling knife.** Crashed **-36% on 7/30** ($6.57 →
  $4.19, low $2.96) after running to $7.85 on 7/27. Today's +4.8% is a bounce off a
  two-day collapse. ABAT precedent (lesson 2026-06-09): a real catalyst does not make a
  knife catchable. No long here.
- **STI +8.3%, ROLR +6.1%, CLNN +3.6%, GMRS +3.4%, FJET +3.2%** — all print **RelVol
  ≤0.2x.** No volume = no catalyst confirmation. STI, CLNN and FJET are also already on the
  standing avoid list. Drift, not catalyst.
- **BIOA -60.6%, MYGN -42.0%, GLUE -31.8%, FLGT -18.4%** — the four biggest volume prints
  on the board are all **large healthcare DECLINES**. Not longs. Noted as tape color: this
  was a brutal session for small-cap diagnostics/biotech, which is a live caveat on CSTL
  (a diagnostics name) — the sector is being repriced hard around it.
- **ASAN, VPG, AI, MYE, DXC, SAFE, SHAZ, PGY, BJRI, UPBD** — pass on cap but all print
  <1.5x RelVol and carry no dated catalyst. IGR / HIX / ECAT are closed-end funds, not
  operating companies.
- **BOT -7.8%** — already on the standing avoid list (closed-end fund, repeat placements).

### Scheduled / still pending (no action)
- **REPL PDUFA — 2026-08-02.** Not a trade, but the single biggest small-cap binary on the
  calendar. Watch how it resolves; an approval + orderly base is a legitimate week-2 setup.
- **CSTL / AMCX**: both just reported — earnings risk is behind them.
- **URGN**: UGN-103 NDA still NOT filed — guidance Q3/2H 2026. Watch for the filing PR.
- **BLFS**: Q2 confirmed **Aug 6, 2026**. **CAPR** earnings 8/11.
- **BOOM / CMCO / XRX** (7/30 names): BOOM failed its base and was correctly skipped; CMCO
  and XRX both exceeded the chase ceiling. None shows a fresh trigger today. **Removed.**

**Verdict**: Two real satellites for the first time this week, and the cash breach has an
honest cure that isn't another IWM top-up. **Ranked: CSTL first (13 sh ≈ $378) on catalyst
quality, AMCX second (35 sh ≈ $390) on squeeze setup and superior tape.** Taking both means
selling 2 IWM shares — permitted and appropriate. **But the base window is gone and both
names are extended off their bases as of 10:05 AM.** Do not chase either one into midday;
if the entry levels ($28.60 / $10.83) are lost, there is no trade and the fallback is the
core, not cash. Verify dilution on both before committing — that check did not get run.

---

## Skip / Avoid List (standing)

| Symbol | Reason |
|--------|--------|
| DFNS | 1-for-125 reverse split to hold Nasdaq listing → 0.3M manufactured float; $27.1M net loss on $3.65M revenue; **$20M private placement** (active dilution). HARD AVOID. |
| DRUG | Active dilution (Jan $175M offering @ $90 + ATM on file) + ~1,500% YTD pump profile. HARD AVOID. |
| BOT | Closed-end fund, not an operating small cap; repeated private placements = active dilution. HARD AVOID. |
| WOLF | Active S-1 dilution overhang + distressed recovery name. AVOID. |
| STI | Going-concern doubt, defaulted note, ~$85K Q1 revenue. HARD AVOID. |
| BNAI | Promotional AI hype; dilutive equity commitment below market. AVOID. |
| FULC | Dead-cat bounce, 85% workforce cut, shareholder lawsuits. HARD AVOID. |
| CAST | Going-concern/$93k-revenue pump. HARD AVOID. |
| TLSI | Securities-fraud investigations + guidance cut. HARD AVOID. |
| BKSY | $250M ATM equity program (active dilution). AVOID. |
| SPCE | Space theme dead. AVOID. |
| QMCO / CLNN / FJET | Dilution (private placement / convertible / ATM). Skip per standing rule. |

---

## Entry Framework Reminders

- **Universe**: Market cap $50M–$2B, price >$3, NYSE/NASDAQ, avg vol >300k, US-domiciled.
- **Chase rule**: Never enter >20% above prior close. +20–35% = gap-and-go on 10-min base.
  +35%+ = wait for second-day/pullback entry (within 10% of prior close).
- **Volume**: Only enter if volume >1.5x avg in first 5–10 min (9:45–9:50 base confirmation),
  read off **raw 5-min bars**, never the scanner's one-line RelVol (lesson 10).
- **Dilution rule**: Skip any name with an announced offering / ATM / convertible closing
  within 2 weeks.
- **Sizing (pooled ~$10k shared account)**: Rocket slice = 30% (~$3,024). 15% max position
  ≈ $453; 1.5% risk ≈ $45. Use `alpaca_client.py size SYMBOL ENTRY STOP`. Verify free
  pooled cash first — and note the script's max may exceed Rocket's free buffer.
- **Partial trims use `sell SYMBOL QTY`** — `close` always fully liquidates (lesson 11).
- **Stop**: 7% trailing stop set immediately at entry (atomic with buy). Core carries none.
- **Targets**: +15% (lock 1/3), +25% (lock 1/3), trail final 1/3. **Log every exit same-day.**
- **No new entries after 3:30 PM ET. Max 4 satellites, max 5 satellite trades/week.**

---

## Recently Resolved Ideas

| Symbol | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| MRLN | $8.88 (1,670 sh, Jun 5) | $8.90 (Jun 5) | +$33.40 (+0.23%) | Defense catalyst real; hit +15% target then chopped back. Lesson: lock 1/3 at first target. |
| CAMP | $4.85 (3,093 sh, Jun 16) | UNRECOVERABLE | Unknown | Closed pre-7/20 merge; exit never logged, gone from Alpaca history. See trade_log.md + lessons item 9. |
