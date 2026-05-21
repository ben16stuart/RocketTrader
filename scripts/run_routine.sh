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
# shellcheck source=/dev/null
source "$ENV_FILE"

cd "$REPO_DIR"

# Pull latest memory from GitHub
git pull origin main --quiet 2>&1 | tee -a "$LOG_FILE" || true

# Install/update dependencies quietly
python3 -m pip install -r requirements.txt -q 2>&1 | tee -a "$LOG_FILE" || true

# Extract only the "## Prompt" section (strips setup documentation)
PROMPT_CONTENT=$(awk '/^## Prompt$/{found=1; next} found{print}' "$PROMPT_FILE")

if [[ -z "$PROMPT_CONTENT" ]]; then
  echo "❌ Could not extract ## Prompt section from $PROMPT_FILE" | tee -a "$LOG_FILE"
  exit 1
fi

echo "  ✅ Prompt extracted ($(echo "$PROMPT_CONTENT" | wc -l | tr -d ' ') lines)" | tee -a "$LOG_FILE"

# Auth via Keychain (source: "claude.ai") — works for Pro subscribers.
# The com.bull.token_refresh LaunchAgent keeps the shared Keychain entry fresh.
# Do NOT use CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR — that path requires
# org:create_api_key scope which Pro subscriptions don't have.
claude \
  --model claude-opus-4-7 \
  --dangerously-skip-permissions \
  -p "$PROMPT_CONTENT" \
  2>&1 | tee -a "$LOG_FILE"

echo "── Done: $ROUTINE — $(date) ──" | tee -a "$LOG_FILE"

# Keep only last 30 log files per routine
ls -t "$LOG_DIR/${ROUTINE}_"*.log 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null || true
