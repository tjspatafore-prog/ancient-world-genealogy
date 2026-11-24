"""Shared node/edge builder helpers for modular genealogy scripts."""


def N(id_, name, tradition, tier, era, role, sources, notes, altNames=None, major=False):
    return {
        "id": id_,
        "name": name,
        "altNames": altNames or [],
        "tradition": tradition,
        "tier": tier,
        "era": era,
        "role": role,
        "sources": sources,
        "notes": notes,
        "major": major,
    }


def E(src, dst, typ, label):
    return {"from": src, "to": dst, "type": typ, "label": label}


def add_children(nodes, edges, parent_id, tradition, tier, era, items, default_edge="direct", default_sources=None):
    for item in items:
        cid, cname = item[0], item[1]
        extra = item[2] if len(item) > 2 else {}
        nodes.append(N(
            cid,
            cname,
            extra.get("tradition", tradition),
            extra.get("tier", tier),
            extra.get("era", era),
            extra.get("role", "Individual / Lineage Member"),
            extra.get("sources", default_sources or ["Primary Text"]),
            extra.get("notes", f"Listed descendant of {parent_id}."),
            altNames=extra.get("altNames", []),
            major=extra.get("major", False),
        ))
        edges.append(E(
            parent_id,
            cid,
            extra.get("edge_type", default_edge),
            extra.get("edge_label", f"Child ({', '.join(extra.get('sources', default_sources or ['Primary Text']))})"),
        ))


def add_chain(nodes, edges, items, start_parent=None, start_edge_type="direct", start_edge_label="Succession / Descent",
              tradition="biblical", default_edge_type="direct", default_sources=None):
    """Add a sequential dynastic/genealogical chain where each item links from the previous item."""
    prev_id = start_parent
    for idx, item in enumerate(items):
        cid, cname, tier, era, role, notes = item[:6]
        extra = item[6] if len(item) > 6 else {}
        nodes.append(N(
            cid,
            cname,
            extra.get("tradition", tradition),
            tier,
            era,
            role,
            extra.get("sources", default_sources or ["Primary Text"]),
            notes,
            altNames=extra.get("altNames", []),
            major=extra.get("major", False),
        ))
        parent = extra.get("parent", prev_id)
        if parent:
            et = start_edge_type if (idx == 0 and "edge_type" not in extra and start_parent) else extra.get("edge_type", default_edge_type)
            el = start_edge_label if (idx == 0 and "edge_label" not in extra and start_parent) else extra.get("edge_label", "Dynastic / Genealogical Succession")
            edges.append(E(parent, cid, et, el))
        prev_id = cid


def add_roster(nodes, edges, parent_id, prefix, tradition, tier, era, role, sources, items,
               edge_type="direct", edge_label="Dynastic / Lineage Member", chain=False):
    """
    Add a roster of individual people cleanly as individual searchable nodes (major=False by default).
    Each item can be a string 'Name' or tuple ('Name', 'Optional note/reign/alt') or dict.
    If chain=True, links parent_id -> item[0] -> item[1] -> ...; otherwise fans out from parent_id.
    """
    import re
    prev = parent_id
    used = set()
    for idx, item in enumerate(items):
        if isinstance(item, str):
            name, note, alt, maj = item, f"{role} ({era}).", [], False
        elif isinstance(item, tuple):
            name = item[0]
            note = item[1] if len(item) > 1 and item[1] else f"{role} ({era})."
            alt = item[2] if len(item) > 2 and item[2] else []
            maj = item[3] if len(item) > 3 else False
        else:
            name = item["name"]
            note = item.get("notes", f"{role} ({era}).")
            alt = item.get("altNames", [])
            maj = item.get("major", False)
        slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:28] or f"m{idx}"
        cid = f"{prefix}_{idx+1:02d}_{slug}"
        while cid in used:
            cid += "x"
        used.add(cid)
        nodes.append(N(cid, name, tradition, tier, era, role, sources, note, altNames=alt, major=maj))
        edges.append(E(prev if chain else parent_id, cid, edge_type, edge_label))
        if chain:
            prev = cid
    return prev

