# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Thu 2026-09-17 premarket (Week 38 day 4 — **first post-FOMC session**)  ← CURRENT

**Book (hand-built — BASE NAMED, lesson 23a/44)**: **$2,992.32** = IWM **9.8636 sh**
(raw qty from `GET /v2/positions/IWM`, lesson 24a/24d — the formatted table says "10")
× **$283.92** *settled* 9/16 close = **$2,800.31 (93.58%)** + notional cash **$192.01 (6.42%)**.
✅ **Inside the 10% buffer — no bearish thesis required or written.**
Satellites **0/4** · weekly count **0/5** (last trade 8/26 OMER stop-out) ·
max satellite **$469.25** · 1.5% risk **$46.92** · shared cash $1,935.21 (pooled with Bull —
**fund from core, not cash**).

## 🚩 VERDICT: NO ENTRY — hold IWM. **Seven in-universe names screened, seven dead on named gates.** But today's board is different in kind from the last eight, and that is the finding: **for the first time, stop width was NOT the binding constraint.**

### market_open addendum (9:45 AM ET) — three fresh names checked, zero catalysts, zero trades

`unusual_volume` ∩ `top_movers` = **SECZ, GOSS** (plus HAWK/OSS, already closed above). All
three (SECZ, GOSS, PSIX — PSIX pulled from `unusual_volume` alone on its +12.4%/5.0x size)
passed `eligibility` cleanly but **none has a dated catalyst for today's specific move**:
- **SECZ** (+14.9%, 5.7x, float 5%) — only recent analyst action is Needham's Buy init,
  **9/8, nine days stale.** No fresh news found. Rule 1 kill.
- **GOSS** (+6.8%, 3.3x) — the FDA/seralutinib surge was a **prior, larger (+25%) move**;
  today's smaller gain has no fresh dated news, and the company just did a **1-for-80
  reverse split to meet Nasdaq listing requirements** — a distress signal, not a momentum
  setup. Rule 1 kill.
- **PSIX** (+12.4%, 5.0x, float 30%) — CEO appointment (8/17) and Q2 earnings (8/6) are
  both weeks stale; no dated news found for today's move. Rule 1 kill.

No catalyst named on any of the three → no trade, per rule 1. Holds the premarket verdict.

### midday addendum (12:15 PM ET) — no satellite positions to review (core-only book); one real catalyst found, barred by the >35% rule

