"""
Module 19: Person-by-Person Caucasian / Georgian Chronicles (Kartlis Tskhovreba),
Al-Biruni's Chronology of Ancient Nations (Parthian/Ashkanian, Sasanian,
Afrighid Khwarazmia, Himyarite & Lakhmid), and Budge's Ethiopic Kebra Nagast.

Wave 4: Replaced all 6 flat add_roster fans with true sequential parent->child & dynastic chains.
"""

from . import N, E


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. CAUCASIAN, BIRUNI & KEBRA NAGAST STRUCTURAL ANCHORS
    # -------------------------------------------------------------------------
    nodes += [
        N("geo_targamos_8sons", "Targamos / Togarmah (Patriarch of All Caucasian Nations, Kartlis Tskhovreba)", "iranian", 7, "Caucasian Table of Nations (Kartlis Tskhovreba pp. 13-18)",
          "Patriarchal Origin of All Peoples of the Caucasus", ["Kartlis Tskhovreba (Leonti Mroveli pp. 13-18)"],
          "Targamos (Togarmah, lived 600 yrs between Mt. Ararat & Masis) divided the Caucasus among 8 sons (Haos, Kartlos, Bardos, Movak'an, Lek', Heros, K'avk'as, Egros) + Uobos.",
          ["Haos / Hayk (Armenia)", "Kartlos (Georgia)", "K'avk'as", "Egros", "Lek'", "Uobos (Ossetians)"], major=True),
        N("geo_kartlos_5sons_uplos", "Kartlos's Proto-Georgian Branch Anchor (Mtskhetos to Uplos)", "iranian", 8, "Proto-Georgian Heroic Era (Kartlis Tskhovreba p. 16)",
          "Founders of Mtskheta, Kakheti, Gardabani, Uplistsikhe & Javakheti Anchor", ["Kartlis Tskhovreba (Leonti Mroveli p. 16)"],
          "Bridge from Kartlos's sons Mtskhetos and Uplos down to King Parnavaz I of Kartli.",
          ["Mtskhetos", "Uplos", "K'akhos", "Javakhos"]),
        N("geo_parnavaz_nebrothids", "Kings of Iberia / Kartli Anchor (Pharnavazids, Nebrotids & Arshak'ids)", "iranian", 18, "c. 299 BCE - 284 CE (Kartlis Tskhovreba pp. 22-41)",
          "First Royal Dynasties of Georgia & Creator of Georgian Script Anchor", ["Kartlis Tskhovreba (Leonti Mroveli pp. 22-41)"],
          "Anchor linking Parnavaz I through Mirvan I (Nebrotid), Arshak' I, Parsman, and Aspagur to Abeshuru.",
          ["King Parnavaz I", "Saurmag", "Mirvan I (Nebrotid)", "Aderk'i", "Parsman the Valiant"], major=True),
        N("geo_chosroids_mirian_vakhtang", "Chosroid (Mihranid-Sasanian) Dynasty Anchor (Mirian III to Vakht'ang Gorgasali)", "iranian", 19, "284-580 CE (Kartlis Tskhovreba pp. 41-108)",
          "Christianizers of Georgia & Founder of Tbilisi Anchor", ["Kartlis Tskhovreba (Leonti Mroveli & Juansher pp. 41-108)"],
          "Mirian III (Mikhran, Sasanian prince + Abeshuru + St. Nino) -> Bakar -> Archil -> Vakht'ang I Gorgasali -> Dachi.",
          ["King Mirian III & St. Nino", "Vakht'ang Gorgasali", "King Dachi"], major=True),
        N("geo_bagrationi_davidic", "Bagrat'ioni Royal House Anchor (Sumbat Davitisdze Davidic Claim)", "iranian", 19, "588-1213 CE (Kartlis Tskhovreba, Sumbat Davitisdze pp. 211-217)",
          "Longest-Reigning Christian Royal House (Davidic Claim Anchor)", ["Kartlis Tskhovreba (Sumbat Davitisdze pp. 211-217)"],
          "Unrolled person-by-person below from Bagrat' and Guaram I through Ashot' I, Bagrat' III, David IV, and Queen Tamar.",
          ["Guaram Kuropalates", "Ashot' I the Great", "Bagrat' III", "David IV the Builder", "Queen Tamar"], major=True),

        N("bir_parthians_ashkanians", "Parthian / Ashkanian Empire Anchor (Al-Biruni -> Kayanian Siyavush)", "iranian", 18, "247 BCE - 224 CE (Al-Biruni pp. 116-120; Betham Tab. CV)",
          "470-Year Iranian Superpower Bridged to Kayanian Siyavush", ["Al-Biruni Chronology (Sachau pp. 116-120, 401)", "Betham 1795 Tab. CV"],
          "Al-Biruni (p. 116) traces Ashk ben Ashkan (Arsaces I) directly back to Kayanian Prince Siyavush; unrolled individually in Wave 4.",
          ["Arsaces I / Ashk", "Mithridates I & II of Parthia", "Orodes II", "Vologases I", "Artabanus IV"], major=True),
        N("bir_sasanians_complete", "Sasanian Empire Anchor (Al-Biruni Pedigree from Kay Bahman & Esfandiyar)", "iranian", 19, "224-651 CE (Al-Biruni pp. 45-48, 122-130; Betham Tab. CVI-CVII)",
          "Last Pre-Islamic Persian Empire Anchor", ["Al-Biruni Chronology (Sachau pp. 45-48, 122-130)"],
          "Al-Biruni (p. 122) traces Ardashir I -> Babak -> Sasan -> Bahman -> Isfandiyar; unrolled person-by-person below.",
          ["Ardashir I", "Shapur I & II", "Bahram V Gur", "Khosrow I Anushirvan", "Khosrow II", "Yazdegerd III"], major=True),
        N("bir_khwarazm_afrighids", "Afrighid Shahs of Khwarazm Anchor (22 Generations in Al-Biruni)", "iranian", 19, "305-995 CE (Al-Biruni pp. 40-42, 379)",
          "Al-Biruni's Homeland Dynasty — 22 Unbroken Generations Anchor", ["Al-Biruni Chronology (Sachau pp. 40-42, 379)"],
          "22 unbroken father-to-son Khwarazmshahs from Afrigh (305 CE) to Abu 'Abdallah Muhammad (d. 995 CE), chained individually below.",
          ["Afrigh (305 CE)", "Arthamukh", "Askajamuk", "Shawushfar", "Abu 'Abdallah Muhammad"], major=True),
        N("bir_himyar_lakhmid_ghassan", "Pre-Islamic Arab Kingdoms Anchor (Himyarite Tubbas, Lakhmids & Ghassanids)", "arabian", 19, "c. 110 BCE - 636 CE (Al-Biruni pp. 40-50, 311, 384; Kebra Nagast Ch. 117)",
          "Qahtanite / South Arabian & Syro-Mesopotamian Arab Monarchies Anchor", ["Al-Biruni Chronology (pp. 40-50, 311, 384)", "Kebra Nagast Ch. 117"],
          "Himyarite Tubbas, Lakhmid kings of Al-Hirah, and Christian Ghassanid kings of Syria.",
          ["Himyarite Tubbas", "Dhu-Nuwas (Yusuf As'ar)", "Al-Mundhir & Al-Nu'man (Lakhmids)", "Ghassanids"], major=True),

        N("keb_premakeda_tamrin_azaryas", "Kebra Nagast Royal Court & Pre-Makeda Kings Anchor", "african", 16, "c. 960 BCE (Kebra Nagast Ch. 22-48, Intro p. xxxv)",
          "Bearers of the Ark of Zion from Jerusalem to Aksum Anchor", ["Kebra Nagast (Budge 1922 Intro p. xxxv, Ch. 22-48, p. 62)"],
          "5 pre-Makeda kings, Merchant Tamrin, and High Priest 'Azaryas (son of Zadok) + 21 Israelite firstborn nobles.",
          ["Tamrin", "'Azaryas son of Zadok", "21 Israelite Firstborn Nobles", "Gedur / Kawnasya"]),
        N("keb_adrami_rome_shem", "Kebra Nagast World-Kingdoms Bridge ('Adrami, Fares & 'Akamhel)", "african", 16, "Kebra Nagast Ch. 72-81 (Budge pp. 121-140)",
          "Ethiopic Universal Bridge of Rome, Persia & Philistia to Israel", ["Kebra Nagast (Budge 1922 Ch. 72-81, pp. 121-140)"],
          "Solomon's youngest son 'Adrami marries 'Adlonya to rule Rome; Perez (Fares) -> Persia; Samson + Delilah -> 'Akamhel.",
          ["'Adrami (Solomonic King of Rome)", "Zanbares & Baltasar", "'Akamhel (Son of Samson)"]),
        N("keb_kaleb_gabramaskal_yekuno", "Aksumite & Solomonic Restoration Anchor (King Kaleb -> Gabra Maskal -> Yekuno 'Amlak)", "african", 19, "c. 520-1285 CE (Kebra Nagast Ch. 117 & Colophon, Budge pp. 225-229)",
          "6th-Century Aksumite Expedition & 1270 CE Restoration Anchor", ["Kebra Nagast (Budge 1922 Ch. 117, pp. 225-229)"],
          "King Kaleb defeated Himyarite Dhu-Nuwas in Yemen (525 CE); restored under Yekuno 'Amlak in 1270 CE.",
          ["King Kaleb of Aksum", "Gabra Maskal", "Takla Haymanot (Zagwe)", "Emperor Yekuno 'Amlak"], major=True),
    ]

    # -------------------------------------------------------------------------
    # 2. CAUCASIAN TABLE OF NATIONS — INDIVIDUAL SONS & GRANDSONS
    # -------------------------------------------------------------------------
    cauc_nodes = [
        ("geor_8s_01_haos_hayk_progenitor_of_arme", "Haos / Hayk (Eldest Son of Targamos; Progenitor of Armenians)", 7, "Kartlis Tskhovreba pp. 13-15"),
        ("geor_8s_02_kartlos_progenitor_of_georgi", "Kartlos (2nd Son of Targamos; Progenitor of Georgians)", 7, "Kartlis Tskhovreba pp. 13-16"),
        ("geor_8s_03_bardos_founder_of_barda", "Bardos (Son of Targamos; Founder of Barda)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_04_movak_an_founder_of_movak_ne", "Movak'an (Son of Targamos; Founder of Movak'neti / Albania)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_05_lek_progenitor_of_lezgins_da", "Lek' (Son of Targamos; Progenitor of Lezgins / Dagestan)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_06_heros_founder_of_hereti", "Heros (Son of Targamos; Founder of Hereti)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_07_k_avk_as_durdzuk_north_cauca", "K'avk'as (Son of Targamos; Progenitor of North Caucasians)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_durdzuk", "Durdzuk' (Renowned Son of K'avk'as; Eponym of Vainakhs)", 8, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_08_egros_founder_of_egrisi_colc", "Egros (Son of Targamos; Founder of Egrisi / Colchis)", 7, "Kartlis Tskhovreba p. 14"),
        ("geor_8s_09_uobos_khazar_ancestor_of_oss", "Uobos (Khazar-Targamosid Ancestor of Ossetians)", 8, "Kartlis Tskhovreba p. 17"),
        ("geor_8s_10_mtskhetos_uplos_odzrkhos_jav", "Mtskhetos (Eldest Son of Kartlos; Founder of Mtskheta)", 8, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_uplos", "Uplos (Eldest Son of Mtskhetos; Builder of Uplistsikhe)", 9, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_odzrkhos", "Odzrkhos (Son of Mtskhetos; Eponym of Odzrkhe)", 9, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_javakhos", "Javakhos (Son of Mtskhetos; Eponym of Javakheti)", 9, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_11_gardabos_k_akhos_k_ukhos_gac", "Gardabos (Son of Kartlos; Eponym of Gardabani)", 8, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_kakhos", "K'akhos (Son of Kartlos; Eponym of Kakheti)", 8, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_kukhos", "K'ukhos (Son of Kartlos; Eponym of Kukheti)", 8, "Kartlis Tskhovreba p. 16"),
        ("geor_8s_gachios", "Gachios (Son of Kartlos; Founder of Gachiani)", 8, "Kartlis Tskhovreba p. 16"),
    ]
    for nid, nm, tr, dt in cauc_nodes:
        nodes.append(N(nid, nm, "iranian", tr, dt, "Caucasian Eponymous Ancestor", ["Kartlis Tskhovreba (Leonti Mroveli)"], f"Caucasian chronicle ancestor: {nm}.", major=False))

    edges += [
        E("geo_targamos_8sons", "geor_8s_01_haos_hayk_progenitor_of_arme", "direct", "Targamos -> eldest son Haos"),
        E("geor_8s_01_haos_hayk_progenitor_of_arme", "arm_hayk_pat", "cognate", "Georgian Haos = Armenian Hayk Nahapet"),
        E("geo_targamos_8sons", "geor_8s_02_kartlos_progenitor_of_georgi", "direct", "Targamos -> son Kartlos"),
        E("geo_targamos_8sons", "geor_8s_03_bardos_founder_of_barda", "direct", "Targamos -> son Bardos"),
        E("geo_targamos_8sons", "geor_8s_04_movak_an_founder_of_movak_ne", "direct", "Targamos -> son Movak'an"),
        E("geo_targamos_8sons", "geor_8s_05_lek_progenitor_of_lezgins_da", "direct", "Targamos -> son Lek'"),
        E("geo_targamos_8sons", "geor_8s_06_heros_founder_of_hereti", "direct", "Targamos -> son Heros"),
        E("geo_targamos_8sons", "geor_8s_07_k_avk_as_durdzuk_north_cauca", "direct", "Targamos -> son K'avk'as"),
        E("geor_8s_07_k_avk_as_durdzuk_north_cauca", "geor_8s_durdzuk", "direct", "K'avk'as -> son Durdzuk'"),
        E("geo_targamos_8sons", "geor_8s_08_egros_founder_of_egrisi_colc", "direct", "Targamos -> son Egros"),
        E("geo_targamos_8sons", "geor_8s_09_uobos_khazar_ancestor_of_oss", "expansion", "Targamosids / Khazar line -> Uobos"),
        E("geor_8s_02_kartlos_progenitor_of_georgi", "geor_8s_10_mtskhetos_uplos_odzrkhos_jav", "direct", "Kartlos -> eldest son Mtskhetos"),
        E("geor_8s_02_kartlos_progenitor_of_georgi", "geor_8s_11_gardabos_k_akhos_k_ukhos_gac", "direct", "Kartlos -> son Gardabos"),
        E("geor_8s_02_kartlos_progenitor_of_georgi", "geor_8s_kakhos", "direct", "Kartlos -> son K'akhos"),
        E("geor_8s_02_kartlos_progenitor_of_georgi", "geor_8s_kukhos", "direct", "Kartlos -> son K'ukhos"),
        E("geor_8s_02_kartlos_progenitor_of_georgi", "geor_8s_gachios", "direct", "Kartlos -> son Gachios"),
        E("geor_8s_10_mtskhetos_uplos_odzrkhos_jav", "geor_8s_uplos", "direct", "Mtskhetos -> eldest son Uplos"),
        E("geor_8s_10_mtskhetos_uplos_odzrkhos_jav", "geor_8s_odzrkhos", "direct", "Mtskhetos -> son Odzrkhos"),
        E("geor_8s_10_mtskhetos_uplos_odzrkhos_jav", "geor_8s_javakhos", "direct", "Mtskhetos -> son Javakhos"),
    ]

    # -------------------------------------------------------------------------
    # 3. KINGS OF KARTLI / IBERIA — SEQUENTIAL CHAIN (Uplos -> Parnavaz -> Vakht'ang -> Bak'ur)
    # -------------------------------------------------------------------------
    kartli_list = [
        ("geor_kgs_01_1_parnavaz_i_1st_king_of_kar", "1. King Parnavaz I of Kartli (Creator of Georgian Script, r. c. 299–234 BCE)"),
        ("geor_kgs_02_2_saurmag_i", "2. King Saurmag I of Kartli (Son of Parnavaz I)"),
        ("geor_kgs_03_3_mirvan_i_nebrotid", "3. King Mirvan I (Nebrotid / Adopted Son-in-Law of Saurmag I)"),
        ("geor_kgs_04_4_parnajom", "4. King Parnajom (Son of Mirvan I)"),
        ("geor_kgs_05_5_arshak_i_arshak_id", "5. King Arshak' I of Kartli (Armenian-Arshak'id; Wed Daughter of Parnavazid Line)"),
        ("geor_kgs_06_6_art_ag", "6. King Art'ag of Kartli (Son of Arshak' I)"),
        ("geor_kgs_07_7_bart_om_i", "7. King Bart'om I of Kartli (Son of Art'ag)"),
        ("geor_kgs_08_8_mirvan_ii", "8. King Mirvan II of Kartli (Son of Parnajom)"),
        ("geor_kgs_09_9_arshak_ii", "9. King Arshak' II of Kartli (Son of Mirvan II & Pharnavazid Mother)"),
        ("geor_kgs_10_10_aderk_i_birth_of_christ_e", "10. King Aderk'i / Pharasmanes I (Grandson of Bart'om I; Reign at Birth of Christ)"),
        ("geor_kgs_11_15_parsman_the_valiant_queen", "15. King Parsman II the Valiant (+ Queen Gadana of Armenia)"),
        ("geor_kgs_12_19_rev_i_the_righteous", "19. King Rev I the Righteous (Grandson of Parsman the Valiant)"),
        ("geor_kgs_13_23_aspagur_last_male_pharnav", "23. King Aspagur (Last Male Pharnavazid Ruler of Kartli)"),
        ("geor_kgs_abeshuru", "Princess Abeshuru (Daughter & Heiress of Aspagur; Wife of Mirian III)"),
        ("geor_kgs_14_24_mirian_iii_queen_nana_st_", "24. King Mirian III of Iberia (+ Queen Nana & St. Nino; Christianized Georgia 337 CE)"),
        ("geor_kgs_15_25_bakar_26_mirdat_27_varaz_", "25. King Bakar I of Iberia (Son of Mirian III & Nana)"),
        ("geor_kgs_mirdat3", "26. King Mirdat' III of Iberia (Son of Bakar I)"),
        ("geor_kgs_varaz_bakar", "27. King Varaz-Bakar of Iberia (Son of Mirdat' III)"),
        ("geor_kgs_16_31_archil_32_mirdat", "31. King Archil I of Iberia (Son of Mirdat' IV)"),
        ("geor_kgs_mirdat5", "32. King Mirdat' V of Iberia (Son of Archil I; Father of Vakht'ang Gorgasali)"),
        ("geor_kgs_17_33_vakht_ang_i_gorgasali_fou", "33. King Vakht'ang I Gorgasali (Son of Mirdat' V; Founder of Tbilisi, 5th c.)"),
        ("geor_kgs_18_34_king_dachi_bak_ur", "34. King Dachi of Iberia (Son of Vakht'ang I Gorgasali)"),
        ("geor_kgs_bakur", "35. King Bak'ur II of Iberia (Son of King Dachi)"),
    ]
    for nid, nm in kartli_list:
        nodes.append(N(nid, nm, "iranian", 18 if "299" in nm or "Mirvan" in nm or "Aderk" in nm or "Arshak" in nm or "Saurmag" in nm or "Parnajom" in nm or "Art'ag" in nm or "Bart'om" in nm or "Parsman" in nm or "Rev I" in nm or "Aspagur" in nm else 19,
                       "299 BCE - 580 CE (Kartlis Tskhovreba)", "King of Kartli / Iberia", ["Kartlis Tskhovreba (pp. 22-108)"], f"Iberian royal figure: {nm}.", major=False))
    edges.append(E("geor_8s_uplos", "geor_kgs_01_1_parnavaz_i_1st_king_of_kar", "expansion", "Line of Uplos -> King Parnavaz I"))
    edges.append(E("geo_parnavaz_nebrothids", "geor_kgs_01_1_parnavaz_i_1st_king_of_kar", "direct", "Iberian royal anchor link"))
    link_seq(edges, [x[0] for x in kartli_list], "direct", "Successive Kings of Kartli / Iberia (Kartlis Tskhovreba)")

    # -------------------------------------------------------------------------
    # 4. BAGRAT'IONI ROYAL HOUSE — PERSON-BY-PERSON CHAIN TO 1213 CE
    # -------------------------------------------------------------------------
    bag_list = [
        ("geor_bag_01_bagrat_founder_of_armenian_g", "Bagrat' (Patriarch of the Armenian & Georgian Bagratids)"),
        ("geor_bag_02_guaram_i_kuropalates", "Guaram I Kuropalates of Iberia (c. 588–590 CE)"),
        ("geor_bag_03_st_epanoz_i_demet_re_jvari_c", "St'epanoz I of Iberia (Son of Guaram I; Builder of Jvari)"),
        ("geor_bag_04_ashot_i_kuropalates_the_grea", "Ashot' I Kuropalates the Great (d. 826 CE)"),
        ("geor_bag_05_bagrat_i_david_i_kuropalates", "Bagrat' I Kuropalates (Son of Ashot' I the Great)"),
        ("geor_bag_david1", "David I Kuropalates (Son of Bagrat' I)"),
        ("geor_bag_06_adarnase_iv_king_of_the_kart", "King Adarnase IV of the Kartvels (Son of David I, d. 923)"),
        ("geor_bag_07_david_iii_the_great_kuropala", "David III the Great Kuropalates of Tao (Grandson of Adarnase IV, d. 1001)"),
        ("geor_bag_08_gurgen_king_of_kings_d_1008", "Gurgen, King of Kings (Grandson of Adarnase IV; Father of Bagrat' III, d. 1008)"),
        ("geor_bag_09_bagrat_iii_1st_king_of_unifi", "King Bagrat' III (Son of Gurgen; Adopted Heir of David III; 1st King of Unified Georgia, 1008–1014)"),
        ("geor_bag_10_king_giorgi_i", "King Giorgi I of Georgia (Son of Bagrat' III, r. 1014–1027)"),
        ("geor_bag_11_king_david_iv_the_builder_10", "King David IV the Builder (Grandson of Giorgi I via Bagrat IV & Giorgi II, r. 1089–1125)"),
        ("geor_bag_12_queen_tamar_the_great_1184_1", "Queen Tamar the Great (Great-Granddaughter of David IV via Demetrius I & Giorgi III, r. 1184–1213)"),
    ]
    for nid, nm in bag_list:
        nodes.append(N(nid, nm, "iranian", 19, "588-1213 CE (Sumbat Davitisdze)", "Bagrat'ioni Monarch", ["Kartlis Tskhovreba (Sumbat Davitisdze pp. 211-217)"], f"Georgian Bagrat'ioni monarch: {nm}.", major=False))
    nodes.append(N("geor_bag_demetre", "Demet're Hypatos (Brother of St'epanoz I; Builder of Mtskheta Jvari)", "iranian", 19, "c. 600 CE (Kartlis Tskhovreba)", "Iberian Bagratid-Guaramid Prince", ["Kartlis Tskhovreba"], "Brother of St'epanoz I commemorated in the relief of Jvari Monastery."))
    edges.append(E("geo_bagrationi_davidic", "geor_bag_01_bagrat_founder_of_armenian_g", "direct", "Davidic Bagrat'ioni claim -> Bagrat'"))
    link_seq(edges, [x[0] for x in bag_list], "direct", "Bagrat'ioni royal succession")
    edges.append(E("geor_bag_02_guaram_i_kuropalates", "geor_bag_demetre", "direct", "Guaram I -> son Demet're Hypatos"))
    edges.append(E("geor_bag_12_queen_tamar_the_great_1184_1", "mod_geo_tamar_to_constantine2", "direct", "Queen Tamar -> Late Medieval Bagrationis"))

    # -------------------------------------------------------------------------
    # 5. AL-BIRUNI'S 22 AFRIGHID SHAHS OF KHWARAZM (305-995 CE Unbroken Chain)
    # -------------------------------------------------------------------------
    afr_list = [
        ("birr_afr_01_1_afrigh_305_ce", "1. Afrigh (Founder of Afrighid Castle, 305 CE)"),
        ("birr_afr_02_2_baghra", "2. Baghra ibn Afrigh"),
        ("birr_afr_03_3_sakhassak", "3. Sakhassak ibn Baghra"),
        ("birr_afr_04_4_askajamuk_i", "4. Askajamuk I ibn Sakhassak"),
        ("birr_afr_05_5_azkajawar_i", "5. Azkajawar I ibn Askajamuk"),
        ("birr_afr_06_6_sakhr_i", "6. Sakhr I ibn Azkajawar"),
        ("birr_afr_07_7_shawush", "7. Shawush ibn Sakhr"),
        ("birr_afr_08_8_khamgri", "8. Khamgri ibn Shawush"),
        ("birr_afr_09_9_buzkar", "9. Buzkar ibn Khamgri"),
        ("birr_afr_10_10_arthamukh_time_of_prophet", "10. Arthamukh ibn Buzkar (Time of Prophet Muhammad)"),
        ("birr_afr_11_11_sakhr_ii", "11. Sakhr II ibn Arthamukh"),
        ("birr_afr_12_12_sabri", "12. Sabri ibn Sakhr II"),
        ("birr_afr_13_13_azkajawar_ii", "13. Azkajawar II ibn Sabri"),
        ("birr_afr_14_14_askajamuk_ii", "14. Askajamuk II ibn Azkajawar II"),
        ("birr_afr_15_15_shawushfar", "15. Shawushfar ibn Askajamuk II"),
        ("birr_afr_16_16_turkasbatha", "16. Turkasbatha ibn Shawushfar"),
        ("birr_afr_17_17_abdallah", "17. 'Abdallah ibn Turkasbatha"),
        ("birr_afr_18_18_mansur", "18. Mansur ibn 'Abdallah"),
        ("birr_afr_19_19_irak", "19. 'Irak ibn Mansur"),
        ("birr_afr_20_20_muhammad", "20. Muhammad ibn 'Irak"),
        ("birr_afr_21_21_ahmad", "21. 'Ahmad ibn Muhammad"),
        ("birr_afr_22_22_abu_abdallah_muhammad_las", "22. Abu 'Abdallah Muhammad (Last Afrighid Shah, d. 995 CE)"),
    ]
    for nid, nm in afr_list:
        nodes.append(N(nid, nm, "iranian", 19, "305-995 CE (Al-Biruni pp. 40-42)", "Afrighid Shah of Khwarazm", ["Al-Biruni Chronology (Sachau pp. 40-42)"], f"Afrighid Khwarazmshah in Al-Biruni's unbroken 22-generation list: {nm}.", major=False))
    edges.append(E("bir_khwarazm_afrighids", "birr_afr_01_1_afrigh_305_ce", "direct", "Al-Biruni Afrighid anchor -> Afrigh"))
    link_seq(edges, [x[0] for x in afr_list], "direct", "Father-to-son Khwarazmshah succession (Al-Biruni pp. 40-42)")

    # -------------------------------------------------------------------------
    # 6. SASANIAN DYNASTY — INDIVIDUALIZED CHAIN (Sasan -> Yazdegerd III + Buwayhids/Samanids)
    # -------------------------------------------------------------------------
    sas_list = [
        ("birr_sas_01_sasan_papak_ancestors_of_sas", "Sasan (Priest of Istakhr; Ancestor of the Sasanian Dynasty)"),
        ("birr_sas_papak", "Papak (Son of Sasan; King of Persis & Father of Ardashir I)"),
        ("birr_sas_02_ardashir_i_founder_224_242_c", "Shahanshah Ardashir I (Son of Papak; Founder of Sasanian Empire, 224–242 CE)"),
        ("birr_sas_03_shapur_i_captured_roman_empe", "Shahanshah Shapur I (Son of Ardashir I; Captured Valerian, 240–270 CE)"),
        ("birr_sas_narseh", "Shahanshah Narseh (Son of Shapur I; r. 293–302 CE)"),
        ("birr_sas_04_shapur_ii_70_yr_reign_309_37", "Shahanshah Shapur II (Grandson of Narseh via Hormizd II; 70-yr Reign, 309–379 CE)"),
        ("birr_sas_05_yazdegerd_i_bahram_v_gur_anc", "Shahanshah Yazdegerd I (Son of Shapur III; r. 399–420 CE)"),
        ("birr_sas_bahram5", "Shahanshah Bahram V Gur (Son of Yazdegerd I; Ancestor of Buwayhids, 420–438 CE)"),
        ("birr_sas_peroz1", "Shahanshah Peroz I (Grandson of Bahram V Gur via Yazdegerd II; 459–484 CE)"),
        ("birr_sas_06_kavadh_i_ancestor_of_bavandi", "Shahanshah Kavadh I (Son of Peroz I; Ancestor of Bavandids, 488–531 CE)"),
        ("birr_sas_07_khosrow_i_anushirvan_immorta", "Shahanshah Khosrow I Anushirvan (Son of Kavadh I, 531–579 CE)"),
        ("birr_sas_hormizd4", "Shahanshah Hormizd IV (Son of Khosrow I, 579–590 CE)"),
        ("birr_sas_08_khosrow_ii_parviz", "Shahanshah Khosrow II Parviz (Son of Hormizd IV, 590–628 CE)"),
        ("birr_sas_09_queen_boran_first_female_sas", "Queen Boran / Purandokht (Daughter of Khosrow II; First Sasanian Empress, 630–631 CE)"),
        ("birr_sas_10_yazdegerd_iii_last_sasanian_", "Shahanshah Yazdegerd III (Grandson of Khosrow II via Shahriyar; Last Sasanian Shah, d. 651)"),
    ]
    for nid, nm in sas_list:
        nodes.append(N(nid, nm, "iranian", 19, "224-651 CE (Al-Biruni; Betham)", "Sasanian Ruler", ["Al-Biruni Chronology (Sachau pp. 45-48, 122-130)", "Betham Tab. CVI-CVII"], f"Sasanian imperial figure: {nm}.", major=False))
    nodes += [
        N("birr_sas_11_buwaihi_founder_of_buwayhid_", "Buwaihi / Abu Shuja Buya (Founder of Buwayhid Dynasty; Desc. from Bahram V Gur, Al-Biruni p. 45)", "iranian", 20, "10th c. CE (Al-Biruni p. 45)", "Ancestor of Buyid Amirs of Baghdad & Shiraz", ["Al-Biruni Chronology p. 45"], "Al-Biruni preserves a 14-generation pedigree connecting Buyah directly to Sasanian Shah Bahram V Gur."),
        N("birr_sas_12_isma_il_samani_founder_of_sa", "Isma'il ibn Ahmad Samani (Founder of Samanids via Saman Khuda & Bahram Chobin, Al-Biruni p. 48)", "iranian", 20, "849-907 CE (Al-Biruni p. 48)", "Samanid Emir of Bukhara & Samarkand", ["Al-Biruni Chronology p. 48"], "Al-Biruni traces the Samanids via 9 generations from Saman Khuda and Mihranid general Bahram Chobin."),
    ]
    edges.append(E("bir_sasanians_complete", "birr_sas_01_sasan_papak_ancestors_of_sas", "direct", "Sasanian anchor -> Sasan"))
    link_seq(edges, [x[0] for x in sas_list[:-2]], "direct", "Sasanian imperial succession")
    edges += [
        E("birr_sas_08_khosrow_ii_parviz", "birr_sas_09_queen_boran_first_female_sas", "direct", "Khosrow II -> daughter Queen Boran"),
        E("birr_sas_08_khosrow_ii_parviz", "birr_sas_10_yazdegerd_iii_last_sasanian_", "direct", "Khosrow II -> Prince Shahriyar -> Shah Yazdegerd III"),
        E("birr_sas_bahram5", "birr_sas_11_buwaihi_founder_of_buwayhid_", "expansion", "Al-Biruni p. 45: 14 generations from Bahram V Gur -> Buwaihi"),
        E("birr_sas_hormizd4", "birr_sas_12_isma_il_samani_founder_of_sa", "expansion", "Al-Biruni p. 48: Mihranid/Bahram Chobin era -> Saman Khuda -> Isma'il Samani"),
        E("birr_sas_08_khosrow_ii_parviz", "mod_exilarchs_bostanai", "direct", "Princess Izdundad (daughter of Khosrow II) marries Exilarch Bostanai"),
    ]

    # -------------------------------------------------------------------------
    # 7. KEBRA NAGAST PRE-MAKEDA KINGS & 21 ISRAELITE FIRSTBORN NOBLES
    # -------------------------------------------------------------------------
    pre_makeda = [
        ("kebr_21_01_arawi_angabo_gedur_sebado_ka", "King Arawi (First Pre-Makeda King in Budge Oxford MS)"),
        ("kebr_angabo", "King Angabo (Slayer of the Serpent King; Pre-Makeda Line)"),
        ("kebr_gedur", "King Gedur (Pre-Makeda Ethiopian King)"),
        ("kebr_sebado", "King Sebado (Pre-Makeda Ethiopian King)"),
        ("kebr_kawnasya", "King Kawnasya (Father of Queen Makeda in Kebra Nagast)"),
    ]
    for nid, nm in pre_makeda:
        nodes.append(N(nid, nm, "african", 15, "Pre-960 BCE (Kebra Nagast Budge p. xxxv)", "Pre-Makeda Ethiopian Monarch", ["Kebra Nagast (Budge 1922 Intro p. xxxv)"], f"Pre-Makeda Ethiopian ruler: {nm}.", major=False))

    kn_nobles = [
        ("kebr_21_02_tamrin_chief_merchant_of_que", "Tamrin (Chief Merchant of Queen Makeda)"),
        ("kebr_21_03_azaryas_son_of_zadok_stole_a", "'Azaryas (Son of High Priest Zadok; Carried the Ark of Zion to Aksum)"),
        ("kebr_21_04_elyas_son_of_arni_archdeacon", "'Elyas son of 'Arni (Archdeacon of Aksum)"),
        ("kebr_21_05_adram_son_of_arderones", "'Adram son of 'Arderones (Israelite Firstborn Noble)"),
        ("kebr_21_06_fankera_akonhel_samneyas_fik", "Fankera, 'Akonhel, Samneyas & Fikaros (Kebra Nagast Nobles)"),
        ("kebr_21_07_lewandos_fakuten_matan_ad_ar", "Lewandos, Fakuten, Matan & Ad'araz (Kebra Nagast Nobles)"),
        ("kebr_21_08_dalakem_adaryos_awsteran_ast", "Dalakem, 'Adaryos, 'Awsteran & 'Astar'ayon (Kebra Nagast Nobles)"),
        ("kebr_21_09_imi_makri_abis_lik_wendeyos_", "Imi, Makri, 'Abis, Lik Wendeyos, Karmi & Seranyas (Kebra Nagast Nobles)"),
    ]
    for nid, nm in kn_nobles:
        nodes.append(N(nid, nm, "african", 16, "c. 960 BCE (Kebra Nagast Ch. 43, Budge p. 62)", "Kebra Nagast Court & Firstborn Noble", ["Kebra Nagast (Budge 1922 p. 62)"], f"Kebra Nagast companion of Menyelek I: {nm}.", major=False))

    edges.append(E("keb_premakeda_tamrin_azaryas", "kebr_21_01_arawi_angabo_gedur_sebado_ka", "expansion", "Oxford MS pre-Makeda king list"))
    link_seq(edges, [x[0] for x in pre_makeda] + ["eth_makeda"], "direct", "Pre-Makeda Ethiopian royal succession")
    edges += [
        E("pri_eleazar_zadok", "kebr_21_03_azaryas_son_of_zadok_stole_a", "direct", "Kebra Nagast Ch. 43: High Priest Zadok -> son 'Azaryas"),
        E("keb_premakeda_tamrin_azaryas", "kebr_21_02_tamrin_chief_merchant_of_que", "expansion", "Queen Makeda's chief merchant Tamrin"),
        E("kebr_21_03_azaryas_son_of_zadok_stole_a", "kebr_21_04_elyas_son_of_arni_archdeacon", "expansion", "Companions of 'Azaryas carrying the Ark"),
        E("kebr_21_04_elyas_son_of_arni_archdeacon", "kebr_21_05_adram_son_of_arderones", "expansion", "Kebra Nagast Ch. 43 nobles"),
        E("kebr_21_05_adram_son_of_arderones", "kebr_21_06_fankera_akonhel_samneyas_fik", "expansion", "Kebra Nagast Ch. 43 nobles"),
        E("kebr_21_06_fankera_akonhel_samneyas_fik", "kebr_21_07_lewandos_fakuten_matan_ad_ar", "expansion", "Kebra Nagast Ch. 43 nobles"),
        E("kebr_21_07_lewandos_fakuten_matan_ad_ar", "kebr_21_08_dalakem_adaryos_awsteran_ast", "expansion", "Kebra Nagast Ch. 43 nobles"),
        E("kebr_21_08_dalakem_adaryos_awsteran_ast", "kebr_21_09_imi_makri_abis_lik_wendeyos_", "expansion", "Kebra Nagast Ch. 43 nobles"),
    ]

    # Cross-links connecting into the existing Atlas graph
    edges += [
        E("bib_togarmah", "geo_targamos_8sons", "expansion", "Kartlis Tskhovreba: Targamos (Togarmah) -> 8 Caucasian Hero-Sons"),
        E("geo_targamos_8sons", "geo_kartlos_5sons_uplos", "direct", "Kartlos -> Mtskhetos -> Uplos"),
        E("geo_kartlos_5sons_uplos", "geo_parnavaz_nebrothids", "direct", "Uplos -> King Parnavaz I"),
        E("bib_nimrod", "geo_parnavaz_nebrothids", "syncretic", "Kartlis Tskhovreba: Nebrotid (Nimrodid) Kings Mirvan I & Parnajom"),
        E("geo_parnavaz_nebrothids", "geo_chosroids_mirian_vakhtang", "direct", "Abeshuru marries Sasanian Prince Mirian III"),
        E("bir_sasanians_complete", "geo_chosroids_mirian_vakhtang", "direct", "Sasanian Prince Mikhran (Mirian III) founds Chosroid Dynasty"),
        E("nt_mary_clopas_alphaeus", "geo_bagrationi_davidic", "syncretic", "Sumbat Davitisdze traces Bagrat'ionis via K'leop'a -> 26 gens -> Bagrat'"),
        E("jud_david", "geo_bagrationi_davidic", "syncretic", "Georgian Bagrat'ioni royal claim of direct Davidic descent"),
        E("ir_siyavash", "bir_parthians_ashkanians", "expansion", "Al-Biruni p. 116 traces Parthian founder Ashk ben Ashkan to Kayanian Siyavush"),
        E("ir_bahman", "bir_sasanians_complete", "expansion", "Al-Biruni p. 122 traces Sasanian founder Ardashir I to Kay Bahman & Esfandiyar"),
        E("ir_kay_khosrow", "bir_khwarazm_afrighids", "expansion", "Al-Biruni pp. 40-42 traces all 22 Afrighid Khwarazmshahs to Siyavush & Kay Khosrow"),
        E("bib_joktan", "bir_himyar_lakhmid_ghassan", "expansion", "Qahtanite South Arabian Kingdoms (Himyarites, Lakhmids & Ghassanids)"),
        E("eth_makeda", "keb_premakeda_tamrin_azaryas", "expansion", "Pre-Makeda rulers, Tamrin & 21 Israelite firstborn nobles led by 'Azaryas"),
        E("jud_solomon", "keb_adrami_rome_shem", "expansion", "Kebra Nagast Ch. 72: Solomon's youngest son 'Adrami becomes King of Rome"),
        E("jud_perez", "keb_adrami_rome_shem", "syncretic", "Kebra Nagast Ch. 77: Judah's son Perez (Fares) -> Fars (Persia)"),
        E("jdg_samson", "keb_adrami_rome_shem", "expansion", "Kebra Nagast Ch. 80: Samson + Delilah -> 'Akamhel (King of Philistines)"),
        E("eth_ezana", "keb_kaleb_gabramaskal_yekuno", "direct", "Aksumite succession -> King Kaleb -> Gabra Maskal -> Yekuno 'Amlak"),
        E("keb_kaleb_gabramaskal_yekuno", "bir_himyar_lakhmid_ghassan", "cognate", "King Kaleb of Aksum defeats Himyarite King Dhu-Nuwas in Yemen (525 CE)"),
        E("keb_kaleb_gabramaskal_yekuno", "eth_lalibela", "expansion", "Zagwe interlude (Lalibala) -> Solomonic Restoration under Yekuno 'Amlak (1270 CE)"),
    ]

    return {
        "module": "19_caucasus_georgia_armenia_biruni",
        "title": "Georgian Chronicles (Kartlis Tskhovreba: Targamos -> 8 Caucasian Sons -> Kings of Kartli -> Davidic Bagrationis), Al-Biruni (Parthians, Sasanians, 22 Afrighids, Himyarites) & Kebra Nagast Expansion",
        "nodes": nodes,
        "edges": edges,
    }
