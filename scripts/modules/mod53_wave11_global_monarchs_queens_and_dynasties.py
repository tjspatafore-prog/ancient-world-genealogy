"""
Module 53: Wave 11 — Global Monarchs, Queens & Living 2026 Crowns:
Habsburg Austria-Hungary, Romanovs, Post-1815 France & Italy, Modern Greece,
Balkan Empires (Bulgaria, Serbia, Wallachia/Moldavia, Romania), Imperial China Gaps (Lü Zhi, Wu Zetian, Wanli),
Delhi Sultanate, Mysore, Jhansi, Nepal, Living 2026 Bhutan/Thailand/Cambodia/Brunei/Malaysia,
Living 2026 Arabian Gulf Crowns (Saudi Arabia, Oman, UAE, Qatar, Kuwait, Bahrain, Hashemite Iraq),
& Ancient Near East / Classical Missing Monarchs (Commagene, Saba Karib'il Watar, Gudit, Evagoras, Sidon, Edessa).
"""

from . import N, E


def add_chain(nodes, edges, parent_id, items, tradition, era_default, sources, default_type="direct"):
    prev = parent_id
    for item in items:
        nid, name, tier = item[0], item[1], item[2]
        era = item[3] if len(item) > 3 else era_default
        role = item[4] if len(item) > 4 else "Sovereign / Monarch"
        notes = item[5] if len(item) > 5 else f"Chronicle succession in {', '.join(sources)}."
        major = item[6] if len(item) > 6 else False
        nodes.append(N(nid, name, tradition, tier, era, role, sources, notes, major=major))
        if prev:
            edges.append(E(prev, nid, default_type, f"{', '.join(sources)}: succession"))
        prev = nid


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # SECTION A: EUROPEAN & BALKAN MONARCHIES (24 nodes)
    # =========================================================================
    add_chain(nodes, edges, "roy6_leopold2_hre", [
        ("roy11_francis2_austria", "Emperor Francis II / I (Final Holy Roman Emperor & 1st Emperor of Austria, 1792–1835)", 21, "1768–1835 CE", "Emperor of Austria & Last HRE"),
        ("roy11_franz_joseph_sisi", "Emperor Franz Joseph I (+ Empress Elisabeth 'Sisi', r. 1848–1916 CE)", 21, "1830–1916 CE", "Emperor of Austria & King of Hungary", "Longest-reigning Habsburg monarch of Austria-Hungary; great-uncle of Otto & Karl von Habsburg.", True),
    ], "europe_norse", "18th–20th c. CE", ["Almanach de Gotha", "Habsburg Archives"])
    nodes += [
        N("roy11_franz_ferdinand", "Archduke Franz Ferdinand of Austria-Este (Nephew of Franz Joseph, 1863–1914 CE)", "europe_norse", 21, "1863–1914 CE", "Heir Presumptive to Austria-Hungary", ["Almanach de Gotha"], "His 1914 assassination at Sarajevo triggered World War I."),
        N("roy11_karl1_otto_habsburg", "Emperor Blessed Karl I → Otto von Habsburg → Archduke Karl (Living 2026 House of Habsburg)", "europe_norse", 22, "1887–Present CE", "Living 2026 Head of House of Habsburg-Lorraine", ["Almanach de Gotha", "Burke's Royal Families"], "Final Austrian Emperor Karl I (grandnephew of Franz Joseph) -> Crown Prince Otto -> Karl von Habsburg (b. 1961)."),
    ]
    edges += [
        E("roy11_franz_joseph_sisi", "roy11_franz_ferdinand", "direct", "Nephew & heir presumptive of Emperor Franz Joseph I"),
        E("roy11_franz_joseph_sisi", "roy11_karl1_otto_habsburg", "direct", "Great-uncle to Emperor Karl I -> Living House of Habsburg (2026)"),
    ]

    add_chain(nodes, edges, "mon_rus_catherine2", [
        ("roy11_tsar_alexander1_nicholas1", "Tsars Paul I, Alexander I (Napoleonic Era) & Nicholas I of Russia (1796–1855 CE)", 21, "1754–1855 CE", "Emperors of All Russia"),
        ("roy11_tsar_alexander2_3", "Tsar Alexander II (Liberator, r. 1855–1881) & Tsar Alexander III (1881–1894 CE)", 21, "1818–1894 CE", "Emperors of All Russia"),
    ], "europe_norse", "1796–1894 CE", ["Almanach de Gotha", "Russian Imperial Archives"])
    edges.append(E("roy11_tsar_alexander2_3", "roy6_tsar_nicholas2", "direct", "Father-to-son succession to Tsar Nicholas II"))

    add_chain(nodes, edges, "mon_fra_napoleon", [
        ("roy11_louis18_charles10", "Kings Louis XVIII & Charles X of France (Bourbon Restoration, 1814–1830 CE)", 21, "1755–1836 CE", "Bourbon Kings of France"),
        ("roy11_louis_philippe", "King Louis-Philippe I of the French (House of Orléans, r. 1830–1848 CE)", 21, "1773–1850 CE", "King of the French (Orléans)"),
        ("roy11_napoleon3_eugenie", "Emperor Napoleon III (+ Empress Eugénie; Nephew of Napoleon I, r. 1852–1870 CE)", 21, "1808–1873 CE", "Emperor of the French"),
    ], "europe_norse", "1814–1870 CE", ["Almanach de Gotha", "French Royal Archives"], default_type="expansion")

    add_chain(nodes, edges, "sav_witichind_hubert_victor", [
        ("roy11_victor_emmanuel2", "King Victor Emmanuel II of Italy (Savoy Unifier of Italy, 1861–1878 CE)", 21, "1820–1878 CE", "1st King of United Italy", "House of Savoy sovereign proclaimed first King of Italy in 1861 CE.", True),
        ("roy11_umberto1_victor3", "Kings Umberto I, Victor Emmanuel III & Umberto II of Italy (1878–1946 CE)", 21, "1844–1983 CE", "Kings of Italy"),
    ], "europe_norse", "1861–1946 CE", ["Almanach de Gotha", "Savoy Royal Archives"])

    add_chain(nodes, edges, "mon_eng_victoria", [
        ("roy11_george1_greece", "King George I of Greece (+ Grand Duchess Olga Konstantinovna of Russia, 1863–1913 CE)", 21, "1845–1913 CE", "King of the Hellenes (Glücksburg)"),
        ("roy11_constantine1_greece", "King Constantine I (+ Sophia of Prussia, Granddaughter of Queen Victoria, 1913–1922)", 21, "1868–1923 CE", "King of the Hellenes"),
        ("roy11_paul_frederica_greece", "King Paul & Queen Frederica of Greece (Parents of Queen Sofía of Spain, 1947–1964 CE)", 21, "1901–1981 CE", "King & Queen of Greece"),
        ("roy11_constantine2_greece", "King Constantine II of Greece & Crown Prince Pavlos (1940–Present CE)", 22, "1940–Present CE", "Glücksburg Royal House of Greece"),
    ], "europe_norse", "1863–2026 CE", ["Almanach de Gotha", "Greek Royal Archives"], default_type="expansion")
    edges.append(E("roy11_paul_frederica_greece", "eur9_juan_carlos1", "direct", "Daughter Princess Sofía of Greece married King Juan Carlos I of Spain"))

    add_chain(nodes, edges, "mon_rom_basil2", [
        ("roy11_khan_asparukh_boris1", "Khan Asparukh (681 CE) → Krum → Tsar St. Boris I of Bulgaria (Baptized 864 CE)", 19, "681–907 CE", "Khans & Christianizer of Bulgaria"),
        ("roy11_tsar_simeon1_bulgaria", "Tsar Simeon I the Great of Bulgaria (Preslav Golden Age, r. 893–927 CE)", 19, "864–927 CE", "1st Tsar / Emperor of Bulgaria", "Educated in Constantinople; proclaimed Tsar of Bulgarians and Greeks.", True),
        ("roy11_tsar_samuel_ivan_asen2", "Tsars Samuel, Ivan Asen II & Simeon II of Bulgaria (10th c. – 2026 Living Line)", 21, "997–Present CE", "Tsars of Bulgaria"),
    ], "europe_norse", "7th c. – 2026 CE", ["Bulgarian Chronicles", "De Administrando Imperio"], default_type="expansion")

    add_chain(nodes, edges, "mon_rom_basil2", [
        ("roy11_stefan_nemanja", "Grand Župan Stefan Nemanja → King Stefan the First-Crowned (Serbia, 1166–1228 CE)", 20, "1113–1228 CE", "Founder of Nemanjić Serbia"),
        ("roy11_stefan_dusan", "Emperor Stefan Uroš IV Dušan ('Dušan the Mighty', Serbian Empire, 1331–1355 CE)", 20, "c. 1308–1355 CE", "Tsar of Serbs & Greeks", "Promulgated Dušan's Code and raised the Serbian Archbishopric to a Patriarchate.", True),
        ("roy11_prince_lazar_kosovo", "Prince St. Lazar Hrebeljanović (Kosovo 1389) & Despot Stefan Lazarević (d. 1427 CE)", 20, "c. 1329–1427 CE", "Serbian Prince & Despot"),
    ], "europe_norse", "12th–15th c. CE", ["Serbian Royal Chronicles", "Echard Roman History"], default_type="expansion")

    add_chain(nodes, edges, "eur42_almos_arpad_stephen", [
        ("roy11_mircea_vlad3_dracula", "Voivodes Mircea the Elder & Vlad III Drăculea ('Vlad the Impaler', Wallachia, 1386–1476)", 20, "1355–1477 CE", "Voivodes of Wallachia"),
        ("roy11_stephen_great_moldavia", "Voivode St. Stephen the Great of Moldavia (Ştefan cel Mare, r. 1457–1504 CE)", 21, "c. 1433–1504 CE", "Prince / Voivode of Moldavia", "Fought 36 battles defending Moldavia; cousin-ally of Vlad III and candidate to Matthias Corvinus.", True),
    ], "europe_norse", "14th–16th c. CE", ["Danubian Chronicles", "Knolles Turkish History"], default_type="expansion")

    add_chain(nodes, edges, "mon_eng_victoria", [
        ("roy11_carol1_queen_marie_romania", "King Carol I, King Ferdinand I & Queen Marie of Romania (Granddaughter of Queen Victoria, 1866–1938)", 21, "1839–1938 CE", "Hohenzollern-Sigmaringen Monarchs of Romania"),
        ("roy11_king_michael1_romania", "King Michael I of Romania (+ Anne of Bourbon-Parma) & Margareta (Living 2026)", 22, "1921–Present CE", "Final King of Romania & Custodian of the Crown"),
    ], "europe_norse", "1866–2026 CE", ["Almanach de Gotha"], default_type="expansion")

    # =========================================================================
    # SECTION B: IMPERIAL CHINA GAPS — LÜ ZHI TO WU ZETIAN, WANLI & QING (18 nodes)
    # =========================================================================
    nodes += [
        N("chn11_empress_lu_zhi", "Empress Dowager Lü Zhi (+ Liu Bang / Han Gaozu; First Woman Ruler of Imperial China, d. 180 BCE)", "chinese", 17, "241–180 BCE", "Han Empress Dowager & Regent", ["Sima Qian Shiji Ch. 9"], "Consort of Han founder Liu Bang (Han Gaozu) & regent of Early Western Han."),
        N("chn11_emperor_xuan_han", "Emperor Xuan of Han / Liu Bingyi (Great-Grandson of Han Wudi, r. 74–49 BCE)", "chinese", 18, "91–49 BCE", "Western Han Emperor", ["Book of Han (Han Shu)"], "Golden Age Western Han sovereign under whom the Xiongnu submitted."),
        N("chn11_wang_mang", "Emperor Wang Mang (Xin Dynasty Interregnum, 9–23 CE)", "chinese", 19, "45 BCE–23 CE", "Emperor of Xin Dynasty", ["Book of Han"], "Nephew of Empress Wang Zhengjun between Western & Eastern Han."),
        N("chn11_emperor_ming_han", "Emperor Ming of Han & Emperor Zhang (Patron of First Buddhist Temple at Luoyang, 57–88 CE)", "chinese", 19, "28–88 CE", "Eastern Han Emperors", ["Book of Later Han"], "Sons & grandsons of Han Guangwu; sent Ban Chao along the Silk Road."),
        N("chn11_emperor_xian_han", "Emperor Xian of Han / Liu Xie (Final Han Emperor, Abdicated 220 CE to Cao Pi)", "chinese", 19, "181–234 CE", "Last Emperor of Han Dynasty", ["Records of the Three Kingdoms"], "Last Eastern Han monarch whose 220 CE abdication launched the Three Kingdoms."),
    ]
    edges += [
        E("eas5_han_gaozu", "chn11_empress_lu_zhi", "direct", "Consort of Emperor Han Gaozu (Liu Bang)"),
        E("eas5_han_jing", "chn11_emperor_xuan_han", "direct", "Great-grandson of Han Wudi / descendant of Emperor Jing"),
        E("chn11_emperor_xuan_han", "chn11_wang_mang", "expansion", "Western Han imperial interregnum (9–23 CE)"),
        E("chn11_wang_mang", "chn11_emperor_ming_han", "expansion", "Eastern Han restoration under Guangwu & Mingdi"),
        E("chn11_emperor_ming_han", "chn11_emperor_xian_han", "direct", "Eastern Han imperial descent to Emperor Xian"),
        E("chn11_emperor_xian_han", "unb_chn_cao_cao", "expansion", "220 CE Imperial Abdication to Cao Pi (Cao Wei)"),
    ]

    nodes += [
        N("chn11_sima_yan_jin", "Emperor Wu of Jin / Sima Yan (Reunified China 280 CE, Western Jin Dynasty)", "chinese", 19, "236–290 CE", "Founder of Jin Dynasty", ["Book of Jin"], "Grandson of Sima Yi; ended the Three Kingdoms era in 280 CE."),
        N("chn11_xiaowen_northern_wei", "Emperor Xiaowen of Northern Wei (Tuoba Hong / Yuan Hong, r. 471–499 CE)", "chinese", 19, "467–499 CE", "Xianbei Emperor of Northern Wei", ["Book of Wei"], "Sinicized Northern Wei court and built the Longmen Grottoes."),
        N("chn11_emperor_yang_sui", "Emperor Yang of Sui / Yang Guang (Built Grand Canal, r. 604–618 CE)", "chinese", 19, "569–618 CE", "2nd Emperor of Sui Dynasty", ["Book of Sui"], "Son of Sui Wendi; completed the Grand Canal before Tang Gaozu's rise."),
        N("chn11_emperor_gaozong_wu_zetian", "Emperor Tang Gaozong & Empress Regnant Wu Zetian (Zhou Dynasty, 624–705 CE)", "chinese", 19, "624–705 CE", "Sole Female Emperor Regnant of China", ["Old & New Book of Tang"], "Only woman in Chinese history to reign as Huángdì (Emperor Regnant) in her own right; mother of Emperors Zhongzong & Ruizong.", True),
        N("chn11_emperor_suzong_tang", "Emperor Suzong → Dezong → Xianzong of Tang (Post-An Lushan Restoration, 756–820 CE)", "chinese", 19, "711–820 CE", "Late Tang Emperors", ["New Book of Tang"], "Son of Tang Xuanzong; rebuilt Tang authority after An Lushan."),
    ]
    edges += [
        E("unb_chn_cao_cao", "chn11_sima_yan_jin", "expansion", "266 CE Cao Wei -> Sima Jin Dynasty succession"),
        E("chn11_sima_yan_jin", "chn11_xiaowen_northern_wei", "expansion", "Northern & Southern Dynasties transition"),
        E("unb_chn_wen_sui", "chn11_emperor_yang_sui", "direct", "Son of Emperor Wen of Sui"),
        E("eas5_tang_gaozu", "chn11_emperor_gaozong_wu_zetian", "direct", "Son Taizong -> Grandson Gaozong & Empress Regnant Wu Zetian"),
        E("chn11_emperor_gaozong_wu_zetian", "eas5_tang_xuanzong", "direct", "Grandmother Empress Wu Zetian -> Emperor Tang Xuanzong"),
        E("eas5_tang_xuanzong", "chn11_emperor_suzong_tang", "direct", "Son Emperor Suzong & grandson Xianzong"),
    ]

    nodes += [
        N("chn11_yelv_abaoji_liao", "Emperor Taizu Yelü Abaoji (Founder of Khitan Liao Dynasty, 907–926 CE)", "chinese", 19, "872–926 CE", "Founder of Liao Dynasty", ["History of Liao"], "Khitan founder whose western branch formed Qara Khitai."),
        N("chn11_aguda_jin", "Emperor Taizu Wanyan Aguda (Founder of Jurchen Jin Dynasty, 1115–1123 CE)", "chinese", 20, "1068–1123 CE", "Founder of Jin Dynasty", ["History of Jin"], "Jurchen ancestor of the Aisin Gioro / Manchu Qing founders."),
        N("chn11_song_renzong_gaozong", "Emperors Renzong (Northern Song Peak) & Gaozong (1st Southern Song Emperor, 1022–1162 CE)", "chinese", 20, "1010–1187 CE", "Song Dynasty Emperors", ["History of Song"], "Golden Age Northern Song Renzong & Southern Song founder Gaozong."),
        N("chn11_ming_xuande_zhengtong", "Emperors Xuande (Zhu Zhanji) & Zhengtong / Tianshun of Ming (1425–1464 CE)", "chinese", 20, "1399–1464 CE", "Ming Dynasty Emperors", ["History of Ming"], "Grandson & great-grandson of Emperor Yongle; patronized Zheng He's final voyage."),
        N("chn11_ming_wanli", "Emperor Wanli / Zhu Yijun (48-Year Ming Reign, r. 1572–1620 CE; Hosted Matteo Ricci)", "chinese", 21, "1563–1620 CE", "14th Emperor of Ming Dynasty", ["History of Ming", "Du Halde 1738"], "Longest-reigning Ming emperor; sent armies to defend Joseon Korea in the Imjin War.", True),
        N("chn11_ming_chongzhen", "Emperor Chongzhen / Zhu Youjian (17th & Final Ming Emperor of Beijing, d. 1644 CE)", "chinese", 21, "1611–1644 CE", "Last Ming Emperor", ["History of Ming"], "Grandson of Wanli; died in 1644 CE as Manchu Qing entered Beijing."),
        N("chn11_qing_yongzheng", "Emperor Yongzheng / Yinzhen (4th Son of Kangxi; Father of Qianlong, r. 1722–1735 CE)", "chinese", 21, "1678–1735 CE", "Qing Emperor", ["Draft History of Qing", "Du Halde 1738"], "Son of Kangxi & father of Qianlong."),
        N("chn11_qing_jiaqing_guangxu", "Qing Emperors Jiaqing, Daoguang, Xianfeng, Tongzhi & Guangxu (1796–1908 CE)", "chinese", 21, "1760–1908 CE", "Late Qing Emperors", ["Draft History of Qing"], "Late 19th-century Qing emperors ruling under Empress Dowager Cixi prior to Puyi."),
    ]
    edges += [
        E("eas5_song_taizu", "chn11_song_renzong_gaozong", "direct", "Song imperial line to Renzong & Southern Song Gaozong"),
        E("chn11_song_renzong_gaozong", "chn11_yelv_abaoji_liao", "expansion", "Song–Liao 1004 Chanyuan Treaty imperial contemporaries"),
        E("chn11_yelv_abaoji_liao", "chn11_aguda_jin", "expansion", "Liao -> Jurchen Jin imperial transition"),
        E("eas5_ming_yongle", "chn11_ming_xuande_zhengtong", "direct", "Grandson Xuande & great-grandson Zhengtong"),
        E("chn11_ming_xuande_zhengtong", "chn11_ming_wanli", "direct", "Ming imperial descent to Emperor Wanli"),
        E("chn11_ming_wanli", "chn11_ming_chongzhen", "direct", "Grandfather-to-grandson Ming succession to 1644 CE"),
        E("eas5_qing_qianlong", "chn11_qing_yongzheng", "direct", "Father of Emperor Qianlong"),
        E("eas5_qing_qianlong", "chn11_qing_jiaqing_guangxu", "direct", "Son Jiaqing -> Daoguang -> Xianfeng -> Guangxu"),
        E("chn11_qing_jiaqing_guangxu", "chr6_empress_dowager_cixi", "direct", "Consort Xianfeng & aunt-regent Empress Dowager Cixi"),
    ]

    # =========================================================================
    # SECTION C: SOUTH & SE ASIAN MONARCHS + LIVING 2026 ASIAN CROWNS (20 nodes)
    # =========================================================================
    add_chain(nodes, edges, "mon_isl_mahmud_ghazni", [
        ("asi11_qutb_iltutmish", "Sultans Qutb al-Din Aibak & Shams ad-Din Iltutmish (Founders of Delhi Sultanate, 1206–1236 CE)", 20, "1150–1236 CE", "Mamluk Sultans of Delhi"),
        ("asi11_razia_sultana", "Sultana Razia al-Din (First & Only Woman Sultan of Delhi, r. 1236–1240 CE)", 20, "1205–1240 CE", "Sovereign Sultana of Delhi", "Daughter of Sultan Iltutmish designated above her brothers as sovereign ruler of Delhi.", True),
        ("asi11_alauddin_khalji", "Sultan Alauddin Khalji (Repelled Mongol Invasions, r. 1296–1316 CE)", 20, "c. 1266–1316 CE", "Sultan of Delhi"),
        ("asi11_tughluq_ibn_battuta", "Sultan Muhammad bin Tughluq (Appointed Ibn Battuta Chief Qadi of Delhi, r. 1325–1351 CE)", 20, "c. 1290–1351 CE", "Sultan of Delhi"),
        ("asi11_sher_shah_suri", "Emperor Sher Shah Suri (Built Grand Trunk Road & Rupee Currency, r. 1540–1545 CE)", 21, "1486–1545 CE", "Emperor of North India (Sur)", "Defeated Humayun and reorganized North Indian administration & currency.", True),
    ], "vedic", "13th–16th c. CE", ["Ferishta History of Hindostan", "Ibn Battuta"], default_type="expansion")
    edges.append(E("asi11_tughluq_ibn_battuta", "isl10_ibn_battuta", "expansion", "1334–1341 CE Court of Muhammad bin Tughluq & Ibn Battuta in Delhi"))

    nodes += [
        N("asi11_nizam_asaf_jah1", "Nizam-ul-Mulk Asaf Jah I (Founder of Hyderabad Nizams, 1724–1748 CE)", "vedic", 21, "1671–1748 CE", "1st Nizam of Hyderabad", ["Mughal & Deccan Chronicles"], "Mughal governor under Aurangzeb who founded the Asaf Jahi dynasty."),
        N("asi11_hyder_ali_tipu_sultan", "Sultan Hyder Ali & Tipu Sultan ('Tiger of Mysore', r. 1761–1799 CE)", "vedic", 21, "1720–1799 CE", "Sultans of Mysore", ["Mysore Chronicles"], "Modernizing South Indian sovereigns who allied with France against British rule.", True),
        N("asi11_rani_lakshmibai", "Maharani Lakshmibai of Jhansi (Queen of Jhansi, 1828–1858 CE)", "vedic", 21, "1828–1858 CE", "Rani of Jhansi", ["Indian Chronicles"], "Born Manikarnika Tambe in a Maratha Peshwa court family; central heroine of 1857.", True),
    ]
    edges += [
        E("mon_mug_aurangzeb_ind", "asi11_nizam_asaf_jah1", "expansion", "Mughal Deccan Viceroy appointed under Aurangzeb"),
        E("asi11_nizam_asaf_jah1", "asi11_hyder_ali_tipu_sultan", "expansion", "18th c. South Indian sovereigns of Hyderabad & Mysore"),
        E("ind9_shahu_baji_rao1", "asi11_rani_lakshmibai", "expansion", "Maratha Bithoor/Peshwa court lineage & Jhansi sovereignty"),
    ]

    add_chain(nodes, edges, "ind_raj_mewar_sisodia", [
        ("asi11_prithvi_narayan_nepal", "King Prithvi Narayan Shah (Unifier of Kingdom of Nepal, 1743–1775 CE)", 21, "1723–1775 CE", "Founder of Modern Nepal"),
        ("asi11_tribhuvan_birendra_nepal", "Kings Tribhuvan, Mahendra, Birendra & Gyanendra of Nepal (Shah Dynasty, 1911–2008 CE)", 21, "1906–Present CE", "Shah Kings of Nepal"),
    ], "vedic", "18th–21st c. CE", ["Nepalese Royal Chronicles (Mewar Sisodia Descent)"], default_type="expansion")

    add_chain(nodes, edges, "tib8_fifth_dalai_lama", [
        ("asi11_ugyen_wangchuck_bhutan", "Druk Gyalpo Ugyen Wangchuck (1st Hereditary King of Bhutan, r. 1907–1926 CE)", 21, "1862–1926 CE", "1st Dragon King of Bhutan"),
        ("asi11_bhutan_jigme_khesar_2026", "LIVING (2026): King Jigme Khesar Namgyel Wangchuck of Bhutan (5th Druk Gyalpo)", 22, "1980–Present CE", "Reigning King of Bhutan (Living 2026)", "Present-day Dragon King of Bhutan descended from Drukpa Tibetan spiritual-noble houses.", True),
    ], "vedic", "1907–2026 CE", ["Bhutanese Royal Chronicles"], default_type="expansion")

    add_chain(nodes, edges, "unb_sea_mongkut_chulalongkorn", [
        ("asi11_rama6_rama7", "Kings Vajiravudh (Rama VI), Prajadhipok (Rama VII) & Ananda Mahidol (Rama VIII)", 21, "1881–1946 CE", "Chakri Kings of Thailand"),
        ("asi11_bhumibol_rama9", "King Bhumibol Adulyadej the Great (Rama IX, r. 1946–2016 CE)", 21, "1927–2016 CE", "9th Chakri King of Thailand", "Reigned 70 years as constitutional monarch of Thailand.", True),
        ("asi11_thailand_rama10_2026", "LIVING (2026): King Maha Vajiralongkorn (Rama X) of Thailand", 22, "1952–Present CE", "Reigning King of Thailand (Living 2026)", "Present-day reigning Chakri monarch of Thailand (2026).", True),
    ], "southeast_asia", "1910–2026 CE", ["Royal Chronicles of Siam & Thailand"])

    add_chain(nodes, edges, "unb_sea_jayavarman7", [
        ("asi11_norodom_sihanouk", "King Norodom → King Norodom Sihanouk of Cambodia (1834–2012 CE)", 21, "1834–2012 CE", "Norodom Kings of Cambodia"),
        ("asi11_cambodia_sihamoni_2026", "LIVING (2026): King Norodom Sihamoni of Cambodia", 22, "1953–Present CE", "Reigning King of Cambodia (Living 2026)", "Present-day reigning monarch of Cambodia continuing Angkor-Khmer royal heritage.", True),
    ], "southeast_asia", "1860–2026 CE", ["Cambodian Royal Chronicles"], default_type="expansion")

    add_chain(nodes, edges, "chr6_sultan_mahmud_shah", [
        ("asi11_bolkiah_golden_age", "Sultan Bolkiah (5th Sultan of Brunei, 'Golden Age', r. 1485–1524 CE)", 21, "1485–1524 CE", "5th Sultan of Brunei"),
        ("asi11_brunei_hassanal_bolkiah_2026", "LIVING (2026): Sultan Hassanal Bolkiah of Brunei (29th Sultan, r. 1967–Present)", 22, "1946–Present CE", "Reigning Sultan of Brunei (Living 2026)", "One of the longest-reigning monarchs in world history, continuing the Brunei royal line since Muhammad Shah.", True),
    ], "southeast_asia", "1485–2026 CE", ["Salasilah Raja-Raja Brunei"], default_type="expansion")
    nodes.append(N("asi11_malaysia_yang_di_pertuan_2026", "LIVING (2026): Sultan Ibrahim of Johor (17th Yang di-Pertuan Agong / King of Malaysia)", "southeast_asia", 22, "1958–Present CE", "Reigning King of Malaysia (Living 2026)", ["Johor & Malacca Royal Chronicles"], "Reigning King of Malaysia (2024–present) from the House of Temenggong / Johor-Malacca continuity.", True))
    edges.append(E("chr6_sultan_mahmud_shah", "asi11_malaysia_yang_di_pertuan_2026", "expansion", "Malacca–Johor Sultanate royal continuity to Living 2026 King of Malaysia"))

    # =========================================================================
    # SECTION D: ARABIAN GULF & MIDDLE EAST LIVING 2026 MONARCHIES (14 nodes)
    # =========================================================================
    add_chain(nodes, edges, "bib_ishmael", [
        ("ara11_muhammad_ibn_saud", "Imam Muhammad ibn Saud (Founder of First Saudi State at Diriyah, 1744–1765 CE)", 21, "1687–1765 CE", "Founder of House of Saud"),
        ("ara11_abdulaziz_ibn_saud", "King Abdulaziz ibn Saud (Founder of Kingdom of Saudi Arabia, 1932–1953 CE)", 21, "1875–1953 CE", "1st King of Saudi Arabia", "Unified Nejd and Hejaz into the modern Kingdom of Saudi Arabia.", True),
        ("ara11_king_faisal_saud", "Kings Saud, Faisal, Khalid, Fahd & Abdullah of Saudi Arabia (1953–2015 CE)", 21, "1902–2015 CE", "Kings of Saudi Arabia"),
        ("ara11_saudi_salman_mbs_2026", "LIVING (2026): King Salman bin Abdulaziz & Crown Prince Mohammed bin Salman (Saudi Arabia)", 22, "1935–Present CE", "Reigning King & Crown Prince of Saudi Arabia (Living 2026)", "Present-day Al Saud monarchs in 2026.", True),
    ], "arabian", "1744–2026 CE", ["Al Saud Najdi Chronicles"], default_type="expansion")

    add_chain(nodes, edges, "afr10_seyyid_said_zanzibar", [
        ("ara11_sultan_qaboos_oman", "Sultan Said bin Taimur → Sultan Qaboos bin Said of Oman (Al Bu Said, 1932–2020 CE)", 21, "1940–2020 CE", "Sultans of Oman"),
        ("ara11_oman_haitham_2026", "LIVING (2026): Sultan Haitham bin Tariq of Oman (Al Bu Said Dynasty)", 22, "1955–Present CE", "Reigning Sultan of Oman (Living 2026)", "Cousin of Sultan Qaboos & direct Al Bu Said descendant of Sayyid Said bin Sultan.", True),
    ], "arabian", "1932–2026 CE", ["Omani Al Bu Said Chronicles"])

    nodes += [
        N("ara11_sheikh_zayed_uae", "Sheikh Zayed bin Sultan Al Nahyan (Founder of the United Arab Emirates, 1918–2004 CE)", "arabian", 21, "1918–2004 CE", "Founding Father of the UAE", ["Bani Yas / Al Nahyan Chronicles"], "Bani Yas Al Nahyan ruler of Abu Dhabi & founding President of the UAE (1971).", True),
        N("ara11_uae_mbz_2026", "LIVING (2026): Sheikh Mohamed bin Zayed Al Nahyan & Sheikh Mohammed bin Rashid (UAE)", "arabian", 22, "1961–Present CE", "Living 2026 UAE Royal Rulers", ["Al Nahyan & Al Maktoum Chronicles"], "Present-day hereditary rulers of Abu Dhabi & Dubai leading the UAE in 2026."),
        N("ara11_jassim_al_thani", "Sheikh Jassim bin Mohammed Al Thani (Founder of Modern Qatar, c. 1825–1913 CE)", "arabian", 21, "c. 1825–1913 CE", "Founder of Qatar (Al Thani)", ["Al Thani Chronicles (Banu Tamim)"], "Mudar-Adnanite Banu Tamim lineage founding Qatar."),
        N("ara11_qatar_tamim_2026", "LIVING (2026): Emir Sheikh Tamim bin Hamad Al Thani of Qatar", "arabian", 22, "1980–Present CE", "Reigning Emir of Qatar (Living 2026)", ["Al Thani Chronicles"], "Present-day reigning Emir of the State of Qatar."),
        N("ara11_kuwait_al_sabah_2026", "LIVING (2026): Sheikh Sabah al-Ahmad → Emir Mishal al-Ahmad Al-Sabah of Kuwait (Utub)", "arabian", 22, "1940–Present CE", "Reigning Emir of Kuwait (Living 2026)", ["Al-Sabah Utub Chronicles"], "Reigning Al-Sabah Emir continuing the 1752 Bani Utbah house of Kuwait."),
        N("ara11_bahrain_al_khalifa_2026", "LIVING (2026): King Hamad bin Isa Al Khalifa & Crown Prince Salman of Bahrain (Utub)", "arabian", 22, "1950–Present CE", "Reigning King of Bahrain (Living 2026)", ["Al Khalifa Utub Chronicles"], "Reigning Al Khalifa monarch continuing since 1783 CE."),
        N("ara11_king_faisal1_iraq", "King Faisal I of Iraq & Syria (3rd Son of Sharif Hussein of Mecca, 1885–1933 CE)", "arabian", 21, "1885–1933 CE", "Hashemite King of Syria & Iraq", ["Hashemite Chronicles"], "Brother of King Abdullah I of Jordan; first Hashemite king of Iraq."),
        N("ara11_king_faisal2_iraq", "Kings Ghazi & Faisal II of Iraq (1912–1958 CE)", "arabian", 21, "1935–1958 CE", "Hashemite Kings of Iraq", ["Hashemite Chronicles"], "Son & grandson of King Faisal I; cousin to King Hussein of Jordan."),
    ]
    edges += [
        E("ara11_muhammad_ibn_saud", "ara11_sheikh_zayed_uae", "expansion", "Arabian Peninsula Anazzah / Adnanite royal neighbors"),
        E("ara11_sheikh_zayed_uae", "ara11_uae_mbz_2026", "direct", "Father-to-son Al Nahyan succession (UAE 2026)"),
        E("ara11_muhammad_ibn_saud", "ara11_jassim_al_thani", "expansion", "Adnanite Tamim–Anazzah Gulf royal houses"),
        E("ara11_jassim_al_thani", "ara11_qatar_tamim_2026", "direct", "Al Thani succession to Living Emir Tamim (2026)"),
        E("ara11_muhammad_ibn_saud", "ara11_kuwait_al_sabah_2026", "expansion", "Bani Utbah / Anazzah royal house of Kuwait"),
        E("ara11_kuwait_al_sabah_2026", "ara11_bahrain_al_khalifa_2026", "cognate", "Sister Bani Utbah houses (Al-Sabah & Al Khalifa)"),
        E("mod_abdullah2_hussein_iman", "ara11_king_faisal1_iraq", "expansion", "Brother of King Abdullah I of Jordan (Sons of Sharif Hussein)"),
        E("ara11_king_faisal1_iraq", "ara11_king_faisal2_iraq", "direct", "Hashemite Kings of Iraq"),
    ]

    # =========================================================================
    # SECTION E: ANCIENT NEAR EAST & CLASSICAL MISSING MONARCHS (10 nodes)
    # =========================================================================
    nodes += [
        N("anc11_antiochus1_commagene", "King Antiochus I Theos of Commagene (Nemrut Dağı; Dual Persian-Macedonian Descent, 70–31 BCE)", "greek", 18, "c. 86–31 BCE", "King of Commagene", ["Nemrut Dağı Inscriptions", "Josephus"], "Carved colossal twin ancestor galleries tracing his father directly to Darius I and his mother Laodice VII directly to Seleucus & Alexander's world.", True),
        N("anc11_vaballathus_palmyra", "Emperor Vaballathus of Palmyra (Son of Queen Zenobia & Odenathus, r. 267–272 CE)", "greek", 19, "259–273 CE", "Palmyrene Augustus", ["Historia Augusta", "Zosimus"], "Co-ruled the Palmyrene Empire with his mother Zenobia."),
        N("anc11_karibil_watar_saba", "Mukarrib Karib'il Watar of Saba (Contemporary of Sennacherib, c. 685 BCE)", "arabian", 16, "c. 685 BCE", "Great Mukarrib of Saba (Sheba)", ["Sabaic Sirwah Inscription RES 3945", "Assyrian Annals"], "Sovereign of South Arabian Saba who exchanged diplomatic gifts with Sennacherib of Assyria.", True),
        N("anc11_queen_gudit_ethiopia", "Queen Gudit / Yodit of Ethiopia (10th c. CE Post-Aksumite Warrior Queen)", "african", 20, "10th c. CE", "Queen of Damot / Aksum", ["Kebra Nagast Traditions", "History of the Patriarchs"], "Ended Aksumite era prior to the Zagwe dynasty of Lalibela."),
        N("anc11_evagoras_cyprus", "King Evagoras I of Salamis (Cyprus; Teucrid House of Ajax, 411–374 BCE)", "greek", 18, "c. 435–374 BCE", "King of Salamis in Cyprus", ["Isocrates Evagoras", "Diodorus"], "Greek-Cypriot king descended from Teucer (brother of Telamonian Ajax)."),
        N("anc11_tabnit_eshmunazar2_sidon", "Kings Tabnit & Eshmunazar II of Sidon (5th c. BCE Phoenician Royal Sarcophagi)", "levant_egypt", 17, "5th c. BCE", "Kings of Sidon", ["Eshmunazar II Sarcophagus (KAI 14)", "Records of the Past"], "Phoenician Sidonian kings granted Dor & Joppa by the Persian Great King."),
        N("anc11_abgar5_edessa", "King Abgar V Ukkama & Queen Helena Contemporary of Edessa / Osroene (r. 4 BCE–50 CE)", "biblical", 19, "r. 4 BCE–50 CE", "King of Osroene (Edessa)", ["Eusebius Church History I.13", "Syriac Chronicles"], "Early Syriac-Armenian ruler of Edessa linked to Adiabene & Armenia."),
        N("anc11_mausolus_artemisia2", "Satrap-King Mausolus & Queen Artemisia II (+ Queen Ada of Caria; Adoptive Mother of Alexander)", "greek", 18, "d. 353 BCE", "Hecatomnid Rulers of Caria", ["Diodorus", "Arrian Anabasis"], "Builders of the Mausoleum at Halicarnassus; sister Ada adopted Alexander the Great."),
        N("anc11_ariarathes_cappadocia", "Kings Ariarathes I → Ariarathes V of Cappadocia (Persian-Hellenistic Royal Line, 331–130 BCE)", "iranian", 18, "331–130 BCE", "Kings of Cappadocia", ["Diodorus Book XXXI", "Justin"], "Cappadocian kings claiming Achaemenid descent and intermarrying with Seleucids & Pontus."),
        N("anc11_prusias_nicomedes_bithynia", "Kings Zipoetes I, Prusias I & Nicomedes IV of Bithynia (326–74 BCE)", "greek", 18, "326–74 BCE", "Kings of Bithynia", ["Polybius", "Appian"], "Anatolian Hellenistic kings allied with Macedon, Pontus & Rome."),
    ]
    edges += [
        E("per4_achaemenes", "anc11_antiochus1_commagene", "expansion", "Nemrut Dagi Royal Pedigree: Paternal descent from Darius I of Persia"),
        E("grk_alexander", "anc11_antiochus1_commagene", "expansion", "Nemrut Dagi Royal Pedigree: Maternal Seleucid-Macedonian descent"),
        E("anc11_antiochus1_commagene", "jos_iotape_commagene", "direct", "Commagene royal descent to Princess Iotape (married into Herodians)"),
        E("pal_odenathus_zenobia", "anc11_vaballathus_palmyra", "direct", "Son & co-ruler of Queen Zenobia & King Odenathus"),
        E("eth_menelik", "anc11_karibil_watar_saba", "expansion", "South Arabian Saba–Aksumite Sabaean royal horizon"),
        E("anc11_karibil_watar_saba", "ar4_sayf_ibn_dhi_yazan", "expansion", "Ancient Sabaic -> Himyarite South Arabian royal continuity"),
        E("mon_eth_ezana", "anc11_queen_gudit_ethiopia", "expansion", "Late Aksumite transition to Queen Gudit & Zagwe dynasty"),
        E("anc11_queen_gudit_ethiopia", "mon_eth_lalibela", "expansion", "10th–12th c. Post-Gudit Zagwe restoration"),
        E("grkr_b3_ajax", "anc11_evagoras_cyprus", "expansion", "Teucrid royal house of Salamis descended from Teucer (brother of Ajax)"),
        E("cls3_pygmalion", "anc11_tabnit_eshmunazar2_sidon", "expansion", "Phoenician Sidon–Tyre royal continuity"),
        E("cls3_tigranes2_great", "anc11_abgar5_edessa", "expansion", "Armenian–Osroene royal kinship of Edessa"),
        E("grk_alexander", "anc11_mausolus_artemisia2", "expansion", "334 BCE: Carian Queen Ada (sister of Mausolus) adopted Alexander the Great"),
        E("per4_achaemenes", "anc11_ariarathes_cappadocia", "expansion", "Achaemenid-derived Cappadocian royal house"),
        E("cls_pontus_mithridates", "anc11_ariarathes_cappadocia", "expansion", "Pontic–Cappadocian royal marriages"),
        E("cls_pontus_mithridates", "anc11_prusias_nicomedes_bithynia", "expansion", "Pontus–Bithynia Black Sea royal rivals & allies"),
    ]

    return {
        "module": "53_wave11_global_monarchs_queens_and_dynasties",
        "title": "Wave 11: Global Monarchs, Queens & Living 2026 Crowns (Austria-Hungary, Balkans, China, South/SE Asia, Arabian Gulf & ANE)",
        "nodes": nodes,
        "edges": edges,
    }
