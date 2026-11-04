#!/usr/bin/env bash
# Usage: scripts/release.sh <new-version>   e.g. scripts/release.sh 0.3.0
# Bumps plugin.json, marketplace.json and the template .hq-version, prepends a CHANGELOG stub, commits and tags vX.Y.Z. Never pushes.
set -euo pipefail
cd "$(dirname "$0")/.."
v="${1:?usage: scripts/release.sh <new-version>}"
[[ "$v" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "version must be X.Y.Z"; exit 1; }
[ -z "$(git status --porcelain)" ] || { echo "commit or stash your changes first"; exit 1; }
git rev-parse "v$v" >/dev/null 2>&1 && { echo "tag v$v exists"; exit 1; }
sed -i.bak -E "s/(\"version\": \")[0-9.]+/\1$v/" .claude-plugin/plugin.json .claude-plugin/marketplace.json
rm -f .claude-plugin/*.bak
printf '%s\n' "$v" > template/workspace/.hq-version
python3 - "$v" <<'PY'
import sys, datetime
v = sys.argv[1]
s = open("CHANGELOG.md").read()
head, _, rest = s.partition("\n## ")
open("CHANGELOG.md", "w").write(f"{head}\n## {v} ({datetime.date.today()})\n\n- TODO: one line on what changed, and what /hq:upgrade will do.\n\n## {rest}")
PY
bash scripts/check-version.sh
git add -A
git commit -qm "release $v"
git tag "v$v"
echo "committed and tagged v$v (not pushed). The CHANGELOG entry is a stub: edit it, then git add -A && git commit --amend --no-edit && git tag -f v$v"