Rocket holds zero satellites today (confirmed via `position_reconciler` — Rocket's only
live position is the IWM core; JPM/SCHW/SPY on the shared account are Bull's). Nothing to
cut or tighten. `unusual_volume` re-scanned for afternoon setups:

- **PAAI (Paradium.AI, fka The Arena Group)** — real, dated, verified catalyst: a 10-year,
  **$1B MediaOS deal with Roundtable** (NASDAQ:RTB), plus an $89M minority-stake investment
  for ~49% of the company. Confirmed via web search, not scanner text alone. Raw yfinance
  bars confirm the move is real, not a scanner artifact (lesson 17/55 check run): 9/16 close
  **$0.90** → 9/17 high **$3.47**, last **$3.34** = **+271%**, volume **31.76M vs 13.1M
  float (2.4x the entire float turned over)**. NYSE American (ASE) — passes the exchange
  gate. Mcap $158M — in-universe.
  🚫 **NOT tradeable today** — CLAUDE.md's >35% same-day rule requires a second-day entry;
  today's spike is the day-1 print. Also flagging: every close in the trailing 5 sessions
  was **under $3.00** ($0.90–$1.09) — today is the first bar to clear the price floor, and
  only because of the spike itself. Whether it holds above $3 through the close is unverified.
  **Per the missed-catalyst rule: check PAAI every session for the next 3 days for a
  second-day or pullback entry**, gates (esp. rule 13 cap-lid, rule 11 analyst ladder if any
  exists, and a fresh 9/18 base check) required before any entry.
- Rest of the board: **USDE, BRR** — standing crypto/treasury mandate kills. **GLOO** —
  liquidity-locked (not catalyst-reopenable). **ACVA, ALMU** — already-closed names (cash
  tender cap; stale catalyst respectively). Remainder flat-to-negative or closed-end funds.

No trade. Satellite floor remains breached (0% < 50%) — see portfolio_state.md.

---

# 🚨 THE FINDING: the board was killed by CATALYST QUALITY, not by the 7% trail — which is evidence AGAINST lesson 48a's framing

Eight sessions have concluded that "the catalyst screen works and the stop width forbids
everything it finds" (48a/48e/48g). Today falsifies that as a general claim. Run 48d's
diagnostic on today's survivors' **normal-day median ranges**:

| Name | Median daily range | ÷ 7% trail | Fits the trail? |
|---|---|---|---|
| **UNCY** | 5.56% | 0.79× | ✅ yes |
| **GLAS** | 5.61% | 0.80× | ✅ yes |
| **DUOT** | 6.84% | 0.98× | ✅ borderline |
| **HAWK** | 6.87% | 0.98× | ✅ borderline |
| **KMTS** | 6.30% | 0.90× | ✅ yes |
| TRAX | 8.68% | 1.24× | ❌ |
| OSS | 7.97% | 1.14× | ❌ |

**Five of seven fit inside a 7% trail on a normal day — and the board still produced
nothing**, because the catalysts were **an MoU with no committed dollars (HAWK), a
$400,000 award against a $224M market cap (OSS), an unexplained cannabis premarket
print (GLAS), and a class-action-adjacent bounce off a Complete Response Letter (UNCY).**

📌 **Why this matters and why it is written down rather than omitted.** 48a reframed lesson
36 from a *board-quality* problem into a *mandate-quality* one — "everything qualified and
the stop doesn't fit any of it." **On the first board where the stop DOES fit, nothing
qualified anyway.** The two constraints are separable and today separated them. **48a's
reframing was over-claimed; lesson 36's board-quality diagnosis is alive and was today's
actual answer.** Recorded against Rocket's own argument, per 45h/51e.

---

# 🚨 THE SECOND FINDING: yesterday's MDD statistic now cuts AGAINST the change Rocket asked for

Lesson 51 (written yesterday) showed a 7% trail keys on **drawdown from the running high**,
not daily range, and that KMTS's 9/15 catalyst bar had an MDD of only **6.18%** — so the
trail survived and would have paid **+15.49%**. Escalation 2 asked to adopt MDD-from-HWM as
the stop-fit statistic on that evidence.

**Run the identical measurement on the very next bar, KMTS 9/16, 77 five-minute bars:**

| | Value |
|---|---|
| Bar | O 25.20 · H 25.328 · L 23.86 · C 24.08 |
| **Max drawdown from running high** | **5.80%** (13:40 ET) |
| **7% trail** | ✅ **SURVIVED — never threatened** |
| **Open → close** | 🚨 **−4.44%** |

🚨 **The trail survived and the trade lost money anyway.** That is the counter-example to
yesterday's argument, found one session later on the same stock.

📌 **What this does and does not change.** Lesson 51's *correctness* is untouched — MDD is
still what the broker computes and range is still a loose bound on it. **What changes is the
claim attached to it.** Yesterday's framing implied the corrected statistic would have
*unlocked profit*. It would not have. **It removes a false veto; it does not supply an edge.**
A gate that stops vetoing good trades also stops vetoing bad ones. **Escalation 2 is re-stated
below in the honest form: this is an accuracy fix, not a profit case.**

---

### 🥇 KMTS — Kestra Medical. **Gates B and E PASSED today — and rule 4 closed the name on the same session**

**The settled 9/16 bar: O 25.20 · H 25.328 · L 23.86 · C 24.08 · V 825,000.**

| | Gate | Status |
|---|---|---|
| **A** | Rule 4 shape on the 9/15 catalyst bar | ✅ **PASS** (closed 93.3% of range) — banked 9/16 |
| **B** | Stop fit (range ≤10% on a non-catalyst session) | ✅ **PASS — range 6.10%.** Held exactly as written per rule 42/51d even though 51 proved it measures the wrong thing |
| **C** | Dilution | ✅ **PASS** — S-3ASR 2026-04-01 **undrawn**, $244.7M cash |
| **E** | Calendar | ✅ **PASS — the FOMC is done.** Hiked 25bp as priced |
| **D** | Liquidity | ⚠️ **MARGINAL.** Mean 381,055 (catalyst-contaminated); **63d median 319,300 (+6.4%); 2y median 254,200 FAILS by 15%.** Last two non-catalyst sessions: **310,500 · 241,600** |
| **F** | Ladder | ⚠️ **Still no DATED post-print target** (11a) |
| 🚨 **G** | Domicile | ❌ **Bermuda (`stateOfIncorporation` = D0).** Unresolved → rule 38/52b **FAIL** |
| 🚨 **RULE 4, on the bar that would decide TODAY's entry** | 🚨 **FAIL — and this is the binding kill** | **Closed −4.37% at 15.0% of its range on 825,000 shares = 2.58× the 63d median and 3.25× the 2y median.** Below the midpoint on heavy volume = **distribution** |

🚨 **The market move does not explain it.** SPY closed −0.44% and IWM −0.43% on 9/16.
**KMTS was −4.37% — ten times the index — at 15% of range on 2.6× volume.**

📌 **And the entry window is gone on its own terms.** The catalyst printed 9/14 AMC. Day 1
was 9/15 (+4.65%), **day 2 was 9/16 and gave the move back.** Rule 2/3's second-day
continuation entry is a *day-2* instrument; today is day 3.

❌ **KMTS is CLOSED, not deferred** (42d/45e: a price-action kill closes a name rather than
dating it). **Re-open on a new dated catalyst only** — and the gate-G domicile ruling is
still owed regardless.

🥇 **Worth recording for what it says about the gate stack, not about the stock.** KMTS
cleared the guidance gate (5g, first ever), gate A (first ever), **and today gates B and E
— and a fourth gate killed it anyway.** That is 5g's shape repeating: *"the guidance gate
finally passed something, and two other gates killed it anyway."* **Independent gates do
not net out** (42a), and a name accumulating passes is not thereby earning a trade.

---

### The board — five overlap names, all dead before any research

`top_movers` ∩ `unusual_volume` = **XTND · DUOT · BNC · USDE · HAWK.**
**BNC and USDE are standing crypto/treasury mandate kills (lesson 31) — mandate checked
before the chart, zero research spent.** DUOT is a standing 7a kill (~60× announcement-to-cash).

✅ **Instrument note first, because it nearly became a false alarm.** The scanner's prices
looked wildly wrong against 9/16's settled closes (GLAS "+7.2%" vs a −0.12% close, SOC
"+2.8%" vs −7.66%, HAWK "+3.9%" vs −1.94%). **They are not wrong.** Every row reconciles
**exactly** as a **9/17 premarket quote against the 9/16 settled close** — GLAS $8.61/$8.03
= +7.2% ✓, ACP $4.96/$4.65 = +6.7% ✓, OSS $8.98/$8.52 = +5.4% ✓, HAWK $16.80/$16.17 = +3.9% ✓,
FLNC $7.27/$9.05 = −19.7% ✓, ALMU $11.47/$13.43 = −14.6% ✓. **Eleven for eleven.** 📌 **This
file was one step from recording "four sign flips, the Change % column has reverted to broken"
as an instrument-health finding. It would have been false** — lesson 39/38: verify the entity
before asserting the defect.

