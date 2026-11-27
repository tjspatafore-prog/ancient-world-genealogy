"""
Module 23: Person-by-Person Irish Lebor Gabála Érenn (Part IV: Fir Bolg & Tuatha Dé Danann)
from R.A.S. Macalister (Irish Texts Society Vol. 41, leborgablare04macauoft.pdf).

Wave 5: Replaced all 3 flat add_roster fans with true Irish genealogical parent->child & fosterage chains.
"""

from . import N, E


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    nodes += [
        N("cel_nemed_pedigree", "Irish Universal Pedigree: Noah → Japheth → Magog → Fathacht → Sera → Agnomain → Nemed", "europe_norse", 8, "Mythic Irish Settlements (Lebor Gabála Érenn R1 ¶316, p. 127)",
          "Bridge Uniting Genesis 10 (Magog) to Ireland's Pre-Milesian Peoples", ["Lebor Gabála Érenn Part IV (Macalister ¶280, ¶316, pp. 9, 127)"],
          "Macalister R1 ¶316 traces Nemed directly from Noah -> Japheth -> Magog -> Fathacht -> Esru -> Sru -> Sera -> Tat -> Pamp -> Agnomain -> Nemed.",
          ["Nemed mac Agnomain", "Cessair", "Partholón", "Iarbonel Fatha", "Semeon"], major=True),
        N("cel_fir_bolg_kings", "Complete Fir Bolg Dynasty Anchor (Dela's 5 Sons & All 9 Kings to Eochu mac Eirc)", "europe_norse", 9, "Pre-Tuatha Dé Ireland (Lebor Gabála Part IV Sect. VI, pp. 7-21)",
          "First Organizers of Ireland's Five Provinces Anchor", ["Lebor Gabála Érenn Part IV (Macalister ¶278-289, pp. 7-21)"],
          "Dela's 5 sons divided Ireland into its 5 provinces; unrolled individually below.",
          ["Dela", "Sláine", "Eochu mac Eirc", "Queen Tailtiu"], major=True),
        N("cel_tdd_nuadu_dian_cecht", "Tuatha Dé Danann Line A & B1 Anchor (Nuadu Airgetlám, Dian Cécht & Lugh Lámfada)", "europe_norse", 10, "Battle of Mag Tuired (Lebor Gabála Part IV Sect. VII, pp. 113-159)",
          "Silver-Handed King Nuadu, Divine Craftsmen & Hero-King Lugh Anchor", ["Lebor Gabála Érenn Part IV (Macalister ¶310-316, ¶341, pp. 113-159)"],
          "Unrolled individually below from Tat mac Tabarn -> Nuadu, Dian Cécht -> Cian (+ Ethniu dau. of Balor) -> Lugh Lámfada.",
          ["Nuadu Airgetlám", "Dian Cécht", "Goibniu", "Balor of the Evil Eye", "Lugh Lámfada"], major=True),
        N("cel_tdd_dagda_ogma_eriu", "Tuatha Dé Danann Line B2 Anchor (Elada → The Dagda, Brigit, Ogma & Ériu)", "europe_norse", 10, "Tuatha Dé Danann Golden Age (Lebor Gabála Part IV Sect. VII, pp. 121-197)",
          "The Great Dagda, Goddess Brigit, Ogma & Eponymous Queens Anchor", ["Lebor Gabála Érenn Part IV (Macalister ¶313-317, ¶335-344, pp. 121-197)"],
          "Unrolled individually below from Elada -> Dagda, Ogma & Bres down to Ériu, Banba & Fódla.",
          ["The Dagda (Eochu Ollathair)", "Óengus Mac Óc", "Goddess Brigit", "Ogma", "Ériu / Banba / Fódla", "Bres"], major=True),
    ]

    # 1. Fir Bolg Sequential Succession
    fb_list = [
        ("celr_fb_01_1_sl_ine_slanga_mac_dela_fua", "1. King Sláine / Slanga mac Dela (+ Queen Fuat)"),
        ("celr_fb_02_2_rudraige_mac_dela_liber", "2. King Rudraige mac Dela (+ Queen Liber)"),
        ("celr_fb_03_3_gann_mac_dela_etar", "3. King Gann mac Dela (+ Queen Etar)"),
        ("celr_fb_04_4_genann_mac_dela_cnucha", "4. King Genann mac Dela (+ Queen Cnucha)"),
        ("celr_fb_05_5_sengann_mac_dela_anust", "5. King Sengann mac Dela (+ Queen Anust)"),
        ("celr_fb_06_6_fiacha_cendfindan_mac_star", "6. King Fiacha Cendfindan mac Starn (Grandson of Rudraige)"),
        ("celr_fb_07_7_rindail_mac_genann", "7. King Rindail mac Genann (Son of Genann)"),
        ("celr_fb_08_8_fodbgenid_mac_sengann", "8. King Fodbgenid mac Sengann (Son of Sengann)"),
        ("celr_fb_09_9_eochu_mac_eirc_queen_tailt", "9. King Eochu mac Eirc (+ Queen Tailtiu of Spain; Foster-Parents of Lugh)"),
        ("celr_fb_10_oengus_mac_umor_d_n_aengusa", "Oengus mac Umor (Fir Bolg Chieftain of Dún Aengusa, Aran Islands)"),
    ]
    for nid, nm in fb_list:
        nodes.append(N(nid, nm, "europe_norse", 9, "Lebor Gabála Sect. VI (Macalister)", "Fir Bolg Sovereign", ["Lebor Gabála Érenn Part IV (pp. 7-21)"], f"Fir Bolg sovereign in Lebor Gabála Érenn: {nm}.", major=False))
    edges.append(E("cel_fir_bolg_kings", "celr_fb_01_1_sl_ine_slanga_mac_dela_fua", "direct", "Fir Bolg anchor -> 1st King Sláine"))
    link_seq(edges, [x[0] for x in fb_list], "direct", "Fir Bolg royal succession (Macalister Sect. VI)")
    edges += [
        E("celr_fb_04_4_genann_mac_dela_cnucha", "celr_fb_07_7_rindail_mac_genann", "direct", "Genann -> son Rindail"),
        E("celr_fb_05_5_sengann_mac_dela_anust", "celr_fb_08_8_fodbgenid_mac_sengann", "direct", "Sengann -> son Fodbgenid"),
    ]

    # 2. Tuatha Dé Danann Line A & B1 (Tat -> Nuadu, Dian Cécht -> Cian + Ethniu -> Lugh)
    tdd1_nodes = [
        ("celr_tdd1_01_tat_mac_tabarn_common_ancest", "Tat mac Tabarn (Common Patriarch of Tuatha Dé Danann)"),
        ("celr_tdd1_02_nuadu_airgetl_m_king_27_yrs", "King Nuadu Airgetlám ('Silver Hand', Son of Eochu mac Etarlám, 27 yrs)"),
        ("celr_tdd1_03_midir_of_br_l_ith", "Midir of Brí Léith (Son of Induí; Noble of Tuatha Dé)"),
        ("celr_tdd1_04_n_t_war_god_fea_neman", "Nét (War God of Tuatha Dé, + Fea & Neman; Great-Grandson of Tat)"),
        ("celr_tdd1_05_goibniu_divine_smith", "Goibniu (Divine Smith, Son of Esarg mac Nét)"),
        ("celr_tdd1_06_creidne_divine_brazier", "Creidne (Divine Brazier Who Forged Nuadu's Silver Hand)"),
        ("celr_tdd1_07_luichtne_divine_carpenter", "Luichtne / Luchta (Divine Carpenter of Tuatha Dé)"),
        ("celr_tdd1_08_dian_c_cht_divine_physician", "Dian Cécht (Divine Physician, Son of Esarg mac Nét)"),
        ("celr_tdd1_09_cian_scal_balb_father_of_lug", "Cian / Scal Balb (Son of Dian Cécht; Father of Lugh)"),
        ("celr_tdd1_10_miach_airmed_healers", "Miach & Airmed (Children of Dian Cécht; Herbal Physicians)"),
        ("celr_tdd1_12_balor_of_the_evil_eye_fomori", "King Balor of the Evil Eye (Fomorian Monarch; Grandfather of Lugh)"),
        ("celr_tdd1_11_ethniu_daughter_of_balor_mot", "Princess Ethniu (Daughter of Balor; Wife of Cian & Mother of Lugh)"),
        ("celr_tdd1_13_lugh_l_mfada_king_40_yrs_vic", "King Lugh Lámfada ('Long-Arm', Son of Cian & Ethniu; Victor at Mag Tuired, 40 yrs)"),
        ("celr_tdd1_14_manann_n_mac_lir_sea_god", "Manannán mac Lir (Sea God & Sovereign of Emain Ablach)"),
    ]
    for nid, nm in tdd1_nodes:
        nodes.append(N(nid, nm, "europe_norse", 10, "Lebor Gabála Sect. VII (Macalister)", "Tuatha Dé Danann Deity / Sovereign", ["Lebor Gabála Érenn Part IV (pp. 113-159)"], f"Tuatha Dé Danann figure: {nm}.", major=False))

    edges += [
        E("cel_tdd_nuadu_dian_cecht", "celr_tdd1_01_tat_mac_tabarn_common_ancest", "direct", "Tuatha Dé anchor -> Tat mac Tabarn"),
        E("celr_tdd1_01_tat_mac_tabarn_common_ancest", "celr_tdd1_02_nuadu_airgetl_m_king_27_yrs", "direct", "Tat -> Etarlám -> Eochu -> King Nuadu Airgetlám"),
        E("celr_tdd1_01_tat_mac_tabarn_common_ancest", "celr_tdd1_03_midir_of_br_l_ith", "direct", "Tat -> Induí -> Midir of Brí Léith"),
        E("celr_tdd1_01_tat_mac_tabarn_common_ancest", "celr_tdd1_04_n_t_war_god_fea_neman", "direct", "Tat -> Allai -> Induí -> Nét"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd1_05_goibniu_divine_smith", "direct", "Nét -> Esarg -> Goibniu"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd1_06_creidne_divine_brazier", "direct", "Nét -> Esarg -> Creidne"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd1_07_luichtne_divine_carpenter", "direct", "Nét -> Esarg -> Luichtne"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd1_08_dian_c_cht_divine_physician", "direct", "Nét -> Esarg -> Dian Cécht"),
        E("celr_tdd1_01_tat_mac_tabarn_common_ancest", "celr_tdd1_14_manann_n_mac_lir_sea_god", "direct", "Tat -> Allai -> Lir -> Manannán mac Lir"),
        E("celr_tdd1_08_dian_c_cht_divine_physician", "celr_tdd1_09_cian_scal_balb_father_of_lug", "direct", "Dian Cécht -> son Cian"),
        E("celr_tdd1_08_dian_c_cht_divine_physician", "celr_tdd1_10_miach_airmed_healers", "direct", "Dian Cécht -> children Miach & Airmed"),
        E("cel_tdd_nuadu_dian_cecht", "celr_tdd1_12_balor_of_the_evil_eye_fomori", "expansion", "Fomorian ally & adversary Balor of the Evil Eye"),
        E("celr_tdd1_12_balor_of_the_evil_eye_fomori", "celr_tdd1_11_ethniu_daughter_of_balor_mot", "direct", "Balor -> daughter Ethniu"),
        E("celr_tdd1_09_cian_scal_balb_father_of_lug", "celr_tdd1_13_lugh_l_mfada_king_40_yrs_vic", "direct", "Father Cian -> Lugh Lámfada"),
        E("celr_tdd1_11_ethniu_daughter_of_balor_mot", "celr_tdd1_13_lugh_l_mfada_king_40_yrs_vic", "direct", "Mother Ethniu -> Lugh Lámfada"),
        E("celr_fb_09_9_eochu_mac_eirc_queen_tailt", "celr_tdd1_13_lugh_l_mfada_king_40_yrs_vic", "expansion", "Queen Tailtiu fosters young Lugh Lámfada"),
    ]

    # 3. Tuatha Dé Danann Line B2 (Elada -> Dagda, Ogma, Bres -> Ériu/Banba/Fódla)
    tdd2_nodes = [
        ("celr_tdd2_01_elada_elathan_father_of_dagd", "Elada / Elathan mac Delbaeth (Father of Dagda, Ogma & Bres)"),
        ("celr_tdd2_02_bres_mac_elathan_half_fomori", "King Bres mac Elathan (Half-Fomorian King, 7 yrs)"),
        ("celr_tdd2_03_eochu_ollathair_the_dagda_ki", "Eochu Ollathair / The Dagda (Son of Elada; High King 80 yrs)"),
        ("celr_tdd2_04_engus_mac_c_son_of_dagda_br_", "Óengus Mac Óc (Son of Dagda & Boann of Brú na Bóinne)"),
        ("celr_tdd2_05_brigit_the_poetess_daughter_", "Brigit the Poetess (Daughter of Dagda; Patroness of Healing & Poetry)"),
        ("celr_tdd2_06_cermait_milbel_son_of_dagda", "Cermait Milbel (Son of Dagda; Father of the Final Three Kings)"),
        ("celr_tdd2_07_mac_cuill_sethor_queen_banba", "King Mac Cuill / Éthur (Son of Cermait; Wed Queen Banba)"),
        ("celr_tdd2_08_mac_c_cht_tethor_queen_f_dla", "King Mac Cécht / Téthur (Son of Cermait; Wed Queen Fódla)"),
        ("celr_tdd2_09_mac_gr_ine_cethor_queen_riu", "King Mac Gréine / Cethur (Son of Cermait; Wed Queen Ériu)"),
        ("celr_tdd2_10_ogma_champion_inventor_of_og", "Ogma (Son of Elada; Champion & Inventor of Ogham Script)"),
        ("celr_tdd2_11_delbaeth_tuirenn_king_10_yrs", "King Delbaeth / Tuirenn mac Ogma (10 yrs)"),
        ("celr_tdd2_12_fiachna_mac_delbaeth_king_10", "King Fiachna mac Delbaeth (10 yrs; Father of Ériu, Banba & Fódla)"),
        ("celr_tdd2_13_brian_iuchar_iucharba_three_", "Brian, Iuchar & Iucharba (Sons of Tuirenn / Brigit; Three Gods of Danu)"),
        ("celr_tdd2_15_ernmas_the_morr_gan", "Ernmas & The Morrígan (Matriarch of Tuatha Dé Goddesses)"),
        ("celr_tdd2_14_riu_banba_f_dla_sovereignty_", "Ériu, Banba & Fódla (Sovereignty Goddesses of Ireland)"),
    ]
    for nid, nm in tdd2_nodes:
        nodes.append(N(nid, nm, "europe_norse", 10, "Lebor Gabála Sect. VII (Macalister)", "Tuatha Dé Danann Sovereign / Deity", ["Lebor Gabála Érenn Part IV (pp. 121-197)"], f"House of Elada / Dagda / Ogma: {nm}.", major=False))

    edges += [
        E("cel_tdd_dagda_ogma_eriu", "celr_tdd2_01_elada_elathan_father_of_dagd", "direct", "Dagda/Ogma anchor -> Elada"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd2_01_elada_elathan_father_of_dagd", "direct", "Nét -> Delbaeth -> Elada"),
        E("celr_tdd2_01_elada_elathan_father_of_dagd", "celr_tdd2_02_bres_mac_elathan_half_fomori", "direct", "Elada + Ériu -> Bres"),
        E("celr_tdd2_01_elada_elathan_father_of_dagd", "celr_tdd2_03_eochu_ollathair_the_dagda_ki", "direct", "Elada -> Eochu Ollathair (The Dagda)"),
        E("celr_tdd2_01_elada_elathan_father_of_dagd", "celr_tdd2_10_ogma_champion_inventor_of_og", "direct", "Elada -> Ogma"),
        E("celr_tdd2_03_eochu_ollathair_the_dagda_ki", "celr_tdd2_04_engus_mac_c_son_of_dagda_br_", "direct", "The Dagda -> Óengus Mac Óc"),
        E("celr_tdd2_03_eochu_ollathair_the_dagda_ki", "celr_tdd2_05_brigit_the_poetess_daughter_", "direct", "The Dagda -> daughter Brigit"),
        E("celr_tdd2_03_eochu_ollathair_the_dagda_ki", "celr_tdd2_06_cermait_milbel_son_of_dagda", "direct", "The Dagda -> Cermait Milbel"),
        E("celr_tdd2_06_cermait_milbel_son_of_dagda", "celr_tdd2_07_mac_cuill_sethor_queen_banba", "direct", "Cermait -> Mac Cuill"),
        E("celr_tdd2_06_cermait_milbel_son_of_dagda", "celr_tdd2_08_mac_c_cht_tethor_queen_f_dla", "direct", "Cermait -> Mac Cécht"),
        E("celr_tdd2_06_cermait_milbel_son_of_dagda", "celr_tdd2_09_mac_gr_ine_cethor_queen_riu", "direct", "Cermait -> Mac Gréine"),
        E("celr_tdd2_10_ogma_champion_inventor_of_og", "celr_tdd2_11_delbaeth_tuirenn_king_10_yrs", "direct", "Ogma -> Delbaeth / Tuirenn"),
        E("celr_tdd2_11_delbaeth_tuirenn_king_10_yrs", "celr_tdd2_12_fiachna_mac_delbaeth_king_10", "direct", "Delbaeth -> Fiachna"),
        E("celr_tdd2_11_delbaeth_tuirenn_king_10_yrs", "celr_tdd2_13_brian_iuchar_iucharba_three_", "direct", "Tuirenn -> Brian, Iuchar & Iucharba"),
        E("celr_tdd1_04_n_t_war_god_fea_neman", "celr_tdd2_15_ernmas_the_morr_gan", "direct", "Nét -> Ernmas & The Morrígan"),
        E("celr_tdd2_12_fiachna_mac_delbaeth_king_10", "celr_tdd2_14_riu_banba_f_dla_sovereignty_", "direct", "Fiachna -> Ériu, Banba & Fódla"),
        E("celr_tdd2_15_ernmas_the_morr_gan", "celr_tdd2_14_riu_banba_f_dla_sovereignty_", "direct", "Mother Ernmas -> Ériu, Banba & Fódla"),
        E("celr_tdd2_14_riu_banba_f_dla_sovereignty_", "eur_milesians", "expansion", "Sovereignty of Ireland passed to the Milesians (Amairgin's pact with Ériu)"),
    ]

    # Cross-links into existing Atlas graph
    edges += [
        E("bib_magog", "cel_nemed_pedigree", "syncretic", "Lebor Gabála Érenn R1 ¶316 traces Nemed from Noah -> Japheth -> Magog"),
        E("cel_nemed_pedigree", "cel_fir_bolg_kings", "direct", "Nemed -> Starn -> Semeon -> Dela -> 5 Sons & 9 Fir Bolg Kings"),
        E("cel_nemed_pedigree", "cel_tdd_nuadu_dian_cecht", "direct", "Nemed -> Iarbonel -> Bethach -> Tat -> Nuadu Airgetlám & Dian Cécht -> Lugh"),
        E("cel_nemed_pedigree", "cel_tdd_dagda_ogma_eriu", "direct", "Nemed -> Tat -> Nét -> Elada -> The Dagda, Ogma & Ériu"),
        E("cel_tdd_dagda_ogma_eriu", "eur_tuatha_de", "direct", "Complete Tuatha Dé Danann royal & divine pantheon"),
        E("cel_tdd_dagda_ogma_eriu", "eur_milesians", "expansion", "Sons of Míl defeat Mac Cuill, Mac Cécht & Mac Gréine (Ériu gives her name to Ireland!)"),
    ]

    return {
        "module": "23_celtic_lebor_gabala",
        "title": "Complete Irish Lebor Gabála Érenn Part IV: Nemedian Pedigree from Magog, All 9 Fir Bolg Kings & Complete Tuatha Dé Danann Pantheon (Macalister)",
        "nodes": nodes,
        "edges": edges,
    }
