"""
Module 25: Abraham's Lineage to the Present Day (2026) — Five Living Royal,
Rabbinic & Archaeogenetic Branches Extending Directly from Existing Atlas Anchors.

Strict Provenance Separation Preserved:
- Contemporaneously documented medieval-to-2026 successions are tagged 'direct'.
- Ancient-to-medieval chronicle bridges (e.g., Adnan -> Ishmael, Kebra Nagast Aksum -> Solomon,
  Babylonian Exilarchs -> Zerubbabel, Rashi/Maharal -> King David) are transparently tagged
  'expansion' or 'syncretic' (noting the scholarly 'Descent from Antiquity' boundary!).
- Modern living biological Y-DNA clusters (Kohanim J1-Z18271 & Hashemites J1-L859) are tagged 'genetic'.
"""

from . import N, E, add_chain, add_roster


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
        ("mod_qatadah_sharifs", "Qatadah ibn Idris (1st Qatadid Sharif of Mecca, 1201) → Abu Numayy I → Barakat I & II → Abu Numayy II → Dhawu Awn Clan", 20, "1201-1850 CE (700-Year Sharifate of Mecca)",
         "Unbroken Seven-Century Sharifian Rulers of Mecca (Banu Qatadah)",
         "Contemporaneously documented patrilineal sequence from Qatadah ibn Idris (Emir of Mecca, 1201-1220) through Ali al-Akbar, Abu Sa'd al-Hasan, Abu Numayy I, Rumaithah, Ajlan, Ali, Hasan, Barakat I, Muhammad, Barakat II, Abu Numayy II, Hasan, Abdullah, Hussein, Abdullah, Muhammad, Awn, Abd al-Mu'in, Muhammad & Ali Pasha!",
         {"major": True, "altNames": ["Qatadah ibn Idris", "Abu Numayy I & II", "Barakat I & II", "Dhawu Awn"]}),
        ("mod_hussein_abdullah1", "Sharif Hussein bin Ali (King of Hejaz, 1854–1931) → King Abdullah I → King Talal → King Hussein of Jordan (1935–1999)", 21, "1854-1999 CE (Modern Hashemite Kingdoms)",
         "Founders of Modern Jordan, Iraq (Faisal I) & Syria",
         "Sharif Hussein bin Ali led the Great Arab Revolt (1916); his sons Faisal I (King of Iraq) and Abdullah I (Founder of Jordan, r. 1921-1951) established modern Hashemite monarchies -> King Talal -> King Hussein bin Talal (r. 1952-1999).",
         {"major": True, "altNames": ["Sharif Hussein bin Ali", "King Abdullah I", "King Faisal I of Iraq", "King Hussein of Jordan"]}),
        ("mod_abdullah2_hussein_iman", "LIVING (2026): King Abdullah II of Jordan (b. 1962, 41st Gen) → Crown Prince Al-Hussein (b. 1994, 42nd Gen) → Princess Iman bint Al-Hussein (b. Aug 2024, 43rd Gen!)", 22, "1962 – Present Day (2026 • Living Royal House of Jordan)",
         "Living 41st–43rd Generation Direct Descendants of Prophet Muhammad (Hashemite Dynasty)",
         "Reigning Hashemite King Abdullah II bin Al-Hussein (acceded 1999) + Queen Rania -> Crown Prince Al-Hussein bin Abdullah II (b. 1994, + Princess Rajwa Al Saif) -> Princess Iman bint Al-Hussein (born August 3, 2024 — 43rd generation from Prophet Muhammad; alongside her aunt Princess Iman bint Abdullah, b. 1996, & Prince Hashem, b. 2005!).",
         {"major": True, "altNames": ["King Abdullah II (Living)", "Crown Prince Hussein (Living)", "Princess Iman (b. 2024)"]}),
    ]
    add_chain(nodes, edges, hashemite_chain, start_parent="ar_hashim_muhammad_caliphs", start_edge_type="direct",
              start_edge_label="Fatimah & Ali -> Imam Hasan ibn Ali -> Continuous Hashemite Line to 2026",
              tradition="arabian", default_edge_type="direct", default_sources=["Hashemite Royal Registers", "Meccan Sharifate Chronicles"])

    # Branch 1B: Alaouite Dynasty of Morocco (Living King Mohammed VI & Crown Prince Moulay Hassan)
    nodes += [
        N("mod_alaouite_morocco", "LIVING (2026): Alaouite Dynasty of Morocco — Hassan al-Dakhil (13th c.) → Moulay Ali Cherif (1631) → Mohammed V → Hassan II → King Mohammed VI (b. 1963) → Crown Prince Moulay Hassan (b. 2003)", "arabian", 22, "1266 – Present Day (2026 • Living Royal House of Morocco)",
          "Living Hasanid Dynasty Ruling Morocco (via Hasan al-Muthanna & Al-Nafs al-Zakiyya)", ["Moroccan Alaouite Chronicles", "Official Royal Registers"],
          "Descended from Hasan al-Muthanna -> Muhammad al-Nafs al-Zakiyya -> Hassan al-Dakhil (migrated from Yanbu in Arabia to Tafilalt, Morocco in the 13th c.) -> Moulay Ali Cherif (1631) -> Moulay Ismail -> Mohammed V -> Hassan II -> reigning King Mohammed VI (b. 1963) & Crown Prince Moulay Hassan (b. 2003).",
          ["Hassan al-Dakhil", "Moulay Ismail", "King Mohammed VI (Living)", "Crown Prince Moulay Hassan (Living)"], major=True),
        N("mod_agakhan5_ismaili", "LIVING (2026): Nizari Ismaili Imamat — Husayn ibn Ali → Ja'far al-Sadiq → Fatimid Caliphs → Aga Khan IV (d. Feb 2025) → Aga Khan V (Prince Rahim al-Hussaini, b. 1971, 50th Imam!)", "arabian", 22, "680 – Present Day (2026 • 50th Hereditary Imam)",
          "Living Husaynid Spiritual Imamat (Continuous Nass Succession to 2026)", ["Nizari Ismaili Imamat Archives", "Fatimid Chronicles"],
          "Traces continuous hereditary Imamat from Fatimah & Ali -> Imam Husayn -> Ali Zayn al-Abidin -> Muhammad al-Baqir -> Ja'far al-Sadiq -> Isma'il -> Fatimid Caliphs (Cairo) -> Alamut & Persian Imams -> Aga Khan I–IV -> Prince Rahim al-Hussaini (Aga Khan V, living, b. 1971, acceded Feb 2025 as 50th Imam!).",
          ["Ja'far al-Sadiq", "Fatimid Caliphs", "Aga Khan IV", "Aga Khan V / Prince Rahim (Living)"], major=True),
    ]

    # -------------------------------------------------------------------------
    # BRANCH 2: ABRAHAM -> ISAAC -> JACOB -> JUDAH -> DAVID -> SOLOMON -> LIVING ETHIOPIAN SOLOMONIC HOUSE (2026)
    # -------------------------------------------------------------------------
    solomonic_chain = [
        ("mod_eth_yekuno_to_lebna", "Solomonic Imperial Spine (1270–1540): Yekuno Amlak → Wedem Arad → Amda Seyon I → Newaya Krestos → Dawit I → Zara Yaqob → Ba'eda Maryam I → Naod → Dawit II (Lebna Dengel)", 20, "1270-1540 CE (Ethiopian Royal Chronicles)",
         "Medieval Golden Age of the Restored Solomonic Empire of Ethiopia",
         "Nine unbroken father-to-son emperors from Yekuno Amlak (1270) through scholar-emperor Zara Yaqob (1434-1468) down to Dawit II (Lebna Dengel, r. 1508-1540).",
         {"major": True, "altNames": ["Amda Seyon I", "Emperor Zara Yaqob", "Dawit II (Lebna Dengel)"]}),
        ("mod_eth_shewa_sahle", "Shewan Solomonic Branch (1540–1930): Abeto Yaqob → Segwe Qal → Werede Qal → Libse Qal → Negasi Krestos (1682) → Sebaste → Abuye → Amha Iyesus → Asfa Wossen → Wossen Seged → Negus Sahle Selassie → Princess Tenagnework → Ras Makonnen", 21, "1540-1906 CE (Shewan Royal Chronicles)",
         "14-Generation Shewan Bridge Connecting Lebna Dengel to Emperor Haile Selassie I",
         "Lebna Dengel's 4th son Abeto Yaqob settled in Menz (Shewa) -> Negasi Krestos founded the Kingdom of Shewa (c. 1682) -> King Sahle Selassie (1813-1847, grandfather of Emperor Menelik II & great-grandfather of Haile Selassie via Princess Tenagnework -> Ras Makonnen!).",
         {"altNames": ["Negasi Krestos", "Negus Sahle Selassie", "Princess Tenagnework", "Ras Makonnen", "Emperor Menelik II"]}),
        ("mod_eth_living_2026", "LIVING (2026): Ethiopian Imperial House — Emperor Haile Selassie I (1892–1975) → Crown Prince Amha Selassie (1916–1997) → Prince Zera Yacob Amha Selassie (b. 1953) & Prince Ermias Sahle Selassie (b. 1960)", 22, "1930 – Present Day (2026 • Living Solomonic Princes)",
         "Living Heads of the Ethiopian Imperial House & Crown Council (225th Traditional Monarch Line)",
         "Emperor Haile Selassie I (Tafari Makonnen, r. 1930-1974) -> Crown Prince Asfaw Wossen (Amha Selassie) -> Prince Zera Yacob Amha Selassie (living, b. 1953, Head of the Imperial House of Ethiopia) alongside his cousin Prince Ermias Sahle Selassie (living, b. 1960, President of the Crown Council of Ethiopia).",
         {"major": True, "altNames": ["Amha Selassie", "Prince Zera Yacob (Living)", "Prince Ermias Sahle Selassie (Living)"]}),
    ]
    add_chain(nodes, edges, solomonic_chain, start_parent="keb_kaleb_gabramaskal_yekuno", start_edge_type="direct",
              start_edge_label="Continuous Ethiopian Solomonic Succession from Yekuno Amlak (1270) to 2026",
              tradition="african", default_edge_type="direct", default_sources=["Ethiopian Royal Chronicles", "Crown Council of Ethiopia"])

    # -------------------------------------------------------------------------
    # BRANCH 3: ABRAHAM -> DAVID -> [KARTLIS TSKHOVREBA CLAIM] -> LIVING GEORGIAN BAGRATIONI HOUSE (2026)
    # -------------------------------------------------------------------------
    bagrationi_chain = [
        ("mod_geo_tamar_to_constantine2", "Late Medieval Bagrationis (1213–1505): Queen Tamar → George IV & Queen Rusudan → Demetrius II → George V the Brilliant → David IX → Bagrat V → Constantine I → Alexander I the Great → Constantine II", 20, "1213-1505 CE (Georgian Royal Annals)",
         "Common Ancestors of All Modern Bagrationi Branches (Mukhrani, Kartli & Kakheti)",
         "George V the Brilliant freed Georgia from Mongol rule; Alexander I the Great (1412-1442) and Constantine II (1478-1505) were the last kings before the kingdom divided into Kartli/Mukhrani, Kakheti, and Imereti.",
         {"altNames": ["George V the Brilliant", "Alexander I the Great", "Constantine II of Georgia"]}),
        ("mod_geo_mukhrani_erekle2", "Mukhrani & Kakheti Royal Houses (1505–2008): Prince Bagrat I of Mukhrani → Vakhtang V & VI → Prince George Mukhrani; AND King Heraclius II (Erekle II, 1720–1798) → King George XII → Prince Nugzar Bagration-Gruzinsky", 21, "1505-2008 CE (Bagrationi Royal Houses)",
         "Senior Agnatic Mukhrani Branch & Last Reigning Kings of Kartli-Kakheti",
         "Bagrat I founded the senior male-line House of Mukhrani; King Heraclius II (Erekle II) & King George XII were the final reigning Georgian monarchs before Russian annexation in 1800, continuing through the Gruzinsky branch.",
         {"altNames": ["Bagrat I of Mukhrani", "King Heraclius II (Erekle II)", "King George XII"]}),
        ("mod_geo_giorgi_2011", "LIVING (2026): Prince David Bagration of Mukhrani (b. 1976) & Princess Ana Bagration-Gruzinsky (b. 1976) → Prince Giorgi Bagrationi (b. Sept 27, 2011!)", 22, "1976 – Present Day (2026 • Living Royal House of Georgia)",
         "21st-Century Unification of Both Living Georgian Bagrationi Royal Lines",
         "Born in 2011 and baptized by Georgian Patriarch Ilia II, Prince Giorgi Bagrationi unites both historic surviving branches of the world's oldest Christian royal house (Mukhrani via father Prince David & Kakheti/Gruzinsky via mother Princess Ana)!",
         {"major": True, "altNames": ["Prince David Bagration (Living)", "Princess Ana Bagration-Gruzinsky (Living)", "Prince Giorgi Bagrationi (b. 2011)"]}),
    ]
    add_chain(nodes, edges, bagrationi_chain, start_parent="geo_bagrationi_davidic", start_edge_type="direct",
              start_edge_label="Continuous Bagrationi Succession from Queen Tamar (1213) to Prince Giorgi (b. 2011)",
              tradition="iranian", default_edge_type="direct", default_sources=["Georgian Royal Annals", "Royal House of Georgia"])

    # -------------------------------------------------------------------------
    # BRANCH 4: ABRAHAM -> DAVID -> JEHOIACHIN -> ZERUBBABEL -> EXILARCHS -> RASHI / MAHARAL / ABRAVANEL -> LIVING FAMILIES (2026)
    # -------------------------------------------------------------------------
    davidic_chain = [
        ("mod_exilarchs_bostanai", "Babylonian Exilarchs (Resh Galuta): Huna I → Mar Ukba → Mar Zutra II → Bostanai ben Haninai (+ Sasanian Princess Izdundad!) → Hisdai → David ben Zakkai → Hezekiah Gaon (d. 1058)", 20, "c. 170-1058 CE (Seder Olam Zuta; Letter of Sherira Gaon; Talmud)",
         "Recognized Patrilineal Davidic Heads of Babylonian Jewry (Intermarried with Sasanians!)",
         "The Babylonian Exilarchs (Resh Galuta) maintained a recognized Davidic succession via Zerubbabel under Parthian, Sasanian & Abbasid rule! Exilarch Bostanai (c. 618-670) married Sasanian Princess Izdundad (daughter of Shah Khosrow II!). After last Exilarch Hezekiah Gaon (d. 1058), surviving branches migrated to Spain and France.",
         {"major": True, "altNames": ["Exilarch Bostanai", "Princess Izdundad", "David ben Zakkai", "Hezekiah Gaon (Last Exilarch)"]}),
        ("mod_abravanel_sephardic", "Sephardic Exilarchic Line: Don Judah Abravanel → Don Isaac Abravanel (1437–1508) → Leone Ebreo → Living Abravanel & Ibn Daud Families (2026)", 21, "1100 – Present Day (2026 • Sephardic Davidic Heritage)",
         "Documented Iberian-Sephardic Family Preserving Direct Exilarchic Davidic Tradition",
         "Don Isaac Abravanel (statesman, Torah commentator & Treasurer of Portugal and Spain before 1492) and his son Judah (philosopher Leone Ebreo) preserved one of the best-documented Iberian family pedigrees claiming descent from the Babylonian Exilarchs — with thousands of living Abravanel/Abarbanel descendants worldwide today!",
         {"major": True, "altNames": ["Don Isaac Abravanel", "Leone Ebreo", "Living Abravanel Family"]}),
        ("mod_rashi_maharal_living", "LIVING (2026): Ashkenazi Davidic Rabbinic Trunk — Hillel the Elder → Johanan HaSandlar → Rashi (1040–1105) → Maharal of Prague (1525–1609) → Living Luria, Horowitz, Katzenellenbogen, Dayan, Charlap & Schneersohn Families", 22, "1040 – Present Day (2026 • Living Rabbinic & Hasidic Dynasties)",
         "Primary Ancestral Trunk of Living Ashkenazi & Hasidic Davidic Traditions (Note: Pre-Rashi Link Traditional)",
         "Historically proven lineages descend continuously from Rashi (Rabbi Shlomo Yitzchaki, Troyes, 1040-1105 -> daughters Yocheved, Miriam & Rachel -> Rabbeinu Tam) and the Maharal of Prague (1525-1609) into living families today (Katzenellenbogen, Luria, Horowitz, Shapiro, Treves, Charlap, Dayan [incl. Moshe Dayan], & Chabad-Lubavitch Schneersohns). Scholarly integrity note: modern genealogists (Avotaynu) note the pre-1040 bridge from Rashi/Maharal back to Hillel & King David is traditional rather than contemporaneously documented.",
         {"major": True, "altNames": ["Rashi (1040-1105)", "Maharal of Prague", "Katzenellenbogen / Luria / Horowitz / Dayan / Schneersohn"]}),
    ]
    add_chain(nodes, edges, davidic_chain, start_parent="kg_j13_jehoiachin", start_edge_type="expansion",
              start_edge_label="Seder Olam Zuta / Talmudic Tradition: Zerubbabel -> Babylonian Exilarchs (Resh Galuta)",
              tradition="biblical", default_edge_type="expansion", default_sources=["Seder Olam Zuta", "Letter of Sherira Gaon", "Rabbinic Genealogical Archives"])

    # -------------------------------------------------------------------------
    # BRANCH 5: MODERN ARCHAEOGENETIC BIOLOGICAL BRIDGES TO LIVING PEOPLE TODAY (2026)
    # -------------------------------------------------------------------------
    nodes += [
        N("dna_living_kohanim_j1", "LIVING (2026) Y-DNA: Cohen Modal Haplotype (J1-Z18271 / P58) & Samaritan Kohanim — ~3,000-Year Iron Age Levantine Patrilineal Cluster", "dna", 22, "c. 1200 BCE – Present Day (2026 • Modern Population Genetics)",
          "Scientific Biological Continuity of Living Jewish & Samaritan Priestly Families", ["Hammer et al. 2009 (Human Genetics)", "Behar et al. 2017", "FTDNA / YFull J-Z18271"],
          "Over 46% of living Ashkenazi and Sephardic Kohanim (and Samaritan priestly lines) share an extended Y-chromosome signature on Haplogroup J1-P58 (specifically clade J-Z18271, TMRCA ~3,100 yrs ago) — directly matching the Iron Age Levantine timeframe of the Aaronite priesthood!",
          ["Cohen Modal Haplotype", "Y-DNA J1-Z18271", "Living Kohanim & Samaritans"], major=True),
        N("dna_living_hashemites_l859", "LIVING (2026) Y-DNA: Hashemite / Sharifian Genetic Clade (J1-L859 / FGC8703) — Shared Arabian Patrilineal Lineage Today", "dna", 22, "c. 500 CE – Present Day (2026 • Modern Genetic Genealogy)",
          "Independent Living Hashemite, Hasanid & Husaynid Families Converging on Y-DNA J1-L859", ["YFull J-L859 / FGC8703 Phylogeny", "Arabian Y-DNA Consortium"],
          "Modern whole-Y sequencing of geographically separated Ashraf/Sayyid families across Jordan, Hejaz, Iraq, Yemen & Morocco reveals a striking shared J1-P58 downstream clade (J1-L859 / FGC8703) coalescing ~1,400–1,600 years ago — providing independent genetic corroboration of medieval Quraysh/Hashemite patrilineal continuity!",
          ["Y-DNA J1-L859", "FGC8703", "Living Ashraf & Sayyids"], major=True),
    ]

    # Exhaustive individual-level rosters for the 24 Qatadid Sharifs & 23 Solomonic generations!
    add_roster(nodes, edges, "mod_qatadah_sharifs", "modr_has", "arabian", 20, "1201-1999 CE (Banu Qatadah)", "Sharif of Mecca / Hashemite Monarch", ["Meccan Sharifate Chronicles", "Hashemite Royal Court"], [
        "1. Qatadah ibn Idris (Emir of Mecca, 1201-1220)", "2. Ali al-Akbar ibn Qatadah", "3. Abu Sa'd al-Hasan ibn Ali",
        "4. Muhammad Abu Numayy I (d. 1301)", "5. Rumaithah ibn Abu Numayy I", "6. Ajlan ibn Rumaithah",
        "7. Ali ibn Ajlan", "8. Hasan ibn Ajlan", "9. Barakat I ibn Hasan", "10. Muhammad ibn Barakat",
        "11. Barakat II ibn Muhammad", "12. Muhammad Abu Numayy II (1525-1584)", "13. Hasan ibn Abu Numayy II",
        "14. Abdullah ibn Hasan (Ancestor of Abadilah)", "15. Hussein -> 16. Abdullah -> 17. Muhsin -> 18. Awn",
        "19. Abd al-Mu'in -> 20. Muhammad -> 21. Ali Pasha", "22. Sharif Hussein bin Ali (King of Hejaz, 1854-1931)",
        "23. King Abdullah I of Jordan & King Faisal I of Iraq", "24. King Talal -> King Hussein of Jordan (1935-1999)"
    ], edge_type="direct", edge_label="Banu Qatadah Sharifian Line")

    add_roster(nodes, edges, "mod_eth_shewa_sahle", "modr_eth", "african", 21, "1270-1975 CE (Solomonic Dynasty)", "Solomonic Emperor / Prince of Ethiopia", ["Ethiopian Royal Chronicles"], [
        "Wedem Arad (Son of Yekuno Amlak)", "Amda Seyon I (1314-1344)", "Newaya Krestos -> Dawit I",
        "Emperor Zara Yaqob (1434-1468)", "Ba'eda Maryam I -> Naod", "Dawit II / Lebna Dengel (1508-1540)",
        "Abeto Yaqob -> Segwe Qal -> Werede Qal -> Libse Qal", "Negasi Krestos (1st Ruler of Shewa, 1682)",
        "Sebaste -> Abuye -> Amha Iyesus -> Asfa Wossen -> Wossen Seged", "Negus Sahle Selassie of Shewa (1813-1847)",
        "Princess Tenagnework Sahle Selassie -> Ras Makonnen", "Emperor Menelik II (Victor of Adwa, 1896)"
    ], edge_type="direct", edge_label="Solomonic Imperial Succession")

    # Cross-links connecting into the existing Atlas graph!
    edges += [
        E("mod_hasan_muthanna", "mod_alaouite_morocco", "direct", "Hasan al-Muthanna -> Al-Nafs al-Zakiyya -> Hassan al-Dakhil -> Living King Mohammed VI"),
        E("ar_hashim_muhammad_caliphs", "mod_agakhan5_ismaili", "direct", "Fatimah & Ali -> Imam Husayn -> Fatimids -> Living Aga Khan V (2025)"),
        E("mod_eth_shewa_sahle", "eth_haile_selassie", "direct", "Ras Makonnen -> Emperor Haile Selassie I (1892-1975)"),
        E("eth_haile_selassie", "mod_eth_living_2026", "direct", "Haile Selassie -> Amha Selassie -> Living Princes Zera Yacob & Ermias"),
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
