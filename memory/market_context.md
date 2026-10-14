# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-10-14 Wednesday premarket (Week 42 day 3 — **floor breached 17 closes; MEDIUM bar active**)  ← CURRENT

"Close" figures are **Tue 2026-10-13 settled closes**. LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.27 close 10/13** → 15.25 LIVE | Calm. No size restriction |
| **10-yr** | **5.22% close 10/13** | Slightly lower |
| **FUTURES** | ES +0.19% · NQ −0.06% · **RTY +0.30%** LIVE | Small caps firm ahead of CPI. One session (28) |
| **Brent / WTI** | **105.69 / 94.14 close 10/13** (+0.7% / +1.2% LIVE) | IRGC: container ship sank after hitting a mine south of Hormuz |
| Gold / Dollar | 4,177.30 / 102.18 close 10/13 | |
| **SPY / IWM** | **778.01 / 276.70 close 10/13** (−0.01% / −0.43%) | Small caps lagged |

**Rule 29 / event risk:** **CPI 8:30 ET** (headline +0.6% m/m / 3.6% y/y expected, core +0.2% / 2.5%). It is pre-open, so not a binary inside the
session, but expect a gap. Fed's Collins wants rates "a bit further" higher before year-end. BAC/MS earnings today. PPI, retail sales and claims Thu 10/15.
**Binding constraint (53): board quality.**

### Instrument health
- ✅ `eligibility` 16/16 (43 ✓). ✅ `macro`. ✅ Alpaca news (strict=False). ✅ EDGAR submissions via `company_tickers.json`.
- ⚠️ Scanners (04:20 ET): RelVol blank for most rows. DBI/VRA "+10–12%" have no IEX print since the 10/13 close (17). Name source only.

## Snapshot — 2026-10-13 Tuesday premarket (Week 42 day 2 — **floor breached 16 closes; MEDIUM bar active**)

"Close" figures are **Mon 2026-10-12 settled closes** (SPY/IWM/10Y also 10/12). LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.21 close 10/12** → 15.28 LIVE | Calm. No size restriction |
| **10-yr** | **5.24% close 10/12** | Flat |
| **FUTURES** | ES +0.06% · NQ −0.48% · **RTY +0.47%** LIVE | Small caps leading. Memory names (MU/SNDK) are dragging NQ on China CXMT news. One session, no signal (28) |
| **Brent / WTI** | **106.65 / 93.74 close 10/12** (−2.1% LIVE) | Bessent: Iran's economy "collapsing". Houthi airport strike in Saudi Arabia |
| Gold / Dollar | 4,190.60 / 102.58 close 10/12 | |
| **SPY / IWM** | **778.10 / 277.90 close 10/12** (−0.06% / −0.37%) | |

**Rule 29 / event risk:** big-bank earnings today (JPM/GS/WFC/C; UNH beat and raised). Fed: Waller, Barkin, Collins today.
**CPI Wed 10/14 8:30 ET** (consensus +0.6% m/m, 3.6% y/y vs 3.4% prior, per investinglive). PPI, retail sales and claims Thu 10/15.
CPI is pre-open, so it is not a binary inside the session, but expect a gap.
**Binding constraint (53): board quality.** The in-universe earnings rung is still banks and ADV-locked names.

### Instrument health
- ✅ `eligibility` 10/10 (43 ✓). ✅ `macro`. ✅ Nasdaq calendar. ✅ Alpaca news (strict=False). ✅ EDGAR submissions.
- ⚠️ EDGAR `browse-edgar?ticker=OIG` returned a **stale CIK (1108967, a 2023 shell)**. Resolve tickers via `company_tickers.json`.
- ⚠️ Scanners (04:20 ET): RelVol blank, Change % stale (17). The Finviz breakouts query returned no results. Name source only.

## Snapshot — 2026-10-12 Monday premarket (Week 42 day 1, Columbus Day — floor breached 15 closes)

"Close" figures are **Fri 2026-10-09 settled closes** (10Y = 10/09). LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **14.84 close 10/09** → 15.47 LIVE | Calm. No size restriction |
| **10-yr** | **5.24% close 10/09** | Flat. The bond market is CLOSED today (Columbus Day) |
| **FUTURES** | ES +0.09% · NQ −0.10% · **RTY +0.04%** LIVE | Flat open expected |
| **Brent / WTI** | **104.72 / 91.85 close 10/09** (+0.8% LIVE) | Iran calls the US response to its peace terms "inadequate"; Iranian shipping strikes now number over a dozen |
| Gold / Dollar | 4,216.30 / 102.21 close 10/09 | |
| **SPY / IWM** | **778.57 / 278.94 close 10/09** (+0.60% / +0.49%) | Dow posted a weekly gain |

