"""
Module 50: Wave 8 Person-by-Person Expansion Across Byzantium, Goths, Merovingian Franks,
Kashmir (Rajatarangini), Sri Lanka (Mahavamsa), Burma (Glass Palace Chronicle), Tibet (Blue Annals),
Ottoman Sultans/Valide Sultans & Midrashic-Arabic Chronicles (Pirkei de-Rabbi Eliezer & Kitab al-Magall).
"""

from . import N, E


def add_chain(nodes, edges, parent_id, items, tradition, era_default, sources, default_type="direct"):
    prev = parent_id
    for item in items:
        nid, name, tier = item[0], item[1], item[2]
        era = item[3] if len(item) > 3 else era_default
        role = item[4] if len(item) > 4 else "Sovereign / Royal Lineage"
        notes = item[5] if len(item) > 5 else f"Chronicle succession in {', '.join(sources)}."
        major = item[6] if len(item) > 6 else False
        nodes.append(N(nid, name, tradition, tier, era, role, sources, notes, major=major))
        if prev:
            edges.append(E(prev, nid, default_type, f"{', '.join(sources)}: succession"))
        prev = nid


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # SECTION A: COMPLETE BYZANTINE & LATE ROMAN IMPERIAL DYNASTIES (~28 nodes)
    # =========================================================================
    add_chain(nodes, edges, "mon_rom_constantine1", [
        ("byz8_constantius2", "Emperor Constantius II (Son of Constantine the Great, 337–361 CE)", 19, "317–361 CE", "Roman Emperor"),
        ("byz8_valentinian1", "Emperor Valentinian I (Founder of Valentinian Dynasty, 364–375 CE)", 19, "321–375 CE", "Western Roman Emperor"),
        ("byz8_valens", "Emperor Valens (Eastern Roman Emperor, 364–378 CE; Battle of Adrianople)", 19, "328–378 CE", "Eastern Roman Emperor"),
        ("byz8_gratian", "Emperor Gratian (Son of Valentinian I, 367–383 CE)", 19, "359–383 CE", "Western Roman Emperor"),
    ], "greek", "4th c. CE", ["Ammianus Marcellinus", "Echard Roman History Vol. 4"])
    edges.append(E("byz8_valentinian1", "mon_rom_theodosius1", "expansion", "Theodosius I married Galla, daughter of Valentinian I"))

    add_chain(nodes, edges, "rom3_arcadius", [
        ("byz8_theodosius2", "Emperor Theodosius II (Codex Theodosianus & Theodosian Walls, 408–450 CE)", 19, "401–450 CE", "Eastern Roman Emperor"),
        ("byz8_pulcheria_marcian", "Empress St. Pulcheria (+ Emperor Marcian; Council of Chalcedon 451 CE)", 19, "399–457 CE", "Eastern Roman Augusta & Emperor"),
        ("byz8_leo1_zeno", "Emperor Leo I the Thracian → Emperor Zeno & Ariadne (457–491 CE)", 19, "457–491 CE", "Leonid Dynasty Emperors"),
    ], "greek", "5th c. CE", ["Echard Roman History Vol. 4", "Chronicon Paschale"])

    nodes += [
        N("byz8_justin1", "Emperor Justin I (Uncle of Justinian I, 518–527 CE)", "greek", 19, "450–527 CE", "Founder of Justinianic Dynasty", ["Echard Roman History Vol. 4", "Procopius"], "Imperial commander elevated after Anastasius I; mentor and uncle of Justinian I."),
        N("byz8_justin2_maurice", "Emperor Justin II → Tiberius II → Emperor Maurice (565–602 CE)", "greek", 19, "565–602 CE", "Late Justinianic Emperors", ["Echard Roman History Vol. 4", "Chronicon Paschale"], "Nephew Justin II and generals Tiberius II & Maurice, whose daughter Maria wed Khosrow II of Persia."),
    ]
    edges += [
        E("byz8_leo1_zeno", "byz8_justin1", "expansion", "Late Roman imperial transition (Leo I / Anastasius I -> Justin I)"),
        E("byz8_justin1", "mon_rom_justinian1", "direct", "Uncle and adoptive father of Emperor Justinian I"),
        E("mon_rom_justinian1", "byz8_justin2_maurice", "direct", "Nephew-to-son-in-law imperial succession"),
    ]

    add_chain(nodes, edges, "mon_rom_heraclius", [
        ("byz8_constans2", "Emperor Constans II (Grandson of Heraclius, 641–668 CE)", 19, "630–668 CE", "Heraclian Emperor"),
        ("byz8_constantine4", "Emperor Constantine IV Pogonatos (First Arab Siege of Constantinople, 668–685 CE)", 19, "652–685 CE", "Heraclian Emperor"),
        ("byz8_justinian2", "Emperor Justinian II Rhinotmetos (685–711 CE)", 19, "668–711 CE", "Last Heraclian Emperor"),
    ], "greek", "7th–8th c. CE", ["Echard Roman History Vol. 4", "Theophanes"])

    add_chain(nodes, edges, "mon_rom_leo3", [
        ("byz8_constantine5", "Emperor Constantine V Kopronymos (Son of Leo III, 741–775 CE)", 19, "718–775 CE", "Isaurian Emperor"),
        ("byz8_irene_athens", "Empress Irene of Athens (First Sole Female Byzantine Emperor, 797–802 CE)", 19, "c. 752–803 CE", "Byzantine Empress Regnant", "Restored icons (Nicaea II, 787 CE); exchanged marriage embassy with Charlemagne.", True),
        ("byz8_theophilos_michael3", "Emperor Theophilos → Emperor Michael III (Amorian Dynasty, 829–867 CE)", 19, "829–867 CE", "Amorian Emperors"),
    ], "greek", "8th–9th c. CE", ["Echard Roman History Vol. 5"])
    edges.append(E("byz8_irene_athens", "mon_fra_charlemagne", "expansion", "802 CE Imperial Marriage Proposal between Empress Irene and Emperor Charlemagne"))

    add_chain(nodes, edges, "mon_rom_basil1", [
        ("byz8_leo6_wise", "Emperor Leo VI the Wise (Basilika Law Code, 886–912 CE)", 19, "866–912 CE", "Macedonian Emperor"),
        ("byz8_constantine7", "Emperor Constantine VII Porphyrogenitos (De Administrando Imperio, 913–959 CE)", 20, "905–959 CE", "Scholar Emperor"),
        ("byz8_romanos2", "Emperor Romanos II (+ Theophano; Father of Basil II, Anna & Theophanu, 959–963 CE)", 20, "938–963 CE", "Macedonian Emperor"),
    ], "greek", "9th–10th c. CE", ["Echard Roman History Vol. 5", "De Administrando Imperio"])
    nodes += [
        N("byz8_constantine8", "Emperor Constantine VIII (Brother of Basil II, 1025–1028 CE)", "greek", 20, "960–1028 CE", "Macedonian Emperor", ["Echard Roman History Vol. 5"], "Younger son of Romanos II."),
        N("byz8_empress_zoe_theodora", "Empresses Zoë Porphyrogenita & Theodora (Final Macedonian Heiresses, 1028–1056 CE)", "greek", 20, "978–1056 CE", "Macedonian Empresses Regnant", ["Echard Roman History Vol. 5"], "Daughters of Constantine VIII."),
        N("byz8_anna_porphyrogenita", "Princess Anna Porphyrogenita (+ St. Vladimir the Great of Kiev, 988 CE)", "greek", 20, "963–1011 CE", "Byzantine Princess & Grand Princess of Kiev", ["Russian Primary Chronicle", "Echard Roman History Vol. 5"], "Sister of Emperor Basil II whose marriage to St. Vladimir Christianized Kievan Rus' and connected Byzantium directly into Europe's royal houses.", True),
        N("byz8_theophanu_hre", "Empress Theophanu (+ Holy Roman Emperor Otto II, Mother of Otto III)", "greek", 20, "c. 955–991 CE", "Holy Roman Empress & Regent", ["Echard Roman History Vol. 5", "Thietmar of Merseburg"], "Byzantine imperial princess married to Otto II in 972 CE, transmitting Eastern imperial blood to the Ottonians.", True),
        N("byz8_otto2_otto3", "Emperors Otto II (+ Theophanu) → Emperor Otto III of the Holy Roman Empire", "europe_norse", 20, "955–1002 CE", "Holy Roman Emperors", ["Modern Universal History Vol. 10"], "Son & grandson of Otto I connecting Byzantine & Ottonian crowns."),
    ]
    edges += [
        E("byz8_romanos2", "mon_rom_basil2", "direct", "Father-to-son Macedonian succession"),
        E("byz8_romanos2", "byz8_constantine8", "direct", "Son of Romanos II"),
        E("byz8_constantine8", "byz8_empress_zoe_theodora", "direct", "Daughters of Constantine VIII"),
        E("byz8_romanos2", "byz8_anna_porphyrogenita", "direct", "Daughter of Romanos II & sister of Basil II"),
        E("byz8_anna_porphyrogenita", "rus_vladimir_great", "direct", "988 CE Royal Marriage: Anna Porphyrogenita & St. Vladimir of Kiev"),
        E("byz8_romanos2", "byz8_theophanu_hre", "expansion", "Byzantine Macedonian / Skleraina imperial niece"),
        E("mon_hre_otto1", "byz8_otto2_otto3", "direct", "Son Otto II & grandson Otto III of Otto the Great"),
        E("byz8_theophanu_hre", "byz8_otto2_otto3", "expansion", "972 CE Imperial Marriage: Byzantine Princess Theophanu & Emperor Otto II"),
    ]

    add_chain(nodes, edges, "mon_rom_alexios1", [
        ("byz8_john2_komnenos", "Emperor John II Komnenos (Son of Alexios I, 1118–1143 CE)", 20, "1087–1143 CE", "Komnenian Emperor"),
        ("byz8_manuel1_komnenos", "Emperor Manuel I Komnenos (1143–1180 CE)", 20, "1118–1180 CE", "Komnenian Emperor"),
        ("byz8_andronikos1_isaac2", "Emperors Andronikos I Komnenos & Isaac II Angelos → Alexios III", 20, "1183–1204 CE", "Komnenoi & Angeloi Emperors"),
        ("byz8_theodore1_laskaris", "Emperor Theodore I Laskaris (Empire of Nicaea, 1205–1221 CE)", 20, "c. 1175–1221 CE", "Founder of Nicaean Empire"),
    ], "greek", "12th–13th c. CE", ["Echard Roman History Vol. 5", "Choniates"])
    nodes.append(N("byz8_maria_komnene_jerusalem", "Queen Maria Komnene of Jerusalem (Grandniece of Manuel I; Wed King Amalric I)", "greek", 20, "c. 1154–1217 CE", "Queen of Jerusalem", ["William of Tyre", "Echard Vol. 5"], "Married King Amalric I of Jerusalem; mother of Queen Isabella I, uniting Komnenian & Crusader royal blood."))
    edges += [
        E("byz8_manuel1_komnenos", "byz8_maria_komnene_jerusalem", "expansion", "Great-uncle of Queen Maria Komnene of Jerusalem (+ King Amalric I)"),
        E("byz8_theodore1_laskaris", "mon_rom_michael8", "expansion", "Empire of Nicaea -> Palaiologan restoration of Constantinople (1261)"),
    ]

    add_chain(nodes, edges, "mon_rom_michael8", [
        ("byz8_andronikos2", "Emperor Andronikos II Palaiologos (1282–1328 CE)", 20, "1259–1332 CE", "Palaiologan Emperor"),
        ("byz8_john5_palaiologos", "Emperor John V Palaiologos (1341–1391 CE)", 20, "1332–1391 CE", "Palaiologan Emperor"),
        ("byz8_manuel2_palaiologos", "Emperor Manuel II Palaiologos (Diplomatic Tour to London & Paris, 1391–1425 CE)", 21, "1350–1425 CE", "Palaiologan Emperor"),
        ("byz8_john8_palaiologos", "Emperor John VIII Palaiologos (Council of Florence, 1425–1448 CE)", 21, "1392–1448 CE", "Palaiologan Emperor"),
    ], "greek", "13th–15th c. CE", ["Echard Roman History Vol. 5"])
    nodes += [
        N("byz8_thomas_palaiologos", "Despot Thomas Palaiologos of the Morea (Brother of Constantine XI; Father of Zoe/Sophia)", "greek", 21, "1409–1465 CE", "Despot of the Morea", ["Echard Roman History Vol. 5"], "Younger son of Manuel II; carried Byzantine imperial inheritance to Rome & Moscow via daughter Sophia."),
        N("byz8_john6_kantakouzenos", "Emperor John VI Kantakouzenos (1347–1354 CE)", "greek", 20, "c. 1292–1383 CE", "Byzantine Emperor", ["Echard Vol. 5", "Knolles Turkish History"], "Father-in-law of John V Palaiologos & Ottoman Sultan Orhan Ghazi."),
        N("byz8_theodora_kantakouzene", "Princess Theodora Kantakouzene (+ Ottoman Sultan Orhan Ghazi, 1346 CE)", "greek", 20, "c. 1330–1396 CE", "Byzantine Princess & Ottoman Hatun", ["Kantakouzenos Historia", "Knolles Turkish History"], "1346 CE royal marriage between Byzantine Princess Theodora and Sultan Orhan, joining Palaiologan-Kantakouzenos & Ottoman lines.", True),
    ]
    edges += [
        E("byz8_manuel2_palaiologos", "byz8_thomas_palaiologos", "direct", "Son of Emperor Manuel II Palaiologos"),
        E("byz8_manuel2_palaiologos", "mon_rom_constantine11", "direct", "Son of Emperor Manuel II Palaiologos"),
        E("byz8_thomas_palaiologos", "roy6_sophia_palaiologina", "direct", "Father of Zoe / Sophia Palaiologina (+ Ivan III of Moscow)"),
        E("byz8_john5_palaiologos", "byz8_john6_kantakouzenos", "expansion", "Byzantine co-emperorship & marriage alliance"),
        E("byz8_john6_kantakouzenos", "byz8_theodora_kantakouzene", "direct", "Daughter of Emperor John VI Kantakouzenos"),
        E("byz8_theodora_kantakouzene", "mon_ott_orhan", "expansion", "1346 CE Royal Marriage: Theodora Kantakouzene wed Ottoman Sultan Orhan Ghazi"),
    ]

    # =========================================================================
    # SECTION B: AMALI OSTROGOTHS, BALTI VISIGOTHS & MEROVINGIAN FRANKS (~26 nodes)
    # =========================================================================
    add_chain(nodes, edges, "goth_amali_theoderic", [
        ("got8_ostrogotha", "King Ostrogotha → Kniva (Early Gothic Monarchs of Scythia & Moesia)", 18, "c. 240–270 CE", "Amali Gothic Founders"),
        ("got8_ermanaric", "King Ermanaric the Great (Oium Gothic Empire on Dnieper & Black Sea, d. 376 CE)", 19, "d. 376 CE", "Amali High King"),
        ("got8_valamir_theodemir", "King Valamir & King Theodemir (+ Ereleuva; Parents of Theoderic)", 19, "5th c. CE", "Amali Ostrogothic Brothers"),
        ("got8_theodoric_great", "King Theoderic the Great of Italy (+ Audofleda, Sister of Clovis I, 493–526 CE)", 19, "454–526 CE", "King of the Ostrogoths & Italy", "Raised hostage at Constantinople; defeated Odoacer; married Clovis I's sister Audofleda.", True),
        ("got8_amalasuntha", "Queen Amalasuntha of the Ostrogoths (+ Eutharic; Daughter of Theoderic, d. 535 CE)", 19, "c. 495–535 CE", "Ostrogothic Queen Regent"),
        ("got8_totila", "King Totila / Baduila (Gothic Resistance vs Justinian & Belisarius, 541–552 CE)", 19, "d. 552 CE", "King of the Ostrogoths"),
    ], "europe_norse", "3rd–6th c. CE", ["Jordanes Getica", "Modern Universal History Vol. 8"])
    edges += [
        E("got8_theodoric_great", "mon_fra_clovis1", "expansion", "493 CE Royal Marriage: Theoderic the Great wed Audofleda, sister of King Clovis I"),
        E("got8_totila", "mon_rom_justinian1", "expansion", "Gothic War (535–554 CE): Totila vs Justinian I & Belisarius"),
    ]

    add_chain(nodes, edges, "goth_amali_theoderic", [
        ("got8_alaric1", "King Alaric I of the Visigoths (Balti Dynasty; Sack of Rome 410 CE)", 19, "c. 370–410 CE", "1st King of the Visigoths", "Balti dynasty king who captured Rome in 410 CE.", True),
        ("got8_ataulf", "King Ataulf (+ Empress Galla Placidia, 410–415 CE)", 19, "r. 410–415 CE", "King of the Visigoths"),
        ("got8_theodoric1_visigoth", "King Theodoric I of Toulouse (Fell at Chalons vs Attila, 418–451 CE)", 19, "r. 418–451 CE", "Visigothic King of Toulouse"),
        ("got8_euric", "King Euric (Code of Euric, 466–484 CE)", 19, "c. 440–484 CE", "Visigothic King"),
        ("got8_alaric2", "King Alaric II (+ Thiudigotho, Daughter of Theoderic the Great, 484–507 CE)", 19, "r. 484–507 CE", "Visigothic King"),
        ("got8_leovigild", "King Leovigild of Toledo (Unified Visigothic Spain, 568–586 CE)", 19, "519–586 CE", "Visigothic King of Spain"),
        ("got8_wamba_witiza", "Kings Wamba, Erwig, Egica & Witiza (Late Visigothic Spain, 672–710 CE)", 19, "672–710 CE", "Late Visigothic Kings"),
    ], "europe_norse", "4th–8th c. CE", ["Jordanes Getica", "Mariana General History of Spain 1699"])
    edges += [
        E("got8_ataulf", "rom3_galla_placidia", "direct", "414 CE Marriage: King Ataulf & Roman Princess Galla Placidia"),
        E("got8_theodoric_great", "got8_alaric2", "expansion", "Marriage of Alaric II to Thiudigotho, daughter of Theoderic the Great"),
        E("got8_leovigild", "mon_esp_reccared1", "direct", "Father of King Reccared I of the Visigoths"),
        E("got8_wamba_witiza", "mon_esp_roderick", "expansion", "Late Visigothic succession to King Roderick"),
    ]

    add_chain(nodes, edges, "eur_greg_merovingians", [
        ("mer8_merovech", "King Merovech / Merovaeus (Eponym of the Merovingian Franks, fl. 448–457 CE)", 18, "c. 411–457 CE", "Merovingian Founder"),
        ("mer8_childeric1", "King Childeric I (+ Queen Basina; Tomb at Tournai, d. 481 CE)", 19, "c. 437–481 CE", "Salic Frankish King"),
    ], "europe_norse", "5th c. CE", ["Gregory of Tours History of the Franks"])
    nodes += [
        N("mer8_clotilde_burgundy", "Queen St. Clotilde of Burgundy (+ King Clovis I; Christianized the Franks)", "europe_norse", 19, "c. 475–545 CE", "Queen of the Franks", ["Gregory of Tours"], "Burgundian princess whose marriage to Clovis I led to the conversion of the Frankish kingdom."),
        N("mer8_theuderic1", "King Theuderic I of Austrasia / Reims (Eldest Son of Clovis I, 511–534 CE)", "europe_norse", 19, "c. 485–534 CE", "Merovingian King of Austrasia", ["Gregory of Tours"], "Son of Clovis I."),
        N("mer8_childebert1", "King Childebert I of Paris (Son of Clovis I & Clotilde, 511–558 CE)", "europe_norse", 19, "c. 496–558 CE", "Merovingian King of Paris", ["Gregory of Tours"], "Son of Clovis I & St. Clotilde."),
        N("mer8_sigebert1", "King Sigebert I of Austrasia (Son of Chlothar I, 561–575 CE)", "europe_norse", 19, "c. 535–575 CE", "Merovingian King", ["Gregory of Tours"], "Married Visigothic princess Brunhilda."),
        N("mer8_brunhilda_visigoth", "Queen Brunhilda of Austrasia (Visigothic Princess; Rival of Fredegund, d. 613 CE)", "europe_norse", 19, "c. 543–613 CE", "Visigothic Princess & Frankish Queen Regent", ["Gregory of Tours", "Fredegar"], "Daughter of Visigothic King Athanagild; dominated Merovingian politics for 45 years.", True),
        N("mer8_childebert2", "King Childebert II of Austrasia & Burgundy (Son of Sigebert I & Brunhilda, 575–596 CE)", "europe_norse", 19, "570–596 CE", "Merovingian King", ["Gregory of Tours"], "Son of Sigebert I & Brunhilda."),
        N("mer8_chilperic1", "King Chilperic I of Neustria (Son of Chlothar I, 561–584 CE)", "europe_norse", 19, "c. 539–584 CE", "Merovingian King of Soissons", ["Gregory of Tours"], "Husband of Queen Fredegund; father of Chlothar II."),
        N("mer8_fredegund", "Queen Fredegund of Neustria (Mother of Chlothar II, d. 597 CE)", "europe_norse", 19, "d. 597 CE", "Frankish Queen Regent", ["Gregory of Tours"], "Arch-rival of Brunhilda; secured the Frankish throne for her son Chlothar II.", True),
        N("mer8_chlothar2", "King Chlothar II the Great (Reunited All Frankish Kingdoms 613 CE; Father of Dagobert I)", "europe_norse", 19, "584–629 CE", "King of All the Franks", ["Gregory of Tours", "Fredegar"], "Son of Chilperic I & Fredegund; reunited the Merovingian realm."),
        N("mer8_childeric3", "King Childeric III (Final Merovingian King, Deposed 751 CE by Pepin the Short)", "europe_norse", 19, "c. 717–754 CE", "Last Merovingian King", ["Royal Frankish Annals", "Mézeray 1683"], "Last Merovingian monarch before the Carolingian accession."),
        N("mer8_pepin_landen", "St. Pepin of Landen (+ St. Arnulf of Metz; Pippinid Ancestor, d. 640 CE)", "europe_norse", 19, "c. 580–640 CE", "Mayor of the Palace of Austrasia", ["Fredegar", "Mézeray 1683"], "Advisor to Chlothar II & Dagobert I; grandfather of Pepin of Herstal."),
        N("mer8_pepin_herstal", "Pepin of Herstal (Duke of the Franks; Father of Charles Martel, d. 714 CE)", "europe_norse", 19, "c. 635–714 CE", "Mayor of the Palace", ["Mézeray 1683", "Modern Universal History Vol. 9"], "United Austrasia & Neustria at Tertry (687 CE); father of Charles Martel."),
    ]
    edges += [
        E("mer8_childeric1", "mon_fra_clovis1", "direct", "Father of King Clovis I"),
        E("mon_fra_clovis1", "mer8_clotilde_burgundy", "direct", "Royal Marriage: Clovis I & St. Clotilde of Burgundy"),
        E("mon_fra_clovis1", "mer8_theuderic1", "direct", "Son of Clovis I"),
        E("mon_fra_clovis1", "mer8_childebert1", "direct", "Son of Clovis I & Clotilde"),
        E("mon_fra_chlothar1", "mer8_sigebert1", "direct", "Son of Chlothar I"),
        E("mer8_sigebert1", "mer8_brunhilda_visigoth", "direct", "Marriage of Sigebert I & Visigothic Princess Brunhilda"),
        E("esp_visigoths_reccared_roderick", "mer8_brunhilda_visigoth", "expansion", "Daughter of Visigothic King Athanagild"),
        E("mer8_brunhilda_visigoth", "mer8_childebert2", "direct", "Son of Sigebert I & Brunhilda"),
        E("mon_fra_chlothar1", "mer8_chilperic1", "direct", "Son of Chlothar I"),
        E("mer8_chilperic1", "mer8_fredegund", "direct", "Marriage of Chilperic I & Queen Fredegund"),
        E("mer8_fredegund", "mer8_chlothar2", "direct", "Son of Chilperic I & Fredegund"),
        E("mer8_chlothar2", "mon_fra_dagobert1", "direct", "Father of King Dagobert I"),
        E("mon_fra_dagobert1", "mer8_childeric3", "direct", "Late Merovingian royal descent to Childeric III"),
        E("mer8_chlothar2", "mer8_pepin_landen", "expansion", "Austrasian mayor under Chlothar II"),
        E("mer8_pepin_landen", "mer8_pepin_herstal", "direct", "Grandson (Arnulfing-Pippinid union)"),
        E("mer8_pepin_herstal", "mon_fra_charles_martel", "direct", "Father of Charles Martel"),
    ]

    # =========================================================================
    # SECTION C: KASHMIR, SRI LANKA, BURMA & TIBET (~35 nodes)
    # =========================================================================
    add_chain(nodes, edges, "kas_gonanda_ashoka", [
        ("kas8_jalauka", "King Jalauka of Kashmir (Son of Emperor Ashoka in Rajatarangini Book I)", 15, "3rd c. BCE", "King of Kashmir"),
        ("kas8_kanishka_kashmir", "Hushka, Jushka & Kanishka of Kashmir (Turushka Kings, Rajatarangini I.168)", 17, "1st–2nd c. CE", "Kushan Kings of Kashmir"),
        ("kas8_meghavahana", "King Meghavahana (Restorer of Gonanda Dynasty in Kashmir)", 18, "5th c. CE", "Gonandiya King of Kashmir"),
        ("kas8_pravarasena2", "King Pravarasena II (Founder of Pravarapura / Srinagar, 6th c. CE)", 19, "6th c. CE", "King of Kashmir"),
        ("kas8_durlabhavardhana", "King Durlabhavardhana (Founder of Karkota Dynasty, Visited by Xuanzang, 625 CE)", 19, "r. 625–661 CE", "Founder of Karkota Dynasty"),
        ("kas8_lalitaditya", "Emperor Lalitaditya Muktapida (Martand Sun Temple; Pan-Indian Empire, 724–760 CE)", 19, "r. 724–760 CE", "Great Emperor of Kashmir", "Most celebrated Karkota conqueror in Kalhana's Rajatarangini Book IV.", True),
        ("kas8_avantivarman", "King Avantivarman (Founder of Utpala Dynasty & Avantipur Temples, 855–883 CE)", 19, "r. 855–883 CE", "Founder of Utpala Dynasty"),
        ("kas8_queen_didda", "Queen Didda of Kashmir (Sovereign Queen Regnant, 958–1003 CE)", 20, "c. 924–1003 CE", "Sovereign Queen of Kashmir", "Ruled Kashmir for nearly 45 years; scion of Lohara & Hindu Shahi houses.", True),
        ("kas8_sangramaraja", "King Sangramaraja (Nephew of Queen Didda; Founder of Lohara Dynasty, 1003–1028 CE)", 20, "r. 1003–1028 CE", "Founder of Lohara Dynasty"),
        ("kas8_kota_rani_shah_mir", "Queen Kota Rani → Sultan Shah Mir (14th c. Kashmir Transition)", 20, "14th c. CE", "Final Hindu Queen & Shah Mir Founder"),
    ], "vedic", "3rd c. BCE – 14th c. CE", ["Kalhana's Rajatarangini (M.A. Stein 1900)"])
    edges.append(E("kas8_kota_rani_shah_mir", "chr6_mirza_haidar_dughlat", "expansion", "Kashmir sultanate period preceding Mirza Haidar Dughlat (1540)"))

    add_chain(nodes, edges, "ind5_pandukabhaya", [
        ("lka8_devanampiya_tissa", "King Devanampiya Tissa of Anuradhapura (Buddhist Envoy of Ashoka, 250–210 BCE)", 15, "r. 250–210 BCE", "King of Sri Lanka"),
        ("lka8_dutthagamani", "King Dutthagamani / Dutugemunu (Hero of Mahavamsa, 161–137 BCE)", 17, "r. 161–137 BCE", "Great Unifier of Lanka", "Reunified Sri Lanka; central hero of the Mahavamsa.", True),
        ("lka8_vattagamani", "King Vattagamani Abhaya / Valagamba (Writing of the Pali Canon, 89–77 BCE)", 17, "r. 89–77 BCE", "King of Sri Lanka"),
        ("lka8_mahasena", "King Mahasena of Anuradhapura (Minneriya Tank & Jetavanaramaya, 277–304 CE)", 19, "r. 277–304 CE", "King of Sri Lanka"),
        ("lka8_kashyapa_sigiriya", "King Kashyapa I of Sigiriya (473–495 CE) & King Dhatusena", 19, "r. 473–495 CE", "Builder of Sigiriya Rock Fortress"),
        ("lka8_vijayabahu1", "King Vijayabahu I (Drove Out Cholas; Restored Polonnaruwa, 1055–1110 CE)", 20, "r. 1055–1110 CE", "King of Polonnaruwa"),
        ("lka8_parakramabahu1", "King Parakramabahu I the Great (Polonnaruwa Zenith, 1153–1186 CE)", 20, "r. 1153–1186 CE", "Great King of Sri Lanka", "Constructed Parakrama Samudra and sent expeditions to Burma and South India.", True),
        ("lka8_nissanka_malla", "King Nissanka Malla of Polonnaruwa (Kalinga Dynasty, 1187–1196 CE)", 20, "r. 1187–1196 CE", "King of Sri Lanka"),
    ], "vedic", "3rd c. BCE – 12th c. CE", ["Mahavamsa & Culavamsa (Geiger)"])
    edges += [
        E("ind5_mahendra_sanghamitta", "lka8_devanampiya_tissa", "expansion", "Mahavamsa XIII: Emperor Ashoka's children Mahinda & Sanghamitta brought Buddhism & Bodhi Sapling to Tissa"),
        E("ceylon_vijaya_mahinda", "lka8_devanampiya_tissa", "cognate", "Same Sinhalese founder dynasty"),
        E("lka8_vijayabahu1", "mon_ind_rajendra1", "expansion", "11th c. Chola–Sinhalese conflicts & Kalinga royal marriages"),
    ]

    add_chain(nodes, edges, "burma_abhiraza_tagaung", [
        ("bur8_pyusawhti", "King Pyusawhti (Early Legendary Lineage of Pagan, Glass Palace Chronicle)", 15, "2nd–3rd c. CE", "Early Pagan Ancestor"),
        ("bur8_anawrahta", "King Anawrahta of Pagan (1st Historical Unifier of Burma, 1044–1077 CE)", 20, "1014–1077 CE", "Founder of Pagan Empire", "Established Theravada Buddhism and unified Myanmar from Pagan.", True),
        ("bur8_kyansittha", "King Kyansittha of Pagan (Built Ananda Temple; Envoy to China, 1084–1112 CE)", 20, "r. 1084–1112 CE", "Emperor of Pagan"),
        ("bur8_alaungsithu", "King Alaungsithu / Sithu I (Grandson of Kyansittha, 1112–1167 CE)", 20, "1090–1167 CE", "Emperor of Pagan"),
        ("bur8_narathihapate", "King Narathihapate (Pagan Monarch During 1287 Mongol Campaigns)", 20, "1238–1287 CE", "Last Major Pagan King"),
        ("bur8_tabinshwehti", "King Tabinshwehti of Toungoo (Reunified Burma, 1530–1550 CE)", 21, "1516–1550 CE", "Toungoo Conqueror"),
        ("bur8_bayinnaung", "Emperor Bayinnaung Kyawhtin Nawrahta (Largest SE Asian Empire, 1550–1581 CE)", 21, "1516–1581 CE", "Toungoo Emperor", "Built the largest empire in Southeast Asian history across Burma, Shan States, Lan Na & Ayutthaya.", True),
        ("bur8_alaungpaya", "King Alaungpaya (Founder of Konbaung Dynasty, 1752–1760 CE)", 21, "1714–1760 CE", "Founder of Konbaung Dynasty"),
        ("bur8_mindon_min", "King Mindon Min (Founded Mandalay; 5th Buddhist Council, 1853–1878 CE)", 21, "1808–1878 CE", "Konbaung King of Mandalay"),
        ("bur8_king_thibaw", "King Thibaw Min & Queen Supayalat (Final Burmese Monarch, r. 1878–1885 CE)", 21, "1859–1916 CE", "Last King of Burma"),
    ], "southeast_asia", "2nd c. CE – 1885 CE", ["Glass Palace Chronicle of the Kings of Burma (Hmannan Yazawin)"])
    edges += [
        E("bur8_narathihapate", "mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "expansion", "1277–1287 CE Yuan-Pagan campaigns under Kublai Khan"),
        E("bur8_bayinnaung", "unb_sea_naresuan", "expansion", "16th c. Toungoo–Ayutthaya royal rivalry & hostage-prince Naresuan at Pegu"),
    ]

    add_chain(nodes, edges, "ind5_songtsen_gampo", [
        ("tib8_trisong_detsen", "Emperor Trisong Detsen (Founded Samye Monastery with Padmasambhava, 755–797 CE)", 19, "742–c. 800 CE", "Yarlung Dharma Emperor", "Second great Dharma King of the Tibetan Empire; Tang princess mother Jincheng.", True),
        ("tib8_ralpachen_langdarma", "Emperors Ralpachen & Langdarma (Final Yarlung Emperors, d. 842 CE)", 19, "815–842 CE", "Late Yarlung Emperors"),
        ("tib8_atisha_dromton", "Atiśa Dīpaṃkara & Dromtönpa (11th c. Revival in Blue Annals Book V)", 20, "982–1064 CE", "Kadam Tradition Founders"),
        ("tib8_marpa_milarepa", "Marpa Lotsawa & Jetsun Milarepa (Kagyu Lineage in Blue Annals Book VIII)", 20, "1012–1135 CE", "Tibetan Buddhist Masters"),
        ("tib8_sakya_pandita", "Sakya Pandita Kunga Gyaltsen & Drogön Chögyal Phagpa (Yuan Imperial Preceptors)", 20, "1182–1280 CE", "Sakya Spiritual Sovereigns"),
        ("tib8_tsongkhapa", "Je Tsongkhapa (Founder of Gelug School & Ganden, 1357–1419 CE)", 20, "1357–1419 CE", "Gelug Founder"),
        ("tib8_fifth_dalai_lama", "5th Dalai Lama Ngawang Lobsang Gyatso (Reunified Tibet & Built Potala, 1617–1682 CE)", 21, "1617–1682 CE", "Great Fifth Dalai Lama", "Built the Potala Palace at Lhasa; spiritual & temporal ruler of unified Tibet.", True),
    ], "vedic", "8th–17th c. CE", ["The Blue Annals (George N. Roerich)"])
    edges += [
        E("tib_nyatri_songtsen", "tib8_trisong_detsen", "expansion", "Blue Annals Book I: Yarlung royal lineage continuity"),
        E("tib8_sakya_pandita", "mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "expansion", "1260 CE Patron-Priest Alliance: Drogön Phagpa named Imperial Preceptor (Guoshi) by Kublai Khan"),
    ]

    # =========================================================================
    # SECTION D: COMPLETE OTTOMAN SULTANS & VALIDE SULTANS (~18 nodes)
    # =========================================================================
    nodes += [
        N("ott8_hurrem_sultan", "Hürrem Sultan / Roxelana (+ Sultan Suleiman the Magnificent; Mother of Selim II)", "steppe", 21, "c. 1502–1558 CE", "Haseki Sultan of Ottoman Empire", ["Knolles & Rycaut Vols. 1–3", "Ottoman Imperial Registry"], "Elevated Ottoman royal consort to legal empress; mother of Sultan Selim II & Mihrimah Sultan.", True),
        N("ott8_mihrimah_sultan", "Mihrimah Sultan (Daughter of Suleiman I & Hürrem; Wife of Grand Vizier Rüstem Pasha)", "steppe", 21, "1522–1578 CE", "Ottoman Imperial Princess", ["Ottoman Chronicles"], "Influential Ottoman princess & daughter of Sultan Suleiman I."),
        N("ott8_nurbanu_safiye", "Valide Sultans Nurbanu Sultan (+ Selim II) & Safiye Sultan (+ Murad III)", "steppe", 21, "1525–1619 CE", "Valide Sultans (Queen Mothers)", ["Knolles & Rycaut Vols. 2–3"], "Led the Ottoman 'Sultanate of Women' alongside Selim II & Murad III."),
        N("ott8_kosem_sultan", "Valide Sultan Kösem Sultan (+ Ahmed I; Mother of Murad IV & Ibrahim I, d. 1651)", "steppe", 21, "c. 1589–1651 CE", "Regent & Valide Sultan", ["Knolles & Rycaut Vol. 3"], "Served twice as official regent (naib-i saltanat) of the Ottoman Empire.", True),
    ]
    edges += [
        E("mon_ott_suleiman1", "ott8_hurrem_sultan", "direct", "Royal Marriage: Sultan Suleiman I & Hürrem Sultan"),
        E("ott8_hurrem_sultan", "mon_ott_selim2", "direct", "Mother of Sultan Selim II"),
        E("ott8_hurrem_sultan", "ott8_mihrimah_sultan", "direct", "Daughter of Suleiman I & Hürrem Sultan"),
        E("pc_ottoman_imperial_women", "ott8_hurrem_sultan", "cognate", "Ottoman Imperial Women individual expansion"),
        E("mon_ott_selim2", "ott8_nurbanu_safiye", "direct", "Consort & Valide lineage of Selim II & Murad III"),
        E("mon_ott_ahmed1", "ott8_kosem_sultan", "direct", "Consort of Sultan Ahmed I"),
        E("ott8_kosem_sultan", "mon_ott_murad4", "direct", "Mother of Sultan Murad IV"),
    ]

    nodes += [
        N("ott8_mehmed3", "Sultan Mehmed III (Son of Murad III; Siege of Eger, 1595–1603 CE)", "steppe", 21, "1566–1603 CE", "13th Ottoman Sultan", ["Knolles & Rycaut Vol. 2–3"], "Son of Murad III & Safiye Sultan; father of Ahmed I & Mustafa I."),
        N("ott8_osman2_mustafa1", "Sultans Mustafa I & Osman II the Young (1617–1623 CE)", "steppe", 21, "1591–1622 CE", "15th & 16th Ottoman Sultans", ["Knolles & Rycaut Vol. 3"], "Brother & eldest son of Ahmed I preceding Murad IV."),
        N("ott8_ibrahim1", "Sultan Ibrahim I (Son of Ahmed I & Kösem Sultan, 1640–1648 CE)", "steppe", 21, "1615–1648 CE", "18th Ottoman Sultan", ["Knolles & Rycaut Vol. 3"], "Father of Mehmed IV, Suleiman II & Ahmed II."),
    ]
    edges += [
        E("mon_ott_murad3", "ott8_mehmed3", "direct", "Son of Murad III"),
        E("ott8_mehmed3", "mon_ott_ahmed1", "direct", "Son of Mehmed III"),
        E("mon_ott_ahmed1", "ott8_osman2_mustafa1", "direct", "Son/Brother succession of Ahmed I"),
        E("ott8_osman2_mustafa1", "mon_ott_murad4", "direct", "Succession to Murad IV (son of Ahmed I & Kösem)"),
        E("mon_ott_murad4", "ott8_ibrahim1", "direct", "Brother succession (sons of Ahmed I & Kösem)"),
        E("ott8_kosem_sultan", "ott8_ibrahim1", "direct", "Mother of Sultan Ibrahim I"),
        E("ott8_ibrahim1", "mon_ott_mehmed4", "direct", "Son of Sultan Ibrahim I"),
    ]

    add_chain(nodes, edges, "mon_ott_mehmed4", [
        ("ott8_suleiman2_ahmed2_mustafa2", "Sultans Suleiman II, Ahmed II & Mustafa II (1687–1703 CE)", 21, "1642–1703 CE", "20th–22nd Ottoman Sultans"),
        ("ott8_ahmed3", "Sultan Ahmed III (Tulip Era; Son of Mehmed IV, 1703–1730 CE)", 21, "1673–1736 CE", "23rd Ottoman Sultan"),
        ("ott8_mahmud1_osman3_mustafa3", "Sultans Mahmud I, Osman III & Mustafa III (1730–1774 CE)", 21, "1696–1774 CE", "24th–26th Ottoman Sultans"),
        ("ott8_abdulhamid1", "Sultan Abdulhamid I (Son of Ahmed III, 1774–1789 CE)", 21, "1725–1789 CE", "27th Ottoman Sultan"),
        ("ott8_selim3", "Sultan Selim III (Nizam-i Cedid Reformer, 1789–1807 CE) & Mustafa IV", 21, "1761–1808 CE", "28th–29th Ottoman Sultans"),
    ], "steppe", "1687–1808 CE", ["Modern Universal History Vol. 3–4", "Ottoman Registry"])
    edges.append(E("ott8_selim3", "mon_ott_mahmud2", "direct", "Half-cousin succession (sons of Abdulhamid I & Mustafa III)"))

    add_chain(nodes, edges, "mon_ott_mahmud2", [
        ("ott8_abdulmejid1", "Sultan Abdulmejid I (Tanzimat Reforms; Son of Mahmud II, 1839–1861 CE)", 21, "1823–1861 CE", "31st Ottoman Sultan"),
        ("ott8_abdulaziz", "Sultan Abdulaziz (Son of Mahmud II; Visited London & Paris, 1861–1876 CE)", 21, "1830–1876 CE", "32nd Ottoman Sultan"),
        ("ott8_abdulhamid2", "Sultan Abdulhamid II (Son of Abdulmejid I, 1876–1909 CE)", 21, "1842–1918 CE", "34th Ottoman Sultan", "Final strong autocratic Ottoman Sultan; built the Hejaz Railway.", True),
        ("ott8_mehmed5", "Sultan Mehmed V Reşad (1909–1918 CE)", 21, "1844–1918 CE", "35th Ottoman Sultan"),
        ("ott8_mehmed6", "Sultan Mehmed VI Vahideddin (36th & Final Ottoman Sultan, 1918–1922 CE)", 21, "1861–1926 CE", "36th & Last Ottoman Sultan"),
        ("ott8_abdulmejid2_osmanoglu", "Caliph Abdulmejid II & House of Osmanoğlu Descendants (Living 2026 Line)", 21, "1868–Present CE", "Modern Osmanoğlu Imperial House (Living 2026)"),
    ], "steppe", "1839–2026 CE", ["Ottoman Imperial Registry", "Almanach de Gotha"])

    # =========================================================================
    # SECTION E: PIRKEI DE-RABBI ELIEZER & KITAB AL-MAGALL (6 nodes)
    # =========================================================================
    nodes += [
        N("mid8_pirkei_eliezer_calendar", "Pirkei de-Rabbi Eliezer: Adam → Enoch → Shem Intercalation & 7-Epoch Covenant", "biblical", 3, "Extra-Biblical Midrash", "Intercalation & Patriarchal Transmission", ["Pirkei de-Rabbi Eliezer (bub_gb_DTpRAAAAYAAJ.pdf)"], "Ch. 8–22 traces the sacred calendar secret handed from Adam through Enoch, Noah & Shem to Abraham & Moses."),
        N("mid8_pirkei_eliezer_nimrod_garments", "Pirkei de-Rabbi Eliezer: Adam's Skin Garments Passed via Noah → Ham → Nimrod → Esau", "biblical", 5, "Patriarchal Midrash", "Esau–Nimrod Garment & Sovereignty Motif", ["Pirkei de-Rabbi Eliezer Ch. 24", "Sefer ha-Yashar"], "Famous Midrashic link connecting Nimrod's hunting coat back to Adam and forward to Esau (Gen 25:27–34)."),
        N("mid8_pirkei_eliezer_ishmael_wives", "Pirkei de-Rabbi Eliezer Ch. 30: Ishmael's Wives ('Aisha / Fatima / Meribah) & Abraham's Visits", "biblical", 7, "Abrahamic Midrash", "Ishmael's Arabian Household", ["Pirkei de-Rabbi Eliezer Ch. 30"], "Preserves parallel Islamic-Jewish tradition on Ishmael's two wives and Abraham's desert visits."),
        N("mid8_kitab_al_magall_adam_cave", "Apocrypha Arabica (Kitab al-Magall / Book of the Rolls): Adam → Seth → Noah Cave Treasures", "biblical", 2, "Christian Arabic Roll", "Arabic Cave of Treasures Patriarchs", ["Apocrypha Arabica (Gibson, apocryphaarabica00gibsuoft.pdf)"], "10th-century Sinai Arabic manuscript closely parallel to Syriac Cave of Treasures tracing every patriarch from Adam to Christ."),
        N("mid8_kitab_al_magall_shem_melchizedek", "Kitab al-Magall: Shem & Melchizedek Guardians at Golgotha / Jerusalem", "biblical", 4, "Christian Arabic Roll", "Shem–Melchizedek Guardianship", ["Apocrypha Arabica (Gibson)"], "Details Shem & Melchizedek carrying Adam's body to Jerusalem."),
        N("mid8_kitab_al_magall_mary_david", "Kitab al-Magall: 64-Generation Royal-Priestly Pedigree of Virgin Mary to King David", "biblical", 14, "Christian Arabic Roll", "Arabic Davidic–Marian Genealogy", ["Apocrypha Arabica (Gibson)"], "Constructs an explicit 64-generation stemma joining Judah, David, and Mary in Christian-Arabic tradition."),
    ]
    edges += [
        E("bib_adam", "mid8_pirkei_eliezer_calendar", "expansion", "Pirkei de-Rabbi Eliezer Ch. 8: Adam received calendar wisdom"),
        E("bib_shem", "mid8_pirkei_eliezer_calendar", "expansion", "Transmitted through Noah & Shem to Abraham"),
        E("bib_nimrod", "mid8_pirkei_eliezer_nimrod_garments", "expansion", "Pirkei de-Rabbi Eliezer Ch. 24: Garments of Adam held by Nimrod"),
        E("bib_esau", "mid8_pirkei_eliezer_nimrod_garments", "expansion", "Esau slew Nimrod and inherited the royal hunting garments"),
        E("bib_ishmael", "mid8_pirkei_eliezer_ishmael_wives", "expansion", "Pirkei de-Rabbi Eliezer Ch. 30: Ishmael's desert wives"),
        E("bib_adam", "mid8_kitab_al_magall_adam_cave", "expansion", "Kitab al-Magall (Sinai Arabic): Cave of Treasures patriarchal roll"),
        E("bib_noah", "mid8_kitab_al_magall_adam_cave", "expansion", "Ark preservation of Adam's relics in Kitab al-Magall"),
        E("bib_shem", "mid8_kitab_al_magall_shem_melchizedek", "expansion", "Shem & Melchizedek guardianship in Kitab al-Magall"),
        E("jud_david", "mid8_kitab_al_magall_mary_david", "expansion", "Kitab al-Magall Arabic Davidic pedigree of Virgin Mary"),
    ]

    return {
        "module": "50_wave8_byzantium_goths_franks_south_asia_ottomans",
        "title": "Wave 8: Byzantium, Amali/Balti Goths, Merovingians, Kashmir/Lanka/Burma/Tibet, Ottomans & Midrashic-Arabic Chronicles",
        "nodes": nodes,
        "edges": edges,
    }
