"""
Module 18: Complete 31 Dynasties of Ancient Egypt, Manetho's Gods/Demigods/Spirits of the Dead,
Palermo Stone Predynastic Kings, Theban Priest-Kings, Pasenhor Libyan Genealogy,
Complete Ptolemaic Dynasty, and Complete Napatan & Meroitic Kings of Nubia/Kush (Person-by-Person).

Sources mined from sources/:
- manethowithengli00maneuoft.pdf (Manetho's Aegyptiaca, Loeb Classical Library, Waddell 1940)
- Ancient Records Of Egypt Vol-1.pdf (J.H. Breasted, Palermo Stone & Dynasties I-XVII)
- King list 1-6.pdf (Sjef Willockx 2006, Dynasties I-VI critical synchronization)
- The book of the kings of Egypt.pdf (E.A. Wallis Budge Vol. II, Dynasties XX-XXX, Ptolemies & Napata/Meroe)
"""

from . import N, E, add_chain


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. MANETHO'S PREDYNASTIC GODS, DEMIGODS, SHEMSU-HOR & PALERMO STONE KINGS
    # -------------------------------------------------------------------------
    nodes += [
        N("eg_manetho_demigods", "Manetho's Divine & Shemsu-Hor Horizon (Pre-Menes Era)", "levant_egypt", 3, "Predynastic Mythic Era (Manetho Fr. 1-4, Loeb pp. 3-19)",
          "Manetho Pre-Dynastic Canon Anchor", ["Manetho Aegyptiaca Fr. 1-4 (Loeb)", "Turin Royal Canon"],
          "Manetho's opening divine & demigod kingship sequence preceding Menes: Ptah -> Re -> Shu -> Geb -> Osiris -> Seth -> Horus -> 9 Demigods -> Shemsu-Hor ('Spirits of the Dead').",
          ["Shemsu-Hor", "Bydis/Bites", "Manetho Divine Dynasties"], major=True),
        N("eg_palermo_predynastic", "King Scorpion I/II & Palermo Stone Lower Egypt Kings (Dynasty 0)", "levant_egypt", 5, "c. 3200-3000 BCE (Breasted Vol. I §90, p. 57)",
          "Earliest Historically Inscribed Rulers of the Nile Before Narmer", ["Palermo Stone (Breasted Vol. I p. 57)", "Dynasty 0 Inscriptions"],
          "Pre-Unification Red Crown kings preserved on Row 1 of the Palermo Stone (Seka, Khayu, Tiu, Thesh, Neheb, Wazner, Mekh) alongside Upper Egyptian Dynasty 0 rulers Iry-Hor, Ka & King Scorpion.",
          ["Seka", "Khayu", "Tiu", "Thesh", "Neheb", "Wazner", "Mekh", "King Scorpion"]),
    ]

    # -------------------------------------------------------------------------
    # 2. DYNASTIC HORIZON ANCHORS (Preserving Existing IDs Across Modules)
    # -------------------------------------------------------------------------
    dyn_anchors = [
        ("eg_dyn1_complete", "Dynasty I Horizon (Thinite, 8 Kings, c. 2982–2803 BCE)", 6, "c. 2982-2803 BCE (Willockx pp. 7-8; Manetho Fr. 6-7)", "Complete Unification Dynasty", "179 historical years (Manetho: 253 yrs); Africanus makes every king son of his predecessor.", {}),
        ("eg_dyn2_complete", "Dynasty II Horizon (9 Kings, c. 2803–2657 BCE)", 6, "c. 2803-2657 BCE (Willockx pp. 9-10; Manetho Fr. 8-10)", "Consolidation of Memphis & Horus/Seth Reconciliation", "Under Nynetjer (Binothris) it was decreed women could hold royal dignity.", {}),
        ("eg_dyn3_complete", "Dynasty III Horizon (Memphite Step Pyramid Era, c. 2657–2589 BCE)", 7, "c. 2657-2589 BCE (Willockx p. 11; Manetho Fr. 11-12)", "Dawn of Stone Pyramid Architecture", "Djoser & Imhotep built the Saqqara Step Pyramid; Huni inaugurated the royal cartouche.", {}),
        ("eg_dyn4_complete", "Dynasty IV Horizon (Giza Great Pyramid Builders, c. 2589–2454 BCE)", 7, "c. 2589-2454 BCE (Willockx p. 12; Manetho Fr. 14-16)", "Pyramid Dynasty of Dahshur & Giza", "Sneferu, Khufu, Djedefre, Khafre, Baka, Menkaure, Shepseskaf & Queen Khentkawes.", {}),
        ("eg_dyn5_complete", "Dynasty V Horizon (Solar Kings & Pyramid Texts, c. 2454–2297 BCE)", 8, "c. 2454-2297 BCE (Willockx pp. 13-14; Manetho Fr. 18)", "Sun Temple Builders & Pyramid Texts", "Palermo Stone Annals compiled under Userkaf; oldest Pyramid Texts inscribed under Unas.", {}),
        ("eg_dyn6_complete", "Dynasty VI Horizon (Memphite Old Kingdom Finale, c. 2297–2168 BCE)", 8, "c. 2297-2168 BCE (Willockx pp. 15-16; Manetho Fr. 20-21)", "Era of Pepi II & Queen Nitocris", "Concludes the Old Kingdom with 94-year reign of Pepi II and Queen Nitocris.", {"major": True}),
        ("eg_dyn7_10_fip", "First Intermediate Period (Dynasties VII–X, Khety/Achthoes & Merikare)", 9, "c. 2168-2040 BCE (Manetho Fr. 23-30; Breasted Vol. I)", "Rival Houses of Memphis & Heracleopolis", "Khety / Achthoes of Heracleopolis (Teaching for King Merikare).", {"altNames": ["Achthoes / Khety", "Merikare"]}),
        ("eg_dyn11_complete", "Dynasty XI Horizon (Theban Middle Kingdom Unifiers, c. 2160–2000 BCE)", 10, "c. 2160-2000 BCE (Breasted Vol. I §63; Manetho Fr. 31-32)", "Theban Unifiers of Egypt", "Intef I–III and Mentuhotep II–IV reunified Upper & Lower Egypt.", {}),
        ("eg_dyn12_complete", "Dynasty XII Horizon (Middle Kingdom Golden Age, 2000–1788 BCE)", 11, "2000-1788 BCE (Breasted Vol. I §64; Manetho Fr. 34-36)", "Classical Peak of Egyptian Literature & Labyrinth", "Manetho preserves direct parent-child succession through Queen Sobekneferu (Scemiophris).", {"major": True}),
        ("eg_dyn13_14_sip", "Dynasties XIII–XIV Horizon (Second Intermediate Period)", 12, "c. 1788-1650 BCE (Manetho Fr. 38-42; Artapanus)", "Theban & Eastern Delta Transition", "Sobekhotep IV (Chenephres in Artapanus) and Dedumose (Tutimaeus).", {}),
        ("eg_dyn15_17_hyksos_thebes", "Dynasties XV–XVII Horizon (Great Hyksos & Theban Liberation)", 13, "c. 1650-1550 BCE (Manetho Fr. 42-49 via Josephus Against Apion)", "Hyksos Rulers of Avaris & Theban Liberators", "Josephus (quoting Manetho verbatim) preserved the 6 Great Hyksos rulers until Seqenenre & Kamose launched liberation.", {}),
        ("eg_dyn18_early", "Dynasty XVIII Horizon (Thutmoside Empire, 1550–1391 BCE)", 14, "1550-1391 BCE (Manetho Fr. 50-53; Breasted Vol. I)", "New Kingdom Imperial Expansion", "Ahmose I through Hatshepsut, Thutmose III & Thutmose IV.", {}),
        ("eg_dyn18_amarna_end", "Dynasty XVIII Late Horizon (Amarna & Harmais/Danaus Transition)", 15, "1391-1292 BCE (Manetho Fr. 50-53; Amarna Letters)", "Amarna Revolution & Horemheb/Danaus Synchronism", "Manetho Fr. 50/53 identifies Horemheb ('Harmais') = Danaus & Ramesses/Seti = Aegyptus.", {}),
        ("eg_dyn19_complete", "Dynasty XIX Horizon (Ramesside & Trojan War Synchronism)", 15, "1292-1189 BCE (Manetho Fr. 55-56; Breasted Vol. I)", "Ramesside Empire & Queen Twosret / Thuoris", "Manetho notes under Queen Twosret ('Thuoris') Troy was taken.", {}),
        ("eg_dyn20_complete", "Dynasty XX Horizon (Ramesside II & Sea Peoples Defense)", 16, "1189-1077 BCE (Budge Vol. II pp. 1-20; Manetho Fr. 57)", "Ten Sons of Ramesses III to High Priest Herihor", "Concludes the New Kingdom down to Ramesses XI.", {}),
        ("eg_dyn21_tanite_theban", "Dynasty XXI Horizon (Tanite Pharaohs & Theban Priest-Kings)", 16, "1077-943 BCE (Budge Vol. II pp. 20-34; Manetho Fr. 58-59)", "Divided Egypt (Biblical Era of David & Solomon)", "Siamun & Psusennes II in Tanis alongside High Priests Herihor to Pinudjem II at Thebes.", {"major": True}),
        ("eg_dyn22_libyan_pasenhor", "Dynasty XXII Horizon (Libyan Bubastite — Stele of Pasenhor)", 17, "943-716 BCE (Budge Vol. II pp. 35-60; Manetho Fr. 60-61)", "15-Generation Meshwesh Libyan Genealogy", "Serapeum Stele of Pasenhor traces Shoshenq I back 6 generations to Buyuwawa and forward to Shoshenq V.", {}),
        ("eg_dyn23_24_saite", "Dynasties XXIII–XXIV Horizon (Delta Coalitions & Bocchoris)", 17, "818-715 BCE (Budge Vol. II pp. 60-69; Manetho Fr. 62-65)", "Delta Rival Houses Resisting Kush", "Pedubast I, Osorkon III, Tefnakht I & lawgiver Bakenranef (Bocchoris).", {}),
        ("eg_dyn25_kush_budge", "Dynasty XXV Horizon (Kushite Pharaohs & God's Wives Amenirdis/Shepenupet)", 17, "744-656 BCE (Budge Vol. II pp. 70-78, 195-199; Manetho Fr. 66-67)", "Nubian Reunifiers of Egypt", "Unifies Kushite royal family with 26th Dynasty Saite succession.", {}),
        ("eg_dyn26_saite_complete", "Dynasty XXVI Horizon (Saite Renaissance, 664–525 BCE)", 17, "664-525 BCE (Budge Vol. II pp. 78-90; Manetho Fr. 68-69; Jer 44:30)", "Last Great Native Egyptian Renaissance", "Psamtik I, Necho II, Psamtik II, Apries (Hophra), Amasis II & Psamtik III.", {"major": True}),
        ("eg_dyn27_31_late_native", "Dynasties XXVII–XXXI Horizon (Persian Conquests & Last Native Pharaohs)", 18, "525-332 BCE (Budge Vol. II pp. 91-106; Manetho Fr. 70-75)", "Native Resistance Through Nectanebo II to Alexander (332 BCE)", "Amyrtaeus, Nepherites I, Hakor, Nectanebo I, Teos & Nectanebo II.", {"major": True}),
        ("eg_ptolemies_complete", "Ptolemaic Dynasty Horizon (Alexandria, 305–30 BCE)", 18, "305-30 BCE (Budge Vol. II pp. 107-154)", "Macedonian-Greek Pharaohs of Alexandria (Septuagint & Rosetta Stone)", "All 15 Ptolemies & 7 Cleopatras down to Cleopatra VII & Ptolemy XV Caesarion.", {}),
    ]
    add_chain(nodes, edges, dyn_anchors, start_parent="eg_menes", start_edge_type="direct",
              start_edge_label="Manetho & Budge Chronological Framework",
              tradition="levant_egypt", default_edge_type="expansion", default_sources=["Manetho Aegyptiaca (Loeb)", "Budge Book of Kings Vol. II"])

    nodes += [
        N("af_napata_aspelta_nastasen", "Napatan Kingdom of Kush Horizon (c. 653–315 BCE)", "african", 18, "c. 653-315 BCE (Budge Vol. II pp. 199-205)",
          "Post-25th Dynasty Nubian Pyramid Builders of Nuri", ["Budge Book of the Kings of Egypt Vol. II (pp. 199-205)"],
          "Napatan succession at Nuri & Jebel Barkal from Atlanersa through Nastasen.", major=True),
        N("af_meroe_ergamenes_natakamani", "Meroitic Kingdom Horizon (c. 270 BCE – 50 CE)", "african", 19, "c. 270 BCE – 50 CE (Budge Vol. II pp. 205-214; Diodorus III.6; Acts 8:27)",
          "Meroitic Civilization & Biblical Candace Era", ["Budge Book of the Kings of Egypt Vol. II (pp. 205-214)", "Acts 8:27"],
          "Meroitic monarchs from Arqamani (Ergamenes) to Natakamani & Kandake Amanitore."),
    ]

    edges += [
        E("eg_ptah", "eg_manetho_demigods", "expansion", "Manetho Fr. 1: Ptah -> Re -> Shu -> Geb -> Osiris -> Horus -> Demigods"),
        E("eg_manetho_demigods", "eg_palermo_predynastic", "expansion", "Shemsu-Hor -> Palermo Stone Predynastic Kings"),
        E("eg_palermo_predynastic", "eg_menes", "direct", "Dynasty 0 -> Unification under Narmer/Menes"),
        E("eg_dyn18_amarna_end", "grk_aegyptus_danaus", "syncretic", "Manetho Fr. 50/53: Horemheb (Harmais) = Danaus & Seti/Ramesses = Aegyptus"),
        E("eg_dyn19_complete", "grk_priam_hector", "cognate", "Manetho Fr. 55–57: Queen Twosret (Thuoris) synchronized with Fall of Troy"),
        E("eg_dyn21_tanite_theban", "jud_solomon", "cognate", "Siamun era: Pharaoh's daughter marries King Solomon (1 Kgs 3:1, 9:16)"),
        E("eg_dyn22_libyan_pasenhor", "eg_shoshenq1", "direct", "Stele of Pasenhor anchor"),
        E("eg_dyn25_kush_budge", "af_taharqa", "direct", "Kushite Dynasty XXV anchor"),
        E("eg_dyn26_saite_complete", "for_pharaoh_neco", "direct", "Saite Dynasty XXVI anchor"),
        E("eg_dyn27_31_late_native", "ir_cambyses2_atossa", "cognate", "Cambyses II conquers Egypt (Dynasty XXVII, 525 BCE)"),
        E("eg_dyn27_31_late_native", "grk_alexander", "cognate", "Alexander the Great enters Egypt (332 BCE)"),
        E("eg_ptolemies_complete", "eg_ptolemy_cleopatra", "direct", "Ptolemaic Dynasty anchor"),
        E("af_tantamani", "af_napata_aspelta_nastasen", "direct", "Post-25th Dynasty Napatan Kingdom of Kush"),
        E("af_napata_aspelta_nastasen", "af_meroe_ergamenes_natakamani", "direct", "Napatan -> Meroitic transition"),
        E("af_meroe_ergamenes_natakamani", "af_kandakes", "direct", "Meroitic Kandake Queens"),
    ]

    # -------------------------------------------------------------------------
    # 3. SEQUENTIAL PERSON-BY-PERSON PHARAOH CHAINS (DYNASTIES I–XXX)
    # -------------------------------------------------------------------------
    def link_seq(items, tradition="levant_egypt", sources=None, edge_type="direct", edge_label="Dynastic / Royal Succession"):
        srcs = sources or ["Manetho Aegyptiaca (Loeb)", "Willockx King List 1-6", "Budge Book of Kings Vol. II"]
        prev = None
        for it in items:
            if isinstance(it, str):
                prev = it
                continue
            nid, name, tier, era, role, note, maj = it[0], it[1], it[2], it[3], it[4], it[5], it[6]
            nodes.append(N(nid, name, tradition, tier, era, role, srcs, note, major=maj))
            if prev:
                edges.append(E(prev, nid, edge_type, edge_label))
            prev = nid

    # Dynasties I–II (Narmer -> Hor-Aha -> ... -> Khasekhemwy -> Djoser)
    link_seq([
        "eg_menes", "eg_hor_aha",
        ("egr_d1_2_01_djer_kenkenes_dyn_i_47_yrs", "Djer / Kenkenes (Dyn. I, 47 yrs)", 6, "c. 2950 BCE (Willockx p.7; Manetho)", "3rd Pharaoh of Dynasty I", "Son of Hor-Aha; tomb at Abydos.", False),
        ("egr_d1_2_02_djet_uenephes_dyn_i_13_yrs", "Djet / Uenephes (Dyn. I, 13 yrs)", 6, "c. 2910 BCE (Willockx p.7; Manetho)", "4th Pharaoh of Dynasty I", "Son of Djer; wed Queen Merneith.", False),
        ("egr_d1_2_03_queen_merneith_regent_of_dyn", "Queen Merneith (Regent of Dyn. I; Mother of Den)", 6, "c. 2900 BCE (Willockx p.7)", "Regent Queen of Dynasty I", "Consort of Djet and mother-regent for young King Den; buried with royal honors at Abydos.", True),
        ("egr_d1_2_04_adjib_miebis_dyn_i", "Adjib / Miebis (Dyn. I)", 6, "c. 2850 BCE (Willockx p.8; Manetho)", "6th Pharaoh of Dynasty I", "Son of Den.", False),
        ("egr_d1_2_05_semerkhet_semempses_dyn_i", "Semerkhet / Semempses (Dyn. I)", 6, "c. 2840 BCE (Willockx p.8; Manetho)", "7th Pharaoh of Dynasty I", "7th king of the Thinite First Dynasty.", False),
        ("egr_d1_2_06_qa_a_bieneches_dyn_i", "Qa'a / Bieneches (Dyn. I)", 6, "c. 2820–2803 BCE (Willockx p.8; Manetho)", "Last Pharaoh of Dynasty I", "Last king buried in the Abydos Umm el-Qa'ab royal necropolis.", False),
        ("egr_d1_2_07_hotepsekhemwy_boethos_dyn_ii", "Hotepsekhemwy / Boethos (Dyn. II Founder)", 6, "c. 2803 BCE (Willockx p.9; Manetho Fr. 8)", "Founder of Dynasty II", "Moved royal tombs to Saqqara.", False),
        ("egr_d1_2_08_nebre_kaiechos_dyn_ii", "Nebre / Kaiechos (Dyn. II)", 6, "c. 2780 BCE (Willockx p.9; Manetho Fr. 8)", "2nd Pharaoh of Dynasty II", "First pharaoh to incorporate Ra into his royal name.", False),
        ("egr_d1_2_09_nynetjer_binothris_dyn_ii", "Nynetjer / Binothris (Dyn. II)", 6, "c. 2760 BCE (Willockx p.9; Manetho Fr. 8)", "3rd Pharaoh of Dynasty II", "Manetho records that in his reign women were declared eligible to hold royal dignity.", False),
        ("egr_d1_2_10_weneg_tlas_dyn_ii", "Weneg / Tlas (Dyn. II)", 6, "c. 2730 BCE (Willockx p.9; Manetho)", "Pharaoh of Dynasty II", "Mid-2nd Dynasty Memphite ruler.", False),
        ("egr_d1_2_11_sened_sethenes_dyn_ii", "Sened / Sethenes (Dyn. II)", 6, "c. 2715 BCE (Willockx p.9; Manetho)", "Pharaoh of Dynasty II", "Revered in Memphite funerary cults.", False),
        ("egr_d1_2_12_seth_peribsen_dyn_ii", "Seth-Peribsen (Dyn. II)", 6, "c. 2700 BCE (Willockx p.10)", "Pharaoh of Dynasty II", "Took a Seth-name above his Abydos serekh before Khasekhemwy reconciled Horus and Seth.", False),
        "eg_dyn2_khasekhemwy",
    ], edge_label="Dynasty I–II Succession (Willockx; Manetho)")
    edges.append(E("eg_den_qaa", "egr_d1_2_04_adjib_miebis_dyn_i", "direct", "Den -> Adjib (Dynasty I)"))
    edges.append(E("eg_dyn1_complete", "eg_hor_aha", "direct", "Dynasty I sequence anchor"))

    # Old Kingdom Dynasties III–VI (Khasekhemwy -> Sanakht -> Djoser -> ... -> Pepi II -> Nitocris)
    link_seq([
        "eg_dyn2_khasekhemwy",
        ("egr_d3_6_01_sanakht_necherophes_dyn_iii", "Sanakht / Necherophes (Dyn. III)", 7, "c. 2657 BCE (Willockx p.11; Manetho Fr. 11)", "1st Pharaoh of Dynasty III", "Elder brother/predecessor of Djoser; buried at Beit Khallaf.", False),
        "eg_djoser",
        ("egr_d3_6_02_sekhemkhet_tyris_dyn_iii", "Sekhemkhet / Tyris (Dyn. III)", 7, "c. 2630 BCE (Willockx p.11; Manetho Fr. 11)", "Successor of Djoser", "Builder of the Buried Pyramid at Saqqara.", False),
        ("egr_d3_6_03_khaba_dyn_iii", "Khaba (Dyn. III)", 7, "c. 2615 BCE (Willockx p.11)", "Pharaoh of Dynasty III", "Builder of the Layer Pyramid at Zawyet el-Aryan.", False),
        ("egr_d3_6_04_huni_kerpheres_dyn_iii", "Huni / Kerpheres (Dyn. III)", 7, "c. 2600–2589 BCE (Willockx p.11; Manetho)", "Last Pharaoh of Dynasty III", "Father of Queen Hetepheres I and builder of Meidum.", False),
        "eg_sneferu", "eg_khufu",
        ("egr_d3_6_05_djedefre_ratoises_dyn_iv", "Djedefre / Ratoises (Dyn. IV)", 7, "c. 2550 BCE (Willockx p.12; Manetho)", "Son & Successor of Khufu", "Son of Khufu; built pyramid at Abu Rawash and first took 'Son of Ra' title.", False),
        ("egr_d3_6_06_baka_bicheris_dyn_iv", "Baka / Bicheris (Dyn. IV)", 7, "c. 2520 BCE (Manetho Fr. 14)", "4th Dynasty Ruler", "Manetho's Bicheris placed amid Khufu's sons.", False),
        "eg_khafre_menkaure",
        ("egr_d3_6_07_shepseskaf_dyn_iv", "Shepseskaf (Dyn. IV)", 7, "c. 2472–2467 BCE (Willockx p.12)", "Son of Menkaure", "Built Mastabat el-Fir'aun at South Saqqara.", False),
        ("egr_d3_6_08_queen_khentkawes_dyn_iv_v_br", "Queen Khentkawes I (Dyn. IV/V Bridge; 'Mother of Two Kings')", 7, "c. 2465–2450 BCE (Willockx p.12; Budge)", "Daughter of Menkaure & Mother of Dyn. V", "Monument at Giza calls her 'King of Upper and Lower Egypt' and mother of Userkaf/Sahure.", True),
        ("egr_d3_6_09_userkaf_usercheres_dyn_v", "Userkaf / Usercheres (Dyn. V Founder)", 8, "c. 2454–2447 BCE (Willockx p.13; Manetho Fr. 18)", "Founder of Dynasty V", "Built the first solar temple at Abusir; Palermo Stone annals era.", False),
        ("egr_d3_6_10_sahure_sephres_dyn_v", "Sahure / Sephres (Dyn. V)", 8, "c. 2447–2435 BCE (Willockx p.13; Manetho)", "2nd Pharaoh of Dynasty V", "Dispatched first attested Egyptian maritime expedition to Punt.", False),
        ("egr_d3_6_11_neferirkare_kakai_dyn_v", "Neferirkare Kakai (Dyn. V)", 8, "c. 2435–2415 BCE (Willockx p.13)", "3rd Pharaoh of Dynasty V", "Honored in the Abusir Papyri.", False),
        ("egr_d3_6_12_shepseskare_dyn_v", "Shepseskare (Dyn. V)", 8, "c. 2415 BCE (Willockx p.13)", "Pharaoh of Dynasty V", "Brief Abusir ruler.", False),
        ("egr_d3_6_13_neferefre_dyn_v", "Neferefre (Dyn. V)", 8, "c. 2410 BCE (Willockx p.13)", "Pharaoh of Dynasty V", "Elder son of Neferirkare.", False),
        ("egr_d3_6_14_nyuserre_ini_dyn_v", "Nyuserre Ini (Dyn. V)", 8, "c. 2400–2375 BCE (Willockx p.14)", "Pharaoh of Dynasty V", "Built solar temple at Abu Gorab.", False),
        ("egr_d3_6_15_menkauhor_dyn_v", "Menkauhor (Dyn. V)", 8, "c. 2375–2367 BCE (Willockx p.14)", "Pharaoh of Dynasty V", "Seventh king of Dynasty V.", False),
        ("egr_d3_6_16_djedkare_isesi_dyn_v", "Djedkare Isesi (Dyn. V)", 8, "c. 2367–2335 BCE (Willockx p.14)", "8th Pharaoh of Dynasty V", "Era of Vizier Ptahhotep's Maxims.", False),
        ("egr_d3_6_17_unas_onnus_dyn_v_pyramid_tex", "Unas / Onnus (Last of Dyn. V — Pyramid Texts!)", 8, "c. 2335–2305 BCE (Willockx p.14; Manetho)", "9th Pharaoh of Dynasty V", "First ruler to carve the sacred Pyramid Texts inside his Saqqara tomb.", True),
        ("egr_d3_6_18_teti_othoes_dyn_vi", "Teti / Othoes (Dyn. VI Founder)", 8, "c. 2305–2285 BCE (Willockx p.15; Manetho Fr. 20)", "Founder of Dynasty VI", "Married Princess Iput daughter of Unas.", False),
        ("egr_d3_6_19_userkare_dyn_vi", "Userkare (Dyn. VI)", 8, "c. 2285 BCE (Willockx p.15)", "Interim King of Dynasty VI", "Brief ruler between Teti and Pepi I.", False),
        ("egr_d3_6_20_pepi_i_phius_dyn_vi", "Pepi I / Phius (Dyn. VI)", 8, "c. 2282–2250 BCE (Willockx p.15; Manetho)", "Son of Teti", "Expanded trade to Byblos & Nubia; father of Merenre I & Pepi II.", False),
        ("egr_d3_6_21_merenre_i_dyn_vi", "Merenre I (Dyn. VI)", 8, "c. 2250–2240 BCE (Willockx p.15)", "Elder Son of Pepi I", "Received Nubian chiefs' homage at Elephantine.", False),
        ("egr_d3_6_22_pepi_ii_phiops_dyn_vi_94_yrs", "Pepi II / Phiops (Dyn. VI — 94-Year Reign!)", 8, "c. 2240–2150 BCE (Manetho Fr. 20; Willockx p.16)", "Longest-Reigning Monarch of Antiquity", "Ascended at age 6 and ruled into his 90s (Manetho: 94 yrs).", True),
        ("egr_d3_6_23_merenre_ii_dyn_vi", "Merenre II Nemtyemsaf (Dyn. VI)", 8, "c. 2150 BCE (Willockx p.16)", "Son of Pepi II", "Brief successor of aged Pepi II.", False),
        ("egr_d3_6_24_queen_nitocris_neith_iqerty_", "Queen Nitocris / Neith-iqerty (Close of Old Kingdom, Dyn. VI)", 8, "c. 2149 BCE (Manetho Fr. 21; Herodotus II.100)", "Last Sovereign of the Old Kingdom", "Described by Manetho as 'the noblest and loveliest of the women of her time' who built the third pyramid tradition.", True),
    ], edge_label="Old Kingdom Succession (Dyn. III–VI)")
    edges.append(E("eg_dyn4_complete", "egr_d3_6_05_djedefre_ratoises_dyn_iv", "direct", "Dynasty IV Giza lineage anchor"))

    # Middle Kingdom & Second Intermediate Period (Dyn. XI–XVII)
    link_seq([
        "eg_dyn7_10_fip",
        ("egr_mk_01_intef_i_dyn_xi", "Intef I (Theban Dyn. XI Founder)", 10, "c. 2130 BCE (Breasted Vol. I §63)", "Founder of Theban Dynasty XI", "First Theban ruler to take a Horus name Sehertawy.", False),
        ("egr_mk_02_intef_ii_dyn_xi", "Intef II Wahankh (Dyn. XI)", 10, "c. 2112–2063 BCE (Breasted Vol. I)", "Brother of Intef I", "Pushed Theban power north to Abydos over 49-year reign.", False),
        ("egr_mk_03_intef_iii_dyn_xi", "Intef III (Dyn. XI)", 10, "c. 2063–2055 BCE (Breasted Vol. I)", "Son of Intef II", "Father of unifier Mentuhotep II.", False),
        "eg_mentuhotep2",
        ("egr_mk_04_mentuhotep_iii_dyn_xi", "Mentuhotep III Sankhkare (Dyn. XI)", 10, "c. 2004–1992 BCE (Breasted Vol. I)", "Son of Mentuhotep II", "Sent Hannu on Red Sea expedition to Punt.", False),
        ("egr_mk_05_mentuhotep_iv_dyn_xi", "Mentuhotep IV Nebtawyre (Last of Dyn. XI)", 10, "c. 1992–1985 BCE (Breasted Vol. I)", "Last Pharaoh of Dynasty XI", "Vizier Amenemhat (future Amenemhat I) led his Wadi Hammamat quarry expedition.", False),
        ("egr_mk_06_amenemhat_i_dyn_xii", "Amenemhat I (Dyn. XII Founder)", 11, "c. 1985–1955 BCE (Manetho Fr. 34; Breasted Vol. I)", "Founder of Dynasty XII", "Founded Itjtawy; father of Senusret I.", False),
        ("egr_mk_07_senusret_i_sesonchosis_dyn_x", "Senusret I / Sesonchosis (Dyn. XII)", 11, "c. 1955–1911 BCE (Manetho Fr. 35; Story of Sinuhe)", "Son of Amenemhat I", "Built White Chapel at Karnak; era of Story of Sinuhe.", True),
        ("egr_mk_08_amenemhat_ii_dyn_xii", "Amenemhat II (Dyn. XII)", 11, "c. 1911–1877 BCE (Manetho Fr. 35)", "Son of Senusret I", "Expanded Near Eastern & Nubian trade.", False),
        ("egr_mk_09_senusret_ii_dyn_xii", "Senusret II (Dyn. XII; Beni Hasan Era)", 11, "c. 1877–1870 BCE (Manetho Fr. 35)", "Son of Amenemhat II", "Faiyum irrigation pioneer; Beni Hasan tomb painting of Semitic caravan of Abishai.", False),
        "eg_senusret3_amenemhat3",
        ("egr_mk_10_amenemhat_iv_dyn_xii", "Amenemhat IV (Dyn. XII)", 11, "c. 1807–1798 BCE (Manetho Fr. 35)", "Son/Co-Regent of Amenemhat III", "Reigned 9 years before sister Sobekneferu.", False),
        ("egr_mk_11_queen_sobekneferu_scemiophri", "Queen Sobekneferu / Scemiophris (First Attested Female Pharaoh, Dyn. XII)", 11, "c. 1798–1794 BCE (Manetho Fr. 35 p.91)", "Last Ruler of Dynasty XII", "Sister of Amenemhat IV; Manetho explicitly notes Scemiophris 'reigned for 4 years' closing the 12th Dynasty.", True),
        ("egr_mk_12_sobekhotep_iv_chenephres_dyn", "Sobekhotep IV / Chenephres (Dyn. XIII; Artapanus's Moses Era)", 12, "c. 1725 BCE (Manetho Fr. 38; Artapanus)", "Greatest King of Dynasty XIII", "Identified in Waddell's Manetho notes with Artapanus's Pharaoh Chenephres.", False),
        ("egr_mk_13_dedumose_tutimaeus_dyn_xiii", "Dedumose / Tutimaeus (Late Dyn. XIII; Manetho Hyksos Entry)", 12, "c. 1660 BCE (Manetho Fr. 42 via Josephus Ag. Ap. I.14)", "Pharaoh Under Whom Hyksos Entered Egypt", "Named by Josephus quoting Manetho as Tutimaeus, when easterners seized Memphis without battle.", False),
        ("egr_mk_14_salitis_hyksos_dyn_xv", "Salitis (1st Great Hyksos King of Avaris, Dyn. XV)", 13, "c. 1650 BCE (Josephus Ag. Ap. I.14)", "Founder of 15th Hyksos Dynasty", "Fortified Avaris in the Eastern Delta.", False),
        ("egr_mk_15_khyan_iannas_hyksos_dyn_xv", "Khyan / Iannas (Great Hyksos King, Dyn. XV)", 13, "c. 1610–1580 BCE (Manetho Fr. 42)", "International Hyksos Sovereign", "Inscribed artifacts found from Knossos to Hattusa and Baghdad.", False),
        ("egr_mk_16_apophis_apepi_hyksos_dyn_xv", "Apophis / Apepi (Hyksos King, Dyn. XV; Traditional Pharaoh of Joseph)", 13, "c. 1580–1545 BCE (Manetho Fr. 42; Syncellus)", "Great Hyksos Adversary of Thebes", "Synchronized by George Syncellus as Pharaoh of Joseph; clashed with Seqenenre Tao.", True),
        "eg_seqenenre",
        ("egr_mk_17_kamose_theban_liberator_dyn_", "Kamose (Last King of Dyn. XVII; Liberator Before Ahmose I)", 14, "c. 1555–1550 BCE (Breasted; Carnarvon Tablet)", "Elder Brother of Ahmose I", "Drove Hyksos back to Avaris; succeeded by younger brother Ahmose I.", False),
        "eg_ahmose1",
    ], edge_label="Middle Kingdom & Hyksos Succession (Dyn. XI–XVII)", edge_type="expansion")

    # New Kingdom Dynasties XVIII–XX (Ahmose I -> ... -> Horemheb/Danaus -> Seti I -> Ramesses II -> Twosret -> Ramesses XI)
    link_seq([
        "eg_ahmose1",
        ("egr_nk_01_amenhotep_i_dyn_xviii", "Amenhotep I (Son of Ahmose I; Deir el-Medina Founder, Dyn. XVIII)", 14, "1525–1504 BCE (Manetho Fr. 50)", "2nd Pharaoh of Dynasty XVIII", "Consolidated Nubia and founded the royal artisans' village.", False),
        "eg_thutmose1",
        ("egr_nk_02_thutmose_ii_dyn_xviii", "Thutmose II (Son of Thutmose I; Husband of Hatshepsut, Dyn. XVIII)", 14, "1492–1479 BCE (Manetho Fr. 50)", "4th Pharaoh of Dynasty XVIII", "Father of Thutmose III.", False),
        ("egr_nk_03_queen_hatshepsut_amessis_dyn", "Queen Hatshepsut / Amessis (Regnant Female Pharaoh, Dyn. XVIII)", 14, "1479–1458 BCE (Manetho Fr. 50; Deir el-Bahari)", "Female Pharaoh of Dynasty XVIII", "Built Deir el-Bahari and dispatched fleet to Punt; co-regent with stepson Thutmose III.", True),
        "eg_thutmose3",
        ("egr_nk_04_amenhotep_ii_dyn_xviii", "Amenhotep II (Son of Thutmose III; Dyn. XVIII)", 14, "1427–1401 BCE (Breasted; Manetho)", "7th Pharaoh of Dynasty XVIII", "Renowned archer-king who campaigned in Canaan.", False),
        ("egr_nk_05_thutmose_iv_dyn_xviii", "Thutmose IV (Dream Stele Pharaoh; Father of Amenhotep III, Dyn. XVIII)", 15, "1401–1391 BCE (Manetho Fr. 50)", "8th Pharaoh of Dynasty XVIII", "Married Mitanni princess and restored Great Sphinx.", False),
        "eg_amenhotep3",
        ("egr_nk_06_queen_tiye_wife_of_amenhotep", "Queen Tiye (Wife of Amenhotep III; Mother of Akhenaten)", 15, "c. 1398–1338 BCE (Amarna Letters)", "Great Royal Wife of Amenhotep III", "Daughter of Yuya & Tjuyu; mother of Akhenaten.", False),
        "eg_akhenaten",
        ("egr_nk_07_queen_nefertiti_amarna_queen", "Queen Nefertiti (Great Royal Wife of Akhenaten)", 15, "c. 1370–1330 BCE (Amarna)", "Queen of Amarna & Mother-in-Law of Tutankhamun", "Bore six princesses incl. Ankhesenamun (wife of Tutankhamun).", True),
        ("egr_nk_08_smenkhkare_dyn_xviii", "Smenkhkare / Neferneferuaten (Amarna Co-Regent, Dyn. XVIII)", 15, "c. 1336–1334 BCE (Amarna)", "Brief Successor of Akhenaten", "Married Meritaten.", False),
        "eg_tutankhamun",
        ("egr_nk_09_pharaoh_ay_dyn_xviii", "Pharaoh Ay (Successor of Tutankhamun, Dyn. XVIII)", 15, "1323–1319 BCE (Manetho)", "Penultimate King of Dynasty XVIII", "Former vizier & God's Father who buried Tutankhamun.", False),
        ("egr_nk_10_horemheb_harmais_danaus_dyn_", "Horemheb / Harmais = Danaus (Manetho Fr. 50/53; Dyn. XVIII)", 15, "1319–1292 BCE (Manetho Fr. 50/53 p.139)", "Final King of Dyn. XVIII Synchronized With Danaus", "Manetho explicitly equates Horemheb ('Harmais') fleeing Egypt to Argos with Greek King Danaus!", True),
        ("egr_nk_11_ramesses_i_dyn_xix", "Ramesses I (Dyn. XIX Founder)", 15, "1292–1290 BCE (Manetho Fr. 55)", "Founder of 19th Ramesside Dynasty", "Vizier Paramesse designated heir by Horemheb.", False),
        ("egr_nk_12_seti_i_sethos_dyn_xix", "Seti I / Sethos (Father of Ramesses II; Manetho's Aegyptus!)", 15, "1290–1279 BCE (Manetho Fr. 53/55; Abydos King List)", "2nd Pharaoh of Dynasty XIX", "Manetho equates Sethos with Aegyptus, brother of Harmais/Danaus; carved the Abydos King List.", True),
        "eg_ramesses2", "eg_merneptah",
        ("egr_nk_13_amenmesse_dyn_xix", "Amenmesse (Dyn. XIX Rival)", 15, "1203–1200 BCE (Budge)", "Theban Counter-King", "Reigned in Upper Egypt during Seti II's early years.", False),
        ("egr_nk_14_seti_ii_dyn_xix", "Seti II (Son of Merneptah; Dyn. XIX)", 15, "1200–1194 BCE (Breasted)", "Son of Merneptah", "Husband of Queen Twosret.", False),
        ("egr_nk_15_siptah_dyn_xix", "Siptah (Dyn. XIX)", 15, "1194–1188 BCE (Budge)", "Young Pharaoh Under Bay & Twosret", "Ruled six years under stepmother Queen Twosret's regency.", False),
        ("egr_nk_16_queen_twosret_thuoris_dyn_xi", "Queen Twosret / Thuoris (Manetho's Trojan War Synchronism, Dyn. XIX)", 15, "1191–1189 BCE (Manetho Fr. 56 p.188)", "Last Ruler of Dynasty XIX", "Manetho states Troy was taken during the reign of Thuoris (identified with Homer's Polybus/Alcandra).", True),
        ("egr_nk_17_setnakhte_dyn_xx", "Setnakhte (Dyn. XX Founder; Father of Ramesses III)", 16, "1189–1186 BCE (Elephantine Stele; Budge Vol. II)", "Founder of Dynasty XX", "Restored order and fathered Ramesses III.", False),
        "eg_ramesses3",
        ("egr_nk_18_ramesses_iv_dyn_xx", "Ramesses IV (Son of Ramesses III; Papyrus Harris I)", 16, "1155–1149 BCE (Budge Vol. II p.9)", "Son of Ramesses III", "Commissioned Great Harris Papyrus.", False),
        ("egr_nk_19_ramesses_v_dyn_xx", "Ramesses V (Son of Ramesses IV)", 16, "1149–1145 BCE (Budge Vol. II p.12)", "Son of Ramesses IV", "Turin Papyrus era.", False),
        ("egr_nk_20_ramesses_vi_dyn_xx", "Ramesses VI (Son of Ramesses III)", 16, "1145–1137 BCE (Budge Vol. II p.13)", "Son of Ramesses III", "Brother of Ramesses IV.", False),
        ("egr_nk_21_ramesses_vii_dyn_xx", "Ramesses VII (Son of Ramesses VI)", 16, "1137–1130 BCE (Budge Vol. II p.14)", "Son of Ramesses VI", "Short Valley of the Kings reign.", False),
        ("egr_nk_22_ramesses_viii_dyn_xx", "Ramesses VIII (Son of Ramesses III)", 16, "1130–1129 BCE (Budge Vol. II p.15)", "Last Surviving Son of Ramesses III", "One-year reign.", False),
        ("egr_nk_23_ramesses_ix_dyn_xx", "Ramesses IX (Dyn. XX)", 16, "1129–1111 BCE (Budge Vol. II p.16)", "Son of Prince Montuherkhepeshef", "18-year reign.", False),
        ("egr_nk_24_ramesses_x_dyn_xx", "Ramesses X (Dyn. XX)", 16, "1111–1107 BCE (Budge Vol. II p.18)", "Penultimate Ramesside", "Predecessor of Ramesses XI.", False),
        ("egr_nk_25_ramesses_xi_dyn_xx", "Ramesses XI (Final Ramesside Pharaoh, Dyn. XX)", 16, "1107–1077 BCE (Budge Vol. II p.19)", "Last Pharaoh of Dynasty XX & New Kingdom", "Saw Rise of High Priest Herihor at Thebes & Smendes at Tanis (Report of Wenamun).", False),
    ], edge_label="New Kingdom Royal Chain (Dyn. XVIII–XX)")
    edges += [
        E("eg_nk_02_thutmose_ii_dyn_xviii" if False else "egr_nk_02_thutmose_ii_dyn_xviii", "egr_nk_03_queen_hatshepsut_amessis_dyn", "direct", "Consorts & royal co-regency"),
        E("egr_nk_06_queen_tiye_wife_of_amenhotep", "eg_akhenaten", "direct", "Mother Queen Tiye -> Akhenaten"),
        E("egr_nk_10_horemheb_harmais_danaus_dyn_", "grk_aegyptus_danaus", "syncretic", "Manetho Fr. 50/53: Harmais/Horemheb = Greek Danaus"),
        E("egr_nk_12_seti_i_sethos_dyn_xix", "grk_aegyptus_danaus", "syncretic", "Manetho Fr. 53: Sethos = Greek Aegyptus"),
        E("egr_nk_16_queen_twosret_thuoris_dyn_xi", "grk_priam_hector", "cognate", "Manetho Fr. 56: Fall of Troy synchronized with Twosret/Thuoris"),
    ]

    # Dynasty XXI Theban Priest-Kings & Tanite Pharaohs -> XXII Libyan Pasenhor -> XXIII–XXX
    link_seq([
        "egr_nk_25_ramesses_xi_dyn_xx",
        ("egr_3ip_01_herihor_theban_priest_king", "Herihor (High Priest of Amun & Ruler at Thebes)", 16, "c. 1080 BCE (Budge Vol. II p.21)", "Founder of Theban Priest-Kings", "Assumed royal titles in Upper Egypt alongside Smendes in the Delta.", False),
        ("egr_3ip_02_piankh_theban_priest_king", "Piankh (High Priest of Amun)", 16, "c. 1074–1070 BCE (Budge Vol. II)", "Theban High Priest", "Father of Pinudjem I.", False),
        ("egr_3ip_03_pinudjem_i_theban_priest_kin", "Pinudjem I (Theban Priest-King)", 16, "c. 1070–1032 BCE (Budge Vol. II)", "High Priest & Father of Psusennes I", "Wed Duathathor-Henuttawy (daughter of Ramesses XI!); father of Psusennes I & Menkheperre.", False),
        ("egr_3ip_04_menkheperre_theban_priest_ki", "Menkheperre (High Priest of Amun)", 16, "c. 1045–992 BCE (Budge Vol. II)", "Son of Pinudjem I", "Fortified Upper Egypt; father of Pinudjem II.", False),
        ("egr_3ip_05_pinudjem_ii_theban_priest_ki", "Pinudjem II (High Priest of Amun; Royal Cache Founder)", 16, "c. 990–969 BCE (Budge Vol. II)", "Son of Menkheperre", "Fathered Psusennes II and preserved the New Kingdom royal mummies in DB320.", False),
    ], edge_label="Theban High Priestly Succession (Dyn. XXI)", edge_type="expansion")

    link_seq([
        "egr_nk_25_ramesses_xi_dyn_xx",
        ("egr_3ip_06_smendes_dyn_xxi", "Smendes I (Dyn. XXI Founder at Tanis)", 16, "1077–1051 BCE (Budge Vol. II p.22)", "Founder of 21st Tanite Dynasty", "Ruled Lower Egypt during Wenamun's mission to Byblos.", False),
        ("egr_3ip_07_psusennes_i_silver_pharaoh_d", "Psusennes I (Silver Pharaoh of Tanis, Dyn. XXI)", 16, "1047–1001 BCE (Budge Vol. II; Montet)", "Son of Pinudjem I; King of Tanis", "Intact silver-coffin royal tomb excavated at Tanis.", True),
        ("egr_3ip_08_amenemope_dyn_xxi", "Amenemope (Dyn. XXI; Contemporary of David)", 16, "1001–992 BCE (Budge Vol. II)", "Son of Psusennes I", "Ruled Tanis during David's monarchy.", False),
        ("egr_3ip_09_siamun_dyn_xxi", "Siamun (Dyn. XXI — Era of King Solomon & Gezer)", 16, "986–967 BCE (Budge Vol. II; 1 Kgs 9:16)", "Pharaoh Who Captured Gezer", "Synchronized with early reign of King Solomon (cf. 1 Kgs 3:1, 9:16).", True),
        ("egr_3ip_10_psusennes_ii_dyn_xxi", "Psusennes II (Last of Dyn. XXI; Father-in-Law of Osorkon I)", 16, "967–943 BCE (Budge Vol. II)", "Last Pharaoh of Dynasty XXI", "Son of Pinudjem II; daughter Maatkare married Osorkon I of Dyn. XXII.", False),
    ], edge_label="Tanite 21st Dynasty Succession")
    edges.append(E("egr_3ip_05_pinudjem_ii_theban_priest_ki", "egr_3ip_10_psusennes_ii_dyn_xxi", "direct", "Pinudjem II -> Psusennes II"))

    link_seq([
        ("egr_3ip_11_buyuwawa_libyan_ancestor_pas", "Buyuwawa the Libyan (6-Gen Ancestor, Serapeum Stele of Pasenhor)", 16, "c. 1100 BCE (Budge Vol. II pp.35–39)", "Progenitor of 22nd Libyan Dynasty", "Founder of the Meshwesh lineage recorded on the Serapeum Stele of Pasenhor.", False),
        "eg_shoshenq1",
        ("egr_3ip_12_osorkon_i_dyn_xxii", "Osorkon I (Son of Shoshenq I & Karamat; Dyn. XXII)", 17, "922–887 BCE (Budge Vol. II p.43)", "Son of Shishak", "Son of Shoshenq I; wed Maatkare (daughter of Psusennes II).", False),
        ("egr_3ip_13_takelot_i_dyn_xxii", "Takelot I (Son of Osorkon I, Dyn. XXII)", 17, "885–872 BCE (Budge Vol. II)", "Son of Osorkon I", "Father of Osorkon II.", False),
        ("egr_3ip_14_osorkon_ii_dyn_xxii", "Osorkon II (Son of Takelot I, Dyn. XXII)", 17, "872–837 BCE (Budge Vol. II p.47)", "Ally of Ahab & Levant Coalition (853 BCE Battle of Qarqar Era)", "Sent Egyptian contingent noted with Ahab in Shalmaneser III's Kurkh Monolith.", False),
        ("egr_3ip_15_shoshenq_ii_dyn_xxii", "Shoshenq II (Silver Falcon Coffin, Tanis, Dyn. XXII)", 17, "c. 887–885 BCE (Budge Vol. II)", "Son of Osorkon I", "Co-regent buried at Tanis.", False),
        ("egr_3ip_16_takelot_ii_dyn_xxii", "Takelot II (Dyn. XXII)", 17, "845–820 BCE (Budge Vol. II)", "Theban-Tanite Ruler", "Chronicle of Prince Osorkon.", False),
        ("egr_3ip_17_shoshenq_iii_dyn_xxii", "Shoshenq III (Dyn. XXII)", 17, "837–798 BCE (Budge Vol. II)", "Son of Takelot II", "39-year reign at Tanis.", False),
        ("egr_3ip_18_pami_dyn_xxii", "Pami (Dyn. XXII)", 17, "785–778 BCE (Budge Vol. II)", "Son of Shoshenq III", "Father of Shoshenq V.", False),
        ("egr_3ip_19_shoshenq_v_dyn_xxii", "Shoshenq V (Dyn. XXII; Pasenhor Stele Erected in Year 37!)", 17, "778–740 BCE (Budge Vol. II p.35)", "Son of Pami", "Priestly Serapeum Stele of Pasenhor dated to his 37th regnal year.", False),
    ], edge_label="Libyan 22nd Dynasty (Pasenhor Stele)")
    edges.append(E("eg_dyn22_libyan_pasenhor", "egr_3ip_11_buyuwawa_libyan_ancestor_pas", "direct", "Stele of Pasenhor ancestor"))
    edges.append(E("egr_3ip_10_psusennes_ii_dyn_xxi", "egr_3ip_12_osorkon_i_dyn_xxii", "direct", "Maatkare bat Psusennes II marries Osorkon I"))

    link_seq([
        "egr_3ip_17_shoshenq_iii_dyn_xxii",
        ("egr_3ip_20_pedubast_i_dyn_xxiii", "Pedubast I (Dyn. XXIII Founder)", 17, "829–804 BCE (Budge Vol. II p.60)", "Founder of 23rd Dynasty", "Rival Theban-Leontopolitan king during Shoshenq III.", False),
        ("egr_3ip_21_osorkon_iii_dyn_xxiii", "Osorkon III (Dyn. XXIII)", 17, "798–769 BCE (Budge Vol. II)", "23rd Dynasty Pharaoh", "Father of Takelot III & Shepenupet I.", False),
        ("egr_3ip_22_tefnakht_i_dyn_xxiv", "Tefnakht I of Sais (Dyn. XXIV Founder vs. Piye)", 17, "732–725 BCE (Budge Vol. II p.68; Victory Stele)", "Chief of Sais & Dynasty XXIV Founder", "Fought Kushite King Piye (Piankhi Stele); father of Bocchoris.", False),
        ("egr_3ip_23_bakenranef_bocchoris_dyn_xxi", "Bakenranef / Bocchoris (Dyn. XXIV Lawgiver)", 17, "725–720 BCE (Manetho Fr. 64; Budge)", "Famed Egyptian Lawgiver King", "Defeated by Kushite Shabaka when uniting Egypt under Dynasty XXV.", False),
        "af_piye",
        ("egr_3ip_24_shabaka_sabacon_dyn_xxv", "Shabaka / Sabacon (Dyn. XXV Pharaoh)", 17, "716–702 BCE (Manetho Fr. 66; Herodotus II.137)", "Kushite Brother of Piye", "Son of Kashta; defeated Bocchoris and unified all Egypt.", False),
        ("egr_3ip_25_shabataka_sebichos_dyn_xxv", "Shabataka / Sebichos (Dyn. XXV Pharaoh)", 17, "702–690 BCE (Manetho Fr. 66; Budge Vol. II)", "Son of Piye", "Dispatched young Prince Taharqa northward to relieve Hezekiah.", False),
        "af_taharqa",
    ], edge_label="Dynasties XXIII–XXV Succession", edge_type="expansion")

    link_seq([
        "af_taharqa",
        ("egr_3ip_26_psamtik_i_dyn_xxvi_54_yrs", "Psamtik I (Dyn. XXVI Reunifier, 54-Year Reign!)", 17, "664–610 BCE (Budge Vol. II p.79; Herodotus II)", "Founder of Saite 26th Dynasty", "Son of Necho I of Sais; unified Egypt & expelled Assyrians; father of Necho II.", True),
        "for_pharaoh_neco",
        ("egr_3ip_27_psamtik_ii_dyn_xxvi", "Psamtik II (Son of Necho II, Dyn. XXVI)", 17, "595–589 BCE (Budge Vol. II p.83)", "Son of Necho II", "Led 593 BCE Napatan expedition.", False),
        ("egr_3ip_28_apries_pharaoh_hophra_dyn_xx", "Apries / Biblical Pharaoh Hophra (Dyn. XXVI, Jer 44:30)", 17, "589–570 BCE (Jeremiah 44:30; Budge Vol. II p.85)", "Son of Psamtik II; Sheltered Prophet Jeremiah", "Marched against Nebuchadnezzar II during 588 BCE siege of Jerusalem (Jer 37:5).", True),
        ("egr_3ip_29_amasis_ii_dyn_xxvi_44_yrs", "Amasis II / Ahmose II (Dyn. XXVI, 44-Year Reign!)", 17, "570–526 BCE (Herodotus II.162; Budge Vol. II p.86)", "Penultimate Saite King", "Promoted Greek Naucratis trade & allied with Croesus of Lydia.", False),
        ("egr_3ip_30_psamtik_iii_dyn_xxvi", "Psamtik III (Last Native Saite King, 525 BCE)", 17, "526–525 BCE (Herodotus III.10; Budge)", "Defeated at Pelusium by Cambyses II", "Fell to Persian conquest in 525 BCE.", False),
        "ir_cambyses2_atossa",
    ], edge_label="Saite 26th Dynasty Succession")

    link_seq([
        "eg_dyn27_31_late_native",
        ("egr_3ip_31_amyrtaeus_dyn_xxviii", "Amyrtaeus of Sais (Sole King of Dyn. XXVIII, 404–399 BCE)", 18, "404–399 BCE (Manetho Fr. 72; Budge Vol. II)", "Liberator From First Persian Rule", "Led native Egyptian revolt freeing Egypt from Darius II.", False),
        ("egr_3ip_32_nepherites_i_dyn_xxix", "Nepherites I (Founder of Mendes Dyn. XXIX, 399–393 BCE)", 18, "399–393 BCE (Manetho Fr. 73; Budge Vol. II)", "Founder of 29th Mendesian Dynasty", "Allied with King Agesilaus II of Sparta against Persia.", False),
        ("egr_3ip_33_hakor_achoris_dyn_xxix", "Hakor / Achoris (Dyn. XXIX, 393–380 BCE)", 18, "393–380 BCE (Manetho Fr. 73; Budge Vol. II)", "29th Dynasty Defender of Egypt", "Repelled Persian invasion with Greek mercenaries.", False),
        ("egr_3ip_34_nectanebo_i_dyn_xxx", "Nectanebo I / Nakhtnebef (Founder of Dyn. XXX, 380–362 BCE)", 18, "380–362 BCE (Manetho Fr. 74; Budge Vol. II)", "Founder of Last Native Dynasty", "Fortified Delta & built Philae/Karnak pylons.", False),
        ("egr_3ip_35_teos_tachos_dyn_xxx", "Teos / Tachos (Dyn. XXX, 362–360 BCE)", 18, "362–360 BCE (Manetho Fr. 74; Budge Vol. II)", "Son of Nectanebo I", "Led joint Greco-Egyptian campaign into Phoenicia.", False),
        ("egr_3ip_36_nectanebo_ii_last_native_pha", "Nectanebo II / Nakhthorheb (LAST Native Pharaoh of Egypt, 360–343 BCE)", 18, "360–343 BCE (Manetho Fr. 74; Budge Vol. II p.104)", "Final Native Egyptian Pharaoh", "Nephew of Teos; deposed by Artaxerxes III in 343 BCE (Alexander Romance calls him Alexander's secret father!).", True),
    ], edge_label="Late Native Dynasties XXVIII–XXX Succession", edge_type="expansion")

    # -------------------------------------------------------------------------
    # 4. COMPLETE PTOLEMAIC FAMILY CHAIN & KUSHITE NAPATA->MEROE CHAIN
    # -------------------------------------------------------------------------
    link_seq([
        "grk_alexander",
        ("egr_ptol_01_ptolemy_i_soter_berenice_i", "Ptolemy I Soter (+ Berenice I, 305–282 BCE)", 18, "305–282 BCE (Budge Vol. II p.111)", "Founder of Ptolemaic Egypt", "General of Alexander; built Alexandria & Library; father of Ptolemy II.", True),
        ("egr_ptol_02_ptolemy_ii_philadelphus_arsi", "Ptolemy II Philadelphus (+ Arsinoe II; Sponsored Septuagint, 282–246 BCE)", 18, "282–246 BCE (Budge Vol. II p.114; Letter of Aristeas)", "Patron of Manetho & Septuagint Torah Translation", "Expanded Library of Alexandria and commissioned High Priest Eleazar's 72 translators.", True),
        ("egr_ptol_03_ptolemy_iii_euergetes_bereni", "Ptolemy III Euergetes (+ Berenice II, 246–222 BCE)", 18, "246–222 BCE (Budge Vol. II p.119)", "Son of Ptolemy II", "Canopus Decree.", False),
        ("egr_ptol_04_ptolemy_iv_philopator_arsino", "Ptolemy IV Philopator (+ Arsinoe III, 222–204 BCE)", 18, "222–204 BCE (Budge Vol. II p.123; 3 Maccabees)", "Son of Ptolemy III", "Victor of Raphia (217 BCE) over Antiochus III.", False),
        ("egr_ptol_05_ptolemy_v_epiphanes_cleopatr", "Ptolemy V Epiphanes (+ Cleopatra I Syra; Rosetta Stone, 204–180 BCE)", 18, "204–180 BCE (Budge Vol. II p.126; Memphis Decree)", "Son of Ptolemy IV", "Issued the trilingual Rosetta Stone (196 BCE) and wed Seleucid Princess Cleopatra I Syra.", True),
        ("egr_ptol_06_ptolemy_vi_philometor_cleopa", "Ptolemy VI Philometor (+ Cleopatra II; Patron of Onias IV, 180–145 BCE)", 18, "180–145 BCE (Budge Vol. II p.129; Josephus Ant. XIII.3)", "Elder Son of Ptolemy V & Cleopatra I Syra", "Granted Leontopolis to Jewish High Priest Onias IV.", False),
        ("egr_ptol_07_ptolemy_viii_euergetes_ii_cl", "Ptolemy VIII Euergetes II Physcon (+ Cleopatra III, 170–116 BCE)", 18, "170–116 BCE (Budge Vol. II p.134)", "Younger Son of Ptolemy V", "Grandfather of Cleopatra VII.", False),
        ("egr_ptol_08_ptolemy_ix_soter_ii", "Ptolemy IX Soter II Lathyros (116–81 BCE)", 18, "116–81 BCE (Budge Vol. II p.138)", "Son of Ptolemy VIII & Cleopatra III", "Father of Ptolemy XII Auletes.", False),
        ("egr_ptol_09_ptolemy_x_alexander_i_bereni", "Ptolemy X Alexander I (+ Berenice III, 107–88 BCE)", 18, "107–88 BCE (Budge Vol. II p.141)", "Brother of Ptolemy IX", "Co-regent & uncle of Ptolemy XII.", False),
        ("egr_ptol_10_ptolemy_xii_auletes", "Ptolemy XII Auletes (Father of Cleopatra VII, 80–51 BCE)", 18, "80–51 BCE (Budge Vol. II p.144)", "Son of Ptolemy IX", "Father of Cleopatra VII, Berenice IV, Arsinoe IV, Ptolemy XIII & Ptolemy XIV.", False),
        "eg_ptolemy_cleopatra",
        ("egr_ptol_12_ptolemy_xv_caesarion_son_of_", "Ptolemy XV Caesarion (Son of Cleopatra VII & Julius Caesar, d. 30 BCE)", 19, "47–30 BCE (Budge Vol. II p.152)", "Last Pharaoh of Ptolemaic Egypt", "Eldest son of Cleopatra VII by Julius Caesar; slain after Actium.", True),
    ], edge_label="Ptolemaic Royal Dynasty (Budge Vol. II)")
    nodes += [
        N("egr_ptol_11_ptolemy_xiii_xiv", "Ptolemy XIII Theos Philopator (Son of Ptolemy XII, d. 47 BCE)", "levant_egypt", 18, "62–47 BCE (Budge Vol. II p.149)", "Co-Regent Brother of Cleopatra VII", ["Budge Vol. II p.149"], "Drowned in the Nile during the Alexandrian War."),
        N("egr_ptol_14", "Ptolemy XIV (Younger Brother of Cleopatra VII, d. 44 BCE)", "levant_egypt", 18, "c. 60–44 BCE (Budge Vol. II p.151)", "Youngest Son of Ptolemy XII", ["Budge Vol. II p.151"], "Nominal co-ruler alongside Cleopatra VII."),
    ]
    edges += [
        E("egr_ptol_06_ptolemy_vi_philometor_cleopa", "bib16_pri_14_high_priest_onias_iv_built_l", "cognate", "Ptolemy VI grants Leontopolis Temple site to Onias IV (Josephus Ant. XIII.3)"),
        E("egr_ptol_10_ptolemy_xii_auletes", "eg_ptolemy_cleopatra", "direct", "Father Ptolemy XII -> Queen Cleopatra VII"),
        E("egr_ptol_10_ptolemy_xii_auletes", "egr_ptol_11_ptolemy_xiii_xiv", "direct", "Father Ptolemy XII -> Ptolemy XIII"),
        E("egr_ptol_10_ptolemy_xii_auletes", "egr_ptol_14", "direct", "Father Ptolemy XII -> Ptolemy XIV"),
        E("grk_julius_augustus", "egr_ptol_12_ptolemy_xv_caesarion_son_of_", "direct", "Father Julius Caesar -> Ptolemy XV Caesarion"),
    ]

    link_seq([
        "af_tantamani",
        ("afr_kush_01_atlanersa_napata", "Atlanersa of Napata (Son of Taharqa / Tantamani Era)", 18, "c. 653–640 BCE (Budge Vol. II p.199)", "Napatan King of Kush", "Buried at Nuri.", False),
        ("afr_kush_02_senkamanisken_napata", "Senkamanisken of Napata", 18, "c. 640–620 BCE (Budge Vol. II p.200)", "Napatan King of Kush", "Father of Anlamani & Aspelta.", False),
        ("afr_kush_03_anlamani_napata", "Anlamani of Napata", 18, "c. 620–600 BCE (Budge Vol. II p.201)", "Son of Senkamanisken", "Crowned at Kawa; elder brother of Aspelta.", False),
        ("afr_kush_04_aspelta_moved_capital_to_mer", "Aspelta (Moved Kushite Capital South to Meroe, c. 593 BCE)", 18, "c. 600–580 BCE (Budge Vol. II p.202)", "Son of Senkamanisken", "Resisted Psamtik II's 593 BCE expedition and transferred center to Meroe.", True),
        ("afr_kush_05_harsiotef_napata", "Harsiotef of Kush", 18, "c. 404–369 BCE (Budge Vol. II p.204)", "Napatan-Meroitic Sovereign", "Stele of 35 regnal years.", False),
        ("afr_kush_06_nastasen_napata", "Nastasen of Kush (Last Great Napatan Tomb at Nuri)", 18, "c. 335–315 BCE (Budge Vol. II p.205)", "Successor of Harsiotef", "Defended Nubia against Khababash era forces.", False),
        ("afr_kush_07_arqamani_ergamenes_meroe", "Arqamani / King Ergamenes of Meroe (Friend of Ptolemy II & IV)", 19, "c. 270–220 BCE (Diodorus III.6; Budge Vol. II)", "Builder of Dakka Temple", "Greek-educated Meroitic king mentioned by Diodorus Siculus.", True),
        ("afr_kush_08_king_natakamani_meroe", "King Natakamani of Meroe (Husband of Kandake Amanitore)", 19, "c. 1–20 CE (Budge Vol. II p.213)", "Meroitic Sovereign (Naqa / Gebel Barkal)", "Co-ruler with Kandake Queen Amanitore during Meroe's architectural zenith.", True),
        ("afr_kush_09_queen_amanitore_kandake_of_m", "Queen Amanitore (Kandake / Biblical 'Candace' Era)", 19, "c. 1–20 CE (Budge Vol. II p.214; Acts 8:27)", "Kandake Co-Regent of Meroe", "Built Lion Temple at Naqa & restored Amun temple at Meroe; maternal figure of Acts 8:27 'Candace' dynasty.", True),
        ("afr_kush_10_prince_arikhankharer_meroe", "Crown Prince Arikhankharer (Son of Natakamani & Amanitore)", 19, "1st c. CE (Budge Vol. II p.214)", "Prince of Meroe", "Depicted with Natakamani & Amanitore at Naqa.", False),
        ("afr_kush_11_prince_shorkaror_meroe", "King Shorkaror (Son of Natakamani & Amanitore)", 19, "c. 20–30 CE (Budge Vol. II p.214)", "Successor of Natakamani & Amanitore", "Inscribed victory relief at Jebel Qeili.", False),
    ], tradition="african", sources=["Budge Book of the Kings of Egypt Vol. II (pp.195–214)"], edge_label="Napatan–Meroitic Succession")
    edges.append(E("afr_kush_08_king_natakamani_meroe", "afr_kush_09_queen_amanitore_kandake_of_m", "direct", "Co-regency of Natakamani & Kandake Amanitore"))
    edges.append(E("afr_kush_09_queen_amanitore_kandake_of_m", "afr_kush_10_prince_arikhankharer_meroe", "direct", "Mother Amanitore -> Arikhankharer"))
    edges.append(E("afr_kush_09_queen_amanitore_kandake_of_m", "afr_kush_11_prince_shorkaror_meroe", "direct", "Mother Amanitore -> Shorkaror"))

    return {
        "module": "18_egypt_31_dynasties_manetho_budge",
        "title": "Person-by-Person 31 Dynasties of Egypt (Manetho, Palermo Stone, Willockx, Budge) + Complete Ptolemies & Kushite Kings",
        "nodes": nodes,
        "edges": edges,
    }
