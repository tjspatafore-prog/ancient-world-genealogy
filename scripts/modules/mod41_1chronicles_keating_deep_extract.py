"""
Module 41: Deep Clean-Text Extraction of:
1. Jacob M. Myers, Anchor Bible 1 Chronicles (ab1Chronicles2nd MyersJM 1965-opt.pdf):
   Exhaustive Tribal Sub-Clans of 1 Chronicles 2-8 including hidden international/royal bridges
   (Jarha the Egyptian + Ahlai; Mered + Pharaoh's Daughter Bithiah; Beriah; Shaharaim in Moab; Simeon, Reuben, Gad, Issachar, Asher, Benjamin).
2. Geoffrey Keating, Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf — 38 full clean-text pages):
   All 12 Noble Tribes of the Gaels (Saorchlanna) from Eber Finn, Eremon, Ir & Ith down to O'Brien,
   MacCarthy, O'Neill, O'Donnell (+ St. Columba), O'Connor, MacMurrough-Kavanagh (+ Strongbow), Magennis & Dal Riada.
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # 1. 1 CHRONICLES 2-8 COMPLETE TRIBAL SUB-CLANS & BRIDGES (Myers 1965)
    # =========================================================================
    nodes += [
        N("chr41_jerahmeel_atarah", "Jerahmeel ben Hezron (+ Atarah) → Ram, Bunah, Oren, Ozem, Ahijah & Onam (1 Chr 2:25–33)", "biblical", 14,
          "1 Chronicles 2:25–33 (Myers Anchor Bible 1965)",
          "Firstborn Clan of Hezron of Judah", ["1 Chronicles 2:25–33", "Jacob M. Myers 1 Chronicles (1965)"],
          "Hezron's firstborn Jerahmeel wed a second wife Atarah, mother of Onam (-> Shammai, Jada -> Peleth & Zaza); elder line via Ram -> Maaz, Jamin & Eker.",
          ["Atarah wife of Jerahmeel"], major=False),
        N("chr41_sheshan_jarha_egypt", "Sheshan → Daughter Ahlai + Jarha the Egyptian → Attai → Nathan → Zabad → Elishama (1 Chr 2:34–41)", "biblical", 15,
          "1 Chronicles 2:34–41 (Judah–Egypt Intermarriage)",
          "Explicit 13-Generation Egyptian Bloodline Grafted Into Tribe of Judah!",
          ["1 Chronicles 2:34–41", "Jacob M. Myers Anchor Bible 1 Chronicles (1965)"],
          "Sheshan of Jerahmeel had no sons, so he gave his daughter Ahlai to his Egyptian servant Jarha — establishing a 13-generation documented Egyptian-Judahite pedigree: Jarha + Ahlai -> Attai -> Nathan -> Zabad -> Ephlal -> Obed -> Jehu -> Azariah -> Helez -> Eleasah -> Sismai -> Shallum -> Jekamiah -> Elishama!",
          ["Jarha the Egyptian", "Ahlai bat Sheshan"], major=True),
        N("chr41_ashhur_tekoa", "Ashhur Father of Tekoa (+ Helah & Naarah) → Ahuzzam, Hepher, Temeni, Haahashtari & Zohar (1 Chr 4:5–7)", "biblical", 14,
          "1 Chronicles 4:5–7 (Posthumous Son of Hezron)",
          "Founder of Judahite Tekoa (Home of Prophet Amos)", ["1 Chronicles 4:5–7", "Myers 1 Chronicles (1965)"],
          "Posthumous son of Hezron & Abijah; wed Helah and Naarah, founding Tekoa and Bethlehem-area clans.",
          ["Helah & Naarah"], major=False),
        N("chr41_jabez", "Jabez ('More Honorable Than His Brothers', 1 Chr 4:9–10)", "biblical", 15,
          "1 Chronicles 4:9–10 (Myers Anchor Bible 1965)",
          "Judahite Patriarch of Scribal Clans of Jabez", ["1 Chronicles 4:9–10", "Myers 1 Chronicles (1965)"],
          "Famed in 1 Chronicles 4 for his prayer of blessing and associated in 1 Chr 2:55 with the Kenite scribal families (Rechabites -> Hammath).", major=False),
        N("chr41_mered_bithiah_pharaoh", "Mered of Judah + Bithiah Daughter of Pharaoh (1 Chr 4:18) → Miriam, Shammai & Ishbah", "biblical", 15,
          "1 Chronicles 4:17–18 (Judah–Pharaoh Royal Marriage)",
          "Second Explicit Egyptian Royal Princess Wed Into Judahite Line!",
          ["1 Chronicles 4:17–18", "Myers 1 Chronicles (1965)", "Talmud Sanhedrin 19b"],
          "Beside Caleb's line in 1 Chr 4:17–18, Mered married BOTH a Jewish wife (Jered, Heber, Jekuthiel) AND 'Bithiah the daughter of Pharaoh' — bearing Miriam, Shammai, and Ishbah (rabbinic tradition identifies Mered with Caleb and Bithiah with Moses's adoptive mother!).",
          ["Bithiah dau. of Pharaoh", "Mered of Judah"], major=True),
        N("chr41_shobal_salma", "Shobal (Father of Kiriath-jearim) & Salma (Father of Bethlehem) — Sons of Hur (1 Chr 2:50–55)", "biblical", 15,
          "1 Chronicles 2:50–55 (Caleb → Hur)",
          "Judahite Founders of Bethlehem & Kiriath-jearim", ["1 Chronicles 2:50–55", "Myers 1 Chronicles (1965)"],
          "Sons of Hur (firstborn of Ephrath & Caleb) who settled Bethlehem, Kiriath-jearim, Zorathites & Kenite scribes.", major=False),
        N("chr41_simeon_clans", "Simeonites (1 Chr 4:24–43): Shallum → Mibsam → Mishma → Hammuel → Zaccur → Shimei (16 Sons & 6 Daughters)", "biblical", 15,
          "1 Chronicles 4:24–43 (Myers 1965)",
          "Simeonite Desert Princes & Mt. Seir Settlers", ["1 Chronicles 4:24–43", "Myers Anchor Bible 1 Chronicles"],
          "Details Simeon's southern clans including Shimei's 16 sons and 6 daughters and 500 Simeonites under Ishi's sons (Pelatiah, Neariah, Rephaiah, Uzziel) who settled Mt. Seir.", major=False),
        N("chr41_reuben_beerah", "Reubenites (1 Chr 5:4–6): Joel → Shemaiah → Gog → Shimei → Micah → Reaiah → Baal → Prince Beerah", "biblical", 16,
          "1 Chronicles 5:4–6 (Assyrian Exile 733 BCE)",
          "Transjordanian House of Reuben Until Tiglath-Pileser III", ["1 Chronicles 5:4–6", "Myers 1 Chronicles (1965)"],
          "Complete 8-generation Reubenite lineage ending with tribal prince Beerah, carried captive to Halah and Habor by Assyrian emperor Tiglath-Pileser III (Pul).",
          ["Prince Beerah of Reuben"], major=False),
        N("chr41_gad_clans", "Gadites in Bashan (1 Chr 5:11–17): Joel, Shapham, Janai, Shaphat & Abihail ben Huri", "biblical", 15,
          "1 Chronicles 5:11–17 (Gilead & Bashan)",
          "Chiefs of Gad in Transjordan", ["1 Chronicles 5:11–17", "Myers 1 Chronicles (1965)"],
          "Traces Gadite houses in Gilead and Bashan registered under Kings Jotham of Judah and Jeroboam II of Israel.", major=False),
        N("chr41_manasseh_east", "Half-Tribe of Manasseh in Bashan & Mt. Hermon (1 Chr 5:24): Epher, Ishi, Eliel, Azriel, Jeremiah, Hodaviah & Jahdiel", "biblical", 16,
          "1 Chronicles 5:23–26 (Myers 1965)",
          "Transjordanian Mighty Warriors of Manasseh", ["1 Chronicles 5:23–26", "Myers 1 Chronicles (1965)"],
          "Seven named tribal heads of eastern Manasseh from Bashan to Mount Hermon.", major=False),
        N("chr41_issachar_tola", "Issachar (1 Chr 7:1–5): Tola → Uzzi → Izrahiah → Michael, Obadiah, Joel & Isshiah", "biblical", 14,
          "1 Chronicles 7:1–5 (Myers 1965)",
          "Principal Sub-Clans of Issachar", ["1 Chronicles 7:1–5", "Myers 1 Chronicles (1965)"],
          "Traces Tola's six warrior clans (Uzzi, Rephaiah, Jeriel, Jahmai, Ibsam, Shemuel) and Izrahiah's five chief sons.", major=False),
        N("chr41_benjamin_clans", "Benjamin (1 Chr 7:6–12, 8:1–32): Jediael, Shaharaim (+ Hushim & Baara/Hodesh in Moab), Beriah & Shema (Aijalon)", "biblical", 15,
          "1 Chronicles 7:6–12, 8:1–32 (Myers 1965)",
          "Complete Benjamite Houses of Geba, Moab, Aijalon & Jerusalem", ["1 Chronicles 7:6–12, 8:1–32", "Myers 1 Chronicles (1965)"],
          "Includes Shaharaim (who fathered seven sons by Hodesh and Hushim in the country of Moab), Beriah & Shema (founders of Ono, Lod & Aijalon), and Jeiel's Gibeon clan.",
          ["Shaharaim in Moab", "Hodesh & Hushim"], major=False),
        N("chr41_asher_shua", "Asher (1 Chr 7:30–40): Heber → Japhlet, Shomer, Hotham & Sister Shua (F) → Zophah & Ithran", "biblical", 15,
          "1 Chronicles 7:30–40 (Myers 1965)",
          "Northern Coastal Asherite Pedigree & Named Daughter Shua", ["1 Chronicles 7:30–40", "Myers 1 Chronicles (1965)"],
          "Complete 4-generation pedigree from Heber ben Beriah ben Asher down through Birzaith, Shomer, Hotham, and named sister Shua (1 Chr 7:32).",
          ["Shua bat Heber"], major=False),
    ]
    edges += [
        E("chr_hezron_ram", "chr41_jerahmeel_atarah", "direct", "1 Chr 2:25–33: Hezron -> Jerahmeel (+ Atarah) -> Onam"),
        E("chr41_jerahmeel_atarah", "chr41_sheshan_jarha_egypt", "direct", "1 Chr 2:34–41: Sheshan -> Ahlai + Jarha the Egyptian -> 13 gens"),
        E("chr_hezron_ram", "chr41_ashhur_tekoa", "direct", "1 Chr 4:5–7: Hezron -> Ashhur (+ Helah & Naarah) -> Tekoa"),
        E("tri_judah", "chr41_jabez", "direct", "1 Chr 4:9–10: Judah -> Jabez"),
        E("tri_judah", "chr41_mered_bithiah_pharaoh", "direct", "1 Chr 4:17–18: Mered + Bithiah daughter of Pharaoh -> Miriam, Shammai & Ishbah"),
        E("chr_hezron_ram", "chr41_shobal_salma", "direct", "1 Chr 2:50–55: Caleb ben Hezron -> Hur -> Shobal & Salma (Bethlehem)"),
        E("tri_simeon", "chr41_simeon_clans", "direct", "1 Chr 4:24–43: Simeonite princes & Mt. Seir clan"),
        E("tri_reuben", "chr41_reuben_beerah", "direct", "1 Chr 5:4–6: Joel -> ... -> Prince Beerah"),
        E("tri_gad", "chr41_gad_clans", "direct", "1 Chr 5:11–17: Gadite chiefs of Bashan & Gilead"),
        E("jos_manasseh", "chr41_manasseh_east", "direct", "1 Chr 5:24: Transjordan Manasseh chiefs"),
        E("tri_issachar", "chr41_issachar_tola", "direct", "1 Chr 7:1–5: Tola -> Uzzi -> Izrahiah"),
        E("tri_benjamin", "chr41_benjamin_clans", "direct", "1 Chr 7–8: Benjamite clans of Gibeon, Moab & Aijalon"),
        E("tri_asher", "chr41_asher_shua", "direct", "1 Chr 7:30–40: Heber -> Japhlet, Shomer, Hotham & Sister Shua"),
    ]

    # =========================================================================
    # 2. GEOFFREY KEATING FORAS FEASA AR EIRINN GENEALOGIES (4. Geneal_Synch.pdf)
    # =========================================================================
    nodes += [
        N("kea_obrien_dalgcais", "O'Brien / Dal gCais Pedigree (Keating pp.2–10): Cormac Cas → Brian Boru → Turlough → Muirchertach → Donnchadh Cairbreach", "europe_norse", 19,
          "4th–17th c. CE (Keating Foras Feasa Genealogies)",
          "Munster / Thomond High-King Pedigree From Eber Finn",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf)"],
          "Complete unbroken generational stem of the Dal gCais (O'Briens, O'Carrolls, McMahons & MacNamaras) from Milesius's son Eber Finn -> Oilioll Olum -> Cormac Cas -> Cass -> Brian Boru -> Turlough -> Conor na Siudaine.",
          ["O'Brien of Thomond", "Dal gCais"], major=True),
        N("kea_maccarthy_cashel", "Eoghanacht of Cashel & Desmond (Keating): Eoghan Mor → Fiacha Muilleathan → Corc → Ceallachan of Cashel → MacCarthy Mor & O'Sullivan", "europe_norse", 19,
          "3rd–17th c. CE (Keating Foras Feasa Genealogies)",
          "Royal Eoghanacht Kings of Cashel & Munster",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf pp.3–9)"],
          "Traces the elder Milesian line of Eber Finn through Eoghan Mor -> Fiacha Muilleathan -> Corc of Cashel -> Nad Fraoich -> Ceallachan Caisil -> Carthach (eponym of MacCarthy Mor) & O'Sullivan Beara.",
          ["MacCarthy Mor", "Ceallachan of Cashel", "O'Sullivan"], major=False),
        N("kea_oneill_odonnell_columba", "Northern Ui Neill (Keating): Eoghan (O'Neill of Tyrone) & Conall Gulban (O'Donnell of Tyrconnell & St. Columba of Iona!)", "europe_norse", 18,
          "5th–17th c. CE (Keating Foras Feasa Genealogies)",
          "Most Famous Northern Irish Royal & Monastic Bloodline From Niall",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf)"],
          "Two eldest sons of Niall of the Nine Hostages: Eoghan -> Cenel nEoghain -> Hugh O'Neill (Earl of Tyrone); Conall Gulban -> Fedlimid -> St. Columba (Colum Cille, Apostle of Scotland!) & Red Hugh O'Donnell.",
          ["St. Columba (Colum Cille)", "O'Neill", "O'Donnell"], major=True),
        N("kea_oconnor_connacht", "O'Connor Kings of Connacht (Keating): Eochaid Mugmedon → Brion → Turlough Mor → Rory O'Connor (Last High King of Ireland, d. 1198)", "europe_norse", 19,
          "4th–17th c. CE (Keating Foras Feasa Genealogies)",
          "Western High Kings of Ireland (Ui Briuin)",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf)"],
          "Half-brother of Niall of the Nine Hostages -> Brión -> Ui Briuin -> Turlough Mor -> Rory O'Connor (Ruaidri Ua Conchobair, last High King of Ireland before the Anglo-Norman arrival).",
          ["Rory O'Connor", "O'Connor Connacht"], major=False),
        N("kea_macmurrough_leinster", "Kings of Leinster (Keating): Cathaoir Mor → Diarmait Mac Murchada → Princess Aoife (+ Strongbow → Isabel de Clare!)", "europe_norse", 19,
          "2nd–13th c. CE (Keating Foras Feasa Genealogies)",
          "Milesian Eremon Line Bridging Into Anglo-Norman & British Royalty!",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf)"],
          "Traces Eremon -> Ugaine Mor -> Cathaoir Mor -> Diarmait Mac Murchada, whose daughter Aoife MacMurrough wed Richard de Clare ('Strongbow') -> Isabel de Clare (+ William Marshal!) — directly injecting ancient Milesian/Gaelic royal blood into English, Scottish & European royalty!",
          ["Aoife MacMurrough", "Diarmait Mac Murchada", "Strongbow Bridge"], major=True),
        N("kea_dalriada_scotland", "Dal Riada & Ulster/Pictish Clans (Keating): Cairbre Riada → Fergus Mor mac Erc; plus Ir (Magennis/O'More) & Ith (O'Driscoll)", "europe_norse", 18,
          "3rd–17th c. CE (Keating Foras Feasa Genealogies)",
          "Irish-Scottish Dal Riada Link & Lines of Ir and Ith",
          ["Geoffrey Keating Foras Feasa ar Eirinn Genealogies (4. Geneal_Synch.pdf)"],
          "Completes the four Milesian stems in Keating: Eremon's Dal Riada branch crossing to Argyll/Scotland under Fergus Mor, plus Ir (Magennis, O'More, Conall Cearnach) and Ith (O'Driscoll).",
          ["Magennis & O'Driscoll", "Cairbre Riada"], major=False),
    ]
    edges += [
        E("eur_irl_keating_saorchlanna", "kea_obrien_dalgcais", "direct", "Keating Genealogies: Eber Finn -> Cormac Cas -> Brian Boru -> O'Brien"),
        E("irl_niall_brian_boru", "kea_obrien_dalgcais", "direct", "Brian Boru -> Turlough -> Muirchertach -> O'Brien of Thomond"),
        E("eur_irl_keating_saorchlanna", "kea_maccarthy_cashel", "direct", "Keating Genealogies: Eber Finn -> Eoghan Mor -> Ceallachan -> MacCarthy"),
        E("irl_niall_brian_boru", "kea_oneill_odonnell_columba", "direct", "Niall -> Eoghan (O'Neill) & Conall Gulban (O'Donnell & St. Columba)"),
        E("eur_irl_keating_saorchlanna", "kea_oconnor_connacht", "direct", "Eochaid Mugmedon -> Brion -> Turlough Mor -> Rory O'Connor"),
        E("eur_irl_keating_saorchlanna", "kea_macmurrough_leinster", "direct", "Eremon -> Cathaoir Mor -> Diarmait -> Aoife (+ Strongbow)"),
        E("eur_irl_keating_saorchlanna", "kea_dalriada_scotland", "direct", "Eremon (Dal Riada) + Ir (Magennis) + Ith (O'Driscoll)"),
        E("kea_dalriada_scotland", "sco_fergus_macalpin", "direct", "Keating Dal Riada stem -> Fergus Mor mac Erc -> Scottish Kings"),
    ]

    return {
        "module": "41_1chronicles_keating_deep_extract",
        "title": "1 Chronicles 2–8 Exhaustive Sub-Clans (Jarha the Egyptian, Bithiah dau. of Pharaoh, Simeon, Reuben, Gad, Benjamin, Asher) & Geoffrey Keating's Complete Irish Gaelic Genealogies",
        "nodes": nodes,
        "edges": edges,
    }
