---
type: topic
summary: Monthly - context refresh, lint, reorganise
status: draft
updated: {{SETUP_DATE}}
---

# Routine: refresh (first Monday of the month)

Proposals first, apply after a yes. Every change is logged in `log.md`.

## 1. Context refresh
- Read the last 4 weeks of `daily/` and `weekly/` notes and the decisions.
- Propose updates to `goals.md`, the initiative topic READMEs in `research/`, `people/` (profile summaries) and the glossary: what changed, what is done, what is new.
- Move pages that have been in `draft` for 30+ days to `current` after the user confirms, or delete them.

## 1b. People
Run `routines/people.md`: Refresh "Current" for every `close: true` profile, then Resolve identities for people with empty ids. Propose a new close team member when the Map evidence (recurring 1:1, DM frequency) shows one; `close` changes only after the user's yes.

Profile summaries: read each close person's records of the last 4 weeks and propose updates to Role, Personality and How we work together in `profile.md` as exact lines; write after the user's yes. Records are never edited or summarised away. Personnel and feedback entries inform the proposal for the user only; the proposed wording is theirs to give.

## 2. Lint
List:
- contradictions between pages
- people not updated in 90 days (profile `updated` and newest record)
- close people with a missing id, an id without a `sources` entry, or a "Current" older than 35 days
- orphan pages (no links in or out)
- broken `[[links]]`
- `sources/` items never compiled
- files without `summary:`
- a past day's record or drafts file changed after its day (check `git log`); only `outcome:` lines may be appended to old drafts

## 2b. Documents home lint
For every topic folder in `research/` (not `_template`):
- README opens with the CURRENT DOCUMENT callout and the file it points at exists
- README status is `active`, `complete` or `parked`; a complete or parked folder outside `_archive/` is proposed for moving (after a yes)
- every file in `output/` has the frontmatter from `research/CLAUDE.md` (status, version, last_updated, audience)
- every open initiative in the task store has a topic folder, and its Top of mind task carries `Topic folder: <name>`; folder names in tasks still exist (renamed or archived: update)
- README "Shared links" hold no local path
Findings are proposals; change only after a yes.

## 3. Reorganise
- Split pages over about 800 words or with 2 subjects.
- Merge duplicates.
- Create a subfolder, with its own CLAUDE.md, when a folder passes about 30 files and has a clear cluster.
- Promote a subject named in 3+ pages to its own page.
- Move stale pages to `_archive/` in their folder.
- Update every `[[link]]` that a move touches (grep).

## 4. Close
Build the indexes, append to `log.md`, commit.
