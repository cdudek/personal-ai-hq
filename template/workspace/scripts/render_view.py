#!/usr/bin/env python3
"""Render a daily, weekly or review (Friday improvement) view: data JSON -> one self-contained HTML file (works offline).

Usage: python3 scripts/render_view.py views/data/daily-2026-11-04.json
Writes views/<kind>-<date>.html and views/<kind>.html (latest), then you can `open` it.
"""
import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "views"
TEMPLATE = OUT / "template.html"
# shared CSS/JS for both views, plus Alpine.js vendored so the page needs no network or server
PARTS = {"__CSS__": OUT / "app.css", "__APP__": OUT / "app.js", "__ALPINE__": OUT / "vendor" / "alpine-3.14.1.min.js"}


FONTS = [("Inter", 400, "inter-latin-400-normal"), ("Inter", 500, "inter-latin-500-normal"), ("Inter", 600, "inter-latin-600-normal"),
         ("Inter", 700, "inter-latin-700-normal"), ("JetBrains Mono", 400, "jetbrains-mono-latin-400-normal"),
         ("JetBrains Mono", 500, "jetbrains-mono-latin-500-normal")]


def fonts_css() -> str:
    # Latin woff2 from @fontsource 5.0.18 (OFL), inlined so the page looks right offline
    out = []
    for family, weight, name in FONTS:
        f = OUT / "vendor" / "fonts" / f"{name}.woff2"
        if f.exists():
            data = base64.b64encode(f.read_bytes()).decode()
            out.append(f'@font-face{{font-family:"{family}";font-weight:{weight};font-style:normal;font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}')
    return "\n".join(out) + "\n"


def validate(data: dict) -> tuple[str, str]:
    kind = data.get("kind")
    if kind not in ("daily", "weekly", "review"):
        raise ValueError("kind must be daily, weekly or review")
    date = str(data.get("date", ""))
    if not re.fullmatch(r"[A-Za-z0-9-]{1,32}", date):
        raise ValueError("date must be like 2026-11-04 or 2026-W45")
    return kind, date


# source -> (icon file in views/icons, brand colour for monochrome SVGs)
BRANDS = {
    "slack": ("slack.svg", "#4A154B"), "gmail": ("gmail.svg", "#EA4335"),
    "calendar": ("googlecalendar.svg", "#4285F4"), "meet": ("googlemeet.svg", "#00897B"),
    "linear": ("linear.svg", "#5E6AD2"), "github": ("github.svg", "#181717"),
    "asana": ("asana.svg", "#F06A6A"), "miro": ("miro.svg", "#050038"),
    "hubspot": ("hubspot.svg", "#FF7A59"), "posthog": ("posthog.svg", "#000000"),
    "gdocs": ("googledocs.svg", "#4285F4"),
    "demodesk": ("demodesk.png", None), "wispr": ("wisprflow.png", None),
}


def icons() -> dict:
    out = {}
    for source, (name, colour) in BRANDS.items():
        f = OUT / "icons" / name
        if not f.exists():
            continue
        if f.suffix == ".svg":
            svg = f.read_text(encoding="utf-8").replace("<svg ", f'<svg fill="{colour}" ', 1)
            out[source] = "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
        else:
            out[source] = "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode()
    # items about the task board show the task tool's logo, not a "Boa" abbreviation
    m = re.search(r"^store:\s*([a-z-]+)", (OUT.parent / "meta" / "task-store.md").read_text(encoding="utf-8"), re.M) \
        if (OUT.parent / "meta" / "task-store.md").exists() else None
    store = {"github-projects": "github"}.get(m.group(1), m.group(1)) if m else ""
    if store in out:
        out.setdefault("board", out[store])
    return out


