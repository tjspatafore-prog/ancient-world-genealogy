"""
Modular Ancient World Genealogy Dataset Builder & Validator (Phase 4).

Compiles clean modular JSON files under data/modules/ into data/world_genealogy.json
for the interactive web explorer, ensuring zero broken links, full provenance tagging,
and exhaustive person-by-person accounting across 8 modules.
"""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = ROOT / "data" / "modules"
OUT_ALL = ROOT / "data" / "world_genealogy.json"
OUT_CORE = ROOT / "data" / "genealogy_core.json"

TRADITIONS = {
    "archetype":    {"label": "Global Convergence Hubs",        "region": "Worldwide Comparative Layer",  "color": "#6366f1", "order": 0},
    "african":      {"label": "African, Cushite & Ethiopian",   "region": "Nubia / Ethiopia / Africa",    "color": "#16a34a", "order": 1},
    "levant_egypt": {"label": "Egyptian & Canaanite-Phoenician","region": "Nile / Eastern Mediterranean", "color": "#0d9488", "order": 2},
    "greek":        {"label": "Greek & Mediterranean",          "region": "Aegean / Anatolia / Italy",    "color": "#0284c7", "order": 3},
    "biblical":     {"label": "Biblical & Extra-Biblical",      "region": "Levant / Ancient Near East",   "color": "#d97706", "order": 4},
    "arabian":      {"label": "Arabian (Adnanite & Qahtanite)", "region": "Arabian Peninsula",            "color": "#ca8a04", "order": 5},
    "mesopotamian": {"label": "Mesopotamian (Sumer / Akkad)",   "region": "Mesopotamia",                  "color": "#2563eb", "order": 6},
    "iranian":      {"label": "Iranian / Zoroastrian",          "region": "Iranian Plateau / Central Asia","color": "#9333ea", "order": 7},
    "vedic":        {"label": "Vedic & Puranic Indian",         "region": "South Asia / Indus-Ganges",    "color": "#ea580c", "order": 8},
    "steppe":       {"label": "Eurasian Steppe / Turkic",       "region": "Inner Asia / Eurasian Steppe", "color": "#059669", "order": 9},
    "chinese":      {"label": "Ancient Chinese (Sinitic)",      "region": "East Asia / Yellow River",     "color": "#dc2626", "order": 10},
    "japan_korea":  {"label": "Ancient Japanese & Korean",      "region": "East Asia / Archipelago",      "color": "#db2777", "order": 11},
}

