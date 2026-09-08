# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Tue 2026-09-08 premarket (Week 37 day 1)  ← CURRENT

**Book (hand-built — BASE NAMED, lesson 23a/44)**: **$3,111.67** = IWM **9.8636 sh**
($2,919.66 @ $296.01 *settled* close, **93.83%**) + notional cash **$192.01 (6.17%)**.
✅ **Inside the 10% buffer — no bearish thesis required or written.**
Satellites **0/4** · weekly count **0/5** (new week, counted by hand — lesson 24) · max
satellite **$466.75** (15%) · 1.5% risk **$46.68** · shared cash $427.02 (pooled with Bull
— **fund from core, not cash**).

### market_open 9/08 confirmation: scanner threw 2 fresh names, both killed inline, no trade

`unusual_volume`/`top_movers` surfaced **EAF** (GrafTech, +20.6%, 8.1x) and **NVA** (Nova
Minerals, +6.3%, 4.8x) — neither on the premarket board. **EAF**: only news is the Q2 print
from 7/24, nothing dated to today — killed on rule 1 (no catalyst). **NVA**: today's news is
equipment arriving at an Alaska antimony plant (announced 8/26, arrived 9/6) — construction
progress, not a named catalyst type, and Nova Minerals is Australian-domiciled (dual ASX
listing) — mandate kill regardless of the catalyst question. Neither >35%, so the
missed-catalyst 3-day recheck doesn't apply to either. No fills, no stops triggered, IWM
core unchanged. **Confirms the premarket verdict below.**

### midday 9/08: EAF/NVA kills hold on bigger moves, one fresh name (HYPD) killed on mandate

Both scanners now show EAF **+21.9%/4.0x** (up from 8.1x at the open) and NVA **+9.8%/4.3x**
— both moves grew, neither kill reason changed (EAF still has no dated catalyst; NVA's
equipment-arrival news is still 2 days stale and the domicile mandate kill is independent
of the catalyst anyway — also surfaced a **$20M capital raise at a 14% discount**, a fresh
dilution flag on top of the standing kill). 🆕 **HYPD** (Hyperion DeFi, +6.2–7.7%, 5.0x) is
new to the board — a **genuine dated catalyst** (raised FY26 adj. gross profit guide
$5–7M → $7–8M, announced a $20M buyback, both dated today) that would otherwise clear
rule 5/5a cleanly. **Killed anyway: it's a HYPE-token crypto treasury company** (formerly
Eyenovia, pivoted business model) — rule 31 mandate exclusion, independent of catalyst
quality, same shape as BNC/DFDV/USDE/ABTC. No fills. **Result: 0/4 satellites, 100% IWM
core, no trade.**

## 🚩 VERDICT: NO ENTRY. Hold IWM. The earnings calendar is verifiably EMPTY in-universe — and the scanner is the most broken it has ever been.

**Today's finding is instrumental, not name-specific.** For the first time since lesson 41
was written, the earnings calendar produced **zero** in-universe names — and that is a
*measured* empty slate, not a blank one (41b). Meanwhile `top_movers` printed **three sign
flips** and a **35-point error**, the worst session on record.

---

### 🥇 The earnings calendar ran FIRST (lesson 41) — and this time it is genuinely empty

New instrument this session: the **Nasdaq earnings-calendar API**
(`api.nasdaq.com/api/calendar/earnings?date=YYYY-MM-DD`) returns ticker + market cap +
BMO/AMC in one call, with no login wall. Earnings Whispers and stockanalysis.com both
**404'd or hit a login page** via WebFetch; three web searches produced only partial,
undated lists. **This replaces web-searching the calendar — record it as the source.**

| Date | Reporters | In Rocket's universe |
|---|---|---|
| **Fri 9/04** (first regular session is TODAY — the tradeable slate) | 4: VZLA, HURC, VIRC, NTRB | **0** |
| Sat–Mon 9/05–9/07 | 0 (weekend + Labor Day) | 0 |
| **Tue 9/08 BMO** | ABM, UNFI, WDH, CAN, DLNG, GMHS + 5 "time-not-supplied" | **0** |