| Name | Kill |
|---|---|
| 🥇 **HAWK** | The best-constructed name on the board and it dies three ways. ❌ **Rule 13 is the clean one: $2B ÷ 98.0M sh ÷ 1.25 = a hard no-chase ceiling of $16.33 — premarket is $16.80, already 2.9% ABOVE it.** The +25% rung breaches $2B; a one-rung name at best, the ETON shape. ❌ **Rule 4:** 9/16 closed **−1.94% at 31% of range** on 1.02× volume. ❌ **Rule 1 / 49a:** the catalyst is a **Memorandum of Understanding with Leonardo** — an MoU has **no committed dollars at all**, which is worse than ELMT's IDIQ (that at least had a $150M guaranteed minimum). The second "catalyst" is a **Russell 2000 index addition effective 9/21** — 🥇 **a mechanical, pre-announced flow event, and one Rocket's OWN IWM CORE will capture for free.** Buying HAWK to front-run the index that Rocket already owns is paying a satellite's risk budget for beta it holds. ⚠️ Also: **IPO lock-up expired 9/01 with officer Form 144s** (30a supply pressure) and float 67.6M > 50M, so no low-float kicker |
| **OSS** | ❌ **Rule 7a decides it in one line: the catalyst is a ~$400,000 award — 0.18% of a $224M market cap.** That is a press release, not a revenue-changing deal. ❌ **Rule 8 / 8e:** **S-3 filed 8/24 and S-3/A 8/28, three weeks old, size unconfirmed** — a company touting a contract three weeks after filing a shelf may be advertising into the raise; and an unconfirmed size is rule 38's "resolve the gap, never score it." ❌ **Rule 4:** 9/16 closed **−1.05% at 38% of range on 0.90× volume** — the tape rejected the award **on the day it was announced.** ❌ **Rule 37a:** median range **7.97% = 1.14× the entire trail on a normal day** |
| **UNCY** | ❌ **Rule 1 — there is no bullish catalyst; the window's news flow is NEGATIVE.** Four securities class-action solicitations dated **9/14–9/16**, all referencing the **6/30/2026 FDA Complete Response Letter** on oxylanthanum carbonate. 🚨 ❌ **Rule 8 at its worst tier: the ATM was expanded to $150M on 6/05 against a $131M market cap — the authorization is LARGER THAN THE ENTIRE COMPANY.** Float 27.2M = **99% of shares out**, i.e. no insider lock and maximum supply. **A +6.5% premarket print on a post-CRL litigation name with an over-100% ATM is the pump shape lesson 1 was written for, not a catalyst** |
| **GLAS** | ❌ **Rule 1 — no catalyst found at ALL.** The only dated items are a routine H.C. Wainwright conference slot and an **SVP insider SALE (Form 4, 9/14).** An unexplained +7.2% premarket with no verifiable cause is lesson 1's explicit AVOID. ❌ **Rule 8:** live **$100M ATM prospectus dated 7/15/2026** = 13% of a $757M cap. 🚨 ❌ **Domicile: British Columbia** — escalation 4 again, and per 38/52b unresolved = FAIL. ❌ Rule 4: 9/16 closed at 43% of range |
| **XTND** | ❌ **Lesson 46j: only EIGHT daily bars exist — the entire history IS the atypical post-listing regime, so it is un-measurable rather than passing.** ❌ **Rule 37a: median range 14.56% = 2.08× the ENTIRE trail on a normal day.** 🚨 ❌ **Rule 38: the two instruments disagree on a UNIVERSE gate by 11.7× — the scanner says cap $101.15M, `eligibility` says $1,178M** (249.1M sh × $4.73). An unresolved universe gate is a FAIL. No dated catalyst, no float, earnings date unknown |
| **RZLT** | ❌ **The 9/09 Phase 3 sunRIZE readout MISSED its primary endpoint** — a failed readout is not a catalyst. ❌ 9/16 AMC earnings **content could not be confirmed from any primary source** → rule 38 FAIL |
| **ALMU** | Reported 9/16 AMC and is **−14.6% in premarket.** A negative reaction — kill on rule 4/5 without further work |
| **ACP** | ❌ **abrdn Income Credit Strategies is a CLOSED-END FUND, not an operating small cap.** Mandate-excluded. Killed on reading the company name |
| **SOC · FLNC · TRAX · ANRO · TSSI · CVRX · DUOT** | **SOC closed −7.66% on 9/16 at 13% of range** (and median range 7.24% ≥ the whole trail). **FLNC −2.69%, no positive catalyst.** TRAX +1.38% at **19% of range** = noise (rule 1). **ANRO** closed at **10% of range**, still fading — standing tape kill. **TSSI +2.33%, CVRX $3.12** (rule 10 trap zone + standing rule-5 fader), **DUOT +2.22% on 1.01×** — all noise, all previously killed |
| **GLOO** | ❌ `eligibility` ADV **273,478 — FAILS** the 300k gate. Already liquidity-locked. Killed in one call, no research |
| **BNC · USDE · BRR** | Crypto/treasury proxies — **standing mandate kill (31). Mandate checked before the chart** |
| 9/16 AMC + 9/17 BMO slate | **38 reporters screened, ZERO survivors.** LEN/LEN.B $19.3B · SA $3.16B · HUBG $2.05B (all over cap) · ANAB/HTT/NBP previously killed · **LUXE** (Netherlands) · **RYDE** (Singapore) · **SANG** (Canada) · **VFS** (Vietnam) · **IPHA** (France) · **DAVA · YRD · IH · AACG · DSWL · YI · SJ · GAUZ · CLGN · GURE** (non-US) · **UPXI** (crypto treasury, 31) · ATCH/PTN/LKSP/EONR/CMMB/ALAR/SMXT/BTTC/ITP/IPST/SNYR below the floor · **RZLT** and **ALMU** killed above |

