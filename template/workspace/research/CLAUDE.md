# research/ — documents home

Every document and piece of research for an initiative or task has one home: a topic folder here. The task store, the topic README, the views and memory link to it. It lives inside the workspace, so Claude Code and Cowork both see it.

## Structure

```
research/
├── _archive/                 # complete or parked topics
├── _template/                # skeleton: cp -r to start a topic
├── YYYY-MM-DD - Topic Name/  # one folder per initiative or topic
│   ├── README.md             # CURRENT DOCUMENT callout, status, question, decisions, latest documents, shared links, earlier work
│   ├── notes.md              # running log of observations and links
│   ├── working/              # background work: analysis, drafts, reference, research material
│   ├── output/               # finished artifacts others read
│   │   └── _archive/         # previous versions (append-only)
│   └── data/                 # raw and processed data (gitignored)
└── CLAUDE.md
```

## Conventions

- **One initiative = one topic folder.** The README is the memory for that initiative: status, decisions, latest documents, shared links, earlier work. There are no separate project pages in `context/`.
- **Flat, dated names.** `YYYY-MM-DD - Topic Name`: day the topic started, ` - `, relaxed Title Case with real spaces, acronyms uppercase. No nesting. Quote the name in shell commands.
- **Status** in the README: `active`, `complete` or `parked`. Complete or parked: move the whole folder to `_archive/` (keeps its date prefix) after the user's yes.
- **Output vs working.** `output/` holds finished artifacts someone other than the user reads. `working/` holds everything else. Unsure: `working/`.
- **File names:** `YYYY-MM-DD-descriptive-name.md` (kebab-case, optionally starting with `rfc-`, `adr-`, `memo-`, `spike-`). The date is creation or last major update.
- **Versioning:** `output/` holds current versions only. On a significant update move the old version to `output/_archive/` (original name), then update the main file with the new date. Archive is append-only; typo fixes are not archived.
- **Current-document pointer (mandatory):** every README opens with the `📍 CURRENT DOCUMENT` callout (see `_template/README.md`) pointing at the artifact to read; update it whenever the artifact changes. Several current artifacts: one line each.
- **Output frontmatter (mandatory)** on every file in `output/`:
  ```yaml
  ---
  status: current      # current | superseded | draft
  version: 1           # bump on every meaningful content change
  last_updated: YYYY-MM-DD
  audience: who is this for
  supersedes: path/to/previous.md   # optional
  ---
  ```
  Files in `output/_archive/` have `status: superseded`.
- **Data is gitignored** (`research/*/data/`); scripts that create it must be reproducible.
- **Research material** for an initiative (articles, transcripts, notes) goes to that topic's `working/`; general sources stay in `sources/`.
- **Writing style** for finished documents: `context/writing-style.md`.

## Open and close an initiative (after a yes)

- **Open:** `cp -r "research/_template" "research/YYYY-MM-DD - Name"`, fill the README (title, question, `Status: active`, `Started`), link the folder name in the Top of mind task (`Topic folder: <name>`).
- **Close:** README status `complete`, then propose moving the folder to `_archive/`; move it after a second yes.

## Shared versions

A document others must read leaves this folder as a shared URL, never as a path. Where shared versions go is in `context/places.md` ("Shared versions": Google Drive, Notion, Confluence or none); push the full content there, not a pointer. Add the URL under "Shared links" in the README and in the task description. With no shared destination, say "no shared version yet".

**Never put a local path into a shared place** (task tool, ticket tool, chat, mail, shared docs, PR text). Link the shared URL; if there is none yet, say "no shared version yet" or create it first (after a yes). Before saving anything shared, grep it for `~/`, absolute home paths, `research/` and `working/`.

## Links to this folder

- Task store: Top of mind initiative tasks carry `Topic folder: <folder name>` (a name, not a path) plus shared links; a task's description or link holds the shared URL when one exists.
- Views: a task's `docs[]` shows as "Documents" in the panel (`views/CLAUDE.md`).
- Index: `scripts/build_index.py` skips this folder; the READMEs are the index.
