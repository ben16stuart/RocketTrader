# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Tue 2026-09-22 (Week 39 day 2 — **satellite floor breached; MEDIUM bar active per rule 8; market_open NO ENTRY, see MLKN close + widen below**)  ← CURRENT

**Satellites 0/4, floor breached 0% < 50% at two logged `market_close` sessions (9/17, 9/21
— per lesson 58's corrected count).** Rule 8's MEDIUM-conviction bar is active:
**searched at the MEDIUM bar — all 4 screeners run plus the earnings calendar, pushed deeper
down each list.** The catalyst requirement itself does not relax, and nothing was admitted
without one.

### 🚩 VERDICT: NO ENTRY TODAY — but ONE live candidate queued for `market_open`

🚨 **THE FINDING OF THE SESSION IS AN INSTRUMENT ONE AND IT INVALIDATES THE WHOLE
`top_movers` BOARD.** See lesson 59 (new). Every "mover" below reconciled **8-for-8** under
lesson 55b's arithmetic check — and **six of the eight had ZERO premarket trades.**

| Scanner printed | Reality (Alpaca `sip`, 08:00Z→10:23Z) |
|---|---|
| EVMN +7.2% @ $10.13 | **306 shares total, $3,081 notional.** The $10.13 IS a single 202-share print |
| FBRT +6.1% @ $8.18 | **ZERO premarket trades.** No trade occurred at that price |
| BBW +5.2% @ $26.03 | **500 sh @ $24.74 = −0.0%.** The scanner's price does not exist |
| GOSS +3.5% @ $11.67 | **ZERO trades** |
| QTRX / QUIK / SIGA / ACCO / CURR +2.3–2.9% | **ZERO trades each** |

**BBW is the clean falsification**: the arithmetic was perfectly self-consistent around a
price at which nothing traded. ⚠️ **And the check nearly died on its own instrument** — the
Alpaca `iex` feed returns **zero premarket bars even for SPY**; only the `sip` control run
(lesson 38) revealed the real tape. A blank on the wrong feed reads exactly like a finding.

### Named catalyst kills (independent of the volume finding)

| Name | Kill |
|---|---|
| **EVMN** | ❌ **Rule 1 + the only dated news is BEARISH.** Phase 2b of EVO756 in atopic dermatitis **MISSED primary and secondary endpoints at every dose** (9/08); development in AD ceased. The 9/15 item is a **corporate deck** — ASPN precedent: a deck is not a catalyst |
| **FBRT** | ❌ **Rule 1 — not a catalyst type.** CEO reappointment (Byrne back, Comparato resigned 9/15) + a routine **$0.20 dividend, ex-9/30.** Neither is on the catalyst list |
| **BBW** | ❌ **Rule 5 disqualifier — guidance CUT**, FY26 revenue to $500–525M (−3.3% at midpoint); PT cut $61.25 → $43.00. Trading at a **fresh 52-week low ($24.15)**. A bounce off a low on no news is rule 1's trap shape |
| **GOSS** | ❌ **Rule 7a / 8a — the catalyst IS the dilution event.** Real regulatory progress (FDA called the PROSERA effect size a *review* issue not a *filing* issue; seralutinib NDA planned this month). But the financing is **up to $250M gross against a $69M market cap ≈ 3.6× the entire company**, structured and milestone-contingent ($25M at close, ~$125M on NDA acceptance, $100M on approval) — against a **3.8M float** (rule 49b). Auto-kill tier |
| **CURR** | ❌ **Rule 38 — unresolved identity/domicile.** EDGAR's ticker lookup for `CURR` resolves to **Avenir Wellness Solutions (DE)**, a different company from Currenc Group. An unresolved gate is a FAIL, not a pass. Zero premarket volume and no catalyst regardless |
| **USDE** (only `unusual_volume` row >1.0×, 2.5×) | ❌ Standing **crypto/treasury mandate kill** (lesson 31) |

**Rest of board**: `unusual_volume` printed **19 of 20 rows below 1.0×** (RelVol unusable, 6th
straight session). `breakouts` errored on Finviz and returned 3 rows, all <2.5%.
`short_squeeze` — high short floats (WOLF 70.7%, WYFI 55.7%, FRMM 48.0%) but **no catalyst on
any of them and near-zero RelVol**; rule 9/10 requires short float **+ a catalyst**, and the
catalyst leg is missing on all 20. Standing kills carried: BNC, DFDV, CYPH, FWDI, ABTC, NUAI,
OPTX, DUOT, ALMU.

### MIDDAY afternoon scan (10:15 ET) — 4 movers checked, all killed

`unusual_volume` re-run mid-session. Four names web-searched for a fresh dated catalyst
(inline, <5 searches, no subagent per the token-cost rule):

| Name | Kill |
|---|---|
| **GRML** (+73.6%, 44.7×) | ❌ **Un-gradeable + massively extended, not a fresh setup.** Real news exists (Sarfartoq rare-earth land expansion, US-Denmark-Greenland security deal, high-case NPV $2.05B) but the **issuer is a serial-rebrand shell**: EDGAR CIK 0001907223 = Redwoods Acquisition Corp (2022) → ANEW Medical (2024) → Klotho Neurosciences (2024) → Greenland Mines Ltd (2026-03-10), **3 name/business changes in under 2 years**, `stateOfIncorporation` blank and SIC still reads "Biological Products" — the record has not caught up to the rebrand. Rule 38: an unconfirmable domicile is a FAIL, not a pass. Independently, the stock is **already +474% over 4 sessions** ($2.85 on 9/18 → $16.35 today) — this is deep into a parabolic blow-off, not a base or a first/second-day gap (rule 2/2c don't apply this many days out). Two independent kills, neither needed the other. |
| **EAF** (+16.9% on this scan, but settled **−5.78%** on the day per live search) | ❌ Standing no-catalyst kill reconfirmed — no news since the Q2 miss (EPS $1.54 vs $1.65 consensus); today's print was a scanner artifact, the stock actually closed red |
| **SVIA** (formerly ProCap Financial/BRR) | ❌ **Rule 1 — not a catalyst type.** Today's news is a **ticker/name change** (BRR → SVIA) plus a marketing claim about AI benchmark performance; neither is earnings, FDA, contract, upgrade, or insider buying |
| **CYPH** | ❌ Reconfirms the standing **rule 31 crypto-treasury mandate exclusion** — "digital asset strategy anchored by Zcash." Today's news (a board appointment) is not a catalyst type regardless |

**Verdict: NO ENTRY.** No forced cuts (0 satellites open). Satellite floor still 0% — if
unchanged at today's `market_close`, that is the **3rd consecutive breach**, which per rule 8
is escalation territory for tomorrow's premarket, not just a note.

---

## 🎯 MLKN — MillerKnoll Q1 FY2027, reports BMO **today 2026-09-22**

- **Catalyst**: Q1 FY27 earnings, **pre-market today**. Sourced from the earnings calendar,
  not a screener (lesson 41). Consensus **EPS $0.35 on revenue $943.3M**; company's own Q1
  guide is **net sales $928–968M, GM 38.7–39.7%**.
- **Market cap**: $1,397M | Float: 66.7M sh (97% — **not** a low-float name) | Price $20.32
- **Universe**: price ✅ · cap ✅ · **rule 13: +25% → $1,746M, still clears $2B with ~15%
  headroom** ✅ · **domicile MI (Michigan), US-incorporated** ✅ (rule 52c, read from EDGAR)
- **Rule 46 (median ADV, run unconditionally per 46g)**: 63-day **median 627,900 — passes the
  300k gate by 109%**; mean 740,474; 2-y median 544,000; **all five most recent sessions above
  the gate** (652k · 556k · 662k · 1.67M · 1.28M). ✅ **No contamination — clean on every cut**
- **Rule 8 (dilution) — the cleanest tier available**: **no live shelf.** No S-3, no ATM, no
  424B5. Last S-3ASR was **2017** (long expired); the only 424B3 is the **2021 Knoll merger**.
  Everything since is **S-8 only — rule 8b: an S-8 is not an offering** ✅
- **Rule 45 (catalyst-day multiple, measured on its OWN 2-y history)**: median daily range
  **2.94%** (a quiet name — 45b says the gate is *strictest* here). Catalyst multiple **3.94×**
  → **predicted catalyst range 11.60% = 1.66× the 7% trail.** 📌 **That is the closest to
  fitting a 7% trail any catalyst name has come in weeks** (cf. KMTS 2.70× · PLAY 3.61× ·
  FTK 4.33× · SOC 6.54× · EAF 6.89×)
- **Rule 11 (analyst ladder)**: entry ~$20.32 → **+15% rung $23.37 · +25% rung $25.40.**
  Dated Street target (9/20) **$35.00**, range $35.35–36.75. ✅ **Both rungs clear with large
  room** — the inverse of the OOMA/PD kill shape. ⚠️ **Coverage is only 1–2 analysts and the
  quoted avg/low/high are internally inconsistent ($35.00 avg vs $35.35 low)** — thin ladder,
  passes but weakly (11b)
- **Conviction**: **MEDIUM**, pending the print. Not enterable now — *"OK to enter AFTER a
  confirmed beat, NOT before."*

### 🚩 MLKN CLOSED at `market_open` 9/22 — Gate A failed on the print, primary-sourced (8-K ex-99.1)

**Q1 FY27 actual**: revenue **$923.4M — missed BOTH consensus ($943.3M) AND MLKN's own Q1
guide floor ($928M)**; net sales **down 3.4% YoY (organic −3.3%)**; NA Contract sales
**−5.2% organic**, orders −1.6%; Intl Contract sales **−6.2% organic** despite orders +17.9%.
GAAP EPS $0.38 / adj EPS $0.53 vs $0.35 consensus — the only clean beat in the print.

**Gate A (must be)**: FY27 guide RAISED >1.0% vs MLKN's own prior guide. **Actual: revenue
range CUT $3.93–4.13B → $3.88–4.03B (≈−1.9% at midpoint); adjusted EPS range UNCHANGED
$1.85–2.15.** Per lesson 5f a reaffirmation is a 0% change, not a raise — this is worse, a
guide **cut** on the top line with EPS merely reaffirmed. **KILL, no ambiguity.** Gates B–F
never reached — Gate A alone is dispositive. Stock reaction muted (+1.7%, below MA20/MA50),
consistent with the actual print, not the headline EPS beat. **CLOSED, not dated for a
recheck (rule 5's beat-without-raise is a disqualifier, not a demotion).**

### Market_open widen (rule 8 MEDIUM bar) — three more checked inline, all killed

Macro context: SPY +0.08%, IWM +0.61%, Russell fut +0.70% — a mildly green tape, not a
risk-on day that would explain moves by beta alone.

- **MAZE** (+28.2%, 0.8x actual volume despite unusual_volume printing 9.9x RelVol —
  another RelVol/reality mismatch, lesson 17g) — **no dated catalyst found.** Company's own
  IR news page's most recent item is 9/02 (investor-conference attendance, not a catalyst);
  the only real data readout (Phase 2 HORIZON, MZE829) is from **3/25/26, six months stale.**
  Rule 1 fail — volume/price alone, no named catalyst.
- **VFF** ($3.09, +7.1%, real volume 0.9x avg despite 4.5x printed RelVol — same RelVol
  mismatch) — catalyst candidate was a CEO open-market buy, but **only $101,258 (35,000 sh,
  +0.36% of his existing 9.73M-share stake)** — too small to be signal, and **actual volume
  is NOT confirming** (below average, not "unusual"). Price $3.09 is a hair above the
  sub-$3 trap floor. Kill on both volume-not-confirming and catalyst-too-thin.
- **FOSL** (+5.1%, 3.7x RelVol) — no news since Q2 earnings (reiterated FY guidance, not
  raised); no dated catalyst today. Kill on rule 1.

**Verdict: NO ENTRY at market_open.** Satellite floor still breached at 0%; escalates to a
3rd consecutive `market_close` breach if nothing is found by close. Widened board (screener
+ earnings calendar + inline movers check) produced zero names clearing rule 1's catalyst
bar — this is 36's "board quality" problem, not a discipline failure, and it is stated as
such rather than defaulting to 48a's framing without re-measuring (per lesson 53).

### ⚠️ The two things that can kill it, stated in advance

1. 🚨 **GAP RISK IS THE REAL RISK, NOT RANGE** (rule 45a/29). MLKN's own earnings-day gaps
   over 2 years include **−25.83% (2026-03-26)** and **−9.45%**, alongside +9.02% and +5.80%.
   **A 7% trail cannot price a −25.8% gap — it fills at the open, wherever the open is.**
   The 1.66× range figure is the *optimistic* half of this name's history.
2. 🚨 **CONSENSUS IS A LOWERED BAR** (rule 5c). Street EPS was **cut 14.6% in three months,
   $0.41 → $0.35.** A "beat vs $0.35" is a beat against a number that was walked down to meet
   the company. **The firm reference is MLKN's own Q1 guide ($928–968M), not consensus.**

### 📌 Pre-committed gates for `market_open` — written as SHAPES, not levels (rule 42c/42e)

- **Gate A — size the raise (5a/5d).** FY27 guide must be **RAISED >1.0% against MLKN's OWN
  prior FY27 guide**, not against consensus. **State the raise as a percentage.** A
  reaffirmation, a withdrawal-restoration, or a sub-1% nudge is a **KILL** (PD +0.3% · CHPT
  +0.6% · SWBI +0.95% · AVO +1.25% — rule 5a is 4-for-4 as a kill in that band).
- **Gate B — pass-through (5d).** If Q1 beat its own guide, the year must absorb it. **Beat
  the quarter, decline to raise the year → the beat is pull-forward → KILL.**
- **Gate C — price action (rule 4).** **9/22 must close in the UPPER HALF of its own daily
  range. Below the midpoint = KILL regardless of catalyst** — and per 42d/45e a price-action
  kill **CLOSES** the name, it does not date it for a recheck.
- **Gate D — the gap (2c/45a).** Gap **>35% → second-day entry only.** Gap **DOWN materially
  → dead**, do not attempt to catch it; the trail cannot price this name's gap history.
- **Gate E — composition (5e).** Read past the headline: if a **non-recurring item is larger
  than net income**, the one-off IS the beat → KILL.
- **Gate F — open item, unresolved (30/30b).** Four **Form 144s** (7/02, 7/16, 8/04, 8/05)
  plus heavy Form 4 clusters (7/16, 7/23, 8/03) sit right after the 7/20 10-K. **The
  transaction CODE and the `<aff10b5One>` plan-adoption date have NOT been read.** Per 30b
  the flag *reverses* the read, so this is **flagged as unresolved, not scored either way.**
  Cheap to close: fetch the raw Form 4 `.xml` (never the `xslF345X06/` rendered page).

---

### Open escalations awaiting a user decision — TWO (unchanged)

1. **Which rebalance basis governs** (lesson 44) — slice vs. book. Non-binding while IWM sits
   at/near the 50% cap (the cap governs regardless of basis).
2. **The ADV gate binds on account size, not tradeability** (46f). ⚠️ **Note MLKN does NOT
   raise this one** — at a median 627,900 ADV a ~$470 satellite is trivially fillable.

### Scheduled catalysts

- **MLKN Q1 FY27 — BMO TODAY 9/22** (above) · **RCKT program update 10/06** ·
  **CLB earnings 10/28** · **DTIL 11/02** (ADV-locked).
- **THO, KBH, WOR, AZO** also report 9/22 — **all FAIL rule 13's $2B cap**, not screenable.
- **SECZ** — re-open only if it pulls back materially below the $2B cap AND the lock-up
  primary source (Proxy "Other Transaction Agreements — Lock-Up Agreements," p.123) is
  actually read, not summarized secondhand.
- 🚨 **`weekly_review` W36 (9/04), W37 (9/11), W38 (9/18) — THREE owed**, chain 19+ sessions
  stale (last good 8/28 W35). Escalated every session; not remediated (lesson 47c).

### Standing category kills (unchanged — full detail in archive)

Crypto/treasury mandate (lesson 31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI,
BKKT, UPXI. Non-US-incorporated (lesson 52c): KMTS, GLAS, NB, ADNT. Liquidity-locked: GLOO,
TLYS, REF, OPTX (ADV 258k). PAAI CLOSED (catalyst falsified at the primary source, 9/18).
PRTH CLOSED (rule 27, pinned deal price). NUAI CLOSED (lender-mandated $100M ATM).
