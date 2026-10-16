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

### 10/16 PREMARKET UPDATE (Fri, opex; no 8:30 data). Board: **2 MEDIUM tape-confirmed candidates (RAPP #1, EIKN #2)**
Funnel: Alpaca tape (234 headlines, 10/15 15:30 → 10/16 06:30 ET) → all 4 scanners (04:20, stale; breakouts query returned no results, 17) → 15 eligibility
(**15/15 rows, 43 ✓**) → 9 in universe → settled bars + news + EDGAR + 2 searches → **2 candidates**. Binding constraint (53): **board quality.** Floor breached 19 closes → **MEDIUM bar (rule 8).**
**Handed-off check:** HAWK graded at the 10/15 close: $12.82 < $12.99 → **CLOSED** (the day-2 plan died). VSTM closed $9.20 on 10/15, a reclaim of the $8.00 offering price,
but the 10/14 price-action kill already closed the name (42d). It stays closed.
**Kills / passes (10/16):** XXII ($0.63) / AVXL ($1.48) / ACTU fail on price. INR (Scotia Outperform) ADV 280k FAIL. PKE ADV 287k FAIL. CRGY $4.9B / INSW $5.6B fail on cap.
SLDB (UBS Buy $20, 10/15 AMC): **10/13 fell −13% on 2.7× with no cause found** (1 search, 38 → can't grade), plus an S-3ASR/424B5 shelf (8/06) → pass. Re-check if the cause turns out benign.
WVE (UBS Buy $11) at $3.18, 6% above the $3 floor in a steady downtrend (10) → pass. SRTA: a Third Point 5.8% 13D urging a sale. An activist stake isn't on the catalyst list (ESRT precedent) → pass.
SITC: liquidation (a $3.00 special distribution plus delisting) → out. ACRS/CBIO/MGNX: no dated catalyst (1). NYXH (Belgium), IQMX (Finland ADR) are non-US (52c).

## RAPP — UBS initiates Buy, $71 PT (10/15, 5:57 PM ET), the 3rd initiation in 10 days
- Catalyst: analyst initiation wave: **Guggenheim Buy $65 (10/06) → Wolfe Outperform $50 (10/15 AM) → UBS Buy $71 (10/15 AMC).** None of them were on the 6/2024 IPO syndicate,
  so this is independent coverage building, not a quiet-period wave. 10/16 is the first session to react to the UBS note.
- Market cap: $1,419M at $29.57 | Float: 32.4M ✓ (<50M) | Short float: not verified. No squeeze kicker assumed.
- Universe: DE (EDGAR CIK 2012593) ✓ · ADV 351k ✓ but **near the gate (14)**: the IEX median is 14k, thin. Price ✓.
- Setup: a slide from $32.00 (10/06) to $28.36 (10/14). On 10/15 Wolfe's note popped it to $30.39, and it closed $29.45 at 45% of range on 1.1×, so the morning note was partly faded.
- Ladder (11): from $30.50, +15% = **$35.08** and +25% = **$38.13**, far under the $50–71 PTs ✓. Cap at $38.13 ≈ **$1.83B ✓** (13); the ceiling is close, so **no-chase above $31.50**.
- Dilution (8): **no S-3/424B/ATM since the IPO.** Supply is a steady drip of insider Form 144s (8/19 → 10/06), plus routine Form 4s. Cash-rich post-IPO; runway not checked.
- Event (29): the RAP-219 Phase 3 in focal seizures is already enrolling. The long-term open-label safety data is "2H26", date unknown: a small binary risk inside the hold.
- **Entry plan (tape-confirmed, MEDIUM):** open within 10% of **$29.45** (rule 70: quote vs the 10/15 settled close); the **9:45–9:50 bar closes upper half (2b) AND above $30.39**
  (the 10/15 high); opening volume pace ≥1.5× median. **No entry** if it opens flat or red (the third note being ignored), or above $31.50.
- Stop: 7% trail. At $30.50 → **$28.37**, just above the 10/14 low ($28.12). A normal day's range is ~2–5%, so stop fit is OK (37).
- Size: `size RAPP 30.50 28.37` → **14 sh ≈ $427 (14.0%)**, cap-bound (21 risk-based). **CORE FUNDING:** sell ~$427 of IWM right before the BUY (rule 3).
- Conviction: **MEDIUM.** Initiation plans are 0/4 this month (CODI, OIG, ETRA, HAWK), so it needs the shape, not the headline. A three-note wave is the strongest form seen this month.
- **Kill (shape):** an opening pop that fails back under $29.45, or a lower-half 10/16 close on heavy volume (4) → CLOSED. Fallback day-2 Mon 10/19: only on a 10/16 close ≥ $30.39, upper half, ≥1.5×.

## EIKN — H.C. Wainwright initiates Buy, $23 PT (10/16, 6:11 AM ET) + IND submitted for EIK1006 (10/15 PR)
- Catalyst: analyst initiation (dated 10/16 premarket), stacked on the 10/15 IND-submission PR for EIK1006 (prostate cancer). **Weak form:** HCW is a small-cap house, and an IND is not an approval.
- Market cap: $408M at $7.54 | Float: **34.8M ✓** | Short float: not verified.
- Universe: DE (EDGAR CIK 1861123) ✓ · ADV 507k ✓ (IEX median 25k) · price ✓. Next earnings 11/12, outside the hold.
- Setup: a $6.73 low on 10/13 (2% of range), then **two upper-half closes: 10/14 86% on 1.3×, 10/15 $7.54 at 85% on 1.5×.** The tape firmed before the note.
- Ladder (11): from $7.70, +15% = **$8.86** and +25% = **$9.63**, far under $23 ✓. Cap ≈ $520M at +25% ✓.
- Dilution (8): **no S-3/424B since the 2026 IPO** (EDGAR 5/2026 onward: 10-Qs, 8-Ks, 13Gs). **⚠️ IPO lock-up:** 13G filings start 5/06, which puts the IPO around early May 2026 and a 180-day expiry around **early November**.
  That's a supply event just after a 1–5 day hold. **Verify the IPO date and lock-up terms before entry.** If the lock-up ends before 10/23 → no entry.
- **Entry plan (tape-confirmed, MEDIUM):** open within 10% of **$7.54** (rule 70); the **9:45–9:50 bar closes upper half AND above $7.63** (the 10/15 high); opening pace ≥1.5× median.
  No entry if the open is flat or red.
- Stop: 7% trail. At $7.70 → **$7.16**, inside the 10/15 range ($7.08–7.63): a tight fit (37).
- Size: `size EIKN 7.70 7.16` → **59 sh ≈ $454 (14.9%)**, cap-bound. CORE FUNDING sale first.
- Conviction: **MEDIUM**, ranked below RAPP (a single small-house note, thinner tape, the lock-up question). **Take both only if both trigger.** Each needs its own CORE FUNDING sale.
- **Kill (shape):** a fail back under $7.54 after the open, or a lower-half close on heavy volume → CLOSED.

### 10/15 PREMARKET UPDATE (Thu; PPI/retail sales/claims/Philly Fed 8:30 ET). Board: **1 MEDIUM entry candidate (HAWK, tape-confirmed / day-2)**
Funnel: Alpaca tape (223 headlines, 10/14 15:30 → 10/15 06:40 ET) + Nasdaq calendar (10/15: 27 rows, in-universe = banks/ALOY/CTW, nothing BMO with a raise)
→ 2 scanners (04:20, stale: ABEO "+12%", XPER, DBI repeat with no settled move, 17) → 12 eligibility (**12/12 rows, 43 ✓**) → 9 in universe →
settled bars + news + EDGAR → **1 candidate**. Binding constraint (53): **board quality.** Floor breached 18 closes → **MEDIUM bar (rule 8).**
**Handed-off checks (the 10/14 market_close owed these and did NOT do them; done here first):**
- **VSTM CLOSED:** 10/14 $7.71 (O 7.99 H 8.955 L 6.70), 45% of range on 9.7× IEX median. **Under $8.00 = the pre-committed kill fired.** BTIG's PT raise to $24 (10/15) is a maintained Buy (42d), so it doesn't reopen.
- **OIG CLOSED:** 10/14 $9.05 (40% of range, 0.3×), under $9.20 for a second session. The initiation wave is 2 days old and was never bought.
- **CODI CLOSED:** 10/14 $10.68 at 9% of range (−3.4% vs $11.05). The initiation was sold (4).
**Kills / passes (10/15):** CAMP (Needham Buy $8) ADV 271k FAIL. EQBK (beat, no raise, 5) ADV 112k FAIL. AIIR ADV 21k FAIL.
ROCK: $208M D.S. Brown sale to Saint-Gobain to pay down debt. A divestiture isn't on the catalyst list, and the IEX median is 14k → pass (1).
TTI (Clear Street upgrade 10/06, down 13% since) and ESRT (activist 5.8% 13D, 10/06) are stale, with no fresh event. ABEO/UPB/XPER/LTRX/ECVT have no dated catalyst on the tape → out (1).
Out of mandate: BLTE (Cayman), YSS/RDW (Neutral initiations), RCT/CISS/NCPL/BRNX (sub-$3 AH pumps).

## ~~HAWK~~ CLOSED 10/16 (10/15 close $12.82 < $12.99) — Piper Sandler initiates Overweight, $22 PT (10/15, 5:23 AM ET)
- Catalyst: analyst initiation, dated 10/15 premarket. **Better form than CODI/OIG:** Piper was NOT on the IPO syndicate (GS/MS led, IPO 5/06),
  and the quiet period ended long ago, so this is independent coverage. HAWK was the one Overweight in Piper's space-sector launch (YSS and RDW got Neutral the same morning).
- Market cap: $1,213M at $12.38 | Float: 67.4M (above the 50M preference) | Short float: **not verified**. No squeeze kicker assumed.
- Universe: **DE-incorporated** (EDGAR CIK 1750704) ✓ · ADV 1.21M ✓ · price ✓. Filings current (10-Q 8/14).
- Setup: a busted IPO. It opened at $33.53 on 5/07 and is at $12.38 now (−64%). There have been 9 straight lower closes since 9/29 ($15.41). 10/14 closed $12.38 at 32% of range on 2.0×. **A falling knife until the tape says otherwise.**
- Ladder (11): from $13.05, +15% = **$15.01** and +25% = **$16.31**, both well under the $22 PT ✓. +25% cap ≈ $1.60B ✓ (13).
- Dilution (8): the IPO lock-up was **already released 9/02** (early-release clause), and insider Form 144s followed 9/11–10/01. That supply is mostly behind it,
  but insiders are sellers. There's no S-3/424B/ATM since the IPO. The 5/21 8-K (1.01/2.03) is a debt facility. Cash runway not checked.
- **Entry plan, Thu 10/15 (tape-confirmed, MEDIUM):** only if the open is within 10% of $12.38 (2a/2c), the **9:45–9:50 bar closes in its upper half (2b) AND above $12.99**
  (the 10/13 close / 10/14 high), and opening volume pace is ≥1.5× median. Rule 70: quote % vs the **$12.38** 10/14 settled close. No entry if it opens red or flat (the note is being ignored).
  **Fallback, day-2 Fri 10/16:** only on a 10/15 close **≥ $12.99, upper half, ≥1.5× median**. Entry = the 10/16 open within 10% of that close (3).
- Stop: 7% trail. At $13.05 → **$12.14**. Stop fit is tight: 10/14's range was 7.3% in the downtrend, so the stop sits at the edge of a normal day (37).
- Size: `size HAWK 13.05 12.14` → **34 sh ≈ $444 (14.7%)**, cap-bound (49 risk-based). **CORE FUNDING:** sell ~$444 of IWM right before the BUY (rule 3).
- Conviction: **MEDIUM** (rule 8 bar). Initiation plans are 0/3 this month (CODI, OIG, ETRA were all sold), so it needs the shape, not the headline.
- Risk / what kills it: (1) **Space-sector tape:** RKLB −10% premarket on the Neutron slip to 2027, and NQ futures −1.1%. Sector sympathy can swamp one note.
  (2) Insider/post-lock-up supply. (3) Downtrend: an opening pop into resistance gets sold. (4) The 8:30 data dump sets the gap.
  **Kill (shape):** an opening spike that fails back under $12.38, or a lower-half 10/15 close on heavy volume (4) → CLOSED.

### 10/14 PREMARKET UPDATE (Wed, CPI 8:30 ET). Board: **1 MEDIUM entry candidate (CODI, tape-confirmed), 2 conditionals**
Funnel: Alpaca tape (869 headlines from 10/13 06:00 to 10/14 06:30 ET) → 2 scanners (04:20, stale: DBI shows "+11.8%" with no
IEX print since the close, rule 17) → 16 eligibility (**16/16 rows, 43 ✓**) → 10 in universe → settled bars + news + EDGAR → **1 candidate**.
Binding constraint (53): **board quality.** Satellite floor breached for the 17th straight close → **MEDIUM bar per rule 8.**
**Kills / passes (10/14):**
- **BMBL CLOSED (27):** the +56% is a $6.05 all-cash Ithaca Holdings buyout (10/13). Pinned deal.
- **VSTM → conditional only (see below):** Phase 1/2 VS-7375 data plus a **$247.5M offering of 30.94M sh at $8.00** (about 33% dilution, rule 8).
  It also furnished Q3 revenue on the 8-K (2.02): $23.9–24.1M vs $25.1M in Q2, a **sequential decline**, so not revenue acceleration.
  The 10/13 bar closed at 0% of range ($7.45). The scanner's $8.87 is premarket.
- **ETRA CLOSED (4):** the IPO quiet-period initiation wave (Cantor/TD/Evercore/Jefferies) was sold. 10/13 closed $8.66 at **6% of range**
  on about 3× its prior IEX volume.
- **PRCH out (13/7):** a $55M (+$50M deferred) carrier acquisition announced after the close, small next to a $1.96B cap. The cap is at the ceiling,
  and 10/13 closed at 0% of range.
- **GOSS pass (38/57):** Chardan Buy with a printed "$160 PT" on a $9.76, $60M-cap name (post reverse split). The PT looks garbled and can't be verified.
- Out on gates: LQDA ($2.4B; +45% PM on the UTHR settlement), AZZ ($4.1B, ADV 243k; it did raise FY27), BKD $2.4B, ENVX sub-$3, KYNB $24M, SOTK ADV 73k.
- IMTX (Stifel Buy initiation): Immatics N.V. is non-US (52c). DSGR acquisition has undisclosed terms (49). DBI/VRA/ABEO/XPER/TRTX: scanner names, no news, no prints → out (1).

## ~~CODI~~ CLOSED 10/15 (10/14 closed 9% of range, 4) — Ladenburg Thalmann initiates Buy, $17 PT (10/13, 4:20 PM ET, after the close)
- Catalyst: analyst initiation, dated 10/13 AMC, so 10/14 is the first session to react. **Weak form:** Ladenburg is a small broker, and
  this is a single initiation, not a wave. MEDIUM, and only because rule 8 is active.
- Market cap: $831M at $11.05 | Float: 66.9M (above the 50M preference) | Short float: not checked. No squeeze kicker assumed.
- Universe: DE-incorporated (EDGAR) ✓ · ADV 631k ✓ · price ✓. Filings current: 10-Q filed 8/10, auditor change 7/16 (4.01).
- Setup: 10/13 closed $11.05 at 87% of range, a firm close before the news. Recent range is $10.69–$11.20 (10/09 high).
- **Entry plan (tape-confirmed):** a breakout above **$11.20** with the 9:45–9:50 bar closing in its upper half (2b) and opening volume pace
  ≥1.5× median. **No entry** if the open is flat or red, which would mean the market is ignoring the note. Rule 70: quote % vs the **$11.05** 10/13 settled close.
- Stop: 7% trail. At $11.30 → **$10.51**. Targets **$13.00** (+15%) / **$14.13** (+25%). Both are under the $17 PT (11 ✓). +25% cap ≈ $1.06B (13 ✓).
- Size: `size CODI 11.30 10.51` → **40 sh ≈ $452 (14.7%)**, cap-bound (risk-based 58). **CORE FUNDING:** sell ~$452 of IWM right before the BUY (rule 3).
- Risk / what kills it: (1) lender handcuffs from the Lugano fraud: the 5th credit amendment (12/2025) cut the revolver to $100M, sends 100%
  of disposal proceeds to debt and limits restricted payments. That is balance-sheet fragility (7). (2) One small-broker note may carry no flow.
  (3) Over 50M float, so the move should be smaller. (4) CPI 8:30 sets the gap. Kill shape: an opening spike that fails back under $11.05.

### Conditionals (10/14 close checks) — **BOTH CLOSED 10/15** (VSTM kill fired <$8.00; OIG failed again). Graded at 10/15 premarket.
- **VSTM (MEDIUM, day-2 for 10/15):** only if 10/14 closes **upper half on ≥1.5× median (~370k) AND ≥ $8.00** (the offering price holds as support).
  Post-deal cap ≈ 121M sh × $8 ≈ $975M (+25% ✓). Clinical day-2 plans are 0/5, so this needs the shape, not the PR. Kill: a close under $8.00.
  Size ref: `size VSTM 8.20 7.63` → 56 sh ≈ $459.
- **OIG (MEDIUM, re-qualify for 10/15):** the wave is now 5 initiations (GS $13, DB $12.9, RBC $15, Citizens $20, RJ Market Perform). 10/13 closed
  $9.13 SIP, under the $9.20 bar. Re-qualifies only on a 10/14 close **≥ $9.20, upper half, ≥1.5× median**. Kill: a lower-half close <$8.50.

### 10/13 PREMARKET UPDATE (Tue). Board: **0 entries today, 1 new conditional (OIG, for 10/14)**
Funnel: calendar (13 rows 10/13, 1 in universe: UNTY) → Alpaca tape (261 headlines since 10/12 15:30 ET) → all 4 scanners
(stale: RelVol blank, SXC "+6.6%" vs settled +1.2%, rule 17) → 10 eligibility (**10/10 rows, 43 ✓**) → 2 in universe (OIG, CYRX) → 0 entries.
Fails: NRIX $2.3B (huge Q3 "beat" anyway looks like a one-off collaboration milestone, 5e), UNTY ADV 59k, ICCC ADV 21k, NVTS $2.6B,
SMTC $15.7B, BMEA/POLA/FMFC sub-$3. CYRX = BTIG PT raise on a maintained Buy, which is not an upgrade (42d) → pass.
**Handed-off checks done:** TRAX killed (rule 4, below). IRD 10/12 $4.64 at 14% of range, 0.9× → no trigger; the plan's own window
(trigger by the 10/13 close, exit by the 10/14 close) leaves at most a one-day hold → **IRD CLOSED.** SVC 10/12 $5.93 at 12% of range
on 5.0× = distribution (4) → **CLOSED.** UNCY 10/12 $4.05, 50%, 1.3× → no trigger, no kill. ALMS: no NDA PR → stays parked.

### 10/13 MARKET_OPEN: 0 entries. OIG day-2 plan is for 10/14 (not today). Scanner timestamps were 07:45 (stale, rule 17).
BMBL +56.6% on 176× (gap >35%, same-day entry barred by rule 2c). Cause not verified; if a catalyst is found at premarket 10/14, it is a day-2 candidate only.

## OIG — Goldman Sachs initiates Buy, $13 PT (10/13, 5:08 ET) — end of IPO quiet period
- Catalyst: analyst initiation (dated 10/13). **Weak form:** Goldman was a book-runner on the 9/18 IPO, so this is the routine
  syndicate quiet-period wave. Expect RBC/UBS/Raymond James (the leads) today as well. Read them all; they are one event, not several.
- Universe: $886M cap at $8.95 (10/12 settled) ✓ · ADV: 5-session median ~382k (IPO window, rule 46; 10/12 only 259k) ✓ but thin ·
  **FL-incorporated** (EDGAR CIK 2124472) ✓ · float ~20M IPO shares + insiders · short float not checked.
- Setup: IPO **priced $12, cut from the $15–17 range**. Opened $11.50 and slid to a $7.78 low 10/07. The stock is a busted IPO at −25%.
  Ladder (11): from $9.00, +15% = $10.35 and +25% = $11.25, both under the $13 PT ✓ and under the $12 IPO price (supply zone above).
- Dilution (8): fresh IPO, 180-day lock-up (~mid-March 2027). An S-8 filed 9/21 is not an offering (8b). Clean for the hold window.
- **Day-2 plan, Wed 10/14 (MEDIUM, rule 8):** only if 10/13 closes **upper half on ≥1.5× median (≥~960k sh)** AND ≥ $9.20.
  Entry = the 10/14 open if within 10% of the 10/13 close (rule 3), else the 9:45–9:50 base (2b). Rule 70: quote vs the 10/13 settled close.
  CPI is 10/14 at 8:30 ET (pre-open, not FOMC). Defer the entry if the 9:30–9:45 range is >10% (2a).
- Stop: 7% trail. Example at $9.30 → $8.65; targets $10.70 (+15%) / $11.63 (+25%).
- Kill (shape): a 10/13 close in the lower half on heavy volume (initiation sold = 4); a close under $8.50.
- Risk: E&S Florida homeowners book in **hurricane season** (Isaias is in the Gulf). A storm headline is an un-stoppable gap (29).
  Underwriter notes carry little information. Thin ADV for exits.

### 10/12 PREMARKET UPDATE (Mon, Columbus Day). Board: **0 entries today, 1 new conditional (TRAX, for 10/13)**
Funnel: calendar (3 rows 10/12, 14 rows 10/13, 0 in-universe BMO) → Alpaca tape (275 headlines) → 3 searches → 4 scanners →
15 eligibility (**15/15 rows, 43 ✓**) → 13 in universe → 0 entries. Fails: QNRX $22M cap; ASBH ADV 259k (Piper Overweight initiation).

- **TRAX CLOSED 10/13 (rule 4):** 10/12 opened $39.45 (+24%), high $40.50, closed **$34.05 at 14% of range on 11.2× median**.
  That is distribution, and the pre-committed kill fired. Data read is moot. Clinical day-2 plans: 0/5.

### 10/12 kills / passes
- **HUBG CLOSED:** Baird upgrade to Outperform ($29 PT = +12.8% < the +15% strike, rule 11). It's also a serial restatement name
  (2023–25 financials non-reliance, 2025 10-K and Q2 10-Q still unfiled per web search) with three distribution closes 10/07–10/09
  (6% / 39% / 4% of range on 2.2–3.1×, rule 4). Can't verify financials, so a catalyst can't be graded (57).
- **SVC → LOW, no entry.** Cause found: an unsolicited $2.0B TKO cash proposal for the hospitality portfolio (Benzinga 10/12); the
  board "will review." **No 8-K on EDGAR as of 10/12 premarket** (last filing 9/21), so 57 is not met. A non-binding proposal for an
  asset is not on the catalyst list. 10/09 bar: spiked to $7.93, closed $7.14 (56% of range, 11×), a 10% fade from the high, which a 7%
  trail can't survive. Reopen only on a definitive agreement + 8-K.
- KLRA (+16% 10/09, 88%, 2.1×), MEI (5.7× reversal 10/07), SVRA, IMRX: no dated catalyst on the tape or in search → out (1).
- IRD 10/09 $4.64 / 64% / 0.8× → no trigger (needs ≥$4.84 upper-half ≥1.5×). UNCY 36% / 1.1× → no trigger, not yet distribution.
  ALMS 10/09 Phase 3 ONWARD data PR is a data presentation, not the NDA submission → stays closed.
- Out of mandate: YMAT/LNKS/VCIG etc. (sub-$3 premarket pumps), CCC (GTCR/Elliott deal talk, large cap), IREN (cap), SKYA (tender).

### Conditional plans (carried forward; re-read the settled bars every premarket)
- ~~IRD~~ **CLOSED 10/13** (no trigger inside the window). Was: PDUFA 10/17 (a SATURDAY → the FDA can act Fri 10/16 or earlier).** Entry only if a session through
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