**All 8 screened names FAILED, `eligibility` counted 8 requested → 8 returned (lesson 43):**

| Name | Kill |
|---|---|
| **HURC** (9/04) | ADV **36,111** — 12% of the gate |
| **VIRC** (9/04) | ADV **59,229** |
| **NTRB** (9/04) | ADV **21,546** |
| **AXR** (9/08) | ADV **8,345** |
| **AREC** (9/08) | **$2.43** — under the $3 floor |
| **ELME** (9/08) | **$1.69** |
| **UPXI** (9/08) | **$1.07** |
| **ZENA** (9/08) | **$1.68** |
| **VZLA** | Canada-domiciled — mandate |
| **ABM $2.77B · UNFI $2.64B** | Cap, both rungs |
| **WDH · CAN · GMHS** | China-domiciled — mandate |
| **DLNG** | Greece-domiciled LP — mandate |
| **INNV · AVO · MIND · CASY · TTAN · GME · BRZE** | Report **AMC today** — not tradeable today; INNV ($1.46B) and AVO ($1.11B) are the only two in-universe, **re-screen Wednesday** |

**This is lesson 41b's good case: a source that cannot silently go blank returned a
slate, the slate was screened, and it was empty on hard gates.** No judgment was involved
and none was needed.

---

### 🚨 LESSON 17a — TENTH DEMONSTRATION, AND THE WORST SESSION ON RECORD: THREE SIGN FLIPS

Raw daily bars pulled **before** any research (17a). Every scanner row I checked was wrong:

| Ticker | Scanner said | Friday's real settled bar | Error |
|---|---|---|---|
| 🚨 **BNC** | **+41.0%, $4.92, 1393.8× RelVol** | **+6.08%, $3.49, 1.86×** | **35 points** and a **~750× RelVol error** |
| 🚨 **ENOV** | **+3.5%** | **−4.33%**, 5% of range | **sign flip, 7.8 pts** |
| 🚨 **TROX** | **+4.0%** | **−1.43%**, 25% of range | **sign flip** |
| 🚨 **WTI** | **+3.6%** | **−1.80%** | **sign flip** |
| HLF | +7.0%, $13.25 | +1.73%, $12.38 | 5.3 pts |
| SG | +5.3%, $7.20 | +2.40%, $6.84 | 2.9 pts |
| UPB | +4.0% | −1.15% | sign flip (4th) |
| TLYS | +2.0% | **0.00%** | — |
| CHPT | +1.9%, $10.08 | **+8.92%**, $9.89, 2.49× | understated by 7 pts |

🚨 **The overlap tier (top_movers ∩ unusual_volume) was BNC alone — mandate-excluded
(crypto-treasury proxy, lesson 31) — and its numbers were fiction in both lists.**
`top_movers` gave **8 of 20 rows a RelVol of `—` or `0.0x`**; `unusual_volume` had
**16 of 20 below 1.0×**, i.e. below average volume.

---

### The eight in-universe movers — all killed on ONE gate, no research spent

`eligibility HLF SG INSG TROX AMRC WTI ENOV UPB` → **8 requested, 8 returned** (lesson 43).
All eight **pass every universe gate**. **All eight have next earnings 2026-11-02 → 11-05,
i.e. +55 to +58 days.** Rule 1/33: **a move without a dated catalyst is not a signal**, and
four of the eight did not even move up. Killed in one command, zero searches.

---

### ❌ INSG — the only name with a real bar, and it dies three separate ways

Inseego closed **+5.21% at 91% of its range on 1.40× volume** — the prettiest bar on the
board and, per rule 1, exactly the RMNI trap shape. Screened anyway; it fails four gates:

1. ❌ **Rule 1 — no catalyst.** Next earnings **+58 days**. One search returned only the
   press-release *index* page. Nothing dated to 9/04.
2. 🚨 ❌ **Rule 8 — an S-3 is live.** The search surfaced an **INSEEGO CORP. Form S-3,
   FY2026** on EDGAR. On a **$69M** market cap that is a first-order dilution flag.
