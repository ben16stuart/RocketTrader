# Rocket Research Log — Watchlist & Catalyst Notes

Updated by pre-market and midday sessions. Target ≤120 lines. Archive resolved or stale
entries to `memory/archive/research_log_history.md` (the W41 board was archived there 2026-10-10).

---

> 🔁 **2026-10-17 — REBUILT AS RANK → JUDGE (Ben: "rebuild rocket tonight").** Read CLAUDE.md
> "How Rocket Picks Stocks" before anything else. Selection = `scripts/rank_screen.py` (6-1 month
> momentum ÷ vol, ~1,800 small caps $150M–$10B) → your judgment → up to 8 satellites at ~12%, 25%
> trailing stop, no profit ladders, exits on stop / thesis break / weekly rank > 25. Every BUY, top-8
> VETO and non-stop EXIT is logged with `scripts/candidate_ledger.py` and scored vs IWM.
> Why: 22 straight sessions below the 50% floor (9/17–10/16), 0% in stocks after 10/5. The checklist
> below rejected nearly everything and nothing measured what it rejected.
> **Mon 10/19 premarket, priority #1:** satellites 0% vs the 50% floor. Run `rank_screen.py`, fill up to
> 5 slots (this week's cap) from the top of the ranking with the judgment checks, and log every top-8 skip
> as a VETO. The Week 42 board below (RAPP/EIKN/HAWK/CODI…) is **history, not a to-do list**; a name
> from it is bought only if it ranks.

## Watchlist — Week 43 (Mon 10/19 – Fri 10/23), built at W42 review Sat 10/17  ← CURRENT

**The first week under rank → judge.** Satellites **0%** (floor 50%, breached at 20 straight closes). Weekly entry cap: **5**. Healthcare cap: 3.
Book (10/16 close): IWM 9.9763 sh × $270.44 = $2,697.99. Slice $2,988.05 → 12.5% cap ≈ **$373** per satellite. Every BUY needs a
**CORE FUNDING** IWM sale right before it (rule 3). The W42 board (RAPP/EIKN/HAWK/CODI/OIG/TRAX/VSTM) was archived 2026-10-17. It is history.

### Candidates for Monday's premarket to confirm (`rank_screen.py --no-save`, data as of 10/16; RE-RUN Monday, the ranks move)
| rk | sym | sector | cap $M | earn | gate | to check before buying |
|---|---|---|---|---|---|---|
| 1 | REPL | HC | 1,023 | 11/05 | OK | binary veto: RP1 BLA/PDUFA status, any readout ≤10 td. Dilution after a +493% run |
| 2 | SMWB | Tech | 737 | 11/17 | FAIL Israel HQ | log VETO |
| 3 | TXG | HC | 9,102 | 11/05 | OK | EDGAR incorporation; cap near the $10B ceiling |
| 4 | NEO | HC | 2,139 | 10/28 | OK | earnings ≤5 td from Wed 10/21: buy Mon/Tue or veto |
| 5 | ABCL | HC | 3,824 | 11/09 | FAIL Canada HQ | log VETO |
| 6 | OABI | HC | 667 | 10/30 | OK | dilution check |
| 7 | SDGR | HC | 1,691 | 11/04 | OK | probably the HC-cap VETO (4th clean HC name) |
| 8 | DK | Energy | 4,690 | 11/06 | OK | refiner; oil headline risk (Brent 109.86) |
| 9 / 10 / 11 | NSIT / HNGE / GTLB | Tech / HC / Tech | 4,710 / 8,002 / 8,791 | 11/05 / 11/02 / 12/01 | OK | next in line |
| 16 | QMCO | Tech | 728 | 11/09 | OK | 59.6% short, 117 vol: run the pump check |

**Rank-decay replacements:** none (no held satellites).
**Week's scheduled events, ranked names:** NEO 10/28, UTZ/WKC/CDNA 10/29, OABI 10/30. **VIX closed 19.99 on 10/16 (+21%).** Above 22, entries pause.

### Open escalations awaiting a user decision
**RESOLVED 2026-10-17 by the rank → judge rebuild:** #1 (8 slots at 12.5%: the floor needs 4–5 names, not
4/4 at max), #4 ($2B ceiling → $10B, IWM's range), #5 (midday −5% cut retired; 25% stop), #7 (the daily ntfy
now uses `agent_performance.py`, Rocket's own book from fills: +0.88 pts vs IWM since 7/20 on 10/16, which
matches the hand-built +0.93%). #2, #3 and #6 are advisory under the new process.
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
