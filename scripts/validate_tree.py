import json
from collections import Counter, deque
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "world_genealogy.json"


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

    print(f"VALIDATED OK: {len(nodes)} individuals/nodes, {len(edges)} edges")
    print("\nNodes by tradition:")
    for k, v in trad_counts.most_common():
        print(f"  - {traditions[k]['label']}: {v}")
    print("\nEdges by link type:")
    for k, v in edge_counts.most_common():
        print(f"  - {k}: {v}")

    # Verify index.html JS syntax & World Map pin nodeIds
    import re, subprocess, tempfile
    html_path = Path(__file__).resolve().parent.parent / "index.html"
    if html_path.exists():
        html = html_path.read_text(encoding="utf-8")
        js = re.findall(r"<script>([\s\S]*?)</script>", html)[-1]
        with tempfile.NamedTemporaryFile(suffix=".js", delete=False, mode="w", encoding="utf-8") as tmp:
            tmp.write(js)
            tmp_name = tmp.name
        r = subprocess.run(["node", "--check", tmp_name], capture_output=True, text=True)
        assert r.returncode == 0, f"JS syntax error: {r.stderr}"
        pins = re.findall(r'nodeId:"([^"]+)"', js)
        missing_pins = [p for p in pins if p not in nodes_by_id]
        assert not missing_pins, f"Broken World Map pin nodeIds: {missing_pins}"
        print(f"\nUI VERIFIED OK: JS syntax valid + all {len(pins)} World Map pins resolve cleanly")

    tests = [
        ("bib_moses", "eg_osarseph_bithiah", {"direct", "expansion", "cognate", "syncretic"}, "Moses -> Egyptian Osarseph / Musaeus / King of Cush"),
        ("bib_enoch", "eg_thoth_saurid", {"direct", "expansion", "cognate", "syncretic"}, "Enoch -> Egyptian Thoth / King Saurid"),
        ("jas_shu_bildad", "ved_bharata_kuru", {"direct", "expansion", "cognate"}, "Bildad (Abraham->Shuah, Jasher 25) -> Pandavas (Strict Textual + Cognates Only)"),
        ("jas_tog_tarki", "chn_yu_xia", {"direct", "expansion", "cognate", "syncretic"}, "Tarki (Japheth->Togarmah, Jasher 10) -> Chinese Xia Dynasty"),
        ("jud_solomon", "eth_menelik", {"direct", "expansion"}, "King Solomon + Sheba -> Menelik I of Ethiopia"),
        ("jas_janeus", "bib_kittim", {"direct", "expansion", "syncretic"}, "Janeus (Esau->Eliphaz->Zepho, Jasher 62) -> Kittim (Italy/Rome)"),
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
