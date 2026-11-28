"""
Module 52: Wave 10 — Islamic Golden Age (Fatimids, Ayyubids, Mamluks, Al-Andalus & Polymaths),
West & East Africa (Ghana, Mali, Songhai, Hausa/Sokoto & Swahili Kilwa/Zanzibar),
Central Asia/Steppe (Samanids, Khwarazm, Ilkhanate, Timurids, Golden Horde, Crimea & Kazakhs),
Biblical-Era Ancient Near East (Aram-Damascus/Tel Dan, Moab/Mesha, Urartu, Phrygia/Lydia),
& Complete All 10 Living 2026 European Monarchies + Americas Royal Gateways.
"""

from . import N, E


def add_chain(nodes, edges, parent_id, items, tradition, era_default, sources, default_type="direct"):
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
    # SECTION A: FATIMIDS, AYYUBIDS, MAMLUKS, AL-ANDALUS & POLYMATHS (28 nodes)
    # =========================================================================
    add_chain(nodes, edges, "mon_isl_ali", [
        ("isl10_al_mahdi_billah", "Caliph Abdullah al-Mahdi Billah (Founder of Fatimid Caliphate, 909–934 CE)", 19, "874–934 CE", "1st Fatimid Caliph"),
        ("isl10_al_muizz_cairo", "Caliph Al-Mu'izz li-Din Allah (Founded Cairo & Al-Azhar, 969 CE)", 20, "931–975 CE", "Fatimid Caliph of Cairo", "Conquered Egypt in 969 CE and founded Al-Qahirah (Cairo) & Al-Azhar Mosque.", True),
        ("isl10_al_aziz_hakim", "Caliphs Al-Aziz Billah & Al-Hakim bi-Amr Allah (975–1021 CE)", 20, "955–1021 CE", "Fatimid Caliphs"),
        ("isl10_al_mustansir", "Caliph Al-Mustansir Billah (60-Year Reign; Father of Nizar & Al-Musta'li, 1036–1094)", 20, "1029–1094 CE", "8th Fatimid Caliph"),
    ], "arabian", "10th–11th c. CE", ["Ibn al-Athir", "Al-Maqrizi", "Lane-Poole"])
    nodes += [
        N("isl10_nizar_ismaili", "Imam Nizar ibn al-Mustansir (Progenitor of Nizari Ismaili Imamat / Aga Khans, 1045–1095)", "arabian", 20, "1045–1095 CE", "Fatimid-Nizari Imam", ["Alamut & Aga Khan Chronicles"], "Eldest son of Caliph al-Mustansir; Alamut Nizari Imamat line continuing to Living Aga Khan V (2026)."),
        N("isl10_al_mustali_tayyibi", "Caliph Al-Musta'li → Al-Adid (Final Fatimid Caliph, d. 1171 CE)", "arabian", 20, "1074–1171 CE", "Late Fatimid Caliphs", ["Ibn al-Athir", "Al-Maqrizi"], "Younger son Fatimid succession to Al-Adid (d. 1171 CE)."),
    ]
    edges += [
        E("isl10_al_mustansir", "isl10_nizar_ismaili", "direct", "Eldest son of Fatimid Caliph al-Mustansir"),
        E("isl10_nizar_ismaili", "mod_agakhan5_ismaili", "direct", "Alamut -> Persian -> Living 2026 Imamat of Aga Khan V"),
        E("isl10_al_mustansir", "isl10_al_mustali_tayyibi", "direct", "Younger son Fatimid succession to 1171 CE"),
    ]

    nodes.append(N("isl10_najm_ad_din_ayyub", "Najm ad-Din Ayyub & Asad ad-Din Shirkuh (Patriarchs of the Ayyubid Dynasty, d. 1173 CE)", "arabian", 20, "d. 1173 CE", "Ayyubid Founders", ["Ibn Shaddad", "Modern Universal History Vol. 2"], "Kurdish generals from Dvin (Armenia) who united Syria & Egypt; father & uncle of Saladin."))
    edges.append(E("isl10_najm_ad_din_ayyub", "mon_isl_saladin", "direct", "Father of Sultan Saladin"))
    add_chain(nodes, edges, "mon_isl_saladin", [
        ("isl10_al_adil1", "Sultan Al-Adil I (Saphadin; Brother of Saladin, Negotiated with Richard I, 1200–1218)", 20, "1145–1218 CE", "Ayyubid Sultan"),
        ("isl10_al_kamil", "Sultan Al-Kamil of Egypt (1229 Treaty of Jaffa with Emperor Frederick II, 1218–1238)", 20, "1177–1238 CE", "Ayyubid Sultan"),
        ("isl10_shajar_al_durr", "Sultana Shajar al-Durr of Egypt (1250 CE; Transition to Mamluk Sultanate)", 20, "d. 1257 CE", "Sovereign Sultana of Egypt", "Widow of al-Salih Ayyub who defeated Louis IX's crusade and wed Mamluk Sultan Aybak.", True),
        ("isl10_qalawun", "Mamluk Sultan Al-Mansur Qalawun (Qalawunid Dynasty Founder, 1279–1290 CE)", 20, "c. 1222–1290 CE", "Bahri Mamluk Sultan"),
        ("isl10_al_nasir_muhammad", "Sultan Al-Nasir Muhammad ibn Qalawun (Architectural Peak of Mamluk Cairo, d. 1341)", 20, "1285–1341 CE", "Bahri Mamluk Sultan"),
        ("isl10_qansuh_al_ghuri", "Mamluk Sultan Al-Ashraf Qansuh al-Ghuri (Fell at Marj Dabiq 1516 vs Selim I)", 21, "c. 1441–1516 CE", "Penultimate Burji Mamluk Sultan"),
    ], "arabian", "12th–16th c. CE", ["Al-Maqrizi", "Modern Universal History Vol. 2–3"])
    edges += [
        E("isl10_al_adil1", "mon_eng_richard1", "expansion", "1192 Treaty of Jaffa diplomatic exchanges between Al-Adil & Richard I"),
        E("isl10_al_kamil", "mon_hre_frederick2", "expansion", "1229 Treaty of Jaffa between Sultan al-Kamil & Emperor Frederick II"),
        E("isl10_shajar_al_durr", "mon_isl_baybars", "expansion", "Bahri Mamluk military coalition under Shajar al-Durr & Baybars"),
        E("isl10_qansuh_al_ghuri", "mon_ott_selim1", "expansion", "1516 Battle of Marj Dabiq: Ottoman Selim I annexed Mamluk Levant & Egypt"),
    ]

    add_chain(nodes, edges, "mon_esp_alfonso6", [
        ("isl10_yusuf_ibn_tashfin", "Emir Yusuf ibn Tashfin (Almoravid Founder of Marrakesh; Battle of Sagrajas 1086)", 20, "c. 1009–1106 CE", "Almoravid Sovereign"),
        ("isl10_ibn_tumart_abd_al_mumin", "Ibn Tumart & Caliph Abd al-Mu'min (Almohad Caliphate Founders, 1121–1163 CE)", 20, "1094–1163 CE", "Almohad Founders"),
        ("isl10_yaqub_al_mansur", "Caliph Abu Yusuf Yaqub al-Mansur (Patron of Ibn Rushd; Koutoubia & Giralda, 1184–1199)", 20, "c. 1160–1199 CE", "Almohad Caliph"),
        ("isl10_muhammad1_nasrid", "Sultan Muhammad I ibn al-Ahmar (Founder of Nasrid Emirate of Granada & Alhambra, 1238)", 20, "1195–1273 CE", "Founder of Nasrid Granada"),
        ("isl10_yusuf1_muhammad5_alhambra", "Sultans Yusuf I & Muhammad V of Granada (Alhambra Palaces, 1333–1391 CE)", 20, "1318–1391 CE", "Granadan Alhambra Builders"),
        ("isl10_boabdil_granada", "Sultan Muhammad XII / Boabdil of Granada (1482–1492 CE)", 21, "c. 1460–c. 1533 CE", "Last Emir of Granada", "Surrendered Granada to Ferdinand & Isabella in January 1492 CE.", True),
    ], "arabian", "11th–15th c. CE", ["Mariana General History of Spain 1699", "Ibn Khaldun"], default_type="expansion")
    edges.append(E("isl10_boabdil_granada", "mon_esp_isabella_ferdinand", "expansion", "1492 Capitulation of Granada to Ferdinand & Isabella"))

    nodes += [
        N("isl10_al_khwarizmi", "Muhammad ibn Musa al-Khwarizmi (Father of Algebra & Algorithms, House of Wisdom, c. 780–850)", "arabian", 19, "c. 780–850 CE", "Mathematician & Astronomer", ["Al-Tabari", "House of Wisdom"], "Coined Algebra (Al-Jabr) & Algorithm at Caliph Al-Ma'mun's House of Wisdom in Baghdad.", True),
        N("isl10_al_kindi_farabi", "Al-Kindi (Baghdad) & Al-Farabi ('The Second Teacher' After Aristotle, c. 801–950 CE)", "arabian", 19, "801–950 CE", "Philosophers & Polymaths", ["Ibn Abi Usaybi'a"], "Translated and synthesized Greek philosophy across the Abbasid world."),
        N("isl10_al_biruni_polymath", "Abu Rayhan al-Biruni (Geodesist, Astronomer & Author of Chronology of Ancient Nations, 973–1048)", "iranian", 20, "973–1048 CE", "Khwarazmian Polymath & Historian", ["Al-Biruni Chronology", "Sachau"], "Measured Earth's radius and compiled synchronous world royal genealogies at Ghazni."),
        N("isl10_omar_khayyam", "Omar Khayyam (Astronomer, Mathematician & Poet of Nishapur, 1048–1131 CE)", "iranian", 20, "1048–1131 CE", "Seljuk Astronomer & Poet", ["Modern Universal History Vol. 3"], "Reformed the Persian Jalali solar calendar under Sultan Malik-Shah I."),
        N("isl10_nizam_al_mulk", "Nizam al-Mulk (Seljuk Grand Vizier & Founder of Nizamiyya Universities, 1018–1092 CE)", "iranian", 20, "1018–1092 CE", "Seljuk Grand Vizier", ["Siyasatnama", "Modern Universal History Vol. 3"], "Statesman serving Alp Arslan & Malik-Shah I; patron of Al-Ghazali & Omar Khayyam."),
        N("isl10_ibn_rushd_averroes", "Ibn Rushd / Averroes (Philosopher & Qadi of Cordoba & Marrakesh, 1126–1198 CE)", "arabian", 20, "1126–1198 CE", "Andalusi Philosopher & Jurist", ["Ibn Khaldun"], "Chief judge of Seville & Cordoba; famed commentator on Aristotle under Almohad Caliphs."),
        N("isl10_al_idrisi", "Muhammad al-Idrisi (Andalusi Geographer; Tabula Rogeriana for Roger II, 1100–1165 CE)", "arabian", 20, "1100–1165 CE", "Cartographer & Geographer", ["Nuzhat al-Mushtaq"], "Created the world atlas Tabula Rogeriana at King Roger II's court in Sicily."),
        N("isl10_ibn_battuta", "Ibn Battuta of Tangier (75,000-Mile World Traveler to Granada, Mali, Constantinople & China, 1304–1369)", "arabian", 20, "1304–1369 CE", "Global Explorer & Jurist", ["Rihla of Ibn Battuta"], "Recorded firsthand eyewitness accounts of Granada, Mansa Sulayman of Mali, Kilwa, Byzantium, Delhi & Yuan China.", True),
        N("isl10_ibn_khaldun", "Ibn Khaldun of Tunis (Founder of Historiography & Sociology; Met Tamerlane 1401, 1332–1406 CE)", "arabian", 20, "1332–1406 CE", "Philosopher of History & Statesman", ["Muqaddimah", "Histoire des Berbères"], "Authored the Muqaddimah & Berber/Arab universal histories; negotiated with Timur at Damascus.", True),
    ]
    edges += [
        E("mon_isl_al_mamun", "isl10_al_khwarizmi", "expansion", "Patronage of Al-Khwarizmi at the House of Wisdom in Baghdad"),
        E("mon_isl_al_mamun", "isl10_al_kindi_farabi", "expansion", "Abbasid patronage of Al-Kindi & Al-Farabi"),
        E("mon_isl_mahmud_ghazni", "isl10_al_biruni_polymath", "expansion", "Ghaznavid court astronomer & India chronicler"),
        E("stp5_malik_shah1", "isl10_omar_khayyam", "expansion", "1079 CE Jalali solar calendar patronage under Malik-Shah I"),
        E("stp5_malik_shah1", "isl10_nizam_al_mulk", "expansion", "Seljuk Grand Vizier of Malik-Shah I"),
        E("isl10_yaqub_al_mansur", "isl10_ibn_rushd_averroes", "expansion", "Almohad royal physician & philosopher at Marrakesh & Cordoba"),
        E("eur9_roger2_sicily", "isl10_al_idrisi", "expansion", "1154 CE Royal Cartography Commission: King Roger II & Al-Idrisi"),
        E("isl10_yusuf1_muhammad5_alhambra", "isl10_ibn_battuta", "expansion", "1350 CE Visit of Ibn Battuta to Nasrid Granada"),
        E("ber4_berr", "isl10_ibn_khaldun", "expansion", "Principal historian of Amazigh / Berber genealogies in Kitab al-Ibar"),
        E("mngr_imp_12_timur_tamerlane_barlas_clan_", "isl10_ibn_khaldun", "expansion", "1401 CE Damascus diplomatic meeting between Ibn Khaldun and Timur"),
    ]

    # =========================================================================
    # SECTION B: WEST & EAST AFRICA INDIVIDUAL SOVEREIGNS & SCHOLARS (16 nodes)
    # =========================================================================
    add_chain(nodes, edges, "af_sundiata", [
        ("afr10_kaya_maghan_tunka", "Kaya Maghan Cissé & Tunka Menin of Wagadu / Ghana Empire (8th–11th c. CE)", 19, "8th–11th c. CE", "Kings of Ghana Empire"),
        ("afr10_sundiata_keita", "Mansa Sundiata Keita ('Lion King' Founder of Mali Empire; Kouroukan Fouga 1235 CE)", 20, "c. 1217–1255 CE", "Founder of Mali Empire"),
        ("afr10_mansa_abu_bakr2", "Mansa Abu Bakr II (Atlantic Navigator Emperor of Mali, c. 1311 CE)", 20, "r. c. 1311 CE", "Mansa of Mali"),
    ], "african", "8th–14th c. CE", ["Oral Epic of Sundiata", "Ibn Khaldun", "Al-Umari"])
    edges += [
        E("afr10_mansa_abu_bakr2", "mon_afr_mansa_musa", "direct", "Predecessor/brother transition to Mansa Musa I (1312 CE)"),
        E("mon_afr_mansa_musa", "afr10_mansa_sulayman", "direct", "Brother & successor Mansa Sulayman of Mali (1341–1360 CE)"),
    ]
    nodes.append(N("afr10_mansa_sulayman", "Mansa Sulayman of Mali (Brother of Mansa Musa; Visited by Ibn Battuta 1352 CE)", "african", 20, "r. 1341–1360 CE", "Mansa of Mali", ["Ibn Battuta Rihla", "Ibn Khaldun"], "Presided over prosperous Mali; hosted Ibn Battuta."))
    edges.append(E("isl10_ibn_battuta", "afr10_mansa_sulayman", "expansion", "1352–1353 CE Journey of Ibn Battuta to Mansa Sulayman's Court"))

    add_chain(nodes, edges, "sng_sonni_askia_timbuktu", [
        ("afr10_sonni_ali_ber", "Emperor Sonni Ali Ber (Conquered Timbuktu & Djenné, 1464–1492 CE)", 20, "r. 1464–1492 CE", "Emperor of Songhai"),
        ("afr10_askia_dawud", "Emperor Askia Dawud (Songhai Golden Age Scholar-Patron, 1549–1582 CE)", 21, "r. 1549–1582 CE", "Askia of Songhai"),
        ("afr10_ahmad_baba_timbuktu", "Ahmad Baba al-Timbukti (Chancellor of Sankore University, Timbuktu, 1556–1627 CE)", 21, "1556–1627 CE", "Great Scholar of Timbuktu", ["Tarikh al-Sudan"], "Descendant of Timbuktu's Aqit scholarly lineage; authored over 40 works."),
    ], "african", "15th–17th c. CE", ["Tarikh es-Soudan", "Modern Universal History Vol. 7"])
    edges.append(E("afr10_sonni_ali_ber", "mon_afr_askia_mohammed", "direct", "Songhai royal succession (1493 CE)"))

    add_chain(nodes, edges, "unb_afr_kanem_dugu", [
        ("afr10_bayajidda_daurama", "Queen Magajiya Daurama & Bayajidda (Founders of the Seven Hausa Bakwai States)", 19, "9th–11th c. CE", "Hausa State Founders"),
        ("afr10_queen_amina_zazzau", "Queen Amina / Aminatu of Zazzau (16th c. Hausa Warrior Queen, Kano Chronicle)", 21, "c. 1533–1610 CE", "Queen of Zazzau (Zaria)", "Extended Zazzau dominion from Nupe to Kwararafa and built the legendary Ganuwar Amina walls.", True),
        ("afr10_usman_dan_fodio", "Shehu Usman dan Fodio (Founder of Sokoto Caliphate, 1754–1817 CE)", 21, "1754–1817 CE", "1st Caliph of Sokoto", "Fulani-Torodbe scholar who founded the Sokoto Caliphate in 1804 CE.", True),
        ("afr10_muhammad_bello_nana_asmau", "Sultan Muhammad Bello & Poet-Scholar Nana Asma'u of Sokoto (1781–1864 CE)", 21, "1781–1864 CE", "2nd Sultan of Sokoto & Scholar-Princess"),
    ], "african", "11th–19th c. CE", ["Kano Chronicle", "Sokoto Caliphate Archives"], default_type="expansion")

    nodes += [
        N("afr10_empress_eleni", "Empress Eleni of Ethiopia (+ Zara Yaqob; Sent 1509 Portuguese Diplomatic Embassy)", "african", 21, "d. 1522 CE", "Queen Regent of Ethiopia", ["Ethiopian Royal Chronicles", "Portuguese Asia"], "Consort of Zara Yaqob; initiator of the 1509–1520 Ethiopian–Portuguese alliance."),
        N("afr10_emperor_fasilides", "Emperor Fasilides of Ethiopia (Founded Gondar & Fasil Ghebbi Castles, 1632–1667 CE)", "african", 21, "1603–1667 CE", "Gondarine Solomonic Emperor", ["Ludolf New History of Ethiopia"], "Built the walled imperial city of Gondar in 1636 CE."),
        N("afr10_tewodros2_taytu", "Emperor Tewodros II & Empress Taytu Betul (+ Menelik II, Co-Victor of Adwa 1896)", "african", 21, "1818–1918 CE", "Modernizing Ethiopian Sovereigns", ["Ethiopian Imperial Chronicles"], "Tewodros II initiated modern Ethiopian unification; Empress Taytu co-led the 1896 victory at Adwa."),
        N("afr10_kilwa_ali_shirazi", "Sultan Ali ibn al-Hassan Shirazi (Founder of Kilwa Sultanate, Swahili Coast, c. 957 CE)", "african", 19, "10th c. CE", "Shirazi Founder of Kilwa Kisiwani", ["Kilwa Chronicle", "Ibn Battuta"], "Shirazi Persian prince who settled East Africa and founded the trading sultanate of Kilwa."),
        N("afr10_seyyid_said_zanzibar", "Sultan Sayyid Said bin Sultan of Oman & Zanzibar (1806–1856 CE)", "african", 21, "1791–1856 CE", "Sultan of Muscat, Oman & Zanzibar", ["East African Chronicles"], "Moved the Al Bu Said imperial capital to Stone Town, Zanzibar (1840)."),
    ]
    edges += [
        E("modr_eth_04_emperor_zara_yaqob_1434_1468", "afr10_empress_eleni", "direct", "Royal Consort of Emperor Zara Yaqob & Regent"),
        E("afr10_empress_eleni", "mon_por_manuel1", "expansion", "1509–1520 CE Ethiopian-Portuguese Alliance (Mateus Embassy to Lisbon)"),
        E("modr_eth_04_emperor_zara_yaqob_1434_1468", "afr10_emperor_fasilides", "direct", "Solomonic Gondarine descent from Zara Yaqob"),
        E("modr_eth_12_emperor_menelik_ii_victor_of", "afr10_tewodros2_taytu", "direct", "Imperial Consort Empress Taytu & predecessor Tewodros II"),
        E("bir_sasanians_complete", "afr10_kilwa_ali_shirazi", "expansion", "Shirazi-Persian maritime foundation of Swahili Kilwa Chronicle (957 CE)"),
        E("isl10_ibn_battuta", "afr10_kilwa_ali_shirazi", "expansion", "1331 CE Eyewitness account of Kilwa by Ibn Battuta"),
        E("afr10_kilwa_ali_shirazi", "afr10_seyyid_said_zanzibar", "expansion", "Swahili-Omani Indian Ocean sovereignty continuing at Zanzibar"),
    ]

    # =========================================================================
    # SECTION C: CENTRAL ASIA, ILKHANATE, GOLDEN HORDE, CRIMEA & TIMURIDS (20 nodes)
    # =========================================================================
    add_chain(nodes, edges, "fam6_ibn_sina", [
        ("per10_ismail_samani", "Emir Ismail Samani (Founder of Samanid Renaissance of Bukhara, 892–907 CE)", 19, "849–907 CE", "Samanid Emir"),
        ("per10_adud_al_dawla", "Emir Adud al-Dawla (Buyid King of Kings of Shiraz & Baghdad, 949–983 CE)", 19, "936–983 CE", "Buyid Amir al-Umara"),
    ], "iranian", "9th–10th c. CE", ["Al-Tabari", "Al-Biruni"], default_type="expansion")
    edges.append(E("per10_ismail_samani", "mon_isl_mahmud_ghazni", "expansion", "Samanid -> Ghaznavid Central Asian succession"))
    nodes += [
        N("per10_sultan_sanjar", "Sultan Ahmad Sanjar (Final Great Seljuk Sultan of Merv, 1118–1157 CE)", "iranian", 20, "1085–1157 CE", "Great Seljuk Sultan", ["Modern Universal History Vol. 3"], "Son of Malik-Shah I."),
        N("per10_ala_addin_khwarazm", "Shah Ala ad-Din Muhammad II of Khwarazm (1200–1220 CE)", "iranian", 20, "1169–1220 CE", "Khwarazmshah", ["Juvayni History of the World Conqueror"], "Ruled Transoxiana & Persia prior to Genghis Khan's 1219 campaign."),
        N("per10_jalal_addin_mangburni", "Sultan Jalal ad-Din Mangburni (Last Khwarazmshah, Battle of the Indus 1221 CE)", "iranian", 20, "1199–1231 CE", "Last Khwarazmshah", ["Juvayni", "Secret History of the Mongols"], "Fought Genghis Khan at the Indus River (1221 CE)."),
    ]
    edges += [
        E("stp5_malik_shah1", "per10_sultan_sanjar", "direct", "Son of Great Seljuk Sultan Malik-Shah I"),
        E("per10_sultan_sanjar", "per10_ala_addin_khwarazm", "expansion", "Seljuk Khorasan succession to Khwarazmshahs"),
        E("per10_ala_addin_khwarazm", "per10_jalal_addin_mangburni", "direct", "Son of Khwarazmshah Muhammad II"),
        E("per10_jalal_addin_mangburni", "mng_genghis_khan_borte", "expansion", "1221 CE Battle of the Indus against Genghis Khan"),
    ]

    add_chain(nodes, edges, "abg_tolui_hulagu_ilkhan", [
        ("per10_hulagu_khan", "Ilkhan Hulagu Khan (Grandson of Genghis; Founded Ilkhanate of Persia 1256 CE)", 20, "1217–1265 CE", "1st Ilkhan of Persia"),
        ("per10_abaqa_arghun", "Ilkhans Abaqa Khan & Arghun Khan (Envoys Rabban Bar Sauma & Edward I, 1265–1291)", 20, "1234–1291 CE", "Ilkhans of Persia"),
        ("per10_ghazan_oljaitu", "Ilkhans Ghazan & Öljaitü (+ Vizier Rashid al-Din Jami' al-Tawarikh, 1295–1316 CE)", 20, "1271–1316 CE", "Ilkhans & Patron of World History"),
    ], "iranian", "13th–14th c. CE", ["Rashid al-Din Jami' al-Tawarikh", "Modern Universal History Vol. 4"])
    add_chain(nodes, edges, "mngr_imp_12_timur_tamerlane_barlas_clan_", [
        ("per10_shah_rukh_gawhar_shad", "Shah Rukh & Queen Gawhar Shad (Timurid Herat Renaissance, 1405–1447 CE)", 20, "1377–1457 CE", "Timurid Emperor & Queen"),
        ("per10_ulugh_beg", "Sultan Ulugh Beg (Samarkand Observatory & Zij-i-Sultani, 1394–1449 CE)", 21, "1394–1449 CE", "Timurid Astronomer-King", "Computed the length of the sidereal year within 58 seconds at his Samarkand observatory.", True),
        ("per10_husayn_bayqara", "Sultan Husayn Bayqara & Poet Ali-Shir Nava'i (1469–1506 CE Herat Court)", 21, "1438–1506 CE", "Timurid Patron of Herat"),
    ], "iranian", "15th–16th c. CE", ["Baburnama", "Tarikh-i-Rashidi"])
    nodes.append(N("per10_pahlavi_iran", "Reza Shah Pahlavi → Mohammad Reza Shah Pahlavi of Iran (1925–1979 CE)", "iranian", 21, "1878–1980 CE", "20th c. Pahlavi Shahs", ["Modern Iranian History"], "20th-century imperial dynasty succeeding Qajar Iran."))
    edges.append(E("mon_ir_agha_mohammad", "per10_pahlavi_iran", "expansion", "1925 Transition from Qajar Persia to Pahlavi Iran"))

    add_chain(nodes, edges, "mngr_imp_02_batu_khan_founder_of_golden_", [
        ("per10_berke_khan", "Khan Berke of the Golden Horde (Allied with Mamluk Baybars, 1257–1266 CE)", 20, "d. 1266 CE", "Khan of the Golden Horde"),
        ("per10_ozbeg_khan", "Khan Öz Beg of the Golden Horde (Longest Reign; Golden Age of Sarai, 1313–1341 CE)", 20, "1282–1341 CE", "Khan of the Golden Horde"),
        ("per10_tokhtamysh", "Khan Tokhtamysh (Rival of Timur; Restorer of Golden Horde, 1380–1395 CE)", 20, "d. 1406 CE", "Khan of the Golden Horde"),
        ("per10_haci_menli_giray", "Khans Hacı I & Meñli I Giray of Crimea (+ Ayşe Hafsa Sultan, Mother of Suleiman I)", 21, "1397–1515 CE", "Crimean Giray Khans"),
    ], "steppe", "13th–16th c. CE", ["Abulghazi", "Modern Universal History Vol. 4"])
    edges += [
        E("per10_berke_khan", "mon_isl_baybars", "expansion", "1263 CE Golden Horde–Mamluk Alliance between Berke Khan & Baybars"),
        E("per10_haci_menli_giray", "mon_ott_suleiman1", "direct", "Maternal grandfather Meñli I Giray via Ayşe Hafsa Valide Sultan"),
    ]
    nodes += [
        N("per10_shaybani_khan", "Muhammad Shaybani Khan (Founder of Uzbek Shaybanid Dynasty of Bukhara, 1451–1510)", "steppe", 21, "1451–1510 CE", "Jochid Uzbek Khan", ["Baburnama", "Abulghazi"], "Jochid descendant of Batu/Shiban; rival of Babur."),
        N("per10_kerey_janibek", "Khans Kerey & Janibek (Founders of the Kazakh Khanate, 1465 CE)", "steppe", 21, "15th c. CE", "Founders of Kazakh Khanate", ["Tarikh-i-Rashidi", "Abulghazi"], "Jochid/Orda-Iden princes who established the Kazakh Khanate."),
        N("per10_ablai_khan", "Khan Ablai of the Kazakhs (1711–1781 CE)", "steppe", 21, "1711–1781 CE", "Great Khan of all Three Kazakh Jüz", ["Kazakh & Steppe Chronicles"], "United the Senior, Middle & Junior Kazakh Jüz."),
        N("per10_kuchum_siberia", "Khan Kuchum of Siberia (Final Chinggisid Khan of the Khanate of Sibir, d. c. 1601 CE)", "steppe", 21, "d. c. 1601 CE", "Shibanid Khan of Sibir", ["Abulghazi", "Russian Chronicles"], "Last Shaybanid-Chinggisid sovereign of Western Siberia."),
    ]
    edges += [
        E("per10_tokhtamysh", "per10_shaybani_khan", "direct", "Jochid-Shibanid Steppe lineage"),
        E("per10_shaybani_khan", "mug_akbar_aurangzeb", "expansion", "1500–1510 Central Asian rivalry between Shaybani Khan & Babur"),
        E("per10_tokhtamysh", "per10_kerey_janibek", "direct", "White Horde / Jochid lineage to Kerey & Janibek"),
        E("per10_kerey_janibek", "per10_ablai_khan", "direct", "Kazakh Chinggisid Khanate succession"),
        E("per10_shaybani_khan", "per10_kuchum_siberia", "direct", "Shibanid cousin line to Sibir"),
    ]

    # =========================================================================
    # SECTION D: BIBLICAL ANE (ARAM-DAMASCUS, MOAB, AMMON, URARTU, PHRYGIA/LYDIA) (20 nodes)
    # =========================================================================
    add_chain(nodes, edges, "bib_aram", [
        ("ane10_rezon_damascus", "King Rezon of Damascus (1 Kings 11:23–25; Solomon's Adversary)", 14, "c. 960–930 BCE", "1st King of Aram-Damascus"),
        ("ane10_ben_hadad1", "King Ben-Hadad I of Aram-Damascus (1 Kings 15:18)", 15, "r. c. 885–865 BCE", "King of Aram-Damascus"),
        ("ane10_ben_hadad2_qarqar", "King Ben-Hadad II / Hadadezer (Battle of Qarqar 853 BCE vs Shalmaneser III; 1 Kgs 20)", 15, "r. c. 865–842 BCE", "King of Aram-Damascus"),
        ("ane10_hazael_tel_dan", "King Hazael of Aram-Damascus (Tel Dan Stele 'House of David', 2 Kgs 8:15, c. 842–796 BCE)", 15, "r. c. 842–796 BCE", "King of Aram-Damascus", "Erected the Tel Dan Stele bearing the oldest extra-biblical reference to 'BYTDWD' (House of David).", True),
        ("ane10_ben_hadad3", "King Ben-Hadad III (Son of Hazael, 2 Kgs 13:3)", 16, "r. c. 796–770 BCE", "King of Aram-Damascus"),
        ("ane10_rezin_damascus", "King Rezin of Damascus (Syro-Ephraimite War, Isa 7:1, 2 Kgs 16:9)", 16, "d. 732 BCE", "Last King of Aram-Damascus"),
    ], "biblical", "10th–8th c. BCE", ["1–2 Kings", "Tel Dan Stele", "Assyrian Royal Inscriptions"], default_type="expansion")
    edges += [
        E("ane10_ben_hadad2_qarqar", "akl_102_shalmaneser3", "expansion", "853 BCE Battle of Qarqar coalition (Kurkh Monolith)"),
        E("ane10_hazael_tel_dan", "jud_david", "expansion", "Tel Dan Stele Inscription (9th c. BCE) attesting 'House of David' (Bēt Dāwīd)"),
        E("for_hiram_syria_moab", "ane10_hazael_tel_dan", "cognate", "Same Syro-Aramaean sovereign"),
    ]

    nodes += [
        N("ane10_mesha_moab", "King Mesha of Moab (Mesha Stele / Moabite Stone, 2 Kgs 3:4, c. 840 BCE)", "biblical", 15, "c. 840 BCE", "King of Moab (Mesha Stele)", ["2 Kings 3:4", "Mesha Stele (KAI 181)"], "Carved the Moabite Stone recording Omri, Chemosh & House of David.", True),
        N("ane10_nahash_hanun_ammon", "Kings Nahash & Hanun of Ammon (1 Sam 11, 2 Sam 10)", "biblical", 14, "c. 1020–990 BCE", "Kings of Ammon", ["1 Samuel 11", "2 Samuel 10"], "Ammonite kings descended from Ben-Ammi son of Lot."),
        N("ane10_baalis_ammon", "King Baalis of Ammon (Jeremiah 40:14, 6th c. BCE Seal Verified)", "biblical", 17, "fl. 586 BCE", "King of Ammon", ["Jeremiah 40:14", "Tell el-'Umeiri Seal"], "Attested archaeologically on Ammonite royal official Milkom'ur seal."),
        N("ane10_achish_gath", "King Achish of Gath & Kings of Ashdod/Gaza (1 Sam 21, 27, 29)", "biblical", 14, "c. 1010 BCE", "Philistine Seren of Gath", ["1 Samuel 21 & 27"], "Sheltered young David at Ziklag."),
        N("ane10_ikausu_ekron", "King Ikausu / Achish of Ekron (Ekron Royal Dedicatory Inscription, 7th c. BCE)", "biblical", 16, "7th c. BCE", "King of Ekron (Philistia)", ["Ekron Royal Inscription", "Assyrian Annals"], "Named in Esarhaddon/Ashurbanipal prism & Ekron foundation inscription."),
    ]
    edges += [
        E("bib_lot", "ane10_mesha_moab", "expansion", "Gen 19:37: Moab son of Lot -> King Mesha of Moab"),
        E("for_hiram_syria_moab", "ane10_mesha_moab", "cognate", "Same Mesha Stele sovereign"),
        E("bib_lot", "ane10_nahash_hanun_ammon", "expansion", "Gen 19:38: Ben-Ammi son of Lot -> Kings of Ammon"),
        E("ane10_nahash_hanun_ammon", "ane10_baalis_ammon", "expansion", "Ammonite royal succession to King Baalis"),
        E("jud_david", "ane10_achish_gath", "expansion", "1 Sam 27: Alliance of David & King Achish of Gath"),
        E("ane10_achish_gath", "ane10_ikausu_ekron", "expansion", "Philistine Pentapolis dynastic continuity to Ekron"),
    ]

    add_chain(nodes, edges, "arm_hayk_pat", [
        ("ane10_aramu_sarduri1", "Kings Aramu & Sarduri I of Urartu (Founders of Tushpa / Lake Van, c. 858–824 BCE)", 15, "858–824 BCE", "Founders of Kingdom of Urartu"),
        ("ane10_menua_urartu", "King Menua of Urartu (Shamiram Canal & Cuneiform Inscriptions, 810–786 BCE)", 16, "810–786 BCE", "King of Urartu"),
        ("ane10_argishti1_yerevan", "King Argishti I of Urartu (Founded Erebuni / Yerevan 782 BCE)", 16, "786–764 BCE", "Great King of Urartu / Ararat", "Built the fortress of Erebuni in 782 BCE, direct origin of Armenia's capital Yerevan.", True),
        ("ane10_sarduri2", "King Sarduri II of Urartu (Peak Extent vs Tiglath-Pileser III, 764–735 BCE)", 16, "764–735 BCE", "King of Urartu"),
        ("ane10_rusa1_rusa2", "Kings Rusa I & Rusa II (Musasir & Teishebaini vs Sargon II, 735–645 BCE)", 16, "735–645 BCE", "Late Kings of Urartu"),
    ], "iranian", "9th–7th c. BCE", ["Urartian Cuneiform Inscriptions", "Khorenatsi"], default_type="expansion")
    edges.append(E("ane10_rusa1_rusa2", "aklr_neo_11_sargon_ii_722_705_bce", "expansion", "714 BCE 8th Campaign of Sargon II against Rusa I of Urartu"))

    nodes += [
        N("ane10_gordias_midas", "Kings Gordias & Midas of Phrygia ('Mita of Mushki', d. c. 696 BCE)", "greek", 16, "8th c. BCE", "Kings of Phrygia (Gordion)", ["Herodotus", "Assyrian Annals of Sargon II"], "Historical King Midas wed a Greek princess of Cyme and corresponded with Sargon II of Assyria.", True),
        N("ane10_gyges_lydia", "King Gyges of Lydia ('Gugu' in Ashurbanipal Annals, 680–644 BCE)", "greek", 16, "r. 680–644 BCE", "Founder of Mermnad Lydia", ["Herodotus Book I", "Rassam Cylinder"], "Sent mercenaries to Egypt's Psamtik I and envoys to Nineveh."),
        N("ane10_alyattes_lydia", "King Alyattes of Lydia (Eclipse of Thales Battle 585 BCE; Father of Croesus)", "greek", 17, "r. c. 619–560 BCE", "King of Lydia", ["Herodotus Book I"], "Coined earliest electrum money; father of Croesus."),
        N("ane10_harpagus_artemisia", "Queen Artemisia I of Halicarnassus & Satrap Mausolus of Caria (Mausoleum)", "greek", 18, "5th–4th c. BCE", "Carian Sovereigns", ["Herodotus", "Diodorus"], "Naval commander at Salamis (480 BCE) and builder of the Mausoleum at Halicarnassus."),
    ]
    edges += [
        E("cls_lydia_gyges_croesus", "ane10_gordias_midas", "expansion", "Anatolian royal neighbors (Phrygia & Lydia)"),
        E("ane10_gordias_midas", "aklr_neo_11_sargon_ii_722_705_bce", "expansion", "717–709 BCE Diplomatic Correspondence of Mita of Mushki (Midas) & Sargon II"),
        E("cls_lydia_gyges_croesus", "ane10_gyges_lydia", "direct", "Founder Gyges of Mermnad Lydia"),
        E("ane10_gyges_lydia", "ane10_alyattes_lydia", "direct", "Mermnad succession to King Alyattes"),
        E("ane10_alyattes_lydia", "cls3_croesus", "direct", "Father of King Croesus of Lydia"),
        E("ir_cyrus", "ane10_harpagus_artemisia", "expansion", "Achaemenid Anatolian vassal-sovereigns of Caria"),
    ]

    # =========================================================================
    # SECTION E: ALL REMAINING LIVING 2026 EUROPEAN MONARCHIES & AMERICAS (20 nodes)
    # =========================================================================
    add_chain(nodes, edges, "eur9_william2_orange", [
        ("liv10_william1_netherlands", "King William I of the Netherlands (1st King of United Kingdom of the Netherlands, 1815–1840)", 21, "1772–1843 CE", "1st King of the Netherlands"),
        ("liv10_wilhelmina_netherlands", "Queen Wilhelmina of the Netherlands (Reigned 1890–1948 CE)", 21, "1880–1962 CE", "Queen of the Netherlands"),
        ("liv10_juliana_netherlands", "Queen Juliana of the Netherlands (Reigned 1948–1980 CE)", 21, "1909–2004 CE", "Queen of the Netherlands"),
        ("liv10_beatrix_netherlands", "Princess (former Queen) Beatrix of the Netherlands (r. 1980–2013; Living 2026)", 21, "1938–Present CE", "Queen of the Netherlands (Living 2026)"),
        ("liv10_willem_alexander_2026", "LIVING (2026): King Willem-Alexander & Princess Catharina-Amalia of the Netherlands", 21, "1967–Present CE", "Reigning King of the Netherlands & Heir (Living 2026)", "Present-day reigning Orange-Nassau monarch of the Netherlands (2026).", True),
    ], "europe_norse", "1815–2026 CE", ["Almanach de Gotha", "Koninklijk Huis"])

    add_chain(nodes, edges, "roy6_edward7", [
        ("liv10_haakon7_maud", "King Haakon VII of Norway (+ Queen Maud, Daughter of Edward VII, r. 1905–1957)", 21, "1872–1957 CE", "1st Modern King of Norway"),
        ("liv10_olav5_norway", "King Olav V of Norway (Son of Haakon VII & Maud, r. 1957–1991)", 21, "1903–1991 CE", "King of Norway"),
        ("liv10_harald5_haakon_2026", "LIVING (2026): King Harald V & Crown Prince Haakon of Norway", 21, "1937–Present CE", "Reigning King of Norway & Heir (Living 2026)", "Present-day reigning Glücksburg–Windsor–Bernadotte monarch of Norway (2026).", True),
    ], "europe_norse", "1905–2026 CE", ["Almanach de Gotha", "Kongehuset"])

    add_chain(nodes, edges, "mon_eng_victoria", [
        ("liv10_leopold1_belgium", "King Leopold I of Belgium (Uncle of Queen Victoria; Saxe-Coburg-Gotha, 1831–1865)", 21, "1790–1865 CE", "1st King of the Belgians"),
        ("liv10_albert1_belgium", "King Albert I & King Leopold III of the Belgians (1909–1951 CE)", 21, "1875–1983 CE", "Kings of the Belgians"),
        ("liv10_baudouin_albert2", "King Baudouin & King Albert II of the Belgians (1951–2013 CE)", 21, "1930–Present CE", "Kings of the Belgians"),
        ("liv10_philippe_elisabeth_2026", "LIVING (2026): King Philippe & Princess Elisabeth of Belgium", 21, "1960–Present CE", "Reigning King of the Belgians & Heir (Living 2026)", "Present-day reigning Belgian sovereign & Duchess of Brabant (2026).", True),
    ], "europe_norse", "1831–2026 CE", ["Almanach de Gotha", "Monarchie.be"], default_type="expansion")

    nodes += [
        N("liv10_luxembourg_guillaume5_2026", "LIVING (2026): Grand Duke Henri & Grand Duke Guillaume V of Luxembourg (Nassau-Weilburg)", "europe_norse", 21, "1955–Present CE", "Living 2026 Sovereigns of Luxembourg", ["Almanach de Gotha"], "Senior House of Nassau-Weilburg grand ducal line continuing in 2026."),
        N("liv10_monaco_albert2_2026", "LIVING (2026): Rainier III (+ Grace Kelly) → Prince Albert II of Monaco (Grimaldi)", "europe_norse", 21, "1923–Present CE", "Living 2026 Sovereign Prince of Monaco", ["Almanach de Gotha", "Burke's Royal Families"], "House of Grimaldi descending via Louise-Hippolyte Grimaldi & Jacques Goyon de Matignon (French nobility under Louis XIV)."),
        N("liv10_liechtenstein_2026", "LIVING (2026): Prince Hans-Adam II & Hereditary Prince Alois of Liechtenstein", "europe_norse", 21, "1945–Present CE", "Living 2026 Princes of Liechtenstein", ["Almanach de Gotha"], "Direct imperial princes elevated under Habsburg Holy Roman Emperors continuing in 2026."),
    ]
    edges += [
        E("liv10_william1_netherlands", "liv10_luxembourg_guillaume5_2026", "direct", "Nassau-Orange / Nassau-Weilburg 1815 Grand Ducal Succession"),
        E("mon_fra_louis14", "liv10_monaco_albert2_2026", "expansion", "French peerage / Matignon-Grimaldi marriage sanctioned under Louis XIV"),
        E("mon_hre_leopold1", "liv10_liechtenstein_2026", "expansion", "1699–1719 Habsburg Imperial Principality of Liechtenstein"),
    ]

    # Americas Royal & Presidential Gateways
    nodes += [
        N("liv10_john_adams_jqa", "Presidents John Adams & John Quincy Adams (New England Plantagenet-Puritan Gateway)", "europe_norse", 21, "1735–1848 CE", "2nd & 6th U.S. Presidents", ["Roberts Royal Descents of 900 Immigrants"], "U.S. Presidential father-and-son dynasty."),
        N("liv10_abraham_lincoln", "President Abraham Lincoln (16th U.S. President; New England Hingham Hanks/Lincoln Line)", "europe_norse", 21, "1809–1865 CE", "16th U.S. President", ["New England Historic Genealogical Register"], "Preserved the Union and issued the Emancipation Proclamation (1863)."),
        N("liv10_roosevelt_delano", "Presidents Theodore Roosevelt & Franklin D. Roosevelt (Delano / House of Lannoy → Charlemagne)", "europe_norse", 21, "1858–1945 CE", "26th & 32nd U.S. Presidents", ["Roberts Royal Descents"], "Connected via Philippe de Lannoy (Delano) into European nobility & Charlemagne."),
        N("liv10_simon_bolivar", "Simón Bolívar ('El Libertador'; Basque-Venezuelan Hidalgo Lineage, 1783–1830 CE)", "europe_norse", 21, "1783–1830 CE", "Liberator of Gran Colombia, Peru & Bolivia", ["Archivo Histórico de Caracas"], "Basque-Spanish colonial noble lineage from Bizkaia."),
        N("liv10_emperor_pedro_brazil", "Emperors Dom Pedro I & Dom Pedro II of Brazil (Braganza-Habsburg Imperial House, 1822–1889)", "europe_norse", 21, "1798–1891 CE", "Emperors of Brazil", ["History of Portugal & Brazil Chronicles"], "Direct Portuguese Braganza & Austrian Habsburg line (Dom Pedro I wed Archduchess Leopoldina, sister of Marie Louise).", True),
    ]
    edges += [
        E("mon_eng_edward3", "liv10_john_adams_jqa", "expansion", "New England Colonial Gateway Descent from Edward III"),
        E("liv10_john_adams_jqa", "liv10_abraham_lincoln", "expansion", "New England Hingham / Massachusetts colonial kinship bridge"),
        E("mon_fra_charlemagne", "liv10_roosevelt_delano", "expansion", "Philippe de Lannoy / Burgundian-Frankish Royal Gateway to Roosevelts"),
        E("mon_esp_philip2", "liv10_simon_bolivar", "expansion", "1589 Basque-Hidalgo Venezuelan colonial grant under Philip II"),
        E("mon_por_john5", "liv10_emperor_pedro_brazil", "direct", "House of Braganza direct royal descent to Emperors of Brazil"),
    ]

    return {
        "module": "52_wave10_islamic_africa_steppe_ane_living2026",
        "title": "Wave 10: Islamic Golden Age, Africa, Steppe, Biblical ANE & All 10 Living 2026 European Monarchies",
        "nodes": nodes,
        "edges": edges,
    }
