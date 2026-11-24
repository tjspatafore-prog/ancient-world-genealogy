"""
Module 24: Classical Mediterranean Kingdoms, Hellenistic Successors, Alba Longa,
7 Kings of Rome, Roman & Byzantine Emperors, and Medieval Universal Royal Bridges
(Carthage/Barcids, Numidia, Tyre, Lydia, Pontus, Armenia, Bactria, Seleucids,
Merovingians, Carolingians, Anglo-Saxons, Rurikids & Islamic Caliphates).

Sources mined from sources/:
- genealogicaltabl00beth.pdf (William Betham, Genealogical Tables of the Sovereigns of the World, 1795)
- bim_eighteenth-century_royal-genealogies-or-t_anderson-james_1732.epub (James Anderson, Royal Genealogies, 1732)
- Eusebius_Chronicle.pdf (Eusebius of Caesarea, Armenian Chronicon trans. Bedrosian)
- complete.pdf (Flavius Josephus, Antiquities)
"""

from . import N, E, add_chain


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. LYDIA, TYRE, CARTHAGE (BARCIDS) & NUMIDIA / MAURETANIA (Betham LXVI, LXXXVIII-XCIII; Eusebius)
    # -------------------------------------------------------------------------
    nodes += [
        N("cls_lydia_gyges_croesus", "Mermnad Dynasty of Lydia: Gyges → Ardys → Sadyattes → Alyattes → King Croesus", "greek", 16, "680-546 BCE (Herodotus I; Eusebius; Betham Tab. LXVI)",
          "Inventors of Coinage & Anatolian Empire Defeated by Cyrus", ["Eusebius Chronicle (Lydian)", "Betham 1795 Tab. LXVI", "Herodotus I.7-91"],
          "Overthrew Heraclid king Candaules (son of Myrsus). Alyattes's daughter Aryenis married Median King Astyages (grandfather of Cyrus the Great!), making Croesus the great-uncle/brother-in-law of the Median court he fought to avenge against Cyrus in 546 BCE.",
          ["Gyges of Lydia", "Alyattes", "King Croesus", "Aryenis"], major=True),
        N("cls_tyre_royal_line", "Kings of Tyre: Abibaal → Hiram I → Baal-ezer → Ethbaal I (Ithobaal) → Mattan I → Pygmalion & Dido", "levant_egypt", 16, "c. 990-774 BCE (Josephus Against Apion I.18; Betham Tab. XCII)",
          "Phoenician Maritime Dynasty Linking Solomon, Ahab & Carthage", ["Josephus Against Apion I.18", "Betham 1795 Tab. XCII-XCIII", "1 Kings 5, 16:31"],
          "Menander of Ephesus (quoted by Josephus!) preserves the complete Tyrian royal archive: Hiram I (ally of David & Solomon) -> ... -> Ethbaal I (Priest of Astarte, father of Queen Jezebel who married King Ahab of Israel!) -> Baal-ezer II -> Mattan I -> Pygmalion & Princess Elissa/Dido (founder of Carthage, 814 BCE)!",
          ["Abibaal", "Ethbaal I (father of Jezebel)", "Mattan I", "Pygmalion of Tyre"], major=True),
        N("cls_carthage_barcids", "Barcid Dynasty of Carthage: Hamilcar Barca → Hannibal Barca, Hasdrubal & Mago", "levant_egypt", 18, "275-183 BCE (Polybius; Livy; Betham Tab. LXXXVIII)",
          "Carthaginian Punic Commanders Against Rome", ["Betham 1795 Tab. LXXXVIII-LXXXIX", "Polybius", "Livy"],
          "Hamilcar Barca (hero of 1st Punic War) fathered Hannibal the Great (crossed the Alps in 218 BCE, victor at Cannae), Hasdrubal Barca, Mago Barca, and daughters married to Hasdrubal the Fair & Numidian prince Naravas. Allied with Hasdrubal Gisco (father of Sophonisba).",
          ["Hamilcar Barca", "Hannibal Barca", "Hasdrubal Barca", "Sophonisba"], major=True),
        N("cls_numidia_mauretania", "Kings of Numidia & Mauretania: Gaia → Masinissa → Micipsa → Jugurtha; Juba I → Juba II (+ Cleopatra Selene II)", "african", 18, "238 BCE – 40 CE (Sallust; Betham Tab. XC-XCI)",
          "Amazigh (Berber) Royal Dynasties of North Africa", ["Betham 1795 Tab. XC-XCI", "Sallust Jugurtha", "Plutarch"],
          "Masinissa unified Numidia (ally of Scipio Africanus against Hannibal); his grandson Jugurtha resisted Rome. Later King Juba II of Mauretania married Cleopatra Selene II (daughter of Mark Antony & Cleopatra VII of Egypt!), fathering King Ptolemy of Mauretania — uniting Berber, Ptolemaic Egyptian, and Roman bloodlines!",
          ["Masinissa", "Jugurtha", "Juba II", "Cleopatra Selene II", "Ptolemy of Mauretania"], major=True),

        # -------------------------------------------------------------------------
        # 2. HELLENISTIC SUCCESSORS, PONTUS, ARMENIA, COMMAGENE, ADIABENE & BACTRIA (Betham LXVIII-CV; Eusebius)
        # -------------------------------------------------------------------------
        N("cls_seleucids", "Seleucid Empire: Seleucus I Nicator (+ Apama of Sogdia) → Antiochus I → Antiochus III the Great → Antiochus IV Epiphanes", "greek", 18, "312-63 BCE (Eusebius Chronicle; Betham Tab. CIII; 1 Maccabees)",
          "Hellenistic Kings of Syria, Mesopotamia & Persia", ["Eusebius Chronicle (Kings of Asia & Syria)", "Betham 1795 Tab. CIII", "1 Maccabees 1"],
          "Founded by Alexander's general Seleucus I Nicator & Iranian princess Apama (daughter of Spitamenes of Sogdia). Antiochus III the Great's daughter Cleopatra I Syra married Ptolemy V (starting the 'Cleopatra' name in Egypt!). Antiochus IV Epiphanes sparked the Maccabean Revolt (167 BCE).",
          ["Seleucus I Nicator", "Apama", "Antiochus III the Great", "Antiochus IV Epiphanes"], major=True),
        N("cls_antigonids_epirus", "Antigonid Macedon (Antigonus I, Demetrius, Philip V, Perseus) & Pyrrhus of Epirus", "greek", 18, "306-168 BCE (Eusebius Chronicle; Betham Tab. LXXVII-LXXXI)",
          "Final Macedonian Kings & Aeacid Kings of Epirus", ["Eusebius Chronicle (Macedonian Kings)", "Betham 1795 Tab. LXXVII, LXXXI"],
          "Antigonus Monophthalmus -> Demetrius Poliorcetes -> Antigonus II Gonatas -> Philip V -> Perseus (defeated by Rome at Pydna, 168 BCE). King Pyrrhus of Epirus (cousin of Alexander via Olympias & claiming descent from Achilles's son Neoptolemus!) fought Rome ('Pyrrhic victory').",
          ["Antigonus I", "Perseus of Macedon", "Pyrrhus of Epirus"]),
        N("cls_pontus_mithridates", "Kingdom of Pontus: Mithridates I Ktistes → Pharnaces I → Mithridates VI Eupator ('The Poison King')", "iranian", 18, "281-63 BCE (Betham Tab. XCV; Appian)",
          "Persian-Greek Royal Dynasty of the Black Sea", ["Betham 1795 Tab. XCV", "Appian Mithridatic Wars"],
          "Claimed descent from both Darius the Great (Achaemenids) and Alexander/Seleucids! Mithridates VI Eupator waged three Mithridatic Wars against Rome; his daughter Cleopatra married King Tigranes the Great of Armenia, and his son Pharnaces II ruled the Bosporan Kingdom ('Veni, vidi, vici').",
          ["Mithridates I", "Mithridates VI Eupator", "Pharnaces II"], major=True),
        N("cls_armenia_tigranes", "Artaxiad Armenia: Artaxias I → Tigranes II the Great (+ Cleopatra of Pontus) → Artavasdes II & Herodian Tigranes V/VI", "iranian", 18, "189 BCE – 63 CE (Betham Tab. LXXXIII; Josephus Ant. XVIII)",
          "Imperial Kingdom of Armenia Linking Pontus, Parthia & Judea", ["Betham 1795 Tab. LXXXIII", "Josephus Antiquities XVIII.5"],
          "Artaxias I founded Artaxata; Tigranes the Great built a vast empire from the Caspian to the Mediterranean. Remarkable dynastic link: Herod the Great's grandson Tigranes V & great-grandson Tigranes VI (via Alexander + Glaphyra of Cappadocia) were placed on the throne of Armenia by Rome!",
          ["Artaxias I", "Tigranes the Great", "Tigranes V & VI (Herodian)"], major=True),
        N("cls_bactria_menander", "Greco-Bactrian & Indo-Greek Kings: Diodotus I → Euthydemus → Demetrius I → Menander I (King Milinda)", "greek", 18, "250-130 BCE (Betham Tab. LXVIII; Milinda Panha)",
          "Hellenistic Kings of Afghanistan & Northwest India", ["Betham 1795 Tab. LXVIII", "Milinda Panha (Questions of King Milinda)", "Strabo"],
          "Diodotus broke away from the Seleucids in Bactria; Demetrius I invaded India (Gandhara/Punjab); Menander I Soter (Pali: Milinda) converted to Buddhism in the famous dialogue Milinda Panha with sage Nagasena — bridging Greek, Iranian, and Indian civilizations!",
          ["Diodotus I", "Demetrius I of Bactria", "Menander I / King Milinda"], major=True),
        N("cls_adiabene_edessa", "Royal Houses of Adiabene (Monobazus I & Queen Helena → Izates II) & Osroene/Edessa (King Abgar V)", "mesopotamian", 19, "1st c. CE (Josephus Ant. XX.2; Betham Tab. LXX-LXXI)",
          "Upper Mesopotamian Client Kingdoms Famous in Jewish & Syriac History", ["Josephus Antiquities XX.2-4", "Betham 1795 Tab. LXX-LXXI", "Eusebius HE I.13"],
          "Queen Helena of Adiabene & her son King Izates II converted to Judaism (~30 CE), funded famine relief in Jerusalem, and built the monumental Tomb of the Kings in Jerusalem. King Abgar V Ukkama of Edessa (Osroene) features in Syriac chronicles as the first Christian monarch.",
          ["Queen Helena of Adiabene", "King Izates II", "King Abgar V of Edessa"]),

        # -------------------------------------------------------------------------
        # 3. ALBA LONGA, 7 KINGS OF ROME, ROMAN & BYZANTINE EMPERORS (Eusebius; Betham CIX-CXLI; Anderson 1732)
        # -------------------------------------------------------------------------
        N("rom_alba_longa", "Kings of Alba Longa: Ascanius (Iulus) → Silvius → Capys → Tiberinus → Aventinus → Procas → Numitor & Amulius", "greek", 15, "c. 1177-753 BCE (Livy I; Eusebius Chronicle; Betham Tab. CIX-CXI)",
          "14 Trojan-Latin Kings Bridging Aeneas to Romulus & Remus", ["Eusebius Chronicle (The Romans)", "Betham 1795 Tab. CIX-CXI", "Livy I.3"],
          "Complete Latin succession from Aeneas (+ Lavinia daughter of King Latinus): Ascanius/Iulus (claimed ancestor of the Julii Caesars!), Silvius Posthumus, Aeneas Silvius, Latinus Silvius, Alba, Atys, Capys, Capetus, Tiberinus (eponym of the Tiber River), Agrippa, Romulus Silvius, Aventinus, Procas -> Numitor (father of Rhea Silvia) & usurper Amulius.",
          ["Ascanius / Iulus", "Silvius", "Tiberinus", "Procas", "Numitor", "Rhea Silvia"]),
        N("rom_seven_kings", "7 Kings of Rome: Romulus, Numa Pompilius, Tullus Hostilius, Ancus Marcius, Tarquinius Priscus, Servius Tullius & Tarquinius Superbus", "greek", 16, "753-509 BCE (Livy I; Eusebius; Betham Tab. CXII)",
          "Complete Roman Monarchy to Republic Founder L. Junius Brutus", ["Betham 1795 Tab. CXII", "Eusebius Chronicle", "Livy Book I"],
          "Sabine co-ruler Titus Tatius -> Numa Pompilius -> Tullus Hostilius -> Ancus Marcius -> Etruscan Tarquinius Priscus (+ Tanaquil) -> Servius Tullius -> Tarquinius Superbus (expelled in 509 BCE by Lucius Junius Brutus & Tarquinius Collatinus, founding the Roman Republic!).",
          ["Numa Pompilius", "Tullus Hostilius", "Servius Tullius", "Tarquinius Superbus", "Lucius Junius Brutus"], major=True),
        N("rom_julio_claudians", "Julio-Claudian Emperors: Augustus (+ Livia) → Tiberius, Caligula, Claudius & Nero", "greek", 19, "27 BCE – 68 CE (Suetonius; Tacitus; Betham Tab. CXXI; Anderson)",
          "First Imperial Dynasty of Rome (New Testament Era)", ["Betham 1795 Tab. CXXI", "Anderson 1732 Tables 119-121", "Luke 2:1, 3:1", "Acts 25"],
          "Augustus (census at Jesus's birth, Luke 2:1) -> Tiberius (Jesus's ministry & crucifixion, Luke 3:1) -> Caligula (descended from Mark Antony & Agrippa) -> Claudius (Acts 18:2) -> Nero (martyrdom of Peter & Paul, Great Fire of 64 CE).",
          ["Emperor Tiberius", "Caligula", "Emperor Claudius", "Emperor Nero"], major=True),
        N("rom_flavians_antonines_severans", "Flavian (Vespasian, Titus, Domitian), Five Good Emperors (Trajan, Hadrian, Marcus Aurelius) & Severan Dynasties", "greek", 19, "69-235 CE (Betham Tab. CXXIV-CXXVII; Anderson 1732)",
          "High Imperial Roman Dynasties (Including Syro-Punic Severans)", ["Betham 1795 Tab. CXXIV-CXXVII", "Anderson 1732 Tables 124-130", "Josephus Wars"],
          "Vespasian & Titus (destruction of Jerusalem Temple, 70 CE — patrons of Josephus!) -> Domitian (interviewed grandsons of Jude, brother of Jesus!). Nerva -> Trajan -> Hadrian -> Antoninus Pius -> Marcus Aurelius -> Commodus. Septimius Severus (Punic/Libyan from Leptis Magna!) + Julia Domna (Priest-King house of Emesa!) -> Caracalla.",
          ["Vespasian", "Emperor Titus", "Trajan", "Hadrian", "Marcus Aurelius", "Septimius Severus & Julia Domna"]),
        N("rom_constantine_byzantium", "Constantine the Great → Theodosius I → Justinian I → Heraclius → Basil I → Alexios Komnenos → Constantine XI", "greek", 19, "306-1453 CE (Betham Tab. CXXXI-CXLI; Anderson 1732 Tables 114, 133-135)",
          "Christian Roman & Eastern Byzantine Imperial Lineages", ["Betham 1795 Tab. CXXXI-CXLI", "Anderson 1732 Tables 114, 133-135"],
          "Constantine I (+ St. Helena) founded Constantinople (330 CE) -> Theodosius I (split East/West 395 CE) -> Justinian I (+ Empress Theodora, Hagia Sophia) -> Heraclius (defeated Sasanian Khosrow II) -> Macedonian Dynasty (Basil I, Basil II) -> Komnenoi -> Palaiologoi (until 1453).",
          ["Constantine the Great", "Theodosius I", "Justinian I", "Heraclius", "Basil I"], major=True),

        # -------------------------------------------------------------------------
        # 4. MEDIEVAL EUROPEAN & ISLAMIC UNIVERSAL CHRONICLE BRIDGES (Anderson 1732 & Betham 1795)
        # -------------------------------------------------------------------------
        N("eur_merovingian_carolingian", "Merovingians (Merovech → Clovis I) & Carolingians (Charles Martel → Pepin → Charlemagne)", "europe_norse", 19, "450-843 CE (Anderson 1732 Table 216; Betham Tab. CXVI)",
          "Frankish Kings & Founder of the Holy Roman Empire (Ancestral Hub of Europe)", ["Anderson 1732 Table 216", "Betham 1795 Tab. CXVI"],
          "Clovis I unified the Franks (481-511). Carolingian Mayor of the Palace Charles Martel (Battle of Tours, 732) -> Pepin the Short -> Charlemagne (crowned Emperor 800 CE) -> Louis the Pious -> Treaty of Verdun (Lothair, Louis the German, Charles the Bald). Chroniclers (Fredegar/Anderson) linked early Franks back to Trojan exiles (Francus)!",
          ["Clovis I", "Charles Martel", "Charlemagne (Charles the Great)"], major=True),
        N("eur_wessex_alfred_norman", "House of Wessex (Cerdic → Egbert → Alfred the Great → Æthelstan) & Normans (Rollo → William the Conqueror)", "europe_norse", 19, "519-1154 CE (Anglo-Saxon Chronicle; Anderson 1732; Betham)",
          "Founders of England (Anglo-Saxon Chronicle Bridges Woden → Sceaf of Noah's Ark!)", ["Anglo-Saxon Chronicle (855 CE)", "Anderson 1732", "Betham 1795"],
          "The Anglo-Saxon Chronicle (under King Æthelwulf, father of Alfred the Great) famously traces Wessex back through Cerdic -> Woden (Odin) -> Geat -> Sceaf ('born in Noah's Ark'!) -> Noah -> Adam! Rollo the Viking founded Normandy -> William the Conqueror (1066) -> Henry II & Eleanor of Aquitaine (Plantagenets).",
          ["Cerdic", "Alfred the Great", "Rollo of Normandy", "William the Conqueror"], major=True),
        N("eur_rurik_harald_viking", "Viking & Slavic Founders: Ragnar Lodbrok, Harald Fairhair (Norway) & Prince Rurik → Vladimir the Great (Kievan Rus')", "europe_norse", 19, "850-1015 CE (Heimskringla; Primary Chronicle; Anderson 1732)",
          "Scandinavian & East Slavic Royal Houses", ["Snorri Sturluson Heimskringla", "Russian Primary Chronicle", "Anderson 1732"],
          "Harald Fairhair (Yngling descendant) unified Norway (~872); Varangian Prince Rurik founded Novgorod (862) -> Igor & St. Olga -> Sviatoslav I -> Vladimir the Great (Christianized Kievan Rus', 988, marrying Byzantine princess Anna Porphyrogenita!) -> Yaroslav the Wise (whose daughters became Queens of France, Norway & Hungary!).",
          ["Harald Fairhair", "Ragnar Lodbrok", "Prince Rurik", "Vladimir the Great", "Yaroslav the Wise"]),
        N("ar_hashim_muhammad_caliphs", "Qusayy → Hashim → Abd al-Muttalib → Prophet Muhammad (570–632 CE) → Fatimah & Ali, Umayyads & Abbasids", "arabian", 19, "c. 400-1258 CE (Ibn Ishaq; Al-Biruni; Anderson 1732 Tables 157-158)",
          "Quraysh Banu Hashim Lineage & Early Islamic Caliphates", ["Ibn Ishaq Sirat Rasul Allah", "Al-Biruni Chronology", "Anderson 1732 Tables 157-158"],
          "Through Adnan -> Fihr (Quraysh) -> Qusayy -> Abd Manaf -> Hashim -> Abd al-Muttalib -> Abdullah & Aminah -> Prophet Muhammad (founder of Islam). Through daughter Fatimah & cousin Ali ibn Abi Talib: Hasan & Husayn (Alids/Hashemites). Through Abd Manaf's son Abd Shams: Umayyad Caliphate (Mu'awiya I, Damascus & Cordoba). Through uncle Al-Abbas: Abbasid Caliphate (Al-Saffah, Harun al-Rashid of Baghdad!).",
          ["Prophet Muhammad", "Hashim ibn Abd Manaf", "Fatimah & Ali ibn Abi Talib", "Mu'awiya I (Umayyads)", "Harun al-Rashid (Abbasids)"], major=True),
    ]

    edges += [
        # Lydia, Tyre, Carthage, Numidia
        E("grk_lydus_tyrrhenus", "cls_lydia_gyges_croesus", "expansion", "Lydian royal succession to Mermnad Dynasty (Betham Tab. LXVI; Herodotus)"),
        E("ir_cyaxares", "cls_lydia_gyges_croesus", "direct", "Alyattes's daughter Aryenis marries Median King Astyages, son of Cyaxares (Herodotus I.74)"),
        E("cls_lydia_gyges_croesus", "ir_cyrus", "cognate", "Cyrus the Great defeats Croesus of Lydia (546 BCE)"),
        E("for_hiram_syria_moab", "cls_tyre_royal_line", "direct", "King Hiram I -> Ethbaal I -> Mattan I -> Pygmalion & Dido (Josephus)"),
        E("cls_tyre_royal_line", "kg_i3_omri_ahab", "direct", "Ethbaal I of Tyre is father of Queen Jezebel (wife of King Ahab, 1 Kgs 16:31)"),
        E("cls_tyre_royal_line", "grk_dido_carthage", "direct", "Mattan I -> Princess Elissa/Dido founder of Carthage (814 BCE)"),
        E("grk_dido_carthage", "cls_carthage_barcids", "expansion", "Punic Carthage leadership -> Barcid Dynasty (Hamilcar & Hannibal)"),
        E("af_mazigh", "cls_numidia_mauretania", "expansion", "Amazigh/Berber Kingdoms of Numidia & Mauretania (Masinissa -> Juba II)"),
        E("eg_ptolemy_cleopatra", "cls_numidia_mauretania", "direct", "Cleopatra VII's daughter Cleopatra Selene II marries King Juba II of Mauretania"),

        # Hellenistic, Pontus, Armenia, Bactria, Adiabene
        E("grk_alexander", "cls_seleucids", "expansion", "Diadochi succession: General Seleucus I Nicator founds Seleucid Empire"),
        E("grk_alexander", "cls_antigonids_epirus", "expansion", "Diadochi succession in Macedonia & Aeacid cousin Pyrrhus of Epirus"),
        E("cls_seleucids", "has_mattathias", "cognate", "Antiochus IV Epiphanes sparks the Maccabean Revolt (167 BCE)"),
        E("ir_darius1", "cls_pontus_mithridates", "expansion", "Mithridatic Dynasty of Pontus claims Achaemenid descent (Betham Tab. XCV)"),
        E("cls_pontus_mithridates", "cls_armenia_tigranes", "direct", "Cleopatra of Pontus marries King Tigranes the Great of Armenia"),
        E("her_herod_great_family", "cls_armenia_tigranes", "direct", "Herod's grandson Tigranes V & great-grandson Tigranes VI rule Armenia (Betham Tab. LXXXIII)"),
        E("cls_seleucids", "cls_bactria_menander", "expansion", "Satrap Diodotus I establishes Greco-Bactrian Kingdom -> Menander/Milinda"),
        E("cls_bactria_menander", "ved_maurya_ashoka", "cognate", "Indo-Greek King Menander I (Milinda) embraces Buddhism in post-Mauryan India"),
        E("her_agrippa_herodias", "cls_adiabene_edessa", "cognate", "Queen Helena & King Izates of Adiabene allied with Herodian Jerusalem (Josephus Ant. XX)"),

        # Alba Longa, Rome, Byzantium
        E("grk_aeneas", "rom_alba_longa", "direct", "Aeneas + Lavinia -> Ascanius/Iulus & Silvius -> 14 Kings of Alba Longa"),
        E("rom_alba_longa", "grk_romulus_remus", "direct", "King Numitor -> Rhea Silvia -> Romulus & Remus (753 BCE)"),
        E("grk_romulus_remus", "rom_seven_kings", "direct", "Romulus -> Numa -> Tarquins -> Roman Republic (509 BCE)"),
        E("grk_julius_augustus", "rom_julio_claudians", "direct", "Augustus -> Tiberius, Caligula, Claudius & Nero"),
        E("rom_julio_claudians", "rom_flavians_antonines_severans", "expansion", "Imperial Roman succession -> Flavians, Antonines & Severans"),
        E("her_agrippa_herodias", "rom_flavians_antonines_severans", "direct", "Severan Empress Julia Domna descends from Priest-Kings of Emesa (allied with Herodians)"),
        E("rom_flavians_antonines_severans", "rom_constantine_byzantium", "expansion", "Constantine the Great -> Christian Roman & Byzantine Emperors"),

        # Medieval Europe & Islamic Caliphates
        E("grk_priam_hector", "eur_merovingian_carolingian", "syncretic", "Medieval Frankish chroniclers (Fredegar/Anderson) bridged Troy -> Merovingians -> Charlemagne"),
        E("rom_constantine_byzantium", "eur_merovingian_carolingian", "expansion", "Charlemagne crowned Western Roman Emperor (800 CE)"),
        E("eur_odin_ask_embla", "eur_wessex_alfred_norman", "syncretic", "Anglo-Saxon Chronicle (855 CE) traces Wessex via Cerdic -> Woden -> Sceaf ('born in Noah's Ark')"),
        E("bib_noah", "eur_wessex_alfred_norman", "syncretic", "Anglo-Saxon Chronicle traces Alfred the Great via Sceaf (son of Noah) to Adam"),
        E("eur_ynglings_skjoldungs", "eur_rurik_harald_viking", "expansion", "Yngling Harald Fairhair (Norway) & Varangian Rurik -> Vladimir of Kievan Rus'"),
        E("rom_constantine_byzantium", "eur_rurik_harald_viking", "direct", "Byzantine Princess Anna Porphyrogenita marries Vladimir the Great (988 CE)"),
        E("ar_adnan_quraysh", "ar_hashim_muhammad_caliphs", "direct", "Adnan -> Fihr (Quraysh) -> Qusayy -> Hashim -> Abd al-Muttalib -> Prophet Muhammad"),
    ]

    return {
        "module": "24_classical_empires_universal",
        "title": "Classical Mediterranean Kingdoms (Lydia, Tyre, Carthage/Barcids, Numidia, Pontus, Armenia, Bactria, Seleucids), Alba Longa, 7 Kings of Rome, Roman/Byzantine Emperors & Universal Royal Bridges (Betham 1795, Anderson 1732, Eusebius)",
        "nodes": nodes,
        "edges": edges,
    }
