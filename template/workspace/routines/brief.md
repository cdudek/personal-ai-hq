---
type: topic
summary: Daily morning brief, collects inboxes, re-plans, asks context gaps, writes daily note and updates the task store
status: draft
updated: {{SETUP_DATE}}
---

# Routine: brief (weekdays, morning)

Goal: one short page that bridges yesterday and today, plus a task store that matches reality. The brief is a conversation: propose changes, write them only after the user confirms. When the run is scheduled and nobody answers, write the brief and leave every proposal open.

## 0. Read
`CLAUDE.md`, `index.md`, `context/me.md`, `context/goals.md`, `context/glossary.md`, `meta/chat-cursor.md`, yesterday's `daily/` note, `meta/task-store.md` and the adapter it names (`routines/stores/<store>.md`), `context/areas/index.md`, and the frontmatter (`name`, `aliases`, `ids`, `relation`, `close`) of `context/people/*.md`: the id table for matching people (`routines/people.md`).

## 0a. Sources check (before any other output)
Run "Required sources" in `CLAUDE.md`: one cheap read per required source. The first lines of the reply name every failed source with the reason and the exact fix; a working source gets no line. Failed sources go into `sources[]` with `ok: false`. A substitute must be labelled "substitute". If a source marked critical there is down, ask once whether to wait or go ahead.

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
Off, declined or cancelled meetings keep their card with last time's items and where they roll to (`routines/meeting-prep.md` section 3); never skip them.
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

People in every source (chat authors, mentions, DM partners, ticket and code actors, mail senders, attendees) are matched by id through `context/people/` (`routines/people.md`, "Matching people elsewhere"), not by name. That is how Needs me and Waiting on name the right person, and how two people with the same first name stay apart. Close people get their name first in the line.

## 3. Re-plan
Compare "This week" with what came in. Propose concrete swaps, for example: "New from X: Y, due Thursday. Move into This week and push Z?" A task that waits on a person goes to Waiting with a `Waiting on: <name>` description line (and the person's id for the task tool from `context/people/` when known: `ids`; never matched by first name; no id or two candidates means ask under "Claude asks" and name only the first name). New tasks go to the Inbox of the task store with Area (by the tie-break), Size (XS-XL), Source, Impact, Confidence, Ease and the computed ICE, Priority (proposed from ICE) and a `Closed when:` line (fields where mapped, else description lines), tagged `ai`. **ICE scoring:** for every new Inbox item and new task Claude scores Impact, Confidence and Ease (1-10 each) with a one-line why each as a task comment, and sets ICE = Impact x Confidence x Ease (never typed by hand). It proposes a Priority from ICE (P0 only when it blocks someone or is due today, else P1 for the top scores, P2 middle, P3 low) and says so in the comment. Priority answers "what first", ICE is the evidence; the user's Priority wins and is never overwritten. MoSCoW is not set here, it comes in the weekly plan. Check each open task's `closed when:` against what came in and propose closing the ones that happened.

**Context cards and choices.**
- Every task Claude creates or triages gets its context card in the description (`meta/task-store.md`). Context card, one line each: `What:` one plain sentence a person who never saw the source understands (e.g. "Merge PR #5088 in billing-api: adds invoice export"); `Why / who waits:` who needs it and what is blocked, or why it matters; `State:` where it stands right now with dates (e.g. "approved by Dana 3 Nov, CI green, conflicts: none"; "3 open invoices, oldest 12 days"); `Decision or next step:` the concrete thing the user has to do or decide, with options if it is a decision; `Effort:` rough size XS-XL and whether Claude can do part of it; `Links:` deep links to the source, never only a link.
- Refresh `State:` whenever the brief reads newer information about a task (a PR approved, a reply arrived, an invoice paid). A task without `What:` and `State:` is incomplete: read its source and write the card before the task is shown.
- Every question that asks the user to choose (next task, which one to continue, triage, weekly proposals, anything under "Claude asks") shows, per option: the What sentence, the State, who waits since when, effort (XS-XL) and what happens if it waits. Then Claude's recommendation with one reason. Never offer bare names, ids, PR numbers or ticket numbers as choices. If a task has no context card, read its source and fix the task first. This covers re-plan proposals and every "Claude asks" question. Example: "Two things are open. 1) **Merge PR #5088** (billing-api, invoice export): approved by Dana yesterday, CI green, Lee waits to deploy. XS, 2 minutes; the deploy waits if you wait. 2) **Supplier invoices**: 3 open from Acme, Globex and Initech, oldest 12 days, due to Finance by Friday. S, about 3 clicks each; a late fee after Friday. I recommend 1 first: it unblocks a deploy and takes 2 minutes."

## 4. Context gaps
Look for unknown terms, projects, documents, milestones, people and recurring themes. Check plurals, acronyms and casing first, and check the references in `CLAUDE.md`. Classify each find before asking:
- **a) Term or acronym:** `context/glossary.md`.
- **b) Person:** `context/people/`. Someone with no profile (no id or email match): resolve their ids first (`routines/people.md`, mode New person), then ask "New person: [Name], [role], [evidence]. Add a profile?". On yes create the stub with the resolved ids and their sources, `close: false`.
- **c) Document, milestone or goal:** the matching file in `context/` (`goals.md`, or the initiative's topic README in `research/`).
- **d) New project or recurring theme:** run the initiative test from `context/areas/index.md`. If it passes, ask: "New initiative? [X] (outcome, end date, area by the tie-break). Add to Top of mind?" On yes: create the initiative container in the task store (description: outcome, end date, OKR, `Topic folder: <name>`; Asana: add all eight `HQ ·` fields to the new project, see the adapter), its Top of mind task, plus its topic folder (`cp -r research/_template "research/YYYY-MM-DD - Name"`, README: question, status active, started). If it fails, it is a normal task or an idea (`ideas/`).
- **d2) New or unknown topic folder or document:** list `research/` for folders and files in `output/` or `working/` created since the last brief (git log or mtime). One that belongs to no initiative or known topic: "New in research/: [folder or file]. Which initiative is it, or is it a new one?". Never move or rename it without a yes.
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
