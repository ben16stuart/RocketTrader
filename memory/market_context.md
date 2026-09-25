# Rocket Market Context — Macro & Small Cap Sentiment

Current snapshot only. Prior dated snapshots: `memory/archive/market_context_history.md`.

---

## Snapshot — 2026-09-25 Friday premarket (Week 39 day 6 — **floor breached 4 confirmed `market_close` sessions; MEDIUM bar active**)  ← CURRENT

All "last close" figures are **Thursday 2026-09-24's settled closes** except where marked
LIVE (a forming bar — never record a LIVE figure as a settled close, per the tool's warning).

| Metric | Level | Read |
|---|---|---|
| **VIX** | **15.38 LIVE** (**−1.85%** vs 15.67 close 9/24) | ✅ **The 9/24 uptick faded** — back toward the multi-week low, far below the 22 brake. No size restriction, no entry block |
| **10-yr** | **5.16% close 9/24** (vs 5.11% close 9/23, **+0.94%**) | ⚠️ Still above the 4.75% trigger — a **level** flag standing for weeks, not a new event (rule 34: flags near a threshold stand down on a trend, never on one print). The 9/22 skipped-bar artifact flagged yesterday has cleared; this is a clean one-session read |
| **FUTURES** | **ES +0.24% · NQ +0.47% · RTY +0.20%** | ✅ **All three legs green, modestly** — reverses 9/24's broad red. Russell, the benchmark-adjacent leg, is positive but the weakest of the three. Lesson 28: one session carries no information, flagged not booked |
| **Brent / WTI** | **98.85** / **92.93** LIVE, **−1.37% / −1.78%** | Both legs down. 🔄 **Brent ROLLED to BZZ26.NYM** — the tool caught it and re-read both legs off the named contract (**naive −7.27% → true −1.37%**). Lesson 50 working as designed |
| **SPY / IWM** | **767.18** / **281.66** — Thursday's settled closes | Both fractionally down (−0.08% / −0.09%) — a flat session, not a move |
| Gold / Dollar | 4,335.80 (+0.88% live) / 101.04 (−0.25% live) | Nothing outside recent range |

### The tape is benign; the binding constraint is still catalyst supply, and today it finally produced one name

**Rule 29 blocks nothing** — VIX 15.38 is nowhere near the 22/25/30 brakes, and futures are
modestly green across all three legs with Russell participating. There is no macro reason to
stand down and no macro reason to size up either.

Today's widened board (earnings calendar first per 41b, then all four screeners, then the FDA
and analyst-initiation channels per rule 8) produced **one** name that survives every universe
gate with a dated, primary-sourced catalyst: **PRME** — FDA clearance of the PM647 IND for
Alpha-1 Antitrypsin Deficiency, 9/24, +13% after hours. It is **MEDIUM conviction and a day-2
(Mon 9/28) candidate only**, behind four pre-committed gates. Full workup — including the
approved max-drawdown-from-running-high stop-fit table, the DE domicile check at EDGAR, and
the undrawn-shelf/18-month-runway hazard — is in `research_log.md`.

🚨 **Which constraint bound today, re-measured rather than assumed (lesson 53a): board and
universe quality, NOT stop width.** PRME's normal-day median MDD is **5.27% = 0.75× the 7%
trail**; AESI, PACK and MASS also fit inside it. Nothing on this board died because the stop
was too tight — they died on a widened loss and an affirmed-only guide (SCHL), a $613.5M
capex *commitment* mislabelled as a contract win (AESI), two unexplained moves with no
verifiable catalyst (PACK, AMPG), three market-cap failures and four ADV failures. **This is
the inconvenient answer for Rocket's own standing stop-width escalation and it is recorded
anyway, per 53b.**

### Instrument health

🚨 **NEW — the Nasdaq earnings-calendar `eps`/`epsForecast` fields fabricated a beat.** The
SCHL row printed `$(2.52) vs $(3.42)` — the shape of a beat — on the day's only in-universe
reporter. The issuer's 8-K exhibit says GAAP loss **widened** to $(3.77) from $(2.83),
adjusted loss $(3.63), revenue **−4% YoY** and below consensus, guidance merely **affirmed**,
stock **−12.57% AH**. Neither calendar figure matches any number in the release on either
basis. **New lesson 65** — the calendar is a name source, never a beat/miss verdict.

🚨 **NEW — the lesson-59 premarket liquidity check is unavailable.** Alpaca `sip` bars return
**403 "subscription does not permit querying recent SIP data"** for every symbol including the
SPY/IWM control; `iex` snapshots still work. **The control is what proved this was a feed
failure and not a quiet tape** (59c), so "zero premarket volume" was not written up as a
market observation. Consequence: every premarket scanner price today is an unverified quote —
55b's arithmetic reconciles (PACK $4.61/$4.22 ✓, AMPG $3.63/$3.44 ✓, TRT $7.47/$7.26 ✓) but
59 proved that certifies nothing. **New lesson 66** — escalated as an entitlement gap.

⚠️ **`eligibility` dropped 2 of 8 rows again (lesson 43a).** `eligibility SCHL LGCY TBN HTLM
ZONE TRT PACK AMPG` returned **6 rows, omitting SCHL and LGCY, exit 0.** Re-run individually
both returned normally — **and SCHL was the session's primary earnings candidate**, the third
time the dropped row was the name that mattered. The count check caught it. A later 6-ticker
call returned 6/6 cleanly.

✅ **`macro` populated every field** and correctly flagged + corrected the Brent contract roll
(naive −7.27% → true −1.37%) rather than printing a plausible-and-backwards number (lesson 50).

⚠️ **Screener `RelVol` remains unusable as a volume signal** (lesson 17d/g, 64): 18 of 20
`unusual_volume` rows printed **below 1.0×** on a list whose entire purpose is ranking by
relative volume. Only GLND (17.9×) and GRML (3.1×) read above 1.0, and both are standing
pump/shell kills. `breakouts` also returned a Finviz query error on one of its screens —
logged, not scored.

### Factor watch

Benchmark is IWM since 2026-09-17 — the core contributes zero excess return by construction.
Satellites sit at **14.7% of slice (RARE only)** against the 50% floor; IWM core at 49.7%,
effectively at its cap. **One PRME entry would take satellites to only ~29.5%** — three more
qualifying names are needed to clear the floor, and the board has not produced three in nine
sessions.

🚨 **`weekly_review` W36 (9/04), W37 (9/11), W38 (9/18) owed — and W39 falls due TODAY
(Fri 9/25), making FOUR.** Chain stale since 8/28 W35, now 20+ sessions. Escalated every
session; not remediated (lesson 47c) / [[launchd-quota-contention]]. **Four owed reviews is
where the escalation backlog — rebalance basis (44), ADV-vs-account-size (46f), stop width
(48c/51d), and now the satellite-floor pattern (61/63) — is stuck.**
