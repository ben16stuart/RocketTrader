# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Monday 2026-07-27 premarket

**Tape**: Risk-ON. VIX 17.58 (-5.4%), Russell 2000 futures +1.27%, Brent -7% after the
US–Iran pause. Small caps leading (R2K +20% YTD vs SPX +11%). Monday calendar is light —
but **FOMC Wed 7/29 2:00 PM + PCE Thu 7/30 + MSFT/META/AAPL/AMZN earnings** = the risk
window is Mon–Tue. Do not carry fresh size into Wednesday afternoon.

**Positions**: Rocket is FLAT. JPM is Bull's. Pooled cash $7,987.75; Rocket slice $3,037.66.
Max position ≈ $455 (15%), 1.5% risk ≈ $45.

**Catalyst breadth today is NARROW.** Two independent research passes surfaced exactly one
in-universe name. The premarket gainer tape is dominated by reverse-split shells and sub-$3
junk (LGHL, BIYA, DFNS, MTNB, SXTC, OMH, GMEX — all fail universe filters).

### 1. TRAX — First Tracks Biotherapeutics — anti-CD122 M&A read-through
- **Catalyst**: argenx to acquire **Forte Biosciences (FBRX) for $77/sh cash (~$2.2B)**,
  ~86% premium, for anti-CD122 antibody FB102 — announced **today 7/27**. TRAX's lead asset
  **ANB033 is also anti-CD122** → direct mechanism validation + hard takeout comp. FRESH.
- **Verified**: Fri close $35.52 | mcap **$1.24B** (in-universe, upper end) | avg vol
  **674,443** (>300k ✓) | Nasdaq, San Diego US ✓ | 34.89M shares out (low float ✓)
- **Premarket**: ~$43.00 (+21%) — thin (~6,300 sh), treat as soft. **Re-pull at 9:30.**
- **Entry plan**: gap is +21% = gap-and-go band, NOT a chase. Entry ONLY on a confirmed
  **9:45–9:50 ten-minute base** with **>1.5x avg volume**. No entry on the opening spike.
- **Stop**: 7% trailing, set atomically at entry (~$39.99 if filled $43.00)
- **Size**: 10 shares ≈ $430 (14.2% of slice) — verified via `alpaca_client.py size`
- **Targets**: +15% ≈ $49.45 (sell 1/3) | +25% ≈ $53.75 (sell 1/3) | trail final 1/3
- **Conviction: MEDIUM — LOW-side. Conditional pass by default.**
- **Risk / what kills it**:
  1. **$43 is ABOVE the 52-week high ($42.90) and AT consensus PT ($43.875)** — the gap
     prices in the entire street target. Zero analyst headroom. *(verified independently)*
  2. **Sympathy trade** — the catalyst is someone else's M&A. TRAX has no company-specific
     news; its own ANB033 celiac readout is not until fiscal Q4 2026. Sympathy gaps on
     third-party deals routinely round-trip by lunch.
  3. **Supply overhang** — 424B3 resale registrations (~10.5M sh, ~30% of shares out) from a
     $13.81 private placement. Those holders are up ~3x at $43. Not a 2-week-rule
     disqualifier (resale ≠ new offering) but a live seller risk into strength.
  4. Second pop on the same theme — already ran to $38.49 on the 7/9 FBRX data, then faded.
- **Short interest: UNVERIFIED** — could not source. Do not assume squeeze fuel.

### Hard skips today
- **FBRX +39% to ~$76** — cash deal at $77 = ~1% spread, upside capped, and $2.2B equity
  value exceeds our $2B cap. Do NOT chase it off a % gainer screen.
- **LVWR** (+86% Fri, Q2 rev +55%) — trades $1.22–$1.48, fails the $3.00 floor.
- **DFNS** +41% — 1-for-125 reverse split 7/20, ~$2–7M cap. Shell.
- **VEEE** +22% — catalyst stale (7/13 reverse-merger pivot), post-spike bleed, shareholder
  suit investigation.

### Scheduled / still pending (no action)
- **URGN**: UGN-103 NDA **has NOT been filed** — guidance still Q3/2H 2026. Confirmed no
  fresh Fri–Mon catalyst. Keep watching for the actual filing press release.
- **BLFS**: no pre-announcement; Q2 confirmed **Aug 6, 2026**. Not actionable until then.
- **ORIC**: stale (Jul 14) + heavily covered. LOW. Only on a genuinely fresh trigger.

**Verdict into the open: NO HIGH-CONVICTION TRADE.** TRAX is the only name that passes the
filters and it fails on entry price quality (at 52w high, at consensus PT, sympathy-driven).
Default is **stand flat**; take it only if it builds a genuine volume-confirmed base at
9:45–9:50 *below* the opening spike. Cash is a position — do not force a trade to break the
flat streak, especially into FOMC week.

---

## Skip / Avoid List (standing)

| Symbol | Reason |
|--------|--------|
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
- **Volume**: Only enter if volume >1.5x avg in first 5–10 min (9:45–9:50 base confirmation).
- **Dilution rule**: Skip any name with an announced offering / ATM / convertible closing
  within 2 weeks.
- **Sizing (pooled ~$10k shared account)**: Rocket slice = 30% (~$3,030). 15% max position
  ≈ $454; 1.5% risk ≈ $45. Use `alpaca_client.py size SYMBOL ENTRY STOP`. Verify free pooled
  cash first — do not assume the full slice is available (Bull consumes shared cash).
- **Stop**: 7% trailing stop set immediately at entry (atomic with buy).
- **Targets**: +15% (lock 1/3), +25% (lock 1/3), trail final 1/3. **Log every exit same-day.**
- **No new entries after 3:30 PM ET. Max 4 positions, max 5 trades/week.**

---

## Recently Resolved Ideas

| Symbol | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| MRLN | $8.88 (1,670 sh, Jun 5) | $8.90 (Jun 5) | +$33.40 (+0.23%) | Defense catalyst real; hit +15% target then chopped back. Lesson: lock 1/3 at first target. |
| CAMP | $4.85 (3,093 sh, Jun 16) | UNRECOVERABLE | Unknown | Closed pre-7/20 merge; exit never logged, gone from Alpaca history. See trade_log.md + lessons item 9. |