📌 **Lesson 41d honest tally: the earnings calendar sourced ZERO survivors — now 3-for-6.**
Recorded as a real result, not an empty board (41b): **38 reporters were screened and every
one died on a named gate.**

---

### Scheduled catalysts

- ✅ **FOMC delivered 9/16: 25bp HIKE, as priced.** Rule 29's board-wide block is **lifted.**
  The event risk that closed the last three sessions is gone — **and the board still produced
  nothing**, which is the whole point of the finding above.
- ❌ **KMTS — CLOSED on rule 4** (9/16 closed at 15% of range on 2.6× volume). Gates B/E
  passed on the same session. New dated catalyst only; gate-G ruling still owed.
- **HAWK joins the Russell 2000 effective 9/21** — Rocket's IWM core picks it up automatically.
  No action required, and that is the reason not to buy it directly.
- **RCKT program update 10/06** · **CLB earnings 10/28** · **NB 9/28** (resolve BC-domicile
  first — same question as GLAS) · **DTIL 11/02** (ADV-locked) · **KMTS 12/14**.
- 🚨 **`weekly_review` W36 (due 9/04) AND W37 (due 9/11) BOTH still unrun — EIGHTH session
  flagging W36 — and W38 falls due TOMORROW, 9/18, which would make THREE owed.**
  `memory/weekly_reviews/` ends at **2026-W35**; the hand-built Rocket-vs-SPY chain is
  **fourteen sessions stale** (last good 8/28 W35, −2.51%). Lesson 47c.

