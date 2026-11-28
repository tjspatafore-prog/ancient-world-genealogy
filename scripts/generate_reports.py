"""Generate exhaustive v33.0 downloadable genealogy reports for all biblically connected lineages.

v33.0 fixes:
- Strictly directed chronological shortest-path Dijkstra solver from bib_adam
  (never walks backwards up parent->child edges; excludes source_meta nodes & motif_parallel links)
- Separates every link cleanly by semantic relation_type:
  parents, offspring, successors, spouses, historical_links, parallels
- Separates node_type (person, dynasty_cluster, source_meta) in PDF, Markdown, CSV & JSONL
- Includes Pending Bridge appendix note in Executive Summary (no 2-node orphan chapters)
"""

import csv
import datetime as dt
import heapq
import html
import json
import os
import tempfile
from collections import Counter, defaultdict, deque
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

LINK_WEIGHTS = {
    "direct": 1.0,
    "expansion": 1.4,
    "cognate": 3.0,
    "syncretic": 5.0,
}


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


def compute_directed_paths(nodes_by_id: dict, edges: list, start_id: str = "bib_adam"):
    """3-pass strictly directed chronological lineage & historical path solver.

    Pass 1 (directed_lineage): forward only over relation_type in {'parent_of', 'successor_of'}
      with provenance in {'direct', 'expansion', 'cognate', 'syncretic'}, skipping source_meta.
      Uses Dijkstra weights so direct/expansion canonical lines beat syncretic jumps.
    Pass 2 (directed_historical): forward only from Pass 1 boundary over {'spouse_of',
      'contemporary_of', 'foe_or_ally_of'}, skipping source_meta.
    Pass 3 (collateral_predecessor): for nodes whose outgoing directed links point into Pass 1/2
      nodes (ancestors/wives/predecessors of bridged kings), walk forward to nearest Pass 1/2 anchor.
    """
    non_meta = {nid for nid, n in nodes_by_id.items() if n.get("node_type") != "source_meta"}
    fwd_lineage = defaultdict(list)
    fwd_hist = defaultdict(list)
    fwd_all = defaultdict(list)

    for e in edges:
        src, dst, lt = e["from"], e["to"], e["type"]
        rt = e.get("relation_type", "parent_of")
        if src not in non_meta or dst not in non_meta or src == dst:
            continue
        if lt not in LINK_WEIGHTS or rt == "motif_parallel":
            continue
        w = LINK_WEIGHTS[lt]
        fwd_all[src].append((dst, e, w))
        if rt in ("parent_of", "successor_of"):
            fwd_lineage[src].append((dst, e, w))
        else:
            fwd_hist[src].append((dst, e, w))

    # Pass 1: Dijkstra on strict forward parent_of / successor_of
    dist = {start_id: 0.0}
    hops = {start_id: 0}
    parent_edge = {start_id: None}
    mode = {start_id: "directed_lineage"}
    pq = [(0.0, 0, start_id)]
    while pq:
        d, h, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue
        for v, edge, w in fwd_lineage.get(u, []):
            nd = d + w
            nh = h + 1
            if nd < dist.get(v, float("inf")) or (nd == dist.get(v, float("inf")) and nh < hops.get(v, 9999)):
                dist[v] = nd
                hops[v] = nh
                parent_edge[v] = (u, edge)
                mode[v] = "directed_lineage"
                heapq.heappush(pq, (nd, nh, v))

    # Pass 2: Extend forward over spouse_of / contemporary_of / foe_or_ally_of without overwriting Pass 1
    pq2 = [(dist[u], hops[u], u) for u in list(dist.keys())]
    heapq.heapify(pq2)
    while pq2:
        d, h, u = heapq.heappop(pq2)
        if d > dist.get(u, float("inf")):
            continue
        # Walk one or more forward historical/marital edges + downstream lineage if any
        next_edges = fwd_hist.get(u, []) + (fwd_lineage.get(u, []) if mode.get(u) == "directed_historical" else [])
        for v, edge, w in next_edges:
            if mode.get(v) == "directed_lineage":
                continue
            nd = d + w + 2.0
            nh = h + 1
            if nd < dist.get(v, float("inf")) or (nd == dist.get(v, float("inf")) and nh < hops.get(v, 9999)):
                dist[v] = nd
                hops[v] = nh
                parent_edge[v] = (u, edge)
                mode[v] = "directed_historical"
                heapq.heappush(pq2, (nd, nh, v))

    def reconstruct(target_id):
        chain = []
        cur = target_id
        seen = set()
        while cur is not None and cur not in seen:
            seen.add(cur)
            prev_info = parent_edge.get(cur)
            n_obj = nodes_by_id[cur]
            if prev_info is None:
                chain.append({"id": cur, "name": str(n_obj["name"]), "via": None})
                break
            prev_id, edge = prev_info
            chain.append({
                "id": cur,
                "name": str(n_obj["name"]),
                "via": {
                    "type": edge["type"],
                    "relation_type": edge.get("relation_type", "parent_of"),
                    "label": edge["label"],
                },
            })
            cur = prev_id
        chain.reverse()
        return chain

    results = {}
    for nid, n_obj in nodes_by_id.items():
        if n_obj.get("node_type") == "source_meta":
            results[nid] = {
                "mode": "source_meta",
                "steps": None,
                "path_text": "[Bibliographical / Chronological Source Reference]",
                "chain": [],
            }
        elif nid in dist:
            ch = reconstruct(nid)
            results[nid] = {
                "mode": mode[nid],
                "steps": len(ch) - 1,
                "path_text": " -> ".join(step["name"] for step in ch),
                "chain": ch,
            }
        else:
            # Pass 3: Collateral / Predecessor — find shortest forward path from nid INTO any Pass 1/2 node
            q = deque([(nid, [(nid, None)])])
            vis_fwd = {nid}
            anchor_found = None
            while q:
                u, subpath = q.popleft()
                if u != nid and u in dist:
                    anchor_found = (u, subpath)
                    break
                for v, edge, _ in fwd_all.get(u, []):
                    if v not in vis_fwd:
                        vis_fwd.add(v)
                        q.append((v, subpath + [(v, edge)]))
            if anchor_found:
                anchor_id, subpath = anchor_found
                anchor_chain = reconstruct(anchor_id)
                desc_str = " -> ".join(str(nodes_by_id[p_id]["name"]) for p_id, _ in subpath[1:])
                base_str = " -> ".join(step["name"] for step in anchor_chain)
                results[nid] = {
                    "mode": "collateral_predecessor",
                    "steps": None,
                    "path_text": f"Predecessor / Collateral Root -> {desc_str} [Bridged at {nodes_by_id[anchor_id]['name']} via {base_str}]",
                    "chain": anchor_chain,
                }
            else:
                results[nid] = {
                    "mode": "collateral_other",
                    "steps": None,
                    "path_text": "Historical / Cross-Reference Connection within Biblical Network",
                    "chain": [],
                }
    return results


