"""
Environment check — run at the start of every Bull routine session.
Verifies that all required packages and API connections are working.
If anything is broken, prints a clear error and exits with code 1
so the agent knows to STOP and report the issue rather than proceeding
with stale/fake data.

Usage: python scripts/check_env.py
"""
import sys
import os
import subprocess


def section(title: str):
    print(f"\n── {title} {'─' * (44 - len(title))}")


def ok(msg: str):
    print(f"  ✅ {msg}")


def fail(msg: str):
    print(f"  ❌ {msg}")


def warn(msg: str):
    print(f"  ⚠️  {msg}")


print("\n" + "=" * 50)
print("  Bull Environment Check")
print("=" * 50)

errors = []

# ── 1. Required environment variables ─────────────────
section("Environment Variables")

required_vars = {
    "ALPACA_API_KEY":     os.environ.get("ALPACA_API_KEY", ""),
    "ALPACA_SECRET_KEY":  os.environ.get("ALPACA_SECRET_KEY", ""),
    "ALPACA_BASE_URL":    os.environ.get("ALPACA_BASE_URL", ""),
    "NTFY_TOPIC":         os.environ.get("NTFY_TOPIC", ""),
}

for var, val in required_vars.items():
    if val:
        ok(f"{var} = {val[:6]}...")
    else:
        fail(f"{var} is not set")
        errors.append(f"Missing env var: {var}")

# ── 2. Python packages ─────────────────────────────────
section("Python Packages")

required_packages = ["requests", "yfinance", "pandas", "numpy", "alpaca", "openbb"]

missing = []
for pkg in required_packages:
    try:
        __import__(pkg.replace("-", "_"))
        ok(pkg)
    except ImportError:
        fail(f"{pkg} not installed")
        missing.append(pkg)

if missing:
    warn("Installing missing packages from requirements.txt ...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        ok("pip install succeeded — re-run this script or continue")
    else:
        fail("pip install failed")
        fail(result.stderr[:300])
        errors.append("pip install failed")

# ── 3. Alpaca API connectivity ─────────────────────────
section("Alpaca API")

api_key    = os.environ.get("ALPACA_API_KEY", "")
secret_key = os.environ.get("ALPACA_SECRET_KEY", "")
base_url   = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets")

if api_key and secret_key:
    try:
        import requests
        r = requests.get(
            f"{base_url}/v2/account",
            headers={
                "APCA-API-KEY-ID":     api_key,
                "APCA-API-SECRET-KEY": secret_key,
            },
            timeout=10,
        )
        if r.status_code == 200:
            data = r.json()
            ok(f"Connected — portfolio value: ${float(data['portfolio_value']):,.2f}")
        else:
            fail(f"HTTP {r.status_code}: {r.text[:100]}")
            errors.append(f"Alpaca returned {r.status_code}")
    except Exception as e:
        fail(f"Cannot reach Alpaca: {e}")
        errors.append(f"Alpaca unreachable: {e}")
else:
    warn("Skipping Alpaca check — credentials not set")

# ── 4. Ntfy connectivity ───────────────────────────────
section("Ntfy Notifications")

ntfy_topic = os.environ.get("NTFY_TOPIC", "")
if ntfy_topic:
    try:
        import requests
        r = requests.get(f"https://ntfy.sh/{ntfy_topic}/json?poll=1", timeout=5)
        if r.status_code in (200, 304):
            ok(f"ntfy.sh reachable (topic: {ntfy_topic})")
        else:
            warn(f"ntfy.sh returned {r.status_code} — may still work for sends")
    except Exception as e:
        fail(f"Cannot reach ntfy.sh: {e}")
        errors.append(f"ntfy unreachable: {e}")
else:
    warn("NTFY_TOPIC not set — notifications will fail")

# ── 5. Market data (yfinance) ─────────────────────────
section("Market Data (yfinance)")

try:
    import yfinance as yf
    t = yf.Ticker("SPY")
    hist = t.history(period="2d")
    if not hist.empty:
        spy_price = float(hist["Close"].iloc[-1])
        ok(f"yfinance working — SPY last close: ${spy_price:.2f}")
    else:
        warn("yfinance returned empty data for SPY")
except Exception as e:
    fail(f"yfinance error: {e}")
    errors.append(f"yfinance: {e}")

# ── Summary ────────────────────────────────────────────
print("\n" + "=" * 50)
if errors:
    print(f"  RESULT: {len(errors)} ERROR(S) — DO NOT PROCEED")
    for e in errors:
        print(f"    • {e}")
    print("\n  ACTION: Report these errors to Ben before continuing.")
    print("  Do not place trades or write memory files with stale data.")
    print("=" * 50 + "\n")
    sys.exit(1)
else:
    print("  RESULT: All systems go ✅")
    print("  Bull is ready to trade.")
    print("=" * 50 + "\n")
    sys.exit(0)
