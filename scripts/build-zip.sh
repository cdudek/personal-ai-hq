#!/usr/bin/env bash
# Builds dist/hq-<version>.zip for Cowork's "Upload plugin" route.
# The zip has the plugin at its root: .claude-plugin/, skills/, template/.
set -euo pipefail
cd "$(dirname "$0")/.."
version=$(python3 -c 'import json;print(json.load(open(".claude-plugin/plugin.json"))["version"])')
mkdir -p dist
out="dist/hq-${version}.zip"
rm -f "$out"
zip -rq "$out" .claude-plugin skills template README.md LICENSE CHANGELOG.md -x '*.DS_Store' '*__pycache__*'
echo "$out"