def load_biblical_graph():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    traditions = data["traditions"]
    bib_nodes = [n for n in data["nodes"] if n.get("biblicalConnected") is True]
    pending_nodes = [n for n in data["nodes"] if n.get("tradition") != "dna" and not n.get("biblicalConnected")]
    bib_ids = {n["id"] for n in bib_nodes}
    nodes_by_id = {n["id"]: n for n in bib_nodes}

    bib_edges = [e for e in data["edges"] if e["from"] in bib_ids and e["to"] in bib_ids]
    paths = compute_directed_paths(nodes_by_id, bib_edges, "bib_adam")

    parents_of = defaultdict(list)
    offspring_of = defaultdict(list)
    successors_of = defaultdict(list)
    spouses_of = defaultdict(list)
    historical_of = defaultdict(list)
    parallels_of = defaultdict(list)

    for e in bib_edges:
        src = nodes_by_id[e["from"]]
        dst = nodes_by_id[e["to"]]
        rt = e.get("relation_type", "parent_of")
        out_item = {"id": e["to"], "name": str(dst["name"]), "type": e["type"], "relation_type": rt, "label": e["label"], "direction": "outgoing"}
        in_item = {"id": e["from"], "name": str(src["name"]), "type": e["type"], "relation_type": rt, "label": e["label"], "direction": "incoming"}

        if rt == "parent_of":
            parents_of[e["to"]].append(in_item)
            offspring_of[e["from"]].append(out_item)
        elif rt == "successor_of":
            successors_of[e["to"]].append({**in_item, "direction": "predecessor"})
            successors_of[e["from"]].append({**out_item, "direction": "successor"})
        elif rt == "spouse_of":
            spouses_of[e["from"]].append(out_item)
            spouses_of[e["to"]].append(in_item)
        elif rt == "motif_parallel":
            parallels_of[e["from"]].append(out_item)
            parallels_of[e["to"]].append(in_item)
        else:
            historical_of[e["from"]].append(out_item)
            historical_of[e["to"]].append(in_item)

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
                0 if x.get("node_type") != "source_meta" else 1,
                int(x.get("tier", 999)),
                paths[x["id"]]["steps"] if isinstance(paths[x["id"]]["steps"], int) else 999,
                0 if x.get("major") else 1,
                str(x["name"]).lower(),
            )
        )
        t_recs = []
        for n in t_nodes:
            nid = n["id"]
            pinfo = paths[nid]
            pars = parents_of[nid]
            kids = offspring_of[nid]
            succs = successors_of[nid]
            sps = spouses_of[nid]
            hists = historical_of[nid]
            plls = parallels_of[nid]
            total_conn = len(pars) + len(kids) + len(succs) + len(sps) + len(hists) + len(plls)
            rec = {
                "id": nid,
                "name": str(n["name"]),
                "node_type": n.get("node_type", "person"),
                "alt_names": as_str_list(n.get("altNames")),
                "tradition": t_key,
                "tradition_label": t_meta.get("label", t_key),
                "region": t_meta.get("region", ""),
                "color": t_meta.get("color", "#475569"),
                "tier": n.get("tier"),
                "era_years": str(n.get("era", "")),
                "role": str(n.get("role", "")),
                "is_major": bool(n.get("major")),
                "adam_path_mode": pinfo["mode"],
                "steps_from_adam": pinfo["steps"],
                "lineage_path_from_adam": pinfo["path_text"],
                "shortest_path_from_adam": pinfo["chain"],
                "parent_count": len(pars),
                "parents": pars,
                "offspring_count": len(kids),
                "offspring": kids,
                "successor_count": len(succs),
                "successors": succs,
                "spouse_count": len(sps),
                "spouses": sps,
                "historical_count": len(hists),
                "historical_links": hists,
                "parallel_count": len(plls),
                "parallels": plls,
                "total_connections": total_conn,
                "sources": as_str_list(n.get("sources")),
                "notes": str(n.get("notes", "")),
            }
            records.append(rec)
            t_recs.append(rec)
        grouped_records.append((t_key, t_meta, t_recs))

    return data, bib_nodes, pending_nodes, bib_edges, records, grouped_records


