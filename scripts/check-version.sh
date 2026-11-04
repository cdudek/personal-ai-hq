#!/usr/bin/env bash
# Fails (exit 1) unless plugin.json, marketplace.json, the template's .hq-version and the top CHANGELOG entry carry the same version.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 - <<'PY'
import json, re, sys
v = {
    "plugin.json": json.load(open(".claude-plugin/plugin.json"))["version"],
    "marketplace.json": json.load(open(".claude-plugin/marketplace.json"))["plugins"][0]["version"],
    ".hq-version": open("template/workspace/.hq-version").readline().strip(),
    "CHANGELOG.md": re.search(r"^## (\d+\.\d+\.\d+)", open("CHANGELOG.md").read(), re.M).group(1),
}
if len(set(v.values())) != 1:
    sys.exit("version mismatch: " + ", ".join(f"{k} {x}" for k, x in v.items()))
print("version", v["plugin.json"], "consistent")
PY