3. 🚨 ❌ **Lesson 46 — THIRD STRAIGHT SESSION, same shape.** `eligibility` read ADV
   **323,390 — a PASS by 7.8%**, inside lesson 14's ±10% re-verify band. Raw 63-day bars:

   | Measure (63d) | Value | vs 300k gate |
   |---|---|---|
   | Mean, as-is | **331,479** | ✅ passes by 10.5% |
   | Mean, ex-max bar | 305,750 | ✅ passes by 1.9% |
   | **Median** | **265,700** | ❌ **fails by 11%** |

4. ❌ **Rule 37a/45 — median daily range 6.12%, i.e. ~87% of the entire 7% trail.** Own
   catalyst-day multiple **2.36×** ⇒ predicted catalyst-day range **14.4% = 2.1× the trail**.
   Own widest days: 11.4%, 11.6%, 14.4%, 16.0%, **22.0%**.

---

### ✅ Friday's kills graded against the bars (lesson 32c) — 4 for 4

| Name | Friday's settled bar | Verdict on the kill |
|---|---|---|
| 🥇 **SWBI** | Indicated **+9.0%** premarket → **closed +5.05% at 39% of range** on 2.88×, range **15.52%** | ✅ **The 5a/5d guidance kill graded correct in one session.** It faded more than half the indicated gap and **closed below its midpoint on heavy volume — rule 4's distribution shape.** ⚠️ **And rule 45's forecast was biased LOW**: predicted 10.2%, actual **15.52%** (see new lesson 45f) |
| **TLYS** | **0.00% on 1.45×**, closed at 28% of an 11.36% range | ✅ Lesson 46 liquidity kill correct a **second** session running |
| **NX** | **+22.23% on 6.68×, closed at 90% of range** | ⚠️ **The strongest bar on the tape — and the kill still stands.** Rule 5f (reinstated guide = 0% change) is a *guidance* gate; lesson 45e says only *range* kills convert to a date. **Rule 42a: a strong close is not a credit that offsets a failed guide.** Recorded as an uncomfortable carry, not re-opened |
| **CHPT** | **+8.92% on 2.49%**, 62% of range | ⚠️ Still running after 9/03's +49.3%. Killed on rule 5a (+0.6% guide midpoint, below the reported quarter). **Not re-opened** — same reason as NX |

📌 **Missed-catalyst rule check**: nothing in-universe ran **>35%** in the last 3 sessions.
NX (+22%) and CHPT (+49% on 9/03, day 3 today) are both under active *guidance* kills, which
the rule does not override.

---

### 🚩 Rebalance-basis divergence — carried, NARROWED, **FIFTH** session (lesson 44/44c)

Both bases struck off **settled** closes this time, so the comparison is clean:

| Basis | Value | Divergence |
|---|---|---|
| **Book** (hand-built, lesson 23a — **the base used above**) | **$3,111.67** | — |
| **Slice** (30% of settled shared equity $10,666.11) | $3,199.83 | **slice +$88.16 richer** |

**Narrowed from $106.66 → $88.16, and the direction confirms lesson 44b's mechanism runs
both ways**: Friday **IWM +0.28% vs SPY −0.39%**, so Rocket's core outran Bull's book and
the gap closed. It closed for the same reason it opens — **not because anything was fixed.**
🚨 **Fifth consecutive session. Escalated 9/01, 9/02, 9/03, 9/04; still awaiting a user
decision on which basis governs.** No action here — rebalancing is `market_close` only (rule 6).

---

### Re-run of Step 2 scanners (later premarket pull) — one new overlap name, killed

Fresh `top_movers`/`unusual_volume` pull (07:21 local): overlap tier is **BNC** (still
mandate-excluded, now an even worse fiction at **+61.6%, 1806.3× RelVol**) and one new
name, **EAF** (GrafTech, +8.5%/1.9× both lists). `eligibility EAF` **passes every
universe gate** (cap $189M, price $7.26, ADV 340,538). ❌ **Killed on rule 1 anyway** —
the only explanation found is a Seeking Alpha headline "GrafTech surges on speculation
of Defense Department partnership," **undated and explicitly speculative** (rule 33's
trap: a headline describing a move is not evidence), next earnings **+52 days**, and
the move itself is modest (1.9×, not a breakout). No dated catalyst, no trade.