### 🚨 Open escalations awaiting a user decision — FOUR

1. **Which rebalance basis governs** (lesson 44) — **THIRTEENTH+ consecutive session.**
   Slice **$3,128.32** vs book **$2,992.32** = **$136.00**, ⚠️ **widened for a second straight
   session** (was $133.91, then $130.87). ✅ Cause re-confirmed as 44b: **Bull's** JPM/SPY marks
   rise while Rocket's IWM falls, and every dollar Bull makes mechanically raises Rocket's core
   target. No action here (rule 6: `market_close` only).
2. ⚠️ **Satellite stop width — THE ARGUMENT WEAKENED TODAY, ON ROCKET'S OWN EVIDENCE.**
   Yesterday this was escalated as *"MDD-from-HWM would have let Rocket hold KMTS to +15.49%."*
   **The identical measurement on the next bar shows the trail surviving at 5.80% MDD while the
   trade lost 4.44%.** The honest ask is therefore narrower than yesterday's: **may Rocket
   replace `range ÷ trail` with `max drawdown from the running high` as the stop-fit statistic —
   on ACCURACY grounds, not profit grounds?** It is free, exact, and is what the broker computes.
   **It is not an edge and must not be sold as one.** **NOT self-approved** (42/51d).
3. **The ADV gate binds on account size, not tradeability** (46f) — KMTS's marginal median is
   the same bind from the other side.
4. **Does "US-domiciled" mean INCORPORATION or OPERATIONS?** **Still unresolved, and it hit a
   THIRD name today: GLAS is British Columbia-incorporated** (KMTS Bermuda/Kirkland WA, ADNT
   Ireland/Plymouth MI, NB British Columbia). Per rule 38 an unresolved mandate question is a
   **FAIL**, so all four are blocked meanwhile — **but logged as awaiting a ruling, not as
   killed** (52b), or the escalation disappears into the kill table and never gets decided.

### Re-open conditions for killed names (everything else needs a new dated catalyst)

