---
type: topic
summary: The areas tasks are sorted into, the tie-break that picks one, and the initiative test
status: draft
updated: {{SETUP_DATE}}
---

# Areas

Every task carries exactly one Area. The task store holds only the field; the definitions live here, one file per area (`context/areas/<slug>.md`: definition, examples, people, recurring meetings).

## Areas

| Area | What it is | Examples |
|---|---|---|
{{AREAS_TABLE}}

## Tie-break (first match wins)

{{TIE_BREAK}}

## Initiative test

An initiative is a clear outcome, an end date, and more than one task or longer than a week. It lives only in the task store: its own container (an Asana project `🤖 <Initiative>`, a Notion page, a Monday board, a Trello card or a GitHub milestone; `routines/stores/README.md`) plus one task in Top of mind linking to it. Claude proposes a new one when tasks pass the test and creates it only after a yes: the container (its description holds outcome, end date, OKR if any, `Topic folder: <name>`, links), the Top of mind task and its topic folder (`cp -r research/_template "research/YYYY-MM-DD - Name"`, README: question, status active, started). Closing is proposed when all its tasks are done or the end date passed; after a yes the README status becomes `complete` and moving the folder to `research/_archive/` is proposed (second yes).

## Ideas

Uncommitted ideas stay in `ideas/`. They become a task only when you commit to them.

## Drift

`review` checks every Friday: an area collecting misfits, a catch-all area, an initiative to open or close, a tie-break that keeps being corrected. Changes here are proposals until you say yes.
