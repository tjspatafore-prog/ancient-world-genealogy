"""
Module 45: Wave 3 Person-by-Person Classical Mediterranean Kingdoms, Hellenistic Successors,
Alba Longa (14 Kings), 7 Kings of Rome, Julio-Claudian Family Tree & Chronicon Paschale Late Roman Houses.

Sources mined from sources/:
- complete.pdf (Flavius Josephus Against Apion I.18: Kings of Tyre)
- romanantiquities01dionuoft.pdf (Dionysius of Halicarnassus, Roman Antiquities Book I)
- Eusebius_Chronicle.pdf (Eusebius of Caesarea: Aegialeus of Sicyon, Inachus, Cecrops, Seleucids, Lydians, Alba Longa)
- Chronicon_Paschale_284-628.pdf (Constantine, Theodosius I, Arcadius, Honorius, Galla Placidia)
- genealogicaltabl00beth.pdf (William Betham 1795 Tables LXVI-CXLI)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    def chain(items, tradition, sources, edge_label, edge_type="direct", start_parent=None):
        prev = start_parent
        for it in items:
            if isinstance(it, str):
                prev = it
                continue
            nid, nm, tr, er, rl, nt, mj = it[0], it[1], it[2], it[3], it[4], it[5], it[6]
            nodes.append(N(nid, nm, tradition, tr, er, rl, sources, nt, major=mj))
            if prev:
                edges.append(E(prev, nid, edge_type, edge_label))
            prev = nid

    # =========================================================================
    # 1. TYRE (Josephus Ag. Ap. I.18) & BARCID CARTHAGE & NUMIDIA / MAURETANIA
    # =========================================================================
    chain([
        "cls_tyre_royal_line",
        ("cls3_abibaal", "King Abibaal of Tyre (Father of Hiram I, Josephus Ag. Ap. I.18)", 15, "c. 1000–990 BCE (Josephus Ag. Ap. I.18)", "Founder of Tyrian Royal Line", "Father of Solomon's ally King Hiram I.", False),
        ("cls3_hiram1", "King Hiram I of Tyre (980–947 BCE; Ally of David & Solomon, 1 Kgs 5)", 16, "980–947 BCE (1 Kgs 5; Josephus Ag. Ap. I.18)", "King of Tyre & Lebanon Cedar Ally", "Son of Abibaal; supplied cedar and craftsman Huram-Abi for Solomon's Temple.", True),
        ("cls3_baalezer1", "King Baal-ezer I of Tyre (Son of Hiram I, 946–930 BCE)", 16, "946–930 BCE (Josephus Ag. Ap. I.18)", "Son of Hiram I", "Succeeded Hiram I through Abdastartus.", False),
        "isr_ethbaal_sidon",
        ("cls3_baalezer2", "King Baal-ezer II of Tyre (Son of Ethbaal I; Brother of Jezebel, 846–841 BCE)", 17, "846–841 BCE (Kurkh Monolith; Josephus Ag. Ap. I.18)", "Son of Ethbaal & Brother of Queen Jezebel", "Paid tribute to Shalmaneser III in 841 BCE.", False),
        ("cls3_mattan1", "King Mattan I of Tyre (Father of Pygmalion & Queen Dido, 840–832 BCE)", 17, "840–832 BCE (Josephus Ag. Ap. I.18)", "Father of Dido & Pygmalion", "Son of Baal-ezer II; father of Pygmalion and Elissa/Dido.", False),
        ("cls3_pygmalion", "King Pygmalion / Pumayyaton of Tyre (Brother of Dido, 831–785 BCE)", 17, "831–785 BCE (Josephus Ag. Ap. I.18; Nora Stone)", "Son of Mattan I", "Reigned 47 years; sister Elissa/Dido founded Carthage in his 7th year (814 BCE).", False),
    ], "levant_egypt", ["Josephus Against Apion I.18 (Menander)", "Betham Tab. XCII"], "Tyrian Royal Line (Josephus Ag. Ap. I.18)")
    edges += [
        E("for_hiram_syria_moab", "cls3_hiram1", "direct", "1 Kgs 5: Tyrian King Hiram I"),
        E("cls3_mattan1", "grk_dido_carthage", "direct", "Josephus Ag. Ap. I.18: Mattan I -> Elissa / Queen Dido of Carthage"),
    ]

    nodes += [
        N("cls3_hamilcar_barca", "General Hamilcar Barca (First Punic War & Iberia, d. 228 BCE)", "levant_egypt", 18, "275–228 BCE (Polybius I; Nepos)", "Founder of Barcid Dynasty", ["Polybius I–II", "Betham Tab. LXXXVIII"], "Father of Hannibal, Hasdrubal, and Mago Barca.", True),
        N("cls3_hannibal_barca", "Hannibal Barca of Carthage (247–183 BCE; Crossed Alps 218 BCE)", "levant_egypt", 18, "247–183 BCE (Polybius III; Livy XXI)", "Supreme Carthaginian General", ["Polybius III", "Livy XXI–XXX"], "Eldest son of Hamilcar Barca; victor of Trebia, Trasimene & Cannae.", major=True),
        N("cls3_hasdrubal_barca", "Hasdrubal Barca (Brother of Hannibal; Commander in Hispania, d. 207 BCE)", "levant_egypt", 18, "d. 207 BCE (Livy XXVII.49)", "Barcid General", ["Livy XXVII"], "Fell at the Battle of the Metaurus."),
        N("cls3_mago_barca", "Mago Barca (Youngest Son of Hamilcar Barca, d. 203 BCE)", "levant_egypt", 18, "d. 203 BCE (Livy XXX.19)", "Youngest Barcid Brother", ["Livy XXX"], "Founded Port Mahon and fought in Italy."),
        N("cls3_hasdrubal_gisco", "General Hasdrubal Gisco (Father of Sophonisba, d. 202 BCE)", "levant_egypt", 18, "d. 202 BCE (Livy XXIX)", "Carthaginian Commander", ["Livy XXIX–XXX"], "Father of Sophonisba."),
        N("cls3_sophonisba", "Queen Sophonisba (Daughter of Hasdrubal Gisco; Wife of Syphax & Masinissa)", "african", 18, "d. 203 BCE (Livy XXX.12–15)", "Carthaginian-Numidian Queen", ["Livy XXX.12–15"], "Married Numidian kings Syphax and Masinissa during the 2nd Punic War."),
    ]
    edges += [
        E("grk_dido_carthage", "cls3_hamilcar_barca", "expansion", "Carthaginian Punic aristocracy -> Barcid House"),
        E("cls_carthage_barcids", "cls3_hamilcar_barca", "direct", "Barcid Dynasty founder"),
        E("cls3_hamilcar_barca", "cls3_hannibal_barca", "direct", "Father Hamilcar -> Hannibal Barca"),
        E("cls3_hamilcar_barca", "cls3_hasdrubal_barca", "direct", "Father Hamilcar -> Hasdrubal Barca"),
        E("cls3_hamilcar_barca", "cls3_mago_barca", "direct", "Father Hamilcar -> Mago Barca"),
        E("cls3_hamilcar_barca", "cls3_hasdrubal_gisco", "cognate", "Carthaginian leadership of Second Punic War"),
        E("cls3_hasdrubal_gisco", "cls3_sophonisba", "direct", "Father Hasdrubal Gisco -> Sophonisba"),
    ]

    chain([
        "cls_numidia_mauretania",
        ("cls3_gaia", "King Gaia of the Massylii (Father of Masinissa, d. 206 BCE)", 18, "d. 206 BCE (Livy XXIV.48)", "Numidian King", "Father of unifier King Masinissa.", False),
        ("cls3_masinissa", "King Masinissa of Numidia (202–148 BCE; Ally of Rome at Zama)", 18, "238–148 BCE (Polybius; Livy XXX)", "First King of Unified Numidia", "Allied with Scipio Africanus at Zama; father of Micipsa, Mastanabal & Gulussa.", True),
        ("cls3_micipsa", "King Micipsa of Numidia (148–118 BCE; Adoptive Father of Jugurtha)", 18, "148–118 BCE (Sallust Jugurtha 5–11)", "Son of Masinissa", "Father of Adherbal & Hiempsal I; adopted nephew Jugurtha.", False),
        ("cls3_jugurtha", "King Jugurtha of Numidia (Nephew of Micipsa, 118–104 BCE)", 18, "160–104 BCE (Sallust Bellum Jugurthinum)", "Adversary of Marius & Sulla", "Son of Mastanabal; resisted Rome in the Jugurthine War.", False),
        ("cls3_juba1", "King Juba I of Numidia (Father of Juba II, d. 46 BCE)", 18, "c. 85–46 BCE (Caesar Bellum Africum)", "Son of Hiempsal II", "Allied with Cato & Scipio at Thapsus; father of scholar-king Juba II.", False),
        "jos_juba2",
        ("cls3_ptolemy_mauretania", "King Ptolemy of Mauretania (Son of Juba II & Cleopatra Selene II, 23–40 CE)", 19, "c. 10 BCE – 40 CE (Tacitus Annals IV.23; Suetonius Caligula 35)", "Last Ptolemaic-Numidian King of Mauretania", "Son of King Juba II and Queen Cleopatra Selene II; grandson of Mark Antony & Cleopatra VII!", True),
    ], "african", ["Sallust Jugurtha", "Betham Tab. XC–XCI"], "Numidian & Mauretanian Royal Succession")
    nodes.append(N("cls3_cleopatra_selene2", "Queen Cleopatra Selene II (Daughter of Cleopatra VII & Mark Antony; Wife of Juba II)", "levant_egypt", 18,
                   "40 BCE – c. 5 CE (Plutarch Antony 36; Dio)", "Ptolemaic Princess & Queen of Mauretania",
                   ["Plutarch Life of Antony 36", "Josephus Ant. I.15", "Betham Tab. XCI"],
                   "Twin daughter of Cleopatra VII and Mark Antony; raised by Octavia Minor in Rome, wed King Juba II of Mauretania, and bore King Ptolemy of Mauretania.", major=True))
    edges += [
        E("cls3_masinissa", "cls3_sophonisba", "direct", "Brief marriage of Masinissa & Sophonisba"),
        E("eg_ptolemy_cleopatra", "cls3_cleopatra_selene2", "direct", "Mother Cleopatra VII -> Cleopatra Selene II"),
        E("mon_rom_mark_antony", "cls3_cleopatra_selene2", "direct", "Father Mark Antony -> Cleopatra Selene II"),
        E("jos_juba2", "cls3_cleopatra_selene2", "direct", "Marriage of King Juba II & Cleopatra Selene II"),
        E("cls3_cleopatra_selene2", "cls3_ptolemy_mauretania", "direct", "Mother Cleopatra Selene II -> King Ptolemy of Mauretania"),
    ]

    # =========================================================================
    # 2. LYDIA, SELEUCIDS, ANTIGONIDS, PONTUS, ARMENIA, BACTRIA & SICYON
    # =========================================================================
    chain([
        "cls_lydia_gyges_croesus",
        ("cls3_gyges", "King Gyges of Lydia (Mermnad Founder, 680–644 BCE)", 16, "680–644 BCE (Herodotus I.8–14; Eusebius)", "Founder of Mermnad Lydia", "Overthrew Heraclid Candaules; allied with Assyria under Ashurbanipal.", False),
        ("cls3_ardys", "King Ardys II of Lydia (644–624 BCE)", 16, "644–624 BCE (Herodotus I.15)", "Son of Gyges", "Son of Gyges.", False),
        ("cls3_sadyattes", "King Sadyattes of Lydia (624–612 BCE)", 16, "624–612 BCE (Herodotus I.16)", "Son of Ardys", "Father of Alyattes.", False),
        ("cls3_alyattes", "King Alyattes of Lydia (612–560 BCE; Coinage Pioneer)", 16, "612–560 BCE (Herodotus I.16–25)", "Father of Croesus & Queen Aryenis", "Minted earliest electrum coins; wed daughter Aryenis to Median Crown Prince Astyages.", False),
        ("cls3_croesus", "King Croesus of Lydia (560–546 BCE; Conquered by Cyrus)", 17, "560–546 BCE (Herodotus I.26–91; Eusebius)", "Last Mermnad King of Lydia", "Famed for wealth; fought Cyrus the Great at Thymbra & Sardis (546 BCE).", True),
    ], "greek", ["Herodotus I.7–91", "Eusebius Chronicle", "Betham Tab. LXVI"], "Mermnad Lydian Royal Succession")
    nodes.append(N("cls3_aryenis", "Queen Aryenis of Media (Daughter of Alyattes; Wife of Astyages, Herodotus I.74)", "greek", 16,
                   "fl. 585 BCE (Herodotus I.74)", "Lydian Princess & Median Queen", ["Herodotus I.74"],
                   "Married Astyages of Media to seal the Battle of the Eclipse peace treaty (585 BCE)."))
    edges += [
        E("cls3_alyattes", "cls3_aryenis", "direct", "Herodotus I.74: Alyattes -> Aryenis"),
        E("ir_cyaxares", "cls3_aryenis", "direct", "Astyages ben Cyaxares marries Aryenis of Lydia"),
        E("cls3_croesus", "ir_cyrus", "cognate", "546 BCE: Cyrus defeats Croesus"),
    ]

    chain([
        "cls_seleucids",
        ("cls3_seleucus1", "Emperor Seleucus I Nicator (312–281 BCE; Husband of Apama)", 18, "358–281 BCE (Eusebius; Appian)", "Founder of Seleucid Empire", "General of Alexander; wed Sogdian princess Apama.", True),
        ("cls3_antiochus1", "Emperor Antiochus I Soter (281–261 BCE)", 18, "324–261 BCE (Eusebius; Betham Tab. CIII)", "Son of Seleucus I & Apama", "Co-regent in Babylon & victor over Galatians.", False),
        ("cls3_antiochus2", "Emperor Antiochus II Theos (261–246 BCE; Husband of Laodice & Berenice)", 18, "286–246 BCE (Dan 11:6; Eusebius)", "Son of Antiochus I", "Married Ptolemaic princess Berenice (Daniel 11:6 'King of the North').", False),
        ("cls3_seleucus2", "Emperor Seleucus II Callinicus (246–225 BCE)", 18, "265–225 BCE (Eusebius)", "Son of Antiochus II & Laodice I", "Father of Seleucus III & Antiochus III.", False),
        ("cls3_antiochus3", "Emperor Antiochus III the Great (223–187 BCE; Dan 11:11)", 18, "241–187 BCE (Eusebius; Polybius)", "Rebuilder of Seleucid Asia", "Restored Seleucid authority east to Bactria/India; wed daughter Cleopatra I Syra to Ptolemy V.", True),
        ("cls3_seleucus4", "Emperor Seleucus IV Philopator (187–175 BCE; 2 Macc 3)", 18, "218–175 BCE (2 Macc 3; Dan 11:20)", "Elder Son of Antiochus III", "Dispatched Heliodorus to Jerusalem Temple.", False),
        ("cls3_demetrius1_soter", "Emperor Demetrius I Soter (161–150 BCE; 1 Macc 7)", 18, "185–150 BCE (1 Macc 7; Josephus Ant. XII)", "Son of Seleucus IV", "Authorized High Priest Alcimus against Judas Maccabeus.", False),
    ], "greek", ["Eusebius Chronicle", "Appian Syriaca", "1–2 Maccabees", "Betham Tab. CIII"], "Seleucid Imperial Succession")
    nodes += [
        N("cls3_apama", "Queen Apama of Sogdia (Daughter of Spitamenes; Wife of Seleucus I)", "iranian", 18, "d. after 299 BCE (Arrian VII.4)", "Sogdian Queen of the Seleucid Empire", ["Arrian Anabasis VII.4"], "Daughter of Sogdian leader Spitamenes; sole Alexander-era queen marriage never repudiated."),
        N("cls3_cleopatra1_syra", "Queen Cleopatra I Syra of Egypt (Daughter of Antiochus III; Wife of Ptolemy V)", "greek", 18, "c. 204–176 BCE (Dan 11:17; Livy XXXV)", "Seleucid Princess Who Brought Name 'Cleopatra' to Egypt", ["Daniel 11:17", "Appian Syr. 5"], "Introduced Seleucid marriage link and name Cleopatra into the Ptolemaic house."),
        N("cls3_antiochus4", "Emperor Antiochus IV Epiphanes (175–164 BCE; Sparked Maccabean Revolt)", "greek", 18, "215–164 BCE (1 Macc 1; Dan 11:21)", "Younger Son of Antiochus III", ["1 Maccabees 1", "Josephus Ant. XII.5"], "Desecrated the Second Temple in 167 BCE, provoking Mattathias & Judas Maccabeus.", True),
        N("cls3_antiochus5", "Emperor Antiochus V Eupator (Son of Antiochus IV, 164–161 BCE)", "greek", 18, "173–161 BCE (1 Macc 6; Josephus Ant. XII.9)", "Boy-King of Syria", ["1 Maccabees 6"], "Young son of Antiochus IV.", False),
    ]
    edges += [
        E("cls3_seleucus1", "cls3_apama", "direct", "Susa Marriage (324 BCE): Seleucus I & Apama"),
        E("cls3_apama", "cls3_antiochus1", "direct", "Mother Apama -> Antiochus I"),
        E("cls3_antiochus3", "cls3_cleopatra1_syra", "direct", "Antiochus III -> Cleopatra I Syra"),
        E("cls3_cleopatra1_syra", "egr_ptol_05_ptolemy_v_epiphanes_cleopatr", "direct", "Marriage of Cleopatra I Syra & Ptolemy V (193 BCE)"),
        E("cls3_antiochus3", "cls3_antiochus4", "direct", "Younger son: Antiochus IV Epiphanes"),
        E("cls3_antiochus4", "has_mattathias", "cognate", "167 BCE persecution triggers Mattathias's revolt"),
        E("cls3_antiochus4", "cls3_antiochus5", "direct", "Antiochus IV -> Antiochus V"),
    ]

    chain([
        "cls_antigonids_epirus",
        ("cls3_antigonus1", "King Antigonus I Monophthalmus (d. 301 BCE at Ipsus)", 18, "382–301 BCE (Diodorus; Plutarch)", "Diadochos & Antigonid Founder", "Unifier of Asia until Battle of Ipsus.", False),
        ("cls3_demetrius_poliorcetes", "King Demetrius I Poliorcetes (337–283 BCE)", 18, "337–283 BCE (Plutarch Demetrius)", "Son of Antigonus I", "Father of Antigonus II Gonatas.", False),
        ("cls3_antigonus2", "King Antigonus II Gonatas of Macedon (277–239 BCE)", 18, "319–239 BCE (Eusebius Chronicle)", "Restorer of Antigonid Macedonia", "Son of Demetrius Poliorcetes.", False),
        ("cls3_philip5", "King Philip V of Macedon (221–179 BCE)", 18, "238–179 BCE (Polybius; Livy)", "Antigonid Adversary of Rome", "Father of final king Perseus.", False),
        ("cls3_perseus_macedon", "King Perseus of Macedon (Last King of Macedon, 179–168 BCE; Pydna)", 18, "212–166 BCE (Livy XLIV; Eusebius p.75)", "Last Sovereign of Antigonid Macedonia", "Defeated by Aemilius Paullus at Pydna (168 BCE) and interned at Alba Fucens.", False),
    ], "greek", ["Eusebius Chronicle", "Plutarch Lives", "Betham Tab. LXXVII"], "Antigonid Macedonian Succession")
    nodes.append(N("cls3_pyrrhus_epirus", "King Pyrrhus of Epirus (319–272 BCE; Aeacid Cousin of Alexander)", "greek", 18,
                   "319–272 BCE (Plutarch Life of Pyrrhus)", "Molossian King Claiming Descent From Achilles",
                   ["Plutarch Life of Pyrrhus 1–34", "Betham Tab. LXXXI"],
                   "Son of Aeacides; second cousin of Alexander the Great and renowned adversary of Rome ('Pyrrhic victory').", major=True))
    edges.append(E("grkr_b3_neoptolemus", "cls3_pyrrhus_epirus", "direct", "Molossian Aeacid descent -> King Pyrrhus"))

    # Pontus, Artaxiad Armenia, Greco-Bactria, Sicyon & Edessa
    chain([
        "cls_pontus_mithridates",
        ("cls3_mithridates1", "King Mithridates I Ktistes of Pontus (281–266 BCE)", 18, "281–266 BCE (Appian Mith. 9)", "Founder of Pontic Kingdom", "Claimed Achaemenid Persian noble lineage.", False),
        ("cls3_pharnaces1", "King Pharnaces I of Pontus (185–155 BCE)", 18, "185–155 BCE (Polybius)", "Son of Mithridates III", "Captured Sinope.", False),
        ("cls3_mithridates6", "King Mithridates VI Eupator ('The Great' / Poison King, 120–63 BCE)", 18, "135–63 BCE (Appian; Plutarch Pompey)", "Greatest Anatolian Adversary of Rome", "Fought three Mithridatic Wars against Sulla, Lucullus & Pompey; father of Cleopatra of Pontus & Pharnaces II.", True),
        ("cls3_pharnaces2", "King Pharnaces II of Pontus & Bosporus (Son of Mithridates VI; Battle of Zela 47 BCE)", 18, "97–47 BCE (Suetonius Julius 37)", "Subject of Caesar's 'Veni, vidi, vici'", "Son of Mithridates VI defeated by Julius Caesar at Zela (47 BCE).", False),
    ], "iranian", ["Appian Mithridatic Wars", "Betham Tab. XCV"], "Pontic Royal Succession")
    nodes.append(N("cls3_cleopatra_pontus", "Queen Cleopatra of Pontus (Daughter of Mithridates VI; Wife of Tigranes the Great)", "iranian", 18,
                   "fl. 94–66 BCE (Plutarch Lucullus; Betham Tab. LXXXIII)", "Pontic Princess Married to Armenia",
                   ["Plutarch Lucullus", "Betham Tab. LXXXIII"], "Daughter of Mithridates VI; married Tigranes II the Great of Armenia and bore Artavasdes II."))
    edges.append(E("cls3_mithridates6", "cls3_cleopatra_pontus", "direct", "Mithridates VI -> daughter Cleopatra"))

    chain([
        "cls_armenia_tigranes",
        ("cls3_artaxias1", "King Artaxias I of Armenia (189–160 BCE; Founder of Artaxata)", 18, "189–160 BCE (Strabo XI.14)", "Founder of Artaxiad Armenia", "Established Artaxiad Dynasty & capital Artaxata.", False),
        ("cls3_tigranes2_great", "Emperor Tigranes II the Great of Armenia (95–55 BCE; King of Kings)", 18, "140–55 BCE (Plutarch Lucullus; Betham Tab. LXXXIII)", "Emperor of Greater Armenia", "Built empire from Caspian to Syria; wed Cleopatra of Pontus.", True),
        ("cls3_artavasdes2", "King Artavasdes II of Armenia (55–34 BCE; Son of Tigranes II)", 18, "d. 31 BCE (Plutarch Antony; Dio)", "Author-King of Artaxiad Armenia", "Scholarly son of Tigranes the Great & Cleopatra of Pontus.", False),
    ], "iranian", ["Betham Tab. LXXXIII", "Strabo XI"], "Artaxiad Armenian Succession")
    edges.append(E("cls3_cleopatra_pontus", "cls3_artavasdes2", "direct", "Mother Cleopatra of Pontus -> Artavasdes II"))

    chain([
        "cls_bactria_menander",
        ("cls3_diodotus1", "King Diodotus I Soter of Bactria (250–239 BCE)", 18, "250–239 BCE (Justin XLI.4; Strabo XI)", "Founder of Greco-Bactrian Kingdom", "Broke away from Antiochus II in Bactria/Sogdia.", False),
        ("cls3_euthydemus1", "King Euthydemus I of Bactria (230–200 BCE)", 18, "230–200 BCE (Polybius XI.34)", "Defender of Bactra Against Antiochus III", "Father of Indo-Greek conqueror Demetrius I.", False),
        ("cls3_demetrius1_bactria", "King Demetrius I of Bactria (c. 200–180 BCE; Conqueror of Gandhara)", 18, "c. 200–180 BCE (Strabo XI.11.1)", "Son of Euthydemus I", "Extended Hellenistic rule into Northwest India.", False),
        ("cls3_menander1", "King Menander I Soter / King Milinda (165–130 BCE; Milinda Panha)", 18, "c. 165–130 BCE (Strabo XI; Milinda Panha)", "Indo-Greek Monarch of Sagala", "Central royal interlocutor of Buddhist classic Milinda Panha.", True),
    ], "greek", ["Strabo XI", "Milinda Panha", "Betham Tab. LXVIII"], "Greco-Bactrian & Indo-Greek Succession")

    nodes += [
        N("cls3_aegialeus_sicyon", "King Aegialeus of Sicyon (1st King in Eusebius Chronicle, p. 53)", "greek", 8,
          "Eusebius Chronicle p.53 (Synchronized With Belus & Ninus)", "First Attested Greek City-King in Eusebius",
          ["Eusebius Chronicle p.53", "Apollodorus II.i.1"],
          "Son of Inachus in Apollodorus; placed by Eusebius at the dawn of Greek chronology as contemporary of Nimrod/Belus & Ninus.", False),
        N("cls3_abgar5_edessa", "King Abgar V Ukkama of Osroene / Edessa (4 BCE–7 CE, 13–50 CE)", "mesopotamian", 19,
          "1st c. CE (Edessa — Eusebius HE I.13; Doctrine of Addai)", "Abgarid King of Syriac Edessa",
          ["Eusebius HE I.13", "Doctrine of Addai", "Betham Tab. LXXI"],
          "Abgarid king of Edessa prominent in early Syriac Christian historiography.", True),
    ]
    edges += [
        E("grk_inachus_io", "cls3_aegialeus_sicyon", "direct", "Apollodorus II.i.1 & Eusebius p.53: Inachus -> Aegialeus of Sicyon"),
        E("bib_nimrod", "cls3_aegialeus_sicyon", "cognate", "Eusebius Chronicle p.53: Synchronizes Aegialeus with Nimrod/Belus"),
        E("cls_adiabene_edessa", "cls3_abgar5_edessa", "direct", "Osroene / Edessa royal house"),
    ]

    # =========================================================================
    # 3. ALBA LONGA (ALL 14 KINGS) & ALL 7 KINGS OF ROME (Dionysius & Eusebius)
    # =========================================================================
    nodes += [
        N("rom3_king_latinus", "King Latinus of Laurentum (Father of Lavinia, Dionysius I.57–64)", "greek", 13, "12th c. BCE (Dionysius Ant. I.57–64; Livy I.1)", "Aboriginal King of Latium", ["Dionysius Roman Antiquities I.57–64"], "Welcomed Aeneas and gave daughter Lavinia in marriage.", False),
        N("rom3_lavinia", "Queen Lavinia (Daughter of Latinus; Wife of Aeneas; Mother of Silvius)", "greek", 13, "12th c. BCE (Dionysius I.60–70)", "Latin Princess & Mother of Alban Dynasty", ["Dionysius I.60–70", "Virgil Aeneid VII"], "Eponym of Lavinium; mother of Silvius Posthumus by Aeneas.", False),
        N("rom3_ascanius_iulus", "King Ascanius / Iulus (Son of Aeneas & Creusa; Founder of Alba Longa, Dionysius I.65–70)", "greek", 14, "c. 1150 BCE (Dionysius I.65–70; Livy I.3)", "Founder of Alba Longa & Claimed Ancestor of Gens Julia", ["Dionysius Roman Antiquities I.65–70", "Virgil Aeneid I"], "Son of Aeneas & Trojan Creusa; built Alba Longa.", True),
    ]
    edges += [
        E("rom3_king_latinus", "rom3_lavinia", "direct", "Dionysius I.60: King Latinus -> Lavinia"),
        E("grk_aeneas", "rom3_lavinia", "direct", "Marriage of Aeneas & Lavinia"),
        E("grk_aeneas", "rom3_ascanius_iulus", "direct", "Dionysius I.65: Aeneas -> Ascanius / Iulus"),
        E("grkr_b3_creusa_troy", "rom3_ascanius_iulus", "direct", "Mother Creusa -> Ascanius"),
        E("rom_alba_longa", "rom3_ascanius_iulus", "direct", "Founder of Alba Longa"),
    ]
    alba_chain = [
        ("rom3_silvius", "1. King Silvius Posthumus (Son of Aeneas & Lavinia, 29 yrs)", 14, "c. 1139–1110 BCE (Dionysius I.70–71)", "Second King of Alba Longa", "Half-brother of Ascanius; ancestor of all Alban Silvii.", False),
        ("rom3_aeneas_silvius", "2. King Aeneas Silvius (31 yrs, Dionysius I.71)", 14, "Dionysius I.71; Livy I.3", "King of Alba Longa", "Son of Silvius.", False),
        ("rom3_latinus_silvius", "3. King Latinus Silvius (51 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Aeneas Silvius.", False),
        ("rom3_alba", "4. King Alba Silvius (39 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Latinus Silvius.", False),
        ("rom3_atys_alba", "5. King Atys / Capetus I Silvius (26 yrs, Livy I.3)", 14, "Livy I.3; Dionysius I.71", "King of Alba Longa", "Son of Alba.", False),
        ("rom3_capys_alba", "6. King Capys Silvius (28 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Atys.", False),
        ("rom3_capetus", "7. King Capetus / Calpetus Silvius (13 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Capys.", False),
        ("rom3_tiberinus", "8. King Tiberinus Silvius (Eponym of River Tiber, Dionysius I.71)", 14, "Dionysius I.71; Livy I.3", "King of Alba Longa", "Drowned in the Albula, thereafter named the Tiber River.", False),
        ("rom3_agrippa_alba", "9. King Agrippa Silvius (41 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Tiberinus.", False),
        ("rom3_romulus_silvius", "10. King Romulus / Alladius Silvius (19 yrs, Dionysius I.71)", 14, "Dionysius I.71", "King of Alba Longa", "Son of Agrippa.", False),
        ("rom3_aventinus", "11. King Aventinus Silvius (37 yrs; Eponym of Aventine Hill)", 15, "Dionysius I.71; Livy I.3", "King of Alba Longa", "Buried on the Aventine Hill.", False),
        ("rom3_procas", "12. King Procas Silvius (23 yrs; Father of Numitor & Amulius)", 15, "c. 817–794 BCE (Dionysius I.71)", "King of Alba Longa", "Father of rightful heir Numitor and usurper Amulius.", False),
        ("rom3_numitor", "13. King Numitor Silvius of Alba Longa (Grandfather of Romulus & Remus)", 15, "c. 794–753 BCE (Dionysius I.76–85)", "Father of Rhea Silvia", "Restored to Alba Longa's throne by grandsons Romulus & Remus.", False),
        ("rom3_rhea_silvia", "Rhea Silvia / Ilia (Daughter of Numitor; Mother of Romulus & Remus)", 15, "8th c. BCE (Dionysius I.76–78)", "Vestal Princess of Alba Longa", "Mother of Rome's twin founders Romulus & Remus.", True),
        "grk_romulus_remus",
    ]
    chain(alba_chain, "greek", ["Dionysius Roman Antiquities I.70–85", "Livy I.3", "Eusebius Chronicle"], "Alban Royal Succession (Dionysius I.70–71)", start_parent="grk_aeneas")
    nodes.append(N("rom3_amulius", "King Amulius of Alba Longa (42-Year Usurper, Dionysius I.71, 76)", "greek", 15, "c. 794–753 BCE (Dionysius I.71, 76)", "Younger Brother of Numitor", ["Dionysius I.71–83"], "Overthrew Numitor before being slain by Romulus & Remus."))
    nodes.append(N("rom3_remus", "Remus (Twin Brother of Romulus, 753 BCE)", "greek", 15, "d. 753 BCE (Livy I.7; Dionysius I.87)", "Co-Founder Twin of Rome", ["Livy I.6–7", "Dionysius I.87"], "Twin brother of Romulus born to Rhea Silvia."))
    edges += [
        E("rom3_lavinia", "rom3_silvius", "direct", "Mother Lavinia -> Silvius"),
        E("rom3_procas", "rom3_amulius", "direct", "Procas -> Amulius"),
        E("rom3_rhea_silvia", "rom3_remus", "direct", "Rhea Silvia -> Remus"),
        E("rom_alba_longa", "rom3_procas", "expansion", "Alba Longa royal summary anchor"),
    ]

    # Remaining 6 Kings of Rome (Romulus -> ... -> Tarquinius Superbus -> Brutus)
    chain([
        "grk_romulus_remus",
        ("rom3_numa_pompilius", "2. King Numa Pompilius (Sabine Lawgiver King, 715–673 BCE)", 16, "715–673 BCE (Livy I.18; Dionysius II)", "2nd King of Rome", "Instituted Roman religious calendar, temples & priestly colleges.", False),
        ("rom3_tullus_hostilius", "3. King Tullus Hostilius (673–642 BCE; Absorbed Alba Longa)", 16, "673–642 BCE (Livy I.22–31)", "3rd King of Rome", "Destroyed Alba Longa and incorporated its noble Alban clans into Rome.", False),
        ("rom3_ancus_marcius", "4. King Ancus Marcius (642–617 BCE; Grandson of Numa)", 16, "642–617 BCE (Livy I.32–35)", "4th King of Rome", "Grandson of Numa Pompilius; built Sublician Bridge & Ostia port.", False),
        ("rom3_tarquinius_priscus", "5. King Lucius Tarquinius Priscus (+ Tanaquil, 616–579 BCE)", 16, "616–579 BCE (Livy I.35–40)", "5th King of Rome (Etruscan)", "Initiated Circus Maximus & Cloaca Maxima.", False),
        ("rom3_servius_tullius", "6. King Servius Tullius (578–535 BCE; Servian Constitution & Walls)", 16, "578–535 BCE (Livy I.41–48)", "6th King of Rome", "Reformed Roman centuriate classes; son-in-law of Tarquinius Priscus.", False),
        ("rom3_tarquinius_superbus", "7. King Lucius Tarquinius Superbus (535–509 BCE; Expelled at Republic's Founding)", 16, "535–509 BCE (Livy I.49–60)", "7th & Final King of Rome", "Expelled in 509 BCE by Lucius Junius Brutus, inaugurating the Roman Republic.", False),
        "mon_rom_brutus_founder",
    ], "greek", ["Livy Book I", "Dionysius Roman Antiquities II–IV", "Betham Tab. CXII"], "Roman Regal Succession (753–509 BCE)")
    edges.append(E("rom_seven_kings", "rom3_numa_pompilius", "direct", "Seven Kings of Rome anchor"))

    # =========================================================================
    # 4. GENS JULIA, JULIO-CLAUDIAN FAMILY TREE & CHRONICON PASCHALE LATE ROME
    # =========================================================================
    nodes += [
        N("rom3_julius_caesar", "Gaius Julius Caesar (100–44 BCE; Dictator Perpetuo)", "greek", 18, "100–44 BCE (Suetonius Divus Julius)", "Dictator of Rome & Great-Uncle / Adoptive Father of Augustus", ["Suetonius Divus Julius", "Plutarch Caesar"], "Descendant of Gens Julia; crossed Rubicon 49 BCE, wed Cornelia/Calpurnia, fathered Julia & Ptolemy XV Caesarion, adopted Octavian.", True),
        N("rom3_julia_minor", "Julia Minor (Sister of Julius Caesar; Grandmother of Augustus)", "greek", 18, "101–51 BCE (Suetonius Augustus 4, 8)", "Grandmother of Emperor Augustus", ["Suetonius Augustus 4, 8"], "Sister of Julius Caesar; wed Marcus Atius Balbus and bore Atia."),
        N("rom3_atia", "Atia Balba (Niece of Julius Caesar; Mother of Augustus & Octavia Minor)", "greek", 18, "85–43 BCE (Suetonius Augustus 4)", "Mother of Emperor Augustus", ["Suetonius Augustus 4"], "Daughter of Julia Minor & Balbus; wed Gaius Octavius and bore Octavia Minor & Augustus."),
        N("rom3_octavia_minor", "Octavia Minor (Sister of Augustus; Wife of Mark Antony; Progenitress of Caligula, Claudius & Nero!)", "greek", 18, "69–11 BCE (Plutarch Antony; Suetonius)", "Key Matriarch Linking Julii, Antonii & Julio-Claudians", ["Suetonius Augustus 61", "Plutarch Antony"], "Elder sister of Augustus; bore Antonia Minor by Mark Antony — uniting Julian & Antonian lines in Caligula, Claudius, and Nero!", True),
        N("rom3_augustus", "Emperor Augustus / Gaius Octavius (27 BCE–14 CE; Luke 2:1)", "greek", 19, "63 BCE – 14 CE (Luke 2:1; Suetonius Augustus)", "First Roman Emperor", ["Luke 2:1", "Suetonius Divus Augustus", "Betham Tab. CXXI"], "Adopted heir of Julius Caesar; ruled 27 BCE–14 CE during the birth of Jesus.", True),
        N("rom3_livia_drusilla", "Empress Livia Drusilla / Julia Augusta (Wife of Augustus; Mother of Tiberius & Drusus)", "greek", 19, "58 BCE – 29 CE (Tacitus Annals I, V)", "First Empress of Rome & Mother of Tiberius", ["Tacitus Annals V.1", "Suetonius Tiberius"], "Mother of Emperor Tiberius and General Drusus the Elder by Tiberius Claudius Nero; wed Augustus for 51 years.", True),
        N("rom3_marcus_agrippa", "Marcus Vipsanius Agrippa (c. 63–12 BCE; Builder of Pantheon & Co-Ruler)", "greek", 19, "63–12 BCE (Cassius Dio LIV)", "Son-in-Law of Augustus & Maternal Grandfather of Caligula", ["Cassius Dio LIII–LIV", "Suetonius Augustus 63"], "Wed Augustus's daughter Julia the Elder, fathering Gaius, Lucius, Agrippina the Elder & Agrippa Postumus."),
        N("rom3_julia_elder", "Julia the Elder (Sole Biological Child of Emperor Augustus)", "greek", 19, "39 BCE – 14 CE (Suetonius Augustus 63–65)", "Daughter of Augustus & Scribonia", ["Suetonius Augustus 63–65"], "Mother of Agrippina the Elder by Marcus Agrippa."),
        N("rom3_drusus_elder", "General Nero Claudius Drusus (Son of Livia; Brother of Tiberius; Husband of Antonia)", "greek", 19, "38–9 BCE (Suetonius Claudius 1)", "Stepson of Augustus & Father of Germanicus & Claudius", ["Suetonius Claudius 1"], "Brother of Emperor Tiberius; wed Antonia Minor and fathered Germanicus and Emperor Claudius."),
        N("rom3_antonia_minor", "Antonia Minor (Daughter of Mark Antony & Octavia; Mother of Germanicus & Claudius)", "greek", 19, "36 BCE – 37 CE (Suetonius Claudius 11; Josephus Ant. XVIII.6)", "Matriarch of Three Generations of Roman Emperors", ["Suetonius Claudius 1, 11", "Josephus Ant. XVIII.6.6"], "Befriended Berenice I & young Herod Agrippa I in Rome; bore Germanicus, Livilla & Emperor Claudius.", True),
        N("rom3_germanicus", "General Germanicus Julius Caesar (15 BCE–19 CE; Father of Caligula)", "greek", 19, "15 BCE – 19 CE (Tacitus Annals I–II; Suetonius Caligula 1–7)", "Celebrated Heir Adopted by Tiberius", ["Tacitus Annals I–II", "Suetonius Caligula 1–7"], "Son of Drusus the Elder & Antonia Minor; wed Agrippina the Elder, bearing Caligula & Agrippina the Younger."),
        N("rom3_agrippina_elder", "Agrippina the Elder (Daughter of Julia & Agrippa; Mother of Caligula & Agrippina II)", "greek", 19, "c. 14 BCE – 33 CE (Tacitus Annals I–VI)", "Granddaughter of Augustus", ["Tacitus Annals I–VI"], "Granddaughter of Augustus; mother of Emperor Caligula and Agrippina the Younger."),
        N("rom3_agrippina_younger", "Empress Agrippina the Younger (Sister of Caligula; Wife of Claudius; Mother of Nero)", "greek", 19, "15–59 CE (Tacitus Annals XII–XIV; Suetonius Nero 6)", "Daughter of Germanicus & Mother of Emperor Nero", ["Tacitus Annals XII–XIV", "Suetonius Nero"], "Great-granddaughter of Augustus; mother of Emperor Nero."),
        # Chronicon Paschale Late Roman Imperial Houses
        N("rom3_constantius_chlorus", "Emperor Constantius I Chlorus (Tetrarch, 293–306 CE; Father of Constantine I)", "greek", 19, "250–306 CE (Chronicon Paschale; Eusebius)", "Western Augustus & Father of Constantine the Great", ["Chronicon Paschale", "Eusebius VC I"], "Father of Constantine the Great by St. Helena."),
        N("rom3_st_helena", "Empress St. Helena Augusta (Mother of Constantine the Great, c. 246–330 CE)", "greek", 19, "c. 246–330 CE (Eusebius VC III; Chronicon Paschale)", "Mother of Constantine I", ["Eusebius Vita Constantini III", "Chronicon Paschale"], "Mother of first Christian Emperor Constantine I."),
        N("rom3_constantine2", "Emperor Constantine II (Son of Constantine I, 337–340 CE)", "greek", 19, "316–340 CE (Chronicon Paschale)", "Eldest Son of Constantine & Fausta", ["Chronicon Paschale"], "Ruled Gaul, Spain & Britain after 337 CE."),
        N("rom3_constantius2", "Emperor Constantius II (Son of Constantine I, 337–361 CE)", "greek", 19, "317–361 CE (Chronicon Paschale)", "Middle Son of Constantine & Eastern Emperor", ["Chronicon Paschale"], "Ruled the Eastern Roman Empire 337–361 CE."),
        N("rom3_constans", "Emperor Constans I (Son of Constantine I, 337–350 CE)", "greek", 19, "323–350 CE (Chronicon Paschale)", "Youngest Son of Constantine & Fausta", ["Chronicon Paschale"], "Ruled Italy, Africa & Illyricum."),
        N("rom3_arcadius", "Emperor Arcadius (Elder Son of Theodosius I, 395–408 CE; Chronicon Paschale p. 80)", "greek", 19, "377–408 CE (Chronicon Paschale p.80)", "First Emperor of Permanently Divided Eastern Roman Empire", ["Chronicon Paschale (Whitby p.80)"], "Proclaimed Augustus by father Theodosius I at the Hebdomon in Constantinople (383 CE); father of Theodosius II.", True),
        N("rom3_honorius", "Emperor Honorius (Younger Son of Theodosius I, 395–423 CE)", "greek", 19, "384–423 CE (Chronicon Paschale)", "Western Roman Emperor", ["Chronicon Paschale"], "Son of Theodosius I & Aelia Flaccilla."),
        N("rom3_galla_placidia", "Empress Galla Placidia (Daughter of Theodosius I; Queen of Visigoths & Augusta, c. 390–450 CE)", "greek", 19, "c. 390–450 CE (Chronicon Paschale)", "Daughter of Theodosius I & Mother of Valentinian III", ["Chronicon Paschale"], "Daughter of Theodosius I & Galla; wed Visigothic King Athaulf and later Emperor Constantius III."),
        N("rom3_valentinian3", "Emperor Valentinian III (Son of Galla Placidia, 425–455 CE)", "greek", 19, "419–455 CE (Chronicon Paschale)", "Grandson of Theodosius I", ["Chronicon Paschale"], "Western Emperor during Attila's campaigns."),
    ]
    edges += [
        E("grk_julius_augustus", "rom3_julius_caesar", "direct", "Gens Julia -> Gaius Julius Caesar"),
        E("grk_julius_augustus", "rom3_julia_minor", "direct", "Gens Julia -> Julia Minor"),
        E("rom3_julia_minor", "rom3_atia", "direct", "Mother Julia Minor -> Atia Balba"),
        E("rom3_atia", "rom3_octavia_minor", "direct", "Mother Atia -> Octavia Minor"),
        E("rom3_atia", "rom3_augustus", "direct", "Mother Atia -> Emperor Augustus"),
        E("rom3_julius_caesar", "rom3_augustus", "expansion", "Adoptive father Julius Caesar -> Augustus"),
        E("rom_julio_claudians", "rom3_augustus", "direct", "Julio-Claudian Dynasty founder Augustus"),
        E("rom3_augustus", "rom3_livia_drusilla", "direct", "51-year marriage of Augustus & Empress Livia"),
        E("rom3_augustus", "rom3_julia_elder", "direct", "Father Augustus -> Julia the Elder"),
        E("rom3_julia_elder", "rom3_marcus_agrippa", "direct", "Marriage of Julia & Marcus Agrippa"),
        E("rom3_julia_elder", "rom3_agrippina_elder", "direct", "Mother Julia -> Agrippina the Elder"),
        E("rom3_marcus_agrippa", "rom3_agrippina_elder", "direct", "Father Marcus Agrippa -> Agrippina the Elder"),
        E("rom3_livia_drusilla", "mon_rom_tiberius", "direct", "Mother Livia -> Emperor Tiberius"),
        E("rom3_livia_drusilla", "rom3_drusus_elder", "direct", "Mother Livia -> Drusus the Elder"),
        E("mon_rom_mark_antony", "rom3_octavia_minor", "direct", "Marriage of Mark Antony & Octavia Minor"),
        E("rom3_octavia_minor", "rom3_antonia_minor", "direct", "Mother Octavia Minor -> Antonia Minor"),
        E("mon_rom_mark_antony", "rom3_antonia_minor", "direct", "Father Mark Antony -> Antonia Minor"),
        E("rom3_drusus_elder", "rom3_antonia_minor", "direct", "Marriage of Drusus the Elder & Antonia Minor"),
        E("rom3_drusus_elder", "rom3_germanicus", "direct", "Father Drusus -> General Germanicus"),
        E("rom3_antonia_minor", "rom3_germanicus", "direct", "Mother Antonia Minor -> General Germanicus"),
        E("rom3_drusus_elder", "mon_rom_claudius", "direct", "Father Drusus -> Emperor Claudius"),
        E("rom3_antonia_minor", "mon_rom_claudius", "direct", "Mother Antonia Minor -> Emperor Claudius"),
        E("rom3_germanicus", "rom3_agrippina_elder", "direct", "Marriage of Germanicus & Agrippina the Elder"),
        E("rom3_germanicus", "mon_rom_caligula", "direct", "Father Germanicus -> Emperor Caligula"),
        E("rom3_agrippina_elder", "mon_rom_caligula", "direct", "Mother Agrippina -> Emperor Caligula"),
        E("rom3_germanicus", "rom3_agrippina_younger", "direct", "Father Germanicus -> Agrippina the Younger"),
        E("rom3_agrippina_elder", "rom3_agrippina_younger", "direct", "Mother Agrippina I -> Agrippina the Younger"),
        E("rom3_agrippina_younger", "mon_rom_nero", "direct", "Mother Agrippina II -> Emperor Nero"),
        E("rom_constantine_byzantium", "rom3_constantius_chlorus", "direct", "Constantinian Dynasty founder"),
        E("rom3_constantius_chlorus", "rom3_st_helena", "direct", "Constantius Chlorus & St. Helena"),
        E("rom3_constantius_chlorus", "mon_rom_constantine1", "direct", "Constantius Chlorus -> Constantine I"),
        E("rom3_st_helena", "mon_rom_constantine1", "direct", "Mother St. Helena -> Constantine I"),
        E("mon_rom_constantine1", "rom3_constantine2", "direct", "Constantine I -> Constantine II"),
        E("mon_rom_constantine1", "rom3_constantius2", "direct", "Constantine I -> Constantius II"),
        E("mon_rom_constantine1", "rom3_constans", "direct", "Constantine I -> Constans I"),
        E("mon_rom_theodosius1", "rom3_arcadius", "direct", "Chronicon Paschale p.80: Theodosius I -> Arcadius"),
        E("mon_rom_theodosius1", "rom3_honorius", "direct", "Theodosius I -> Honorius"),
        E("mon_rom_theodosius1", "rom3_galla_placidia", "direct", "Theodosius I -> Galla Placidia"),
        E("rom3_galla_placidia", "rom3_valentinian3", "direct", "Mother Galla Placidia -> Valentinian III"),
    ]

    return {
        "module": "45_wave3_classical_mediterranean_rome",
        "title": "Wave 3 Person-by-Person Classical Mediterranean, Phoenicia/Carthage, Hellenistic Kingdoms, Alba Longa (14 Kings), 7 Kings of Rome & Julio-Claudian/Paschale Families",
        "nodes": nodes,
        "edges": edges,
    }
