"""
Module 29: Noahic & Biblical-Connected Bridges Across China, Persia, India,
Kashmir, Sri Lanka, Burma & Tibet.

Sources integrated:
- Al-Mas'udi, Meadows of Gold Vol. I (pp. 312-317, historicalencycl00masrich.pdf)
- Al-Tabari, History of Prophets and Kings (Vols. 1-2)
- John Jackson, Chronological Antiquities (1752)
- James Anderson, Royal Genealogies (1732 EPUB)
- Mirkhwand, Rawdat al-Safa (History of the Early Kings of Persia, b29318981.pdf p. 50)
- Kalhana's Rajatarangini Vol. I (M.A. Stein, 1900)
- Mahavamsa: Great Chronicle of Ceylon (Wilhelm Geiger, Ch. II-VII)
- Glass Palace Chronicle of the Kings of Burma (2015.99723.The-Glass-Palace-Chronicle-Of-The-Kings-Of-Burma.pdf)
- The Blue Annals (George N. Roerich, 2015.283021.The-Blue.pdf)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # 1. China from Noah (Al-Mas'udi, Cave of Treasures Yonton, Jackson 1752, Anderson 1732)
    nodes += [
        N("chn_masudi_abur_lotsatis", "'Abur (Amur) b. Japheth → Yarej → Na'ur → Lotsatis (1st King of China at Anku)", "chinese", 7,
          "Post-Flood Eastern Dispersion (Al-Mas'udi Vol. I pp. 312-313)",
          "Classical Arabic Japhethic Ancestry of the Early Sovereigns of China",
          ["Al-Mas'udi Meadows of Gold Vol. I pp. 312-313"],
          "Al-Mas'udi explicitly derives the Chinese sovereigns from Japheth b. Noah: 'The majority of the children of Abur followed the course of the river to the extremity of China... Their first king in this new settlement was Lotsatis ben Na'ur ben Yarej ben Abur ben Yafeth ben Nuh' at Anku.",
          ["'Abur b. Yafeth", "Lotsatis of China"], major=True),
        N("chn_masudi_successors", "'Arun → 'Abirun → 'Athinan → Jaraban (Early Noahic Chinese Monarchs of Mas'udi)", "chinese", 8,
          "Post-Lotsatis China (Al-Mas'udi Vol. I pp. 313-317)",
          "Early Chinese Dynasty in Al-Mas'udi's Universal Chronicle",
          ["Al-Mas'udi Meadows of Gold Vol. I pp. 313-317"],
          "Al-Mas'udi continues Lotsatis's lineage through 'Arun, 'Abirun, 'Athinan (bordering the Turks, descendants of his uncle), Jaraban (who sent ships to India & Babylon) & his temple-building lawgiver successor.",
          ["'Arun", "'Abirun", "'Athinan", "Jaraban"], major=False),
    ]
    edges += [
        E("bib_japheth", "chn_masudi_abur_lotsatis", "syncretic", "Al-Mas'udi Meadows of Gold Vol. I pp. 312-313: Majority of children of 'Abur b. Yafeth b. Nuh settled China; first king Lotsatis b. Na'ur b. Yarej b. 'Abur b. Japheth b. Noah"),
        E("chn_masudi_abur_lotsatis", "chn_fuxi_nuwa", "syncretic", "Cross-cultural chronicler synchronization of China's Noahic founding era"),
        E("chn_masudi_abur_lotsatis", "chn_masudi_successors", "expansion", "Al-Mas'udi Vol. I pp. 313-317: Successors of Lotsatis who initiated Chinese maritime trade to India & Babylon, temples & law codes"),
        E("syr_yonton_4th_son", "chn_fuxi_nuwa", "syncretic", "Cave of Treasures p. 143: Noah sent 4th son Yonton (Jonitus) to the Far East ('Land of the Rising Sun')"),
        E("bib_noah", "chn_fuxi_nuwa", "syncretic", "John Jackson 1752 Chronological Antiquities & James Anderson 1732: 18th-c. universal chronography identifying Chinese sovereign Fo-hi (Fuxi) with Noah"),
    ]

    # 2. Persia directly bridged from Adam, Shem/Lud & Japheth/Gomer/Madai
    edges += [
        E("bib_adam", "ir_gayomart", "syncretic", "Al-Tabari Vol. 1 p. 369 & Mirkhwand p. 50 (Imam Ghazali): Persian/Islamic chroniclers equating Gayomart (Kayumars) with Adam"),
        E("bib_lud", "ir_gayomart", "syncretic", "Mirkhwand p. 50 & Al-Mas'udi p. 77: Persian historians identifying Gayomart with Umaym b. Lud b. Aram b. Shem b. Noah"),
        E("bib_gomer", "ir_gayomart", "syncretic", "Al-Tabari Vol. 2 p. 15 & Mirkhwand p. 50: Genealogy tracing Persian kings back to Jayumart / Gomer b. Japheth b. Noah"),
        E("bib_madai", "ir_cyrus", "syncretic", "Al-Tabari Vol. 2 p. 15: Cyrus the Mede, conqueror of Belshazzar, descended from Madai b. Japheth"),
    ]

    # 3. India, Kashmir, Sri Lanka, Burma & Tibet from Noah
    nodes += [
        N("ind_hind_sind_noah", "Hind & Sind (Progenitors of India & Sindh in Tabari & Mas'udi)", "vedic", 7,
          "Post-Flood South Asia (Al-Tabari Vol. 2 pp. 15-17; Al-Mas'udi)",
          "Noahic Anchors of India & Sindh via Ham (Cush) and Shem (Joktan)",
          ["Al-Tabari Vol. 2 pp. 15, 17", "Al-Mas'udi Meadows of Gold"],
          "Al-Tabari records both major traditions linking India to Noah: (1) Indians & Sindis descending from Ham -> Cush/Canaan (p. 15), and (2) Ibn 'Abbas & Hisham al-Kalbi's line Shem -> Arphaxad -> Shelah -> Eber -> Qahtan (Joktan) -> Buqayin, father of Hind & Sind (p. 17).",
          ["Hind", "Sind", "Buqayin b. Qahtan"], major=True),
        N("ind_mahasammata_okkaka", "King Mahāsammata (= Manu) → Okkaka (= Ikshvaku) → Śākya Royal Stem", "vedic", 8,
          "Pali & Buddhist Royal Stem (Mahavamsa Ch. II p. 80)",
          "Solar-Buddhist Dynastic Bridge Linking India, Sri Lanka, Burma & Tibet",
          ["Mahavamsa Ch. II p. 80 (Geiger)", "Glass Palace Chronicle of Burma", "The Blue Annals"],
          "The Pali Mahavamsa opens its royal pedigree with first elected king Mahāsammata (cognate of Manu) -> Roja -> Mandhatar -> Okkaka (Pali form of Solar Dynasty founder Ikshvaku!) -> the Śākya clan of Kapilavastu.",
          ["Mahāsammata", "Okkaka (= Ikshvaku)"], major=True),
        N("kas_gonanda_ashoka", "Kashmir Kings (Kalhana's Rajatarangini): Gonanda I (Kurukshetra) → Ashoka of Kashmir", "vedic", 14,
          "Kurukshetra to 3rd c. BCE (Kalhana's Rajatarangini Book I)",
          "Historical Kashmiri Dynasty Synchronized with Pandavas & Emperor Ashoka",
          ["Kalhana's Rajatarangini Vol. 1 (M.A. Stein 1900)"],
          "Kalhana's Rajatarangini begins Kashmir's royal chronology at the Kurukshetra War under Gonanda I (contemporary of the Pandavas) and directly includes Emperor Ashoka (who exchanged envoys with Ptolemy II of Egypt!).",
          ["Gonanda I", "Jalauka", "Ashoka in Kashmir"], major=True),
        N("ceylon_vijaya_mahinda", "Sri Lanka (Mahavamsa): Prince Vijaya (1st King of Lanka, 543 BCE) & Thera Mahinda (Son of Ashoka)", "vedic", 14,
          "543–247 BCE (Mahavamsa Ch. II-VII, XIII)",
          "Founding Sinhalese Dynasty & Mauryan Buddhist Mission to Lanka",
          ["Mahavamsa (Geiger Ch. II, VI-VII, XIII)"],
          "The Mahavamsa connects Sri Lanka's first monarch Vijaya (landing on the exact day of Buddha's Parinirvana) -> Devanampiya Tissa with Emperor Ashoka's own son Mahinda and daughter Sanghamitta.",
          ["King Vijaya", "Devanampiya Tissa", "Mahinda & Sanghamitta"], major=True),
        N("burma_abhiraza_tagaung", "Burma (Glass Palace Chronicle): King Abhiraza (Śākya Prince of Kapilavastu → Founder of Tagaung)", "vedic", 13,
          "Ancient Tagaung Era (Glass Palace Chronicle)",
          "Burmese Royal Origin Descended from Mahāsammata & Okkaka / Śākya",
          ["Glass Palace Chronicle of the Kings of Burma (Pe Maung Tin & Luce)"],
          "The Hmannan Yazawin (Glass Palace Chronicle) traces the founding kings of Burma to Śākya prince Abhiraza, descendant of Mahāsammata and Okkaka (Ikshvaku), who marched from northern India to build Tagaung.",
          ["Abhiraza of Tagaung", "Pyusawhti"], major=True),
        N("tib_nyatri_songtsen", "Tibet (The Blue Annals): Nyatri Tsenpo (1st Yarlung King, Śākya/Licchavi Stem) → Songtsen Gampo", "vedic", 19,
          "Ancient Yarlung to 7th c. CE (Roerich The Blue Annals Book I)",
          "Tibetan Royal Lineage Derived from India's Śākya / Licchavi House",
          ["The Blue Annals (Deb-ther sngon-po, George Roerich tr., Book I)"],
          "'Gos Lo-tsā-ba's Blue Annals Book I opens the Royal Chronicle of Tibet with the Indian Śākya/Licchavi origin of Tibet's first king Nyatri Tsenpo (gNya'-khri btsan-po) descending to Buddhist unifier Songtsen Gampo.",
          ["Nyatri Tsenpo", "Songtsen Gampo"], major=True),
    ]
    edges += [
        E("bib_cush", "ind_hind_sind_noah", "syncretic", "Al-Tabari Vol. 2 p. 15 & Al-Mas'udi: Indians (Hind) & Sindis descend from Ham b. Noah via Cush/Canaan"),
        E("bib_joktan", "ind_hind_sind_noah", "syncretic", "Al-Tabari Vol. 2 p. 17 (Ibn 'Abbas / Hisham al-Kalbi): Alternate tradition tracing Hind & Sind to Buqayin b. Qahtan (Joktan) b. Eber b. Shem"),
        E("ind_hind_sind_noah", "ved_vaivasvata_manu", "syncretic", "Chronicler bridge linking Noahic Hind/Sind to India's Great Flood survivor Vaivasvata Manu"),
        E("bib_noah", "ved_vaivasvata_manu", "syncretic", "Great Flood survivor Vaivasvata Manu (Shatapatha Brahmana / Matsya Purana) — classic Noahic cognate"),
        E("ved_vaivasvata_manu", "ind_mahasammata_okkaka", "cognate", "Mahavamsa Ch. II p. 80 & Glass Palace Chronicle: Buddhist royal stem from first king Mahāsammata -> Okkaka (Ikshvaku) -> Śākya clan"),
        E("ind_mahasammata_okkaka", "ved_buddha", "direct", "Okkaka / Ikshvaku -> Śākya clan -> King Shuddhodana -> Siddhartha Gautama Buddha"),
        E("ved_maurya_ashoka", "kas_gonanda_ashoka", "cognate", "Kalhana's Rajatarangini Book I (Stein): Kashmir chronology anchored to Pandavas/Kurukshetra & Emperor Ashoka (who links historically to Ptolemy II!)"),
        E("ved_buddha", "ceylon_vijaya_mahinda", "expansion", "Mahavamsa Ch. II-VII: Vijaya arrives on the day of Buddha's Parinirvana; Mahinda son of Ashoka brings Buddhism to Lanka"),
        E("ved_maurya_ashoka", "ceylon_vijaya_mahinda", "direct", "Son Mahinda & daughter Sanghamitta of Emperor Ashoka"),
        E("ind_mahasammata_okkaka", "burma_abhiraza_tagaung", "expansion", "Glass Palace Chronicle of the Kings of Burma: Traces Burmese kings directly to Śākya prince Abhiraza, descendant of Mahāsammata & Okkaka/Ikshvaku"),
        E("ind_mahasammata_okkaka", "tib_nyatri_songtsen", "expansion", "Roerich The Blue Annals Book I (Royal Chronicle of Tibet): Traces 1st Tibetan king Nyatri Tsenpo to the Indian Śākya/Licchavi lineage of Mahāsammata & Ikshvaku"),
    ]

    return {
        "module": "29_asia_china_india_persia_noahic",
        "title": "Noahic Lineages of China, Persia, India, Kashmir, Sri Lanka, Burma & Tibet",
        "nodes": nodes,
        "edges": edges,
    }
