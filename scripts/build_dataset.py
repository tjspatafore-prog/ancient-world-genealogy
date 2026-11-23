"""
Modular Ancient World Genealogy Dataset Builder & Validator (Phase 2).

Generates clean modular JSON files under data/modules/ and compiles them into
data/world_genealogy.json for the interactive web explorer, ensuring zero broken
links, full provenance tagging, and exhaustive individual person accounting.
"""

import json
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = ROOT / "data" / "modules"
OUT_ALL = ROOT / "data" / "world_genealogy.json"
OUT_CORE = ROOT / "data" / "genealogy_core.json"

TRADITIONS = {
    "archetype":    {"label": "Global Convergence Hubs",        "region": "Worldwide Comparative Layer", "color": "#6366f1", "order": 0},
    "levant_egypt": {"label": "Egyptian & Canaanite-Phoenician","region": "Nile / Eastern Mediterranean", "color": "#0d9488", "order": 1},
    "biblical":     {"label": "Biblical & Extra-Biblical",      "region": "Levant / Ancient Near East",   "color": "#d97706", "order": 2},
    "arabian":      {"label": "Arabian (Adnanite & Qahtanite)", "region": "Arabian Peninsula",            "color": "#ca8a04", "order": 3},
    "mesopotamian": {"label": "Mesopotamian (Sumer / Akkad)",   "region": "Mesopotamia",                  "color": "#2563eb", "order": 4},
    "iranian":      {"label": "Iranian / Zoroastrian",          "region": "Iranian Plateau / Central Asia","color": "#9333ea", "order": 5},
    "vedic":        {"label": "Vedic & Puranic Indian",         "region": "South Asia / Indus-Ganges",    "color": "#ea580c", "order": 6},
    "steppe":       {"label": "Eurasian Steppe / Turkic",       "region": "Inner Asia / Eurasian Steppe", "color": "#059669", "order": 7},
    "chinese":      {"label": "Ancient Chinese (Sinitic)",      "region": "East Asia / Yellow River",     "color": "#dc2626", "order": 8},
    "japan_korea":  {"label": "Ancient Japanese & Korean",      "region": "East Asia / Archipelago",      "color": "#db2777", "order": 9},
}

LINK_TYPES = {
    "direct":    "Explicit parent-child or biological descent within primary canonical/ancient texts",
    "expansion": "Matriarchs, additional children, intermediate links, or migrations supplied by extra-biblical or secondary chronicles (Book of Jasher, Jubilees, 1 Enoch, Qumran, Shiji, Puranas)",
    "cognate":   "Linguistically or historically attested cross-tradition identity/ethnonym bridge (e.g., Vedic Vivasvan = Avestan Vivanghant; Biblical Madai = Medes; Mizraim = Phoenician Misor/Egypt)",
    "parallel":  "Independent structural/archetypal parallel across ancient corpora (Great Flood survivors, 7th antediluvian sage, tripartite world division)",
    "syncretic": "Ancient, Greco-Egyptian, or medieval chronicler identification bridging figures across cultures (e.g., Enoch = Thoth/Saurid; Moses = Osarseph/Musaeus; Japheth = Oghuz Khagan; Zepho = King of Kittim/Rome)"
}


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
    """Helper to register a batch of individual children under a parent node cleanly."""
    for item in items:
        if isinstance(item, tuple):
            cid, cname = item[0], item[1]
            extra = item[2] if len(item) > 2 else {}
        else:
            raise ValueError("Item must be tuple")
        nodes.append(N(
            cid,
            cname,
            extra.get("tradition", tradition),
            extra.get("tier", tier),
            extra.get("era", era),
            extra.get("role", "Individual / Tribal Eponym"),
            extra.get("sources", default_sources or ["Genesis"]),
            extra.get("notes", f"Listed descendant of {parent_id}."),
            altNames=extra.get("altNames", []),
            major=extra.get("major", False),
        ))
        edges.append(E(
            parent_id,
            cid,
            extra.get("edge_type", default_edge),
            extra.get("edge_label", f"Child ({', '.join(extra.get('sources', default_sources or ['Genesis']))})"),
        ))


