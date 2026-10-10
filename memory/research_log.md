# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines. Archive resolved or stale
entries to `memory/archive/research_log_history.md` (the W41 board was archived there 2026-10-10).

---

## Watchlist — Week 42 (Mon 10/12 – Fri 10/16), built at W41 review Sat 10/10  ← CURRENT

**Book (10/09 close, hand-built 23a):** IWM 9.9763 sh × $278.94 = $2,782.79 (raw qty via `/v2/positions`)
+ cash $142.17 = **$2,924.96**. Slice $3,108.32 → 15% cap = **$466.25**. Satellites **0%**.
**Satellite floor breached 15 consecutive closes. Rule 8 MEDIUM bar ACTIVE.** Book cash is only $142, so every
entry needs a **CORE FUNDING** IWM sale right before the BUY (rule 3). **Rule 70 on every entry.**
_W41 board (KOPN/PCRX/TLRY/ANGO/RGP/WOLF/FEAM/TBCH notes) archived 2026-10-10._
**W41 gate counterfactual (10/09 closes):** every in-universe kill or pass was flat-to-down: ANGO −26% (5f), RGP −25%,
FEAM −7% (resale), CRVO −3%, TLRY −2%, ITG −8% from its day 2, PCRX pinned, ACRS +1%, ALMS +3%. The only runners
were out of mandate: PENG +18% ($3.3B, 13) and VEEA +48% (pump, 1). WOLF/NEOG (cap-blocked) faded their AH pops.

**Mon 10/12 = Columbus Day: the bond market is closed and equities are open.** Thin-volume day; the ADV and RelVol reads are weaker.

### Conditional plans (carried forward; re-read the settled bars every premarket)
- **IRD — PDUFA 10/17 (a SATURDAY → the FDA can act Fri 10/16 or earlier).** Entry only if a session through
  **10/13** closes **upper half on ≥1.5× median** AND ≥ **$4.84**. **Exit by the 10/14 close** (moved up a day from
  10/15, rule 29: the decision can land Friday or earlier). Kill: a close < $4.40 on heavy volume. 10/09: $4.64, 64% of range,
  light volume → no trigger. Read the S-3 (effective 8/14) shelf size via the CIK path before sizing (8).
- **UNCY — NDA acceptance PR** (≤30 days from 9/29 → by ~10/29). Day-2 only on an upper-half close ≥2× median.
  10/09 $4.11 (36%). Still sliding. One more low close on ≥1.5× = distribution (4) → close it.
- **ALMS — reopen ONLY on the NDA-submission PR** ("on track 4Q26"). A regulatory, dated catalyst plus a day-2 shape.
  $902M, ADV 2.4M. 10/09 $7.17 (69%). A data presentation does not count (0/4 category).

### Unverified scanner names from the 10/10 run (name source only, 17). Premarket reads the filing or PR first.
- **SVC** (Service Properties Trust, REIT, ~$926M): 10/09 **+14.9% on 10.5× RelVol**. Cause unknown. A web search
  returned an undated "$51M Massachusetts property sale" item and a "raises $490M" item (debt or equity? check the 8-K,
  8). An asset sale is not on the catalyst list. Only a dated 8-K showing a strategic/transformative event qualifies. **LOW.**
- **KLRA** (Kailera, obesity biotech, IPO April 2026): 10/09 +16.1%. No cause on the news tape or a search.
  **Cap conflict:** scanner $1.51B vs search $2.46B → run `eligibility` first (13). The IPO lock-up likely expires around now
  (supply, 8). **LOW.**
- DNA +14.6% (NSF X-Labs access, Araceli integration) is a partnership PR, not revenue-changing. It already FAILED the rule-11 ladder (10/05). Out.
- FEAM +10% stays closed (resale overhang, 10/05). PCRX pinned. CABO/XRPN/CDNL/ALHC are decliners.

### W42 scheduled catalysts (Nasdaq rows as of 10/10, thin; RE-PULL every premarket, confirm on the 8-K, 65)
| Name | Date | Cap | Note |
|---|---|---|---|
| UNTY | 10/13 | $554M | regional bank. Banks rarely guide → rule 5 hard to meet |
| SOTK | 10/14 BMO | $107M | check median ADV first (46) |
| EQBK | 10/14 AMC | $977M | bank |
| BSVN / CWBC / WABC | 10/15 | $529M / $707M / $1.38B | banks |
| ALOY | 10/15 | $526M | REalloys. Check domicile (52c) and ADV |
| CTW | 10/15 AMC | $143M | check ADV, domicile |
| RBCAA / MCBS / PBAM / ATLO / BVFL | 10/16 | banks | |
**Q3 season gets going the week of 10/19.** W42's earnings rung is mostly banks. Lean on the FDA tape and the Alpaca news tape.

### Scheduled catalysts — other
- **CLB** earnings 10/28 · **DTIL** 11/02 (ADV-locked).
- **SECZ**: reopen only if it trades materially below the $2B cap AND the lock-up schedule (Proxy p.123) is read.

### Sourcing order for W42 premarkets (strategy.md throughput commitments)
1. Earnings calendar (prior AMC + today BMO). Confirm "raised" on the 8-K.
2. **Alpaca news tape** (`/v1beta1/news`, parse with `strict=False`). W41's best source: it surfaced KOPN's PR and the PCRX deal.
3. FDA/regulatory tape (approvals, not data readouts).
4. Analyst initiations: Buy, dated, in universe.
5. Screeners last, as a name source.
6. **market_open/midday:** check the Alpaca news tape for a mover BEFORE a web search. On 10/08 one web search missed the
   Viatris/PCRX deal that had been public for 2 hours.
7. Log the funnel in session notes: screened → survivors → entries.

---

### Open escalations awaiting a user decision
1. **Satellite floor arithmetic** — IWM cap LIFTED 2026-10-06 (Ben chose option 1). RULED 2026-10-06: per-slot cap (15%) and 50% floor stay UNCHANGED —
   no proven edge to size up (last 2 entries stopped out); revisit after >=8 closed satellite trades.
2. **Rebalance basis** (lesson 44). Now binding — IWM fills to the 90% line.
3. **ADV gate vs account size** (46f).
4. **$2B ceiling vs the +25% ladder** (13). It blocks CNXC and PRGS this week.
5. **Midday −5% cut vs stop distance** (67).
6. **`sip` data entitlement for premarket liquidity checks** (66).
7. 🆕 **Daily ntfy "Rocket vs IWM" is wrong (W41).** `portfolio_snapshot.py` computes it as 30% of the SHARED account vs
   the rebase, so it includes Bull's P&L. It printed +6.6–7.3% all week; the hand-built figure is **+0.93%**. Ask Ben whether
   to fix the script (a hand-built book carried by fills) or drop the line from the ntfy. Until then, never quote it.

### Standing category kills (full detail in archive)
Crypto/treasury (31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI, BKKT, UPXI, HSDT.
Non-US-incorporated (52c): KMTS, GLAS, NB, ADNT, DAVA. Liquidity: GLOO, TLYS, REF, OPTX,
SRZN, TTRX, IDT, TRAK, BSET. Pump/shell: GLND, GRML. **CLOSED:** PAAI (catalyst
falsified), PRTH (pinned deal), NUAI (mandated ATM), SCHL (miss + affirmed guide), PRME
(Gate A 9/25), MLKN (guide cut 9/22), XTND (undisclosed contract value, SPAC ADV).
