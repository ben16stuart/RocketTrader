#!/bin/bash
# Rocket routine runner — called by launchd on schedule.
# Usage: ./run_routine.sh <routine_name>

set -euo pipefail

ROUTINE="${1:-}"
REPO_DIR="/Users/benstuart/Desktop/DockerApps/RocketTrader"
LOG_DIR="$REPO_DIR/logs"
mkdir -p "$LOG_DIR"

if [[ -z "$ROUTINE" ]]; then
  echo "Usage: $0 <routine_name>" >&2
  echo "Available: premarket market_open midday market_close weekly_review" >&2
  exit 1
fi

PROMPT_FILE="$REPO_DIR/routines/${ROUTINE}.md"
if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "Routine file not found: $PROMPT_FILE" >&2
  exit 1
fi

LOG_FILE="$LOG_DIR/${ROUTINE}_$(date +%Y-%m-%d_%H%M).log"
echo "── Rocket Routine: $ROUTINE — $(date) ──" | tee "$LOG_FILE"

# Restore full environment (launchd strips it)
export HOME="/Users/benstuart"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
eval "$(pyenv init -)" 2>/dev/null || true
unset CLAUDECODE  # prevent nested-session guard

# --- Keep the Mac awake for the length of this run ---------------------------
# launchd fires these jobs on a macOS DarkWake, and on battery the Sleep Service
# puts the machine BACK to sleep ~30s later. A premarket runs 8-15 minutes, so the
# network connection died mid-response ("API Error: Connection closed mid-response")
# on BOTH agents' premarkets on 2026-09-21 -- the first widened-mandate premarket --
# and on 2026-09-07/08 before it. The fallback model failed identically, because the
# cause is the machine sleeping, not the model. A PreventUserIdleSystemSleep
# assertion is honored on battery; `-w $$` ties it to this script's lifetime so it
# releases itself the moment the run ends. (`-s` would be ignored on battery.)
( /usr/bin/caffeinate -i -w $$ >/dev/null 2>&1 & ) || true

# Load Rocket-specific secrets from .env.local
ENV_FILE="$REPO_DIR/.env.local"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "❌ $ENV_FILE not found — copy .env.local.example and fill in your secrets" | tee -a "$LOG_FILE"
  exit 1
fi

# Claude auth is shared with Bull: a long-lived (1yr) CLAUDE_CODE_OAUTH_TOKEN
# from `claude setup-token`, stored in Bull's .env.local. No refresh needed.
BULL_REPO="/Users/benstuart/Desktop/DockerApps/OpusTrader"
BULL_ENV="$BULL_REPO/.env.local"

# shellcheck source=/dev/null
source "$ENV_FILE"

# macOS ships bash 3.2, where `source <(...)` process substitution can silently
# fail to propagate variables to the parent shell — extract directly instead.
CLAUDE_CODE_OAUTH_TOKEN=$(grep '^export CLAUDE_CODE_OAUTH_TOKEN=' "$BULL_ENV" | sed "s/^export CLAUDE_CODE_OAUTH_TOKEN='\\(.*\\)'\$/\\1/")
export CLAUDE_CODE_OAUTH_TOKEN

cd "$REPO_DIR"

# Pull latest memory from GitHub
git pull origin main --quiet 2>&1 | tee -a "$LOG_FILE" || true

# Deps are installed once manually (pip install -r requirements.txt).
# Re-run that by hand after editing requirements.txt — not on every routine.

# Extract only the "## Prompt" section (strips setup documentation)
PROMPT_CONTENT=$(awk '/^## Prompt$/{found=1; next} found{print}' "$PROMPT_FILE")

if [[ -z "$PROMPT_CONTENT" ]]; then
  echo "❌ Could not extract ## Prompt section from $PROMPT_FILE" | tee -a "$LOG_FILE"
  exit 1
fi

echo "  ✅ Prompt extracted ($(echo "$PROMPT_CONTENT" | wc -l | tr -d ' ') lines)" | tee -a "$LOG_FILE"

# Parse the model TIER from the routine header (e.g. "**Model**: sonnet ...").
# Headers name a tier (opus / sonnet / haiku), not a pinned version. resolve_model.py
# asks the Anthropic catalog which model in that tier shipped most recently, so the
# agents move onto each new release automatically.
#
# Do NOT swap this for the CLI's own alias (--model opus): that alias table is baked
# into the installed binary and lags reality -- on CLI 2.1.153 it still resolved
# "opus" to claude-opus-4-7, older than what we pin here.
MODEL_TIER=$(grep -m1 '^\*\*Model\*\*:' "$PROMPT_FILE" 2>/dev/null | sed 's/\*\*Model\*\*:[[:space:]]*//' | awk '{print $1}' || true)
MODEL_TIER="${MODEL_TIER:-opus}"
MODEL=$(python3 "$REPO_DIR/scripts/resolve_model.py" "$MODEL_TIER" 2>>"$LOG_FILE" || true)
MODEL="${MODEL:-$MODEL_TIER}"
echo "  🤖 Model: $MODEL (tier: $MODEL_TIER)" | tee -a "$LOG_FILE"

