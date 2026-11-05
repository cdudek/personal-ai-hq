---
type: topic
summary: Re-plan during the day after new input
status: draft
updated: {{SETUP_DATE}}
---

# Routine: sync (on demand, during the day)

Trigger: the user says "sync" or gives new input ("new priority: ...", "Alex wants ...").

1. Collect what's new since the last brief or sync: the same sources as `brief.md`, step 1 (including `routines/ingest.md` on `sources/_incoming/`), plus whatever the user just said.
2. Run `routines/radar.md`, but show only new items.
3. Re-plan: compare This week with the new input and propose swaps ("Move X in, push Y?"). Apply after a yes.
4. Append a "Sync HH:MM" section to today's `daily/` note listing what moved and why.
5. Update today's `views/data/daily-YYYY-MM-DD.json` with the new items and moved tasks, run `python3 scripts/render_view.py` on it and open `views/daily.html` (the page's "Refresh with Claude" button runs this routine, so the page must change).
6. Update `meta/chat-cursor.md`. Build the indexes, append to `log.md`, commit.

Friction: `- YYYY-MM-DD sync: ... -> ...` to `meta/friction.md`.
