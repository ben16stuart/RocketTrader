# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines — archive resolved/stale
entries to `memory/archive/research_log_history.md`.

---

## Watchlist — Wed 2026-09-23 (Week 39 day 4 — **satellite floor breached 4 consecutive `market_close` sessions (9/17, 9/21, 9/22, 9/23 at 14.9%); MEDIUM bar active per rule 8**)  ← CURRENT

**Satellites 0/4.** Full board run: `top_movers` + `unusual_volume` screeners, universe
eligibility gate on every mover of note, then catalyst validation by web search on survivors.

**Screener board**: only **GRML** appeared in both `top_movers` (+43.2%) and `unusual_volume`
(17.7×) — the "first priority tier" per the routine. **Standing kill, reconfirmed**: pulled
EDGAR `CIK0001907223` fresh this session — `stateOfIncorporation` is **still blank**,
`sicDescription` still reads "Biological Products" (the record has not caught up to the
March rebrand). Lesson 60 stands. The stock is now **further extended** on top of the prior
+474%/4-session run. No re-open condition met.

Universe-gate + catalyst check on the rest of the movers:

| Name | Verdict |
|---|---|
| **TPB** (+15.7% printed) | ❌ **Rule 1 — no fresh dated catalyst, and price data is internally inconsistent across sources** (scanner $69.74, yfinance eligibility $60.28, a cited "last close" of $108 from a stale secondary page). The only concrete items found — a Q2 EPS miss, a Sept 18 $0.08 dividend ex-date, prior analyst PT raises — are all weeks old and already priced in. Not enterable without a corroborated same-day source for the move itself. |
| **AGPU** | ❌ **Rule 1 — catalyst is stale.** Real news exists (Blackwell B300 $1.5B contract, $317M prepayments) but it is all **June/July**, already fully digested; today's +6.5% carries only 0.7× RelVol (not actually unusual volume). No fresh news found. |
| **ONT** | ❌ **Rule 1 — catalyst too old/too small.** A C$9M contract award is dated 9/14 (9 days stale) and immaterial against an $840–900M FY revenue guide (<0.5%); the larger item (board-led strategic review) is dated 8/05, six weeks stale. Neither explains today's move. |
| **HSDT / VUZI** | ❌ **Universe FAIL** — HSDT avg volume 296,911 (min 300,000); VUZI price $2.96 (min $3.00). |
| ZSTK, BYRN, TNXP | ❌ Weak, unremarkable moves (≤3.5%, RelVol ≤0.1×) with no catalyst surfaced — rule 1 default fail, not worth further search spend. |

**Midday update (9/23):** Position held. News check surfaced a Pomerantz law-firm
"investor alert" (9/22–9/23) — resolves to a 3-week-stale Phase 3 Aspire trial miss
for an unrelated drug (apazunersen), already priced into the base; not a new catalyst
event, no cut (lesson 62). Afternoon `unusual_volume` scan checked NNBR (extended,
soft guide language) and CBRL (guide below consensus, rule 5c kill) — both killed, no
new satellite entries.

**Market_close update (9/23):** Held overnight — $14.895, -1.23% from entry, clear of
the $14.00 stop; multi-day FDA catalyst qualifies for the CLAUDE.md hold-overnight
exception. Satellite floor still 14.9% < 50% (4th consecutive `market_close` breach,
lesson 63) — 3 more satellite slots need filling; that's tomorrow's premarket job.

### 🎯 RARE — Ultragenyx Pharmaceutical: the one name that clears the catalyst bar

- **Catalyst**: **First-ever FDA full approval of Fayuvi (UX111)** gene therapy for pediatric
  Sanfilippo syndrome Type A, announced **2026-09-17** (primary source: FDA/company
  announcement; stock gapped from $12.88 close 9/16 to $14.50 close 9/17, +12.6% on 12.4M
  shares vs ~4–5M normal). Same day, **Citigroup raised PT to $32 (from $31, Buy)** and
  **Morgan Stanley raised PT to $20 (from $18, Equal-Weight)** — both dated 9/18.
- **Universe**: price $15.62 ✅ · market cap $1,539M ✅ · avg volume 3.72M ✅ · **domicile DE**
  (confirmed via EDGAR submissions JSON) ✅ — clears every gate.