# --- Gatekeeper pre-flight -------------------------------------------------
# Homebrew stamps com.apple.quarantine on every cask artifact, so the FIRST launch
# of a freshly-upgraded `claude` binary raises a macOS approval dialog. A launchd
# job at 4am has no one to click it, so the session blocks until someone does.
# This bit us twice: 2026-07-24, and again 2026-07-31 after a 2.1.153 -> 2.1.212
# upgrade, when premarket started at 04:00 and did not finish until 08:16 -- its
# research landing 41 minutes AFTER the open it was written to inform.
# Clearing the flag here is scoped to this one binary and self-heals after any
# future upgrade. It is not a security downgrade: the binary is still signature-
# checked by macOS, and Anthropic signs it (Developer ID: Anthropic PBC).
CLAUDE_BIN="$(command -v claude || true)"
if [[ -n "$CLAUDE_BIN" ]]; then
  CLAUDE_BIN="$(readlink -f "$CLAUDE_BIN" 2>/dev/null || echo "$CLAUDE_BIN")"
  if xattr -p com.apple.quarantine "$CLAUDE_BIN" >/dev/null 2>&1; then
    echo "  🔓 clearing macOS quarantine on $CLAUDE_BIN (post-upgrade)" | tee -a "$LOG_FILE"
    xattr -d com.apple.quarantine "$CLAUDE_BIN" 2>/dev/null || true
  fi
fi

# Subagents inherit the parent model unless told otherwise. On 2026-07-27 that
# silently put 5 research subagents on Opus 5 -- 48% of that day's tokens -- and
# starved Rocket's market_open into a session limit. Subagents only ever do
# retrieval (web search, news checks, screeners); the parent does all reasoning
# and every trading decision. So pin them to Sonnet regardless of parent tier.
SUBAGENT_MODEL=$(python3 "$REPO_DIR/scripts/resolve_model.py" sonnet 2>>"$LOG_FILE" || true)
export CLAUDE_CODE_SUBAGENT_MODEL="${SUBAGENT_MODEL:-claude-sonnet-5}"
echo "  🤖 Subagents: $CLAUDE_CODE_SUBAGENT_MODEL (retrieval only)" | tee -a "$LOG_FILE"