def fmt_link_list(items, empty_msg):
    if not items:
        return empty_msg
    return " | ".join(f"{x['name']} [{x['id']}] ({x['type']}/{x['relation_type']}: {x['label']})" for x in items)


def write_markdown_report(data, pending_nodes, bib_edges, records, grouped_records):
    meta = data["metadata"]
    edge_counts = Counter(e.get("relation_type", "parent_of") for e in bib_edges)
    node_type_counts = Counter(r["node_type"] for r in records)
    major_count = sum(1 for r in records if r["is_major"])
    pending_trads = Counter(n["tradition"] for n in pending_nodes)
    generated = dt.date.today().isoformat()

    lines = [
        f"# {meta['title']} — Exhaustive Biblical Lineage Compendium (AI-Parsed Edition)",
        "",
        f"- **Version:** {meta['version']}",
        f"- **Generated:** {generated}",
        "- **Scope:** Every deduplicated individual, dynasty cluster, and source reference connected to `bib_adam` (Adam & Eve)",
        f"- **Total Biblically Connected Records:** {len(records):,} (`person`: {node_type_counts.get('person', 0):,}, `dynasty_cluster`: {node_type_counts.get('dynasty_cluster', 0):,}, `source_meta`: {node_type_counts.get('source_meta', 0):,})",
        f"- **Major Landmarks:** {major_count:,}",
        f"- **Total Verified Edges:** {len(bib_edges):,} ({', '.join(f'{k}: {v:,}' for k, v in edge_counts.most_common())})",
        f"- **Pending Bridge Appendix (Excluded from Main Chapters):** {len(pending_nodes):,} non-DNA pre-Columbian Americas/Polynesia & unbridged global records ({', '.join(f'{k}: {v}' for k, v in pending_trads.most_common())})",
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
            steps_lbl = str(r["steps_from_adam"]) if r["steps_from_adam"] is not None else r["adam_path_mode"]
            lines.extend([
                f"### [{r['id']}] {r['name']}",
                f"- **Record Type:** `{r['node_type']}` | **Tradition:** {r['tradition_label']} (`{r['tradition']}`, {r['region']})",
                f"- **Era / Years:** {r['era_years']} | **Generation Tier:** {r['tier']} | **Major Landmark:** {'Yes' if r['is_major'] else 'No'} | **Steps From Adam:** {steps_lbl}",
                f"- **Role / Title:** {r['role']}",
                f"- **Alt / Cognate Names:** {alt_str}",
                f"- **Directed Lineage From Adam ({r['adam_path_mode']}):** {r['lineage_path_from_adam']}",
                f"- **Parents ({r['parent_count']}):** {fmt_link_list(r['parents'], 'None / Root or Preceding Anchor')}",
                f"- **Offspring ({r['offspring_count']}):** {fmt_link_list(r['offspring'], 'None / Terminal Leaf')}",
            ])
            if r["successors"]:
                lines.append(f"- **Dynastic / Office Successors ({r['successor_count']}):** {fmt_link_list(r['successors'], 'None')}")
            if r["spouses"]:
                lines.append(f"- **Spouses / Consorts ({r['spouse_count']}):** {fmt_link_list(r['spouses'], 'None')}")
            if r["historical_links"]:
                lines.append(f"- **Allies, Rivals & Contemporaries ({r['historical_count']}):** {fmt_link_list(r['historical_links'], 'None')}")
            if r["parallels"]:
                lines.append(f"- **Archetypal / Motif Parallels ({r['parallel_count']}):** {fmt_link_list(r['parallels'], 'None')}")
            lines.extend([
                f"- **Primary Sources:** {src_str}",
                f"- **Notes:** {r['notes']}",
                "",
            ])

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_csv_report(records):
    fieldnames = [
        "id",
        "name",
        "node_type",
        "alt_names",
        "tradition",
        "tradition_label",
        "region",
        "tier",
        "era_years",
        "role",
        "is_major",
        "adam_path_mode",
        "steps_from_adam",
        "lineage_path_from_adam",
        "parent_count",
        "parents",
        "offspring_count",
        "offspring",
        "successor_count",
        "successors",
        "spouse_count",
        "spouses",
        "historical_count",
        "historical_links",
        "parallel_count",
        "parallels",
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
                "node_type": r["node_type"],
                "alt_names": "; ".join(r["alt_names"]),
                "tradition": r["tradition"],
                "tradition_label": r["tradition_label"],
                "region": r["region"],
                "tier": r["tier"],
                "era_years": r["era_years"],
                "role": r["role"],
                "is_major": "TRUE" if r["is_major"] else "FALSE",
                "adam_path_mode": r["adam_path_mode"],
                "steps_from_adam": "" if r["steps_from_adam"] is None else r["steps_from_adam"],
                "lineage_path_from_adam": r["lineage_path_from_adam"],
                "parent_count": r["parent_count"],
                "parents": "; ".join(f"{p['name']} [{p['id']}]" for p in r["parents"]),
                "offspring_count": r["offspring_count"],
                "offspring": "; ".join(f"{k['name']} [{k['id']}]" for k in r["offspring"]),
                "successor_count": r["successor_count"],
                "successors": "; ".join(f"{s['name']} [{s['id']}] ({s['direction']})" for s in r["successors"]),
                "spouse_count": r["spouse_count"],
                "spouses": "; ".join(f"{s['name']} [{s['id']}]" for s in r["spouses"]),
                "historical_count": r["historical_count"],
                "historical_links": "; ".join(f"{h['name']} [{h['id']}]" for h in r["historical_links"]),
                "parallel_count": r["parallel_count"],
                "parallels": "; ".join(f"{p['name']} [{p['id']}]" for p in r["parallels"]),
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
  font-size: 8.1pt;
  line-height: 1.31;
  color: #1c1917;
  margin: 0;
  padding: 0;
}
.cover-box {
  border-top: 4px solid #b45309;
  border-bottom: 2px solid #d6d3d1;
  padding: 14px 0 10px 0;
  margin-bottom: 10px;
}
.cover-kicker {
  font-size: 8.2pt;
  font-weight: bold;
  color: #b45309;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
h1.title {
  font-family: "AtlasSerif", serif;
  font-size: 19pt;
  line-height: 1.15;
  color: #0f172a;
  margin: 0 0 6px 0;
}
.subtitle {
  font-size: 9.2pt;
  color: #44403c;
  margin: 0 0 7px 0;
}
h2.section {
  font-family: "AtlasSerif", serif;
  font-size: 11.8pt;
  color: #0f172a;
  border-bottom: 1.5px solid #b45309;
  padding-bottom: 2px;
  margin: 10px 0 5px 0;
}
h2.chap {
  font-family: "AtlasSerif", serif;
  font-size: 13.5pt;
  color: #0f172a;
  border-bottom: 2px solid #b45309;
  padding-bottom: 4px;
  margin: 0 0 4px 0;
}
.chap-meta {
  font-size: 7.9pt;
  color: #57534e;
  margin-bottom: 7px;
}
table.summary {
  width: 100%;
  border-collapse: collapse;
  font-size: 7.6pt;
  margin: 5px 0 8px 0;
}
table.summary th {
  background-color: #f3efe8;
  color: #1c1917;
  text-align: left;
  padding: 3.5px 5px;
  border-bottom: 1.5px solid #a8a29e;
  font-weight: bold;
}
table.summary td {
  padding: 2.5px 5px;
  border-bottom: 0.5px solid #e7e5e4;
}
.appendix-box {
  background-color: #fafaf9;
  border: 1px solid #d6d3d1;
  border-left: 3px solid #0284c7;
  padding: 6px 8px;
  font-size: 7.7pt;
  color: #292524;
  margin-top: 6px;
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
.rec-meta {
  border-left: 3px solid #64748b;
  background-color: #f8fafc;
}
.rec-head {
  font-size: 8.5pt;
  font-weight: bold;
  color: #0f172a;
  margin-bottom: 1.5px;
}
.rec-id {
  font-weight: normal;
  font-size: 7.2pt;
  color: #78716c;
}
.rec-badge {
  font-size: 7pt;
  font-weight: bold;
  color: #b45309;
}
.rec-type-badge {
  font-size: 6.9pt;
  font-weight: bold;
  color: #475569;
}
.rec-line {
  font-size: 7.6pt;
  color: #292524;
  margin: 1px 0;
}
.lbl { font-weight: bold; color: #44403c; }
.lbl-par { font-weight: bold; color: #0369a1; }
.lbl-kid { font-weight: bold; color: #9a3412; }
.lbl-suc { font-weight: bold; color: #0f766e; }
.lbl-sps { font-weight: bold; color: #be185d; }
.lbl-hst { font-weight: bold; color: #4338ca; }
.lbl-pll { font-weight: bold; color: #6d28d9; }
.rec-notes { font-size: 7.5pt; color: #44403c; margin: 1.5px 0; }
.rec-src { font-size: 7.1pt; color: #57534e; }
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


def build_cover_html(data, pending_nodes, bib_edges, records, grouped_records) -> str:
    meta = data["metadata"]
    rel_counts = Counter(e.get("relation_type", "parent_of") for e in bib_edges)
    node_types = Counter(r["node_type"] for r in records)
    major_count = sum(1 for r in records if r["is_major"])
    pending_trads = Counter(n["tradition"] for n in pending_nodes)
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

    rel_descriptions = {
        "parent_of": "Biological or traditional parent -> child descent",
        "successor_of": "Dynastic, royal, or episcopal office succession",
        "spouse_of": "Marriage, consort, or dynastic bridal alliance",
        "foe_or_ally_of": "Military rival, treaty ally, campaign, or diplomatic envoy",
        "contemporary_of": "Collateral kin (uncle/cousin/in-law), counselor, tutor, or source link",
        "motif_parallel": "Cross-cultural archetypal or longevity parallel (excluded from descent BFS)",
    }
    rel_rows = [
        f"<tr><td><b>{esc(k)}</b></td><td style='text-align:right'>{rel_counts.get(k, 0):,}</td>"
        f"<td>{esc(rel_descriptions[k])}</td></tr>"
        for k in ("parent_of", "successor_of", "spouse_of", "foe_or_ally_of", "contemporary_of", "motif_parallel")
    ]

    by_id = {r["id"]: r for r in records}
    stem_ids = [
        "bib_adam", "bib_seth", "bib_enoch", "bib_methuselah",
        "bib_noah", "bib_shem", "bib_ham", "bib_japheth",
        "bib_abraham", "jud_david", "nt_jesus",
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

    pending_summary = ", ".join(
        f"{data['traditions'].get(tk, {}).get('label', tk)}: {cnt}"
        for tk, cnt in pending_trads.most_common()
    )

    return f"""
    <div class="cover-box">
      <div class="cover-kicker">Universal World Genealogy Compendium &bull; Canonical Directed Edition</div>
      <h1 class="title">Ancient World Genealogy Atlas</h1>
      <p class="subtitle">Exhaustive Directed Prosopography of All {len(records):,} Deduplicated Biblically Connected Patriarchs, Monarchs, Queens, Prophets &amp; Sources ({esc(meta['version'])})</p>
      <p style="font-size:7.8pt;color:#57534e;margin:0;">
        <b>Generated:</b> {generated} &nbsp;|&nbsp;
        <b>Persons:</b> {node_types.get('person', 0):,} &nbsp;|&nbsp;
        <b>Dynasty Clusters:</b> {node_types.get('dynasty_cluster', 0):,} &nbsp;|&nbsp;
        <b>Source References:</b> {node_types.get('source_meta', 0):,} &nbsp;|&nbsp;
        <b>Major Landmarks:</b> {major_count:,} &nbsp;|&nbsp;
        <b>Edges:</b> {len(bib_edges):,}
      </p>
    </div>

    <h2 class="section">1. Executive Breakdown by Historical &amp; Scriptural Tradition</h2>
    <table class="summary">
      <thead><tr><th>#</th><th>Tradition Chapter</th><th>Region</th><th style="text-align:right">Records</th><th style="text-align:right">Major</th><th style="text-align:right">Semantic Links</th></tr></thead>
      <tbody>{''.join(trad_rows)}</tbody>
    </table>

    <h2 class="section">2. Semantic Edge Classification (Separation of Descent, Marriage &amp; History)</h2>
    <table class="summary">
      <thead><tr><th>Relation Type</th><th style="text-align:right">Edges</th><th>Definition</th></tr></thead>
      <tbody>{''.join(rel_rows)}</tbody>
    </table>

    <h2 class="section">3. Primeval Backbone Landmarks (Strictly Parent-Offspring Descent)</h2>
    <table class="summary">
      <thead><tr><th>Landmark Person</th><th>Horizon / Era</th><th style="text-align:right">Direct Offspring</th><th>Key Direct Descendants (parent_of only)</th></tr></thead>
      <tbody>{''.join(stem_rows)}</tbody>
    </table>

    <div class="appendix-box">
      <b>Appendix Note — Pending Bridge World Dynasties ({len(pending_nodes):,} records):</b> Independent Indigenous Americas &amp; Polynesia (Maya, Aztec, Inca, Hawaii, Aotearoa, Tonga) and unbridged regional chronicles ({esc(sanitize_pdf_text(pending_summary))}) are preserved in the Atlas's interactive <i>All</i> &amp; <i>Pending Bridge</i> views and are intentionally omitted from the canonically bridged main chapters above.
    </div>
    """


def format_pdf_record(r: dict) -> str:
    nt = r["node_type"]
    cls = "rec rec-meta" if nt == "source_meta" else ("rec rec-major" if r["is_major"] else "rec")
    badge = ' <span class="rec-badge">[MAJOR]</span>' if r["is_major"] else ""
    tbadge = f' <span class="rec-type-badge">({nt})</span>' if nt != "person" else ""
    alt = ", ".join(r["alt_names"]) if r["alt_names"] else ""
    src = "; ".join(r["sources"]) if r["sources"] else "Primary Archive"
    steps_txt = str(r["steps_from_adam"]) if r["steps_from_adam"] is not None else r["adam_path_mode"]

    def join_items(items, limit=8):
        txt = "; ".join(f"{x['name']} ({x['type']}: {x['label']})" for x in items[:limit])
        if len(items) > limit:
            txt += f"; +{len(items) - limit} more"
        return txt

    parts = [
        f'<div class="{cls}">',
        f'<div class="rec-head">{esc(sanitize_pdf_text(r["name"]))}{badge}{tbadge} <span class="rec-id">[{esc(r["id"])}]</span></div>',
        f'<div class="rec-line"><span class="lbl">Era:</span> {esc(sanitize_pdf_text(r["era_years"]))} &bull; '
        f'<span class="lbl">Tier:</span> {r["tier"]} &bull; '
        f'<span class="lbl">Steps from Adam:</span> {esc(steps_txt)} &bull; '
        f'<span class="lbl">Role:</span> {esc(sanitize_pdf_text(r["role"]))}</div>',
    ]
    if alt:
        parts.append(f'<div class="rec-line"><span class="lbl">Alt Names:</span> {esc(sanitize_pdf_text(alt))}</div>')
    parts.append(f'<div class="rec-line"><span class="lbl">Adam Path ({esc(r["adam_path_mode"])}):</span> {esc(sanitize_pdf_text(r["lineage_path_from_adam"]))}</div>')
    if r["parents"] or nt != "source_meta":
        par_txt = join_items(r["parents"], 6) if r["parents"] else "Root / Preceding Anchor"
        parts.append(f'<div class="rec-line"><span class="lbl-par">Parents ({r["parent_count"]}):</span> {esc(sanitize_pdf_text(par_txt))}</div>')
    if r["offspring"]:
        parts.append(f'<div class="rec-line"><span class="lbl-kid">Offspring ({r["offspring_count"]}):</span> {esc(sanitize_pdf_text(join_items(r["offspring"], 8)))}</div>')
    if r["successors"]:
        parts.append(f'<div class="rec-line"><span class="lbl-suc">Successors ({r["successor_count"]}):</span> {esc(sanitize_pdf_text(join_items(r["successors"], 6)))}</div>')
    if r["spouses"]:
        parts.append(f'<div class="rec-line"><span class="lbl-sps">Spouses / Consorts ({r["spouse_count"]}):</span> {esc(sanitize_pdf_text(join_items(r["spouses"], 5)))}</div>')
    if r["historical_links"]:
        parts.append(f'<div class="rec-line"><span class="lbl-hst">Allies / Rivals / Contemporaries ({r["historical_count"]}):</span> {esc(sanitize_pdf_text(join_items(r["historical_links"], 6)))}</div>')
    if r["parallels"]:
        parts.append(f'<div class="rec-line"><span class="lbl-pll">Motif Parallels ({r["parallel_count"]}):</span> {esc(sanitize_pdf_text(join_items(r["parallels"], 4)))}</div>')
    if r["notes"]:
        parts.append(f'<div class="rec-notes"><span class="lbl">Notes:</span> {esc(sanitize_pdf_text(r["notes"]))}</div>')
    parts.append(f'<div class="rec-src"><span class="lbl">Sources:</span> {esc(sanitize_pdf_text(src))}</div>')
    parts.append("</div>")
    return "".join(parts)


def write_pdf_report(data, pending_nodes, bib_edges, records, grouped_records) -> int:
    tmp_pdf = Path(tempfile.gettempdir()) / "awg_compendium_raw.pdf"
    font_dir = r"C:\Windows\Fonts"
    archive = pymupdf.Archive(font_dir) if os.path.isdir(font_dir) else None
    mediabox = pymupdf.paper_rect("letter")
    content_rect = mediabox + (42, 46, -42, -46)

    toc = []
    writer = pymupdf.DocumentWriter(str(tmp_pdf))
    current_page = 1

    cover_pages = render_story_pages(writer, archive, build_cover_html(data, pending_nodes, bib_edges, records, grouped_records), content_rect)
    toc.append([1, "Executive Summary & Provenance Overview", current_page])
    current_page += cover_pages

    chunk_size = 150
    for idx, (t_key, t_meta, t_recs) in enumerate(grouped_records, start=1):
        chap_title = f"{idx}. {t_meta['label']} ({len(t_recs):,} Records)"
        toc.append([1, sanitize_pdf_text(chap_title), current_page])
        for start in range(0, len(t_recs), chunk_size):
            batch = t_recs[start : start + chunk_size]
            if start == 0:
                header = (
                    f'<h2 class="chap">{esc(sanitize_pdf_text(chap_title))}</h2>'
                    f'<div class="chap-meta">Tradition Key: <b>{esc(t_key)}</b> &bull; Region: {esc(sanitize_pdf_text(t_meta["region"]))}</div>'
                )
            else:
                header = f'<div class="chap-meta"><i>Continued: {esc(sanitize_pdf_text(chap_title))}</i></div>'
            body_html = header + "".join(format_pdf_record(r) for r in batch)
            current_page += render_story_pages(writer, archive, body_html, content_rect)

    writer.close()
    del writer

    doc = pymupdf.open(str(tmp_pdf))
    total_pages = len(doc)
    doc.set_metadata({
        "title": "Ancient World Genealogy Atlas — Complete Canonical Compendium",
        "author": "Ancient World Genealogy Atlas",
        "subject": f"Exhaustive Directed Prosopography of {len(records)} Biblically Connected Records",
        "creator": "PyMuPDF Story Generator (v33.0)",
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
            f"Ancient World Genealogy Atlas (v{version_str}) -- Canonical Biblically Connected Compendium ({len(records):,} Records)",
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
    data, bib_nodes, pending_nodes, bib_edges, records, grouped_records = load_biblical_graph()

    print(f"Loaded {len(records)} biblically connected records and {len(bib_edges)} internal edges (Pending Bridge: {len(pending_nodes)}).")
    write_markdown_report(data, pending_nodes, bib_edges, records, grouped_records)
    print(f"Wrote Markdown: {OUT_MD.name} ({human_size(OUT_MD.stat().st_size)})")

    write_csv_report(records)
    print(f"Wrote CSV:      {OUT_CSV.name} ({human_size(OUT_CSV.stat().st_size)})")

    write_jsonl_report(records)
    print(f"Wrote JSONL:    {OUT_JSONL.name} ({human_size(OUT_JSONL.stat().st_size)})")

    pdf_pages = write_pdf_report(data, pending_nodes, bib_edges, records, grouped_records)
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
