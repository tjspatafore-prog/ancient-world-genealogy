"""
Module 22: Complete East Asian & Eurasian Steppe Chronicles —
1. China: Pre-Dynastic Emperors, ALL 17 Xia Kings, ALL 30 Shang/Yin Kings, ALL 34 Western & Eastern Zhou Kings
   (James Legge, The Chinese Classics Vol. III: Shoo King & Annals of the Bamboo Books).
2. Japan: 7 Heavenly Kami Generations, 5 Earthly Kami Generations, ALL 25 Emperors of Nihongi Vol. I
   (Jimmu through Buretsu + Empress Jingo + Yamato Takeru) & Ancestral Clans (Nakatomi, Imibe, Mononobe, Ohotomo, Soga)
   (W.G. Aston, Nihongi Vol. I).
3. Mongols: Complete 22-Generation Borjigin Genealogy from Börte Čino & Qo'ai Maral through Alan Qo'a,
   Bodončar, Qabul Qa'an, Yisügei, Činggis Qa'an (Genghis Khan) to Batu, Güyük, Möngke & Qubilai Qa'an
   (Igor de Rachewiltz, The Secret History of the Mongols).
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. CHINA: ALL 17 XIA, ALL 30 SHANG, ALL 34 ZHOU KINGS (Legge Vol. III / Bamboo Books)
    # -------------------------------------------------------------------------
    nodes += [
        N("chn_xia_complete", "Complete Xia Dynasty (All 17 Kings, Bamboo Books): Yu → Qi → Tai Kang → Zhong Kang → Xiang → Shao Kang → Zhu → Huai → Mang → Xie → Bu Jiang → Jiong → Jin → Kong Jia → Gao → Fa → Jie", "chinese", 8, "c. 1989-1557 BCE (Bamboo Books Part III; Shoo King)",
          "First Hereditary Dynasty of China (17 Kings, 432-471 yrs)", ["Legge Chinese Classics Vol. III (Proleg. pp. 117-127; Shoo pp. 160-171)"],
          "Complete father-son & brother succession from Yu the Great (son of Gun) through the usurpation of Hou Yi & Han Zhuo, restoration by posthumous son Shao Kang (+ Empress Min), 59-yr reign of Bu Jiang, and final tyrant Jie (overthrown by Tang of Shang).",
          ["17 Xia Kings", "Empress Min", "Tyrant Jie"], major=True),
        N("chn_shang_complete", "Complete Shang / Yin Dynasty (All 30 Kings, Bamboo Books): Tang → Tai Jia → Tai Wu → Zu Yi → Pan Geng → Wu Ding → Zu Jia → Wen Ding → Di Yi → Di Xin (King Zhou)", "chinese", 11, "c. 1557-1049 BCE (Bamboo Books Part IV; Shoo King)",
          "Oracle-Bone Bronze Age Dynasty (30 Kings Including Tang, Pan Geng & Wu Ding)", ["Legge Chinese Classics Vol. III (Proleg. pp. 128-141; Shoo pp. 193-278)"],
          "Descended from Emperor Ku & Jiandi -> Xie (13 generations to Tang the Victorious). Features lateral brother-to-brother succession (e.g., 4 brothers Yang Jia -> Pan Geng -> Xiao Xin -> Xiao Yi!), Pan Geng's move to Yin, Wu Ding's 59-yr golden age, and Di Xin's fall at Muye to King Wu of Zhou.",
          ["30 Shang Kings", "Pan Geng", "Tai Wu", "Wu Ding"], major=True),
        N("chn_zhou_western_eastern", "Complete Zhou Dynasty (All 34 Kings, Bamboo Books): Pre-Dynastic (Hou Ji → Danfu → King Wen) → 12 Western Zhou (King Wu → Cheng → Kang → Mu → Li → Xuan → You) → 22 Eastern Zhou (King Ping → King Nan)", "chinese", 14, "1049-256 BCE (Bamboo Books Part V, Proleg. pp. 142-183)",
          "Longest Dynasty in Chinese History (Mandate of Heaven, Spring & Autumn, Warring States)", ["Legge Chinese Classics Vol. III (Proleg. pp. 142-183)"],
          "From Emperor Ku & Jiang Yuan -> Hou Ji -> Gong Liu -> Old Duke Danfu (King Tai) -> Jili -> King Wen -> King Wu & Duke of Zhou -> 12 Western Zhou kings (ending when King You fell in 771 BCE) -> 22 Eastern Zhou kings at Luoyang (Ping through King Nan, era of Confucius & Laozi!).",
          ["Danfu / King Tai", "King Mu of Zhou", "King Ping", "King Nan"], major=True),
        N("chn_han_tang_empires", "Imperial China Dynastic Bridges: Han Dynasty (Liu Bang / Gaozu → Emperor Wu / Han Wudi; Sima Qian) & Tang Dynasty (Li Yuan → Taizong → Empress Wu Zetian)", "chinese", 19, "202 BCE – 907 CE (Shiji; Anderson 1732 Tables 161-162)",
          "Classical Imperial Silk Road Dynasties Connecting China to Parthia, India & Rome", ["Sima Qian Shiji", "Anderson 1732 Tables 161-162"],
          "Han Gaozu (Liu Bang) founded the 400-year Han Dynasty; Han Wudi opened the Silk Road via Zhang Qian to Fergana/Bactria/Parthia (and court historian Sima Qian wrote the Shiji!). Tang Taizong & Wu Zetian presided over cosmopolitan Chang'an.",
          ["Liu Bang / Han Gaozu", "Emperor Wu of Han", "Sima Qian", "Tang Taizong", "Empress Wu Zetian"], major=True),
    ]

    add_roster(nodes, edges, "chn_xia_complete", "chnr_xia", "chinese", 8, "c. 1989-1557 BCE (Bamboo Books)", "Xia Dynasty King", ["Bamboo Books (Legge Vol. III pp. 117-127)"], [
        "1. Yu the Great (Hea-how)", "2. Qi / K'e (Son of Yu)", "3. Tai Kang (Eldest Son of Qi)", "4. Zhong Kang (Brother of Tai Kang)",
        "5. Xiang / Seang (Son of Zhong Kang)", "6. Shao Kang (Posthumous Son of Xiang & Empress Min)", "7. Zhu / Ch'oo (Son of Shao Kang)",
        "8. Huai / Fun (Son of Zhu, 44 yrs)", "9. Mang (Son of Huai, 58 yrs)", "10. Xie / Seëh (Son of Mang)", "11. Bu Jiang (Son of Xie, 59 yrs)",
        "12. Jiong / Keung (Brother of Bu Jiang)", "13. Jin / Kin (Son of Jiong)", "14. Kong Jia (Son of Bu Jiang)",
        "15. Gao / Haou (Son of Kong Jia)", "16. Fa / Fah (Son of Gao)", "17. Jie / Kwei (Son of Fa, Last Xia King)"
    ], edge_type="direct", edge_label="Xia Dynasty Succession (Bamboo Books)")

    add_roster(nodes, edges, "chn_shang_complete", "chnr_shg", "chinese", 11, "c. 1557-1049 BCE (Bamboo Books)", "Shang / Yin Dynasty King", ["Bamboo Books (Legge Vol. III pp. 128-141)"], [
        "1. Tang the Victorious / Da Yi", "2. Wai Bing (Son of Tang)", "3. Zhong Ren (Son of Tang)", "4. Tai Jia (Grandson of Tang via Tai Ding)",
        "5. Wo Ding (Son of Tai Jia)", "6. Tai Geng / Xiao Geng (Brother of Wo Ding)", "7. Xiao Jia (Son of Tai Geng)", "8. Yong Ji (Brother of Xiao Jia)",
        "9. Tai Wu / Tai-tsung (Brother of Yong Ji, 75 yrs)", "10. Zhong Ding (Son of Tai Wu)", "11. Wai Ren (Brother of Zhong Ding)",
        "12. He Dan Jia (Brother of Wai Ren)", "13. Zu Yi (Son of He Dan Jia)", "14. Zu Xin (Son of Zu Yi)", "15. Wo Jia / K'ae-keah (Brother of Zu Xin)",
        "16. Zu Ding (Son of Zu Xin)", "17. Nan Geng (Son of Wo Jia)", "18. Yang Jia (Son of Zu Ding)", "19. Pan Geng (Moved to Yin, 28 yrs)",
        "20. Xiao Xin (Brother of Pan Geng)", "21. Xiao Yi (Brother of Xiao Xin)", "22. Wu Ding / Gaozong (Son of Xiao Yi, 59 yrs)",
        "23. Zu Geng (Son of Wu Ding)", "24. Zu Jia (Brother of Zu Geng, 33 yrs)", "25. Lin Xin / Fung-sin (Son of Zu Jia)",
        "26. Geng Ding (Brother of Lin Xin)", "27. Wu Yi (Son of Geng Ding)", "28. Wen Ding / Tai Ding (Son of Wu Yi)",
        "29. Di Yi (Son of Wen Ding)", "30. Di Xin / King Zhou (+ Daji, Last Shang King)"
    ], edge_type="direct", edge_label="Shang Dynasty Succession (Bamboo Books)")

    add_roster(nodes, edges, "chn_zhou_western_eastern", "chnr_zho", "chinese", 15, "1049-256 BCE (Bamboo Books)", "Zhou Dynasty King", ["Bamboo Books (Legge Vol. III pp. 142-183)"], [
        "Danfu / Old Duke King Tai (Pre-Dynastic)", "Jili / King Ji (+ Tai Ren)", "1. King Wu / Fa (Conqueror of Shang)",
        "2. King Cheng / Sung (37 yrs)", "3. King Kang / Ch'aou (26 yrs)", "4. King Zhao / Hea", "5. King Mu / Mwan (55 yrs)",
        "6. King Gong / E", "7. King Yi / Keen", "8. King Xiao / Peih-fang", "9. King Yi / Seë", "10. King Li / Hoo (Gonghe Regency)",
        "11. King Xuan / Tsing (46 yrs)", "12. King You / Neë (End of Western Zhou, 771 BCE)", "13. King Ping / E-k'ew (1st Eastern Zhou, 51 yrs)",
        "14. King Huan", "15. King Zhuang", "16. King Xi", "17. King Hui", "18. King Xiang", "19. King Qing", "20. King Kuang",
        "21. King Ding", "22. King Jian", "23. King Ling", "24. King Jing / Kwei", "25. King Jing / K'ae", "26. King Yuan",
        "27. King Zhending", "28. King Kao", "29. King Weilie", "30. King An", "31. King Lie", "32. King Xian", "33. King Shenjing", "34. King Nan (Last Zhou King)"
    ], edge_type="direct", edge_label="Zhou Dynasty Succession (Bamboo Books)")

    # -------------------------------------------------------------------------
    # 2. JAPAN: NIHONGI KAMI GENERATIONS, ALL 25 EMPERORS (VOL I) & CLANS (Aston)
    # -------------------------------------------------------------------------
    nodes += [
        N("jpn_nihongi_7heaven_5earth", "Nihongi Kami Generations: 7 Heavenly Generations (Kuni-toko-tachi → Izanagi & Izanami) & 5 Earthly Generations (Amaterasu → Oshihomimi → Ninigi → Hiko-hoho-demi → Ugayafukiaezu)", "japan_korea", 3, "Age of the Gods (Nihongi Books I-II, Aston pp. 3-108)",
          "Complete Imperial Shinto Divine Pedigree Leading to Emperor Jimmu", ["Nihongi Vol. I Books I-II (Aston pp. 3-108)"],
          "Seven Heavenly Generations: 1. Kuni-toko-tachi, 2. Kuni-no-sa-tsuchi, 3. Toyo-kumu-nu, 4. Uhiji-ni & Suhiji-ni, 5. Oho-to-nochi & Oho-to-mahe, 6. Omo-taru & Kashiko-ne, 7. Izanagi & Izanami. Five Earthly Generations descend from Amaterasu & Taka-mi-musubi via Ninigi (+ Kono-hana-saku-ya-hime) & Hiko-hoho-demi (+ Sea-Princess Toyo-tama-hime) to Jimmu!",
          ["Kuni-toko-tachi", "Taka-mi-musubi", "Kono-hana-saku-ya-hime", "Ugayafukiaezu"]),
        N("jpn_nihongi_emperors_1_25", "Complete Nihongi Vol. I Imperial Line (1st Jimmu → 25th Buretsu + Empress Jingo): Unbroken Yamato Succession", "japan_korea", 17, "660 BCE – 506 CE Trad. (Nihongi Books III-XV, Aston pp. 109-407)",
          "First 25 Emperors of Japan + Regent Empress Jingo & Takechi no Sukune", ["Nihongi Vol. I Books III-XV (Aston pp. 109-407)"],
          "Complete father-son & brother succession from 1st Jimmu (Hime-tatara-Isuzu) through Suizei, Annei, Itoku, Kosho, Koan, Korei, Kogen, Kaika, Sujin, Suinin, Keiko (-> Yamato-dake), Seimu, Chuai + Regent Empress Jingo, Ojin, Nintoku (giant keyhole kofun tomb!), Richu, Hanzei, Ingyo, Anko, Yuryaku, Seinei, Kenzo, Ninken, and 25th Buretsu.",
          ["Nintoku Tenno", "Yuryaku Tenno", "Empress Jingo", "Yamato-dake"], major=True),
        N("jpn_ancestral_clans_nihongi", "Ancient Japanese Noble Clans (Nihongi): Nakatomi/Fujiwara (Ame-no-Koyane), Imibe (Futo-dama), Mononobe (Nigi-haya-hi), Ohotomo & Soga (Takechi no Sukune)", "japan_korea", 16, "Yamato Period (Nihongi Books I-XIV, Aston)",
          "Founding Aristocratic Houses of the Imperial Yamato Court", ["Nihongi Vol. I (Aston pp. 42, 128, 148, 190, 306)"],
          "Ame-no-Koyane -> Nakatomi (ancestors of the Fujiwara Regents!); Futo-dama -> Imibe priests; Heavenly deity Nigi-haya-hi -> Mononobe military clan; Michi-no-Omi -> Ohotomo guards; Emperor Kogen -> Takechi no Sukune (legendary 300-yr Prime Minister!) -> Soga no Manchi & Soga clan!",
          ["Ame-no-Koyane (Nakatomi/Fujiwara)", "Nigi-haya-hi (Mononobe)", "Takechi no Sukune (Soga)"]),
    ]

    add_roster(nodes, edges, "jpn_nihongi_emperors_1_25", "jpnr_emp", "japan_korea", 17, "Nihongi Books III-XV (Aston)", "Emperor / Empress of Japan", ["Nihongi Vol. I (Aston pp. 109-407)"], [
        "2. Suizei Tenno (Son of Jimmu & Hime-tatara-Isuzu)", "3. Annei Tenno (Son of Suizei)", "4. Itoku Tenno (Son of Annei)",
        "5. Kosho Tenno (Son of Itoku)", "6. Koan Tenno (Son of Kosho)", "7. Korei Tenno (Son of Koan)", "8. Kogen Tenno (Ancestor of Soga/Abe)",
        "9. Kaika Tenno (Son of Kogen)", "10. Sujin Tenno (First Historically Attested Yamato King)", "11. Suinin Tenno (Son of Sujin)",
        "12. Keiko Tenno (Father of Yamato-dake)", "13. Seimu Tenno (Son of Keiko)", "14. Chuai Tenno (Son of Yamato-dake)",
        "Empress Jingo (Regent, Great-Grandchild of Kaika)", "15. Ojin Tenno (Son of Chuai & Empress Jingo)",
        "16. Nintoku Tenno (Son of Ojin — Daisen Kofun)", "17. Richu Tenno (Eldest Son of Nintoku)", "18. Hanzei Tenno (Brother of Richu)",
        "19. Ingyo Tenno (Brother of Hanzei)", "20. Anko Tenno (Son of Ingyo)", "21. Yuryaku Tenno (5th Child of Ingyo)",
        "22. Seinei Tenno (Son of Yuryaku)", "23. Kenzo Tenno (Grandson of Richu)", "24. Ninken Tenno (Brother of Kenzo)",
        "25. Buretsu / Muretsu Tenno (Son of Ninken, End of Nihongi Vol. I)"
    ], edge_type="direct", edge_label="Imperial Yamato Succession (Nihongi Vol. I)")

    # -------------------------------------------------------------------------
    # 3. MONGOLS: COMPLETE 22-GENERATION BORJIGIN GENEALOGY (Secret History of the Mongols)
    # -------------------------------------------------------------------------
    mng_chain = [
        ("mng_borte_chino", "1. Börte Čino ('Blue-Grey Wolf') & Qo'ai Maral ('Fallow Doe')", 15, "c. 8th c. CE Mythic Origin (SHM §1)", "Heaven-Ordained Ancestors of the Mongol Borjigin Lineage", "Crossed the Tenggis Sea to Burqan Qaldun at the headwaters of the Onan River (Secret History of the Mongols §1, Rachewiltz p. 1).", {"major": True, "altNames": ["Börte Čino", "Qo'ai Maral"]}),
        ("mng_batachiqan_to_toroqoljin", "2–11. Batačiqan → Tamača → Qoričar Mergen → A'ujam Boro'ul → Sali Qača'u → Yeke Nidün → Sem Soči → Qarču → Borjigidai Mergen → Toroqoljin Bayan", 16, "Gens 2-11 (SHM §§1-3)", "Ten Ancestral Generations from Börte Čino to Dobun Mergen", "Borjigidai Mergen (+ Mongqoljin Qo'a) -> Toroqoljin Bayan (+ Boroqčin Qo'a), father of Du'a Soqor (Dörben clan) and Dobun Mergen.", {"altNames": ["Batačiqan", "Borjigidai Mergen", "Du'a Soqor"]}),
        ("mng_alan_qoa_bodonchar", "12–13. Dobun Mergen & Lady Alan Qo'a → Five Sons (Bügünütei, Belgünütei, Buqu Qatagi, Buqatu Salji & Bodončar Mungqaq)", 17, "c. 10th c. CE (SHM §§7-44)", "The Five Arrows Parable & Founder of the Borjigin Royal Clan", "Alan Qo'a (of Qori Tumat) taught her five sons unity using the famous parable of the five arrows. Her youngest son Bodončar Mungqaq (conceived by a radiant golden light!) founded the Borjigin clan — while his stepson Jajiradai became ancestor of Genghis Khan's blood-brother & rival Jamuqa!", {"major": True, "altNames": ["Alan Qo'a", "Bodončar Mungqaq", "Jamuqa (Jadaran Clan)"]}),
        ("mng_qabichi_qaidu_qabul", "14–18. Qabiči Ba'atur → Menen Tudun (7 Sons incl. Barulas!) → Qači Külük → Qaidu → Bai Šingqor Doqšin → Tumbinai Sečen → Qabul Qa'an (1st All-Mongol Qan!) & Ambaqai Qa'an → Bartan Ba'atur", 18, "c. 1000-1150 CE (SHM §§43-57)", "Khamag Mongol Khagans & Founder of the Barlas Clan (Ancestors of Timur!)", "Menen Tudun's sons Qači'u/Qačula founded the Barulas (Barlas) clan — later ancestors of Timur (Tamerlane) and the Mughal Emperors! Qabul Qa'an became 1st Khan of All Mongols; his sons included Qutula Qa'an and Bartan Ba'atur.", {"altNames": ["Menen Tudun (Barulas)", "Qaidu", "Qabul Qa'an", "Ambaqai Qa'an", "Qutula Qa'an"]}),
        ("mng_yesugei_hoelun", "19. Yisügei Ba'atur & Lady Hö'elün (Olqunu'ut) → Temüjin, Qasar, Qači'un, Temüge, Temülün (+ Bekter & Belgütei)", 18, "c. 1134-1171 CE (SHM §§50-68)", "Parents & Siblings of Genghis Khan", "Yisügei Ba'atur (poisoned by Tatars when Temüjin was 9) & fierce mother Lady Hö'elün raised Temüjin (born clutching a blood clot at Deli'ün Boldaq!), brothers Joči Qasar, Qači'un, Temüge Otčigin, sister Temülün, and half-brothers Bekter & Belgütei (by Mother Sučigil).", {"altNames": ["Yesügei", "Lady Hö'elün", "Joči Qasar", "Belgütei"]}),
        ("mng_genghis_khan_borte", "20. Temüjin / Činggis Qa'an (Genghis Khan, 1162–1227) & Empress Börte (Onggirat)", 19, "1162-1227 CE (SHM §§59-268)", "Founder of the Mongol Empire (Largest Contiguous Land Empire in History)", "Unified the Steppe in 1206 CE as Činggis Qa'an. With principal wife Lady Börte (plus Yisüi, Yisügen, Qulan & Ibaqa Beki) fathered the 4 Great Imperial Sons (Jöči, Ča'adai, Ögödei, Tolui) and 5 diplomat daughters (Qojin, Al Altun, Čečeyigen, Alaqa, Tümelün).", {"major": True, "altNames": ["Genghis Khan", "Temüjin", "Empress Börte"]}),
        ("mng_four_sons_grandsons", "21–22. The Four Great Houses: Jöči (→ Batu Khan, Golden Horde), Ča'adai (→ Büri), Ögödei Qa'an (+ Töregene → Güyük) & Tolui (+ Sorqaqtani Beki → Möngke Qa'an, Qubilai Qa'an / Kublai Khan & Hülegü Khan)", 19, "1227-1368 CE (SHM §§242-282, Rachewiltz Index)", "Great Khans of the Golden Horde, Chagatai, Yuan China & Ilkhanate Persia", "Tolui & Kereyit Christian princess Sorqaqtani Beki produced Möngke (4th Great Khan), Kublai Khan (founder of China's Yuan Dynasty, host of Marco Polo!), and Hülegü (founder of the Persian Ilkhanate). Jöči's son Batu founded the Golden Horde; Ögödei & Güyük ruled Karakorum!", {"major": True, "altNames": ["Jöči -> Batu Khan", "Ča'adai", "Ögödei -> Güyük", "Tolui & Sorqaqtani Beki", "Möngke", "Kublai Khan (Yuan)", "Hülegü"]}),
    ]
    add_chain(nodes, edges, mng_chain, start_parent="stp_xiongnu", start_edge_type="expansion",
              start_edge_label="Steppe Continuity -> Secret History of the Mongols (Borjigin Genealogy)",
              tradition="steppe", default_edge_type="direct", default_sources=["The Secret History of the Mongols (Rachewiltz)"])

    add_roster(nodes, edges, "mng_batachiqan_to_toroqoljin", "mngr_anc", "steppe", 16, "SHM Ch. 1 §§1-48", "Borjigin Ancestor", ["The Secret History of the Mongols (Rachewiltz §§1-48)"], [
        "Batačiqan (Gen 2)", "Tamača (Gen 3)", "Qoričar Mergen (Gen 4)", "A'ujam Boro'ul (Gen 5)", "Sali Qača'u (Gen 6)",
        "Yeke Nidün (Gen 7)", "Sem Soči (Gen 8)", "Qarču (Gen 9)", "Borjigidai Mergen (Gen 10)", "Toroqoljin Bayan (Gen 11)",
        "Du'a Soqor (Dörben Clan)", "Dobun Mergen (Gen 12)", "Bügünütei & Belgünütei", "Buqu Qatagi & Buqatu Salji",
        "Jajiradai -> Jamuqa (Jadaran Clan)", "Qabiči Ba'atur (Gen 14)", "Menen Tudun (Gen 15)", "Qači Külük & Mother Nomolun (Gen 16)",
        "Qaidu (Gen 17)", "Ambaqai Qa'an (Tayiči'ut)", "Bai Šingqor Doqšin (Gen 18)", "Tumbinai Sečen (Gen 19)",
        "Qabul Qa'an (1st All-Mongol Qan)", "Qutula Qa'an", "Bartan Ba'atur"
    ], edge_type="direct", edge_label="Borjigin Patrilineal Ancestor (SHM Ch. 1)")

    add_roster(nodes, edges, "mng_four_sons_grandsons", "mngr_imp", "steppe", 19, "1206-1368 CE (SHM)", "Chinggisid Imperial Prince / Princess", ["The Secret History of the Mongols (Rachewiltz)"], [
        "Jöči (Eldest Son of Genghis Khan)", "Batu Khan (Founder of Golden Horde)", "Ča'adai (2nd Son, Chagatai Khanate)",
        "Büri (Grandson of Ča'adai)", "Ögödei Qa'an (2nd Great Khan, + Töregene)", "Güyük Qa'an (3rd Great Khan)",
        "Prince Tolui (4th Son)", "Sorqaqtani Beki (Kereyit Princess, Mother of 3 Khans)", "Möngke Qa'an (4th Great Khan)",
        "Qubilai Qa'an / Kublai Khan (Founder of Yuan Dynasty)", "Hülegü Khan (Ilkhanate of Persia)", "Timur / Tamerlane (Barlas Clan -> Babur / Mughals)"
    ], edge_type="direct", edge_label="Chinggisid Imperial Descendant")

    edges += [
        E("chn_yu_xia", "chn_xia_complete", "direct", "All 17 Xia Kings from Yu to Jie (Legge Bamboo Books)"),
        E("chn_shang", "chn_shang_complete", "direct", "All 30 Shang/Yin Kings from Tang to Di Xin (Legge Bamboo Books)"),
        E("chn_zhou", "chn_zhou_western_eastern", "direct", "All 34 Western & Eastern Zhou Kings (Legge Bamboo Books)"),
        E("chn_boyi_qin", "chn_han_tang_empires", "expansion", "Qin -> Han Dynasty (Silk Road) -> Tang Dynasty"),
        E("jk_izanagi_amaterasu", "jpn_nihongi_7heaven_5earth", "direct", "Complete 7 Heavenly & 5 Earthly Kami Generations (Aston Nihongi)"),
        E("jk_jimmu", "jpn_nihongi_emperors_1_25", "direct", "Complete 1st–25th Emperors of Japan in Nihongi Vol. I"),
        E("jpn_nihongi_7heaven_5earth", "jpn_ancestral_clans_nihongi", "direct", "Heavenly Kami ancestors of Nakatomi, Imibe, Mononobe & Ohotomo clans"),
        E("mng_four_sons_grandsons", "chn_han_tang_empires", "cognate", "Kublai Khan establishes the Yuan Dynasty of China (1271 CE)"),
        E("dna_d_c_n_asia", "mng_genghis_khan_borte", "genetic", "Steppe Y-DNA Haplogroup C2b1a2 (Star-Cluster associated with Mongol/Steppe expansion)"),
    ]

    return {
        "module": "22_east_asia_bamboo_nihongi_mongols",
        "title": "Complete Chinese Xia/Shang/Zhou King Lists (Legge Bamboo Books), Nihongi Vol. I Kami & 25 Emperors (Aston), & Complete Secret History of the Mongols Borjigin Genealogy (Rachewiltz)",
        "nodes": nodes,
        "edges": edges,
    }