if [[ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
  echo "❌ CLAUDE_CODE_OAUTH_TOKEN not found in $BULL_ENV" | tee -a "$LOG_FILE"
  exit 1
fi
echo "  ✅ Auth token loaded (${CLAUDE_CODE_OAUTH_TOKEN:0:16}...)" | tee -a "$LOG_FILE"

# >>> model attempt chain
# How a run FAILS decides what happens next. Getting this wrong was expensive twice:
#   2026-09-23  Opus 5.5 shipped; this CLI (2.1.212) rejects it. Every failure was treated as
#               a rate limit, so Opus-tier analysis silently ran on Sonnet for two days.
#   2026-09-24  Session limit hit at the close. The runner fell to Haiku, which shares the same
#               account-wide limit, failed identically, and the log still said "Done".
#
#   unsupported    CLI too old for the model -> next-older model in the SAME tier.
#   session_limit  Account-wide: every Claude model shares it, so NO fallback helps. Fail loudly.
#   transient      529 / 5xx / dropped connection -> retry the SAME model after a pause, but only
#                  if it failed almost immediately (see below). Never downgrade to a weaker model:
#                  a Sonnet-grade "Opus" session quietly corrupts what is being measured.
#   other          Fail loudly.
#
# A run is only ever retried if it failed within FRESH_SECS. In `-p` mode nothing is printed until
# the end, so a long run that dies mid-way looks identical to one that died at the first call --
# but it may already have placed an order or edited memory, and a blind rerun would repeat that.
if [[ "$(basename "$REPO_DIR")" == "OpusTrader" ]]; then AGENT_LABEL="Bull"; else AGENT_LABEL="Rocket"; fi
ATTEMPT_OUT="$(mktemp -t agent_attempt.XXXXXX)"
trap 'rm -f "$ATTEMPT_OUT"' EXIT

FRESH_SECS="${AGENT_FRESH_SECS:-30}"
RETRY_SLEEP="${AGENT_RETRY_SLEEP:-60}"
FAIL_KIND=""; FAIL_DETAIL=""; FAIL_ELAPSED=0; RAN_MODEL=""; RUN_OK=0

run_claude() {
  "${CLAUDE_CMD:-claude}" \
    --model "$1" \
    --dangerously-skip-permissions \
    -p "$PROMPT_CONTENT" \
    2>&1 | tee -a "$LOG_FILE" | tee "$ATTEMPT_OUT"
  return "${PIPESTATUS[0]}"
}

classify_failure() {
  FAIL_KIND="other"
  if grep -qiE "does not support this model|version [0-9.]+ or newer is required" "$ATTEMPT_OUT"; then
    FAIL_KIND="unsupported"
  elif grep -qiE "hit your .{0,30}limit|session limit|usage limit" "$ATTEMPT_OUT"; then
    FAIL_KIND="session_limit"
  elif grep -qiE "API Error: (5[0-9]{2}|Connection closed|Unable to connect)|overloaded|ENOTFOUND|ECONNRESET|ETIMEDOUT|Could not resolve" "$ATTEMPT_OUT"; then
    FAIL_KIND="transient"
  fi
  FAIL_DETAIL="$( { grep -ioE "resets [0-9]{1,2}(:[0-9]{2})?[ap]m \([A-Za-z_/]+\)" "$ATTEMPT_OUT" || true; } | head -1 )"
  return 0
}

# try_tier <tier>: 0 = a model ran; 1 = failed (FAIL_KIND / FAIL_DETAIL / FAIL_ELAPSED say why).
try_tier() {
  local tier="$1" m n started
  local chain=()
  while IFS= read -r m; do
    if [[ -n "$m" ]]; then chain+=("$m"); fi
  done <<< "$(python3 "$REPO_DIR/scripts/resolve_model.py" "$tier" --all 2>>"$LOG_FILE" || true)"
  if [ "${#chain[@]}" -eq 0 ]; then chain=("$tier"); fi
  for m in "${chain[@]}"; do
    n=0
    while :; do
      n=$((n + 1)); RAN_MODEL="$m"
      echo "  🤖 Attempt: $m (try $n)" | tee -a "$LOG_FILE"
      started=$SECONDS
      if run_claude "$m"; then return 0; fi
      FAIL_ELAPSED=$((SECONDS - started))
      classify_failure
      case "$FAIL_KIND" in
        unsupported)
          echo "  ⚠️  $m is rejected by this Claude Code install (run 'claude update') — trying the next-older $tier model" | tee -a "$LOG_FILE"
          break ;;
        transient)
          if [ "$FAIL_ELAPSED" -le "$FRESH_SECS" ] && [ "$n" -lt 3 ]; then
            echo "  ⏳ transient API error ${FAIL_ELAPSED}s in — retrying $m in ${RETRY_SLEEP}s" | tee -a "$LOG_FILE"
            sleep "$RETRY_SLEEP"
            continue
          fi
          return 1 ;;
        *) return 1 ;;
      esac
    done
  done
  return 1
}

report_failure() {
  local why hint
  case "$FAIL_KIND" in
    session_limit) why="Claude session limit${FAIL_DETAIL:+ ($FAIL_DETAIL)}. Every Claude model shares it, so there is no fallback." ;;
    unsupported)   why="No $MODEL_TIER model is supported by this Claude Code. Run 'claude update'." ;;
    transient)     why="API error persisted (last failure ${FAIL_ELAPSED}s in)." ;;
    *)             why="Unrecognized failure. See the log." ;;
  esac
  if [ "$FAIL_ELAPSED" -le "$FRESH_SECS" ]; then
    hint="It failed before doing any work: nothing was executed."
  else
    hint="It ran ${FAIL_ELAPSED}s before failing, so some steps may already have executed. Check positions and open orders before rerunning."
  fi
  echo "  🚨 FAILED: $why $hint" | tee -a "$LOG_FILE"
  if [[ -z "${AGENT_TEST_MODE:-}" ]]; then
    (cd "$REPO_DIR" && python3 scripts/ntfy_notify.py \
      "🚨 $AGENT_LABEL $ROUTINE FAILED — no output" "$why $hint" --priority high >/dev/null 2>&1) || true
  fi
}

if try_tier "$MODEL_TIER"; then
  RUN_OK=1
  echo "  🤖 Ran on: $RAN_MODEL" | tee -a "$LOG_FILE"
else
  report_failure
fi
# <<< model attempt chain

if [ "$RUN_OK" = 1 ]; then
  echo "── Done: $ROUTINE — $(date) ──" | tee -a "$LOG_FILE"
else
  # Not "Done": a run that produced nothing must never read as a success in the log.
  echo "── FAILED: $ROUTINE — ${FAIL_KIND:-unknown} — $(date) ──" | tee -a "$LOG_FILE"
fi

# Keep only last 30 log files per routine
ls -t "$LOG_DIR/${ROUTINE}_"*.log 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null || true

# Exit non-zero on failure so launchd's last-exit code reflects it.
if [ "$RUN_OK" != 1 ]; then exit 1; fi
