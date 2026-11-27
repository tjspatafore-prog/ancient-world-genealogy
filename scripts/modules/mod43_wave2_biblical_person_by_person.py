"""
Module 43: Wave 2 Person-by-Person Biblical Backbone
Unpacks every grouped/summary chain in the core Biblical narrative into individual clickable people
with exact parent->child, mother->child, and spouse arrows:
1. Perez -> Hezron -> Ram -> Amminadab -> Nahshon -> Salmon (+ Rahab) -> Boaz (+ Ruth) -> Obed -> Jesse -> David + 6 Brothers & 2 Sisters' Generals
2. All 20 Monarchs of Judah & All 13 Named Queen Mothers (individualized king-by-king & mother-by-mother) + Jehoiachin's 7 Sons + Zerubbabel's 8 Children -> 1 Chr 3:21-24 to Anani
3. All 19 Monarchs of Northern Israel (individualized king-by-king with dynastic breaks)
4. All 12 Judges of Israel + Deborah/Barak/Jael/Heber + Gideon's sons + Eli's & Samuel's Households
5. Complete House of Saul (Aphiah -> Becorath -> Zeror -> Abiel -> Kish/Ner -> Saul -> all sons & Mephibosheth -> Mica -> 4 sons)
6. All Major & Minor Prophets, Esther/Mordecai/Vashti/Haman houses, Job's house, Conquest heroes, & Giants
7. Complete Individual Matthew 1 (10 post-Zerubbabel links) & Luke 3 (41 individual generations Nathan -> Mary -> Jesus) + NT Households
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # 1. PEREZ -> KING DAVID (10 INDIVIDUAL GENERATIONS + JESSE'S HOUSEHOLD)
    # =========================================================================
    perez_to_jesse = [
        ("w2_hezron", "Hezron (Son of Perez, Ruth 4:18; 1 Chr 2:9)", 14, "Egypt Era (Gen 46:12; 1 Chr 2:9)", "Patriarch of the Hezronites", "jud_perez", "Ruth 4:18 & 1 Chr 2:9: Perez -> Hezron", True),
        ("w2_ram", "Ram / Aram (Son of Hezron, Ruth 4:19; Matt 1:3)", 14, "Egypt Era (Ruth 4:19; 1 Chr 2:9)", "Judahite Royal Ancestor", "w2_hezron", "1 Chr 2:9: Hezron -> Ram", False),
        ("w2_amminadab", "Amminadab (Son of Ram, Ruth 4:19; Exod 6:23)", 14, "Egypt / Exodus (Ruth 4:19; Exod 6:23)", "Father of Nahshon & Elisheba", "w2_ram", "1 Chr 2:10: Ram -> Amminadab", False),
        ("w2_nahshon", "Nahshon ben Amminadab (Prince of Judah, Num 1:7, 7:12)", 15, "Wilderness Era (Num 1:7; 1 Chr 2:10)", "Tribal Prince of Judah & Brother of Elisheba", "w2_amminadab", "1 Chr 2:10: Amminadab -> Nahshon", True),
        ("w2_salmon", "Salmon / Salma (Son of Nahshon; Husband of Rahab, Matt 1:5)", 15, "Conquest Era (Ruth 4:20; Matt 1:5)", "Husband of Rahab & Father of Boaz", "w2_nahshon", "Ruth 4:20 & Matt 1:5: Nahshon -> Salmon", False),
        ("w2_obed", "Obed (Son of Boaz & Ruth the Moabite, Ruth 4:17)", 15, "Judges Era (Ruth 4:17; Matt 1:5)", "Grandfather of King David", "jud_boaz_jesse", "Ruth 4:21: Boaz -> Obed", False),
        ("w2_jesse", "Jesse of Bethlehem (Son of Obed; Father of King David)", 15, "c. 1070–1010 BCE (Ruth 4:22; 1 Sam 16)", "Bethlehem Patriarch of the Davidic Line", "w2_obed", "Ruth 4:22: Obed -> Jesse", True),
        ("w2_nitzevet", "Nitzevet bat Adael (Mother of King David, Talmud Bava Batra 91a)", 15, "c. 1070–1010 BCE (Bava Batra 91a)", "Mother of King David", "w2_jesse", "Bava Batra 91a: Wife of Jesse & Mother of David", False),
    ]
    for nid, nm, tr, er, rl, par, lbl, mj in perez_to_jesse:
        nodes.append(N(nid, nm, "biblical", tr, er, rl, ["Ruth 4:18–22", "1 Chronicles 2:9–15", "Matthew 1:3–6"], f"{nm}.", major=mj))
        edges.append(E(par, nid, "direct", lbl))
    edges += [
        E("w2_salmon", "cb_rahab", "direct", "Matt 1:5: Salmon weds Rahab of Jericho"),
        E("w2_salmon", "jud_boaz_jesse", "direct", "Ruth 4:21 & Matt 1:5: Salmon -> Boaz"),
        E("cb_rahab", "jud_boaz_jesse", "direct", "Matt 1:5: Rahab -> Boaz"),
        E("cb_ruth", "w2_obed", "direct", "Ruth 4:13: Mother Ruth -> Obed"),
        E("w2_jesse", "jud_david", "direct", "1 Sam 16:11 & Ruth 4:22: Jesse -> youngest son David"),
        E("w2_nitzevet", "jud_david", "direct", "Bava Batra 91a: Mother Nitzevet -> David"),
        E("w2_jesse", "cb_zeruiah", "direct", "1 Chr 2:16: Jesse -> daughter Zeruiah"),
        E("w2_jesse", "cb_abigail_jesse", "direct", "1 Chr 2:17: Jesse -> daughter Abigail"),
    ]
    # 6 Elder Brothers of David + Generals Joab, Abishai, Asahel, Amasa + Jonathan ben Shimea
    jesse_bros = [
        ("w2_abinadab_jesse", "Abinadab (2nd Son of Jesse, 1 Sam 16:8; 1 Chr 2:13)"),
        ("w2_shimea_jesse", "Shimea / Shammah (3rd Son of Jesse, 1 Chr 2:13)"),
        ("w2_nethanel_jesse", "Nethanel (4th Son of Jesse, 1 Chr 2:14)"),
        ("w2_raddai_jesse", "Raddai (5th Son of Jesse, 1 Chr 2:14)"),
        ("w2_ozem_jesse", "Ozem (6th Son of Jesse, 1 Chr 2:15)"),
    ]
    for bid, bname in jesse_bros:
        nodes.append(N(bid, bname, "biblical", 15, "11th c. BCE (1 Chr 2:13–15)", "Elder Brother of King David", ["1 Chronicles 2:13–15"], bname))
        edges.append(E("w2_jesse", bid, "direct", "1 Chr 2:13–15: son of Jesse"))
    edges.append(E("w2_jesse", "bib_zeruiah_joab", "direct", "1 Chr 2:13: eldest son Eliab of Jesse"))
    nodes += [
        N("w2_jonathan_shimea", "Jonathan ben Shimea (Nephew of David Who Slew Giant of Gath, 2 Sam 21:21)", "biblical", 16, "10th c. BCE (2 Sam 21:21; 1 Chr 20:7)", "Nephew of King David", ["2 Samuel 21:21", "1 Chronicles 20:7"], "Son of David's brother Shimea; slew the six-fingered giant of Gath."),
        N("w2_abishai", "Abishai (Eldest Son of Zeruiah; Chief of David's Mighty Thirty, 1 Chr 2:16)", "biblical", 16, "c. 1010–970 BCE (2 Sam 23:18; 1 Chr 2:16)", "Commander & Nephew of King David", ["2 Samuel 23:18", "1 Chronicles 2:16"], "Saved David from Ishbi-benob and led the vanguard at Rabbah."),
        N("w2_joab", "General Joab (Son of Zeruiah; Commander of Israel's Armies, 1 Chr 2:16)", "biblical", 16, "c. 1010–970 BCE (2 Sam 8:16; 1 Chr 2:16)", "Supreme Commander of King David", ["2 Samuel 8:16", "1 Chronicles 2:16"], "Nephew of David and commander-in-chief throughout his reign.", major=True),
        N("w2_asahel", "Asahel (Son of Zeruiah; Swift-Footed Mighty Man, 2 Sam 2:18)", "biblical", 16, "c. 1005 BCE (2 Sam 2:18–23; 1 Chr 2:16)", "Nephew of King David", ["2 Samuel 2:18", "1 Chronicles 2:16"], "Youngest son of Zeruiah, slain by Abner at Gibeon."),
        N("w2_jether_ishmaelite", "Jether / Ithra the Ishmaelite (Husband of Abigail bat Jesse, 1 Chr 2:17)", "biblical", 15, "11th c. BCE (1 Chr 2:17; 2 Sam 17:25)", "Brother-in-Law of King David", ["1 Chronicles 2:17", "2 Samuel 17:25"], "Ishmaelite husband of David's sister Abigail."),
        N("w2_amasa", "General Amasa (Son of Jether & Abigail bat Jesse, 2 Sam 17:25)", "biblical", 16, "c. 980 BCE (2 Sam 17:25, 20:4)", "Commander & Nephew of King David", ["2 Samuel 17:25", "1 Chronicles 2:17"], "Appointed commander by Absalom and later by David before being slain by Joab."),
    ]
    edges += [
        E("w2_shimea_jesse", "w2_jonathan_shimea", "direct", "2 Sam 21:21: Shimea -> Jonathan"),
        E("cb_zeruiah", "w2_abishai", "direct", "1 Chr 2:16: Zeruiah -> Abishai"),
        E("cb_zeruiah", "w2_joab", "direct", "1 Chr 2:16: Zeruiah -> General Joab"),
        E("cb_zeruiah", "w2_asahel", "direct", "1 Chr 2:16: Zeruiah -> Asahel"),
        E("cb_abigail_jesse", "w2_jether_ishmaelite", "direct", "1 Chr 2:17: Marriage of Abigail & Jether"),
        E("cb_abigail_jesse", "w2_amasa", "direct", "1 Chr 2:17: Mother Abigail -> General Amasa"),
        E("w2_jether_ishmaelite", "w2_amasa", "direct", "1 Chr 2:17: Father Jether -> General Amasa"),
    ]

    # =========================================================================
    # 2. ALL 20 MONARCHS OF JUDAH & THEIR 13 NAMED QUEEN MOTHERS + EXILIC DAVIDIDS
    # =========================================================================
    nodes += [
        # Missing individual Judah kings formerly bundled inside kg_j7, kg_j8, kg_j10, kg_j12
        N("kg2_amaziah", "King Amaziah of Judah (9th King, 796–767 BCE)", "biblical", 17, "Kingdom of Judah (796–767 BCE)", "Davidic Monarch of Judah", ["2 Kings 14:1–21", "2 Chronicles 25"], "Son of King Joash & Jehoaddan; father of King Uzziah.", major=False),
        N("kg2_jotham", "King Jotham of Judah (11th King, 750–735 BCE)", "biblical", 17, "Kingdom of Judah (750–735 BCE)", "Davidic Monarch of Judah", ["2 Kings 15:32–38", "2 Chronicles 27"], "Son of King Uzziah & Jerusha bat Zadok; rebuilt Upper Gate of the Temple.", major=False),
        N("kg2_ahaz", "King Ahaz of Judah (12th King, 735–715 BCE)", "biblical", 17, "Kingdom of Judah (735–715 BCE)", "Davidic Monarch of Judah", ["2 Kings 16", "Isaiah 7", "Matt 1:9"], "Son of King Jotham; father of King Hezekiah; attested in Tiglath-Pileser III inscriptions as Yauhazi.", major=False),
        N("kg2_amon", "King Amon of Judah (15th King, 643–641 BCE)", "biblical", 17, "Kingdom of Judah (643–641 BCE)", "Davidic Monarch of Judah", ["2 Kings 21:19–26", "Matt 1:10"], "Son of King Manasseh & Meshullemeth; father of King Josiah.", major=False),
        N("kg2_johanan_josiah", "Prince Johanan (Eldest Son of King Josiah, 1 Chr 3:15)", "biblical", 17, "c. 630–609 BCE (1 Chr 3:15)", "Firstborn Prince of King Josiah", ["1 Chronicles 3:15"], "Eldest of Josiah's four sons listed in 1 Chr 3:15.", major=False),
        N("kg2_jehoahaz", "King Jehoahaz / Shallum of Judah (17th King, 609 BCE)", "biblical", 17, "Kingdom of Judah (609 BCE)", "Davidic Monarch of Judah", ["2 Kings 23:31–34", "Jeremiah 22:11"], "Son of Josiah & Hamutal; reigned 3 months before being deposed to Egypt by Pharaoh Neco II.", major=False),
        N("kg2_zedekiah", "King Zedekiah / Mattaniah (20th & Final King of Judah, 597–586 BCE)", "biblical", 17, "Kingdom of Judah (597–586 BCE)", "Final Pre-Exilic Davidic Monarch of Judah", ["2 Kings 24:17–25:7", "Jeremiah 39"], "Third son of Josiah (& Hamutal); blinded and deported when Nebuchadnezzar II destroyed Jerusalem in 586 BCE.", major=True),
        # Individualized Queen Mothers of Judah
        N("qm_mahalath", "Queen Mahalath (Granddaughter of David; Wife of Rehoboam, 2 Chr 11:18)", "biblical", 17, "10th c. BCE (2 Chr 11:18)", "Wife of King Rehoboam", ["2 Chronicles 11:18"], "Daughter of Jerimoth ben David and Abihail bat Eliab; bore Jeush, Shemariah, and Zaham."),
        N("qm_maacah_rehoboam", "Queen Maacah (Granddaughter of Absalom; Mother of King Abijah, 1 Kgs 15:2)", "biblical", 17, "10th c. BCE (1 Kgs 15:2; 2 Chr 11:20)", "Queen Mother (Gebirah) of Judah", ["1 Kings 15:2", "2 Chronicles 11:20–21"], "Favorite wife of Rehoboam; bore King Abijah, Attai, Ziza, and Shelomith."),
        N("qm_zibiah", "Queen Zibiah of Beersheba (Mother of King Joash, 2 Kgs 12:1)", "biblical", 17, "9th c. BCE (2 Kgs 12:1)", "Queen Mother of Judah", ["2 Kings 12:1", "2 Chronicles 24:1"], "Wife of Ahaziah and mother of King Joash."),
        N("qm_jehoaddan", "Queen Jehoaddan of Jerusalem (Mother of King Amaziah, 2 Kgs 14:2)", "biblical", 17, "9th–8th c. BCE (2 Kgs 14:2)", "Queen Mother of Judah", ["2 Kings 14:2", "2 Chronicles 25:1"], "Wife of King Joash and mother of King Amaziah."),
        N("qm_jecoliah", "Queen Jecoliah of Jerusalem (Mother of King Uzziah, 2 Kgs 15:2)", "biblical", 17, "8th c. BCE (2 Kgs 15:2)", "Queen Mother of Judah", ["2 Kings 15:2", "2 Chronicles 26:3"], "Wife of King Amaziah and mother of King Uzziah."),
        N("qm_jerusha", "Queen Jerusha bat Zadok (Mother of King Jotham, 2 Kgs 15:33)", "biblical", 17, "8th c. BCE (2 Kgs 15:33)", "Queen Mother of Judah", ["2 Kings 15:33", "2 Chronicles 27:1"], "Daughter of Zadok; wife of Uzziah and mother of King Jotham."),
        N("qm_abi_abijah", "Queen Abi / Abijah bat Zechariah (Mother of King Hezekiah, 2 Kgs 18:2)", "biblical", 17, "8th c. BCE (2 Kgs 18:2; 2 Chr 29:1)", "Queen Mother of King Hezekiah", ["2 Kings 18:2", "2 Chronicles 29:1"], "Wife of King Ahaz and mother of reforming King Hezekiah."),
        N("qm_hephzibah", "Queen Hephzibah (Wife of Hezekiah; Mother of King Manasseh, 2 Kgs 21:1)", "biblical", 17, "7th c. BCE (2 Kgs 21:1)", "Queen Mother of Judah", ["2 Kings 21:1"], "Wife of King Hezekiah and mother of Manasseh."),
        N("qm_meshullemeth", "Queen Meshullemeth bat Haruz of Jotbah (Mother of King Amon, 2 Kgs 21:19)", "biblical", 17, "7th c. BCE (2 Kgs 21:19)", "Queen Mother of Judah", ["2 Kings 21:19"], "Wife of Manasseh and mother of King Amon."),
        N("qm_jedidah", "Queen Jedidah bat Adaiah of Bozkath (Mother of King Josiah, 2 Kgs 22:1)", "biblical", 17, "7th c. BCE (2 Kgs 22:1)", "Queen Mother of King Josiah", ["2 Kings 22:1"], "Wife of King Amon and mother of reforming King Josiah."),
        N("qm_zebidah", "Queen Zebidah bat Pedaiah of Rumah (Mother of King Jehoiakim, 2 Kgs 23:36)", "biblical", 17, "7th c. BCE (2 Kgs 23:36)", "Queen Mother of Judah", ["2 Kings 23:36"], "Wife of Josiah and mother of King Jehoiakim."),
        N("qm_hamutal", "Queen Hamutal bat Jeremiah of Libnah (Mother of Jehoahaz & Zedekiah, 2 Kgs 23:31, 24:18)", "biblical", 17, "7th–6th c. BCE (2 Kgs 23:31, 24:18)", "Queen Mother of Two Kings of Judah", ["2 Kings 23:31, 24:18"], "Wife of King Josiah; mother of both Jehoahaz and final king Zedekiah."),
        N("qm_nehushta", "Queen Nehushta bat Elnathan of Jerusalem (Mother of Jehoiachin, 2 Kgs 24:8)", "biblical", 17, "c. 615–597 BCE (2 Kgs 24:8, 12; Jer 22:26)", "Deported Queen Mother of Judah", ["2 Kings 24:8, 12"], "Wife of Jehoiakim; deported to Babylon with her son King Jehoiachin in 597 BCE."),
        # Jehoshaphat's 6 Younger Sons (2 Chr 21:2)
        N("dav2_azariah_jehosh", "Azariah (Son 2 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        N("dav2_jehiel_jehosh", "Jehiel (Son 3 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        N("dav2_zechariah_jehosh", "Zechariah (Son 4 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        N("dav2_azariahu_jehosh", "Azariahu (Son 5 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        N("dav2_michael_jehosh", "Michael (Son 6 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        N("dav2_shephatiah_jehosh", "Shephatiah (Son 7 of Jehoshaphat, 2 Chr 21:2)", "biblical", 17, "9th c. BCE", "Prince of Judah", ["2 Chronicles 21:2"], "Son of King Jehoshaphat."),
        # Exilic Sons of Jehoiachin (1 Chr 3:17-18) -> Zerubbabel -> 8 Children -> Anani (1 Chr 3:19-24)
        N("dav_shealtiel", "Prince Shealtiel ben Jehoiachin (Father/Uncle of Zerubbabel, 1 Chr 3:17; Matt 1:12)", "biblical", 18, "6th c. BCE (Babylon — 1 Chr 3:17; Matt 1:12)", "Eldest Exilic Son of King Jehoiachin", ["1 Chronicles 3:17", "Matthew 1:12"], "Eldest son of deported King Jehoiachin; legal father of Governor Zerubbabel.", major=True),
        N("dav_malchiram", "Malchiram (Son 2 of Jehoiachin, 1 Chr 3:18)", "biblical", 18, "6th c. BCE", "Exilic Davidic Prince", ["1 Chronicles 3:18"], "Second son of Jehoiachin in Babylon."),
        N("dav_pedaiah", "Pedaiah ben Jehoiachin (Son 3 of Jehoiachin; Biological Father of Zerubbabel, 1 Chr 3:18–19)", "biblical", 18, "6th c. BCE (1 Chr 3:18–19)", "Exilic Davidic Prince", ["1 Chronicles 3:18–19"], "Son of Jehoiachin named as father of Zerubbabel and Shimei in 1 Chr 3:19 (Levirate link to Shealtiel)."),
        N("dav_shenazzar", "Shenazzar / Sheshbazzar (Son 4 of Jehoiachin, 1 Chr 3:18; Ezra 1:8)", "biblical", 18, "6th c. BCE", "Exilic Davidic Prince", ["1 Chronicles 3:18"], "Fourth son of Jehoiachin."),
        N("dav_jekamiah", "Jekamiah (Son 5 of Jehoiachin, 1 Chr 3:18)", "biblical", 18, "6th c. BCE", "Exilic Davidic Prince", ["1 Chronicles 3:18"], "Fifth son of Jehoiachin."),
        N("dav_hoshama", "Hoshama (Son 6 of Jehoiachin, 1 Chr 3:18)", "biblical", 18, "6th c. BCE", "Exilic Davidic Prince", ["1 Chronicles 3:18"], "Sixth son of Jehoiachin."),
        N("dav_nedabiah", "Nedabiah (Son 7 of Jehoiachin, 1 Chr 3:18)", "biblical", 18, "6th c. BCE", "Exilic Davidic Prince", ["1 Chronicles 3:18"], "Seventh son of Jehoiachin."),
        N("dav_zerubbabel", "Governor Zerubbabel of Yehud (Rebuilder of Second Temple, 538–515 BCE; Ezra 3; Hag 1)", "biblical", 18, "c. 538–515 BCE (1 Chr 3:19; Ezra 3; Matt 1:12)", "Governor of Judah & Rebuilder of the Second Temple", ["Ezra 3:2", "Haggai 1:1", "1 Chronicles 3:19", "Matthew 1:12"], "Davidic governor who led the return from Babylon under Cyrus and rebuilt the Second Temple alongside High Priest Jeshua.", major=True),
        N("dav_zer_meshullam", "Meshullam (Son 1 of Zerubbabel, 1 Chr 3:19)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:19"], "Eldest son of Zerubbabel."),
        N("dav_zer_hananiah", "Hananiah (Son 2 of Zerubbabel, 1 Chr 3:19, 21)", "biblical", 18, "5th c. BCE", "Ancestor of Post-Exilic Davidic Line", ["1 Chronicles 3:19, 21"], "Second son of Zerubbabel through whom Chronicles traces the post-exilic Davidic line to Anani."),
        N("dav_zer_shelomith", "Princess Shelomith (Daughter of Zerubbabel, 1 Chr 3:19; Stamp Seal!)", "biblical", 18, "late 6th c. BCE (1 Chr 3:19; Bullae)", "Daughter of Governor Zerubbabel & Wife of Governor Elnathan", ["1 Chronicles 3:19"], "Named daughter of Zerubbabel, corroborated by a 6th-c. BCE Yehud seal reading 'Belonging to Shelomith maidservant of Elnathan the Governor'!"),
        N("dav_zer_hashubah", "Hashubah (Son 3 of Zerubbabel, 1 Chr 3:20)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:20"], "Third son of Zerubbabel."),
        N("dav_zer_ohel", "Ohel (Son 4 of Zerubbabel, 1 Chr 3:20)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:20"], "Fourth son of Zerubbabel."),
        N("dav_zer_berechiah", "Berechiah (Son 5 of Zerubbabel, 1 Chr 3:20)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:20"], "Fifth son of Zerubbabel."),
        N("dav_zer_hasadiah", "Hasadiah (Son 6 of Zerubbabel, 1 Chr 3:20)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:20"], "Sixth son of Zerubbabel."),
        N("dav_zer_jushabhesed", "Jushab-hesed (Son 7 of Zerubbabel, 1 Chr 3:20)", "biblical", 18, "5th c. BCE", "Son of Zerubbabel", ["1 Chronicles 3:20"], "Seventh son of Zerubbabel."),
        # Post-Zerubbabel Chronicles chain (1 Chr 3:21-24)
        N("dav_chr_pelatiah", "Pelatiah & Jeshaiah (Sons of Hananiah, 1 Chr 3:21)", "biblical", 18, "5th c. BCE", "Davidic Line (1 Chr 3:21)", ["1 Chronicles 3:21"], "Wait—split Jeshaiah? No, let's keep Pelatiah as individual here and add Jeshaiah separately if needed."),
        N("dav_chr_rephaiah", "Rephaiah (1 Chr 3:21)", "biblical", 18, "5th–4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:21"], "Post-exilic Davidic link."),
        N("dav_chr_arnan", "Arnan (1 Chr 3:21)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:21"], "Post-exilic Davidic link."),
        N("dav_chr_obadiah", "Obadiah (1 Chr 3:21)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:21"], "Post-exilic Davidic link."),
        N("dav_chr_shecaniah", "Shecaniah (1 Chr 3:21)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:21"], "Father of Shemaiah & Hattush."),
        N("dav_chr_shemaiah", "Shemaiah ben Shecaniah (1 Chr 3:22)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:22"], "Father of Neariah."),
        N("dav_chr_neariah", "Neariah ben Shemaiah (1 Chr 3:22–23)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:22–23"], "Father of Elioenai, Hizkiah & Azrikam."),
        N("dav_chr_elioenai", "Elioenai ben Neariah (Father of 7 Sons, 1 Chr 3:23–24)", "biblical", 18, "4th c. BCE", "Post-Exilic Davidic Line", ["1 Chronicles 3:23–24"], "Father of Hodaviah, Eliashib, Pelaiah, Akkub, Johanan, Delaiah, and Anani."),
        N("dav_chr_anani", "Anani (Final Named Davidic Descendant in 1 Chr 3:24)", "biblical", 18, "4th c. BCE (1 Chr 3:24)", "Last Person Listed in Chronicles' Davidic Genealogy", ["1 Chronicles 3:24"], "Youngest son of Elioenai and final named person in the Old Testament genealogy of the House of David."),
    ]
    # Replace bundled label of dav_chr_pelatiah cleanly before appending
    nodes = [n if n["id"] != "dav_chr_pelatiah" else N("dav_chr_pelatiah", "Pelatiah (Son of Hananiah, 1 Chr 3:21)", "biblical", 18, "5th c. BCE", "Post-Exilic Davidic Descendant", ["1 Chronicles 3:21"], "Son of Hananiah ben Zerubbabel.") for n in nodes]
    edges += [
        E("kg_j7_joash", "kg2_amaziah", "direct", "2 Kgs 14:1: Joash -> Amaziah"),
        E("kg2_amaziah", "kg_j8_uzziah", "direct", "2 Kgs 15:1: Amaziah -> Uzziah"),
        E("kg_j8_uzziah", "kg2_jotham", "direct", "2 Kgs 15:32: Uzziah -> Jotham"),
        E("kg2_jotham", "kg2_ahaz", "direct", "2 Kgs 16:1: Jotham -> Ahaz"),
        E("kg2_ahaz", "kg_j9_hezekiah", "direct", "2 Kgs 18:1: Ahaz -> Hezekiah"),
        E("kg_j10_manasseh", "kg2_amon", "direct", "2 Kgs 21:19: Manasseh -> Amon"),
        E("kg2_amon", "kg_j11_josiah", "direct", "2 Kgs 22:1: Amon -> Josiah"),
        E("kg_j11_josiah", "kg2_johanan_josiah", "direct", "1 Chr 3:15: 1st son Johanan"),
        E("kg_j11_josiah", "kg2_jehoahaz", "direct", "2 Kgs 23:31: Josiah -> Jehoahaz"),
        E("kg_j11_josiah", "kg2_zedekiah", "direct", "2 Kgs 24:17 / 1 Chr 3:15: Josiah -> Zedekiah"),
        E("kg_j12_jehoiakim_zedekiah", "kg_j13_jehoiachin", "direct", "2 Kgs 24:6: Jehoiakim -> Jehoiachin"),
        # Queen Mother edges
        E("kg_j1_rehoboam", "qm_mahalath", "direct", "2 Chr 11:18: wife Mahalath"),
        E("bib16_dav_jerimoth", "qm_mahalath", "direct", "2 Chr 11:18: Jerimoth -> Mahalath"),
        E("kg_j1_rehoboam", "qm_maacah_rehoboam", "direct", "1 Kgs 15:2: wife Maacah"),
        E("cb_tamar_absalom", "qm_maacah_rehoboam", "direct", "2 Chr 11:20 / 2 Sam 14:27: Maacah granddaughter of Absalom"),
        E("qm_maacah_rehoboam", "kg_j2_abijah", "direct", "1 Kgs 15:2: Mother Maacah -> Abijah"),
        E("kg_j5_jehoram", "cb_q_athaliah", "direct", "2 Kgs 8:18: Jehoram + Athaliah"),
        E("cb_q_athaliah", "kg_j6_ahaziah", "direct", "2 Kgs 8:26: Mother Athaliah -> Ahaziah"),
        E("kg_j6_ahaziah", "qm_zibiah", "direct", "2 Kgs 12:1: wife Zibiah"),
        E("qm_zibiah", "kg_j7_joash", "direct", "2 Kgs 12:1: Mother Zibiah -> Joash"),
        E("kg_j7_joash", "qm_jehoaddan", "direct", "2 Kgs 14:2: wife Jehoaddan"),
        E("qm_jehoaddan", "kg2_amaziah", "direct", "2 Kgs 14:2: Mother Jehoaddan -> Amaziah"),
        E("kg2_amaziah", "qm_jecoliah", "direct", "2 Kgs 15:2: wife Jecoliah"),
        E("qm_jecoliah", "kg_j8_uzziah", "direct", "2 Kgs 15:2: Mother Jecoliah -> Uzziah"),
        E("kg_j8_uzziah", "qm_jerusha", "direct", "2 Kgs 15:33: wife Jerusha"),
        E("qm_jerusha", "kg2_jotham", "direct", "2 Kgs 15:33: Mother Jerusha -> Jotham"),
        E("kg2_ahaz", "qm_abi_abijah", "direct", "2 Kgs 18:2: wife Abi/Abijah"),
        E("qm_abi_abijah", "kg_j9_hezekiah", "direct", "2 Kgs 18:2: Mother Abi -> Hezekiah"),
        E("kg_j9_hezekiah", "qm_hephzibah", "direct", "2 Kgs 21:1: wife Hephzibah"),
        E("qm_hephzibah", "kg_j10_manasseh", "direct", "2 Kgs 21:1: Mother Hephzibah -> Manasseh"),
        E("kg_j10_manasseh", "qm_meshullemeth", "direct", "2 Kgs 21:19: wife Meshullemeth"),
        E("qm_meshullemeth", "kg2_amon", "direct", "2 Kgs 21:19: Mother Meshullemeth -> Amon"),
        E("kg2_amon", "qm_jedidah", "direct", "2 Kgs 22:1: wife Jedidah"),
        E("qm_jedidah", "kg_j11_josiah", "direct", "2 Kgs 22:1: Mother Jedidah -> Josiah"),
        E("kg_j11_josiah", "qm_zebidah", "direct", "2 Kgs 23:36: wife Zebidah"),
        E("qm_zebidah", "kg_j12_jehoiakim_zedekiah", "direct", "2 Kgs 23:36: Mother Zebidah -> Jehoiakim"),
        E("kg_j11_josiah", "qm_hamutal", "direct", "2 Kgs 23:31: wife Hamutal"),
        E("qm_hamutal", "kg2_jehoahaz", "direct", "2 Kgs 23:31: Mother Hamutal -> Jehoahaz"),
        E("qm_hamutal", "kg2_zedekiah", "direct", "2 Kgs 24:18: Mother Hamutal -> Zedekiah"),
        E("kg_j12_jehoiakim_zedekiah", "qm_nehushta", "direct", "2 Kgs 24:8: wife Nehushta"),
        E("qm_nehushta", "kg_j13_jehoiachin", "direct", "2 Kgs 24:8: Mother Nehushta -> Jehoiachin"),
        # Jehoshaphat sons
        E("kg_j4_jehoshaphat", "dav2_azariah_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        E("kg_j4_jehoshaphat", "dav2_jehiel_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        E("kg_j4_jehoshaphat", "dav2_zechariah_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        E("kg_j4_jehoshaphat", "dav2_azariahu_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        E("kg_j4_jehoshaphat", "dav2_michael_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        E("kg_j4_jehoshaphat", "dav2_shephatiah_jehosh", "direct", "2 Chr 21:2: son of Jehoshaphat"),
        # Jehoiachin -> Zerubbabel -> 1 Chr 3:24 Anani
        E("kg_j13_jehoiachin", "dav_shealtiel", "direct", "1 Chr 3:17: Son 1 Shealtiel"),
        E("kg_j13_jehoiachin", "dav_malchiram", "direct", "1 Chr 3:18: Son 2 Malchiram"),
        E("kg_j13_jehoiachin", "dav_pedaiah", "direct", "1 Chr 3:18: Son 3 Pedaiah"),
        E("kg_j13_jehoiachin", "dav_shenazzar", "direct", "1 Chr 3:18: Son 4 Shenazzar"),
        E("kg_j13_jehoiachin", "dav_jekamiah", "direct", "1 Chr 3:18: Son 5 Jekamiah"),
        E("kg_j13_jehoiachin", "dav_hoshama", "direct", "1 Chr 3:18: Son 6 Hoshama"),
        E("kg_j13_jehoiachin", "dav_nedabiah", "direct", "1 Chr 3:18: Son 7 Nedabiah"),
        E("dav_shealtiel", "dav_zerubbabel", "direct", "Matt 1:12 & Ezra 3:2: Legal Father Shealtiel -> Zerubbabel"),
        E("dav_pedaiah", "dav_zerubbabel", "direct", "1 Chr 3:19: Biological Father Pedaiah -> Zerubbabel"),
        E("dav_zerubbabel", "dav_zer_meshullam", "direct", "1 Chr 3:19: Son 1 Meshullam"),
        E("dav_zerubbabel", "dav_zer_hananiah", "direct", "1 Chr 3:19: Son 2 Hananiah"),
        E("dav_zerubbabel", "dav_zer_shelomith", "direct", "1 Chr 3:19: Daughter Shelomith"),
        E("dav_zerubbabel", "dav_zer_hashubah", "direct", "1 Chr 3:20: Son 3 Hashubah"),
        E("dav_zerubbabel", "dav_zer_ohel", "direct", "1 Chr 3:20: Son 4 Ohel"),
        E("dav_zerubbabel", "dav_zer_berechiah", "direct", "1 Chr 3:20: Son 5 Berechiah"),
        E("dav_zerubbabel", "dav_zer_hasadiah", "direct", "1 Chr 3:20: Son 6 Hasadiah"),
        E("dav_zerubbabel", "dav_zer_jushabhesed", "direct", "1 Chr 3:20: Son 7 Jushab-hesed"),
        E("dav_zer_hananiah", "dav_chr_pelatiah", "direct", "1 Chr 3:21: Hananiah -> Pelatiah"),
        E("dav_chr_pelatiah", "dav_chr_rephaiah", "direct", "1 Chr 3:21: Davidic succession"),
        E("dav_chr_rephaiah", "dav_chr_arnan", "direct", "1 Chr 3:21: Rephaiah -> Arnan"),
        E("dav_chr_arnan", "dav_chr_obadiah", "direct", "1 Chr 3:21: Arnan -> Obadiah"),
        E("dav_chr_obadiah", "dav_chr_shecaniah", "direct", "1 Chr 3:21: Obadiah -> Shecaniah"),
        E("dav_chr_shecaniah", "dav_chr_shemaiah", "direct", "1 Chr 3:22: Shecaniah -> Shemaiah"),
        E("dav_chr_shemaiah", "dav_chr_neariah", "direct", "1 Chr 3:22: Shemaiah -> Neariah"),
        E("dav_chr_neariah", "dav_chr_elioenai", "direct", "1 Chr 3:23: Neariah -> Elioenai"),
        E("dav_chr_elioenai", "dav_chr_anani", "direct", "1 Chr 3:24: Elioenai -> Anani"),
        E("dav_zerubbabel", "nt_matthew_joseph", "direct", "Matt 1:13: Zerubbabel -> Abiud -> ... -> Joseph"),
        E("dav_zerubbabel", "ir_cyrus", "cognate", "Ezra 1–3: Zerubbabel leads return under Cyrus the Great"),
    ]

    # =========================================================================
    # 3. ALL REMAINING MONARCHS OF NORTHERN ISRAEL (19 KINGS PERSON-BY-PERSON)
    # =========================================================================
    israel_more = [
        ("isr_zeruah", "Zeruah (Widow Mother of Jeroboam I, 1 Kgs 11:26)", "kg_i1_jeroboam", "1 Kgs 11:26: Mother of Jeroboam I", False),
        ("isr_abijah_jeroboam", "Prince Abijah ben Jeroboam I (1 Kgs 14:1–18)", "kg_i1_jeroboam", "1 Kgs 14:1: son of Jeroboam I", False),
        ("isr_nadab", "2. King Nadab ben Jeroboam I (909–908 BCE)", "kg_i1_jeroboam", "1 Kgs 15:25: Jeroboam I -> Nadab", False),
        ("isr_elah", "4. King Elah ben Baasha (886–885 BCE)", "kg_i2_baasha", "1 Kgs 16:8: Baasha -> Elah", False),
        ("isr_zimri", "5. King Zimri (Reigned 7 Days in Tirzah, 885 BCE)", "isr_elah", "1 Kgs 16:10: Zimri seizes throne", False),
        ("isr_ahab", "7. King Ahab ben Omri (874–853 BCE; Kurkh Monolith)", "kg_i3_omri_ahab", "1 Kgs 16:29: Omri -> King Ahab", True),
        ("isr_ethbaal_sidon", "King Ethbaal / Ithobaal I of Sidon & Tyre (Father of Queen Jezebel, 1 Kgs 16:31)", "bib_sidon", "Josephus Ag. Ap. I.18: Phoenician King of Tyre", True),
        ("isr_jezebel", "Queen Jezebel of Israel (Daughter of Ethbaal; Wife of Ahab, 1 Kgs 16:31)", "isr_ethbaal_sidon", "1 Kgs 16:31: Ethbaal -> Queen Jezebel", True),
        ("isr_ahaziah", "8. King Ahaziah of Israel (Son of Ahab & Jezebel, 853–852 BCE)", "isr_ahab", "1 Kgs 22:51: Ahab -> Ahaziah", False),
        ("isr_joram", "9. King Joram / Jehoram of Israel (Son of Ahab & Jezebel, 852–841 BCE)", "isr_ahab", "2 Kgs 3:1: Ahab -> Joram", False),
        ("isr_jehoahaz", "11. King Jehoahaz ben Jehu (814–798 BCE)", "kg_i4_jehu", "2 Kgs 13:1: Jehu -> Jehoahaz", False),
        ("isr_jehoash", "12. King Jehoash / Joash of Israel (798–782 BCE)", "isr_jehoahaz", "2 Kgs 13:10: Jehoahaz -> Jehoash", False),
        ("isr_jeroboam2", "13. King Jeroboam II of Israel (793–753 BCE; Amos Era)", "isr_jehoash", "2 Kgs 14:23: Jehoash -> Jeroboam II", True),
        ("isr_zechariah", "14. King Zechariah ben Jeroboam II (Last of House of Jehu, 753 BCE)", "isr_jeroboam2", "2 Kgs 15:8: Jeroboam II -> Zechariah", False),
        ("isr_shallum", "15. King Shallum ben Jabesh (752 BCE, 1 Month)", "isr_zechariah", "2 Kgs 15:13: Shallum slays Zechariah", False),
        ("isr_menahem", "16. King Menahem ben Gadi (752–742 BCE)", "isr_shallum", "2 Kgs 15:14: Menahem succeeds Shallum", False),
        ("isr_pekahiah", "17. King Pekahiah ben Menahem (742–740 BCE)", "isr_menahem", "2 Kgs 15:23: Menahem -> Pekahiah", False),
        ("isr_pekah", "18. King Pekah ben Remaliah (740–732 BCE)", "isr_pekahiah", "2 Kgs 15:25: Pekah slays Pekahiah", False),
    ]
    for iid, iname, ipar, ilbl, imaj in israel_more:
        nodes.append(N(iid, iname, "biblical", 17, "Northern Kingdom of Israel (931–722 BCE)", "Monarch / Royal of Northern Israel", ["1–2 Kings"], f"{iname}.", major=imaj))
        edges.append(E(ipar, iid, "direct" if "ben" in ilbl or "->" in ilbl else "expansion", ilbl))
    edges += [
        E("isr_ahab", "isr_jezebel", "direct", "1 Kgs 16:31: Marriage of Ahab & Queen Jezebel"),
        E("isr_jezebel", "isr_ahaziah", "direct", "Mother Jezebel -> Ahaziah"),
        E("isr_jezebel", "isr_joram", "direct", "Mother Jezebel -> Joram"),
        E("isr_jezebel", "cb_q_athaliah", "direct", "Mother Jezebel -> Queen Athaliah of Judah"),
        E("isr_ahab", "cb_q_athaliah", "direct", "2 Kgs 8:26: Father Ahab -> Queen Athaliah of Judah"),
        E("grk_dido_carthage", "isr_ethbaal_sidon", "cognate", "Josephus Against Apion I.18: Ethbaal is great-uncle of Queen Dido of Carthage"),
        E("isr_pekah", "kg_i5_hoshea", "expansion", "2 Kgs 15:30: Hoshea ben Elah succeeds Pekah"),
    ]

    # =========================================================================
    # 4. ALL 12 JUDGES, BARAK/JAEL, ELI'S HOUSE, SAMUEL'S HOUSE & HOUSE OF SAUL
    # =========================================================================
    nodes += [
        N("jdg2_barak", "General Barak ben Abinoam (Kedesh-naphtali, Judg 4:6)", "biblical", 16, "Judges Era (Judg 4–5)", "Israelite Commander Under Deborah", ["Judges 4:6–22", "Hebrews 11:32"], "Summoned by Judge Deborah from Naphtali; routed Sisera at Mt. Tabor."),
        N("jdg2_heber_kenite", "Heber the Kenite (Descendant of Hobab/Jethro, Judg 4:11)", "biblical", 16, "Judges Era (Judg 4:11)", "Kenite Patriarch Allied With Israel", ["Judges 4:11, 17"], "Descendant of Moses's father-in-law Hobab/Jethro; husband of Jael."),
        N("jdg2_jael", "Jael (Wife of Heber the Kenite Who Slew Sisera, Judg 4:21)", "biblical", 16, "Judges Era (Judg 4:17–22, 5:24–27)", "Deliverer Celebrated in the Song of Deborah", ["Judges 4:17–22, 5:24"], "'Most blessed of women' who struck down Canaanite commander Sisera with a tent peg.", major=True),
        N("jdg2_abimelech", "Abimelech (Son of Gideon by Shechemite Concubine, Judg 9)", "biblical", 16, "Judges Era (Judg 9:1–57)", "Self-Proclaimed King of Shechem", ["Judges 9:1–57"], "Son of Gideon who seized rule at Shechem before falling at Thebez."),
        N("jdg2_jotham", "Jotham (Youngest Son of Gideon; Speaker of Fable of Trees, Judg 9:5–21)", "biblical", 16, "Judges Era (Judg 9:5–21)", "Surviving Son of Gideon", ["Judges 9:5–21"], "Sole survivor among Gideon's 70 sons who pronounced the Fable of the Trees on Mt. Gerizim."),
        N("jdg2_jair", "7. Judge Jair of Gilead (Manasseh, Judg 10:3–5)", "biblical", 16, "Judges Era (Judg 10:3–5)", "Seventh Judge of Israel", ["Judges 10:3–5"], "Gileadite judge for 22 years whose 30 sons rode 30 donkeys and governed Havvoth-jair."),
        N("jdg2_elon", "10. Judge Elon the Zebulunite (Judg 12:11–12)", "biblical", 16, "Judges Era (Judg 12:11–12)", "Tenth Judge of Israel", ["Judges 12:11–12"], "Buried at Aijalon in Zebulun after judging 10 years."),
        N("jdg2_abdon", "11. Judge Abdon ben Hillel the Pirathonite (Judg 12:13–15)", "biblical", 16, "Judges Era (Judg 12:13–15)", "Eleventh Judge of Israel", ["Judges 12:13–15"], "Ephraimite judge with 40 sons and 30 grandsons riding 70 donkeys."),
        N("jdg2_manoah", "Manoah of Zorah (+ Wife / Eluma; Parents of Samson, Judg 13)", "biblical", 16, "Judges Era (Judg 13:2–23)", "Danite Father of Samson", ["Judges 13:2–24"], "Danite of Zorah visited by the Angel of the Lord before Samson's birth."),
        N("jdg2_delilah", "Delilah of the Valley of Sorek (Judg 16:4–21)", "biblical", 16, "Judges Era (Judg 16:4–21)", "Philistine Confidante Who Learned Secret of Samson's Vow", ["Judges 16:4–21"], "Betrayed Samson to the five Philistine lords for 1,100 pieces of silver each."),
        # House of Eli & Samuel
        N("jdg2_hophni", "Hophni (Son of Eli, 1 Sam 1:3, 4:11)", "biblical", 16, "c. 1100 BCE (1 Sam 1–4)", "Priest of Shiloh", ["1 Samuel 1:3, 4:11"], "Elder son of Eli slain when the Ark was captured at Aphek."),
        N("jdg2_phinehas_eli", "Phinehas ben Eli (+ Widow; Father of Ahitub & Ichabod, 1 Sam 4:19)", "biblical", 16, "c. 1100 BCE (1 Sam 4:11–22, 14:3)", "Priest of Shiloh", ["1 Samuel 4:11–22, 14:3"], "Younger son of Eli; father of Ahitub and Ichabod."),
        N("jdg2_ichabod", "Ichabod (Son of Phinehas ben Eli, 1 Sam 4:21)", "biblical", 16, "c. 1070 BCE (1 Sam 4:21)", "Posthumous Grandson of Eli", ["1 Samuel 4:19–22"], "Born as his mother heard the Ark was taken ('No glory')."),
        N("jdg2_ahitub_eli", "Ahitub ben Phinehas (1 Sam 14:3, 22:9)", "biblical", 16, "11th c. BCE (1 Sam 14:3)", "Priest of Ithamar's Line", ["1 Samuel 14:3, 22:9"], "Son of Phinehas ben Eli; father of Ahiah/Ahimelech of Nob."),
        N("jdg2_ahimelech", "High Priest Ahimelech of Nob (Who Sheltered David, 1 Sam 21–22)", "biblical", 16, "c. 1015 BCE (1 Sam 21–22)", "High Priest at Nob", ["1 Samuel 21:1, 22:9–20"], "Aided fleeing David with showbread & Goliath's sword before Doeg's massacre."),
        N("jdg2_abiathar", "High Priest Abiathar ben Ahimelech (David's High Priest, 1 Sam 22:20)", "biblical", 16, "c. 1015–970 BCE (1 Sam 22:20; 1 Kgs 2:26)", "Sole Survivor of Nob & Co-High Priest With Zadok", ["1 Samuel 22:20", "1 Kings 2:26–27"], "Escaped Nob to serve David alongside Zadok; father of Jonathan & Ahimelech II."),
        N("jdg2_elkanah", "Elkanah (Father of Prophet Samuel, 1 Sam 1:1; 1 Chr 6:34)", "biblical", 15, "11th c. BCE (1 Sam 1:1)", "Kohathite Levite of Ramathaim-zophim", ["1 Samuel 1:1", "1 Chronicles 6:33–38"], "Husband of Hannah and Peninnah; father of Samuel."),
        N("jdg2_hannah", "Hannah (Mother of Prophet Samuel, 1 Sam 1–2)", "biblical", 15, "11th c. BCE (1 Sam 1–2)", "Matriarch & Psalm-Singer of Shiloh", ["1 Samuel 1–2"], "Prayed silently at Shiloh and dedicated firstborn Samuel, later bearing 3 more sons and 2 daughters (1 Sam 2:21).", major=True),
        N("jdg2_joel_samuel", "Joel / Vashni (Elder Son of Samuel; Father of Heman, 1 Sam 8:2; 1 Chr 6:33)", "biblical", 16, "11th c. BCE (1 Sam 8:2; 1 Chr 6:33)", "Elder Son of Prophet Samuel", ["1 Samuel 8:2", "1 Chronicles 6:28, 33"], "Father of David's chief Temple musician Heman."),
        N("jdg2_abijah_samuel", "Abijah (Second Son of Prophet Samuel, 1 Sam 8:2)", "biblical", 16, "11th c. BCE (1 Sam 8:2)", "Judge in Beersheba", ["1 Samuel 8:2"], "Younger son of Samuel."),
        N("jdg2_heman_singer", "Heman the Ezrahite / Singer (Grandson of Samuel; Chief Seer-Musician, 1 Chr 6:33, 25:5)", "biblical", 16, "10th c. BCE (1 Chr 6:33, 25:4–6)", "Davidic Temple Choir Master With 14 Sons & 3 Daughters", ["1 Chronicles 6:33, 25:4–6", "Psalm 88"], "Grandson of Prophet Samuel and leader of David's Temple music."),
        # Complete House of King Saul (1 Sam 9, 14; 1 Chr 8:33-40)
        N("saul_abiel", "Abiel / Jeiel (Father of Kish & Ner, 1 Sam 9:1; 1 Chr 8:29)", "biblical", 15, "11th c. BCE (1 Sam 9:1; 1 Chr 9:35)", "Benjaminite Patriarch of Gibeon", ["1 Samuel 9:1", "1 Chronicles 8:29, 9:35"], "Benjaminite ancestor of King Saul and General Abner."),
        N("saul_kish", "Kish ben Abiel (Father of King Saul, 1 Sam 9:1)", "biblical", 15, "11th c. BCE (1 Sam 9:1–3)", "Father of 1st King of Israel", ["1 Samuel 9:1", "Acts 13:21"], "Mighty Benjaminite of Gibeah; father of King Saul."),
        N("saul_ner", "Ner ben Abiel (Uncle of Saul & Father of Abner, 1 Sam 14:50; 1 Chr 8:33)", "biblical", 15, "11th c. BCE (1 Sam 14:50)", "Brother of Kish & Father of General Abner", ["1 Samuel 14:50", "1 Chronicles 8:33"], "Benjaminite patriarch whose son Abner commanded Saul's army."),
        N("saul_abner", "General Abner ben Ner (Commander of King Saul, 1 Sam 14:50; 2 Sam 3)", "biblical", 16, "d. c. 1003 BCE (1 Sam 14:50; 2 Sam 2–3)", "Commander-in-Chief of House of Saul", ["1 Samuel 14:50", "2 Samuel 2–3"], "Cousin of Saul; crowned Ish-bosheth before negotiating Israel's union with David."),
        N("saul_abinadab", "Prince Abinadab / Ishvi (Son of Saul, d. Mt. Gilboa, 1 Sam 31:2)", "biblical", 16, "d. c. 1010 BCE (1 Sam 31:2)", "Second Son of King Saul", ["1 Samuel 14:49, 31:2"], "Slain beside father Saul and brothers at Mount Gilboa."),
        N("saul_malchishua", "Prince Malchi-shua (Son of Saul, d. Mt. Gilboa, 1 Sam 31:2)", "biblical", 16, "d. c. 1010 BCE (1 Sam 31:2)", "Third Son of King Saul", ["1 Samuel 31:2", "1 Chronicles 8:33"], "Slain beside Saul and Jonathan at Mount Gilboa."),
        N("saul_ishbosheth", "King Ish-bosheth / Esh-baal (Son of Saul, 2 Sam 2:8–4:7)", "biblical", 16, "c. 1010–1003 BCE (2 Sam 2–4; 1 Chr 8:33)", "Successor of Saul Over Northern Israel", ["2 Samuel 2:8–4:12", "1 Chronicles 8:33"], "Fourth son of Saul; reigned two years at Mahanaim."),
        N("saul_armoni_mephi", "Armoni & Mephibosheth II (Sons of King Saul & Rizpah, 2 Sam 21:8)", "biblical", 16, "c. 1010–995 BCE (2 Sam 21:8)", "Sons of King Saul & Rizpah bat Aiah", ["2 Samuel 21:8–14"], "Guard-watched by their mother Rizpah on the rock of Gibeah."),
        N("saul_mica_line", "Mica → Pithon, Melech, Tarea & Ahaz (1 Chr 8:35–40 Post-Jonathan Line)", "biblical", 17, "10th–6th c. BCE (1 Chr 8:35–40)", "Surviving Benjamite Line of Jonathan ben Saul", ["1 Chronicles 8:35–40, 9:41–44"], "Continues Jonathan's royal line through Ahaz -> Jehoaddah -> Alemeth/Azmaveth/Zimri -> Moza -> Binea -> Raphah -> Eleasah -> Azel -> Eshek -> Ulam."),
    ]
    edges += [
        E("jdg_deborah", "jdg2_barak", "expansion", "Judg 4:6: Deborah summons General Barak"),
        E("mid_jethro", "jdg2_heber_kenite", "direct", "Judg 4:11: descendant of Hobab/Jethro"),
        E("jdg2_heber_kenite", "jdg2_jael", "direct", "Judg 4:17: wife of Heber the Kenite"),
        E("jdg_gideon", "jdg2_abimelech", "direct", "Judg 8:31: Gideon -> Abimelech"),
        E("jdg_gideon", "jdg2_jotham", "direct", "Judg 9:5: Gideon -> youngest son Jotham"),
        E("jos_manasseh", "jdg2_jair", "direct", "Judg 10:3: Gileadite Judge Jair"),
        E("jdg_tola_jair", "jdg2_jair", "expansion", "6th & 7th Judges succession"),
        E("tri_zebulun_elon", "jdg2_elon", "direct", "Judg 12:11: Zebulunite Judge Elon"),
        E("jdg_ibzan_elon_abdon", "jdg2_elon", "expansion", "Minor Judges succession"),
        E("jos_ephraim", "jdg2_abdon", "direct", "Judg 12:13: Ephraimite Judge Abdon"),
        E("tri_dan", "jdg2_manoah", "direct", "Judg 13:2: Danite Manoah of Zorah"),
        E("jdg2_manoah", "jdg_samson", "direct", "Judg 13:24: Manoah -> Samson"),
        E("jdg_samson", "jdg2_delilah", "cognate", "Judg 16:4: Samson & Delilah"),
        E("jdg_eli", "jdg2_hophni", "direct", "1 Sam 1:3: Eli -> Hophni"),
        E("jdg_eli", "jdg2_phinehas_eli", "direct", "1 Sam 1:3: Eli -> Phinehas"),
        E("jdg2_phinehas_eli", "jdg2_ichabod", "direct", "1 Sam 4:21: Phinehas -> Ichabod"),
        E("jdg2_phinehas_eli", "jdg2_ahitub_eli", "direct", "1 Sam 14:3: Phinehas -> Ahitub"),
        E("jdg2_ahitub_eli", "jdg2_ahimelech", "direct", "1 Sam 22:9: Ahitub -> Ahimelech of Nob"),
        E("jdg2_ahimelech", "jdg2_abiathar", "direct", "1 Sam 22:20: Ahimelech -> Abiathar"),
        E("bib_korah_asaph", "jdg2_elkanah", "direct", "1 Chr 6:33–38: Korah -> Elkanah"),
        E("jdg2_elkanah", "jdg2_hannah", "direct", "1 Sam 1:2: Marriage of Elkanah & Hannah"),
        E("jdg2_elkanah", "jdg_samuel", "direct", "1 Sam 1:20: Father Elkanah -> Samuel"),
        E("jdg2_hannah", "jdg_samuel", "direct", "1 Sam 1:20: Mother Hannah -> Samuel"),
        E("jdg_samuel", "jdg2_joel_samuel", "direct", "1 Sam 8:2: Samuel -> Joel"),
        E("jdg_samuel", "jdg2_abijah_samuel", "direct", "1 Sam 8:2: Samuel -> Abijah"),
        E("jdg2_joel_samuel", "jdg2_heman_singer", "direct", "1 Chr 6:33: Joel -> Heman the Singer"),
        E("tri_benjamin", "saul_abiel", "direct", "1 Sam 9:1 & 1 Chr 8:29: Benjamin -> Abiel"),
        E("saul_abiel", "saul_kish", "direct", "1 Sam 9:1: Abiel -> Kish"),
        E("saul_abiel", "saul_ner", "direct", "1 Chr 8:33: Abiel -> Ner"),
        E("saul_kish", "bib_saul", "direct", "1 Sam 9:1–2: Kish -> King Saul"),
        E("saul_ner", "saul_abner", "direct", "1 Sam 14:50: Ner -> General Abner"),
        E("bib_saul", "saul_abinadab", "direct", "1 Sam 14:49: Saul -> Abinadab"),
        E("cb_ahinoam_saul", "saul_abinadab", "direct", "Mother Ahinoam -> Abinadab"),
        E("bib_saul", "saul_malchishua", "direct", "1 Sam 14:49: Saul -> Malchi-shua"),
        E("cb_ahinoam_saul", "saul_malchishua", "direct", "Mother Ahinoam -> Malchi-shua"),
        E("bib_saul", "saul_ishbosheth", "direct", "1 Chr 8:33: Saul -> Ish-bosheth"),
        E("cb_ahinoam_saul", "saul_ishbosheth", "direct", "Mother Ahinoam -> Ish-bosheth"),
        E("bib_saul", "saul_armoni_mephi", "direct", "2 Sam 21:8: Saul -> Armoni & Mephibosheth II"),
        E("cb_rizpah", "saul_armoni_mephi", "direct", "2 Sam 21:8: Mother Rizpah -> Armoni & Mephibosheth II"),
        E("bib_saul", "bib_jonathan_abner", "direct", "1 Sam 14:49: Saul -> Crown Prince Jonathan"),
        E("cb_ahinoam_saul", "bib_jonathan_abner", "direct", "Mother Ahinoam -> Jonathan"),
        E("bib_jonathan_abner", "cb_mephibosheth_mica", "direct", "2 Sam 9:6: Jonathan -> Mephibosheth"),
        E("cb_mephibosheth_mica", "saul_mica_line", "direct", "1 Chr 8:35–40: Mephibosheth -> Mica -> 4 sons"),
    ]

    # =========================================================================
    # 5. PROPHETS, ESTHER HOUSEHOLD, ANAKIM, BATHSHEBA & JOB INDIVIDUALLY
    # =========================================================================
    nodes += [
        N("pro2_elisha", "Prophet Elisha ben Shaphat of Abel-meholah (1 Kgs 19:16; 2 Kgs 2–13)", "biblical", 17, "c. 850–800 BCE (1 Kgs 19; 2 Kgs 2–13)", "Successor of Elijah", ["1 Kings 19:16", "2 Kings 2–13"], "Received Elijah's double portion; anointed Jehu of Israel and Hazael of Damascus.", major=True),
        N("pro2_zephaniah", "Prophet Zephaniah ben Cushi (Great-Great-Grandson of King Hezekiah, Zeph 1:1)", "biblical", 17, "c. 640–609 BCE (Zeph 1:1)", "Royal Davidic Prophet Under King Josiah", ["Zephaniah 1:1"], "Zeph 1:1 explicitly traces Cushi -> Gedaliah -> Amariah -> King Hezekiah!"),
        N("pro2_shear_jashub", "Shear-jashub (Elder Son of Prophet Isaiah, Isa 7:3)", "biblical", 17, "8th c. BCE (Isa 7:3)", "Prophetic Sign Son of Isaiah", ["Isaiah 7:3"], "Accompanied Isaiah to meet King Ahaz ('A remnant shall return')."),
        N("pro2_maher_shalal", "Maher-shalal-hash-baz (Younger Son of Isaiah & the Prophetess, Isa 8:3)", "biblical", 17, "8th c. BCE (Isa 8:1–4)", "Prophetic Sign Son of Isaiah", ["Isaiah 8:1–4"], "Named before Damascus and Samaria fell to Assyria."),
        N("pro2_baruch", "Baruch ben Neriah (Scribe of Jeremiah; Brother of Seraiah, Jer 36, 51:59)", "biblical", 17, "c. 605–582 BCE (Jer 36, 45; Bulla!)", "Scribe & Companion of Prophet Jeremiah", ["Jeremiah 36:4", "Jeremiah 45"], "Wrote Jeremiah's dictated scroll and left two authentic Jerusalem clay bullae ('Berekhyahu ben Neriyahu ha-Sofer')!"),
        N("pro2_ezekiel", "Prophet Ezekiel ben Buzi (Zadokite Priest Exiled to Tel-abib, Ezek 1:3)", "biblical", 17, "593–571 BCE (Babylon — Ezek 1:1–3)", "Exilic Priestly Prophet", ["Ezekiel 1:1–3"], "Exiled with King Jehoiachin in 597 BCE to the Kebar canal in Babylonia.", major=True),
        N("pro2_hananiah_shadrach", "Hananiah / Shadrach, Mishael / Meshach & Azariah / Abednego (Three Judean Youths, Dan 1–3)", "biblical", 17, "6th c. BCE (Babylon — Daniel 1–3)", "Judean Nobles in Nebuchadnezzar's Court", ["Daniel 1:6–7, 3"], "Exiled from Judah with Daniel and appointed administrators of Babylon province."),
        N("pro2_nehemiah", "Governor Nehemiah ben Hacaliah (Cupbearer to Artaxerxes I, Neh 1:1)", "biblical", 18, "445–432 BCE (Susa → Jerusalem — Neh 1–13)", "Builder of Jerusalem's Walls", ["Nehemiah 1–13"], "Cupbearer at Susa commissioned by Artaxerxes I to rebuild Jerusalem's walls.", major=True),
        N("pro2_gomer", "Gomer bat Diblaim (Wife of Prophet Hosea, Hos 1:3)", "biblical", 17, "8th c. BCE (Hosea 1:3)", "Wife of Hosea & Mother of Jezreel, Lo-ruhamah & Lo-ammi", ["Hosea 1:2–9"], "Mother of three prophetic-sign children with Hosea."),
        N("pro2_amos", "Prophet Amos of Tekoa (760–750 BCE)", "biblical", 17, "c. 760 BCE (Amos 1:1)", "Shepherd-Prophet at Bethel", ["Amos 1:1, 7:14"], "Herdsman from Judahite Tekoa who prophesied at Bethel under Jeroboam II."),
        N("pro2_jonah", "Prophet Jonah ben Amittai of Gath-hepher (2 Kgs 14:25; Jonah 1:1)", "biblical", 17, "8th c. BCE (2 Kgs 14:25; Book of Jonah)", "Galilean Prophet Sent to Nineveh", ["2 Kings 14:25", "Book of Jonah"], "Zebulunite prophet of Gath-hepher whose mission to Nineveh is cited in Matt 12:40.", major=True),
        N("pro2_micah", "Prophet Micah of Moresheth (Mic 1:1)", "biblical", 17, "c. 735–700 BCE (Micah 1:1; Jer 26:18)", "Prophet of Bethlehem Prophecy (Mic 5:2)", ["Micah 1:1, 5:2"], "Contemporary of Isaiah who prophesied Messiah's birth in Bethlehem."),
        N("pro2_habakkuk", "Prophet Habakkuk (Hab 1:1)", "biblical", 17, "c. 605 BCE (Habakkuk 1–3)", "Judean Watchman-Prophet", ["Book of Habakkuk"], "Prophesied on the eve of the Neo-Babylonian rise."),
        N("pro2_zechariah_iddo", "Prophet Zechariah ben Berechiah ben Iddo (Zech 1:1; Ezra 5:1)", "biblical", 18, "520–518 BCE (Zech 1:1; Neh 12:16)", "Post-Exilic Priestly Prophet", ["Zechariah 1:1", "Ezra 5:1"], "Grandson of Iddo; encouraged Zerubbabel and Jeshua in rebuilding the Second Temple."),
        N("pro2_haggai", "Prophet Haggai (Hag 1:1; Ezra 5:1)", "biblical", 18, "520 BCE (Haggai 1–2)", "Post-Exilic Temple Prophet", ["Haggai 1–2", "Ezra 5:1"], "Called Zerubbabel and High Priest Jeshua to resume Temple construction in Darius I's 2nd year."),
        N("pro2_malachi", "Prophet Malachi (Final OT Prophetic Scroll, Mal 1:1)", "biblical", 18, "5th c. BCE (Book of Malachi)", "Final Canonical Prophet of the Old Testament", ["Book of Malachi"], "Called post-exilic priesthood to covenant faithfulness."),
        # Other key individualizations
        N("w2_ahithophel", "Ahithophel of Giloh (Grandfather of Bathsheba; David's Counselor, 2 Sam 15, 23:34)", "biblical", 15, "c. 1010–980 BCE (2 Sam 15–17)", "Royal Counselor & Maternal Grandfather of Bathsheba", ["2 Samuel 15:12, 23:34"], "Father of Eliam (2 Sam 23:34) and grandfather of Queen Bathsheba."),
        N("w2_uriah_hittite", "Uriah the Hittite (Mighty Man of David; 1st Husband of Bathsheba, 2 Sam 11, 23:39)", "biblical", 15, "d. c. 995 BCE (2 Sam 11; 1 Chr 11:41)", "Hittite Champion Among David's Thirty", ["2 Samuel 11:3–17", "2 Samuel 23:39"], "Honored Hittite soldier and first husband of Bathsheba."),
        N("w2_caleb_jephunneh", "Caleb ben Jephunneh the Kenizzite (Father of Achsah, Num 13; Josh 14)", "biblical", 16, "Exodus & Conquest (Num 13:6; Josh 14:6–15)", "Faithful Spy & Conqueror of Hebron", ["Numbers 13:6", "Joshua 14:6–15", "1 Chronicles 4:15"], "Companion spy with Joshua who inherited Hebron and gave daughter Achsah to Othniel.", major=True),
        N("w2_abihail_esther", "Abihail (Uncle of Mordecai & Father of Queen Esther, Esth 2:15)", "biblical", 17, "5th c. BCE (Esther 2:15, 9:29)", "Benjaminite Father of Queen Esther", ["Esther 2:15", "Esther 9:29"], "Brother of Mordecai's father Jair; father of Hadassah / Queen Esther."),
        N("w2_queen_esther", "Queen Esther / Hadassah (Daughter of Abihail; Queen of Xerxes I, Esth 2–9)", "biblical", 18, "5th c. BCE (Susa — Book of Esther)", "Jewish Queen of the Achaemenid Persian Empire", ["Book of Esther"], "Orphaned daughter of Abihail raised by cousin Mordecai; wed Emperor Ahasuerus/Xerxes I and thwarted Haman's decree.", major=True),
        N("w2_queen_vashti", "Queen Vashti (1st Consort of King Ahasuerus / Xerxes I, Esth 1:9)", "biblical", 18, "5th c. BCE (Susa — Esther 1)", "Preceding Queen of Persia", ["Esther 1:9–22"], "Deposed prior to the selection of Queen Esther."),
        N("w2_anak", "Anak (Father of Sheshai, Ahiman & Talmai at Hebron, Num 13:22, 33)", "biblical", 15, "Patriarchal / Conquest (Num 13:22)", "Progenitor of the Anakim", ["Numbers 13:22, 33", "Joshua 15:14"], "Son of Arba; father of the three Anakim clans of Hebron."),
        N("w2_job_jemimah", "Jemimah (Eldest Fair Daughter of Job, Job 42:14)", "biblical", 10, "Book of Job (Job 42:14)", "Daughter & Co-Heir of Patriarch Job", ["Job 42:14–15"], "Eldest of Job's three post-trial daughters granted equal inheritance."),
        N("w2_job_keziah", "Keziah (Second Fair Daughter of Job, Job 42:14)", "biblical", 10, "Book of Job (Job 42:14)", "Daughter & Co-Heir of Patriarch Job", ["Job 42:14–15"], "Second of Job's three daughters ('Cassia')."),
        N("w2_job_kerenhappuch", "Keren-happuch (Third Fair Daughter of Job, Job 42:14)", "biblical", 10, "Book of Job (Job 42:14)", "Daughter & Co-Heir of Patriarch Job", ["Job 42:14–15"], "Youngest of Job's three daughters."),
        N("w2_asaph_seer", "Asaph ben Berechiah ('The Seer' & Chief Gershonite Psalmist, 1 Chr 6:39, 25:1)", "biblical", 16, "10th c. BCE (1 Chr 6:39, 25:1–2; Pss 50, 73–83)", "Gershonite Levite Chief Musician", ["1 Chronicles 6:39", "2 Chronicles 29:30"], "Ancestor of the post-exilic Sons of Asaph choir (Ezra 2:41)."),
        N("w2_ethan_jeduthun", "Ethan / Jeduthun (Chief Merarite Psalmist, 1 Chr 6:44, 25:1)", "biblical", 16, "10th c. BCE (1 Chr 6:44, 25:1–3; Ps 89)", "Merarite Levite Chief Musician", ["1 Chronicles 6:44", "Psalm 89 title"], "Third chief Levitical musician alongside Heman and Asaph."),
    ]
    edges += [
        E("pro_elijah_elisha", "pro2_elisha", "direct", "2 Kgs 2: Spiritual succession Elijah -> Elisha"),
        E("kg_j9_hezekiah", "pro2_zephaniah", "direct", "Zeph 1:1: King Hezekiah -> Amariah -> Gedaliah -> Cushi -> Prophet Zephaniah"),
        E("pro_isaiah_zephaniah", "pro2_shear_jashub", "direct", "Isa 7:3: Isaiah -> Shear-jashub"),
        E("pro_isaiah_zephaniah", "pro2_maher_shalal", "direct", "Isa 8:3: Isaiah -> Maher-shalal-hash-baz"),
        E("pro_jeremiah_ezekiel", "pro2_baruch", "expansion", "Jer 36:4: Scribe Baruch ben Neriah"),
        E("pri_eleazar_zadok", "pro2_ezekiel", "direct", "Ezek 1:3: Zadokite priestly house -> Prophet Ezekiel ben Buzi"),
        E("kg_j12_jehoiakim_zedekiah", "pro2_hananiah_shadrach", "expansion", "Dan 1:6: Judean noble exiles Hananiah, Mishael, Azariah"),
        E("pro_daniel_nehemiah", "pro2_nehemiah", "expansion", "Neh 1:1: Statesman Nehemiah ben Hacaliah"),
        E("ir_artaxerxes1", "pro2_nehemiah", "cognate", "Neh 2: Artaxerxes I dispatches cupbearer Nehemiah"),
        E("pro_minor_prophets", "pro2_gomer", "direct", "Hos 1:3: Marriage of Hosea & Gomer"),
        E("kg_i4_jehu", "pro2_amos", "expansion", "Amos 1:1: Prophet Amos under Jeroboam II"),
        E("tri_zebulun", "pro2_jonah", "expansion", "2 Kgs 14:25: Prophet Jonah of Gath-hepher (Zebulun)"),
        E("kg_j9_hezekiah", "pro2_micah", "expansion", "Mic 1:1: Prophet Micah of Moresheth"),
        E("kg_j12_jehoiakim_zedekiah", "pro2_habakkuk", "expansion", "Hab 1: Prophet Habakkuk"),
        E("dav_zerubbabel", "pro2_zechariah_iddo", "expansion", "Zech 1 & Ezra 5:1: Zechariah ben Iddo"),
        E("dav_zerubbabel", "pro2_haggai", "expansion", "Hag 1 & Ezra 5:1: Prophet Haggai"),
        E("pri_ezra_jaddua", "pro2_malachi", "expansion", "Post-exilic prophet Malachi"),
        E("w2_ahithophel", "bib_bathsheba_uriah", "direct", "2 Sam 23:34: Ahithophel -> Eliam"),
        E("bib_bathsheba_uriah", "cb_w_dav_bathsheba", "direct", "2 Sam 11:3: Eliam -> Queen Bathsheba"),
        E("bib_heth", "w2_uriah_hittite", "expansion", "Hittite soldier Uriah"),
        E("w2_uriah_hittite", "cb_w_dav_bathsheba", "direct", "2 Sam 11:3: 1st marriage of Bathsheba to Uriah"),
        E("bib_joshua_caleb", "w2_caleb_jephunneh", "expansion", "Two faithful spies Joshua & Caleb"),
        E("w2_caleb_jephunneh", "cb_achsah", "direct", "Josh 15:16: Caleb -> daughter Achsah"),
        E("bib_esther_mordecai", "w2_abihail_esther", "direct", "Esth 2:15: Uncle Abihail of Mordecai"),
        E("w2_abihail_esther", "w2_queen_esther", "direct", "Esth 2:15: Abihail -> Hadassah / Queen Esther"),
        E("ir_xerxes1", "w2_queen_esther", "cognate", "Esth 2:17: Queen Esther wed to Xerxes I (Ahasuerus)"),
        E("ir_xerxes1", "w2_queen_vashti", "cognate", "Esth 1:9: Preceding Queen Vashti"),
        E("bib_anakim_goliath", "w2_anak", "direct", "Num 13:22: Anakim -> Goliath"),
        E("bib_job", "w2_job_jemimah", "direct", "Job 42:14: Job -> Jemimah"),
        E("bib_job", "w2_job_keziah", "direct", "Job 42:14: Job -> Keziah"),
        E("bib_job", "w2_job_kerenhappuch", "direct", "Job 42:14: Job -> Keren-happuch"),
        E("lev_gershon", "w2_asaph_seer", "direct", "1 Chr 6:39: Gershon -> Asaph the Seer"),
        E("lev_merari", "w2_ethan_jeduthun", "direct", "1 Chr 6:44: Merari -> Ethan / Jeduthun"),
    ]

    # =========================================================================
    # 6. COMPLETE INDIVIDUAL MATTHEW 1 (10 LINKS) & LUKE 3 (41 LINKS) + NT FAMILIES
    # =========================================================================
    matt1_links = [
        ("m1_abiud", "Abiud (Son of Zerubbabel, Matt 1:13)", "dav_zerubbabel"),
        ("m1_eliakim", "Eliakim (Matt 1:13)", "m1_abiud"),
        ("m1_azor", "Azor (Matt 1:13–14)", "m1_eliakim"),
        ("m1_zadok", "Zadok (Matt 1:14)", "m1_azor"),
        ("m1_achim", "Achim (Matt 1:14)", "m1_zadok"),
        ("m1_eliud", "Eliud (Matt 1:14–15)", "m1_achim"),
        ("m1_eleazar", "Eleazar (Matt 1:15)", "m1_eliud"),
        ("m1_matthan", "Matthan (Matt 1:15 — Syriac Matthan + Sebhrath!)", "m1_eleazar"),
        ("m1_jacob", "Jacob ben Matthan (Father of Joseph, Matt 1:15–16)", "m1_matthan"),
    ]
    for mid, mname, mpar in matt1_links:
        nodes.append(N(mid, mname, "biblical", 18, "5th–1st c. BCE (Matthew 1:13–16)", "Messianic Royal Legal Lineage (Matthew 1)", ["Matthew 1:13–16"], f"{mname} in Matthew 1."))
        edges.append(E(mpar, mid, "direct", "Matt 1:13–16: legal Davidic lineage"))
    edges.append(E("m1_jacob", "nt_matthew_joseph", "direct", "Matt 1:16: Jacob -> Joseph of Nazareth"))
    edges.append(E("m1_matthan", "syr_twin_jacob_yonakhir", "expansion", "Syriac Cave of Treasures: Matthan + Sebhrath -> Twins Jacob & Yonakhir"))

    luke3_names = [
        "Mattatha", "Menna", "Melea", "Eliakim (Luke 3)", "Jonam", "Joseph (son of Jonam)",
        "Judah (son of Joseph)", "Simeon (Luke 3)", "Levi (son of Simeon)", "Matthat (son of Levi)",
        "Jorim", "Eliezer (son of Jorim)", "Joshua / Jose (Luke 3)", "Er (son of Joshua)", "Elmadam",
        "Cosam", "Addi", "Melchi (son of Addi)", "Neri (Father of Shealtiel, Luke 3:27)",
        "Rhesa (Luke 3:27)", "Joanan (Luke 3:27)", "Joda", "Josech", "Semein",
        "Mattathias (son of Semein)", "Maath", "Naggai", "Esli", "Nahum (Luke 3:25)",
        "Amos (son of Nahum)", "Mattathias II (son of Amos)", "Joseph II (son of Mattathias)",
        "Jannai", "Melchi II (son of Jannai)", "Levi II (son of Melchi)", "Matthat II (Grandfather of Mary, Luke 3:24)"
    ]
    prev_l3 = "bib16_dav_10_nathan_ben_david_son_by_bath"
    for idx, lname in enumerate(luke3_names, 1):
        lid = f"l3_{idx:02d}_{lname.split()[0].lower().replace('(', '').replace(')', '')}"
        nodes.append(N(lid, f"{lname} (Luke 3:{32 - (idx // 3)})", "biblical", 18, "10th–1st c. BCE (Luke 3:23–31)",
                       "Davidic Messianic Ancestor via Nathan (Luke 3)", ["Luke 3:23–31"],
                       f"Link #{idx+1} in the Gospel of Luke's David-via-Nathan pedigree."))
        edges.append(E(prev_l3, lid, "direct", "Luke 3:23–31: biological Davidic descent"))
        if lname.startswith("Neri"):
            edges.append(E(lid, "dav_shealtiel", "direct", "Luke 3:27: Neri -> Shealtiel"))
            prev_l3 = "dav_zerubbabel"
            continue
        prev_l3 = lid
    edges.append(E(prev_l3, "nt_joachim_anne", "direct", "Luke 3:23–24: Matthat -> Heli / Joachim (father of Mary)"))
    edges.append(E("nt_joachim_anne", "nt_luke_mary", "direct", "Joachim/Heli & Saint Anne -> Blessed Virgin Mary"))
    edges.append(E("bib16_apo_saint_anne", "nt_luke_mary", "direct", "Mother Saint Anne -> Virgin Mary"))

    # Remaining individual NT church families from cb_nt_households_women
    nt_extra = [
        ("nt2_zechariah_priest", "Priest Zechariah (Course of Abijah; Father of John the Baptist, Luke 1:5)", "chr_levi_24_courses", "Luke 1:5: 8th Course of Abijah -> Zechariah"),
        ("nt2_elizabeth", "Elizabeth (Daughter of Aaron & Sobe; Mother of John the Baptist, Luke 1:5)", "bib16_apo_sobe", "Tradition: Sobe -> Elizabeth"),
        ("nt2_aquila", "Aquila of Pontus (Tentmaker Co-Worker of Paul, Acts 18:2)", "nt_paul", "Acts 18:2: Paul's co-worker Aquila"),
        ("nt2_priscilla", "Priscilla / Prisca (Teacher of Apollos, Acts 18:2, 26; Rom 16:3)", "nt2_aquila", "Acts 18:2: Marriage of Aquila & Priscilla"),
        ("nt2_simon_cyrene", "Simon of Cyrene (Cross-Bearer; Father of Alexander & Rufus, Mark 15:21)", "nt_jesus", "Mark 15:21: Carried the cross of Jesus"),
        ("nt2_alexander_cyrene", "Alexander (Son of Simon of Cyrene, Mark 15:21)", "nt2_simon_cyrene", "Mark 15:21: Simon -> Alexander"),
        ("nt2_rufus_cyrene", "Rufus (Son of Simon of Cyrene; Greeted in Rom 16:13)", "nt2_simon_cyrene", "Mark 15:21 & Rom 16:13: Simon -> Rufus"),
        ("nt2_philip_evangelist", "Philip the Evangelist of Caesarea (One of the Seven; Father of 4 Prophetesses, Acts 21:8–9)", "nt_jesus", "Acts 6:5 & 21:8: Early Jerusalem deacon/evangelist"),
        ("nt2_philip_4daughters", "Four Prophesying Virgin Daughters of Philip (Acts 21:9; Eusebius HE III.31)", "nt2_philip_evangelist", "Acts 21:9: Daughters of Evangelist Philip"),
    ]
    for nid, nm, par, lbl in nt_extra:
        nodes.append(N(nid, nm, "biblical", 19, "1st c. CE (New Testament)", "Named New Testament Individual", ["Gospels, Acts & Epistles"], nm))
        edges.append(E(par, nid, "direct" if "Son" in lbl or "Course" in lbl or "Sobe" in lbl or "Marriage" in lbl or "Daughters" in lbl else "expansion", lbl))
    edges += [
        E("nt2_zechariah_priest", "nt2_elizabeth", "direct", "Luke 1:5: Marriage of Zechariah & Elizabeth"),
        E("nt2_zechariah_priest", "nt_john_baptist", "direct", "Luke 1:13: Father Zechariah -> John the Baptist"),
        E("nt2_elizabeth", "nt_john_baptist", "direct", "Luke 1:57: Mother Elizabeth -> John the Baptist"),
    ]

    return {
        "module": "43_wave2_biblical_person_by_person",
        "title": "Wave 2 Person-by-Person Biblical Backbone (Perez → David → All 20 Kings & Queen Mothers of Judah → All 19 Kings of Israel → All 12 Judges → House of Saul → Prophets → Matthew 1 & Luke 3)",
        "nodes": nodes,
        "edges": edges,
    }
