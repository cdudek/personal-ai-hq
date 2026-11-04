---
type: topic
summary: Meeting prep used by brief (today) and weekly (the week) - reads attached docs and last time's action items
status: draft
updated: {{SETUP_DATE}}
---

# Routine: meeting prep (called by brief and weekly)

Goal: for every meeting, the user sees why it matters, what is attached, and what was promised last time, by them and by the others. `brief.md` runs this for today's meetings, `weekly.md` for the next 7 days. On its own: "Follow routines/meeting-prep.md for <meeting>".

## 1. The event
From the calendar (see tool routing): title, time, attendees, description, attachments, and whether it is recurring. If the calendar source does not return attachments, try another connector for that event, then the browser. Say in one line which source you used.

## 2. Read what is attached or linked
For each attachment and each link in the description, read it with the right connector and write a 1-2 sentence summary of what matters for this meeting: documents and sheets (docs connector), task boards and tasks (tasks connector: open tasks, owners, due dates), tickets and projects (state, last update), whiteboards (whiteboard connector), anything else (browser).

If a document cannot be opened (no access, connector missing), list it with "not readable: <reason>". Never summarise a document you did not read.

## 3. Last time (recurring meetings, or the last meeting with the same people)
**Always, also when the meeting is off:** off, declined, cancelled or moved meetings still show last time's decisions, open action items (mine and others') and open points, and say where they roll to (the next occurrence, with its date). Never drop the prep because the meeting does not happen. If the notes are partial or garbled, say so in one line.
Every recurring meeting on the page gets this, not only the first one: check each before writing the page.

Find the previous occurrence:
- transcript or summary from the notes and meetings tool
- the running notes doc, if the event has one attached (often the action items live there)

Extract the action items:
- **mine:** what the user committed to. Check if it is done (sent mail, merged PR, closed ticket, chat reply). Status: done | open | unclear.
- **others:** what each other attendee committed to, with their name and the same status check.
- **open points:** questions left open.

The user's open items also go to the Inbox of the task store with `closed when:` (proposal, as in the brief).

## 3a. 1:1s: what runs between you
Only for meetings explicitly marked as a 1:1 in the title ("1:1", "1-1", "1on1", "One-on-One", "Name / <user>"). Not for any other small meeting.

Match the attendee to a profile in `context/people/` by email or id (never by first name; two candidates means ask). Then:
1. Read the profile's "Current" section first and use it as the starting point.
2. Refresh it (`routines/people.md`, mode Refresh) when it is older than 7 days or missing, then use the fresh one. No profile or no ids: resolve them first (mode Resolve), or say so in one line and use names.

Look at the last 14 days between the user and that person:
- chat DMs and threads where both wrote, mail threads with them, tickets and PRs where one waits for the other, earlier 1:1 notes, their page in `context/people/` (ids give exact matches in each tool).
- **you owe:** unanswered messages from them, open promises from the last 1:1, PRs or tickets where they wait on the user.
- **they owe:** their open promises, answers the user waits for.
- **threads:** 3-5 running topics, one line each, each with its deep link.
- **agenda:** 3 proposed points that follow from the above.

## 3b. Topic meetings: where the topic stands
When the meeting is about a topic that lives somewhere (title, description or an attachment names a ticket, project or initiative, or a goal from `context/goals.md`), read that and add:
- **state:** status or health and progress, in one line.
- **updates:** the latest 2-3 status updates or comments, with date.
- **open:** open questions, blockers, overdue sub-items, each with its deep link.

If no topic can be matched, skip it; never guess one. Role adapters list typical meeting types (see `context/me.md`).

## 4. Prep category and action
- **Deep prep:** strategy, roadmap, important stakeholders. Becomes a task in This week with `closed when:`.
- **Quick reminder:** syncs and 1:1s ("read last notes 5 minutes before").
- **No action:** broadcasts and all-hands.

## 5. Output into the view data
Per meeting, in `meetings[]` (schema in `views/CLAUDE.md`). Always: who (with a one-line note from `context/people/`), why, prep, attachments[] (label, url, source, summary), action_items.mine[] and action_items.others[] (who, text, status), open_points[], links[], tag (prep category). For 1:1s also `between`, for topic meetings also `topic`.

## Friction
When the user corrects the prep, log it to `meta/friction.md`.
