# Brief design language

The daily and weekly views share one small design language. Goal: every element tells you what it is by its shape, before you read it. The sample pages (`/hq:demo`) show every atom.

## Principles

1. **One shape per meaning.** Priority, status, area, initiative, signal and size each have their own shape. No pills. If two things look alike, they mean the same.
2. **Colour means attention.** Red: act now (blocking, overdue, P0). Amber: decide or due soon. Green: done. Everything else is ink on paper.
3. **Indigo means Claude.** Only for buttons that copy a prompt (spark icon), Claude's questions, and staged board changes waiting for Claude. Links are never indigo.
4. **A rule means quoted.** Words from Slack, mail, Linear sit behind a grey rule in Inter. Never Claude's own summaries. No serif anywhere.
5. **Mono means data.** Times, counts, sizes, priorities, eyebrow labels.
6. **Calm by default.** Hairlines, no shadows except overlays. Row actions appear on hover; the panel holds the details.

## Tokens (`app.css`, section 1)

| Token | Role |
|---|---|
| `--paper`, `--surface`, `--sunken` | page, cards and tables, inset areas (panel controls) |
| `--line`, `--line-2` | hairline, stronger line (quote rule, hover) |
| `--ink`, `--ink-2`, `--ink-3` | primary text, secondary text, labels and meta |
| `--red`, `--amber`, `--green` | signals only |
| `--claude` | Claude only |
| `--sans`, `--mono` | Inter (interface, quotes), JetBrains Mono (data). Latin subsets are embedded by `render_view.py`, so the page looks the same offline |
| `--d-*`, `--t-*` | area tints (Product, Engineering, Team, Company, Admin, Me), Linear team keys |
| `--r-sm` 4, `--r` 8, `--r-lg` 12 | labels, buttons, cards |

Light and dark follow the system setting. Components use tokens only, never hex values.

## Type roles

| Role | Style | Use for |
|---|---|---|
| Title (h1) | 34 / 650 | the date |
| Headline | 17 ink-2 | the one-sentence summary |
| Section (h2) | 17 / 620 + mono count | section names |
| Eyebrow | mono 11 caps ink-3 | zone label, kicker, panel block headings |
| Item title | 15.5 / 620 | card and meeting titles |
| Meta | 12.5 ink-3 | where, who |
| Rule | 13 ink-3 | the one line under a section heading |

## Atoms

| Atom | Shape | Means | Never for |
|---|---|---|---|
| Signal | coloured dot + caps text | why an item wants attention (Blocking, Decision, Due Thu, Deep prep) | status or category |
| Status | circle glyph + text: hollow, dashed, green check, dotted | where a task stands (open, waiting, done, unclear) | urgency |
| Priority | mono badge, soft ladder: P0 red tint + outline, P1 grey fill, P2 outline, P3 plain | task priority | anything else |
| Area | muted tint per area + square swatch (text colour, 10 % fill, 28 % border) | which responsibility it belongs to | status |
| Initiative | plain text with a small diamond, no box | which initiative it belongs to | area, status |
| Team key | `WEB-638`, key bold in the team colour | which Linear team owns it | urgency, area |
| Claude suggests | square indigo block, 10 px square before the label | Claude's suggestion, with Decide differently next to Accept | facts |
| Size | plain mono | effort | |
| Quote | Inter with left rule | someone else's words | Claude's own summaries |
| Next | "NEXT" eyebrow + text | the one step the user takes | |

## Buttons

- **Claude button** (indigo, copy glyph): copies a prompt for Claude. Filled for the main action of a region, tinted for row-level actions. After a click: dashed indigo border and "Copied. Paste in Claude" for 4 s, never green; Confirmed (green) only when the next brief shows the change.
- **Quiet button** (outlined): everything else (Update brief, Close, Undo, Move, Drop, links in the panel).
- **External link**: ink text with an arrow, underline on hover. Opens the source.

## Zones

Every section belongs to one zone. The zone sets the eyebrow and the look.

| Zone | Sections | Look |
|---|---|---|
| Context | Top of mind | light outlined cards |
| Act | Needs me, team PRs | one raised card per item, red edge when blocking |
| Plan | This week, Inbox, proposals | table on a surface |
| Read | insights, Linear, drift | cards in one container |
| Recap | Yesterday's meetings, finished | no container, smaller, one-line quotes |
| Time | Today, This week (meetings) | timeline in the right rail; current meeting has a filled dot |
| Claude | Claude needs your answer | indigo tinted card |

Unknown section ids fall back to Plan (boards) or Read (cards). A new section gets an entry in `ORDER` (its place) and `EYEBROW` (its zone label) in `app.js`.

## Adding something new

1. Does an existing atom already mean this? Use it.
2. If not, give it a shape no other atom has, add it to this file.
3. Never add a new colour. If it needs attention, it is a signal.

Times show in 12h format on the page; the data keeps `HH:MM`.

## Atom row

Priority, area, initiative, topic, always in this order under the title of anything you can act on (initiative and topic only when there is one). Missing priority or area shows a dashed placeholder, never nothing. Area colours are one list (`--d-1` to `--d-11`), the same on every page.

## Two-minute rules

- Page order (daily): Start here + Next meeting, Needs attention, This week, Replies and reviews, Waiting on others, Inbox, Context (Top of mind), Yesterday, Claude asks. Weekly: Last week, Capacity, Start here, Plan this week, Top of mind, Meetings, Linear, Product insights, Team PRs.
- Section limits with "Show N more": Needs attention 5 (urgent never hidden), Replies and reviews 8, Waiting 5, Inbox 5, Top of mind 3.
- Buttons: the primary action is the right-most; links ("Open in GitHub") sit left of the buttons. Phone: hit areas 44 px, row buttons become icon-only.
- Failure states: source failed (amber line in the nav and rail), copy failed (prompt shown selected), pending edits (dock: pending, copied, updated).
- No shadows except overlays (panel, dock, toast). Dark mode: system setting or the Dark button.

Review page (Friday): zone Plan/Improve, eyebrow "IMPROVE". Each proposal is one card: facts in ink, the proposal itself in a "Claude suggests" block, then Not now / Adjust / Adopt (pressed = ink fill; answered cards get an indigo tint, skipped ones fade). One "Send to Claude" sends only decided lines and follows the plan action cycle (pending, copied, decisions changed). Plan vs actual uses plain numbers and one mono bar per source of unplanned work.

Not built from the PDF: the Linear team-colour charts (closed by team / by project bars, stale analysis cards), and the Product insights deal charts (pages 14 to 15 of the PDF).
