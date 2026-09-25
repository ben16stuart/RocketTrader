# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Fri 2026-09-25 (Week 39 day 6 — **satellite floor breached 5 confirmed `market_close` sessions (9/17, 9/21, 9/22, 9/23, 9/25); MEDIUM bar active per rule 8; PRME CLOSED at `market_close` on Gate A**)  ← CURRENT

**Satellites 1/4 (RARE only), 14.7% of slice vs a 50% floor.** Breach count is **4 actual
`market_close` sessions, not 5** — **no `market_close` ran on 2026-09-24** (`trade_log.md` and
`session_notes.md` both end 9/24 at MIDDAY; only premarket/market_open/midday have entries).
Per lesson 58, an absent session is not a session that ran and found nothing, so it is not
counted. The breach was continuously true across the gap regardless (no trades 9/24), so the
MEDIUM bar stays active. RARE settled 9/24 at **$14.77**, clear of the $14.00 stop.

**Sourcing order run this session (earnings calendar FIRST per lesson 41b, then screeners,
then FDA/analyst channels — all four screeners run per rule 8):**

### 1. PRME — FDA clears the PM647 IND (Alpha-1 Antitrypsin Deficiency), 2026-09-24

- **Catalyst**: FDA clearance of the Investigational New Drug application for **PM647**, an
  in vivo Prime Editor for AATD, announced **2026-09-24** (company PR + GlobeNewswire,
  primary-sourced and dated). Enables first-in-human dosing in the US; **initial clinical
  data guided to 2027.** Stock traded **+13.0% after hours to ~$3.47** off a **$3.07**
  settled close. On Rocket's approved list as an FDA/regulatory win.
- **Market cap**: $557M | **Float**: 112.2M sh (62% of 181.4M) | **Short float**: **22.65%**
  (short ratio **11.74 days to cover**) → squeeze-candidate flag per rule 9/10
- **Universe gates** (`eligibility`, all PASS): price $3.07 · cap $557M · NASDAQ · earnings
  **11/06 (+42d)**, clean calendar (rule 29). **Domicile verified at the primary source:
  EDGAR `stateOfIncorporation` = `DE`** (rule 52a/52c), CIK 0001894562.
- **ADV, on the MEDIAN per rule 46** — 63-day mean 3,281,405 / **median 3,075,700**, 2-yr
  median 2,313,500, last five sessions **3.25M · 4.67M · 2.95M · 3.33M · 4.19M**. Passes by
  ~10×, **no mean/median contamination and no sub-gate recent sessions** — the cleanest ADV
  profile screened in weeks. 46e/46g spread check not required at this margin.
- **Dilution (rule 8, run first)**: EDGAR shows **zero offering filings in all of 2026** — no
  S-3, S-3ASR, S-1, 424B5 or FWP. The only capital-markets form is an **S-8 (2026-03-03),
  which is not an offering** (8b). ⚠️ **But grade the runway, not just the absence of a
  takedown**: cash/investments **$108.8M at 6/30/2026 with runway only "into 2027"** on a
  pre-revenue gene-editing burner. **A clean EDGAR here means the shelf is UNDRAWN and
  available, and an IND-clearance pop is the textbook window to price one** — this is rule 8e
  in its forward-looking form, and it is the single largest risk on the name.
- **Analyst ladder (rule 11)**: entry ~$3.47 → **+15% rung $3.99, +25% rung $4.34.** Street
  mean **$7.02** (13 analysts, S&P Global) / median **$6.00** (16 analysts), low **$4.25**,
  high **$11.00**. **Both rungs clear even the LOWEST target** and the mean sits ~1.6× above
  the second rung — the inverse of the OOMA/PD kill shape (42b). ⚠️ **The consensus is
  UNDATED in the sources pulled, so per 11a it is flagged, not booked** — margin is wide
  enough that a stale mark still clears, but re-verify against a dated post-9/24 mark before
  entering.
- **Stop fit, measured with the APPROVED statistic (54c — max drawdown from the running high,
  NOT range ÷ trail)**, on PRME's own 4,674 five-minute regular-hours bars, 7/01–9/24:
  | | value | vs 7% trail |
  |---|---|---|
  | Median MDD, all 60 sessions | **5.27%** | 0.75× — **fits** |
  | 7% trail survives | **77% of sessions** | — |
  | Median MDD, its 8 widest sessions | **11.52%** | **1.65× — blown** |
  | Worst (2026-07-10) | **15.12%** | 2.16× |
  🚨 **And read the SHAPE, which is the part that decides this**: of those 8 widest sessions,
  **five closed in the bottom quartile of their own range** (24.0% · 14.3% · 10.8% · 1.2% ·
  7.4%) and only two closed strong. **A wide day in PRME is historically a distribution day,
  not the one-way trend bar that made KMTS safe under lesson 51.** Six of the eight blow
  through a 7% trail. So the name fits the trail on a normal session and does not fit it on a
  catalyst session — **which is exactly rule 45c's "not today, not not-ever."**
