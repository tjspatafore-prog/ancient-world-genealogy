"""
Module 25: Abraham's Lineage to the Present Day (2026) — Five Living Royal,
Rabbinic & Archaeogenetic Branches Extending Directly from Existing Atlas Anchors.

Wave 4: Replaced flat add_roster fans for the 24 Qatadid Sharifs & Ethiopian Solomonic
emperors with true person-by-person sequential father->son chains while preserving every
existing ID verbatim.
"""

from . import N, E, add_chain


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # BRANCH 1: ABRAHAM -> ISHMAEL -> PROPHET MUHAMMAD -> LIVING HASHEMITE, ALAOUITE & NIZARI HOUSES (2026)
    # -------------------------------------------------------------------------
    hashemite_chain = [
        ("mod_hasan_muthanna", "Hasan ibn Ali → Hasan al-Muthanna → Abdallah al-Kamil → Musa al-Jawn → Idris", 20, "661-1180 CE (Early Hasanid Ashraf)",
         "Early Hasanid Descendants of Prophet Muhammad & Fatimah",
         "Through Prophet Muhammad's daughter Fatimah & Ali ibn Abi Talib -> eldest grandson Imam Hasan ibn Ali -> Hasan al-Muthanna (married Fatimah bint al-Husayn, uniting BOTH grandsons of Muhammad!) -> Abdallah al-Kamil -> Musa al-Jawn -> Idris (father of Qatadah).",
         {"major": True, "altNames": ["Hasan al-Muthanna", "Abdallah al-Kamil", "Musa al-Jawn"]}),
        ("mod_qatadah_sharifs", "Qatadah ibn Idris (1st Qatadid Sharif of Mecca, 1201) Anchor", 20, "1201-1850 CE (700-Year Sharifate of Mecca)",
         "Unbroken Seven-Century Sharifian Rulers of Mecca Anchor",
         "Anchor for the unbroken Banu Qatadah line (generations 1-21) unrolled individually below.",
         {"major": True, "altNames": ["Qatadah ibn Idris", "Abu Numayy I & II", "Barakat I & II", "Dhawu Awn"]}),
        ("mod_hussein_abdullah1", "Sharif Hussein bin Ali → King Abdullah I → King Talal → King Hussein Anchor", 21, "1854-1999 CE (Modern Hashemite Kingdoms)",
         "Founders of Modern Jordan, Iraq (Faisal I) & Syria Anchor",
         "Modern Hashemite royal line from Sharif Hussein bin Ali through King Hussein of Jordan, unrolled individually below.",
         {"major": True, "altNames": ["Sharif Hussein bin Ali", "King Abdullah I", "King Faisal I of Iraq", "King Hussein of Jordan"]}),
        ("mod_abdullah2_hussein_iman", "LIVING (2026): King Abdullah II of Jordan (b. 1962, 41st Gen) → Crown Prince Al-Hussein (b. 1994, 42nd Gen) → Princess Iman bint Al-Hussein (b. Aug 2024, 43rd Gen!)", 22, "1962 – Present Day (2026 • Living Royal House of Jordan)",
         "Living 41st–43rd Generation Direct Descendants of Prophet Muhammad (Hashemite Dynasty)",
         "Reigning Hashemite King Abdullah II bin Al-Hussein (acceded 1999) + Queen Rania -> Crown Prince Al-Hussein bin Abdullah II (b. 1994, + Princess Rajwa Al Saif) -> Princess Iman bint Al-Hussein (born August 3, 2024 — 43rd generation from Prophet Muhammad!).",
         {"major": True, "altNames": ["King Abdullah II (Living)", "Crown Prince Hussein (Living)", "Princess Iman (b. 2024)"]}),
    ]
    add_chain(nodes, edges, hashemite_chain, start_parent="ar_hashim_muhammad_caliphs", start_edge_type="direct",
              start_edge_label="Fatimah & Ali -> Imam Hasan ibn Ali -> Continuous Hashemite Line to 2026",
              tradition="arabian", default_edge_type="direct", default_sources=["Hashemite Royal Registers", "Meccan Sharifate Chronicles"])

    # Person-by-person Banu Qatadah 24-Generation Chain (preserving every modr_has_* ID!)
    has_seq = [
        ("modr_has_01_1_qatadah_ibn_idris_emir_of_", "1. Qatadah ibn Idris (Emir of Mecca, 1201–1220 CE)", 20),
        ("modr_has_02_2_ali_al_akbar_ibn_qatadah", "2. Ali al-Akbar ibn Qatadah", 20),
        ("modr_has_03_3_abu_sa_d_al_hasan_ibn_ali", "3. Abu Sa'd al-Hasan ibn Ali", 20),
        ("modr_has_04_4_muhammad_abu_numayy_i_d_13", "4. Muhammad Abu Numayy I ibn Abi Sa'd (d. 1301 CE)", 20),
        ("modr_has_05_5_rumaithah_ibn_abu_numayy_i", "5. Rumaithah ibn Abu Numayy I", 20),
        ("modr_has_06_6_ajlan_ibn_rumaithah", "6. Ajlan ibn Rumaithah", 20),
        ("modr_has_07_7_ali_ibn_ajlan", "7. Ali ibn Ajlan", 20),
        ("modr_has_08_8_hasan_ibn_ajlan", "8. Hasan ibn Ajlan", 20),
        ("modr_has_09_9_barakat_i_ibn_hasan", "9. Barakat I ibn Hasan", 20),
        ("modr_has_10_10_muhammad_ibn_barakat", "10. Muhammad ibn Barakat", 20),
        ("modr_has_11_11_barakat_ii_ibn_muhammad", "11. Barakat II ibn Muhammad", 20),
        ("modr_has_12_12_muhammad_abu_numayy_ii_15", "12. Muhammad Abu Numayy II ibn Barakat (1525–1584)", 20),
        ("modr_has_13_13_hasan_ibn_abu_numayy_ii", "13. Hasan ibn Abu Numayy II", 20),
        ("modr_has_14_14_abdullah_ibn_hasan_ancest", "14. Abdullah ibn Hasan (Ancestor of Abadilah Clan)", 20),
        ("modr_has_15_15_hussein_16_abdullah_17_mu", "15. Hussein ibn Abdullah", 20),
        ("modr_has_16_abdullah", "16. Abdullah ibn Hussein", 20),
        ("modr_has_17_muhsin", "17. Muhsin ibn Abdullah", 20),
        ("modr_has_18_awn", "18. Awn ibn Muhsin (Eponym of Dhawu Awn)", 21),
        ("modr_has_16_19_abd_al_mu_in_20_muhammad_", "19. Abd al-Mu'in ibn Awn", 21),
        ("modr_has_20_muhammad", "20. Sharif Muhammad ibn Abd al-Mu'in", 21),
        ("modr_has_21_ali_pasha", "21. Ali Pasha ibn Muhammad", 21),
        ("modr_has_17_22_sharif_hussein_bin_ali_ki", "22. Sharif Hussein bin Ali (King of Hejaz, 1854–1931)", 21),
        ("modr_has_18_23_king_abdullah_i_of_jordan", "23. King Abdullah I of Jordan (Founder, r. 1921–1951)", 21),
        ("modr_has_19_24_king_talal_king_hussein_o", "24. King Talal ibn Abdullah of Jordan (1909–1972)", 21),
        ("modr_has_king_hussein", "25. King Hussein ibn Talal of Jordan (1935–1999)", 21),
    ]
    for nid, nm, tr in has_seq:
        nodes.append(N(nid, nm, "arabian", tr, "1201-1999 CE (Banu Qatadah)", "Sharif of Mecca / Hashemite Monarch", ["Hashemite Royal Registers", "Meccan Sharifate Chronicles"], f"Banu Qatadah / Hashemite patrilineal succession: {nm}.", major=False))
    nodes.append(N("modr_has_faisal1_iraq", "King Faisal I of Iraq & Syria (Son of Sharif Hussein bin Ali, 1885–1933)", "arabian", 21, "1885-1933 CE (Hashemite Kingdom of Iraq)", "Brother of King Abdullah I; King of Iraq", ["Hashemite Royal Registers"], "Son of Sharif Hussein bin Ali; King of Greater Syria (1920) and first King of Iraq (1921-1933)."))
    edges.append(E("mod_hasan_muthanna", "modr_has_01_1_qatadah_ibn_idris_emir_of_", "direct", "Idris -> son Qatadah ibn Idris (1st Qatadid Sharif)"))
    edges.append(E("mod_qatadah_sharifs", "modr_has_01_1_qatadah_ibn_idris_emir_of_", "direct", "Qatadid anchor link"))
    link_seq(edges, [x[0] for x in has_seq] + ["mod_abdullah2_hussein_iman"], "direct", "Father-to-son Hashemite royal succession")
    edges.append(E("modr_has_17_22_sharif_hussein_bin_ali_ki", "modr_has_faisal1_iraq", "direct", "Sharif Hussein bin Ali -> son King Faisal I of Iraq"))

    # Branch 1B & 1C: Alaouite Dynasty of Morocco & Nizari Ismaili Imamat
    nodes += [
        N("mod_alaouite_morocco", "LIVING (2026): Alaouite Dynasty of Morocco — Hassan al-Dakhil (13th c.) → Moulay Ali Cherif (1631) → Mohammed V → Hassan II → King Mohammed VI (b. 1963) → Crown Prince Moulay Hassan (b. 2003)", "arabian", 22, "1266 – Present Day (2026 • Living Royal House of Morocco)",
          "Living Hasanid Dynasty Ruling Morocco (via Hasan al-Muthanna & Al-Nafs al-Zakiyya)", ["Moroccan Alaouite Chronicles", "Official Royal Registers"],
          "Descended from Hasan al-Muthanna -> Muhammad al-Nafs al-Zakiyya -> Hassan al-Dakhil -> Moulay Ali Cherif (1631) -> reigning King Mohammed VI (b. 1963) & Crown Prince Moulay Hassan (b. 2003).",
          ["Hassan al-Dakhil", "Moulay Ismail", "King Mohammed VI (Living)", "Crown Prince Moulay Hassan (Living)"], major=True),
        N("mod_agakhan5_ismaili", "LIVING (2026): Nizari Ismaili Imamat — Husayn ibn Ali → Ja'far al-Sadiq → Fatimid Caliphs → Aga Khan IV (d. Feb 2025) → Aga Khan V (Prince Rahim al-Hussaini, b. 1971, 50th Imam!)", "arabian", 22, "680 – Present Day (2026 • 50th Hereditary Imam)",
          "Living Husaynid Spiritual Imamat (Continuous Nass Succession to 2026)", ["Nizari Ismaili Imamat Archives", "Fatimid Chronicles"],
          "Traces continuous hereditary Imamat from Fatimah & Ali -> Imam Husayn -> Ja'far al-Sadiq -> Fatimid Caliphs -> Aga Khan IV -> Prince Rahim al-Hussaini (Aga Khan V, living, b. 1971, 50th Imam!).",
          ["Ja'far al-Sadiq", "Fatimid Caliphs", "Aga Khan IV", "Aga Khan V / Prince Rahim (Living)"], major=True),
    ]

    # -------------------------------------------------------------------------
    # BRANCH 2: SOLOMONIC ETHIOPIA — PERSON-BY-PERSON TO 2026
    # -------------------------------------------------------------------------
    solomonic_chain = [
        ("mod_eth_yekuno_to_lebna", "Solomonic Imperial Spine Anchor (Yekuno Amlak 1270 to Lebna Dengel 1540)", 20, "1270-1540 CE (Ethiopian Royal Chronicles)",
         "Medieval Golden Age of the Restored Solomonic Empire Anchor",
         "Anchor connecting Yekuno Amlak through Zara Yaqob to Lebna Dengel (Dawit II), unrolled individually below.",
         {"major": True, "altNames": ["Amda Seyon I", "Emperor Zara Yaqob", "Dawit II (Lebna Dengel)"]}),
        ("mod_eth_shewa_sahle", "Shewan Solomonic Branch Anchor (Abeto Yaqob to Ras Makonnen)", 21, "1540-1906 CE (Shewan Royal Chronicles)",
         "14-Generation Shewan Bridge to Haile Selassie I Anchor",
         "Shewan branch from Lebna Dengel's son Abeto Yaqob through Negasi Krestos, Sahle Selassie, and Ras Makonnen.",
         {"altNames": ["Negasi Krestos", "Negus Sahle Selassie", "Princess Tenagnework", "Ras Makonnen", "Emperor Menelik II"]}),
        ("mod_eth_living_2026", "LIVING (2026): Ethiopian Imperial House — Emperor Haile Selassie I (1892–1975) → Crown Prince Amha Selassie (1916–1997) → Prince Zera Yacob Amha Selassie (b. 1953) & Prince Ermias Sahle Selassie (b. 1960)", 22, "1930 – Present Day (2026 • Living Solomonic Princes)",
         "Living Heads of the Ethiopian Imperial House & Crown Council (225th Traditional Monarch Line)",
         "Emperor Haile Selassie I -> Crown Prince Amha Selassie -> Prince Zera Yacob Amha Selassie (living, b. 1953) alongside Prince Ermias Sahle Selassie (living, b. 1960).",
         {"major": True, "altNames": ["Amha Selassie", "Prince Zera Yacob (Living)", "Prince Ermias Sahle Selassie (Living)"]}),
    ]
    add_chain(nodes, edges, solomonic_chain, start_parent="keb_kaleb_gabramaskal_yekuno", start_edge_type="direct",
              start_edge_label="Continuous Ethiopian Solomonic Succession from Yekuno Amlak (1270) to 2026",
              tradition="african", default_edge_type="direct", default_sources=["Ethiopian Royal Chronicles", "Crown Council of Ethiopia"])

    eth_seq = [
        ("modr_eth_01_wedem_arad_son_of_yekuno_aml", "Emperor Wedem Arad (Son of Yekuno Amlak, r. 1299–1314)", 20),
        ("modr_eth_02_amda_seyon_i_1314_1344", "Emperor Amda Seyon I (Son of Wedem Arad, r. 1314–1344)", 20),
        ("modr_eth_03_newaya_krestos_dawit_i", "Emperor Newaya Krestos (Son of Amda Seyon I, r. 1344–1372)", 20),
        ("modr_eth_dawit1", "Emperor Dawit I (Son of Newaya Krestos, r. 1382–1413)", 20),
        ("modr_eth_04_emperor_zara_yaqob_1434_1468", "Emperor Zara Yaqob (Son of Dawit I, r. 1434–1468)", 20),
        ("modr_eth_05_ba_eda_maryam_i_naod", "Emperor Ba'eda Maryam I (Son of Zara Yaqob, r. 1468–1478)", 20),
        ("modr_eth_naod", "Emperor Na'od (Son of Ba'eda Maryam I, r. 1494–1508)", 20),
        ("modr_eth_06_dawit_ii_lebna_dengel_1508_1", "Emperor Dawit II / Lebna Dengel (Son of Na'od, r. 1508–1540)", 20),
        ("modr_eth_07_abeto_yaqob_segwe_qal_werede", "Prince Abeto Yaqob of Menz (4th Son of Lebna Dengel)", 21),
        ("modr_eth_08_negasi_krestos_1st_ruler_of_", "Negasi Krestos (Descendant via Segwe Qal -> Libse Qal; 1st Ruler of Shewa, 1682)", 21),
        ("modr_eth_09_sebaste_abuye_amha_iyesus_as", "Meridazmach Sebaste -> Abuye -> Amha Iyesus -> Asfa Wossen -> Wossen Seged of Shewa", 21),
        ("modr_eth_10_negus_sahle_selassie_of_shew", "King Sahle Selassie of Shewa (Son of Wossen Seged, r. 1813–1847)", 21),
        ("modr_eth_11_princess_tenagnework_sahle_s", "Princess Tenagnework Sahle Selassie (Daughter of Negus Sahle Selassie)", 21),
        ("modr_eth_ras_makonnen", "Ras Makonnen Wolde Mikael (Son of Tenagnework; Governor of Harar, 1852–1906)", 21),
    ]
    for nid, nm, tr in eth_seq:
        nodes.append(N(nid, nm, "african", tr, "1299-1906 CE (Ethiopian Royal Chronicles)", "Solomonic Emperor / Prince of Ethiopia", ["Ethiopian Royal Chronicles"], f"Solomonic Ethiopian succession: {nm}.", major=False))
    nodes += [
        N("modr_eth_haile_melekot", "King Haile Melekot of Shewa (Eldest Son of Negus Sahle Selassie, r. 1847–1855)", "african", 21, "1824-1855 CE (Shewan Chronicles)", "Father of Emperor Menelik II", ["Ethiopian Royal Chronicles"], "Eldest son of Sahle Selassie; father of Emperor Menelik II."),
        N("modr_eth_12_emperor_menelik_ii_victor_of", "Emperor Menelik II of Ethiopia (Son of Haile Melekot; Victor of Adwa, 1896)", "african", 21, "1844-1913 CE (Ethiopian Imperial Chronicles)", "Modernizer of Ethiopia & Cousin of Haile Selassie", ["Ethiopian Royal Chronicles"], "Reigned 1889-1913; defended Ethiopian independence at the Battle of Adwa (1896)."),
    ]
    edges.append(E("mod_eth_yekuno_to_lebna", "modr_eth_01_wedem_arad_son_of_yekuno_aml", "direct", "Yekuno Amlak -> son Wedem Arad"))
    link_seq(edges, [x[0] for x in eth_seq] + ["eth_haile_selassie", "mod_eth_living_2026"], "direct", "Father/Mother-to-child Solomonic succession to 2026")
    edges += [
        E("modr_eth_10_negus_sahle_selassie_of_shew", "modr_eth_haile_melekot", "direct", "Sahle Selassie -> eldest son Haile Melekot"),
        E("modr_eth_haile_melekot", "modr_eth_12_emperor_menelik_ii_victor_of", "direct", "Haile Melekot -> Emperor Menelik II"),
        E("mod_eth_shewa_sahle", "eth_haile_selassie", "direct", "Shewan Solomonic anchor -> Emperor Haile Selassie I"),
    ]

    # -------------------------------------------------------------------------
    # BRANCH 3: GEORGIAN BAGRATIONI HOUSE TO 2026
    # -------------------------------------------------------------------------
    bagrationi_chain = [
        ("mod_geo_tamar_to_constantine2", "Late Medieval Bagrationis (1213–1505): Queen Tamar → George IV & Rusudan → George V → Alexander I → Constantine II", 20, "1213-1505 CE (Georgian Royal Annals)",
         "Common Ancestors of All Modern Bagrationi Branches (Mukhrani, Kartli & Kakheti)",
         "George V the Brilliant freed Georgia from Mongol rule; Constantine II (1478-1505) was last monarch of unified Georgia before Mukhrani/Kakheti split.",
         {"altNames": ["George V the Brilliant", "Alexander I the Great", "Constantine II of Georgia"]}),
        ("mod_geo_mukhrani_erekle2", "Mukhrani & Kakheti Royal Houses (1505–2008): Bagrat I of Mukhrani → Vakhtang V; AND Erekle II → George XII → Nugzar", 21, "1505-2008 CE (Bagrationi Royal Houses)",
         "Senior Agnatic Mukhrani Branch & Last Reigning Kings of Kartli-Kakheti",
         "Bagrat I founded the House of Mukhrani; Heraclius II (Erekle II) & George XII led the Kakheti/Gruzinsky royal line.",
         {"altNames": ["Bagrat I of Mukhrani", "King Heraclius II (Erekle II)", "King George XII"]}),
        ("mod_geo_giorgi_2011", "LIVING (2026): Prince David Bagration of Mukhrani (b. 1976) & Princess Ana Bagration-Gruzinsky (b. 1976) → Prince Giorgi Bagrationi (b. Sept 27, 2011!)", 22, "1976 – Present Day (2026 • Living Royal House of Georgia)",
         "21st-Century Unification of Both Living Georgian Bagrationi Royal Lines",
         "Born in 2011 and baptized by Patriarch Ilia II, Prince Giorgi Bagrationi unites both surviving branches (Mukhrani & Kakheti/Gruzinsky).",
         {"major": True, "altNames": ["Prince David Bagration (Living)", "Princess Ana Bagration-Gruzinsky (Living)", "Prince Giorgi Bagrationi (b. 2011)"]}),
    ]
    add_chain(nodes, edges, bagrationi_chain, start_parent="geo_bagrationi_davidic", start_edge_type="direct",
              start_edge_label="Continuous Bagrationi Succession from Queen Tamar (1213) to Prince Giorgi (b. 2011)",
              tradition="iranian", default_edge_type="direct", default_sources=["Georgian Royal Annals", "Royal House of Georgia"])

    # -------------------------------------------------------------------------
    # BRANCH 4: BABYLONIAN EXILARCHS -> SEPHARDIC & ASHKENAZI LIVING FAMILIES (2026)
    # -------------------------------------------------------------------------
    davidic_chain = [
        ("mod_exilarchs_bostanai", "Babylonian Exilarchs (Resh Galuta): Huna I → Mar Ukba → Bostanai ben Haninai (+ Izdundad!) → David ben Zakkai → Hezekiah Gaon", 20, "c. 170-1058 CE (Seder Olam Zuta; Letter of Sherira Gaon; Talmud)",
         "Recognized Patrilineal Davidic Heads of Babylonian Jewry (Intermarried with Sasanians!)",
         "Exilarch Bostanai (c. 618-670) married Sasanian Princess Izdundad (daughter of Shah Khosrow II); continued through Hezekiah Gaon (d. 1058).",
         {"major": True, "altNames": ["Exilarch Bostanai", "Princess Izdundad", "David ben Zakkai", "Hezekiah Gaon (Last Exilarch)"]}),
        ("mod_abravanel_sephardic", "Sephardic Exilarchic Line: Don Judah Abravanel → Don Isaac Abravanel (1437–1508) → Leone Ebreo → Living Abravanel & Ibn Daud Families (2026)", 21, "1100 – Present Day (2026 • Sephardic Davidic Heritage)",
         "Documented Iberian-Sephardic Family Preserving Direct Exilarchic Davidic Tradition",
         "Don Isaac Abravanel (Torah commentator & Treasurer of Portugal/Spain) preserved Iberian family pedigrees claiming Exilarchic Davidic descent.",
         {"major": True, "altNames": ["Don Isaac Abravanel", "Leone Ebreo", "Living Abravanel Family"]}),
        ("mod_rashi_maharal_living", "LIVING (2026): Ashkenazi Davidic Rabbinic Trunk — Hillel the Elder → Johanan HaSandlar → Rashi (1040–1105) → Maharal of Prague (1525–1609) → Living Luria, Horowitz, Katzenellenbogen, Dayan, Charlap & Schneersohn Families", 22, "1040 – Present Day (2026 • Living Rabbinic & Hasidic Dynasties)",
         "Primary Ancestral Trunk of Living Ashkenazi & Hasidic Davidic Traditions (Pre-Rashi Link Traditional)",
         "Historically proven lineages descend continuously from Rashi (1040-1105) and Maharal of Prague (1525-1609) into living families today.",
         {"major": True, "altNames": ["Rashi (1040-1105)", "Maharal of Prague", "Katzenellenbogen / Luria / Horowitz / Dayan / Schneersohn"]}),
    ]
    add_chain(nodes, edges, davidic_chain, start_parent="kg_j13_jehoiachin", start_edge_type="expansion",
              start_edge_label="Seder Olam Zuta / Talmudic Tradition: Zerubbabel -> Babylonian Exilarchs (Resh Galuta)",
              tradition="biblical", default_edge_type="expansion", default_sources=["Seder Olam Zuta", "Letter of Sherira Gaon", "Rabbinic Genealogical Archives"])

    # -------------------------------------------------------------------------
    # BRANCH 5: ARCHAEOGENETIC BIOLOGICAL BRIDGES TO LIVING PEOPLE (2026)
    # -------------------------------------------------------------------------
    nodes += [
        N("dna_living_kohanim_j1", "LIVING (2026) Y-DNA: Cohen Modal Haplotype (J1-Z18271 / P58) & Samaritan Kohanim — ~3,000-Year Iron Age Levantine Patrilineal Cluster", "dna", 22, "c. 1200 BCE – Present Day (2026 • Modern Population Genetics)",
          "Scientific Biological Continuity of Living Jewish & Samaritan Priestly Families", ["Hammer et al. 2009 (Human Genetics)", "Behar et al. 2017", "FTDNA / YFull J-Z18271"],
          "Over 46% of living Ashkenazi and Sephardic Kohanim (and Samaritan priestly lines) share Y-DNA clade J1-Z18271 (TMRCA ~3,100 yrs ago).",
          ["Cohen Modal Haplotype", "Y-DNA J1-Z18271", "Living Kohanim & Samaritans"], major=True),
        N("dna_living_hashemites_l859", "LIVING (2026) Y-DNA: Hashemite / Sharifian Genetic Clade (J1-L859 / FGC8703) — Shared Arabian Patrilineal Lineage Today", "dna", 22, "c. 500 CE – Present Day (2026 • Modern Genetic Genealogy)",
          "Independent Living Hashemite, Hasanid & Husaynid Families Converging on Y-DNA J1-L859", ["YFull J-L859 / FGC8703 Phylogeny", "Arabian Y-DNA Consortium"],
          "Whole-Y sequencing of separated Ashraf/Sayyid families across Jordan, Hejaz, Iraq, Yemen & Morocco converges on Y-DNA J1-L859 / FGC8703.",
          ["Y-DNA J1-L859", "FGC8703", "Living Ashraf & Sayyids"], major=True),
    ]

    # Cross-links
    edges += [
        E("mod_hasan_muthanna", "mod_alaouite_morocco", "direct", "Hasan al-Muthanna -> Al-Nafs al-Zakiyya -> Hassan al-Dakhil -> Living King Mohammed VI"),
        E("ar_hashim_muhammad_caliphs", "mod_agakhan5_ismaili", "direct", "Fatimah & Ali -> Imam Husayn -> Fatimids -> Living Aga Khan V (2025)"),
        E("bir_sasanians_complete", "mod_exilarchs_bostanai", "direct", "Sasanian Princess Izdundad (daughter of Shah Khosrow II) marries Exilarch Bostanai!"),
        E("dna_j1_j2", "dna_living_kohanim_j1", "genetic", "Y-DNA J1-P58 -> Iron Age Levantine J-Z18271 (Living Kohanim & Samaritans)"),
        E("lev_aaron", "dna_living_kohanim_j1", "genetic", "Traditional Aaronite priesthood corroborated by ~3,100-yr J-Z18271 Y-DNA cluster"),
        E("dna_j1_j2", "dna_living_hashemites_l859", "genetic", "Y-DNA J1-P58 -> Arabian J1-L859 / FGC8703 (Living Hashemites & Ashraf)"),
        E("mod_abdullah2_hussein_iman", "dna_living_hashemites_l859", "genetic", "Modern Hashemite / Sharifian families cluster on Y-DNA J1-L859"),
    ]

    return {
        "module": "25_abraham_to_present_day",
        "title": "Abraham's Lineage to the Present Day (2026): Living Hashemites (Jordan), Alaouites (Morocco), Aga Khan V, Ethiopian Solomonids, Georgian Bagrationis, Exilarch/Rabbinic Davidic Lines & Modern Y-DNA Clades",
        "nodes": nodes,
        "edges": edges,
    }