### Scheduled catalysts

- 🚨 **The jobs report was a 3× BEAT: +162K vs +53K consensus**, strongest since March,
  first up-month in five, **prior two months revised UP a net +55K** (July −23K → +21K).
  Unemployment **4.1%, unchanged**. **A September HIKE is more live, not less.**
- 🚨 **FOMC September 15–16, decision Wednesday 9/16 — 6 trading days out.** A satellite
  opened today on a 1–5 day hold clears it; **anything opened Thursday or later carries
  into it.** Rule 29 gate, dated, for the rest of this week.
- **Today**: trade balance 8:30 AM (pre-open, the good case), Services PMI ~9:45 and **ISM
  Services 10:00 AM — 25 minutes AFTER the 9:35 decision window**, the same hostile shape as
  the last several sessions. ⚠️ **The search source for today's calendar recycled stale
  content** (it named a Fed Vice Chair who does not hold the office and labelled August data
  "September") — **treated as low-confidence and not written into `market_context.md` as
  fact** (lesson 39).
- **Wednesday 9/09 is a real slate** — first in a week. In-universe BMO/AMC candidates to
  screen: **CAL ($418M), JILL ($299M), PPIH ($231M), LMNR ($272M, AMC), LSAK ($388M, AMC),
  GLOO ($297M, AMC), LAKE ($118M, AMC), KEQU ($106M, AMC), OCC ($122M)**. Plus **INNV/AVO**
  reporting AMC today. **ANAB stays killed on rule 13** (cap $1.68B → +25% = $2.10B, through
  the $2B lid). ODD/CGNT/NNOX Israel-domiciled, SIG Bermuda — mandate.

### Re-open conditions for killed names (everything else needs a new dated catalyst)

| Name | What would have to change |
|---|---|
| **INSG** | A **dated** catalyst **and** a sustained *median* volume above 300k **and** the S-3 graded (8a) |
| **NX** | A **sized** raise against the **pre-withdrawal** March guide (5f), not a reinstatement |
| **SWBI** | A **sized** raise (>2% on revenue) **and** dated post-print targets. The Q2 +10% guide must be beaten and passed through |
| **CHPT** | A **sized** raise (>2% at the midpoint) **and** a dated post-print consensus above 1.15× entry |
| **BBCP · TLYS** | ⚠️ **Not re-openable on a catalyst** — only a sustained **median** volume above 300k, or a user decision on the ADV gate |
| **CAPR** | In universe ($547M, ADV 6.3M) but the **PDUFA was EXTENDED Aug 22 → Nov 22** — lesson 37c: an extension is a delay repriced as optionality, **not a catalyst delivered.** Rule 29 binary, 2+ months out |
| **HLF · SG · TROX · AMRC · WTI · ENOV · UPB** | Earnings **11/02–11/05**. No dated catalyst inside any tradeable horizon |
| **ALMU** | Earnings **9/16** — re-screen after the print (and note it collides with FOMC day) |
| **PHR** | ⚠️ **Resolve the earnings date first** (two sources disagreed 9/03) |
| **ARCT** | ARCT-810 Phase 2 **date becomes a fact** |
| **BNC · USDE · DFDV · ABTC** | Crypto/stablecoin proxies — **mandate-excluded, lesson 31**. Standing, not re-researched |
| **GIII · DAKT · ANAB · NEOV · YEXT · PD · RMNI · MEI · CBIO · IRD · TYRA · PYXS · RARE · GOLD** | Killed on the tape or a hard gate. New dated catalyst only |
| **LTRX · OOMA · FRNM · SSTK · BBW · OSG · XHLD · NABL · LENZ · ALMS · EOSE · OABI** | Killed W35–W36, reasons in `archive/research_log_history.md` |
