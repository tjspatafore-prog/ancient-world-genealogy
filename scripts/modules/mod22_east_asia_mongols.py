"""
Module 22: Person-by-Person East Asian & Eurasian Steppe Chronicles —
1. China: ALL 17 Xia Kings, ALL 30 Shang/Yin Kings, ALL 34 Western & Eastern Zhou Kings
   (James Legge, The Chinese Classics Vol. III: Shoo King & Annals of the Bamboo Books).
2. Japan: 7 Heavenly Kami Generations, 5 Earthly Kami Generations, ALL 25 Emperors of Nihongi Vol. I
   (Jimmu through Buretsu + Empress Jingo + Yamato Takeru) & Ancestral Clans (W.G. Aston, Nihongi Vol. I).
3. Mongols: Complete 22-Generation Borjigin Genealogy from Börte Čino & Qo'ai Maral through Alan Qo'a,
   Bodončar, Qabul Qa'an, Yisügei, Činggis Qa'an (Genghis Khan) to Batu, Güyük, Möngke & Qubilai Qa'an
   (Igor de Rachewiltz, The Secret History of the Mongols).

Wave 5: Replaced all 6 flat add_roster fans with true sequential royal & patrilineal chains.
"""

from . import N, E, add_chain


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. CHINA, JAPAN & MONGOL STRUCTURAL ANCHORS
    # -------------------------------------------------------------------------
    nodes += [
        N("chn_xia_complete", "Complete Xia Dynasty Anchor (All 17 Kings, Bamboo Books: Yu to Jie)", "chinese", 8, "c. 1989-1557 BCE (Bamboo Books Part III; Shoo King)",
          "First Hereditary Dynasty of China (17 Kings)", ["Legge Chinese Classics Vol. III (Proleg. pp. 117-127; Shoo pp. 160-171)"],
          "Anchor for all 17 Xia kings from Yu the Great to Jie, chained sequentially below.",
          ["17 Xia Kings", "Empress Min", "Tyrant Jie"], major=True),
        N("chn_shang_complete", "Complete Shang / Yin Dynasty Anchor (All 30 Kings, Bamboo Books: Tang to Di Xin)", "chinese", 11, "c. 1557-1049 BCE (Bamboo Books Part IV; Shoo King)",
          "Oracle-Bone Bronze Age Dynasty (30 Kings)", ["Legge Chinese Classics Vol. III (Proleg. pp. 128-141; Shoo pp. 193-278)"],
          "Anchor for all 30 Shang kings from Cheng Tang through Pan Geng & Wu Ding to Di Xin, chained below.",
          ["30 Shang Kings", "Pan Geng", "Tai Wu", "Wu Ding"], major=True),
        N("chn_zhou_western_eastern", "Complete Zhou Dynasty Anchor (All 34 Western & Eastern Zhou Kings, Bamboo Books)", "chinese", 14, "1049-256 BCE (Bamboo Books Part V, Proleg. pp. 142-183)",
          "Longest Dynasty in Chinese History Anchor", ["Legge Chinese Classics Vol. III (Proleg. pp. 142-183)"],
          "Anchor from Danfu & Jili -> King Wen -> King Wu -> all 12 Western & 22 Eastern Zhou kings to King Nan.",
          ["Danfu / King Tai", "King Mu of Zhou", "King Ping", "King Nan"], major=True),
        N("chn_han_tang_empires", "Imperial China Dynastic Bridges: Han Dynasty (Liu Bang → Han Wudi) & Tang Dynasty (Li Yuan → Taizong → Wu Zetian)", "chinese", 19, "202 BCE – 907 CE (Shiji; Anderson 1732 Tables 161-162)",
          "Classical Imperial Silk Road Dynasties Anchor", ["Sima Qian Shiji", "Anderson 1732 Tables 161-162"],
          "Han & Tang imperial Silk Road anchor.",
          ["Liu Bang / Han Gaozu", "Emperor Wu of Han", "Sima Qian", "Tang Taizong", "Empress Wu Zetian"], major=True),

        N("jpn_nihongi_7heaven_5earth", "Nihongi Kami Generations: 7 Heavenly Generations & 5 Earthly Generations to Jimmu", "japan_korea", 3, "Age of the Gods (Nihongi Books I-II, Aston pp. 3-108)",
          "Complete Imperial Shinto Divine Pedigree Leading to Emperor Jimmu", ["Nihongi Vol. I Books I-II (Aston pp. 3-108)"],
          "Kuni-toko-tachi -> Izanagi & Izanami -> Amaterasu -> Ninigi -> Hiko-hoho-demi -> Ugayafukiaezu -> Jimmu.",
          ["Kuni-toko-tachi", "Taka-mi-musubi", "Kono-hana-saku-ya-hime", "Ugayafukiaezu"]),
        N("jpn_nihongi_emperors_1_25", "Complete Nihongi Vol. I Imperial Line Anchor (1st Jimmu to 25th Buretsu + Empress Jingo)", "japan_korea", 17, "660 BCE – 506 CE Trad. (Nihongi Books III-XV, Aston pp. 109-407)",
          "First 25 Emperors of Japan Anchor", ["Nihongi Vol. I Books III-XV (Aston pp. 109-407)"],
          "Anchor for Emperors Jimmu through 25th Buretsu, chained individually below.",
          ["Nintoku Tenno", "Yuryaku Tenno", "Empress Jingo", "Yamato-dake"], major=True),
        N("jpn_ancestral_clans_nihongi", "Ancient Japanese Noble Clans (Nihongi): Nakatomi/Fujiwara, Imibe, Mononobe, Ohotomo & Soga", "japan_korea", 16, "Yamato Period (Nihongi Books I-XIV, Aston)",
          "Founding Aristocratic Houses of the Imperial Yamato Court", ["Nihongi Vol. I (Aston pp. 42, 128, 148, 190, 306)"],
          "Ame-no-Koyane -> Nakatomi/Fujiwara; Nigi-haya-hi -> Mononobe; Kogen -> Takechi no Sukune -> Soga.",
          ["Ame-no-Koyane (Nakatomi/Fujiwara)", "Nigi-haya-hi (Mononobe)", "Takechi no Sukune (Soga)"]),
    ]

    # -------------------------------------------------------------------------
    # 2. ALL 17 XIA KINGS (Bamboo Books Sequential Chain)
    # -------------------------------------------------------------------------
    xia_list = [
        ("chnr_xia_01_1_yu_the_great_hea_how", "1. Yu the Great (Hea-how, Founder of Xia Dynasty)"),
        ("chnr_xia_02_2_qi_k_e_son_of_yu", "2. Qi / K'e (Son of Yu the Great)"),
        ("chnr_xia_03_3_tai_kang_eldest_son_of_qi", "3. Tai Kang (Eldest Son of Qi)"),
        ("chnr_xia_04_4_zhong_kang_brother_of_tai_", "4. Zhong Kang (Brother of Tai Kang)"),
        ("chnr_xia_05_5_xiang_seang_son_of_zhong_k", "5. Xiang / Seang (Son of Zhong Kang)"),
        ("chnr_xia_06_6_shao_kang_posthumous_son_o", "6. Shao Kang (Posthumous Son of Xiang & Empress Min; Restorer)"),
        ("chnr_xia_07_7_zhu_ch_oo_son_of_shao_kang", "7. Zhu / Ch'oo (Son of Shao Kang)"),
        ("chnr_xia_08_8_huai_fun_son_of_zhu_44_yrs", "8. Huai / Fun (Son of Zhu, 44 yrs)"),
        ("chnr_xia_09_9_mang_son_of_huai_58_yrs", "9. Mang (Son of Huai, 58 yrs)"),
        ("chnr_xia_10_10_xie_se_h_son_of_mang", "10. Xie / Seëh (Son of Mang)"),
        ("chnr_xia_11_11_bu_jiang_son_of_xie_59_yr", "11. Bu Jiang (Son of Xie, 59 yrs)"),
        ("chnr_xia_12_12_jiong_keung_brother_of_bu", "12. Jiong / Keung (Brother of Bu Jiang)"),
        ("chnr_xia_13_13_jin_kin_son_of_jiong", "13. Jin / Kin (Son of Jiong)"),
        ("chnr_xia_14_14_kong_jia_son_of_bu_jiang", "14. Kong Jia (Son of Bu Jiang)"),
        ("chnr_xia_15_15_gao_haou_son_of_kong_jia", "15. Gao / Haou (Son of Kong Jia)"),
        ("chnr_xia_16_16_fa_fah_son_of_gao", "16. Fa / Fah (Son of Gao)"),
        ("chnr_xia_17_17_jie_kwei_son_of_fa_last_x", "17. Jie / Kwei (Son of Fa, Last Xia King — Overthrown by Shang)"),
    ]
    for nid, nm in xia_list:
        nodes.append(N(nid, nm, "chinese", 8, "c. 1989-1557 BCE (Bamboo Books)", "Xia Dynasty King", ["Bamboo Books (Legge Vol. III pp. 117-127)"], f"Xia Dynasty monarch: {nm}.", major=False))
    edges.append(E("chn_xia_complete", "chnr_xia_01_1_yu_the_great_hea_how", "direct", "Xia anchor -> Yu the Great"))
    edges.append(E("chnr_xia_11_11_bu_jiang_son_of_xie_59_yr", "chnr_xia_14_14_kong_jia_son_of_bu_jiang", "direct", "Bu Jiang -> son Kong Jia"))
    link_seq(edges, [x[0] for x in xia_list], "direct", "Xia Dynasty succession (Bamboo Books)")

    # -------------------------------------------------------------------------
    # 3. ALL 30 SHANG / YIN KINGS (Bamboo Books Sequential Chain)
    # -------------------------------------------------------------------------
    shg_list = [
        ("chnr_shg_01_1_tang_the_victorious_da_yi", "1. Tang the Victorious / Da Yi (Founder of Shang)"),
        ("chnr_shg_02_2_wai_bing_son_of_tang", "2. Wai Bing (Son of Tang)"),
        ("chnr_shg_03_3_zhong_ren_son_of_tang", "3. Zhong Ren (Son of Tang)"),
        ("chnr_shg_04_4_tai_jia_grandson_of_tang_v", "4. Tai Jia (Grandson of Tang via Tai Ding)"),
        ("chnr_shg_05_5_wo_ding_son_of_tai_jia", "5. Wo Ding (Son of Tai Jia)"),
        ("chnr_shg_06_6_tai_geng_xiao_geng_brother", "6. Tai Geng / Xiao Geng (Brother of Wo Ding)"),
        ("chnr_shg_07_7_xiao_jia_son_of_tai_geng", "7. Xiao Jia (Son of Tai Geng)"),
        ("chnr_shg_08_8_yong_ji_brother_of_xiao_ji", "8. Yong Ji (Brother of Xiao Jia)"),
        ("chnr_shg_09_9_tai_wu_tai_tsung_brother_o", "9. Tai Wu / Tai-tsung (Brother of Yong Ji, 75 yrs)"),
        ("chnr_shg_10_10_zhong_ding_son_of_tai_wu", "10. Zhong Ding (Son of Tai Wu)"),
        ("chnr_shg_11_11_wai_ren_brother_of_zhong_", "11. Wai Ren (Brother of Zhong Ding)"),
        ("chnr_shg_12_12_he_dan_jia_brother_of_wai", "12. He Dan Jia (Brother of Wai Ren)"),
        ("chnr_shg_13_13_zu_yi_son_of_he_dan_jia", "13. Zu Yi (Son of He Dan Jia)"),
        ("chnr_shg_14_14_zu_xin_son_of_zu_yi", "14. Zu Xin (Son of Zu Yi)"),
        ("chnr_shg_15_15_wo_jia_k_ae_keah_brother_", "15. Wo Jia / K'ae-keah (Brother of Zu Xin)"),
        ("chnr_shg_16_16_zu_ding_son_of_zu_xin", "16. Zu Ding (Son of Zu Xin)"),
        ("chnr_shg_17_17_nan_geng_son_of_wo_jia", "17. Nan Geng (Son of Wo Jia)"),
        ("chnr_shg_18_18_yang_jia_son_of_zu_ding", "18. Yang Jia (Son of Zu Ding)"),
        ("chnr_shg_19_19_pan_geng_moved_to_yin_28_", "19. Pan Geng (Brother of Yang Jia; Moved Capital to Yin, 28 yrs)"),
        ("chnr_shg_20_20_xiao_xin_brother_of_pan_g", "20. Xiao Xin (Brother of Pan Geng)"),
        ("chnr_shg_21_21_xiao_yi_brother_of_xiao_x", "21. Xiao Yi (Brother of Xiao Xin)"),
        ("chnr_shg_22_22_wu_ding_gaozong_son_of_xi", "22. Wu Ding / Gaozong (Son of Xiao Yi, 59 yrs)"),
        ("chnr_shg_23_23_zu_geng_son_of_wu_ding", "23. Zu Geng (Son of Wu Ding)"),
        ("chnr_shg_24_24_zu_jia_brother_of_zu_geng", "24. Zu Jia (Brother of Zu Geng, 33 yrs)"),
        ("chnr_shg_25_25_lin_xin_fung_sin_son_of_z", "25. Lin Xin / Fung-sin (Son of Zu Jia)"),
        ("chnr_shg_26_26_geng_ding_brother_of_lin_", "26. Geng Ding (Brother of Lin Xin)"),
        ("chnr_shg_27_27_wu_yi_son_of_geng_ding", "27. Wu Yi (Son of Geng Ding)"),
        ("chnr_shg_28_28_wen_ding_tai_ding_son_of_", "28. Wen Ding / Tai Ding (Son of Wu Yi)"),
        ("chnr_shg_29_29_di_yi_son_of_wen_ding", "29. Di Yi (Son of Wen Ding)"),
        ("chnr_shg_30_30_di_xin_king_zhou_daji_las", "30. Di Xin / King Zhou (+ Daji, Last Shang King — Fell at Muye)"),
    ]
    for nid, nm in shg_list:
        nodes.append(N(nid, nm, "chinese", 11, "c. 1557-1049 BCE (Bamboo Books)", "Shang / Yin Dynasty King", ["Bamboo Books (Legge Vol. III pp. 128-141)"], f"Shang Dynasty ruler: {nm}.", major=False))
    edges.append(E("chn_shang_complete", "chnr_shg_01_1_tang_the_victorious_da_yi", "direct", "Shang anchor -> Tang the Victorious"))
    edges.append(E("chnr_xia_17_17_jie_kwei_son_of_fa_last_x", "chnr_shg_01_1_tang_the_victorious_da_yi", "cognate", "Tang overthrows Xia Tyrant Jie"))
    link_seq(edges, [x[0] for x in shg_list], "direct", "Shang / Yin Dynasty succession (Bamboo Books)")

    # -------------------------------------------------------------------------
    # 4. ALL 34 WESTERN & EASTERN ZHOU KINGS (Bamboo Books Sequential Chain)
    # -------------------------------------------------------------------------
    zho_pre = [
        ("chnr_zho_01_danfu_old_duke_king_tai_pre_", "Old Duke Danfu / King Tai (Pre-Dynastic Ancestor of Zhou)"),
        ("chnr_zho_02_jili_king_ji_tai_ren", "Jili / King Ji (+ Tai Ren; Son of Danfu, Father of King Wen)"),
    ]
    zho_kings = [
        ("chnr_zho_03_1_king_wu_fa_conqueror_of_sh", "1. King Wu / Ji Fa (Son of King Wen; Conqueror of Shang)"),
        ("chnr_zho_04_2_king_cheng_sung_37_yrs", "2. King Cheng / Ji Song (Son of King Wu, 37 yrs)"),
        ("chnr_zho_05_3_king_kang_ch_aou_26_yrs", "3. King Kang / Ji Zhao (Son of King Cheng, 26 yrs)"),
        ("chnr_zho_06_4_king_zhao_hea", "4. King Zhao / Ji Xia (Son of King Kang)"),
        ("chnr_zho_07_5_king_mu_mwan_55_yrs", "5. King Mu / Ji Man (Son of King Zhao, 55 yrs)"),
        ("chnr_zho_08_6_king_gong_e", "6. King Gong / Ji Yi-hu (Son of King Mu)"),
        ("chnr_zho_09_7_king_yi_keen", "7. King Yi / Ji Jian (Son of King Gong)"),
        ("chnr_zho_10_8_king_xiao_peih_fang", "8. King Xiao / Ji Pifang (Brother of King Gong)"),
        ("chnr_zho_11_9_king_yi_se", "9. King Yi / Ji Xie (Son of King Yi Jian)"),
        ("chnr_zho_12_10_king_li_hoo_gonghe_regenc", "10. King Li / Ji Hu (Son of King Yi Xie; Gonghe Regency)"),
        ("chnr_zho_13_11_king_xuan_tsing_46_yrs", "11. King Xuan / Ji Jing (Son of King Li, 46 yrs)"),
        ("chnr_zho_14_12_king_you_ne_end_of_wester", "12. King You / Ji Gongnie (End of Western Zhou, 771 BCE)"),
        ("chnr_zho_15_13_king_ping_e_k_ew_1st_east", "13. King Ping / Ji Yijiu (Son of King You; 1st Eastern Zhou, 51 yrs)"),
        ("chnr_zho_16_14_king_huan", "14. King Huan of Zhou (Grandson of King Ping)"),
        ("chnr_zho_17_15_king_zhuang", "15. King Zhuang of Zhou (Son of King Huan)"),
        ("chnr_zho_18_16_king_xi", "16. King Xi of Zhou (Son of King Zhuang)"),
        ("chnr_zho_19_17_king_hui", "17. King Hui of Zhou (Son of King Xi)"),
        ("chnr_zho_20_18_king_xiang", "18. King Xiang of Zhou (Son of King Hui)"),
        ("chnr_zho_21_19_king_qing", "19. King Qing of Zhou (Son of King Xiang)"),
        ("chnr_zho_22_20_king_kuang", "20. King Kuang of Zhou (Son of King Qing)"),
        ("chnr_zho_23_21_king_ding", "21. King Ding of Zhou (Brother of King Kuang)"),
        ("chnr_zho_24_22_king_jian", "22. King Jian of Zhou (Son of King Ding)"),
        ("chnr_zho_25_23_king_ling", "23. King Ling of Zhou (Son of King Jian)"),
        ("chnr_zho_26_24_king_jing_kwei", "24. King Jing / Gui of Zhou (Son of King Ling)"),
        ("chnr_zho_27_25_king_jing_k_ae", "25. King Jing / Gai of Zhou (Son of King Jing Gui)"),
        ("chnr_zho_28_26_king_yuan", "26. King Yuan of Zhou (Son of King Jing Gai)"),
        ("chnr_zho_29_27_king_zhending", "27. King Zhending of Zhou (Son of King Yuan)"),
        ("chnr_zho_30_28_king_kao", "28. King Kao of Zhou (Son of King Zhending)"),
        ("chnr_zho_31_29_king_weilie", "29. King Weilie of Zhou (Son of King Kao)"),
        ("chnr_zho_32_30_king_an", "30. King An of Zhou (Son of King Weilie)"),
        ("chnr_zho_33_31_king_lie", "31. King Lie of Zhou (Son of King An)"),
        ("chnr_zho_34_32_king_xian", "32. King Xian of Zhou (Brother of King Lie)"),
        ("chnr_zho_35_33_king_shenjing", "33. King Shenjing of Zhou (Son of King Xian)"),
        ("chnr_zho_36_34_king_nan_last_zhou_king", "34. King Nan of Zhou (Son of King Shenjing, Last Zhou King)"),
    ]
    for nid, nm in zho_pre + zho_kings:
        nodes.append(N(nid, nm, "chinese", 15, "1049-256 BCE (Bamboo Books)", "Zhou Dynasty King", ["Bamboo Books (Legge Vol. III pp. 142-183)"], f"Zhou Dynasty ruler: {nm}.", major=False))
    edges += [
        E("chn_zhou_western_eastern", "chnr_zho_01_danfu_old_duke_king_tai_pre_", "direct", "Zhou anchor -> Old Duke Danfu"),
        E("chnr_zho_01_danfu_old_duke_king_tai_pre_", "chnr_zho_02_jili_king_ji_tai_ren", "direct", "Danfu -> son Jili (+ Tai Ren)"),
        E("chnr_zho_02_jili_king_ji_tai_ren", "chn_zhou", "direct", "Jili -> King Wen of Zhou -> King Wu"),
        E("chn_zhou", "chnr_zho_03_1_king_wu_fa_conqueror_of_sh", "direct", "King Wen -> 1. King Wu / Ji Fa"),
        E("chnr_shg_30_30_di_xin_king_zhou_daji_las", "chnr_zho_03_1_king_wu_fa_conqueror_of_sh", "cognate", "King Wu defeats Shang Di Xin at Battle of Muye (1046 BCE)"),
    ]
    link_seq(edges, [x[0] for x in zho_kings], "direct", "Zhou Dynasty father/brother succession (Bamboo Books)")

    # -------------------------------------------------------------------------
    # 5. JAPAN: ALL 25 EMPERORS OF NIHONGI VOL. I + YAMATO TAKERU (Aston)
    # -------------------------------------------------------------------------
    jpn_early = [
        ("jpnr_emp_01_2_suizei_tenno_son_of_jimmu_", "2. Emperor Suizei Tenno (Son of Jimmu & Hime-tatara-Isuzu)"),
        ("jpnr_emp_02_3_annei_tenno_son_of_suizei", "3. Emperor Annei Tenno (Son of Suizei)"),
        ("jpnr_emp_03_4_itoku_tenno_son_of_annei", "4. Emperor Itoku Tenno (Son of Annei)"),
        ("jpnr_emp_04_5_kosho_tenno_son_of_itoku", "5. Emperor Kosho Tenno (Son of Itoku)"),
        ("jpnr_emp_05_6_koan_tenno_son_of_kosho", "6. Emperor Koan Tenno (Son of Kosho)"),
        ("jpnr_emp_06_7_korei_tenno_son_of_koan", "7. Emperor Korei Tenno (Son of Koan)"),
        ("jpnr_emp_07_8_kogen_tenno_ancestor_of_so", "8. Emperor Kogen Tenno (Son of Korei; Ancestor of Soga & Abe Clans)"),
        ("jpnr_emp_08_9_kaika_tenno_son_of_kogen", "9. Emperor Kaika Tenno (Son of Kogen)"),
        ("jpnr_emp_09_10_sujin_tenno_first_histori", "10. Emperor Sujin Tenno (Son of Kaika; First Historically Attested Yamato King)"),
        ("jpnr_emp_10_11_suinin_tenno_son_of_sujin", "11. Emperor Suinin Tenno (Son of Sujin)"),
        ("jpnr_emp_11_12_keiko_tenno_father_of_yam", "12. Emperor Keiko Tenno (Son of Suinin; Father of Yamato Takeru)"),
        ("jpnr_emp_yamato_takeru", "Prince Yamato Takeru / Ousu (Son of Emperor Keiko; Father of Chuai)"),
        ("jpnr_emp_12_13_seimu_tenno_son_of_keiko", "13. Emperor Seimu Tenno (Son of Keiko; Uncle of Chuai)"),
        ("jpnr_emp_13_14_chuai_tenno_son_of_yamato", "14. Emperor Chuai Tenno (Son of Yamato Takeru)"),
        ("jpnr_emp_14_empress_jingo_regent_great_g", "Empress Jingo (Regent; Great-Grandchild of Kaika; Mother of Ojin)"),
        ("jpnr_emp_15_15_ojin_tenno_son_of_chuai_e", "15. Emperor Ojin Tenno (Son of Chuai & Empress Jingo)"),
        ("jpnr_emp_16_16_nintoku_tenno_son_of_ojin", "16. Emperor Nintoku Tenno (Son of Ojin — Daisen Kofun)"),
        ("jpnr_emp_17_17_richu_tenno_eldest_son_of", "17. Emperor Richu Tenno (Eldest Son of Nintoku)"),
        ("jpnr_emp_18_18_hanzei_tenno_brother_of_r", "18. Emperor Hanzei Tenno (Brother of Richu)"),
        ("jpnr_emp_19_19_ingyo_tenno_brother_of_ha", "19. Emperor Ingyo Tenno (Brother of Hanzei)"),
        ("jpnr_emp_20_20_anko_tenno_son_of_ingyo", "20. Emperor Anko Tenno (Son of Ingyo)"),
        ("jpnr_emp_21_21_yuryaku_tenno_5th_child_o", "21. Emperor Yuryaku Tenno (5th Child of Ingyo)"),
        ("jpnr_emp_22_22_seinei_tenno_son_of_yurya", "22. Emperor Seinei Tenno (Son of Yuryaku)"),
        ("jpnr_emp_23_23_kenzo_tenno_grandson_of_r", "23. Emperor Kenzo Tenno (Grandson of Richu)"),
        ("jpnr_emp_24_24_ninken_tenno_brother_of_k", "24. Emperor Ninken Tenno (Brother of Kenzo)"),
        ("jpnr_emp_25_25_buretsu_muretsu_tenno_son", "25. Emperor Buretsu / Muretsu Tenno (Son of Ninken, End of Nihongi Vol. I)"),
    ]
    for nid, nm in jpn_early:
        nodes.append(N(nid, nm, "japan_korea", 17, "Nihongi Books III-XV (Aston)", "Emperor / Prince of Japan", ["Nihongi Vol. I (Aston pp. 109-407)"], f"Imperial Yamato lineage: {nm}.", major=False))
    edges.append(E("jk_jimmu", "jpnr_emp_01_2_suizei_tenno_son_of_jimmu_", "direct", "Emperor Jimmu -> 2. Suizei Tenno"))
    edges.append(E("jpn_nihongi_emperors_1_25", "jpnr_emp_01_2_suizei_tenno_son_of_jimmu_", "direct", "Nihongi emperors anchor -> Suizei Tenno"))
    link_seq(edges, [x[0] for x in jpn_early], "direct", "Imperial Yamato succession (Nihongi Vol. I)")

    # -------------------------------------------------------------------------
    # 6. MONGOLS: COMPLETE 22-GENERATION BORJIGIN GENEALOGY (Secret History)
    # -------------------------------------------------------------------------
    mng_chain = [
        ("mng_borte_chino", "1. Börte Čino ('Blue-Grey Wolf') & Qo'ai Maral ('Fallow Doe')", 15, "c. 8th c. CE Mythic Origin (SHM §1)", "Heaven-Ordained Ancestors of Mongol Borjigin Lineage", "Crossed the Tenggis Sea to Burqan Qaldun (Secret History §1).", {"major": True, "altNames": ["Börte Čino", "Qo'ai Maral"]}),
        ("mng_batachiqan_to_toroqoljin", "Borjigin Ancestors Anchor (Gens 2–11: Batačiqan to Toroqoljin)", 16, "Gens 2-11 (SHM §§1-3)", "Ten Ancestral Generations Anchor", "Anchor for Gens 2-11 chained individually below.", {"altNames": ["Batačiqan", "Borjigidai Mergen", "Du'a Soqor"]}),
        ("mng_alan_qoa_bodonchar", "12–13. Dobun Mergen & Lady Alan Qo'a → Bodončar Mungqaq (Founder of Borjigin)", 17, "c. 10th c. CE (SHM §§7-44)", "Five Arrows Parable & Founder of Borjigin Clan", "Alan Qo'a bore 5 sons; youngest Bodončar Mungqaq founded the Borjigin clan.", {"major": True, "altNames": ["Alan Qo'a", "Bodončar Mungqaq", "Jamuqa (Jadaran Clan)"]}),
        ("mng_qabichi_qaidu_qabul", "Borjigin & Khamag Mongol Khagans Anchor (Qabiči Ba'atur to Bartan Ba'atur)", 18, "c. 1000-1150 CE (SHM §§43-57)", "Khamag Mongol Khagans & Barlas Clan Origin Anchor", "Menen Tudun -> Barulas (Barlas) clan; Qabul Qa'an -> Bartan Ba'atur.", {"altNames": ["Menen Tudun (Barulas)", "Qaidu", "Qabul Qa'an", "Ambaqai Qa'an", "Qutula Qa'an"]}),
        ("mng_yesugei_hoelun", "19. Yisügei Ba'atur & Lady Hö'elün (Parents of Genghis Khan)", 18, "c. 1134-1171 CE (SHM §§50-68)", "Parents of Genghis Khan", "Son of Bartan Ba'atur; fathered Temüjin (Genghis Khan) with Lady Hö'elün.", {"altNames": ["Yesügei", "Lady Hö'elün", "Joči Qasar", "Belgütei"]}),
        ("mng_genghis_khan_borte", "20. Temüjin / Činggis Qa'an (Genghis Khan, 1162–1227) & Empress Börte", 19, "1162-1227 CE (SHM §§59-268)", "Founder of the Mongol Empire", "Unified the Steppe in 1206 CE; fathered Jöči, Ča'adai, Ögödei, and Tolui with Empress Börte.", {"major": True, "altNames": ["Genghis Khan", "Temüjin", "Empress Börte"]}),
        ("mng_four_sons_grandsons", "21–22. The Four Great Chinggisid Houses Anchor (Golden Horde, Chagatai, Yuan & Ilkhanate)", 19, "1227-1368 CE (SHM §§242-282)", "Great Khans of Eurasia Anchor", "Anchor for the 4 Chinggisid imperial lines chained below.", {"major": True, "altNames": ["Jöči -> Batu Khan", "Ča'adai", "Ögödei -> Güyük", "Tolui & Sorqaqtani Beki", "Möngke", "Kublai Khan (Yuan)", "Hülegü"]}),
    ]
    add_chain(nodes, edges, mng_chain, start_parent="stp_xiongnu", start_edge_type="expansion",
              start_edge_label="Steppe Continuity -> Secret History of the Mongols (Borjigin Genealogy)",
              tradition="steppe", default_edge_type="direct", default_sources=["The Secret History of the Mongols (Rachewiltz)"])

    # Individual Borjigin ancestors (preserving every mngr_anc_* ID!)
    borj_pre = [
        ("mngr_anc_01_bata_iqan_gen_2", "Batačiqan (Gen 2, Son of Börte Čino & Qo'ai Maral)"),
        ("mngr_anc_02_tama_a_gen_3", "Tamača (Gen 3)"),
        ("mngr_anc_03_qori_ar_mergen_gen_4", "Qoričar Mergen (Gen 4)"),
        ("mngr_anc_04_a_ujam_boro_ul_gen_5", "A'ujam Boro'ul (Gen 5)"),
        ("mngr_anc_05_sali_qa_a_u_gen_6", "Sali Qača'u (Gen 6)"),
        ("mngr_anc_06_yeke_nid_n_gen_7", "Yeke Nidün (Gen 7)"),
        ("mngr_anc_07_sem_so_i_gen_8", "Sem Soči (Gen 8)"),
        ("mngr_anc_08_qar_u_gen_9", "Qarču (Gen 9)"),
        ("mngr_anc_09_borjigidai_mergen_gen_10", "Borjigidai Mergen (+ Mongqoljin Qo'a, Gen 10)"),
        ("mngr_anc_10_toroqoljin_bayan_gen_11", "Toroqoljin Bayan (+ Boroqčin Qo'a, Gen 11)"),
        ("mngr_anc_12_dobun_mergen_gen_12", "Dobun Mergen (Gen 12, Son of Toroqoljin; Husband of Alan Qo'a)"),
    ]
    borj_post = [
        ("mngr_anc_16_qabi_i_ba_atur_gen_14", "Qabiči Ba'atur (Gen 14, Son of Bodončar)"),
        ("mngr_anc_17_menen_tudun_gen_15", "Menen Tudun (Gen 15, Son of Qabiči)"),
        ("mngr_anc_18_qa_i_k_l_k_mother_nomolun_ge", "Qači Külük (+ Mother Nomolun, Gen 16)"),
        ("mngr_anc_19_qaidu_gen_17", "Qaidu Khan (Gen 17, Son of Qači Külük)"),
        ("mngr_anc_21_bai_ingqor_doq_in_gen_18", "Bai Šingqor Doqšin (Gen 18, Eldest Son of Qaidu)"),
        ("mngr_anc_22_tumbinai_se_en_gen_19", "Tumbinai Sečen (Gen 19, Father of Qabul Qa'an & Qačuli/Barlas)"),
        ("mngr_anc_23_qabul_qa_an_1st_all_mongol_q", "Qabul Qa'an (1st All-Mongol Qan; Son of Tumbinai Sečen)"),
        ("mngr_anc_25_bartan_ba_atur", "Bartan Ba'atur (Son of Qabul Qa'an; Father of Yisügei)"),
    ]
    borj_sibs = [
        ("mngr_anc_11_du_a_soqor_d_rben_clan", "Du'a Soqor (Elder Brother of Dobun Mergen; Dörben Clan)"),
        ("mngr_anc_13_b_g_n_tei_belg_n_tei", "Bügünütei & Belgünütei (Eldest Sons of Dobun Mergen & Alan Qo'a)"),
        ("mngr_anc_14_buqu_qatagi_buqatu_salji", "Buqu Qatagi & Buqatu Salji (Half-Brothers of Bodončar)"),
        ("mngr_anc_15_jajiradai_jamuqa_jadaran_cla", "Jajiradai → Jamuqa (Jadaran Clan, Anda & Rival of Genghis Khan)"),
        ("mngr_anc_20_ambaqai_qa_an_tayi_i_ut", "Ambaqai Qa'an (Descendant of Qaidu's Son Čaraqai Lingqu; Tayiči'ut)"),
        ("mngr_anc_24_qutula_qa_an", "Qutula Qa'an (Son of Qabul Qa'an; Brother of Bartan Ba'atur)"),
    ]
    for nid, nm in borj_pre + borj_post + borj_sibs:
        nodes.append(N(nid, nm, "steppe", 17 if "14" in nm or "15" in nm or "16" in nm or "17" in nm else (18 if "18" in nm or "19" in nm or "Qabul" in nm or "Qutula" in nm or "Bartan" in nm or "Ambaqai" in nm else 16),
                       "SHM Ch. 1 §§1-57", "Borjigin Ancestor / Kinsman", ["The Secret History of the Mongols (Rachewiltz §§1-57)"], f"Secret History of the Mongols figure: {nm}.", major=False))

    edges.append(E("mng_borte_chino", "mngr_anc_01_bata_iqan_gen_2", "direct", "Börte Čino -> Batačiqan"))
    edges.append(E("mng_batachiqan_to_toroqoljin", "mngr_anc_01_bata_iqan_gen_2", "direct", "Borjigin anchor -> Batačiqan"))
    link_seq(edges, [x[0] for x in borj_pre] + ["mng_alan_qoa_bodonchar"] + [x[0] for x in borj_post] + ["mng_yesugei_hoelun"], "direct", "Borjigin 22-generation patrilineal pedigree (SHM Ch. 1)")
    edges += [
        E("mngr_anc_10_toroqoljin_bayan_gen_11", "mngr_anc_11_du_a_soqor_d_rben_clan", "direct", "Toroqoljin Bayan -> eldest son Du'a Soqor"),
        E("mng_alan_qoa_bodonchar", "mngr_anc_13_b_g_n_tei_belg_n_tei", "direct", "Alan Qo'a -> sons Bügünütei & Belgünütei"),
        E("mng_alan_qoa_bodonchar", "mngr_anc_14_buqu_qatagi_buqatu_salji", "direct", "Alan Qo'a -> sons Buqu Qatagi & Buqatu Salji"),
        E("mng_alan_qoa_bodonchar", "mngr_anc_15_jajiradai_jamuqa_jadaran_cla", "direct", "Bodončar's household -> Jajiradai -> Jamuqa"),
        E("mngr_anc_19_qaidu_gen_17", "mngr_anc_20_ambaqai_qa_an_tayi_i_ut", "direct", "Qaidu -> Čaraqai Lingqu -> Sengün Bilge -> Ambaqai Qa'an"),
        E("mngr_anc_23_qabul_qa_an_1st_all_mongol_q", "mngr_anc_24_qutula_qa_an", "direct", "Qabul Qa'an -> son Qutula Qa'an"),
    ]

    # Chinggisid Imperial Children & Grandsons (True Family Tree!)
    mng_imp_nodes = [
        ("mngr_imp_01_j_i_eldest_son_of_genghis_kh", "Jöči (Eldest Son of Genghis Khan & Börte)"),
        ("mngr_imp_02_batu_khan_founder_of_golden_", "Batu Khan (Son of Jöči; Founder of the Golden Horde)"),
        ("mngr_imp_03_a_adai_2nd_son_chagatai_khan", "Ča'adai (2nd Son of Genghis Khan; Chagatai Khanate)"),
        ("mngr_imp_04_b_ri_grandson_of_a_adai", "Büri (Grandson of Ča'adai via Mö'etüken)"),
        ("mngr_imp_05_g_dei_qa_an_2nd_great_khan_t", "Ögödei Qa'an (3rd Son of Genghis Khan; 2nd Great Khan, + Töregene)"),
        ("mngr_imp_06_g_y_k_qa_an_3rd_great_khan", "Güyük Qa'an (Son of Ögödei & Töregene; 3rd Great Khan)"),
        ("mngr_imp_07_prince_tolui_4th_son", "Prince Tolui (4th Son of Genghis Khan & Börte)"),
        ("mngr_imp_08_sorqaqtani_beki_kereyit_prin", "Empress Sorqaqtani Beki (Kereyit Princess; Wife of Tolui)"),
        ("mngr_imp_09_m_ngke_qa_an_4th_great_khan", "Möngke Qa'an (Eldest Son of Tolui & Sorqaqtani; 4th Great Khan)"),
        ("mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "Qubilai Qa'an / Kublai Khan (Son of Tolui & Sorqaqtani; Yuan Emperor)"),
        ("mngr_imp_11_h_leg_khan_ilkhanate_of_pers", "Hülegü Khan (Son of Tolui & Sorqaqtani; Ilkhan of Persia)"),
        ("mngr_imp_12_timur_tamerlane_barlas_clan_", "Amir Timur / Tamerlane (Barlas Clan from Tumbinai's Son Qačuli -> Babur / Mughals)"),
    ]
    for nid, nm in mng_imp_nodes:
        nodes.append(N(nid, nm, "steppe", 19, "1206-1405 CE (SHM & Timurid Chronicles)", "Chinggisid / Barlas Imperial Ruler", ["The Secret History of the Mongols (Rachewiltz)"], f"Chinggisid/Timurid imperial lineage: {nm}.", major=False))

    edges += [
        E("mng_genghis_khan_borte", "mngr_imp_01_j_i_eldest_son_of_genghis_kh", "direct", "Genghis Khan & Börte -> eldest son Jöči"),
        E("mngr_imp_01_j_i_eldest_son_of_genghis_kh", "mngr_imp_02_batu_khan_founder_of_golden_", "direct", "Jöči -> Batu Khan (Golden Horde)"),
        E("mng_genghis_khan_borte", "mngr_imp_03_a_adai_2nd_son_chagatai_khan", "direct", "Genghis Khan & Börte -> 2nd son Ča'adai"),
        E("mngr_imp_03_a_adai_2nd_son_chagatai_khan", "mngr_imp_04_b_ri_grandson_of_a_adai", "direct", "Ča'adai -> Mö'etüken -> Büri"),
        E("mng_genghis_khan_borte", "mngr_imp_05_g_dei_qa_an_2nd_great_khan_t", "direct", "Genghis Khan & Börte -> 3rd son Ögödei Qa'an"),
        E("mngr_imp_05_g_dei_qa_an_2nd_great_khan_t", "mngr_imp_06_g_y_k_qa_an_3rd_great_khan", "direct", "Ögödei & Töregene -> Güyük Qa'an"),
        E("mng_genghis_khan_borte", "mngr_imp_07_prince_tolui_4th_son", "direct", "Genghis Khan & Börte -> 4th son Tolui"),
        E("mngr_imp_07_prince_tolui_4th_son", "mngr_imp_08_sorqaqtani_beki_kereyit_prin", "direct", "Marriage of Prince Tolui & Sorqaqtani Beki"),
        E("mngr_imp_07_prince_tolui_4th_son", "mngr_imp_09_m_ngke_qa_an_4th_great_khan", "direct", "Tolui -> eldest son Möngke Qa'an"),
        E("mngr_imp_08_sorqaqtani_beki_kereyit_prin", "mngr_imp_09_m_ngke_qa_an_4th_great_khan", "direct", "Mother Sorqaqtani Beki -> Möngke Qa'an"),
        E("mngr_imp_07_prince_tolui_4th_son", "mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "direct", "Tolui -> son Kublai Khan"),
        E("mngr_imp_08_sorqaqtani_beki_kereyit_prin", "mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "direct", "Mother Sorqaqtani Beki -> Kublai Khan"),
        E("mngr_imp_07_prince_tolui_4th_son", "mngr_imp_11_h_leg_khan_ilkhanate_of_pers", "direct", "Tolui -> son Hülegü Khan (Ilkhanate)"),
        E("mngr_imp_08_sorqaqtani_beki_kereyit_prin", "mngr_imp_11_h_leg_khan_ilkhanate_of_pers", "direct", "Mother Sorqaqtani Beki -> Hülegü Khan"),
        E("mngr_anc_22_tumbinai_se_en_gen_19", "mngr_imp_12_timur_tamerlane_barlas_clan_", "direct", "Tumbinai Sečen -> Qačuli -> Barlas Clan -> Amir Timur"),
        E("mngr_imp_12_timur_tamerlane_barlas_clan_", "mug_babur_humayun", "direct", "Timur -> Miran Shah -> Umar Shaikh II -> Emperor Babur"),
        E("mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "chn_han_tang_empires", "cognate", "Kublai Khan establishes the Yuan Dynasty of China (1271 CE)"),
    ]

    # Cross-links into existing graph
    edges += [
        E("chn_yu_xia", "chn_xia_complete", "direct", "All 17 Xia Kings from Yu to Jie (Legge Bamboo Books)"),
        E("chn_shang", "chn_shang_complete", "direct", "All 30 Shang/Yin Kings from Tang to Di Xin (Legge Bamboo Books)"),
        E("chn_zhou", "chn_zhou_western_eastern", "direct", "All 34 Western & Eastern Zhou Kings (Legge Bamboo Books)"),
        E("chn_boyi_qin", "chn_han_tang_empires", "expansion", "Qin -> Han Dynasty (Silk Road) -> Tang Dynasty"),
        E("jk_izanagi_amaterasu", "jpn_nihongi_7heaven_5earth", "direct", "Complete 7 Heavenly & 5 Earthly Kami Generations (Aston Nihongi)"),
        E("jk_jimmu", "jpn_nihongi_emperors_1_25", "direct", "Complete 1st–25th Emperors of Japan in Nihongi Vol. I"),
        E("jpn_nihongi_7heaven_5earth", "jpn_ancestral_clans_nihongi", "direct", "Heavenly Kami ancestors of Nakatomi, Imibe, Mononobe & Ohotomo clans"),
        E("mng_four_sons_grandsons", "mngr_imp_01_j_i_eldest_son_of_genghis_kh", "direct", "Chinggisid Four Houses anchor -> Jöči"),
        E("dna_d_c_n_asia", "mng_genghis_khan_borte", "genetic", "Steppe Y-DNA Haplogroup C2b1a2 (Star-Cluster associated with Mongol expansion)"),
    ]

    return {
        "module": "22_east_asia_bamboo_nihongi_mongols",
        "title": "Complete Chinese Xia/Shang/Zhou King Lists (Legge Bamboo Books), Nihongi Vol. I Kami & 25 Emperors (Aston), & Complete Secret History of the Mongols Borjigin Genealogy (Rachewiltz)",
        "nodes": nodes,
        "edges": edges,
    }
