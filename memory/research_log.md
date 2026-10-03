# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines. Archive resolved or stale
entries to `memory/archive/research_log_history.md` (the 9/25 board was archived there 2026-09-26).

---

## Watchlist — Week 41 (Mon 10/05 – Fri 10/09), built at W40 review Sat 10/03  ← CURRENT

**Book (10/02 close, hand-built 23a):** IWM 5.4746 sh $1,541.21 (49.6% of slice, at cap) + RARE 31 sh $471.82
(15.2%) + cash $966.33 = **$2,979.36**. Slice $3,109.01 → 15% cap = **$466.35**.
**Satellite floor breached 10 consecutive closes. Rule 8 MEDIUM bar ACTIVE.** Two cap-size satellites are
fundable from book cash before any IWM sale (rule 3). **Rule 70 on every entry.**
_W40 board (UNCY/LBRX/IRD/ACHV/GLUE/AGEN notes) archived to `archive/research_log_history.md` 2026-10-03._
W40 gate counterfactual: all 7 pre-committed shape kills would have lost by 10/02 (W40 review §3). Keep the gates.

### Monday 10/05 — day-2 plan (42, pre-committed as shapes)
- **FEAM** (5E Advanced Materials, $162M, float 22.4M, ADV 767k, **DE** via 10-K cover; EDGAR field blank).
  Catalyst: Searles Valley asset acquisition **closed 10/01** (8-K 1.01/2.01/2.03). 10/02: +20.1% to **$3.88**,
  94% of range ($3.25–$3.92) on 6.1× median. **Conviction MEDIUM, conditional.**
  - BEFORE sizing (premarket): read the 9/15 8-K (Item 3.02 unregistered sale, 8) and compute 60-day 5-min
    MDD (daily ranges 14–21%, so stop fit is the likely kill, 37).
  - Enter only if 2a ✓, the 9:45–9:50 bar closes upper half, and price is $3.88–$4.27. **Dead below $3.585**.
  - Bear: 8.3M stock-consideration shares (~20%) issued; $10M 8% PIK bridge due ~6/2027 → a raise is likely;
    going-concern language; pre-revenue; +128% in a month. **At the MEDIUM bar, dilution is the tiebreaker.**

### W41 scheduled catalysts (Nasdaq/nextearningsdate rows; confirm on the 8-K, never the row, 65)
| Name | Date | Gates | Conviction | Plan |
|---|---|---|---|---|
| **ANGO** | **10/08 BMO** (issuer) | $635M, ADV 496k, DE ✓ | MEDIUM | Raised FY guide >1% (5a) → day-2 **10/09** if upper-half close |
| **RGP** | 10/07 | $134M, $3.89, ADV 413k, DE ✓ | watch | Beat + raise on 8-K only. Near $3 floor (10) |
| **BYRN** | 10/08 | $81M, $3.48, ADV 661k, DE ✓ | watch | Same. Near $3 floor (10) |
| ~~HELE~~ | 10/08 | EDGAR inc D0 = **Bermuda** | FAIL (52c) | |
Out (cap): PENG, NEOG, NRIX, AEHR, AZZ. Out (ADV): APOG, RELL, ODC, VLGEA, BSET.

### Conditional plans
- **IRD — PDUFA 10/17.** Entry only if a session 10/05–10/13 closes **upper half on ≥1.5× median (~3.4M)** AND
  ≥ $4.84. **Exit by 10/15 close** (29). Kill: closes < $4.40 on heavy volume. 10/02 $4.58 (59%, 0.8×) — no trigger.
  Dilution: S-3 filed 8/07, effective 8/14 — read the shelf size before sizing.
- **UNCY — NDA acceptance PR** (≤30 days from 9/29). Day-2 only on an upper-half close ≥2× median. 10/02 $4.22, sliding.
- **TBCH** ($251M, float 10.8M, short 32%, NV ✓): +9.4% 10/02 on 3.7×. The only catalyst found ("B. Riley Buy/$21")
  reads like a misdated 2025 article (33); no 8-K since 8/06. Date it at the source or PASS (1).

### Closed this session
- **NNBR** FAIL: undisclosed contract terms (49) + authorized shares doubled 90M→180M on 9/30 (8) + Form 144s
  9/23, 9/29, 10/02. **NEOV** FAIL (8): 4.5M-share resale 424B3 + new S-3 10/02; no catalyst found for +21%.

### Held
- **RARE** 31 sh @ $15.08. **10/02 settled close $15.22** (+3.2% vs $14.75), 74% of range. Stop **$14.4336**
  (HWM $15.52, verified `/v2/orders` 10/02). HOLD, stop governs (32a). Rungs +15% $17.34 / +25% $18.85.
  Catalyst (Fayuvi approval 9/17) is now 12 sessions old; EMA validated the UX111 MAA 10/02.

### Scheduled catalysts — other
- ~~RCKT~~ program update 10/06 — **FAIL price ($2.59, 10/02)**. Dropped.
- **CLB** earnings 10/28 · **DTIL** 11/02 (ADV-locked).
- **SECZ**: reopen only if it trades materially below the $2B cap AND the lock-up schedule
  (Proxy p.123) is read at the primary source.

### Sourcing order for W41 premarkets (strategy.md throughput commitments)
1. The earnings calendar for the prior AMC and today's BMO. Confirm "raised" on the 8-K.
2. **FDA/regulatory tape** (approvals, IND clearances, CRLs lifted). Approvals ≠ data readouts:
   clinical-data names went 0/4 on day 2 in W40 (sell-the-news default).
3. Analyst initiations, Buy-rated and dated, **in universe**.
4. Screeners last, as a name source.
5. Log the funnel count in session notes: screened → survivors → entries.

---

### Open escalations awaiting a user decision
1. **Satellite floor arithmetic** (W39 §6, W40 §7: 8.8% then 21.0% at full effort). 50% needs 4/4 slots at the 15% cap. Recommend
   counting slots (≥2 of 4) or a ~30% floor.
2. **Rebalance basis** (lesson 44). Not binding at the 50% IWM cap.
3. **ADV gate vs account size** (46f).
4. **$2B ceiling vs the +25% ladder** (13). It blocks CNXC and PRGS this week.
5. **Midday −5% cut vs stop distance** (67).
6. **`sip` data entitlement for premarket liquidity checks** (66).

### Standing category kills (full detail in archive)
Crypto/treasury (31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI, BKKT, UPXI, HSDT.
Non-US-incorporated (52c): KMTS, GLAS, NB, ADNT, DAVA. Liquidity: GLOO, TLYS, REF, OPTX,
SRZN, TTRX, IDT, TRAK, BSET. Pump/shell: GLND, GRML. **CLOSED:** PAAI (catalyst
falsified), PRTH (pinned deal), NUAI (mandated ATM), SCHL (miss + affirmed guide), PRME
(Gate A 9/25), MLKN (guide cut 9/22), XTND (undisclosed contract value, SPAC ADV).