- **Entry plan**: **NO ENTRY TODAY. Day-2 entry Mon 2026-09-28**, per rule 2 (🥇 same-day
  0-for-3, second-day 2-for-3) and the MDD table above. The +13% AH gap is below rule 2c's
  20–35% gap-and-go band, so 2c does not authorise a same-day chase either.
- **Pre-committed gates, written as SHAPES not levels (rule 42c), struck now at $3.07
  settled / ~$3.47 after hours, and to be honoured verbatim regardless of where price is
  Monday:**
  - **Gate A — price action.** PRME's **9/25 session must close in the upper half of its own
    daily range.** Below the midpoint = **KILL, closed not deferred** (42d/45e) — and given
    five of eight wide days closed in the bottom quartile, this gate is genuinely load-bearing
    rather than a formality.
  - **Gate B — dilution.** Any **424B5 / S-3 / S-1 / FWP filed between now and Monday's open**
    = **KILL** (rule 8). Re-pull `data.sec.gov/submissions/CIK0001894562.json` at Monday
    premarket; the undrawn shelf plus an 18-month runway is the live hazard.
  - **Gate C — falsifiable forecast, to be graded (rule 45 discipline).** Catalyst multiple
    **3.00×** on a 6.40% median range → **predicted 9/25 range 19.2%**; **predicted 9/25 MDD
    from the running high ≈ 11.5% (1.65× the trail).** Grade both against the settled bar and
    5-min series at `market_close`, magnitude separately from verdict (45h).
  - **Gate D — ladder.** Re-verify a **dated** post-9/24 consensus before sizing; if the
    dated high target lands below the **$3.99** +15% rung, kill on rule 11/42b.
