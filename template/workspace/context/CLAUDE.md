# context/

Memory. Read by every routine. Write only after the user says yes (see top-level rule 1).

- `me.md`: role, way of working, preferences
- `goals.md`: goals and OKRs, with pointers to the source docs
- `glossary.md`: terms, abbreviations, internal names. One line each: `**term**: meaning (source, date)`. Before adding: check plurals, acronyms, casing.
- `writing-style.md`: the voice file. Every drafting routine reads it. Changes only via `review` with approval; append a dated line to its "Learned" section.
- `areas/`: `index.md` (areas, tie-break, initiative test) and one file per area. The areas of the task store live here, not in the tool.
- `places.md`: where files, repos, documents and the shared destination live. Read it before searching the disk.
- `people/<slug>/profile.md`: one high-level profile per person (ids per tool, `relation`, `close`, role, how we work, how I write to them, a derived "Current" section). Schema, privacy rules and who may change what: `routines/people.md`. Ids and `close` change only after the user's yes; "Current" is rewritten by Claude on every refresh.
- `people/<slug>/records/YYYY/MM/YYYY-MM-DD.md`: the records, one file per person per day, entries `- HH:MM [type] text · source: <link or "the user">`, types feedback-given, feedback-received, 1:1, decision, commitment, discussion, personnel. **Immutable:** a past day's file is never edited; a correction is a new entry today that names the earlier date. `[personnel]` and feedback entries come only from the user's own words and never leave the workspace. Details: `routines/people.md`, "Records".
- Initiatives and projects are not in `context/`: each has a topic folder in `research/` whose README is its memory (`research/CLAUDE.md`).

Pages are compiled from `sources/` and the inbox. Every fact links its source: `(source: [[sources/...]])` or `(<name>, YYYY-MM-DD)`.

Split a page when it passes about 800 words or covers two subjects. Create a subfolder when a folder passes about 30 files and has a clear cluster (e.g. `people/engineering/`); give the new subfolder its own CLAUDE.md.

Status `draft` means seeded by Claude and not yet confirmed by the user.
