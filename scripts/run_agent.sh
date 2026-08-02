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

# If the primary model hits a rate limit (or any failure), retry once with a
# lighter model rather than letting the whole session die with no output.
# Resolved from the tier below the primary, so the chain also stays version-proof.
case "$MODEL" in
  claude-opus-*)   FALLBACK_TIER="sonnet" ;;
  claude-sonnet-*) FALLBACK_TIER="haiku" ;;
  *)               FALLBACK_TIER="" ;;
esac
FALLBACK_MODEL=""
if [[ -n "$FALLBACK_TIER" ]]; then
  FALLBACK_MODEL=$(python3 "$REPO_DIR/scripts/resolve_model.py" "$FALLBACK_TIER" 2>>"$LOG_FILE" || true)
fi

run_claude() {
  claude \
    --model "$1" \
    --dangerously-skip-permissions \
    -p "$PROMPT_CONTENT" \
    2>&1 | tee -a "$LOG_FILE"
  return "${PIPESTATUS[0]}"
}

if ! run_claude "$MODEL"; then
  if [[ -n "$FALLBACK_MODEL" ]]; then
    echo "  ⚠️  $MODEL failed (likely rate limit) — retrying with fallback: $FALLBACK_MODEL" | tee -a "$LOG_FILE"
    run_claude "$FALLBACK_MODEL"
  fi
fi

echo "── Done: $ROUTINE — $(date) ──" | tee -a "$LOG_FILE"

# Keep only last 30 log files per routine
ls -t "$LOG_DIR/${ROUTINE}_"*.log 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null || true