- **Conviction: MEDIUM** (rule 8's relaxed bar, active since the 9/21 breach). It is MEDIUM
  and not HIGH because **an IND clearance is the lowest rung of FDA news** — permission to
  begin a Phase 1, zero revenue, zero efficacy data, first readout 2027. That is optionality
  granted rather than a result delivered, adjacent to rule 37c's warning; it is a real, dated,
  primary-sourced catalyst, which is why it is on the board at all, but it is not a rung-1
  beat-and-raise.
- **Risk / what kills it**: (1) **the raise** — $108.8M and runway "into 2027" against an
  undrawn shelf, with a pop to sell into; (2) **$3.07 sits only 2.3% above the $3.00 universe
  floor**, inside rule 10's 5% watch band, and a 7% trail off a $3.07 entry lands at $2.86,
  *below* the floor Rocket refuses to buy at; (3) **112.2M float is not low float**, so 22.65%
  short interest is a large absolute short base with no scarcity to squeeze; (4) PRME's own
  wide-day fade pattern (Gate A exists for this); (5) an IND clearance is un-monetisable for
  years — nothing here changes the cash burn.

**🚨 `market_close` Gate grading — PRME CLOSED, not deferred (Gate A failed).** 9/25 5-min
bars (IEX feed): session **opened at the high, $3.42**, traded down all day to a **low of
$2.875**, settled **$2.905**. Range midpoint = **$3.1475**; the close sat at **5.5% of the
day's range from the low** — nowhere near the upper half Gate A required. Per the
pre-committed rule (42d, "below the midpoint = KILL, closed not deferred"), **the Monday 9/28
day-2 entry is off.** Gate B checked anyway for the record: `data.sec.gov/submissions/
CIK0001894562.json` shows **no filings of any kind since before 9/20** — dilution stayed
clean, moot given Gate A. Gate C graded for calibration: predicted 9/25 range 19.2% vs
actual **17.75%** (close, slightly overestimated); predicted MDD-from-high ≈11.5% (1.65× the
trail) vs **actual 15.94% (2.28× the trail)** — worse than predicted, essentially matching the
premarket stop-fit table's historical worst case (15.12%, 2026-07-10). **This is exactly the
"wide day = distribution, not trend" shape the premarket MDD analysis flagged** (five of
PRME's eight widest historical sessions closed in the bottom quartile) — the gate worked as
designed and the underlying stop-fit read was directionally right, if a touch optimistic on
magnitude. See lesson 68.

### 2. Everything else on the board, and why it died

**Earnings calendar (24 reporters 9/24 AMC, 10 for 9/25) — one in-universe name, and it was
a MISS:**
- 🚨 **SCHL (Scholastic) — KILLED at the primary source, and the calendar row lied.** The
  Nasdaq calendar printed `eps $(2.52) vs $(3.42)`, whose *shape* reads as a beat. The
  issuer's own 8-K exhibit says: **GAAP loss $(3.77) vs $(2.83) a year ago — WIDENED;
  adjusted loss $(3.63); revenue $216.8M, DOWN 4% YoY** and below consensus; FY27 outlook
  merely **"affirmed"** at 2–4% revenue growth / $135–145M adj EBITDA — **a reaffirmation is
  a 0% change, not a raise (rule 5f)**. Stock **−12.57% after hours to $30.45.** Neither
  calendar figure matches any number in the release on either basis. See new lesson 65.
- Out of universe: **TBN** (ADV 136,707 FAIL), **LGCY** (43,176 FAIL), **HTLM** ($1.78 FAIL),
  **ZONE** ($0.13 FAIL), **HUBG** ($1.92B — rule 13: ×1.25 = $2.40B, fails the cap at the
  +25% rung), **DAVA** (UK plc, domicile), SNX/BB/DRI/COST (cap), VFS/UXIN/YRD/IH (foreign),
  RAVE and below (sub-$50M cap).

**Screeners — overlap tier (`top_movers` ∩ `unusual_volume`) was GLND, GRML, TRT, TE, HSDT:**
- **GLND** +15.0% / 17.9× — **third independent kill.** Same three grounds market_open and
  midday used on 9/24 (geopolitical basket headline not a company catalyst; the only dated
  company news is a farm-out *deadline extension*; pump shape, float 0.0M, −83% off a $23
  high). No new fact today, just more extension.
- **GRML** +10.9% / 3.1× — **standing kill, lesson 60**: blank EDGAR `stateOfIncorporation`
  on a shell renamed three times in four years, and already +474% over four sessions.
- **TRT** +2.9% — **at the LOW of its own week range ($7.26 vs $11.45 high), −28.0% on the
  month, below MA50**, and its 9/24 print was a **$(0.02) loss.** A catalyst with a collapsing
  tape is not a trade.
- **TE** (T1 Energy, $1.16B, 26.5% short float) and **HSDT** — HSDT is **"Solana Co"**, a
  crypto-treasury mandate kill (lesson 31); TE has no dated catalyst, 0.2× real volume.
- **PACK** +9.2% and **AMPG** +5.6% — both in universe on every gate (PACK $362M / ADV 508k;
  AMPG $103M / ADV 2.15M) and **both killed on rule 1: no verifiable catalyst found.** Both
  also sit **below MA50** (PACK −16.1% on the month). Rule 1's "unusual volume without a
  verifiable catalyst = likely manipulation, AVOID" applies directly.
- **AESI** (Atlas Energy Solutions, $1,373M, +9.3%, 26.8% short float) — in universe, DE, and
  **killed on catalyst type.** The 9/24 8-K (**Item 1.01**, the credible route per 57a) is a
  **$613.5M equipment PURCHASE commitment** — $340.5M balance-of-plant + $273M generators,
  payments running Sept 2026 → Jan 2028. **That is cash OUT equal to 44.7% of market cap, not
  a contract win**, on a company that suspended its common dividend in Q3 2025. Rule 7a run
  in reverse: **the announcement IS the funding need.** Not on the approved catalyst list.
- **MASS** (908 Devices) — in universe but **median ADV 307,800 against a 300,000 gate = a
  2.6% pass, a coin flip reported as a verdict** (46i), and **no catalyst** at +3.5% on 0.0×.
- `breakouts`: Finviz returned an error on one query (logged, not scored) and the rest was
  immaterial — **SRZN** (+6.2%, but **ADV 219,296 FAIL**), MASS, PUBM +1.5%, **BLFS $1.90B**
  (rule 13 fail), CYPH (crypto kill), AGEN −2.1%.
- `short_squeeze`: **same perpetually-shorted names as 9/24 with no fresh volume and no dated
  catalyst** — WOLF 74.9%, WYFI 50.5%, LENZ 39.1%, JACK 36.7%, XRX 36.2%, VELO 36.0% — every
  row at 0.0–0.2× RelVol and ±1%. High short float without a catalyst is not a setup (rule 9).

**FDA / analyst-initiation channels (lesson 41 sourcing, run because rule 8 demands the
widened board):** the FDA channel produced **PRME** (above). The analyst-initiation channel
produced **six** dated 9/24 Buy initiations and **all six fail the universe**: PGEN ($2.76B
cap), BFLY ($2.51B), USAR ($5.77B), TTRX (ADV 117k), QNCX ($31M cap + 30k ADV), ENTX ($2.80
price, and an Israeli Ltd). **6 requested → 6 rows returned; count verified per lesson 43b.**

**Which constraint actually bound today — re-measured, not assumed (lesson 53a).** It was
**catalyst and universe quality (lesson 36), not stop width.** PRME's normal-day MDD is
5.27% = **0.75× the trail**, and AESI/PACK/MASS all sit under it too on median range — the
stop fits these names. They died on domicile-free grounds: a miss, a capex commitment, two
unexplained moves, three cap failures, four ADV failures. 53b's discipline applies: this is
the inconvenient answer for Rocket's own standing stop-width escalation, and it is recorded
anyway.

**Verdict: no entry this session (market closed — premarket is analysis only). ONE name
carried forward: PRME, MEDIUM, day-2 Monday 9/28, contingent on Gates A–D.** Satellite floor
breached 4 confirmed `market_close` sessions and searched at the MEDIUM-conviction bar per
rule 8 — all four screeners plus the earnings calendar, FDA and analyst-initiation channels.

**`market_open` re-check (live tape)**: PRME trading +0.7% at $3.09 at the open — AH pop
faded, plan stays Monday-only, nothing to grade until Gates A–D at `market_close`. Overlap
tier live = AESI only (standing kill). One fresh name not on the premarket board, **WNC**
(+10.5%, 1.4x), killed on rule 1 — no dated catalyst, last earnings a miss, next report 10/29.
🚨 **Note honestly that PRME alone cannot close the floor**: one satellite at the 15% position
cap takes satellites from 14.7% to ~29.5%, still short of 50%. **Three more qualifying names
are needed**, and the board has not produced three in nine sessions. IWM core sits at its 50%
cap; no cash-thesis exception applies because no bearish view is being made.

---

### Open escalations awaiting a user decision — TWO (unchanged)

1. **Which rebalance basis governs** (lesson 44) — slice vs. book. Non-binding while IWM sits
   at/near the 50% cap (the cap governs regardless of basis).
2. **The ADV gate binds on account size, not tradeability** (46f). Non-binding on RARE — at
   3.72M avg volume a satellite this size is trivially fillable.

### Scheduled catalysts

- **RARE** — Fayuvi approval live, stop $14.0616 (HWM $15.12, trail 7%; `market_close` 9/25:
  −1.79% today / −3.81% from entry, price $14.505 still 3.1% clear of the stop, no negative
  news [Barclays PT $35, Evercore $18, both well above spot], held per lesson 67 precedent) ·
  **PRME CLOSED** (Gate A kill, 9/25 — see lesson 68, no Monday entry) · **RCKT program update
  10/06** · **CLB earnings 10/28** · **DTIL 11/02** (ADV-locked).
- **SECZ** — re-open only if it pulls back materially below the $2B cap AND the lock-up
  primary source (Proxy "Other Transaction Agreements — Lock-Up Agreements," p.123) is
  actually read, not summarized secondhand.
- 🚨 **`weekly_review` W36 (9/04), W37 (9/11), W38 (9/18) — THREE owed, and W39 falls due
  TODAY (Fri 9/25) making FOUR**, chain 20+ sessions stale (last good 8/28 W35). Escalated
  every session; not remediated (lesson 47c) / [[launchd-quota-contention]].

### Standing category kills (unchanged — full detail in archive)

Crypto/treasury mandate (lesson 31): BNC, DFDV, USDE, HYPD, ABTC, GEMI, QMLS, CYPH, FWDI,
BKKT, UPXI, **HSDT ("Solana Co")**. Non-US-incorporated (lesson 52c): KMTS, GLAS, NB, ADNT,
**DAVA**. Liquidity-locked: GLOO, TLYS, REF, OPTX (ADV 258k), **SRZN (219k)**, **TTRX (117k)**.
Pump/shell shape: **GLND** (3× killed), **GRML** (lesson 60). PAAI CLOSED (catalyst falsified
at the primary source, 9/18). PRTH CLOSED (rule 27, pinned deal price). NUAI CLOSED
(lender-mandated $100M ATM). **SCHL CLOSED** (miss + widened loss + affirmed-only guide, 9/24).
**PRME CLOSED** (Gate A price-action kill, closed bottom-5.5%-of-range on 9/25, lesson 68).
