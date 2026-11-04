---
type: topic
summary: Daily morning brief, collects inboxes, re-plans, asks context gaps, writes daily note and updates the task store
status: draft
updated: {{SETUP_DATE}}
---

# Routine: brief (weekdays, morning)

Goal: one short page that bridges yesterday and today, plus a task store that matches reality. The brief is a conversation: propose changes, write them only after the user confirms. When the run is scheduled and nobody answers, write the brief and leave every proposal open.

## 0. Read
`CLAUDE.md`, `index.md`, `context/me.md`, `context/goals.md`, `context/glossary.md`, `meta/chat-cursor.md`, yesterday's `daily/` note, `meta/task-store.md` and the adapter it names (`routines/stores/<store>.md`), `context/areas/index.md`.

## 1. Collect (since the last brief; on the first run, the last 24 hours)
Follow the tool routing in `CLAUDE.md`. Skip every row that says "none":
- **Calendar:** today and tomorrow
- **Notes and meetings:** yesterday's meetings (transcripts, recordings, notes) and new voice notes
- **Chat:**
  - mentions and DMs to the user
  - saved messages (saved = open)
  - new messages in the user's DM to themselves, after the cursor
- **Mail:** inbox mode "new only" (see `CLAUDE.md`)
- **Task store:** open tasks (read via the adapter) and all comments added since the last run: each comment is an instruction ("next week", "delegate to X", "P0"); propose the matching change in step 3. Never reorder a task the user moved.
- **Tasks and tickets elsewhere:** items assigned to the user in team tools and notifications; each becomes a team task in the task store (link back, or multi-home where the adapter allows)
- **Code:** review requests and the user's open PRs
- **Drop folder:** new items (see "Phone input" in `CLAUDE.md`)

Tips for the system itself (a colleague suggests a workflow, a post or tool about working with AI) go to `meta/tips.md`, not the task store.

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
Compare "This week" with what came in. Propose concrete swaps, for example: "New from X: Y, due Thursday. Move into This week and push Z?" New tasks go to the Inbox of the task store with Area (by the tie-break), Priority, Size, Source and a `closed when:` line, tagged `ai`. Check each open task's `closed when:` against what came in and propose closing the ones that happened.

## 4. Context gaps
Look for unknown terms, projects, documents, milestones, people and recurring themes. Check plurals, acronyms and casing first, and check the references in `CLAUDE.md`. Classify each find before asking:
- **a) Term or acronym:** `context/glossary.md`.
- **b) Person:** `context/people/`.
- **c) Document, milestone or goal:** the matching file in `context/` (`projects/`, `topics/`, `goals.md`).
- **d) New project or recurring theme:** run the initiative test from `context/areas/index.md`. If it passes, ask: "New initiative? [X] (outcome, end date, area by the tie-break). Add to Top of mind?" On yes: create the Top of mind task and the Initiative option in the task store, plus a context note in `context/projects/`. If it fails, it is a normal task or an idea (`ideas/`).
- **e) Fits no area by the tie-break:** do not force it. Log `- YYYY-MM-DD brief: area misfit: <what> -> proposes new or split area` to `meta/friction.md`, so the Friday improve loop proposes a new or split area.

Rules: ask at most 3 questions per brief, in the form "A term I didn't know, the [X]... I read [source] and understand [Y]. Want me to save?". On "yes" save as is; on "yes, but..." save the user's version; on "no" or no answer discard. Never guess a definition. Only after a verified write (read it back), say "Saved [X]".

## 5. Write
**Labels (required):** every item in Needs attention, Replies and reviews, Waiting on others, Task proposals and on the board gets `priority` and `area` (from the task store; else blocking or due today = P0, due this week = P1, otherwise P2 or P3; area by the tie-break in `context/areas/index.md`), plus `initiative` and `okr` when they apply. Board items also carry `id` and `url` (the task's deep link) from the task store. The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

`daily/YYYY-MM-DD.md`, section "Brief", in this order:
1. **Needs me** (from radar: PRs, tickets, mail, chat, tasks waiting for the user)
   **Waiting on others** (from radar section 6: what the user asked and nobody answered yet)
2. **Urgent items and blockers**
3. **Action items from yesterday** (checkboxes, each with its source)
4. **Meeting recaps** (one line per meeting)
5. **Today's calendar** (with prep notes)
6. **Task proposals** (from step 3)
7. **Context and vocabulary updates** ("No new terminology detected." if none)

Keep it to one screen. Then:
- write `views/data/daily-YYYY-MM-DD.json` (schema in `views/CLAUDE.md`): today's meetings with who, why, prep and open points from the last meeting; the open tasks of the task store (Top of mind, This week, Waiting, Inbox) with `id`, `url`, `section`, `area`, `initiative`, `priority`, `size`, `source`, `okr`, `waiting_on`, `closed_when`, `due`; cards for Needs me and yesterday's meetings. Also `sources[]` (`{name, ok, read_at, note}`, failed ones named), `start_here` (`{title, why, minutes, until, key}`: the one thing to do first), a `replies` section (items with `kind` reply | review, `what`, `who`), `what` on Waiting items, and `rec` (`{text, source}`) when Claude suggests a decision (schema: `views/CLAUDE.md`). Details go into the data so the click-through panel has them
- run `python3 scripts/render_view.py views/data/daily-YYYY-MM-DD.json`
- open `views/daily.html` (`open` on macOS, `xdg-open` on Linux, `start` on Windows)
- if the routing has a work chat, send the user a DM to themselves that starts with `[Brief]`: date and headline, the top 5 "Needs me" items with links, today's clashes, and the path to the daily view. Max 15 lines. Work content only, nothing from `journal/` or private lists

After the user confirms, apply the changes to the task store through the adapter. Update `meta/chat-cursor.md` (after the `[Brief]` DM, so it is not read back as a capture).

## 6. Close
Build the indexes, append to `log.md`, commit.

## Friction
When the user corrects anything in this routine, append to `meta/friction.md`: `- YYYY-MM-DD brief: <what went wrong> -> <what they wanted>`.
