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
          "Surya Vamsha (Solar Dynasty of Ayodhya)", ["Valmiki Ramayana", "Vishnu Purana IV", "Mahavamsa / Pali Canon"],
          "Son of Vaivasvata Manu. Produces Harishchandra, Bhagiratha, Raghu, and Prince Rama of Ayodhya. Buddhist chronicles (Mahavamsa, Ambattha Sutta) trace Siddhartha Gautama's Shakya clan to King Okkaka = Ikshvaku!", major=True),
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

    return {"module": "07_vedic_india", "title": "Vedic & Puranic Indian Genealogy (Core Foundation)", "nodes": nodes, "edges": edges}


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
            "title": "Ancient World Genealogy Atlas — Exhaustive Multi-Tradition Database (Phase 6)",
            "version": "6.0.0",
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
