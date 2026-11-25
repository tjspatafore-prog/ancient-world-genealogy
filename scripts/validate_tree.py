import json
from collections import Counter, deque
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "world_genealogy.json"


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def find_reachable(nodes_by_id, edges, start_id, allowed_types):
    adj = {nid: [] for nid in nodes_by_id}
    for e in edges:
        if e["type"] in allowed_types:
            adj[e["from"]].append(e["to"])
            adj[e["to"]].append(e["from"])
    q = deque([start_id])
    visited = {start_id}
    while q:
        curr = q.popleft()
        for nxt in adj[curr]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return visited


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

    # Verify index.html JS syntax, World Map pin nodeIds & World Map arc endpoints
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
        pin_ids = set(re.findall(r'\{\s*id:"(pin_[^"]+)"', js))
        arc_refs = re.findall(r'from:"(pin_[^"]+)",\s*to:"(pin_[^"]+)"', js)
        bad_arcs = [(a, b) for a, b in arc_refs if a not in pin_ids or b not in pin_ids]
        assert not bad_arcs, f"Broken World Map arc pin IDs: {bad_arcs}"
        print(f"\nUI VERIFIED OK: JS syntax valid + all {len(pins)} World Map pins & {len(arc_refs)} arcs resolve cleanly")

    # Enforce 100% Adam & Noahic connectivity across every non-DNA node
    non_dna_ids = {n["id"] for n in nodes if n["tradition"] != "dna"}
    reachable_adam = find_reachable(nodes_by_id, edges, "bib_adam", {"direct", "expansion", "cognate", "syncretic"})
    reachable_noah = find_reachable(nodes_by_id, edges, "bib_noah", {"direct", "expansion", "cognate", "syncretic"})
    disc_adam = sorted(non_dna_ids - reachable_adam)
    disc_noah = sorted(non_dna_ids - reachable_noah)
    assert not disc_adam, f"Non-DNA nodes not connected to Adam: {disc_adam[:10]}"
    assert not disc_noah, f"Non-DNA nodes not connected to Noah: {disc_noah[:10]}"
    print(f"NOAHIC CONNECTIVITY GATE OK: 100% of all {len(non_dna_ids)} non-DNA nodes trace directly/syncretically to Adam & Noah (0 disconnected)")

    tests = [
        ("bib_noah", "rus_vladimir_great", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Slavs & Rus' -> St. Vladimir of Kiev"),
        ("bib_noah", "irl_niall_brian_boru", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Magog -> Fenius Farsa -> Milesius -> Niall & Brian Boru"),
        ("bib_noah", "chn_masudi_abur_lotsatis", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> 'Abur -> Lotsatis (1st King of China in Mas'udi)"),
        ("bib_noah", "chn_fuxi_nuwa", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Yonton (4th Son) / Fo-hi -> Fuxi & Nüwa (China)"),
        ("bib_noah", "arm_hayk_pat", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Togarmah -> Hayk (Armenia)"),
        ("bib_noah", "ber_branes_botr", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Ham -> Canaan -> Mazigh -> Berber Branes & Botr"),
        ("bib_noah", "sud_jaaliyyin_abbas", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Shem -> Abraham -> Ishmael -> Muhammad -> Ja'aliyyin of Sudan"),
        ("bib_noah", "tib_nyatri_songtsen", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Vaivasvata Manu -> Mahasammata/Okkaka -> Nyatri Tsenpo (Tibet)"),
        ("bib_moses", "eg_osarseph_bithiah", {"direct", "expansion", "cognate", "syncretic"}, "Moses -> Egyptian Osarseph / Musaeus / King of Cush"),
        ("jud_solomon", "eth_menelik", {"direct", "expansion"}, "King Solomon + Sheba -> Menelik I of Ethiopia"),
        ("bib_noah", "mug_akbar_aurangzeb", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Turk -> Oghuz -> Genghis Khan -> Timur -> Babur -> Mughal Emperors"),
        ("bib_noah", "ott_mehmed2_suleiman", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Turk/Oghuz -> Seljuks -> Osman I -> Suleiman the Magnificent"),
        ("bib_noah", "eng_stuart_great_britain", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Wessex/Scottish/Tudor Lines -> King James I of Great Britain"),
        ("bib_noah", "por_braganza_restoration", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Tubal/Iberia -> Afonso I Henriques -> Aviz & Braganza of Portugal"),
        ("bib_noah", "rus_romanov_peter_great", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Russ/Slavs -> Rurik -> Yaroslav -> Romanovs & Peter the Great"),
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
