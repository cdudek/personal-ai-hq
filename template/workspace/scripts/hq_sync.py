#!/usr/bin/env python3
"""Keep a workspace's system files in step with the plugin template. Never touches user data.

  hq_sync.py manifest <workspace>                  record hashes of the system files as installed
  hq_sync.py plan <template> <workspace>           classify every system file
  hq_sync.py apply <template> <workspace> <rel>... copy those files (rel = "safe" copies all safe/new ones)

plan prints one "<status> <path>" per line: new | safe | edited | same | obsolete.
  safe = the user did not edit it, overwrite. edited = the user changed it, show the diff and ask.
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

VIEWS = ["template.html", "app.css", "app.js", "CLAUDE.md", "DESIGN.md", "README.md", "styleguide.template.html"]
MANIFEST = ".hq-manifest.json"


def system_files(root: Path) -> set[str]:
    out = {str(p.relative_to(root)) for d in ("routines", "scripts", "views/vendor", "views/icons")
           for p in (root / d).rglob("*") if p.is_file() and p.name != "index.md" and "__pycache__" not in p.parts}  # index.md is generated
    out |= {f"views/{v}" for v in VIEWS if (root / "views" / v).exists()}
    out |= {str(p.relative_to(root)) for p in root.glob("*/CLAUDE.md")}  # per-folder rule files, not the root one
    if (root / "SYSTEM.md").exists():
        out.add("SYSTEM.md")
    return out


def norm(b: bytes) -> bytes:  # the setup date is filled in at install time, so ignore it when comparing
    return re.sub(rb"(?m)^updated: .*$", b"updated: X", b.replace(b"{{SETUP_DATE}}", b"X"))


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(ws: Path) -> dict:
    f = ws / MANIFEST
    return json.loads(f.read_text()) if f.exists() else {}


def save(ws: Path, m: dict) -> None:
    (ws / MANIFEST).write_text(json.dumps(m, indent=1, sort_keys=True) + "\n")


def plan(tpl: Path, ws: Path) -> list[tuple[str, str]]:
    m, res = load(ws), []
    for rel in sorted(system_files(tpl)):
        t, w = tpl / rel, ws / rel
        if not w.exists():
            res.append(("new", rel))
        elif norm(w.read_bytes()) == norm(t.read_bytes()):
            res.append(("same", rel))
        elif m.get(rel) == digest(w):
            res.append(("safe", rel))
        else:
            res.append(("edited", rel))
    res += [("obsolete", r) for r in sorted(set(m) - system_files(tpl))]
    return res


def apply(tpl: Path, ws: Path, rels: list[str]) -> None:
    status = {r: s for s, r in plan(tpl, ws)}
    chosen = [r for r, s in status.items() if s in ("safe", "new")] if rels == ["safe"] else rels
    m = load(ws)
    for rel in chosen:
        if rel not in system_files(tpl):
            raise SystemExit(f"not a system file: {rel}")
        dst = ws / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes((tpl / rel).read_bytes().replace(b"{{SETUP_DATE}}", date.today().isoformat().encode()))
        m[rel] = digest(dst)
        print("updated", rel)
    save(ws, m)


if __name__ == "__main__":
    cmd, args = sys.argv[1], [Path(a) for a in sys.argv[2:]]
    if cmd == "manifest":
        save(args[0], {r: digest(args[0] / r) for r in system_files(args[0])})
    elif cmd == "plan":
        for s, r in plan(args[0], args[1]):
            print(s, r)
    elif cmd == "apply":
        apply(args[0], args[1], [str(a) for a in args[2:]])
    else:
        raise SystemExit(__doc__)
