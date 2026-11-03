# sources/

Raw material, never edited after filing. The wiki (`context/`) is compiled from it.

- `_incoming/`: drop zone. The user drops files or links here; `ingest` processes and empties it.
- `transcripts/`, `articles/`, `documents/`: filed sources, `YYYY-MM-DD-kebab-title.md` (or the original file plus a `.md` sidecar with the same name).
- Frontmatter: type source, summary, url or origin, captured, tags, compiled_into (list of `[[context/...]]` pages it fed).
- A source is "compiled" once its facts are in `context/` pages that link back to it.
