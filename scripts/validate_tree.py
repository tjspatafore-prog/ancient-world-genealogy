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

    # Enforce Adam & Noahic connectivity across all core/Noahic modules while tracking Pending Bridge items
    non_dna_ids = {n["id"] for n in nodes if n["tradition"] != "dna"}
    reachable_adam = find_reachable(nodes_by_id, edges, "bib_adam", {"direct", "expansion", "cognate", "syncretic"})
    reachable_noah = find_reachable(nodes_by_id, edges, "bib_noah", {"direct", "expansion", "cognate", "syncretic"})
    assert reachable_adam == reachable_noah, "Adam and Noah reachable sets must match"

    bib_conn_ids = set()
    pending_ids = set()
    for n in nodes:
        assert isinstance(n.get("biblicalConnected"), bool), f"Missing biblicalConnected bool on {n['id']}"
        assert n["biblicalConnected"] == (n["id"] in reachable_adam), f"Mismatched biblicalConnected on {n['id']}"
        if n["tradition"] != "dna":
            if n["biblicalConnected"]:
                bib_conn_ids.add(n["id"])
            else:
                pending_ids.add(n["id"])

    unexpected_pending = [nid for nid in sorted(pending_ids) if not (nid.startswith("amp_") or nid.startswith("unb_") or nid in {"afr_buganda_kintu", "afr_kongo_lukeni", "afr_zimbabwe_mutota", "sea_khmer_jayavarman2", "sea_java_raden_wijaya"})]
    assert not unexpected_pending, f"Unexpected non-DNA nodes disconnected from Adam/Noah: {unexpected_pending[:10]}"
    dna_total = sum(1 for n in nodes if n["tradition"] == "dna")
    print(f"SCOPE GATE OK: {len(bib_conn_ids)} Biblically Connected + {len(pending_ids)} Pending Bridge (All non-DNA={len(non_dna_ids)}, DNA={dna_total})")

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
        ("bib_noah", "sng_sonni_askia_timbuktu", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Shem/Joktan (Yemen) -> Za-Al-Ayaman -> Sonni Ali & Askia the Great (Songhai/Timbuktu)"),
        ("bib_noah", "esp_ferdinand_isabella_habsburg", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Tubal (Mariana 1699) -> Visigoths -> Pelayo -> Ferdinand & Isabella"),
        ("bib_noah", "pal_odenathus_zenobia", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Shem -> King Solomon (Tadmor/Palmyra) -> Aretas -> Queen Zenobia"),
        ("bib_noah", "asm_records_past_inscriptions", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Shem -> Asshur -> George Smith Eponym Canon & Records of the Past (Sennacherib/Hezekiah)"),
        ("bib_noah", "mal_parameswara_iskandar", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Javan -> Alexander (Iskandar Zulkarnain) -> Malay Annals -> Parameswara (Malacca!)"),
        ("bib_adam", "cb_sopanim_2enoch", {"direct", "expansion"}, "Adam -> Seth -> Lamech -> Nir + Sopanim -> Melchizedek (2 Enoch 70-71)"),
        ("bib_noah", "eur_ice_erik_leif", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Norse Ynglings -> Ingolfur Arnarson (Iceland) -> Erik the Red -> Leif Erikson (Vinland)"),
        ("bib_noah", "tib_ladakh_sengge_namgyal", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Tibet Yarlung -> Skyid-lde Nyi-ma-mgon -> Sengge Namgyal (Ladakh)"),
        ("bib_noah", "ind_raj_mewar_sisodia", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Vaivasvata Manu -> Rama -> Lava -> Bappa Rawal -> Maharana Pratap (Mewar Rajputs)"),
        ("bib_noah", "stp_moghul_said_haidar", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Japheth -> Turk -> Genghis Khan -> Chagatai -> Tughlugh Timur -> Tarikh-i-Rashidi (Moghulistan)"),
        ("bib_esau", "jos_haman_amalekite", {"direct", "expansion"}, "Esau -> Eliphaz -> Amalek -> King Agag -> Haman (Josephus Ant. VI.7 & XI.6)"),
        ("bib_esau", "jos_herod_armenia_cilicia", {"direct", "expansion"}, "Esau -> Idumea -> Herod the Great -> Kings Tigranes V/VI of Armenia & Roman Consuls"),
        ("bib_abraham", "jos_sparta_lycurgus_leonidas", {"direct", "expansion", "cognate", "syncretic"}, "Abraham -> Sparta Charter (1 Macc 12:21 / Josephus XII.4.10) -> King Leonidas I"),
        ("bib_abraham", "grk_heracles", {"direct", "expansion", "cognate", "syncretic"}, "Abraham + Keturah -> Epher (Africa) -> Heracles Marriage (Josephus Ant. I.15)"),
        ("bib_noah", "eur42_jadwiga_jagiello", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Rus' Yaroslav -> Poland/Hungary -> Queen Jadwiga & Jagiello (Lithuania)"),
        ("bib_noah", "fam_washington_jefferson", {"direct", "expansion", "cognate", "syncretic"}, "Noah -> Wessex -> Edward III -> George Washington & Thomas Jefferson"),
        ("jud_perez", "jud_david", {"direct", "expansion"}, "Perez -> Hezron -> Ram -> Amminadab -> Nahshon -> Salmon -> Boaz -> Obed -> Jesse -> King David (Individual)"),
        ("jud_david", "dav_zerubbabel", {"direct", "expansion"}, "King David -> Solomon -> Individual 20 Kings of Judah -> Jehoiachin -> Zerubbabel"),
        ("has_mattathias", "jos_tigranes6_armenia", {"direct", "expansion"}, "Mattathias -> Simon Thassi -> John Hyrcanus I -> Jannaeus -> Hyrcanus II -> Alexandra -> Mariamne I -> Prince Alexander -> Armenia Tigranes VI"),
        ("bib_abraham", "tri_dan", {"direct", "expansion"}, "Abraham -> Rotheus -> Bilhah -> Tribe of Dan (Testament of Naphtali / Ginzberg)"),
        ("chr41_sheshan_jarha_egypt", "chr2_elishama", {"direct", "expansion"}, "Sheshan -> Ahlai + Jarha the Egyptian -> 13-Generation Pedigree to Elishama (1 Chr 2:34-41)"),
        ("pri_eleazar_zadok", "bib16_pri_14_high_priest_onias_iv_built_l", {"direct", "expansion"}, "Zadok I -> ... -> Jehozadak -> Jeshua -> Jaddua -> Onias I -> Simon I -> Onias II -> Simon II -> Onias III -> Onias IV"),
        ("eg_menes", "grk_aegyptus_danaus", {"direct", "expansion", "syncretic"}, "Menes -> Dynasties I–XVIII -> Horemheb/Harmais -> Danaus (Manetho Fr. 50/53)"),
        ("grk_inachus_io", "jos_sparta_lycurgus_leonidas", {"direct", "expansion", "cognate", "syncretic"}, "Inachus -> Perseus -> Heracles -> Eurysthenes -> Agiad Kings of Sparta (Leonidas I)"),
        ("grk_aeneas", "grk_romulus_remus", {"direct", "expansion"}, "Aeneas -> Silvius -> 14 Kings of Alba Longa -> Numitor -> Rhea Silvia -> Romulus"),
        ("rom3_julius_caesar", "mon_rom_caligula", {"direct", "expansion"}, "Julius Caesar -> Julia Minor -> Atia -> Octavia Minor -> Antonia Minor -> Germanicus -> Caligula"),
        ("cls3_abibaal", "cls3_hannibal_barca", {"direct", "expansion"}, "Abibaal -> Hiram I -> Ethbaal I -> Mattan I -> Dido (Carthage) -> Hamilcar -> Hannibal Barca"),
        ("eg_ptolemies_complete", "cls3_ptolemy_mauretania", {"direct", "expansion"}, "Ptolemies -> Cleopatra VII -> Cleopatra Selene II -> King Ptolemy of Mauretania"),
        ("akl_01_tudiya", "aklr_neo_17_ashur_uballit_ii_612_609_bce", {"direct", "expansion"}, "Tudiya -> Adasi -> Ashur-uballit I -> Shalmaneser III -> Sennacherib -> Ashur-uballit II (Complete AKL)"),
        ("mes_hammurabi", "babr_10_06_crown_prince_belshazzar_dani", {"direct", "expansion"}, "Hammurabi -> Samsu-iluna -> Kassites -> Nabopolassar -> Nebuchadnezzar II -> Nabonidus -> Belshazzar"),
        ("per4_achaemenes", "grk_alexander", {"direct", "expansion", "cognate"}, "Achaemenes -> Cyrus the Great -> Atossa + Darius I -> Xerxes I -> Darius III -> Stateira II + Alexander"),
        ("bib_togarmah", "mod_geo_giorgi_2011", {"direct", "expansion", "syncretic"}, "Togarmah -> Kartlos -> Parnavaz I -> Mirian III -> Vakhtang Gorgasali -> Bagrationis -> Living Prince Giorgi (2011)"),
        ("tab_adnan_21gen_quraysh", "mod_abdullah2_hussein_iman", {"direct", "expansion"}, "Adnan -> 21-Gen Quraysh -> Prophet Muhammad -> Fatimah -> Hasan -> 24 Qatadid Sharifs -> Living King Abdullah II"),
        ("ar4_abd_shams", "mon_isl_abdarrahman1", {"direct", "expansion"}, "Abd Shams -> Umayyah -> Marwan I -> Abd al-Malik -> Hisham -> Abd al-Rahman I of Cordoba"),
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
