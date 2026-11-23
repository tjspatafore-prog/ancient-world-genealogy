"""
Modular Ancient World Genealogy Dataset Builder & Validator (Phase 3).

Generates clean modular JSON files under data/modules/ and compiles them into
data/world_genealogy.json for the interactive web explorer, ensuring zero broken
links, full provenance tagging, and exhaustive person-by-person accounting.
"""

import json
from collections import Counter
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
    "expansion": "Matriarchs, additional children, royal successions, or migrations supplied by extra-biblical or secondary chronicles (Book of Jasher, Jubilees, 1 Enoch, Sumerian King List, Bundahishn, Shahnameh, Shiji, Puranas)",
    "cognate":   "Linguistically or historically attested cross-tradition identity/ethnonym bridge (e.g., Vedic Vivasvan/Yama/Aptya = Avestan Vivanghant/Yima/Athwya; Biblical Madai = Medes; Mizraim = Phoenician Misor/Egypt)",
    "parallel":  "Independent structural/archetypal parallel across ancient corpora (Great Flood survivors, 7th antediluvian sage, Adapa/Adam, Sargon/Moses basket, tripartite world division)",
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
    nodes = [
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
    edges = [
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
    return {"module": "04_egypt_levant", "title": "Egyptian Cross-Traditions & Phoenician-Canaanite Lineages", "nodes": nodes, "edges": edges}


def build_module_05_mesopotamia():
    nodes, edges = [], []

    # 1. Primordial Theogony (Enuma Elish, Atrahasis, Sumerian An = Anum) — EVERY Deity Individualized!
    nodes += [
        N("mes_apsu_tiamat", "Apsu & Tiamat", "mesopotamian", 1, "Cosmic Primordial (Enuma Elish I)",
          "Primordial Freshwater & Saltwater Parents", ["Enuma Elish Tablet I"],
          "Primordial cosmic waters whose mingling generates the elder gods Lahmu and Lahamu.", ["Abzu & Tiamat"], major=True),
        N("mes_lahmu_lahamu", "Lahmu & Lahamu", "mesopotamian", 1, "Cosmic Gen 2 (Enuma Elish I)", "First Divine Pair", ["Enuma Elish Tablet I"], "Born of Apsu & Tiamat; parents of Anshar & Kishar."),
        N("mes_anshar_kishar", "Anshar & Kishar", "mesopotamian", 1, "Cosmic Gen 3 (Enuma Elish I)", "Heavenly & Earthly Horizons", ["Enuma Elish Tablet I"], "Parents of the Sky Father Anu."),
        N("mes_anu", "Anu (An) & Antu / Ki", "mesopotamian", 1, "Sky Father (Sumerian/Babylonian)", "King of Heaven", ["Enuma Elish", "Sumerian Myths"], "Supreme sky deity of Uruk; father of Enki (Ea) and Enlil.", ["An"], major=True),
        N("mes_enki", "Enki (Ea) & Damkina (Ninhursag)", "mesopotamian", 1, "God of Wisdom, Waters & Eridu", "Creator of Humanity & Protector of Flood Survivor", ["Enuma Elish", "Atrahasis", "Eridu Genesis"], "Patron of Eridu; with Nintu/Belet-ili fashions the first humans (Lullu) from clay mixed with divine blood, and secretly warns Ziusudra/Atrahasis of the Flood.", ["Ea", "Nudimmud"], major=True),
        N("mes_enlil", "Enlil & Ninlil", "mesopotamian", 1, "Lord of Wind & Nippur", "Ruler of Divine Assembly", ["Atrahasis", "Enlil and Ninlil"], "Father of Nanna (Sin) and Ninurta; decrees the Deluge in Atrahasis.", major=True),
        N("mes_marduk", "Marduk (Bel)", "mesopotamian", 2, "Patron God of Babylon", "Slayer of Tiamat & Cosmic Architect", ["Enuma Elish IV-VI"], "Son of Enki (Ea) & Damkina; slays Tiamat, builds Babylon, and fashions humanity from Qingu's blood.", ["Bel"], major=True),
        N("mes_nabu", "Nabu (Scribe God of Borsippa)", "mesopotamian", 2, "Babylonian Patron of Writing", "Son of Marduk & Sarpanit", ["Babylonian Pantheon"], "Son of Marduk; keeper of the Tablets of Destiny and patron of scribes."),
        N("mes_ninurta", "Ninurta (Ningirsu)", "mesopotamian", 2, "Warrior-Hunter Deity of Nippur", "Son of Enlil (Compared to Nimrod)", ["Lugal-e", "Anzu Myth"], "Mythic hunter and champion of the gods — widely proposed by Assyriologists as a mythological source for Biblical Nimrod ('mighty hunter')!", ["Ningirsu", "Possible root of Nimrod"]),
        N("mes_nanna", "Nanna (Sin — Moon God of Ur)", "mesopotamian", 2, "Patron of Ur", "Son of Enlil & Ninlil", ["Sumerian Hymns"], "Moon god of Ur; marries Ningal and fathers Utu (Shamash) and Inanna (Ishtar)."),
        N("mes_shamash", "Utu (Shamash — Sun God of Sippar/Larsa)", "mesopotamian", 2, "God of Sun & Justice", "Father of Meskiaggasher (Founder of Uruk)", ["Sumerian King List", "Enmeduranki Text"], "Son of Nanna; reveals celestial tablets to 7th king Enmeduranki at Sippar and fathers Meskiaggasher of Uruk!"),
        N("mes_inanna", "Inanna (Ishtar — Queen of Heaven)", "mesopotamian", 2, "Goddess of Uruk", "Daughter of Nanna / Anu", ["Descent of Inanna", "Epic of Gilgamesh"], "Patron goddess of Uruk (Eanna) and consort of Dumuzid."),
        N("mes_lullu_adapa", "Lullu (First Humans) & Adapa / Uanna (1st Apkallu)", "mesopotamian", 2, "Primordial Eridu (Atrahasis / Adapa Myth)", "First Humans & 1st Antediluvian Sage", ["Atrahasis Tablet I", "Myth of Adapa", "Berossus Babyloniaca"], "Lullu is fashioned from clay + divine blood of We-ilu/Qingu. Adapa (1st Apkallu sage under Alulim, called Oannes by Berossus) ascends to heaven and forfeits eternal life — widely compared to Adam!", ["Oannes (Berossus)", "Adapa <-> Adam Parallel"], major=True),
    ]
    edges += [
        E("hub_primordial", "mes_apsu_tiamat", "parallel", "Primordial cosmic creation"),
        E("hub_primordial", "mes_lullu_adapa", "parallel", "Humans fashioned from clay + divine blood; Adapa <-> Adam"),
        E("bib_adam", "mes_lullu_adapa", "parallel", "Adapa of Eridu forfeits eternal life in heaven <-> Adam"),
        E("mes_apsu_tiamat", "mes_lahmu_lahamu", "direct", "First divine pair (Enuma Elish I)"),
        E("mes_lahmu_lahamu", "mes_anshar_kishar", "direct", "Second divine pair (Enuma Elish I)"),
        E("mes_anshar_kishar", "mes_anu", "direct", "Son (Enuma Elish I)"),
        E("mes_anu", "mes_enki", "direct", "Son (Enuma Elish I)"),
        E("mes_anu", "mes_enlil", "direct", "Son (Sumerian tradition)"),
        E("mes_enki", "mes_marduk", "direct", "Enki + Damkina -> Marduk (Enuma Elish)"),
        E("mes_marduk", "mes_nabu", "direct", "Son (Babylonian pantheon)"),
        E("mes_enki", "mes_lullu_adapa", "direct", "Enki fashions Lullu & creates sage Adapa"),
        E("mes_enlil", "mes_ninurta", "direct", "Son (Sumerian pantheon)"),
        E("mes_enlil", "mes_nanna", "direct", "Enlil + Ninlil -> Nanna/Sin"),
        E("mes_nanna", "mes_shamash", "direct", "Nanna + Ningal -> Utu/Shamash"),
        E("mes_nanna", "mes_inanna", "direct", "Nanna + Ningal -> Inanna/Ishtar"),
        E("bib_nimrod", "mes_ninurta", "parallel", "Scholars compare Nimrod ('mighty hunter') to Mesopotamian hunter-warrior Ninurta"),
    ]

    # 2. ALL 10 Antediluvian Kings + 7 Apkallu Sages (Individualized!)
    ante_kings = [
        ("mes_k1_alulim", "1. Alulim (Aloros of Eridu)", 2, "28,800 yrs (Eridu)", "1st Antediluvian King of Eridu; advised by 1st Apkallu sage Uanna/Adapa.", ["Aloros"], True),
        ("mes_k2_alalngar", "2. Alalngar (Alaparos of Eridu)", 2, "36,000 yrs (Eridu)", "2nd Antediluvian King of Eridu; sage Uannedugga.", ["Alaparos"], False),
        ("mes_k3_enmenluana", "3. En-men-lu-ana (Amelon of Bad-tibira)", 2, "43,200 yrs (Bad-tibira)", "3rd Antediluvian King; kingship moves to Bad-tibira; sage Enmedugga.", ["Amelon"], False),
        ("mes_k4_enmengalana", "4. En-men-gal-ana (Ammenon of Bad-tibira)", 2, "28,800 yrs (Bad-tibira)", "4th Antediluvian King of Bad-tibira; sage Enmegalamma.", ["Ammenon"], False),
        ("mes_k5_dumuzid", "5. Dumuzid the Shepherd (Daonos)", 2, "36,000 yrs (Bad-tibira)", "5th Antediluvian King of Bad-tibira; sage Enmebulugga.", ["Daonos"], False),
        ("mes_k6_ensipadzidana", "6. En-sipad-zid-ana (Amempsinos of Larak)", 3, "28,800 yrs (Larak)", "6th Antediluvian King; kingship moves to Larak; sage An-Enlilda.", ["Amempsinos"], False),
        ("mes_enmeduranki", "7. En-men-dur-ana (Enmeduranki of Sippar)", 3, "21,000 yrs (Sippar)", "7th Antediluvian King (Euedorachos in Berossus); ruler of sun-city Sippar, initiated by Shamash & Adad into heavenly secrets and divination alongside 7th sage Utuabzu (who ascends to heaven) — exact structural parallel to Enoch (7th patriarch, 365 solar years)!", ["Euedorachos", "7th Sage: Utuabzu"], True),
        ("mes_k8_megalaros", "8. Megalaros / Amegalaros (Berossus)", 3, "Berossus 10-King List", "Included in Berossus's 10-king antediluvian list (matching Genesis 5's 10 patriarchs).", ["Amegalaros"], False),
        ("mes_k9_ubaratutu", "9. Ubara-Tutu (Otiartes of Shuruppak)", 3, "18,600 yrs (Shuruppak)", "Last king of Shuruppak before the Deluge; father of Ziusudra / Utnapishtim!", ["Otiartes", "Ardates"], True),
        ("mes_ziusudra", "10. Ziusudra / Utnapishtim / Atrahasis", 4, "Flood Horizon (Shuruppak)", "10th Antediluvian ruler (Xisouthros in Berossus). Warned by Enki/Ea of the Deluge; builds a vessel preserving family and animals; releases dove, swallow, and raven; lands on Mt. Nimush.", ["Xisouthros", "Utnapishtim", "Atrahasis"], True),
    ]
    prev_k = "mes_lullu_adapa"
    for kid, kname, ktier, kera, knote, kalts, kmaj in ante_kings:
        nodes.append(N(kid, kname, "mesopotamian", ktier, f"Antediluvian SKL • {kera}",
                       "Antediluvian King (Sumerian King List / Berossus)",
                       ["Sumerian King List (WB 444)", "Berossus Babyloniaca", "Uruk List of Kings & Sages"],
                       knote, altNames=kalts, major=kmaj))
        edges.append(E(prev_k, kid, "direct" if kid == "mes_ziusudra" else "expansion",
                       "Son of Ubara-Tutu (Gilgamesh XI / Eridu Genesis)" if kid == "mes_ziusudra" else "Sumerian King List antediluvian succession"))
        prev_k = kid

    # 7th Apkallu Sage Utuabzu explicitly linked to Enmeduranki & Enoch!
    nodes.append(N("mes_utuabzu", "Utuabzu (7th Apkallu Sage Who Ascended to Heaven)", "mesopotamian", 3, "Antediluvian Sippar",
                   "7th Sage under Enmeduranki", ["Uruk List of Kings & Sages", "Bit Meseri"],
                   "The 7th antediluvian sage, counselor to 7th king Enmeduranki, explicitly recorded as 'having ascended to heaven' — a stunning Mesopotamian parallel to Enoch (7th from Adam, taken to heaven)!",
                   ["7th Apkallu"], major=False))
    edges += [
        E("mes_enmeduranki", "mes_utuabzu", "expansion", "7th Apkallu sage serving 7th king Enmeduranki"),
        E("bib_enoch", "mes_enmeduranki", "parallel", "7th antediluvian figure; sun/365 association; heavenly ascent & tablets"),
        E("bib_enoch", "mes_utuabzu", "parallel", "7th antediluvian sage who ascended to heaven (Bit Meseri <-> Gen 5:24)"),
        E("hub_flood", "mes_ziusudra", "parallel", "Boat on Mt. Nimush; dove/swallow/raven (Gilgamesh XI / Atrahasis)"),
    ]

    # 3. Post-Flood First Dynasty of Kish (ALL named rulers of Kish I individually!)
    kish1 = [
        ("mes_kish_jushur", "Jushur (1st Post-Flood King of Kish)", 5, "1,200 yrs", True, "First king after the Flood swept over and kingship descended from heaven anew at Kish."),
        ("mes_kish_kullassinabel", "Kullassina-bel", 5, "960 yrs", False, "2nd king of Kish I ('All of them were lord')."),
        ("mes_kish_nangishlishma", "Nangishlishma", 5, "670 yrs", False, "3rd king of Kish I."),
        ("mes_kish_entarahana", "En-tarah-ana", 5, "420 yrs", False, "4th king of Kish I."),
        ("mes_kish_babum", "Babum", 5, "300 yrs", False, "5th king of Kish I."),
        ("mes_kish_puannum", "Puannum", 5, "840 yrs", False, "6th king of Kish I."),
        ("mes_kish_kalibum", "Kalibum", 5, "960 yrs", False, "7th king of Kish I."),
        ("mes_kish_kalumum", "Kalumum", 5, "840 yrs", False, "8th king of Kish I."),
        ("mes_kish_zuqaqip", "Zuqaqip ('Scorpion')", 5, "900 yrs", False, "9th king of Kish I."),
        ("mes_kish_atab", "Atab", 5, "600 yrs", False, "10th king of Kish I."),
        ("mes_kish_mashda", "Mashda (son of Atab)", 5, "840 yrs", False, "11th king of Kish I; son of Atab."),
        ("mes_kish_arwium", "Arwium (son of Mashda)", 5, "720 yrs", False, "12th king of Kish I; son of Mashda."),
        ("mes_etana", "Etana of Kish (Ascended on an Eagle)", 6, "1,500 yrs", True, "13th king of Kish I; 'the shepherd who ascended to heaven and consolidated all foreign countries' on an eagle's back to obtain the Plant of Birth."),
        ("mes_balih", "Balih (son of Etana)", 6, "400 yrs", False, "14th king of Kish I; son of Etana."),
        ("mes_enmenuna", "En-me-nuna", 6, "660 yrs", False, "15th king of Kish I; father of Melem-Kish and Barsal-nuna."),
        ("mes_melemkish", "Melem-Kish (son of En-me-nuna)", 6, "900 yrs", False, "16th king of Kish I."),
        ("mes_barsalnuna", "Barsal-nuna (son of En-me-nuna)", 6, "1,200 yrs", False, "17th king of Kish I."),
        ("mes_zamug", "Zamug (son of Barsal-nuna)", 6, "140 yrs", False, "18th king of Kish I."),
        ("mes_tizqar", "Tizqar (son of Zamug)", 6, "305 yrs", False, "19th king of Kish I."),
        ("mes_ilku", "Ilku", 6, "900 yrs", False, "20th king of Kish I."),
        ("mes_iltasadum", "Iltasadum", 6, "1,200 yrs", False, "21st king of Kish I."),
        ("mes_enmebaragesi", "Enmebaragesi of Kish (Conqueror of Elam)", 7, "c. 2600 BCE", True, "22nd king of Kish I; earliest Sumerian king confirmed by contemporary inscriptions! 'Carried away as spoil the weapons of Elam'."),
        ("mes_aga_kish", "Aga (Agga) of Kish", 7, "c. 2600 BCE", False, "23rd and final king of Kish I; son of Enmebaragesi, besieged Uruk and clashed with Gilgamesh."),
    ]
    prev_kish = "mes_ziusudra"
    for kid, kname, ktier, kera, kmaj, knote in kish1:
        nodes.append(N(kid, kname, "mesopotamian", ktier, f"First Dynasty of Kish • {kera}",
                       "King of Kish I", ["Sumerian King List (WB 444)"], knote, major=kmaj))
        # Direct parent-child edges explicitly stated in SKL!
        direct_pairs = {("mes_kish_atab","mes_kish_mashda"), ("mes_kish_mashda","mes_kish_arwium"),
                        ("mes_etana","mes_balih"), ("mes_enmenuna","mes_melemkish"),
                        ("mes_enmenuna","mes_barsalnuna"), ("mes_barsalnuna","mes_zamug"),
                        ("mes_zamug","mes_tizqar"), ("mes_enmebaragesi","mes_aga_kish")}
        parent_for_edge = "mes_enmenuna" if kid == "mes_barsalnuna" else prev_kish
        et = "direct" if (parent_for_edge, kid) in direct_pairs else "expansion"
        el = "Son (Sumerian King List)" if et == "direct" else "First Dynasty of Kish succession (SKL)"
        edges.append(E(parent_for_edge, kid, et, el))
        prev_kish = kid
    edges.append(E("mes_enmebaragesi", "bib_elam", "cognate", "Historical warfare between Kish and Elam (SKL)"))

    # 4. First Dynasty of Uruk / Biblical Erech (ALL 12 Kings Individually!)
    nodes += [
        N("mes_meskiaggasher", "Meskiaggasher (Founder of Uruk / Erech)", "mesopotamian", 5, "Early Dynastic I (Eanna / Uruk)",
          "Son of Sun God Utu (Shamash) / 1st King of Uruk", ["Sumerian King List (WB 444)"],
          "High priest and king of Eanna; 'entered the sea and ascended to the mountains'. Father of Enmerkar.", major=True),
        N("mes_enmerkar", "Enmerkar (Builder of Uruk / Erech)", "mesopotamian", 6, "Early Dynastic II (c. 2800 BCE)",
          "2nd King of Uruk / Inventor of Cuneiform", ["Sumerian King List", "Enmerkar and the Lord of Aratta"],
          "Son of Meskiaggasher; built Uruk (Biblical Erech, Gen 10:10) and invented cuneiform clay tablets in rivalry with Aratta (Iranian plateau!). Widely compared to Nimrod ('Enmer the Hunter').",
          ["Enmer the Hunter", "Compared to Nimrod"], major=True),
        N("mes_lugalbanda", "Lugalbanda & Goddess Ninsun", "mesopotamian", 6, "Early Dynastic II (Uruk I)",
          "3rd King of Uruk / Father of Gilgamesh", ["Sumerian King List", "Lugalbanda Epics", "Epic of Gilgamesh"],
          "Companion of Enmerkar; weds goddess Ninsun and fathers Gilgamesh.", major=True),
        N("mes_dumuzid_fisherman", "Dumuzid the Fisherman (of Kuara)", "mesopotamian", 7, "Early Dynastic II (Uruk I)",
          "4th King of Uruk I", ["Sumerian King List"],
          "Captured Enmebaragesi of Kish single-handedly before Gilgamesh."),
        N("mes_uruk_gilgamesh", "Gilgamesh (Bilgamesh of Uruk / Erech)", "mesopotamian", 7, "Early Dynastic II (c. 2700 BCE)",
          "5th King of Uruk / Builder of Uruk's Walls / Qumran Giant", ["Sumerian King List", "Epic of Gilgamesh", "Qumran Book of Giants (4Q530)"],
          "Son of Lugalbanda & Ninsun; visits Flood survivor Utnapishtim. Uruk is explicitly 'Erech' in Gen 10:10 — and 'Gilgamesh' is literally named as a Giant in Qumran Book of Giants (4Q530)!",
          ["Bilgamesh", "Erech (Gen 10:10)", "Gilgamesh in Qumran 4Q530"], major=True),
    ]
    edges += [
        E("mes_shamash", "mes_meskiaggasher", "direct", "Son of Utu/Shamash (Sumerian King List)"),
        E("mes_meskiaggasher", "mes_enmerkar", "direct", "Son (Sumerian King List)"),
        E("mes_enmerkar", "mes_lugalbanda", "expansion", "Succession at Uruk (SKL)"),
        E("mes_lugalbanda", "mes_dumuzid_fisherman", "expansion", "Succession at Uruk (SKL)"),
        E("mes_lugalbanda", "mes_uruk_gilgamesh", "direct", "Lugalbanda + Ninsun -> Gilgamesh (Epic of Gilgamesh)"),
        E("mes_uruk_gilgamesh", "mes_ziusudra", "expansion", "Epic of Gilgamesh XI: Gilgamesh visits Flood survivor Utnapishtim"),
        E("bib_nimrod", "mes_enmerkar", "parallel", "Enmerkar ('Enmer the Hunter', builder of Erech/Uruk) <-> Nimrod (Gen 10:10)"),
        E("bib_nimrod", "mes_uruk_gilgamesh", "cognate", "Gen 10:10 explicitly names Shinar, Babel & Erech (Uruk)"),
        E("eno_ohya_hahya", "mes_uruk_gilgamesh", "expansion", "Qumran Book of Giants (4Q530/4Q531) literally names Gilgamesh as a Giant!"),
    ]

    # Individual late Uruk I kings (6th to 12th)
    late_uruk = [
        ("mes_urnungal", "Ur-Nungal (son of Gilgamesh)", "direct", "6th king of Uruk I; son of Gilgamesh (reigned 30 yrs)."),
        ("mes_udulkalama", "Udul-kalama (son of Ur-Nungal)", "direct", "7th king of Uruk I; grandson of Gilgamesh (15 yrs)."),
        ("mes_labashum", "La-ba'shum", "expansion", "8th king of Uruk I (9 yrs)."),
        ("mes_ennuntarahana", "En-nun-tarah-ana", "expansion", "9th king of Uruk I (8 yrs)."),
        ("mes_meshhe", "Mesh-he", "expansion", "10th king of Uruk I (36 yrs)."),
        ("mes_melemana", "Melem-ana", "expansion", "11th king of Uruk I (6 yrs)."),
        ("mes_lugalkitun", "Lugal-kitun", "expansion", "12th and final king of Uruk I (36 yrs)."),
    ]
    prev_u = "mes_uruk_gilgamesh"
    for uid, uname, uet, unote in late_uruk:
        nodes.append(N(uid, uname, "mesopotamian", 8, "Early Dynastic II-III (Uruk I)", "King of Uruk I", ["Sumerian King List (WB 444)"], unote))
        edges.append(E(prev_u, uid, uet, "Son (Sumerian King List)" if uet == "direct" else "Uruk I succession (SKL)"))
        prev_u = uid

    # 5. Ur I, Akkad (ALL individual members!), Ur III (ALL 5 kings!), Amorite Babylon (ALL kings!) & Assyria
    nodes += [
        N("mes_mesannepada", "Mesannepada (Founder of Ur I)", "mesopotamian", 8, "Early Dynastic III (c. 2550 BCE)", "1st King of First Dynasty of Ur", ["Sumerian King List", "Royal Cemetery of Ur"], "Overthrew Uruk I; attested by royal seals from Ur.", major=True),
        N("mes_meshkiangnanna", "Mesh-ki-ang-nanna (son of Mesannepada)", "mesopotamian", 8, "Ur I", "2nd King of Ur I", ["Sumerian King List"], "Son of Mesannepada; followed by Elulu and Balulu."),
        N("mes_sargon", "Sargon of Akkad (Sharru-kin)", "mesopotamian", 8, "Akkadian Empire (c. 2334-2279 BCE)", "Founder of Akkad (Biblical Accad)", ["Sumerian King List", "Birth Legend of Sargon"], "Cupbearer of Ur-Zababa of Kish who founded the world's first empire (Biblical Accad, Gen 10:10). His Birth Legend ('reed basket sealed with bitumen on the river') parallels Moses in Exodus 2!", ["Sharru-kin", "Accad (Gen 10:10)"], major=True),
        N("mes_enheduanna", "Enheduanna (High Priestess of Ur)", "mesopotamian", 9, "c. 2285-2250 BCE", "Daughter of Sargon / Earliest Named Author in History", ["Exaltation of Inanna", "Temple Hymns", "Disk of Enheduanna"], "Daughter of Sargon of Akkad appointed High Priestess of Nanna at Ur; world's earliest known named author!", major=True),
        N("mes_rimush", "Rimush (son of Sargon)", "mesopotamian", 9, "c. 2279-2270 BCE", "2nd King of Akkad", ["Sumerian King List"], "Son of Sargon; campaigned against rebellious Sumerian cities and Elam."),
        N("mes_manishtushu", "Manishtushu (son of Sargon)", "mesopotamian", 9, "c. 2270-2255 BCE", "3rd King of Akkad", ["Sumerian King List", "Manishtushu Obelisk"], "Son of Sargon; father of Naram-Sin."),
        N("mes_naramsin", "Naram-Sin ('King of the Four Quarters')", "mesopotamian", 9, "c. 2254-2218 BCE", "4th King of Akkad (Grandson of Sargon)", ["Victory Stele of Naram-Sin", "Curse of Agade"], "Son of Manishtushu; peak of Akkadian Empire.", major=True),
        N("mes_sharkalisharri", "Shar-Kali-Sharri (son of Naram-Sin)", "mesopotamian", 9, "c. 2217-2193 BCE", "5th King of Akkad", ["Sumerian King List"], "Son of Naram-Sin; reigned as the Akkadian Empire faced Gutian invasions."),
        N("mes_urnammu", "Ur-Nammu (Founder of Ur III — Ur of the Chaldees)", "mesopotamian", 9, "Neo-Sumerian Empire (c. 2112-2095 BCE)", "Builder of Great Ziggurat / Oldest Law Code", ["Code of Ur-Nammu", "Sumerian King List"], "Founded Ur III and issued history's oldest surviving law code — the exact historical era of Ur of the Chaldees before Terah & Abraham's migration (Gen 11:31)!", ["Ur of the Chaldees Horizon"], major=True),
        N("mes_shulgi", "Shulgi (son of Ur-Nammu)", "mesopotamian", 9, "c. 2094-2047 BCE", "2nd King of Ur III", ["Sumerian King List", "Shulgi Hymns"], "Son of Ur-Nammu; reigned 48 years, standardized weights, measures, and scribal academies."),
        N("mes_amarsin", "Amar-Sin (son of Shulgi)", "mesopotamian", 9, "c. 2046-2038 BCE", "3rd King of Ur III", ["Sumerian King List"], "Son of Shulgi."),
        N("mes_shusin", "Shu-Sin (brother/son of Amar-Sin)", "mesopotamian", 9, "c. 2037-2029 BCE", "4th King of Ur III", ["Sumerian King List"], "Built the Martu Wall to hold back western Amorite tribes."),
        N("mes_ibbisin", "Ibbi-Sin (Last King of Ur III)", "mesopotamian", 9, "c. 2028-2004 BCE", "5th King of Ur III (Fall of Ur to Elam)", ["Lament for Ur", "Sumerian King List"], "Ur fell to Elamite and Shimashki invaders in 2004 BCE — matching the historical backdrop of Terah & Abraham leaving Ur!"),
        N("mes_sumuabum", "Sumu-abum → Sumu-la-El → Sin-Muballit (Early Babylon)", "mesopotamian", 10, "Old Babylonian Dynasty (c. 1894-1793 BCE)", "Amorite Founders of Babylon", ["Babylonian King List"], "Amorite chieftains who established the First Dynasty of Babylon: Sumu-abum -> Sumu-la-El -> Sabium -> Apil-Sin -> Sin-Muballit (father of Hammurabi)."),
        N("mes_hammurabi", "Hammurabi of Babylon (→ Samsu-iluna)", "mesopotamian", 10, "Old Babylonian Empire (c. 1792-1750 BCE)", "Amorite Lawgiver King of Babylon (Babel)", ["Code of Hammurabi", "Babylonian King List"], "6th king of the Amorite Dynasty of Babylon; unified Mesopotamia and issued the Code of Hammurabi. Father of Samsu-iluna.", ["Amraphel? (Traditional comparison)"], major=True),
        N("mes_assyria_kings", "Tudiya → Ushpia → Shamshi-Adad I → Tukulti-Ninurta I → Ashurbanipal", "mesopotamian", 10, "Assyrian King List (c. 2100-627 BCE)", "Kings of Assyria (Biblical Asshur / Nineveh)", ["Assyrian King List", "Library of Ashurbanipal"], "Begins with '17 Kings Who Lived in Tents' (Tudiya -> Ushpia) and leads to Tukulti-Ninurta I (often cited as a historical prototype for Nimrod!), Sennacherib, and Ashurbanipal (whose library preserved Gilgamesh & Enuma Elish!).", ["Asshur (Gen 10:11, 22)", "Tukulti-Ninurta I <-> Nimrod"], major=True),
    ]
    edges += [
        E("mes_lugalkitun", "mes_mesannepada", "expansion", "Kingship passes from Uruk I to Ur I (SKL)"),
        E("mes_mesannepada", "mes_meshkiangnanna", "direct", "Son (SKL)"),
        E("mes_meshkiangnanna", "mes_sargon", "expansion", "Sumerian King List succession to Akkad"),
        E("mes_sargon", "mes_enheduanna", "direct", "Daughter of Sargon (Disk of Enheduanna)"),
        E("mes_sargon", "mes_rimush", "direct", "Son of Sargon (SKL)"),
        E("mes_sargon", "mes_manishtushu", "direct", "Son of Sargon (SKL)"),
        E("mes_manishtushu", "mes_naramsin", "direct", "Son of Manishtushu (SKL)"),
        E("mes_naramsin", "mes_sharkalisharri", "direct", "Son of Naram-Sin (SKL)"),
        E("mes_sharkalisharri", "mes_urnammu", "expansion", "Ur III restores Sumer after Gutian interlude (SKL)"),
        E("mes_urnammu", "mes_shulgi", "direct", "Son (SKL)"),
        E("mes_shulgi", "mes_amarsin", "direct", "Son (SKL)"),
        E("mes_amarsin", "mes_shusin", "direct", "Brother/Son (SKL)"),
        E("mes_shusin", "mes_ibbisin", "direct", "Son (SKL)"),
        E("mes_ibbisin", "bib_terah", "cognate", "Fall of Ur III (c. 2004 BCE) = historical horizon of Terah & Abraham leaving Ur of the Chaldees (Gen 11:31)"),
        E("mes_ibbisin", "mes_sumuabum", "expansion", "Fall of Ur III gives rise to Amorite Dynasty of Babylon"),
        E("mes_sumuabum", "mes_hammurabi", "direct", "Sin-Muballit -> Hammurabi (Babylonian King List)"),
        E("bib_amorite", "mes_sumuabum", "cognate", "First Dynasty of Babylon was ethnically Amorite (Amurru)"),
        E("bib_nimrod", "mes_sargon", "cognate", "Gen 10:10 explicitly names Accad (Akkad) & Nineveh"),
        E("bib_nimrod", "mes_assyria_kings", "parallel", "Assyriologists compare Nimrod to Tukulti-Ninurta I, conqueror of Babylon"),
        E("bib_asshur", "mes_assyria_kings", "cognate", "Biblical Asshur = historical Assyria (Ashur & Nineveh)"),
        E("bib_moses", "mes_sargon", "parallel", "Reed basket sealed with bitumen placed in river (Exod 2 <-> Sargon Birth Legend)"),
    ]

    return {"module": "05_mesopotamia", "title": "Exhaustive Mesopotamian Genealogy (Enuma Elish, All 10 Antediluvian Kings, All Kish I, All Uruk I, Akkad, Ur III, Babylon & Assyria)", "nodes": nodes, "edges": edges}


def build_module_06_iranian_zoroastrian():
    nodes, edges = [], []

    # 1. Primordial Creation & Bundahishn Ch. 14 Table of Nations (Every named progenitor!)
    nodes += [
        N("ir_gayomart", "Gayomart (Gaya Maretan / Keyumars)", "iranian", 1, "Primordial Creation (Avesta / Bundahishn 14)",
          "First Mortal Human & First Pishdadian King", ["Avesta (Yasht 13.87)", "Bundahishn Ch. 14", "Shahnameh"],
          "Created by Ahura Mazda ('Mortal Life'). From his seed purified in the earth grew a rhubarb plant splitting into Mashya and Mashyana.",
          ["Keyumars", "Gaya Maretan"], major=True),
        N("ir_mashya_mashyana", "Mashya & Mashyana", "iranian", 2, "Primordial Gen 2 (Bundahishn 14)",
          "First Human Couple (7 Pairs of Twins)", ["Bundahishn Ch. 14"],
          "Twin first man and woman who bore 7 pairs of twins, including Siamak & Nashak (ancestors of Iran) and Fravak & Fravakain (ancestors of all 15 human races!).",
          ["Mahrya & Mahryana"], major=True),
        N("ir_fravak", "Fravak & Fravakain (Zoroastrian Table of Nations)", "iranian", 3, "Bundahishn Ch. 14 Ethnogenesis",
          "Progenitors of the 15 Races Across 7 Climes", ["Bundahishn Ch. 14:36-39"],
          "Bundahishn Ch. 14 traces 15 distinct human nations across the 7 climes (karshvars) to Fravak & Fravakain — including Iranians (Hoshang), Arabs (Taz), Mazandaran, India, Turan, China (Chin), and the West (Rum)!",
          ["15 Races of 7 Climes"], major=True),
    ]
    add_children(nodes, edges, "ir_fravak", "iranian", 4, "Bundahishn Ch. 14 (15 Races / Climes)", [
        ("ir_taz", "Taz & Tazag (Arabs / Taziks)", {"major": True, "sources": ["Bundahishn Ch. 14, 35"], "notes": "Son of Fravak; eponym of the Arabian peoples (Middle Persian Tazig) and ancestor of Merdas -> Zahhak!"}),
        ("ir_bund_mazandaran", "Mazandarani (Caspian Lineage)", {"sources": ["Bundahishn Ch. 14"], "notes": "One of the races descended from Fravak in Bundahishn Ch. 14."}),
        ("ir_bund_hindug", "Hindug (Indians in Bundahishn)", {"sources": ["Bundahishn Ch. 14"], "notes": "Branch of humanity settling India from Fravak's 15 pairs."}),
        ("ir_bund_chin", "Chin (China in Bundahishn)", {"sources": ["Bundahishn Ch. 14"], "notes": "Branch of humanity settling East Asia/China in Zoroastrian ethnography."}),
        ("ir_bund_rum", "Arum / Rum (Western Peoples)", {"sources": ["Bundahishn Ch. 14"], "notes": "Branch settling the western Mediterranean/Anatolian clime."}),
    ], default_edge="direct", default_sources=["Bundahishn Ch. 14"])

    nodes += [
        N("ir_merdas", "Merdas (Arabian King, desc. of Taz)", "iranian", 4, "Pishdadian Era", "Father of Zahhak", ["Bundahishn 35", "Shahnameh"], "Pious Arabian king descended from Taz, slain by his own son Zahhak under Ahriman's deception."),
        N("ir_zahhak", "Zahhak (Azi Dahaka)", "iranian", 4, "Pishdadian Interregnum", "Dragon Usurper King of Babylon & Iran", ["Avesta (Yasht 5, 9)", "Bundahishn 35", "Shahnameh"], "Son of Merdas; overthrows Jamshid and rules 1,000 years from Bawri (Babylon!) before being bound on Mt. Damavand by Fereydun. Ancestor of Mehrab Kaboli -> Rudabeh (mother of Rostam!).", ["Azi Dahaka", "Bivar-asp"], major=True),
    ]
    edges += [
        E("hub_primordial", "ir_gayomart", "parallel", "First mortal human created by Ahura Mazda"),
        E("ir_gayomart", "ir_mashya_mashyana", "direct", "Rhubarb plant from Gayomart's seed -> Mashya & Mashyana (Bundahishn 14)"),
        E("ir_mashya_mashyana", "ir_fravak", "direct", "Twin offspring -> Fravak & Fravakain (Bundahishn 14)"),
        E("ir_taz", "ir_merdas", "direct", "Descendant of Taz (Bundahishn 35 / Shahnameh)"),
        E("ir_merdas", "ir_zahhak", "direct", "Son (Shahnameh)"),
        E("hub_world_division", "ir_fravak", "parallel", "Bundahishn Ch. 14: 15 Races across 7 Climes"),
        E("bib_noah", "ir_gayomart", "syncretic", "al-Tabari & medieval chronicles equate Gayomart with Adam or Noah's kin"),
        E("ir_taz", "bib_joktan", "parallel", "Bundahishn's Taz (Arabia) <-> Arabian Qahtan/Ishmael ethnography"),
        E("ir_bund_hindug", "ved_vaivasvata_manu", "parallel", "Zoroastrian Bundahishn ethnographic link to India"),
        E("ir_bund_chin", "chn_huangdi", "parallel", "Zoroastrian Bundahishn ethnographic link to China (Chin)"),
    ]

    # 2. Full Pishdadian Dynasty (Every Individual!)
    nodes += [
        N("ir_siamak", "Siamak & Nashak", "iranian", 2, "Pishdadian Gen 2", "Son of Keyumars / Mashya", ["Bundahishn 14, 35", "Shahnameh"], "Slain by the Black Div; avenged by his son Hushang."),
        N("ir_hushang", "Hushang (Haoshyangha) & Guzak", "iranian", 3, "Pishdadian King 2", "Discoverer of Fire & Iron", ["Avesta (Yasht 5, 19)", "Bundahishn 35", "Shahnameh"], "Founder of the Pishdadian ('First Lawgivers') dynasty; establishes Sadeh upon discovering fire.", major=True),
        N("ir_tahmuras", "Tahmuras (Takhma Urupi)", "iranian", 3, "Pishdadian King 3 ('Binder of Demons')", "Teacher of 30 Scripts & Weaving", ["Avesta (Yasht 15, 19)", "Shahnameh"], "Binds Ahriman for 30 years and learns 30 scripts from captive demons to teach humanity."),
        N("ir_vivanghant", "Vivanghant (Vivanhao)", "iranian", 3, "Avestan Antediluvian Horizon", "Exact Cognate of Vedic Vivasvan", ["Avesta (Yasna 9.4, Vendidad 2)", "Bundahishn 35"], "EXACT Proto-Indo-Iranian linguistic & genealogical cognate of Vedic Vivasvan (Surya)! Strongest verified prehistoric ancestral bridge between Iran and India.", ["Vivanhao", "Cognate: Vedic Vivasvan"], major=True),
        N("ir_yima", "Yima Khshaeta (Jamshid) & Yimak", "iranian", 4, "Golden Age / Cataclysm Horizon", "4th Pishdadian King & Builder of the Vara", ["Avesta (Vendidad 2, Yasna 9)", "Bundahishn 35", "Shahnameh"], "Son of Vivanghant — exact cognate of Vedic Yama! Builds the subterranean Vara preserving pairs of humans, animals, and seeds against the great cosmic winter/meltwater cataclysm.", ["Jamshid", "Cognate: Vedic Yama", "Twin: Yimak"], major=True),
        N("ir_shahrnaz_arnavaz", "Shahrnaz & Arnavaz (Daughters of Jamshid)", "iranian", 4, "Pishdadian Princesses", "Wives of Fereydun / Mothers of Salm, Tur & Iraj", ["Shahnameh"], "Daughters/sisters of Jamshid rescued from Zahhak by Fereydun; Shahrnaz bears Salm & Tur, and Arnavaz bears Iraj!"),
        N("ir_athwya", "Athwya (Abtin) & Faranak", "iranian", 4, "Pishdadian Descent from Jamshid", "Father of Fereydun / Exact Cognate of Vedic Aptya", ["Avesta (Yasna 9.7)", "Bundahishn 35", "Shahnameh"], "Descendant of Jamshid (via Pur-Tora/Sog-Tora in Bundahishn 35); EXACT Proto-Indo-Iranian cognate of Vedic Aptya (father of Trita Aptya)!", ["Abtin", "Cognate: Vedic Aptya"], major=True),
        N("ir_fereydun", "Fereydun (Thraetaona)", "iranian", 5, "Post-Cataclysm Pishdadian King 6", "Binder of Zahhak & Divider of the World Into Three", ["Avesta (Yasht 5, 19)", "Bundahishn 35", "Shahnameh"], "Son of Athwya (Abtin) & Faranak — cognate of Vedic Trita! Weds Shahrnaz & Arnavaz, binds Zahhak on Mt. Damavand, and divides the world among Salm, Tur, and Iraj.", ["Thraetaona", "Faridun", "Cognate: Vedic Trita"], major=True),
    ]
    edges += [
        E("ir_mashya_mashyana", "ir_siamak", "direct", "Siamak & Nashak (Bundahishn 14; son of Keyumars in Shahnameh)"),
        E("ir_siamak", "ir_hushang", "direct", "Son (Shahnameh / Bundahishn 35)"),
        E("ir_hushang", "ir_tahmuras", "direct", "Son/Descendant (Shahnameh / Bundahishn)"),
        E("ir_tahmuras", "ir_vivanghant", "expansion", "Pishdadian lineage to Vivanghant (Bundahishn 35)"),
        E("ir_vivanghant", "ir_yima", "direct", "Son (Avesta Yasna 9.4)"),
        E("ir_yima", "ir_shahrnaz_arnavaz", "direct", "Daughters/sisters of Jamshid (Shahnameh)"),
        E("ir_shahrnaz_arnavaz", "ir_fereydun", "direct", "Wives of Fereydun (mothers of Salm, Tur & Iraj)"),
        E("ir_yima", "ir_athwya", "direct", "Descendant of Jamshid via Pur-Tora -> Abtin/Athwya (Bundahishn 35)"),
        E("ir_athwya", "ir_fereydun", "direct", "Son (Avesta Yasna 9.7; Shahnameh)"),
        E("hub_flood", "ir_yima", "parallel", "Vara enclosure against cataclysmic winter/meltwater"),
        E("hub_world_division", "ir_fereydun", "parallel", "Tripartite division of Eurasia: Salm, Tur, Iraj"),
    ]

    # 3. Fereydun's 3 Sons + Turanian House + Pishdadian Line + Sistan House (Every Person Individualized!)
    nodes += [
        N("ir_salm", "Salm (Ruler of the West / Rum)", "iranian", 6, "Tripartite Division", "1st Son of Fereydun (West / Anatolia / Europe)", ["Bundahishn 35", "Shahnameh"], "Eldest son of Fereydun & Shahrnaz; receives Rum/West.", major=True),
        N("ir_tur", "Tur (Ruler of Turan / Central Asia)", "iranian", 6, "Tripartite Division", "2nd Son of Fereydun (Turan / Steppe)", ["Bundahishn 35", "Shahnameh"], "Second son of Fereydun & Shahrnaz; receives Central Asia & Steppe.", major=True),
        N("ir_zadsham", "Zadsham (son of Tur)", "iranian", 6, "Turanian Line", "Son of Tur", ["Bundahishn 35", "Shahnameh"], "Father of Pashang."),
        N("ir_pashang", "Pashang (King of Turan)", "iranian", 7, "Turanian Line", "Father of Afrasiab, Garsivaz & Aghriras", ["Bundahishn 35", "Shahnameh"], "Son of Zadsham; launches the great Iran-Turan wars."),
        N("ir_afrasiab", "Afrasiab (Franrasyan)", "iranian", 8, "Turanian Emperor", "Great King of Turan / Grandfather of Kay Khosrow", ["Avesta (Yasht 5, 19)", "Bundahishn 35", "Shahnameh"], "Son of Pashang; legendary rival of Iran whose daughter Farangis marries Siyavash, uniting Iran and Turan in Kay Khosrow!", ["Franrasyan"], major=True),
        N("ir_garsivaz_aghriras", "Garsivaz & Aghriras (Brothers of Afrasiab)", "iranian", 8, "Turanian Princes", "Sons of Pashang", ["Shahnameh"], "Aghriras (noble brother who saved Iranian captives) and Garsivaz (instigator of Siyavash's murder)."),
        N("ir_farangis", "Farangis (Turanian Princess)", "iranian", 9, "Daughter of Afrasiab", "Wife of Siyavash / Mother of Kay Khosrow", ["Shahnameh"], "Daughter of Afrasiab; marries Iranian prince Siyavash and gives birth to Kay Khosrow, uniting Turan and Iran!"),

        N("ir_iraj", "Iraj (Ruler of Iran / Eranshahr)", "iranian", 6, "Tripartite Division", "3rd Son of Fereydun / Eponym of Iran", ["Bundahishn 35", "Shahnameh"], "Youngest son of Fereydun & Arnavaz; receives Iran. Slain by Salm & Tur.", major=True),
        N("ir_mahafarid", "Mah-Afarid (Daughter of Iraj)", "iranian", 6, "House of Iraj", "Grandmother/Mother of Manuchehr", ["Shahnameh"], "Daughter of Iraj wed to Pashang (nephew of Fereydun), preserving Iraj's bloodline into Manuchehr."),
        N("ir_manuchehr", "Manuchehr (Manushchihr)", "iranian", 7, "Pishdadian King 7", "Avenger of Iraj / Ancestor of Kayanians & Zoroaster", ["Avesta (Yasht 13)", "Bundahishn 35", "Shahnameh"], "Avenges Iraj against Salm & Tur; defines Iran's border via Arash the Archer's legendary shot!", major=True),
        N("ir_nowzar", "Nowzar (son of Manuchehr)", "iranian", 8, "Pishdadian King 8", "Father of Heroes Tus & Gostaham", ["Shahnameh"], "Slain by Afrasiab; his sons Tus and Gostaham become leading Iranian generals."),
        N("ir_tus_gostaham", "Tus & Gostaham (Sons of Nowzar)", "iranian", 8, "Pishdadian Princes", "Iranian Commanders", ["Shahnameh"], "Sons of Nowzar who serve the Kayanian kings."),
        N("ir_zav", "Zav (Uzava, son of Tahmasp)", "iranian", 8, "Pishdadian King 9", "Restorer of Iran's Canals", ["Bundahishn 35", "Shahnameh"], "Descendant of Manuchehr who restores agriculture after Afrasiab's drought."),
        N("ir_garshasp", "Garshasp (Keresaspa — Dragon-Slayer)", "iranian", 8, "Final Pishdadian / Avestan Hero", "Slayer of Azi Sruvara", ["Avesta (Yasna 9.10)", "Bundahishn 35", "Shahnameh"], "Avestan champion and final Pishdadian ruler; ancestor of the Sistan paladins (Nariman -> Sam -> Zal -> Rostam)."),

        # Sistan Heroic House (Individualized!)
        N("ir_nariman", "Nariman (son of Garshasp)", "iranian", 8, "Sistan Heroic Line", "Father of Sam", ["Shahnameh", "Garshaspnameh"], "Warrior ancestor of the House of Sistan."),
        N("ir_sam", "Sam (Paladin of Iran)", "iranian", 8, "Sistan Heroic Line", "Father of Zal", ["Shahnameh"], "Champion under Manuchehr; initially abandoned his white-haired infant Zal on Mt. Alborz before reclaiming him from the Simurgh."),
        N("ir_zal", "Zal (Dastan — Raised by the Simurgh)", "iranian", 8, "Sistan Heroic Line", "Father of Rostam", ["Shahnameh"], "White-haired sage-warrior raised by the mythical Simurgh; weds Rudabeh of Kabul.", major=True),
        N("ir_mehrab", "Mehrab Kaboli (King of Kabul)", "iranian", 7, "Kabul / Indo-Iranian Frontier", "Descendant of Zahhak / Father of Rudabeh", ["Shahnameh"], "Ruler of Kabul descended from Zahhak; father of Rudabeh."),
        N("ir_rudabeh", "Rudabeh (Princess of Kabul)", "iranian", 8, "Kabul / Sistan", "Wife of Zal / Mother of Rostam", ["Shahnameh"], "Her union with Zal bridges Kabul/Zahhak's line with Iran's greatest heroic house!"),
        N("ir_rostam", "Rostam (Champion of Iran)", "iranian", 9, "Sistan Heroic Era", "Greatest Hero of the Shahnameh", ["Shahnameh"], "Son of Zal & Rudabeh; serves the Kayanian kings for centuries. Marries Tahmineh of Samangan (Turan) -> Sohrab, plus Faramarz and warrior daughter Banu Goshasp.", major=True),
        N("ir_shaghad", "Shaghad (Half-Brother of Rostam)", "iranian", 9, "Sistan / Kabul", "Son of Zal", ["Shahnameh"], "Rostam's treacherous half-brother who conspires with the King of Kabul."),
        N("ir_sohrab", "Sohrab (son of Rostam & Tahmineh)", "iranian", 10, "Shahnameh", "Son of Rostam & Turanian Princess Tahmineh", ["Shahnameh"], "Born in Samangan (Turan); tragically slain in single combat by his father Rostam before they recognize one another."),
        N("ir_faramarz", "Faramarz & Banu Goshasp (Children of Rostam)", "iranian", 10, "Shahnameh / Faramarznameh", "Warrior Children of Rostam", ["Shahnameh", "Banu Goshaspnameh"], "Faramarz leads expeditions into India and avenges Rostam; Banu Goshasp is a celebrated Iranian warrior heroine."),
    ]
    edges += [
        E("ir_fereydun", "ir_salm", "direct", "1st son (West / Rum)"),
        E("ir_fereydun", "ir_tur", "direct", "2nd son (Turan / Central Asia)"),
        E("ir_fereydun", "ir_iraj", "direct", "3rd son (Iran / Eranshahr)"),
        E("ir_tur", "ir_zadsham", "direct", "Son (Bundahishn 35)"),
        E("ir_zadsham", "ir_pashang", "direct", "Son (Bundahishn 35)"),
        E("ir_pashang", "ir_afrasiab", "direct", "Son (Shahnameh)"),
        E("ir_pashang", "ir_garsivaz_aghriras", "direct", "Sons (Shahnameh)"),
        E("ir_afrasiab", "ir_farangis", "direct", "Daughter (Shahnameh)"),
        E("ir_iraj", "ir_mahafarid", "direct", "Daughter (Shahnameh)"),
        E("ir_mahafarid", "ir_manuchehr", "direct", "Descendant of Iraj -> Manuchehr (Shahnameh)"),
        E("ir_manuchehr", "ir_nowzar", "direct", "Son (Shahnameh)"),
        E("ir_nowzar", "ir_tus_gostaham", "direct", "Sons (Shahnameh)"),
        E("ir_manuchehr", "ir_zav", "expansion", "Descendant of Manuchehr (Bundahishn 35)"),
        E("ir_zav", "ir_garshasp", "direct", "Son/Successor (Shahnameh)"),
        E("ir_garshasp", "ir_nariman", "direct", "Sistan heroic descent"),
        E("ir_nariman", "ir_sam", "direct", "Son (Shahnameh)"),
        E("ir_sam", "ir_zal", "direct", "Son (Shahnameh)"),
        E("ir_zahhak", "ir_mehrab", "direct", "Descendant ruling Kabul (Shahnameh)"),
        E("ir_mehrab", "ir_rudabeh", "direct", "Daughter (Shahnameh)"),
        E("ir_zal", "ir_rostam", "direct", "Son via Rudabeh (Shahnameh)"),
        E("ir_rudabeh", "ir_rostam", "direct", "Mother of Rostam"),
        E("ir_zal", "ir_shaghad", "direct", "Son (Shahnameh)"),
        E("ir_rostam", "ir_sohrab", "direct", "Son via Tahmineh of Samangan (Turan)"),
        E("ir_rostam", "ir_faramarz", "direct", "Children of Rostam"),
    ]

    # 4. Full Kayanian Dynasty + Prophet Zarathustra's Complete Family (Individualized!)
    nodes += [
        N("ir_kay_kavad", "Kay Kavad (Kavi Kavata)", "iranian", 8, "Founder of Kayanian Dynasty", "1st Kayanian King", ["Avesta (Yasht 19)", "Bundahishn 35", "Shahnameh"], "Descendant of Manuchehr brought from Mt. Alborz by Rostam; father of Kay Kavus and Kay Apiveh.", major=True),
        N("ir_kay_apiveh", "Kay Apiveh → Kay Arash & Kay Pishin", "iranian", 8, "Kayanian Branch", "Sons of Kay Kavad", ["Bundahishn 35", "Avesta (Yasht 19)"], "Branch of Kay Kavad leading to Kay Lohrasp and Kay Goshtasp (patron of Zoroaster)."),
        N("ir_kay_kavus", "Kay Kavus (Kavi Usan)", "iranian", 9, "2nd Kayanian King", "Cognate: Vedic Kavi Ushanas", ["Avesta (Yasht 14, 19)", "Bundahishn 35", "Shahnameh"], "Linguistic cognate of Vedic sage Kavi Ushanas! Father of Prince Siyavash.", ["Kavi Usan", "Cognate: Vedic Kavi Ushanas"], major=True),
        N("ir_siyavash", "Siyavash (Syavarshan)", "iranian", 9, "Martyred Kayanian Prince", "Son of Kay Kavus / Husband of Farangis", ["Avesta (Yasht 19)", "Shahnameh"], "Passes through fire unscathed; weds Afrasiab's daughter Farangis in Turan; father of Kay Khosrow and Farud."),
        N("ir_farud", "Farud (son of Siyavash & Jarireh)", "iranian", 10, "Shahnameh", "Half-Brother of Kay Khosrow", ["Shahnameh"], "Son of Siyavash and Jarireh (daughter of Turanian sage Piran Viseh)."),
        N("ir_kay_khosrow", "Kay Khosrow (Kavi Husravah)", "iranian", 10, "3rd Kayanian King (Unifier of Iran & Turan)", "Ideal Sacred King of Avesta & Shahnameh", ["Avesta (Yasht 9, 19)", "Bundahishn 35", "Shahnameh"], "Son of Siyavash (Iran) & Farangis (Turan); unites both houses, defeats Afrasiab, and passes the crown to Kay Lohrasp.", major=True),
        N("ir_kay_lohrasp", "Kay Lohrasp (Aurvat-aspa)", "iranian", 10, "4th Kayanian King", "Father of Kay Goshtasp", ["Avesta", "Bundahishn 35", "Shahnameh"], "Descended from Kay Apiveh -> Kay Pishin -> Kay Lohrasp; builds the fire temple at Balkh."),
        N("ir_kay_goshtasp", "Kay Goshtasp (Kavi Vishtaspa)", "iranian", 10, "5th Kayanian King", "Royal Patron of Prophet Zarathustra", ["Avesta (Yasna 46, 51)", "Bundahishn 35", "Shahnameh"], "Champions Prophet Zarathustra's religion; father of hero Esfandiyar and brother Zarir.", ["Kavi Vishtaspa"], major=True),
        N("ir_esfandiyar", "Esfandiyar (Spento-data)", "iranian", 11, "Kayanian Champion", "Son of Kay Goshtasp / Father of Bahman", ["Avesta", "Shahnameh"], "Bronze-bodied champion of Zoroastrianism slain by Rostam's tamarisk arrow; father of Kay Bahman."),
        N("ir_bahman", "Kay Bahman → Queen Homai → Darab → Dara", "iranian", 11, "Late Kayanian Kings", "Bridge to Historical Artaxerxes & Darius III", ["Bundahishn 35", "Shahnameh"], "Kay Bahman (equated in Persian lore with Artaxerxes Longimanus) -> Queen Homai -> Darab -> Dara (Darius III, rival of Alexander!)."),

        # Zarathustra's Full Family (Bundahishn Ch. 35!)
        N("ir_pourushaspa", "Spitama → Haechataspa → Pourushaspa & Dughdova", "iranian", 9, "Bundahishn Ch. 35:50-55", "Parents & Clan of Zarathustra", ["Avesta (Yasna 9.13)", "Bundahishn Ch. 35"], "Bundahishn traces Spitama (descended from Manuchehr) -> Haechataspa -> Pourushaspa, who marries Dughdova to birth Zarathustra."),
        N("ir_zoroaster", "Prophet Zarathustra (Zoroaster) & Hvovi", "iranian", 10, "c. 1500-1000 BCE (or 6th c. BCE trad.)", "Founder of Zoroastrianism", ["Avesta (Gathas)", "Bundahishn Ch. 35:50-56"], "Author of the Gathas; weds Hvovi (of the Hvova clan, kin of Frashaoshtra & Jamaspa) and fathers 3 sons and 3 daughters.", ["Zoroaster", "Zartosht"], major=True),
    ]
    add_children(nodes, edges, "ir_zoroaster", "iranian", 11, "Children of Zarathustra (Bundahishn 35:56)", [
        ("ir_zor_isatvastra", "Isatvastra (son of Zarathustra)", {"sources": ["Bundahishn 35:56", "Yasht 13.98"], "notes": "Eldest son of Zarathustra; head of the priestly estate (Athornan)."}),
        ("ir_zor_urvatatnara", "Urvatatnara (son of Zarathustra)", {"sources": ["Bundahishn 35:56"], "notes": "Son of Zarathustra; head of the pastoral/agricultural estate."}),
        ("ir_zor_hvarechithra", "Hvarechithra (son of Zarathustra)", {"sources": ["Bundahishn 35:56"], "notes": "Son of Zarathustra; head of the warrior estate."}),
        ("ir_zor_freni", "Freni (dau. of Zarathustra)", {"sources": ["Bundahishn 35:56", "Yasht 13.139"], "notes": "1st daughter of Zarathustra."}),
        ("ir_zor_thriti", "Thriti (dau. of Zarathustra)", {"sources": ["Bundahishn 35:56", "Yasht 13.139"], "notes": "2nd daughter of Zarathustra."}),
        ("ir_zor_pouruchista", "Pouruchista (+ Jamaspa)", {"sources": ["Avesta (Yasna 53)", "Bundahishn 35:56"], "notes": "Youngest daughter of Zarathustra celebrated in Gatha Yasna 53; marries sage Jamaspa (counselor of King Vishtaspa)."}),
    ], default_edge="direct", default_sources=["Bundahishn Ch. 35:56"])

    edges += [
        E("ir_manuchehr", "ir_kay_kavad", "expansion", "Descendant of Manuchehr (Bundahishn 35)"),
        E("ir_kay_kavad", "ir_kay_apiveh", "direct", "Son (Bundahishn 35)"),
        E("ir_kay_kavad", "ir_kay_kavus", "direct", "Son (Shahnameh / Bundahishn)"),
        E("ir_kay_kavus", "ir_siyavash", "direct", "Son (Shahnameh)"),
        E("ir_siyavash", "ir_farud", "direct", "Son via Jarireh (Shahnameh)"),
        E("ir_siyavash", "ir_kay_khosrow", "direct", "Son via Farangis (Shahnameh)"),
        E("ir_farangis", "ir_kay_khosrow", "direct", "Mother of Kay Khosrow (uniting Turan & Iran!)"),
        E("ir_kay_apiveh", "ir_kay_lohrasp", "direct", "Kay Apiveh -> Kay Pishin -> Kay Lohrasp (Bundahishn 35)"),
        E("ir_kay_khosrow", "ir_kay_lohrasp", "expansion", "Kay Khosrow passes throne to Kay Lohrasp"),
        E("ir_kay_lohrasp", "ir_kay_goshtasp", "direct", "Son (Shahnameh / Bundahishn)"),
        E("ir_kay_goshtasp", "ir_esfandiyar", "direct", "Son (Shahnameh)"),
        E("ir_esfandiyar", "ir_bahman", "direct", "Son Bahman -> Homai -> Darab -> Dara"),
        E("ir_manuchehr", "ir_pourushaspa", "expansion", "Bundahishn 35: Manuchehr -> ... -> Spitama -> Pourushaspa"),
        E("ir_pourushaspa", "ir_zoroaster", "direct", "Pourushaspa + Dughdova -> Zarathustra (Yasna 9.13)"),
        E("ir_kay_goshtasp", "ir_zoroaster", "expansion", "Kavi Vishtaspa (Goshtasp) champions Zarathustra"),
    ]

    # 5. Historical Median & Achaemenid Persian Dynasties (Individualized!)
    nodes += [
        N("ir_deioces", "Deioces → Phraortes (Early Medes)", "iranian", 8, "c. 700-625 BCE", "Founders of the Median Kingdom (Biblical Madai)", ["Herodotus I.96-102"], "Deioces (Dayukku) unifies the Median tribes at Ecbatana; followed by his son Phraortes."),
        N("ir_cyaxares", "Cyaxares (Uvakhshatra) → Astyages", "iranian", 9, "c. 625-550 BCE", "Conquerors of Nineveh / Kings of Media", ["Herodotus I", "Babylonian Chronicle"], "Cyaxares destroys Nineveh (612 BCE) in alliance with Babylon; his son Astyages fathers Princess Mandane (mother of Cyrus the Great!).", ["Madai (Gen 10:2)"], major=True),
        N("ir_mandane", "Mandane (Median Princess)", "iranian", 9, "c. 600 BCE", "Daughter of Astyages / Mother of Cyrus the Great", ["Herodotus I.107"], "Unites the Median (Madai) and Persian/Elamite (Anshan) royal houses!"),
        N("ir_achaemenes", "Achaemenes (Hakhamanish) → Teispes", "iranian", 8, "c. 700-640 BCE", "Founders of Achaemenid Dynasty (Anshan in Elam)", ["Behistun Inscription", "Cyrus Cylinder"], "Achaemenes -> Teispes (Chishpish), who divides his kingdom between Cyrus I (Anshan/Elam) and Ariaramnes (Persia)."),
        N("ir_cambyses1", "Cyrus I → Cambyses I (Kings of Anshan)", "iranian", 9, "c. 640-559 BCE", "Kings of Anshan (Elam) / Father of Cyrus the Great", ["Cyrus Cylinder"], "Cambyses I marries Median princess Mandane and fathers Cyrus the Great."),
        N("ir_cyrus", "Cyrus the Great (Koresh)", "iranian", 10, "Achaemenid Empire (559-530 BCE)", "Founder of Persian Empire / Liberator of Judah", ["Cyrus Cylinder", "Ezra 1:1-4", "Isaiah 45:1", "Herodotus"], "Son of Cambyses I (Anshan/Elam) & Mandane (Media/Madai). Conquers Babylon (539 BCE) and decrees the return of Judean exiles to rebuild Jerusalem! Father of Cambyses II, Bardiya, and Atossa.", ["Koresh (Hebrew)", "Kurush"], major=True),
        N("ir_cambyses2_atossa", "Cambyses II, Bardiya & Queen Atossa", "iranian", 10, "530-475 BCE", "Children of Cyrus the Great", ["Behistun Inscription", "Herodotus III"], "Cambyses II conquers Egypt (525 BCE); Queen Atossa marries Darius I and becomes mother of Xerxes I (Ahasuerus)!"),
        N("ir_hystaspes", "Ariaramnes → Arsames → Hystaspes (Vishtaspa)", "iranian", 9, "c. 640-522 BCE", "Junior Achaemenid Branch", ["Behistun Inscription"], "Line from Teispes to Hystaspes, father of Darius I."),
        N("ir_darius1", "Darius I the Great (Darayavahush)", "iranian", 10, "522-486 BCE", "3rd Achaemenid Emperor (Ezra 4-6)", ["Behistun Inscription", "Ezra 6"], "Son of Hystaspes; marries Cyrus's daughter Atossa, uniting both Achaemenid lines, and confirms Cyrus's decree to complete the Second Temple in Jerusalem.", major=True),
        N("ir_xerxes1", "Xerxes I (Ahasuerus of Book of Esther)", "iranian", 11, "486-465 BCE", "4th Achaemenid Emperor", ["Persepolis Inscriptions", "Book of Esther", "Herodotus VII"], "Son of Darius I & Atossa; widely identified with King Ahasuerus (Achashverosh) in the Book of Esther!", ["Ahasuerus (Esther)", "Khshayarsha"], major=True),
        N("ir_artaxerxes1", "Artaxerxes I → Darius III", "iranian", 11, "465-330 BCE", "Patron of Ezra & Nehemiah → Final Achaemenid", ["Ezra 7", "Nehemiah 2"], "Son of Xerxes I; commissions Ezra and Nehemiah to rebuild Jerusalem; dynasty continues down to Darius III (Shahnameh's Dara)."),
    ]
    edges += [
        E("bib_madai", "ir_deioces", "cognate", "Biblical Madai (Gen 10:2) = Historical Medes (Old Persian Mada)"),
        E("ir_deioces", "ir_cyaxares", "direct", "Phraortes -> Cyaxares -> Astyages (Herodotus)"),
        E("ir_cyaxares", "ir_mandane", "direct", "Daughter of Astyages (Herodotus)"),
        E("bib_elam", "ir_achaemenes", "cognate", "Achaemenids ruled as Kings of Anshan in Elam (Gen 10:22)"),
        E("ir_iraj", "ir_achaemenes", "expansion", "Iranian royal continuity from Eranshahr to historical Persia"),
        E("ir_achaemenes", "ir_cambyses1", "direct", "Teispes -> Cyrus I -> Cambyses I (Cyrus Cylinder)"),
        E("ir_achaemenes", "ir_hystaspes", "direct", "Teispes -> Ariaramnes -> Arsames -> Hystaspes (Behistun)"),
        E("ir_cambyses1", "ir_cyrus", "direct", "Son (Cyrus Cylinder)"),
        E("ir_mandane", "ir_cyrus", "direct", "Mother of Cyrus (uniting Medes/Madai & Persia/Elam!)"),
        E("ir_cyrus", "ir_cambyses2_atossa", "direct", "Children of Cyrus the Great"),
        E("ir_hystaspes", "ir_darius1", "direct", "Son (Behistun Inscription)"),
        E("ir_cambyses2_atossa", "ir_darius1", "direct", "Queen Atossa marries Darius I (uniting both Achaemenid lines)"),
        E("ir_darius1", "ir_xerxes1", "direct", "Darius I + Atossa -> Xerxes I (Ahasuerus)"),
        E("ir_xerxes1", "ir_artaxerxes1", "direct", "Son Artaxerxes I -> ... -> Darius III"),
        E("ir_bahman", "ir_artaxerxes1", "cognate", "Shahnameh's Bahman/Darab/Dara preserves historical memory of Artaxerxes & Darius III"),
        E("jud_solomon", "ir_cyrus", "cognate", "Ezra 1: Cyrus King of Persia decrees return of Judah's Davidic exiles to Jerusalem"),
    ]

    return {"module": "06_iranian_zoroastrian", "title": "Exhaustive Iranian & Zoroastrian Genealogy (Avesta, Bundahishn Ch. 14 & 35, Shahnameh, Sistan, Zarathustra, Medes & Achaemenids)", "nodes": nodes, "edges": edges}


def build_module_07_asia_steppe():
    nodes, edges = [], []

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
        N("ved_trita_aptya", "Aptya → Trita Aptya & Kavi Ushanas", "vedic", 4, "Rigvedic Mythic Horizon",
          "Exact Proto-Indo-Iranian Cognates of Athwya/Thraetaona & Kavi Usan", ["Rigveda 1.105, 10.8, 10.99"],
          "Vedic dragon-slayer Trita son of Aptya is the exact linguistic cognate of Avestan Thraetaona (Fereydun) son of Athwya (Abtin), while sage Kavi Ushanas is the exact cognate of Iranian King Kavi Usan (Kay Kavus)!",
          ["Trita = Fereydun", "Aptya = Abtin", "Kavi Ushanas = Kay Kavus"]),
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
        E("ved_brahma_manu", "ved_trita_aptya", "expansion", "Rigvedic mythic heroes Trita Aptya & Kavi Ushanas"),
        E("ved_vaivasvata_manu", "ved_surya_vamsha", "direct", "Son Ikshvaku -> Solar Dynasty"),
        E("ved_vaivasvata_manu", "ved_yayati", "direct", "Via Ila + Budha -> Pururavas -> Yayati"),
        E("ved_brahma_manu", "ved_yayati", "direct", "Brahma -> Atri -> Soma -> Budha"),
        E("ved_puru", "ved_bharata_kuru", "direct", "Puru -> Bharata -> Kuru -> Pandavas"),
        E("ir_vivanghant", "ved_vivasvan", "cognate", "EXACT Proto-Indo-Iranian cognate: Vivanghant = Vivasvan"),
        E("ir_yima", "ved_yama", "cognate", "EXACT Proto-Indo-Iranian cognate: Yima = Yama"),
        E("ir_athwya", "ved_trita_aptya", "cognate", "EXACT Proto-Indo-Iranian cognate: Athwya/Thraetaona = Aptya/Trita"),
        E("ir_kay_kavus", "ved_trita_aptya", "cognate", "EXACT Proto-Indo-Iranian cognate: Kavi Usan (Kay Kavus) = Kavi Ushanas"),
        E("hub_flood", "ved_vaivasvata_manu", "parallel", "Ship towed by Matsya to Himalayas"),
        E("hub_world_division", "ved_yayati", "parallel", "Yayati's 5 Sons (Panchajana)"),
        E("bib_abraham", "ved_brahma_manu", "syncretic", "Folkloric/syncretic comparison of Abraham/Sarah <-> Brahma/Saraswati (non-cognate)"),
    ]

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

    return {"module": "07_asia_steppe", "title": "Vedic/Puranic India, China, Korea, Japan & Eurasian Steppe", "nodes": nodes, "edges": edges}


def main():
    MODULES_DIR.mkdir(parents=True, exist_ok=True)
    for old_name in ("04_near_east_egypt.json", "05_asia_steppe.json"):
        old_p = MODULES_DIR / old_name
        if old_p.exists():
            old_p.unlink()

    modules = [
        load_existing_module("01_antediluvian"),
        load_existing_module("02_table_of_nations"),
        load_existing_module("03_abraham_all_nations"),
        build_module_04_egypt_levant(),
        build_module_05_mesopotamia(),
        build_module_06_iranian_zoroastrian(),
        build_module_07_asia_steppe(),
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
            "title": "Ancient World Genealogy Atlas — Exhaustive Multi-Tradition Database (Phase 3)",
            "version": "3.0.0",
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