def build_module_01_antediluvian():
    nodes, edges = [], []

    # Global Archetype Hubs
    nodes += [
        N("hub_primordial", "Primordial Human Ancestors", "archetype", 0, "Primordial / Creation",
          "Comparative Convergence Hub", ["Comparative Mythology"],
          "Structural hub linking the first humans fashioned from clay, earth, or cosmic life across Near Eastern, Indo-Iranian, and East Asian texts.",
          ["First Couple Archetype"], major=True),
        N("hub_flood", "Great Flood / Cataclysm Survivors", "archetype", 4, "Flood Horizon",
          "Comparative Convergence Hub", ["Genesis 6-9", "Atrahasis", "Gilgamesh XI", "Shatapatha Brahmana 1.8.1", "Vendidad 2", "Shangshu"],
          "Global ancestral bottleneck motif where a righteous survivor preserves humanity and restarts post-cataclysm lineages.",
          ["Diluvial Bottleneck"], major=True),
        N("hub_world_division", "Post-Flood Division of Nations", "archetype", 5, "Early Post-Flood",
          "Comparative Convergence Hub", ["Genesis 10", "Jubilees 8-9", "Book of Jasher 7 & 10", "Shahnameh", "Mahabharata", "Shiji Ch. 1"],
          "Genealogical maps dividing humanity across Eurasia and Africa through sons of a universal ancestor.",
          ["Ancient Tables of Nations"], major=True),
    ]

    # Adam, Eve & Children
    nodes += [
        N("bib_adam", "Adam & Eve (Hawwah)", "biblical", 1, "Creation (Gen 1-5)",
          "Primeval Progenitors", ["Genesis 2-5", "Jubilees 3-4", "Book of Jasher 1"],
          "First human couple. Book of Jasher 1:12-13 notes they bore two sons (Cain, Abel) and three daughters; Jubilees 4 explicitly names their daughters Awan and Azura.",
          ["Adamah", "Hawwah"], major=True),
        N("bib_abel", "Abel (Hevel)", "biblical", 2, "Antediluvian Gen 2",
          "Second Son of Adam & Eve", ["Genesis 4:2-8", "Jubilees 4:1-4", "Book of Jasher 1:12-25"],
          "Shepherd slain by Cain. In Jasher 1:13-25 the conflict involves the division of fields, flocks, and twin sisters.",
          ["Hevel", "Habil"]),
        N("bib_cain", "Cain (Qayin) & Awan", "biblical", 2, "Antediluvian Gen 2",
          "Firstborn / Builder of City of Enoch", ["Genesis 4:1-17", "Jubilees 4:9", "Book of Jasher 1"],
          "Founder of the Cainite line. Jubilees 4:9 names his wife Awan (his sister). Jasher 2:26-27 recounts his accidental death by blind Lamech's arrow.",
          ["Qayin", "Wife: Awan (Jub 4:9)"], major=True),
        N("bib_seth", "Seth (Shet) & Azura", "biblical", 2, "Antediluvian Gen 2",
          "Sethite Patriarch", ["Genesis 4:25, 5:3", "Jubilees 4:11", "Book of Jasher 2:1", "Josephus Ant. 1.2.3"],
          "Appointed in place of Abel. Jubilees 4:11 names his wife Azura. Josephus credits Seth's descendants with inventing astronomy and inscribing it on two pillars to survive flood and fire.",
          ["Shet", "Wife: Azura (Jub 4:11)"], major=True),
    ]
    edges += [
        E("hub_primordial", "bib_adam", "parallel", "Primeval couple from dust/adamah"),
        E("bib_adam", "bib_cain", "direct", "Firstborn son (Gen 4:1); wife Awan (Jub 4:9)"),
        E("bib_adam", "bib_abel", "direct", "Second son (Gen 4:2)"),
        E("bib_adam", "bib_seth", "direct", "Son (Gen 4:25); wife Azura (Jub 4:11)"),
    ]

    # Full Cainite Line (individual nodes!)
    cain_chain = [
        ("bib_cain_enoch", "Enoch (son of Cain)", "bib_cain", "Gen 4:17; Jasher 1:35", "Eponym of the first city built by Cain."),
        ("bib_irad", "Irad", "bib_cain_enoch", "Gen 4:18; Jasher 2:16", "Son of Cainite Enoch."),
        ("bib_mehujael", "Mehujael", "bib_irad", "Gen 4:18; Jasher 2:16", "Son of Irad."),
        ("bib_methushael", "Methushael", "bib_mehujael", "Gen 4:18; Jasher 2:17", "Son of Mehujael; father of Cainite Lamech."),
        ("bib_cain_lamech", "Lamech (Cainite)", "bib_methushael", "Gen 4:18-24; Jasher 2:17-37", "Marries Adah and Zillah (daughters of Sethite Cainan in Jasher 2:18!). Father of Jabal, Jubal, Tubal-cain, and Naamah."),
    ]
    for cid, cname, pid, src, note in cain_chain:
        nodes.append(N(cid, cname, "biblical", 3, "Antediluvian Cainite Line", "Cainite Descendant", src.split("; "), note, major=(cid == "bib_cain_lamech")))
        edges.append(E(pid, cid, "direct", f"Son ({src})"))

    add_children(nodes, edges, "bib_cain_lamech", "biblical", 3, "Antediluvian Gen 8 (Cainite)", [
        ("bib_jabal", "Jabal", {"sources": ["Genesis 4:20", "Book of Jasher 2:20"], "role": "Father of Nomadic Herders", "notes": "Son of Lamech & Adah; father of those who dwell in tents and keep livestock."}),
        ("bib_jubal", "Jubal", {"sources": ["Genesis 4:21", "Book of Jasher 2:20"], "role": "Father of Musicians", "notes": "Son of Lamech & Adah; inventor of harp and flute/organ."}),
        ("bib_tubalcain", "Tubal-cain", {"sources": ["Genesis 4:22", "Book of Jasher 2:25-27"], "role": "Master of Bronze & Iron Metallurgy", "notes": "Son of Lamech & Zillah. Jasher 2:26-27 relates how he guided blind Lamech's bow, accidentally killing Cain before being slain by Lamech."}),
        ("bib_naamah_cain", "Naamah (dau. of Lamech)", {"sources": ["Genesis 4:22", "Genesis Rabbah 23:3"], "role": "Sister of Tubal-cain", "notes": "Named in Genesis 4:22. Rabbinic tradition (Genesis Rabbah 23:3) identifies her as Noah's wife (while Book of Jasher 5:15 names Noah's wife as Naamah daughter of Enoch)."}),
    ])

    # Full Sethite Antediluvian Line (individual nodes + ALL Jasher children!)
    nodes += [
        N("bib_enosh", "Enosh & Noam", "biblical", 2, "Antediluvian Gen 3", "3rd Patriarch",
          ["Genesis 5:6-11", "Jubilees 4:13", "Book of Jasher 2:2-7"],
          "Jubilees 4:13 names his wife Noam. Jasher 2:4-7 says idol worship began in his days and the sea (Gihon) flooded a third of the earth.",
          ["Enos", "Wife: Noam (Jub 4:13)"]),
        N("bib_kenan", "Kenan (Cainan) & Mualeleth", "biblical", 2, "Antediluvian Gen 4", "4th Patriarch",
          ["Genesis 5:9-14", "Jubilees 4:14", "Book of Jasher 2:8-15"],
          "Jubilees 4:14 names his wife Mualeleth. Book of Jasher 2:11-12 says Kenan ruled wisely, inscribed prophecies of the Flood on stone tablets, and fathered 3 sons (Mahalalel, Enan, Mered) and 2 daughters (Adah, Zillah).",
          ["Cainan", "Wife: Mualeleth (Jub 4:14)"], major=True),
        N("bib_mahalalel", "Mahalalel & Dinah", "biblical", 3, "Antediluvian Gen 5", "5th Patriarch",
          ["Genesis 5:12-17", "Jubilees 4:15", "Book of Jasher 2:11-15"],
          "Jubilees 4:15 names his wife Dinah, daughter of Barakiel.",
          ["Maleleel", "Wife: Dinah (Jub 4:15)"]),
        N("bib_jared", "Jared (Yered) & Baraka", "biblical", 3, "Antediluvian Gen 6", "6th Patriarch",
          ["Genesis 5:15-20", "1 Enoch 6:6", "Jubilees 4:15-16", "Book of Jasher 2:37"],
          "Jubilees 4:16 names his wife Baraka (dau. of Rasujal). 1 Enoch 6 and Jubilees 4:15 connect his name ('descent') to the descent of the Watchers on Mount Hermon.",
          ["Yered", "Wife: Baraka (Jub 4:16)"], major=True),
        N("bib_enoch", "Enoch (Khanokh) & Edni", "biblical", 3, "Antediluvian Gen 7 (365 yrs)", "7th Patriarch / Scribe of Righteousness",
          ["Genesis 5:21-24", "1 Enoch 1-108", "Jubilees 4:17-25", "Book of Jasher 3"],
          "7th from Adam; lived 365 years and ascended to heaven. Jubilees 4:17 credits him as first to learn writing, calendar, and astronomy. Book of Jasher 3:1 names his 3 sons (Methuselah, Elisha, Elimelech) and 2 daughters (Melca, Nahmah/Naamah). Widely equated in Greco-Egyptian & Arabic lore with Thoth/Hermes/King Saurid and compared to 7th Sumerian king Enmeduranki!",
          ["Idris (Arabic)", "Thoth / Hermes (Syncretic)", "King Saurid (Egyptian-Arabic lore)", "Wife: Edni (Jub 4:20)"], major=True),
        N("bib_methuselah", "Methuselah & Edna", "biblical", 3, "Antediluvian Gen 8 (969 yrs)", "8th Patriarch / Longest-Lived",
          ["Genesis 5:25-27", "1 Enoch 82 & 106", "Jubilees 4:27", "Book of Jasher 3-5"],
          "Custodian of Enoch's books. Jubilees 4:27 names his wife Edna. Jasher 5:35 also names his son Eliakim, whose 3 daughters marry Noah's 3 sons!",
          ["Metushelach", "Wife: Edna (Jub 4:27)"], major=True),
        N("bib_lamech_seth", "Lamech (Sethite) & Betenos / Ashmua", "biblical", 3, "Antediluvian Gen 9", "9th Patriarch / Father of Noah",
          ["Genesis 5:28-31", "1 Enoch 106", "Genesis Apocryphon (1Q20)", "Jubilees 4:28", "Book of Jasher 4:11-14"],
          "Jubilees 4:28 names his wife Betenos; Book of Jasher 4:11 names her Ashmua, daughter of Elisha son of Enoch! 1 Enoch 106 & Qumran 1Q20 recount his awe at Noah's luminous birth.",
          ["Wife: Betenos (Jub)", "Wife: Ashmua (Jasher 4:11)"]),
        N("bib_noah", "Noah (Noach) & Emzara / Naamah", "biblical", 4, "Flood Horizon (Gen 6-9)", "10th Patriarch / Universal Post-Flood Ancestor",
          ["Genesis 5:29-9:29", "Jubilees 4:33, 5-10", "1 Enoch 106", "Book of Jasher 4-6"],
          "Called Noah by Lamech and Menahem by Methuselah (Jasher 4:14). Jubilees 4:33 names his wife Emzara; Jasher 5:15 names her Naamah daughter of Enoch (while Genesis Rabbah identifies her with Cainite Naamah). Father of Japheth, Ham, and Shem.",
          ["Nuh (Arabic)", "Menahem (Jasher 4:14)", "Wife: Emzara (Jub) / Naamah (Jasher)"], major=True),
    ]
    edges += [
        E("bib_seth", "bib_enosh", "direct", "Son (Gen 4:26; 5:6)"),
        E("bib_enosh", "bib_kenan", "direct", "Son (Gen 5:9)"),
        E("bib_kenan", "bib_mahalalel", "direct", "Son (Gen 5:12; Jasher 2:11)"),
        E("bib_mahalalel", "bib_jared", "direct", "Son (Gen 5:15)"),
        E("bib_jared", "bib_enoch", "direct", "Son (Gen 5:18)"),
        E("bib_enoch", "bib_methuselah", "direct", "Son (Gen 5:21; Jasher 3:1)"),
        E("bib_methuselah", "bib_lamech_seth", "direct", "Son (Gen 5:25; Jasher 4:1)"),
        E("bib_lamech_seth", "bib_noah", "direct", "Son (Gen 5:28-29; Jasher 4:14)"),
        E("bib_naamah_cain", "bib_noah", "expansion", "Genesis Rabbah 23:3 identifies Cainite Naamah as Noah's wife"),
        E("hub_flood", "bib_noah", "parallel", "Ark on Ararat (Genesis / Jubilees / Jasher)"),
    ]

    # Extra-Biblical children of Kenan (Jasher 2:11)
    add_children(nodes, edges, "bib_kenan", "biblical", 3, "Antediluvian Gen 5 (Jasher)", [
        ("jas_enan", "Enan (son of Kenan)", {"edge_type": "expansion", "sources": ["Book of Jasher 2:11"], "notes": "Listed in Book of Jasher 2:11 as one of Kenan's three sons alongside Mahalalel and Mered."}),
        ("jas_mered", "Mered (son of Kenan)", {"edge_type": "expansion", "sources": ["Book of Jasher 2:11"], "notes": "Listed in Book of Jasher 2:11 as one of Kenan's three sons."}),
        ("jas_adah_kenan", "Adah (dau. of Kenan)", {"edge_type": "expansion", "sources": ["Book of Jasher 2:11, 2:18"], "notes": "In Book of Jasher 2:18, Adah daughter of Sethite Kenan marries Cainite Lamech (mother of Jabal & Jubal), bridging the Sethite and Cainite lines!"}),
        ("jas_zillah_kenan", "Zillah (dau. of Kenan)", {"edge_type": "expansion", "sources": ["Book of Jasher 2:11, 2:18"], "notes": "In Book of Jasher 2:18, Zillah daughter of Sethite Kenan marries Cainite Lamech (mother of Tubal-cain & Naamah)."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 2:11"])
    edges += [
        E("jas_adah_kenan", "bib_cain_lamech", "expansion", "Jasher 2:18: marries Cainite Lamech (Sethite-Cainite union)"),
        E("jas_zillah_kenan", "bib_cain_lamech", "expansion", "Jasher 2:18: marries Cainite Lamech (Sethite-Cainite union)"),
    ]

    # Extra-Biblical children of Enoch (Jasher 3:1) & Methuselah (Jasher 5:35)
    add_children(nodes, edges, "bib_enoch", "biblical", 3, "Antediluvian Gen 8 (Jasher)", [
        ("jas_elisha_enoch", "Elisha (son of Enoch)", {"sources": ["Book of Jasher 3:1, 4:11"], "notes": "Son of Enoch in Jasher 3:1; father of Ashmua, who marries Lamech and births Noah (Jasher 4:11)!"}),
        ("jas_elimelech_enoch", "Elimelech (son of Enoch)", {"sources": ["Book of Jasher 3:1"], "notes": "One of three sons of Enoch named in Book of Jasher 3:1."}),
        ("jas_melca_enoch", "Melca (dau. of Enoch)", {"sources": ["Book of Jasher 3:1"], "notes": "Daughter of Enoch named in Book of Jasher 3:1."}),
        ("jas_naamah_enoch", "Naamah (dau. of Enoch)", {"sources": ["Book of Jasher 3:1, 5:15"], "notes": "Named in Book of Jasher 3:1 & 5:15 as daughter of Enoch who marries Noah (at age 580) and becomes mother of Shem, Ham, and Japheth!"}),
    ], default_edge="expansion", default_sources=["Book of Jasher 3:1"])
    edges += [
        E("jas_naamah_enoch", "bib_noah", "expansion", "Jasher 5:15: Wife of Noah"),
        E("jas_elisha_enoch", "bib_lamech_seth", "expansion", "Jasher 4:11: Daughter Ashmua marries Lamech"),
    ]

    add_children(nodes, edges, "bib_methuselah", "biblical", 3, "Antediluvian Gen 9 (Jasher)", [
        ("jas_eliakim", "Eliakim (son of Methuselah)", {"sources": ["Book of Jasher 5:35"], "notes": "Named in Book of Jasher 5:35 as son of Methuselah whose three daughters Noah chose as wives for Shem, Ham, and Japheth."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 5:35"])

    # 1 Enoch Watchers & Qumran Book of Giants
    nodes += [
        N("eno_watchers", "The Watchers (Semyaza & Azazel)", "biblical", 3, "Antediluvian Gen 6 (1 Enoch)",
          "Angelic Watchers (Grigori)", ["Genesis 6:1-4", "1 Enoch 6-16", "Jubilees 5:1-10"],
          "200 Watchers descend on Mount Hermon in the days of Jared; chiefs include Semyaza, Azazel (metallurgy/weapons), Araqiel, Kokabiel, Baraqiel, Armaros, Penemue, and Gadreel.",
          ["Grigori", "Bene Elohim"], major=True),
        N("eno_ohya_hahya", "Ohya & Hahya (Nephilim Giants)", "biblical", 3, "Antediluvian (Book of Giants)",
          "Sons of Semyaza", ["Qumran Book of Giants (4Q530, 4Q531)", "1 Enoch 7"],
          "Named Giant brothers in the Dead Sea Scrolls Book of Giants who dream of the impending Flood and send Mahaway to ask Enoch to interpret it.",
          ["Ohyah & Hahyah", "Nephilim"]),
        N("eno_mahaway", "Mahaway (Giant Messenger)", "biblical", 3, "Antediluvian (Book of Giants)",
          "Son of Watcher Baraqiel", ["Qumran Book of Giants (4Q530)"],
          "Winged Giant son of Baraqiel who flies across the world to consult Enoch on behalf of the Nephilim."),
    ]
    edges += [
        E("bib_jared", "eno_watchers", "expansion", "1 Enoch 6:6: Watchers descend on Mt. Hermon in Jared's days"),
        E("eno_watchers", "eno_ohya_hahya", "expansion", "Semyaza + human wives -> Nephilim/Giants (4Q530)"),
        E("eno_watchers", "eno_mahaway", "expansion", "Baraqiel -> Mahaway (Qumran Book of Giants)"),
        E("eno_mahaway", "bib_enoch", "expansion", "Consults Enoch to interpret the Giants' Flood dreams (4Q530)"),
    ]

    return {"module": "01_antediluvian", "title": "Primordial Hubs & Biblical/Extra-Biblical Antediluvian Era", "nodes": nodes, "edges": edges}


def build_module_02_table_of_nations():
    nodes, edges = [], []

    # Three Sons of Noah
    nodes += [
        N("bib_ham", "Ham (Cham) & Na'eltama'uk", "biblical", 5, "Post-Flood Gen 1", "Progenitor of Cush, Mizraim, Phut, Canaan",
          ["Genesis 10:6-20", "Jubilees 7:16, 8:22-24", "Book of Jasher 7:10-13"],
          "Assigned Africa and southern lands in Jubilees 8. Father of Cush, Mizraim (Egypt), Phut (Libya/Punt), and Canaan.",
          ["Cham", "Wife: Na'eltama'uk (Jub 7:16)"], major=True),
        N("bib_shem", "Shem (Sem) & Sedeqetelebab", "biblical", 5, "Post-Flood Gen 1", "Progenitor of Semitic & Near Eastern Nations",
          ["Genesis 10:21-31", "Jubilees 7:16, 8:12-21", "Book of Jasher 7:14-22"],
          "Assigned central Asia from the Mediterranean to India (Tinas) in Jubilees 8. Father of Elam, Asshur, Arphaxad, Lud, and Aram.",
          ["Sam (Arabic)", "Wife: Sedeqetelebab (Jub 7:16)"], major=True),
        N("bib_japheth", "Japheth (Yefet) & Adataneses", "biblical", 5, "Post-Flood Gen 1", "Progenitor of Northern Eurasian Nations",
          ["Genesis 10:2-5", "Jubilees 7:16, 8:25-30", "Book of Jasher 7:3-9, 10"],
          "Assigned Europe, Anatolia, Iranian highlands, and Northern Eurasia in Jubilees 8. Father of Gomer, Magog, Madai, Javan, Tubal, Meshech, and Tiras.",
          ["Yefet", "Yafith (Arabic)", "Wife: Adataneses (Jub 7:16)"], major=True),
    ]
    edges += [
        E("bib_noah", "bib_ham", "direct", "Son (Gen 9:18); wife Na'eltama'uk (Jub 7:16)"),
        E("bib_noah", "bib_shem", "direct", "Son (Gen 9:18); wife Sedeqetelebab (Jub 7:16)"),
        E("bib_noah", "bib_japheth", "direct", "Son (Gen 9:18); wife Adataneses (Jub 7:16)"),
        E("jas_eliakim", "bib_shem", "expansion", "Jasher 5:35: Noah's sons marry 3 daughters of Eliakim"),
        E("hub_world_division", "bib_ham", "parallel", "Table of Nations: Southern/African Zone"),
        E("hub_world_division", "bib_shem", "parallel", "Table of Nations: Central/Near Eastern Zone"),
        E("hub_world_division", "bib_japheth", "parallel", "Table of Nations: Northern Eurasian Zone"),
    ]

    # ---------------- JAPHETH (ALL 7 SONS + ALL GENESIS & JASHER 7/10 CHILDREN) ----------------
    add_children(nodes, edges, "bib_japheth", "biblical", 6, "Post-Flood Gen 2 (Japheth)", [
        ("bib_gomer", "Gomer", {"major": True, "sources": ["Genesis 10:2-3", "Book of Jasher 7:3, 10:8"], "role": "Eponym of Cimmerians (Gimirrai)", "notes": "Father of Ashkenaz, Riphath, and Togarmah. Jasher 10:8 locates his descendants along the Franca/European rivers."}),
        ("bib_magog", "Magog", {"major": True, "sources": ["Genesis 10:2", "Ezekiel 38", "Book of Jasher 7:4"], "role": "Northern Steppe / Scythian Anchor", "notes": "Josephus identifies Magog with the Scythians; Jasher 7:4 names his sons Elichanaf and Lubal."}),
        ("bib_madai", "Madai (Medes)", {"major": True, "sources": ["Genesis 10:2", "Jubilees 9:9, 10:35", "Book of Jasher 7:5"], "role": "Eponym of Iranian Medes (Mada)", "notes": "Direct historical cognate of the Medes. Jubilees 10:35 says Madai married a daughter of Shem and settled the Iranian plateau. Jasher 7:5 lists his 4 sons: Achon, Zeelo, Chazoni, Lot."}),
        ("bib_javan", "Javan (Ionians / Greeks)", {"major": True, "sources": ["Genesis 10:2-4", "Book of Jasher 7:6, 10:15"], "role": "Eponym of Greeks (Iawones)", "notes": "Linguistic cognate of Ionia. Father of Elishah, Tarshish, Kittim, and Dodanim."}),
        ("bib_tubal", "Tubal", {"sources": ["Genesis 10:2", "Book of Jasher 7:7, 10:12"], "role": "Anatolian Tabal / Iberia", "notes": "Jasher 7:7 names his 3 sons: Ariphi, Kesed, Taari (Jasher 10:12 places Tubal in Tuscany/Pisa)."}),
        ("bib_meshech", "Meshech", {"sources": ["Genesis 10:2", "Book of Jasher 7:8"], "role": "Anatolian Mushki / Phrygia", "notes": "Jasher 7:8 names his 3 sons: Dedon, Zaron, Shebashni."}),
        ("bib_tiras", "Tiras", {"sources": ["Genesis 10:2", "Book of Jasher 7:9, 10:14"], "role": "Thracians / Tyrsenians", "notes": "Jasher 7:9 names his 4 sons: Benib, Gera, Lupirion, Gilak (Jasher 10:14 links Tiras to Rushash/Kushni/Ongolis)."}),
    ])

    # Children of Gomer + Togarmah's 10 Jasher sons!
    add_children(nodes, edges, "bib_gomer", "biblical", 7, "Post-Flood Gen 3 (Gomer)", [
        ("bib_ashkenaz", "Ashkenaz", {"sources": ["Genesis 10:3", "Book of Jasher 7:3, 10:9"], "role": "Scythians (Ashkuza) / Ashkenaz", "notes": "Assyrian Ashkuza (Scythians); later medieval Jewish name for Rhineland/Germany."}),
        ("bib_riphath", "Riphath (Rephath)", {"sources": ["Genesis 10:3", "Book of Jasher 7:3, 10:9"], "role": "Son of Gomer", "notes": "Associated by Josephus with Paphlagonia; Jasher 10:9 connects Rephath with Western Europe (Bartonim/Bretons)."}),
        ("bib_togarmah", "Togarmah", {"major": True, "sources": ["Genesis 10:3", "Book of Jasher 7:3, 10:10"], "role": "Armenian & Turkic-Steppe Ancestor (Jasher 10)", "notes": "Armenian chronicles (Moses of Chorene) trace Armenians to Togarmah; Book of Jasher 10:10 (via Josippon) lists 10 sons representing Turkic, Bulgar, Khazar, Pecheneg, and Hungarian steppe tribes!"}),
    ])
    add_children(nodes, edges, "bib_togarmah", "biblical", 8, "Post-Flood Gen 4 (Jasher 10:10)", [
        ("jas_tog_buzar", "Buzar (Cozar / Khazars)", {"notes": "Son of Togarmah in Book of Jasher 10:10; linked to the Khazars."}),
        ("jas_tog_parzunac", "Parzunac (Pechenegs)", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_balgar", "Balgar (Bulgars)", {"notes": "Son of Togarmah in Book of Jasher 10:10; linked to the Volga/Danube Bulgars."}),
        ("jas_tog_elicanum", "Elicanum", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_ragbib", "Ragbib", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_tarki", "Tarki (Turks)", {"major": True, "notes": "Son of Togarmah in Book of Jasher 10:10 — explicit Jasher/Josippon bridge from Japheth to the Turkic peoples of the Eurasian Steppe!"}),
        ("jas_tog_bid", "Bid", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_zebuc", "Zebuc", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_ongal", "Ongal (Onogurs / Hungarians)", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
        ("jas_tog_tilmaz", "Tilmaz", {"notes": "Son of Togarmah in Book of Jasher 10:10."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 10:10"])

    # Jasher 7 children of Magog, Madai, Tubal, Meshech, Tiras
    add_children(nodes, edges, "bib_magog", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:4)", [
        ("jas_mag_elichanaf", "Elichanaf", {"notes": "Son of Magog listed in Book of Jasher 7:4."}),
        ("jas_mag_lubal", "Lubal", {"notes": "Son of Magog listed in Book of Jasher 7:4."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:4"])

    add_children(nodes, edges, "bib_madai", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:5)", [
        ("jas_mad_achon", "Achon", {"notes": "Son of Madai listed in Book of Jasher 7:5."}),
        ("jas_mad_zeelo", "Zeelo", {"notes": "Son of Madai listed in Book of Jasher 7:5."}),
        ("jas_mad_chazoni", "Chazoni", {"notes": "Son of Madai listed in Book of Jasher 7:5."}),
        ("jas_mad_lot", "Lot (son of Madai)", {"notes": "Son of Madai listed in Book of Jasher 7:5."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:5"])

    add_children(nodes, edges, "bib_javan", "biblical", 7, "Post-Flood Gen 3 (Javan)", [
        ("bib_elishah", "Elishah", {"sources": ["Genesis 10:4", "Book of Jasher 7:6, 10:15"], "notes": "Historically Alashiya (Cyprus); Jasher 10:15 links his descendants to the Almanim/Lombards."}),
        ("bib_tarshish", "Tarshish", {"sources": ["Genesis 10:4", "Book of Jasher 7:6"], "notes": "Mediterranean maritime center (Tartessos in Spain or Tarsus in Cilicia)."}),
        ("bib_kittim", "Kittim (Chittim)", {"major": True, "sources": ["Genesis 10:4", "Book of Jasher 7:6, 10:16, 61"], "notes": "Historically Kition (Cyprus) and western Mediterranean islands. In Book of Jasher 10:16 & 61, Kittim settles Italy/Rome (Romim), where Esau's grandson Zepho becomes king!"}),
        ("bib_dodanim", "Dodanim (Rodanim)", {"sources": ["Genesis 10:4", "1 Chronicles 1:7", "Book of Jasher 7:6, 10:17"], "notes": "Historically Rhodes (Rodanim in 1 Chr 1:7/LXX); Jasher 10:17 links them to Mediterranean coastal peoples."}),
    ])

    add_children(nodes, edges, "bib_tubal", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:7)", [
        ("jas_tub_ariphi", "Ariphi", {"notes": "Son of Tubal in Book of Jasher 7:7."}),
        ("jas_tub_kesed", "Kesed", {"notes": "Son of Tubal in Book of Jasher 7:7."}),
        ("jas_tub_taari", "Taari", {"notes": "Son of Tubal in Book of Jasher 7:7."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:7"])

    add_children(nodes, edges, "bib_meshech", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:8)", [
        ("jas_mes_dedon", "Dedon", {"notes": "Son of Meshech in Book of Jasher 7:8."}),
        ("jas_mes_zaron", "Zaron", {"notes": "Son of Meshech in Book of Jasher 7:8."}),
        ("jas_mes_shebashni", "Shebashni", {"notes": "Son of Meshech in Book of Jasher 7:8."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:8"])

    add_children(nodes, edges, "bib_tiras", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:9)", [
        ("jas_tir_benib", "Benib", {"notes": "Son of Tiras in Book of Jasher 7:9."}),
        ("jas_tir_gera", "Gera", {"notes": "Son of Tiras in Book of Jasher 7:9."}),
        ("jas_tir_lupirion", "Lupirion", {"notes": "Son of Tiras in Book of Jasher 7:9."}),
        ("jas_tir_gilak", "Gilak", {"notes": "Son of Tiras in Book of Jasher 7:9."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:9"])

    # ---------------- HAM (ALL 4 SONS + ALL GENESIS & JASHER 7 CHILDREN) ----------------
    add_children(nodes, edges, "bib_ham", "biblical", 6, "Post-Flood Gen 2 (Ham)", [
        ("bib_cush", "Cush (Kush)", {"major": True, "sources": ["Genesis 10:6-8", "Book of Jasher 7:10, 23"], "role": "Eponym of Nubia/Ethiopia & Father of Nimrod", "notes": "Progenitor of Seba, Havilah, Sabtah, Raamah, Sabteca, and Nimrod. Jasher 7:24 says Cush inherited Adam's garments from Ham and gave them to Nimrod."}),
        ("bib_mizraim", "Mizraim (Egypt)", {"major": True, "sources": ["Genesis 10:6, 13-14", "Book of Jasher 7:11, 10:25"], "role": "Eponym of Egypt (Misor)", "notes": "Hebrew/Semitic name for Egypt, cognate with Phoenician Misor (Sanchuniathon) and Coptic/Arabic Misrayim/Baysar."}),
        ("bib_phut", "Phut (Put)", {"sources": ["Genesis 10:6", "Book of Jasher 7:12"], "role": "Eponym of Libya / Punt", "notes": "Jasher 7:12 names his 4 sons: Gebul, Hadan, Benah, and Adan."}),
        ("bib_canaan", "Canaan", {"major": True, "sources": ["Genesis 10:6, 15-19", "Book of Jasher 7:13"], "role": "Eponym of Levantine & Phoenician Peoples", "notes": "Father of 11 Levantine nations including Sidon (Phoenicia), Heth (Hittites), and the Sinites."}),
    ])

    add_children(nodes, edges, "bib_cush", "biblical", 7, "Post-Flood Gen 3 (Cush)", [
        ("bib_seba", "Seba", {"sources": ["Genesis 10:7", "Book of Jasher 7:10"], "notes": "Son of Cush; linked to Upper Nile / Meroe / Red Sea coast."}),
        ("bib_havilah_cush", "Havilah (son of Cush)", {"sources": ["Genesis 10:7", "Book of Jasher 7:10"], "notes": "Son of Cush; associated with Red Sea / SW Arabian-African gold lands."}),
        ("bib_sabtah", "Sabtah", {"sources": ["Genesis 10:7", "Book of Jasher 7:10"], "notes": "Son of Cush (often linked to Shabwah in Hadhramaut)."}),
        ("bib_raamah", "Raamah", {"sources": ["Genesis 10:7", "Book of Jasher 7:10"], "notes": "Son of Cush; father of Sheba and Dedan."}),
        ("bib_sabteca", "Sabteca", {"sources": ["Genesis 10:7", "Book of Jasher 7:10"], "notes": "Son of Cush."}),
        ("bib_nimrod", "Nimrod (Mighty Hunter of Shinar)", {"major": True, "sources": ["Genesis 10:8-12", "Book of Jasher 7:23-48, 11-12", "Josephus Ant. 1.4"], "role": "King of Babel, Erech (Uruk), Accad & Nineveh", "notes": "Crucial Biblical-Mesopotamian bridge: Gen 10:10 links him to Shinar (Sumer), Babel, Erech (Uruk), Accad (Akkad), and Nineveh. Jasher 7:47 names his son Mardon, and Jasher 27 narrates Esau slaying Nimrod!"}),
    ])
    add_children(nodes, edges, "bib_raamah", "biblical", 8, "Post-Flood Gen 4 (Raamah)", [
        ("bib_sheba_raamah", "Sheba (son of Raamah)", {"sources": ["Genesis 10:7"], "notes": "Grandson of Cush via Raamah; Arabian/Red Sea trade lineage."}),
        ("bib_dedan_raamah", "Dedan (son of Raamah)", {"sources": ["Genesis 10:7"], "notes": "Grandson of Cush via Raamah; NW Arabian oasis of Dedan (Al-Ula)."}),
    ])
    add_children(nodes, edges, "bib_nimrod", "biblical", 8, "Post-Flood Gen 4 (Jasher 7:47)", [
        ("jas_mardon", "Mardon (son of Nimrod)", {"sources": ["Book of Jasher 7:47-48"], "notes": "Named in Book of Jasher 7:47 as Nimrod's son, 'more wicked than his father', origin of the proverb 'from the wicked goeth forth wickedness'."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:47"])

    add_children(nodes, edges, "bib_mizraim", "biblical", 7, "Post-Flood Gen 3 (Mizraim)", [
        ("bib_ludim", "Ludim", {"sources": ["Genesis 10:13", "Book of Jasher 7:11"], "notes": "Descendant of Mizraim; Egyptian/North African archer peoples."}),
        ("bib_anamim", "Anamim", {"sources": ["Genesis 10:13", "Book of Jasher 7:11, 10:25"], "notes": "Descendant of Mizraim; Jasher 10:25 places Anamim in Alexandria/coastal Egypt."}),
        ("bib_lehabim", "Lehabim", {"sources": ["Genesis 10:13", "Book of Jasher 7:11"], "notes": "Libyans / western Nile delta peoples."}),
        ("bib_naphtuhim", "Naphtuhim", {"sources": ["Genesis 10:13", "Book of Jasher 7:11"], "notes": "Lower Egypt / Memphis ('People of Ptah' — Na-Ptah!)."}),
        ("bib_pathrusim", "Pathrusim", {"sources": ["Genesis 10:14", "Book of Jasher 7:11"], "notes": "Upper Egypt (Egyptian Pa-to-ris, 'the Southland')."}),
        ("bib_casluhim", "Casluhim (→ Philistines)", {"sources": ["Genesis 10:14", "Book of Jasher 7:11"], "notes": "Genesis 10:14 notes 'from whom came the Philistines'."}),
        ("bib_caphtorim", "Caphtorim (Crete)", {"sources": ["Genesis 10:14", "Book of Jasher 7:11"], "notes": "Historically Keftiu / Minoan Crete, linked to Sea Peoples / Philistines."}),
    ])

    add_children(nodes, edges, "bib_phut", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:12)", [
        ("jas_phut_gebul", "Gebul", {"notes": "Son of Phut listed in Book of Jasher 7:12."}),
        ("jas_phut_hadan", "Hadan", {"notes": "Son of Phut listed in Book of Jasher 7:12."}),
        ("jas_phut_benah", "Benah", {"notes": "Son of Phut listed in Book of Jasher 7:12."}),
        ("jas_phut_adan", "Adan", {"notes": "Son of Phut listed in Book of Jasher 7:12."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:12"])

    add_children(nodes, edges, "bib_canaan", "biblical", 7, "Post-Flood Gen 3 (Canaan)", [
        ("bib_sidon", "Sidon (Zidon)", {"sources": ["Genesis 10:15", "Book of Jasher 7:13"], "notes": "Firstborn of Canaan; eponym of Phoenician Sidon."}),
        ("bib_heth", "Heth (Hittites)", {"sources": ["Genesis 10:15", "Book of Jasher 7:13"], "notes": "Eponym of the Hittites / Children of Heth (from whom Abraham purchased Machpelah)."}),
        ("bib_jebusite", "Jebusite (Jebusi)", {"sources": ["Genesis 10:16", "Book of Jasher 7:13"], "notes": "Pre-Israelite inhabitants of Jerusalem (Jebus)."}),
        ("bib_amorite", "Amorite (Emori)", {"sources": ["Genesis 10:16", "Book of Jasher 7:13"], "notes": "Western Semitic Amurru peoples of Syria and Canaan."}),
        ("bib_girgashite", "Girgashite (Girgashi)", {"sources": ["Genesis 10:16", "Book of Jasher 7:13"], "notes": "Canaanite nation listed in Genesis 10:16."}),
        ("bib_hivite", "Hivite (Hivi)", {"sources": ["Genesis 10:17", "Book of Jasher 7:13"], "notes": "Inhabitants of Shechem, Gibeon, and Mt. Hermon foothills."}),
        ("bib_arkite", "Arkite (Arki)", {"sources": ["Genesis 10:17", "Book of Jasher 7:13"], "notes": "Ancient city of Arqa in northern Lebanon."}),
        ("bib_sinite", "Sinite (Sini)", {"sources": ["Genesis 10:17", "Book of Jasher 7:13"], "notes": "Coastal Phoenician city of Sinna/Siannu (later speculated by early European writers as China/Sinim, though historically Levantine)."}),
        ("bib_arvadite", "Arvadite (Arvadi)", {"sources": ["Genesis 10:18", "Book of Jasher 7:13"], "notes": "Phoenician island city of Arwad (Syria)."}),
        ("bib_zemarite", "Zemarite (Zemari)", {"sources": ["Genesis 10:18", "Book of Jasher 7:13"], "notes": "Ancient Syrian coastal city of Sumur/Simyra."}),
        ("bib_hamathite", "Hamathite (Hamathi)", {"sources": ["Genesis 10:18", "Book of Jasher 7:13"], "notes": "Ancient Syrian kingdom of Hamath (Hama) on the Orontes."}),
    ])

    # ---------------- SHEM (ALL 5 SONS + ALL GENESIS, JUBILEES & JASHER 7 CHILDREN) ----------------
    add_children(nodes, edges, "bib_shem", "biblical", 6, "Post-Flood Gen 2 (Shem)", [
        ("bib_elam", "Elam", {"major": True, "sources": ["Genesis 10:22", "Book of Jasher 7:15"], "role": "Eponym of Elam (SW Iran / Susa)", "notes": "Historical kingdom of Elam in SW Iran. Book of Jasher 7:15 names his 3 sons: Shushan (Susa!), Machul, and Harmon."}),
        ("bib_asshur", "Asshur", {"major": True, "sources": ["Genesis 10:22", "Book of Jasher 7:16"], "role": "Eponym of Assyria (Ashur)", "notes": "Historical Assyria. Book of Jasher 7:16 names his 2 sons: Mirus and Mokil."}),
        ("bib_arphaxad", "Arphaxad (Arpachshad)", {"major": True, "sources": ["Genesis 10:22-24", "Jubilees 8:1", "Book of Jasher 7:17"], "role": "Ancestor of Eber, Hebrews & Arabs", "notes": "Father of Shelach (and Cainan in LXX/Jubilees 8:1). Book of Jasher 7:17 also names his sons Anar and Ashcol."}),
        ("bib_lud", "Lud", {"sources": ["Genesis 10:22", "Book of Jasher 7:18"], "role": "Eponym of Lydia (Anatolia)", "notes": "Book of Jasher 7:18 names his 2 sons: Pethor and Bizayon."}),
        ("bib_aram", "Aram", {"major": True, "sources": ["Genesis 10:22-23", "Book of Jasher 7:19"], "role": "Eponym of Arameans / Syria", "notes": "Father of Uz, Hul, Gether, and Mash."}),
    ])

    add_children(nodes, edges, "bib_elam", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:15)", [
        ("jas_elam_shushan", "Shushan (Susa)", {"notes": "Son of Elam in Book of Jasher 7:15 — eponym of the historical Elamite capital Susa!"}),
        ("jas_elam_machul", "Machul", {"notes": "Son of Elam in Book of Jasher 7:15."}),
        ("jas_elam_harmon", "Harmon", {"notes": "Son of Elam in Book of Jasher 7:15."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:15"])

    add_children(nodes, edges, "bib_asshur", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:16)", [
        ("jas_ass_mirus", "Mirus", {"notes": "Son of Asshur in Book of Jasher 7:16."}),
        ("jas_ass_mokil", "Mokil", {"notes": "Son of Asshur in Book of Jasher 7:16."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:16"])

    add_children(nodes, edges, "bib_lud", "biblical", 7, "Post-Flood Gen 3 (Jasher 7:18)", [
        ("jas_lud_pethor", "Pethor", {"notes": "Son of Lud in Book of Jasher 7:18."}),
        ("jas_lud_bizayon", "Bizayon", {"notes": "Son of Lud in Book of Jasher 7:18."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 7:18"])

    add_children(nodes, edges, "bib_aram", "biblical", 7, "Post-Flood Gen 3 (Aram)", [
        ("bib_uz_aram", "Uz (son of Aram)", {"sources": ["Genesis 10:23", "Book of Jasher 7:19"], "notes": "Often connected with the Land of Uz (Book of Job) / Damascus region."}),
        ("bib_hul", "Hul", {"sources": ["Genesis 10:23", "Book of Jasher 7:19"], "notes": "Son of Aram; linked to Huleh valley or Armenia (Josephus)."}),
        ("bib_gether", "Gether", {"sources": ["Genesis 10:23", "Book of Jasher 7:19"], "notes": "Son of Aram; linked in Arab tradition to Thamud/Jadhis."}),
        ("bib_mash", "Mash (Meshech)", {"sources": ["Genesis 10:23", "Book of Jasher 7:19"], "notes": "Son of Aram; associated with Mount Masius in Upper Mesopotamia."}),
    ])

    # Arphaxad -> Cainan (LXX/Jub) -> Shelah -> Eber -> Peleg & ALL 13 sons of Joktan!
    add_children(nodes, edges, "bib_arphaxad", "biblical", 7, "Post-Flood Gen 3 (Arphaxad)", [
        ("jub_cainan_post", "Cainan (son of Arphaxad)", {"edge_type": "expansion", "sources": ["Jubilees 8:1-4", "Septuagint Gen 10:24", "Luke 3:36"], "notes": "Present in Jubilees and Septuagint; Jubilees 8:3 says he discovered an antediluvian rock inscription of the Watchers' astrological teachings."}),
        ("bib_shelah", "Shelah (Salah)", {"major": True, "sources": ["Genesis 10:24, 11:12", "Book of Jasher 7:17"], "notes": "Father of Eber (son of Arphaxad in Masoretic/Jasher; son of Cainan in Jubilees/LXX)."}),
        ("jas_anar", "Anar (son of Arphaxad)", {"edge_type": "expansion", "sources": ["Book of Jasher 7:17"], "notes": "Additional son of Arphaxad listed in Book of Jasher 7:17."}),
        ("jas_ashcol", "Ashcol (son of Arphaxad)", {"edge_type": "expansion", "sources": ["Book of Jasher 7:17"], "notes": "Additional son of Arphaxad listed in Book of Jasher 7:17."}),
    ])
    edges.append(E("jub_cainan_post", "bib_shelah", "expansion", "Father of Shelah in Jubilees 8:5 & LXX"))

    nodes += [
        N("bib_eber", "Eber (Hud)", "biblical", 7, "Post-Flood Gen 5", "Eponym of Hebrews ('Ivrim) & Southern Arabs",
          ["Genesis 10:24-25, 11:14-17", "Jubilees 8:7", "Book of Jasher 7:20-21"],
          "Eponym of the Hebrews and identified in Arabian tradition with Prophet Hud. Father of Peleg and Joktan (Qahtan).",
          ["Hud (Arabian)", "Heber"], major=True),
        N("bib_peleg", "Peleg", "biblical", 8, "Post-Flood Gen 6 (Babel Division)", "Patriarch of the Division of the Earth",
          ["Genesis 10:25, 11:16-19", "Jubilees 8:8", "Book of Jasher 7:21-22"],
          "'In his days the earth was divided' (Tower of Babel). Father of Reu (and Yen in Jasher 7:22).", major=True),
        N("bib_joktan", "Joktan (Qahtan)", "arabian", 8, "Post-Flood Gen 6 (Arabia)", "Progenitor of Southern Arabs (13 Sons)",
          ["Genesis 10:25-30", "Book of Jasher 7:21", "Ibn al-Kalbi", "al-Tabari"],
          "Brother of Peleg; father of 13 Arabian tribes spanning from Mesha to Sephar (Yemen/Hadhramaut/Oman). Identified in Arabian genealogy with Qahtan.",
          ["Qahtan (Arabic)"], major=True),
    ]
    edges += [
        E("bib_shelah", "bib_eber", "direct", "Son (Gen 10:24; 11:14)"),
        E("bib_eber", "bib_peleg", "direct", "Son (Gen 10:25; Jasher 7:21)"),
        E("bib_eber", "bib_joktan", "direct", "Son (Gen 10:25; Arabian Qahtan)"),
    ]

    # ALL 13 Sons of Joktan (Gen 10:26-29; Jasher 7:21)
    add_children(nodes, edges, "bib_joktan", "arabian", 9, "Post-Flood Gen 7 (13 Sons of Joktan)", [
        ("bib_almodad", "Almodad", {"notes": "1st of 13 sons of Joktan (Gen 10:26; Jasher 7:21)."}),
        ("bib_sheleph", "Sheleph", {"notes": "2nd son of Joktan; linked to Sulaf tribe of Yemen."}),
        ("bib_hazarmaveth", "Hazarmaveth (Hadhramaut)", {"notes": "3rd son of Joktan; exact historical cognate of Hadhramaut in southern Yemen!"}),
        ("bib_jerah", "Jerah", {"notes": "4th son of Joktan; linked to South Arabian lunar sanctuary/tribe."}),
        ("bib_hadoram", "Hadoram", {"notes": "5th son of Joktan."}),
        ("bib_uzal", "Uzal (Sana'a)", {"notes": "6th son of Joktan; classical ancient name of Sana'a, Yemen!"}),
        ("bib_diklah", "Diklah", {"notes": "7th son of Joktan."}),
        ("bib_obal", "Obal (Ebal)", {"notes": "8th son of Joktan (Ebal in 1 Chr 1:22)."}),
        ("bib_abimael", "Abimael", {"notes": "9th son of Joktan."}),
        ("bib_sheba_joktan", "Sheba / Saba (son of Joktan)", {"major": True, "notes": "10th son of Joktan; linked to the Sabaean Kingdom of Yemen (Queen of Sheba / Makeda!)."}),
        ("bib_ophir", "Ophir", {"notes": "11th son of Joktan; famed ancient source of gold (1 Kings 9:28)."}),
        ("bib_havilah_joktan", "Havilah (son of Joktan)", {"notes": "12th son of Joktan; Arabian gold/myrrh region."}),
        ("bib_jobab", "Jobab", {"notes": "13th son of Joktan."}),
    ], default_sources=["Genesis 10:26-29", "Book of Jasher 7:21"])

    # Peleg -> Reu -> Serug -> Nahor I -> Terah
    nodes += [
        N("jas_yen", "Yen (son of Peleg)", "biblical", 8, "Post-Flood Gen 7 (Jasher 7:22)", "Son of Peleg",
          ["Book of Jasher 7:22"], "Additional son of Peleg listed alongside Reu in Book of Jasher 7:22."),
        N("bib_reu", "Reu & Ora", "biblical", 8, "Post-Flood Gen 7", "Patriarch",
          ["Genesis 11:18-21", "Jubilees 11:1", "Book of Jasher 7:22"], "Jubilees 11:1 names his wife Ora, daughter of Ur (founder of Ur of the Chaldees!)."),
        N("bib_serug", "Serug & Milka", "biblical", 8, "Post-Flood Gen 8", "Patriarch",
          ["Genesis 11:20-23", "Jubilees 11:6-7", "Book of Jasher 7:22"], "Jubilees 11:6 notes his original name Seroh and wife Milka; Ur/Haran region (Saruj)."),
        N("bib_nahor1", "Nahor I & Iyaska", "biblical", 8, "Post-Flood Gen 9", "Father of Terah",
          ["Genesis 11:22-25", "Jubilees 11:8-9", "Book of Jasher 7:49"], "Jubilees 11:9 names his wife Iyaska, daughter of Nestag of the Chaldeans."),
        N("bib_terah", "Terah & Amthelo / Edna", "biblical", 9, "Post-Flood Gen 10 (Ur of the Chaldees)", "Father of Abraham, Nahor II & Haran",
          ["Genesis 11:24-32", "Jubilees 11:14", "Book of Jasher 7:49-51, 8-12"],
          "Jasher 7:49 names his wife Amthelo daughter of Cornebo (Jubilees 11:14 names Edna). Jasher portrays Terah as captain of Nimrod's host in Shinar before departing Ur for Haran.",
          ["Wife: Amthelo (Jasher) / Edna (Jub)"], major=True),
    ]
    edges += [
        E("bib_peleg", "jas_yen", "expansion", "Son (Book of Jasher 7:22)"),
        E("bib_peleg", "bib_reu", "direct", "Son (Gen 11:18)"),
        E("bib_reu", "bib_serug", "direct", "Son (Gen 11:20)"),
        E("bib_serug", "bib_nahor1", "direct", "Son (Gen 11:22)"),
        E("bib_nahor1", "bib_terah", "direct", "Son (Gen 11:24)"),
    ]

    return {"module": "02_table_of_nations", "title": "Complete Table of Nations (Genesis 10, Jubilees 8-9 & Jasher 7/10)", "nodes": nodes, "edges": edges}


def build_module_03_abraham_all_nations():
    nodes, edges = [], []

    # Terah's 3 Sons: Abraham, Nahor II, Haran
    nodes += [
        N("bib_abraham", "Abraham (Abram)", "biblical", 9, "Patriarchal Era (c. 2000-1800 BCE trad.)",
          "Common Patriarch of Israelites, Ishmaelites, Edomites & Midianites",
          ["Genesis 11-25", "Jubilees 11-23", "Book of Jasher 8-26", "Josephus Ant. 1.8"],
          "Fathers 8 sons across three wives: Isaac (Sarah), Ishmael (Hagar), and Zimran, Jokshan, Medan, Midian, Ishbak, Shuah (Keturah). Josephus & Artapanus say Abraham taught astronomy and mathematics in Egypt.",
          ["Ibrahim (Arabic)", "Wives: Sarah, Hagar, Keturah"], major=True),
        N("bib_nahor2", "Nahor II & Milcah / Reumah", "biblical", 9, "Patriarchal Era (Haran / Paddan-Aram)",
          "Brother of Abraham / Grandfather of Rebekah, Leah & Rachel",
          ["Genesis 11:26, 22:20-24", "Book of Jasher 9:1"],
          "Fathers 8 sons by Milcah (including Bethuel -> Rebekah & Laban) and 4 children by Reumah.", major=True),
        N("bib_haran", "Haran (brother of Abraham)", "biblical", 9, "Patriarchal Era (Ur)",
          "Father of Lot, Milcah & Sarai/Iscah",
          ["Genesis 11:27-29", "Book of Jasher 9:2-3, 12:37"],
          "Died in Ur of the Chaldees (Jasher 12 says he died in Nimrod's furnace). Father of Lot, Milcah, and Sarai/Iscah (Jasher 9:3).", major=True),
    ]
    edges += [
        E("bib_terah", "bib_abraham", "direct", "Son (Gen 11:26; Jasher 8)"),
        E("bib_terah", "bib_nahor2", "direct", "Son (Gen 11:26; Jasher 7:50)"),
        E("bib_terah", "bib_haran", "direct", "Son (Gen 11:26; Jasher 7:50)"),
    ]

    # Haran -> Lot -> Moab & Ammon; + Milcah & Sarah
    add_children(nodes, edges, "bib_haran", "biblical", 10, "Patriarchal Era (Haran)", [
        ("bib_lot", "Lot", {"major": True, "sources": ["Genesis 11:27, 19:30-38", "Book of Jasher 19"], "role": "Ancestor of Moab & Ammon", "notes": "Nephew of Abraham; rescued from Sodom. Father of Moab and Ben-Ammi (Ammon)."}),
        ("bib_milcah", "Milcah", {"sources": ["Genesis 11:29, 22:20"], "notes": "Daughter of Haran; marries her uncle Nahor II (mother of Bethuel)."}),
        ("bib_sarah", "Sarah (Sarai / Iscah)", {"major": True, "sources": ["Genesis 11:29, 20:12", "Book of Jasher 9:3"], "role": "Matriarch / Wife of Abraham", "notes": "Wife of Abraham and mother of Isaac. Book of Jasher 9:3 and Talmud Megillah 14a identify her as Haran's daughter Iscah."}),
    ])
    edges += [
        E("bib_milcah", "bib_nahor2", "direct", "Wife of Nahor II (Gen 11:29)"),
        E("bib_sarah", "bib_abraham", "direct", "Wife of Abraham (Gen 11:29; Jasher 9:3)"),
    ]
    add_children(nodes, edges, "bib_lot", "biblical", 11, "Post-Sodom Transjordan", [
        ("bib_moab", "Moab (Moabites)", {"major": True, "sources": ["Genesis 19:37", "Book of Jasher 19:60"], "role": "Eponym of Kingdom of Moab", "notes": "Progenitor of the Moabites (ancestors of Ruth, great-grandmother of King David!)."}),
        ("bib_ammon", "Ben-Ammi (Ammonites)", {"major": True, "sources": ["Genesis 19:38", "Book of Jasher 19:61"], "role": "Eponym of Kingdom of Ammon", "notes": "Progenitor of the Ammonites (centered at Rabbah / modern Amman)."}),
    ])

    # Nahor II -> ALL 12 Children (Gen 22:20-24) -> Bethuel -> Laban & Rebekah
    add_children(nodes, edges, "bib_nahor2", "biblical", 10, "Patriarchal Era (Aram-Naharaim)", [
        ("bib_uz_nahor", "Uz (son of Nahor)", {"notes": "Firstborn of Nahor II & Milcah (Gen 22:21)."}),
        ("bib_buz", "Buz", {"notes": "Son of Nahor II & Milcah; eponym of Elihu the Buzite in Job."}),
        ("bib_kemuel", "Kemuel (father of Aram)", {"notes": "Son of Nahor II & Milcah; father of Aram (Gen 22:21)."}),
        ("bib_chesed", "Chesed (Chaldeans?)", {"notes": "Son of Nahor II & Milcah; often linked to the Kasdim/Chaldeans."}),
        ("bib_hazo", "Hazo", {"notes": "Son of Nahor II & Milcah."}),
        ("bib_pildash", "Pildash", {"notes": "Son of Nahor II & Milcah."}),
        ("bib_jidlaph", "Jidlaph", {"notes": "Son of Nahor II & Milcah."}),
        ("bib_bethuel", "Bethuel", {"major": True, "notes": "Son of Nahor II & Milcah; father of Rebekah (wife of Isaac) and Laban (father of Leah & Rachel)."}),
        ("bib_tebah", "Tebah", {"notes": "Son of Nahor II & Reumah (Gen 22:24)."}),
        ("bib_gaham", "Gaham", {"notes": "Son of Nahor II & Reumah (Gen 22:24)."}),
        ("bib_tahash", "Tahash", {"notes": "Son of Nahor II & Reumah (Gen 22:24)."}),
        ("bib_maacah_nahor", "Maacah (child of Nahor)", {"notes": "Child of Nahor II & Reumah (Gen 22:24); eponym of Aramean Maacah."}),
    ], default_sources=["Genesis 22:20-24"])
    add_children(nodes, edges, "bib_bethuel", "biblical", 11, "Patriarchal Era (Haran)", [
        ("bib_rebekah", "Rebekah (Rivkah)", {"sources": ["Genesis 24", "Book of Jasher 24"], "notes": "Marries Isaac; mother of Esau and Jacob."}),
        ("bib_laban", "Laban", {"sources": ["Genesis 24, 29", "Book of Jasher 28-31"], "notes": "Father of Leah and Rachel (wives of Jacob)."}),
    ])

    # ================= ABRAHAM'S 8 SONS =================
    # 1. ISHMAEL (via Hagar) -> ALL 12 PRINCES + MAHALATH
    nodes.append(N("bib_ishmael", "Ishmael (Isma'il)", "arabian", 10, "Patriarchal Era (Arabia)",
                   "Firstborn of Abraham (via Hagar) / Father of 12 Princes",
                   ["Genesis 16, 25:12-18", "Book of Jasher 21 & 25", "Ibn Ishaq Sirah"],
                   "Jasher 21 names his wives Meribah (divorced) and Malchuth of Egypt. Fathers 12 Arabian tribal princes and daughter Mahalath/Basemath (who marries Esau).",
                   ["Isma'il", "Wives: Meribah & Malchuth (Jasher 21)"], major=True))
    edges.append(E("bib_abraham", "bib_ishmael", "direct", "Firstborn son via Hagar (Gen 16:15)"))

    add_children(nodes, edges, "bib_ishmael", "arabian", 11, "12 Princes of Ishmael (Gen 25:13-16)", [
        ("ish_nebaioth", "Nebaioth (Nabit)", {"major": True, "notes": "1st son of Ishmael; attested as Nabayati in Neo-Assyrian inscriptions and linked to Nabataeans / Adnanite lineage."}),
        ("ish_kedar", "Kedar (Qaydar)", {"major": True, "notes": "2nd son of Ishmael; attested as the Qedarite Kingdom (Qidri) in Neo-Assyrian records; traditional ancestor of Adnan & Quraysh."}),
        ("ish_adbeel", "Adbeel", {"notes": "3rd son of Ishmael; attested as Idibi'ilu in Tiglath-Pileser III annals."}),
        ("ish_mibsam", "Mibsam", {"notes": "4th son of Ishmael."}),
        ("ish_mishma", "Mishma", {"notes": "5th son of Ishmael."}),
        ("ish_dumah", "Dumah", {"notes": "6th son of Ishmael; oasis of Dumat al-Jandal (Adummatu) in Northern Arabia."}),
        ("ish_massa", "Massa", {"notes": "7th son of Ishmael; North Arabian tribe of Mas'a."}),
        ("ish_hadad", "Hadad (Hadar)", {"notes": "8th son of Ishmael."}),
        ("ish_tema", "Tema (Tayma)", {"notes": "9th son of Ishmael; famous NW Arabian caravan oasis of Tayma."}),
        ("ish_jetur", "Jetur (Ituraeans)", {"notes": "10th son of Ishmael; Ituraean tribes of northern Transjordan/Lebanon."}),
        ("ish_naphish", "Naphish", {"notes": "11th son of Ishmael."}),
        ("ish_kedemah", "Kedemah", {"notes": "12th son of Ishmael."}),
        ("ish_mahalath", "Mahalath / Basemath (dau. of Ishmael)", {"sources": ["Genesis 28:9, 36:3"], "notes": "Sister of Nebaioth; marries her cousin Esau, uniting Ishmaelite and Edomite lines!"}),
    ], default_sources=["Genesis 25:13-16", "Book of Jasher 25:14"])

    # Adnanite Lineage from Kedar/Nebaioth
    nodes.append(N("ar_adnan_quraysh", "Adnan → Ma'add → Nizar → Quraysh → Muhammad", "arabian", 12, "Classical Arabia → 7th c. CE",
                   "Northern Arabian (Adnanite) & Prophetic Lineage",
                   ["Ibn Ishaq Sirah", "al-Tabari History", "Ibn al-Kalbi"],
                   "Classical Arabian genealogies trace the Northern Arabs from Ishmael (via Kedar/Nebaioth) through Adnan -> Ma'add -> Nizar -> Mudar -> Fihr (Quraysh) -> Qusayy -> Abd Manaf -> Hashim -> Abd al-Muttalib -> Abdullah -> Muhammad.",
                   ["Adnanites", "Banu Hashim"], major=True))
    edges += [
        E("ish_kedar", "ar_adnan_quraysh", "expansion", "Arabian genealogical bridge via Qaydar/Adnan"),
        E("ish_nebaioth", "ar_adnan_quraysh", "expansion", "Alternate Arabian tradition via Nabit/Adnan"),
    ]

    # 2. KETURAH'S 6 SONS + ALL GRANDCHILDREN (Gen 25:1-4 & Book of Jasher 25:1-6!!)
    add_children(nodes, edges, "bib_abraham", "biblical", 10, "Patriarchal Era (Keturah's 6 Sons)", [
        ("ket_zimran", "Zimran", {"major": True, "sources": ["Genesis 25:2", "Book of Jasher 25:2-3"], "notes": "1st son of Abraham & Keturah. Jasher 25:3 names his 3 sons: Abihen, Molich, Narim."}),
        ("ket_jokshan", "Jokshan", {"major": True, "sources": ["Genesis 25:2-3", "Book of Jasher 25:2"], "notes": "2nd son of Abraham & Keturah; father of Sheba and Dedan."}),
        ("ket_medan", "Medan", {"major": True, "sources": ["Genesis 25:2", "Book of Jasher 25:2, 25:4"], "notes": "3rd son of Abraham & Keturah. Jasher 25:4 names his 5 sons: Amida, Joab, Gochi, Elisha, Nothach."}),
        ("ket_midian", "Midian", {"major": True, "sources": ["Genesis 25:2-4", "Exodus 2-3", "Book of Jasher 25:2"], "role": "Progenitor of Midianites (Jethro & Zipporah)", "notes": "4th son of Abraham & Keturah; father of Ephah, Epher, Hanoch, Abida, Eldaah. Ancestor of Reuel/Jethro and Moses's wife Zipporah."}),
        ("ket_ishbak", "Ishbak", {"major": True, "sources": ["Genesis 25:2", "Book of Jasher 25:2, 25:5"], "notes": "5th son of Abraham & Keturah. Jasher 25:5 names his 3 sons: Makiro, Beydod, Tator."}),
        ("ket_shuah", "Shuah", {"major": True, "sources": ["Genesis 25:2", "Book of Jasher 25:2, 25:5"], "notes": "6th son of Abraham & Keturah; eponym of Shuhites (Bildad in Job). Jasher 25:5 names his 4 sons: Bildad, Mamdad, Munan, Meban."}),
    ], default_edge="direct", default_sources=["Genesis 25:1-4", "Book of Jasher 25"])

    # Jasher 25 & Gen 25 Grandchildren of Keturah!
    add_children(nodes, edges, "ket_zimran", "biblical", 11, "Jasher 25:3 (Zimran's Sons)", [
        ("jas_zim_abihen", "Abihen", {"notes": "Son of Zimran in Book of Jasher 25:3."}),
        ("jas_zim_molich", "Molich", {"notes": "Son of Zimran in Book of Jasher 25:3."}),
        ("jas_zim_narim", "Narim", {"notes": "Son of Zimran in Book of Jasher 25:3."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 25:3"])

    add_children(nodes, edges, "ket_jokshan", "biblical", 11, "Gen 25:3 (Jokshan's Sons)", [
        ("ket_sheba", "Sheba (son of Jokshan)", {"sources": ["Genesis 25:3"], "notes": "Grandson of Abraham via Jokshan (Northern Sabaean trade network)."}),
        ("ket_dedan", "Dedan (son of Jokshan)", {"sources": ["Genesis 25:3"], "notes": "Grandson of Abraham via Jokshan; father of Asshurim, Letushim, Leummim."}),
    ], default_sources=["Genesis 25:3"])
    add_children(nodes, edges, "ket_dedan", "biblical", 12, "Gen 25:3 (Dedan's Sons)", [
        ("ket_asshurim", "Asshurim", {"notes": "Descendant tribe of Abraham via Jokshan -> Dedan (Gen 25:3)."}),
        ("ket_letushim", "Letushim", {"notes": "Descendant tribe of Abraham via Jokshan -> Dedan (Gen 25:3)."}),
        ("ket_leummim", "Leummim", {"notes": "Descendant tribe of Abraham via Jokshan -> Dedan (Gen 25:3)."}),
    ], default_sources=["Genesis 25:3"])

    add_children(nodes, edges, "ket_medan", "biblical", 11, "Jasher 25:4 (Medan's Sons)", [
        ("jas_med_amida", "Amida", {"notes": "Son of Medan in Book of Jasher 25:4."}),
        ("jas_med_joab", "Joab (son of Medan)", {"notes": "Son of Medan in Book of Jasher 25:4."}),
        ("jas_med_gochi", "Gochi", {"notes": "Son of Medan in Book of Jasher 25:4."}),
        ("jas_med_elisha", "Elisha (son of Medan)", {"notes": "Son of Medan in Book of Jasher 25:4."}),
        ("jas_med_nothach", "Nothach", {"notes": "Son of Medan in Book of Jasher 25:4."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 25:4"])

    add_children(nodes, edges, "ket_midian", "biblical", 11, "Gen 25:4 (Midian's 5 Sons + Jethro)", [
        ("mid_ephah", "Ephah", {"notes": "1st son of Midian (Gen 25:4; attested as Khayappa in Assyrian annals)."}),
        ("mid_epher", "Epher", {"notes": "2nd son of Midian (Gen 25:4)."}),
        ("mid_hanoch", "Hanoch (son of Midian)", {"notes": "3rd son of Midian (Gen 25:4)."}),
        ("mid_abida", "Abida", {"notes": "4th son of Midian (Gen 25:4)."}),
        ("mid_eldaah", "Eldaah", {"notes": "5th son of Midian (Gen 25:4)."}),
        ("mid_jethro", "Reuel / Jethro (Priest of Midian) → Zipporah", {"major": True, "edge_type": "expansion", "sources": ["Exodus 2:18, 3:1", "Book of Jasher 76"], "notes": "Midianite priest (Shu'ayb in Islamic tradition) who shelters Moses after his reign in Cush (Jasher 76) and gives him his daughter Zipporah."}),
    ], default_sources=["Genesis 25:4", "Book of Jasher 25:4"])

    add_children(nodes, edges, "ket_ishbak", "biblical", 11, "Jasher 25:5 (Ishbak's Sons)", [
        ("jas_ishb_makiro", "Makiro", {"notes": "Son of Ishbak in Book of Jasher 25:5."}),
        ("jas_ishb_beydod", "Beydod", {"notes": "Son of Ishbak in Book of Jasher 25:5."}),
        ("jas_ishb_tator", "Tator", {"notes": "Son of Ishbak in Book of Jasher 25:5."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 25:5"])

    add_children(nodes, edges, "ket_shuah", "biblical", 11, "Jasher 25:5 (Shuah's Sons)", [
        ("jas_shu_bildad", "Bildad (son of Shuah)", {"notes": "Son of Shuah in Book of Jasher 25:5 — connects Shuah to Bildad the Shuhite in the Book of Job!"}),
        ("jas_shu_mamdad", "Mamdad", {"notes": "Son of Shuah in Book of Jasher 25:5."}),
        ("jas_shu_munan", "Munan", {"notes": "Son of Shuah in Book of Jasher 25:5."}),
        ("jas_shu_meban", "Meban", {"notes": "Son of Shuah in Book of Jasher 25:5."}),
    ], default_edge="expansion", default_sources=["Book of Jasher 25:5"])

    # 3. ISAAC (via Sarah) -> ESAU & JACOB
    nodes.append(N("bib_isaac", "Isaac (Yitzhak) & Rebekah", "biblical", 10, "Patriarchal Era",
                   "Son of Abraham & Sarah", ["Genesis 21-35", "Jubilees 16-36", "Book of Jasher 22-35"],
                   "Marries Rebekah (daughter of Bethuel, granddaughter of Nahor II). Father of twin sons Esau (Edom) and Jacob (Israel).",
                   ["Yitzhak", "Ishaq"], major=True))
    edges += [
        E("bib_abraham", "bib_isaac", "direct", "Son via Sarah (Gen 21:3)"),
        E("bib_rebekah", "bib_isaac", "direct", "Wife of Isaac (Gen 24:67)"),
    ]

    # ---------------- ESAU (EDOM) — ALL SONS, GRANDSONS & JASHER ROME BRIDGE ----------------
    nodes.append(N("bib_esau", "Esau (Edom)", "biblical", 11, "Patriarchal Era (Mount Seir / Edom)",
                   "Progenitor of the Edomites & Amalekites", ["Genesis 25, 36", "Book of Jasher 27, 36, 57, 61"],
                   "Marries Adah (Hittite), Oholibamah (Hivite/Horite), and Basemath/Mahalath (daughter of Ishmael). Jasher 27 narrates Esau slaying Nimrod and taking Adam's garments!",
                   ["Edom"], major=True))
    edges += [
        E("bib_isaac", "bib_esau", "direct", "Firstborn twin (Gen 25:25)"),
        E("ish_mahalath", "bib_esau", "direct", "Wife of Esau (Gen 28:9; 36:3)"),
    ]

    add_children(nodes, edges, "bib_esau", "biblical", 12, "Genesis 36 (Esau's 5 Sons)", [
        ("esa_eliphaz", "Eliphaz", {"major": True, "sources": ["Genesis 36:4, 11-12", "Book of Jasher 36, 57"], "notes": "Firstborn of Esau (via Adah); father of Teman, Omar, Zepho, Gatam, Kenaz, and Amalek (via Timna)."}),
        ("esa_reuel", "Reuel (son of Esau)", {"major": True, "sources": ["Genesis 36:4, 13", "Book of Jasher 36"], "notes": "Son of Esau & Basemath (daughter of Ishmael) — uniting Edom and Ishmael! Father of Nahath, Zerah, Shammah, Mizzah."}),
        ("esa_jeush", "Jeush", {"sources": ["Genesis 36:5"], "notes": "Son of Esau & Oholibamah (daughter of Anah the Horite)."}),
        ("esa_jalam", "Jalam", {"sources": ["Genesis 36:5"], "notes": "Son of Esau & Oholibamah."}),
        ("esa_korah", "Korah (son of Esau)", {"sources": ["Genesis 36:5"], "notes": "Son of Esau & Oholibamah."}),
    ])
    add_children(nodes, edges, "esa_eliphaz", "biblical", 13, "Gen 36:11-12 (Eliphaz's Sons)", [
        ("esa_teman", "Teman", {"notes": "Eponym of Teman in Edom (linked to Eliphaz the Temanite in Job)."}),
        ("esa_omar", "Omar", {"notes": "Son of Eliphaz (Gen 36:11)."}),
        ("esa_zepho", "Zepho (King of Kittim / Italy)", {"major": True, "sources": ["Genesis 36:11", "Book of Jasher 57, 61"], "role": "Traditional Jasher Bridge from Edom to Italy/Rome", "notes": "In Book of Jasher ch. 57-61, Zepho escapes Joseph's prison in Egypt, flees to Kittim (Italy), slays a beast and defeats Angeas king of Africa, and becomes King of Chittim (father of Janeus/Janus)!"}),
        ("esa_gatam", "Gatam", {"notes": "Son of Eliphaz (Gen 36:11)."}),
        ("esa_kenaz", "Kenaz", {"notes": "Son of Eliphaz (Gen 36:11); linked to the Kenizzites."}),
        ("esa_amalek", "Amalek (Amalekites)", {"major": True, "sources": ["Genesis 36:12", "Exodus 17"], "notes": "Son of Eliphaz & Timna (sister of Lotan the Horite); ancestor of the Amalekites."}),
    ], default_sources=["Genesis 36:11-12"])
    add_children(nodes, edges, "esa_reuel", "biblical", 13, "Gen 36:13 (Reuel's Sons)", [
        ("esa_nahath", "Nahath", {"notes": "Son of Reuel (Gen 36:13)."}),
        ("esa_zerah", "Zerah (son of Reuel)", {"notes": "Son of Reuel (Gen 36:13); father of Jobab king of Edom (Gen 36:33)."}),
        ("esa_shammah", "Shammah", {"notes": "Son of Reuel (Gen 36:13)."}),
        ("esa_mizzah", "Mizzah", {"notes": "Son of Reuel (Gen 36:13)."}),
    ], default_sources=["Genesis 36:13"])
    add_children(nodes, edges, "esa_zepho", "biblical", 14, "Jasher 61-62 (Kittim/Italy)", [
        ("jas_janeus", "Janeus (Janus of Italy)", {"sources": ["Book of Jasher 62:25", "Book of Jasher 64"], "notes": "Son of Zepho in Book of Jasher 62:25, succeeding him as king over Kittim (Italy) — echoing Roman Janus!"}),
    ], default_edge="syncretic", default_sources=["Book of Jasher 62:25"])
    edges.append(E("esa_zepho", "bib_kittim", "syncretic", "Jasher 61: Zepho becomes first King of Kittim (Italy/Rome)"))

    # ---------------- JACOB (ISRAEL) — ALL 12 SONS, DINAH, ALL GRANDCHILDREN, MOSES & DAVID ----------------
    nodes.append(N("bib_jacob", "Jacob (Israel)", "biblical", 11, "Patriarchal Era",
                   "Father of the 12 Tribes of Israel & Dinah",
                   ["Genesis 25-49", "Jubilees 24-45", "Book of Jasher 28-56"],
                   "Marries Leah and Rachel (daughters of Laban) plus Bilhah and Zilpah. Fathers 12 sons and daughter Dinah, with all 70 household members enumerated in Genesis 46 & Jasher 59.",
                   ["Yaakov", "Yisrael"], major=True))
    edges += [
        E("bib_isaac", "bib_jacob", "direct", "Second twin (Gen 25:26)"),
        E("bib_laban", "bib_jacob", "direct", "Daughters Leah & Rachel marry Jacob (Gen 29)"),
    ]

    # All 12 Tribes + Dinah
    tribes = [
        ("tri_reuben", "Reuben", "Leah", ["Hanoch", "Pallu", "Hezron", "Carmi"]),
        ("tri_simeon", "Simeon", "Leah", ["Jemuel", "Jamin", "Ohad", "Jachin", "Zohar", "Shaul"]),
        ("tri_levi", "Levi", "Leah", []),  # Expanded deeply to Moses & Aaron below!
        ("tri_judah", "Judah", "Leah", []), # Expanded deeply to David & Solomon below!
        ("tri_dan", "Dan", "Bilhah", ["Hushim"]),
        ("tri_naphtali", "Naphtali", "Bilhah", ["Jahzeel", "Guni", "Jezer", "Shillem"]),
        ("tri_gad", "Gad", "Zilpah", ["Ziphion", "Haggi", "Shuni", "Ezbon", "Eri", "Arodi", "Areli"]),
        ("tri_asher", "Asher", "Zilpah", ["Imnah", "Ishvah", "Ishvi", "Beriah", "Serah (dau.)"]),
        ("tri_issachar", "Issachar", "Leah", ["Tola", "Puvah", "Job (Jashub)", "Shimron"]),
        ("tri_zebulun", "Zebulun", "Leah", ["Sered", "Elon", "Jahleel"]),
        ("tri_dinah", "Dinah (dau. of Jacob)", "Leah", []),
        ("tri_joseph", "Joseph (Zaphenath-Paneah)", "Rachel", []), # Expanded below!
        ("tri_benjamin", "Benjamin", "Rachel", ["Bela", "Becher", "Ashbel", "Gera", "Naaman", "Ehi", "Rosh", "Muppim", "Huppim", "Ard"]),
    ]

    for tid, tname, mother, kids in tribes:
        is_maj = tid in {"tri_levi", "tri_judah", "tri_joseph", "tri_reuben", "tri_benjamin"}
        extra_notes = f"Child of Jacob & {mother} (Gen 29-30, 46; Jasher 45, 59)."
        alts = []
        if tid == "tri_joseph":
            extra_notes = "Vizier of Egypt under Pharaoh; given the Egyptian name Zaphenath-Paneah (Gen 41:45; Jasher 49:18) and wed to Asenath daughter of Poti-phera, Priest of On/Heliopolis. Often compared to Imhotep (vizier of Djoser during a 7-year famine)."
            alts = ["Zaphenath-Paneah (Egyptian name)", "Yusuf (Arabic)", "Compared to Imhotep"]
        elif tid == "tri_dinah":
            extra_notes = "Daughter of Jacob & Leah. Book of Jasher 49:16-18 (and Pirkei de-Rabbi Eliezer) famously states that Asenath (Joseph's Egyptian wife) was Dinah's daughter adopted by Poti-phera in Egypt!"
        nodes.append(N(tid, tname, "biblical", 12, "12 Tribes of Israel (Gen 46)", f"Tribal Patriarch / Child of {mother}",
                       ["Genesis 29-30, 46:8-27", "Book of Jasher 45, 59"], extra_notes, altNames=alts, major=is_maj))
        edges.append(E("bib_jacob", tid, "direct", f"Via {mother} (Gen 46)"))
        for k in kids:
            slug = k.lower().replace(" ", "_").replace("(", "").replace(")", "").replace(".", "")
            kid_id = f"{tid}_{slug}"
            knote = f"Child of {tname} listed in Genesis 46 & Book of Jasher 59."
            if "Serah" in k:
                knote = "Daughter of Asher; celebrated in Book of Jasher 54:35 as the harp-playing maiden who broke the news to Jacob that Joseph was alive in Egypt!"
            nodes.append(N(kid_id, k, "biblical", 13, "70 Souls Entering Egypt (Gen 46)", f"Child of {tname}",
                           ["Genesis 46:8-27", "Book of Jasher 59"], knote))
            edges.append(E(tid, kid_id, "direct", f"Child of {tname} (Gen 46)"))

    # Levi -> Gershon, Kohath, Merari -> Amram + Jochebed -> Miriam, Aaron, Moses -> Gershom & Eliezer
    add_children(nodes, edges, "tri_levi", "biblical", 13, "Levitical Lineage (Exod 6)", [
        ("lev_gershon", "Gershon", {"notes": "1st son of Levi (Gen 46:11; Exod 6:16)."}),
        ("lev_kohath", "Kohath", {"major": True, "notes": "2nd son of Levi; grandfather of Moses, Aaron & Miriam."}),
        ("lev_merari", "Merari", {"notes": "3rd son of Levi (Gen 46:11; Exod 6:16)."}),
        ("lev_jochebed", "Jochebed (dau. of Levi)", {"sources": ["Exodus 6:20", "Numbers 26:59", "Book of Jasher 67:2"], "notes": "Daughter of Levi born in Egypt; wife of Amram and mother of Miriam, Aaron, and Moses."}),
    ], default_sources=["Genesis 46:11", "Exodus 6:16-20"])
    add_children(nodes, edges, "lev_kohath", "biblical", 14, "Egypt Sojourn (Exod 6)", [
        ("lev_amram", "Amram", {"major": True, "sources": ["Exodus 6:18-20", "Book of Jasher 67"], "notes": "Father of Miriam, Aaron, and Moses."}),
        ("lev_izhar", "Izhar", {"notes": "Son of Kohath; father of Korah (Exod 6:21)."}),
        ("lev_hebron", "Hebron (son of Kohath)", {"notes": "Son of Kohath (Exod 6:18)."}),
        ("lev_uzziel", "Uzziel", {"notes": "Son of Kohath (Exod 6:18)."}),
    ], default_sources=["Exodus 6:18"])
    edges.append(E("lev_jochebed", "lev_amram", "direct", "Wife of Amram (Exod 6:20)"))

    add_children(nodes, edges, "lev_amram", "biblical", 15, "Exodus Era (c. 15th-13th c. BCE)", [
        ("lev_miriam", "Miriam", {"sources": ["Exodus 15:20", "Book of Jasher 67:12"], "notes": "Prophetess, sister of Moses and Aaron."}),
        ("lev_aaron", "Aaron (High Priest)", {"major": True, "sources": ["Exodus 6:20-23"], "notes": "First High Priest of Israel; marries Elisheba (father of Nadab, Abihu, Eleazar, Ithamar)."}),
        ("bib_moses", "Moses (Moshe)", {"major": True, "sources": ["Exodus 2-40", "Book of Jasher 68-87", "Artapanus", "Josephus Against Apion 1.26"], "role": "Lawgiver / Prince of Egypt / King of Cush (Jasher)", "altNames": ["Jekuthiel / Heber / Jered (Jasher 68:32)", "Osarseph (Manetho)", "Musaeus (Artapanus)", "Mose (Egyptian root)"], "notes": "Raised by Pharaoh's daughter Bithiah (1 Chr 4:18; Jasher 68). Book of Jasher 72-76 (and Josephus Ant. 2.10) recounts Moses serving as King of Cush (Ethiopia) for 40 years with Queen Adoniah before marrying Zipporah in Midian! Identified in Manetho as Egyptian priest Osarseph and in Artapanus as Musaeus/Hermes."}),
    ])
    add_children(nodes, edges, "bib_moses", "biblical", 16, "Wilderness / Midian", [
        ("mos_gershom", "Gershom (son of Moses)", {"sources": ["Exodus 2:22, 18:3", "Book of Jasher 77"], "notes": "Firstborn son of Moses & Zipporah (daughter of Jethro of Midian)."}),
        ("mos_eliezer", "Eliezer (son of Moses)", {"sources": ["Exodus 18:4", "Book of Jasher 77"], "notes": "Second son of Moses & Zipporah."}),
    ])
    edges.append(E("mid_jethro", "bib_moses", "direct", "Daughter Zipporah marries Moses (Exod 2:21; Jasher 76)"))

    # Judah -> Er, Onan, Shelah, Zerah, Perez -> Boaz (+ Ruth) -> Jesse -> David -> Solomon -> Menelik I!
    add_children(nodes, edges, "tri_judah", "biblical", 13, "Judahite Line (Gen 38, 46)", [
        ("jud_er", "Er", {"notes": "1st son of Judah & Shua's daughter (Gen 38:3)."}),
        ("jud_onan", "Onan", {"notes": "2nd son of Judah (Gen 38:4)."}),
        ("jud_shelah", "Shelah (son of Judah)", {"notes": "3rd son of Judah (Gen 38:5)."}),
        ("jud_zerah", "Zerah (son of Judah)", {"notes": "Twin son of Judah & Tamar (Gen 38:30); linked in some classical/Irish traditions to Mediterranean migrations."}),
        ("jud_perez", "Perez (Pharez)", {"major": True, "sources": ["Genesis 38:29", "Ruth 4:18-22"], "notes": "Twin son of Judah & Tamar; direct ancestor of Boaz, King David, and the royal Davidic line."}),
    ], default_sources=["Genesis 38", "Genesis 46:12"])

    nodes += [
        N("jud_boaz_jesse", "Hezron → Ram → Nahshon → Boaz (+ Ruth) → Jesse", "biblical", 14, "Judges Era (Ruth 4)",
          "Bridge from Perez to Davidic Dynasty (Uniting Judah & Moab)", ["Ruth 4:18-22", "1 Chronicles 2:5-15"],
          "Boaz marries Ruth the Moabitess (descendant of Lot!), uniting the Israelite line of Judah with the Moabite line of Lot."),
        N("jud_david", "King David", "biblical", 15, "United Monarchy (c. 1010-970 BCE)",
          "King of Israel & Founder of Davidic Dynasty", ["1-2 Samuel", "1 Chronicles 3"],
          "Son of Jesse; father of Solomon, Absalom, Adonijah, Nathan, and Tamar.", major=True),
        N("jud_solomon", "King Solomon (Shlomo)", "biblical", 16, "United Monarchy (c. 970-931 BCE)",
          "Builder of the First Temple", ["1 Kings 1-11", "Kebra Nagast"],
          "Father of Rehoboam (Judah). In Ethiopia's national epic Kebra Nagast, Solomon and Makeda (Queen of Sheba) parent Menelik I, bridging Israel, Arabia/Sheba, and Ethiopia!",
          ["Shlomo", "Sulayman"], major=True),
        N("eth_menelik", "Menelik I (Solomonic Dynasty of Ethiopia)", "levant_egypt", 17, "c. 10th c. BCE trad. (Kebra Nagast)",
          "Founder of Ethiopia's Solomonic Dynasty", ["Kebra Nagast (Ethiopian National Epic)"],
          "Son of King Solomon and Queen Makeda of Sheba (Saba). Creates a famous African-Arabian-Israelite royal genealogy bridging Cush/Ethiopia, Sheba, and Judah!",
          ["Ebna la-Hakim", "Bayna Lehkem"], major=True),
    ]
    edges += [
        E("jud_perez", "jud_boaz_jesse", "direct", "Perez -> Hezron -> Ram -> Amminadab -> Nahshon -> Salmon -> Boaz -> Obed -> Jesse"),
        E("bib_moab", "jud_boaz_jesse", "direct", "Ruth the Moabitess marries Boaz (Ruth 4)"),
        E("jud_boaz_jesse", "jud_david", "direct", "Son of Jesse (1 Chr 2:15)"),
        E("jud_david", "jud_solomon", "direct", "Son via Bathsheba (2 Sam 12:24)"),
        E("jud_solomon", "eth_menelik", "expansion", "Kebra Nagast: Solomon + Queen Makeda of Sheba -> Menelik I"),
        E("bib_sheba_joktan", "eth_menelik", "expansion", "Queen of Sheba (Makeda / Saba) -> mother of Menelik I"),
    ]

    # Joseph + Asenath -> Manasseh & Ephraim
    add_children(nodes, edges, "tri_joseph", "biblical", 13, "Egypt (Gen 41:50-52)", [
        ("jos_manasseh", "Manasseh (son of Joseph)", {"major": True, "sources": ["Genesis 41:51", "Book of Jasher 50"], "notes": "Firstborn of Joseph & Asenath (daughter of Poti-phera, Priest of On)."}),
        ("jos_ephraim", "Ephraim (son of Joseph)", {"major": True, "sources": ["Genesis 41:52", "Book of Jasher 50"], "notes": "Second son of Joseph & Asenath; ancestor of Joshua."}),
    ])
    edges.append(E("tri_dinah", "tri_joseph", "expansion", "Jasher 49:16-18: Asenath (Joseph's wife) was Dinah's daughter raised by Poti-phera!"))

    return {"module": "03_abraham_all_nations", "title": "Complete Descendants of Abraham, Lot, Nahor II, Ishmael, Keturah, Esau & Jacob", "nodes": nodes, "edges": edges}


def build_module_04_near_east_egypt():
    nodes, edges = [], []

    # Egyptian & Cross-Biblical Identifications (User specifically asked for Moses, Noah, Enoch in Egypt!)
    nodes += [
        N("eg_ennead", "Atum → Shu/Tefnut → Geb/Nut → Osiris & Isis → Horus", "levant_egypt", 1, "Old Kingdom Pyramid Texts (c. 2400 BCE)",
          "Heliopolitan Great Ennead", ["Pyramid Texts", "Turin King List", "Manetho Aegyptiaca"],
          "Egyptian royal king lists trace historical pharaohs directly from the Ennead and Horus through the Shemsu-Hor ('Followers of Horus'). Osiris placed in a chest/ark on the Nile was later compared by syncretists to Noah.",
          ["Heliopolitan Ennead", "Nun (Primeval Waters)"], major=True),
        N("eg_thoth_saurid", "Thoth (Djehuty / Hermes) & King Saurid (Surid)", "levant_egypt", 3, "Egyptian / Greco-Egyptian & Coptic-Arabic Lore",
          "Egyptian Scribe of the Gods / Antediluvian Pyramid Builder",
          ["Pseudo-Eupolemus (2nd c. BCE)", "Corpus Hermeticum", "Akhbar al-Zaman", "al-Maqrizi Khitat", "Bar Hebraeus"],
          "Greco-Egyptian, Hermetic, Coptic, and Arabic histories explicitly identify Biblical Enoch (Idris) with Egyptian Thoth / Hermes Trismegistus and the antediluvian Egyptian King Saurid (Surid), who foresaw the Flood and built the Pyramids to preserve astronomy and sacred wisdom!",
          ["Djehuty", "Hermes Trismegistus", "Surid / Saurid", "Idris = Enoch"], major=True),
        N("eg_menes", "Menes / Narmer (1st Dynasty) & Baysar (Misrayim)", "levant_egypt", 6, "First Dynasty (c. 3100 BCE)",
          "First Historical Pharaoh of Egypt (Mizraim)", ["Narmer Palette", "Turin King List", "Manetho", "al-Maqrizi Khitat"],
          "Historical unifier of Egypt. Medieval Coptic/Arabic chronicles (al-Maqrizi) trace post-Flood Egyptian kings from Ham -> Baysar -> Misrayim (Mizraim), while Book of Jasher 14 recounts Rikayon establishing the royal title 'Pharaoh'!",
          ["Narmer", "Misr / Baysar (Coptic-Arabic lore)", "Rikayon (Jasher 14)"], major=True),
        N("eg_imhotep", "Imhotep (Vizier of Djoser / 7-Year Famine)", "levant_egypt", 12, "Old Kingdom (3rd Dynasty) / Ptolemaic Famine Stela",
          "Egyptian Sage, Architect & Famine Vizier", ["Famine Stela (Sehel Island)", "Manetho"],
          "Master architect of the Step Pyramid and high priest of Heliopolis (On). The Sehel Island Famine Stela credits Imhotep with ending a 7-year Nile famine—frequently compared in cross-cultural lore with Joseph (Zaphenath-Paneah), who wed the daughter of the Priest of On!",
          ["Compared to Joseph (Zaphenath-Paneah)"]),
        N("eg_osarseph_bithiah", "Osarseph (Manetho) / Musaeus (Artapanus) / Bithiah & Adoniah", "levant_egypt", 15, "Greco-Egyptian Chronicles (3rd-2nd c. BCE) & Jasher",
          "Egyptian & Cushite Names/Traditions of Moses",
          ["Manetho (via Josephus Against Apion 1.26)", "Artapanus (via Eusebius)", "Book of Jasher 68, 72-76"],
          "Manetho preserves an Egyptian tradition of a Heliopolitan priest named Osarseph who took the name Moses; Artapanus calls Moses 'Musaeus' (teacher of Orpheus) and Egyptian 'Hermes', leading an expedition into Cush/Ethiopia — strikingly echoing Book of Jasher 72-76 where Moses rules Cush with Queen Adoniah!",
          ["Osarseph", "Musaeus", "Queen Adoniah of Cush (Jasher 73)", "Princess Bithiah (Jasher 68)"], major=True),
        N("le_sanchuniathon", "Protogonos → Misor & Sydyk → Taaut (Thoth) & Chna (Canaan)", "levant_egypt", 6, "Phoenician-Canaanite Lore",
          "Phoenician Genealogy Bridging Egypt & Levant", ["Philo of Byblos / Sanchuniathon (via Eusebius Praep. Ev. I.10)"],
          "Explicitly names Misor (direct cognate of Biblical Mizraim!) as brother of Sydyk (Righteousness, cf. Melchizedek) and father of Taaut (Egyptian Thoth, inventor of writing), alongside Chna (Canaan).",
          ["Misor = Mizraim", "Taaut = Thoth", "Chna = Canaan"], major=True),
    ]
    edges += [
        E("hub_primordial", "eg_ennead", "parallel", "Heliopolitan primeval divine pairs & Nun"),
        E("eg_ennead", "eg_menes", "expansion", "Turin King List: Horus -> Shemsu-Hor -> Menes"),
        E("bib_enoch", "eg_thoth_saurid", "syncretic", "Pseudo-Eupolemus, Hermetic & Coptic-Arabic lore equate Enoch (Idris) with Thoth / King Saurid"),
        E("eg_ennead", "bib_noah", "syncretic", "Syncretic comparison: Osiris's Nile ark / primeval waters of Nun <-> Noah"),
        E("bib_mizraim", "eg_menes", "cognate", "Biblical Mizraim = Egypt (land of Menes / Coptic Misrayim)"),
        E("bib_mizraim", "le_sanchuniathon", "cognate", "Biblical Mizraim = Phoenician Misor"),
        E("bib_canaan", "le_sanchuniathon", "cognate", "Biblical Canaan = Phoenician Chna"),
        E("le_sanchuniathon", "eg_thoth_saurid", "cognate", "Phoenician Taaut = Egyptian Thoth"),
        E("tri_joseph", "eg_imhotep", "parallel", "7-year famine vizier linked to On/Heliopolis (Famine Stela <-> Gen 41)"),
        E("bib_moses", "eg_osarseph_bithiah", "syncretic", "Manetho's Osarseph, Artapanus's Musaeus & Jasher's King of Cush"),
        E("bib_cush", "eg_osarseph_bithiah", "expansion", "Jasher 72-76 & Josephus Ant. 2.10: Moses rules Cush & marries Queen Adoniah"),
    ]

    # Mesopotamian
    nodes += [
        N("mes_enuma", "Apsu & Tiamat → Anu → Enki (Ea) → Marduk", "mesopotamian", 1, "c. 1800-1100 BCE texts",
          "Creation of Humanity (Lullu) from Clay", ["Enuma Elish", "Atrahasis Tablet I"],
          "Enki (Ea) and Nintu shape the first humans (Lullu) from clay mixed with divine blood, paralleling Genesis's creation of Adam from dust.", major=True),
        N("mes_alulim", "Alulim of Eridu → Antediluvian Kings (1-6)", "mesopotamian", 2, "Antediluvian (Sumerian King List)",
          "Sumerian Pre-Flood Dynasty", ["Sumerian King List (WB 444)", "Berossus Babyloniaca"],
          "8 kings in the Sumerian King List (10 in Berossus: Aloros -> Alaparos -> Amelon -> Ammenon -> Megalaros -> Daonos), reigning vast lifespans before the Flood — paralleling Genesis 5's 10 patriarchs.",
          ["Aloros (Berossus)"], major=True),
        N("mes_enmeduranki", "En-men-dur-ana (Enmeduranki, 7th King of Sippar)", "mesopotamian", 3, "Antediluvian Gen 7",
          "7th King / Initiated into Heavenly Secrets by Shamash", ["Sumerian King List", "Enmeduranki Text (K 2486)", "Berossus"],
          "7th antediluvian king, ruler of Sippar (city of sun god Shamash), admitted to heaven to learn celestial tablets and divination — widely recognized parallel to Enoch (7th patriarch, 365 solar years).",
          ["Euedorachos (Berossus)"], major=True),
        N("mes_ziusudra", "Ubara-Tutu → Ziusudra / Utnapishtim / Atrahasis", "mesopotamian", 4, "Flood Horizon",
          "Mesopotamian Great Flood Survivor", ["Eridu Genesis", "Atrahasis", "Epic of Gilgamesh XI", "Berossus"],
          "King/sage of Shuruppak warned by Enki/Ea; builds a vessel preserving family and animals, sends out dove/swallow/raven, lands on Mt. Nimush.",
          ["Xisouthros (Berossus)"], major=True),
        N("mes_uruk_gilgamesh", "Meskiaggasher → Enmerkar → Lugalbanda → Gilgamesh", "mesopotamian", 7, "Early Dynastic II (c. 2700 BCE)",
          "Hero-Kings of Uruk (Biblical Erech)", ["Sumerian King List", "Epic of Gilgamesh", "Qumran Book of Giants (4Q530)"],
          "Gilgamesh journeys to Flood survivor Utnapishtim. Uruk is explicitly named 'Erech' in Gen 10:10 — and remarkably, 'Gilgamesh' is ALSO named as one of the Giants in the Dead Sea Scrolls Book of Giants (4Q530)!",
          ["Erech (Gen 10:10)", "Gilgamesh in Qumran 4Q530"], major=True),
        N("mes_sargon", "Sargon of Akkad → Enheduanna & Naram-Sin", "mesopotamian", 8, "Akkadian Empire (c. 2334-2154 BCE)",
          "First Imperial Dynasty of Mesopotamia (Accad)", ["Sumerian King List", "Birth Legend of Sargon"],
          "Founder of Akkad (Biblical 'Accad' in Gen 10:10). Note also the striking 'basket in the river sealed with bitumen' motif in Sargon's Birth Legend paralleling Moses in Exodus 2!",
          ["Sharru-kin", "Accad (Gen 10:10)"], major=True),
    ]
    edges += [
        E("hub_primordial", "mes_enuma", "parallel", "Humans fashioned from clay + divine blood"),
        E("mes_enuma", "mes_alulim", "direct", "Kingship descends to Eridu (Sumerian King List)"),
        E("mes_alulim", "mes_enmeduranki", "direct", "Antediluvian royal succession to 7th king"),
        E("mes_enmeduranki", "mes_ziusudra", "direct", "Succession to Ubara-Tutu -> Ziusudra"),
        E("mes_ziusudra", "mes_uruk_gilgamesh", "expansion", "Post-Flood kingship restored at Kish & Uruk"),
        E("mes_uruk_gilgamesh", "mes_sargon", "expansion", "Sumerian King List: Uruk -> Akkad"),
        E("bib_enoch", "mes_enmeduranki", "parallel", "7th antediluvian figure; solar/heavenly ascent & tablets"),
        E("hub_flood", "mes_ziusudra", "parallel", "Vessel on Mt. Nimush (Atrahasis / Gilgamesh XI)"),
        E("bib_nimrod", "mes_uruk_gilgamesh", "cognate", "Gen 10:10 explicitly names Shinar, Babel & Erech (Uruk)"),
        E("bib_nimrod", "mes_sargon", "cognate", "Gen 10:10 explicitly names Accad (Akkad) & Nineveh"),
        E("bib_asshur", "mes_sargon", "cognate", "Asshur = Assyria (Mesopotamian sphere)"),
        E("eno_ohya_hahya", "mes_uruk_gilgamesh", "expansion", "Qumran Book of Giants (4Q530/4Q531) literally names Gilgamesh as one of the Giants!"),
        E("bib_moses", "mes_sargon", "parallel", "Reed basket sealed with bitumen placed in river (Exod 2 <-> Sargon Birth Legend)"),
    ]

    # Iranian / Zoroastrian
    nodes += [
        N("ir_gayomart", "Gayomart (Keyumars) → Mashya & Mashyana", "iranian", 1, "Primordial (Avesta / Bundahishn)",
          "First Mortal & Primeval Iranian Couple", ["Avesta (Yasht 13)", "Bundahishn Ch. 14", "Shahnameh"],
          "Created by Ahura Mazda. From Gayomart's seed grew a rhubarb plant splitting into Mashya & Mashyana, bearing 7 twin pairs populating the 7 climes of the world.", major=True),
        N("ir_vivanghant", "Siamak → Hushang → Tahmuras → Vivanghant", "iranian", 3, "Mythic Pishdadian Era",
          "Father of Yima / Exact Proto-Indo-Iranian Bridge", ["Avesta (Yasna 9.4, Vendidad 2)", "Bundahishn"],
          "EXACT linguistic & genealogical cognate of Vedic Vivasvan (Surya)! One of the strongest academically verified prehistoric ancestral bridges between Iran and India.",
          ["Vivanhao"], major=True),
        N("ir_yima", "Yima Khshaeta (Jamshid)", "iranian", 4, "Cataclysm / Golden Age Horizon",
          "Golden Age King & Vara Ark Builder", ["Avesta (Vendidad 2, Yasna 9)", "Shahnameh"],
          "Son of Vivanghant — exact Proto-Indo-Iranian cognate of Vedic Yama. Warned by Ahura Mazda of a world-destroying winter/meltwater cataclysm, builds the subterranean Vara preserving pairs of humans, animals, and seeds.",
          ["Jamshid"], major=True),
        N("ir_fereydun", "Fereydun (Thraetaona)", "iranian", 5, "Post-Cataclysm Pishdadian Era",
          "Divider of the World Among Three Sons", ["Avesta (Yasht 5, 19)", "Bundahishn", "Shahnameh"],
          "Divides the earth into three realms among his sons Salm (West), Tur (Turan/Steppe), and Iraj (Iran) — striking tripartite parallel to Noah.", major=True),
        N("ir_salm", "Salm (West / Rum)", "iranian", 6, "Tripartite Division (Shahnameh)", "Ancestor of Western Realms", ["Bundahishn Ch. 35", "Shahnameh"], "Eldest son of Fereydun; receives Anatolia and the West (Rum)."),
        N("ir_tur", "Tur (Turan / Central Asia)", "iranian", 6, "Tripartite Division (Shahnameh)", "Ancestor of Turan / Steppe", ["Bundahishn Ch. 35", "Shahnameh"], "Second son of Fereydun; receives Turan (Central Asian steppes to China's borders)."),
        N("ir_iraj", "Iraj (Iran → Manuchehr → Kayanians)", "iranian", 6, "Tripartite Division (Shahnameh)", "Ancestor of Iranian Royal Line", ["Bundahishn Ch. 35", "Shahnameh"], "Youngest son of Fereydun; receives Iran (Eranshahr), producing Manuchehr and the Kayanian dynasty (Kay Kavad, Kay Kavus, Siyavash, Kay Khosrow).", major=True),
        N("ir_medes_achaemenids", "Medes (Mada) & Cyrus the Great (Achaemenids)", "iranian", 8, "Iron Age (8th-6th c. BCE)",
          "Historical Iranian Empires", ["Behistun Inscription", "Cyrus Cylinder", "Herodotus", "Ezra / Daniel"],
          "Historical Medes directly match Biblical Madai (Gen 10:2); Cyrus ruled as King of Anshan in Elam (Gen 10:22).", major=True),
    ]
    edges += [
        E("hub_primordial", "ir_gayomart", "parallel", "First mortal -> Mashya & Mashyana"),
        E("ir_gayomart", "ir_vivanghant", "direct", "Siamak -> Hushang -> Tahmuras -> Vivanghant"),
        E("ir_vivanghant", "ir_yima", "direct", "Son (Avesta Yasna 9.4)"),
        E("ir_yima", "ir_fereydun", "direct", "Pishdadian lineage via Abtin/Athwya (Shahnameh)"),
        E("ir_fereydun", "ir_salm", "direct", "1st son (West / Rum)"),
        E("ir_fereydun", "ir_tur", "direct", "2nd son (Turan / Steppe)"),
        E("ir_fereydun", "ir_iraj", "direct", "3rd son (Iran / Eranshahr)"),
        E("ir_iraj", "ir_medes_achaemenids", "expansion", "Iraj -> Kayanian -> Historical Medes & Persians"),
        E("hub_flood", "ir_yima", "parallel", "Vara enclosure against cataclysmic winter/melt"),
        E("hub_world_division", "ir_fereydun", "parallel", "Tripartite division: Salm / Tur / Iraj"),
        E("bib_madai", "ir_medes_achaemenids", "cognate", "Madai (Gen 10:2) = Historical Medes (Old Persian Mada)"),
        E("bib_elam", "ir_medes_achaemenids", "cognate", "Elam (Gen 10:22) = SW Iran / Cyrus King of Anshan"),
        E("bib_noah", "ir_gayomart", "syncretic", "al-Tabari & medieval chronicles equate Gayomart with Adam/Noah's kin"),
    ]

    return {"module": "04_near_east_egypt", "title": "Egyptian Cross-Traditions, Mesopotamia, Phoenicia & Iran", "nodes": nodes, "edges": edges}


def build_module_05_asia_steppe():
    nodes, edges = [], []

    # Vedic & Puranic India (with Yayati's 5 sons individualized!)
    nodes += [
        N("ved_brahma_manu", "Brahma → Svayambhuva Manu & Shatarupa", "vedic", 1, "Satya Yuga / Rigvedic",
          "Vedic Primordial Ancestors & Saptarishis", ["Manusmriti Ch. 1", "Vishnu Purana I", "Bhagavata Purana III"],
          "Brahma manifests Svayambhuva Manu and Shatarupa as the primordial couple, plus the Seven Sages (Marichi, Atri, Angiras, Pulastya, Pulaha, Kratu, Vashishta).", major=True),
        N("ved_kashyapa", "Marichi → Kashyapa (+ Aditi, Diti, Danu)", "vedic", 2, "Vedic Primordial Era",
          "Universal Prajapati Sage", ["Mahabharata Adi Parva", "Vishnu Purana I.15"],
          "Through Daksha's daughters, Kashyapa fathers the Adityas (including Vivasvan/Surya via Aditi), Daityas, Danavas, Garudas, and Nagas.", major=True),
        N("ved_vivasvan", "Vivasvan (Surya)", "vedic", 3, "Vedic Antediluvian Horizon",
          "Exact Cognate of Avestan Vivanghant", ["Rigveda 10.14, 10.17", "Shatapatha Brahmana"],
          "EXACT Proto-Indo-Iranian cognate of Avestan Vivanghant! Father of Yama (Avestan Yima) and Vaivasvata Manu (Great Flood survivor).", major=True),
        N("ved_yama", "Yama & Yami", "vedic", 4, "Vedic Primordial Horizon",
          "Twin First Mortals / Exact Cognate of Yima", ["Rigveda 10.10, 10.14"],
          "Son of Vivasvan; exact linguistic and genealogical twin of Iranian Yima (Jamshid) son of Vivanghant.", major=True),
        N("ved_vaivasvata_manu", "Vaivasvata Manu (7th Manu / Flood Survivor)", "vedic", 4, "Vedic Flood Horizon",
          "Vedic Great Flood Survivor (Saved by Matsya)", ["Shatapatha Brahmana 1.8.1", "Mahabharata Vana Parva", "Matsya Purana"],
          "Saved by Matsya the Fish during the universal Deluge; ship moored to the Himalayas. Common ancestor of humanity (Manava) in the present age.", major=True),
        N("ved_surya_vamsha", "Ikshvaku → Raghu → Dasharatha → Rama & Buddha (Shakya)", "vedic", 6, "Treta Yuga → 6th c. BCE",
          "Surya Vamsha (Solar Dynasty)", ["Valmiki Ramayana", "Vishnu Purana IV", "Mahavamsa / Pali Canon"],
          "Son of Vaivasvata Manu. Produces Harishchandra, Bhagiratha, Raghu, and Prince Rama. Buddhist chronicles (Mahavamsa, Ambattha Sutta) trace Siddhartha Gautama's Shakya clan to King Okkaka = Ikshvaku!", major=True),
        N("ved_yayati", "Atri → Soma → Budha + Ila → Pururavas → Yayati", "vedic", 5, "Early Vedic Royal Horizon",
          "Chandra Vamsha (Lunar Dynasty) / Father of 5 Peoples", ["Rigveda 10.95", "Mahabharata Adi Parva 75-85", "Vishnu Purana IV"],
          "Unites Rishi Atri's lunar line with Vaivasvata Manu's bloodline via Ila. Great-grandson Yayati fathers the five famous Vedic peoples (Panchajana).", major=True),
        N("ved_bharata_kuru", "Bharata → Kuru → Pandavas & Kauravas (Mahabharata)", "vedic", 8, "Late Vedic / Iron Age (c. 1200-900 BCE)",
          "Eponym of Bharatavarsha (India)", ["Mahabharata", "Vishnu Purana IV.19-21"],
          "Emperor Bharata gives India its classical name. Descends through Kuru to the Pandavas (Arjuna -> Abhimanyu -> Parikshit).", major=True),
    ]
    add_children(nodes, edges, "ved_yayati", "vedic", 6, "Rigvedic Panchajana (5 Sons of Yayati)", [
        ("ved_yadu", "Yadu (Yadavas → Krishna & Balarama)", {"major": True, "notes": "Eldest son of Yayati & Devayani; ancestor of the Yadava dynasty including Krishna and Balarama."}),
        ("ved_turvasu", "Turvasu", {"notes": "Son of Yayati & Devayani; associated in Puranas with southern/western tribes."}),
        ("ved_druhyu", "Druhyu (Gandhara / NW Tribes)", {"notes": "Son of Yayati & Sharmishtha; Puranas trace NW Gandhara and trans-Indus Central Asian/Mleccha tribes to Druhyu!"}),
        ("ved_anu", "Anu (Anga, Vanga, Kalinga, Shibi)", {"notes": "Son of Yayati & Sharmishtha; ancestor of northern and eastern Indian kingdoms."}),
        ("ved_puru", "Puru (Pauravas)", {"major": True, "notes": "Youngest son of Yayati & Sharmishtha; inherits the central realm and fathers the Bharata/Kuru dynasty."}),
    ], default_sources=["Rigveda 1.108.8", "Mahabharata Adi Parva 85", "Vishnu Purana IV"])

    edges += [
        E("hub_primordial", "ved_brahma_manu", "parallel", "Svayambhuva Manu & Shatarupa"),
        E("ved_brahma_manu", "ved_kashyapa", "direct", "Brahma -> Marichi -> Kashyapa"),
        E("ved_kashyapa", "ved_vivasvan", "direct", "Kashyapa + Aditi -> Vivasvan (Surya)"),
        E("ved_vivasvan", "ved_yama", "direct", "Son (Rigveda 10.14)"),
        E("ved_vivasvan", "ved_vaivasvata_manu", "direct", "Son (Shatapatha Brahmana)"),
        E("ved_vaivasvata_manu", "ved_surya_vamsha", "direct", "Son Ikshvaku -> Solar Dynasty"),
        E("ved_vaivasvata_manu", "ved_yayati", "direct", "Via Ila + Budha -> Pururavas -> Yayati"),
        E("ved_brahma_manu", "ved_yayati", "direct", "Brahma -> Atri -> Soma -> Budha"),
        E("ved_puru", "ved_bharata_kuru", "direct", "Puru -> Bharata -> Kuru -> Pandavas"),
        E("ir_vivanghant", "ved_vivasvan", "cognate", "EXACT Proto-Indo-Iranian cognate: Vivanghant = Vivasvan"),
        E("ir_yima", "ved_yama", "cognate", "EXACT Proto-Indo-Iranian cognate: Yima = Yama"),
        E("hub_flood", "ved_vaivasvata_manu", "parallel", "Ship towed by Matsya to Himalayas"),
        E("hub_world_division", "ved_yayati", "parallel", "Yayati's 5 Sons (Panchajana)"),
        E("bib_abraham", "ved_brahma_manu", "syncretic", "Folkloric/syncretic comparison of Abraham/Sarah <-> Brahma/Saraswati (non-cognate)"),
    ]

    # Ancient China, Korea, Japan & Steppe
    nodes += [
        N("chn_fuxi_nuwa", "Fuxi & Nüwa (Three Sovereigns)", "chinese", 1, "Primordial / Three Sovereigns",
          "Primordial Sibling-Consorts & Clay Creators", ["Shan Hai Jing", "Huainanzi", "Fengsu Tongyi"],
          "Serpent-tailed creators who mend heaven after Gonggong's flood and mold humans from yellow clay; preserved in SW Chinese lore as Great Flood survivors.", major=True),
        N("chn_yandi", "Yandi (Flame Emperor / Shennong)", "chinese", 2, "Three Sovereigns",
          "Co-Ancestor of Huaxia (Yan-Huang)", ["Shiji Ch. 1", "Guoyu", "Yijing"],
          "Guoyu records Yandi (Jiang clan) and Huangdi (Ji clan) as half-brothers born of Shaodian; their alliance forms the unified Yan-Huang ancestry.", major=True),
        N("chn_huangdi", "Huangdi (Yellow Emperor) & Leizu", "chinese", 2, "Five Emperors (c. 2697 BCE trad.)",
          "Universal Royal Ancestor in Sima Qian's Shiji", ["Sima Qian Shiji Ch. 1", "Bamboo Annals", "Da Dai Liji"],
          "Sima Qian traces ALL Five Emperors, all Three Dynasties (Xia, Shang, Zhou), Qin, Chu, and the northern Xiongnu back to Huangdi's 25 sons (14 surnames).", major=True),
        N("chn_zhuanxu", "Changyi → Zhuanxu (Gaoyang)", "chinese", 3, "Five Emperors Era",
          "Ancestor of Xia, Shun, Chu & Qin", ["Shiji Ch. 1, 2, 5", "Shan Hai Jing"],
          "Grandson of Huangdi; separates Heaven and Earth; progenitor of Gun -> Yu the Great (Xia), Emperor Shun, and the House of Ying (Qin Shi Huang).", major=True),
        N("chn_yu_xia", "Gun → Yu the Great (Da Yu) → Qi (Xia Dynasty)", "chinese", 4, "Great Flood / Xia (c. 2070-1600 BCE)",
          "Chinese Great Flood Hero & First Hereditary Dynasty", ["Shangshu (Yu Gong)", "Shiji Ch. 2", "Bamboo Annals"],
          "Dredges rivers to tame the Gun-Yu Great Flood across the Nine Provinces; establishes the Xia Dynasty.", major=True),
        N("chn_ku_yao_shun", "Emperor Ku (Di Ku) → Emperor Yao & Shun", "chinese", 5, "Five Emperors Era (c. 2350-2200 BCE trad.)",
          "Sage Emperors & Ancestor of Shang/Zhou", ["Shiji Ch. 1, 3, 4", "Shangshu"],
          "Great-grandson of Huangdi via Xuanxiao -> Jiaoji; fathers Emperor Yao, Xie (Shang), and Hou Ji (Zhou).", major=True),
        N("chn_shang", "Xie → Tang of Shang (Shang Dynasty → Confucius)", "chinese", 6, "Bronze Age China (c. 1600-1046 BCE)",
          "Oracle-Bone Dynasty (Zi Clan)", ["Anyang Oracle Bones", "Shiji Ch. 3", "Shijing"],
          "Historically attested by oracle bones at Anyang; Confucius traced his ancestry to the Shang royal line via the Dukes of Song.", major=True),
        N("chn_zhou", "Hou Ji (Lord Millet) → King Wen & Wu (Zhou Dynasty)", "chinese", 6, "Bronze/Iron Age China (1046-256 BCE)",
          "Classical Zhou Dynasty (Ji Clan)", ["Shiji Ch. 4", "Shijing"],
          "Descended from Di Ku & Jiang Yuan via Hou Ji; established the Mandate of Heaven and classical Chinese philosophy era.", major=True),

        N("jk_izanagi_amaterasu", "Izanagi & Izanami → Amaterasu & Susanoo", "japan_korea", 1, "Age of the Gods (Kamiyo)",
          "Japanese Primordial Couple & Sun Goddess", ["Kojiki (712 CE)", "Nihon Shoki (720 CE)"],
          "Create the Japanese archipelago and birth Amaterasu (Sun), Tsukuyomi (Moon), and Susanoo (Storm).", major=True),
        N("jk_dangun", "Hwanin → Hwanung + Ungnyeo → Dangun Wanggeom", "japan_korea", 5, "Traditional 2333 BCE (Gojoseon)",
          "Progenitor of Korea", ["Samguk Yusa", "Jewang Ungi"],
          "Founder of Gojoseon; later annals also link Shang prince Jizi (Gija) migrating to Joseon after 1046 BCE.", major=True),
        N("jk_jimmu", "Ninigi → Hoori → Emperor Jimmu", "japan_korea", 6, "Traditional 660 BCE",
          "Founder of Japan's Continuous Imperial Line", ["Kojiki Book II", "Nihon Shoki Book III"],
          "Descendant of Amaterasu through Ninigi's descent to Mount Takachiho; founder of the Yamato Imperial House.", major=True),

        N("stp_xiongnu", "Chunwei → Xiongnu (Modu Chanyu)", "steppe", 6, "Bronze Age → 3rd c. BCE",
          "Sima Qian's Bridge Between Chinese Xia & Steppe", ["Sima Qian Shiji Ch. 110"],
          "Sima Qian explicitly records that the Xiongnu descended from Chunwei, a prince of the Chinese Xia Dynasty.", major=True),
        N("stp_oghuz", "Turk (Oljai Khan) → Oghuz Khagan (6 Sons / 24 Tribes)", "steppe", 8, "Mythic Steppe / Medieval Synthesis",
          "Eponymous Ancestor of Turkic Peoples", ["Oghuzname", "Rashid al-Din Jami al-Tawarikh (1307)", "Abulghazi Shajara-i Tarakima"],
          "Rashid al-Din & Abulghazi explicitly graft Turkic/Mongol ancestry onto Biblical Japheth (Yafith -> Oljai -> Tatar & Mongol -> Kara Khan -> Oghuz Khagan -> Gun, Ay, Yildiz, Gok, Dag, Deniz) and Iranian Turan.", major=True),
    ]
    edges += [
        E("hub_primordial", "chn_fuxi_nuwa", "parallel", "Nüwa molds humans from yellow clay"),
        E("hub_primordial", "jk_izanagi_amaterasu", "parallel", "Primordial island-creator couple"),
        E("chn_fuxi_nuwa", "chn_yandi", "expansion", "Three Sovereigns succession"),
        E("chn_yandi", "chn_huangdi", "expansion", "Guoyu: Half-brothers from Shaodian (Yan-Huang)"),
        E("chn_huangdi", "chn_zhuanxu", "direct", "Huangdi -> Changyi -> Zhuanxu (Shiji Ch. 1)"),
        E("chn_zhuanxu", "chn_yu_xia", "direct", "Zhuanxu -> Gun -> Yu the Great -> Xia"),
        E("chn_huangdi", "chn_ku_yao_shun", "direct", "Huangdi -> Xuanxiao -> Jiaoji -> Di Ku -> Yao"),
        E("chn_zhuanxu", "chn_ku_yao_shun", "direct", "Zhuanxu -> ... -> Emperor Shun"),
        E("chn_ku_yao_shun", "chn_shang", "direct", "Di Ku + Jiandi -> Xie -> Shang Dynasty"),
        E("chn_ku_yao_shun", "chn_zhou", "direct", "Di Ku + Jiang Yuan -> Hou Ji -> Zhou Dynasty"),
        E("chn_shang", "jk_dangun", "expansion", "Shang prince Jizi (Gija) migrates to Gojoseon"),
        E("jk_izanagi_amaterasu", "jk_jimmu", "direct", "Amaterasu -> Ninigi -> Hoori -> Emperor Jimmu"),
        E("chn_yu_xia", "stp_xiongnu", "expansion", "Shiji Ch. 110: Xiongnu descend from Chunwei of Xia"),
        E("stp_xiongnu", "stp_oghuz", "expansion", "Steppe continuity: Modu Chanyu linked to Oghuz legend"),
        E("bib_japheth", "stp_oghuz", "syncretic", "Rashid al-Din (1307): Yafith (Japheth) -> Turk -> Oghuz Khagan"),
        E("jas_tog_tarki", "stp_oghuz", "syncretic", "Book of Jasher 10:10 Tarki (son of Togarmah) <-> Turkic lineage"),
        E("ir_tur", "stp_oghuz", "syncretic", "Tur (Turan) equated in Persian/Turkic lore with Turkic Steppe"),
        E("bib_noah", "chn_fuxi_nuwa", "syncretic", "17th-c. Figurists compared Noah to Fuxi"),
        E("hub_flood", "chn_yu_xia", "parallel", "Gun-Yu Great Flood & channeling of rivers"),
        E("hub_world_division", "chn_huangdi", "parallel", "Huangdi's 25 Sons -> Xia, Shang, Zhou, Xiongnu"),
    ]

    return {"module": "05_asia_steppe", "title": "Vedic/Puranic India, China, Korea, Japan & Eurasian Steppe", "nodes": nodes, "edges": edges}


def main():
    MODULES_DIR.mkdir(parents=True, exist_ok=True)
    builders = [
        build_module_01_antediluvian,
        build_module_02_table_of_nations,
        build_module_03_abraham_all_nations,
        build_module_04_near_east_egypt,
        build_module_05_asia_steppe,
    ]

    all_nodes, all_edges = [], []
    module_summaries = []

    for fn in builders:
        mod = fn()
        mod_path = MODULES_DIR / f"{mod['module']}.json"
        with open(mod_path, "w", encoding="utf-8") as f:
            json.dump(mod, f, indent=2, ensure_ascii=False)
        all_nodes.extend(mod["nodes"])
        all_edges.extend(mod["edges"])
        module_summaries.append({"file": mod["module"], "title": mod["title"], "nodes": len(mod["nodes"]), "edges": len(mod["edges"])})

    # Validate strictly
    nodes_by_id = {}
    for n in all_nodes:
        assert n["id"] not in nodes_by_id, f"Duplicate node ID: {n['id']}"
        assert n["tradition"] in TRADITIONS, f"Unknown tradition: {n['tradition']}"
        nodes_by_id[n["id"]] = n

    seen_edges = set()
    clean_edges = []
    for idx, e in enumerate(all_edges):
        assert e["from"] in nodes_by_id, f"Edge {idx} missing from: {e['from']}"
        assert e["to"] in nodes_by_id, f"Edge {idx} missing to: {e['to']}"
        assert e["type"] in LINK_TYPES, f"Unknown link type: {e['type']}"
        key = (e["from"], e["to"], e["type"], e["label"])
        if key not in seen_edges:
            seen_edges.add(key)
            clean_edges.append(e)

    compiled = {
        "metadata": {
            "title": "Ancient World Genealogy Atlas — Exhaustive Multi-Tradition Database (Phase 2)",
            "version": "2.0.0",
            "modules": module_summaries,
            "linkTypes": LINK_TYPES,
        },
        "traditions": TRADITIONS,
        "nodes": all_nodes,
        "edges": clean_edges,
    }

    for target in (OUT_ALL, OUT_CORE):
        with open(target, "w", encoding="utf-8") as f:
            json.dump(compiled, f, indent=2, ensure_ascii=False)

    trad_counts = Counter(n["tradition"] for n in all_nodes)
    edge_counts = Counter(e["type"] for e in clean_edges)
    major_count = sum(1 for n in all_nodes if n.get("major"))

    print(f"BUILT & VALIDATED OK: {len(all_nodes)} individuals/nodes ({major_count} major landmarks), {len(clean_edges)} edges across {len(module_summaries)} modules")
    print("\nModules:")
    for m in module_summaries:
        print(f"  - {m['file']}: {m['nodes']} nodes, {m['edges']} edges ({m['title']})")
    print("\nNodes by tradition:")
    for k, v in trad_counts.most_common():
        print(f"  - {TRADITIONS[k]['label']}: {v}")
    print("\nEdges by provenance tier:")
    for k, v in edge_counts.most_common():
        print(f"  - {k}: {v}")


if __name__ == "__main__":
    main()
