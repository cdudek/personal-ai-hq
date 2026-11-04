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

An initiative is a clear outcome, an end date, and more than one task or longer than a week. It lives only in the task store: one task in Top of mind plus one Initiative option on its tasks. Claude proposes a new one when tasks pass the test and creates it only after a yes. Closing is proposed when all its tasks are done or the end date passed.

## Ideas

Uncommitted ideas stay in `ideas/`. They become a task only when you commit to them.

## Drift

`review` checks every Friday: an area collecting misfits, a catch-all area, an initiative to open or close, a tie-break that keeps being corrected. Changes here are proposals until you say yes.
