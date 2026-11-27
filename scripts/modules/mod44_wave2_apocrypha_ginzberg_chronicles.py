"""
Module 44: Wave 2 Person-by-Person Deep Extractions from:
1. Myers Anchor Bible 1 Chronicles (ab1Chronicles2nd MyersJM 1965-opt.pdf):
   - 13-Generation Judah-Egypt Pedigree (1 Chr 2:34-41): Sheshan -> Ahlai + Jarha -> Attai -> ... -> Elishama
   - Mered + Bithiah Daughter of Pharaoh (1 Chr 4:17-18) -> Miriam, Shammai, Ishbah; Judahite wife -> Jered, Heber, Jekuthiel
   - Jerahmeel (+ Atarah) -> 6 Sons & Onam; Ashhur (+ Helah & Naarah); Hur -> Uri -> Bezalel, Shobal, Salma
   - Ephraim -> Beriah & Sheerah -> 10-Generation Pedigree to Joshua (1 Chr 7:20-27)
   - Reuben 8-Generation Pedigree to Prince Beerah (1 Chr 5:4-6)
   - Asher -> Heber -> Japhlet, Shomer, Hotham & Sister Shua (1 Chr 7:30-40)
   - Benjamin -> Shaharaim (+ Hushim & Hodesh in Moab) & Beriah/Shema (1 Chr 8)
   - Complete First Temple High Priests (1 Chr 6:4-15): every link from Abishua -> Zadok I -> Hilkiah -> Seraiah -> Jehozadak
2. Charles APOT Vol. 2 / Testaments of the Twelve Patriarchs (charles2.pdf) & Ginzberg's Legends of the Jews:
   - Bilhah & Zilpah's Chaldean Pedigree (Testament of Naphtali 1:9-12; Ginzberg II, 209): Rotheus (+ Euna) & Sister Deborah (Rebekah's Nurse)
   - Levi + Melcha bat Bathuel (Testament of Levi 11:1) -> Gershon, Kohath, Merari, Jochebed
   - Hadorah & Malchiel tradition -> Serah bat Asher (Ginzberg II, 39)
   - Issachar + Aridah (Ginzberg Index p. 61; Jasher 45)
   - Pseudo-Philo Individualized Persons (Noaba, Themech, Judge Kenaz, Zebul, Seila, Eluma)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # 1. 1 CHRONICLES 2:34-41 JUDAH-EGYPT 13-GEN PEDIGREE (SHEHAN -> JARHA -> ELISHAMA)
    # =========================================================================
    nodes += [
        N("chr2_sheshan", "Sheshan (Jerahmeelite Father of Ahlai, 1 Chr 2:34–35)", "biblical", 14,
          "1 Chronicles 2:31, 34–35", "Jerahmeelite Patriarch Without Sons", ["1 Chronicles 2:31, 34–35", "Myers 1 Chronicles (1965 p.109)"],
          "Descended from Jerahmeel -> Onam -> Shammai -> Nadab -> Appaim -> Ishi -> Sheshan; wed his daughter Ahlai to his Egyptian servant Jarha."),
        N("chr2_ahlai", "Ahlai (Daughter of Sheshan; Wife of Jarha the Egyptian, 1 Chr 2:31, 35)", "biblical", 15,
          "1 Chronicles 2:31, 35", "Judahite Heiress Wed to Jarha the Egyptian", ["1 Chronicles 2:31, 35", "Myers 1 Chronicles p.109"],
          "Daughter and heiress of Sheshan who married Jarha the Egyptian and bore Attai."),
        N("chr2_jarha", "Jarha the Egyptian (Son-in-Law of Sheshan, 1 Chr 2:34–35)", "levant_egypt", 15,
          "1 Chronicles 2:34–35", "Egyptian Grafted Into Tribe of Judah", ["1 Chronicles 2:34–35", "Myers 1 Chronicles p.109"],
          "Egyptian servant freed and given Sheshan's daughter Ahlai in marriage, founding a 13-generation Judahite lineage."),
    ]
    edges += [
        E("chr41_jerahmeel_atarah", "chr2_sheshan", "direct", "1 Chr 2:28–34: Onam -> Shammai -> Nadab -> Appaim -> Ishi -> Sheshan"),
        E("chr2_sheshan", "chr2_ahlai", "direct", "1 Chr 2:31, 35: Sheshan -> daughter Ahlai"),
        E("chr2_ahlai", "chr2_jarha", "direct", "1 Chr 2:35: Marriage of Ahlai & Jarha the Egyptian"),
        E("chr41_sheshan_jarha_egypt", "chr2_ahlai", "direct", "1 Chr 2:35: Judah-Egypt household anchor"),
    ]
    jarha_chain = [
        ("chr2_attai", "Attai (Son of Jarha & Ahlai, 1 Chr 2:35–36)"),
        ("chr2_nathan", "Nathan ben Attai (1 Chr 2:36)"),
        ("chr2_zabad", "Zabad ben Nathan (1 Chr 2:36)"),
        ("chr2_ephlal", "Ephlal ben Zabad (1 Chr 2:37)"),
        ("chr2_obed", "Obed ben Ephlal (1 Chr 2:37)"),
        ("chr2_jehu", "Jehu ben Obed (1 Chr 2:38)"),
        ("chr2_azariah", "Azariah ben Jehu (1 Chr 2:38)"),
        ("chr2_helez", "Helez ben Azariah (1 Chr 2:39)"),
        ("chr2_eleasah", "Eleasah ben Helez (1 Chr 2:39)"),
        ("chr2_sismai", "Sismai ben Eleasah (1 Chr 2:40)"),
        ("chr2_shallum", "Shallum ben Sismai (1 Chr 2:40)"),
        ("chr2_jekamiah", "Jekamiah ben Shallum (1 Chr 2:41)"),
        ("chr2_elishama", "Elishama ben Jekamiah (13th Gen From Jarha, 1 Chr 2:41)"),
    ]
    prev_j = "chr2_ahlai"
    for jid, jnm in jarha_chain:
        nodes.append(N(jid, jnm, "biblical", 15, "1 Chronicles 2:35–41", "Judah–Egyptian Lineage Member",
                       ["1 Chronicles 2:35–41", "Myers Anchor Bible 1 Chronicles p.109"], f"{jnm}."))
        edges.append(E(prev_j, jid, "direct", "1 Chr 2:35–41: Jarha–Ahlai pedigree"))
        if prev_j == "chr2_ahlai":
            edges.append(E("chr2_jarha", jid, "direct", "1 Chr 2:35: Father Jarha the Egyptian -> Attai"))
        prev_j = jid

    # =========================================================================
    # 2. MERED + BITHIAH DAUGHTER OF PHARAOH (1 Chr 4:17-18) & HEZRON/HUR BRANCHES
    # =========================================================================
    nodes += [
        N("chr2_mered", "Mered of Judah (Son of Ezrah; Husband of Pharaoh's Daughter Bithiah, 1 Chr 4:17–18)", "biblical", 15,
          "1 Chronicles 4:17–18 (Myers p.122)", "Judahite Husband of Egyptian Princess Bithiah", ["1 Chronicles 4:17–18", "Talmud Sanhedrin 19b"],
          "Son of Ezrah; married both a Judahite wife (Hodiah) and Pharaoh's daughter Bithiah."),
        N("chr2_bithiah", "Princess Bithiah (Daughter of Pharaoh; Wife of Mered, 1 Chr 4:18; Ginzberg II, 270)", "levant_egypt", 15,
          "1 Chronicles 4:18 (Myers p.122; Ginzberg II, 270)", "Egyptian Princess Married Into Tribe of Judah",
          ["1 Chronicles 4:18", "Ginzberg Legends II, 270, V, 398"],
          "Explicitly named in 1 Chr 4:18 as 'Bithiah the daughter of Pharaoh, whom Mered married'; identified in Rabbinic tradition (Ginzberg II, 270; VII, 84) as Moses's adoptive mother!", major=True),
        N("chr2_miriam_bithiah", "Miriam (Daughter of Mered & Bithiah, 1 Chr 4:17)", "biblical", 15, "1 Chronicles 4:17", "Daughter of Mered & Pharaoh's Daughter", ["1 Chronicles 4:17"], "First named child of Bithiah in 1 Chr 4:17."),
        N("chr2_shammai_bithiah", "Shammai (Son of Mered & Bithiah, 1 Chr 4:17)", "biblical", 15, "1 Chronicles 4:17", "Son of Mered & Pharaoh's Daughter", ["1 Chronicles 4:17"], "Father of Maon and Eshtemoa."),
        N("chr2_ishbah_bithiah", "Ishbah (Father of Eshtemoa; Son of Mered & Bithiah, 1 Chr 4:17)", "biblical", 15, "1 Chronicles 4:17", "Son of Mered & Pharaoh's Daughter", ["1 Chronicles 4:17"], "Founder of Eshtemoa."),
        N("chr2_jered_mered", "Jered (Father of Gedor; Son of Mered & Judahite Wife, 1 Chr 4:18)", "biblical", 15, "1 Chronicles 4:18", "Son of Mered", ["1 Chronicles 4:18"], "Father of Gedor."),
        N("chr2_heber_mered", "Heber (Father of Soco; Son of Mered & Judahite Wife, 1 Chr 4:18)", "biblical", 15, "1 Chronicles 4:18", "Son of Mered", ["1 Chronicles 4:18"], "Father of Soco."),
        N("chr2_jekuthiel_mered", "Jekuthiel (Father of Zanoah; Son of Mered & Judahite Wife, 1 Chr 4:18)", "biblical", 15, "1 Chronicles 4:18", "Son of Mered", ["1 Chronicles 4:18"], "Father of Zanoah."),
        # Hur -> Uri -> Bezalel, Shobal, Salma + Ashhur
        N("chr2_hur", "Hur (Son of Caleb ben Hezron & Ephrath; Supported Moses's Hands, Exod 17:10; 1 Chr 2:19)", "biblical", 15,
          "Exodus Era (Exod 17:10; 1 Chr 2:19, 50)", "Judahite Elder & Grandfather of Bezalel", ["Exodus 17:10", "1 Chronicles 2:19–20, 50"],
          "Firstborn of Ephrath; father of Uri, Shobal, Salma, and Hareph."),
        N("chr2_uri_hur", "Uri ben Hur (Father of Bezalel, Exod 31:2; 1 Chr 2:20)", "biblical", 15, "1 Chronicles 2:20", "Son of Hur", ["Exodus 31:2", "1 Chronicles 2:20"], "Father of Tabernacle architect Bezalel."),
        N("chr2_bezalel", "Bezalel ben Uri (Chief Architect of the Tabernacle & Ark, Exod 31:2)", "biblical", 16, "Exodus Era (Exod 31:2–6, 35:30)", "Chief Artisan of the Ark of the Covenant", ["Exodus 31:2–6", "1 Chronicles 2:20"], "Filled with the Spirit of God to craft the Ark and Tabernacle.", major=True),
        N("chr2_shobal_hur", "Shobal ben Hur (Founder of Kiriath-jearim, 1 Chr 2:50)", "biblical", 15, "1 Chronicles 2:50", "Eldest Son of Hur", ["1 Chronicles 2:50"], "Father of Kiriath-jearim."),
        N("chr2_salma_hur", "Salma ben Hur (Founder of Bethlehem & Kenite Scribes, 1 Chr 2:51, 54)", "biblical", 15, "1 Chronicles 2:51, 54", "Son of Hur", ["1 Chronicles 2:51, 54"], "Father of Bethlehem and Netophathites."),
        N("chr2_atarah", "Atarah (2nd Wife of Jerahmeel; Mother of Onam, 1 Chr 2:26)", "biblical", 14, "1 Chronicles 2:26", "Wife of Jerahmeel", ["1 Chronicles 2:26"], "Second wife of Jerahmeel ben Hezron; mother of Onam."),
        N("chr2_onam", "Onam (Son of Jerahmeel & Atarah, 1 Chr 2:26, 28)", "biblical", 14, "1 Chronicles 2:26–28", "Ancestor of Sheshan & Jarha", ["1 Chronicles 2:26–28"], "Son of Jerahmeel & Atarah; grandfather of Appaim/Sheshan."),
        N("chr2_helah_naarah", "Helah & Naarah (Wives of Ashhur of Tekoa, 1 Chr 4:5–7)", "biblical", 14, "1 Chronicles 4:5–7", "Wives of Ashhur", ["1 Chronicles 4:5–7"], "Bore Zereth, Izhar, Ethnan, Ahuzzam, Hepher, Temeni, and Haahashtari."),
    ]
    edges += [
        E("chr41_mered_bithiah_pharaoh", "chr2_mered", "direct", "1 Chr 4:17–18: Mered of Judah"),
        E("chr41_mered_bithiah_pharaoh", "chr2_bithiah", "direct", "1 Chr 4:18: Bithiah daughter of Pharaoh"),
        E("chr2_mered", "chr2_bithiah", "direct", "1 Chr 4:18: Marriage of Mered & Bithiah bat Pharaoh"),
        E("chr2_bithiah", "chr2_miriam_bithiah", "direct", "1 Chr 4:17: Bithiah -> Miriam"),
        E("chr2_mered", "chr2_miriam_bithiah", "direct", "1 Chr 4:17: Mered -> Miriam"),
        E("chr2_bithiah", "chr2_shammai_bithiah", "direct", "1 Chr 4:17: Bithiah -> Shammai"),
        E("chr2_mered", "chr2_shammai_bithiah", "direct", "1 Chr 4:17: Mered -> Shammai"),
        E("chr2_bithiah", "chr2_ishbah_bithiah", "direct", "1 Chr 4:17: Bithiah -> Ishbah"),
        E("chr2_mered", "chr2_ishbah_bithiah", "direct", "1 Chr 4:17: Mered -> Ishbah"),
        E("chr2_mered", "chr2_jered_mered", "direct", "1 Chr 4:18: Mered -> Jered"),
        E("chr2_mered", "chr2_heber_mered", "direct", "1 Chr 4:18: Mered -> Heber"),
        E("chr2_mered", "chr2_jekuthiel_mered", "direct", "1 Chr 4:18: Mered -> Jekuthiel"),
        E("w2_caleb_jephunneh", "chr2_hur", "direct", "1 Chr 2:19: Caleb + Ephrath -> Hur"),
        E("chr2_hur", "chr2_uri_hur", "direct", "1 Chr 2:20: Hur -> Uri"),
        E("chr2_uri_hur", "chr2_bezalel", "direct", "Exod 31:2 & 1 Chr 2:20: Uri -> Bezalel"),
        E("chr2_hur", "chr2_shobal_hur", "direct", "1 Chr 2:50: Hur -> Shobal"),
        E("chr2_hur", "chr2_salma_hur", "direct", "1 Chr 2:51: Hur -> Salma"),
        E("chr41_jerahmeel_atarah", "chr2_atarah", "direct", "1 Chr 2:26: Wife Atarah"),
        E("chr2_atarah", "chr2_onam", "direct", "1 Chr 2:26: Atarah -> Onam"),
        E("chr41_ashhur_tekoa", "chr2_helah_naarah", "direct", "1 Chr 4:5–7: Wives of Ashhur"),
    ]

    # =========================================================================
    # 3. EPHRAIM -> JOSHUA (10 GENS) + REUBEN -> BEERAH (8 GENS) + ASHER/BENJAMIN
    # =========================================================================
    eph_chain = [
        ("chr2_eph_beriah", "Beriah ben Ephraim (1 Chr 7:23)"),
        ("chr2_eph_rephah", "Rephah ben Beriah (1 Chr 7:25)"),
        ("chr2_eph_resheph", "Resheph (1 Chr 7:25)"),
        ("chr2_eph_telah", "Telah (1 Chr 7:25)"),
        ("chr2_eph_tahan", "Tahan (1 Chr 7:25)"),
        ("chr2_eph_ladan", "Ladan (1 Chr 7:26)"),
        ("chr2_eph_ammihud", "Ammihud ben Ladan (1 Chr 7:26)"),
        ("chr2_eph_elishama", "Elishama ben Ammihud (Prince of Ephraim, Num 1:10; 1 Chr 7:26)"),
        ("chr2_eph_nun", "Nun ben Elishama (Father of Joshua, 1 Chr 7:27)"),
    ]
    prev_e = "jos_ephraim"
    for eid, enm in eph_chain:
        nodes.append(N(eid, enm, "biblical", 15, "1 Chronicles 7:23–27", "Ephraimite Ancestor of Joshua", ["1 Chronicles 7:23–27"], f"{enm}."))
        edges.append(E(prev_e, eid, "direct", "1 Chr 7:23–27: Ephraim -> Joshua"))
        prev_e = eid
    edges.append(E(prev_e, "bib_joshua_caleb", "direct", "1 Chr 7:27: Nun -> Joshua ben Nun"))
    nodes.append(N("chr2_sheerah", "Sheerah (Daughter of Ephraim; Founder of Beth-horon, 1 Chr 7:24)", "biblical", 14,
                   "1 Chronicles 7:24", "City-Builder Daughter of Ephraim", ["1 Chronicles 7:24"],
                   "Built Lower Beth-horon, Upper Beth-horon, and Uzzen-sheerah."))
    edges.append(E("jos_ephraim", "chr2_sheerah", "direct", "1 Chr 7:24: Ephraim -> daughter Sheerah"))

    reub_chain = [
        ("chr2_reu_joel", "Joel (Reubenite Chief, 1 Chr 5:4)"),
        ("chr2_reu_shemaiah", "Shemaiah (1 Chr 5:4)"),
        ("chr2_reu_gog", "Gog ben Shemaiah (1 Chr 5:4)"),
        ("chr2_reu_shimei", "Shimei ben Gog (1 Chr 5:4)"),
        ("chr2_reu_micah", "Micah ben Shimei (1 Chr 5:5)"),
        ("chr2_reu_reaiah", "Reaiah ben Micah (1 Chr 5:5)"),
        ("chr2_reu_baal", "Baal ben Reaiah (1 Chr 5:5)"),
        ("chr2_reu_beerah", "Prince Beerah of Reuben (Exiled by Tiglath-Pileser III, 1 Chr 5:6)"),
    ]
    prev_r = "tri_reuben"
    for rid, rnm in reub_chain:
        nodes.append(N(rid, rnm, "biblical", 15, "1 Chronicles 5:4–6", "Reubenite Lineage to Assyrian Exile", ["1 Chronicles 5:4–6"], f"{rnm}."))
        edges.append(E(prev_r, rid, "direct", "1 Chr 5:4–6: Reubenite lineage"))
        prev_r = rid
    edges.append(E("chr41_reuben_beerah", "chr2_reu_beerah", "direct", "1 Chr 5:6: Prince Beerah"))

    nodes += [
        N("chr2_ash_japhlet", "Japhlet ben Heber (Asherite Chief, 1 Chr 7:32)", "biblical", 15, "1 Chr 7:32", "Son of Heber ben Beriah", ["1 Chronicles 7:32"], "Eldest son of Heber; father of Pasach, Bimhal & Ashvath."),
        N("chr2_ash_shomer", "Shomer / Shemer ben Heber (1 Chr 7:32, 34)", "biblical", 15, "1 Chr 7:32", "Son of Heber", ["1 Chronicles 7:32"], "Father of Ahi, Rohgah, Jehubbah & Aram."),
        N("chr2_ash_hotham", "Hotham / Helem ben Heber (1 Chr 7:32, 35)", "biblical", 15, "1 Chr 7:32", "Son of Heber", ["1 Chronicles 7:32"], "Father of Zophah, Imna, Shelesh & Amal."),
        N("chr2_ash_shua", "Shua (Sister of Japhlet, Shomer & Hotham, 1 Chr 7:32)", "biblical", 15, "1 Chr 7:32", "Named Asherite Woman", ["1 Chronicles 7:32"], "Daughter of Heber ben Beriah explicitly named in Chronicles."),
        N("chr2_ben_shaharaim", "Shaharaim (Benjamite in Moab + Hushim & Hodesh, 1 Chr 8:8–11; Myers p.155)", "biblical", 15,
          "1 Chronicles 8:8–11", "Benjamite Chief Settled in Moab", ["1 Chronicles 8:8–11", "Myers 1 Chronicles p.155"],
          "Fathered 7 sons by Hodesh in Moab (Jobab, Zibia, Mesha, Malcam, Jeuz, Sachiah, Mirmah) and Abitub & Elpaal by Hushim."),
    ]
    edges += [
        E("chr41_asher_shua", "chr2_ash_japhlet", "direct", "1 Chr 7:32: Heber -> Japhlet"),
        E("chr41_asher_shua", "chr2_ash_shomer", "direct", "1 Chr 7:32: Heber -> Shomer"),
        E("chr41_asher_shua", "chr2_ash_hotham", "direct", "1 Chr 7:32: Heber -> Hotham"),
        E("chr41_asher_shua", "chr2_ash_shua", "direct", "1 Chr 7:32: Heber -> daughter Shua"),
        E("chr41_benjamin_clans", "chr2_ben_shaharaim", "direct", "1 Chr 8:8: Benjamite Shaharaim in Moab"),
    ]

    # =========================================================================
    # 4. COMPLETE FIRST TEMPLE HIGH PRIESTS (1 Chr 6:4-15 INDIVIDUAL CHAIN)
    # =========================================================================
    pri_chain = [
        ("pri2_zerahiah", "High Priest Zerahiah ben Uzzi (1 Chr 6:6)"),
        ("pri2_meraioth", "High Priest Meraioth ben Zerahiah (1 Chr 6:6–7)"),
        ("pri2_amariah1", "High Priest Amariah I ben Meraioth (1 Chr 6:7)"),
        ("pri2_ahitub1", "High Priest Ahitub I ben Amariah (1 Chr 6:7–8)"),
        ("pri2_ahimaaz", "High Priest Ahimaaz ben Zadok (2 Sam 15:27; 1 Chr 6:8)"),
        ("pri2_azariah1", "High Priest Azariah I ben Ahimaaz (Solomon's Temple, 1 Kgs 4:2; 1 Chr 6:9)"),
        ("pri2_johanan1", "High Priest Johanan ben Azariah (1 Chr 6:9–10)"),
        ("pri2_azariah2", "High Priest Azariah II ben Johanan (1 Chr 6:10)"),
        ("pri2_amariah2", "High Priest Amariah II (1 Chr 6:11; 2 Chr 19:11)"),
        ("pri2_jehoiada", "High Priest Jehoiada (+ Princess Jehosheba; Protector of King Joash, 2 Kgs 11; 2 Chr 23)"),
        ("pri2_zechariah_jehoiada", "Prophet-Priest Zechariah ben Jehoiada (Martyred, 2 Chr 24:20–22)"),
        ("pri2_ahitub2", "High Priest Ahitub II (1 Chr 6:11–12)"),
        ("pri2_zadok2", "High Priest Zadok II (1 Chr 6:12)"),
        ("pri2_shallum", "High Priest Shallum / Meshullam (1 Chr 6:12–13)"),
        ("pri2_hilkiah", "High Priest Hilkiah (Found Book of the Law, 622 BCE; 2 Kgs 22:8; 1 Chr 6:13)"),
        ("pri2_azariah3", "High Priest Azariah III ben Hilkiah (1 Chr 6:13–14)"),
        ("pri2_seraiah", "High Priest Seraiah ben Azariah (Slain at Riblah, 586 BCE; 2 Kgs 25:18; 1 Chr 6:14)"),
        ("pri2_jehozadak", "High Priest Jehozadak ben Seraiah (Exiled to Babylon, 1 Chr 6:14–15)"),
    ]
    prev_p = "cb_pri_uzzi"
    for pid, pnm in pri_chain:
        maj = "Hilkiah" in pnm or "Seraiah" in pnm or "Jehoiada" in pnm
        nodes.append(N(pid, pnm, "biblical", 17 if "Jehoiada" in pnm or "Hilkiah" in pnm or "Seraiah" in pnm or "Jehozadak" in pnm else 16,
                       "1 Chronicles 6:6–15", "First Temple Zadokite High Priest", ["1 Chronicles 6:6–15", "Dutripon p.23"], f"{pnm}.", major=maj))
        if pid == "pri2_ahimaaz":
            edges.append(E("pri_eleazar_zadok", pid, "direct", "1 Chr 6:8: High Priest Zadok I -> Ahimaaz"))
        elif pid == "pri2_jehoiada":
            edges.append(E("pri2_amariah2", pid, "expansion", "2 Chr 19 & 23: High Priestly succession -> Jehoiada"))
            edges.append(E(pid, "cb_jehosheba", "direct", "2 Chr 22:11: Marriage of Jehoiada & Princess Jehosheba"))
        elif pid == "pri2_zechariah_jehoiada":
            edges.append(E("pri2_jehoiada", pid, "direct", "2 Chr 24:20: Jehoiada -> Zechariah"))
        elif pid == "pri2_ahitub2":
            edges.append(E("pri2_amariah2", pid, "direct", "1 Chr 6:11: Amariah II -> Ahitub II"))
        else:
            edges.append(E(prev_p, pid, "direct", "1 Chr 6:6–15: Zadokite High Priestly father->son chain"))
            if pid == "pri2_ahitub1":
                edges.append(E(pid, "pri_eleazar_zadok", "direct", "1 Chr 6:8: Ahitub I -> High Priest Zadok I"))
        prev_p = pid
    edges.append(E("pri2_jehozadak", "bib16_pri_01_high_priest_jeshua_ben_jehoz", "direct", "1 Chr 6:15 & Ezra 3:2: Jehozadak -> High Priest Jeshua"))
    edges.append(E("pri2_seraiah", "pri_ezra_jaddua", "direct", "Ezra 7:1: Seraiah -> Ezra the Scribe"))

    # =========================================================================
    # 5. GINZBERG & TESTAMENTS OF THE TWELVE PATRIARCHS + PSEUDO-PHILO INDIVIDUALS
    # =========================================================================
    nodes += [
        N("ginz_rotheus", "Rotheus of Chaldea (Brother of Rebekah's Nurse Deborah; Father of Bilhah, T. Naph. 1:9–12)", "biblical", 11,
          "Patriarchal Era (Testament of Naphtali 1:9–12; Ginzberg II, 209)",
          "Chaldean Kinsman of Abraham & Father of Bilhah",
          ["R.H. Charles APOT Vol. 2 / Testaments (charles2.pdf p.350)", "Ginzberg Legends II, 209 & VII Index"],
          "Testament of Naphtali 1:9–12 explicitly states: 'Bilhah, daughter of Rotheus the brother of Deborah, Rebecca's nurse... And Rotheus was of the family of Abraham, a Chaldean, God-fearing, free-born, and noble.'",
          ["Rutheus"], major=True),
        N("ginz_euna", "Euna (Wife of Rotheus; Mother of Bilhah, T. Naph. 1:11–12)", "biblical", 11,
          "Patriarchal Era (Testament of Naphtali 1:11–12)",
          "Chaldean Mother of Bilhah", ["Testament of Naphtali 1:11–12 (charles2.pdf p.350)"],
          "Wife of Rotheus (named Euna/Hannah in variants) who named her daughter Bilhah in Haran."),
        N("ginz_deborah_nurse", "Deborah (Nurse of Rebekah & Sister of Rotheus, Gen 35:8; T. Naph. 1:9)", "biblical", 11,
          "Patriarchal Era (Gen 24:59, 35:8; T. Naph. 1:9)",
          "Rebekah's Nurse Buried Beneath Allon-bacuth", ["Genesis 35:8", "Testament of Naphtali 1:9 (charles2.pdf p.350)"],
          "Rebekah's lifelong nurse buried beneath the Oak of Weeping below Bethel."),
        N("ginz_melcha_levi", "Melcha (Daughter of Bathuel; Wife of Levi, Testament of Levi 11:1)", "biblical", 13,
          "Patriarchal Era (Testament of Levi 11:1; Jub 34:20)",
          "Matriarch of All Levites & Mother of Jochebed", ["Testament of Levi 11:1 (charles2.pdf p.324)"],
          "Testament of Levi 11:1 records: 'When I took a wife I was twenty-eight years old, and her name was Melcha' — bearing Gersam (Gershon), Kohath, Merari & Jochebed."),
        N("ginz_hadurah_serah", "Hadurah / Hadorah (Wife of Malchiel / Asher; Mother of Serah, Ginzberg II, 39; Jasher 45)", "biblical", 13,
          "Egypt / Patriarchal Horizon (Ginzberg II, 39; Jasher 45)",
          "Mother of Righteous Longevity Matriarch Serah bat Asher", ["Ginzberg Legends II, 39 & VII p.440", "Book of Jasher 45"],
          "Widow of Malchiel who wed Asher and brought righteous Serah bat Asher into Jacob's household (Ginzberg II, 39, VII p.440)."),
        N("ginz_aridah_issachar", "Aridah (Daughter of Jobab; Wife of Issachar, Ginzberg Index p.61; Jasher 45)", "biblical", 13,
          "Patriarchal Era (Jasher 45; Ginzberg VII Index p.61)",
          "Wife of Issachar & Sister of Adinah", ["Book of Jasher 45", "Ginzberg Legends VII p.61"],
          "Daughter of Jobab ben Joktan; younger sister of Levi's wife Adinah."),
        # Pseudo-Philo individualized people
        N("pp_noaba", "Noaba (Twin Daughter of Adam & Eve, Pseudo-Philo I.1)", "biblical", 2, "Antediluvian (Pseudo-Philo I.1)", "Named Daughter of Adam & Eve", ["Pseudo-Philo Biblical Antiquities Ch. 1"], "Named twin sister/daughter alongside Cain in Pseudo-Philo."),
        N("pp_themech", "Themech (Wife of Cain, Pseudo-Philo II.1)", "biblical", 3, "Antediluvian (Pseudo-Philo II.1)", "Wife of Cain in Pseudo-Philo", ["Pseudo-Philo Biblical Antiquities Ch. 2"], "Named wife of Cain in Pseudo-Philo Ch. 2."),
        N("pp_kenaz", "Judge Kenaz (57-Year First Judge in Pseudo-Philo Ch. 25–28)", "biblical", 16, "Post-Joshua (Pseudo-Philo Ch. 25–28)", "First Judge of Israel in Pseudo-Philo", ["Pseudo-Philo Biblical Antiquities Ch. 25–28"], "Father of Othniel & uncle/brother in Caleb's Kenizzite house."),
        N("pp_zebul", "Judge Zebul (Successor of Kenaz, Pseudo-Philo Ch. 29)", "biblical", 16, "Judges Era (Pseudo-Philo Ch. 29)", "Judge of Israel in Pseudo-Philo", ["Pseudo-Philo Biblical Antiquities Ch. 29"], "Succeeded Kenaz and established a sacred treasury at Shiloh."),
        N("pp_eluma", "Eluma bat Remac (Mother of Judge Samson, Pseudo-Philo Ch. 42)", "biblical", 16, "Judges Era (Pseudo-Philo Ch. 42)", "Mother of Samson Named in Pseudo-Philo", ["Pseudo-Philo Biblical Antiquities Ch. 42"], "Named wife of Manoah of Zorah in Pseudo-Philo."),
    ]
    edges += [
        E("bib_abraham", "ginz_rotheus", "expansion", "Testament of Naphtali 1:10: Rotheus was 'of the family of Abraham, a Chaldean'"),
        E("ginz_rotheus", "ginz_deborah_nurse", "direct", "T. Naph. 1:9: Brother Rotheus & Sister Deborah"),
        E("ginz_deborah_nurse", "bib_isaac", "expansion", "Gen 24:59 / 35:8: Nurse of Rebekah"),
        E("ginz_rotheus", "ginz_euna", "direct", "T. Naph. 1:11: Marriage of Rotheus & Euna"),
        E("ginz_rotheus", "cb_bilhah", "direct", "T. Naph. 1:9: Father Rotheus -> Bilhah"),
        E("ginz_euna", "cb_bilhah", "direct", "T. Naph. 1:11: Mother Euna -> Bilhah"),
        E("ginz_rotheus", "cb_zilpah", "expansion", "Rabbinic midrash (Gen. Rab. 74:13 / Ginzberg): Bilhah & Zilpah half-sisters"),
        E("tri_levi", "ginz_melcha_levi", "expansion", "T. Levi 11:1: Marriage of Levi & Melcha"),
        E("ginz_melcha_levi", "lev_gershon", "direct", "T. Levi 11:1: Mother Melcha -> Gershon"),
        E("ginz_melcha_levi", "lev_kohath", "direct", "T. Levi 11:1: Mother Melcha -> Kohath"),
        E("ginz_melcha_levi", "lev_merari", "direct", "T. Levi 11:1: Mother Melcha -> Merari"),
        E("ginz_melcha_levi", "lev_jochebed", "expansion", "Exod 6:20 & T. Levi: Levi & Melcha -> Jochebed"),
        E("cb_w_levi", "ginz_melcha_levi", "expansion", "Melka / Melcha harmonization"),
        E("cb_w_asher", "ginz_hadurah_serah", "expansion", "Jasher 45 & Ginzberg II, 39: Hadurah"),
        E("ginz_hadurah_serah", "tri_asher_serah_dau", "expansion", "Ginzberg II, 39: Hadurah -> Serah bat Asher"),
        E("cb_w_issachar", "ginz_aridah_issachar", "expansion", "Ginzberg VII p.61 & Jasher 45: Aridah"),
        E("cb_noaba_pphilo", "pp_noaba", "expansion", "Pseudo-Philo I.1: Noaba"),
        E("cb_themech_pphilo", "pp_themech", "expansion", "Pseudo-Philo II.1: Themech"),
        E("cb_pphilo_kenaz", "pp_kenaz", "expansion", "Pseudo-Philo Ch. 25–28: Judge Kenaz"),
        E("pp_kenaz", "pp_zebul", "direct", "Pseudo-Philo Ch. 29: Kenaz -> Zebul"),
        E("cb_samson_women", "pp_eluma", "expansion", "Pseudo-Philo Ch. 42: Eluma bat Remac"),
        E("pp_eluma", "jdg_samson", "direct", "Pseudo-Philo Ch. 42: Mother Eluma -> Samson"),
    ]

    return {
        "module": "44_wave2_apocrypha_ginzberg_chronicles",
        "title": "Wave 2 Person-by-Person 1 Chronicles (Jarha, Bithiah, Ephraim->Joshua, Reuben, 1 Chr 6 High Priests), Ginzberg Legends & Testaments of the 12 Patriarchs",
        "nodes": nodes,
        "edges": edges,
    }
