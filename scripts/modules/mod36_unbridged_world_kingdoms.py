"""
Module 36: Unbridged World Kingdoms & Dynasties (Pending Bridge).
Contains remaining pre-Columbian Americas, Polynesia, and unbridged Sub-Saharan African
royalty & founders awaiting primary-source Biblical/Noahic bridges.
(Malacca graduated in v17; Sparta & N./Central Europe in v18; Benin, Kanem-Bornu,
Vietnam, Java/Majapahit, Khmer/Siam, Japanese Shogunates/Meiji, Korean Goryeo/Joseon,
Chinese Three Kingdoms/Sui/Song/Ming & Classical Greek Sages graduated in Wave 7 / v24.0!)
"""

from . import N, E


def add_chain(nodes, edges, parent_id, items, tradition, era_default, sources, default_type="expansion"):
    prev = parent_id
    for item in items:
        nid, name, tier = item[0], item[1], item[2]
        era = item[3] if len(item) > 3 else era_default
        role = item[4] if len(item) > 4 else "Sovereign / Royal Lineage"
        notes = item[5] if len(item) > 5 else f"Chronicle succession in {', '.join(sources)}."
        major = item[6] if len(item) > 6 else False
        nodes.append(N(nid, name, tradition, tier, era, role, sources, notes, major=major))
        if prev:
            edges.append(E(prev, nid, default_type, f"{', '.join(sources)}: succession"))
        prev = nid


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # 1. AMERICAS & POLYNESIA (~62 individual kings, queens & chiefs under amp_*)
    # =========================================================================
    add_chain(nodes, edges, "amp_aztec_tenochtitlan", [
        ("unb_azt_acamapichtli", "Acamapichtli (1st Tlatoani of Tenochtitlan, 1376–1395)", 13, "1376–1395 CE"),
        ("unb_azt_huitzilihuitl", "Huitzilihuitl (2nd Tlatoani)", 13, "1396–1417 CE"),
        ("unb_azt_chimalpopoca", "Chimalpopoca (3rd Tlatoani)", 14, "1417–1427 CE"),
        ("unb_azt_itzcoatl", "Itzcoatl (Founder of Triple Alliance, 1427–1440)", 14, "1427–1440 CE"),
        ("unb_azt_moctezuma1", "Moctezuma I Ilhuicamina (1440–1469)", 15, "1440–1469 CE"),
        ("unb_azt_axayacatl", "Axayacatl (6th Tlatoani, Sun Stone)", 15, "1469–1481 CE"),
        ("unb_azt_tizoc", "Tizoc (7th Tlatoani)", 16, "1481–1486 CE"),
        ("unb_azt_ahuitzotl", "Ahuitzotl (8th Tlatoani)", 16, "1486–1502 CE"),
        ("unb_azt_moctezuma2", "Moctezuma II Xocoyotzin (1502–1520)", 17, "1502–1520 CE"),
        ("unb_azt_cuitlahuac", "Cuitlahuac (10th Tlatoani, 1520)", 18, "1520 CE"),
        ("unb_azt_cuauhtemoc", "Cuauhtemoc (Final Mexica Emperor, d. 1525)", 18, "1520–1525 CE"),
    ], "americas_pacific", "14th–16th c. CE", ["Codex Mendoza", "Modern Universal History Vol. 14"])

    # Allied/rival Mesoamerican & Caribbean figures under amp_aztec_tenochtitlan
    for cid, cname, t, era, role, note in [
        ("unb_azt_nezahualcoyotl", "Nezahualcoyotl (Poet-King of Texcoco, Triple Alliance)", 15, "1402–1472 CE", "Tlatoani of Texcoco", "Codex Xolotl & Triple Alliance co-founder."),
        ("unb_azt_tlacaelel", "Tlacaelel (Cihuacoatl Architect of Mexica Empire)", 15, "1397–1487 CE", "Chief Vizier (Cihuacoatl)", "Advised Itzcoatl, Moctezuma I, Axayacatl & Ahuitzotl."),
        ("unb_azt_xicotencatl", "Xicotencatl the Younger (General of Tlaxcala)", 17, "1484–1521 CE", "Tlaxcalan Commander", "Opposed Cortes in Modern Universal History Vol. 14 p. 200."),
        ("unb_azt_malintzin_tecuichpotzin", "Tecuichpotzin / Doña Isabel Moctezuma (dau. of Moctezuma II) & Malintzin", 18, "1509–1550 CE", "Mexica Imperial Heiress", "Daughter of Moctezuma II whose descendants entered Spanish Ducal houses (Dukes of Moctezuma de Tultengo)."),
        ("unb_car_guacanagari", "Cacique Guacanagari (Marién, Hispaniola, 1492)", 17, "1492–1494 CE", "Taíno Cacique", "Greeted Columbus on Hispaniola (Mod. Univ. Hist. Vol. 14 p. 145)."),
        ("unb_car_caonabo", "King Caonabo of Maguana (Hispaniola)", 17, "d. 1496 CE", "Taíno Sovereign", "Sovereign who resisted early Spanish forts (Mod. Univ. Hist. Vol. 14 p. 145)."),
    ]:
        nodes.append(N(cid, cname, "americas_pacific", t, era, role, ["Modern Universal History Vol. 14", "Codex Mendoza"], note, major=False))
        edges.append(E("amp_aztec_tenochtitlan", cid, "expansion", "Mesoamerican / Caribbean contact-era dynasty"))

    # Full Inca Sapa Inca list under amp_inca_manco
    add_chain(nodes, edges, "amp_inca_manco", [
        ("unb_inc_sinchi_roca", "Sinchi Roca (2nd Sapa Inca)", 11, "c. 1230 CE"),
        ("unb_inc_lloque_yupanqui", "Lloque Yupanqui (3rd Sapa Inca)", 11, "c. 1260 CE"),
        ("unb_inc_mayta_capac", "Mayta Capac (4th Sapa Inca)", 12, "c. 1290 CE"),
        ("unb_inc_capac_yupanqui", "Capac Yupanqui (5th Sapa Inca)", 12, "c. 1320 CE"),
        ("unb_inc_inca_roca", "Inca Roca (6th Sapa Inca, Hanan Cusco)", 13, "c. 1350 CE"),
        ("unb_inc_yahuar_huacac", "Yahuar Huacac (7th Sapa Inca)", 13, "c. 1380 CE"),
        ("unb_inc_viracocha_inca", "Viracocha Inca (8th Sapa Inca)", 14, "c. 1410–1438 CE"),
        ("unb_inc_pachacuti", "Pachacuti Inca Yupanqui (9th Sapa Inca, Machu Picchu)", 15, "1438–1471 CE"),
        ("unb_inc_tupac_yupanqui", "Tupac Inca Yupanqui (10th Sapa Inca)", 16, "1471–1493 CE"),
        ("unb_inc_huayna_capac", "Huayna Capac (11th Sapa Inca)", 17, "1493–1527 CE"),
        ("unb_inc_huascar", "Huascar Inca (12th Sapa Inca)", 18, "1527–1532 CE"),
        ("unb_inc_atahualpa", "Atahualpa (13th Sapa Inca)", 18, "1532–1533 CE"),
        ("unb_inc_manco_inca", "Manco Inca Yupanqui (Vilcabamba Dynasty)", 19, "1533–1544 CE"),
        ("unb_inc_sayri_tupac", "Sayri Tupac (Vilcabamba)", 19, "1544–1561 CE"),
        ("unb_inc_titu_cusi", "Titu Cusi Yupanqui (Vilcabamba)", 20, "1563–1571 CE"),
        ("unb_inc_tupac_amaru", "Tupac Amaru (Last Sapa Inca of Vilcabamba, 1572)", 20, "1571–1572 CE"),
        ("unb_inc_mama_ocllo_garcilaso", "Coya Mama Ocllo, Quispe Sisa & Chronicler Inca Garcilaso de la Vega (1539–1616)", 20, "15th–17th c. CE"),
    ], "americas_pacific", "13th–16th c. CE", ["Garcilaso de la Vega Royal Commentaries", "Modern Universal History Vol. 14"])
    edges.append(E("amp_inca_pachacuti", "unb_inc_pachacuti", "cognate", "Same Inca sovereign chain expanded individually"))
    nodes.append(N("unb_may_lady_sak_kuk", "Lady Sak K'uk' (Queen Regent & Mother of Pakal the Great of Palenque)", "americas_pacific", 15, "612–640 CE", "Maya Royal Mother", ["Palenque Inscriptions"], "Conveyed the royal Palenque diadem directly to her son K'inich Janaab Pakal I.", major=False))
    edges.append(E("unb_may_lady_yohl_iknal", "unb_may_lady_sak_kuk", "direct", "Palenque royal matrilineal succession -> Pakal"))
    edges.append(E("unb_may_lady_sak_kuk", "unb_may_pakal_great", "direct", "Mother of Pakal the Great"))

    # Maya Classic Royal Houses under amp_maya_four_men
    add_chain(nodes, edges, "amp_maya_four_men", [
        ("unb_may_yax_ehb_xook", "Yax Ehb Xook (Founder of Tikal Dynasty)", 8, "c. 90 CE"),
        ("unb_may_chak_tok_ichaak", "Chak Tok Ich'aak I (Great Jaguar Paw of Tikal)", 13, "360–378 CE"),
        ("unb_may_jasaw_chan_kawiil", "Jasaw Chan K'awiil I (Restorer of Tikal, Temple I)", 16, "682–734 CE"),
    ], "americas_pacific", "Classic Maya", ["Tikal Hieroglyphic Inscriptions"])
    add_chain(nodes, edges, "amp_maya_four_men", [
        ("unb_may_kukinich_yax_kuk_mo", "K'inich Yax K'uk' Mo' (Founder of Copán Dynasty, 426 CE)", 14, "426–437 CE"),
        ("unb_may_18_rabbit", "Waxaklajuun Ub'aah K'awiil ('18 Rabbit' of Copán)", 16, "695–738 CE"),
        ("unb_may_yuknoom_cheen", "Yuknoom Ch'een II ('the Great' of Calakmul)", 16, "636–686 CE"),
        ("unb_may_lady_six_sky", "Lady Six Sky (Wak Chanil Ajaw of Naranjo)", 16, "682–741 CE"),
    ], "americas_pacific", "Classic Maya", ["Copán, Calakmul & Naranjo Stelae"])
    add_chain(nodes, edges, "amp_maya_four_men", [
        ("unb_may_kuk_bahlam1", "K'uk' Bahlam I (Founder of Palenque Dynasty, 431 CE)", 14, "431–435 CE"),
        ("unb_may_lady_yohl_iknal", "Lady Yohl Ik'nal (Queen of Palenque)", 15, "583–604 CE"),
        ("unb_may_pakal_great", "K'inich Janaab Pakal (Pakal the Great of Palenque)", 16, "615–683 CE"),
        ("unb_may_kan_bahlam2", "K'inich Kan Bahlam II (Palenque Cross Group)", 16, "684–702 CE"),
    ], "americas_pacific", "Classic Maya", ["Palenque Temple of the Inscriptions"])

    # North American Indigenous Leaders & Confed. under amp_na_skywoman & amp_na_dine_lakota
    for cid, cname, par, t, era, role in [
        ("unb_na_deganawida", "Deganawida (The Great Peacemaker — Haudenosaunee)", "amp_na_skywoman", 18, "c. 12th–15th c. CE", "Co-Founder of Iroquois League"),
        ("unb_na_hiawatha", "Hiawatha (Ayenwatha — Onondaga/Mohawk)", "unb_na_deganawida", 18, "c. 12th–15th c. CE", "Unifier of the Five Nations"),
        ("unb_na_jigonhsasee", "Jigonhsasee ('Mother of Nations' — Neutral/Seneca)", "unb_na_deganawida", 18, "c. 12th–15th c. CE", "First Clan Mother of Haudenosaunee"),
        ("unb_na_powhatan", "Wahunsenacawh (Paramount Chief Powhatan, d. 1618)", "amp_na_skywoman", 20, "c. 1545–1618 CE", "Tsenacommacah Paramount Chief"),
        ("unb_na_pocahontas", "Matoaka (Pocahontas, Daughter of Powhatan)", "unb_na_powhatan", 20, "1596–1617 CE", "Powhatan Noblewoman"),
        ("unb_na_metacomet", "Metacomet (King Philip of the Wampanoag, d. 1676)", "amp_na_skywoman", 21, "1638–1676 CE", "Sachem of Pokanoket"),
        ("unb_na_tecumseh", "Tecumseh (Shawnee Confederacy Leader, 1768–1813)", "amp_na_skywoman", 21, "1768–1813 CE", "Pan-Indigenous Leader"),
        ("unb_na_sequoyah", "Sequoyah (Cherokee Syllabary Creator, c. 1770–1843)", "amp_na_skywoman", 21, "c. 1770–1843 CE", "Cherokee Scholar"),
        ("unb_na_sitting_bull", "Tȟatȟáŋka Íyotake (Sitting Bull, Hunkpapa Lakota)", "amp_na_dine_lakota", 21, "1831–1890 CE", "Lakota Chief & Holy Man"),
        ("unb_na_crazy_horse", "Tȟašúŋke Witkó (Crazy Horse, Oglala Lakota)", "amp_na_dine_lakota", 21, "c. 1840–1877 CE", "Oglala War Leader"),
    ]:
        nodes.append(N(cid, cname, "americas_pacific", t, era, role, ["Indigenous Oral History", "North American Chronicles"], f"{cname}.", major=False))
        edges.append(E(par, cid, "expansion", "North American indigenous historical succession"))

    # Polynesia / Hawaii / Tonga / Samoa / Tahiti
    add_chain(nodes, edges, "amp_poly_kumulipo", [
        ("unb_ply_kamehameha1", "King Kamehameha I the Great (Unifier of Hawai'i, 1795)", 21, "1758–1819 CE"),
        ("unb_ply_kamehameha2", "King Kamehameha II (Liholiho)", 21, "1797–1824 CE"),
        ("unb_ply_kamehameha3", "King Kamehameha III (Kauikeaouli)", 21, "1814–1854 CE"),
        ("unb_ply_kalakaua", "King David Kalakaua (Monarch of Hawai'i)", 21, "1836–1891 CE"),
        ("unb_ply_liliuokalani", "Queen Lili'uokalani (Final Sovereign Queen of Hawai'i)", 21, "1838–1917 CE"),
    ], "americas_pacific", "18th–19th c. CE", ["Hawaiian Royal Mo'okū'auhau", "Kumulipo"])
    for cid, cname, era, role in [
        ("unb_ply_aho_eitu", "'Aho'eitu (1st Tu'i Tonga of Tonga Empire, c. 950 CE)", "c. 950 CE", "Tu'i Tonga Founder"),
        ("unb_ply_salamasina", "Queen Salamasina (Tafa'ifa of Samoa, c. 1500 CE)", "c. 1500 CE", "Paramount Queen of Samoa"),
        ("unb_ply_pomare1", "King Pomare I (Unifier of Kingdom of Tahiti)", "1743–1803 CE", "King of Tahiti"),
    ]:
        nodes.append(N(cid, cname, "americas_pacific", 19, era, role, ["Polynesian Royal Whakapapa"], f"{cname}.", major=False))
        edges.append(E("amp_poly_kupe_tonga", cid, "expansion", "Polynesian island sovereign dynasty"))

    # =========================================================================
    # 2. INDEPENDENT SUB-SAHARAN AFRICAN KINGDOMS (~38 nodes — NOT Noahic-linked!)
    # =========================================================================
    add_chain(nodes, edges, None, [
        ("afr_buganda_kintu", "Buganda Kingdom Founders: Kintu & Nambi → Kabaka Chwa I", 10, "c. 13th c. CE", "Buganda Mythic-Royal Founders", "Basimba / Baganda oral dynasty preceding direct Biblical links.", True),
        ("unb_afr_kimera", "Kabaka Kimera (3rd King of Buganda, Bunyoro Link)", 18, "c. 14th–15th c. CE"),
        ("unb_afr_ssuuna2", "Kabaka Ssuuna II of Buganda (1832–1856)", 21, "1832–1856 CE"),
        ("unb_afr_muteesa1", "Kabaka Muteesa I of Buganda (1856–1884)", 21, "1856–1884 CE"),
        ("unb_afr_mwanga2", "Kabaka Mwanga II of Buganda (1884–1899)", 21, "1884–1899 CE"),
    ], "african", "13th–19th c. CE", ["Baganda Royal Chronicle (Apolo Kagwa)"])
    for cid, cname, role in [
        ("unb_afr_rukidi_bunyoro", "Rukidi Mpuga (1st Bito King of Bunyoro-Kitara)", "Bito Dynasty Founder"),
        ("unb_afr_gikuyu_mumbi", "Gikuyu & Mumbi (Progenitors of the 9 Agikuyu Clans)", "Kikuyu Founders"),
        ("unb_afr_gihanga_rwanda", "King Gihanga (Founder of the Kingdom of Rwanda)", "Nyiginya Founder"),
        ("unb_afr_ruganzu2_rwanda", "Mwami Ruganzu II Ndori of Rwanda (16th c.)", "Mwami of Rwanda"),
        ("unb_afr_kigeli4_rwanda", "Mwami Kigeli IV Rwabugiri (1853–1895)", "Mwami of Rwanda"),
    ]:
        nodes.append(N(cid, cname, "african", 19, "East African Kingdoms", role, ["Great Lakes Oral Chronicles"], f"{cname}.", major=False))
        edges.append(E("afr_buganda_kintu", cid, "expansion", "Great Lakes / East African regional dynasty"))

    add_chain(nodes, edges, None, [
        ("afr_kongo_lukeni", "Kingdom of Kongo: Lukeni lua Nimi (c. 1390 CE, Mbanza-Kongo)", 19, "c. 1390 CE", "1st Manikongo", "Mod. Univ. Hist. Vols. 6-7 & Portuguese chronicles.", True),
        ("unb_afr_nzinga_nkuwu", "Nzinga a Nkuwu / King Joao I of Kongo (Baptized 1491)", 20, "1470–1509 CE"),
        ("unb_afr_afonso1_kongo", "King Afonso I of Kongo (Mvemba a Nzinga, 1509–1542)", 21, "1509–1542 CE"),
        ("unb_afr_alvaro1_kongo", "King Alvaro I of Kongo (1568–1587)", 21, "1568–1587 CE"),
        ("unb_afr_garcia2_kongo", "King Garcia II of Kongo (1641–1660)", 21, "1641–1660 CE"),
        ("unb_afr_ngola_kiluanje", "Ngola Kiluanje (Founder of Ndongo / Angola)", 20, "c. 1515 CE"),
        ("unb_afr_queen_nzinga", "Queen Nzinga Mbande of Ndongo & Matamba (1583–1663)", 21, "1583–1663 CE"),
    ], "african", "14th–17th c. CE", ["Modern Universal History Vols. 6-7", "Kongo Royal Letters"])

    add_chain(nodes, edges, None, [
        ("afr_zimbabwe_mutota", "Great Zimbabwe & Mutapa: Nyatsimba Mutota → Nyanhewe Matope", 19, "c. 1420–1480 CE", "Mwene Mutapa Founders", "Central-Southern African stone-citadel kingdoms.", True),
        ("unb_afr_senzangakhona", "Senzangakhona kaJama (Zulu Chief)", 21, "1762–1816 CE"),
        ("unb_afr_queen_nandi", "Queen Nandi kaBhebhe (Mother of King Shaka Zulu, c. 1760–1827)", 21, "c. 1760–1827 CE"),
        ("unb_afr_shaka_zulu", "King Shaka kaSenzangakhona (Founder of Zulu Kingdom, 1816–1828)", 21, "1816–1828 CE"),
        ("unb_afr_dingane", "King Dingane & King Mpande of the Zulus", 21, "1828–1872 CE"),
        ("unb_afr_cetshwayo", "King Cetshwayo kaMpande (1872–1884)", 21, "1872–1884 CE"),
    ], "african", "15th–19th c. CE", ["Southern African Oral & Historical Chronicles"])

    add_chain(nodes, edges, None, [
        ("unb_afr_osei_tutu", "Ashanti Empire (Kumasi): Asantehene Osei Tutu I (Golden Stool, 1701)", 21, "1701–1717 CE", "Founder of Ashanti Empire", "Akan-Ashanti state foundation.", True),
        ("unb_afr_opoku_ware", "Asantehene Opoku Ware I (1720–1750)", 21, "1720–1750 CE"),
        ("unb_afr_osei_bonsu", "Asantehene Osei Bonsu (1804–1824)", 21, "1804–1824 CE"),
        ("unb_afr_yaa_asantewaa", "Nana Yaa Asantewaa (Queen Mother of Ejisu, 1900)", 21, "1840–1921 CE"),
    ], "african", "18th–19th c. CE", ["Modern Universal History Vol. 7", "Ashanti Chronicles"])

    for cid, cname, era, role in [
        ("unb_afr_houegbadja", "King Houegbadja (Founder of Dahomey, c. 1645–1685)", "1645–1685 CE", "King of Dahomey"),
        ("unb_afr_agaja", "King Agaja & King Ghezo of Dahomey", "1708–1858 CE", "Kings of Dahomey"),
        ("unb_afr_behanzin", "King Behanzin of Dahomey (1889–1894)", "1889–1894 CE", "Final Independent Dahomey King"),
    ]:
        nodes.append(N(cid, cname, "african", 21, era, role, ["West African Kingdom Chronicles", "Mod. Univ. Hist. Vol. 7"], f"{cname}.", major=False))
        edges.append(E("unb_afr_osei_tutu", cid, "expansion", "West African forest-belt sovereign tradition"))

    return {
        "module": "36_unbridged_world_kingdoms",
        "title": "Pre-Columbian Americas, Polynesia & Unbridged Sub-Saharan African Kingdoms (Pending Bridge)",
        "nodes": nodes,
        "edges": edges,
    }