def safe_json(obj) -> str:
    # data comes partly from Slack, mail and Linear text: make <, >, & unrepresentable in raw markup
    return (json.dumps(obj, ensure_ascii=False)
            .replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def render(data: dict) -> str:
    validate(data)
    html = TEMPLATE.read_text(encoding="utf-8")
    for marker, f in PARTS.items():
        code = f.read_text(encoding="utf-8")
        if "</script" in code.lower() or "</style" in code.lower():
            raise ValueError(f"{f.name} would close its own tag")
        html = html.replace(marker, (fonts_css() if marker == "__CSS__" else "") + code, 1)
    # data last, so text inside it can never be taken for a marker
    return html.replace("__ICONS__", safe_json(icons()), 1).replace("__DATA__", safe_json(data), 1)


# sources whose items always have their own URL; anything else may come without a link
LINKED = {"github", "linear", "slack", "gmail", "asana", "calendar", "meet", "demodesk", "miro", "hubspot", "gdocs"}
# list pages and inbox roots: a link, but not to the specific item
GENERIC = [r"github\.com/pulls", r"/pulls\?", r"/issues\?", r"mail\.google\.com/mail/[^#]*(#(inbox|all|sent))?/?$",
           r"app\.asana\.com/0/(my-tasks|home|inbox)", r"slack\.com/archives/[A-Z0-9]+/?$", r"slack\.com/client",
           r"calendar\.google\.com/?$", r"linear\.app/[^/]+/?$", r"linear\.app/[^/]+/(inbox|my-issues)"]


def link_problems(data: dict) -> list[str]:
    items = [i for s in data.get("sections", []) for i in s.get("items", [])]
    items += [t for lst in (data.get("board") or {}).values() for t in lst]
    items += data.get("meetings", []) + data.get("top_of_mind", [])
    items += ((data.get("linear") or {}).get("stale") or {}).get("items", [])  # weekly: stale issues carry source linear
    items = [dict(i, source=i.get("source", "linear")) for i in items]
    out = []
    for it in items:
        link = it.get("link") or ""
        if not link and it.get("source") in LINKED and it.get("source") not in ("calendar", "meet") or \
                (it.get("source") in ("calendar", "meet") and not link and not it.get("links")):
            out.append(f"no link: [{it.get('source')}] {it.get('title', '')[:70]}")
        elif link and any(re.search(g, link) for g in GENERIC):
            out.append(f"not a deep link: [{it.get('source')}] {it.get('title', '')[:70]} -> {link[:80]}")
    return out


# sections whose items are things to act on: priority and area are required there (views/CLAUDE.md, Labels)
LABELLED = {"needs", "replies", "waiting", "proposals"}
REVIEW_KEYS = ("style", "glossary", "fixes", "tips", "routines_new")


def label_problems(data: dict) -> list[str]:
    board = [t for lst in (data.get("board") or {}).values() for t in lst]
    by_link = {k: t for t in board for k in (t.get("link"), t.get("url")) if k}
    out = []

    def check(where: str, it: dict, need_priority: bool = True) -> None:
        t = by_link.get(it.get("link") or "") or {}  # an item on the board inherits its task's labels
        miss = [n for n, need in (("priority", need_priority), ("area", True)) if need and not (it.get(n) or t.get(n))]
        if miss:
            name = it.get("title") or it.get("term") or it.get("issue") or it.get("tip") or it.get("channel") or "?"
            out.append(f"{where}: {' and '.join(miss)} missing: {str(name)[:70]}")

    for s in data.get("sections", []):
        if s.get("id") in LABELLED:
            for it in s.get("items", []):
                check(s["id"], it)
    for lst, tasks in (data.get("board") or {}).items():
        for t in tasks:
            check("board " + lst, t)
    for p in data.get("proposals", []):
        check("proposal", p)
    for t in data.get("top_of_mind", []):
        check("top of mind", t, need_priority=False)
    for k in REVIEW_KEYS:
        for it in data.get(k, []):
            check("review " + k, it)
    return out


def main(path: str) -> None:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    kind, date = validate(data)
    html = render(data)
    dated = OUT / f"{kind}-{date}.html"
    if dated.resolve().parent != OUT.resolve():
        raise ValueError("output path escapes views/")
    dated.write_text(html, encoding="utf-8")
    if date != "sample":  # the sample must never replace the real latest view
        (OUT / f"{kind}.html").write_text(html, encoding="utf-8")
    print(dated)
    if lp := label_problems(data):
        print(f"LABEL CHECK: {len(lp)} item(s) missing priority or area (the page shows a dashed placeholder). Fill them from the task store or the rules (views/CLAUDE.md, Labels) and render again:")
        print("\n".join("  - " + p for p in lp))
    if problems := link_problems(data):
        print(f"LINK CHECK: {len(problems)} item(s) without a deep link to the specific thing. Fix the data and render again:")
        print("\n".join("  - " + p for p in problems))


def self_check() -> None:
    html = render({"kind": "daily", "date": "x", "title": "</script><!--<b>&"})
    if "</script><!--" in html.split('id="data"')[1].split("</script>")[0]:
        raise RuntimeError("escaping failed")
    for bad in ({"kind": "x", "date": "1"}, {"kind": "daily", "date": "../../etc"}):
        try:
            validate(bad)
        except ValueError:
            continue
        raise RuntimeError(f"validation accepted {bad}")


if __name__ == "__main__":
    self_check()
    main(sys.argv[1])