| Name | What would have to change |
|---|---|
| ❌ **KMTS** | **CLOSED on rule 4** (42d/45e). Gates A/B/C/E banked and irrelevant while the entry bar is a distribution bar. **A new dated catalyst only** — plus the gate-G ruling |
| **HAWK** | ⚠️ **Price ≤ $16.33** (rule 13 two-rung ceiling) **AND** a catalyst with committed dollars — an MoU converting to a signed contract with a stated value. The index add is not re-openable; it is beta Rocket already owns |
| **OSS** | A contract **material to a $224M company** (the $400k award is 0.18%) **and** the 8/24 shelf's size and drawn/undrawn status resolved |
| **UNCY** | ⚠️ **Effectively never at this structure** — a $150M ATM against a $131M cap, post-CRL, with live securities litigation |
| **GLAS** | A dated primary-source catalyst **and** the escalation-4 BC-domicile ruling |
| **XTND** | ⚠️ **Un-measurable, not killed** — needs ~60+ bars of post-listing history (46j) **and** the 11.7× market-cap disagreement resolved to a single number |
| **RCKT** | A **delivered** readout, not a resumption — and a close in the upper half of range. 10/06 update |
| **DTIL** | Sustained **median** volume >300k on non-catalyst bars, or a user decision on the ADV gate |
| ❌ **ELMT** | **CLOSED — gate A failed** (42d/45e), and vindicated by the corrected MDD test (15.66%). New dated catalyst only |
| **FTK** | ⚠️ Not re-openable while the class action and PREPA termination are live |
| **SOC · EAF · INDP** | Median range at/above the whole trail — ⚠️ **re-test with MDD-from-HWM before re-killing on that basis** |
| **PLAY** | Not re-openable on this print (negative reaction). Keep on the earnings calendar |
| **CRBP** | A **dated primary-source** CRB-913 Ph1b topline **and** a close in the upper half of range |
| **ACVA** | ⚠️ **Never.** $10.50 cash tender caps upside below rung 1 |
| **NB** | Earnings **9/28** — re-screen then, **and resolve the BC-incorporation question** (escalation 4, same as GLAS) |
| **CAPR** | PDUFA **EXTENDED Aug 22 → Nov 22** — a delay repriced as optionality (37c) |
| **CLB** | A name-specific dated catalyst (earnings 10/28) **and** a dated target above the +15% rung |
| **DBI · STIM · LPTH · REF · FEIM · WLTH · SHOE · CMRC · TSSI · IRD · CAL · AVO · NX · SWBI · CHPT · INSG · PHR · ARCT · HLF · SG · TROX · AMRC · WTI · ENOV · UPB** | Named gates unchanged from W37/W38; reasons in `archive/research_log_history.md` |
| ⚠️ **Liquidity-locked** — FLWS · RFIL · CODA · INNV · OCC · BBCP · TLYS · JILL · PPIH · CSHR · LSAK · **GLOO** · LMNR · LAKE · KEQU · SKIL · MCFT · VNCE · LOVE · QUIK · NMAD · IBEX · ZUMZ · AENT · CSBR · HOFT · RENT · PLCE · VRA · RLGT · ESP · **DTIL** | **Not re-openable on a catalyst** — only sustained **median** volume above 300k, or a user decision on the ADV gate |
| **Standing mandate kills** — BNC · CSHR · USDE · DFDV · ABTC · HYPD · HYMC · QMLS · GOLD.com · BRR · **UPXI** (crypto/treasury, lesson 31) · **ACP** (closed-end fund) · **ADNT** · **GLAS** · **NB** (⚠️ all three see escalation 4) · FTFT · LPA · TEN · YB · IMPP · **DAVA** · **YRD** · **VFS** · **IPHA** · **IH** · SA · ODD · CGNT · NNOX · COE · AACG · NVA · CMCM · HTLM · MNY · CURR · GRFS · CBAT · HITI · BIOX · ZENA · LUXE · SANG · RYDE · DSWL · SJ · YI · GURE · ISPR · GAUZ · CLGN | Category-excluded. Not re-researched |
| **Hard-gate kills** — CATX · AIV · HAIN · CHRN · FRGT · AREC · EPM · TCOM · FPS · ELME · ANAB · UROY · M · FIZZ · AEO · **HUBG** · SIG · ASO · CULP · HTT · NBP · ANIX · ALPS · KR · ZONE · CVRX · TRT | Cap / price / volume / exchange. New instrument only |
| **Tape kills** — GIII · DAKT · NEOV · YEXT · PD · RMNI · MEI · CBIO · TYRA · PYXS · RARE · GOLD · LTRX · OOMA · FRNM · SSTK · BBW · OSG · XHLD · NABL · LENZ · ALMS · EOSE · OABI · DUOT · AGPU · SVCO · ANRO · AVEX · BETR · **ALMU** · **RZLT** · **FLNC** · **TRAX** | New dated catalyst only |
