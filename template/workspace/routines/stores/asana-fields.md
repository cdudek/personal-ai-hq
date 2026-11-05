---
type: topic
summary: The shared HQ custom fields for Asana (exact names, types, options, descriptions) and how to create them once
status: current
updated: {{SETUP_DATE}}
---

# Asana: the HQ fields

One place for the field spec. Setup (`/hq:setup`, step "Create the task store"), the upgrade to 0.3.6 and the adapter's "Create the board" all point here. The eight fields below are a **prerequisite** for an Asana task store: HQ reads and writes them by id, and the pages sort on them. They are created **once per organisation** as shared library fields; every colleague's setup then only finds and reuses them through the standard Asana connector (no token).

`Area` is never a field: it follows from the task's initiative (its project description) or, without one, from the `Area:` description line.

## Check first

List the workspace's shared custom fields through the connector and look for each name below (exact, including the `HQ · ` prefix with the middle dot). Found: **validate it against the spec below before using it**: single-select fields must have every listed option (names exact; extra options are allowed), number fields must be of type number with 0 decimal places. A field with the right name but the wrong type, or without all required options (for example `HQ · Source` still on the old shorter list, `HQ · Size` without XS or XL), is **invalid and counts as not found**: writes to it would fail or be dropped. A valid field: add it to the board project and record its id and option ids in `meta/task-store.md` (`fields`). Missing or invalid: fix them first (see "Create the missing fields" and "Repair an invalid field"); setup does not go on until all eight are valid and a second check finds them. Description lines instead of fields only when the user explicitly says to skip fields.

## The fields

Options are listed in the order to create them. Every field goes into the organisation's field library (so every project and every colleague can use it).

**HQ · Priority**
- Type: single select. Options: P0, P1, P2, P3.
- Description: `Order of work: P0 now, P1 this week, P2 soon, P3 later. Set by rules or by the owner.`

**HQ · Size**
- Type: single select. Options: XS, S, M, L, XL.
- Description: `T-shirt size, a rough effort guess: XS under an hour, S half a day, M a day or two, L most of a week, XL more than a week (split it).`

**HQ · Source**
- Type: single select. Options: Slack, Mail, Meeting, Asana, Linear, GitHub, Jira, HubSpot, Google Drive, Miro, Figma, Notion, Confluence, LinkedIn, Data, Voice, Me (Me last).
- Description: `The tool the task came from. Asana = someone assigned or commented in another Asana project; GitHub = PRs, issues, reviews (GitHub Projects too); Google Drive = comments or assignments in Docs, Sheets, Slides; HubSpot = tickets, deals, mentions; Meeting = calendar events and transcripts (Meet, Demodesk, Wispr notetaker, Granola); Voice = Wispr dictation or Scratchpad; Data = warehouse or dashboard alerts; Me = own capture (self-message, typed).`

**HQ · MoSCoW**
- Type: single select. Options: Must, Should, Could, Won't.
- Description: `Scope within an initiative or the week. Must: has to happen. Should: important, not fatal if it slips. Could: only if there is room. Won't: explicitly out this cycle.`

**HQ · Impact**
- Type: number, precision 0 (whole numbers 1 to 10).
- Description: `ICE, Impact 1-10: how much finishing this moves the goal. Scored by Claude as a proposal.`

**HQ · Confidence**
- Type: number, precision 0.
- Description: `ICE, Confidence 1-10: how sure we are about the impact and the effort. Scored by Claude as a proposal.`

**HQ · Ease**
- Type: number, precision 0.
- Description: `ICE, Ease 1-10: how little effort it takes (10 = trivial). Scored by Claude as a proposal.`

**HQ · ICE**
- Type: number, precision 0.
- Description: `Impact x Confidence x Ease (1 to 1000). Computed by Claude, never typed by hand. Proposes the Priority, does not set it.`

## Create the missing fields

### By hand (works everywhere, the default)

In Asana, for each missing field, in the order above:

1. Open any project, then click **Customize** (top right), then **+ Add field**.
2. Click **Create new field**.
3. **Title:** the exact name, e.g. `HQ · MoSCoW`. (Type the middle dot as `·`.)
4. **Type:** Single-select for Priority, Size, Source, MoSCoW; Number for Impact, Confidence, Ease, ICE (set **Format** to Number and **Decimal places** to 0).
5. **Options** (single-select only): enter them in the order listed above, one per line.
6. **Description:** paste the description text above.
7. Switch **on** "Add to my organization's field library" (shown as "Add to library"). Without it the field stays local to that one project and nobody else can reuse it.
8. Click **Create field**. Repeat for the next one.

Then tell Claude "done" and it checks the library again. Only an organisation member who is allowed to add fields to the library can do this once for everyone; if you cannot, ask one colleague who can, or an admin.

### With an API token (Claude Code only, optional)

Only if the environment variable `ASANA_API_TOKEN` exists (check with `[ -n "$ASANA_API_TOKEN" ]`; never print it, never write it to a file, never pass it on a command line that is shown). Offer it as an option: "I can create the 8 fields for your whole organisation with your Asana token. Do that? [yes / I will do it by hand]". The token is never required.

After a yes, for each missing field send one `POST https://app.asana.com/api/1.0/custom_fields` with the header `Authorization: Bearer $ASANA_API_TOKEN` (read from the environment inside the command), and a JSON `data` body holding: `workspace` (the workspace gid), `name` (exact), `resource_subtype` (`enum` or `number`), `description`, `is_global_to_workspace: true` (this is the library switch), for `enum` the `enum_options` (`[{"name": "P0"}, ...]` in the listed order), for `number` `precision: 0`. Read the created field gids from the response. Report the field names created, never the token. If a call fails (no permission to add library fields: say so; any other error: one line), fall back to "By hand".

## Repair an invalid field

For each invalid field say what is wrong in one line (field, what the spec needs, what it has), then offer, in this order:
1. **Missing options (single-select):** a person who may edit the field adds them by hand (field > Edit > add option, names exactly as in the spec); or, in Claude Code with `ASANA_API_TOKEN` (never printed), one `POST https://app.asana.com/api/1.0/custom_fields/<field gid>/enum_options` with `{"data": {"name": "<option>"}}` per missing option, after a yes.
2. **Wrong type:** the type cannot be changed. A person renames the old field (for example `HQ · Source (old)`), then the field is created fresh as above.
3. **Skip:** only on the user's explicit yes. That one property becomes a description line, recorded in `meta/task-store.md` ("Field mapping": `<property> = description line`), and the other seven fields still go on the board.

Then run the check again. Never write to an invalid field.

## After creation

Check the library again through the connector. Continue only when all eight are found. Add each to the board project and record gids and option gids under `fields` in `meta/task-store.md`.
