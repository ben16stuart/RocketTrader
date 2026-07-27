# Rocket Market Context

Last updated: 2026-07-27 (Monday pre-open)

---

## Snapshot — 2026-07-27 Monday Pre-Open  ← CURRENT

### Account structure
- SHARED Alpaca account with Bull. Shared value **$10,125.55**; Rocket slice (30%) =
  **$3,037.66**. Pooled cash **$7,987.75**. **Rocket is FLAT** — JPM is Bull's only position.
- Position math: 15% max ≈ **$455**; 1.5% risk ≈ **$45**. Sizes are small — accept it.
- Rocket +0.20% since 7/20 rebase vs SPY -0.43% → **+0.63% relative**.

### Macro — FAVORABLE (risk-on), but a narrow window
- **VIX 17.58 (-5.4%)**, down from ~18.6–19.0 Friday. Well under the 22 pause threshold →
  full 1.5% sizing permitted.
- **US–Iran fighting paused** over the weekend → **Brent -7% to sub-$86**, unwinding Friday's
  oil/geopolitical overhang. This is the driver of today's bid.
- Futures: S&P +0.96%, Nasdaq-100 +1.59%, **Russell 2000 +1.27%**. Small caps participating.
- **Russell 2000 +20% YTD vs S&P +11%** — best year since 2003; small caps are LEADING, not
  lagging. Favorable regime for the strategy.
- Partial reversal of the 7/23 mega-cap capex selloff, but that thesis gets retested this week.

### ⚠️ Event risk — the tradeable window is Mon–Tue only
- **Wed 7/29 2:00 PM ET — FOMC decision + presser** (expected hold at 3.75%). Main event.
- **Thu 7/30 — Q2 GDP advance + June PCE/Core PCE.**
- **All week — MSFT, META, AAPL, AMZN earnings.**
- No CPI (next 8/12), no payrolls (next 8/7). Monday itself is light (Durable Goods, Dallas Fed).
- **Implication**: take entries Mon/Tue; tighten stops or scale out before Wednesday 2 PM.
  Do NOT initiate fresh risk into the FOMC print.

### THEME READ (7/27)
- **Catalyst breadth is NARROW.** One in-universe name found across two independent research
  passes: **TRAX** (+21% premarket on the argenx/Forte anti-CD122 M&A read-through). It is a
  *sympathy* trade, gapping to **above its 52-week high and at its consensus PT** — poor entry
  quality despite a real catalyst. Conditional/pass.
- **M&A is today's live theme**: argenx buying Forte (FBRX) at $77/sh cash, ~86% premium, for
  anti-CD122. Watch for further immunology read-throughs.
- **Premarket gainer tape is mostly junk** — reverse-split shells and sub-$3 names (LGHL,
  BIYA, DFNS, MTNB, SXTC, OMH, GMEX). All fail universe filters. Do not screen-chase.
- **Zero small-cap analyst initiations or PT raises** dated 7/24 or 7/27. No verifiable
  short-squeeze setup (>15% short float + fresh catalyst) found.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 reduce size; >30 no new longs (currently ~17.6, clear).
- **Scanner is BROKEN again** — single-letter symbol truncation, $0.00 and wildly wrong prices
  (MRAM "$1572", GBX "+52.9%"). Treat output as unusable; verify every name via
  `market_data.py` + web before sizing. This is now 4+ consecutive sessions.
- Chase rule: no entry >20% above prior close except gap-and-go on a 9:45–9:50 base.
- Dilution rule: skip active S-1/ATM/convertible names. TRAX carries a ~10.5M-share resale
  overhang (not a hard disqualifier, but a real seller risk).
- Oil headline risk is now two-sided in the *other* direction — a collapse of the Iran pause
  would re-spike crude and hit the tape.

---

## Snapshot — 2026-07-24 Friday Pre-Open (superseded)

### Account structure (post-merge)
- SHARED Alpaca paper account with Bull (merged 2026-07-20). Shared value ~$10,091.
  Rocket's allocated slice = 30% (~$3,027). Cash POOLED with Bull (~$7,988) — verify free
  cash before sizing. JPM is Bull's only open position now.
- Real position sizes are SMALL (account ~$10k). 15% max position ≈ $454 of Rocket's slice;
  1.5% risk ≈ $45. Size accordingly.

### Macro — CAUTIOUS / MIXED (volatility ticking up)
- **VIX 18.97** (+1.4%, up from 16.64 on 7/23) — still under 25, full 1.5% sizing
  technically fine, but the calm risk-on lean has softened.
- **Tech-led selloff 7/23**: Nasdaq fell >2% on mega-cap capex fears (Alphabet Q2 capex
  hike) + Iran tensions lifting oil prices. Two-sided risk backdrop.
- **Small-cap bounce premarket**: Russell 2000 +0.37% into the 7/24 open, modest recovery.
  Small caps amplify direction — mixed tape, could whip either way off yesterday's selloff.

### THEME READ (7/24 movers)
- **No clean fresh single-stock small-cap catalyst.** Scanner garbage again.
- **HARD AVOID**: DRUG +71.5% (Bright Minds — active Jan $175M offering + ATM dilution +
  ~1,500% YTD pump + chase).
- **SKIP (stale)**: ORIC +11.3% (Phase 3 initiation Jul 14, 10 days old, heavily covered);
  KPTI +7% (exec retention program 7/20 which it SANK on — no positive catalyst).
- **Not tradeable (large-cap)**: 7/23 earnings beats MEDP +18.4%, CLF +12.2%, ALLE +10% —
  all outside the $50M–$2B universe.

### Intraday Triggers to Watch
- VIX >22: pause new entries; >25 no new longs (currently ~19, fine but rising).
- **Scanner data STILL unreliable** — single-letter symbol artifacts, RelVol dashes, $0.00
  prices, SAM +176.3% glitch. Independently verify price + volume before sizing.
- No entries on any +20%+ gapper (chase rule) — wait for second-day/pullback base.
- Dilution rule: skip active S-1 / ATM / convertible names (DRUG fails today).
- Oil/Iran headline risk two-sided; watch for a red reversal — small caps amplify a down tape.
- Cash is small and pooled — confirm free cash post-Bull before sizing.

**Note**: This 7/24 pre-open snapshot is the current live macro read. Refresh at Monday
07-27 premarket for next week's tape. Prior dated snapshots archived to
`memory/archive/market_context_history.md`.
