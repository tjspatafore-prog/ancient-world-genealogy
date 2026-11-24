"""
Module 17: Complete Mesopotamian Royal Chronicles —
1. Complete Assyrian King List (AKL, all 116 kings from Tudiya & Adamu to Ashur-uballit II)
   from Regine Pruzsinszky (045_068 Pruzsinszky.pdf) & Eusebius's Assyrian Chronicle.
2. Complete Remaining Sumerian King List Dynasties (Ur I, Awan, Kish II, Hamazi, Uruk II,
   Ur II, Adab, Mari, Kish III [Queen Ku-Baba], Akshak, Kish IV, Uruk III [Lugal-zagesi],
   Uruk IV, Gutium, Uruk V [Utu-hengal], Isin I, plus Lagash/Gudea) from Thorkild Jacobsen (as11.pdf).
3. Complete Babylonian Dynasties (Babylon I Amorite, II Sealand, III Kassite, IV Isin II,
   Neo-Babylonian/Chaldean) from L.W. King (chroniclesconcer01londuoft.pdf) & Eusebius.
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. COMPLETE ASSYRIAN KING LIST (AKL, Pruzsinszky pp. 45-68, Tables 17a-17b)
    # -------------------------------------------------------------------------
    # Group 1: The 17 Kings Who Lived in Tents (AKL 1-17)
    akl_tents = [
        ("akl_01_tudiya", "1. Tudiya (1st Assyrian Tent-King)", 7, "c. 2400 BCE (AKL 1)", "First King of Assyria (Ebla Treaty Attested!)", "First of the '17 kings who lived in tents' in the Assyrian King List; historically attested in the Ebla archives concluding a trade treaty with Vizier Ibrium of Ebla!", {"major": True, "altNames": ["Tudia", "Dudiya"]}),
        ("akl_02_adamu", "2. Adamu (2nd Assyrian Tent-King)", 7, "c. 2380 BCE (AKL 2)", "West Semitic/Assyrian Tent-King (Cognate of Adam!)", "Second king of Assyria in the AKL; earliest known historical ruler bearing the Semitic name Adamu ('Man/Red Earth'), cognate with Biblical Adam!", {"major": True, "altNames": ["Cognate: Adam"]}),
        ("akl_03_08_tents", "3–8. Yangi, Suhlamu, Harharu, Mandaru, Imsu & Harsu", 7, "c. 2360-2260 BCE (AKL 3-8)", "Assyrian Tent-Dwelling Patriarchal Kings", "Kings 3-8 of the AKL tent-dwellers, reflecting Amorite/West Semitic pastoral confederacies.", {"altNames": ["Yangi", "Suhlamu", "Harharu", "Mandaru", "Imsu", "Harsu"]}),
        ("akl_09_10_didanu_hanu", "9–10. Didanu (Tidnum) & Hanu (Hana)", 7, "c. 2240-2200 BCE (AKL 9-10)", "Eponymous Amorite Tribal Ancestors (Cognate: Dedan?)", "Didanu corresponds to the Amorite tribe Tidnum/Ditanu (also ancestral to the Ugaritic royal cult and compared with Biblical Dedan); Hanu corresponds to the Middle Euphrates tribe of Hana.", {"altNames": ["Didanu / Tidnum", "Hanu"]}),
        ("akl_11_15_tents", "11–15. Zuabu, Nuabu, Abazu, Belu & Azarah", 7, "c. 2180-2100 BCE (AKL 11-15)", "Late Tent-Dwelling Kings of Assyria", "Kings 11-15 of the canonical Assyrian King List (Pruzsinszky Table 17a).", {"altNames": ["Zuabu", "Nuabu", "Abazu", "Belu", "Azarah"]}),
        ("akl_16_ushpia", "16. Ushpia (Builder of the Temple of Ashur)", 8, "c. 2080 BCE (AKL 16)", "Founder of the E-hursag-kurkurra Temple of Ashur", "Credited in inscriptions of Shalmaneser I and Esarhaddon as the earliest founder of the great Temple of the god Ashur in Assur.", {"major": True, "altNames": ["Ušpia"]}),
        ("akl_17_apiashal", "17. Apiashal (Son of Ushpia — Bridge to Ancestors)", 8, "c. 2060 BCE (AKL 17)", "Last Tent-King & First of the 10 Ancestors", "Appears at both the end of Section 1 (17 tent-dwellers) and the beginning of Section 2 (10 kings whose fathers are known), linking Shamshi-Adad I's pedigree back to Ushpia!", {"altNames": ["Apiašal"]}),
    ]
    add_chain(nodes, edges, akl_tents, start_parent="bib_asshur", start_edge_type="cognate",
              start_edge_label="Genesis 10:11 Asshur <-> Canonical Assyrian King List (AKL)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Assyrian King List (Pruzsinszky Table 17a)"])

    # Group 2: 10 Kings Whose Fathers Are Known (AKL 18-26, Shamshi-Adad I's Amorite Ancestors!)
    akl_ancestors = [
        ("akl_18_24_ancestors", "18–24. Hale, Samani, Hayani, Ilu-Mer, Yakmesi, Yakmeni & Yazkur-El", 8, "c. 2050-1900 BCE (AKL 18-24)", "Patrilineal Ancestors of Shamshi-Adad I", "Listed in reverse genealogical order ('PN1 son of PN2') in AKL Section 2 to trace the Amorite royal pedigree of Shamshi-Adad I (Pruzsinszky pp. 48, 51).", {"altNames": ["Hale", "Samani", "Hayani", "Ilu-Mer", "Yakmesi", "Yakmeni", "Yazkur-El"]}),
        ("akl_25_26_ilukabkabi_aminu", "25–26. Ilu-kabkabi & Aminu (Father & Brother of Shamshi-Adad I)", 9, "c. 1850-1810 BCE (AKL 25-26)", "Amorite King of Ekallatum / Terqa", "Ilu-kabkabi fathered Aminu and the great conqueror Shamshi-Adad I.", {"altNames": ["Ilu-kabkabi", "Aminu"]}),
    ]
    add_chain(nodes, edges, akl_ancestors, start_parent="akl_17_apiashal", start_edge_type="direct",
              start_edge_label="AKL Section 2: 'Ten kings whose fathers are known'",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17a)"])

    # Group 3: 6 Kings of Unknown Eponyms & Old Assyrian Puzur-Ashur Dynasty (AKL 27-38)
    akl_old = [
        ("akl_27_29_sulili_kikia", "27–29. Sulili, Kikia & Akia (End of Ur III Period)", 9, "c. 2025-1980 BCE (AKL 27-29)", "Early City-Rulers of Assur (Wall Builder Kikia)", "Kikia built the city wall of Assur; Sulili (son of Aminu) marks Assur's independence after Ur III.", {"altNames": ["Sulili", "Kikia", "Akia"]}),
        ("akl_30_32_puzur_ilushuma", "30–32. Puzur-Ashur I → Shalim-ahum → Ilushuma", 9, "c. 1975-1935 BCE (AKL 30-32)", "Founders of the Old Assyrian Merchant Dynasty", "Ilushuma established free trade privileges for Akkadian merchants and founded the Old Assyrian trading empire.", {"altNames": ["Puzur-Ashur I", "Shalim-ahum", "Ilushuma"]}),
        ("akl_33_34_erishum_ikunum", "33–34. Erishum I (40 yrs, First Eponym List!) → Ikunum (15 yrs)", 10, "c. 1934-1880 BCE (AKL 33-34; KEL)", "First King with Kültepe Eponym List (līmu) Chronology", "Erishum I rebuilt the Ashur Temple and inaugurated the Kültepe Eponym List (KEL), giving exact year-by-year dating from 1974/1934 BCE!", {"altNames": ["Erishum I", "Ikunum"]}),
        ("akl_35_38_sargon1_naramsin", "35–38. Sargon I (40 yrs) → Puzur-Ashur II → Naram-Sin of Assur → Erishum II", 10, "c. 1880-1808 BCE (AKL 35-38)", "Height of Old Assyrian Anatolian Colony Trade (Kanesh)", "Named after the great Akkadian kings Sargon & Naram-Sin; overthrown in 1808 BCE by Shamshi-Adad I.", {"altNames": ["Sargon I of Assyria", "Puzur-Ashur II", "Naram-Sin of Assyria", "Erishum II"]}),
        ("akl_39_40_shamshi_adad1", "39–40. Shamshi-Adad I (33 yrs) → Ishme-Dagan I (40 yrs) & Yasmah-Adad", 11, "1808-1736 BCE (AKL 39-40; Mari Archives)", "Founder of the Kingdom of Upper Mesopotamia (Contemporary of Hammurabi!)", "Son of Ilu-kabkabi; conquered Assur, Mari, and Shubat-Enlil. His son Ishme-Dagan I ruled Ekallatum/Assur while Yasmah-Adad ruled Mari (famed in the Mari Letters!).", {"major": True, "altNames": ["Šamšī-Adad I", "Ishme-Dagan I", "Yasmah-Adad"]}),
        ("akl_41_47_usurpers", "41–47. Ashur-dugul & Six Usurpers (Ashur-apla-idi, Nasir-Sin, Sin-namir, Ipqi-Ishtar, Adad-salulu, Adasi)", 11, "c. 1735-1700 BCE (AKL 41-47)", "Interregnum & Adasi (Progenitor of the 1,000-Year Adaside Dynasty!)", "Six 'sons of a nobody' ruled briefly; the last, Adasi, became the revered ancestor of Assyria's royal Adaside house down to Esarhaddon!", {"altNames": ["Ashur-dugul", "Adasi"]}),
        ("akl_48_53_belubani", "48–53. Belu-bani (son of Adasi) → Libaya → Sharma-Adad I → Iptar-Sin → Bazaya → Lullaya", 12, "c. 1700-1618 BCE (AKL 48-53)", "Early Adaside Kings of Assur", "Belu-bani (10 yrs) founded the unbroken Adaside royal dynasty; Bazaya ruled 28 years.", {"altNames": ["Belu-bani", "Libaya", "Sharma-Adad I", "Iptar-Sin", "Bazaya", "Lullaya"]}),
        ("akl_54_66_old_late", "54–66. Kidin-Ninua → Sharma-Adad II → Erishum III → Shamshi-Adad II → Ishme-Dagan II → Shamshi-Adad III → Ashur-nirari I → Puzur-Ashur III → Enlil-nasir I → Nur-ili → Ashur-shaduni → Ashur-rabi I → Ashur-nadin-ahhe I", 13, "c. 1617-1431 BCE (AKL 54-66)", "Late Old Assyrian / Mitanni Vassalage Kings", "Preserved unbroken Adaside patrilineal continuity through the Mitanni era (Pruzsinszky Table 17b).", {"altNames": ["Kidin-Ninua", "Ashur-nirari I", "Puzur-Ashur III", "Ashur-rabi I"]}),
        ("akl_67_72_pre_middle", "67–72. Enlil-nasir II → Ashur-nirari II → Ashur-bel-nisheshu → Ashur-rim-nisheshu → Ashur-nadin-ahhe II → Eriba-Adad I", 14, "c. 1430-1364 BCE (AKL 67-72)", "Transition to Middle Assyrian Independence", "Eriba-Adad I (27 yrs) broke Mitanni supremacy, setting the stage for his son Ashur-uballit I.", {"altNames": ["Enlil-nasir II", "Ashur-bel-nisheshu", "Eriba-Adad I"]}),
    ]
    add_chain(nodes, edges, akl_old, start_parent="akl_25_26_ilukabkabi_aminu", start_edge_type="expansion",
              start_edge_label="Old Assyrian Dynasty & Shamshi-Adad I (AKL 27-72)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Tables 17a-b)"])

    # Group 4: Middle Assyrian Empire (AKL 73-97)
    akl_middle = [
        ("akl_73_76_ashuruballit1", "73–76. Ashur-uballit I (Amarna Letters!) → Enlil-nirari → Arik-den-ili → Adad-nirari I", 15, "1363-1274 BCE (AKL 73-76; Amarna Letters)", "Founders of the Middle Assyrian Great Power", "Ashur-uballit I (36 yrs) wrote directly to Pharaoh Akhenaten as 'Great King' (EA 15-16) and married his daughter Muballitat-Sherua to Kassite Babylon! Adad-nirari I (32 yrs) annexed Hanigalbat (Mitanni).", {"major": True, "altNames": ["Aššur-uballiṭ I", "Adad-nirari I"]}),
        ("akl_77_78_shalmaneser1_tukulti", "77–78. Shalmaneser I (30 yrs) → Tukulti-Ninurta I (37 yrs, Conqueror of Babylon)", 15, "1273-1207 BCE (AKL 77-78)", "Peak of the Middle Assyrian Empire", "Shalmaneser I founded Kalhu (Nimrud); Tukulti-Ninurta I captured Kassite King Kashtiliash IV of Babylon and built Kar-Tukulti-Ninurta — often compared with the Nimrod legend!", {"major": True, "altNames": ["Shalmaneser I", "Tukulti-Ninurta I"]}),
        ("akl_79_86_ninurta_apil", "79–86. Ashur-nadin-apli → Ashur-nirari III → Enlil-kudurri-usur → Ninurta-apil-Ekur → Ashur-dan I (46 yrs) → Ninurta-tukulti-Ashur → Mutakkil-Nusku → Ashur-resh-ishi I", 16, "1206-1115 BCE (AKL 79-86)", "Bronze Age Collapse Survival & Revival", "Ninurta-apil-Ekur (descendant of Eriba-Adad I) restored dynastic stability; Ashur-dan I ruled 46 years; Ashur-resh-ishi I defeated Nebuchadnezzar I of Babylon.", {"altNames": ["Ninurta-apil-Ekur", "Ashur-dan I", "Ashur-resh-ishi I"]}),
        ("akl_87_97_tiglath1_to_2", "87–97. Tiglath-Pileser I (39 yrs) → Ashared-apil-Ekur → Ashur-bel-kala → Eriba-Adad II → Shamshi-Adad IV → Ashurnasirpal I → Shalmaneser II → Ashur-nirari IV → Ashur-rabi II (41 yrs) → Ashur-resh-ishi II → Tiglath-Pileser II", 16, "1114-935 BCE (AKL 87-97)", "Tiglath-Pileser I's Mediterranean Campaigns & Aramean Era", "Tiglath-Pileser I marched to the Mediterranean, hunted elephants in Syria, and compiled the Middle Assyrian Laws. Followed by 140 years of Aramean pressure until Ashur-dan II.", {"altNames": ["Tiglath-Pileser I", "Ashur-bel-kala", "Ashur-rabi II", "Tiglath-Pileser II"]}),
    ]
    add_chain(nodes, edges, akl_middle, start_parent="akl_67_72_pre_middle", start_edge_type="direct",
              start_edge_label="Middle Assyrian Empire (AKL 73-97)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17b)"])

    # Group 5: Neo-Assyrian Empire (AKL 98-116)
    akl_neo = [
        ("akl_98_101_ashurnasirpal2", "98–101. Ashur-dan II → Adad-nirari II → Tukulti-Ninurta II → Ashurnasirpal II (Nimrud Palace)", 17, "934-859 BCE (AKL 98-101)", "Founders of the Neo-Assyrian Empire", "Adad-nirari II inaugurated the unbroken Eponym Canon (911-649 BCE); Ashurnasirpal II (25 yrs) built the magnificent Northwest Palace at Kalhu (Nimrud).", {"major": True, "altNames": ["Adad-nirari II", "Ashurnasirpal II"]}),
        ("akl_102_shalmaneser3", "102. Shalmaneser III (35 yrs — Black Obelisk of Jehu & Battle of Qarqar!)", 17, "858-824 BCE (AKL 102; Kurkh Monolith; Black Obelisk)", "First Assyrian King Explicitly Naming Israelite Kings Ahab & Jehu", "Fought King Ahab of Israel & Hadadezer of Damascus at Qarqar (853 BCE); his Black Obelisk depicts King Jehu of Israel ('son of Omri') bowing in tribute — the ONLY contemporary depiction of an Israelite king!", {"major": True, "altNames": ["Šalmaneser III", "Black Obelisk"]}),
        ("akl_103_104_semiramis", "103–104. Shamshi-Adad V & Queen Shammuramat (Semiramis!) → Adad-nirari III", 17, "823-783 BCE (AKL 103-104; Herodotus; Eusebius)", "Historical Queen Semiramis & Adad-nirari III (Tribute of Joash of Israel)", "Babylonian princess Shammuramat (Greek: Semiramis!) served as regent/queen mother alongside her son Adad-nirari III (28 yrs), who collected tribute from Jehoash of Israel and Ben-Hadad of Damascus.", {"major": True, "altNames": ["Queen Shammuramat", "Semiramis", "Adad-nirari III"]}),
        ("akl_105_107_eclipse_kings", "105–107. Shalmaneser IV → Ashur-dan III (763 BCE Bur-Sagale Solar Eclipse!) → Ashur-nirari V", 17, "782-745 BCE (AKL 105-107)", "Anchor of All Ancient Near Eastern Chronology (June 15, 763 BCE Eclipse)", "The Assyrian Eponym List records a total solar eclipse in Sivan under Ashur-dan III (June 15, 763 BCE), astronomically locking ALL Assyrian and Biblical monarchic dates!", {"altNames": ["Shalmaneser IV", "Ashur-dan III (763 BCE Eclipse)", "Ashur-nirari V"]}),
        ("akl_108_109_tp3_shalm5", "108–109. Tiglath-Pileser III (Pul, 745-727 BCE) → Shalmaneser V (726-722 BCE, Siege of Samaria)", 17, "745-722 BCE (AKL 108-109; 2 Kings 15-17)", "Final Kings of Canonical AKL (SDAS Tablet) & Biblical 'Pul'", "Tiglath-Pileser III (called 'Pul' in 2 Kings 15:19) created the provincial empire; his son Shalmaneser V besieged Samaria (final king on the SDAS AKL tablet!).", {"altNames": ["Tiglath-Pileser III (Pul)", "Shalmaneser V"]}),
        ("akl_110_116_sargonids", "110–116. Sargonid Dynasty: Sargon II → Sennacherib → Esarhaddon → Ashurbanipal → Ashur-etil-ilani → Sin-shar-ishkun → Ashur-uballit II", 17, "722-609 BCE (Neo-Assyrian Chronicles; 2 Kings 18-19; Isaiah 20)", "Final Imperial Dynasty of Nineveh (Library of Ashurbanipal)", "Sargon II completed the conquest of Israel (722 BCE); Sennacherib besieged Hezekiah's Jerusalem (701 BCE); Esarhaddon conquered Egypt (671 BCE); Ashurbanipal built the great Library of Nineveh (preserving Gilgamesh!). Fell to Babylon & Media in 612-609 BCE.", {"major": True, "altNames": ["Sargon II", "Sennacherib", "Esarhaddon", "Ashurbanipal", "Ashur-uballit II"]}),
    ]
    add_chain(nodes, edges, akl_neo, start_parent="akl_87_97_tiglath1_to_2", start_edge_type="direct",
              start_edge_label="Neo-Assyrian Empire (AKL 98-116)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17b)", "Neo-Assyrian Chronicles"])

    # -------------------------------------------------------------------------
    # 2. COMPLETE REMAINING SUMERIAN KING LIST DYNASTIES (Jacobsen AS 11, pp. 93-127)
    # -------------------------------------------------------------------------
    skl_rest = [
        ("skl_ur1_full", "Ur I Dynasty: Mesannepada → Aannepada → Meskiagnunna → Elulu → Balulu", 7, "c. 2560-2400 BCE (SKL Col. iii-iv, Jacobsen pp. 93-95)", "First Dynasty of Ur (Royal Tombs of Ur Era)", "5 kings (177 yrs): Mesannepada -> son Aannepada (restored from Tummal Chronicle & inscriptions!) -> Meskiagnunna -> Elulu -> Balulu.", {"altNames": ["Aannepada", "Elulu", "Balulu"]}),
        ("skl_awan_kish2_hamazi", "Awan (3 Kings), Kish II (8 Kings: Susuda, Dadasig, Magalgalla, Kalbum, Tuge, Enbi-Ishtar, Lugalmu) & Hamazi (Hatanish)", 7, "c. 2500-2400 BCE (SKL Col. iv, Jacobsen pp. 95-99)", "Early Dynastic Hegemonies of Elam, Kish & Zagros", "Awan (Elamite dynasty, 3 kings, 356 yrs), Kish II (8 kings incl. Kalbum son of Magalgalla), and Hamazi (King Hatanish, later deified in god-list AN:Anum!).", {"altNames": ["Hatanish of Hamazi", "Enbi-Ishtar", "Magalgalla"]}),
        ("skl_uruk2_ur2_adab_mari", "Uruk II (Enshakushanna, Lugal-kinishe-dudu, Lugal-kisal-si), Ur II (Kaku), Adab (Lugal-annemundu) & Mari (Ansud)", 8, "c. 2450-2350 BCE (SKL Col. iv-v, Jacobsen pp. 100-103)", "Pre-Sargonic City-State Empires", "Enshakushanna of Uruk; Lugal-kinishe-dudu & son Lugal-kisal-si (ruled both Uruk II & Ur II!); Lugal-annemundu of Adab (90 yrs, legendary conqueror from Elam to Cedar Mountain); Ansud & 5 kings of Mari.", {"altNames": ["Enshakushanna", "Lugal-annemundu", "Ansud of Mari"]}),
        ("skl_kubaba_kish3", "Queen Ku-Baba (Kish III — Sole Female Monarch in the Sumerian King List!)", 8, "c. 2400 BCE (SKL Col. v 36-41, Jacobsen pp. 104-105)", "Tavern-Keeper Who Consolidated Kish & Founded Kish III–IV", "Ku(g)-Baba ('Baba-ellit', former alewife/barmaid, reigned 100 yrs) is the ONLY woman listed as sovereign king in the entire Sumerian King List; mother of Puzur-Sin & grandmother of Ur-Zababa!", {"major": True, "altNames": ["Kug-Baba", "Kubaba"]}),
        ("skl_akshak_kish4", "Akshak (Unzi, Undalulu, Ur-ur, Puzur-Nirah, Ishu-il, Shu-Sin) & Kish IV (Puzur-Sin → Ur-Zababa → Simu-dar → Usi-watar → Eshtar-muti → Ishme-Shamash → Nannia)", 8, "c. 2400-2334 BCE (SKL Col. v-vi, Jacobsen pp. 106-111)", "Dynasty of Ku-Baba's Descendants & Master of Young Sargon", "Ku-Baba's son Puzur-Sin -> son Ur-Zababa of Kish, whose royal cupbearer was Sargon of Akkad! Contemporary with Akshak's 6 kings.", {"altNames": ["Puzur-Sin", "Ur-Zababa", "Puzur-Nirah"]}),
        ("skl_uruk3_lugalzagesi", "Uruk III: Lugal-zagesi (25 yrs — First Unifier of Sumer Before Sargon)", 9, "c. 2359-2335 BCE (SKL Col. vi 24-27, Jacobsen pp. 110-111)", "Ensi of Umma & Sole King of Uruk III", "United all of Sumer from the Lower Sea (Persian Gulf) to the Upper Sea (Mediterranean) before being defeated and led in a neck-stock to Nippur by Sargon of Akkad.", {"major": True, "altNames": ["Lugal-zage-si"]}),
        ("skl_akkad_late", "Late Akkad Interregnum (Igigi, Nanum, Imi, Elulu) → Dudu → Shu-Durul", 10, "c. 2193-2154 BCE (SKL Col. vii 1-12, Jacobsen pp. 114-115)", "Final Rulers of the Sargonic Akkadian Empire", "'Who was king? Who was not king?' Four rival claimants reigned 3 years before Dudu (21 yrs) and his son Shu-Durul (15 yrs) closed the Dynasty of Agade.", {"altNames": ["Igigi", "Dudu of Akkad", "Shu-Durul"]}),
        ("skl_uruk4_gutium_uruk5", "Uruk IV (Ur-nigin → Ur-gigir → Kudda → Puzur-ili → Ur-Utu), 21 Gutian Kings (Erridupizir to Tirigan) & Uruk V (Utu-hegal)", 10, "c. 2154-2112 BCE (SKL Col. vii-viii, Jacobsen pp. 114-123)", "Gutian Domination & Sumerian Liberation by Utu-hegal", "21 Gutian rulers from the Zagros mountains (Erridupizir, Imta, Inkishush, Sarlagab, Iarlagab, Hablum -> Puzur-Sin, Si'um, Tirigan [40 days]) expelled by Utu-hegal of Uruk V — whose general/relative Ur-Nammu founded Ur III!", {"major": True, "altNames": ["Gutian Dynasty", "Tirigan", "Utu-hegal"]}),
        ("skl_lagash_gudea", "Independent Lagash II: Ur-Nanshe → Eannatum (Stele of Vultures) → Urukagina → Gudea of Lagash", 10, "c. 2500-2120 BCE (Lagash Royal Inscriptions)", "Sumerian Reformers & Statue-Builder Gudea", "Omitted from the partisan SKL: Ur-Nanshe, Eannatum, law-reformer Urukagina (oldest legal code against corruption), and pious Ensi Gudea of Lagash (contemporary of Ur-Nammu).", {"altNames": ["Eannatum", "Urukagina", "Gudea of Lagash"]}),
        ("skl_isin1_full", "Isin I Dynasty (All 15 Kings): Ishbi-Erra → Shu-ilishu → Iddin-Dagan → Ishme-Dagan → Lipit-Ishtar → Ur-Ninurta → Bur-Sin → Lipit-Enlil → Erra-imitti → Enlil-bani → Zambia → Iter-pisha → Ur-dukuga → Sin-magir → Damiq-ilishu", 11, "c. 2017-1794 BCE (SKL Col. viii 23-45, Jacobsen pp. 124-127)", "Final Dynasty of the Sumerian King List (Code of Lipit-Ishtar)", "Ishbi-Erra broke away from Ibbi-Sin of Ur III. Lipit-Ishtar issued the Sumerian Law Code (180 yrs before Hammurabi!). Gardener Enlil-bani succeeded Erra-imitti (substitute-king ritual!). Ended when Rim-Sin of Larsa conquered Damiq-ilishu.", {"major": True, "altNames": ["Ishbi-Erra", "Lipit-Ishtar", "Enlil-bani", "Damiq-ilishu"]}),
    ]
    add_chain(nodes, edges, skl_rest, start_parent="mes_mesannepada", start_edge_type="direct",
              start_edge_label="Post-Diluvian Sumerian King List Continuation (Jacobsen AS 11)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Sumerian King List (Jacobsen AS 11)"])

    # -------------------------------------------------------------------------
    # 3. COMPLETE BABYLONIAN DYNASTIES I–X (L.W. King Vol. I, pp. 58-222 & Eusebius)
    # -------------------------------------------------------------------------
    bab_all = [
        ("bab_dyn1_amorite", "Babylon I (All 11 Amorite Kings): Sumu-abum → Sumu-la-El → Sabium → Apil-Sin → Sin-muballit → Hammurabi → Samsu-iluna → Abi-eshuh → Ammi-ditana → Ammi-saduqa → Samsu-ditana", 11, "1894-1595 BCE (L.W. King Vol. I pp. 95, 144-150)", "Complete Old Babylonian Amorite Dynasty (Venus Tablet of Ammi-saduqa!)", "Sumu-abum (contemporary of Ilushuma of Assyria) -> Hammurabi (defeated Rim-Sin of Larsa, son of Kudur-Mabuk!) -> son Samsu-iluna -> Abi-eshuh -> Ammi-ditana -> Ammi-saduqa (astronomical Venus Tablet!) -> Samsu-ditana (overthrown by Hittite King Mursili I in 1595 BCE!).", {"major": True, "altNames": ["Sumu-la-El", "Sin-muballit", "Samsu-iluna", "Ammi-saduqa", "Rim-Sin of Larsa"]}),
        ("bab_dyn2_sealand", "Babylon II (First Sealand Dynasty, All 11 Kings): Iluma-ilu → Itti-ili-nibi → Damqi-ilishu → Ishkibal → Shushshi → Gulkishar → Peshgaldaramesh → Ayadaragalama → Akurduana → Melamkurkurra → Ea-gamil", 12, "c. 1732-1460 BCE (L.W. King Vol. I pp. 96, 151-155)", "Southern Marshland Dynasty Overlapping Babylon I & Kassites", "Iluma-ilu fought Samsu-iluna & Abi-eshuh; Gulkishar anchored Babylonian chronology (696 yrs before Nebuchadnezzar I); last king Ea-gamil invaded Elam and was overthrown by Kassite Ulam-Buriash!", {"altNames": ["Iluma-ilu", "Gulkishar", "Ea-gamil"]}),
        ("bab_dyn3_kassite", "Babylon III (Kassite Dynasty, 576 yrs): Gandash → Agum I → Kashtiliash I → Agum II (Restored Marduk!) → Burna-Buriash I → Ulam-Buriash → Burna-Buriash II (Amarna Letters!) → Kurigalzu → Kudur-Enlil → Shagarakti-Shuriash → Meli-Shipak", 14, "c. 1595-1155 BCE (L.W. King Vol. I pp. 79, 101-113, 151-153)", "Longest-Reigning Dynasty in Babylonian History (Zagros Mountain Origin)", "Agum II (son of Urzigurumash) retrieved Marduk's statue from Hani; Ulam-Buriash conquered the Sealand; Burna-Buriash II corresponded with Akhenaten & married Ashur-uballit I's daughter!", {"major": True, "altNames": ["Gandash", "Agum II", "Ulam-Buriash", "Burna-Buriash II", "Meli-Shipak"]}),
        ("bab_dyn4_isin2", "Babylon IV (Isin II): Nebuchadnezzar I → Enlil-nadin-apli → Marduk-nadin-ahhe → Marduk-shapik-zeri → Adad-apla-iddina", 16, "1157-1026 BCE (L.W. King Vol. I pp. 89, 190-193)", "Revival of Native Babylon & Recovery of Marduk from Elam", "Nebuchadnezzar I sacked Susa in Elam and restored Marduk to Babylon; Adad-apla-iddina (Aramean/son of Itti-Marduk-balatu) married his daughter to Assyrian King Ashur-bel-kala.", {"altNames": ["Nebuchadnezzar I", "Marduk-nadin-ahhe", "Adad-apla-iddina"]}),
        ("bab_dyn5_8_inter", "Babylon V–IX: 2nd Sealand (Simbar-Shipak), Bazi Dynasty, Elamite Mar-biti-apla-usur, Nabu-mukin-apli, Nabonassar (747 BCE Era!) & Merodach-Baladan II", 17, "1025-626 BCE (L.W. King Vol. I pp. 184-208; Eusebius)", "Ptolemaic Astronomical Era of Nabonassar & Chaldean Resistance", "King Nabonassar (747 BCE) inaugurated the famous Babylonian astronomical diaries & Ptolemy's Almagest Canon! Chaldean hero Merodach-Baladan II (Marduk-apla-iddina II) sent envoys to King Hezekiah of Judah (2 Kgs 20:12) against Assyria.", {"altNames": ["Simbar-Shipak", "Nabonassar (747 BCE)", "Merodach-Baladan II", "Mushezib-Marduk"]}),
        ("bab_dyn10_chaldean", "Babylon X (Neo-Babylonian / Chaldean Empire): Nabopolassar → Nebuchadnezzar II → Amel-Marduk (Evil-Merodach) → Neriglissar → Labashi-Marduk → Nabonidus & Crown Prince Belshazzar", 17, "626-539 BCE (Babylonian Chronicles; Eusebius; 2 Kings 24-25; Daniel 5)", "Final Native Babylonian Empire (Hanging Gardens & Fall to Cyrus, 539 BCE)", "Nabopolassar allied with Cyaxares of Media to destroy Nineveh (612 BCE); Nebuchadnezzar II built Babylon's Ishtar Gate & exiled Judah (586 BCE); Nabonidus (+ Queen Nitocris / Adad-guppi) & son Belshazzar fell to Cyrus the Great in 539 BCE!", {"major": True, "altNames": ["Nabopolassar", "Amel-Marduk", "Neriglissar", "Nabonidus", "Belshazzar"]}),
    ]
    add_chain(nodes, edges, bab_all, start_parent="mes_hammurabi", start_edge_type="direct",
              start_edge_label="Complete Babylonian Dynastic Sequence (L.W. King Vol. I)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Early Babylonian Chronicles (L.W. King Vol. I)", "Eusebius Chronicle"])

    # Additional SKL & Babylonian cross-links
    edges += [
        E("skl_uruk3_lugalzagesi", "mes_sargon", "expansion", "Sargon of Akkad (former cupbearer of Ur-Zababa) defeats Lugal-zagesi"),
        E("mes_sharkalisharri", "skl_akkad_late", "direct", "Akkad Interregnum -> Dudu -> Shu-Durul (SKL Col. vii)"),
        E("skl_uruk4_gutium_uruk5", "mes_urnammu", "expansion", "Utu-hegal expels Gutians -> Ur-Nammu founds Ur III Dynasty"),
        E("mes_ibbisin", "skl_isin1_full", "expansion", "Fall of Ur III -> Ishbi-Erra founds Isin I Dynasty"),
        E("bab_dyn3_kassite", "eg_akhenaten", "cognate", "Amarna Letters EA 6-11 (Burna-Buriash II writes to Akhenaten)"),
        E("bab_dyn3_kassite", "akl_73_76_ashuruballit1", "direct", "Kassite royal marriage with Ashur-uballit I's daughter Muballitat-Sherua"),
        E("bab_dyn5_8_inter", "kg_j9_hezekiah", "cognate", "Merodach-Baladan II sends letters & gifts to King Hezekiah (2 Kgs 20:12)"),
        E("bab_dyn10_chaldean", "for_nebuchadnezzar", "direct", "Full Chaldean Dynasty from Nabopolassar to Belshazzar"),
        E("bab_dyn10_chaldean", "ir_cyrus", "cognate", "Cyrus Cylinder: Cyrus the Great captures Babylon from Nabonidus & Belshazzar (539 BCE)"),
    ]

    # Cross-links from AKL to existing Biblical, Egyptian, and Mesopotamian nodes
    edges += [
        E("bib_adam", "akl_02_adamu", "cognate", "West Semitic name Adamu (AKL #2) <-> Hebrew Adam"),
        E("mes_hammurabi", "akl_39_40_shamshi_adad1", "cognate", "Contemporaries & treaty partners (Mari Archives, c. 1780 BCE)"),
        E("akl_73_76_ashuruballit1", "eg_akhenaten", "cognate", "Amarna Letters EA 15-16 (Ashur-uballit I writes to Akhenaten)"),
        E("akl_102_shalmaneser3", "kg_i3_omri_ahab", "cognate", "Battle of Qarqar (853 BCE) — Kurkh Monolith names 'Ahab the Israelite'"),
        E("akl_102_shalmaneser3", "kg_i4_jehu", "cognate", "Black Obelisk of Shalmaneser III (841 BCE) depicts King Jehu of Israel"),
        E("akl_108_109_tp3_shalm5", "for_neo_assyria", "cognate", "Biblical 'Pul' / Tiglath-Pileser III & Shalmaneser V"),
        E("akl_110_116_sargonids", "kg_j9_hezekiah", "cognate", "Sennacherib's Taylor Prism & 2 Kings 18-19 (701 BCE Siege of Jerusalem)"),
        E("akl_110_116_sargonids", "af_taharqa", "cognate", "Esarhaddon & Ashurbanipal defeat Kushite Pharaoh Taharqa in Egypt (671-664 BCE)"),
        E("akl_110_116_sargonids", "mes_assyria_kings", "direct", "Completes the Assyrian royal succession"),
    ]

    # -------------------------------------------------------------------------
    # 4. EXHAUSTIVE INDIVIDUAL-BY-INDIVIDUAL ROSTERS (Every Named King in AKL, SKL & Babylon!)
    # -------------------------------------------------------------------------
    add_roster(nodes, edges, "akl_03_08_tents", "aklr_t1", "mesopotamian", 7, "c. 2360-2260 BCE (AKL)", "Assyrian Tent-Dwelling King", ["Assyrian King List (Pruzsinszky Table 17a)"], [
        "Yangi (AKL #3)", "Suhlamu (AKL #4)", "Harharu (AKL #5)", "Mandaru (AKL #6)", "Imsu (AKL #7)", "Harsu (AKL #8)",
        "Didanu / Tidnum (AKL #9)", "Hanu (AKL #10)", "Zuabu (AKL #11)", "Nuabu (AKL #12)", "Abazu (AKL #13)", "Belu (AKL #14)", "Azarah (AKL #15)"
    ], edge_type="expansion", edge_label="AKL Tent-Dwelling King (Pruzsinszky Table 17a)")

    add_roster(nodes, edges, "akl_18_24_ancestors", "aklr_anc", "mesopotamian", 8, "c. 2050-1850 BCE (AKL)", "Patrilineal Ancestor of Shamshi-Adad I", ["Assyrian King List (Pruzsinszky Table 17a)"], [
        "Hale (AKL #18)", "Samani (AKL #19)", "Hayani (AKL #20)", "Ilu-Mer (AKL #21)", "Yakmesi (AKL #22)", "Yakmeni (AKL #23)", "Yazkur-El (AKL #24)", "Ilu-kabkabi (AKL #25)", "Aminu (AKL #26)"
    ], edge_type="direct", edge_label="AKL Ancestor Sequence (Section 2)")

    add_roster(nodes, edges, "akl_48_53_belubani", "aklr_old", "mesopotamian", 12, "c. 2025-1431 BCE (AKL)", "Old Assyrian King", ["Assyrian King List (Pruzsinszky Tables 17a-b)"], [
        "Sulili (AKL #27)", "Kikia (AKL #28)", "Akia (AKL #29)", "Puzur-Ashur I (AKL #30)", "Shalim-ahum (AKL #31)", "Ilushuma (AKL #32)",
        "Erishum I (AKL #33, 40 yrs)", "Ikunum (AKL #34, 15 yrs)", "Sargon I of Assyria (AKL #35, 40 yrs)", "Puzur-Ashur II (AKL #36, 8 yrs)",
        "Naram-Sin of Assyria (AKL #37, 44/55 yrs)", "Erishum II (AKL #38, 10 yrs)", "Ishme-Dagan I (AKL #40, 40 yrs)", "Ashur-dugul (AKL #41, 6 yrs)",
        "Adasi (AKL #47, Adaside Founder)", "Belu-bani (AKL #48, 10 yrs)", "Libaya (AKL #49, 17 yrs)", "Sharma-Adad I (AKL #50, 12 yrs)",
        "Iptar-Sin (AKL #51, 12 yrs)", "Bazaya (AKL #52, 28 yrs)", "Lullaya (AKL #53, 6 yrs)", "Kidin-Ninua (AKL #54, 14 yrs)",
        "Sharma-Adad II (AKL #55, 3 yrs)", "Erishum III (AKL #56, 13 yrs)", "Shamshi-Adad II (AKL #57, 6 yrs)", "Ishme-Dagan II (AKL #58, 16 yrs)",
        "Shamshi-Adad III (AKL #59, 16 yrs)", "Ashur-nirari I (AKL #60, 26 yrs)", "Puzur-Ashur III (AKL #61, 14/24 yrs)",
        "Enlil-nasir I (AKL #62, 13 yrs)", "Nur-ili (AKL #63, 12 yrs)", "Ashur-shaduni (AKL #64)", "Ashur-rabi I (AKL #65)", "Ashur-nadin-ahhe I (AKL #66)"
    ], edge_type="direct", edge_label="Old Assyrian King (AKL)")

    add_roster(nodes, edges, "akl_79_86_ninurta_apil", "aklr_mid", "mesopotamian", 15, "1430-935 BCE (AKL)", "Middle Assyrian King", ["Assyrian King List (Pruzsinszky Table 17b)"], [
        "Enlil-nasir II (AKL #67, 6 yrs)", "Ashur-nirari II (AKL #68, 7 yrs)", "Ashur-bel-nisheshu (AKL #69, 9 yrs)", "Ashur-rim-nisheshu (AKL #70, 8 yrs)",
        "Ashur-nadin-ahhe II (AKL #71, 10 yrs)", "Eriba-Adad I (AKL #72, 27 yrs)", "Enlil-nirari (AKL #74, 10 yrs)", "Arik-den-ili (AKL #75, 12 yrs)",
        "Adad-nirari I (AKL #76, 32 yrs)", "Shalmaneser I (AKL #77, 30 yrs)", "Tukulti-Ninurta I (AKL #78, 37 yrs)", "Ashur-nadin-apli (AKL #79, 4 yrs)",
        "Ashur-nirari III (AKL #80, 6 yrs)", "Enlil-kudurri-usur (AKL #81, 5 yrs)", "Ninurta-apil-Ekur (AKL #82, 13 yrs)", "Ashur-dan I (AKL #83, 46 yrs)",
        "Ninurta-tukulti-Ashur (AKL #84)", "Mutakkil-Nusku (AKL #85)", "Ashur-resh-ishi I (AKL #86, 18 yrs)", "Tiglath-Pileser I (AKL #87, 39 yrs)",
        "Ashared-apil-Ekur (AKL #88, 2 yrs)", "Ashur-bel-kala (AKL #89, 18 yrs)", "Eriba-Adad II (AKL #90, 2 yrs)", "Shamshi-Adad IV (AKL #91, 4 yrs)",
        "Ashurnasirpal I (AKL #92, 19 yrs)", "Shalmaneser II (AKL #93, 12 yrs)", "Ashur-nirari IV (AKL #94, 6 yrs)", "Ashur-rabi II (AKL #95, 41 yrs)",
        "Ashur-resh-ishi II (AKL #96, 5 yrs)", "Tiglath-Pileser II (AKL #97, 32 yrs)"
    ], edge_type="direct", edge_label="Middle Assyrian King (AKL)")

    add_roster(nodes, edges, "akl_110_116_sargonids", "aklr_neo", "mesopotamian", 17, "934-609 BCE (AKL & Chronicles)", "Neo-Assyrian Emperor", ["Assyrian King List (Pruzsinszky)", "Neo-Assyrian Chronicles"], [
        "Ashur-dan II (AKL #98, 23 yrs)", "Adad-nirari II (AKL #99, 21 yrs)", "Tukulti-Ninurta II (AKL #100, 7 yrs)", "Ashurnasirpal II (AKL #101, 25 yrs)",
        "Shamshi-Adad V (AKL #103, 13 yrs)", "Queen Shammuramat / Semiramis (Regent)", "Adad-nirari III (AKL #104, 28 yrs)",
        "Shalmaneser IV (AKL #105, 10 yrs)", "Ashur-dan III (AKL #106, 763 BCE Eclipse)", "Ashur-nirari V (AKL #107, 10 yrs)",
        "Sargon II (722-705 BCE)", "Sennacherib (705-681 BCE)", "Esarhaddon (681-669 BCE)", "Ashurbanipal (669-631 BCE)",
        "Ashur-etil-ilani (631-627 BCE)", "Sin-shar-ishkun (627-612 BCE)", "Ashur-uballit II (612-609 BCE)"
    ], edge_type="direct", edge_label="Neo-Assyrian Ruler")

    add_roster(nodes, edges, "skl_uruk4_gutium_uruk5", "sklr_gut", "mesopotamian", 10, "c. 2154-2112 BCE (SKL Col. vii)", "Gutian King of Sumer", ["Sumerian King List (Jacobsen AS 11 pp. 117-121)"], [
        "Erridupizir (Gutian #1)", "Imta' (Gutian #2, 3 yrs)", "Inkishush (Gutian #3, 6 yrs)", "Sarlagab (Gutian #4, 6 yrs)", "Shulme' (Gutian #5, 6 yrs)",
        "Elulumesh (Gutian #6, 6 yrs)", "Inimabakesh (Gutian #7, 5 yrs)", "Igeshaush (Gutian #8, 6 yrs)", "Iarlagab (Gutian #9, 15 yrs)",
        "Ibate (Gutian #10, 3 yrs)", "Iarlangab (Gutian #11, 3 yrs)", "Kurum (Gutian #12, 1 yr)", "Habil-kin (Gutian #13, 3 yrs)",
        "Laerabum (Gutian #14, 2 yrs)", "Irarum (Gutian #15, 2 yrs)", "Ibranum (Gutian #16, 1 yr)", "Hablum (Gutian #17, 2 yrs)",
        "Puzur-Sin of Gutium (Gutian #18, 7 yrs)", "Iarlaganda (Gutian #19, 7 yrs)", "Si'um (Gutian #20, 7 yrs)", "Tirigan (Gutian #21, 40 days)"
    ], edge_type="expansion", edge_label="Gutian King (SKL Col. vii)")

    add_roster(nodes, edges, "skl_isin1_full", "sklr_isin", "mesopotamian", 11, "c. 2017-1794 BCE (SKL Col. viii)", "King of Isin I Dynasty", ["Sumerian King List (Jacobsen AS 11 pp. 124-127)"], [
        "Ishbi-Erra (33 yrs)", "Shu-ilishu (10 yrs)", "Iddin-Dagan (21 yrs)", "Ishme-Dagan of Isin (20 yrs)", "Lipit-Ishtar (11 yrs, Law Code)",
        "Ur-Ninurta (28 yrs)", "Bur-Sin of Isin (21 yrs)", "Lipit-Enlil (5 yrs)", "Erra-imitti (8 yrs)", "Enlil-bani (24 yrs, Gardener-King)",
        "Zambia (3 yrs)", "Iter-pisha (4 yrs)", "Ur-dukuga (4 yrs)", "Sin-magir (11 yrs)", "Damiq-ilishu (23 yrs)"
    ], edge_type="direct", edge_label="Isin I King (SKL Col. viii)")

    add_roster(nodes, edges, "bab_dyn1_amorite", "babr_1", "mesopotamian", 11, "1894-1595 BCE (L.W. King Vol. I)", "Amorite King of Babylon I", ["Early Babylonian Chronicles (L.W. King Vol. I p. 95)"], [
        "Sumu-la-El (36 yrs)", "Sabium (14 yrs)", "Apil-Sin (18 yrs)", "Sin-muballit (20 yrs, Father of Hammurabi)",
        "Samsu-iluna (38 yrs, Son of Hammurabi)", "Abi-eshuh (28 yrs)", "Ammi-ditana (37 yrs)", "Ammi-saduqa (21 yrs, Venus Tablet)",
        "Samsu-ditana (31 yrs, Fell to Hittites)", "Rim-Sin of Larsa (Son of Kudur-Mabuk)"
    ], edge_type="direct", edge_label="Babylon I / Larsa Ruler")

    add_roster(nodes, edges, "bab_dyn2_sealand", "babr_2", "mesopotamian", 12, "c. 1732-1460 BCE (L.W. King Vol. I)", "King of 1st Sealand Dynasty", ["Early Babylonian Chronicles (L.W. King Vol. I p. 96)"], [
        "Iluma-ilu (60 yrs)", "Itti-ili-nibi (55 yrs)", "Damqi-ilishu (36 yrs)", "Ishkibal (15 yrs)", "Shushshi (27 yrs)",
        "Gulkishar (55 yrs)", "Peshgaldaramesh (50 yrs)", "Ayadaragalama (28 yrs)", "Akurduana (26 yrs)", "Melamkurkurra (7 yrs)", "Ea-gamil (9 yrs)"
    ], edge_type="expansion", edge_label="1st Sealand Dynasty King")

    add_roster(nodes, edges, "bab_dyn3_kassite", "babr_3", "mesopotamian", 14, "c. 1595-1155 BCE (L.W. King Vol. I)", "Kassite King of Babylon", ["Early Babylonian Chronicles (L.W. King Vol. I pp. 101-113)"], [
        "Gandash (16 yrs)", "Agum I (22 yrs)", "Kashtiliash I (22 yrs)", "Ushshi", "Abirattash", "Urzigurumash",
        "Agum II (Restored Marduk)", "Burna-Buriash I", "Ulam-Buriash (Conquered Sealand)", "Burna-Buriash II (Amarna Letters)",
        "Kudur-Enlil", "Shagarakti-Shuriash (13 yrs)", "Meli-Shipak"
    ], edge_type="expansion", edge_label="Kassite Dynasty King")

    add_roster(nodes, edges, "bab_dyn10_chaldean", "babr_10", "mesopotamian", 17, "626-539 BCE (Babylonian Chronicles)", "Neo-Babylonian / Chaldean King", ["Babylonian Chronicles", "Eusebius Chronicle", "2 Kings 24-25"], [
        "Nabopolassar (626-605 BCE)", "Amel-Marduk / Evil-Merodach (562-560 BCE)", "Neriglissar (560-556 BCE)",
        "Labashi-Marduk (556 BCE)", "Nabonidus (556-539 BCE)", "Crown Prince Belshazzar (Daniel 5)"
    ], edge_type="direct", edge_label="Neo-Babylonian / Chaldean Ruler")

    return {
        "module": "17_mesopotamia_complete_kinglists",
        "title": "Complete Assyrian King List (All 116 Kings, Pruzsinszky), Remaining Sumerian King List Dynasties (Jacobsen AS 11) & Complete Babylonian Dynasties (L.W. King)",
        "nodes": nodes,
        "edges": edges,
    }
