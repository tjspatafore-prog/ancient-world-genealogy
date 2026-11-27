"""
Module 17: Person-by-Person Mesopotamian Royal Chronicles —
1. Complete Assyrian King List (AKL, all 116 kings from Tudiya & Adamu to Ashur-uballit II)
   from Regine Pruzsinszky (045_068 Pruzsinszky.pdf) & Eusebius's Assyrian Chronicle.
2. Complete Remaining Sumerian King List Dynasties (Ur I, Awan, Kish II, Hamazi, Uruk II,
   Ur II, Adab, Mari, Kish III [Queen Ku-Baba], Akshak, Kish IV, Uruk III [Lugal-zagesi],
   Uruk IV, Gutium, Uruk V [Utu-hegal], Isin I, plus Lagash/Gudea) from Thorkild Jacobsen (as11.pdf).
3. Complete Babylonian Dynasties (Babylon I Amorite, II Sealand, III Kassite, IV Isin II,
   Neo-Babylonian/Chaldean) from L.W. King (chroniclesconcer01londuoft.pdf) & Eusebius.

Wave 4: Replaced all 11 flat add_roster fans with true sequential father->son & dynastic chains.
"""

from . import N, E, add_chain


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. ASSYRIAN KING LIST ANCHORS (AKL, Pruzsinszky Tables 17a-b)
    # -------------------------------------------------------------------------
    akl_tents = [
        ("akl_01_tudiya", "1. Tudiya (1st Assyrian Tent-King)", 7, "c. 2400 BCE (AKL 1)", "First King of Assyria (Ebla Treaty Attested!)", "First of the '17 kings who lived in tents' in the Assyrian King List; historically attested in the Ebla archives concluding a trade treaty with Vizier Ibrium of Ebla!", {"major": True, "altNames": ["Tudia", "Dudiya"]}),
        ("akl_02_adamu", "2. Adamu (2nd Assyrian Tent-King)", 7, "c. 2380 BCE (AKL 2)", "West Semitic/Assyrian Tent-King (Cognate of Adam!)", "Second king of Assyria in the AKL; earliest known historical ruler bearing the Semitic name Adamu ('Man/Red Earth'), cognate with Biblical Adam!", {"major": True, "altNames": ["Cognate: Adam"]}),
        ("akl_03_08_tents", "AKL Tent-Kings 3–8 Anchor (Yangi to Harsu)", 7, "c. 2360-2260 BCE (AKL 3-8)", "Assyrian Tent-Dwelling Patriarchal Group Anchor", "Anchor for Kings 3-8 of the AKL tent-dwellers, linked sequentially below.", {"altNames": ["Yangi", "Suhlamu", "Harharu", "Mandaru", "Imsu", "Harsu"]}),
        ("akl_09_10_didanu_hanu", "AKL Tent-Kings 9–10 Anchor (Didanu & Hanu)", 7, "c. 2240-2200 BCE (AKL 9-10)", "Eponymous Amorite Tribal Ancestors Anchor", "Didanu corresponds to Tidnum/Ditanu; Hanu corresponds to the Middle Euphrates tribe of Hana.", {"altNames": ["Didanu / Tidnum", "Hanu"]}),
        ("akl_11_15_tents", "AKL Tent-Kings 11–15 Anchor (Zuabu to Azarah)", 7, "c. 2180-2100 BCE (AKL 11-15)", "Late Tent-Dwelling Kings Anchor", "Kings 11-15 of the canonical Assyrian King List (Pruzsinszky Table 17a).", {"altNames": ["Zuabu", "Nuabu", "Abazu", "Belu", "Azarah"]}),
        ("akl_16_ushpia", "16. Ushpia (Builder of the Temple of Ashur)", 8, "c. 2080 BCE (AKL 16)", "Founder of the E-hursag-kurkurra Temple of Ashur", "Credited in inscriptions of Shalmaneser I and Esarhaddon as the earliest founder of the great Temple of the god Ashur in Assur.", {"major": True, "altNames": ["Ušpia"]}),
        ("akl_17_apiashal", "17. Apiashal (Son of Ushpia — Bridge to Ancestors)", 8, "c. 2060 BCE (AKL 17)", "Last Tent-King & First of the 10 Ancestors", "Appears at both the end of Section 1 (17 tent-dwellers) and the beginning of Section 2 (10 kings whose fathers are known), linking Shamshi-Adad I's pedigree back to Ushpia!", {"altNames": ["Apiašal"]}),
    ]
    add_chain(nodes, edges, akl_tents, start_parent="bib_asshur", start_edge_type="cognate",
              start_edge_label="Genesis 10:11 Asshur <-> Canonical Assyrian King List (AKL)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Assyrian King List (Pruzsinszky Table 17a)"])

    akl_ancestors = [
        ("akl_18_24_ancestors", "AKL Section 2 Anchor (Kings 18–24: Hale to Yazkur-El)", 8, "c. 2050-1900 BCE (AKL 18-24)", "Patrilineal Ancestors of Shamshi-Adad I Anchor", "Listed in reverse genealogical order ('PN1 son of PN2') in AKL Section 2 (Pruzsinszky pp. 48, 51).", {"altNames": ["Hale", "Samani", "Hayani", "Ilu-Mer", "Yakmesi", "Yakmeni", "Yazkur-El"]}),
        ("akl_25_26_ilukabkabi_aminu", "AKL Kings 25–26 Anchor (Ilu-kabkabi & Aminu)", 9, "c. 1850-1810 BCE (AKL 25-26)", "Amorite King of Ekallatum / Terqa Anchor", "Ilu-kabkabi fathered Aminu and the great conqueror Shamshi-Adad I.", {"altNames": ["Ilu-kabkabi", "Aminu"]}),
    ]
    add_chain(nodes, edges, akl_ancestors, start_parent="akl_17_apiashal", start_edge_type="direct",
              start_edge_label="AKL Section 2: 'Ten kings whose fathers are known'",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17a)"])

    akl_old = [
        ("akl_27_29_sulili_kikia", "AKL Kings 27–29 Anchor (Sulili, Kikia & Akia)", 9, "c. 2025-1980 BCE (AKL 27-29)", "Early City-Rulers of Assur Anchor", "Kikia built the city wall of Assur; Sulili (son of Aminu) marks Assur's independence after Ur III.", {"altNames": ["Sulili", "Kikia", "Akia"]}),
        ("akl_30_32_puzur_ilushuma", "AKL Kings 30–32 Anchor (Puzur-Ashur I to Ilushuma)", 9, "c. 1975-1935 BCE (AKL 30-32)", "Founders of the Old Assyrian Merchant Dynasty Anchor", "Ilushuma established free trade privileges for Akkadian merchants and founded the Old Assyrian trading empire.", {"altNames": ["Puzur-Ashur I", "Shalim-ahum", "Ilushuma"]}),
        ("akl_33_34_erishum_ikunum", "AKL Kings 33–34 Anchor (Erishum I & Ikunum)", 10, "c. 1934-1880 BCE (AKL 33-34; KEL)", "First King with Kultepe Eponym List Chronology Anchor", "Erishum I rebuilt the Ashur Temple and inaugurated the Kultepe Eponym List (KEL).", {"altNames": ["Erishum I", "Ikunum"]}),
        ("akl_35_38_sargon1_naramsin", "AKL Kings 35–38 Anchor (Sargon I to Erishum II)", 10, "c. 1880-1808 BCE (AKL 35-38)", "Old Assyrian Anatolian Colony Trade Anchor", "Overthrown in 1808 BCE by Shamshi-Adad I.", {"altNames": ["Sargon I of Assyria", "Puzur-Ashur II", "Naram-Sin of Assyria", "Erishum II"]}),
        ("akl_39_40_shamshi_adad1", "39. King Shamshi-Adad I of Assyria (33 yrs, c. 1808–1776 BCE)", 11, "1808-1776 BCE (AKL 39; Mari Archives)", "Founder of the Kingdom of Upper Mesopotamia (Contemporary of Hammurabi)", "Son of Ilu-kabkabi; conquered Assur, Mari, and Shubat-Enlil; father of Ishme-Dagan I and Yasmah-Adad.", {"major": True, "altNames": ["Samši-Adad I"]}),
        ("akl_41_47_usurpers", "AKL Kings 41–47 Anchor (Ashur-dugul & Six Usurpers to Adasi)", 11, "c. 1735-1700 BCE (AKL 41-47)", "Interregnum & Adaside Origin Anchor", "Six claimants ruled briefly before Adasi founded the 1,000-year Adaside dynasty.", {"altNames": ["Ashur-dugul", "Adasi"]}),
        ("akl_48_53_belubani", "AKL Kings 48–53 Anchor (Belu-bani to Lullaya)", 12, "c. 1700-1618 BCE (AKL 48-53)", "Early Adaside Kings of Assur Anchor", "Belu-bani (10 yrs) founded the unbroken Adaside royal dynasty; Bazaya ruled 28 years.", {"altNames": ["Belu-bani", "Libaya", "Sharma-Adad I", "Iptar-Sin", "Bazaya", "Lullaya"]}),
        ("akl_54_66_old_late", "AKL Kings 54–66 Anchor (Kidin-Ninua to Ashur-nadin-ahhe I)", 13, "c. 1617-1431 BCE (AKL 54-66)", "Late Old Assyrian / Mitanni Vassalage Anchor", "Preserved unbroken Adaside patrilineal continuity through the Mitanni era (Pruzsinszky Table 17b).", {"altNames": ["Kidin-Ninua", "Ashur-nirari I", "Puzur-Ashur III", "Ashur-rabi I"]}),
        ("akl_67_72_pre_middle", "AKL Kings 67–72 Anchor (Enlil-nasir II to Eriba-Adad I)", 14, "c. 1430-1364 BCE (AKL 67-72)", "Transition to Middle Assyrian Independence Anchor", "Eriba-Adad I (27 yrs) broke Mitanni supremacy, setting the stage for his son Ashur-uballit I.", {"altNames": ["Enlil-nasir II", "Ashur-bel-nisheshu", "Eriba-Adad I"]}),
    ]
    add_chain(nodes, edges, akl_old, start_parent="akl_25_26_ilukabkabi_aminu", start_edge_type="expansion",
              start_edge_label="Old Assyrian Dynasty & Shamshi-Adad I (AKL 27-72)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Tables 17a-b)"])

    akl_middle = [
        ("akl_73_76_ashuruballit1", "73. King Ashur-uballit I of Assyria (Amarna Letters EA 15–16, 1363–1328 BCE)", 15, "1363-1328 BCE (AKL 73; Amarna Letters)", "Founder of the Middle Assyrian Great Power", "Son of Eriba-Adad I; wrote to Pharaoh Akhenaten as 'Great King' (EA 15-16) and married his daughter Muballitat-Sherua to Kassite King Burna-Buriash II of Babylon.", {"major": True, "altNames": ["Aššur-uballit I"]}),
        ("akl_77_78_shalmaneser1_tukulti", "AKL Kings 77–78 Anchor (Shalmaneser I & Tukulti-Ninurta I)", 15, "1273-1207 BCE (AKL 77-78)", "Peak of the Middle Assyrian Empire Anchor", "Shalmaneser I founded Kalhu (Nimrud); Tukulti-Ninurta I captured Kassite Babylon.", {"major": True, "altNames": ["Shalmaneser I", "Tukulti-Ninurta I"]}),
        ("akl_79_86_ninurta_apil", "AKL Kings 79–86 Anchor (Ashur-nadin-apli to Ashur-resh-ishi I)", 16, "1206-1115 BCE (AKL 79-86)", "Bronze Age Collapse Survival & Revival Anchor", "Ninurta-apil-Ekur restored dynastic stability; Ashur-dan I ruled 46 years.", {"altNames": ["Ninurta-apil-Ekur", "Ashur-dan I", "Ashur-resh-ishi I"]}),
        ("akl_87_97_tiglath1_to_2", "AKL Kings 87–97 Anchor (Tiglath-Pileser I to Tiglath-Pileser II)", 16, "1114-935 BCE (AKL 87-97)", "Tiglath-Pileser I & Aramean Era Anchor", "Tiglath-Pileser I marched to the Mediterranean and compiled the Middle Assyrian Laws.", {"altNames": ["Tiglath-Pileser I", "Ashur-bel-kala", "Ashur-rabi II", "Tiglath-Pileser II"]}),
    ]
    add_chain(nodes, edges, akl_middle, start_parent="akl_67_72_pre_middle", start_edge_type="direct",
              start_edge_label="Middle Assyrian Empire (AKL 73-97)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17b)"])

    akl_neo = [
        ("akl_98_101_ashurnasirpal2", "AKL Kings 98–101 Anchor (Ashur-dan II to Ashurnasirpal II)", 17, "934-859 BCE (AKL 98-101)", "Founders of the Neo-Assyrian Empire Anchor", "Adad-nirari II inaugurated the unbroken Eponym Canon; Ashurnasirpal II built Nimrud.", {"major": True, "altNames": ["Adad-nirari II", "Ashurnasirpal II"]}),
        ("akl_102_shalmaneser3", "102. Shalmaneser III (35 yrs — Black Obelisk of Jehu & Battle of Qarqar!)", 17, "858-824 BCE (AKL 102; Kurkh Monolith; Black Obelisk)", "First Assyrian King Explicitly Naming Israelite Kings Ahab & Jehu", "Fought King Ahab of Israel & Hadadezer of Damascus at Qarqar (853 BCE); his Black Obelisk depicts King Jehu of Israel ('son of Omri') bowing in tribute — the ONLY contemporary depiction of an Israelite king!", {"major": True, "altNames": ["Šalmaneser III", "Black Obelisk"]}),
        ("akl_103_104_semiramis", "AKL Kings 103–104 Anchor (Shamshi-Adad V, Semiramis & Adad-nirari III)", 17, "823-783 BCE (AKL 103-104; Herodotus; Eusebius)", "Queen Shammuramat (Semiramis) & Adad-nirari III Anchor", "Shammuramat served as regent alongside her son Adad-nirari III.", {"major": True, "altNames": ["Queen Shammuramat", "Semiramis", "Adad-nirari III"]}),
        ("akl_105_107_eclipse_kings", "AKL Kings 105–107 Anchor (Shalmaneser IV to Ashur-nirari V)", 17, "782-745 BCE (AKL 105-107)", "763 BCE Bur-Sagale Solar Eclipse Anchor", "Assyrian Eponym List records the June 15, 763 BCE total solar eclipse under Ashur-dan III.", {"altNames": ["Shalmaneser IV", "Ashur-dan III (763 BCE Eclipse)", "Ashur-nirari V"]}),
        ("akl_108_109_tp3_shalm5", "AKL Kings 108–109 Anchor (Tiglath-Pileser III / Pul & Shalmaneser V)", 17, "745-722 BCE (AKL 108-109; 2 Kings 15-17)", "Canonical AKL End & Biblical 'Pul' Anchor", "Tiglath-Pileser III ('Pul', 2 Kgs 15:19) and son Shalmaneser V (siege of Samaria).", {"altNames": ["Tiglath-Pileser III (Pul)", "Shalmaneser V"]}),
        ("akl_110_116_sargonids", "Sargonid Dynasty Anchor (Sargon II to Ashur-uballit II)", 17, "722-609 BCE (Neo-Assyrian Chronicles; 2 Kings 18-19; Isaiah 20)", "Final Imperial Dynasty of Nineveh Anchor", "Sargon II, Sennacherib, Esarhaddon, Ashurbanipal, Ashur-etil-ilani, Sin-shar-ishkun, Ashur-uballit II — unrolled person-by-person below.", {"major": True, "altNames": ["Sargon II", "Sennacherib", "Esarhaddon", "Ashurbanipal", "Ashur-uballit II"]}),
    ]
    add_chain(nodes, edges, akl_neo, start_parent="akl_87_97_tiglath1_to_2", start_edge_type="direct",
              start_edge_label="Neo-Assyrian Empire (AKL 98-116)",
              tradition="mesopotamian", default_edge_type="direct", default_sources=["Assyrian King List (Pruzsinszky Table 17b)", "Neo-Assyrian Chronicles"])

    # -------------------------------------------------------------------------
    # 2. REMAINING SUMERIAN KING LIST ANCHORS (Jacobsen AS 11, pp. 93-127)
    # -------------------------------------------------------------------------
    skl_rest = [
        ("skl_ur1_full", "Ur I Dynasty: Mesannepada → Aannepada → Meskiagnunna → Elulu → Balulu", 7, "c. 2560-2400 BCE (SKL Col. iii-iv, Jacobsen pp. 93-95)", "First Dynasty of Ur (Royal Tombs of Ur Era)", "5 kings (177 yrs): Mesannepada -> son Aannepada (restored from Tummal Chronicle & inscriptions!) -> Meskiagnunna -> Elulu -> Balulu.", {"altNames": ["Aannepada", "Elulu", "Balulu"]}),
        ("skl_awan_kish2_hamazi", "Awan (3 Kings), Kish II (8 Kings) & Hamazi (King Hatanish)", 7, "c. 2500-2400 BCE (SKL Col. iv, Jacobsen pp. 95-99)", "Early Dynastic Hegemonies of Elam, Kish & Zagros", "Awan (Elamite dynasty, 3 kings), Kish II (8 kings incl. Kalbum son of Magalgalla), and Hamazi (King Hatanish).", {"altNames": ["Hatanish of Hamazi", "Enbi-Ishtar", "Magalgalla"]}),
        ("skl_uruk2_ur2_adab_mari", "Uruk II (Enshakushanna), Ur II (Kaku), Adab (Lugal-annemundu) & Mari (Ansud)", 8, "c. 2450-2350 BCE (SKL Col. iv-v, Jacobsen pp. 100-103)", "Pre-Sargonic City-State Empires", "Enshakushanna of Uruk; Lugal-kinishe-dudu & son Lugal-kisal-si; Lugal-annemundu of Adab; Ansud of Mari.", {"altNames": ["Enshakushanna", "Lugal-annemundu", "Ansud of Mari"]}),
        ("skl_kubaba_kish3", "Queen Ku-Baba (Kish III — Sole Female Monarch in the Sumerian King List!)", 8, "c. 2400 BCE (SKL Col. v 36-41, Jacobsen pp. 104-105)", "Tavern-Keeper Who Consolidated Kish & Founded Kish III–IV", "Ku(g)-Baba ('Baba-ellit', reigned 100 yrs) is the ONLY woman listed as sovereign king in the entire Sumerian King List; mother of Puzur-Sin & grandmother of Ur-Zababa!", {"major": True, "altNames": ["Kug-Baba", "Kubaba"]}),
        ("skl_akshak_kish4", "Akshak (6 Kings) & Kish IV (Puzur-Sin → Ur-Zababa → Nannia)", 8, "c. 2400-2334 BCE (SKL Col. v-vi, Jacobsen pp. 106-111)", "Dynasty of Ku-Baba's Descendants & Master of Young Sargon", "Ku-Baba's son Puzur-Sin -> son Ur-Zababa of Kish, whose royal cupbearer was Sargon of Akkad.", {"altNames": ["Puzur-Sin", "Ur-Zababa", "Puzur-Nirah"]}),
        ("skl_uruk3_lugalzagesi", "Uruk III: King Lugal-zagesi (25 yrs — First Unifier of Sumer Before Sargon)", 9, "c. 2359-2335 BCE (SKL Col. vi 24-27, Jacobsen pp. 110-111)", "Ensi of Umma & Sole King of Uruk III", "United all of Sumer from the Lower Sea to the Upper Sea before being defeated by Sargon of Akkad.", {"major": True, "altNames": ["Lugal-zage-si"]}),
        ("skl_akkad_late", "Late Akkad Interregnum (Igigi, Nanum, Imi, Elulu) → Dudu → Shu-Durul", 10, "c. 2193-2154 BCE (SKL Col. vii 1-12, Jacobsen pp. 114-115)", "Final Rulers of the Sargonic Akkadian Empire", "'Who was king? Who was not king?' Four rival claimants before Dudu (21 yrs) and his son Shu-Durul (15 yrs).", {"altNames": ["Igigi", "Dudu of Akkad", "Shu-Durul"]}),
        ("skl_uruk4_gutium_uruk5", "Uruk IV → 21 Gutian Kings → Uruk V (Utu-hegal) Anchor", 10, "c. 2154-2112 BCE (SKL Col. vii-viii, Jacobsen pp. 114-123)", "Gutian Domination & Sumerian Liberation Anchor", "21 Gutian rulers from the Zagros mountains expelled by Utu-hegal of Uruk V — unrolled person-by-person below.", {"major": True, "altNames": ["Gutian Dynasty", "Tirigan", "Utu-hegal"]}),
        ("skl_lagash_gudea", "Independent Lagash II: Ur-Nanshe → Eannatum → Urukagina → Gudea of Lagash", 10, "c. 2500-2120 BCE (Lagash Royal Inscriptions)", "Sumerian Reformers & Statue-Builder Gudea", "Ur-Nanshe, Eannatum, law-reformer Urukagina, and pious Ensi Gudea of Lagash.", {"altNames": ["Eannatum", "Urukagina", "Gudea of Lagash"]}),
        ("skl_isin1_full", "Isin I Dynasty Anchor (15 Kings: Ishbi-Erra to Damiq-ilishu)", 11, "c. 2017-1794 BCE (SKL Col. viii 23-45, Jacobsen pp. 124-127)", "Final Dynasty of the Sumerian King List Anchor", "15 kings of Isin I (Ishbi-Erra through Damiq-ilishu) unrolled person-by-person below.", {"major": True, "altNames": ["Ishbi-Erra", "Lipit-Ishtar", "Enlil-bani", "Damiq-ilishu"]}),
    ]
    add_chain(nodes, edges, skl_rest, start_parent="mes_mesannepada", start_edge_type="direct",
              start_edge_label="Post-Diluvian Sumerian King List Continuation (Jacobsen AS 11)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Sumerian King List (Jacobsen AS 11)"])

    # -------------------------------------------------------------------------
    # 3. BABYLONIAN DYNASTY ANCHORS I-X (L.W. King Vol. I & Eusebius)
    # -------------------------------------------------------------------------
    bab_all = [
        ("bab_dyn1_amorite", "Babylon I Amorite Dynasty Anchor (Sumu-abum to Samsu-ditana)", 11, "1894-1595 BCE (L.W. King Vol. I pp. 95, 144-150)", "Complete Old Babylonian Amorite Dynasty Anchor", "All 11 Amorite kings of Babylon I chained father-to-son below.", {"major": True, "altNames": ["Sumu-la-El", "Sin-muballit", "Samsu-iluna", "Ammi-saduqa", "Rim-Sin of Larsa"]}),
        ("bab_dyn2_sealand", "Babylon II First Sealand Dynasty Anchor (Iluma-ilu to Ea-gamil)", 12, "c. 1732-1460 BCE (L.W. King Vol. I pp. 96, 151-155)", "Southern Marshland Dynasty Anchor", "All 11 kings of the 1st Sealand Dynasty chained sequentially below.", {"altNames": ["Iluma-ilu", "Gulkishar", "Ea-gamil"]}),
        ("bab_dyn3_kassite", "Babylon III Kassite Dynasty Anchor (Gandash to Meli-Shipak)", 14, "c. 1595-1155 BCE (L.W. King Vol. I pp. 79, 101-113, 151-153)", "Longest-Reigning Dynasty in Babylonian History Anchor", "Kassite kings from Gandash through Burna-Buriash II & Meli-Shipak chained below.", {"major": True, "altNames": ["Gandash", "Agum II", "Ulam-Buriash", "Burna-Buriash II", "Meli-Shipak"]}),
        ("bab_dyn4_isin2", "Babylon IV (Isin II): Nebuchadnezzar I → Enlil-nadin-apli → Marduk-nadin-ahhe → Adad-apla-iddina", 16, "1157-1026 BCE (L.W. King Vol. I pp. 89, 190-193)", "Revival of Native Babylon & Recovery of Marduk from Elam", "Nebuchadnezzar I sacked Susa in Elam and restored Marduk to Babylon; Adad-apla-iddina married his daughter to Assyrian King Ashur-bel-kala.", {"altNames": ["Nebuchadnezzar I", "Marduk-nadin-ahhe", "Adad-apla-iddina"]}),
        ("bab_dyn5_8_inter", "Babylon V–IX: 2nd Sealand, Bazi Dynasty, Nabonassar (747 BCE Era!) & Merodach-Baladan II", 17, "1025-626 BCE (L.W. King Vol. I pp. 184-208; Eusebius)", "Ptolemaic Astronomical Era of Nabonassar & Chaldean Resistance", "King Nabonassar (747 BCE) inaugurated Ptolemy's Almagest Canon; Merodach-Baladan II sent envoys to King Hezekiah of Judah (2 Kgs 20:12).", {"altNames": ["Simbar-Shipak", "Nabonassar (747 BCE)", "Merodach-Baladan II", "Mushezib-Marduk"]}),
        ("bab_dyn10_chaldean", "Babylon X Neo-Babylonian / Chaldean Empire Anchor (Nabopolassar to Belshazzar)", 17, "626-539 BCE (Babylonian Chronicles; Eusebius; 2 Kings 24-25; Daniel 5)", "Final Native Babylonian Empire Anchor", "Nabopolassar -> Nebuchadnezzar II -> Amel-Marduk -> Neriglissar -> Labashi-Marduk -> Nabonidus & Belshazzar unrolled below.", {"major": True, "altNames": ["Nabopolassar", "Amel-Marduk", "Neriglissar", "Nabonidus", "Belshazzar"]}),
    ]
    add_chain(nodes, edges, bab_all, start_parent="mes_hammurabi", start_edge_type="direct",
              start_edge_label="Complete Babylonian Dynastic Sequence (L.W. King Vol. I)",
              tradition="mesopotamian", default_edge_type="expansion", default_sources=["Early Babylonian Chronicles (L.W. King Vol. I)", "Eusebius Chronicle"])

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
    # 4. PERSON-BY-PERSON SEQUENTIAL CHAINS (Zero Flat Rosters!)
    # -------------------------------------------------------------------------
    # A. AKL Section 1: Kings 3-15 (Tent-Dwellers)
    akl_t1_list = [
        ("aklr_t1_01_yangi_akl_3", "3. Yangi (AKL #3)", 7, "c. 2360 BCE"),
        ("aklr_t1_02_suhlamu_akl_4", "4. Suhlamu (AKL #4)", 7, "c. 2345 BCE"),
        ("aklr_t1_03_harharu_akl_5", "5. Harharu (AKL #5)", 7, "c. 2330 BCE"),
        ("aklr_t1_04_mandaru_akl_6", "6. Mandaru (AKL #6)", 7, "c. 2315 BCE"),
        ("aklr_t1_05_imsu_akl_7", "7. Imsu (AKL #7)", 7, "c. 2300 BCE"),
        ("aklr_t1_06_harsu_akl_8", "8. Harsu (AKL #8)", 7, "c. 2285 BCE"),
        ("aklr_t1_07_didanu_tidnum_akl_9", "9. Didanu / Tidnum (AKL #9)", 7, "c. 2260 BCE"),
        ("aklr_t1_08_hanu_akl_10", "10. Hanu (AKL #10)", 7, "c. 2240 BCE"),
        ("aklr_t1_09_zuabu_akl_11", "11. Zuabu (AKL #11)", 7, "c. 2220 BCE"),
        ("aklr_t1_10_nuabu_akl_12", "12. Nuabu (AKL #12)", 7, "c. 2200 BCE"),
        ("aklr_t1_11_abazu_akl_13", "13. Abazu (AKL #13)", 7, "c. 2170 BCE"),
        ("aklr_t1_12_belu_akl_14", "14. Belu (AKL #14)", 7, "c. 2140 BCE"),
        ("aklr_t1_13_azarah_akl_15", "15. Azarah (AKL #15)", 7, "c. 2110 BCE"),
    ]
    for nid, nm, tr, dt in akl_t1_list:
        nodes.append(N(nid, nm, "mesopotamian", tr, f"{dt} (AKL)", "Assyrian Tent-Dwelling King", ["Assyrian King List (Pruzsinszky Table 17a)"], f"Assyrian King List Section 1 tent-dwelling ruler: {nm}.", major=False))
    edges.append(E("akl_02_adamu", "aklr_t1_01_yangi_akl_3", "expansion", "AKL Tent-Kings succession: Adamu -> Yangi"))
    edges.append(E("akl_03_08_tents", "aklr_t1_01_yangi_akl_3", "expansion", "AKL Tent-Kings 3-15 anchor link"))
    link_seq(edges, [x[0] for x in akl_t1_list] + ["akl_16_ushpia"], "expansion", "AKL Tent-Kings sequential succession")

    # B. AKL Section 2: 10 Ancestors (AKL 18-26)
    akl_anc_list = [
        ("aklr_anc_01_hale_akl_18", "18. Hale (Son of Apiashal, AKL #18)", 8, "c. 2040 BCE"),
        ("aklr_anc_02_samani_akl_19", "19. Samani (Son of Hale, AKL #19)", 8, "c. 2020 BCE"),
        ("aklr_anc_03_hayani_akl_20", "20. Hayani (Son of Samani, AKL #20)", 8, "c. 2000 BCE"),
        ("aklr_anc_04_ilu_mer_akl_21", "21. Ilu-Mer (Son of Hayani, AKL #21)", 8, "c. 1980 BCE"),
        ("aklr_anc_05_yakmesi_akl_22", "22. Yakmesi (Son of Ilu-Mer, AKL #22)", 8, "c. 1960 BCE"),
        ("aklr_anc_06_yakmeni_akl_23", "23. Yakmeni (Son of Yakmesi, AKL #23)", 8, "c. 1940 BCE"),
        ("aklr_anc_07_yazkur_el_akl_24", "24. Yazkur-El (Son of Yakmeni, AKL #24)", 8, "c. 1910 BCE"),
        ("aklr_anc_08_ilu_kabkabi_akl_25", "25. Ilu-kabkabi (Son of Yazkur-El; Father of Shamshi-Adad I, AKL #25)", 9, "c. 1860 BCE"),
        ("aklr_anc_09_aminu_akl_26", "26. Aminu (Son of Ilu-kabkabi; Elder Brother of Shamshi-Adad I, AKL #26)", 9, "c. 1830 BCE"),
    ]
    for nid, nm, tr, dt in akl_anc_list:
        nodes.append(N(nid, nm, "mesopotamian", tr, f"{dt} (AKL)", "Patrilineal Ancestor of Shamshi-Adad I", ["Assyrian King List (Pruzsinszky Table 17a)"], f"AKL Section 2 patrilineal ancestor: {nm}.", major=False))
    edges.append(E("akl_17_apiashal", "aklr_anc_01_hale_akl_18", "direct", "AKL Section 2: Apiashal -> son Hale"))
    link_seq(edges, [x[0] for x in akl_anc_list], "direct", "AKL Section 2 father-to-son pedigree")
    edges.append(E("aklr_anc_08_ilu_kabkabi_akl_25", "akl_39_40_shamshi_adad1", "direct", "Father Ilu-kabkabi -> Shamshi-Adad I"))

    # C. AKL Section 3 & Adaside Old Assyrian Dynasty (AKL 27-66)
    akl_old_1 = [
        ("aklr_old_01_sulili_akl_27", "27. Sulili (Son of Aminu, AKL #27)", 9, "c. 2025 BCE"),
        ("aklr_old_02_kikia_akl_28", "28. Kikia (Wall Builder of Assur, AKL #28)", 9, "c. 2005 BCE"),
        ("aklr_old_03_akia_akl_29", "29. Akia (AKL #29)", 9, "c. 1990 BCE"),
        ("aklr_old_04_puzur_ashur_i_akl_30", "30. Puzur-Ashur I (AKL #30)", 9, "c. 1975 BCE"),
        ("aklr_old_05_shalim_ahum_akl_31", "31. Shalim-ahum (Son of Puzur-Ashur I, AKL #31)", 9, "c. 1955 BCE"),
        ("aklr_old_06_ilushuma_akl_32", "32. Ilushuma (Son of Shalim-ahum, AKL #32)", 9, "c. 1945 BCE"),
        ("aklr_old_07_erishum_i_akl_33_40_yrs", "33. Erishum I (Son of Ilushuma; 40 yrs, KEL Start, AKL #33)", 10, "c. 1934-1895 BCE"),
        ("aklr_old_08_ikunum_akl_34_15_yrs", "34. Ikunum (Son of Erishum I; 15 yrs, AKL #34)", 10, "c. 1894-1880 BCE"),
        ("aklr_old_09_sargon_i_of_assyria_akl_35_4", "35. Sargon I of Assyria (Son of Ikunum; 40 yrs, AKL #35)", 10, "c. 1880-1840 BCE"),
        ("aklr_old_10_puzur_ashur_ii_akl_36_8_yrs", "36. Puzur-Ashur II (Son of Sargon I; 8 yrs, AKL #36)", 10, "c. 1840-1832 BCE"),
        ("aklr_old_11_naram_sin_of_assyria_akl_37_", "37. Naram-Sin of Assyria (Son of Puzur-Ashur II; AKL #37)", 10, "c. 1832-1818 BCE"),
        ("aklr_old_12_erishum_ii_akl_38_10_yrs", "38. Erishum II (Son of Naram-Sin; 10 yrs, AKL #38)", 10, "c. 1818-1808 BCE"),
    ]
    akl_old_2 = [
        ("aklr_old_13_ishme_dagan_i_akl_40_40_yrs", "40. Ishme-Dagan I (Son of Shamshi-Adad I; 40 yrs, AKL #40)", 11, "1776-1736 BCE"),
        ("aklr_old_14_ashur_dugul_akl_41_6_yrs", "41. Ashur-dugul (Interregnum Claimant; 6 yrs, AKL #41)", 11, "c. 1735-1729 BCE"),
        ("aklr_old_15_adasi_akl_47_adaside_founder", "47. Adasi (Founder of the 1,000-Year Adaside Dynasty, AKL #47)", 11, "c. 1715-1700 BCE"),
        ("aklr_old_16_belu_bani_akl_48_10_yrs", "48. Belu-bani (Son of Adasi; 10 yrs, AKL #48)", 12, "c. 1700-1690 BCE"),
        ("aklr_old_17_libaya_akl_49_17_yrs", "49. Libaya (Son of Belu-bani; 17 yrs, AKL #49)", 12, "c. 1690-1673 BCE"),
        ("aklr_old_18_sharma_adad_i_akl_50_12_yrs", "50. Sharma-Adad I (Son of Libaya; 12 yrs, AKL #50)", 12, "c. 1673-1661 BCE"),
        ("aklr_old_19_iptar_sin_akl_51_12_yrs", "51. Iptar-Sin (Son of Sharma-Adad I; 12 yrs, AKL #51)", 12, "c. 1661-1649 BCE"),
        ("aklr_old_20_bazaya_akl_52_28_yrs", "52. Bazaya (Son of Belu-bani; 28 yrs, AKL #52)", 12, "c. 1649-1621 BCE"),
        ("aklr_old_21_lullaya_akl_53_6_yrs", "53. Lullaya ('Son of a Nobody'; 6 yrs, AKL #53)", 12, "c. 1621-1615 BCE"),
        ("aklr_old_22_kidin_ninua_akl_54_14_yrs", "54. Kidin-Ninua (Son of Bazaya; 14 yrs, AKL #54)", 13, "c. 1615-1601 BCE"),
        ("aklr_old_23_sharma_adad_ii_akl_55_3_yrs", "55. Sharma-Adad II (Son of Kidin-Ninua; 3 yrs, AKL #55)", 13, "c. 1601-1598 BCE"),
        ("aklr_old_24_erishum_iii_akl_56_13_yrs", "56. Erishum III (Son of Kidin-Ninua; 13 yrs, AKL #56)", 13, "c. 1598-1585 BCE"),
        ("aklr_old_25_shamshi_adad_ii_akl_57_6_yrs", "57. Shamshi-Adad II (Son of Erishum III; 6 yrs, AKL #57)", 13, "c. 1585-1579 BCE"),
        ("aklr_old_26_ishme_dagan_ii_akl_58_16_yrs", "58. Ishme-Dagan II (Son of Shamshi-Adad II; 16 yrs, AKL #58)", 13, "c. 1579-1563 BCE"),
        ("aklr_old_27_shamshi_adad_iii_akl_59_16_y", "59. Shamshi-Adad III (Descendant of Bazaya; 16 yrs, AKL #59)", 13, "c. 1563-1547 BCE"),
        ("aklr_old_28_ashur_nirari_i_akl_60_26_yrs", "60. Ashur-nirari I (Son of Ishme-Dagan II; 26 yrs, AKL #60)", 13, "c. 1547-1521 BCE"),
        ("aklr_old_29_puzur_ashur_iii_akl_61_14_24", "61. Puzur-Ashur III (Son of Ashur-nirari I; 14/24 yrs, AKL #61)", 13, "c. 1521-1497 BCE"),
        ("aklr_old_30_enlil_nasir_i_akl_62_13_yrs", "62. Enlil-nasir I (Son of Puzur-Ashur III; 13 yrs, AKL #62)", 13, "c. 1497-1484 BCE"),
        ("aklr_old_31_nur_ili_akl_63_12_yrs", "63. Nur-ili (Son of Enlil-nasir I; 12 yrs, AKL #63)", 13, "c. 1484-1472 BCE"),
        ("aklr_old_32_ashur_shaduni_akl_64", "64. Ashur-shaduni (Son of Nur-ili, AKL #64)", 13, "c. 1472 BCE"),
        ("aklr_old_33_ashur_rabi_i_akl_65", "65. Ashur-rabi I (Son of Enlil-nasir I, AKL #65)", 13, "c. 1472-1452 BCE"),
        ("aklr_old_34_ashur_nadin_ahhe_i_akl_66", "66. Ashur-nadin-ahhe I (Son of Ashur-rabi I, AKL #66)", 13, "c. 1452-1431 BCE"),
    ]
    for nid, nm, tr, dt in akl_old_1 + akl_old_2:
        nodes.append(N(nid, nm, "mesopotamian", tr, f"{dt} (AKL)", "Old Assyrian King", ["Assyrian King List (Pruzsinszky Tables 17a-b)"], f"Old Assyrian ruler: {nm}.", major=False))
    nodes.append(N("aklr_old_yasmah_adad", "Yasmah-Adad of Mari (Younger Son of Shamshi-Adad I, Mari Letters)", "mesopotamian", 11, "c. 1796-1776 BCE (Mari Archives)", "Viceroy of Mari & Brother of Ishme-Dagan I", ["Mari Archives", "Assyrian King List"], "Younger son of Shamshi-Adad I appointed ruler of Mari; famed recipient of royal letters from his father and brother."))
    edges.append(E("akl_39_40_shamshi_adad1", "aklr_old_yasmah_adad", "direct", "Shamshi-Adad I -> younger son Yasmah-Adad of Mari"))
    edges.append(E("aklr_anc_09_aminu_akl_26", "aklr_old_01_sulili_akl_27", "direct", "AKL: Aminu -> Sulili"))
    link_seq(edges, [x[0] for x in akl_old_1] + ["akl_39_40_shamshi_adad1"] + [x[0] for x in akl_old_2], "direct", "Old Assyrian royal succession (AKL 27-66)")

    # D. AKL Middle Assyrian Dynasty (AKL 67-97)
    akl_mid_1 = [
        ("aklr_mid_01_enlil_nasir_ii_akl_67_6_yrs", "67. Enlil-nasir II (Brother of Ashur-nadin-ahhe I; 6 yrs, AKL #67)", 14, "c. 1430-1425 BCE"),
        ("aklr_mid_02_ashur_nirari_ii_akl_68_7_yrs", "68. Ashur-nirari II (Son of Enlil-nasir II; 7 yrs, AKL #68)", 14, "c. 1424-1418 BCE"),
        ("aklr_mid_03_ashur_bel_nisheshu_akl_69_9_", "69. Ashur-bel-nisheshu (Son of Ashur-nirari II; 9 yrs, AKL #69)", 14, "c. 1417-1409 BCE"),
        ("aklr_mid_04_ashur_rim_nisheshu_akl_70_8_", "70. Ashur-rim-nisheshu (Son of Ashur-bel-nisheshu; 8 yrs, AKL #70)", 14, "c. 1408-1401 BCE"),
        ("aklr_mid_05_ashur_nadin_ahhe_ii_akl_71_1", "71. Ashur-nadin-ahhe II (Son of Ashur-rim-nisheshu; 10 yrs, AKL #71)", 14, "c. 1400-1391 BCE"),
        ("aklr_mid_06_eriba_adad_i_akl_72_27_yrs", "72. Eriba-Adad I (Son of Ashur-bel-nisheshu; 27 yrs, AKL #72)", 14, "c. 1390-1364 BCE"),
    ]
    akl_mid_2 = [
        ("aklr_mid_07_enlil_nirari_akl_74_10_yrs", "74. Enlil-nirari (Son of Ashur-uballit I; 10 yrs, AKL #74)", 15, "1327-1318 BCE"),
        ("aklr_mid_08_arik_den_ili_akl_75_12_yrs", "75. Arik-den-ili (Son of Enlil-nirari; 12 yrs, AKL #75)", 15, "1317-1306 BCE"),
        ("aklr_mid_09_adad_nirari_i_akl_76_32_yrs", "76. Adad-nirari I (Son of Arik-den-ili; 32 yrs, AKL #76)", 15, "1305-1274 BCE"),
        ("aklr_mid_10_shalmaneser_i_akl_77_30_yrs", "77. Shalmaneser I (Son of Adad-nirari I; 30 yrs, AKL #77)", 15, "1273-1244 BCE"),
        ("aklr_mid_11_tukulti_ninurta_i_akl_78_37_", "78. Tukulti-Ninurta I (Son of Shalmaneser I; 37 yrs, Conqueror of Babylon, AKL #78)", 15, "1243-1207 BCE"),
        ("aklr_mid_12_ashur_nadin_apli_akl_79_4_yr", "79. Ashur-nadin-apli (Son of Tukulti-Ninurta I; 4 yrs, AKL #79)", 16, "1206-1203 BCE"),
        ("aklr_mid_13_ashur_nirari_iii_akl_80_6_yr", "80. Ashur-nirari III (Son of Ashur-nasir-apli; 6 yrs, AKL #80)", 16, "1202-1197 BCE"),
        ("aklr_mid_14_enlil_kudurri_usur_akl_81_5_", "81. Enlil-kudurri-usur (Son of Tukulti-Ninurta I; 5 yrs, AKL #81)", 16, "1196-1192 BCE"),
        ("aklr_mid_15_ninurta_apil_ekur_akl_82_13_", "82. Ninurta-apil-Ekur (Descendant of Eriba-Adad I; 13 yrs, AKL #82)", 16, "1191-1179 BCE"),
        ("aklr_mid_16_ashur_dan_i_akl_83_46_yrs", "83. Ashur-dan I (Son of Ninurta-apil-Ekur; 46 yrs, AKL #83)", 16, "1178-1133 BCE"),
        ("aklr_mid_17_ninurta_tukulti_ashur_akl_84", "84. Ninurta-tukulti-Ashur (Son of Ashur-dan I, AKL #84)", 16, "c. 1133 BCE"),
        ("aklr_mid_18_mutakkil_nusku_akl_85", "85. Mutakkil-Nusku (Brother of Ninurta-tukulti-Ashur, AKL #85)", 16, "c. 1133 BCE"),
        ("aklr_mid_19_ashur_resh_ishi_i_akl_86_18_", "86. Ashur-resh-ishi I (Son of Mutakkil-Nusku; 18 yrs, AKL #86)", 16, "1132-1115 BCE"),
        ("aklr_mid_20_tiglath_pileser_i_akl_87_39_", "87. Tiglath-Pileser I (Son of Ashur-resh-ishi I; 39 yrs, AKL #87)", 16, "1114-1076 BCE"),
        ("aklr_mid_21_ashared_apil_ekur_akl_88_2_y", "88. Ashared-apil-Ekur (Son of Tiglath-Pileser I; 2 yrs, AKL #88)", 16, "1075-1074 BCE"),
        ("aklr_mid_22_ashur_bel_kala_akl_89_18_yrs", "89. Ashur-bel-kala (Son of Tiglath-Pileser I; 18 yrs, AKL #89)", 16, "1073-1056 BCE"),
        ("aklr_mid_23_eriba_adad_ii_akl_90_2_yrs", "90. Eriba-Adad II (Son of Ashur-bel-kala; 2 yrs, AKL #90)", 16, "1055-1054 BCE"),
        ("aklr_mid_24_shamshi_adad_iv_akl_91_4_yrs", "91. Shamshi-Adad IV (Son of Tiglath-Pileser I; 4 yrs, AKL #91)", 16, "1053-1050 BCE"),
        ("aklr_mid_25_ashurnasirpal_i_akl_92_19_yr", "92. Ashurnasirpal I (Son of Shamshi-Adad IV; 19 yrs, AKL #92)", 16, "1049-1031 BCE"),
        ("aklr_mid_26_shalmaneser_ii_akl_93_12_yrs", "93. Shalmaneser II (Son of Ashurnasirpal I; 12 yrs, AKL #93)", 16, "1030-1019 BCE"),
        ("aklr_mid_27_ashur_nirari_iv_akl_94_6_yrs", "94. Ashur-nirari IV (Son of Shalmaneser II; 6 yrs, AKL #94)", 16, "1018-1013 BCE"),
        ("aklr_mid_28_ashur_rabi_ii_akl_95_41_yrs", "95. Ashur-rabi II (Son of Ashurnasirpal I; 41 yrs, AKL #95)", 16, "1012-972 BCE"),
        ("aklr_mid_29_ashur_resh_ishi_ii_akl_96_5_", "96. Ashur-resh-ishi II (Son of Ashur-rabi II; 5 yrs, AKL #96)", 16, "971-967 BCE"),
        ("aklr_mid_30_tiglath_pileser_ii_akl_97_32", "97. Tiglath-Pileser II (Son of Ashur-resh-ishi II; 32 yrs, AKL #97)", 16, "966-935 BCE"),
    ]
    for nid, nm, tr, dt in akl_mid_1 + akl_mid_2:
        nodes.append(N(nid, nm, "mesopotamian", tr, f"{dt} (AKL)", "Middle Assyrian King", ["Assyrian King List (Pruzsinszky Table 17b)"], f"Middle Assyrian monarch: {nm}.", major=False))
    edges.append(E("aklr_old_34_ashur_nadin_ahhe_i_akl_66", "aklr_mid_01_enlil_nasir_ii_akl_67_6_yrs", "direct", "Brother Enlil-nasir II succeeds Ashur-nadin-ahhe I"))
    link_seq(edges, [x[0] for x in akl_mid_1] + ["akl_73_76_ashuruballit1"] + [x[0] for x in akl_mid_2], "direct", "Middle Assyrian succession (AKL 67-97)")

    # E. AKL Neo-Assyrian Empire (AKL 98-116)
    akl_neo_1 = [
        ("aklr_neo_01_ashur_dan_ii_akl_98_23_yrs", "98. Ashur-dan II (Son of Tiglath-Pileser II; 23 yrs, AKL #98)", 17, "934-912 BCE"),
        ("aklr_neo_02_adad_nirari_ii_akl_99_21_yrs", "99. Adad-nirari II (Son of Ashur-dan II; 21 yrs, AKL #99)", 17, "911-891 BCE"),
        ("aklr_neo_03_tukulti_ninurta_ii_akl_100_7", "100. Tukulti-Ninurta II (Son of Adad-nirari II; 7 yrs, AKL #100)", 17, "890-884 BCE"),
        ("aklr_neo_04_ashurnasirpal_ii_akl_101_25_", "101. Ashurnasirpal II (Son of Tukulti-Ninurta II; 25 yrs, Nimrud, AKL #101)", 17, "883-859 BCE"),
    ]
    akl_neo_2 = [
        ("aklr_neo_05_shamshi_adad_v_akl_103_13_yr", "103. Shamshi-Adad V (Son of Shalmaneser III; 13 yrs, AKL #103)", 17, "823-811 BCE"),
        ("aklr_neo_07_adad_nirari_iii_akl_104_28_y", "104. Adad-nirari III (Son of Shamshi-Adad V & Semiramis; 28 yrs, AKL #104)", 17, "810-783 BCE"),
        ("aklr_neo_08_shalmaneser_iv_akl_105_10_yr", "105. Shalmaneser IV (Son of Adad-nirari III; 10 yrs, AKL #105)", 17, "782-773 BCE"),
        ("aklr_neo_09_ashur_dan_iii_akl_106_763_bc", "106. Ashur-dan III (Son of Adad-nirari III; 763 BCE Eclipse, AKL #106)", 17, "772-755 BCE"),
        ("aklr_neo_10_ashur_nirari_v_akl_107_10_yr", "107. Ashur-nirari V (Son of Adad-nirari III; 10 yrs, AKL #107)", 17, "754-745 BCE"),
        ("aklr_neo_tp3", "108. Tiglath-Pileser III / Pul (18 yrs; 2 Kgs 15:19, AKL #108)", 17, "745-727 BCE"),
        ("aklr_neo_shalm5", "109. Shalmaneser V (Son of Tiglath-Pileser III; Besieged Samaria, AKL #109)", 17, "726-722 BCE"),
        ("aklr_neo_11_sargon_ii_722_705_bce", "110. Sargon II (722–705 BCE, Annexed Samaria)", 17, "722-705 BCE"),
        ("aklr_neo_12_sennacherib_705_681_bce", "111. Sennacherib (Son of Sargon II; 701 BCE Jerusalem Campaign)", 17, "705-681 BCE"),
        ("aklr_neo_13_esarhaddon_681_669_bce", "112. Esarhaddon (Son of Sennacherib; Conquered Egypt 671 BCE)", 17, "681-669 BCE"),
        ("aklr_neo_14_ashurbanipal_669_631_bce", "113. Ashurbanipal (Son of Esarhaddon; Great Library of Nineveh)", 17, "669-631 BCE"),
        ("aklr_neo_15_ashur_etil_ilani_631_627_bce", "114. Ashur-etil-ilani (Son of Ashurbanipal, 631–627 BCE)", 17, "631-627 BCE"),
        ("aklr_neo_16_sin_shar_ishkun_627_612_bce", "115. Sin-shar-ishkun (Son of Ashurbanipal; Fall of Nineveh 612 BCE)", 17, "627-612 BCE"),
        ("aklr_neo_17_ashur_uballit_ii_612_609_bce", "116. Ashur-uballit II (Last King of Assyria at Harran, 612–609 BCE)", 17, "612-609 BCE"),
    ]
    for nid, nm, tr, dt in akl_neo_1 + akl_neo_2:
        nodes.append(N(nid, nm, "mesopotamian", tr, f"{dt} (AKL & Chronicles)", "Neo-Assyrian Emperor", ["Assyrian King List (Pruzsinszky)", "Neo-Assyrian Chronicles"], f"Neo-Assyrian monarch: {nm}.", major=False))
    nodes.append(N("aklr_neo_06_queen_shammuramat_semiramis_", "Queen Shammuramat / Semiramis (Consort of Shamshi-Adad V; Mother & Regent of Adad-nirari III)", "mesopotamian", 17, "c. 811-806 BCE (AKL & Chronicles)", "Historical Queen Regent Behind the Legend of Semiramis", ["Assyrian King List", "Herodotus", "Eusebius"], "Babylonian princess and wife of Shamshi-Adad V who served as coregent/queen mother during the early reign of Adad-nirari III."))
    edges.append(E("aklr_mid_30_tiglath_pileser_ii_akl_97_32", "aklr_neo_01_ashur_dan_ii_akl_98_23_yrs", "direct", "Tiglath-Pileser II -> son Ashur-dan II"))
    link_seq(edges, [x[0] for x in akl_neo_1] + ["akl_102_shalmaneser3"] + [x[0] for x in akl_neo_2], "direct", "Neo-Assyrian royal succession (AKL 98-116)")
    edges += [
        E("aklr_neo_05_shamshi_adad_v_akl_103_13_yr", "aklr_neo_06_queen_shammuramat_semiramis_", "direct", "Queen consort of Shamshi-Adad V"),
        E("aklr_neo_06_queen_shammuramat_semiramis_", "aklr_neo_07_adad_nirari_iii_akl_104_28_y", "direct", "Mother Shammuramat -> Adad-nirari III"),
        E("aklr_neo_12_sennacherib_705_681_bce", "kg_j9_hezekiah", "cognate", "Taylor Prism & 2 Kings 18-19: Sennacherib besieges Hezekiah (701 BCE)"),
        E("aklr_neo_13_esarhaddon_681_669_bce", "af_taharqa", "cognate", "Esarhaddon defeats Kushite Pharaoh Taharqa (671 BCE)"),
    ]

    # F. 21 Gutian Kings + Utu-hegal of Uruk V (Jacobsen AS 11)
    gut_list = [
        ("sklr_gut_01_erridupizir_gutian_1", "1. Erridupizir (First Gutian King of Sumer)"),
        ("sklr_gut_02_imta_gutian_2_3_yrs", "2. Imta' (Gutian King #2, 3 yrs)"),
        ("sklr_gut_03_inkishush_gutian_3_6_yrs", "3. Inkishush (Gutian King #3, 6 yrs)"),
        ("sklr_gut_04_sarlagab_gutian_4_6_yrs", "4. Sarlagab (Gutian King #4, 6 yrs)"),
        ("sklr_gut_05_shulme_gutian_5_6_yrs", "5. Shulme' (Gutian King #5, 6 yrs)"),
        ("sklr_gut_06_elulumesh_gutian_6_6_yrs", "6. Elulumesh (Gutian King #6, 6 yrs)"),
        ("sklr_gut_07_inimabakesh_gutian_7_5_yrs", "7. Inimabakesh (Gutian King #7, 5 yrs)"),
        ("sklr_gut_08_igeshaush_gutian_8_6_yrs", "8. Igeshaush (Gutian King #8, 6 yrs)"),
        ("sklr_gut_09_iarlagab_gutian_9_15_yrs", "9. Iarlagab (Gutian King #9, 15 yrs)"),
        ("sklr_gut_10_ibate_gutian_10_3_yrs", "10. Ibate (Gutian King #10, 3 yrs)"),
        ("sklr_gut_11_iarlangab_gutian_11_3_yrs", "11. Iarlangab (Gutian King #11, 3 yrs)"),
        ("sklr_gut_12_kurum_gutian_12_1_yr", "12. Kurum (Gutian King #12, 1 yr)"),
        ("sklr_gut_13_habil_kin_gutian_13_3_yrs", "13. Habil-kin (Gutian King #13, 3 yrs)"),
        ("sklr_gut_14_laerabum_gutian_14_2_yrs", "14. Laerabum (Gutian King #14, 2 yrs)"),
        ("sklr_gut_15_irarum_gutian_15_2_yrs", "15. Irarum (Gutian King #15, 2 yrs)"),
        ("sklr_gut_16_ibranum_gutian_16_1_yr", "16. Ibranum (Gutian King #16, 1 yr)"),
        ("sklr_gut_17_hablum_gutian_17_2_yrs", "17. Hablum (Gutian King #17, 2 yrs)"),
        ("sklr_gut_18_puzur_sin_of_gutium_gutian_1", "18. Puzur-Sin of Gutium (Son of Hablum, Gutian King #18, 7 yrs)"),
        ("sklr_gut_19_iarlaganda_gutian_19_7_yrs", "19. Iarlaganda (Gutian King #19, 7 yrs)"),
        ("sklr_gut_20_si_um_gutian_20_7_yrs", "20. Si'um (Gutian King #20, 7 yrs)"),
        ("sklr_gut_21_tirigan_gutian_21_40_days", "21. Tirigan (Last Gutian King #21, 40 days — Defeated by Utu-hegal)"),
    ]
    for nid, nm in gut_list:
        nodes.append(N(nid, nm, "mesopotamian", 10, "c. 2154-2112 BCE (SKL Col. vii)", "Gutian King of Sumer", ["Sumerian King List (Jacobsen AS 11 pp. 117-121)"], f"Gutian ruler in Sumer: {nm}.", major=False))
    nodes.append(N("sklr_utu_hegal", "King Utu-hegal of Uruk V (Liberator of Sumer from Tirigan, c. 2112 BCE)", "mesopotamian", 10, "c. 2119-2112 BCE (SKL Col. viii)", "Sole King of Uruk V Who Overthrew Gutium", ["Sumerian King List (Jacobsen AS 11 p. 123)"], "Defeated last Gutian king Tirigan; his governor Ur-Nammu founded the 3rd Dynasty of Ur."))
    edges.append(E("skl_uruk4_gutium_uruk5", "sklr_gut_01_erridupizir_gutian_1", "expansion", "SKL Gutian Dynasty sequence"))
    link_seq(edges, [x[0] for x in gut_list] + ["sklr_utu_hegal"], "expansion", "Gutian dynastic sequence & defeat by Utu-hegal")
    edges.append(E("sklr_utu_hegal", "mes_urnammu", "expansion", "Utu-hegal -> Ur-Nammu (Founder of Ur III)"))

    # G. Isin I Dynasty (All 15 Kings, Jacobsen AS 11)
    isin_list = [
        ("sklr_isin_01_ishbi_erra_33_yrs", "1. Ishbi-Erra of Isin (33 yrs, c. 2017–1985 BCE)"),
        ("sklr_isin_02_shu_ilishu_10_yrs", "2. Shu-ilishu (Son of Ishbi-Erra, 10 yrs)"),
        ("sklr_isin_03_iddin_dagan_21_yrs", "3. Iddin-Dagan (Son of Shu-ilishu, 21 yrs)"),
        ("sklr_isin_04_ishme_dagan_of_isin_20_yrs", "4. Ishme-Dagan of Isin (Son of Iddin-Dagan, 20 yrs)"),
        ("sklr_isin_05_lipit_ishtar_11_yrs_law_code", "5. Lipit-Ishtar (Son of Ishme-Dagan, 11 yrs — Sumerian Law Code)"),
        ("sklr_isin_06_ur_ninurta_28_yrs", "6. Ur-Ninurta (28 yrs)"),
        ("sklr_isin_07_bur_sin_of_isin_21_yrs", "7. Bur-Sin of Isin (Son of Ur-Ninurta, 21 yrs)"),
        ("sklr_isin_08_lipit_enlil_5_yrs", "8. Lipit-Enlil (Son of Bur-Sin, 5 yrs)"),
        ("sklr_isin_09_erra_imitti_8_yrs", "9. Erra-imitti (8 yrs)"),
        ("sklr_isin_10_enlil_bani_24_yrs_gardener_k", "10. Enlil-bani (24 yrs, Gardener Substitute-King)"),
        ("sklr_isin_11_zambia_3_yrs", "11. Zambia (3 yrs)"),
        ("sklr_isin_12_iter_pisha_4_yrs", "12. Iter-pisha (4 yrs)"),
        ("sklr_isin_13_ur_dukuga_4_yrs", "13. Ur-dukuga (4 yrs)"),
        ("sklr_isin_14_sin_magir_11_yrs", "14. Sin-magir (11 yrs)"),
        ("sklr_isin_15_damiq_ilishu_23_yrs", "15. Damiq-ilishu (Son of Sin-magir, 23 yrs — Last King of Isin I)"),
    ]
    for nid, nm in isin_list:
        nodes.append(N(nid, nm, "mesopotamian", 11, "c. 2017-1794 BCE (SKL Col. viii)", "King of Isin I Dynasty", ["Sumerian King List (Jacobsen AS 11 pp. 124-127)"], f"Isin I Dynasty ruler: {nm}.", major=False))
    edges.append(E("mes_ibbisin", "sklr_isin_01_ishbi_erra_33_yrs", "direct", "Collapse of Ur III -> Ishbi-Erra of Isin"))
    edges.append(E("skl_isin1_full", "sklr_isin_01_ishbi_erra_33_yrs", "direct", "Isin I anchor -> Ishbi-Erra"))
    link_seq(edges, [x[0] for x in isin_list], "direct", "Isin I Dynasty succession (SKL Col. viii)")

    # H. Babylon I Amorite Dynasty (True Father->Son Sequence + Rim-Sin)
    bab1_a = [
        ("babr_1_01_sumu_la_el_36_yrs", "2. Sumu-la-El of Babylon (36 yrs, c. 1880–1845 BCE)"),
        ("babr_1_02_sabium_14_yrs", "3. Sabium (Son of Sumu-la-El, 14 yrs)"),
        ("babr_1_03_apil_sin_18_yrs", "4. Apil-Sin (Son of Sabium, 18 yrs)"),
        ("babr_1_04_sin_muballit_20_yrs_father_o", "5. Sin-muballit (Son of Apil-Sin; Father of Hammurabi, 20 yrs)"),
    ]
    bab1_b = [
        ("babr_1_05_samsu_iluna_38_yrs_son_of_ha", "7. Samsu-iluna (Son of Hammurabi, 38 yrs)"),
        ("babr_1_06_abi_eshuh_28_yrs", "8. Abi-eshuh (Son of Samsu-iluna, 28 yrs)"),
        ("babr_1_07_ammi_ditana_37_yrs", "9. Ammi-ditana (Son of Abi-eshuh, 37 yrs)"),
        ("babr_1_08_ammi_saduqa_21_yrs_venus_tab", "10. Ammi-saduqa (Son of Ammi-ditana, 21 yrs — Venus Tablet)"),
        ("babr_1_09_samsu_ditana_31_yrs_fell_to_", "11. Samsu-ditana (Son of Ammi-saduqa, 31 yrs — Fell to Hittites 1595 BCE)"),
    ]
    for nid, nm in bab1_a + bab1_b:
        nodes.append(N(nid, nm, "mesopotamian", 11, "1894-1595 BCE (L.W. King Vol. I)", "Amorite King of Babylon I", ["Early Babylonian Chronicles (L.W. King Vol. I p. 95)"], f"First Dynasty of Babylon king: {nm}.", major=False))
    nodes.append(N("babr_1_10_rim_sin_of_larsa_son_of_kudu", "King Rim-Sin of Larsa (Son of Kudur-Mabuk; Conquered Isin; Rival of Hammurabi)", "mesopotamian", 11, "c. 1822-1763 BCE (L.W. King Vol. I)", "Amorite-Elamite King of Larsa", ["Early Babylonian Chronicles (L.W. King Vol. I)"], "Son of Kudur-Mabuk; conquered Damiq-ilishu of Isin before falling to Hammurabi of Babylon."))
    edges.append(E("mes_sumuabum", "babr_1_01_sumu_la_el_36_yrs", "direct", "Babylon I succession: Sumu-abum -> Sumu-la-El"))
    edges.append(E("bab_dyn1_amorite", "babr_1_01_sumu_la_el_36_yrs", "direct", "Babylon I anchor link"))
    link_seq(edges, [x[0] for x in bab1_a] + ["mes_hammurabi"] + [x[0] for x in bab1_b], "direct", "Babylon I father-to-son pedigree")
    edges.append(E("sklr_isin_15_damiq_ilishu_23_yrs", "babr_1_10_rim_sin_of_larsa_son_of_kudu", "expansion", "Rim-Sin of Larsa conquers Damiq-ilishu of Isin (c. 1794 BCE)"))
    edges.append(E("babr_1_10_rim_sin_of_larsa_son_of_kudu", "mes_hammurabi", "cognate", "Hammurabi defeats Rim-Sin of Larsa (c. 1763 BCE)"))

    # I. Babylon II Sealand Dynasty (All 11 Kings)
    bab2_list = [
        ("babr_2_01_iluma_ilu_60_yrs", "1. Iluma-ilu (60 yrs)"),
        ("babr_2_02_itti_ili_nibi_55_yrs", "2. Itti-ili-nibi (55 yrs)"),
        ("babr_2_03_damqi_ilishu_36_yrs", "3. Damqi-ilishu (36 yrs)"),
        ("babr_2_04_ishkibal_15_yrs", "4. Ishkibal (15 yrs)"),
        ("babr_2_05_shushshi_27_yrs", "5. Shushshi (27 yrs)"),
        ("babr_2_06_gulkishar_55_yrs", "6. Gulkishar (55 yrs)"),
        ("babr_2_07_peshgaldaramesh_50_yrs", "7. Peshgaldaramesh (Son of Gulkishar, 50 yrs)"),
        ("babr_2_08_ayadaragalama_28_yrs", "8. Ayadaragalama (Son of Gulkishar, 28 yrs)"),
        ("babr_2_09_akurduana_26_yrs", "9. Akurduana (26 yrs)"),
        ("babr_2_10_melamkurkurra_7_yrs", "10. Melamkurkurra (7 yrs)"),
        ("babr_2_11_ea_gamil_9_yrs", "11. Ea-gamil (9 yrs — Overthrown by Kassite Ulam-Buriash)"),
    ]
    for nid, nm in bab2_list:
        nodes.append(N(nid, nm, "mesopotamian", 12, "c. 1732-1460 BCE (L.W. King Vol. I)", "King of 1st Sealand Dynasty", ["Early Babylonian Chronicles (L.W. King Vol. I p. 96)"], f"First Sealand Dynasty ruler: {nm}.", major=False))
    edges.append(E("bab_dyn2_sealand", "babr_2_01_iluma_ilu_60_yrs", "expansion", "First Sealand Dynasty sequence"))
    link_seq(edges, [x[0] for x in bab2_list], "expansion", "First Sealand Dynasty succession")

    # J. Babylon III Kassite Dynasty
    bab3_list = [
        ("babr_3_01_gandash_16_yrs", "1. Gandash (16 yrs)", 13),
        ("babr_3_02_agum_i_22_yrs", "2. Agum I (Son of Gandash, 22 yrs)", 13),
        ("babr_3_03_kashtiliash_i_22_yrs", "3. Kashtiliash I (Son of Agum I, 22 yrs)", 13),
        ("babr_3_04_ushshi", "4. Ushshi (Son of Kashtiliash I)", 14),
        ("babr_3_05_abirattash", "5. Abirattash", 14),
        ("babr_3_06_urzigurumash", "6. Urzigurumash", 14),
        ("babr_3_07_agum_ii_restored_marduk", "7. Agum II (Son of Urzigurumash — Restored Marduk Statue)", 14),
        ("babr_3_08_burna_buriash_i", "8. Burna-Buriash I", 14),
        ("babr_3_09_ulam_buriash_conquered_seala", "9. Ulam-Buriash (Son of Burna-Buriash I — Conquered Sealand)", 14),
        ("babr_3_10_burna_buriash_ii_amarna_lett", "10. Burna-Buriash II (Amarna Letters EA 6-11; Wed Ashur-uballit I's Daughter)", 15),
        ("babr_3_11_kudur_enlil", "11. Kudur-Enlil", 15),
        ("babr_3_12_shagarakti_shuriash_13_yrs", "12. Shagarakti-Shuriash (Son of Kudur-Enlil, 13 yrs)", 15),
        ("babr_3_13_meli_shipak", "13. Meli-Shipak", 16),
    ]
    for nid, nm, tr in bab3_list:
        nodes.append(N(nid, nm, "mesopotamian", tr, "c. 1595-1155 BCE (L.W. King Vol. I)", "Kassite King of Babylon", ["Early Babylonian Chronicles (L.W. King Vol. I pp. 101-113)"], f"Kassite Dynasty king: {nm}.", major=False))
    edges.append(E("bab_dyn3_kassite", "babr_3_01_gandash_16_yrs", "expansion", "Kassite Dynasty sequence"))
    link_seq(edges, [x[0] for x in bab3_list], "expansion", "Kassite Dynasty succession")
    edges += [
        E("babr_2_11_ea_gamil_9_yrs", "babr_3_09_ulam_buriash_conquered_seala", "cognate", "Ulam-Buriash overthrows Ea-gamil of the Sealand"),
        E("akl_73_76_ashuruballit1", "babr_3_10_burna_buriash_ii_amarna_lett", "direct", "Marriage of Burna-Buriash II & Ashur-uballit I's daughter Muballitat-Sherua"),
        E("babr_3_10_burna_buriash_ii_amarna_lett", "eg_akhenaten", "cognate", "Amarna Letters EA 6-11 between Burna-Buriash II & Akhenaten"),
    ]

    # K. Babylon X Neo-Babylonian / Chaldean Dynasty
    bab10_nodes = [
        N("babr_10_01_nabopolassar_626_605_bce", "Nabopolassar (Founder of Neo-Babylonian Empire, 626–605 BCE)", "mesopotamian", 17, "626-605 BCE (Babylonian Chronicles)", "Neo-Babylonian Founder & Ally of Cyaxares", ["Babylonian Chronicles", "Eusebius Chronicle"], "Founded the Chaldean Empire and allied with Media to conquer Nineveh (612 BCE); father of Nebuchadnezzar II."),
        N("babr_10_02_amel_marduk_evil_merodach_56", "Amel-Marduk / Evil-Merodach (Son of Nebuchadnezzar II, 562–560 BCE; 2 Kgs 25:27)", "mesopotamian", 17, "562-560 BCE (2 Kings 25:27)", "Son & Successor of Nebuchadnezzar II", ["2 Kings 25:27", "Babylonian Chronicles"], "Son of Nebuchadnezzar II; released King Jehoiachin of Judah from prison in Babylon."),
        N("babr_10_03_neriglissar_560_556_bce", "Neriglissar / Nergal-sharezer (Son-in-Law of Nebuchadnezzar II, 560–556 BCE)", "mesopotamian", 17, "560-556 BCE (Jeremiah 39:3; Chronicles)", "Chaldean King & Brother-in-Law of Amel-Marduk", ["Babylonian Chronicles", "Jeremiah 39:3"], "Married Nebuchadnezzar II's daughter Kashshaya; seized the throne from Amel-Marduk."),
        N("babr_10_04_labashi_marduk_556_bce", "Labashi-Marduk (Son of Neriglissar, 556 BCE)", "mesopotamian", 17, "556 BCE (Babylonian Chronicles)", "Grandson of Nebuchadnezzar II", ["Babylonian Chronicles"], "Young son of Neriglissar deposed after nine months by the Nabonidus conspiracy."),
        N("babr_10_05_nabonidus_556_539_bce", "King Nabonidus (Son of Nabu-balatsu-iqbi & Adad-guppi, 556–539 BCE)", "mesopotamian", 17, "556-539 BCE (Nabonidus Chronicle)", "Last King of Independent Babylon", ["Babylonian Chronicles", "Harran Stelae"], "Resided 10 years at Tayma in Arabia while entrusting Babylon to his eldest son Belshazzar."),
        N("babr_10_06_crown_prince_belshazzar_dani", "Crown Prince Belshazzar (Son & Coregent of Nabonidus, Daniel 5)", "mesopotamian", 17, "d. 539 BCE (Daniel 5; Nabonidus Cylinders)", "Babylonian Crown Prince at the Fall of Babylon", ["Daniel 5", "Nabonidus Chronicle"], "Coregent of Babylon under Nabonidus until the city fell to Cyrus the Great in 539 BCE."),
    ]
    nodes += bab10_nodes
    edges += [
        E("bab_dyn10_chaldean", "babr_10_01_nabopolassar_626_605_bce", "direct", "Chaldean dynasty -> Nabopolassar"),
        E("babr_10_01_nabopolassar_626_605_bce", "for_nebuchadnezzar", "direct", "Father Nabopolassar -> Nebuchadnezzar II"),
        E("for_nebuchadnezzar", "babr_10_02_amel_marduk_evil_merodach_56", "direct", "Nebuchadnezzar II -> son Amel-Marduk"),
        E("for_nebuchadnezzar", "babr_10_03_neriglissar_560_556_bce", "direct", "Nebuchadnezzar II -> son-in-law Neriglissar"),
        E("babr_10_03_neriglissar_560_556_bce", "babr_10_04_labashi_marduk_556_bce", "direct", "Neriglissar -> son Labashi-Marduk"),
        E("babr_10_04_labashi_marduk_556_bce", "babr_10_05_nabonidus_556_539_bce", "expansion", "Labashi-Marduk -> successor Nabonidus"),
        E("babr_10_05_nabonidus_556_539_bce", "babr_10_06_crown_prince_belshazzar_dani", "direct", "Nabonidus -> son & coregent Belshazzar"),
        E("babr_10_06_crown_prince_belshazzar_dani", "ir_cyrus", "cognate", "Fall of Babylon under Belshazzar & Nabonidus to Cyrus (539 BCE)"),
    ]

    return {
        "module": "17_mesopotamia_complete_kinglists",
        "title": "Complete Assyrian King List (All 116 Kings, Pruzsinszky), Remaining Sumerian King List Dynasties (Jacobsen AS 11) & Complete Babylonian Dynasties (L.W. King)",
        "nodes": nodes,
        "edges": edges,
    }
