#!/usr/bin/env python3
"""Render a learning-narrative unit dir to docs/<unit_id>/index.html.

Source of truth remains markdown + YAML. Generated HTML is a Pages artifact.

Usage:
  python tools/render_unit.py examples/secplus-ports-helpdesk
  python tools/render_unit.py examples/secplus-auth-helpdesk

Requires PyYAML (see Setup in AGENTS.md: python3 -m venv .venv).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

from _unit_page_template import render_html

try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML is required. Try:\n"
        "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt\n"
        "then: .venv/bin/python tools/render_unit.py <unit_dir>"
    )

KIT_ROOT = Path(__file__).resolve().parent.parent
MARK_RE = re.compile(r"\[\[([a-z0-9_]+)\|([^\]]+)\]\]")


def load_glossary(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    terms = {}
    for t in data["terms"]:
        terms[t["id"]] = {
            "id": t["id"],
            "title": t["title"],
            "definition": t.get("definition", ""),
            "context": t.get("context"),
            "tier": t.get("tier", "exam"),
            "tags": t.get("tags") or [],
            "refs": t.get("refs") or [],
        }
    return data, terms


def escape_text(s: str) -> str:
    return html.escape(s, quote=False)


def escape_inline(s: str) -> str:
    """Escape HTML then apply light inline md: *em* and `code`."""
    s = escape_text(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def inline_md(text: str, terms: dict, used_ids: list) -> str:
    """Convert inline markdown + [[id|text]] marks; escape plain text."""
    parts = []
    pos = 0
    for m in MARK_RE.finditer(text):
        if m.start() > pos:
            parts.append(escape_inline(text[pos : m.start()]))
        tid = m.group(1)
        surface = m.group(2)
        used_ids.append(tid)
        if tid not in terms:
            raise SystemExit(f"Unknown glossary id in narrative: {tid!r}")
        tier = terms[tid]["tier"]
        parts.append(
            f'<span class="term {tier}" data-term="{html.escape(tid)}" '
            f'data-tier="{html.escape(tier)}">{escape_text(surface)}</span>'
        )
        pos = m.end()
    if pos < len(text):
        parts.append(escape_inline(text[pos:]))
    return "".join(parts)


KNOWN_FIELDS = {
    "caption",
    "title",
    "kind",
    "id",
    "priority",
    "status",
    "queue",
    "from",
    "requester",
    "host",
    "opened",
    "subject",
    "chrome",
    "url",
    "heading",
    "actions",
    "error",
    "issued_to",
    "issued_by",
    "valid",
    "product",
    "severity",
    "process",
    "user",
    "time",
    "label",
    "value",
    "note",
}


def parse_fields(block: str) -> tuple[dict[str, str], str]:
    """Pull leading known key: value lines; leftover is the body.

    Only keys in KNOWN_FIELDS count, so console output like
    `FileSystemLabel : CLIENT_DECK` or `https://…` stays in the body.
    """
    fields: dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        if raw.strip() == "---":
            i += 1
            break
        m = re.match(r"^([A-Za-z][A-Za-z0-9_]*)\s*:\s*(.*)$", raw)
        if m and m.group(1).lower() in KNOWN_FIELDS:
            fields[m.group(1).lower()] = m.group(2).strip()
            i += 1
            continue
        break
    return fields, "\n".join(lines[i:]).strip("\n")


def _caption(fields: dict[str, str], fallback: str) -> str:
    return fields.get("caption") or fields.get("title") or fallback


def render_ticket(fields: dict[str, str], terms: dict, used_ids: list) -> str:
    tid = fields.get("id", "")
    pri = fields.get("priority", "")
    status = fields.get("status", "")
    subject = fields.get("subject", "")
    pri_class = re.sub(r"[^a-z]+", "", pri.lower()) or "med"
    rows = []
    for key in ("queue", "from", "requester", "host", "opened"):
        if fields.get(key):
            rows.append(
                f"<div><dt>{html.escape(key)}</dt>"
                f"<dd>{inline_md(fields[key], terms, used_ids)}</dd></div>"
            )
    return (
        f'<figure class="artifact ticket">'
        f'<figcaption>Help desk ticket</figcaption>'
        f'<div class="ticket-chrome">'
        f'<div class="ticket-bar">'
        f'<span class="ticket-id">{html.escape(tid)}</span>'
        f'<span class="pri {html.escape(pri_class)}">{html.escape(pri)}</span>'
        f'<span class="ticket-status">{html.escape(status)}</span>'
        f"</div>"
        f'<div class="ticket-subject">{inline_md(subject, terms, used_ids)}</div>'
        f'<dl class="ticket-meta">{"".join(rows)}</dl>'
        f"</div></figure>"
    )


def render_console(fields: dict[str, str], body: str, terms: dict, used_ids: list) -> str:
    caption = _caption(fields, "Console")
    out_lines = []
    for line in body.splitlines():
        cls = "out"
        stripped = line.lstrip()
        if (
            stripped.startswith(("$ ", "PS ", ">>> "))
            or stripped.startswith("PS C:")
            or re.match(r"^[A-Za-z]:\\", stripped)
        ):
            cls = "cmd"
        elif stripped.startswith("#"):
            cls = "cmt"
        out_lines.append(f'<span class="{cls}">{inline_md(line, terms, used_ids)}</span>')
    body_html = "\n".join(out_lines) + ("\n" if out_lines else "")
    return (
        f'<figure class="artifact console">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        f'<pre class="console-body">{body_html}</pre>'
        f"</figure>"
    )


def render_gui(fields: dict[str, str], body: str, terms: dict, used_ids: list) -> str:
    kind = (fields.get("kind") or "window").replace("_", "-")
    chrome = fields.get("chrome") or fields.get("url") or "Window"
    heading = fields.get("heading") or fields.get("title") or ""
    actions = [a.strip() for a in fields.get("actions", "").split("|") if a.strip()]
    extra = []
    for key, label in (
        ("error", "Error"),
        ("issued_to", "Issued to"),
        ("issued_by", "Issued by"),
        ("valid", "Validity"),
        ("status", "Status"),
    ):
        if fields.get(key):
            extra.append(
                f'<div class="gui-row"><span>{html.escape(label)}</span>'
                f"<strong>{inline_md(fields[key], terms, used_ids)}</strong></div>"
            )
    action_html = "".join(
        f'<button type="button" tabindex="-1">{html.escape(a)}</button>' for a in actions
    )
    body_html = f"<p>{inline_md(body, terms, used_ids)}</p>" if body else ""
    return (
        f'<figure class="artifact gui kind-{html.escape(kind)}">'
        f'<figcaption>On screen</figcaption>'
        f'<div class="gui-window">'
        f'<div class="gui-chrome">{html.escape(chrome)}</div>'
        f'<div class="gui-body">'
        f'<div class="gui-icon" aria-hidden="true"></div>'
        f'<div class="gui-copy">'
        f'<h3>{inline_md(heading, terms, used_ids)}</h3>'
        f"{body_html}{''.join(extra)}"
        f"</div></div>"
        f'<div class="gui-actions">{action_html}</div>'
        f"</div></figure>"
    )


def render_alert(fields: dict[str, str], body: str, terms: dict, used_ids: list) -> str:
    sev = fields.get("severity", "High")
    product = fields.get("product", "EDR")
    title = fields.get("heading") or fields.get("title") or "Alert"
    rows = []
    for key in ("host", "user", "process", "time"):
        if fields.get(key):
            rows.append(
                f"<div><dt>{html.escape(key)}</dt>"
                f"<dd>{inline_md(fields[key], terms, used_ids)}</dd></div>"
            )
    body_html = f"<p>{inline_md(body, terms, used_ids)}</p>" if body else ""
    return (
        f'<figure class="artifact alert">'
        f"<figcaption>{html.escape(product)} alert</figcaption>"
        f'<div class="alert-chrome">'
        f'<div class="alert-bar">'
        f'<span class="sev {html.escape(sev.lower())}">{html.escape(sev)}</span>'
        f'<span class="alert-product">{html.escape(product)}</span>'
        f"</div>"
        f'<div class="alert-title">{inline_md(title, terms, used_ids)}</div>'
        f'<dl class="alert-meta">{"".join(rows)}</dl>'
        f"{body_html}"
        f"</div></figure>"
    )


def render_tree(fields: dict[str, str], body: str, terms: dict, used_ids: list) -> str:
    caption = _caption(fields, "Process tree")
    items = []
    for line in body.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        depth = indent // 2
        items.append(
            f'<li class="d{depth}" style="--d:{depth}">{inline_md(line.strip(), terms, used_ids)}</li>'
        )
    return (
        f'<figure class="artifact tree">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        f'<ol class="proc-tree">{"".join(items)}</ol>'
        f"</figure>"
    )


def render_chain(fields: dict[str, str], body: str, terms: dict, used_ids: list) -> str:
    caption = _caption(fields, "Certificate chain")
    items = []
    for line in body.splitlines():
        raw = line.strip()
        if raw.startswith("- "):
            raw = raw[2:]
        if not raw:
            continue
        parts = [p.strip() for p in raw.split("|")]
        name = parts[0] if parts else raw
        state = parts[1].lower() if len(parts) > 1 else "ok"
        note = parts[2] if len(parts) > 2 else ""
        state_cls = re.sub(r"[^a-z]+", "", state) or "ok"
        note_html = f'<span class="chain-note">{inline_md(note, terms, used_ids)}</span>' if note else ""
        items.append(
            f'<li class="{html.escape(state_cls)}">'
            f'<span class="chain-name">{inline_md(name, terms, used_ids)}</span>'
            f'<span class="chain-state">{html.escape(state)}</span>'
            f"{note_html}</li>"
        )
    return (
        f'<figure class="artifact chain">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        f'<ol class="cert-chain">{"".join(items)}</ol>'
        f"</figure>"
    )


def render_meter(fields: dict[str, str], terms: dict, used_ids: list) -> str:
    caption = _caption(fields, "Meter")
    label = fields.get("label", "")
    try:
        value = max(0, min(100, int(re.sub(r"[^\d]", "", fields.get("value", "0") or "0") or "0")))
    except ValueError:
        value = 0
    note = fields.get("note", "")
    return (
        f'<figure class="artifact meter">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        f'<div class="meter-row">'
        f'<span class="meter-label">{inline_md(label, terms, used_ids)}</span>'
        f'<span class="meter-track"><span class="meter-fill" style="width:{value}%"></span></span>'
        f'<span class="meter-val">{value}%</span>'
        f"</div>"
        f'<p class="meter-note">{inline_md(note, terms, used_ids)}</p>'
        f"</figure>"
    )


def render_table(rows: list[list[str]], terms: dict, used_ids: list, caption: str = "") -> str:
    if not rows:
        return ""
    header, body = rows[0], rows[1:]
    th = "".join(f"<th>{inline_md(c, terms, used_ids)}</th>" for c in header)
    trs = []
    for row in body:
        tds = "".join(f"<td>{inline_md(c, terms, used_ids)}</td>" for c in row)
        trs.append(f"<tr>{tds}</tr>")
    cap = f"<figcaption>{html.escape(caption)}</figcaption>" if caption else ""
    return (
        f'<figure class="artifact table">{cap}'
        f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead>'
        f"<tbody>{''.join(trs)}</tbody></table></div></figure>"
    )


def split_table_row(line: str) -> list[str]:
    """Split a pipe row without breaking [[id|surface]] marks."""
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells: list[str] = []
    buf: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line.startswith("[[", i):
            end = line.find("]]", i)
            if end != -1:
                buf.append(line[i : end + 2])
                i = end + 2
                continue
        if line[i] == "|":
            cells.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(line[i])
        i += 1
    cells.append("".join(buf).strip())
    return cells


def is_table_sep(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.match(r"^:?-{3,}:?$", c) for c in cells)


def render_fence(kind: str, block: str, terms: dict, used_ids: list) -> str:
    tokens = kind.split()
    ftype = (tokens[0] if tokens else "code").lower()
    subtype = tokens[1].lower() if len(tokens) > 1 else ""
    fields, body = parse_fields(block)
    if subtype and "kind" not in fields:
        fields["kind"] = subtype
    if ftype == "ticket":
        return render_ticket(fields, terms, used_ids)
    if ftype in ("console", "terminal", "shell"):
        return render_console(fields, body, terms, used_ids)
    if ftype in ("gui", "dialog", "window"):
        return render_gui(fields, body, terms, used_ids)
    if ftype == "alert":
        return render_alert(fields, body, terms, used_ids)
    if ftype in ("tree", "process"):
        return render_tree(fields, body, terms, used_ids)
    if ftype == "chain":
        return render_chain(fields, body, terms, used_ids)
    if ftype == "meter":
        return render_meter(fields, terms, used_ids)
    if ftype == "table":
        lines = [ln for ln in body.splitlines() if ln.strip()]
        rows: list[list[str]] = []
        for ln in lines:
            if is_table_sep(ln):
                continue
            if ln.startswith("|"):
                rows.append(split_table_row(ln))
        return render_table(rows, terms, used_ids, _caption(fields, ""))
    # Fallback: preformatted exhibit
    caption = _caption(fields, ftype)
    return (
        f'<figure class="artifact code">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        f"<pre>{inline_md(body or block, terms, used_ids)}</pre>"
        f"</figure>"
    )


def md_to_html(md: str, terms: dict):
    lines = md.splitlines()
    used_ids: list[str] = []
    title = None
    byline = None
    body_start = 0
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body_start = 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1
        if (
            body_start < len(lines)
            and lines[body_start].startswith("*")
            and lines[body_start].endswith("*")
        ):
            byline = lines[body_start].strip("*").strip()
            body_start += 1

    paras: list[str] = []
    buf: list[str] = []

    def flush_para():
        nonlocal buf
        if not buf:
            return
        text = " ".join(buf)
        paras.append(f"<p>{inline_md(text, terms, used_ids)}</p>")
        buf = []

    i = body_start
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            flush_para()
            i += 1
            continue
        if line.startswith("```"):
            flush_para()
            kind = line.strip()[3:].strip() or "code"
            i += 1
            block_lines: list[str] = []
            while i < n and not lines[i].startswith("```"):
                block_lines.append(lines[i])
                i += 1
            if i < n:
                i += 1
            paras.append(render_fence(kind, "\n".join(block_lines), terms, used_ids))
            continue
        if line.startswith("|") and i + 1 < n and is_table_sep(lines[i + 1]):
            flush_para()
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < n and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = [split_table_row(ln) for ln in table_lines if not is_table_sep(ln)]
            paras.append(render_table(rows, terms, used_ids))
            continue
        if line.startswith("## "):
            flush_para()
            paras.append(f"<h2>{inline_md(line[3:].strip(), terms, used_ids)}</h2>")
            i += 1
            continue
        if line.startswith("# "):
            flush_para()
            paras.append(f"<h1>{inline_md(line[2:].strip(), terms, used_ids)}</h1>")
            i += 1
            continue
        buf.append(line.strip())
        i += 1
    flush_para()

    return title, byline, "\n".join(paras), used_ids



def render_unit(unit_dir: Path, kit_root: Path | None = None, also_local: Path | None = None) -> Path:
    """Render unit_dir → docs/<unit_id>/index.html. Returns output path."""
    kit_root = kit_root or KIT_ROOT
    unit_dir = unit_dir.resolve()
    unit_path = unit_dir / "unit.yaml"
    narrative_path = unit_dir / "narrative.md"
    glossary_path = unit_dir / "glossary.yaml"

    for p in (unit_path, narrative_path, glossary_path):
        if not p.is_file():
            raise SystemExit(f"Missing required file: {p}")

    unit = yaml.safe_load(unit_path.read_text(encoding="utf-8"))
    unit_id = unit.get("unit_id")
    if not unit_id:
        raise SystemExit(f"unit.yaml missing unit_id: {unit_path}")

    _, terms = load_glossary(glossary_path)
    md = narrative_path.read_text(encoding="utf-8")
    title, byline, body_html, used_ids = md_to_html(md, terms)

    page_title = unit.get("title") or title or unit_id
    if byline:
        subtitle = byline
    else:
        subtitle = unit.get("audience") or "A learning narrative"

    missing = [u for u in used_ids if u not in terms]
    if missing:
        raise SystemExit(f"Missing glossary ids: {missing}")

    exam_marks = sum(1 for u in used_ids if terms[u]["tier"] == "exam")
    support_marks = sum(1 for u in used_ids if terms[u]["tier"] == "support")
    unique_used = sorted(set(used_ids))

    gloss_list = [
        terms[tid] for tid in sorted(terms.keys(), key=lambda k: terms[k]["title"].lower())
    ]
    gloss_json = json.dumps({t["id"]: t for t in gloss_list}, ensure_ascii=False, separators=(',', ':'))

    html_out = render_html(page_title, subtitle, body_html, gloss_json)

    out_dir = kit_root / "docs" / unit_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html_out, encoding="utf-8")
    body = body_html.strip() + "\n"
    # Split large narratives so Pages artifacts stay MCP-push-friendly
    parts = []
    max_size = 15000
    if len(body) <= max_size:
        parts = [body]
    else:
        import re as _re
        chunks = _re.split(r"(?<=</p>)|(?<=</h2>)|(?<=</h1>)|(?<=</figure>)", body)
        buf = ""
        for c in chunks:
            if not c:
                continue
            if buf and len(buf) + len(c) > max_size:
                parts.append(buf)
                buf = c
            else:
                buf += c
        if buf:
            parts.append(buf)
        final = []
        for p in parts:
            while len(p) > max_size:
                final.append(p[:max_size])
                p = p[max_size:]
            if p:
                final.append(p)
        parts = final
    # Remove prior narrative parts
    for oldp in out_dir.glob("narrative*.html"):
        oldp.unlink()
    part_names = []
    for i, part in enumerate(parts):
        name = f"narrative.{i}.html" if len(parts) > 1 else "narrative.0.html"
        (out_dir / name).write_text(part, encoding="utf-8")
        part_names.append(name)
        print("Wrote", out_dir / name, len(part))
    import json as _json
    manifest = {"parts": part_names}
    (out_dir / "narrative.manifest.json").write_text(
        _json.dumps(manifest) + "\n", encoding="utf-8"
    )
    print("Wrote", out_dir / "narrative.manifest.json")
    gloss_js = "window.__GLOSSARY__ = " + gloss_json + ";\n"
    (out_dir / "glossary.js").write_text(gloss_js, encoding="utf-8")
    print("Wrote", out_dir / "glossary.js")

    if also_local is not None:
        also_local.write_text(html_out, encoding="utf-8")

    unused = sorted(set(terms.keys()) - set(used_ids))
    print("Wrote", out_path)
    if also_local is not None:
        print("Wrote", also_local)
    print(f"Marks total: {len(used_ids)} (exam={exam_marks}, support={support_marks})")
    print(f"Unique glossary ids used: {len(unique_used)} / {len(terms)}")
    if unused:
        print("Unused glossary ids:", ", ".join(unused))
    else:
        print("All glossary ids appear in narrative.")
    return out_path


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Render a unit directory to docs/<unit_id>/index.html"
    )
    parser.add_argument(
        "unit_dir",
        type=Path,
        help="Path to unit directory (must contain narrative.md + glossary.yaml + unit.yaml)",
    )
    parser.add_argument(
        "--kit-root",
        type=Path,
        default=None,
        help="Kit root (default: parent of tools/)",
    )
    args = parser.parse_args(argv)
    render_unit(args.unit_dir, kit_root=args.kit_root)


if __name__ == "__main__":
    main()
