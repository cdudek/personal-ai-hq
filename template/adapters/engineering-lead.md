---
role: engineering-lead
summary: Defaults for engineering leads - code and tickets first, review queues and team health
---

# Adapter: engineering lead

## Tool defaults
Code (GitHub or GitLab, `gh` CLI as fallback), tickets (Linear or Jira), chat (Slack or Teams), mail and calendar, docs (Notion, Confluence or Google Docs), incidents and errors (Sentry, PagerDuty), meeting notes.

## Routine emphasis
- `radar`: code section on top. Own PRs, review requests, failed checks, PRs waiting for a first review.
- `weekly`: switch on the team code status block (old PRs, review wait time, trend) as a pattern view, not a per-person list. Add incidents and on-call handover as recurring inputs.
- `brief`: blockers for the team before anything else.
- `meeting-prep`: 1:1s matter most; use the 1:1 block for every direct report.
- `review`: learn the style of PR comments, design docs and incident notes.

## Glossary seeds
- **PR**: pull request
- **RFC**: request for comments, a design document
- **ADR**: architecture decision record
- **SLO**: service level objective
- **DORA**: four delivery metrics (deployment frequency, lead time, change failure rate, time to restore)
- **Trunk-based**: merging small changes to the main branch often

## Typical meeting types
Daily standup, team 1:1, sprint planning, retro, architecture review, incident review, hiring debrief, roadmap sync with product.

## Default areas (setup proposes, you confirm)
- **Delivery:** how we build and ship. Roadmap delivery, quality, reviews, releases.
- **Platform:** infra, data, tooling, security, on-call and incidents.
- **Product:** the what and why with product partners. Roadmap input, estimates, trade-offs.
- **Team:** people. Hiring, 1:1s, feedback, performance, org design.
- **Company:** up and across. Management, budget, other units.
- **Admin:** contracts, invoices, access, expenses.
- **Me:** own growth and outside presence.

Example tie-break: 1 about a specific person: Team. 2 for someone outside engineering: Company. 3 running systems or incidents: Platform. 4 building and shipping: Delivery. 5 what or why: Product. 6 pure bureaucracy: Admin. 7 for yourself: Me.
