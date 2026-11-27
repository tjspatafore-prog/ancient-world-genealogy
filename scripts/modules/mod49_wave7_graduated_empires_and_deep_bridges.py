"""
Module 49: Wave 7 Graduated Empires, Deep Ancient Near Eastern Royal Bridges & Living 2026 Lineages.
- Graduates 92 verified historical/chronicle nodes out of 36_unbridged_world_kingdoms while
  preserving their exact original IDs (Benin, Kanem-Bornu, Vietnam, Java/Majapahit, Khmer/Siam,
  Japanese Shogunates/Meiji, Korean Goryeo/Joseon, Chinese Three Kingdoms/Sui/Song/Ming &
  Classical Greek Philosophers/Lawgivers).
- Adds person-by-person chains for the Hittite Empire, Kingdom of Mitanni, Elamite Empire,
  Nabataean Kingdom of Petra, Modern Japanese Imperial House to Living Emperor Naruhito (2026),
  and Post-Columbian Spanish-Habsburg Noble Houses of Mexico & Peru.
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
    # PART A: 92 GRADUATED NODES FROM MOD36 (EXACT ORIGINAL IDS PRESERVED)
    # =========================================================================

    # 1. Benin Empire (3 nodes) -> bridged from Eweka I (af_eweka1, son of Oranmiyan)
    add_chain(nodes, edges, "af_eweka1", [
        ("unb_afr_ewuare_benin", "Oba Ewuare the Great of Benin (1440–1473)", 21, "1440–1473 CE", "Oba of Benin", "Rebuilt Benin City walls and moats; direct royal descendant of Eweka I.", True),
        ("unb_afr_queen_idia", "Iyoba Queen Idia of Benin (Mother of Oba Esigie, c. 1504)", 21, "15th–16th c. CE", "First Iyoba (Queen Mother) of Benin", "Mother of Oba Esigie; iconic Benin ivory mask."),
        ("unb_afr_esigie_ovonramwen", "Oba Ozolua → Oba Esigie → Oba Ovonramwen of Benin", 21, "1481–1897 CE", "Obas of Benin", "Royal Oba lineage of the Kingdom of Benin."),
    ], "african", "15th–19th c. CE", ["Benin Royal Oral Chronicles", "Mod. Univ. Hist. Vol. 7"], default_type="direct")
    edges.append(E("af_eweka1", "unb_afr_ewuare_benin", "direct", "Royal Oba dynasty of Benin descended from Eweka I (son of Oranmiyan)"))

    # 2. Kanem-Bornu Sayfawa Empire (3 nodes) -> bridged from Himyarite Sayf ibn Dhi Yazan (ar4_sayf_ibn_dhi_yazan)
    add_chain(nodes, edges, None, [
        ("unb_afr_kanem_dugu", "Kanem-Bornu Empire: King Dugu (Sefawa) → Mai Humai (c. 1075 CE)", 19, "8th–11th c. CE", "Sayfawa / Duguwa Roots", "Girgam Chronicle of Kanem-Bornu traces the Sayfawa dynasty to Himyarite Yemen.", True),
        ("unb_afr_dunama_dabbalemi", "Mai Dunama Dabbalemi (Kanem Peak, c. 1210–1248)", 20, "1210–1248 CE", "Mai of Kanem-Bornu"),
        ("unb_afr_idris_alooma", "Mai Idris Alooma of Bornu (1571–1603)", 21, "1571–1603 CE", "Mai of Bornu Empire", "Peak Bornu ruler; Ottoman diplomatic & military correspondence."),
    ], "african", "Medieval Chad Basin", ["Diwan / Girgam of Bornu"])
    edges.append(E("ar4_sayf_ibn_dhi_yazan", "unb_afr_kanem_dugu", "expansion", "Diwan / Girgam of Bornu: Sayfawa dynasty traces descent from Himyarite prince Sayf ibn Dhi Yazan"))

    # 3. Vietnam / Dai Viet (9 nodes) -> bridged from Yandi / Shennong (chn_yandi)
    add_chain(nodes, edges, None, [
        ("unb_sea_lac_long_quan", "Vietnam Ancient Origins: Lac Long Quan & Au Co → Hung Vuong Kings (Van Lang)", 8, "Legendary Bronze Age", "Hong Bang Founders", "Dai Viet Su Ky Toan Thu traces Kinh Duong Vuong & Lac Long Quan to Than Nong / Shennong (Yandi).", True),
        ("unb_sea_an_duong_vuong", "An Duong Vuong (Kingdom of Au Lac / Co Loa)", 13, "c. 257–207 BCE", "King of Au Lac"),
        ("unb_sea_trung_sisters", "Trung Sisters (Trung Trac & Trung Nhi, 40–43 CE)", 19, "40–43 CE", "Hung Royal Descendants & National Heroines"),
        ("unb_sea_ngo_quyen", "Ngo Quyen (Bach Dang Victory & Independence, 938 CE)", 19, "938–944 CE", "King of Independent Vietnam"),
        ("unb_sea_dinh_bo_linh", "Dinh Bo Linh (Emperor of Dai Co Viet, 968 CE)", 19, "968–979 CE", "Emperor of Dai Co Viet"),
        ("unb_sea_ly_thai_to", "Ly Thai To (Founder of Later Ly Dynasty, Thang Long / Hanoi, 1009)", 20, "1009–1028 CE", "Founder of Ly Dynasty"),
        ("unb_sea_tran_thai_tong", "Tran Thai Tong & General Tran Hung Dao (Defeated Kublai's Fleets)", 20, "1225–1300 CE", "Tran Dynasty Rulers"),
        ("unb_sea_le_loi", "Le Loi (Le Thai To, Founder of Later Le Dynasty, 1428)", 20, "1428–1433 CE", "Founder of Later Le Dynasty"),
        ("unb_sea_gia_long", "Emperor Gia Long (Unifier of Nguyen Dynasty Vietnam, 1802)", 21, "1802–1820 CE", "Founder of Nguyen Dynasty"),
    ], "southeast_asia", "Ancient to 19th c. CE", ["Dai Viet Su Ky Toan Thu"])
    edges.append(E("chn_yandi", "unb_sea_lac_long_quan", "expansion", "Dai Viet Su Ky Toan Thu: Kinh Duong Vuong & Lac Long Quan descend from Flame Emperor Shennong (Yandi / Than Nong)"))

    # 4. Srivijaya, Medang & Majapahit (5 nodes) -> bridged from Sang Sapurba (mal_sang_sapurba) & Malacca Sultan Mansur Shah
    add_chain(nodes, edges, None, [
        ("sea_java_raden_wijaya", "Srivijaya, Medang & Majapahit: Dapunta Hyang → Sanjaya → Airlangga → Raden Wijaya (1293)", 20, "671–1309 CE", "Maritime Indonesian Founders", "Srivijaya, Mataram, Singhasari & Majapahit founders.", True),
        ("unb_sea_tribhuwana", "Queen Tribhuwana Wijayatunggadewi of Majapahit (1328–1350)", 20, "1328–1350 CE", "Queen Regnant of Majapahit"),
        ("unb_sea_hayam_wuruk", "Hayam Wuruk & Prime Minister Gajah Mada (Majapahit Peak, 1350–1389)", 20, "1350–1389 CE", "Maharaja of Majapahit"),
    ], "southeast_asia", "7th–15th c. CE", ["Nagarakretagama", "Pararaton", "Sejarah Melayu"])
    for cid, cname, era in [
        ("unb_sea_balaputradewa", "Balaputradewa of Srivijaya (Shailendra Dynasty)", "9th c. CE"),
        ("unb_sea_ken_arok", "Ken Arok & King Kertanegara of Singhasari", "1222–1292 CE"),
    ]:
        nodes.append(N(cid, cname, "southeast_asia", 19, era, "Javanese/Sumatran Monarch", ["Pararaton", "Nalanda Inscription"], f"{cname}.", major=False))
        edges.append(E("sea_java_raden_wijaya", cid, "expansion", "Archipelagic Indonesian lineage"))
    edges += [
        E("mal_sang_sapurba", "sea_java_raden_wijaya", "expansion", "Srivijaya-Palembang & Javanese royal continuity (Pararaton / Sejarah Melayu)"),
        E("unb_sea_hayam_wuruk", "chr6_sultan_mansur_shah", "expansion", "Sejarah Melayu: Malacca-Majapahit royal marriage to Princess Raden Galoh Candra Kirana"),
    ]

    # 5. Khmer / Angkor & Siam / Ayutthaya / Chakri (15 nodes) -> bridged from Vasishtha / Kaundinya gotra
    add_chain(nodes, edges, None, [
        ("sea_khmer_jayavarman2", "Funan & Angkor Founders: Kaundinya I (+ Queen Soma) → Jayavarman II (802 CE, Chakravartin)", 19, "1st–9th c. CE", "Founders of Funan & Angkor Empire", "Early Cambodian steles & Chinese records trace Funan/Chenla & Angkor to Brahmin Kaundinya I + Naga Queen Soma.", True),
        ("unb_sea_indravarman1", "Indravarman I (Preah Ko & Bakong)", 19, "877–889 CE", "Khmer Emperor"),
        ("unb_sea_yasovarman1", "Yasovarman I (Founder of Yasodharapura / Angkor)", 19, "889–910 CE", "Khmer Emperor"),
        ("unb_sea_suryavarman1", "Suryavarman I of Angkor (1006–1050)", 20, "1006–1050 CE", "Khmer Emperor"),
        ("unb_sea_suryavarman2", "Suryavarman II (Builder of Angkor Wat, 1113–1150)", 20, "1113–1150 CE", "Builder of Angkor Wat"),
        ("unb_sea_jayavarman7", "Jayavarman VII (Builder of Angkor Thom & Bayon, 1181–1218)", 20, "1181–1218 CE", "Great Builder Emperor of Angkor", "Built Angkor Thom, Bayon & 102 hospitals; peak extent of the Khmer Empire.", True),
    ], "southeast_asia", "1st–13th c. CE", ["Khmer Inscriptions", "Zhou Daguan"])
    add_chain(nodes, edges, "sea_khmer_jayavarman2", [
        ("unb_sea_sri_indraditya", "Sri Indraditya (Founder of Sukhothai Kingdom, 1238)", 20, "1238–1270 CE", "Founder of Sukhothai"),
        ("unb_sea_ram_khamhaeng", "King Ram Khamhaeng the Great (Thai Alphabet, 1279–1298)", 20, "1279–1298 CE", "King of Sukhothai"),
        ("unb_sea_uthong", "King Uthong / Ramathibodi I (Founder of Ayutthaya, 1351)", 20, "1351–1369 CE", "Founder of Ayutthaya"),
        ("unb_sea_trailok", "King Borommatrailokkanat / Trailok (1448–1488)", 20, "1448–1488 CE", "King of Ayutthaya"),
        ("unb_sea_naresuan", "King Naresuan the Great of Ayutthaya (1590–1605)", 21, "1590–1605 CE", "King of Ayutthaya"),
        ("unb_sea_narai", "King Narai the Great (1656–1688)", 21, "1656–1688 CE", "King of Ayutthaya"),
        ("unb_sea_taksin", "King Taksin the Great (Thonburi, 1767–1782)", 21, "1767–1782 CE", "King of Thonburi"),
        ("unb_sea_rama1_chakri", "King Rama I (Founder of Chakri Dynasty of Siam, 1782)", 21, "1782–1809 CE", "Founder of Chakri Dynasty"),
        ("unb_sea_mongkut_chulalongkorn", "King Mongkut (Rama IV) → King Chulalongkorn (Rama V)", 21, "1851–1910 CE", "Chakri Modernizing Monarchs"),
    ], "southeast_asia", "13th–20th c. CE", ["Royal Chronicles of Ayutthaya & Siam"])
    edges.append(E("ind_rishis_vasishtha_agastya", "sea_khmer_jayavarman2", "expansion", "Angkorian steles & Liangshu: Funan founder Kaundinya I (Vasishtha/Kaundinya Brahmin gotra) wed Queen Soma of Cambodia"))

    # 6. Japanese Seiwa Genji Shogunates, Meiji & Living 2026 Imperial House (13 graduated + 6 new = 19 nodes)
    nodes.append(N("jpn7_emperor_seiwa", "Emperor Seiwa (56th Emperor of Japan, r. 858–876 CE; Seiwa Genji Progenitor)", "japan_korea", 19, "850–881 CE", "56th Emperor of Japan & Ancestor of Shoguns", ["Nihon Sandai Jitsuroku", "Azuma Kagami"], "Direct imperial descendant of Emperor Jimmu & Emperor Kammu; progenitor of the Seiwa Genji clans (Minamoto, Ashikaga, Tokugawa).", major=False))
    edges.append(E("pc_japan_nara_heian", "jpn7_emperor_seiwa", "direct", "56th Emperor Seiwa (Heian Imperial House descended from Emperor Jimmu)"))

    add_chain(nodes, edges, None, [
        ("unb_jpn_yoritomo", "Minamoto no Yoritomo (1st Kamakura Shogun, 1192)", 20, "1147–1199 CE", "1st Shogun of Japan", "Seiwa Genji leader; Mod. Univ. Hist. Vol. 5 & Azuma Kagami.", True),
        ("unb_jpn_hojo_masako_yoshitsune", "Hojo Masako ('Nun Shogun') & General Minamoto no Yoshitsune", 20, "1156–1225 CE", "Kamakura Leaders"),
        ("unb_jpn_hojo_tokimasa", "Hojo Tokimasa (Shikken Regency of Kamakura)", 20, "1138–1215 CE", "1st Kamakura Shikken"),
        ("unb_jpn_ashikaga_takauji", "Ashikaga Takauji (1st Muromachi Shogun, 1338)", 20, "1305–1358 CE", "1st Ashikaga Shogun"),
        ("unb_jpn_ashikaga_yoshimitsu", "Ashikaga Yoshimitsu (Golden Pavilion Kinkaku-ji)", 20, "1358–1408 CE", "3rd Ashikaga Shogun"),
        ("unb_jpn_oda_nobunaga", "Oda Nobunaga (1st Great Unifier of Sengoku Japan)", 21, "1534–1582 CE", "1st Sengoku Unifier"),
        ("unb_jpn_hideyoshi", "Toyotomi Hideyoshi (2nd Great Unifier)", 21, "1537–1598 CE", "Kampaku Unifier"),
        ("unb_jpn_tokugawa_ieyasu", "Tokugawa Ieyasu (Founder of Edo Shogunate, 1603)", 21, "1543–1616 CE", "1st Tokugawa Shogun"),
        ("unb_jpn_date_masamune", "Date Masamune ('One-Eyed Dragon' of Sendai, Hasekura Tsunenaga Mission)", 21, "1567–1636 CE", "Daimyo of Sendai"),
        ("unb_jpn_tokugawa_hidetada", "Tokugawa Hidetada (2nd Tokugawa Shogun)", 21, "1579–1632 CE", "2nd Tokugawa Shogun"),
        ("unb_jpn_tokugawa_iemitsu", "Tokugawa Iemitsu (3rd Tokugawa Shogun)", 21, "1604–1651 CE", "3rd Tokugawa Shogun"),
        ("unb_jpn_tokugawa_yoshinobu", "Tokugawa Yoshinobu (15th & Final Tokugawa Shogun)", 21, "1837–1913 CE", "15th Tokugawa Shogun"),
        ("unb_jpn_emperor_meiji", "Emperor Meiji (Meiji Restoration, 1868)", 21, "1852–1912 CE", "122nd Emperor of Japan", "Direct imperial line from Emperor Jimmu; presided over Meiji Restoration.", True),
    ], "japan_korea", "12th–20th c. CE", ["Modern Universal History Vol. 5", "Japanese Chronicles"])
    edges += [
        E("jpn7_emperor_seiwa", "unb_jpn_yoritomo", "direct", "Seiwa Genji imperial patriline (Minamoto, Ashikaga & Tokugawa shogunal houses)"),
        E("pc_japan_nara_heian", "unb_jpn_emperor_meiji", "direct", "Unbroken Japanese Imperial House succession from Emperor Jimmu to 122nd Emperor Meiji"),
    ]
    add_chain(nodes, edges, "unb_jpn_emperor_meiji", [
        ("jpn7_emperor_taisho", "Emperor Taishō / Yoshihito (123rd Emperor of Japan, r. 1912–1926)", 21, "1879–1926 CE", "123rd Emperor of Japan"),
        ("jpn7_emperor_showa", "Emperor Shōwa / Hirohito (124th Emperor of Japan, r. 1926–1989)", 21, "1901–1989 CE", "124th Emperor of Japan"),
        ("jpn7_emperor_akihito", "Emperor Emeritus Akihito (125th Emperor of Japan, r. 1989–2019; Living 2026)", 21, "1933–Present CE", "125th Emperor Emeritus (Living 2026)"),
        ("jpn7_emperor_naruhito", "Emperor Naruhito of Japan (126th Emperor, r. 2019–Present; Living 2026)", 21, "1960–Present CE", "126th Emperor of Japan (Living 2026)", "Present-day reigning head of the Imperial House of Japan, descended in unbroken traditional succession from Emperor Jimmu.", True),
        ("jpn7_princess_aiko", "Princess Aiko, Crown Prince Akishino & Prince Hisahito (Living 2026 Imperial Heirs)", 21, "1965–Present CE", "Living 2026 Japanese Imperial Family"),
    ], "japan_korea", "1879–2026 CE", ["Imperial Household Agency of Japan"], default_type="direct")

    # 7. Korean Goryeo & Joseon (11 graduated nodes) -> bridged from Unified Silla / Wave 5 counterparts
    add_chain(nodes, edges, None, [
        ("unb_kor_wang_geon", "Taejo Wang Geon (Founder of Goryeo Dynasty, 918 CE)", 19, "877–943 CE", "Goryeo Founder", "Goryeosa & Joseon Wangjo Sillok; wed Silla royal princesses.", True),
        ("unb_kor_gwangjong", "King Gwangjong of Goryeo", 19, "925–975 CE", "4th King of Goryeo"),
        ("unb_kor_yi_seonggye", "Taejo Yi Seong-gye (Founder of Joseon Dynasty, 1392)", 20, "1335–1408 CE", "Founder of Joseon Dynasty"),
        ("unb_kor_taejong", "King Taejong of Joseon (Yi Bang-won)", 20, "1367–1422 CE", "3rd King of Joseon"),
        ("unb_kor_sejong_great", "King Sejong the Great (Hangul Alphabet, 1418–1450)", 20, "1397–1450 CE", "4th King of Joseon"),
        ("unb_kor_sejo", "King Sejo of Joseon", 20, "1417–1468 CE", "7th King of Joseon"),
        ("unb_kor_yi_sunsin", "Admiral Yi Sun-sin (Joseon Naval Hero)", 21, "1545–1598 CE", "Joseon Admiral"),
        ("unb_kor_yeongjo_jeongjo", "King Yeongjo → King Jeongjo of Joseon", 21, "1694–1800 CE", "Joseon Enlightenment Kings"),
        ("unb_kor_gojong", "Emperor Gojong (Final Joseon Monarch / Korean Empire)", 21, "1852–1919 CE", "1st Emperor of Korea"),
        ("unb_kor_injo_sukjong", "King Injo & King Sukjong of Joseon (17th–18th c.)", 21, "1623–1720 CE", "Joseon Monarchs"),
        ("unb_kor_daewongun_myeongseong", "Heungseon Daewongun & Empress Myeongseong (Queen Min)", 21, "1820–1895 CE", "Late Joseon Regent & Empress"),
    ], "japan_korea", "10th–20th c. CE", ["Goryeosa", "Veritable Records of the Joseon Dynasty", "Homer Hulbert History of Korea Vols. 1–2"])
    edges += [
        E("eas5_king_munmu", "unb_kor_wang_geon", "expansion", "Goryeosa: Taejo Wang Geon unified Later Three Kingdoms & wed Silla royal princesses"),
        E("eas5_wang_geon_goryeo", "unb_kor_wang_geon", "cognate", "Same monarch across Wave 5 & Graduated Chronicle cards"),
        E("eas5_taejo_joseon", "unb_kor_yi_seonggye", "cognate", "Same founder across Wave 5 & Graduated Chronicle cards"),
        E("eas5_king_sejong", "unb_kor_sejong_great", "cognate", "Same monarch across Wave 5 & Graduated Chronicle cards"),
    ]

    # 8. Chinese Three Kingdoms, Sui, Song & Ming (10 graduated nodes) -> bridged from Han/Tang/Song/Ming Wave 5
    add_chain(nodes, edges, None, [
        ("unb_chn_cao_cao", "Cao Cao → Emperor Wen of Wei (Cao Pi, Three Kingdoms)", 19, "155–226 CE", "Cao Wei Founders", "Records of the Three Kingdoms.", True),
        ("unb_chn_wen_sui", "Emperor Wen of Sui (Yang Jian, Reunified China 581 CE)", 19, "541–604 CE", "Founder of Sui Dynasty"),
        ("unb_chn_song_taizu", "Emperor Taizu of Song (Zhao Kuangyin, 960 CE)", 20, "927–976 CE", "Founder of Song Dynasty"),
        ("unb_chn_song_huizong", "Emperor Huizong of Song", 20, "1082–1135 CE", "8th Emperor of Song"),
        ("unb_chn_yue_fei_zhuxi", "General Yue Fei (1103–1142) & Neo-Confucian Master Zhu Xi (1130–1200)", 20, "12th c. CE", "Song Statesman-General & Philosopher"),
        ("unb_chn_ming_hongwu", "Emperor Hongwu (Zhu Yuanzhang, Founder of Ming Dynasty, 1368)", 20, "1328–1398 CE", "Founder of Ming Dynasty"),
        ("unb_chn_empress_ma", "Empress Ma (Consort of Hongwu) & Prince Zhu Biao", 20, "1332–1382 CE", "Ming Imperial Family"),
        ("unb_chn_ming_yongle", "Emperor Yongle (Zhu Di) & Admiral Zheng He (Treasure Fleets)", 20, "1360–1424 CE", "3rd Ming Emperor & Admiral"),
    ], "chinese", "3rd–15th c. CE", ["Records of the Three Kingdoms", "History of Song & Ming"])
    for cid, cname, role in [
        ("unb_chn_liu_bei_zhuge", "Liu Bei (Emperor of Shu Han) & Chancellor Zhuge Liang", "Shu Han Rulers"),
        ("unb_chn_sun_quan", "Sun Quan (Emperor of Eastern Wu)", "Eastern Wu Founder"),
    ]:
        nodes.append(N(cid, cname, "chinese", 19, "Three Kingdoms (220–280 CE)", role, ["Sanguozhi / Three Kingdoms"], f"{cname}.", major=False))
        edges.append(E("unb_chn_cao_cao", cid, "cognate", "Contemporaries of China's Three Kingdoms era"))
    edges += [
        E("eas5_han_jing", "unb_chn_liu_bei_zhuge", "direct", "Sanguozhi: Liu Bei descended from Prince Liu Sheng of Zhongshan, son of Han Emperor Jing"),
        E("eas5_han_guangwu", "unb_chn_cao_cao", "expansion", "Late Eastern Han chancellor & imperial transition to Cao Wei (220 CE)"),
        E("unb_chn_wen_sui", "eas5_tang_gaozu", "expansion", "Sui-Tang imperial cousinage (Empress Dugu & Li Yuan / Tang Gaozu)"),
        E("eas5_song_taizu", "unb_chn_song_taizu", "cognate", "Same founder across Wave 5 & Graduated Chronicle cards"),
        E("eas5_ming_hongwu", "unb_chn_ming_hongwu", "cognate", "Same founder across Wave 5 & Graduated Chronicle cards"),
        E("eas5_ming_yongle", "unb_chn_ming_yongle", "cognate", "Same emperor across Wave 5 & Graduated Chronicle cards"),
    ]

    # 9. Classical Greek Philosophers, Lawgivers & Statesmen (23 graduated nodes)
    add_chain(nodes, edges, None, [
        ("unb_grk_thales", "Seven Sages & Ionian Philosophers: Thales of Miletus → Anaximander", 17, "c. 624–546 BCE", "Ionian Philosophy Founders", "Lives of Ancient Philosophers (1702) & Diogenes Laertius.", True),
        ("unb_grk_pythagoras", "Pythagoras of Samos (Mathematics & Harmonics)", 17, "c. 570–495 BCE", "Mathematician & Philosopher"),
        ("unb_grk_socrates", "Socrates of Athens (Teacher of Classical Philosophy)", 18, "470–399 BCE", "Classical Philosopher"),
        ("unb_grk_plato", "Plato (Founder of the Academy, Athens)", 18, "428–348 BCE", "Philosopher & Codrid-Solonian Scion"),
        ("unb_grk_aristotle", "Aristotle of Stagira (Founder of the Lyceum, Tutor of Alexander)", 18, "384–322 BCE", "Philosopher & Tutor of Alexander"),
    ], "greek", "6th–4th c. BCE", ["The Lives of the Ancient Philosophers (1702)", "Plutarch Lives"])
    for cid, cname, era, role in [
        ("unb_grk_homer_hesiod", "Homer & Hesiod (Epic Poets of Greece)", "c. 8th–7th c. BCE", "Epic Poets"),
        ("unb_grk_heraclitus", "Heraclitus of Ephesus", "c. 535–475 BCE", "Pre-Socratic Philosopher"),
        ("unb_grk_parmenides", "Parmenides & Zeno of Elea", "c. 515–430 BCE", "Eleatic Philosophers"),
        ("unb_grk_empedocles", "Empedocles of Acragas", "c. 494–434 BCE", "Philosopher"),
        ("unb_grk_democritus", "Leucippus & Democritus (Atomic Theory)", "c. 460–370 BCE", "Atomist Philosophers"),
        ("unb_grk_hippocrates", "Hippocrates of Kos (Father of Medicine)", "c. 460–370 BCE", "Physician (Asclepiad Clan)"),
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
        ("unb_grk_solon_lycurgus", "Greek Lawgivers: Solon of Athens → Cleisthenes (Athenian Democracy)", 17, "8th–6th c. BCE", "Constitutional Founders", "Plutarch Lives Vols. 1-5.", True),
        ("unb_grk_miltiades_themistocles", "Miltiades (Marathon, 490 BCE) & Themistocles (Salamis, 480 BCE)", 18, "5th c. BCE", "Athenian Commanders (Philaid Clan)"),
        ("unb_grk_pericles", "Pericles of Athens (Golden Age Statesman, d. 429 BCE)", 18, "495–429 BCE", "Athenian Statesman (Alcmaeonid)"),
        ("unb_grk_alcibiades_lysander", "Alcibiades of Athens & Lysander", 18, "5th c. BCE", "Athenian & Spartan Leaders"),
        ("unb_grk_epaminondas", "Epaminondas of Thebes (Battle of Leuctra, 371 BCE)", 18, "d. 362 BCE", "Theban Strategos"),
        ("unb_grk_pyrrhus_epirus", "King Pyrrhus of Epirus (319–272 BCE)", 18, "319–272 BCE", "Aeacid King of Epirus"),
    ], "greek", "8th–3rd c. BCE", ["Plutarch's Lives", "Thucydides", "Herodotus"])
    edges += [
        E("grkr_aeo_12_neleus_of_pylos", "unb_grk_solon_lycurgus", "expansion", "Plutarch Solon 1: Solon & Codrid house of Athens descend from King Neleus of Pylos"),
        E("unb_grk_solon_lycurgus", "unb_grk_plato", "expansion", "Diogenes Laertius III.1: Plato descended from King Codrus (via Ariston) & Solon's brother Dropides (via Perictione)"),
        E("grkr_aeo_13_king_nestor_of_pylos", "unb_grk_pericles", "expansion", "Alcmaeonid lineage of Pericles traced to King Nestor of Pylos"),
        E("grkr_b3_ajax", "unb_grk_miltiades_themistocles", "expansion", "Herodotus VI.35: Philaid house of Miltiades descended from Philaeus, son of Telamonian Ajax"),
        E("grkr_b3_ajax", "unb_grk_alcibiades_lysander", "expansion", "Plutarch Alcibiades 1: Alcibiades descended from Eurysaces, son of Telamonian Ajax"),
        E("grkr_b3_neoptolemus", "unb_grk_pyrrhus_epirus", "direct", "Aeacid royal dynasty of Epirus descended from Achilles & Neoptolemus"),
        E("cls3_pyrrhus_epirus", "unb_grk_pyrrhus_epirus", "cognate", "Same Aeacid king across Wave 3 & Graduated Chronicle cards"),
        E("grkr_div_07_apollo_artemis_twins_of_zeus", "unb_grk_hippocrates", "expansion", "Asclepiad clan of Kos traced 18-20 generations to Asclepius (son of Apollo) & Heracles"),
        E("unb_grk_aristotle", "grk_alexander", "expansion", "Tutor of Alexander the Great at Mieza (Plutarch Alexander 7)"),
        E("egr_ptol_01_ptolemy_i_soter_berenice_i", "unb_grk_euclid", "expansion", "Royal patronage of Euclid at Alexandria under Ptolemy I Soter"),
    ]

    # =========================================================================
    # PART B: NEW DEEP ANCIENT & LIVING ROYAL BRIDGES (~45 NEW NODES)
    # =========================================================================

    # 1. Hittite Empire (15 nodes) -> from bib_heth (Gen 10:15) to Ramesses II, Akhenaten & Babylon
    add_chain(nodes, edges, "bib_heth", [
        ("hit7_labarna", "Labarna I (Founder of Old Hittite Kingdom, c. 1680–1650 BCE)", 9, "c. 1680–1650 BCE", "Founder of Old Hittite Kingdom"),
        ("hit7_hattusili1", "Hattusili I / Labarna II (Founder of Hattusa Capital)", 9, "c. 1650–1620 BCE", "Great King of Hattusa"),
        ("hit7_mursili1", "Mursili I (Sacked Babylon 1595 BCE, Ending Hammurabi's Dynasty)", 10, "c. 1620–1590 BCE", "Great King of Hattusa"),
        ("hit7_telipinu", "King Telipinu (Edict of Telipinu Royal Succession Law)", 10, "c. 1525–1500 BCE", "Great King of Hatti"),
        ("hit7_tudhalya1", "Tudhaliya I/II (Founder of Hittite New Kingdom)", 11, "c. 1400 BCE", "Great King of Hatti"),
        ("hit7_suppiluliuma1", "Suppiluliuma I (Hittite Empire Peak; Amarna Letters EA 41)", 12, "c. 1344–1322 BCE", "Great King of Hatti", "Expanded Hittite Empire across Syria, Mitanni & Anatolia; Amarna Letter EA 41.", True),
        ("hit7_mursili2", "Mursili II (Annals of Mursili & Plague Prayers)", 12, "c. 1321–1295 BCE", "Great King of Hatti"),
    ], "levant_egypt", "2nd Millennium BCE", ["Genesis 10:15", "Hittite State Archives (CTH)", "Amarna Letters"])
    nodes.append(N("hit7_zannanza", "Prince Zannanza of Hatti (Betrothed to Ankhesenamun; Slain en route to Egypt)", "levant_egypt", 12, "c. 1323 BCE", "Hittite Royal Prince (Zannanza Affair)", ["Deeds of Suppiluliuma (KBo V.6)", "Amarna Letters"], "Son of Suppiluliuma I requested as husband by Egyptian Queen Ankhesenamun (daughter of Akhenaten)."))
    edges += [
        E("hit7_suppiluliuma1", "hit7_zannanza", "direct", "Son of Suppiluliuma I"),
        E("hit7_zannanza", "eg_akhenaten", "expansion", "Deeds of Suppiluliuma: Ankhesenamun (daughter of Akhenaten & widow of Tutankhamun) requested Zannanza in marriage"),
        E("hit7_mursili1", "babr_1_09_samsu_ditana_31_yrs_fell_to_", "expansion", "1595 BCE: Hittite King Mursili I sacked Babylon and ended Samsu-ditana's Amorite dynasty"),
    ]
    add_chain(nodes, edges, "hit7_mursili2", [
        ("hit7_muwatalli2", "Muwatalli II (Battle of Kadesh vs Ramesses II, 1274 BCE)", 13, "c. 1295–1272 BCE", "Great King of Hatti"),
        ("hit7_mursili3", "Mursili III / Urhi-Teshub (Deposed Son of Muwatalli II)", 13, "c. 1272–1267 BCE", "Great King of Hatti"),
    ], "levant_egypt", "13th c. BCE", ["Hittite State Archives", "Kadesh Inscriptions"], default_type="direct")
    add_chain(nodes, edges, "hit7_mursili2", [
        ("hit7_hattusili3", "Great King Hattusili III & Queen Puduhepa (Kadesh Peace Treaty 1259 BCE)", 13, "c. 1267–1237 BCE", "Great King & Tawananna of Hatti", "Co-author of the oldest surviving international peace treaty with Ramesses II (1259 BCE).", True),
        ("hit7_maathorneferure", "Princess Maathorneferure (Hittite Princess Married Pharaoh Ramesses II, 1246 BCE)", 13, "13th c. BCE", "Great Royal Wife of Egypt", "Daughter of Hattusili III & Puduhepa wed to Pharaoh Ramesses II in Year 34 to seal the Egyptian-Hittite alliance.", True),
    ], "levant_egypt", "13th c. BCE", ["Egyptian-Hittite Peace Treaty (KUB III / Karnak)"], default_type="direct")
    edges.append(E("hit7_maathorneferure", "eg_ramesses2", "expansion", "1246 BCE Royal Marriage: Princess Maathorneferure wed Pharaoh Ramesses II"))
    add_chain(nodes, edges, "hit7_hattusili3", [
        ("hit7_tudhalya4", "Tudhaliya IV (Yazılıkaya Sanctuary & Aegean Campaigns)", 13, "c. 1237–1209 BCE", "Great King of Hatti"),
        ("hit7_suppiluliuma2", "Suppiluliuma II (Final Great King of Hattusa, Bronze Age Collapse)", 14, "c. 1207–1178 BCE", "Last Great King of Hatti"),
        ("hit7_kuzi_teshub", "King Kuzi-Teshub of Carchemish (Neo-Hittite Survival Line)", 14, "12th c. BCE", "Great King of Carchemish (Syro-Hittite)"),
    ], "levant_egypt", "13th–12th c. BCE", ["Hittite State Archives", "Carchemish Inscriptions"], default_type="direct")

    # 2. Kingdom of Mitanni (8 nodes) -> Amarna diplomatic marriages with Thutmose IV, Amenhotep III, Akhenaten & Hatti
    add_chain(nodes, edges, None, [
        ("mit7_kirta_parshatatar", "King Kirta → Shuttarna I → Parshatatar (Founders of Mitanni / Hanigalbat)", 11, "c. 1500–1450 BCE", "Mitanni Dynasty Founders"),
        ("mit7_saushtatar", "King Saushtatar of Mitanni (Silver-Gold Door Looted from Ashur)", 11, "c. 1430 BCE", "King of Mitanni"),
        ("mit7_artatama1", "King Artatama I of Mitanni (7 Letters to Thutmose IV, EA 24/29)", 12, "c. 1410–1400 BCE", "King of Mitanni", "Formed Mitanni-Egypt alliance; his daughter married Pharaoh Thutmose IV."),
        ("mit7_shuttarna2", "King Shuttarna II of Mitanni (Amarna Alliance)", 12, "c. 1400–1385 BCE", "King of Mitanni"),
        ("mit7_tushratta", "King Tushratta of Mitanni (Amarna Letters EA 17–29)", 12, "c. 1380–1350 BCE", "Great King of Mitanni", "Major Near Eastern sovereign in Amarna correspondence with Amenhotep III & Akhenaten.", True),
        ("mit7_tadukhepa", "Princess Tadukhepa of Mitanni (Married Amenhotep III & Akhenaten)", 12, "14th c. BCE", "Mitanni Princess & Egyptian Royal Wife"),
    ], "mesopotamian", "15th–14th c. BCE", ["Amarna Letters (EA 17–29)"], default_type="direct")
    nodes += [
        N("mit7_gilukhepa", "Princess Gilukhepa of Mitanni (Daughter of Shuttarna II; Wed Amenhotep III)", "mesopotamian", 12, "c. 1380 BCE", "Mitanni Princess & Egyptian Queen", ["Amenhotep III Marriage Scarabs"], "Brought 317 attendants to Thebes in Amenhotep III Year 10."),
        N("mit7_shattiwaza", "King Shattiwaza of Mitanni (Wed Daughter of Hittite Suppiluliuma I)", "mesopotamian", 12, "c. 1350–1320 BCE", "Vassal King of Mitanni", ["Shattiwaza-Suppiluliuma Treaty (CTH 51)"], "Son of Tushratta restored by Suppiluliuma I through dynastic marriage."),
    ]
    edges += [
        E("mit7_artatama1", "egr_nk_05_thutmose_iv_dyn_xviii", "expansion", "Amarna EA 29: Artatama I's daughter wed Pharaoh Thutmose IV"),
        E("mit7_shuttarna2", "mit7_gilukhepa", "direct", "Daughter of Shuttarna II"),
        E("mit7_gilukhepa", "eg_amenhotep3", "expansion", "Amenhotep III Year 10 Marriage Scarab: Gilukhepa wed Pharaoh Amenhotep III"),
        E("mit7_tadukhepa", "eg_amenhotep3", "expansion", "Amarna Letters EA 19–22: Princess Tadukhepa wed Pharaoh Amenhotep III"),
        E("mit7_tadukhepa", "eg_akhenaten", "expansion", "Amarna Letters EA 27–29: Tadukhepa passed to Amenhotep IV / Akhenaten"),
        E("mit7_tushratta", "mit7_shattiwaza", "direct", "Son of Tushratta"),
        E("mit7_shattiwaza", "hit7_suppiluliuma1", "expansion", "CTH 51 Treaty: Shattiwaza wed daughter of Hittite King Suppiluliuma I"),
    ]

    # 3. Elamite Empire (8 nodes) -> from bib_elam (Gen 10:22) to Chedorlaomer & Kassite Babylon
    add_chain(nodes, edges, "bib_elam", [
        ("ela7_awan_puzur_inshushinak", "King Puzur-Inshushinak of Awan & Susa (Linear Elamite Builder)", 8, "c. 2100 BCE", "King of Awan & Elam"),
        ("ela7_sukkalmah_ebarat", "Ebarat II & Shilhaha (Sukkalmah / Grand Regent Dynasty of Elam)", 9, "c. 1850 BCE", "Sukkalmah Founders"),
        ("ela7_igihalki", "Igi-Halki (Founder of Middle Elamite Dynasty, c. 1400 BCE)", 12, "c. 1400–1380 BCE", "King of Anshan & Susa"),
        ("ela7_untash_napirisha", "King Untash-Napirisha (+ Queen Napirasu; Builder of Chogha Zanbil)", 13, "c. 1340–1300 BCE", "King of Anshan & Susa"),
        ("ela7_shutruk_nakhunte", "King Shutruk-Nakhunte I of Elam (Seized Code of Hammurabi to Susa)", 13, "c. 1190–1155 BCE", "Great King of Elam", "Married eldest daughter of Kassite King Meli-Shipak; carried Hammurabi's stele & Naram-Sin's Victory Stele to Susa.", True),
        ("ela7_kutir_nahhunte", "King Kutir-Nahhunte III (Ended Kassite Dynasty of Babylon, 1155 BCE)", 14, "c. 1155–1150 BCE", "King of Elam"),
        ("ela7_shilhak_inshushinak", "King Shilhak-Inshushinak (Imperial Height of Middle Elam)", 14, "c. 1150–1120 BCE", "King of Elam"),
        ("ela7_humban_haltash3", "King Humban-Haltash III (Final Neo-Elamite King Before Ashurbanipal 647 BCE)", 16, "r. 649–647 BCE", "Last Neo-Elamite King"),
    ], "mesopotamian", "2100–647 BCE", ["Genesis 10:22", "Susa Royal Inscriptions", "Berlin Letter"], default_type="expansion")
    edges += [
        E("ela7_sukkalmah_ebarat", "bib16_foes_01_chedorlaomer_king_of_elam_ge", "expansion", "Elamite Sukkalmah / Old Babylonian era synchronism with Chedorlaomer (Gen 14)"),
        E("ela7_untash_napirisha", "babr_3_10_burna_buriash_ii_amarna_lett", "expansion", "Berlin Letter VAT 17020: Kassite-Elamite diplomatic marriages (Kurigalzu / Burna-Buriash line)"),
        E("ela7_shutruk_nakhunte", "bab_dyn3_kassite", "expansion", "Berlin Letter VAT 17020: Shutruk-Nakhunte wed eldest daughter of Kassite King Meli-Shipak"),
    ]

    # 4. Nabataean Kingdom of Petra (10 nodes) -> from ish_nebaioth (Gen 25:13) to Cypros & Herod Antipas
    add_chain(nodes, edges, "ish_nebaioth", [
        ("nab7_aretas1", "King Aretas I of Petra (1st Named Nabataean King, 2 Macc 5:8, 168 BCE)", 17, "fl. 168 BCE", "King of the Nabataeans"),
        ("nab7_aretas2", "King Aretas II of Nabataea (Ally of Gaza vs Alexander Jannaeus)", 17, "c. 120–96 BCE", "King of the Nabataeans"),
        ("nab7_obodas1", "King Obodas I (Conquered Moab & Gilead; Entombed at Avdat)", 17, "r. c. 96–85 BCE", "King of the Nabataeans"),
        ("nab7_aretas3", "King Aretas III Philhellenos (Coined Damascus; Ally of Hyrcanus II)", 18, "r. 84–62 BCE", "King of Nabataea & Coele-Syria"),
        ("nab7_malichus1", "King Malichus I (Allied with Julius Caesar; Rival of Herod)", 18, "r. 59–30 BCE", "King of the Nabataeans"),
        ("nab7_obodas3", "King Obodas III (Built Petra Monuments; Syllaeus Era)", 18, "r. 30–9 BCE", "King of the Nabataeans"),
        ("nab7_aretas4", "King Aretas IV Philopatris (Built Petra Al-Khazneh Treasury; 2 Cor 11:32)", 18, "r. 9 BCE–40 CE", "Great King of Nabataea (NT 2 Cor 11:32)", "Ruled Damascus when Paul escaped in a basket (2 Cor 11:32); father-in-law of Herod Antipas.", True),
        ("nab7_malichus2", "King Malichus II (40–70 CE; Sent Cavalry to Titus)", 19, "r. 40–70 CE", "King of the Nabataeans"),
        ("nab7_rabbel2", "King Rabbel II Soter (Final Sovereign King of Petra, 70–106 CE)", 19, "r. 70–106 CE", "Last King of Nabataea"),
    ], "arabian", "2nd c. BCE – 106 CE", ["Josephus Ant. I.12.4, XIV, XVIII", "2 Corinthians 11:32", "Nabataean Petra Inscriptions"], default_type="expansion")
    nodes.append(N("nab7_phasaelis", "Princess Phasaelis of Nabataea (1st Wife of Tetrarch Herod Antipas; Josephus Ant. XVIII.5.1)", "arabian", 18, "1st c. CE", "Nabataean Princess & Wife of Herod Antipas", ["Josephus Antiquities XVIII.5.1"], "Daughter of King Aretas IV; her divorce by Herod Antipas for Herodias triggered war with Nabataea and John the Baptist's rebuke.", major=True))
    edges += [
        E("nab7_aretas4", "nab7_phasaelis", "direct", "Daughter of King Aretas IV of Nabataea"),
        E("nab7_phasaelis", "bib16_her_08_tetrarch_herod_antipas_phasa", "expansion", "Josephus Ant. XVIII.5.1: Royal Marriage of Princess Phasaelis & Tetrarch Herod Antipas"),
        E("nab7_aretas3", "her2_cypros_nabataea", "expansion", "Josephus Ant. XIV.7.3: Nabataean royal house of Petra (Cypros wife of Antipater I)"),
        E("pal_solomon_aretas_tadmor", "nab7_aretas4", "cognate", "Cross-chronicle Aretas / Al-Harith Nabataean-Petra link"),
    ]

    # 5. Post-Columbian Spanish-Habsburg Noble Houses of Mexico & Peru (4 nodes)
    # Linked STRICTLY to Charles V & Philip II (ZERO links to mod36/mod13 unbridged pre-Columbian nodes!)
    for nid, name, parent, era, role, notes in [
        ("esp7_isabel_moctezuma_tultengo", "Doña Isabel Moctezuma & Dukes of Moctezuma de Tultengo (Grandees of Spain)", "mon_esp_charles5", "1509–Present CE", "Hispano-Mexican Ducal House (Grandees of Spain)", "Granted royal encomienda & perpetual Spanish noble patent under Emperor Charles V; elevated to Dukes of Moctezuma de Tultengo."),
        ("esp7_martin_cortes_malintzin", "Don Martín Cortés & Marquesses of the Valley of Oaxaca (New Spain)", "mon_esp_charles5", "c. 1523–1595 CE", "Hispano-Mexican Noble House", "Patent & Habsburg court service under Emperor Charles V & King Philip II."),
        ("esp7_beatriz_clara_coya_loyola", "Doña Beatriz Clara Coya + Don Martín García Óñez de Loyola (Marquesses of Santiago de Oropesa)", "mon_esp_philip2", "1556–1600 CE", "Hispano-Peruvian Marquisate House", "1572 Habsburg viceregal marriage uniting Spanish noble house of Loyola with Peruvian colonial Marquisate of Oropesa."),
        ("esp7_inca_garcilaso", "Inca Garcilaso de la Vega (1539–1616; Author of Comentarios Reales)", "mon_esp_philip2", "1539–1616 CE", "Renaissance Chronicler & Spanish Noble Historian", "Son of Spanish conquistador Sebastián Garcilaso de la Vega & Chimpu Ocllo; served in Philip II's Spanish army in Andalusia."),
    ]:
        nodes.append(N(nid, name, "europe_norse", 21, era, role, ["Archivo General de Indias", "Comentarios Reales (1609)"], notes, major=False))
        edges.append(E(parent, nid, "expansion", "Post-Columbian Spanish Habsburg royal patent / court service (unconnected to pre-Columbian Pending Bridge graphs)"))

    return {
        "module": "49_wave7_graduated_empires_and_deep_bridges",
        "title": "Wave 7: Graduated World Empires (92 Nodes) & Deep Ancient/Living Royal Bridges (Hittite, Mitanni, Elam, Nabataea, Japan 2026)",
        "nodes": nodes,
        "edges": edges,
    }
