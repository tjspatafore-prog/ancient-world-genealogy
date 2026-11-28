"""Generate exhaustive downloadable genealogy reports for all biblically connected lineages.

Outputs written to reports/:
  - Ancient_World_Genealogy_Complete_Report.pdf  (Formatted Compendium PDF with bookmarks & page numbers)
  - Ancient_World_Genealogy_AI_Parsed.md         (Structured LLM/AI-readable Markdown prosopography)
  - Ancient_World_Genealogy_Data_Points.csv      (UTF-8-BOM flat spreadsheet of every node & connections)
  - Ancient_World_Genealogy_AI_Records.jsonl     (One complete JSON record per line for vector/DB ingest)
  - report_manifest.json                         (Sizes, counts & PDF page metadata for the UI modal)
"""

import csv
import datetime as dt
import html
import json
import os
from collections import Counter, deque
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "world_genealogy.json"
REPORTS_DIR = ROOT / "reports"

OUT_PDF = REPORTS_DIR / "Ancient_World_Genealogy_Complete_Report.pdf"
OUT_MD = REPORTS_DIR / "Ancient_World_Genealogy_AI_Parsed.md"
OUT_CSV = REPORTS_DIR / "Ancient_World_Genealogy_Data_Points.csv"
OUT_JSONL = REPORTS_DIR / "Ancient_World_Genealogy_AI_Records.jsonl"
OUT_MANIFEST = REPORTS_DIR / "report_manifest.json"


def human_size(num_bytes: int) -> str:
    value = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024.0 or unit == "GB":
            return f"{value:.2f} {unit}" if unit in ("MB", "GB") else f"{int(round(value))} {unit}"
        value /= 1024.0
    return f"{num_bytes} B"


def esc(text: str) -> str:
    return html.escape(str(text or ""), quote=True)


def as_str_list(val) -> list:
    if not val or isinstance(val, bool):
        return []
    if isinstance(val, (list, tuple)):
        return [str(x) for x in val if x is not None and not isinstance(x, bool) and str(x).strip()]
    return [str(val)]