LINK_TYPES = {
    "direct":    "Explicit parent-child or biological descent within primary canonical/ancient texts",
    "expansion": "Matriarchs, additional children, royal successions, or migrations supplied by extra-biblical or secondary chronicles (Book of Jasher, Jubilees, 1 Enoch, Manetho, Kebra Nagast, Sumerian King List, Bundahishn, Shahnameh, Shiji, Puranas)",
    "cognate":   "Linguistically or historically attested cross-tradition identity/ethnonym bridge (e.g., Taharqa = Tirhakah; Merneptah Stele = Israel; Shoshenq I = Shishak; Ptah = Naphtuhim; Vedic Vivasvan/Yama/Aptya = Avestan Vivanghant/Yima/Athwya; Madai = Medes)",
    "parallel":  "Independent structural/archetypal parallel across ancient corpora (Great Flood survivors, 7th sage, Imhotep/Joseph famine, Adapa/Adam, Sargon/Moses basket, tripartite world division)",
    "syncretic": "Ancient, Greco-Egyptian, or medieval chronicler identification bridging figures across cultures (e.g., Enoch = Thoth/Saurid; Moses = Osarseph/Musaeus; Noah = Osiris/Nun; Japheth = Oghuz Khagan; Zepho = King of Kittim/Rome)"
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


def load_existing_module(filename):
    path = MODULES_DIR / f"{filename}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_module_04_egypt_levant():
    nodes, edges = [], []

    # 1. Primordial Heliopolitan & Memphite Divine Dynasties (Pyramid Texts, Turin King List, Manetho)
    nodes += [
        N("eg_nun_atum", "Nun (Primeval Waters) → Atum / Ra (Re)", "levant_egypt", 1, "Heliopolitan Cosmogony (Pyramid Texts)",
          "Creator Deity of Heliopolis (On)", ["Pyramid Texts", "Turin King List", "Manetho"],
          "Atum-Ra emerges from the primeval flood-waters of Nun (often compared to cosmic Flood waters) to generate Shu & Tefnut.",
          ["Atum-Ra", "Nun"], major=True),
        N("eg_ptah", "Ptah (Creator of Memphis — Hikuptah)", "levant_egypt", 1, "Memphite Theology (Shabaka Stone)",
          "Creator Deity of Memphis / Eponym of Egypt & Naphtuhim", ["Shabaka Stone", "Manetho Aegyptiaca"],
          "Manetho places Ptah (Hephaestus) at the head of Egypt's divine kings! His temple Hikuptah ('House of the Ka of Ptah') gave Greece the word 'Aigyptos' (Egypt), and 'Na-Ptah' ('People of Ptah') is the exact linguistic cognate of Biblical Naphtuhim (Gen 10:13)!",
          ["Hephaestus (Manetho)", "Root of 'Egypt' & Naphtuhim"], major=True),
        N("eg_shu_tefnut", "Shu & Tefnut → Geb & Nut", "levant_egypt", 2, "Heliopolitan Ennead",
          "Air/Moisture & Earth/Sky Pairs", ["Pyramid Texts", "Turin King List"],
          "Parents of Osiris, Isis, Set, and Nephthys — recorded as divine pre-dynastic sovereigns in the Turin King List."),
        N("eg_ennead", "Osiris (Usir) & Isis (Aset) / Set & Nephthys", "levant_egypt", 2, "Heliopolitan Ennead",
          "Divine Sovereign Pair (Nile Ark Motif)", ["Pyramid Texts", "Plutarch De Iside", "Turin King List"],
          "Osiris reigns as Egypt's first mortal-like civilizing king, is sealed in a chest/ark floated down the Nile by Set (compared by syncretists to Noah's Ark!), and resurrects via Isis to sire Horus. Nephthys & Osiris/Set parent Anubis.",
          ["Usir & Aset", "Osiris Ark <-> Noah"], major=True),
        N("eg_horus", "Horus (Heru) & Shemsu-Hor ('Followers of Horus')", "levant_egypt", 3, "Predynastic Horizon (Turin King List)",
          "Living Prototype of Every Egyptian Pharaoh", ["Turin King List", "Manetho"],
          "Son of Osiris & Isis; rules Egypt before passing sovereignty through the Shemsu-Hor ('Followers of Horus' / demigods) to Narmer/Menes.", major=True),
        N("eg_thoth_saurid", "Thoth (Djehuty / Hermes) & King Saurid (Surid)", "levant_egypt", 3, "Egyptian / Greco-Egyptian & Coptic-Arabic Lore",
          "Scribe of the Gods / Antediluvian Pyramid Builder", ["Pseudo-Eupolemus (2nd c. BCE)", "Corpus Hermeticum", "Akhbar al-Zaman", "al-Maqrizi Khitat", "Bar Hebraeus"],
          "Manetho lists Thoth (Hermes) among Egypt's divine sovereigns. Greco-Egyptian, Hermetic, and Coptic-Arabic histories explicitly identify Biblical Enoch (Idris) with Thoth / Hermes Trismegistus and antediluvian King Saurid, who foresaw the Flood and built the Pyramids to preserve astronomy!",
          ["Djehuty", "Hermes Trismegistus", "Surid / Saurid", "Idris = Enoch"], major=True),
        N("eg_philemon", "Hujib → Philemon (Aflimun, Egyptian Priest on Noah's Ark)", "levant_egypt", 4, "Coptic-Arabic Flood Chronicle",
          "Egyptian Sage Preserving Pre-Flood Lore", ["Akhbar al-Zaman", "al-Maqrizi Khitat"],
          "Coptic-Arabic chronicles describe Philemon (descendant/priest of King Saurid's line) joining Noah on the Ark and guiding Ham's grandson Misrayim (Mizraim) back to resettle Egypt after the Flood!"),
    ]
    edges += [
        E("hub_primordial", "eg_nun_atum", "parallel", "Heliopolitan primeval creation out of Nun"),
        E("eg_nun_atum", "eg_shu_tefnut", "direct", "Atum -> Shu & Tefnut -> Geb & Nut"),
        E("eg_shu_tefnut", "eg_ennead", "direct", "Geb + Nut -> Osiris, Isis, Set, Nephthys"),
        E("eg_ennead", "eg_horus", "direct", "Osiris + Isis -> Horus -> Shemsu-Hor (Turin King List)"),
        E("eg_ptah", "eg_nun_atum", "expansion", "Manetho: Ptah (Hephaestus) -> Ra (Helios) -> Shu -> Geb -> Osiris"),
        E("eg_ptah", "bib_naphtuhim", "cognate", "Naphtuhim (Gen 10:13) = Egyptian Na-Ptah ('People of Ptah / Memphis')!"),
        E("eg_horus", "eg_thoth_saurid", "expansion", "Turin King List & Manetho: Thoth rules after Horus"),
        E("eg_thoth_saurid", "eg_philemon", "expansion", "Coptic-Arabic Khitat: Saurid -> Hujib -> Priest Philemon"),
        E("eg_philemon", "bib_noah", "syncretic", "Coptic-Arabic lore: Egyptian priest Philemon sails on Noah's Ark"),
        E("bib_enoch", "eg_thoth_saurid", "syncretic", "Pseudo-Eupolemus, Hermetic & Coptic-Arabic lore equate Enoch (Idris) with Thoth / King Saurid"),
        E("eg_ennead", "bib_noah", "syncretic", "Syncretic comparison: Osiris sealed in Nile chest/ark <-> Noah"),
    ]

    # 2. Coptic-Arabic Post-Flood Egypt (Baysar -> Misrayim -> Qift/Ashmun/Atrib/Sa) & Book of Jasher Pharaohs!
    nodes += [
        N("eg_baysar_misr", "Baysar → Misrayim (Misr) → Qift (Copts), Ashmun, Atrib & Sa", "levant_egypt", 6, "Post-Flood Coptic-Arabic Chronicle",
          "Coptic-Arabic Eponymous Founders of Egypt", ["al-Maqrizi Khitat", "Ibn Abd al-Hakam", "Akhbar al-Zaman"],
          "Medieval Coptic-Arabic histories trace post-Flood Egypt from Ham -> Baysar -> Misrayim (Mizraim), whose 4 sons Qift (eponym of the Copts/Qift!), Ashmun (Hermopolis), Atrib (Athribis), and Sa (Sais) divide Egypt!",
          ["Misr", "Qift (Copts)"], major=True),
        N("eg_jas_rikayon", "Rikayon (First 'Pharaoh' in Book of Jasher) → Melol → Adikam", "levant_egypt", 10, "Book of Jasher Ch. 14, 66, 77-81",
          "Extra-Biblical Pharaohs of Abraham, Joseph & Moses", ["Book of Jasher 14, 66-68, 77-81"],
          "Book of Jasher 14 recounts Rikayon rising to power in Shinar/Egypt and receiving the title 'Pharaoh', followed in later generations by King Melol (Pharaoh at Moses's birth, father of Princess Bithiah) and short-statured King Adikam (Pharaoh of the Exodus!).",
          ["Rikayon (Jasher 14)", "Melol (Jasher 66)", "Adikam (Jasher 77)"]),
        N("le_sanchuniathon", "Protogonos → Misor & Sydyk → Taaut (Thoth) & Chna (Canaan)", "levant_egypt", 6, "Phoenician-Canaanite Lore",
          "Phoenician Genealogy Bridging Egypt & Levant", ["Philo of Byblos / Sanchuniathon (via Eusebius Praep. Ev. I.10)"],
          "Explicitly names Misor (direct cognate of Biblical Mizraim!) as brother of Sydyk (cf. Melchizedek) and father of Taaut (Egyptian Thoth), alongside Chna (Canaan).",
          ["Misor = Mizraim", "Taaut = Thoth", "Chna = Canaan"], major=True),
    ]
    edges += [
        E("bib_mizraim", "eg_baysar_misr", "cognate", "Biblical Mizraim = Coptic-Arabic Misrayim/Misr"),
        E("eg_philemon", "eg_baysar_misr", "expansion", "Philemon guides Misrayim back to settle post-Flood Egypt (Khitat)"),
        E("bib_mizraim", "eg_jas_rikayon", "expansion", "Book of Jasher 14: Rikayon establishes the royal title Pharaoh in Egypt"),
        E("bib_mizraim", "le_sanchuniathon", "cognate", "Biblical Mizraim = Phoenician Misor"),
        E("bib_canaan", "le_sanchuniathon", "cognate", "Biblical Canaan = Phoenician Chna"),
        E("le_sanchuniathon", "eg_thoth_saurid", "cognate", "Phoenician Taaut = Egyptian Thoth"),
    ]

    # 3. Early Dynastic & Old Kingdom Pharaohs (Dynasties 1-6 — Pyramid Builders!)
    nodes += [
        N("eg_menes", "Narmer / Menes (Unifier of Upper & Lower Egypt)", "levant_egypt", 6, "Dynasty 1 (c. 3100 BCE)",
          "First Historical Pharaoh of Unified Egypt", ["Narmer Palette", "Abydos King List", "Turin King List", "Manetho"],
          "Unified Upper and Lower Egypt and founded Memphis (city of Ptah); historical anchor for the land of Mizraim.",
          ["Narmer", "Menes", "Scorpion II precursor"], major=True),
        N("eg_hor_aha", "Hor-Aha → Djer → Djet & Queen Merneith", "levant_egypt", 6, "Dynasty 1 (c. 3050-2970 BCE)",
          "Early First Dynasty Royal Line", ["Abydos King List", "Palermo Stone"],
          "Hor-Aha (son of Narmer) -> Djer -> Djet + Regent Queen Merneith (first known female ruler/regent in Egyptian history!)."),
        N("eg_den_qaa", "Den → Anedjib → Semerkhet → Qa'a (Late Dynasty 1)", "levant_egypt", 6, "Dynasty 1 (c. 2970-2890 BCE)",
          "First Pharaoh Wearing Double Crown (Den)", ["Palermo Stone", "Abydos King List"],
          "Den (son of Djet & Merneith) first wore the Double Crown of Egypt; followed by Anedjib, Semerkhet, and Qa'a."),
        N("eg_dyn2_khasekhemwy", "Hotepsekhemwy → Peribsen → Khasekhemwy & Nimaathap", "levant_egypt", 7, "Dynasty 2 (c. 2890-2686 BCE)",
          "Reconciler of Horus & Set / Parents of Djoser", ["Palermo Stone", "Abydos Inscriptions"],
          "Khasekhemwy reunited Egypt under both Horus and Set symbols; with Queen Nimaathap he founded the line leading to 3rd Dynasty pyramid builders!"),
        N("eg_djoser", "Djoser (Netjerikhet) — Builder of Step Pyramid", "levant_egypt", 7, "Dynasty 3 (c. 2670 BCE)",
          "Founder of Old Kingdom Pyramid Age", ["Saqqara Step Pyramid", "Famine Stela", "Turin King List"],
          "Commissioned the world's first monumental stone pyramid at Saqqara through his vizier Imhotep.", major=True),
        N("eg_imhotep", "Imhotep (Vizier of Djoser / 7-Year Famine Stela)", "levant_egypt", 7, "Dynasty 3 / Ptolemaic Famine Stela",
          "Architect, Physician, Priest of On & Famine Vizier", ["Famine Stela (Sehel Island)", "Manetho"],
          "High Priest of Heliopolis (On) and vizier of Djoser. The Sehel Island Famine Stela credits Imhotep with ending a 7-year Nile famine — famously compared to Joseph (Zaphenath-Paneah), who wed the daughter of the Priest of On!",
          ["Compared to Joseph (Zaphenath-Paneah)"], major=True),
        N("eg_sneferu", "Huni → Sneferu & Queen Hetepheres I", "levant_egypt", 8, "Dynasty 4 (c. 2613-2589 BCE)",
          "Builder of Bent & Red Pyramids / Father of Khufu", ["Palermo Stone", "Dahshur Pyramids"],
          "Sneferu built three giant pyramids (Meidum, Bent, Red) and with Hetepheres I fathered Khufu.", major=True),
        N("eg_khufu", "Khufu (Cheops) — Great Pyramid of Giza", "levant_egypt", 8, "Dynasty 4 (c. 2589-2566 BCE)",
          "Builder of the Great Pyramid", ["Giza Plateau", "Diary of Merer", "Herodotus II"],
          "Son of Sneferu & Hetepheres I; commissioned the Great Pyramid of Giza (attributed in Coptic-Arabic folklore to antediluvian King Saurid/Enoch!). Father of Djedefre and Khafre.",
          ["Cheops"], major=True),
        N("eg_khafre_menkaure", "Djedefre, Khafre (Sphinx) → Menkaure → Shepseskaf", "levant_egypt", 8, "Dynasty 4 (c. 2566-2503 BCE)",
          "Giza Pyramid Builders", ["Giza Plateau", "Turin King List"],
          "Sons of Khufu (Djedefre & Khafre, builder of 2nd Giza Pyramid & Great Sphinx) -> Menkaure (3rd Giza Pyramid) -> Shepseskaf."),
        N("eg_dyn5_6", "Userkaf → Unas (Pyramid Texts) → Pepi I → Pepi II & Nitocris", "levant_egypt", 9, "Dynasties 5-6 (c. 2494-2181 BCE)",
          "Solar Kings & Old Kingdom Pyramid Texts", ["Pyramid Texts of Unas", "Turin King List", "Manetho"],
          "Unas inscribed the world's oldest surviving religious corpus (Pyramid Texts); Pepi II reigned ~94 years before the Old Kingdom collapsed."),
    ]
    edges += [
        E("eg_horus", "eg_menes", "expansion", "Turin King List: Horus -> Shemsu-Hor -> Narmer/Menes"),
        E("bib_mizraim", "eg_menes", "cognate", "Biblical Mizraim = Egypt (land unified by Narmer/Menes)"),
        E("eg_menes", "eg_hor_aha", "direct", "Son Hor-Aha -> Djer -> Djet & Merneith"),
        E("eg_hor_aha", "eg_den_qaa", "direct", "Djet + Merneith -> Den -> Anedjib -> Semerkhet -> Qa'a"),
        E("eg_den_qaa", "eg_dyn2_khasekhemwy", "expansion", "Dynasty 1 -> Dynasty 2 (Hotepsekhemwy -> Khasekhemwy)"),
        E("eg_dyn2_khasekhemwy", "eg_djoser", "direct", "Khasekhemwy + Nimaathap -> Djoser (Dynasty 3)"),
        E("eg_djoser", "eg_imhotep", "expansion", "Vizier & Priest of On under Djoser (Step Pyramid & Famine Stela)"),
        E("eg_djoser", "eg_sneferu", "expansion", "Sekhemkhet -> Huni -> Sneferu (Dynasty 4)"),
        E("eg_sneferu", "eg_khufu", "direct", "Sneferu + Hetepheres I -> Khufu"),
        E("eg_khufu", "eg_khafre_menkaure", "direct", "Sons Djedefre & Khafre -> Menkaure -> Shepseskaf"),
        E("eg_khafre_menkaure", "eg_dyn5_6", "expansion", "Dynasty 4 -> Dynasties 5-6 (Userkaf -> Unas -> Pepi II)"),
        E("tri_joseph", "eg_imhotep", "parallel", "7-year famine vizier linked to On/Heliopolis (Famine Stela <-> Gen 41)"),
        E("eg_thoth_saurid", "eg_khufu", "syncretic", "Coptic-Arabic lore attributes Giza Pyramids to Saurid/Enoch before the Flood"),
    ]

    # 4. Middle Kingdom & Hyksos (Dynasties 11-17 — Patriarchal & Joseph Horizon!)
    nodes += [
        N("eg_mentuhotep2", "Mentuhotep II → Amenemhat I → Senusret I", "levant_egypt", 10, "Dynasties 11-12 (c. 2055-1926 BCE)",
          "Middle Kingdom Reunifiers (Abraham Horizon)", ["Deir el-Bahari", "Story of Sinuhe", "Beni Hasan Tomb"],
          "Mentuhotep II reunites Egypt; Amenemhat I & Senusret I inaugurate the Middle Kingdom (the Beni Hasan tomb depicts Semitic Aamu caravans entering Egypt in this exact era, paralleling Abraham & Jacob!).", major=True),
        N("eg_senusret3_amenemhat3", "Senusret II → Senusret III → Amenemhat III → Sobekneferu", "levant_egypt", 11, "Late Dynasty 12 (c. 1897-1802 BCE)",
          "Peak of Middle Kingdom & Faiyum Canal", ["Lahun Papyri", "Turin King List"],
          "Senusret III expands into Nubia (Kush); Amenemhat III builds the Faiyum irrigation system (later called Bahr Yussef, 'Canal of Joseph' in Egyptian tradition!); Sobekneferu is the first verified female Pharaoh."),
        N("eg_hyksos", "Salitis → Khyan → Apepi (15th Dynasty Hyksos)", "levant_egypt", 12, "Second Intermediate Period (c. 1650-1550 BCE)",
          "West-Semitic Rulers of Avaris in the Nile Delta", ["Manetho (via Josephus Against Apion)", "Turin King List"],
          "Canaanite/West-Semitic kings ruling Lower Egypt from Avaris (Goshen/Delta!). Both Manetho and Josephus linked the Hyksos era to the arrival/expulsion of the Israelites under Joseph and Moses.",
          ["Heqau-Khasut ('Rulers of Foreign Lands')", "Apophis"], major=True),
        N("eg_seqenenre", "Seqenenre Tao (+ Ahhotep I) → Kamose", "levant_egypt", 13, "Dynasty 17 (c. 1560-1550 BCE)",
          "Theban Liberators vs. Hyksos", ["Carnarvon Tablet", "Royal Mummies"],
          "Theban royal family who fought to expel the Hyksos from Avaris; parents of Ahmose I (founder of the New Kingdom)."),
    ]
    edges += [
        E("eg_dyn5_6", "eg_mentuhotep2", "expansion", "First Intermediate Period -> Middle Kingdom reunified by Mentuhotep II"),
        E("eg_mentuhotep2", "eg_senusret3_amenemhat3", "direct", "Senusret I -> Amenemhat II -> Senusret II -> Senusret III -> Amenemhat III -> Sobekneferu"),
        E("eg_senusret3_amenemhat3", "eg_hyksos", "expansion", "Weakening of 13th Dynasty leads to Hyksos rule in the Delta"),
        E("eg_hyksos", "eg_seqenenre", "expansion", "Theban 17th Dynasty challenges Hyksos king Apepi"),
        E("tri_joseph", "eg_hyksos", "parallel", "Josephus & historians link Semitic vizier Joseph/Goshen to 12th/Hyksos Delta horizon"),
        E("bib_abraham", "eg_mentuhotep2", "parallel", "Middle Kingdom Beni Hasan Aamu caravans parallel Abraham's sojourn in Egypt (Gen 12)"),
    ]

    # 5. New Kingdom (18th, 19th, 20th Dynasties — Hatshepsut, Akhenaten, Tutankhamun, Ramesses II, Merneptah!)
    nodes += [
        N("eg_ahmose1", "Ahmose I (+ Ahmose-Nefertari) → Amenhotep I", "levant_egypt", 13, "Dynasty 18 (c. 1550-1504 BCE)",
          "Founder of the New Kingdom (Expeller of Hyksos)", ["Tempest Stele", "Tomb of Ahmose son of Ibana"],
          "Son of Seqenenre Tao & Ahhotep I; expels the Hyksos from Avaris and conquers Sharuhen in Canaan.", major=True),
        N("eg_thutmose1", "Thutmose I → Thutmose II & Queen Hatshepsut", "levant_egypt", 14, "Dynasty 18 (c. 1504-1458 BCE)",
          "Empire Builder & Great Female Pharaoh", ["Deir el-Bahari Temple", "Punt Expedition Reliefs"],
          "Thutmose I campaigns to the Euphrates and Kush; daughter Hatshepsut rules as Pharaoh and dispatches the famed expedition to the Land of Punt (East Africa/Horn of Africa) — sometimes compared in early-Exodus chronology to Pharaoh's daughter who raised Moses!",
          ["Hatshepsut (Maatkare)"], major=True),
        N("eg_thutmose3", "Thutmose III → Amenhotep II → Thutmose IV", "levant_egypt", 14, "Dynasty 18 (c. 1479-1391 BCE)",
          "Peak of Egyptian Empire in Canaan & Nubia", ["Annals of Thutmose III (Karnak)", "Dream Stele"],
          "Thutmose III wins the Battle of Megiddo in Canaan and extends Egyptian rule from the Euphrates to the 4th Cataract of Nubia."),
        N("eg_amenhotep3", "Amenhotep III & Queen Tiye", "levant_egypt", 14, "Dynasty 18 (c. 1391-1353 BCE)",
          "Golden Age Pharaoh & Powerful Royal Matriarch", ["Amarna Letters", "Colossi of Memnon"],
          "Corresponded with Babylon, Assyria, Mitanni, and Canaanite vassals (Amarna Letters mentioning 'Habiru'!). With Queen Tiye fathered Akhenaten."),
        N("eg_akhenaten", "Akhenaten (Amenhotep IV) & Nefertiti", "levant_egypt", 15, "Amarna Period (c. 1353-1336 BCE)",
          "Pharaoh of Aten Solar Monotheism", ["Great Hymn to the Aten", "Amarna Letters"],
          "Son of Amenhotep III & Tiye; established solar monotheism at Akhetaten (Amarna). Frequently linked in comparative history (e.g., Psalm 104 <-> Great Hymn to Aten; Manetho's Osarseph memory) to the Mosaic era!",
          ["Amenhotep IV", "Great Hymn to Aten <-> Psalm 104"], major=True),
        N("eg_tutankhamun", "Tutankhamun (+ Ankhesenamun) → Ay → Horemheb", "levant_egypt", 15, "Late Dynasty 18 (c. 1332-1292 BCE)",
          "Boy Pharaoh Who Restored Amun", ["Tomb KV62", "Restoration Stele"],
          "Son of Akhenaten; marries half-sister Ankhesenamun (who famously wrote to Hittite King Suppiluliuma I asking for a Hittite prince to marry — bridging Egypt and Heth/Hittites!).", major=True),
        N("eg_ramesses2", "Ramesses I → Seti I → Ramesses II the Great (+ Nefertari)", "levant_egypt", 15, "Dynasty 19 (c. 1292-1213 BCE)",
          "Builder of Pi-Ramesses & Battle of Kadesh", ["Pi-Ramesses", "Treaty of Kadesh", "Exodus 1:11"],
          "Built the Delta capital Pi-Ramesses (named 'Raamses' in Exodus 1:11!) and signed history's oldest surviving peace treaty with the Hittites (Hattusili III). Most widely cited Pharaoh of the late-date Exodus!",
          ["Ozymandias", "Pi-Ramesses (Exod 1:11)"], major=True),
        N("eg_merneptah", "Merneptah (Israel Stele, c. 1208 BCE)", "levant_egypt", 16, "Dynasty 19 (c. 1213-1203 BCE)",
          "13th Son of Ramesses II / Earliest Inscription of Israel", ["Merneptah Stele (Cairo CG 34025)"],
          "Son of Ramesses II; his 1208 BCE Victory Stele contains the earliest extra-biblical mention of 'Israel' as a people in Canaan!",
          ["Israel Stele (1208 BCE)"], major=True),
        N("eg_ramesses3", "Ramesses III (Defender Against Sea Peoples / Peleset)", "levant_egypt", 16, "Dynasty 20 (c. 1186-1155 BCE)",
          "Victor Over the Sea Peoples (Philistines)", ["Medinet Habu Inscriptions", "Papyrus Harris I"],
          "Repelled the Sea Peoples invasion including the Peleset (Philistines — Caphtorim/Casluhim of Gen 10:14!), who subsequently settled coastal Canaan!"),
        N("eg_shoshenq1", "Shoshenq I (Biblical Shishak, 22nd Libyan Dynasty)", "levant_egypt", 16, "Dynasty 22 (c. 943-922 BCE)",
          "Meshwesh/Libyan Pharaoh Who Raided Jerusalem", ["Bubastite Portal (Karnak)", "1 Kings 14:25-26"],
          "Founder of the Libyan (Phut/Lehabim) 22nd Dynasty; explicitly named 'Shishak' in 1 Kings 14:25, sheltering Jeroboam and campaigning in Judah and Israel after Solomon's death!",
          ["Shishak (1 Kings 14:25)"], major=True),
        N("eg_ptolemy_cleopatra", "Ptolemy I → Ptolemy II (Manetho & LXX) → Cleopatra VII", "levant_egypt", 17, "Ptolemaic Dynasty (305-30 BCE)",
          "Hellenistic Pharaohs & Translators of the Septuagint", ["Letter of Aristeas", "Manetho Aegyptiaca"],
          "Under Ptolemy II Philadelphus, Jewish scholars translated the Torah into Greek (Septuagint) at Alexandria while Egyptian priest Manetho compiled the 30-dynasty history of Egypt and the Osarseph/Moses account; ends with Cleopatra VII.",
          ["Cleopatra VII", "Manetho & Septuagint Era"]),
        N("eg_osarseph_bithiah", "Osarseph (Manetho) / Musaeus (Artapanus) / Bithiah & Adoniah", "levant_egypt", 15, "Greco-Egyptian Chronicles & Jasher",
          "Egyptian & Cushite Names/Traditions of Moses", ["Manetho (via Josephus Against Apion 1.26)", "Artapanus (via Eusebius)", "Book of Jasher 68, 72-76"],
          "Manetho preserves an Egyptian tradition of a Heliopolitan priest named Osarseph who took the name Moses; Artapanus calls Moses 'Musaeus' (teacher of Orpheus) and Egyptian 'Hermes', leading an expedition into Cush/Ethiopia — echoing Book of Jasher 72-76 where Moses rules Cush with Queen Adoniah!",
          ["Osarseph", "Musaeus", "Queen Adoniah of Cush (Jasher 73)", "Princess Bithiah (Jasher 68)"], major=True),
    ]
    edges += [
        E("eg_seqenenre", "eg_ahmose1", "direct", "Son of Seqenenre Tao & Ahhotep I"),
        E("eg_ahmose1", "eg_thutmose1", "expansion", "Amenhotep I -> Thutmose I (Dynasty 18)"),
        E("eg_thutmose1", "eg_thutmose3", "direct", "Thutmose II -> Thutmose III -> Amenhotep II -> Thutmose IV"),
        E("eg_thutmose3", "eg_amenhotep3", "direct", "Son of Thutmose IV"),
        E("eg_amenhotep3", "eg_akhenaten", "direct", "Amenhotep III + Queen Tiye -> Akhenaten"),
        E("eg_akhenaten", "eg_tutankhamun", "direct", "Son Tutankhamun -> Ay -> Horemheb"),
        E("eg_tutankhamun", "bib_heth", "cognate", "Ankhesenamun wrote to Hittite (Heth) king Suppiluliuma I seeking a royal marriage"),
        E("eg_tutankhamun", "eg_ramesses2", "expansion", "Horemheb -> Ramesses I -> Seti I -> Ramesses II (Dynasty 19)"),
        E("eg_ramesses2", "eg_merneptah", "direct", "13th son of Ramesses II"),
        E("eg_merneptah", "eg_ramesses3", "expansion", "Dynasty 19 -> Dynasty 20 (Setnakhte -> Ramesses III)"),
        E("eg_ramesses3", "eg_shoshenq1", "expansion", "Dynasty 20-21 -> 22nd Libyan Dynasty (Shoshenq I)"),
        E("eg_shoshenq1", "eg_ptolemy_cleopatra", "expansion", "Late Period -> Ptolemaic Dynasty -> Cleopatra VII"),
        E("eg_merneptah", "bib_jacob", "cognate", "Merneptah Stele (c. 1208 BCE): earliest extra-biblical inscription naming Israel!"),
        E("eg_ramesses2", "bib_moses", "parallel", "Pi-Ramesses ('Raamses', Exod 1:11) — classic historical horizon for the Exodus"),
        E("eg_akhenaten", "eg_osarseph_bithiah", "parallel", "Comparative historians link Manetho's Osarseph memory to Amarna/Akhenaten monotheism"),
        E("eg_ramesses3", "bib_casluhim", "cognate", "Medinet Habu Peleset (Sea Peoples) = Biblical Philistines (Gen 10:14)!"),
        E("eg_shoshenq1", "jud_solomon", "cognate", "1 Kings 14:25: Shoshenq I = Biblical Shishak who raided Jerusalem after Solomon"),
        E("eg_shoshenq1", "bib_lehabim", "cognate", "22nd Dynasty founded by Libyan (Lehabim/Meshwesh) chieftains"),
        E("bib_moses", "eg_osarseph_bithiah", "syncretic", "Manetho's Osarseph, Artapanus's Musaeus & Jasher's King of Cush"),
        E("eg_jas_rikayon", "eg_osarseph_bithiah", "expansion", "Jasher 68: Pharaoh Melol's daughter Bithiah rescues and raises Moses"),
    ]

    return {"module": "04_egypt_levant", "title": "Exhaustive Ancient Egyptian Dynasties (Ennead, Old/Middle/New Kingdoms, Hyksos, Amarna, Ramesses, Coptic-Arabic & Jasher Chronicles)", "nodes": nodes, "edges": edges}


def build_module_08_african_ethiopian():
    nodes, edges = [], []

    # 1. Kingdom of Kush / Nubia — 25th Dynasty ("Black Pharaohs") & Meroe (Bridging Biblical Cush, Tirhakah, Candace!)
    nodes += [
        N("af_alara", "Alara of Kush (Founder of Napatan Dynasty)", "african", 14, "Kingdom of Kush (c. 795-760 BCE)",
          "Progenitor of the 25th Kushite Dynasty", ["Kawa Inscriptions", "Napatan Royal Stelae"],
          "Unified Upper Nubia around Napata (Jebel Barkal); revered by all later Kushite pharaohs as their founding ancestor.", major=True),
        N("af_kashta", "Kashta & Queen Pebatjma", "african", 15, "c. 760-747 BCE",
          "Brother of Alara / First Kushite King in Upper Egypt", ["Elephantine Stele"],
          "Extended Kushite rule into Upper Egypt and installed his daughter Amenirdis I as God's Wife of Amun at Thebes; father of Piye and Shabaka."),
        N("af_piye", "Piye (Piankhi) & Shabaka (25th Dynasty Pharaohs)", "african", 15, "Dynasty 25 (c. 747-706 BCE)",
          "Kushite Conquerors & Restorers of Unified Egypt", ["Victory Stele of Piye (Jebel Barkal)", "Shabaka Stone"],
          "Piye conquered all of Egypt from Nubia to the Delta; his brother Shabaka preserved the ancient Memphite Theology of Ptah on the Shabaka Stone!",
          ["Piankhi", "Shabaka"], major=True),
        N("af_taharqa", "Shebitku & Taharqa (Biblical Tirhakah, King of Cush!)", "african", 16, "Dynasty 25 (c. 706-664 BCE)",
          "Greatest 25th Dynasty Pharaoh — Named in 2 Kings 19:9", ["2 Kings 19:9", "Isaiah 37:9", "Kawa Stelae"],
          "Son of Piye; explicitly named in the Bible as 'Tirhakah, King of Cush' who marched to relieve King Hezekiah's Jerusalem from Assyrian Emperor Sennacherib (701 BCE)!",
          ["Tirhakah (2 Kings 19:9 / Isa 37:9)"], major=True),
        N("af_tantamani", "Tantamani → Aspelta → Ergamenes (Meroe)", "african", 16, "Late Napata → Meroe (c. 664-270 BCE)",
          "Last Kushite Pharaoh of Egypt → Founders of Meroe", ["Dream Stele", "Diodorus Siculus"],
          "Tantamani (son of Shabaka) was the last 25th Dynasty king in Egypt; Aspelta shifted the royal capital south to Meroe (creating the Meroitic script and pyramid fields!)."),
        N("af_kandakes", "Queen Shanakdakhete → Amanirenas → Amanitore (Kandakes)", "african", 17, "Meroitic Kingdom (c. 170 BCE - 50 CE)",
          "Warrior Queens of Kush (Biblical 'Candace'!)", ["Acts 8:27", "Strabo Geography", "Meroe Reliefs"],
          "Meroe was ruled by powerful Candaces (Kandakes): Amanirenas battled Roman Augustus's legions (capturing his bronze head at Meroe!), and Queen Amanitore corresponds to 'Candace, Queen of the Ethiopians' in Acts 8:27!",
          ["Candace (Acts 8:27)", "Amanirenas", "Amanitore"], major=True),
        N("af_jas_kikanos", "King Kikanos of Cush (+ Queen Adoniah) → Menakrus", "african", 15, "Book of Jasher Ch. 72-76",
          "Cushite Royal House in Moses's 40-Year Reign", ["Book of Jasher 72-76", "Josephus Ant. 2.10"],
          "Book of Jasher 72-76 recounts Moses aiding King Kikanos against the rebel Balaam, marrying Queen Adoniah, and ruling Cush for 40 years before turning the kingdom over to Kikanos's son Menakrus!"),
    ]
    edges += [
        E("bib_cush", "af_alara", "cognate", "Biblical Cush = Historical Kingdom of Kush (Nubia/Sudan)"),
        E("bib_cush", "af_jas_kikanos", "expansion", "Book of Jasher 72: Kikanos King of Cush"),
        E("af_jas_kikanos", "eg_osarseph_bithiah", "expansion", "Jasher 73: Moses marries Queen Adoniah and rules Cush 40 years"),
        E("af_alara", "af_kashta", "direct", "Brother/Successor (Napatan Royal Line)"),
        E("af_kashta", "af_piye", "direct", "Kashta + Pebatjma -> Piye & Shabaka"),
        E("af_piye", "eg_shoshenq1", "cognate", "Piye defeats 22nd/24th Dynasty Delta kings to found Egypt's 25th Dynasty"),
        E("af_piye", "eg_ptah", "cognate", "Shabaka preserves the ancient Memphite Theology of Ptah (Shabaka Stone)"),
        E("af_piye", "af_taharqa", "direct", "Son of Piye (Kawa Inscriptions)"),
        E("af_taharqa", "mes_assyria_kings", "cognate", "2 Kings 19:9: Taharqa (Tirhakah) marches against Assyrian king Sennacherib to aid Jerusalem!"),
        E("af_taharqa", "af_tantamani", "direct", "Nephew/Cousin Tantamani -> Aspelta -> Meroe"),
        E("af_tantamani", "af_kandakes", "expansion", "Meroitic succession to warrior Kandakes (Amanirenas & Amanitore)"),
    ]

    # 2. Ethiopian Royal Chronicles (Tarika Nagast + Kebra Nagast Solomonic & Zagwe Dynasties!)
    nodes += [
        N("eth_ityopis", "Ityopis (Ethiopic, son of Cush) → Aksumawi", "african", 7, "Ethiopian Chronicle (Tarika Nagast)",
          "Traditional Eponym of Ethiopia & Founder of Aksum", ["Tarika Nagast (Ethiopian Royal List)", "Book of Aksum"],
          "Traditional Ethiopian royal chronicles trace Ethiopia directly from Ham -> Cush -> Ityopis (eponym of Ethiopia) -> Aksumawi (founder of Aksum) -> Malakya Aksum!",
          ["Ethiopic", "Aksumawi"], major=True),
        N("eth_angabo", "Arwe (Serpent King) → Angabo → Gedur → Tawasya", "african", 14, "Pre-Solomonic Agazian Dynasty",
          "Slayer of Arwe & Ancestors of Queen Makeda", ["Tarika Nagast", "Ethiopian Oral Chronicles"],
          "Angabo slays the tyrant serpent-king Arwe and founds the Agazian dynasty of Aksum leading directly to Queen Makeda!"),
        N("eth_makeda", "Queen Makeda (Queen of Sheba / Saba / Bilqis)", "african", 16, "c. 10th c. BCE trad. (1 Kings 10 / Kebra Nagast)",
          "Sovereign of Aksum & Sheba / Mother of Menelik I", ["1 Kings 10:1-13", "Kebra Nagast", "Qur'an 27 (Bilqis)"],
          "Journeys from Aksum/Sheba to Jerusalem to test King Solomon's wisdom; bears Menelik I, uniting the lineages of Judah/Israel, Saba/Arabia, and Cush/Ethiopia!",
          ["Queen of Sheba", "Bilqis (Arabic)", "Nicaula (Josephus)"], major=True),
        N("eth_ezana", "Zagduru → Bazen → Emperor Ezana & King Kaleb of Aksum", "african", 17, "Aksumite Empire (c. 1st-6th c. CE)",
          "First Christian Emperor of Aksum (c. 330 CE)", ["Ezana Stone (Ge'ez/Sabaean/Greek)", "Kebra Nagast"],
          "King Bazen reigned at the turn of the 1st century CE; Emperor Ezana converted Aksum to Christianity (c. 330 CE) and conquered Meroe; King Kaleb (Ella Atsbeha) campaigned in Himyar/Yemen!",
          ["Ezana of Aksum", "Kaleb"], major=True),
        N("eth_lalibela", "Mara Takla Haymanot → Emperor Gebre Mesqel Lalibela (Zagwe)", "african", 17, "Zagwe Dynasty (c. 1137-1270 CE)",
          "Carver of Rock-Hewn Churches (Trad. Line of Moses & Zipporah)", ["Gadla Lalibela", "Ethiopian Chronicles"],
          "Ethiopian Zagwe chronicles trace the Zagwe kings to a daughter of the Aksumite line AND traditionally claim descent from Moses & Zipporah! Lalibela carved the 11 monolithic churches of 'New Jerusalem'.",
          ["Zagwe Dynasty", "Moses/Zipporah tradition"]),
        N("eth_haile_selassie", "Yekuno Amlak → Zara Yaqob → Menelik II → Haile Selassie I", "african", 17, "Solomonic Restoration (1270-1974 CE)",
          "Continuous Solomonic Emperors of Ethiopia", ["Kebra Nagast", "Ethiopian Imperial Chronicles"],
          "Yekuno Amlak restored the Solomonic Dynasty in 1270 CE; continued through Zara Yaqob, Menelik II (victor at Adwa), down to Haile Selassie I (225th ruler from Menelik I!).",
          ["Solomonic Restoration", "Lion of Judah"], major=True),
    ]
    edges += [
        E("bib_cush", "eth_ityopis", "expansion", "Tarika Nagast: Cush -> Ityopis (eponym of Ethiopia) -> Aksumawi"),
        E("eth_ityopis", "eth_angabo", "expansion", "Pre-Solomonic Aksumite/Agazian royal succession"),
        E("eth_angabo", "eth_makeda", "direct", "Agazian royal descent to Queen Makeda (Tarika Nagast)"),
        E("bib_sheba_joktan", "eth_makeda", "cognate", "Sabaean / Sheba royal bridge across the Red Sea (Yemen <-> Aksum)"),
        E("eth_makeda", "eth_menelik", "direct", "Mother of Menelik I (Kebra Nagast)"),
        E("eth_menelik", "eth_ezana", "expansion", "Aksumite Solomonic succession: Menelik I -> Zagduru -> Bazen -> Ezana -> Kaleb"),
        E("eth_ezana", "af_kandakes", "cognate", "Ezana Stone (c. 350 CE) records Aksum's conquest of Meroe/Kush"),
        E("eth_ezana", "eth_lalibela", "expansion", "Aksum -> Zagwe Dynasty (via Aksumite princess Masoba Warq)"),
        E("bib_moses", "eth_lalibela", "syncretic", "Ethiopian Zagwe royal tradition claims descent from Moses & Zipporah"),
        E("eth_ezana", "eth_haile_selassie", "expansion", "Solomonic line restored by Yekuno Amlak (1270) -> Menelik II -> Haile Selassie I"),
    ]

    # 3. West, North & East African Ancestral Traditions (Yoruba Oduduwa, Hausa Bayajidda, Mali, Amazigh, Buganda, Kikuyu)
    nodes += [
        N("af_oduduwa", "Olodumare → Obatala & Oduduwa (Progenitor of the Yoruba)", "african", 5, "Ile-Ife Primordial Tradition (West Africa)",
          "Founding Ancestor of Yoruba & Benin Kingdoms", ["Yoruba Oral Tradition (Ifa Corpus)", "Samuel Johnson History of the Yorubas"],
          "In indigenous Ifa cosmology, Olodumare sends Obatala and Oduduwa to establish Ile-Ife (cradle of humanity). A later 19th-c. syncretic oral chronicle (Samuel Johnson) compares Oduduwa's eastern migration to 'Lamurudu' (Nimrod) from the East!",
          ["Odua", "Ile-Ife Cradle", "Syncretic Lamurudu/Nimrod lore"], major=True),
        N("af_okanbi", "Okanbi (Son of Oduduwa)", "african", 6, "Ile-Ife Gen 2", "Father of the 7 Crowned Yoruba Monarchs", ["Yoruba Royal Chronicles"],
          "Only son of Oduduwa in core Ife genealogy; father of 7 royal children who founded the major Yoruba kingdoms and the Benin dynasty."),
        N("af_bayajidda", "Bayajidda (Abuyazidu of Baghdad) + Queen Daurama → Bawo", "african", 14, "Hausa Chronicle (c. 10th c. CE trad.)",
          "Progenitor of the 7 Hausa Bakwai Kingdoms", ["Kano Chronicle", "Daura Oral Tradition"],
          "Prince Bayajidda journeys from Baghdad across Bornu to Daura (Nigeria), slays the well-serpent Sarki, weds Queen Magajiya Daurama, and sires Bawo — father of the 7 Hausa Bakwai states (Daura, Kano, Katsina, Zaria, Gobir, Rano, Biram)!",
          ["Abuyazidu", "Hausa Bakwai"], major=True),
        N("af_sundiata", "Bilali Bounama → Naré Maghann → Sundiata Keita → Mansa Musa", "african", 16, "Mali Empire (13th-14th c. CE)",
          "Founder of the Mali Empire (Lion King of Manden)", ["Epic of Sundiata (Griot Tradition)", "Ibn Battuta"],
          "Mande royal griots trace the Keita dynasty from Bilali Bounama (traditionally linked to Bilal ibn Rabah, Ethiopian companion of Muhammad!) to Sundiata Keita (founder of Mali, 1235 CE) and Mansa Musa!",
          ["Keita Dynasty", "Mansa Musa"], major=True),
        N("af_mazigh", "Mazigh → Baranis & Botr → Queen Dihya (Imazighen / Berbers)", "african", 7, "North African Amazigh Tradition",
          "Eponymous Ancestor of the Amazigh (Berber) Peoples", ["Ibn Khaldun Kitab al-Ibar", "Herodotus IV (Maxyes)"],
          "Imazighen ('Free People', attested in Herodotus as Maxyes and Egyptian inscriptions as Meshwesh!). Medieval North African genealogists (Ibn Khaldun) linked Mazigh to Ham's sons Phut/Canaan, branching into the Baranis & Botr confederations and heroic Queen Dihya (al-Kahina).",
          ["Imazighen", "Meshwesh", "Queen Kahina"], major=True),
        N("af_kintu_gikuyu", "Kintu & Nambi (Buganda) / Gikuyu & Mumbi (Kikuyu)", "african", 1, "East African Primordial Ancestors",
          "First Human Couples of Great Lakes & East Africa", ["Baganda Royal Oral Tradition", "Kikuyu Oral Tradition (Nine Clans)"],
          "Kintu & Nambi (daughter of sky-king Ggulu) are the primeval progenitors of Buganda's Kabaka kings; Gikuyu & Mumbi (created near Mt. Kenya by Ngai) are the progenitors of the nine Kikuyu clans (Nyumba ya Mumbi)."),
    ]
    add_children(nodes, edges, "af_okanbi", "african", 7, "7 Crowned Descendants of Oduduwa (Yoruba & Benin)", [
        ("af_oranmiyan", "Oranmiyan (Oranyan — Founder of Oyo & Benin Dynasty)", {"major": True, "sources": ["Yoruba & Benin Oral Chronicles"], "notes": "Youngest and mightiest grandson of Oduduwa; founded the Oyo Empire (father of Ajaka & Shango!) and fathered Eweka I, founder of the Oba Dynasty of Benin!"}),
        ("af_eweka1", "Eweka I (First Oba of Benin, son of Oranmiyan)", {"tier": 8, "edge_type": "expansion", "sources": ["Benin Royal Chronicle"], "notes": "Son of Oranmiyan & Princess Erinmwinde of Benin; founder of the historic Oba Dynasty of the Kingdom of Benin."}),
        ("af_olowu", "Olowu of Owu", {"sources": ["Yoruba Royal Chronicles"], "notes": "1st crowned grandchild of Oduduwa (son of Okanbi's eldest daughter)."}),
        ("af_alaketu", "Alaketu of Ketu", {"sources": ["Yoruba Royal Chronicles"], "notes": "Founder of the Yoruba kingdom of Ketu (Benin Republic/Nigeria)."}),
        ("af_onisabe", "Onisabe of Sabe", {"sources": ["Yoruba Royal Chronicles"], "notes": "Founder of the kingdom of Sabe."}),
        ("af_olupopo", "Olupopo of Popo", {"sources": ["Yoruba Royal Chronicles"], "notes": "Founder of the Popo kingdom."}),
        ("af_orangun", "Orangun of Ila", {"sources": ["Yoruba Royal Chronicles"], "notes": "Founder of the kingdom of Ila-Orangun."}),
    ], default_sources=["Yoruba Oral Chronicles"])

    add_children(nodes, edges, "af_bayajidda", "african", 15, "7 Hausa Bakwai Kingdoms (Bawo's Sons)", [
        ("af_hausa_kano", "Bagauda (Kano) & Daura", {"notes": "Founding Hausa Bakwai kingdoms descended from Bawo."}),
        ("af_hausa_katsina", "Kumayau (Katsina) & Gunguma (Zaria/Zazzau)", {"notes": "Founding Hausa Bakwai kingdoms (Zaria later famed for Warrior Queen Amina!)."}),
        ("af_hausa_gobir", "Duma (Gobir), Zamna Kogi (Rano) & Biram", {"notes": "Founding Hausa Bakwai kingdoms."}),
    ], default_sources=["Kano Chronicle", "Daura Tradition"])

    edges += [
        E("hub_primordial", "af_oduduwa", "parallel", "Ile-Ife primordial creation & founding of humanity"),
        E("hub_primordial", "af_kintu_gikuyu", "parallel", "East African primeval couples (Kintu & Nambi; Gikuyu & Mumbi)"),
        E("af_oduduwa", "af_okanbi", "direct", "Son of Oduduwa (Ile-Ife Chronicle)"),
        E("af_oranmiyan", "af_eweka1", "direct", "Son of Oranmiyan (Benin Royal Chronicle)"),
        E("bib_nimrod", "af_oduduwa", "syncretic", "19th-c. Yoruba oral syncretism (S. Johnson) compares Oduduwa's ancestor 'Lamurudu' to Nimrod"),
        E("mes_hammurabi", "af_bayajidda", "syncretic", "Hausa chronicle traces Bayajidda migrating from Baghdad/Mesopotamia to Daura"),
        E("bib_phut", "af_mazigh", "syncretic", "Ibn Khaldun & North African chroniclers link Amazigh/Mazigh to Phut & Canaan"),
        E("eg_shoshenq1", "af_mazigh", "cognate", "Shoshenq I came from the Libyan Meshwesh (= ancestral Amazigh/Imazighen)!"),
        E("ar_adnan_quraysh", "af_sundiata", "syncretic", "Mande griot chronicles link Keita ancestor Bilali Bounama to Ethiopian Bilal (companion of Muhammad)"),
    ]

    return {"module": "08_african_ethiopian", "title": "Exhaustive African, Cushite/Nubian (25th Dynasty & Meroe), Ethiopian (Kebra Nagast / Tarika Nagast) & West/North/East African Genealogies", "nodes": nodes, "edges": edges}


def build_module_09_greek_mediterranean():
    nodes, edges = [], []

    # 1. Primordial Theogony & Titans (Hesiod's Theogony)
    nodes += [
        N("grk_chaos_gaia", "Chaos → Gaia (Earth) & Uranus (Sky)", "greek", 1, "Primordial Cosmogony (Hesiod Theogony)",
          "Primordial Greek Progenitors", ["Hesiod Theogony 116-153"],
          "Out of Chaos emerges Gaia (Earth), who births Uranus (Starry Sky); their union generates the 12 Titans.", major=True),
        N("grk_cronus_rhea", "Cronus (Kronos) & Rhea", "greek", 2, "Titan Generation (Hesiod)",
          "King & Queen of the Titans", ["Hesiod Theogony 453-506"],
          "Youngest Titan who overthrows Uranus; parents of the six elder Olympians (Zeus, Hera, Poseidon, Demeter, Hestia, Hades). In Phoenician Sanchuniathon, El is equated with Kronos!", major=True),
        N("grk_iapetus", "Iapetus (Titan) & Clymene / Asia", "greek", 2, "Titan Generation (Hesiod)",
          "Ancestor of Humanity (Compared to Japheth!)", ["Hesiod Theogony 507-514", "Apollodorus I.2.3"],
          "Titan father of Atlas, Prometheus, Epimetheus, and Menoetius — frequently compared by classical and biblical scholars to Noah's son Japheth (Hebrew Yefet <-> Greek Iapetos)!",
          ["Iapetos <-> Japheth (Yefet)"], major=True),
        N("grk_oceanus_hyperion", "Oceanus & Tethys / Hyperion & Coeus", "greek", 2, "Elder Titans (Hesiod)",
          "River, Sun & Celestial Titans", ["Hesiod Theogony 337-408"],
          "Oceanus & Tethys sire the 3,000 River Gods (including Inachus of Argos and Nile!) and Oceanids; Hyperion sires Helios (Sun) & Selene; Coeus sires Leto (mother of Apollo & Artemis)."),
        N("grk_zeus_olympians", "Zeus, Hera, Poseidon, Demeter, Hestia & Hades", "greek", 3, "Olympian Generation (Hesiod)",
          "Elder Olympian Gods (Zeus = PIE Dyaus Pitr!)", ["Hesiod Theogony", "Homer Iliad"],
          "Zeus (exact Proto-Indo-European linguistic cognate of Vedic Sky-Father Dyaus Pitr & Roman Jupiter!) and Poseidon become the divine progenitors of Greece's heroic royal houses.",
          ["Jupiter", "Cognate: Vedic Dyaus Pitr"], major=True),
        N("grk_atlas", "Atlas (Titan) → Pleiades (Electra & Maia)", "greek", 3, "Titan Gen 2 (Hesiod)",
          "Bearer of the Heavens / Ancestor of Troy & Hermes", ["Hesiod Theogony 509", "Apollodorus III.10"],
          "Son of Iapetus; father of the Seven Pleiades including Electra (mother of Dardanus, founder of Troy!) and Maia (mother of Hermes)."),
        N("grk_prometheus", "Prometheus & Epimetheus (+ Pandora)", "greek", 3, "Titan Gen 2 (Hesiod / Ovid)",
          "Clay-Maker of Humanity & Fire-Bringer", ["Hesiod Works & Days", "Apollodorus I.7.1"],
          "Sons of Iapetus. Prometheus molds mortals from clay and water and brings fire from heaven; Epimetheus weds Pandora (first mortal woman) -> Pyrrha!",
          ["Clay Creator Motif"], major=True),
    ]
    edges += [
        E("hub_primordial", "grk_chaos_gaia", "parallel", "Primordial Earth & Sky creation"),
        E("hub_primordial", "grk_prometheus", "parallel", "Prometheus molds first humans from clay + Pandora (first woman)"),
        E("grk_chaos_gaia", "grk_cronus_rhea", "direct", "Gaia + Uranus -> Cronus & Rhea (Theogony)"),
        E("grk_chaos_gaia", "grk_iapetus", "direct", "Gaia + Uranus -> Iapetus (Theogony)"),
        E("grk_chaos_gaia", "grk_oceanus_hyperion", "direct", "Gaia + Uranus -> Oceanus, Hyperion & Coeus (Theogony)"),
        E("grk_cronus_rhea", "grk_zeus_olympians", "direct", "Cronus + Rhea -> Zeus, Hera, Poseidon, Demeter, Hestia, Hades"),
        E("grk_iapetus", "grk_atlas", "direct", "Son of Iapetus (Theogony 509)"),
        E("grk_iapetus", "grk_prometheus", "direct", "Sons of Iapetus (Theogony 510)"),
        E("bib_japheth", "grk_iapetus", "parallel", "Classical & biblical comparison: Hebrew Yefet (Japheth) <-> Greek Titan Iapetos (ancestor of Deucalion)"),
        E("grk_zeus_olympians", "ved_brahma_manu", "cognate", "Proto-Indo-European Sky-Father cognate: Greek Zeus Pater = Vedic Dyaus Pitr!"),
    ]

    # 2. Greek Great Flood & Table of Nations (Deucalion -> Hellen -> Dorus, Xuthus/Ion, Aeolus!)
    nodes += [
        N("grk_deucalion", "Deucalion & Pyrrha (Greek Great Flood Survivors)", "greek", 4, "Greek Flood Horizon (Apollodorus I.7.2)",
          "Survivors of Zeus's Great Deluge", ["Hesiod Catalogue of Women", "Apollodorus I.7.2", "Ovid Metamorphoses I"],
          "Deucalion (son of Prometheus) and Pyrrha (daughter of Epimetheus & Pandora) survive Zeus's world-destroying Flood in a wooden chest/ark (larnax) landing on Mt. Parnassus!",
          ["Ark on Mt. Parnassus"], major=True),
        N("grk_hellen", "Hellen & Orseis (Eponym of the Greeks / Hellenes)", "greek", 5, "Post-Flood Gen 1 (Catalogue of Women)",
          "Progenitor of the Greek Peoples (3 Sons)", ["Hesiod Catalogue of Women fr. 9", "Apollodorus I.7.3"],
          "Son of Deucalion & Pyrrha; divides the Greek world among his three sons Dorus, Xuthus, and Aeolus — the Greek 'Table of Nations'!", major=True),
        N("grk_dorus", "Dorus (Dorians — Sparta & Peloponnese)", "greek", 6, "Greek Table of Nations", "1st Son of Hellen", ["Hesiod fr. 9", "Apollodorus I.7.3"], "Eponymous ancestor of the Dorians."),
        N("grk_xuthus", "Xuthus & Creusa", "greek", 6, "Greek Table of Nations", "2nd Son of Hellen", ["Hesiod fr. 9", "Apollodorus I.7.3"], "Father of Ion (Ionians) and Achaeus (Achaeans)."),
        N("grk_ion", "Ion (Ionians / Iawones = Biblical Javan!)", "greek", 7, "Greek Table of Nations", "Eponym of the Ionians (Exact Cognate of Javan)", ["Hesiod fr. 9", "Euripides Ion", "Genesis 10:2"],
          "Son of Xuthus (or Apollo) & Creusa; eponym of the Ionians (Archaic Greek Iawones) — EXACT linguistic cognate of Biblical Javan (Yawan, son of Japheth, Gen 10:2)!",
          ["Iawones = Javan (Gen 10:2)"], major=True),
        N("grk_achaeus", "Achaeus (Achaeans)", "greek", 7, "Greek Table of Nations", "Son of Xuthus", ["Hesiod fr. 9", "Apollodorus I.7.3"], "Eponymous ancestor of the Achaeans (Homer's Greeks)."),
        N("grk_aeolus", "Aeolus (Aeolians)", "greek", 6, "Greek Table of Nations", "3rd Son of Hellen (7 Sons & 5 Daughters)", ["Hesiod fr. 10", "Apollodorus I.7.3"], "Eponym of the Aeolians; father of Sisyphus, Cretheus, Athamas, Salmoneus, Deion, Magnes, and Perieres.", major=True),
    ]
    add_children(nodes, edges, "grk_aeolus", "greek", 7, "Sons of Aeolus (Apollodorus I.7.3)", [
        ("grk_sisyphus", "Sisyphus (King of Corinth → Bellerophon)", {"notes": "Son of Aeolus; founder of Corinth, grandfather of Pegasus-rider Bellerophon."}),
        ("grk_cretheus", "Cretheus → Aeson → Jason (Argonauts)", {"major": True, "notes": "Son of Aeolus; founder of Iolcus, grandfather of Jason (leader of the Argonauts to Colchis on the Black Sea!)."}),
        ("grk_salmoneus", "Salmoneus → Tyro → Pelias & Neleus (→ Nestor)", {"notes": "Son of Aeolus; ancestor of Neleus and wise King Nestor of Pylos."}),
        ("grk_athamas", "Athamas → Phrixus & Helle (Golden Fleece)", {"notes": "Son of Aeolus; father of Phrixus & Helle (eponym of the Hellespont)."}),
    ], default_sources=["Hesiod Catalogue of Women", "Apollodorus I.7"])

    edges += [
        E("grk_prometheus", "grk_deucalion", "direct", "Prometheus -> Deucalion; Epimetheus + Pandora -> Pyrrha"),
        E("hub_flood", "grk_deucalion", "parallel", "Wooden chest/ark landing on Mt. Parnassus (Apollodorus I.7.2)"),
        E("grk_deucalion", "grk_hellen", "direct", "Son of Deucalion & Pyrrha (Catalogue of Women)"),
        E("hub_world_division", "grk_hellen", "parallel", "Hellen's 3 Sons (Dorus, Xuthus, Aeolus) divide the Greek world"),
        E("grk_hellen", "grk_dorus", "direct", "Son (Hesiod fr. 9)"),
        E("grk_hellen", "grk_xuthus", "direct", "Son (Hesiod fr. 9)"),
        E("grk_hellen", "grk_aeolus", "direct", "Son (Hesiod fr. 9)"),
        E("grk_xuthus", "grk_ion", "direct", "Son (Apollodorus I.7.3)"),
        E("grk_xuthus", "grk_achaeus", "direct", "Son (Apollodorus I.7.3)"),
        E("bib_javan", "grk_ion", "cognate", "EXACT linguistic cognate: Biblical Javan (Yawan, Gen 10:2) = Greek Ion / Iawones (Ionians)!"),
    ]

    # 3. THE GREAT AFRO-ASIATIC <-> GREEK BRIDGE: Inachus -> Io -> Epaphus (Egypt) -> Libya -> Belus & Agenor (Phoenicia, Crete, Thebes, Argos, Aethiopia, Persia, Sparta!)
    nodes += [
        N("grk_inachus_io", "Inachus (Argos) → Phoroneus & Io", "greek", 4, "Argive Primordial Line",
          "First King of Argos & Ancestress of Egypt/Phoenicia/Greece", ["Apollodorus II.1.1-3", "Aeschylus Prometheus Bound"],
          "Inachus (son of Oceanus) fathers Phoroneus (first mortal king of Argos) and Io, who wanders across the Bosporus into Egypt!", major=True),
        N("grk_epaphus", "Epaphus (King of Egypt) & Queen Memphis", "greek", 5, "Argive-Egyptian Bridge (Apollodorus II.1.3)",
          "Son of Zeus & Io / Identified with Egyptian Apis", ["Apollodorus II.1.3", "Herodotus II.153"],
          "Born to Io beside the Nile; becomes King of Egypt, marries Memphis (eponym of Egypt's capital!), and fathers Libya.",
          ["Apis (Herodotus II.153)"], major=True),
        N("grk_libya", "Libya (Eponym of North Africa)", "greek", 6, "Daughter of Epaphus & Memphis",
          "Mother of Belus & Agenor (Uniting Africa, Egypt, Phoenicia & Greece!)", ["Apollodorus II.1.4"],
          "Daughter of Epaphus & Memphis; by Poseidon bears twin sons Belus (Egypt/Babylon/Aethiopia) and Agenor (Tyre/Phoenicia)!", major=True),

        # Branch A: AGENOR (King of Tyre / Phoenicia) -> Europa (Crete), Cadmus (Thebes), Phoenix, Cilix
        N("grk_agenor", "Agenor (King of Tyre / Phoenicia) & Telephassa", "greek", 7, "Phoenician-Greek Bridge (Apollodorus III.1)",
          "Twin Son of Libya & Poseidon / Father of Europa & Cadmus", ["Apollodorus III.1.1", "Herodotus IV.147"],
          "Moves from Egypt to Phoenicia (Tyre/Sidon) and fathers Europa, Cadmus, Phoenix, Cilix, and Thasus!", major=True),
        N("grk_europa_minos", "Europa → King Minos of Crete, Rhadamanthus & Sarpedon", "greek", 8, "Minoan Crete (Caphtorim)",
          "Phoenician Princess → Minoan Royal House (Ariadne & Phaedra)", ["Homer Iliad XIV", "Apollodorus III.1.1-2"],
          "Carried from Phoenicia to Crete (Biblical Caphtorim!) by Zeus; bears King Minos (lawgiver of Knossos; father of Ariadne & Phaedra), Rhadamanthus, and Sarpedon.",
          ["Minos of Knossos", "Crete = Caphtorim"], major=True),
        N("grk_cadmus", "Cadmus (Founder of Thebes) & Harmonia", "greek", 8, "Phoenician-Theban Bridge (Herodotus V.58)",
          "Bringer of the Phoenician Alphabet to Greece", ["Herodotus V.58", "Apollodorus III.4.1-2"],
          "Son of Agenor of Tyre; settles in Boeotia, founds Thebes, and introduces the 'Phoenician letters' (alphabet!) to Greece! Fathers Semele (-> Dionysus), Ino, Autonoe, Agave, and Polydorus.",
          ["Phoenician Alphabet Bridge"], major=True),
        N("grk_dionysus_oedipus", "Semele (→ Dionysus) & Polydorus → Laius → Oedipus → Antigone", "greek", 9, "House of Thebes",
          "Descendants of Cadmus of Phoenicia", ["Sophocles Oedipus Rex & Antigone", "Apollodorus III.4-5"],
          "Cadmus's daughter Semele bears Dionysus; his son Polydorus leads via Labdacus -> Laius to Oedipus -> Antigone, Eteocles, and Polynices."),
        N("grk_phoenix_cilix", "Phoenix (Phoenicians) & Cilix (Cilicia)", "greek", 8, "Sons of Agenor",
          "Eponyms of Phoenicia & Cilicia", ["Apollodorus III.1.1"],
          "Brothers of Cadmus and Europa who settle Phoenicia and Cilicia (SE Anatolia)."),

        # Branch B: BELUS (King of Egypt) -> Aegyptus, Danaus (Argos), Cepheus (Aethiopia) -> Perseus + Andromeda -> Perses & Heracles!
        N("grk_belus", "Belus (King of Egypt — Ba'al)", "greek", 7, "Egyptian-Greek Bridge (Apollodorus II.1.4)",
          "Twin Son of Libya & Poseidon / Father of Aegyptus, Danaus & Cepheus", ["Apollodorus II.1.4", "Nonnus Dionysiaca"],
          "Reigns in Egypt (name reflects Semitic Ba'al/Bel); fathers Aegyptus, Danaus, Cepheus (King of Aethiopia), and Phineus.", major=True),
        N("grk_aegyptus_danaus", "Aegyptus (50 Sons) & Danaus (50 Danaids → Argos)", "greek", 8, "Egyptian-Argive Migration (Apollodorus II.1.5)",
          "Eponym of Egypt & Founder of Danaan Argos", ["Aeschylus Suppliants", "Apollodorus II.1.4-5"],
          "Aegyptus gives his name to Egypt; his twin brother Danaus flees Egypt with his 50 daughters (Danaids) to become King of Argos in Greece (Homer's 'Danaans'!). Daughter Hypermnestra marries Aegyptus's son Lynceus!",
          ["Danaans (Homer)", "Hypermnestra & Lynceus"], major=True),
        N("grk_cepheus_andromeda", "Cepheus (King of Aethiopia) & Cassiopeia → Andromeda", "greek", 8, "Aethiopian-Greek Bridge (Apollodorus II.4.3)",
          "Royal House of Aethiopia", ["Apollodorus II.4.3", "Ovid Metamorphoses IV"],
          "Brother of Danaus & Aegyptus; rules Aethiopia/Joppa coast. Daughter Andromeda is rescued from the sea monster Cetus by Perseus!"),
        N("grk_perseus", "Lynceus → Abas → Acrisius → Danaë → Perseus", "greek", 9, "Argive-Mycenaean Hero (Founder of Mycenae)",
          "Slayer of Medusa / Husband of Andromeda", ["Apollodorus II.2-4", "Herodotus VII.61"],
          "Descendant of Egyptian Danaus & Aegyptus; slays Medusa, rescues and marries Princess Andromeda of Aethiopia, founds Mycenae, and fathers Perses (mythic eponym of Persia!) and the ancestors of Heracles!", major=True),
        N("grk_perses", "Perses (Son of Perseus & Andromeda)", "greek", 10, "Herodotus VII.61",
          "Greek Mythic Eponym of the Persians!", ["Herodotus VII.61", "Apollodorus II.4.5"],
          "Herodotus (VII.61) explicitly records the ancient tradition that the Persians took their name from Perses, son of Perseus and Andromeda — a classic Greek-Iranian genealogical bridge!"),
        N("grk_heracles", "Alcaeus / Electryon → Alcmene → Heracles (Hercules)", "greek", 10, "Heroic Age (Apollodorus II.4-7)",
          "Greatest Greek Hero / Ancestor of Sparta & Macedon", ["Hesiod Shield", "Apollodorus II.4-7", "1 Maccabees 12:21"],
          "Great-grandson of Perseus & Andromeda (via Alcmene & Zeus). His sons (Heraclidae: Hyllus, Temenus) become the royal houses of Sparta and Macedon — and 1 Maccabees 12:21 records Sparta claiming kinship with Abraham!",
          ["Hercules", "Ancestor of Heraclidae"], major=True),
        N("grk_sparta_macedon", "Hyllus → Kings of Sparta (Areus I) & Argead Macedon (Philip II)", "greek", 12, "Classical Greece (Heraclidae)",
          "Spartan & Macedonian Royal Dynasties", ["Herodotus VIII.137", "1 Maccabees 12:20-23", "Josephus Ant. 12.4.10"],
          "Heraclidae conquer the Peloponnese (Sparta: Leonidas, King Areus I who wrote to Jerusalem's High Priest claiming descent from Abraham!) and Temenus's line founds Macedon (Perdiccas I -> Philip II)."),
        N("grk_alexander", "Alexander the Great (Macedon → Persia, Egypt & India)", "greek", 13, "356-323 BCE",
          "Conqueror Uniting Greece, Egypt, Mesopotamia, Persia & NW India", ["Arrian Anabasis", "Plutarch Alexander", "1 Maccabees 1", "Shahnameh (Eskandar)"],
          "Son of Philip II (Heraclid) and Olympias (claiming descent from Achilles!). Conquers Darius III of Persia, is crowned Pharaoh in Egypt, and marches to the Indus — even woven into the Persian Shahnameh as 'Eskandar' (half-brother of Dara)!",
          ["Eskandar (Shahnameh)", "Iskandar"], major=True),
    ]
    edges += [
        E("grk_oceanus_hyperion", "grk_inachus_io", "direct", "Oceanus -> River God Inachus -> Io"),
        E("grk_inachus_io", "grk_epaphus", "direct", "Zeus + Io -> Epaphus (King of Egypt)"),
        E("grk_zeus_olympians", "grk_epaphus", "direct", "Father of Epaphus"),
        E("grk_epaphus", "grk_libya", "direct", "Epaphus + Memphis -> Libya"),
        E("grk_libya", "grk_agenor", "direct", "Libya + Poseidon -> Twin son Agenor (Tyre)"),
        E("grk_libya", "grk_belus", "direct", "Libya + Poseidon -> Twin son Belus (Egypt)"),
        E("grk_agenor", "grk_europa_minos", "direct", "Daughter Europa -> Minos, Rhadamanthus, Sarpedon"),
        E("grk_agenor", "grk_cadmus", "direct", "Son Cadmus -> Founder of Thebes"),
        E("grk_agenor", "grk_phoenix_cilix", "direct", "Sons Phoenix & Cilix"),
        E("grk_cadmus", "grk_dionysus_oedipus", "direct", "Semele (-> Dionysus) & Polydorus -> Oedipus -> Antigone"),
        E("grk_belus", "grk_aegyptus_danaus", "direct", "Twin sons Aegyptus & Danaus (Apollodorus II.1.4)"),
        E("grk_belus", "grk_cepheus_andromeda", "direct", "Son Cepheus (King of Aethiopia) -> Andromeda"),
        E("grk_aegyptus_danaus", "grk_perseus", "direct", "Hypermnestra + Lynceus -> Abas -> Acrisius -> Danae -> Perseus"),
        E("grk_cepheus_andromeda", "grk_perseus", "direct", "Princess Andromeda of Aethiopia marries Perseus"),
        E("grk_perseus", "grk_perses", "direct", "Son of Perseus & Andromeda (Herodotus VII.61)"),
        E("grk_perseus", "grk_heracles", "direct", "Electryon -> Alcmene (+ Zeus) -> Heracles"),
        E("grk_heracles", "grk_sparta_macedon", "direct", "Heraclidae: Hyllus (Sparta) & Temenus (Macedon)"),
        E("grk_sparta_macedon", "grk_alexander", "direct", "Philip II of Macedon -> Alexander the Great"),

        # Cross-Tradition Bridges (Egypt, Phoenicia, Crete/Caphtorim, Ethiopia, Persia, Abraham/Sparta!)
        E("grk_epaphus", "eg_menes", "parallel", "Epaphus King of Egypt (husband of Memphis) <-> Memphite Egyptian kingship"),
        E("grk_aegyptus_danaus", "bib_mizraim", "cognate", "Greek Aegyptus (Hikuptah/Egypt) = Biblical Mizraim"),
        E("grk_libya", "bib_lehabim", "cognate", "Greek Libya = Biblical Lehabim/Libya (Gen 10:13)"),
        E("grk_agenor", "bib_sidon", "cognate", "Agenor & Cadmus of Tyre/Sidon = Phoenician Canaan (Gen 10:15)"),
        E("grk_cadmus", "le_sanchuniathon", "cognate", "Herodotus V.58: Cadmus brings Phoenician alphabet (cf. Taaut/Thoth) to Greece!"),
        E("grk_europa_minos", "bib_caphtorim", "cognate", "Minoan Crete (King Minos) = Biblical Caphtorim / Keftiu (Gen 10:14)!"),
        E("grk_cepheus_andromeda", "bib_cush", "cognate", "Greek Aethiopia = Biblical Cush"),
        E("grk_perses", "ir_achaemenes", "syncretic", "Herodotus VII.61: Greek chroniclers derive Persians from Perses, son of Perseus & Andromeda"),
        E("grk_sparta_macedon", "bib_abraham", "syncretic", "1 Maccabees 12:21 & Josephus Ant. 12.4: King Areus I of Sparta claims brotherhood with Judah through Abraham!"),
        E("grk_alexander", "ir_artaxerxes1", "cognate", "Alexander conquers Darius III (331 BCE); woven into Shahnameh as Eskandar"),
        E("grk_alexander", "eg_ptolemy_cleopatra", "direct", "Alexander's general Ptolemy I founds the Ptolemaic Dynasty of Egypt (305 BCE)"),
    ]

    # 4. Mycenaean Heroes (Pelops/Atreus, Achilles, Odysseus) & House of Troy -> Aeneas -> Romulus & Remus (Rome!)
    nodes += [
        N("grk_pelops_atreus", "Tantalus (Lydia) → Pelops → Atreus & Thyestes", "greek", 9, "Anatolian-Mycenaean Line",
          "House of Atreus (Peloponnese)", ["Homer Iliad", "Pindar Olympian 1", "Apollodorus Epitome 2"],
          "Tantalus of Anatolia/Lydia fathers Pelops (eponym of the Peloponnese!), who fathers Atreus and Thyestes."),
        N("grk_agamemnon_menelaus", "Agamemnon (→ Orestes) & Menelaus (+ Helen of Sparta)", "greek", 10, "Trojan War (c. 1200 BCE trad.)",
          "Kings of Mycenae & Sparta (Sons of Atreus)", ["Homer Iliad & Odyssey"],
          "Agamemnon leads the Achaeans against Troy (father of Orestes, Electra, Iphigenia); Menelaus weds Helen (daughter of Zeus & Leda, sister of Castor, Pollux & Clytemnestra).", major=True),
        N("grk_achilles_odysseus", "Peleus → Achilles & Laertes → Odysseus (→ Telemachus)", "greek", 10, "Trojan War Heroes (Homer)",
          "Champions of the Iliad & Odyssey", ["Homer Iliad & Odyssey"],
          "Achilles (son of Peleus & Thetis, grandson of Aeacus; father of Neoptolemus — claimed ancestor of Alexander's mother Olympias!) and Odysseus (King of Ithaca, father of Telemachus).", major=True),

        N("grk_dardanus_tros", "Dardanus (son of Zeus & Electra) → Erichthonius → Tros", "greek", 7, "Foundation of Troy (Iliad XX.215-240)",
          "Founders of Dardania & Troy (Anatolia)", ["Homer Iliad XX.215-240", "Apollodorus III.12"],
          "Dardanus (son of Zeus & Atlas's daughter Electra) founds Dardania near the Hellespont; grandson Tros gives his name to Troy and fathers Ilus, Assaracus, and Ganymede!", major=True),
        N("grk_priam_hector", "Ilus → Laomedon → King Priam → Hector, Paris & Cassandra", "greek", 10, "Trojan Royal House (Iliad)",
          "Last King of Troy & 50 Sons", ["Homer Iliad", "Apollodorus III.12.5"],
          "Senior branch of Troy: Ilus -> Laomedon -> King Priam & Queen Hecuba, parents of Hector, Paris (Alexander), Cassandra, Helenus, and Creusa (first wife of Aeneas).", major=True),
        N("grk_aeneas", "Assaracus → Capys → Anchises → Aeneas (+ Lavinia)", "greek", 10, "Fall of Troy → Migration to Italy (Aeneid)",
          "Trojan Prince & Ancestor of Rome", ["Homer Iliad XX", "Virgil Aeneid", "Livy I.1"],
          "Junior Trojan branch: Assaracus -> Capys -> Anchises (+ Aphrodite) -> Aeneas, who escapes burning Troy to Italy (Latium), marries Lavinia (daughter of King Latinus), and fathers Ascanius (Iulus) and Silvius!",
          ["Ancestor of Rome & Julius Caesar"], major=True),
        N("grk_romulus_remus", "Ascanius (Iulus) → Alba Longa Kings → Rhea Silvia → Romulus & Remus", "greek", 12, "753 BCE trad. (Foundation of Rome)",
          "Founders of Rome (Bridging Troy & Italy)", ["Livy Ab Urbe Condita I", "Virgil Aeneid", "Plutarch Romulus"],
          "Ascanius (Iulus, ancestor of the Julian clan / Julius Caesar!) & Silvius found Alba Longa -> 12 Alban kings -> Numitor -> Rhea Silvia (+ Mars) -> twin founders Romulus & Remus! Directly intersects Book of Jasher's Kittim/Zepho/Janeus chronicle of early Italy!",
          ["Founders of Rome", "Alba Longa"], major=True),
    ]
    edges += [
        E("grk_zeus_olympians", "grk_pelops_atreus", "direct", "Zeus -> Tantalus -> Pelops -> Atreus & Thyestes"),
        E("grk_pelops_atreus", "grk_agamemnon_menelaus", "direct", "Sons of Atreus (Iliad)"),
        E("grk_zeus_olympians", "grk_achilles_odysseus", "direct", "Zeus -> Aeacus -> Peleus -> Achilles; Hermes -> Autolycus -> Odysseus"),
        E("grk_atlas", "grk_dardanus_tros", "direct", "Electra (dau. of Atlas) + Zeus -> Dardanus -> Erichthonius -> Tros (Iliad XX)"),
        E("grk_dardanus_tros", "grk_priam_hector", "direct", "Tros -> Ilus -> Laomedon -> Priam -> Hector & Paris"),
        E("grk_dardanus_tros", "grk_aeneas", "direct", "Tros -> Assaracus -> Capys -> Anchises -> Aeneas (Iliad XX)"),
        E("grk_aeneas", "grk_romulus_remus", "direct", "Aeneas -> Ascanius/Silvius -> Alba Longa -> Rhea Silvia -> Romulus & Remus"),
        E("grk_romulus_remus", "jas_janeus", "syncretic", "Roman origin tradition (Aeneas/Latinus/Janus/Romulus) intersects Book of Jasher 61-64 (Zepho -> Janeus of Kittim/Italy)!"),
        E("grk_achilles_odysseus", "grk_alexander", "expansion", "Alexander's mother Olympias (Molossian royal house) claimed direct descent from Achilles via Neoptolemus"),
    ]

    # 5. Mediterranean Phoenician-Carthaginian & Lydian-Etruscan Bridges (Dido/Carthage & Lydus/Tyrrhenus!)
    nodes += [
        N("grk_dido_carthage", "Ethbaal of Tyre → Mattan I → Queen Dido (Elissa of Carthage)", "greek", 11, "c. 814 BCE trad. (Tyre → North Africa)",
          "Phoenician Founder of Carthage (Great-Niece of Jezebel!)", ["Josephus Against Apion 1.18", "Justin XVIII", "Virgil Aeneid I & IV"],
          "Tyrian royal records (Menander of Ephesus, quoted by Josephus) trace King Ethbaal (Ithobaal I of Sidon/Tyre, father of Biblical Jezebel!) -> Baal-Eser II -> Mattan I -> Pygmalion & Queen Elissa (Dido), who sails from Tyre to North Africa and founds Carthage!",
          ["Elissa of Tyre", "Founder of Carthage"], major=True),
        N("grk_lydus_tyrrhenus", "Atys of Lydia → Lydus (Lydians) & Tyrrhenus (Etruscans)", "greek", 7, "Anatolia → Italy (Herodotus I.94)",
          "Eponyms of Lydia (Lud) & Etruria (Tiras?)", ["Herodotus Histories I.94"],
          "Herodotus records that during an 18-year famine in Lydia (Biblical Lud, Gen 10:22!), King Atys split his people between Lydus (staying in Anatolia) and Tyrrhenus, who sailed to Italy to found the Etruscans (Tyrsenians — widely linked by scholars to Biblical Tiras, Gen 10:2)!",
          ["Lydians = Lud (Gen 10:22)", "Tyrsenians = Tiras (Gen 10:2)"]),
    ]
    edges += [
        E("bib_sidon", "grk_dido_carthage", "cognate", "Tyrian royal house of Sidon/Tyre (Ethbaal -> Mattan -> Dido/Elissa)"),
        E("grk_dido_carthage", "af_mazigh", "cognate", "Carthage founded in North Africa among ancestral Amazigh/Numidian peoples (King Hiarbas)"),
        E("grk_dido_carthage", "grk_aeneas", "expansion", "Virgil's Aeneid links Carthaginian Queen Dido and Trojan prince Aeneas"),
        E("bib_lud", "grk_lydus_tyrrhenus", "cognate", "Biblical Lud (Gen 10:22) = Herodotus's Lydus / Lydia"),
        E("bib_tiras", "grk_lydus_tyrrhenus", "cognate", "Biblical Tiras (Gen 10:2) = Tyrsenians / Tyrrhenus (Etruscans)!"),
    ]

    return {"module": "09_greek_mediterranean", "title": "Exhaustive Greek & Mediterranean Genealogy (Hesiod Theogony, Deucalion, Hellen/Ion, Egypt-Phoenicia Bridge, Crete, Thebes, Heracles, Troy, Rome, Carthage & Etruscans)", "nodes": nodes, "edges": edges}


def main():
    MODULES_DIR.mkdir(parents=True, exist_ok=True)

    modules = [
        load_existing_module("01_antediluvian"),
        load_existing_module("02_table_of_nations"),
        load_existing_module("03_abraham_all_nations"),
        load_existing_module("04_egypt_levant"),
        load_existing_module("05_mesopotamia"),
        load_existing_module("06_iranian_zoroastrian"),
        load_existing_module("07_asia_steppe"),
        load_existing_module("08_african_ethiopian"),
        build_module_09_greek_mediterranean(),
    ]

    all_nodes, all_edges = [], []
    module_summaries = []

    for mod in modules:
        mod_path = MODULES_DIR / f"{mod['module']}.json"
        with open(mod_path, "w", encoding="utf-8") as f:
            json.dump(mod, f, indent=2, ensure_ascii=False)
        all_nodes.extend(mod["nodes"])
        all_edges.extend(mod["edges"])
        module_summaries.append({"file": mod["module"], "title": mod["title"], "nodes": len(mod["nodes"]), "edges": len(mod["edges"])})

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
            "title": "Ancient World Genealogy Atlas — Exhaustive Multi-Tradition Database (Phase 5)",
            "version": "5.0.0",
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
