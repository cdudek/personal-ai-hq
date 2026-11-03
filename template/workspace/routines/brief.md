---
type: topic
summary: Daily morning brief, collects inboxes, re-plans, asks context gaps, writes daily note and board
status: draft
updated: {{SETUP_DATE}}
---

# Routine: brief (weekdays, morning)

Goal: one short page that bridges yesterday and today, plus a board that matches reality. The brief is a conversation: propose changes, write them only after the user confirms. When the run is scheduled and nobody answers, write the brief and leave every proposal open.

## 0. Read
`CLAUDE.md`, `index.md`, `context/me.md`, `context/goals.md`, `context/glossary.md`, `meta/chat-cursor.md`, yesterday's `daily/` note, `board.md`.

## 1. Collect (since the last brief; on the first run, the last 24 hours)
Follow the tool routing in `CLAUDE.md`. Skip every row that says "none":
- **Calendar:** today and tomorrow
- **Notes and meetings:** yesterday's meetings (transcripts, recordings, notes) and new voice notes
- **Chat:**
  - mentions and DMs to the user
  - saved messages (saved = open)
  - new messages in the user's DM to themselves, after the cursor
- **Mail:** inbox mode "new only" (see `CLAUDE.md`)
- **Tasks and tickets:** assigned items, notifications
- **Code:** review requests and the user's open PRs
- **Drop folder:** new items (see "Phone input" in `CLAUDE.md`)

Tips for the system itself (a colleague suggests a workflow, a post or tool about working with AI) go to `meta/tips.md`, not the board.

If a source fails, say so in one line and continue. Never invent its content.

- **Recurring inputs:** read what `CLAUDE.md` lists under "Recurring inputs" when something new arrived. Summarise in 3-5 bullets, link the original, put them under "Context".

## 1a. Meeting prep
Run `routines/meeting-prep.md` for today's meetings (attached docs, last time's action items, mine and others').

## 1b. Needs me
Run `routines/radar.md`. Its list becomes the first block of the brief.

## 2. Triage
For each item, decide:
- task for the user
- task for the agent
- reply needed
- info only

Close items by the done signals in `inbox/CLAUDE.md`. Write the raw items to `inbox/YYYY-MM-DD.md` (`- HH:MM [source] text`). Apply any standing handling rules the user added to `CLAUDE.md` (for example how to treat invoices).

## 3. Re-plan
Compare "This week" with what came in. Propose concrete swaps, for example: "New from X: Y, due Thursday. Move into This week and push Z?" New tasks go to the Inbox in `board.md` with a `closed when:` line.

## 4. Context gaps
Look for unknown terms, projects, documents, milestones and people.
- Check plurals, acronyms and casing first, and check the references in `CLAUDE.md`.
- Ask at most 3 times: "A term I didn't know, the [X]... I read [source] and understand [Y]. Want me to save?"
- On the answer:
  - "yes": save it as is. Terms and abbreviations go to `context/glossary.md`, people to `context/people/`, projects to `context/projects/`.
  - "yes, but...": save the user's corrected version.
  - "no" or no answer: discard it.
- Never guess a definition.
- Only after a verified save, say "Saved [X] to context".

## 5. Write
**Labels (required):** every item in Needs attention, Replies and reviews, Waiting on others, Board proposals and on the board gets `priority` and `domain` (from `board.md`; else blocking or due today = P0, due this week = P1, otherwise P2 or P3), plus `topic` when it links to a Linear issue, project, initiative or OKR. Copy the `domains` map from `board.md` into the JSON. The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

`daily/YYYY-MM-DD.md`, section "Brief", in this order:
1. **Needs me** (from radar: PRs, tickets, mail, chat, tasks waiting for the user)
   **Waiting on others** (from radar section 6: what the user asked and nobody answered yet)
2. **Urgent items and blockers**
3. **Action items from yesterday** (checkboxes, each with its source)
4. **Meeting recaps** (one line per meeting)
5. **Today's calendar** (with prep notes)
6. **Board proposals** (from step 3)
7. **Context and vocabulary updates** ("No new terminology detected." if none)

Keep it to one screen. Then:
- write `views/data/daily-YYYY-MM-DD.json` (schema in `views/CLAUDE.md`): today's meetings with who, why, prep and open points from the last meeting; the whole board (This week and Inbox) with priority, size, domain, status, notes and links; cards for Needs me and yesterday's meetings. Also `sources[]` (`{name, ok, read_at, note}`, failed ones named), `start_here` (`{title, why, minutes, until, key}`: the one thing to do first), a `replies` section (items with `kind` reply | review, `what`, `who`), `what` on Waiting items, and `rec` (`{text, source}`) when Claude suggests a decision (schema: `views/CLAUDE.md`). Details go into the data so the click-through panel has them
- run `python3 scripts/render_view.py views/data/daily-YYYY-MM-DD.json`
- open `views/daily.html` (`open` on macOS, `xdg-open` on Linux, `start` on Windows)
- if the routing has a work chat, send the user a DM to themselves that starts with `[Brief]`: date and headline, the top 5 "Needs me" items with links, today's clashes, and the path to the daily view. Max 15 lines. Work content only, nothing from `journal/` or private lists

After the user confirms, apply the board changes to `board.md`. Update `meta/chat-cursor.md` (after the `[Brief]` DM, so it is not read back as a capture).

## 6. Close
Build the indexes, append to `log.md`, commit.

## Friction
When the user corrects anything in this routine, append to `meta/friction.md`: `- YYYY-MM-DD brief: <what went wrong> -> <what they wanted>`.
