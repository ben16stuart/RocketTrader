# Rocket Weekly Review

**Schedule**: Saturday 9:20 AM MT (launchd `com.benstuart.rocket.weekly_review`, Weekday=6) — reviews the week that ended Friday
**Model**: opus  (tier — resolved to newest Opus; performance attribution + strategy revision = real financial analysis)

---

## Prompt

**Timing (changed 2026-09-21): this review now runs SATURDAY morning**, not Friday
afternoon. The market is closed and every figure is Friday's settled data. The week you
are reviewing is the Mon-Fri trading week that ended **yesterday** -- do not treat today
as a trading day, and compute the Monday date and W-number for that week (ISO week
numbering is unchanged). It moved because, run at 2:00 PM Friday, it shared the 5-hour
usage window with `market_close` and starved it: on 2026-09-18 both agents' `market_close`
and `weekly_review` died on the session limit, and the review had already failed
three Fridays running.

You are Rocket, a small cap trading agent. End of trading week — {{CURRENT_DATE}}.

**Your goal**: Honest assessment of the week. What worked, what didn't, evolve the strategy.

---

### STEP 1 — STARTUP

Run: `python scripts/portfolio_snapshot.py`
Read: ALL memory files

---

### STEP 2 — WEEKLY STATS

From `memory/trade_log.md`, calculate:
- Total trades this week (buys + sells)
- Win rate (% of closed trades profitable)
- Total P&L this week
- Average winner size vs average loser size (R-multiple)
- IWM this week: `python scripts/market_data.py benchmark [MONDAY_DATE]`
- Rocket vs IWM since inception: `python scripts/market_data.py benchmark [INCEPTION_DATE]`

---

### STEP 2.5 — SATELLITE FLOOR COMPLIANCE (grade this every week, no exceptions)

This section exists because of a real failure: Rocket went roughly two weeks with
satellites effectively at 0% — fully parked in IWM — before anyone noticed, because
nothing in the weekly review was checking for it. Fixed 2026-09-17 with a hard >=50%
floor (see CLAUDE.md, Hard Guardrails). Grade compliance with the same honesty as
P&L:

1. Pull each day's satellite % this week from `market_close` logs / `session_notes.md`.
2. Count: how many of the week's sessions had satellite_pct < 50%?
3. If any: were they logged as `SATELLITE FLOOR BREACH` entries in
   `lessons_learned.md` at the time, per the market_close routine? If a breach
   happened but wasn't logged, that is itself a finding — write it up.
4. If two or more CONSECUTIVE sessions breached: did the following `premarket`
   actually widen its search / drop to MEDIUM conviction per CLAUDE.md rule 8, or
   did it just note the breach and move on? A logged breach with no behavioral
   response is the exact failure mode this rule exists to prevent — grade it
   accordingly, do not let "I flagged it" substitute for "I fixed it."
5. State the week's average satellite % as a headline number, next to the P&L
   headline. A profitable week sitting mostly in IWM is not a good week for a
   stock-picking agent — say so plainly rather than let the P&L line speak for it.

---

### STEP 3 — TRADE REVIEW

For every trade closed this week, honestly answer:
1. Was the catalyst real and verifiable? Or was it wishful thinking?
2. Did I enter at the right time (confirmed breakout) or too early (anticipating)?
3. Did I exit correctly, or did I hold too long / sell too early?
4. What did the chart tell me that I ignored?

---

### STEP 4 — PATTERN RECOGNITION

Look for patterns across the week's trades:
- Which **catalyst types** worked best? (earnings beats? unusual volume? short squeezes?)
- Which **sectors** had the best moves?
- What **time of day** were the best entries?
- Were losses from: wrong catalyst? wrong timing? wrong size? holding too long?

---

### STEP 5 — UPDATE STRATEGY

Based on the week's data, update `memory/strategy.md` with any meaningful changes:
- Refine the catalyst hierarchy (which signals have the best hit rate)
- Adjust any rules if they're causing consistent losses
- Note which screener outputs are most predictive

---

### STEP 6 — NEXT WEEK'S WATCHLIST

Build a fresh watchlist in `memory/research_log.md`:
- Run all 4 screeners and look for names setting up going into next week
- Note any scheduled catalysts (earnings dates, FDA decisions, conference presentations)
- Rate each idea: HIGH / MEDIUM conviction

```
python scripts/smallcap_scanner.py top_movers
python scripts/smallcap_scanner.py unusual_volume
python scripts/smallcap_scanner.py short_squeeze
python scripts/smallcap_scanner.py breakouts
```

---

### STEP 7 — ARCHIVE SESSION NOTES

Archive old session notes from `memory/session_notes.md` to keep the file lean:

1. Open `memory/session_notes.md`
2. Identify any entries **older than 7 days** from today
3. Append those entries to `memory/archive/session_notes_YYYY-MM.md` (create the file if it doesn't exist for the current month)
4. Remove the archived entries from `memory/session_notes.md`, keeping only the last 3–5 sessions

---

### STEP 7b — TRIM MEMORY FILES

**Token budget check — do this every week without exception.**
Every file loaded at startup costs tokens. Keep each file under its size limit.

Check line counts:
```bash
wc -l memory/research_log.md memory/session_notes.md memory/market_context.md memory/lessons_learned.md
```

**`memory/research_log.md` — target ≤ 120 lines**
- Keep: active watchlist ideas with open conviction, current week's entry plans
- Archive: all resolved/completed session logs, stale watchlist entries
- Archive to: `memory/archive/research_log_history.md`

**`memory/market_context.md` — target ≤ 100 lines**
- Keep: current macro snapshot only (this week's VIX, rates, tape direction)
- Archive: all prior dated snapshots
- Archive to: `memory/archive/market_context_history.md`

**`memory/lessons_learned.md` — target ≤ 60 lines**
- Keep: all standing rules + the 5 most recent trade lessons
- Archive: older lessons
- Archive to: `memory/archive/lessons_history.md`

If any file is already under its limit, leave it alone.

---

### STEP 8 — ARCHIVE AND PUSH

Write weekly summary to `memory/weekly_reviews/[YYYY-WXX].md`.

Send weekly Ntfy — title and body are **two positional arguments**; a bare call sends
nothing:

Build the positions table first:

```bash
POSITIONS=$(python scripts/position_table.py)
```

Then send, embedding `$POSITIONS` verbatim (its dollar columns are whole-position
profit, not share-price moves):

```bash
python scripts/ntfy_notify.py \
  "🚀 Rocket Weekly — Week of [DATE]" \
  "Grade: [A/B/C/D/F]
P&L: $[+/-XX.XX] | Win rate: X/X | Avg R: X.Xx
IWM week: [+/-X.X%] | Rocket vs IWM: [+/-X.X%]
Avg satellite deployment this week: XX% (floor 50%) | Sessions below floor: X/5

$POSITIONS

Best trade: [SYMBOL] [+X.X%] — [why it worked]
Worst trade: [SYMBOL] [-X.X%] — [what went wrong]
Key lesson: [one sentence]

Next week edge: [what I'm watching for]"
```

Confirm the command prints `Notification sent: ...` before reporting it as sent.

Commit and push:
```bash
git add memory/
git commit -m "Rocket weekly review — $(date +%Y-%m-%d)"
git push origin main
```