def sanitize_pdf_text(text: str) -> str:
    """Keep text crisp and avoid glyphs outside standard Windows UI/serif fonts."""
    if not text:
        return ""
    replacements = {
        "\u2192": "->",
        "\u2190": "<-",
        "\u2194": "<->",
        "\u2022": "|",
        "\u2605": "[Major]",
        "\u2014": "--",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    out = str(text)
    for k, v in replacements.items():
        out = out.replace(k, v)
    return out


def compute_shortest_paths(nodes_by_id: dict, edges: list, start_id: str = "bib_adam"):
    allowed = {"direct", "expansion", "cognate", "syncretic"}
    adj = {nid: [] for nid in nodes_by_id}
    for e in edges:
        if e["type"] in allowed and e["from"] in nodes_by_id and e["to"] in nodes_by_id:
            adj[e["from"]].append((e["to"], e))
            adj[e["to"]].append((e["from"], e))

    parent_map = {start_id: None}
    depth_map = {start_id: 0}
    q = deque([start_id])
    while q:
        u = q.popleft()
        d = depth_map[u]
        for v, edge in adj.get(u, []):
            if v not in depth_map:
                depth_map[v] = d + 1
                parent_map[v] = (u, edge)
                q.append(v)

    paths = {}
    for nid in nodes_by_id:
        if nid not in depth_map:
            paths[nid] = (-1, [])
            continue
        chain = []
        cur = nid
        while cur is not None:
            prev_info = parent_map[cur]
            n_obj = nodes_by_id[cur]
            if prev_info is None:
                chain.append({"id": cur, "name": n_obj["name"], "via": None})
                break
            prev_id, edge = prev_info
            chain.append({
                "id": cur,
                "name": n_obj["name"],
                "via": {"type": edge["type"], "label": edge["label"]},
            })
            cur = prev_id
        chain.reverse()
        paths[nid] = (depth_map[nid], chain)
    return paths


def load_biblical_graph():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    traditions = data["traditions"]
    bib_nodes = [n for n in data["nodes"] if n.get("biblicalConnected") is True]
    bib_ids = {n["id"] for n in bib_nodes}
    nodes_by_id = {n["id"]: n for n in bib_nodes}

    bib_edges = [e for e in data["edges"] if e["from"] in bib_ids and e["to"] in bib_ids]
    paths = compute_shortest_paths(nodes_by_id, bib_edges, "bib_adam")

    parents_of = {nid: [] for nid in bib_ids}
    offspring_of = {nid: [] for nid in bib_ids}
    for e in bib_edges:
        src = nodes_by_id[e["from"]]
        dst = nodes_by_id[e["to"]]
        parents_of[e["to"]].append({
            "id": e["from"],
            "name": src["name"],
            "type": e["type"],
            "label": e["label"],
        })
        offspring_of[e["from"]].append({
            "id": e["to"],
            "name": dst["name"],
            "type": e["type"],
            "label": e["label"],
        })

    ordered_traditions = sorted(
        traditions.items(),
        key=lambda kv: (kv[1].get("order", 999), kv[0]),
    )
    grouped = {k: [] for k, _ in ordered_traditions}
    for n in bib_nodes:
        grouped.setdefault(n["tradition"], []).append(n)

    records = []
    grouped_records = []
    for t_key, t_meta in ordered_traditions:
        t_nodes = grouped.get(t_key, [])
        if not t_nodes:
            continue
        t_nodes.sort(
            key=lambda x: (
                int(x.get("tier", 999)),
                paths[x["id"]][0] if paths[x["id"]][0] >= 0 else 999,
                0 if x.get("major") else 1,
                x["name"].lower(),
            )
        )
        t_recs = []
        for n in t_nodes:
            nid = n["id"]
            steps, chain = paths[nid]
            pars = parents_of[nid]
            kids = offspring_of[nid]
            path_names = " -> ".join(step["name"] for step in chain)
            rec = {
                "id": nid,
                "name": str(n["name"]),
                "alt_names": as_str_list(n.get("altNames")),
                "tradition": t_key,
                "tradition_label": t_meta.get("label", t_key),
                "region": t_meta.get("region", ""),
                "color": t_meta.get("color", "#475569"),
                "tier": n.get("tier"),
                "era_years": str(n.get("era", "")),
                "role": str(n.get("role", "")),
                "is_major": bool(n.get("major")),
                "steps_from_adam": steps,
                "lineage_path_from_adam": path_names,
                "shortest_path_from_adam": chain,
                "parent_count": len(pars),
                "parents": pars,
                "offspring_count": len(kids),
                "offspring": kids,
                "total_connections": len(pars) + len(kids),
                "sources": as_str_list(n.get("sources")),
                "notes": str(n.get("notes", "")),
            }
            records.append(rec)
            t_recs.append(rec)
        grouped_records.append((t_key, t_meta, t_recs))

    return data, bib_nodes, bib_edges, records, grouped_records


def write_markdown_report(data, bib_edges, records, grouped_records):
    meta = data["metadata"]
    edge_counts = Counter(e["type"] for e in bib_edges)
    major_count = sum(1 for r in records if r["is_major"])
    generated = dt.date.today().isoformat()

    lines = [
        f"# {meta['title']} — Exhaustive Biblical Lineage Compendium (AI-Parsed Edition)",
        "",
        f"- **Version:** {meta['version']}",
        f"- **Generated:** {generated}",
        "- **Scope:** Every individual, monarch, patriarch, dynasty & bridge node with a verified textual/chronicler path to `bib_adam` (Adam & Eve)",
        f"- **Total Biblically Connected Individuals / Nodes:** {len(records):,}",
        f"- **Major Landmarks:** {major_count:,}",
        f"- **Total Connecting Edges:** {len(bib_edges):,} ({', '.join(f'{k}: {v:,}' for k, v in edge_counts.most_common())})",
        "",
        "## Tradition Directory",
        "",
    ]
    for idx, (t_key, t_meta, t_recs) in enumerate(grouped_records, start=1):
        lines.append(f"{idx}. **{t_meta['label']}** (`{t_key}`, {t_meta['region']}) — {len(t_recs):,} records")
    lines.append("")

    for idx, (t_key, t_meta, t_recs) in enumerate(grouped_records, start=1):
        lines.extend([
            "---",
            "",
            f"## {idx}. {t_meta['label']} (`{t_key}` | {t_meta['region']} | {len(t_recs):,} records)",
            "",
        ])
        for r in t_recs:
            alt_str = "; ".join(r["alt_names"]) if r["alt_names"] else "None"
            src_str = "; ".join(r["sources"]) if r["sources"] else "Primary Archive"
            par_str = (
                " | ".join(f"{p['name']} [{p['id']}] ({p['type']}: {p['label']})" for p in r["parents"])
                if r["parents"]
                else "Primeval Origin (Root)"
            )
            kid_str = (
                " | ".join(f"{k['name']} [{k['id']}] ({k['type']}: {k['label']})" for k in r["offspring"])
                if r["offspring"]
                else "None / Terminal Leaf"
            )
            lines.extend([
                f"### [{r['id']}] {r['name']}",
                f"- **Tradition:** {r['tradition_label']} (`{r['tradition']}`, {r['region']})",
                f"- **Era / Years:** {r['era_years']} | **Generation Tier:** {r['tier']} | **Major Landmark:** {'Yes' if r['is_major'] else 'No'} | **Steps From Adam:** {r['steps_from_adam']}",
                f"- **Role / Title:** {r['role']}",
                f"- **Alt / Cognate Names:** {alt_str}",
                f"- **Lineage From Adam:** {r['lineage_path_from_adam']}",
                f"- **Parents / Ancestors ({r['parent_count']}):** {par_str}",
                f"- **Offspring / Successors ({r['offspring_count']}):** {kid_str}",
                f"- **Primary Sources:** {src_str}",
                f"- **Notes:** {r['notes']}",
                "",
            ])

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_csv_report(records):
    fieldnames = [
        "id",
        "name",
        "alt_names",
        "tradition",
        "tradition_label",
        "region",
        "tier",
        "era_years",
        "role",
        "is_major",
        "steps_from_adam",
        "lineage_path_from_adam",
        "parent_count",
        "parents",
        "parent_links",
        "offspring_count",
        "offspring",
        "offspring_links",
        "total_connections",
        "sources",
        "notes",
    ]
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in records:
            w.writerow({
                "id": r["id"],
                "name": r["name"],
                "alt_names": "; ".join(r["alt_names"]),
                "tradition": r["tradition"],
                "tradition_label": r["tradition_label"],
                "region": r["region"],
                "tier": r["tier"],
                "era_years": r["era_years"],
                "role": r["role"],
                "is_major": "TRUE" if r["is_major"] else "FALSE",
                "steps_from_adam": r["steps_from_adam"],
                "lineage_path_from_adam": r["lineage_path_from_adam"],
                "parent_count": r["parent_count"],
                "parents": "; ".join(f"{p['name']} [{p['id']}]" for p in r["parents"]),
                "parent_links": " | ".join(f"{p['id']} ({p['type']}: {p['label']})" for p in r["parents"]),
                "offspring_count": r["offspring_count"],
                "offspring": "; ".join(f"{k['name']} [{k['id']}]" for k in r["offspring"]),
                "offspring_links": " | ".join(f"{k['id']} ({k['type']}: {k['label']})" for k in r["offspring"]),
                "total_connections": r["total_connections"],
                "sources": "; ".join(r["sources"]),
                "notes": r["notes"],
            })


def write_jsonl_report(records):
    with open(OUT_JSONL, "w", encoding="utf-8") as f:
        for r in records:
            clean = {k: v for k, v in r.items() if k != "color"}
            f.write(json.dumps(clean, ensure_ascii=False) + "\n")


PDF_CSS = """
@font-face {
  font-family: "AtlasSerif";
  src: url("georgia.ttf");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "AtlasSerif";
  src: url("georgiab.ttf");
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: "AtlasSans";
  src: url("segoeui.ttf");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "AtlasSans";
  src: url("segoeuib.ttf");
  font-weight: bold;
  font-style: normal;
}
body {
  font-family: "AtlasSans", sans-serif;
  font-size: 8.2pt;
  line-height: 1.32;
  color: #1c1917;
  margin: 0;
  padding: 0;
}
.cover-box {
  border-top: 4px solid #b45309;
  border-bottom: 2px solid #d6d3d1;
  padding: 16px 0 12px 0;
  margin-bottom: 12px;
}
.cover-kicker {
  font-size: 8.5pt;
  font-weight: bold;
  color: #b45309;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
h1.title {
  font-family: "AtlasSerif", serif;
  font-size: 20pt;
  line-height: 1.15;
  color: #0f172a;
  margin: 0 0 6px 0;
}
.subtitle {
  font-size: 9.5pt;
  color: #44403c;
  margin: 0 0 8px 0;
}
h2.section {
  font-family: "AtlasSerif", serif;
  font-size: 12.5pt;
  color: #0f172a;
  border-bottom: 1.5px solid #b45309;
  padding-bottom: 3px;
  margin: 12px 0 6px 0;
}
h2.chap {
  font-family: "AtlasSerif", serif;
  font-size: 14pt;
  color: #0f172a;
  border-bottom: 2px solid #b45309;
  padding-bottom: 4px;
  margin: 0 0 4px 0;
}
.chap-meta {
  font-size: 8pt;
  color: #57534e;
  margin-bottom: 8px;
}
table.summary {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.8pt;
  margin: 6px 0 10px 0;
}
table.summary th {
  background-color: #f3efe8;
  color: #1c1917;
  text-align: left;
  padding: 4px 6px;
  border-bottom: 1.5px solid #a8a29e;
  font-weight: bold;
}
table.summary td {
  padding: 3px 6px;
  border-bottom: 0.5px solid #e7e5e4;
}
.rec {
  border-left: 2.5px solid #cbd5e1;
  border-bottom: 0.5px solid #e7e5e4;
  padding: 3px 0 4px 7px;
  margin-bottom: 4.5px;
  break-inside: avoid;
}
.rec-major {
  border-left: 3px solid #b45309;
  background-color: #fffbf2;
}
.rec-head {
  font-size: 8.6pt;
  font-weight: bold;
  color: #0f172a;
  margin-bottom: 1.5px;
}
.rec-id {
  font-weight: normal;
  font-size: 7.4pt;
  color: #78716c;
}
.rec-badge {
  font-size: 7.1pt;
  font-weight: bold;
  color: #b45309;
}
.rec-line {
  font-size: 7.7pt;
  color: #292524;
  margin: 1px 0;
}
.lbl {
  font-weight: bold;
  color: #44403c;
}
.lbl-par {
  font-weight: bold;
  color: #0369a1;
}
.lbl-kid {
  font-weight: bold;
  color: #9a3412;
}
.rec-notes {
  font-size: 7.6pt;
  color: #44403c;
  margin: 1.5px 0;
}
.rec-src {
  font-size: 7.2pt;
  color: #57534e;
}
"""


def render_story_pages(writer, archive, html_body: str, rect: pymupdf.Rect) -> int:
    full_html = f"<html><head><style>{PDF_CSS}</style></head><body>{html_body}</body></html>"
    story = pymupdf.Story(html=full_html, archive=archive)
    pages_written = 0
    more = True
    while more:
        dev = writer.begin_page(pymupdf.paper_rect("letter"))
        more, _ = story.place(rect)
        story.draw(dev, None)
        writer.end_page()
        pages_written += 1
    return pages_written


def build_cover_html(data, bib_edges, records, grouped_records) -> str:
    meta = data["metadata"]
    edge_counts = Counter(e["type"] for e in bib_edges)
    major_count = sum(1 for r in records if r["is_major"])
    generated = dt.date.today().isoformat()

    trad_rows = []
    for idx, (t_key, t_meta, t_recs) in enumerate(grouped_records, start=1):
        maj = sum(1 for r in t_recs if r["is_major"])
        links = sum(r["total_connections"] for r in t_recs)
        trad_rows.append(
            f"<tr><td>{idx}</td><td><b>{esc(t_meta['label'])}</b></td>"
            f"<td>{esc(t_meta['region'])}</td>"
            f"<td style='text-align:right'>{len(t_recs):,}</td>"
            f"<td style='text-align:right'>{maj:,}</td>"
            f"<td style='text-align:right'>{links:,}</td></tr>"
        )

    prov_rows = []
    for lt, desc in data["metadata"]["linkTypes"].items():
        cnt = edge_counts.get(lt, 0)
        if cnt > 0:
            prov_rows.append(
                f"<tr><td><b>{esc(lt)}</b></td><td style='text-align:right'>{cnt:,}</td>"
                f"<td>{esc(sanitize_pdf_text(desc))}</td></tr>"
            )

    by_id = {r["id"]: r for r in records}
    stem_ids = [
        "bib_adam",
        "bib_seth",
        "bib_enoch",
        "bib_methuselah",
        "bib_noah",
        "bib_shem",
        "bib_ham",
        "bib_japheth",
        "bib_abraham",
        "jud_david",
        "nt_jesus",
    ]
    stem_rows = []
    for sid in stem_ids:
        r = by_id.get(sid)
        if r:
            stem_rows.append(
                f"<tr><td><b>{esc(sanitize_pdf_text(r['name']))}</b></td>"
                f"<td>{esc(sanitize_pdf_text(r['era_years']))}</td>"
                f"<td style='text-align:right'>{r['offspring_count']}</td>"
                f"<td>{esc(sanitize_pdf_text('; '.join(k['name'] for k in r['offspring'][:4])))}</td></tr>"
            )

    return f"""
    <div class="cover-box">
      <div class="cover-kicker">Universal World Genealogy Compendium &bull; Complete Archival Edition</div>
      <h1 class="title">Ancient World Genealogy Atlas</h1>
      <p class="subtitle">Exhaustive Compendium of All {len(records):,} Biblically Connected Patriarchs, Monarchs, Queens, Prophets &amp; Cross-Tradition Bridge Lineages ({esc(meta['version'])})</p>
      <p style="font-size:8pt;color:#57534e;margin:0;">
        <b>Edition:</b> {esc(sanitize_pdf_text(meta['title']))} &nbsp;|&nbsp;
        <b>Generated:</b> {generated} &nbsp;|&nbsp;
        <b>Connected Individuals:</b> {len(records):,} ({major_count:,} Major Landmarks) &nbsp;|&nbsp;
        <b>Verified Edges:</b> {len(bib_edges):,} &nbsp;|&nbsp;
        <b>Source Modules:</b> {len(meta['modules'])}
      </p>
    </div>

    <h2 class="section">1. Executive Breakdown by Historical &amp; Scriptural Tradition</h2>
    <table class="summary">
      <thead><tr><th>#</th><th>Tradition Chapter</th><th>Region</th><th style="text-align:right">Records</th><th style="text-align:right">Major</th><th style="text-align:right">Degree Links</th></tr></thead>
      <tbody>{''.join(trad_rows)}</tbody>
    </table>

    <h2 class="section">2. Provenance Tier Classification Across Connecting Edges</h2>
    <table class="summary">
      <thead><tr><th>Tier Type</th><th style="text-align:right">Count</th><th>Methodological Definition</th></tr></thead>
      <tbody>{''.join(prov_rows)}</tbody>
    </table>

    <h2 class="section">3. Primeval Backbone Landmarks (Adam &amp; Eve -> Noah -> Nations &amp; Messianic Stem)</h2>
    <table class="summary">
      <thead><tr><th>Landmark Person</th><th>Horizon / Era</th><th style="text-align:right">Direct Links</th><th>Key Immediate Descendants / Branches</th></tr></thead>
      <tbody>{''.join(stem_rows)}</tbody>
    </table>
    """


def format_pdf_record(r: dict) -> str:
    cls = "rec rec-major" if r["is_major"] else "rec"
    badge = ' <span class="rec-badge">[MAJOR]</span>' if r["is_major"] else ""
    alt = ", ".join(r["alt_names"]) if r["alt_names"] else ""
    src = "; ".join(r["sources"]) if r["sources"] else "Primary Archive"
    par_str = (
        "; ".join(f"{p['name']} ({p['type']}: {p['label']})" for p in r["parents"][:8])
        + (f"; +{len(r['parents']) - 8} more" if len(r["parents"]) > 8 else "")
        if r["parents"]
        else "Primeval Origin (Adam & Eve Root)"
    )
    kid_str = (
        "; ".join(f"{k['name']} ({k['type']}: {k['label']})" for k in r["offspring"][:10])
        + (f"; +{len(r['offspring']) - 10} more" if len(r["offspring"]) > 10 else "")
        if r["offspring"]
        else "Terminal / Leaf Record"
    )
    parts = [
        f'<div class="{cls}">',
        f'<div class="rec-head">{esc(sanitize_pdf_text(r["name"]))}{badge} <span class="rec-id">[{esc(r["id"])}]</span></div>',
        f'<div class="rec-line"><span class="lbl">Era:</span> {esc(sanitize_pdf_text(r["era_years"]))} &bull; '
        f'<span class="lbl">Tier:</span> {r["tier"]} &bull; '
        f'<span class="lbl">Steps from Adam:</span> {r["steps_from_adam"]} &bull; '
        f'<span class="lbl">Role:</span> {esc(sanitize_pdf_text(r["role"]))}</div>',
    ]
    if alt:
        parts.append(f'<div class="rec-line"><span class="lbl">Alt Names:</span> {esc(sanitize_pdf_text(alt))}</div>')
    parts.append(f'<div class="rec-line"><span class="lbl">Adam Path:</span> {esc(sanitize_pdf_text(r["lineage_path_from_adam"]))}</div>')
    parts.append(f'<div class="rec-line"><span class="lbl-par">Parents ({r["parent_count"]}):</span> {esc(sanitize_pdf_text(par_str))}</div>')
    parts.append(f'<div class="rec-line"><span class="lbl-kid">Offspring ({r["offspring_count"]}):</span> {esc(sanitize_pdf_text(kid_str))}</div>')
    if r["notes"]:
        parts.append(f'<div class="rec-notes"><span class="lbl">Notes:</span> {esc(sanitize_pdf_text(r["notes"]))}</div>')
    parts.append(f'<div class="rec-src"><span class="lbl">Sources:</span> {esc(sanitize_pdf_text(src))}</div>')
    parts.append("</div>")
    return "".join(parts)


def write_pdf_report(data, bib_edges, records, grouped_records) -> int:
    import tempfile
    tmp_pdf = Path(tempfile.gettempdir()) / "awg_compendium_raw.pdf"
    font_dir = r"C:\Windows\Fonts"
    archive = pymupdf.Archive(font_dir) if os.path.isdir(font_dir) else None
    mediabox = pymupdf.paper_rect("letter")
    content_rect = mediabox + (42, 46, -42, -46)

    toc = []
    writer = pymupdf.DocumentWriter(str(tmp_pdf))
    current_page = 1

    # Cover + Executive Summary pages
    cover_pages = render_story_pages(writer, archive, build_cover_html(data, bib_edges, records, grouped_records), content_rect)
    toc.append([1, "Executive Summary & Provenance Overview", current_page])
    current_page += cover_pages

    # One chapter per tradition, rendered in fast Story chunks
    chunk_size = 150
    for idx, (t_key, t_meta, t_recs) in enumerate(grouped_records, start=1):
        chap_title = f"{idx}. {t_meta['label']} ({len(t_recs):,} Records)"
        toc.append([1, sanitize_pdf_text(chap_title), current_page])
        for start in range(0, len(t_recs), chunk_size):
            batch = t_recs[start : start + chunk_size]
            header = ""
            if start == 0:
                header = (
                    f'<h2 class="chap">{esc(sanitize_pdf_text(chap_title))}</h2>'
                    f'<div class="chap-meta">Tradition Key: <b>{esc(t_key)}</b> &bull; Region: {esc(sanitize_pdf_text(t_meta["region"]))}</div>'
                )
            else:
                header = (
                    f'<div class="chap-meta"><i>Continued: {esc(sanitize_pdf_text(chap_title))}</i></div>'
                )
            body_html = header + "".join(format_pdf_record(r) for r in batch)
            current_page += render_story_pages(writer, archive, body_html, content_rect)

    writer.close()
    del writer

    # Post-process: add interactive bookmarks, running headers/footers, subset fonts & compress
    doc = pymupdf.open(str(tmp_pdf))
    total_pages = len(doc)
    doc.set_metadata({
        "title": "Ancient World Genealogy Atlas — Complete Biblical Lineage Compendium",
        "author": "Ancient World Genealogy Atlas",
        "subject": f"Exhaustive Prosopography of {len(records)} Biblically Connected Lineages",
        "creator": "PyMuPDF Story Generator",
    })
    doc.set_toc(toc)

    version_str = data["metadata"]["version"]
    for pno in range(total_pages):
        page = doc[pno]
        if pno == 0:
            footer = f"Ancient World Genealogy Atlas v{version_str}   |   Page 1 of {total_pages}"
            page.insert_text(
                pymupdf.Point(42, mediabox.height - 24),
                footer,
                fontname="helv",
                fontsize=7.5,
                color=(0.42, 0.40, 0.38),
            )
            continue
        page.insert_text(
            pymupdf.Point(42, 28),
            f"Ancient World Genealogy Atlas (v{version_str}) -- Complete Biblically Connected Compendium ({len(records):,} Records)",
            fontname="helv",
            fontsize=7.5,
            color=(0.45, 0.43, 0.40),
        )
        page.insert_text(
            pymupdf.Point(mediabox.width - 108, 28),
            f"Page {pno + 1} of {total_pages}",
            fontname="helv",
            fontsize=7.5,
            color=(0.45, 0.43, 0.40),
        )
        page.draw_line(pymupdf.Point(42, 33), pymupdf.Point(mediabox.width - 42, 33), color=(0.85, 0.83, 0.80), width=0.5)

    doc.subset_fonts()
    doc.save(str(OUT_PDF), garbage=4, deflate=True, clean=True)
    doc.close()
    del doc
    try:
        tmp_pdf.unlink(missing_ok=True)
    except OSError:
        pass
    return total_pages


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    data, bib_nodes, bib_edges, records, grouped_records = load_biblical_graph()

    print(f"Loaded {len(records)} biblically connected individuals and {len(bib_edges)} internal edges.")
    write_markdown_report(data, bib_edges, records, grouped_records)
    print(f"Wrote Markdown: {OUT_MD.name} ({human_size(OUT_MD.stat().st_size)})")

    write_csv_report(records)
    print(f"Wrote CSV:      {OUT_CSV.name} ({human_size(OUT_CSV.stat().st_size)})")

    write_jsonl_report(records)
    print(f"Wrote JSONL:    {OUT_JSONL.name} ({human_size(OUT_JSONL.stat().st_size)})")

    pdf_pages = write_pdf_report(data, bib_edges, records, grouped_records)
    print(f"Wrote PDF:      {OUT_PDF.name} ({pdf_pages} pages, {human_size(OUT_PDF.stat().st_size)})")

    manifest = {
        "version": data["metadata"]["version"],
        "generated_date": dt.date.today().isoformat(),
        "total_biblical_nodes": len(records),
        "total_biblical_edges": len(bib_edges),
        "total_major_landmarks": sum(1 for r in records if r["is_major"]),
        "pdf_pages": pdf_pages,
        "files": {
            "pdf": {
                "filename": OUT_PDF.name,
                "path": f"reports/{OUT_PDF.name}",
                "bytes": OUT_PDF.stat().st_size,
                "human_size": human_size(OUT_PDF.stat().st_size),
                "pages": pdf_pages,
            },
            "markdown": {
                "filename": OUT_MD.name,
                "path": f"reports/{OUT_MD.name}",
                "bytes": OUT_MD.stat().st_size,
                "human_size": human_size(OUT_MD.stat().st_size),
            },
            "csv": {
                "filename": OUT_CSV.name,
                "path": f"reports/{OUT_CSV.name}",
                "bytes": OUT_CSV.stat().st_size,
                "human_size": human_size(OUT_CSV.stat().st_size),
            },
            "jsonl": {
                "filename": OUT_JSONL.name,
                "path": f"reports/{OUT_JSONL.name}",
                "bytes": OUT_JSONL.stat().st_size,
                "human_size": human_size(OUT_JSONL.stat().st_size),
            },
        },
    }
    OUT_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote Manifest: {OUT_MANIFEST.name}")


if __name__ == "__main__":
    main()
