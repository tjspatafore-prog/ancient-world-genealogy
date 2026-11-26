"""
Module 36: Unbridged World Kingdoms, Dynasties & Classical Thinkers (Pending Bridge).
Contains 220+ individual world rulers, queens, dynasties, and classical philosophers
across the Americas, Polynesia, Sub-Saharan Africa, Southeast Asia, Japanese Shogunates,
Korean Goryeo/Joseon, Chinese Three Kingdoms/Song/Ming, Classical Greek Thinkers, and
Central/Northern European Houses — awaiting primary-source Biblical/Noahic bridges.

IMPORTANT: Zero edges from this module connect to Adam, Noah, or any Biblical/Noahic node.
They populate the 'All' scope tab cleanly and appear under 'Pending Bridge'.
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
    ], "americas_pacific", "13th–16th c. CE", ["Garcilaso de la Vega Royal Commentaries", "Modern Universal History Vol. 14"])
    edges.append(E("amp_inca_pachacuti", "unb_inc_pachacuti", "cognate", "Same Inca sovereign chain expanded individually"))

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
        ("unb_afr_shaka_zulu", "King Shaka kaSenzangakhona (Founder of Zulu Kingdom, 1816–1828)", 21, "1816–1828 CE"),
        ("unb_afr_dingane", "King Dingane & King Mpande of the Zulus", 21, "1828–1872 CE"),
        ("unb_afr_cetshwayo", "King Cetshwayo kaMpande (1872–1884)", 21, "1872–1884 CE"),
    ], "african", "15th–19th c. CE", ["Southern African Oral & Historical Chronicles"])

    add_chain(nodes, edges, None, [
        ("unb_afr_kanem_dugu", "Kanem-Bornu Empire: King Dugu (Sefawa) → Mai Humai (c. 1075 CE)", 19, "8th–11th c. CE", "Sayfawa / Duguwa Roots", "Girgam Chronicle of Kanem-Bornu.", True),
        ("unb_afr_dunama_dabbalemi", "Mai Dunama Dabbalemi (Kanem Peak, c. 1210–1248)", 20, "1210–1248 CE"),
        ("unb_afr_idris_alooma", "Mai Idris Alooma of Bornu (1571–1603)", 21, "1571–1603 CE"),
    ], "african", "Medieval Chad Basin", ["Diwan / Girgam of Bornu"])

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
        ("unb_afr_ewuare_benin", "Oba Ewuare the Great of Benin (1440–1473)", "1440–1473 CE", "Oba of Benin"),
        ("unb_afr_esigie_ovonramwen", "Oba Ozolua → Oba Esigie → Oba Ovonramwen of Benin", "1481–1897 CE", "Obas of Benin"),
    ]:
        nodes.append(N(cid, cname, "african", 21, era, role, ["West African Kingdom Chronicles", "Mod. Univ. Hist. Vol. 7"], f"{cname}.", major=False))
        edges.append(E("unb_afr_osei_tutu", cid, "expansion", "West African forest-belt sovereign tradition"))

    # =========================================================================
    # 3. SOUTHEAST ASIAN EMPIRES (~38 nodes — Khmer, Siam, Srivijaya/Java, Vietnam)
    # =========================================================================
    add_chain(nodes, edges, None, [
        ("sea_khmer_jayavarman2", "Funan & Angkor Founders: Kaundinya I (+ Queen Soma) → Jayavarman II (802 CE, Chakravartin)", 19, "1st–9th c. CE", "Founders of Funan & Angkor Empire", "Early Cambodian & Chinese records of Funan/Chenla & Angkor.", True),
        ("unb_sea_indravarman1", "Indravarman I (Preah Ko & Bakong)", 19, "877–889 CE"),
        ("unb_sea_yasovarman1", "Yasovarman I (Founder of Yasodharapura / Angkor)", 19, "889–910 CE"),
        ("unb_sea_suryavarman1", "Suryavarman I of Angkor (1006–1050)", 20, "1006–1050 CE"),
        ("unb_sea_suryavarman2", "Suryavarman II (Builder of Angkor Wat, 1113–1150)", 20, "1113–1150 CE"),
        ("unb_sea_jayavarman7", "Jayavarman VII (Builder of Angkor Thom & Bayon, 1181–1218)", 20, "1181–1218 CE"),
    ], "southeast_asia", "1st–13th c. CE", ["Khmer Inscriptions", "Zhou Daguan"])

    add_chain(nodes, edges, "sea_khmer_jayavarman2", [
        ("unb_sea_sri_indraditya", "Sri Indraditya (Founder of Sukhothai Kingdom, 1238)", 20, "1238–1270 CE"),
        ("unb_sea_ram_khamhaeng", "King Ram Khamhaeng the Great (Thai Alphabet, 1279–1298)", 20, "1279–1298 CE"),
        ("unb_sea_uthong", "King Uthong / Ramathibodi I (Founder of Ayutthaya, 1351)", 20, "1351–1369 CE"),
        ("unb_sea_trailok", "King Borommatrailokkanat / Trailok (1448–1488)", 20, "1448–1488 CE"),
        ("unb_sea_naresuan", "King Naresuan the Great of Ayutthaya (1590–1605)", 21, "1590–1605 CE"),
        ("unb_sea_narai", "King Narai the Great (1656–1688)", 21, "1656–1688 CE"),
        ("unb_sea_taksin", "King Taksin the Great (Thonburi, 1767–1782)", 21, "1767–1782 CE"),
        ("unb_sea_rama1_chakri", "King Rama I (Founder of Chakri Dynasty of Siam, 1782)", 21, "1782–1809 CE"),
        ("unb_sea_mongkut_chulalongkorn", "King Mongkut (Rama IV) → King Chulalongkorn (Rama V)", 21, "1851–1910 CE"),
    ], "southeast_asia", "13th–20th c. CE", ["Royal Chronicles of Ayutthaya & Siam"])

    add_chain(nodes, edges, None, [
        ("sea_java_raden_wijaya", "Srivijaya, Medang & Majapahit: Dapunta Hyang → Sanjaya → Airlangga → Raden Wijaya (1293)", 20, "671–1309 CE", "Maritime Indonesian Founders", "Srivijaya, Mataram, Singhasari & Majapahit.", True),
        ("unb_sea_tribhuwana", "Queen Tribhuwana Wijayatunggadewi of Majapahit (1328–1350)", 20, "1328–1350 CE"),
        ("unb_sea_hayam_wuruk", "Hayam Wuruk & Prime Minister Gajah Mada (Majapahit Peak, 1350–1389)", 20, "1350–1389 CE"),
        ("unb_sea_parameswara", "Parameswara / Iskandar Shah (Founder of Malacca Sultanate, 1400)", 20, "1400–1414 CE"),
        ("unb_sea_mansur_shah", "Sultan Mansur Shah of Malacca (1459–1477)", 20, "1459–1477 CE"),
    ], "southeast_asia", "7th–15th c. CE", ["Nagarakretagama", "Sejarah Melayu / Malay Annals"])
    for cid, cname, era in [
        ("unb_sea_balaputradewa", "Balaputradewa of Srivijaya (Shailendra Dynasty)", "9th c. CE"),
        ("unb_sea_ken_arok", "Ken Arok & King Kertanegara of Singhasari", "1222–1292 CE"),
    ]:
        nodes.append(N(cid, cname, "southeast_asia", 19, era, "Javanese/Sumatran Monarch", ["Pararaton", "Nalanda Inscription"], f"{cname}.", major=False))
        edges.append(E("sea_java_raden_wijaya", cid, "expansion", "Archipelagic Indonesian lineage"))

    add_chain(nodes, edges, None, [
        ("unb_sea_lac_long_quan", "Vietnam Ancient Origins: Lac Long Quan & Au Co → Hung Vuong Kings (Van Lang)", 8, "Legendary Bronze Age", "Hong Bang Founders", "Dai Viet Su Ky Toan Thu.", True),
        ("unb_sea_an_duong_vuong", "An Duong Vuong (Kingdom of Au Lac / Co Loa)", 13, "c. 257–207 BCE"),
        ("unb_sea_trung_sisters", "Trung Sisters (Trung Trac & Trung Nhi, 40–43 CE)", 19, "40–43 CE"),
        ("unb_sea_ngo_quyen", "Ngo Quyen (Bach Dang Victory & Independence, 938 CE)", 19, "938–944 CE"),
        ("unb_sea_dinh_bo_linh", "Dinh Bo Linh (Emperor of Dai Co Viet, 968 CE)", 19, "968–979 CE"),
        ("unb_sea_ly_thai_to", "Ly Thai To (Founder of Later Ly Dynasty, Thang Long / Hanoi, 1009)", 20, "1009–1028 CE"),
        ("unb_sea_tran_thai_tong", "Tran Thai Tong & General Tran Hung Dao (Defeated Kublai's Fleets)", 20, "1225–1300 CE"),
        ("unb_sea_le_loi", "Le Loi (Le Thai To, Founder of Later Le Dynasty, 1428)", 20, "1428–1433 CE"),
        ("unb_sea_gia_long", "Emperor Gia Long (Unifier of Nguyen Dynasty Vietnam, 1802)", 21, "1802–1820 CE"),
    ], "southeast_asia", "Ancient to 19th c. CE", ["Dai Viet Su Ky Toan Thu"])

    # =========================================================================
    # 4. EAST ASIAN SHOGUNATES, GORYEO/JOSEON & THREE KINGDOMS/SONG/MING (~31 nodes)
    # =========================================================================
    add_chain(nodes, edges, None, [
        ("unb_jpn_yoritomo", "Minamoto no Yoritomo (1st Kamakura Shogun, 1192)", 20, "1147–1199 CE", "1st Shogun of Japan", "Mod. Univ. Hist. Vol. 5 & Azuma Kagami.", True),
        ("unb_jpn_hojo_tokimasa", "Hojo Tokimasa (Shikken Regency of Kamakura)", 20, "1138–1215 CE"),
        ("unb_jpn_ashikaga_takauji", "Ashikaga Takauji (1st Muromachi Shogun, 1338)", 20, "1305–1358 CE"),
        ("unb_jpn_ashikaga_yoshimitsu", "Ashikaga Yoshimitsu (Golden Pavilion Kinkaku-ji)", 20, "1358–1408 CE"),
        ("unb_jpn_oda_nobunaga", "Oda Nobunaga (1st Great Unifier of Sengoku Japan)", 21, "1534–1582 CE"),
        ("unb_jpn_hideyoshi", "Toyotomi Hideyoshi (2nd Great Unifier)", 21, "1537–1598 CE"),
        ("unb_jpn_tokugawa_ieyasu", "Tokugawa Ieyasu (Founder of Edo Shogunate, 1603)", 21, "1543–1616 CE"),
        ("unb_jpn_tokugawa_hidetada", "Tokugawa Hidetada (2nd Tokugawa Shogun)", 21, "1579–1632 CE"),
        ("unb_jpn_tokugawa_iemitsu", "Tokugawa Iemitsu (3rd Tokugawa Shogun)", 21, "1604–1651 CE"),
        ("unb_jpn_tokugawa_yoshinobu", "Tokugawa Yoshinobu (15th & Final Tokugawa Shogun)", 21, "1837–1913 CE"),
        ("unb_jpn_emperor_meiji", "Emperor Meiji (Meiji Restoration, 1868)", 21, "1852–1912 CE"),
    ], "japan_korea", "12th–20th c. CE", ["Modern Universal History Vol. 5", "Japanese Chronicles"])

    add_chain(nodes, edges, None, [
        ("unb_kor_wang_geon", "Taejo Wang Geon (Founder of Goryeo Dynasty, 918 CE)", 19, "877–943 CE", "Goryeo Founder", "Goryeosa & Joseon Wangjo Sillok.", True),
        ("unb_kor_gwangjong", "King Gwangjong of Goryeo", 19, "925–975 CE"),
        ("unb_kor_yi_seonggye", "Taejo Yi Seong-gye (Founder of Joseon Dynasty, 1392)", 20, "1335–1408 CE"),
        ("unb_kor_taejong", "King Taejong of Joseon (Yi Bang-won)", 20, "1367–1422 CE"),
        ("unb_kor_sejong_great", "King Sejong the Great (Hangul Alphabet, 1418–1450)", 20, "1397–1450 CE"),
        ("unb_kor_sejo", "King Sejo of Joseon", 20, "1417–1468 CE"),
        ("unb_kor_yi_sunsin", "Admiral Yi Sun-sin (Joseon Naval Hero)", 21, "1545–1598 CE"),
        ("unb_kor_yeongjo_jeongjo", "King Yeongjo → King Jeongjo of Joseon", 21, "1694–1800 CE"),
        ("unb_kor_gojong", "Emperor Gojong (Final Joseon Monarch / Korean Empire)", 21, "1852–1919 CE"),
    ], "japan_korea", "10th–20th c. CE", ["Goryeosa", "Veritable Records of the Joseon Dynasty"])

    add_chain(nodes, edges, None, [
        ("unb_chn_cao_cao", "Cao Cao → Emperor Wen of Wei (Cao Pi, Three Kingdoms)", 19, "155–226 CE", "Cao Wei Founders", "Records of the Three Kingdoms.", True),
        ("unb_chn_wen_sui", "Emperor Wen of Sui (Yang Jian, Reunified China 581 CE)", 19, "541–604 CE"),
        ("unb_chn_song_taizu", "Emperor Taizu of Song (Zhao Kuangyin, 960 CE)", 20, "927–976 CE"),
        ("unb_chn_song_huizong", "Emperor Huizong of Song", 20, "1082–1135 CE"),
        ("unb_chn_ming_hongwu", "Emperor Hongwu (Zhu Yuanzhang, Founder of Ming Dynasty, 1368)", 20, "1328–1398 CE"),
        ("unb_chn_ming_yongle", "Emperor Yongle (Zhu Di) & Admiral Zheng He (Treasure Fleets)", 20, "1360–1424 CE"),
    ], "chinese", "3rd–15th c. CE", ["Records of the Three Kingdoms", "History of Song & Ming"])
    for cid, cname, role in [
        ("unb_chn_liu_bei_zhuge", "Liu Bei (Emperor of Shu Han) & Chancellor Zhuge Liang", "Shu Han Rulers"),
        ("unb_chn_sun_quan", "Sun Quan (Emperor of Eastern Wu)", "Eastern Wu Founder"),
    ]:
        nodes.append(N(cid, cname, "chinese", 19, "Three Kingdoms (220–280 CE)", role, ["Sanguozhi / Three Kingdoms"], f"{cname}.", major=False))
        edges.append(E("unb_chn_cao_cao", cid, "cognate", "Contemporaries of China's Three Kingdoms era"))

    # =========================================================================
    # 5. CLASSICAL GREEK SAGES & CENTRAL/NORTHERN EUROPEAN HOUSES (~64 nodes)
    # =========================================================================
    add_chain(nodes, edges, None, [
        ("unb_grk_thales", "Seven Sages & Ionian Philosophers: Thales of Miletus → Anaximander", 17, "c. 624–546 BCE", "Ionian Philosophy Founders", "Lives of Ancient Philosophers (1702) & Diogenes Laertius.", True),
        ("unb_grk_pythagoras", "Pythagoras of Samos (Mathematics & Harmonics)", 17, "c. 570–495 BCE"),
        ("unb_grk_socrates", "Socrates of Athens (Teacher of Classical Philosophy)", 18, "470–399 BCE"),
        ("unb_grk_plato", "Plato (Founder of the Academy, Athens)", 18, "428–348 BCE"),
        ("unb_grk_aristotle", "Aristotle of Stagira (Founder of the Lyceum, Tutor of Alexander)", 18, "384–322 BCE"),
    ], "greek", "6th–4th c. BCE", ["The Lives of the Ancient Philosophers (1702)", "Plutarch Lives"])
    for cid, cname, era, role in [
        ("unb_grk_homer_hesiod", "Homer & Hesiod (Epic Poets of Greece)", "c. 8th–7th c. BCE", "Epic Poets"),
        ("unb_grk_heraclitus", "Heraclitus of Ephesus", "c. 535–475 BCE", "Pre-Socratic Philosopher"),
        ("unb_grk_parmenides", "Parmenides & Zeno of Elea", "c. 515–430 BCE", "Eleatic Philosophers"),
        ("unb_grk_empedocles", "Empedocles of Acragas", "c. 494–434 BCE", "Philosopher"),
        ("unb_grk_democritus", "Leucippus & Democritus (Atomic Theory)", "c. 460–370 BCE", "Atomist Philosophers"),
        ("unb_grk_hippocrates", "Hippocrates of Kos (Father of Medicine)", "c. 460–370 BCE", "Physician"),
        ("unb_grk_diogenes", "Diogenes of Sinope (Cynic School)", "c. 412–323 BCE", "Philosopher"),
        ("unb_grk_epicurus", "Epicurus (The Garden, Athens)", "341–270 BCE", "Philosopher"),
        ("unb_grk_zeno_stoic", "Zeno of Citium (Founder of Stoicism)", "c. 334–262 BCE", "Stoic Founder"),
        ("unb_grk_euclid", "Euclid of Alexandria (Elements of Geometry)", "c. 300 BCE", "Mathematician"),
        ("unb_grk_archimedes", "Archimedes of Syracuse (287–212 BCE)", "287–212 BCE", "Mathematician & Engineer"),
        ("unb_grk_herodotus_thucydides", "Herodotus of Halicarnassus, Thucydides & Xenophon", "5th–4th c. BCE", "Classical Greek Historians"),
    ]:
        nodes.append(N(cid, cname, "greek", 18, era, role, ["Lives of Ancient Philosophers (1702)", "Herodotus", "Thucydides"], f"{cname}.", major=False))
        edges.append(E("unb_grk_thales", cid, "cognate", "Greek philosophical and literary lineage"))

    add_chain(nodes, edges, None, [
        ("unb_grk_solon_lycurgus", "Greek Lawgivers: Lycurgus of Sparta & Solon of Athens → Cleisthenes", 17, "8th–6th c. BCE", "Constitutional Founders", "Plutarch Lives Vols. 1-5.", True),
        ("unb_grk_miltiades_themistocles", "Miltiades (Marathon, 490 BCE) & Themistocles (Salamis, 480 BCE)", 18, "5th c. BCE"),
        ("unb_grk_leonidas", "King Leonidas I of Sparta (Thermopylae, 480 BCE)", 18, "d. 480 BCE"),
        ("unb_grk_pericles", "Pericles of Athens (Golden Age Statesman, d. 429 BCE)", 18, "495–429 BCE"),
        ("unb_grk_alcibiades_lysander", "Alcibiades of Athens & Lysander of Sparta", 18, "5th c. BCE"),
        ("unb_grk_epaminondas", "Epaminondas of Thebes (Battle of Leuctra, 371 BCE)", 18, "d. 362 BCE"),
        ("unb_grk_pyrrhus_epirus", "King Pyrrhus of Epirus (319–272 BCE)", 18, "319–272 BCE"),
    ], "greek", "8th–3rd c. BCE", ["Plutarch's Lives", "Thucydides", "Herodotus"])

    # Central & Northern European Houses (Mod. Univ. Hist. Vols. 11-12)
    add_chain(nodes, edges, None, [
        ("eur_poland_mieszko", "Piast Dynasty of Poland: Piast → Mieszko I (966 CE) → Boleslaw I the Brave (1025)", 19, "9th–11th c. CE", "Founders of Poland", "Mod. Univ. Hist. Vol. 12.", True),
        ("unb_eur_casimir3_poland", "King Casimir III the Great of Poland (1333–1370)", 20, "1333–1370 CE"),
        ("unb_eur_jadwiga_jagiello", "Queen Jadwiga & Wladyslaw II Jagiello (Polish-Lithuanian Union, 1386)", 20, "1386–1434 CE"),
        ("unb_eur_sigismund_poland", "King Sigismund I the Old (Jagiellonian Golden Age)", 21, "1506–1548 CE"),
        ("unb_eur_john_sobieski", "King John III Sobieski of Poland (Vienna, 1683)", 21, "1674–1696 CE"),
    ], "europe_norse", "10th–17th c. CE", ["Modern Universal History Vol. 12"])

    add_chain(nodes, edges, None, [
        ("unb_eur_almos_arpad", "Hungary (Arpad Dynasty): Almos → Grand Prince Arpad (895 CE) → St. Stephen I (1000 CE)", 19, "895–1038 CE", "Founders of Hungary", "Mod. Univ. Hist. & Hungarian Chronicles.", True),
        ("unb_eur_bela3_hungary", "King Bela III of Hungary (1172–1196)", 20, "1172–1196 CE"),
        ("unb_eur_louis_great_hungary", "King Louis I the Great of Hungary & Poland", 20, "1342–1382 CE"),
        ("unb_eur_hunyadi_corvinus", "John Hunyadi → King Matthias Corvinus of Hungary (1458–1490)", 20, "1446–1490 CE"),
    ], "europe_norse", "9th–15th c. CE", ["European Royal Chronicles"])

    add_chain(nodes, edges, None, [
        ("unb_eur_premysl_bohemia", "Bohemia (Czechia): Premysl & Princess Libuse → St. Wenceslas I (d. 935)", 19, "c. 8th–10th c. CE", "Premyslid Founders", "Cosmas Chronicle.", True),
        ("unb_eur_ottokar2_bohemia", "King Ottokar II of Bohemia ('Iron and Golden King')", 20, "1253–1278 CE"),
        ("unb_eur_charles4_bohemia", "Emperor & King Charles IV of Bohemia (Golden Bull, 1356)", 20, "1346–1378 CE"),
    ], "europe_norse", "8th–14th c. CE", ["Chronicle of the Bohemians"])

    add_chain(nodes, edges, None, [
        ("unb_eur_eric_sweden", "Sweden: Eric the Victorious → Olof Skotkonung → Birger Jarl", 19, "970–1266 CE", "Early Swedish Monarchs", "Mod. Univ. Hist. Vol. 12.", True),
        ("unb_eur_gustav_vasa", "King Gustav I Vasa (Founder of Modern Sweden, 1523)", 21, "1523–1560 CE"),
        ("unb_eur_gustavus_adolphus", "King Gustavus Adolphus & Queen Christina of Sweden", 21, "1611–1654 CE"),
        ("unb_eur_charles12_sweden", "King Charles XII of Sweden (1697–1718)", 21, "1697–1718 CE"),
    ], "europe_norse", "10th–18th c. CE", ["Modern Universal History Vol. 12"])

    add_chain(nodes, edges, None, [
        ("unb_eur_gorm_bluetooth", "Denmark: Gorm the Old → Harald Bluetooth → Sweyn Forkbeard", 19, "c. 936–1014 CE", "Jelling Dynasty", "Mod. Univ. Hist. Vol. 12.", True),
        ("unb_eur_valdemar1_denmark", "King Valdemar I the Great of Denmark (1157–1182)", 20, "1157–1182 CE"),
        ("unb_eur_margaret_kalmar", "Queen Margaret I of Denmark (Kalmar Union, 1397)", 20, "1387–1412 CE"),
        ("unb_eur_christian4_denmark", "King Christian IV of Denmark & Norway (1588–1648)", 21, "1588–1648 CE"),
    ], "europe_norse", "10th–17th c. CE", ["Modern Universal History Vol. 12"])

    add_chain(nodes, edges, "eur_poland_mieszko", [
        ("unb_eur_mindaugas_lithuania", "King Mindaugas of Lithuania (Crowned 1253)", 20, "1236–1263 CE"),
        ("unb_eur_gediminas", "Grand Duke Gediminas of Lithuania (1316–1341)", 20, "1316–1341 CE"),
        ("unb_eur_algirdas_vytautas", "Algirdas & Grand Duke Vytautas the Great (1392–1430)", 20, "1345–1430 CE"),
    ], "europe_norse", "13th–15th c. CE", ["Lithuanian Chronicles", "Mod. Univ. Hist. Vol. 12"])

    return {
        "module": "36_unbridged_world_kingdoms",
        "title": "World Kingdoms, Dynasties & Classical Thinkers Awaiting Primary-Source Biblical Bridge (Pending Bridge)",
        "nodes": nodes,
        "edges": edges,
    }
