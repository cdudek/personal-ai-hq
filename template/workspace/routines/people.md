---
type: topic
summary: People mapping - find the close team, resolve identities across tools, keep a derived Current picture per person
status: draft
updated: {{SETUP_DATE}}
---

# Routine: people (map, resolve, refresh)

Goal: Claude knows who the user's close team is, every person's identity in every tool, and what is running between the user and each of them, so briefs, 1:1 prep, Waiting on and the task store match people reliably. Each person has a folder `context/people/<slug>/` with `profile.md` (schema below) and `records/` (see Records).

## Privacy rules (also in `CLAUDE.md`)

- Only what the user can already see: their DMs, channels they are in, threads they are part of, repos and projects they have access to.
- Never their private mail, never their DMs with other people.
- Facts only. Claude writes no performance judgements, no opinions, no moods.
- Personnel matters and feedback are records in the user's own words (see Records), never paraphrased or inferred by Claude. They never appear on a page, in a draft, chat, tasks or any shared output.
- Work content only. Nothing from `journal/` or private lists.
- The workspace stays local: a profile or record never goes into chat, a ticket, a code review or a shared page.

## Profile schema

Frontmatter of `context/people/<slug>/profile.md`:

```yaml
type: person
name: full name
summary: one line for the index
role: title or function
relation: manager | report | skip-level | peer | stakeholder | freelancer | external
contract: permanent | freelance | unknown
team: team name
areas: [list, from context/areas]
close: true | false
aliases: [nicknames; disambiguate same first names, e.g. two people called Alex]
ids:
  email:
  slack_id:
  slack_handle:
  github:
  linear:
  asana:
  hubspot_owner:   # only sales and CS people
sources: {slack_id: "chat user search 2026-11-04", ...}   # id -> where it came from
last_1on1: YYYY-MM-DD
status: draft | current
updated: YYYY-MM-DD
```

Body sections of `profile.md` (the one high-level file per person; it stays short):
- **Role and what they own.**
- **Personality and how they work:** the user's words only.
- **How we work together:** the user's words only. Claude may propose a line under "Claude asks"; it is written only after the user says yes, in the user's wording.
- **How I write to them:** learned recipient-specific style rules (greeting, language, length, tone, sign-off). Written only from the Friday review, after the user's Adopt (`routines/review.md` section 1). `routines/meeting-prep.md` and every drafting routine read it before drafting to this person.
- **Current:** derived, close people only, fully rewritten on every refresh (see Mode 3). Never edited by hand, never kept across refreshes.
- **Claude asks:** open questions (ambiguous ids, relation, close or not).

## Records

Everything that must not change lives in `context/people/<slug>/records/YYYY/MM/YYYY-MM-DD.md`: feedback the user gives staff, feedback they receive, personnel matters, what they discuss and decide with someone. One file per person per day, append-only. Entry format:

```
- HH:MM [type] text · source: <link or "the user">
```

Types: `feedback-given`, `feedback-received`, `1:1`, `decision`, `commitment`, `discussion`, `personnel`.

Rules:
- **Immutable.** A past day's file is never edited. A correction is a new entry today that names the earlier date ("corrects 2026-01-14 14:10: ..."). Within today's file only append.
- **Own words only.** `personnel` and `feedback-*` entries are written only from the user's own words: they say or dictate them, or confirm a proposal. Claude never infers a judgement about a person. A proposal is shown as the exact line and written only after the user's yes.
- **Never shared.** Records, and `[personnel]` entries above all, never appear on a page, in a draft, chat, tasks, tickets or any shared output, and never leave the workspace.
- **No judgement in the other types.** `1:1`, `decision`, `commitment`, `discussion` hold facts: what was said, decided, promised, with the date.

Who writes records:
- **capture** ("feedback to X: ...", "note on X: ..."): writes the entry from the user's words (`routines/capture.md`).
- **debrief and meeting-prep**, after a 1:1 or meeting: propose entries from the transcript or notes; write after the user confirms (`routines/debrief.md`, `routines/meeting-prep.md`).
- **brief**: when it sees a decision or commitment with a person, it proposes an entry; written after a yes.
- **refresh** (monthly): proposes updates to the profile summary (Role, Personality, How we work together) from the records; written after a yes. The records themselves are never touched.

Rules: an empty id means not resolved yet. Never guess an id. Every id has a `sources` entry. Changing `close`, `relation`, `contract` or any id needs the user's yes (workspace rule 1); `updated` and `Current` are Claude's to rewrite.

## Mode 1: Map (first run, also in setup)

Propose the close team from evidence. Only read, write nothing yet.

