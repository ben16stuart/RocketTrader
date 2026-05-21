"""
Send push notifications via ntfy.sh.
Usage: python scripts/ntfy_notify.py "Title" "Body" [--priority high|default|low]
"""
import os
import sys

import requests


def send_notification(
    title: str,
    body: str,
    priority: str = "default",
    topic: str | None = None,
) -> bool:
    topic = topic or os.environ.get("NTFY_TOPIC", "")
    if not topic:
        print("ERROR: NTFY_TOPIC environment variable not set.")
        return False

    try:
        # Pass title and priority as query params to support emoji/unicode in titles
        r = requests.post(
            f"https://ntfy.sh/{topic}",
            data=body.encode("utf-8"),
            params={
                "title":    title,
                "priority": priority,
            },
            timeout=10,
        )
        r.raise_for_status()
        print(f"Notification sent: [{priority}] {title}")
        return True
    except requests.RequestException as e:
        print(f"Failed to send notification: {e}")
        return False


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: ntfy_notify.py \"Title\" \"Body\" [--priority high|default|low]")
        sys.exit(1)

    title_arg = args[0]
    body_arg  = args[1]
    priority_arg = "default"

    if "--priority" in args:
        idx = args.index("--priority")
        if idx + 1 < len(args):
            priority_arg = args[idx + 1]

    success = send_notification(title_arg, body_arg, priority=priority_arg)
    sys.exit(0 if success else 1)
