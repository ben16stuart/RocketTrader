# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Week 33 (Mon 2026-08-10 →)  ← CURRENT
*Built 2026-08-07 at weekly review, off screeners run with the **repaired** `Change %`
column. Week 32's board is archived. All names verified against raw daily bars.*

**Account (8/07 close)**: shared $10,505.03 / Rocket slice (30%) $3,151.51 / pooled cash
$719.86. Rocket holds **IWM 9 sh = $2,714 (86.1%)** and nothing else.
Open satellites **0 / 4**. Max satellite **$472.73** (15%); 1.5% risk **$47.27**.

🟢 **THE CASH BREACH IS NOW FIXABLE.** Notional slice cash ~$438 (13.9%) has been outside
the 10% buffer for eight sessions purely because one IWM share (9.6% of the book) could
not fit a 3% band. **`alpaca_client.py buy/sell` now accept fractional quantities.**
**Monday's `market_close` must top the core up to target with a fractional order** — e.g.
`buy IWM 0.42` — and log the fill. This is the first live test of the fix; verify the
`qty` in the returned order JSON.

⚠️ **Funding note**: a full-size satellite still needs ~$473 against ~$438 notional cash,
so **sell a fractional IWM slice to fund it** rather than a whole share. No more overshoot.

---

### PRIORITY 1 — QNST (HIGH) — rule-3 continuation, and the only name here with zero dilution risk

**QuinStreet.** Reported Q4 FY26 on 8/06 after the close. **Closed Friday $21.08, +38.5%,
at 91% of its daily range on 4.82M shares (6.2x RelVol).** Rocket passed at $20.21 Friday
morning; it closed higher.

- **Catalyst** — a beat against *company* guidance, not just street: Q4 revenue **$373.9M
  (+43% YoY)**, above the top of its own $350–370M guide; adj EBITDA **$41.4M (+87%)**;
  **GAAP EPS $0.33**. FY26 operating cash flow **$130.9M**. **FY27 guided UP: revenue
  $1.45–1.55B, adj EBITDA $150–160M (+33–42%)** — EBITDA growth guided to *accelerate*.
- ✅ **Dilution risk absent by construction** — GAAP profitable with $130.9M of operating
  cash flow. It does not need the equity market. Rarest quality on any board this month.
- **Universe (8/07)**: cap **$1,211M** ✓ | avg vol 794,944 ✓ | NasdaqGS ✓ | US ✓ | price ✓
  | next earnings **11/05** — no earnings-week bar.
  ✅ **Lesson-18 check passes**: +25% target ($26.35) implies a ~$1.51B cap, **well inside
  the $2B ceiling.** Unlike APPS, this can be held to its own plan.
- **Structure**: float 53.8M of 57.4M — no low-float edge. Short float 11.34%, below the
  15% squeeze bar, but 6.48 days-to-cover is real friction. **Momentum, not a squeeze.**
- **Entry — RULE 3 (second-day continuation).** Gapped >25% ✓, closed above its midpoint
  (91% of range) ✓ → **Monday's open is a valid entry. Zone: up to $23.19** (within 10% of
  the $21.08 close). Confirm >0.75x avg volume off **raw 5-min bars** (lesson 10).
- **Stop** 7% below fill (≈$19.60 on $21.08). **Targets** +15% ≈ $24.24 sell 1/3 | +25% ≈
  $26.35 sell 1/3 | trail the rest. Take the first third *into* the level (MRLN lesson).
- **Size** ≈ **22 sh ≈ $464 (14.7%)** — re-strike as `int(472.73 / fill)`. Needs a
  fractional IWM sale to fund.
- 🚨 **MUST CHECK MONDAY**: the pre-print mean analyst target was **$19.00, now below
  spot.** That was the reason Rocket passed Friday — but those targets are stale by
  construction. **Search for post-print PT revisions before sizing.** If the consensus has
  not been raised above ~$24, the upside leg is missing and this drops to a watch (the AMCX
  signature). Also note performance-marketing revenue is cyclical and concentrated in
  insurance verticals; +43% is partly an auto-insurance ad-spend recovery.

### PRIORITY 2 — CRSR (MEDIUM-HIGH) — record margins, low float, but revenue is shrinking

**Corsair Gaming.** Q2 reported 8/06. **Closed $14.35, +35.2%, at 92% of range** on 9.47M
shares (3.5x).

- **Catalyst**: **record 33.2% gross margin**, gross profit +21% to $104.3M, **adj EBITDA
  $30.8M vs $8.1M** a year ago. Peripherals segment revenue +13% with margin 40.0% → 44.9%.
  **FY26 raised: revenue $1.4–1.47B, adj EBITDA $121–131M, non-GAAP EPS $0.85–0.94.**
- ✅ **Low float**: 46.6M shares, only **44% of shares outstanding** — the best structural
  setup on the board. Avg vol 2.71M, deep liquidity.
- **Universe**: cap **$1,534M** ✓ | price $14.35 ✓ | NasdaqGS ✓ | next earnings 11/03 ✓.
  ⚠️ **Lesson-18 check is TIGHT**: +25% target = $17.94 → cap ≈ **$1.92B, only ~4% under
  the $2B ceiling.** Holdable to plan, but barely. **Re-derive at the actual fill.**
- 🚨 **The knock: revenue FELL 2% YoY.** This is a margin/cost story, not growth — the same
  signature as HNST, which Rocket correctly ranked last last week. Margin expansion has a
  shorter momentum tail than revenue acceleration.
- **Entry**: rule 3 applies (gapped >25%, closed at 92% of range) → zone up to **$15.79**.
- **Stop** ≈$13.35 on a $14.35 fill. **Targets** +15% ≈ $16.50 | +25% ≈ $17.94 (at the cap
  ceiling — consider taking the full remainder there). **Size** ≈ 32 sh ≈ $459 (14.6%).
