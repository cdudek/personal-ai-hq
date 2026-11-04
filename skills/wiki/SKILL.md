---
name: wiki
description: Maintains the second brain. `ingest` files links, articles, transcripts and documents under sources/, writes summaries and proposes the context pages they update; `refresh` runs the monthly refresh (updates context pages, lints the wiki for contradictions, stale pages, orphans and broken links, proposes a reorganisation). Use when the user says "ingest", "file this", "add this article to my wiki", "refresh", "monthly refresh", "lint the workspace" or "reorganise".
argument-hint: "[ingest <link or file>|refresh]"
---

# wiki

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

## Pick the variant

- `ingest <link or file>`: run `routines/ingest.md` for that source.
- `refresh`: run `routines/refresh.md`.
- No argument: run `routines/ingest.md` on the drop zone (`sources/` and the drop folder in `CLAUDE.md`), and say so.

Context changes are proposals until the user says yes. Rebuild indexes with `python3 scripts/build_index.py`, commit locally, never push.
