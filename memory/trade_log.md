# Rocket Trade Log

Append-only record of all Rocket trades. Never delete entries.

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