**Rule 29 / event risk:** no FOMC today. Equities are open on thin volume. Big-bank earnings start Tue 10/13 (JPM/GS/WFC/C).
Inflation data is due this week (headline 10/11: "yields stabilize ahead of inflation data"; date not verified).
**Binding constraint (53): board quality.**

### Instrument health
- ✅ `eligibility` 15/15 (43 ✓). ✅ `macro`. ✅ Nasdaq calendar. ✅ Alpaca news (strict=False). ✅ EDGAR submissions.
- ⚠️ Scanners (04:20 ET) show RelVol blank or 0.0× for most rows and stale Change % (17). Name source only.

## Snapshot — 2026-10-09 Friday premarket (Week 41 day 5 — **floor breached 14 closes; MEDIUM bar active**)

"Close" figures are **Thu 2026-10-08 settled closes**. LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.41 close 10/08** → 15.21 LIVE | Calm, far below the 22 brake. No size restriction |
| **10-yr** | **5.23% close 10/08** (5.28% 10/07) | Off the highs; Pimco "6% risk" headline. Standing flag (34) |
| **FUTURES** | ES +0.40% · NQ +0.80% · **RTY +0.35%** LIVE | Bounce after two down days for small caps. Not a signal alone (28) |
| **Brent / WTI** | **104.28 / 91.49 close 10/08** (−1.2% / −0.9% LIVE) | Iran: Trump "no longer wants a deal"; Gulf tanker attacks. Hurricane Isaias (Cat 2) shut-ins in the Gulf |
| Gold / Dollar | 4,157.00 / 102.14 close 10/08 | Gold +1.2% LIVE |
| **SPY / IWM** | **773.93 / 277.57 close 10/08** (−0.42% / −0.05%) | Small caps outperformed large caps by 0.37 pts |

**Rule 29 / event risk today:** no FOMC, no major data found (one search; thin source; the search's "Columbus Day 10/09"
claim is wrong — Columbus Day is **Mon 10/12**: bond market closed, equities open). Headline risk: Iran, Isaias.
**Binding constraint (53a): board quality.** The one big catalyst (PCRX) is a pinned $36.50 cash deal.

### Instrument health
- ✅ `eligibility` 7/7 rows (43 ✓). ✅ `macro` complete. ✅ Nasdaq earnings calendar API works. ✅ Alpaca news API works
  (parse with `json.loads(..., strict=False)`).
- ⚠️ Scanner (04:20 ET) Change % wrong for 12 of 13 checked names (17). Name source only.

## Snapshot — 2026-10-08 Thursday premarket (Week 41 day 4 — **floor breached 13 closes; MEDIUM bar active**)

"Close" figures are **Wed 2026-10-07 settled closes** (10Y row is 10/07 close). LIVE = indicative only (~06:20 ET).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.08 close 10/07** → 15.72 LIVE | Calm, far below the 22 brake. No size restriction |
| **10-yr** | **5.28% close 10/07** (5.27% 10/06) | Yields "hitting new highs" in headlines. Standing flag (34) |
| **FUTURES** | ES −0.41% · NQ −0.59% · **RTY −0.84%** LIVE | Small caps leading lower for a second day. Not a signal alone (28) |
| **Brent / WTI** | **100.20 / 88.28 close 10/07** (+4.3% / +4.2% LIVE) | Pentagon reportedly readying Iran strikes; Hormuz shipping attacks |
| Gold / Dollar | 4,140.70 / 102.24 close 10/07 | Flat / dollar firmer |
| **SPY / IWM** | **777.22 / 277.70 close 10/07** (−0.24% / −1.29%) | Small caps lagging large caps by 1.05 pts again |

**Rule 29 / event risk today:** no FOMC. Fed speakers Barkin + Bowman 8:30, Schmid 11:30, Daly 1:00 PM ET;
EIA nat gas 10:00. **Geopolitical:** Iran-strike headlines can whipsaw oil and the tape intraday.
**Binding constraint (53a): board quality.** The one real overnight catalyst (WOLF) sits at the $2B ceiling (13).

### Instrument health
- ✅ `eligibility` 16/16 rows (43 ✓). ✅ `macro` complete. ✅ Nasdaq earnings calendar API works.
- ✅ Alpaca news API works. **Gotcha:** responses can carry raw control chars, so parse with `json.loads(..., strict=False)`.
- ⚠️ Scanner (04:20 ET) Change % reflects AH prints for some names (WOLF real), stale for others (17). Name source only.
