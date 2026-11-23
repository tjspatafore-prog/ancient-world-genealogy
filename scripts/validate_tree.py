import json
from collections import Counter, deque
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "genealogy_core.json"


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def find_path(nodes_by_id, edges, start_id, end_id, allowed_types):
    adj = {nid: [] for nid in nodes_by_id}
    for e in edges:
        if e["type"] in allowed_types:
            adj[e["from"]].append((e["to"], e))
            adj[e["to"]].append((e["from"], e))
    q = deque([(start_id, [(start_id, None)])])
    visited = {start_id}
    while q:
        curr, path = q.popleft()
        if curr == end_id:
            return path
        for nxt, edge in adj[curr]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [(nxt, edge)]))
    return None


def main():
    data = load_data()
    nodes = data["nodes"]
    edges = data["edges"]
    traditions = data["traditions"]

    nodes_by_id = {}
    for n in nodes:
        assert n["id"] not in nodes_by_id, f"Duplicate node ID: {n['id']}"
        assert n["tradition"] in traditions, f"Unknown tradition: {n['tradition']}"
        nodes_by_id[n["id"]] = n

    for idx, e in enumerate(edges):
        assert e["from"] in nodes_by_id, f"Edge {idx} missing from: {e['from']}"
        assert e["to"] in nodes_by_id, f"Edge {idx} missing to: {e['to']}"
        assert e["type"] in data["metadata"]["linkTypes"], f"Unknown edge type: {e['type']}"

    trad_counts = Counter(n["tradition"] for n in nodes)
    edge_counts = Counter(e["type"] for e in edges)

    print(f"VALIDATED OK: {len(nodes)} nodes, {len(edges)} edges")
    print("\nNodes by tradition:")
    for k, v in trad_counts.most_common():
        print(f"  - {traditions[k]['label']}: {v}")
    print("\nEdges by link type:")
    for k, v in edge_counts.most_common():
        print(f"  - {k}: {v}")

    # Test cross-tradition paths
    tests = [
        ("bib_isaac_jacob", "ved_bharata_kuru", {"direct", "expansion", "cognate"}, "Israelites -> Pandavas (Strict Textual + Historical Cognate Only)"),
        ("bib_isaac_jacob", "chn_shang_zhou", {"direct", "expansion", "cognate", "syncretic"}, "Israelites -> Shang/Zhou China (Incl. Chronicler Bridges)"),
        ("ar_ishmael_adnan", "mes_uruk_gilgamesh", {"direct", "expansion", "cognate"}, "Arabian Adnanites -> Gilgamesh of Uruk (Strict Textual + Cognate)"),
        ("ir_yima", "ved_surya_vamsha", {"direct", "expansion", "cognate"}, "Iranian Jamshid -> Rama/Buddha Solar Dynasty (Proto-Indo-Iranian Cognate)"),
        ("chn_yu_xia", "stp_oghuz", {"direct", "expansion", "cognate", "syncretic"}, "Chinese Xia Dynasty -> Turkic Oghuz Khagan"),
        ("bib_abraham", "le_sanchuniathon", {"direct", "expansion", "cognate"}, "Abraham -> Phoenician Misor/Thoth (Strict Textual + Cognate)"),
    ]

    print("\nSample Cross-Tradition Ancestry Paths:")
    for s, t, allowed, title in tests:
        path = find_path(nodes_by_id, edges, s, t, allowed)
        print(f"\n[{title}]")
        if not path:
            print("  No path found under selected link types.")
        else:
            for step_i, (nid, edge) in enumerate(path):
                prefix = "  START: " if step_i == 0 else f"  --({edge['type']}: {edge['label']})--> "
                print(f"{prefix}{nodes_by_id[nid]['name']}")


if __name__ == "__main__":
    main()
