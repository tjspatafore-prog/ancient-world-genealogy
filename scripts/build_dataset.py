"""
Modular Ancient World Genealogy Dataset Builder & Validator (Phase 6).

Compiles clean modular JSON files under data/modules/ into data/world_genealogy.json
for the interactive web explorer, ensuring zero broken links, full provenance tagging,
and exhaustive person-by-person accounting across 11 modules.
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
    "expansion": "Matriarchs, additional children, royal successions, or migrations supplied by extra-biblical or secondary chronicles (Book of Jasher, Jubilees, 1 Enoch, Manetho, Kebra Nagast, Sumerian King List, Bundahishn, Shahnameh, Shiji, Samguk Yusa, Kojiki, Puranas)",
    "cognate":   "Linguistically or historically attested cross-tradition identity/ethnonym bridge (e.g., Ion = Javan; Taharqa = Tirhakah; Merneptah Stele = Israel; Vedic Vivasvan/Yama/Aptya = Avestan Vivanghant/Yima/Athwya; Zeus = Dyaus Pitr; Madai = Medes)",
    "parallel":  "Independent structural/archetypal parallel across ancient corpora (Great Flood survivors, 7th sage, Imhotep/Joseph, Adapa/Adam, Sargon/Moses basket, tripartite world division)",
    "syncretic": "Ancient, Greco-Egyptian, or medieval chronicler identification bridging figures across cultures (e.g., Enoch = Thoth/Saurid; Moses = Osarseph/Musaeus; Noah = Osiris/Fuxi; Japheth = Oghuz Khagan; Zepho = King of Kittim/Rome)"
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


def build_module_07_vedic_india():
    nodes, edges = [], []

    # 1. Cosmic Creation, Dyaus Pitr, Saptarishis & Svayambhuva Manu (Vishnu Purana I, Bhagavata Purana III-IV)
    nodes += [
        N("ved_dyaus_prithvi", "Dyaus Pitr (Sky Father) & Prithvi (Earth Mother)", "vedic", 1, "Rigvedic Cosmogony (Rigveda 1.160)",
          "Proto-Indo-European Sky Father (Exact Cognate of Greek Zeus!)", ["Rigveda 1.160, 4.17"],
          "Vedic Sky-Father Dyaus Pitr is the EXACT linguistic cognate of Greek Zeus Pater and Roman Jupiter! Parents of Ushas (Dawn) and Indra in early Rigvedic hymns.",
          ["Cognate: Greek Zeus Pater / Jupiter"], major=True),
        N("ved_brahma_manu", "Brahma → Svayambhuva Manu & Shatarupa", "vedic", 1, "Satya Yuga / Puranic Creation",
          "Vedic Primordial Progenitors & Origin of Saptarishis", ["Manusmriti Ch. 1", "Vishnu Purana I.7", "Bhagavata Purana III.12"],
          "Brahma manifests Svayambhuva Manu and Shatarupa as the primordial human couple, and mind-borns the Saptarishis (Seven Great Sages: Marichi, Atri, Angiras, Pulastya, Pulaha, Kratu, Vashishta) plus Bhrigu and Daksha.",
          ["Svayambhuva Manu", "Shatarupa"], major=True),
        N("ved_priyavrata_rishabha", "Priyavrata → Nabhi → Rishabhanatha (1st Jain Tirthankara) → Bharata", "vedic", 2, "Satya Yuga (Bhagavata Purana V / Jain Tradition)",
          "Eldest Son of Svayambhuva Manu & Jain Progenitor", ["Bhagavata Purana Book V", "Jain Adi Purana"],
          "Priyavrata divides Earth into seven continents (Dvipas); his descendant Rishabhanatha (Adinatha) is the 1st Jain Tirthankara, whose son Chakravartin Bharata is one of the traditional eponyms of Bharatavarsha (India)!"),
        N("ved_uttanapada_dhruva", "Uttanapada → Dhruva (Pole Star) & Daksha (+ Prasuti)", "vedic", 2, "Satya Yuga (Vishnu Purana I.11-15)",
          "Svayambhuva Manu's Family & Prajapati Daksha", ["Vishnu Purana I.11-15", "Bhagavata Purana IV"],
          "Uttanapada fathers Prince Dhruva (the steadfast Pole Star); Svayambhuva Manu's daughter Prasuti marries Prajapati Daksha, father of Sati, Aditi, Diti, Danu, Kadru, and Vinata (and Devahuti + Kardama -> Sage Kapila!)."),
        N("ved_saptarishis_bhrigu", "Vashishta (→ Parashara), Pulastya (→ Ravana) & Bhrigu (→ Shukracharya)", "vedic", 2, "Vedic Saptarishis (Mind-Born Sages)",
          "Ancestral Rishi Clans of India", ["Rigveda", "Vishnu Purana I.7-10", "Ramayana", "Mahabharata"],
          "Vashishta -> Shakti -> Parashara (father of Vyasa!); Pulastya -> Vishrava -> Kubera & Ravana (King of Lanka!); Bhrigu -> Shukracharya / Kavi Ushanas (father of Devayani, exact cognate of Iranian Kavi Usan!) & Jamadagni -> Parashurama!",
          ["Vashishta", "Pulastya -> Ravana", "Bhrigu -> Shukracharya"], major=True),
        N("ved_kashyapa", "Marichi → Kashyapa (+ Aditi, Diti, Danu, Kadru, Vinata)", "vedic", 2, "Vedic Primordial Era",
          "Universal Prajapati Sage (Father of Adityas, Daityas & Nagas)", ["Mahabharata Adi Parva 65", "Vishnu Purana I.15"],
          "Through Daksha's daughters, Kashyapa fathers the 12 Adityas (Vivasvan/Surya, Indra, Varuna, Mitra [= Avestan Mithra!], Vishnu-Vamana via Aditi), Daityas (Hiranyakashipu -> Prahlada -> Mahabali via Diti), Danavas (Danu), Nagas (Kadru), and Garuda (Vinata).", major=True),
        N("ved_prahlada_bali", "Hiranyakashipu → Prahlada → Virochana → King Mahabali", "vedic", 3, "Daitya Lineage (Kashyapa & Diti)",
          "Asura Royal House (Onam / Kerala Tradition)", ["Bhagavata Purana VII-VIII", "Vishnu Purana I.17"],
          "Grandson of Kashyapa & Diti; devotee Prahlada leads to Emperor Mahabali (celebrated annually in Kerala's Onam festival)."),
    ]
    edges += [
        E("hub_primordial", "ved_dyaus_prithvi", "parallel", "Primordial Sky-Father & Earth-Mother"),
        E("hub_primordial", "ved_brahma_manu", "parallel", "Svayambhuva Manu & Shatarupa"),
        E("grk_zeus_olympians", "ved_dyaus_prithvi", "cognate", "EXACT Proto-Indo-European cognate: Greek Zeus Pater = Vedic Dyaus Pitr!"),
        E("ved_brahma_manu", "ved_priyavrata_rishabha", "direct", "Svayambhuva Manu -> Priyavrata -> ... -> Rishabhanatha"),
        E("ved_brahma_manu", "ved_uttanapada_dhruva", "direct", "Svayambhuva Manu -> Uttanapada (-> Dhruva) & Prasuti (+ Daksha)"),
        E("ved_brahma_manu", "ved_saptarishis_bhrigu", "direct", "Brahma -> Vashishta, Pulastya, Bhrigu & Angiras"),
        E("ved_brahma_manu", "ved_kashyapa", "direct", "Brahma -> Marichi -> Kashyapa"),
        E("ved_uttanapada_dhruva", "ved_kashyapa", "direct", "Daksha's daughters (Aditi, Diti, Danu, Kadru, Vinata) marry Kashyapa"),
        E("ved_kashyapa", "ved_prahlada_bali", "direct", "Kashyapa + Diti -> Hiranyakashipu -> Prahlada -> Mahabali"),
    ]

    # 2. Vivasvan (Surya) -> Yama, Vaivasvata Manu (Great Flood!) & ALL 10 Children of Manu
    nodes += [
        N("ved_vivasvan", "Vivasvan (Surya — Solar Progenitor)", "vedic", 3, "Vedic Antediluvian Horizon",
          "Exact Cognate of Avestan Vivanghant", ["Rigveda 10.14, 10.17", "Shatapatha Brahmana", "Vishnu Purana III.2"],
          "Son of Kashyapa & Aditi; EXACT Proto-Indo-Iranian cognate of Avestan Vivanghant! Father of Yama (= Iranian Yima), Vaivasvata Manu (Great Flood survivor), Ashwini Kumaras, Shani, and Tapati.",
          ["Surya", "Cognate: Avestan Vivanghant"], major=True),
        N("ved_yama", "Yama & Yami (Twin First Mortals)", "vedic", 4, "Vedic Primordial Horizon",
          "Lord of Dharma & Exact Cognate of Avestan Yima", ["Rigveda 10.10, 10.14"],
          "Son of Vivasvan; exact linguistic and genealogical twin of Iranian Yima (Jamshid) son of Vivanghant.",
          ["Cognate: Avestan Yima/Jamshid"], major=True),
        N("ved_trita_aptya", "Aptya → Trita Aptya & Kavi Ushanas (Shukracharya)", "vedic", 4, "Rigvedic Mythic Horizon",
          "Exact Proto-Indo-Iranian Cognates of Athwya/Thraetaona & Kavi Usan", ["Rigveda 1.105, 10.8, 10.99"],
          "Vedic dragon-slayer Trita son of Aptya is the exact cognate of Avestan Thraetaona (Fereydun) son of Athwya (Abtin), while sage Kavi Ushanas (Shukracharya, father of Yayati's wife Devayani!) is the exact cognate of Iranian King Kavi Usan (Kay Kavus)!",
          ["Trita = Fereydun", "Aptya = Abtin", "Kavi Ushanas = Kay Kavus"]),
        N("ved_vaivasvata_manu", "Vaivasvata Manu (Shraddhadeva — 7th Manu)", "vedic", 4, "Vedic Flood Horizon (Shatapatha Brahmana 1.8.1)",
          "Vedic Great Flood Survivor (Saved by Matsya)", ["Shatapatha Brahmana 1.8.1", "Mahabharata Vana Parva 185", "Matsya Purana"],
          "Warned by Matsya the Fish (avatar of Vishnu), builds a vessel moored to the Himalayas to survive the universal Deluge. Father of 10 children (Ikshvaku, Ila, Nabhaga, Sharyati, etc.) — universal ancestor of humanity (Manava)!",
          ["Shraddhadeva", "Matsya Flood Survivor"], major=True),
        N("ved_manu_other_sons", "Nabhaga (→ Ambarisha), Sharyati (→ Sukanya), Karusha & 5 Brothers", "vedic", 5, "Early Post-Flood India (Vishnu Purana IV.1)",
          "Other 8 Sons of Vaivasvata Manu", ["Vishnu Purana IV.1", "Bhagavata Purana IX.2-4"],
          "Alongside Ikshvaku and Ila, Vaivasvata Manu fathered Nabhaga (ancestor of devotee King Ambarisha), Sharyati (father of Sukanya who married sage Chyavana, founder of Anarta/Gujarat), Dhrishta, Narishyanta, Pranshu, Dishta, Karusha, and Prishadhra."),
    ]
    edges += [
        E("ved_kashyapa", "ved_vivasvan", "direct", "Kashyapa + Aditi -> Vivasvan (Surya)"),
        E("ved_vivasvan", "ved_yama", "direct", "Son (Rigveda 10.14)"),
        E("ved_vivasvan", "ved_vaivasvata_manu", "direct", "Son (Shatapatha Brahmana)"),
        E("ved_saptarishis_bhrigu", "ved_trita_aptya", "expansion", "Bhrigu -> Kavi Ushanas (Shukracharya) & Rigvedic Trita Aptya"),
        E("ved_vaivasvata_manu", "ved_manu_other_sons", "direct", "8 sons of Vaivasvata Manu (Vishnu Purana IV.1)"),
        E("ir_vivanghant", "ved_vivasvan", "cognate", "EXACT Proto-Indo-Iranian cognate: Vivanghant = Vivasvan"),
        E("ir_yima", "ved_yama", "cognate", "EXACT Proto-Indo-Iranian cognate: Yima = Yama"),
        E("ir_athwya", "ved_trita_aptya", "cognate", "EXACT Proto-Indo-Iranian cognate: Athwya/Thraetaona = Aptya/Trita"),
        E("ir_kay_kavus", "ved_trita_aptya", "cognate", "EXACT Proto-Indo-Iranian cognate: Kavi Usan (Kay Kavus) = Kavi Ushanas"),
        E("hub_flood", "ved_vaivasvata_manu", "parallel", "Ship towed by Matsya to the Himalayas (Shatapatha Brahmana 1.8.1)"),
        E("bib_abraham", "ved_brahma_manu", "syncretic", "Folkloric/syncretic comparison of Abraham/Sarah <-> Brahma/Saraswati (non-cognate)"),
    ]

    # 3. FULL SURYA VAMSHA (Solar Dynasty of Ayodhya — Ikshvaku -> Harishchandra -> Bhagiratha -> Raghu -> Rama -> Lava/Kusha + Buddha & Janaka!)
    nodes += [
        N("ved_ikshvaku", "Ikshvaku (Okkaka — Founder of Solar Dynasty)", "vedic", 5, "Early Solar Dynasty (Ayodhya)",
          "Eldest Son of Vaivasvata Manu / Ancestor of Rama & Buddha", ["Vishnu Purana IV.2", "Valmiki Ramayana", "Ambattha Sutta / Mahavamsa"],
          "First King of Kosala/Ayodhya; fathers 100 sons including Vikukshi (main Solar line), Nimi (Kings of Videha/Janaka!), and Dandaka. Buddhist Pali texts call him King Okkaka, ancestor of the Shakya clan!",
          ["Okkaka (Pali Canon)"], major=True),
        N("ved_nimi_janaka", "Nimi → Mithi → King Janaka of Videha (Father of Sita!)", "vedic", 6, "Videha / Mithila Kingdom",
          "Philosopher-Kings of Mithila (Upanishads & Ramayana)", ["Brihadaranyaka Upanishad", "Valmiki Ramayana", "Vishnu Purana IV.5"],
          "Son of Ikshvaku; founds the Videha dynasty of Mithila culminating in sage-king Janaka, father of Sita (wife of Rama)!"),
        N("ved_mandhata_harishchandra", "Vikukshi → Kakutstha → Mandhata → Trishanku → King Harishchandra", "vedic", 6, "Solar Dynasty (Satya → Treta Yuga)",
          "Universal Monarch Mandhata & Truth-Keeper Harishchandra", ["Vishnu Purana IV.2-3", "Markandeya Purana"],
          "Celebrated Solar monarchs bridging Ikshvaku to Sagara; Harishchandra sacrificed kingdom and family rather than break a single vow of truth."),
        N("ved_sagara_bhagiratha", "King Sagara → Anshuman → Dilipa I → Bhagiratha (River Ganga)", "vedic", 7, "Solar Dynasty (Ayodhya)",
          "Bringer of the Sacred River Ganga to Earth", ["Ramayana Bala Kanda", "Vishnu Purana IV.4"],
          "Sagara's 60,000 sons dug the ocean basin (Sagara); his great-great-grandson Bhagiratha performed austerity to bring the River Ganga down from Heaven to redeem them!", major=True),
        N("ved_raghu_dasharatha", "Dilipa II → Emperor Raghu → Aja → King Dasharatha", "vedic", 7, "Solar Dynasty (Raghuvamsha)",
          "Eponym of Raghuvamsha & Father of Rama", ["Valmiki Ramayana", "Kalidasa Raghuvamsha"],
          "Emperor Raghu gave Rama's clan its name (Raghava); his grandson Dasharatha (+ Kausalya, Kaikeyi, Sumitra) fathered Rama, Bharata, Lakshmana, and Shatrughna.", major=True),
        N("ved_surya_vamsha", "Rama (+ Sita), Bharata, Lakshmana & Shatrughna", "vedic", 8, "Treta Yuga (Valmiki Ramayana)",
          "Hero of the Ramayana (Ayodhya)", ["Valmiki Ramayana", "Vishnu Purana IV.4"],
          "Prince Rama (7th Avatar of Vishnu) marries Sita of Videha and defeats Ravana of Lanka. His brother Bharata's sons Taksha & Pushkala found Taxila (Takshashila) and Pushkalavati in Gandhara!",
          ["Rama of Ayodhya", "Raghava"], major=True),
        N("ved_lava_kusha", "Lava (Lahore) & Kusha (Kushavati) → Brihadbala", "vedic", 9, "Post-Ramayana Solar Line",
          "Twin Sons of Rama & Sita", ["Ramayana Uttara Kanda", "Vishnu Purana IV.4"],
          "Traditional founders of Lavapuri (Lahore) and Kushavati; Kusha's line continues down to King Brihadbala (who fought in the Mahabharata war) and the Ikshvaku kings of Kosala (Prasenajit, contemporary of the Buddha!)."),
        N("ved_buddha", "Shakya Clan (Okkaka) → King Shuddhodana (+ Maya) → Siddhartha Gautama (The Buddha)", "vedic", 10, "c. 563-483 BCE (Kapilavastu / Lumbini)",
          "Founder of Buddhism (Solar / Ikshvaku Lineage)", ["Digha Nikaya (Ambattha Sutta)", "Mahavamsa Ch. 2", "Buddhacarita"],
          "Buddhist chronicles trace the Shakya clan directly to King Okkaka (= Ikshvaku of the Solar Dynasty)! Siddhartha Gautama (son of Shuddhodana & Maya; father of Rahula via Yasodhara) sparks a pan-Asian movement reaching China, Korea, and Japan!",
          ["Gautama Buddha", "Shakyamuni", "Son: Rahula"], major=True),
    ]
    edges += [
        E("ved_vaivasvata_manu", "ved_ikshvaku", "direct", "Eldest son (Vishnu Purana IV.2)"),
        E("ved_ikshvaku", "ved_nimi_janaka", "direct", "Son Nimi -> Videha Dynasty -> King Janaka"),
        E("ved_ikshvaku", "ved_mandhata_harishchandra", "direct", "Vikukshi -> Kakutstha -> Mandhata -> Trishanku -> Harishchandra"),
        E("ved_mandhata_harishchandra", "ved_sagara_bhagiratha", "direct", "Rohita -> ... -> Sagara -> Anshuman -> Dilipa I -> Bhagiratha"),
        E("ved_sagara_bhagiratha", "ved_raghu_dasharatha", "direct", "Ambarisha -> ... -> Dilipa II -> Raghu -> Aja -> Dasharatha"),
        E("ved_raghu_dasharatha", "ved_surya_vamsha", "direct", "Sons Rama, Bharata, Lakshmana & Shatrughna (Ramayana)"),
        E("ved_nimi_janaka", "ved_surya_vamsha", "direct", "King Janaka's daughter Sita marries Rama"),
        E("ved_surya_vamsha", "ved_lava_kusha", "direct", "Twin sons Lava & Kusha -> Brihadbala"),
        E("ved_ikshvaku", "ved_buddha", "expansion", "Pali Canon (Ambattha Sutta / Mahavamsa): Okkaka (Ikshvaku) -> Shakya Clan -> Shuddhodana -> Gautama Buddha!"),
        E("ved_buddha", "jpn_jingu_ojin", "cognate", "Buddhism spreads from India through China & Baekje Korea to Prince Shotoku's Japan!"),
    ]

    # 4. FULL CHANDRA VAMSHA (Lunar Dynasty: Atri -> Soma -> Budha + Ila -> Pururavas -> Ayu -> Nahusha -> Yayati -> ALL 5 SONS!)
    nodes += [
        N("ved_atri_soma", "Atri → Soma (Chandra) → Budha + Ila (Child of Manu)", "vedic", 5, "Foundation of Chandra Vamsha (Lunar Dynasty)",
          "Union of Rishi Atri's Lunar Line & Vaivasvata Manu's Bloodline", ["Vishnu Purana IV.6", "Bhagavata Purana IX.14"],
          "Sage Atri births Soma (Moon); Soma's son Budha marries Ila (child of Vaivasvata Manu), uniting the Solar and Lunar lineages in Pururavas!", major=True),
        N("ved_pururavas_ayu", "Pururavas (+ Urvashi) → Ayu & Amavasu (→ Vishvamitra)", "vedic", 5, "Rigveda 10.95 (Early Lunar Kings)",
          "First Lunar Emperor & Ancestor of Vishvamitra / Dhanvantari", ["Rigveda 10.95", "Shatapatha Brahmana", "Vishnu Purana IV.6-7"],
          "Pururavas & celestial nymph Urvashi father Ayu (leading via Nahusha to Yayati, and via Kshatravriddha to Dhanvantari [Ayurveda] & Kings of Kashi!) and Amavasu (leading via Gadhi to Sage Vishvamitra!)."),
        N("ved_yayati", "Nahusha → Emperor Yayati (+ Devayani & Sharmishtha)", "vedic", 5, "Early Vedic Horizon (Father of the 5 Peoples)",
          "Vedic Table of Nations Ancestor (Panchajana)", ["Rigveda 1.108.8", "Mahabharata Adi Parva 75-85", "Vishnu Purana IV.10"],
          "Son of Nahusha; marries Devayani (daughter of Shukracharya / Kavi Ushanas!) and Sharmishtha (Asura princess), fathering the 5 great Vedic tribes: Yadu, Turvasu, Druhyu, Anu, and Puru!", major=True),
    ]
    edges += [
        E("ved_brahma_manu", "ved_atri_soma", "direct", "Brahma -> Atri -> Soma (Chandra) -> Budha"),
        E("ved_vaivasvata_manu", "ved_atri_soma", "direct", "Child Ila marries Budha (uniting Solar & Lunar lines!)"),
        E("ved_atri_soma", "ved_pururavas_ayu", "direct", "Budha + Ila -> Pururavas -> Ayu & Amavasu"),
        E("ved_pururavas_ayu", "ved_yayati", "direct", "Ayu -> Nahusha -> Yayati"),
        E("ved_trita_aptya", "ved_yayati", "direct", "Shukracharya (Kavi Ushanas)'s daughter Devayani marries Yayati"),
        E("hub_world_division", "ved_yayati", "parallel", "Yayati's 5 Sons (Panchajana — Vedic Table of Nations)"),
    ]

    # Yayati's 5 Sons (Individualized + Deep Expansions for EVERY Son!)
    add_children(nodes, edges, "ved_yayati", "vedic", 6, "Rigvedic Panchajana (5 Sons of Yayati)", [
        ("ved_yadu", "1. Yadu (Progenitor of Yadavas & Haihayas)", {"major": True, "notes": "Eldest son of Yayati & Devayani; progenitor of the Haihayas (Kartavirya Arjuna) and Vrishni/Yadava clan of Mathura & Dvaraka (Krishna, Balarama & Kunti!)."}),
        ("ved_turvasu", "2. Turvasu (Southern / Pandya-Chola-Chera Line)", {"notes": "Son of Yayati & Devayani; Puranas (Matsya/Harivamsha) trace the southern Tamil kingdoms (Pandya, Chola, Chera/Kerala) to Turvasu's line!"}),
        ("ved_druhyu", "3. Druhyu → Gandhara → Prachetas (NW & Trans-Indus Tribes)", {"major": True, "notes": "Son of Yayati & Sharmishtha; ancestor of King Gandhara (eponym of Gandhara / NW Pakistan-Afghanistan) and Prachetas, whose 100 sons migrate north/west across the Indus into Central Asia (Mleccha kingdoms) in Puranic ethnography!"}),
        ("ved_anu", "4. Anu → Ushinara (King Shibi) & Titikshu (Anga, Vanga, Kalinga)", {"notes": "Son of Yayati & Sharmishtha; splits into Ushinara (self-sacrificing King Shibi & Madra/Kekaya in Punjab) and Titikshu -> King Bali -> 5 Eastern Kingdoms (Anga, Vanga [Bengal], Kalinga [Odisha], Pundra, Suhma)!"}),
        ("ved_puru", "5. Puru (Pauravas — Inheritor of Central Realm)", {"major": True, "notes": "Youngest son of Yayati & Sharmishtha; trades his youth to restore his father's vigor and inherits the central throne leading to Bharata, Kuru, and the Mahabharata!"}),
    ], default_sources=["Rigveda 1.108.8", "Mahabharata Adi Parva 85", "Vishnu Purana IV.10-19"])

    # Deep Yadu Line -> Kartavirya Arjuna, Vasudeva, Kunti, Krishna, Balarama, Subhadra, Pradyumna!
    nodes += [
        N("ved_haihaya_satvata", "Sahasrajit (→ Kartavirya Arjuna) & Kroshtu → Satvata → Vrishni → Shurasena", "vedic", 7, "Yadava Royal Line (Vishnu Purana IV.11-14)",
          "Haihaya & Vrishni Branches of Yadu", ["Vishnu Purana IV.11-14", "Harivamsha"],
          "Sahasrajit -> Haihaya -> thousand-armed Emperor Kartavirya Arjuna; Kroshtu -> Satvata -> Andhaka & Vrishni -> Shurasena (grandfather of Krishna and the Pandavas!)."),
        N("ved_vasudeva_kunti", "Vasudeva (+ Devaki & Rohini) & Sister Kunti (Pritha)", "vedic", 8, "Mathura / Hastinapura Bridge",
          "Parents of Krishna/Balarama & Mother of the Pandavas", ["Mahabharata", "Bhagavata Purana X"],
          "Children of Shurasena: Vasudeva fathers Krishna, Balarama, and Subhadra; his sister Kunti marries Kuru prince Pandu, making Krishna and the Pandavas first cousins!", major=True),
        N("ved_krishna_balarama", "Krishna (+ Rukmini), Balarama & Subhadra → Pradyumna → Vajra", "vedic", 9, "Dvapara Yuga (Mahabharata / Bhagavad Gita)",
          "Speaker of the Bhagavad Gita & Lords of Dvaraka", ["Mahabharata", "Bhagavad Gita", "Bhagavata Purana X"],
          "Krishna (8th Avatar of Vishnu) & Balarama rule Dvaraka; Krishna's sister Subhadra marries Pandava Arjuna (birthing Abhimanyu!), while Krishna's son Pradyumna -> Aniruddha -> Vajra survives the fall of Dvaraka to rule Indraprastha!",
          ["Vasudeva Krishna", "Balarama", "Subhadra"], major=True),
    ]
    edges += [
        E("ved_yadu", "ved_haihaya_satvata", "direct", "Yadu -> Sahasrajit (Haihayas) & Kroshtu -> Vrishni -> Shurasena"),
        E("ved_haihaya_satvata", "ved_vasudeva_kunti", "direct", "Shurasena -> Vasudeva & Kunti (Pritha)"),
        E("ved_vasudeva_kunti", "ved_krishna_balarama", "direct", "Vasudeva (+ Devaki/Rohini) -> Krishna, Balarama & Subhadra -> Pradyumna -> Vajra"),
    ]

    # Deep Puru Line -> Dushyanta + Shakuntala -> Bharata -> Hasti -> Panchala/Drupada -> Kuru -> Shantanu -> Vyasa -> Pandavas & Kauravas -> Parikshit -> Mauryas/Ashoka!
    nodes += [
        N("ved_dushyanta_bharata", "Dushyanta (+ Shakuntala) → Emperor Bharata (Eponym of India!)", "vedic", 7, "Paurava Dynasty (Mahabharata Adi Parva)",
          "Universal Sovereign & Eponym of Bharatavarsha", ["Mahabharata Adi Parva 74", "Kalidasa Shakuntala", "Vishnu Purana IV.19"],
          "King Dushyanta (descendant of Puru) marries Shakuntala (daughter of Sage Vishvamitra & Menaka), birthing Emperor Bharata — who gives India its classical name Bharatavarsha!",
          ["Bharatavarsha"], major=True),
        N("ved_hasti_kuru", "Hasti (Hastinapura) → Ajamidha (→ Panchala/Drupada) → King Kuru", "vedic", 7, "Kuru-Panchala Horizon (c. 1200 BCE)",
          "Founders of Hastinapura, Panchala & Kurukshetra", ["Vishnu Purana IV.19", "Mahabharata Adi Parva 94"],
          "Hasti founds Hastinapura; Ajamidha branches into Panchala (King Drupada -> Draupadi & Dhrishtadyumna) and Samvarana (+ Tapati, daughter of Surya!) -> King Kuru (eponym of Kurukshetra & Kauravas)!", major=True),
        N("ved_shantanu_vyasa", "King Shantanu (+ Ganga → Bhishma; + Satyavati) & Sage Vyasa", "vedic", 8, "Mahabharata Gen 1",
          "Patriarchs of Hastinapura & Compiler of the Vedas", ["Mahabharata Adi Parva 95-106"],
          "Shantanu + Goddess Ganga -> Bhishma (vow of celibacy); Shantanu + Satyavati -> Vichitravirya. Satyavati's elder son Sage Vyasa (by Rishi Parashara, great-grandson of Vashishta!) compiles the 4 Vedas & Mahabharata and sires Dhritarashtra, Pandu, and Vidura!",
          ["Bhishma", "Krishna Dvaipayana Vyasa"], major=True),
        N("ved_kauravas", "Dhritarashtra (+ Gandhari) → Duryodhana, Dushasana & 100 Kauravas", "vedic", 9, "Mahabharata (Hastinapura)",
          "Elder Branch of the Kurus", ["Mahabharata"],
          "Blind King Dhritarashtra marries Princess Gandhari of Gandhara (sister of Shakuni — uniting Kuru and NW Gandhara!), fathering Duryodhana, 99 brothers, and daughter Duhshala."),
        N("ved_bharata_kuru", "Pandu (+ Kunti & Madri) → Karna & ALL 5 Pandavas (+ Draupadi)", "vedic", 9, "Mahabharata (Indraprastha / Kurukshetra)",
          "Yudhishthira, Bhima, Arjuna, Nakula & Sahadeva", ["Mahabharata", "Vishnu Purana IV.20"],
          "Kunti bears Karna (by Surya) and Yudhishthira, Bhima (-> Ghatotkacha), & Arjuna; Madri (princess of Madra!) bears twins Nakula & Sahadeva. All 5 Pandavas wed Draupadi (Princess of Panchala); Arjuna also weds Krishna's sister Subhadra -> Abhimanyu!",
          ["Yudhishthira, Bhima, Arjuna, Nakula, Sahadeva", "Karna"], major=True),
        N("ved_parikshit_janamejaya", "Abhimanyu (+ Uttara) → King Parikshit → King Janamejaya", "vedic", 10, "Dawn of Kali Yuga (Vishnu Purana IV.21)",
          "Post-Kurukshetra Kuru Kings", ["Mahabharata", "Bhagavata Purana I", "Vishnu Purana IV.21"],
          "Abhimanyu (son of Arjuna & Subhadra, uniting Kurus & Yadavas!) fathers Parikshit (saved in the womb by Krishna); at his son Janamejaya's serpent sacrifice, Vaishampayana first recites the Mahabharata!"),
        N("ved_maurya_ashoka", "Magadha (Jarasandha → Bimbisara) → Chandragupta Maurya → Emperor Ashoka", "vedic", 13, "Mauryan Empire (322-232 BCE)",
          "Unifier of India & Global Inscription Bridge (Greece, Egypt & Asia!)", ["Vishnu Purana IV.24", "Ashoka Rock Edict XIII (c. 256 BCE)", "Megasthenes Indica"],
          "Chandragupta Maurya (mentored by Chanakya) defeats Alexander's successor Seleucus I (305 BCE) and seals a marriage alliance with the Seleucid house! His grandson Emperor Ashoka the Great explicitly names Ptolemy II of Egypt, Antiochus II of Syria, and Macedon in Rock Edict XIII while sending Buddhist missions across Asia!",
          ["Ashoka Rock Edict XIII", "Chandragupta Maurya"], major=True),
    ]
    edges += [
        E("ved_puru", "ved_dushyanta_bharata", "direct", "Puru -> ... -> Dushyanta (+ Shakuntala) -> Emperor Bharata"),
        E("ved_pururavas_ayu", "ved_dushyanta_bharata", "direct", "Vishvamitra (from Amavasu) -> Shakuntala -> Emperor Bharata"),
        E("ved_dushyanta_bharata", "ved_hasti_kuru", "direct", "Bharata -> Hasti -> Ajamidha -> Samvarana -> King Kuru"),
        E("ved_vivasvan", "ved_hasti_kuru", "direct", "Surya's daughter Tapati marries Samvarana -> King Kuru"),
        E("ved_hasti_kuru", "ved_shantanu_vyasa", "direct", "Kuru -> ... -> Pratipa -> Shantanu"),
        E("ved_saptarishis_bhrigu", "ved_shantanu_vyasa", "direct", "Vashishta -> Shakti -> Parashara -> Sage Vyasa"),
        E("ved_shantanu_vyasa", "ved_kauravas", "direct", "Vyasa -> Dhritarashtra (+ Gandhari) -> 100 Kauravas"),
        E("ved_druhyu", "ved_kauravas", "cognate", "Queen Gandhari hails from NW Gandhara (Druhyu horizon)"),
        E("ved_shantanu_vyasa", "ved_bharata_kuru", "direct", "Vyasa -> Pandu -> 5 Pandavas"),
        E("ved_vasudeva_kunti", "ved_bharata_kuru", "direct", "Kunti (sister of Vasudeva) marries Pandu — uniting Yadavas & Kurus!"),
        E("ved_bharata_kuru", "ved_parikshit_janamejaya", "direct", "Arjuna -> Abhimanyu -> Parikshit -> Janamejaya"),
        E("ved_krishna_balarama", "ved_parikshit_janamejaya", "direct", "Subhadra (sister of Krishna) + Arjuna -> Abhimanyu -> Parikshit!"),
        E("ved_parikshit_janamejaya", "ved_maurya_ashoka", "expansion", "Vishnu Purana IV.24 royal chronology -> Magadha -> Mauryan Empire -> Ashoka"),
        E("grk_alexander", "ved_maurya_ashoka", "cognate", "Chandragupta Maurya defeats Seleucus I (305 BCE) & seals Seleucid marriage treaty (Megasthenes)"),
        E("ved_maurya_ashoka", "eg_ptolemy_cleopatra", "cognate", "Ashoka Rock Edict XIII (c. 256 BCE) explicitly names Ptolemy II of Egypt (Turamaya) as recipient of Dharma envoys!"),
        E("ved_buddha", "ved_maurya_ashoka", "expansion", "Emperor Ashoka champions Gautama Buddha's Dharma across Sri Lanka, Central Asia & the Mediterranean"),
    ]

    return {"module": "07_vedic_india", "title": "Exhaustive Vedic & Puranic Indian Genealogy (Saptarishis, Vaivasvata Manu, Full Surya Vamsha to Rama & Buddha, Full Chandra Vamsha to Krishna, Pandavas & Ashoka)", "nodes": nodes, "edges": edges}


def build_module_10_east_asia_chinese():
    nodes, edges = [], []

    # 1. Primordial Creation & Three Sovereigns (Pangu, Fuxi & Nuwa, Shaodian, Yandi/Shennong, Huangdi)
    nodes += [
        N("chn_pangu", "Pangu (Cosmic Creator)", "chinese", 1, "Primordial Cosmogony (Sanwu Liji)",
          "Separator of Heaven & Earth", ["Sanwu Liji", "Shan Hai Jing"],
          "Emerges from the cosmic egg, separates Yin (Earth) and Yang (Heaven), and transforms his body into mountains, rivers, sun, and moon."),
        N("chn_fuxi_nuwa", "Fuxi & Nüwa (Three Sovereigns)", "chinese", 1, "Primordial / Three Sovereigns",
          "Primordial Sibling-Consorts, Clay-Creators & Flood Survivors", ["Shan Hai Jing", "Huainanzi", "Fengsu Tongyi", "Yijing"],
          "Serpent-tailed sovereigns holding compass and square. Fuxi invents the Eight Trigrams (Bagua), fishing nets, and music; Nüwa repairs the shattered sky after Gonggong's flood and molds humanity from yellow clay. Preserved in SW Chinese Miao/Yao lore as Great Flood survivors!",
          ["Fu Hsi & Nu Wa", "Bagua Inventor"], major=True),
        N("chn_shaodian", "Shaodian & Youqiao (Guoyu)", "chinese", 2, "Pre-Five Emperors (Guoyu)",
          "Common Parents of Yandi & Huangdi", ["Guoyu (Discourses of the States)", "Shiji Ch. 1"],
          "Guoyu explicitly records Shaodian and Lady Youqiao as parents of BOTH Yandi (Jiang surname) and Huangdi (Ji surname) — explaining the ancestral brotherhood of 'Yan-Huang Zisun'!"),
        N("chn_yandi", "Yandi (Flame Emperor / Shennong)", "chinese", 2, "Three Sovereigns (Jiang Clan)",
          "Divine Farmer & Co-Ancestor of Huaxia (Yan-Huang)", ["Shiji Ch. 1", "Guoyu", "Shennong Bencaojing"],
          "Inventor of agriculture, plows, and herbal medicine; ancestor of the Jiang clan (later Jiang Ziya & the State of Qi!). Allies with Huangdi after the Battle of Banquan to defeat Chiyou.",
          ["Shennong", "Jiang Clan"], major=True),
        N("chn_chiyou_jiangziya", "Chiyou (Jiuli Tribe) & Jiang Ziya (State of Qi)", "chinese", 3, "Three Sovereigns → Zhou Era",
          "Yandi/Jiang Lineages & Rival of Huangdi", ["Shiji Ch. 1, 32", "Shan Hai Jing"],
          "Chiyou (legendary bronze-working leader of the Nine Li / Miao-Hmong ancestor!) fought Huangdi at Zhuolu; Jiang Ziya (descendant of Yandi's clan) helped King Wu found the Zhou Dynasty and became Duke of Qi."),
        N("chn_huangdi", "Huangdi (Yellow Emperor) & Leizu", "chinese", 2, "Five Emperors (c. 2697 BCE trad.)",
          "Universal Royal Ancestor in Sima Qian's Shiji (25 Sons)", ["Sima Qian Shiji Ch. 1", "Bamboo Annals", "Da Dai Liji"],
          "Marries Leizu (inventor of silk sericulture) and sires 25 sons bearing 14 surnames. Sima Qian systematically traces ALL Five Emperors, Xia, Shang, Zhou, Qin, Chu, Confucius, and the Xiongnu back to Huangdi!",
          ["Xuanyuan", "Yan-Huang Zisun"], major=True),
    ]
    edges += [
        E("hub_primordial", "chn_pangu", "parallel", "Cosmic separation of Heaven & Earth"),
        E("hub_primordial", "chn_fuxi_nuwa", "parallel", "Nüwa molds humans from yellow clay"),
        E("chn_pangu", "chn_fuxi_nuwa", "expansion", "Chinese mythic chronology: Pangu -> Three Sovereigns"),
        E("chn_fuxi_nuwa", "chn_shaodian", "expansion", "Three Sovereigns succession"),
        E("chn_shaodian", "chn_yandi", "direct", "Son (Jiang clan, Guoyu)"),
        E("chn_shaodian", "chn_huangdi", "direct", "Son (Ji clan, Guoyu — Yan-Huang brotherhood)"),
        E("chn_yandi", "chn_chiyou_jiangziya", "expansion", "Jiang clan -> Jiang Ziya (Qi); Chiyou allied/conflicted with Yan-Huang"),
        E("bib_noah", "chn_fuxi_nuwa", "syncretic", "17th-c. Figurists (Bouvet) compared Noah to Fuxi"),
        E("hub_world_division", "chn_huangdi", "parallel", "Huangdi's 25 Sons (14 surnames) -> Xia, Shang, Zhou, Qin, Chu, Xiongnu"),
    ]

    # 2. Branch A: Huangdi -> Shaohao -> Jiaoji -> Emperor Ku (Di Ku) -> Yao, Shang (Confucius & Jizi/Korea!) & Zhou!
    nodes += [
        N("chn_shaohao", "Shaohao (Xuanxiao) → Jiaoji", "chinese", 3, "Five Emperors Horizon",
          "Eldest Son of Huangdi & Leizu", ["Shiji Ch. 1", "Zuo Zhuan"],
          "Son of Huangdi & Leizu; ancestor of Eastern Yi bird-totem clans and father of Jiaoji -> Emperor Ku."),
        N("chn_diku", "Emperor Ku (Di Ku / Gaoxin)", "chinese", 4, "Five Emperors (c. 2436 BCE trad.)",
          "Great-Grandson of Huangdi / Father of Yao, Shang & Zhou", ["Shiji Ch. 1, 3, 4", "Da Dai Liji"],
          "By his four consorts, Di Ku fathers Emperor Zhi, Emperor Yao (via Qingdu), Xie (founder of Shang via Jiandi), and Hou Ji (founder of Zhou via Jiang Yuan)!",
          ["Gaoxin"], major=True),
        N("chn_yao", "Emperor Yao (Tang Yao → Liu Bang / Han Dynasty)", "chinese", 5, "Five Emperors (c. 2356 BCE trad.)",
          "Model Sage Emperor (Abdicates to Shun)", ["Shangshu (Yao Dian)", "Shiji Ch. 1, 8"],
          "Son of Di Ku & Qingdu; appoints Gun & Yu to combat the Great Flood, marries his daughters Ehuang & Nüying to Emperor Shun, and passes the throne by merit. Han Dynasty emperors (Liu Bang) claimed descent from Yao!", major=True),

        # Shang Dynasty (Xie -> Tang -> Wu Ding & Fu Hao -> Weizi/Confucius & Jizi/Korea!)
        N("chn_xie", "Xie (son of Di Ku & Jiandi) → Wang Hai", "chinese", 5, "Predynastic Shang (14 Generations)",
          "Progenitor of the Shang Royal House (Zi Clan)", ["Shiji Ch. 3 (Yin Benji)", "Shijing"],
          "Conceived when Jiandi swallowed a black bird's egg; assisted Yu the Great with the Flood; leads through 14 predynastic lords (including Wang Hai) to Tang of Shang."),
        N("chn_shang", "Tang of Shang (Cheng Tang) → Pan Geng", "chinese", 6, "Shang Dynasty (c. 1600-1300 BCE)",
          "Founder of Shang Dynasty & Mover of Capital to Anyang", ["Anyang Oracle Bones", "Shiji Ch. 3", "Bamboo Annals"],
          "Overthrew Xia tyrant Jie to found the Shang Dynasty; 19th king Pan Geng moved the capital to Yin (Anyang), where tens of thousands of oracle bones confirm Sima Qian's king list!", major=True),
        N("chn_wuding_fuhao", "King Wu Ding & Warrior Queen Fu Hao", "chinese", 7, "High Shang (c. 1250-1192 BCE)",
          "First Historically Verified Shang Monarch & Female General", ["Anyang Oracle Bones", "Tomb of Fu Hao"],
          "21st Shang king attested in contemporary oracle bones; his consort Fu Hao served as supreme general and high priestess (her intact tomb at Anyang is one of archaeology's greatest treasures!).", major=True),
        N("chn_dixin", "Di Xin (King Zhou of Shang) — Final Shang King", "chinese", 8, "c. 1075-1046 BCE",
          "Last King of Shang (Battle of Muye)", ["Shiji Ch. 3", "Shangshu"],
          "Defeated by King Wu of Zhou in 1046 BCE, ending the Shang Dynasty."),
        N("chn_weizi_confucius", "Weizi Qi (Duke of Song) → Kong He → Confucius (Kong Qiu)", "chinese", 9, "Zhou / Spring & Autumn (551-479 BCE)",
          "Shang Royal Descendant & China's Great Sage", ["Shiji Ch. 38 & Ch. 47 (Kongzi Shijia)", "Analects"],
          "Sima Qian's Shiji Ch. 47 traces Confucius (Kong Qiu) directly back through the Dukes of Song to Weizi Qi (brother of Di Xin) -> Shang Dynasty -> Xie -> Di Ku -> Yellow Emperor!",
          ["Kongzi", "Kong Qiu"], major=True),
        N("chn_jizi", "Jizi (Gija — Shang Prince Migrating to Korea)", "chinese", 8, "c. 1046 BCE (Shang → Gojoseon)",
          "Shang Royal Sage & China-Korea Chronicle Bridge", ["Shiji Ch. 38", "Book of Han", "Samguk Yusa"],
          "Uncle/kinsman of Shang king Di Xin; recorded in both Chinese (*Shiji*) and Korean (*Samguk Yusa*) chronicles as migrating east to Joseon with 5,000 followers after the fall of Shang!"),

        # Zhou Dynasty (Hou Ji -> King Wen -> King Wu & Duke of Zhou -> King Mu!)
        N("chn_houji", "Hou Ji (Lord Millet) → Gong Liu → Gugong Danfu", "chinese", 5, "Predynastic Zhou (Ji Clan)",
          "Minister of Agriculture & Progenitor of Zhou", ["Shiji Ch. 4 (Zhou Benji)", "Shijing (Sheng Min)"],
          "Son of Di Ku & Jiang Yuan; taught millet farming and founded the Ji lineage leading via Buzhu -> Gong Liu -> Gugong Danfu (whose elder sons Taibo & Zhongyong founded the State of Wu!)."),
        N("chn_zhou", "King Wen (Ji Chang) → King Wu (Ji Fa) of Zhou", "chinese", 7, "Western Zhou (1046-1043 BCE)",
          "Founders of the Zhou Dynasty & Mandate of Heaven", ["Shiji Ch. 4", "Shangshu", "Yijing"],
          "King Wen expanded the Yijing (Book of Changes); his son King Wu allied with Jiang Ziya to defeat Shang at Muye (1046 BCE), establishing China's longest dynasty (800 years!).", major=True),
        N("chn_duke_of_zhou", "Duke of Zhou (Ji Dan — Founder of Lu) & King Mu of Zhou", "chinese", 8, "Western Zhou (1042-922 BCE)",
          "Architect of Zhou Rites & Western Silk-Road Traveler", ["Shiji Ch. 4, 33", "Mu Tianzi Zhuan"],
          "Duke of Zhou (brother of King Wu) founded the State of Lu (homeland of Confucius!) and codified classical ritual; 5th king King Mu journeyed far west into Central Asia to meet Xiwangmu (Queen Mother of the West)!"),
    ]
    edges += [
        E("chn_huangdi", "chn_shaohao", "direct", "Huangdi + Leizu -> Shaohao/Xuanxiao -> Jiaoji (Shiji Ch. 1)"),
        E("chn_shaohao", "chn_diku", "direct", "Jiaoji -> Emperor Ku / Di Ku (Shiji Ch. 1)"),
        E("chn_diku", "chn_yao", "direct", "Di Ku + Qingdu -> Emperor Yao (Shiji Ch. 1)"),
        E("chn_diku", "chn_xie", "direct", "Di Ku + Jiandi -> Xie (Shiji Ch. 3)"),
        E("chn_xie", "chn_shang", "direct", "14 predynastic Shang lords -> Tang of Shang -> Pan Geng"),
        E("chn_shang", "chn_wuding_fuhao", "direct", "Shang royal line -> King Wu Ding & Queen Fu Hao"),
        E("chn_wuding_fuhao", "chn_dixin", "direct", "Late Shang kings -> Di Xin"),
        E("chn_dixin", "chn_weizi_confucius", "direct", "Brother Weizi Qi (Duke of Song) -> ... -> Kong He -> Confucius (Shiji Ch. 47!)"),
        E("chn_dixin", "chn_jizi", "direct", "Shang royal kinsman Jizi / Gija (Shiji Ch. 38)"),
        E("chn_diku", "chn_houji", "direct", "Di Ku + Jiang Yuan -> Hou Ji (Shiji Ch. 4)"),
        E("chn_houji", "chn_zhou", "direct", "Gugong Danfu -> Jili -> King Wen -> King Wu of Zhou"),
        E("chn_zhou", "chn_duke_of_zhou", "direct", "Brother Duke of Zhou (Lu) & Descendant King Mu"),
    ]

    # 3. Branch B: Huangdi -> Changyi -> Zhuanxu -> Xia/Yu the Great, Emperor Shun, Qin Shi Huang, State of Chu, Yue & Xiongnu!
    nodes += [
        N("chn_zhuanxu", "Changyi → Emperor Zhuanxu (Gaoyang)", "chinese", 3, "Five Emperors Era",
          "Separator of Heaven & Earth / Ancestor of Xia, Shun, Qin & Chu", ["Shiji Ch. 1, 2, 5, 40", "Shan Hai Jing"],
          "Grandson of Huangdi via Changyi; ordered the separation of Heaven and Earth (Jue Di Tian Tong). Progenitor of FOUR huge dynasties: Xia, Shun/Chen, Qin, and Chu!", major=True),
        N("chn_gun", "Gun (Father of Yu the Great)", "chinese", 3, "Great Flood Era (Shangshu / Shan Hai Jing)",
          "Descendant of Zhuanxu Who Stole Xirang Soil", ["Shiji Ch. 2", "Shan Hai Jing", "Chu Ci"],
          "Descendant of Zhuanxu tasked by Emperor Yao with halting the Great Flood; stole the heavenly self-expanding earth (Xirang) to build dikes, was executed on Feather Mountain, and from his body emerged Yu the Great!"),
        N("chn_yu_xia", "Yu the Great (Da Yu) & Tushan Shi → Qi (Xia Dynasty)", "chinese", 4, "Great Flood / Xia (c. 2070-1600 BCE)",
          "Tamer of the Great Flood & Founder of Xia Dynasty", ["Shangshu (Yu Gong)", "Shiji Ch. 2", "Bamboo Annals"],
          "Spent 13 years dredging channels to drain the Gun-Yu Great Flood into the sea, mapping the Nine Provinces; his son Qi established China's first hereditary dynasty (Xia)!",
          ["Da Yu", "Xia Dynasty"], major=True),
        N("chn_shaokang_yue", "Tai Kang → Shao Kang (Xia Restoration) → King Jie & State of Yue", "chinese", 5, "Xia Dynasty → Warring States Yue",
          "Xia Successors & Ancestors of Yue (King Goujian)", ["Shiji Ch. 2, 41", "Bamboo Annals"],
          "Shao Kang restored the Xia Dynasty after Hou Yi's usurpation; his son Wuyu founded the southern State of Yue (later led by King Goujian); Xia ended under tyrant Jie."),
        N("chn_shun", "Gusou → Emperor Shun (Youyu) & Ehuang / Nüying", "chinese", 5, "Five Emperors (c. 2255 BCE trad.)",
          "Filial Sage Emperor (Descendant of Zhuanxu)", ["Shangshu", "Shiji Ch. 1"],
          "Descended from Zhuanxu via Qiongchan -> Jingkang -> Juwang -> Qiaoniu -> Gusou; married Yao's two daughters Ehuang & Nüying and passed the throne to Yu the Great. Ancestor of the State of Chen!"),
        N("chn_boyi_qin", "Nüxiu → Daye → Boyi → Feizi → Qin Shi Huang (First Emperor)", "chinese", 8, "Five Emperors → 221 BCE (Qin Dynasty)",
          "House of Ying (Descendants of Zhuanxu → Unified China!)", ["Shiji Ch. 5 (Qin Benji) & Ch. 6"],
          "Sima Qian's Shiji Ch. 5 traces the Ying clan from Zhuanxu's granddaughter Nüxiu -> Daye -> Boyi (Yu the Great's companion!) -> Feizi -> Dukes of Qin -> Ying Zheng (**Qin Shi Huang**, First Emperor of unified China, 221 BCE)!",
          ["Ying Zheng", "First Emperor of China"], major=True),
        N("chn_chu_zhurong", "Zhurong → Luzhong (Pengzu, 800 yrs!) → Jilian → State of Chu (Qu Yuan)", "chinese", 7, "Five Emperors → Warring States Chu",
          "House of Mi / Southern Chu Dynasty (Descendant of Zhuanxu)", ["Shiji Ch. 40 (Chu Shijia)", "Chu Ci"],
          "Shiji Ch. 40 traces the southern Chu royal house from Zhuanxu -> Zhurong (Fire deity!) -> Wuhui -> Luzhong (father of 6 sons including 800-year longevity sage Pengzu and Jilian!) -> Xiong Yi -> poet Qu Yuan & Hegemon Xiang Yu!",
          ["Pengzu (800-yr sage)", "Qu Yuan"], major=True),
    ]
    edges += [
        E("chn_huangdi", "chn_zhuanxu", "direct", "Huangdi -> Changyi -> Zhuanxu (Shiji Ch. 1)"),
        E("chn_zhuanxu", "chn_gun", "direct", "Descendant of Zhuanxu (Shiji Ch. 2)"),
        E("chn_gun", "chn_yu_xia", "direct", "Son Yu the Great -> Qi of Xia (Shiji Ch. 2)"),
        E("hub_flood", "chn_yu_xia", "parallel", "Gun-Yu Great Flood & channeling of China's rivers"),
        E("chn_yu_xia", "chn_shaokang_yue", "direct", "Qi -> Tai Kang -> Shao Kang (-> Wuyu of Yue) -> King Jie"),
        E("chn_zhuanxu", "chn_shun", "direct", "Zhuanxu -> Qiongchan -> ... -> Gusou -> Emperor Shun (Shiji Ch. 1)"),
        E("chn_yao", "chn_shun", "direct", "Yao's daughters Ehuang & Nüying marry Emperor Shun"),
        E("chn_zhuanxu", "chn_boyi_qin", "direct", "Zhuanxu -> Nüxiu -> Daye -> Boyi -> Feizi -> Qin Shi Huang (Shiji Ch. 5)"),
        E("chn_zhuanxu", "chn_chu_zhurong", "direct", "Zhuanxu -> Zhurong -> Luzhong (Pengzu & Jilian) -> State of Chu (Shiji Ch. 40)"),
        E("bib_methuselah", "chn_chu_zhurong", "parallel", "800-year longevity sage Pengzu (Shiji Ch. 40) <-> antediluvian Methuselah"),
    ]

    # 4. Eurasian Steppe Bridge (Xiongnu & Oghuz Khagan — 6 Sons Individualized!)
    nodes += [
        N("stp_xiongnu", "Chunwei (Xia Prince) → Touman → Modu Chanyu (Xiongnu)", "steppe", 6, "Bronze Age → 209 BCE (Shiji Ch. 110)",
          "Sima Qian's Bridge Between Chinese Xia & Inner Asian Steppe", ["Sima Qian Shiji Ch. 110 (Account of the Xiongnu)"],
          "Sima Qian explicitly records that the Xiongnu descended from Chunwei, a prince of the Xia Dynasty who migrated to the northern steppes; unified under Touman -> Modu Chanyu (209 BCE)!",
          ["Modu Chanyu", "Huns precursor?"], major=True),
        N("stp_oghuz", "Turk (Oljai Khan) → Tatar & Mongol → Oghuz Khagan", "steppe", 8, "Mythic Steppe / Medieval Synthesis",
          "Eponymous Ancestor of Turkic & Mongol Peoples", ["Oghuzname", "Rashid al-Din Jami al-Tawarikh (1307)", "Abulghazi Shajara-i Tarakima"],
          "Rashid al-Din & Abulghazi explicitly graft Turkic/Mongol ancestry onto Biblical Japheth (Yafith -> Oljai -> Alinja -> Tatar & Mongol -> Kara Khan -> Oghuz Khagan) and Iranian Turan!",
          ["Oghuz Khan", "24 Oghuz Tribes"], major=True),
        N("stp_oghuz_six", "6 Sons of Oghuz: Gün (Sun), Ay (Moon), Yildiz, Gök, Dağ & Deniz", "steppe", 9, "Oghuzname (Bozok & Üçok)",
          "Founders of the 24 Oghuz Turkic Tribes (Seljuks & Ottomans!)", ["Oghuzname", "Jami al-Tawarikh"],
          "Oghuz's 3 elder sons (Bozok: Gün, Ay, Yildiz) and 3 younger sons (Üçok: Gök, Dağ, Deniz) each sire 4 sons = the 24 Oghuz clans (including Kayı -> Ottomans and Kınık -> Seljuks!)."),
    ]
    edges += [
        E("chn_yu_xia", "stp_xiongnu", "expansion", "Shiji Ch. 110: Xiongnu descend from Chunwei of the Xia Dynasty"),
        E("stp_xiongnu", "stp_oghuz", "expansion", "Steppe continuity: Modu Chanyu's biography parallels Oghuz Khagan legend"),
        E("stp_oghuz", "stp_oghuz_six", "direct", "6 sons -> 24 Oghuz Turkic tribes (Oghuzname)"),
        E("bib_japheth", "stp_oghuz", "syncretic", "Rashid al-Din (1307): Yafith (Japheth) -> Turk -> Oghuz Khagan"),
        E("jas_tog_tarki", "stp_oghuz", "syncretic", "Book of Jasher 10:10 Tarki (son of Togarmah) <-> Turkic lineage"),
        E("ir_tur", "stp_oghuz", "syncretic", "Tur (Turan) equated in Persian/Turkic lore with Turkic Steppe"),
    ]

    return {"module": "10_east_asia_chinese", "title": "Exhaustive Ancient Chinese & Inner Asian Steppe Genealogy (Shiji Ch. 1-5, 40, 47, 110; Xia, Shang, Zhou, Qin, Chu, Confucius & Oghuz)", "nodes": nodes, "edges": edges}


def build_module_11_korean_japanese():
    nodes, edges = [], []

    # 1. Ancient Korea (Samguk Yusa & Samguk Sagi — Gojoseon, Goguryeo, Baekje, Silla, Gaya + India Ayodhya Bridge!)
    nodes += [
        N("kor_hwanin_hwanung", "Hwanin (Lord of Heaven) → Hwanung & Ungnyeo", "japan_korea", 3, "Gojoseon Mythic Origin (Samguk Yusa)",
          "Heavenly Prince & Bear-Turned-Woman", ["Samguk Yusa (1281 CE, citing lost Gogi)", "Jewang Ungi"],
          "Hwanung descends from Heaven to Mt. Taebaek with 3,000 followers and the gods of Wind, Rain, and Clouds; weds Ungnyeo (the bear who endured 100 days of mugwort and garlic to become human)."),
        N("jk_dangun", "Dangun Wanggeom (Founder of Gojoseon, 2333 BCE trad.) → Buru", "japan_korea", 5, "Gojoseon (2333 BCE trad.)",
          "Founding Ancestor of the Korean People", ["Samguk Yusa", "Jewang Ungi"],
          "Son of Hwanung & Ungnyeo; founded Gojoseon (Asadal) in the traditional era of Chinese Emperor Yao! Father of Prince Buru (who in Korean annals meets Yu the Great at Tushan!).",
          ["Tangun", "Founder of Gojoseon"], major=True),
        N("kor_jumong", "Hae Mosu + Yuhwa → King Dongmyeong (Jumong — Goguryeo)", "japan_korea", 9, "37 BCE (Three Kingdoms — Goguryeo)",
          "Master Archer & Founder of Goguryeo", ["Gwanggaeto Stele (414 CE)", "Samguk Sagi", "Samguk Yusa"],
          "Born from a luminous egg to Yuhwa (daughter of River God Habaek) and heavenly prince Hae Mosu; founded the northern kingdom of Goguryeo (leading to King Yuri and King Gwanggaeto the Great!).",
          ["Jumong", "Chumo"], major=True),
        N("kor_onjo_baekje", "Soseono → Onjo (Founder of Baekje) → King Geunchogo", "japan_korea", 10, "18 BCE - 660 CE (Baekje Kingdom)",
          "Founder of Baekje & Royal Bridge to Yamato Japan!", ["Samguk Sagi", "Nihon Shoki"],
          "Onjo (son of Jumong & Lady Soseono) founded Baekje in SW Korea; Baekje became Yamato Japan's closest ally, transmitting Chinese writing (Wani), Buddhism, and royal intermarriage (Emperor Kammu's mother descended from Baekje's King Muryeong!)!",
          ["Baekje <-> Yamato Japan Bridge"], major=True),
        N("kor_hyeokgeose_silla", "Park Hyeokgeose (+ Aryeong), Seok Talhae & Kim Alji (Silla)", "japan_korea", 9, "57 BCE - 935 CE (Silla Kingdom)",
          "Founding Clans of Silla (Park, Seok & Kim)", ["Samguk Sagi", "Samguk Yusa"],
          "Park Hyeokgeose (born from a luminous egg at Najeong well) founded Silla; joined by Seok Talhae and Kim Alji (born from a golden box in Gyerim forest — ancestor of Queen Seondeok & unified Silla kings!)."),
        N("kor_suro_heo", "King Suro of Gaya + Queen Heo Hwang-ok (Princess of Ayuta / India!)", "japan_korea", 10, "48 CE trad. (Geumgwan Gaya — Samguk Yusa)",
          "India ↔ Korea Royal Marriage Bridge (Gimhae Kim & Heo Clans)", ["Samguk Yusa (Garakguk-gi)"],
          "King Suro (born from one of 6 golden eggs on Mt. Guji) married Princess Heo Hwang-ok (Suriratna), who sailed to Korea from the Kingdom of Ayuta (traditionally identified with Ayodhya, India — capital of the Solar Dynasty!) carrying a stone pagoda. Ancestors of millions of Gimhae Kim & Heo Koreans!",
          ["Princess Suriratna of Ayodhya", "India <-> Korea Bridge"], major=True),
    ]
    edges += [
        E("hub_primordial", "kor_hwanin_hwanung", "parallel", "Heavenly descent & origin of Korea"),
        E("kor_hwanin_hwanung", "jk_dangun", "direct", "Hwanung + Ungnyeo -> Dangun Wanggeom (Samguk Yusa)"),
        E("chn_jizi", "jk_dangun", "expansion", "Shiji Ch. 38 & Samguk Yusa: Shang prince Jizi (Gija) migrates to Gojoseon"),
        E("jk_dangun", "kor_jumong", "expansion", "Buyeo / Gojoseon continuity -> Hae Mosu -> Jumong (Goguryeo)"),
        E("kor_jumong", "kor_onjo_baekje", "direct", "Son Onjo (via Soseono) founds Baekje (Samguk Sagi)"),
        E("jk_dangun", "kor_hyeokgeose_silla", "expansion", "Gojoseon diaspora -> Six Villages of Saro -> Silla (Park, Seok, Kim)"),
        E("jk_dangun", "kor_suro_heo", "expansion", "Southern Korean confederacies -> Geumgwan Gaya (King Suro)"),
        E("ved_surya_vamsha", "kor_suro_heo", "syncretic", "Samguk Yusa: Queen Heo Hwang-ok sails from Ayuta (trad. Ayodhya, Solar Dynasty capital) to marry King Suro of Gaya!"),
    ]

    # 2. Ancient Japan (Kojiki [712 CE] & Nihon Shoki [720 CE] — Full Divine to Imperial Lineage!)
    nodes += [
        N("jpn_kotoamatsukami", "Ame-no-Minakanushi, Takamimusubi & Kamimusubi", "japan_korea", 1, "Creation of Takamagahara (Kojiki Book I)",
          "Primordial Creator Kami (Kotoamatsukami)", ["Kojiki (712 CE)", "Nihon Shoki (720 CE)"],
          "Three primordial creation deities appearing at the dawn of Heaven and Earth; Takamimusubi is the maternal grandfather of Ninigi!"),
        N("jk_izanagi_amaterasu", "Izanagi & Izanami (Creators of the Japanese Islands)", "japan_korea", 2, "Seven Divine Generations (Kamiyonanayo)",
          "Primordial Creator Couple of Japan", ["Kojiki Book I", "Nihon Shoki Book I"],
          "Stir the primeval ocean with the heavenly jeweled spear Amenonuhoko to birth Onogoro and the Eight Great Islands of Japan, plus Fire God Kagutsuchi and the Three Noble Children.", major=True),
        N("jpn_amaterasu", "Amaterasu-Omikami (Sun Goddess) & Tsukuyomi (Moon)", "japan_korea", 3, "Age of the Gods (Takamagahara)",
          "Supreme Sun Goddess / Ancestress of Japan's Emperors", ["Kojiki Book I", "Nihon Shoki"],
          "Born from Izanagi's left eye upon purifying himself from Yomi (the Underworld); ruler of the High Plain of Heaven (Takamagahara) and divine ancestress of the Imperial House of Japan.",
          ["Sun Goddess"], major=True),
        N("jpn_susanoo", "Susanoo-no-Mikoto (+ Kushinadahime) → Okuninushi (Izumo)", "japan_korea", 3, "Age of the Gods (Izumo Cycle)",
          "Storm God & Slayer of Yamata-no-Orochi", ["Kojiki Book I", "Nihon Shoki"],
          "Brother of Amaterasu; slays the eight-headed serpent Yamata-no-Orochi to win the Kusanagi sword, marries Kushinadahime, and sires the Izumo dynasty leading to Okuninushi (who builds Izumo and cedes the land to Amaterasu's grandson Ninigi!).",
          ["Okuninushi of Izumo"], major=True),
        N("jpn_oshihomimi", "Ame-no-Oshihomimi & Ninigi-no-Mikoto (+ Konohanasakuya-hime)", "japan_korea", 4, "Heavenly Descent (Tenson Korin)",
          "Grandson of Amaterasu Bearing the Three Imperial Regalia", ["Kojiki Book I", "Nihon Shoki Book II"],
          "Amaterasu's son Ame-no-Oshihomimi weds Takamimusubi's daughter and sires Ninigi, who descends to Mt. Takachiho (Kyushu) carrying the Mirror, Jewel, and Sword (Three Imperial Regalia) and marries Mt. Fuji goddess Konohanasakuya-hime!", major=True),
        N("jpn_hoori", "Hoderi & Hoori (+ Toyotama-hime) → Ugayafukiaezu", "japan_korea", 5, "Kyushu Mythic Horizon",
          "Grandfather & Father of Emperor Jimmu", ["Kojiki Book I"],
          "Hoori (Yamasachihiko) journeys to the underwater palace of Sea God Ryujin/Watatsumi, weds sea princess Toyotama-hime, and fathers Ugayafukiaezu -> Emperor Jimmu!"),
        N("jk_jimmu", "Emperor Jimmu (Kamu-yamato Iware-biko, 1st Emperor)", "japan_korea", 6, "660 BCE trad. (Kojiki Book II)",
          "Founder of the Imperial House of Japan (Yamato)", ["Kojiki Book II", "Nihon Shoki Book III"],
          "Great-grandson of Ninigi; leads the Eastern Expedition from Kyushu to Yamato (Nara), guided by the three-legged crow Yatagarasu, founding the world's oldest continuous hereditary monarchy!",
          ["1st Emperor of Japan"], major=True),
        N("jpn_sujin_yamato", "Emperor Sujin (10th) → Emperor Keiko → Prince Yamato Takeru", "japan_korea", 9, "Yayoi → Early Kofun Horizon",
          "First Historical Yamato Anchor & Heroic Prince", ["Kojiki Book II", "Nihon Shoki Books V-VII"],
          "Emperor Sujin is widely regarded as the earliest historically grounded Yamato ruler; his descendant Prince Yamato Takeru wields Susanoo's Kusanagi sword to unify Honshu."),
        N("jpn_jingu_ojin", "Empress Jingu → Emperor Ojin (Hachiman) → Emperor Nintoku → Prince Shotoku", "japan_korea", 11, "Kofun → Asuka Period (4th-7th c. CE)",
          "Yamato Emperors & Architects of Korean/Chinese Cultural Bridge", ["Kojiki Book III", "Nihon Shoki", "17-Article Constitution"],
          "Emperor Ojin (deified as Hachiman) welcomed Baekje Korean scholar Wani (bringing Chinese characters and Confucius's Analects to Japan!); Prince Shotoku (574-622 CE) established Buddhism and Japan's 17-Article Constitution!",
          ["Emperor Ojin (Hachiman)", "Prince Shotoku"], major=True),
    ]
    edges += [
        E("hub_primordial", "jpn_kotoamatsukami", "parallel", "Primordial heavenly creation (Kojiki)"),
        E("jpn_kotoamatsukami", "jk_izanagi_amaterasu", "expansion", "Seven Divine Generations -> Izanagi & Izanami"),
        E("jk_izanagi_amaterasu", "jpn_amaterasu", "direct", "Born from Izanagi's purification (Kojiki I)"),
        E("jk_izanagi_amaterasu", "jpn_susanoo", "direct", "Born from Izanagi's nose (Kojiki I)"),
        E("jpn_amaterasu", "jpn_oshihomimi", "direct", "Amaterasu -> Ame-no-Oshihomimi -> Ninigi"),
        E("jpn_kotoamatsukami", "jpn_oshihomimi", "direct", "Takamimusubi's daughter marries Ame-no-Oshihomimi"),
        E("jpn_susanoo", "jpn_oshihomimi", "expansion", "Okuninushi (descendant of Susanoo) cedes terrestrial rule to Ninigi (Kuni-yuzuri)"),
        E("jpn_oshihomimi", "jpn_hoori", "direct", "Ninigi + Konohanasakuya-hime -> Hoderi & Hoori -> Ugayafukiaezu"),
        E("jpn_hoori", "jk_jimmu", "direct", "Ugayafukiaezu + Tamayori-hime -> Emperor Jimmu"),
        E("jk_jimmu", "jpn_sujin_yamato", "direct", "Yamato Imperial Line -> Sujin -> Keiko -> Yamato Takeru"),
        E("jpn_sujin_yamato", "jpn_jingu_ojin", "direct", "Yamato Takeru -> Chuai (+ Empress Jingu) -> Ojin -> Nintoku -> Prince Shotoku"),
        E("kor_onjo_baekje", "jpn_jingu_ojin", "cognate", "Baekje Korea transmits Chinese script, Analects (Wani) & Buddhism to Yamato Japan (Emperor Ojin & Prince Shotoku)!"),
        E("chn_weizi_confucius", "jpn_jingu_ojin", "cognate", "Confucius's Analects transmitted via Baekje to Emperor Ojin's court in Japan (Kojiki/Nihon Shoki)"),
        E("ved_surya_vamsha", "jpn_jingu_ojin", "cognate", "Buddhist tradition (Siddhartha Gautama, Shakya/Ikshvaku line) enters Japan via Baekje & Prince Shotoku!"),
    ]

    return {"module": "11_korean_japanese", "title": "Exhaustive Ancient Korean & Japanese Genealogy (Samguk Yusa, Samguk Sagi, Kojiki & Nihon Shoki)", "nodes": nodes, "edges": edges}


def main():
    MODULES_DIR.mkdir(parents=True, exist_ok=True)
    old_asia = MODULES_DIR / "07_asia_steppe.json"
    if old_asia.exists():
        old_asia.unlink()

    modules = [
        load_existing_module("01_antediluvian"),
        load_existing_module("02_table_of_nations"),
        load_existing_module("03_abraham_all_nations"),
        load_existing_module("04_egypt_levant"),
        load_existing_module("05_mesopotamia"),
        load_existing_module("06_iranian_zoroastrian"),
        build_module_07_vedic_india(),
        load_existing_module("08_african_ethiopian"),
        load_existing_module("09_greek_mediterranean"),
        build_module_10_east_asia_chinese(),
        build_module_11_korean_japanese(),
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
            "title": "Ancient World Genealogy Atlas — Exhaustive Multi-Tradition Database (Phase 7)",
            "version": "7.0.0",
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