Evidence, last 30 days unless noted:
- **Calendar:** recurring 1:1s (title "1:1", "1-1", "1on1", "One-on-One", "Name / <user>"; two attendees; recurring).
- **Chat:** DM frequency, people the user writes with most.
- **Tickets:** teams and projects the user leads, and who works in them.
- **Code:** frequent reviewers on the user's PRs, and whose PRs the user reviews.
- **Mail:** people the user writes with most (sent and received, last 90 days), and cc patterns: who copies the user in, who the user copies in.
- **Calendar beyond 1:1s:** who organises the recurring meetings the user attends, who appears in the user's team meetings, skip-level pattern (a 1:1 with someone's manager).
- **Org:** people reporting to the user (the manager and report relations; your data warehouse's people table if you have one, see Resolve).

Show the list, one person per line: `**Name:** relation guess, evidence (e.g. "weekly 1:1, 41 DMs, reviews 6 of my PRs")`. People who already have a profile are marked. Ask: "Who is close? Who is missing?" Also propose `relation`, `contract`, `team`, `areas` per person.

### Inferring the relationship

Propose `relation` (manager | report | skip-level | peer | stakeholder | freelancer | external) from every signal you have, and say how sure you are: **likely** (two or more signals agree), **possible** (one signal), **unknown** (none: ask).

- **Titles:** chat profile title, mail signature, calendar display name (e.g. "Engineering Lead", "PM").
- **Engineering org:** your data warehouse's engineering or people table if you have one (login, team, pod, role, lead flag): same team as the user, team lead, role.
- **Tickets:** lead or member of the teams the user leads.
- **Calendar:** who organises the 1:1 (a manager usually organises with their reports), team meetings the user runs, meetings with someone's manager (skip-level).
- **Mail:** cc direction (people who copy the user in on decisions are often stakeholders or a manager; people the user copies in on asks are often reports).
- **CRM:** owner team, for sales and support people only.
- **Contract:** freelancer when the workspace rules say so (e.g. invoices from that person), external when the email domain is not the company's.
- **Context:** what `context/me.md` and the person's existing profile already say.

Show one line per person: `**Name:** report (likely): team lead per warehouse, weekly 1:1 you organise, 38 chat messages, cc'd on 12 mails`. Conflicting signals are named, not resolved silently. Write only what the user confirms.

Write `close: true` (and the confirmed relation, contract, team, areas) only after the user confirms, person by person or as a list. Everyone else keeps `close: false`.

## Mode 2: Resolve identities

For every person with an empty id (close people first, then the rest). Match by email first, then full name. Ambiguous (two people called Alex, nickname only) means: ask under "Claude asks", never guess.

- **Email:** first from calendar attendees (the most reliable work address), then mail headers, then the chat profile. People outside chat (freelancers, external contacts) get their email from calendar and mail. Record the source.
- **Chat:** search users by name or email; take the chat user id (`slack_id` or the tool's equivalent), the handle and the email.
- **Tickets:** list the ticket tool's users filtered by email or name; take the user id or login (`linear` field).
- **Tasks:** the users of the workspace named in `meta/task-store.md`; take the user id (`asana` field). This is the id the task store's "Waiting on" property uses.
- **Code:** the login (`github` field). Use the code connector or the CLI; if you have a data warehouse engineering or people table with author logins and teams, it also gives `team` and who leads a team.
- **CRM owner:** only for sales and customer-success people (the CRM's owners list); the `hubspot_owner` field.

The `ids` key names come from the common tools and stand for whatever you run in that category: `slack_id` and `slack_handle` for any chat tool, `github` for code, `linear` for tickets, `asana` for tasks. A tool not covered goes in as an extra key. A key for a tool you do not use stays empty.

Write the ids into the profile and one `sources` line per id: `slack_id: "chat user search 2026-11-04"`. An id found but contradicting an existing one is not overwritten: ask under "Claude asks". Rewriting `updated` is fine; the ids themselves are a "compile" write, so show the table (name, id per tool, source) and write after the user's yes. In a scheduled run with nobody answering, write nothing and leave the table in the note.

## Mode 3: Refresh "Current"

For close people. Monthly (inside `routines/refresh.md`) and before every 1:1 (`routines/meeting-prep.md` 3a). Read-only sources, so it needs no confirmation: it rewrites only the derived "Current" section and `updated`. Use ids from the frontmatter; never search by first name.

Rewrite `## Current` in `profile.md` completely, with the date, in this shape:

```
## Current
_Refreshed YYYY-MM-DD from: chat, tickets, code, tasks, mail, calendar (name any source that failed)_
- **You owe:** unanswered messages from them, open promises, PRs or issues where they wait on the user. Deep link each.
- **They owe:** their open promises, answers the user waits for. Deep link each.
- **Tickets:** their active issues and projects.
- **Code:** their open PRs; PRs waiting on the user.
- **Threads (30 days):** shared threads, one line each, deep link.
- **Meetings:** recurring meetings with them, with next date.
```

Rules: last 30 days. Deep links as in `routines/radar.md`. Facts only, no judgement. Set `last_1on1` from the last 1:1 on the calendar. An empty line says "none found"; a failed source says so.

## Mode 4: New person

The brief's context gap class (b) (`routines/brief.md` step 4) finds someone unknown. Resolve their ids first (Mode 2 for that one person), then ask: "New person: [Name], [role], [evidence]. Add a profile?" On yes create `context/people/<slug>/profile.md` from the schema with the resolved ids and sources, `close: false`, `status: draft`. Same-first-name slug: `firstname-lastname`, or `firstname-team` when the last name is unknown, and add an alias.

## Matching people elsewhere

Other routines match by id, not by name:
- Chat authors, DM partners and mentions: `slack_id`.
- Code reviewers and authors: `github`.
- Ticket assignees and commenters: `linear`.
- Waiting on in the task store: the `asana` id (the task tool's user id).
- Mail: `email`.
Not in any profile: treat as unknown, do not guess a match; it becomes a class (b) context gap.

## Friction
When the user corrects a mapping, an id or a close decision, append to `meta/friction.md`: `- YYYY-MM-DD people: <what went wrong> -> <what they wanted>`.