- **Dilution check**: NOT YET RUN. Do it before any order.

### PRIORITY 3 — RCEL (WATCH ONLY — do not buy) — best chart of the week, disqualifying balance sheet

**AVITA Medical.** **Closed $7.77, +63.6%, at 86% of range on 7.22M shares (24.4x RelVol)**
— the largest move on the board. Real beat-and-raise: revenue $21.7M (+18% YoY), **record
81.9% gross margin**, opex −6%, **FY26 revenue guidance raised to $86–89M (+20–24%)**,
cash-flow breakeven targeted Q4.

🚨 **HARD SKIP ON DILUTION, not on the chart.** Active **$200M S-3 shelf (dated 31 Mar
2026)** already drawn on (400k shares issued to lenders), plus a **$15M Australian private
placement**, against **under one year of cash runway** and a company that is still burning
to a Q4 breakeven. That is live authorization to sell stock into exactly this spike — the
SOC / SVCO / STLN / BKSY pattern. **Do not buy strength here.**

📌 **Process note**: Friday's premarket rejected RCEL on a **295k average-volume reading
against the 300k gate. The real figure is 302,064 — it passes.** The right outcome came
from the wrong gate. **Re-verify ADV against raw data for any name within ±10% of 300k**
before rejecting it; next time the borderline name will be clean.

### PRIORITY 4 — Secondary board (check Monday premarket, none pre-cleared)

| Symbol | Fri close | Range pos | Note |
|---|---|---|---|
| **OABI** | $3.08 (+37.5%) | **95%** | Strongest close on the board, cap $447M, avg vol 700k ✓. 🚨 **$3.08 is 2.7% off the $3.00 floor** — one bad session puts it out of universe. Float 113.9M, no edge. Needs a dilution check (biotech). |
| **GTN** | $5.37 (+25.5%) | 85% | Gray Media. 🚨 **Market cap returns `unknown — VERIFY MANUALLY`** — an unchecked universe gate is not a pass. Verify the cap or retire the name. |
| **ARCT** | $7.41 (+21.9%) | 87% | Arcturus. Cap $211M, float 26.2M (low ✓), avg vol 476k ✓. Clinical-stage biotech = assume dilution until proven otherwise. |
| **EMBC** | $4.42 (+26.3%) | 63% | Embecta. Reported **8/07 (today)** — cap $262M, avg vol 2.19M ✓. Weakest close of the gappers; only a second-day setup if it holds. |
| **PUBM** | $17.78 (+31.9%) | **52%** | PubMatic. Closed at its midpoint — the weakest close among the big gappers. **Fading, not basing.** Deprioritize unless it rebuilds. |
| **TBCH** | $13.95 (+11.2%) | 71% | Turtle Beach. Float 11.8M (59%) and **30.58% short float** — the only real squeeze structure on the board, but avg vol 317k barely clears. No catalyst identified yet. |

### Eliminated Week 32 — do not re-litigate

**Dead on their own tape** (day-one distribution or a broken print): ASPN, EVH, MRAM,
SVCO (revenue miss + sequential guide-down), CVRX (guidance CUT), NNBR (PIPE magnet).
**Out of universe**: APPS (+25% target sits outside the $2B ceiling), FIGS (~$2.38B at its
gapped price). Full reasoning archived in `research_log_history.md`.

**Barred only by the earnings-week rule — re-screen after the print**: **NRGV (8/11)**,
**REPL (8/11)**, **SPRY (8/13)**.

---

## Skip / Avoid List (standing)

**Active dilution — HARD AVOID** (the reason never expires; do not re-screen on chart quality):
**RCEL** *(new 8/07 — $200M shelf already drawn, <1yr runway)*, **SOC** ($93M sold at
$3.08 + $289M converts), **STLN** ($15M ATM), **DRUG**, **BKSY** ($250M ATM), **DFNS**,
**BOT**, **WOLF**, **QMCO / CLNN / FJET**.

**Structural / integrity — HARD AVOID**: **GCT** (Cayman holdco on mainland-China subs —
fails US-domicile, permanent), **STI** (going concern, defaulted note), **TLSI** (fraud
investigations + guide cut), **FULC / CAST** (going-concern pumps), **BNAI** (promotional
AI hype), **SPCE** (theme dead).

---

## Entry Framework Reminders

Full rules live in CLAUDE.md and `lessons_learned.md`. Only this week's live numbers here:

- **Sizing**: slice $3,151.51 | 15% max **$472.73** | 1.5% risk **$47.27**.
- **Dilution check runs FIRST.** ✅ QNST clean by construction. ❌ **CRSR's is NOT yet run.**
- **Lesson-18 cap check**: QNST's +25% target clears $2B comfortably; **CRSR's by only ~4%.**
- **Fractional orders now work** — fund satellites by selling a *fractional* IWM slice, and
  rebalance the core to the exact target. Partial reductions still use `sell SYMBOL QTY`.
- **Targets**: +15% (lock 1/3), +25% (lock 1/3), trail final 1/3. **Log every exit same-day.**

## Recently Resolved Ideas

| Symbol | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| CSTL | $29.99 (Aug 3) | $29.94 (Aug 6) | −$0.75 (−0.17%) | Trailing stop off the $31.73 HWM. Thesis never broke; the trail gave back the pop. |
| MRLN | $8.88 (Jun 5) | $8.90 (Jun 5) | +$33.40 | Catalyst real; hit +15% then round-tripped. Lock 1/3 at target. |
| CAMP | $4.85 (Jun 16) | UNRECOVERABLE | Unknown | Closed pre-merge, exit never logged. Lessons item 9. |
