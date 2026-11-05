#!/usr/bin/env bash
# Fails (exit 1) when the repo contains private or company-specific terms. Run before every push.
set -uo pipefail
cd "$(dirname "$0")/.."
self="scripts/scrub-check.sh"
hits=0
scan() { # $1 = grep flags, $2 = pattern. grep exits 0 on a match, 1 on none, 2+ on an error (bad regex, unreadable file): an error must fail the check, not read as "0 hits"
  local out rc=0
  out=$(grep -rnE $1 --exclude-dir=.git --exclude-dir=dist --exclude="$(basename "$self")" --exclude=.scrub-terms -- "$2" . 2>&1) || rc=$?
  if [ "$rc" -gt 1 ]; then echo "$out"; echo "scrub-check: grep failed (exit $rc), the check did not run"; exit 2; fi
  if [ -n "$out" ]; then echo "$out"; hits=$((hits+1)); fi
}
# generic leaks: local paths, email addresses, Slack user and channel ids
scan "" '/Users/|U0[0-9A-Z]{8}|C0[0-9A-Z]{8,10}|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|de|io|org)'
# your own private terms (company, colleague names, internal hosts): one regex in .scrub-terms, never committed
if [ -f .scrub-terms ]; then scan -i "$(tr -d '\n' < .scrub-terms)"; else echo "scrub-check: no .scrub-terms file, only generic checks ran"; fi
if [ "$hits" -gt 0 ]; then echo "scrub-check: FAILED"; exit 1; fi
echo "scrub-check: 0 hits"
