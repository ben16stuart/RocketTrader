#!/usr/bin/env python3
"""Resolve a model tier to the newest concrete Claude model ID.

Routine headers name a *tier* ("opus", "sonnet", "haiku") rather than pinning a
version string. This script asks the Anthropic model catalog which model in that
tier was released most recently, so every routine automatically moves to each new
release the day it ships — no file edits required.

Why not just pass the CLI's built-in alias (``claude --model opus``)? That alias
table is baked into the installed CLI binary, so it lags reality: on CLI 2.1.153
``opus`` still resolved to claude-opus-4-7 and ``sonnet`` to claude-sonnet-4-6,
both *older* than what these agents had pinned. Querying the catalog is the only
way to genuinely track the newest model.

If the catalog is unreachable, fall back to a pinned known-good ID so a scheduled
trading session never dies over model resolution.

Usage:  python3 resolve_model.py opus   ->  claude-opus-5
"""

import json
import os
import sys
import urllib.request

MODELS_URL = "https://api.anthropic.com/v1/models?limit=100"

# Used only when the catalog can't be reached. Refresh occasionally, but the
# catalog lookup above is what normally decides.
FALLBACK = {
    "opus": "claude-opus-5",
    "sonnet": "claude-sonnet-5",
    "haiku": "claude-haiku-4-5-20251001",
}


def newest_in_tier(tier, token, timeout=10):
    """Return the most recently released model ID in `tier`, or None."""
    req = urllib.request.Request(
        MODELS_URL,
        headers={
            "authorization": f"Bearer {token}",
            "anthropic-version": "2023-06-01",
            "anthropic-beta": "oauth-2025-04-20",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        catalog = json.load(resp)["data"]

    # The prefix keeps tiers strictly separated -- notably it never lets
    # claude-fable-* satisfy an opus/sonnet request.
    prefix = f"claude-{tier}-"
    candidates = [m for m in catalog if m.get("id", "").startswith(prefix)]
    if not candidates:
        return None
    return max(candidates, key=lambda m: m.get("created_at", ""))["id"]


def tier_models(tier, token, timeout=10):
    """Every model ID in `tier`, newest first.

    The runner walks this list when the newest model is rejected by the installed
    Claude Code (a CLI too old to know a just-released model returns HTTP 400
    "does not support this model"). 2026-09-23: Opus 5.5 shipped 9/21 while the CLI
    was 2.1.212 (needs >= 2.1.280); with only newest_in_tier() available the runner
    could not say "try the next-older Opus", so it stepped down to Sonnet and ran the
    Opus-tier analysis on the wrong model for two days.
    """
    req = urllib.request.Request(
        MODELS_URL,
        headers={
            "authorization": f"Bearer {token}",
            "anthropic-version": "2023-06-01",
            "anthropic-beta": "oauth-2025-04-20",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        catalog = json.load(resp)["data"]
    prefix = f"claude-{tier}-"
    found = [m for m in catalog if m.get("id", "").startswith(prefix)]
    return [m["id"] for m in sorted(found, key=lambda m: m.get("created_at", ""), reverse=True)]


def main():
    requested = sys.argv[1].strip() if len(sys.argv) > 1 else "opus"
    tier = requested.lower()

    # Anything that isn't a known tier is treated as an explicit pin and passed
    # through untouched, so a routine can still hard-pin a model when needed.
    if tier not in FALLBACK:
        print(requested)
        return

    token = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "")

    # --all: the whole tier, newest first, one per line. If the catalog is
    # unreachable, print only the pinned known-good ID (an older, safe model).
    if "--all" in sys.argv[2:]:
        try:
            ids = tier_models(tier, token) if token else []
        except Exception as exc:
            print(f"resolve_model: catalog lookup failed ({exc})", file=sys.stderr)
            ids = []
        print("\n".join(ids or [FALLBACK[tier]]))
        return

    if token:
        try:
            resolved = newest_in_tier(tier, token)
            if resolved:
                print(resolved)
                return
        except Exception as exc:  # network, auth, schema change -- never fatal
            print(f"resolve_model: catalog lookup failed ({exc})", file=sys.stderr)

    print(FALLBACK[tier])


if __name__ == "__main__":
    main()