- **Price action since the catalyst**: based tightly for 3 sessions (9/18 close $14.51, 9/21
  close $14.65 — a ~1% range) and is **now breaking out to $15.62**, a fresh high since the
  approval. This is a *breakout-from-a-short-base* shape layered on top of the FDA catalyst,
  not a textbook fit for any single named entry rule (initial gap was only 12.6%, below the
  20–35% gap-and-go band and well below the >35%/>25% continuation thresholds) — flagged
  explicitly rather than force-fit into a rule that doesn't quite apply.
- **Short interest**: ~16.8–18% of float (dated data, 8/31–9/08) — **>15% + a live catalyst**
  qualifies as a squeeze flag, though float itself (80.4M sh, 82% of shares out) is not low.
- **Priced in?** No — both dated analyst targets ($20 / $32) sit well above the current
  $15.62; MS's more conservative target still implies +28%.
- **Dilution**: checked EDGAR (CIK 0001515673) — **no S-3/424B filing in over 2 years**
  (last 424B5 2024-06-14, last S-3ASR 2024-02-21). Clean.
- **Entry plan**: only on confirmation at `market_open` that volume is genuinely elevated
  (not a premarket-quote artifact, lesson 59) — entry zone **$15.10–$15.80** on a hold above
  the 9/18–9/21 base ($14.51–$14.65). Do **not** chase if it gaps materially above this zone.
- **Stop**: 7% trail from entry (~$14.51 at a $15.60 entry — coincides with the base support).
- **Targets**: +15% ≈ $17.94 (1st third) · +25% ≈ $19.50 (2nd third) · ride final third to stop.
- **Conviction**: **MEDIUM** (rule 8 bar). Catalyst quality is genuinely strong — the entry
  timing is what keeps this off HIGH, since it doesn't cleanly match a pre-defined pattern.
- **Risk / what kills it**: (1) the move is 5 sessions old — if it fails to hold the
  $14.51–$14.65 base at the open, the setup is exhausted, not fresh; (2) float is not low, so
  squeeze upside is capped despite the short-interest %; (3) confirm real volume behind any
  breakout print before treating it as valid (lesson 59's premarket-quote trap).

**Macro context** (`market_data.py macro`): VIX 14.16 (**−4.77%**, new multi-week low, well
below the 22 brake) · Russell futures **−0.28%** (mildly negative, small caps the weak leg
today) · SPY fut +0.05% · 10-yr 4.96% (still through the 4.75% trigger, unchanged read) ·
crude both legs down on the roll-adjusted read. **No macro block on entries.**

**Verdict: NO ENTRY PRE-MARKET (market closed) — RARE queued as the sole `market_open`
candidate, MEDIUM conviction, entry conditional on volume confirmation.** If RARE also fails
at the open, this would be the **4th consecutive satellite-floor breach at today's
`market_close`**, still a stock-picking gap per lesson 61, not a market call.

**✅ EXECUTED at `market_open` (2026-09-23, 9:45 AM ET).** Volume confirmed genuine at the
9:45 checkpoint (278k shares, ~1.07x expected pace by that point in the session — real
regular-hours trades, not a premarket quote artifact per lesson 59), price $15.06 holding
cleanly above the $14.51–$14.65 base and printing a fresh weekly high. Bought 31 sh @ $15.08
avg, 7% trailing stop live at $14.00. See `trade_log.md` for full entry. Satellite floor
moves from 0.0% to 14.9% of slice — floor still breached (one satellite at the 15% cap
cannot close it alone) but the research gap is no longer a complete zero.

---

### Open escalations awaiting a user decision — TWO (unchanged)

1. **Which rebalance basis governs** (lesson 44) — slice vs. book. Non-binding while IWM sits
   at/near the 50% cap (the cap governs regardless of basis).
2. **The ADV gate binds on account size, not tradeability** (46f). Non-binding on RARE — at
   3.72M avg volume a satellite this size is trivially fillable.

### Scheduled catalysts

- **RARE** — Fayuvi approval live, see above · **RCKT program update 10/06** ·
  **CLB earnings 10/28** · **DTIL 11/02** (ADV-locked).
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
