"""
Module 47: Wave 5 Person-by-Person India (Epics, Maurya, Gupta, Tibet, Sri Lanka),
Imperial China & Korea, Abulghazi Turkic/Oghuz/Seljuk/Early Ottoman Stems,
Celtic Ireland/Scotland, Norse/Normandy, British Chronicles & Kievan Rus' Royal Marriages.
"""

from . import N, E


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    def chain(items, tradition, sources, edge_label, edge_type="direct", start_parent=None):
        prev = start_parent
        for it in items:
            if isinstance(it, str):
                prev = it
                continue
            nid, nm, tr, er, rl, nt, mj = it[0], it[1], it[2], it[3], it[4], it[5], it[6]
            nodes.append(N(nid, nm, tradition, tr, er, rl, sources, nt, major=mj))
            if prev:
                edges.append(E(prev, nid, edge_type, edge_label))
            prev = nid

    # =========================================================================
    # 1. INDIA (RAMAYANA, PANDAVAS, MAURYA, GUPTA), SRI LANKA & TIBET
    # =========================================================================
    nodes += [
        N("ind5_lord_rama", "Lord Rama / Sri Ramachandra (Gen 65, Son of Dasharatha; Hero of Ramayana)", "vedic", 9, "Treta Yuga (Valmiki Ramayana; Pargiter p. 147)", "7th Avatar & King of Ayodhya", ["Valmiki Ramayana", "Pargiter p. 147"], "Eldest son of King Dasharatha & Kausalya; husband of Sita; father of Lava & Kusha.", major=True),
        N("ind5_goddess_sita", "Goddess Sita / Janaki (Daughter of Siradhvaja Janaka; Queen of Ayodhya)", "vedic", 9, "Treta Yuga (Valmiki Ramayana)", "Princess of Videha & Mother of Lava and Kusha", ["Valmiki Ramayana"], "Daughter of King Siradhvaja Janaka; mother of twins Lava and Kusha."),
        N("ind5_bharata_ram", "Prince Bharata (Son of Dasharatha & Kaikeyi; Regent of Ayodhya)", "vedic", 9, "Valmiki Ramayana", "Younger Brother of Rama", ["Valmiki Ramayana"], "Ruled Ayodhya from Nandigrama bearing Rama's sandals during the 14-year exile."),
        N("ind5_lakshmana", "Prince Lakshmana (Son of Dasharatha & Sumitra; Companion of Rama)", "vedic", 9, "Valmiki Ramayana", "Twin Brother of Shatrughna", ["Valmiki Ramayana"], "Accompanied Rama & Sita throughout the 14-year forest exile."),
        N("ind5_shatrughna", "Prince Shatrughna (Son of Dasharatha & Sumitra; Founder of Mathura's Solar Line)", "vedic", 9, "Valmiki Ramayana", "Youngest Brother of Rama", ["Valmiki Ramayana"], "Conquered Lavana and founded Mathura."),
        N("ind5_lava", "King Lava of Shravasti (Twin Son of Rama & Sita; Ancestor of Mewar Sisodias)", "vedic", 10, "Treta/Dvapara Transition (Ramayana; Pargiter)", "Twin Prince of North Kosala & Lahore", ["Valmiki Ramayana"], "Traditional Solar ancestor of North Kosala / Shravasti and Mewar Rajputs."),
        N("ind5_kusha", "King Kusha of Kushavati (Twin Son of Rama & Sita; Ancestor of Brihadbala)", "vedic", 10, "Dvapara Yuga (Ramayana; Pargiter p. 149)", "Twin Prince Continuing Ayodhya Main Line", ["Valmiki Ramayana", "Pargiter p. 149"], "Father of Atithi, continuing the Ayodhya Solar Dynasty to Brihadbala."),
    ]
    edges += [
        E("indr_ay2_32_king_dasharatha_gen_64", "ind5_lord_rama", "direct", "Dasharatha -> eldest son Lord Rama"),
        E("indr_ay2_32_king_dasharatha_gen_64", "ind5_bharata_ram", "direct", "Dasharatha -> Bharata"),
        E("indr_ay2_32_king_dasharatha_gen_64", "ind5_lakshmana", "direct", "Dasharatha -> Lakshmana"),
        E("indr_ay2_32_king_dasharatha_gen_64", "ind5_shatrughna", "direct", "Dasharatha -> Shatrughna"),
        E("indr_ail_02_siradhvaja_janaka_father_of_", "ind5_goddess_sita", "direct", "Siradhvaja Janaka -> Sita"),
        E("ind5_lord_rama", "ind5_goddess_sita", "direct", "Marriage of Rama & Sita"),
        E("ind5_lord_rama", "ind5_lava", "direct", "Rama & Sita -> twin Lava"),
        E("ind5_goddess_sita", "ind5_lava", "direct", "Mother Sita -> Lava"),
        E("ind5_lord_rama", "ind5_kusha", "direct", "Rama & Sita -> twin Kusha"),
        E("ind5_goddess_sita", "ind5_kusha", "direct", "Mother Sita -> Kusha"),
        E("ind5_kusha", "ind_ayodhya_late_66_95", "direct", "Kusha -> Post-Rama Solar Spine"),
    ]

    # Mahabharata Pandavas & Kauravas
    nodes += [
        N("ind5_yudhishthira", "Emperor Yudhishthira (Eldest Pandava; Dharmaraja of Indraprastha)", "vedic", 11, "Mahabharata Era (c. 950 BCE trad.)", "Eldest Son of Pandu & Kunti", ["Mahabharata"], "Victor of Kurukshetra & Emperor of Hastinapura."),
        N("ind5_bhima", "Prince Bhima / Bhimasena (2nd Pandava; Slayer of Jarasandha & Duryodhana)", "vedic", 11, "Mahabharata Era", "2nd Son of Pandu & Kunti", ["Mahabharata"], "Father of Ghatotkacha."),
        N("ind5_arjuna", "Prince Arjuna (3rd Pandava; Recipient of the Bhagavad Gita; Ancestor of Parikshit)", "vedic", 11, "Mahabharata Era", "3rd Son of Pandu & Kunti", ["Mahabharata", "Bhagavad Gita"], "Wed Draupadi and Subhadra (sister of Krishna); father of Abhimanyu.", major=True),
        N("ind5_nakula", "Prince Nakula (4th Pandava; Twin Son of Pandu & Madri)", "vedic", 11, "Mahabharata Era", "Twin Son of Pandu & Madri", ["Mahabharata"], "Master of horses and swords."),
        N("ind5_sahadeva", "Prince Sahadeva (5th Pandava; Twin Son of Pandu & Madri)", "vedic", 11, "Mahabharata Era", "Twin Son of Pandu & Madri", ["Mahabharata"], "Scholar-warrior of the Pandavas."),
        N("ind5_duryodhana", "Crown Prince Duryodhana (Eldest of 100 Kauravas; Son of Dhritarashtra & Gandhari)", "vedic", 11, "Mahabharata Era", "Leader of Kauravas at Kurukshetra", ["Mahabharata"], "Eldest son of Dhritarashtra & Gandhari."),
        N("ind5_abhimanyu", "Prince Abhimanyu (Son of Arjuna & Subhadra; Father of Parikshit)", "vedic", 11, "Mahabharata Era", "Heroic Pandava Heir", ["Mahabharata"], "Fell at the Chakravyuha; married Uttara and fathered posthumous heir Parikshit."),
        N("ind5_parikshit", "Emperor Parikshit (Son of Abhimanyu & Uttara; Sole Surviving Kuru Heir)", "vedic", 11, "Post-Kurukshetra Era (Bhagavata Purana)", "Post-War Emperor of Hastinapura", ["Mahabharata", "Bhagavata Purana"], "Saved in the womb by Krishna; father of Janamejaya."),
        N("ind5_janamejaya", "Emperor Janamejaya (Son of Parikshit; Patron of Mahabharata Recitation)", "vedic", 12, "Pargiter Gen 96", "Kuru Sovereign at Taxila & Hastinapura", ["Mahabharata", "Pargiter"], "Heard the Mahabharata recited by Vaishampayana."),
    ]
    edges += [
        E("ved_bharata_kuru", "ind5_yudhishthira", "direct", "Pandu & Kunti -> Yudhishthira"),
        E("ved_bharata_kuru", "ind5_bhima", "direct", "Pandu & Kunti -> Bhima"),
        E("ved_bharata_kuru", "ind5_arjuna", "direct", "Pandu & Kunti -> Arjuna"),
        E("ved_bharata_kuru", "ind5_nakula", "direct", "Pandu & Madri -> Nakula"),
        E("ved_bharata_kuru", "ind5_sahadeva", "direct", "Pandu & Madri -> Sahadeva"),
        E("ved_kauravas", "ind5_duryodhana", "direct", "Dhritarashtra & Gandhari -> Duryodhana"),
        E("ind5_arjuna", "ind5_abhimanyu", "direct", "Arjuna & Subhadra -> Abhimanyu"),
        E("ind5_abhimanyu", "ind5_parikshit", "direct", "Abhimanyu & Uttara -> Parikshit"),
        E("ind5_parikshit", "ind5_janamejaya", "direct", "Parikshit -> Janamejaya"),
        E("ind5_janamejaya", "ved_parikshit_janamejaya", "direct", "Janamejaya individual -> Post-War Kuru anchor"),
    ]

    # Maurya & Gupta Individual Emperors
    chain([
        "ved_maurya_ashoka",
        ("ind5_chandragupta_maurya", "Emperor Chandragupta Maurya (Founder of Maurya Empire, r. 322–297 BCE)", 18, "c. 340–297 BCE (Arthashastra; Megasthenes)", "Unifier of India & Ally/Father-in-Law of Seleucus I", "Overthrew the Nandas with Chanakya and forged a treaty with Seleucus I Nicator.", True),
        ("ind5_bindusara", "Emperor Bindusara Amitraghata (Son of Chandragupta Maurya, r. 297–273 BCE)", 18, "297–273 BCE (Ashokavadana; Strabo)", "Father of Ashoka & Correspondent of Antiochus I", "Extended Mauryan rule south across the Deccan.", False),
        ("ind5_emperor_ashoka", "Emperor Ashoka the Great (r. 268–232 BCE; Pillar Edicts Naming Antiochus II & Ptolemy II)", 18, "304–232 BCE (Rock Edicts; Mahavamsa)", "Buddhist Chakravartin of Magadha", "Sent Buddhist missions to Sri Lanka, Syria, Egypt, and Macedonia.", True),
        ("ind5_mahendra_sanghamitta", "Arahant Mahinda & Therī Sanghamitta (Son & Daughter of Ashoka Who Brought Buddhism to Lanka)", 18, "c. 285–205 BCE (Mahavamsa V–XIX)", "Imperial Missionaries to Sri Lanka", "Brought the Bodhi Tree sapling to Anuradhapura under King Devanampiya Tissa.", False),
    ], "vedic", ["Mauryan Inscriptions", "Mahavamsa", "Pargiter p. 286"], "Mauryan Imperial Succession")

    chain([
        "ind_gupta_golden_age",
        ("ind5_sri_gupta", "Maharaja Sri Gupta (Founder of Gupta Line, c. 240–280 CE)", 19, "c. 240–280 CE (Allahabad Pillar)", "Founder of Gupta House", "Father of Ghatotkacha Gupta.", False),
        ("ind5_chandragupta1", "Maharajadhiraja Chandragupta I (r. 319–335 CE; + Licchavi Princess Kumaradevi)", 19, "319–335 CE (Gupta Gold Coins)", "Founder of Gupta Era (319 CE)", "Allied with the ancient Licchavis of Vaisali through Kumaradevi.", False),
        ("ind5_samudragupta", "Emperor Samudragupta (Son of Chandragupta I, r. 335–375 CE; Allahabad Pillar)", 19, "335–375 CE (Prayaga Prashasti)", "Strategist-Emperor & Musician-Poet", "Extended Gupta suzerainty from Himalayas to South India.", False),
        ("ind5_chandragupta2", "Emperor Chandragupta II Vikramaditya (Son of Samudragupta, r. 375–415 CE)", 19, "375–415 CE (Mehrauli Iron Pillar; Faxian)", "Patron of Kalidasa & Nine Gems", "Overthrew the Western Kshatrapas and hosted Chinese pilgrim Faxian.", True),
        ("ind5_kumaragupta1", "Emperor Kumaragupta I (Son of Chandragupta II, r. 415–455 CE; Founder of Nalanda Mahavihara)", 19, "415–455 CE (Bilsad Inscription)", "Patron of Nalanda University", "Founded the great monastic university of Nalanda.", False),
        ("ind5_skandagupta", "Emperor Skandagupta (Son of Kumaragupta I, r. 455–467 CE; Repelled Huna Invasions)", 19, "455–467 CE (Bhitari & Junagadh Inscriptions)", "Defender of Gupta Empire", "Defeated the Hephthalites (White Huns) in northern India.", False),
    ], "vedic", ["Allahabad Pillar Inscription", "Gupta Epigraphy"], "Gupta Imperial Succession")

    # Sri Lanka (Mahavamsa) & Tibet (Blue Annals)
    chain([
        "ceylon_vijaya_mahinda",
        ("ind5_vijaya_lanka", "King Vijaya of Tambapanni (1st King of Sri Lanka, c. 543 BCE; Mahavamsa VI–VII)", 16, "c. 543–505 BCE (Mahavamsa)", "Founder of Sinhalese Kingdom", "Prince from Lala/Vanga who landed at Tambapanni (Lanka).", False),
        ("ind5_pandukabhaya", "King Pandukabhaya of Anuradhapura (r. 437–367 BCE; Mahavamsa X)", 17, "437–367 BCE (Mahavamsa X)", "Builder of Capital Anuradhapura", "United Sri Lanka and laid out Anuradhapura.", False),
        ("ind5_devanampiya_tissa", "King Devanampiya Tissa of Anuradhapura (r. 250–210 BCE; Ally of Emperor Ashoka)", 18, "250–210 BCE (Mahavamsa XI–XX)", "First Buddhist Monarch of Sri Lanka", "Received Ashoka's son Mahinda and planted the Jaya Sri Maha Bodhi.", False),
        ("ind5_dutugemunu", "King Dutugemunu / Dutthagamani Abhaya (r. 161–137 BCE; Built Ruwanwelisaya Stupa)", 18, "161–137 BCE (Mahavamsa XXII–XXXII)", "Great Unifier of Anuradhapura", "United all Lanka from Ruhuna.", False),
    ], "vedic", ["Mahavamsa (Geiger)"], "Sinhalese Mahavamsa Succession")
    edges.append(E("ind5_mahendra_sanghamitta", "ind5_devanampiya_tissa", "cognate", "Ashoka's children Mahinda & Sanghamitta convert King Devanampiya Tissa"))

    chain([
        "tib_nyatri_songtsen",
        ("ind5_nyatri_tsenpo", "King Nyatri Tsenpo (1st Yarlung King of Tibet; Claimed Shakya/Licchavi Descent)", 17, "Traditional 2nd c. BCE (Blue Annals)", "Founder of Tibet's Yarlung Dynasty", "First of the 7 Heavenly Throne Kings of Tibet.", False),
        ("ind5_songtsen_gampo", "Emperor Songtsen Gampo (33rd Yarlung King, 617–650 CE; Unifier of Tibetan Empire)", 20, "617–650 CE (Old Tibetan Annals; Blue Annals)", "Unifier of Tibet & Sponsor of Tibetan Script", "Married Nepalese princess Bhrikuti and Tang Chinese princess Wencheng.", True),
        ("ind5_trisong_detsen", "Emperor Trisong Detsen (r. 755–797 CE; Founded Samye Monastery with Padmasambhava)", 20, "742–c. 800 CE (Old Tibetan Annals)", "Golden Age Emperor of Tibet", "Brought Shantarakshita & Padmasambhava to Tibet.", False),
        ("ind5_ralpacan", "Emperor Ralpacan (r. 815–838 CE; Grandson of Trisong Detsen)", 20, "802–838 CE (Blue Annals)", "Sino-Tibetan Peace Treaty Monarch", "Expanded Buddhist translations and signed 821 CE treaty with Tang China.", False),
        "tib_ladakh_nyimagon",
    ], "vedic", ["The Blue Annals", "Old Tibetan Annals"], "Yarlung Tibetan Imperial Succession")

    # =========================================================================
    # 2. IMPERIAL CHINA & KOREA (HAN, TANG, SONG, MING, QING, THREE KINGDOMS, JOSEON)
    # =========================================================================
    nodes.append(N("eas5_qin_shi_huang", "Emperor Qin Shi Huang / Ying Zheng (1st Emperor of Unified China, r. 221–210 BCE)", "chinese", 18, "259–210 BCE (Shiji Ch. 6)", "First Emperor of Qin & Builder of Great Wall/Terracotta Army", ["Sima Qian Shiji Ch. 6"], "Unified Warring States China in 221 BCE.", major=True))
    edges.append(E("chn_boyi_qin", "eas5_qin_shi_huang", "direct", "Qin royal house -> Qin Shi Huang"))

    chain([
        "chn_han_tang_empires",
        ("eas5_han_gaozu", "Emperor Han Gaozu / Liu Bang (Founder of Han Dynasty, r. 202–195 BCE)", 18, "256–195 BCE (Shiji Ch. 8)", "Founder of 400-Year Han Empire", "Rose from peasant official to defeat Xiang Yu and establish Han.", True),
        ("eas5_han_wen", "Emperor Wen of Han / Liu Heng (Son of Gaozu, r. 180–157 BCE)", 18, "203–157 BCE (Shiji Ch. 10)", "Rule of Wen and Jing", "Father of Emperor Jing.", False),
        ("eas5_han_jing", "Emperor Jing of Han / Liu Qi (Son of Emperor Wen, r. 157–141 BCE)", 18, "188–141 BCE (Shiji Ch. 11)", "Father of Han Wudi", "Consolidated imperial centralization.", False),
        ("eas5_han_wudi", "Emperor Wu of Han / Liu Che (Han Wudi, r. 141–87 BCE; Opened Silk Road)", 18, "156–87 BCE (Shiji; Han Shu)", "Greatest Han Emperor (Zhang Qian & Sima Qian)", "Sent Zhang Qian to Bactria & Parthia, initiating the Silk Road.", True),
        ("eas5_han_guangwu", "Emperor Guangwu of Han / Liu Xiu (Restorer of Eastern Han, r. 25–57 CE)", 19, "5 BCE–57 CE (Hou Hanshu)", "9th-Gen Descendant of Liu Bang & Eastern Han Founder", "Restored Han Dynasty at Luoyang.", False),
    ], "chinese", ["Sima Qian Shiji", "Han Shu"], "Han Dynasty Imperial Succession")

    chain([
        "chn_han_tang_empires",
        ("eas5_tang_gaozu", "Emperor Tang Gaozu / Li Yuan (Founder of Tang Dynasty, r. 618–626 CE)", 20, "566–635 CE (Old Book of Tang)", "Founder of Cosmopolitan Tang Empire", "Established Tang capital at Chang'an.", False),
        ("eas5_tang_taizong", "Emperor Tang Taizong / Li Shimin (Son of Li Yuan, r. 626–649 CE; Tian Kehan)", 20, "598–649 CE (Old Book of Tang)", "Greatest Military & Cultural Tang Emperor", "Sponsored Xuanzang's journey to India and Princess Wencheng's marriage to Tibet.", True),
        ("eas5_tang_gaozong", "Emperor Tang Gaozong / Li Zhi (Son of Taizong, r. 649–683 CE)", 20, "628–683 CE", "Husband of Empress Wu Zetian", "Unified the Korean Peninsula campaign in alliance with Silla.", False),
        ("eas5_tang_xuanzong", "Emperor Tang Xuanzong / Li Longji (Grandson of Gaozong & Wu Zetian, r. 712–756 CE)", 20, "685–762 CE", "Kaiyuan Golden Age Monarch (Li Bai & Du Fu)", "Presided over Tang cultural zenith.", False),
    ], "chinese", ["Old Book of Tang"], "Tang Imperial Succession")
    nodes.append(N("eas5_wu_zetian", "Empress Wu Zetian (Sole Female Huangdi of China, r. 690–705 CE)", "chinese", 20, "624–705 CE (Book of Tang)", "Only Sovereign Empress Regnant in Chinese History", ["Book of Tang"], "Consort of Gaozong; ruled in her own right as Zhou Dynasty Huangdi.", major=True))
    edges += [
        E("eas5_tang_gaozong", "eas5_wu_zetian", "direct", "Consort & Co-Ruler Wu Zetian"),
        E("eas5_wu_zetian", "eas5_tang_xuanzong", "direct", "Grandmother Wu Zetian -> Emperor Tang Xuanzong"),
        E("eas5_tang_taizong", "ind5_songtsen_gampo", "cognate", "Tang Taizong arranges Princess Wencheng marriage to Emperor Songtsen Gampo"),
    ]

    nodes.append(N("eas5_song_taizu", "Emperor Song Taizu / Zhao Kuangyin (Founder of Song Dynasty, r. 960–976 CE)", "chinese", 20, "927–976 CE (History of Song)", "Founder of Song China", ["History of Song"], "Ended Five Dynasties fragmentation and inaugurated the Northern Song."))
    edges.append(E("eas5_tang_xuanzong", "eas5_song_taizu", "expansion", "Tang -> Five Dynasties -> Emperor Song Taizu"))
    chain([
        "eas5_song_taizu",
        ("eas5_ming_hongwu", "Emperor Hongwu / Zhu Yuanzhang (Founder of Ming Dynasty, r. 1368–1398 CE)", 21, "1328–1398 CE (Ming Shi)", "Founder of Ming Dynasty", "Drove out Yuan rule and established Nanjing.", False),
        ("eas5_ming_yongle", "Emperor Yongle / Zhu Di (Son of Hongwu, r. 1402–1424 CE; Forbidden City & Zheng He)", 21, "1360–1424 CE (Ming Shi)", "Builder of Beijing Forbidden City", "Commissioned Admiral Zheng He's treasure voyages across Asia and East Africa.", True),
    ], "chinese", ["Ming Shi"], "Later Chinese Imperial Continuity", edge_type="expansion")
    edges.append(E("eas5_ming_yongle", "chn_ming_qing_manchu", "expansion", "Ming imperial era -> Qing / Manchu transition"))

    chain([
        "chn_ming_qing_manchu",
        ("eas5_qing_nurhaci", "Khan Nurhaci (Founder of Later Jin / Manchu Aisin Gioro Clan, r. 1616–1626)", 21, "1559–1626 CE (Draft History of Qing)", "Unifier of Jurchen / Manchu Tribes", "Created the Eight Banners; father of Hong Taiji.", False),
        ("eas5_qing_hong_taiji", "Emperor Hong Taiji (Son of Nurhaci; Proclaimed Great Qing, r. 1626–1643)", 21, "1592–1643 CE", "Proclaimer of Qing Dynasty", "Father of Shunzhi.", False),
        ("eas5_qing_shunzhi", "Emperor Shunzhi / Fulin (1st Qing Emperor in Beijing, r. 1644–1661)", 21, "1638–1661 CE", "9th Son of Hong Taiji", "Entered Beijing in 1644 CE.", False),
        ("eas5_qing_kangxi", "Emperor Kangxi / Xuanye (Son of Shunzhi, r. 1661–1722 — 61 yrs)", 21, "1654–1722 CE", "Longest-Reigning Emperor in Chinese History", "Compiled the Kangxi Dictionary and consolidated Tibet & Taiwan.", True),
        ("eas5_qing_yongzheng", "Emperor Yongzheng / Yinzhen (4th Son of Kangxi, r. 1722–1735)", 21, "1678–1735 CE", "Father of Qianlong", "Centralized Qing imperial administration.", False),
        ("eas5_qing_qianlong", "Emperor Qianlong / Hongli (Son of Yongzheng, r. 1735–1796)", 21, "1711–1799 CE", "Summit of Qing Territorial Empire", "Oversaw the Siku Quanshu encyclopedia and zenith of Qing prosperity.", True),
    ], "chinese", ["Draft History of Qing"], "Qing Aisin Gioro Imperial Succession")

    # Korea
    chain([
        "kor_jumong",
        ("eas5_gwanggaeto", "King Gwanggaeto the Great of Goguryeo (r. 391–413 CE; Hulbert Vol. 1)", 19, "374–413 CE (Samguk Sagi; Gwanggaeto Stele)", "Conqueror King of Goguryeo", "Expanded Goguryeo across Manchuria and the Korean Peninsula.", True),
    ], "japan_korea", ["Samguk Sagi", "Hulbert History of Korea"], "Goguryeo Royal Succession")
    chain([
        "kor_hyeokgeose_silla",
        ("eas5_queen_seondeok", "Queen Seondeok of Silla (r. 632–647 CE; Cheomseongdae Observatory)", 20, "d. 647 CE (Samguk Sagi)", "First Sovereign Queen of Silla", "Built Hwangnyongsa Nine-Story Pagoda and Cheomseongdae.", False),
        ("eas5_king_munmu", "King Munmu of Unified Silla (r. 661–681 CE; Nephew-Line Unifier of Korea)", 20, "626–681 CE (Samguk Sagi)", "Unifier of the Three Kingdoms of Korea", "Son of Muyeol; unified Silla in 668–676 CE.", False),
        ("eas5_wang_geon_goryeo", "King Taejo Wang Geon (Founder of Goryeo Dynasty, r. 918–943 CE)", 20, "877–943 CE (Goryeosa)", "Founder of Goryeo (Origin of 'Korea')", "United Later Three Kingdoms in 936 CE.", False),
        ("eas5_taejo_joseon", "King Taejo Yi Seong-gye (Founder of Joseon Dynasty, r. 1392–1398 CE)", 21, "1335–1408 CE (Joseon Annals)", "Founder of 500-Year Joseon Dynasty", "Founded Hanyang (Seoul) as royal capital.", False),
        ("eas5_king_sejong", "King Sejong the Great of Joseon (Son of Taejong, r. 1418–1450 CE; Creator of Hangul)", 21, "1397–1450 CE (Sejong Sillok)", "Creator of Korean Alphabet (Hangul)", "Grandson of Taejo; promulgated Hunminjeongeum (Hangul) in 1446 CE.", True),
    ], "japan_korea", ["Samguk Sagi", "Goryeosa", "Joseon Annals"], "Korean Royal Dynasties", edge_type="expansion")
    edges.append(E("kor_hulbert_three_kingdoms", "eas5_gwanggaeto", "direct", "Hulbert Three Kingdoms -> Gwanggaeto the Great"))

    # =========================================================================
    # 3. ABULGHAZI TURKIC, OGHUZ, SELJUK & EARLY OTTOMAN STEMS
    # =========================================================================
    chain([
        "abg_turk_alanja",
        ("stp5_turk", "Turk / Japhis-Oglany (Eldest Son of Japheth in Abulghazi)", 7, "Abulghazi Genealogy of the Tartars", "Progenitor of Turkic Peoples", "Invented felt tents and ruled the Issyk-Kul steppe.", False),
        ("stp5_taunak", "Taunak Khan (Son of Turk)", 8, "Abulghazi Part I", "Son of Turk", "Succeeded his father Turk.", False),
        ("stp5_ilchi", "Ilchi Khan (Son of Taunak)", 9, "Abulghazi Part I", "3rd Steppe Khan", "Father of Dib Bakuy.", False),
        ("stp5_dib_bakuy", "Dib Bakuy Khan (Son of Ilchi)", 10, "Abulghazi Part I", "4th Steppe Khan", "Father of Kayuk.", False),
        ("stp5_kayuk", "Kayuk Khan (Son of Dib Bakuy)", 11, "Abulghazi Part I", "5th Steppe Khan", "Father of Alanja.", False),
        ("stp5_alanja_khan", "Alanja Khan (Son of Kayuk; Father of Twins Tatar & Mogul)", 12, "Abulghazi Part I", "Father of Tatar & Mogul", "Divided his domains between twin sons Tatar and Mogul.", False),
        ("stp5_mogul_khan", "Mogul / Mung'l Khan (Twin Son of Alanja; Ancestor of Oghuz & Borjigin)", 13, "Abulghazi Part I–II", "Eponym of Mogols", "Brother of Tatar Khan; father of Qara Khan.", False),
        ("stp5_qara_khan", "Qara Khan (Son of Mogul; Father of Oghuz Khan)", 14, "Abulghazi Part II", "Father of Oghuz Khan", "Father of the hero Oghuz.", False),
        ("stp5_oghuz_khan", "Oghuz Khagan (Son of Qara Khan; Epic Founder of the 24 Oghuz Tribes)", 15, "Abulghazi Part II", "Great Khagan of the Oghuz Turks", "United the steppe nations and fathered 6 illustrious sons (Üçok & Bozok).", True),
    ], "steppe", ["Abulghazi Bahadur Khan (1730 trans.)"], "Abulghazi Steppe Patrilineal Line")

    nodes += [
        N("stp5_tatar_khan", "Tatar Khan (Twin Son of Alanja Khan; Eponym of the Tatars)", "steppe", 13, "Abulghazi Part I", "Twin Brother of Mogul Khan", ["Abulghazi Part I"], "Ancestor of the 7-generation Tatar Khans."),
        N("stp5_gun_khan", "Gün Khan ('Sun', Eldest Son of Oghuz; Ancestor of Kayi / Ottomans)", "steppe", 16, "Abulghazi Part II", "Ancestor of Kayi Tribe (Ottomans)", ["Abulghazi"], "Forebear of the Kayi tribe from whom Suleyman Shah, Ertugrul & Osman I sprang."),
        N("stp5_ay_khan", "Ay Khan ('Moon', 2nd Son of Oghuz)", "steppe", 16, "Abulghazi Part II", "2nd Son of Oghuz", ["Abulghazi"], "Bozok prince."),
        N("stp5_yildiz_khan", "Yildiz Khan ('Star', 3rd Son of Oghuz)", "steppe", 16, "Abulghazi Part II", "3rd Son of Oghuz", ["Abulghazi"], "Bozok prince."),
        N("stp5_gok_khan", "Gök Khan ('Sky', 4th Son of Oghuz)", "steppe", 16, "Abulghazi Part II", "4th Son of Oghuz", ["Abulghazi"], "Üçok prince."),
        N("stp5_dag_khan", "Dag Khan ('Mountain', 5th Son of Oghuz)", "steppe", 16, "Abulghazi Part II", "5th Son of Oghuz", ["Abulghazi"], "Üçok prince."),
        N("stp5_deniz_khan", "Deniz Khan ('Sea', 6th Son of Oghuz; Ancestor of Seljuks via Kınık)", "steppe", 16, "Abulghazi Part II", "Ancestor of Kınık Tribe (Seljuks)", ["Abulghazi", "Mahmud al-Kashgari"], "Üçok prince linked with the Kınık clan of the Seljuks."),
    ]
    edges += [
        E("stp5_alanja_khan", "stp5_tatar_khan", "direct", "Alanja -> twin son Tatar Khan"),
        E("abg_tatar_mogul_twins", "stp5_tatar_khan", "direct", "Abulghazi twins -> Tatar"),
        E("abg_tatar_mogul_twins", "stp5_mogul_khan", "direct", "Abulghazi twins -> Mogul"),
    ]
    for ox in ("stp5_gun_khan", "stp5_ay_khan", "stp5_yildiz_khan", "stp5_gok_khan", "stp5_dag_khan", "stp5_deniz_khan"):
        edges.append(E("stp5_oghuz_khan", ox, "direct", "Oghuz Khagan -> 6 Sons"))
        edges.append(E("stp_oghuz_six", ox, "direct", "6 Sons anchor -> individual son"))

    # Seljuks & Early Ottomans
    nodes += [
        N("stp5_seljuk", "Seljuk Beg ibn Duqaq (10th c. CE; Founder of Seljuk Dynasty)", "steppe", 20, "10th c. CE (Oghuz Kınık)", "Eponymous Founder of Seljuk Turks", ["Abulghazi", "Ibn al-Athir"], "Son of Duqaq; converted to Islam near Jand; grandfather of Tughril & Chaghri Beg."),
        N("stp5_mikail", "Mikail ibn Seljuk (Son of Seljuk; Father of Tughril & Chaghri Beg)", "steppe", 20, "late 10th c. CE", "Father of Great Seljuk Sultans", ["Abulghazi"], "Father of Tughril Beg & Chaghri Beg."),
        N("stp5_tughril_beg", "Sultan Tughril Beg (1st Great Seljuk Sultan, r. 1037–1063)", "steppe", 20, "990–1063 CE", "Entered Baghdad 1055 CE", ["Ibn al-Athir"], "Restored Abbasid protection in Baghdad and founded the Great Seljuk Empire."),
        N("stp5_chaghri_beg", "Chaghri Beg (Brother of Tughril; Father of Alp Arslan, d. 1060)", "steppe", 20, "989–1060 CE", "Co-Founder & Ruler of Khorasan", ["Ibn al-Athir"], "Father of Great Sultan Alp Arslan."),
        N("stp5_alp_arslan", "Sultan Alp Arslan (Son of Chaghri Beg; Victor of Manzikert 1071 CE)", "steppe", 20, "1029–1072 CE", "2nd Great Seljuk Sultan", ["Ibn al-Athir"], "Opened Anatolia to Turkish settlement at Manzikert (1071).", major=True),
        N("stp5_malik_shah1", "Sultan Malik-Shah I (Son of Alp Arslan; Patron of Omar Khayyam & Nizam al-Mulk, r. 1072–1092)", "steppe", 20, "1055–1092 CE", "3rd Great Seljuk Sultan", ["Ibn al-Athir"], "Zenith of Great Seljuk power from Syria to Transoxiana."),
        N("stp5_suleyman_shah", "Süleyman Shah (Kayi Chieftain; Father of Ertuğrul Ghazi)", "steppe", 20, "d. c. 1227 CE (Ottoman Chronicles)", "Ancestor of Ottoman Dynasty", ["Abulghazi", "Ottoman Annals"], "Led Kayi clan westward into Anatolia."),
        N("stp5_ertugrul", "Ertuğrul Ghazi (Son of Süleyman Shah; Father of Osman I, d. c. 1280)", "steppe", 20, "c. 1198–1280 CE (Ottoman Chronicles)", "Bey of Söğüt & Father of Osman I", ["Ottoman Chronicles"], "Lord of the Seljuk frontier margraviate at Söğüt; father of Sultan Osman I."),
    ]
    edges += [
        E("stp5_deniz_khan", "stp5_seljuk", "expansion", "Oghuz Kınık lineage -> Seljuk Beg"),
        E("sel_tughril_alparslan", "stp5_seljuk", "direct", "Seljuk anchor -> Seljuk Beg"),
        E("stp5_seljuk", "stp5_mikail", "direct", "Seljuk -> son Mikail"),
        E("stp5_mikail", "stp5_tughril_beg", "direct", "Mikail -> son Tughril Beg"),
        E("stp5_mikail", "stp5_chaghri_beg", "direct", "Mikail -> son Chaghri Beg"),
        E("stp5_chaghri_beg", "stp5_alp_arslan", "direct", "Chaghri Beg -> son Alp Arslan"),
        E("stp5_alp_arslan", "stp5_malik_shah1", "direct", "Alp Arslan -> son Malik-Shah I"),
        E("stp5_gun_khan", "stp5_suleyman_shah", "expansion", "Oghuz Kayi tribe -> Süleyman Shah"),
        E("ott_osman_ertughrul", "stp5_suleyman_shah", "direct", "Ottoman founders anchor -> Süleyman Shah"),
        E("stp5_suleyman_shah", "stp5_ertugrul", "direct", "Süleyman Shah -> son Ertuğrul Ghazi"),
        E("stp5_ertugrul", "mon_ott_osman1", "direct", "Ertuğrul Ghazi -> Sultan Osman I"),
    ]

    # =========================================================================
    # 4. CELTIC IRELAND/SCOTLAND, NORSE/NORMANDY, BRITAIN & KIEVAN RUS'
    # =========================================================================
    chain([
        "irl_baath_fenius",
        ("eur5_fenius_farsa", "Fénius Farsaid (Scythian King Who Studied the 72 Languages at Babel)", 6, "Tower of Babel Era (Lebor Gabála; Keating)", "Ancestor of the Gaels", "Founded the school of languages and fathered Nel / Niul.", False),
        ("eur5_niul", "Prince Nel / Niul (Son of Fénius; Wed Egyptian Princess Scota)", 9, "Exodus Era (Lebor Gabála; Keating)", "Linguist Invited to Egypt by Pharaoh", "Married Scota, daughter of Pharaoh Cingris, and befriended Moses.", False),
        ("eur5_goidel_glas", "Goídel Glas / Gaedhal Glas (Son of Niul & Scota; Eponym of the Gaels)", 9, "Exodus Era (Lebor Gabála; Keating)", "Eponym of All Gaelic Peoples & Language", "Blessed by Moses after the serpent bite; ancestor of the Milesians.", False),
        ("eur5_breogan", "King Breogán (Founder of Brigantia / A Coruña in Galicia, Spain)", 10, "Lebor Gabála Part V", "Builder of Tower of Breogán", "Built the watchtower from whose summit his son Íth sighted Ireland.", False),
        ("eur5_bile", "Bile mac Breogán (Father of Míl Espáine)", 11, "Lebor Gabála Part V", "Father of Milesius", "Elder son of Breogán.", False),
        ("eur5_mil_espaine", "Míl Espáine / Milesius (Galamh, Father of the Milesian Conquerors of Ireland)", 11, "Lebor Gabála Part V; Keating", "Patriarch of Gaelic Irish Dynasties", "Ancestor of Éremón (Uí Néill, Connacht, Leinster, Dal Riada) and Éber Finn (Munster, O'Brien, MacCarthy).", True),
        ("eur5_eremon", "High King Éremón mac Míl (1st Milesian High King; Ancestor of Uí Néill & Scots)", 12, "Lebor Gabála; Keating", "Milesian High King of Ireland", "Co-king with brother Éber Finn; ancestor of Conn of the Hundred Battles.", False),
        ("eur5_conn_hundred_battles", "High King Conn Cétchathach ('Of the Hundred Battles', 2nd c. CE trad.)", 18, "c. 2nd c. CE (Keating Foras Feasa)", "Progenitor of Connachta & Uí Néill", "Ancestor of Cormac mac Airt and Niall of the Nine Hostages.", False),
        ("eur5_cormac_mac_airt", "High King Cormac mac Airt of Tara (3rd c. CE trad.; Lawgiver Patron of Fionn)", 18, "c. 3rd c. CE (Keating)", "Lawgiver High King of Tara", "Grandson of Conn; grandfather of Niall's ancestor Fiacha Sraibtine.", False),
        ("eur5_niall_nine_hostages", "High King Niall Noígíallach ('Of the Nine Hostages', d. c. 405 CE)", 19, "d. c. 405 CE (Keating)", "Progenitor of All Northern & Southern Uí Néill Dynasties", "Father of Eógan (O'Neill), Conall Gulban (O'Donnell / St. Columba) & Lóegaire (met St. Patrick!).", True),
    ], "europe_norse", ["Lebor Gabála Érenn", "Geoffrey Keating Foras Feasa ar Éirinn"], "Gaelic Milesian Pedigree")

    nodes += [
        N("eur5_scota", "Princess Scota (Daughter of Pharaoh Cingris; Wife of Niul & Mother of Goídel Glas)", "levant_egypt", 9, "Exodus Era (Lebor Gabála; Keating)", "Egyptian-Gaelic Matriarch", ["Lebor Gabála Érenn", "Keating"], "Egyptian princess married to Scythian scholar Niul; eponym of Scotland ('Scotia')."),
        N("eur5_eber_finn", "High King Éber Finn mac Míl (Brother of Éremón; Ancestor of Munster / Eoghanacht / Dál gCais)", "europe_norse", 12, "Lebor Gabála; Keating", "Progenitor of Munster Kings", ["Lebor Gabála", "Keating"], "Ancestor of Cormac Cas -> Brian Boru."),
        N("eur5_ir", "Prince Ír mac Míl (Ancestral Founder of Ulaid / Ulster & Dál nAraidi)", "europe_norse", 12, "Lebor Gabála", "Son of Míl Espáine", ["Lebor Gabála"], "Progenitor of Cú Chulainn's Ulaid lineages."),
        N("eur5_amairgin", "Amairgin Glúngel mac Míl (First Poet & Judge of Ireland)", "europe_norse", 12, "Lebor Gabála Part V", "Chief Ollamh / Bard of Milesians", ["Lebor Gabála"], "Sang the Song of Amairgin upon landing in Ireland."),
        N("eur5_eogan_oneill", "Prince Eógan mac Néill (Founder of Cenél nEógain / O'Neill Kings of Ailech)", "europe_norse", 19, "5th c. CE (Keating)", "Son of Niall of the Nine Hostages", ["Keating"], "Progenitor of O'Neill High Kings."),
        N("eur5_conall_gulban", "Prince Conall Gulban mac Néill (Ancestor of O'Donnell & St. Columba of Iona)", "europe_norse", 19, "5th c. CE (Keating; Adomnán)", "Son of Niall; Great-Grandfather of St. Columba", ["Keating", "Adomnán Life of Columba"], "Ancestor of Tyrconnell & St. Columba."),
        N("eur5_brian_boru", "High King Brian Bóruma / Brian Boru (r. 1002–1014 CE; Victor of Clontarf)", "europe_norse", 20, "941–1014 CE (Annals of Ulster; Keating)", "Imperator Scottorum & Unifier of Ireland", ["Annals of Ulster", "Keating"], "Descendant of Éber Finn & Cormac Cas (Dál gCais); defeated Vikings at Clontarf (1014 CE).", major=True),
        N("eur5_fergus_mor", "King Fergus Mór mac Eirc (Founder of Scottish Dál Riata, 498 CE)", "europe_norse", 19, "d. 501 CE (Annals; Keating)", "Ancestor of Kings of Scotland", ["Keating", "Chronicles of Scotland"], "Crossed from Antrim into Argyll, founding the Scottish royal stem."),
        N("eur5_kenneth_macalpin", "King Kenneth I MacAlpin (Cináed mac Ailpín, 843–858 CE; 1st King of Alba/Scotland)", "europe_norse", 20, "810–858 CE (Chronicles of Scotland)", "Unifier of Scots & Picts", ["Chronicle of the Kings of Alba"], "Descendant of Fergus Mór; united Dál Riata and Pictland."),
        N("eur5_malcolm3", "King Malcolm III Canmore (+ St. Margaret of Scotland, r. 1058–1093 CE)", "europe_norse", 20, "1031–1093 CE (Scottish Chronicles)", "6th-Gen Descendant of Kenneth MacAlpin", ["Scottish Chronicles"], "Married St. Margaret of Wessex (linking Scotland & England's House of Wessex!)."),
        N("eur5_robert_bruce", "King Robert I the Bruce of Scotland (r. 1306–1329 CE; Bannockburn 1314)", "europe_norse", 21, "1274–1329 CE (Scottish Chronicles)", "Descendant of Malcolm III & Liberator of Scotland", ["Scottish Chronicles"], "Won Scottish independence at Bannockburn (1314 CE); grandfather of Robert II (House of Stewart).", major=True),
    ]
    edges += [
        E("eur5_scota", "eur5_goidel_glas", "direct", "Mother Princess Scota -> Goídel Glas"),
        E("eur5_mil_espaine", "eur5_eber_finn", "direct", "Míl Espáine -> son Éber Finn"),
        E("eur5_mil_espaine", "eur5_ir", "direct", "Míl Espáine -> son Ír"),
        E("eur5_mil_espaine", "eur5_amairgin", "direct", "Míl Espáine -> poet son Amairgin"),
        E("eur5_niall_nine_hostages", "eur5_eogan_oneill", "direct", "Niall -> Eógan (O'Neill)"),
        E("eur5_niall_nine_hostages", "eur5_conall_gulban", "direct", "Niall -> Conall Gulban (O'Donnell/Columba)"),
        E("eur5_eber_finn", "eur5_brian_boru", "expansion", "Éber Finn -> Cormac Cas -> Brian Boru"),
        E("eur5_eremon", "eur5_fergus_mor", "expansion", "Éremón -> Cairbre Riada -> Fergus Mór mac Eirc"),
        E("sco_fergus_macalpin", "eur5_fergus_mor", "direct", "Scottish anchor -> Fergus Mór"),
        E("eur5_fergus_mor", "eur5_kenneth_macalpin", "direct", "Fergus Mór -> Kenneth I MacAlpin"),
        E("eur5_kenneth_macalpin", "eur5_malcolm3", "direct", "Kenneth MacAlpin -> Malcolm II -> Malcolm III Canmore"),
        E("eur5_malcolm3", "eur5_robert_bruce", "direct", "Malcolm III -> David I -> Earl David -> Isobel -> Robert the Bruce"),
    ]

    # Norse, Normandy & Britain
    nodes += [
        N("eur5_yngvi_freyr", "Yngvi-Freyr (Progenitor of Uppsala Yngling Kings, Prose Edda / Ynglinga Saga)", "europe_norse", 9, "Snorri Sturluson Ynglinga Saga", "Euhemerized Norse Founder", ["Prose Edda", "Ynglinga Saga"], "Son of Njörðr; founder of the Swedish/Norwegian Yngling royal stem."),
        N("eur5_harald_fairhair", "King Harald I Fairhair of Norway (Haraldr Hárfagri, r. 872–930 CE)", "europe_norse", 20, "c. 850–932 CE (Heimskringla)", "First King of Unified Norway", ["Heimskringla"], "Descended from the Ynglings; unified Norway at Hafrsfjord."),
        N("eur5_skjoldr", "King Skjöldr / Scyld Scefing (Eponym of Danish Skjöldung Kings, Beowulf & Edda)", "europe_norse", 10, "Prose Edda; Beowulf", "Mythic Founder of Denmark", ["Prose Edda", "Beowulf"], "Son of Odin in Snorri's Edda; ancestor of Danish and Viking kings."),
        N("eur5_ragnar_lodbrok", "King Ragnar Lodbrok ('Hairy-Breeches', 9th c. CE Legendary Sea-King)", "europe_norse", 20, "9th c. CE (Ragnars Saga Loðbrókar)", "Famous Viking Father of Sons of Ragnar", ["Ragnars Saga Loðbrókar"], "Fathered Björn Ironside, Ivar the Boneless & Sigurd Snake-in-the-Eye."),
        N("eur5_bjorn_ironside", "King Björn Ironside (Son of Ragnar; Raided Mediterranean; Ancestor of Munsö Sweden)", "europe_norse", 20, "9th c. CE (Norse Sagas)", "King of Uppsala / Sweden", ["Ragnars Saga"], "Led 859 CE Viking expedition to Spain and Italy."),
        N("eur5_ivar_boneless", "King Ivar the Boneless (Son of Ragnar; Leader of Great Heathen Army 865 CE)", "europe_norse", 20, "d. c. 873 CE (Anglo-Saxon Chronicle)", "Founder of Uí Ímair (Dublin/York)", ["Anglo-Saxon Chronicle"], "Conquered York and Dublin."),
        N("eur5_sigurd_snake_eye", "King Sigurd Snake-in-the-Eye (Son of Ragnar; Ancestor of Harthacnut & Canute)", "europe_norse", 20, "9th c. CE (Norse Sagas)", "King in Zealand / Denmark", ["Ragnars Saga"], "Ancestor of Gorm the Old & King Canute the Great."),
        N("eur5_rollo_normandy", "Duke Rollo / Hrólfr of Normandy (r. 911–927 CE; Treaty of Saint-Clair-sur-Epte)", "europe_norse", 20, "c. 860–930 CE (Dudo; Orkneyinga Saga)", "1st Viking Ruler of Normandy", ["Heimskringla", "Dudo of Saint-Quentin"], "Norwegian noble of Jarl Rognvald's house (kin/contemporary of Harald Fairhair) who founded Normandy."),
        N("eur5_william_longsword", "Duke William I Longsword of Normandy (Son of Rollo, r. 927–942 CE)", "europe_norse", 20, "c. 893–942 CE", "2nd Duke of Normandy", ["William of Jumièges"], "Son of Rollo & Poppa of Bayeux."),
        N("eur5_richard1_normandy", "Duke Richard I the Fearless of Normandy (Son of William Longsword, r. 942–996)", "europe_norse", 20, "932–996 CE", "3rd Duke of Normandy", ["William of Jumièges"], "Father of Richard II and Emma of Normandy (Queen of Ethelred II & Canute!)."),
        N("eur5_richard2_normandy", "Duke Richard II the Good of Normandy (Son of Richard I, r. 996–1026 CE)", "europe_norse", 20, "c. 963–1026 CE", "4th Duke of Normandy", ["William of Jumièges"], "Father of Robert I the Magnificent."),
        N("eur5_robert1_normandy", "Duke Robert I the Magnificent of Normandy (r. 1027–1035; Father of William the Conqueror)", "europe_norse", 20, "1000–1035 CE", "Father of William the Conqueror", ["Orderic Vitalis"], "Son of Richard II; fathered William I of England with Herleva of Falaise."),
        N("eur5_harald_hardrada", "King Harald III Hardrada of Norway (+ Elizabeth of Kiev, r. 1046–1066 CE)", "europe_norse", 20, "1015–1066 CE (Heimskringla)", "Varangian Commander & King of Norway", ["Heimskringla"], "Married Elizabeth Yaroslavna of Kiev; fell at Stamford Bridge (1066 CE)."),
    ]
    edges += [
        E("eur_ynglings_skjoldungs", "eur5_yngvi_freyr", "direct", "Yngling anchor -> Yngvi-Freyr"),
        E("eur5_yngvi_freyr", "eur5_harald_fairhair", "direct", "Ynglings -> Halfdan the Black -> Harald Fairhair"),
        E("eur5_harald_fairhair", "eur5_harald_hardrada", "direct", "Harald Fairhair -> Sigurd Syr -> Harald Hardrada"),
        E("eur_ynglings_skjoldungs", "eur5_skjoldr", "direct", "Skjöldung anchor -> Skjöldr"),
        E("eur5_skjoldr", "eur5_ragnar_lodbrok", "expansion", "Skjöldung line -> Sigurd Hring -> Ragnar Lodbrok"),
        E("eur5_ragnar_lodbrok", "eur5_bjorn_ironside", "direct", "Ragnar -> Björn Ironside"),
        E("eur5_ragnar_lodbrok", "eur5_ivar_boneless", "direct", "Ragnar -> Ivar the Boneless"),
        E("eur5_ragnar_lodbrok", "eur5_sigurd_snake_eye", "direct", "Ragnar -> Sigurd Snake-in-the-Eye"),
        E("eur5_sigurd_snake_eye", "mon_eng_canute", "direct", "Sigurd -> Harthacnut -> Gorm -> Sweyn -> King Canute"),
        E("eur5_harald_fairhair", "eur5_rollo_normandy", "expansion", "Norwegian Jarls of Møre (contemporary/kin of Fairhair) -> Duke Rollo of Normandy"),
    ]
    link_seq(edges, ["eur5_rollo_normandy", "eur5_william_longsword", "eur5_richard1_normandy", "eur5_richard2_normandy", "eur5_robert1_normandy", "mon_eng_william1"], "direct", "Ducal House of Normandy to William the Conqueror")

    # British & Anglo-Saxon Chronicles
    nodes += [
        N("eur5_brutus_troy", "Brutus of Troy (Son of Silvius; Legendary Founder of Britain, Geoffrey of Monmouth)", "europe_norse", 14, "c. 1100 BCE trad. (Historia Regum Britanniae)", "Eponym of Britain", ["Geoffrey of Monmouth", "Historia Brittonum"], "Great-grandson of Aeneas; divided Britain among sons Locrinus, Camber & Albanactus."),
        N("eur5_locrinus", "King Locrinus of Loegria / England (Eldest Son of Brutus of Troy)", "europe_norse", 14, "Geoffrey of Monmouth II.1", "Founder of England (Loegria)", ["Geoffrey of Monmouth"], "Eldest son of Brutus."),
        N("eur5_camber", "King Camber of Cambria / Wales (Son of Brutus of Troy)", "europe_norse", 14, "Geoffrey of Monmouth II.1", "Eponym of Wales (Cymru/Cambria)", ["Geoffrey of Monmouth"], "2nd son of Brutus."),
        N("eur5_albanactus", "King Albanactus of Alba / Scotland (Youngest Son of Brutus of Troy)", "europe_norse", 14, "Geoffrey of Monmouth II.1", "Eponym of Albany / Scotland", ["Geoffrey of Monmouth"], "3rd son of Brutus."),
        N("eur5_king_lear", "King Leir / Lear of Britain (Father of Goneril, Regan & Cordelia)", "europe_norse", 16, "c. 8th c. BCE trad. (Geoffrey of Monmouth II.11)", "Pre-Roman British King", ["Geoffrey of Monmouth"], "8th-gen descendant of Locrinus."),
        N("eur5_beli_mawr", "King Beli Mawr ('Beli the Great', Progenitor of Welsh Royal Houses)", "europe_norse", 18, "1st c. BCE (Welsh Genealogies; Geoffrey)", "Father of Cassivellaunus & Lludd", ["Harleian Welsh Genealogies"], "Key ancestral node of British and Welsh dynastic pedigrees."),
        N("eur5_uther_pendragon", "King Uther Pendragon (Son of Constantine; Father of King Arthur)", "europe_norse", 19, "5th c. CE (Geoffrey of Monmouth VIII)", "Father of King Arthur", ["Geoffrey of Monmouth"], "Brother of Aurelius Ambrosius; father of King Arthur."),
        N("eur5_king_arthur", "King Arthur of Britain (+ Queen Guinevere, Geoffrey of Monmouth IX–XI)", "europe_norse", 19, "c. 500 CE (Historia Brittonum; Geoffrey)", "Sovereign of Camelot & Britain", ["Geoffrey of Monmouth", "Historia Brittonum"], "Hero-king of post-Roman Britain.", major=True),
        N("eur5_hengist", "King Hengist of Kent (Leader of Anglo-Saxon Arrival, c. 449 CE; Bede HE I.15)", "europe_norse", 19, "d. 488 CE (Bede Ecclesiastical History)", "Founder of Kingdom of Kent", ["Bede HE I.15", "Anglo-Saxon Chronicle"], "Jutish commander tracing pedigree to Woden."),
        N("eur5_cerdic_wessex", "King Cerdic of Wessex (r. 519–534 CE; Direct Male Ancestor of English Kings)", "europe_norse", 19, "d. 534 CE (Anglo-Saxon Chronicle)", "Founder of House of Wessex", ["Anglo-Saxon Chronicle", "Asser"], "Ancestor of Egbert, Alfred the Great & the modern British monarchy."),
    ]
    edges += [
        E("eur_brutus_troy", "eur5_brutus_troy", "direct", "Brutus anchor -> Brutus of Troy"),
        E("eur5_brutus_troy", "eur5_locrinus", "direct", "Brutus -> Locrinus (England)"),
        E("eur5_brutus_troy", "eur5_camber", "direct", "Brutus -> Camber (Wales)"),
        E("eur5_brutus_troy", "eur5_albanactus", "direct", "Brutus -> Albanactus (Scotland)"),
        E("eur5_locrinus", "eur5_king_lear", "direct", "Locrinus -> Bladud -> King Leir"),
        E("eur_king_arthur", "eur5_king_lear", "direct", "Arthurian anchor -> King Leir"),
        E("eur5_king_lear", "eur5_beli_mawr", "expansion", "British royal succession -> Beli Mawr"),
        E("eur5_beli_mawr", "eur5_uther_pendragon", "expansion", "Beli Mawr -> Constantine -> Uther Pendragon"),
        E("eur5_uther_pendragon", "eur5_king_arthur", "direct", "Uther Pendragon -> King Arthur"),
        E("bri_bede_heptarchy_woden", "eur5_hengist", "direct", "Woden pedigree -> Hengist of Kent"),
        E("bri_bede_heptarchy_woden", "eur5_cerdic_wessex", "direct", "Woden pedigree -> Cerdic of Wessex"),
        E("eur5_cerdic_wessex", "mon_eng_egbert", "direct", "Cerdic -> Cynric -> Ceawlin -> Ealhmund -> King Egbert of Wessex"),
    ]

    # Kievan Rus' & Pan-European Royal Marriages (Russian Primary Chronicle)
    nodes += [
        N("eur5_rurik", "Prince Rurik of Novgorod (r. 862–879 CE; Founder of Rurikid Dynasty)", "europe_norse", 20, "d. 879 CE (Russian Primary Chronicle)", "Founder of Kievan Rus'", ["Russian Primary Chronicle"], "Varangian prince invited to rule Novgorod in 862 CE."),
        N("eur5_igor_kiev", "Grand Prince Igor' of Kiev (Son of Rurik, r. 912–945 CE)", "europe_norse", 20, "d. 945 CE (Russian Primary Chronicle)", "Son of Rurik & Father of Svyatoslav", ["Russian Primary Chronicle"], "Married St. Olga of Kiev."),
        N("eur5_st_olga", "Princess St. Olga of Kiev (Regent, 945–960 CE; First Christian Rurikid Sovereign)", "europe_norse", 20, "c. 890–969 CE (Russian Primary Chronicle)", "Equal-to-the-Apostles Matriarch of Rus'", ["Russian Primary Chronicle"], "Baptized in Constantinople (957 CE); grandmother of St. Vladimir."),
        N("eur5_anne_of_kiev", "Queen Anne Yaroslavna of Kiev (Daughter of Yaroslav; Wife of King Henry I of France)", "europe_norse", 20, "c. 1030–1075 CE (Capetian Chronicles)", "Queen of France Linking Kiev to Capetians", ["Capetian Chronicles", "Primary Chronicle"], "Daughter of Yaroslav the Wise & Ingegerd of Sweden; ancestral mother of Capetian France & European royalty!"),
        N("eur5_anastasia_kiev", "Queen Anastasia Yaroslavna of Hungary (Daughter of Yaroslav; Wife of Andrew I)", "europe_norse", 20, "c. 1023–1094 CE", "Queen Consort of Hungary", ["Hungarian Chronicles"], "Mother of King Solomon of Hungary."),
        N("eur5_elizabeth_kiev", "Queen Elizabeth Yaroslavna of Norway (Daughter of Yaroslav; Wife of Harald Hardrada)", "europe_norse", 20, "c. 1025–1067 CE", "Queen of Norway", ["Heimskringla"], "Daughter of Yaroslav the Wise who wed Harald Hardrada."),
        N("eur5_vsevolod1_kiev", "Grand Prince Vsevolod I of Kiev (Son of Yaroslav the Wise; + Byzantine Princess Anastasia Monomachina)", "europe_norse", 20, "1030–1093 CE (Primary Chronicle)", "Son of Yaroslav & Father of Vladimir Monomakh", ["Russian Primary Chronicle"], "Married Byzantine imperial princess of the Monomachos house."),
        N("eur5_vladimir_monomakh", "Grand Prince Vladimir II Monomakh of Kiev (+ Gytha of Wessex, Dau. of King Harold II, r. 1113–1125)", "europe_norse", 20, "1053–1125 CE (Primary Chronicle)", "Rurikid-Byzantine-Wessex Unifier", ["Russian Primary Chronicle"], "Married Princess Gytha of England (daughter of Harold Godwinson!), uniting Kievan Rus', Byzantium & Anglo-Saxon England!", major=True),
        N("eur5_yuri_dolgoruky", "Grand Prince Yuri Dolgoruky ('Long-Arm', Son of Vladimir Monomakh; Founder of Moscow 1147)", "europe_norse", 20, "c. 1099–1157 CE (Russian Chronicles)", "Founder of Moscow & Grandfather of Nevsky", ["Laurentian Chronicle"], "Mentioned in 1147 CE as founder of Moscow; grandfather of St. Alexander Nevsky."),
    ]
    edges += [
        E("rus_rurik_dynasty", "eur5_rurik", "direct", "Rurik anchor -> Prince Rurik"),
        E("eur5_rurik", "eur5_igor_kiev", "direct", "Rurik -> son Igor' of Kiev"),
        E("eur5_igor_kiev", "eur5_st_olga", "direct", "Marriage of Igor' & St. Olga"),
        E("eur5_igor_kiev", "rus_svyatoslav", "direct", "Igor' -> Svyatoslav I"),
        E("eur5_st_olga", "rus_svyatoslav", "direct", "Mother St. Olga -> Svyatoslav I"),
        E("rus_yaroslav_wise", "eur5_anne_of_kiev", "direct", "Yaroslav the Wise -> daughter Anne of Kiev"),
        E("eur5_anne_of_kiev", "mon_fra_henry1", "direct", "Marriage of Anne of Kiev & King Henry I of France"),
        E("rus_yaroslav_wise", "eur5_anastasia_kiev", "direct", "Yaroslav -> daughter Anastasia of Hungary"),
        E("rus_yaroslav_wise", "eur5_elizabeth_kiev", "direct", "Yaroslav -> daughter Elizabeth of Norway"),
        E("eur5_elizabeth_kiev", "eur5_harald_hardrada", "direct", "Marriage of Elizabeth of Kiev & Harald Hardrada"),
        E("rus_yaroslav_wise", "eur5_vsevolod1_kiev", "direct", "Yaroslav -> son Vsevolod I of Kiev"),
        E("eur5_vsevolod1_kiev", "eur5_vladimir_monomakh", "direct", "Vsevolod I -> Vladimir II Monomakh"),
        E("mon_eng_harold2", "eur5_vladimir_monomakh", "direct", "King Harold II -> Princess Gytha -> Vladimir Monomakh"),
        E("eur5_vladimir_monomakh", "eur5_yuri_dolgoruky", "direct", "Vladimir Monomakh -> Yuri Dolgoruky (Founder of Moscow)"),
        E("eur5_yuri_dolgoruky", "mon_rus_nevsky", "direct", "Yuri Dolgoruky -> Vsevolod Big Nest -> Yaroslav II -> St. Alexander Nevsky"),
    ]

    return {
        "module": "47_wave5_india_east_asia_celtic_europe",
        "title": "Wave 5 Person-by-Person India (Epics, Maurya, Gupta, Tibet, Lanka), Imperial China/Korea, Abulghazi Turks/Seljuks, Celtic Milesians, Normandy & Kievan Rus'",
        "nodes": nodes,
        "edges": edges,
    }
