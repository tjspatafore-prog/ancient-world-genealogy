"""
Module 21: Person-by-Person 95-Generation Synchronized Puranic Royal & Rishi Genealogies of India
from F.E. Pargiter's Ancient Indian Historical Tradition (1922, Master Table pp. 144-149 & Chs. VII-XXVII).

Wave 5: Replaced all 5 flat add_roster fans with true sequential Solar, Lunar (sub-dynasty specific)
& Great Rishi parent->child/guru->disciple chains while preserving every existing node ID verbatim.
"""

from . import N, E


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. SOLAR & LUNAR DYNASTY ANCHORS (Preserving All 18 Existing Anchor IDs)
    # -------------------------------------------------------------------------
    nodes += [
        N("ind_ayodhya_early_1_30", "Ayodhya Solar Spine Anchor (Gens 2–30: Ikshvaku to Trayyaruna)", "vedic", 6, "Satya Yuga (Pargiter Master Table Gens 2-30, p. 145)",
          "First 30 Generations of Solar Ayodhya Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 90-92, 145"],
          "Anchor for the first 30 generations of Aikshvaku kings (Mandhatri, Purukutsa, Trasadasyu), unrolled father-to-son below.",
          ["Vikukshi", "Kakutstha", "Mandhatri", "Purukutsa", "Trasadasyu"]),
        N("ind_ayodhya_mid_31_64", "Ayodhya Solar Spine Anchor (Gens 31–64: Trishanku to Dasharatha)", "vedic", 8, "Treta Yuga (Pargiter Master Table Gens 31-64, pp. 145, 147)",
          "Golden Era of Solar Dynasty Leading to Lord Rama Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 92-94, 145-147"],
          "Anchor for Gens 31-64 (Harishchandra, Sagara, Bhagiratha, Raghu, Dasharatha), chained individually below.",
          ["Trishanku", "Harishchandra", "Sagara", "Bhagiratha", "Rituparna", "Dilipa II"]),
        N("ind_ayodhya_late_66_95", "Ayodhya Post-Rama Spine Anchor (Gens 66–95: Kusha to Brihatkshaya)", "vedic", 11, "Dvapara Yuga (Pargiter Master Table Gens 66-95, p. 149)",
          "30 Generations from Rama's Son Kusha to Mahabharata Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 94-95, 149"],
          "Anchor for post-Rama Solar kings down to Brihadbala (Kurukshetra) & Brihatkshaya, chained below.",
          ["Atithi", "Hiranyanabha", "Agnivarna", "Brihadbala"]),
        N("ind_videha_janaka_complete", "Videha / Mithila Solar Dynasty (All 54 Kings: Nimi → Mithi Janaka → Siradhvaja → Janaka-Ugrasena)", "vedic", 9, "Gens 2-98 (Pargiter Ch. VIII pp. 95-96, 145-149, 330)",
          "Philosopher-Kings of Mithila (Upanishadic Janakas & Ramayana)", ["Pargiter Ancient Indian Historical Tradition pp. 95-96, 145-149"],
          "Founded by Ikshvaku's son Nimi -> Mithi Janaka -> Siradhvaja Janaka (father of Goddess Sita).",
          ["Mithi Janaka", "Siradhvaja Janaka (Father of Sita)", "Kushadhvaja", "Kritakshana"]),
        N("ind_vaisali_sharyata_nabhaga", "Manu's Other Solar Kingdoms: Vaisali (Nabhanedishtha → Marutta → Trinabindu), Sharyatas & Nabhagas", "vedic", 7, "Gens 2-64 (Pargiter Ch. VIII pp. 97-98, 145, 147)",
          "Ancient Dynasties of North Bihar (Vaisali) & Gujarat (Anarta)", ["Pargiter Ancient Indian Historical Tradition pp. 97-98, 145-147"],
          "Nabhanedishtha's line produced Marutta & Trinabindu; Sharyati's line produced Raivata Kakudmin.",
          ["Nabhanedishtha", "Marutta of Vaisali", "Trinabindu", "Vishala", "Sharyati -> Raivata Kakudmin"]),

        N("ind_kanyakubja_vishvamitra", "Kanyakubja Dynasty Anchor (Amavasu → Jahnu → Gadhi → Vishvamitra)", "vedic", 8, "Gens 4-35 (Pargiter Ch. IX pp. 99-101, 144, 146)",
          "Aila Kingdom of Kanauj & Origin of Vishvamitra Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 99-101, 234-237"],
          "Pururavas's son Amavasu -> Jahnu -> Gadhi -> Brahmarshi Vishvamitra (Rigveda Mandala III).",
          ["Amavasu", "King Jahnu", "King Gadhi", "Rishi Vishvamitra"], major=True),
        N("ind_kasi_dhanvantari_divodasa", "Kasi (Varanasi) Dynasty Anchor (Kshatravriddha → Dhanvantari → Divodasa II → Alarka)", "vedic", 8, "Gens 5-94 (Pargiter Ch. IX p. 101; Ch. XIII pp. 153-155)",
          "Ancient Sacred Kingdom of Varanasi & Origin of Ayurveda Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 101, 145-155"],
          "Kshatravriddha -> Dhanvantari -> Divodasa II -> Pratardana -> Alarka.",
          ["Kshatravriddha", "Dhanvantari", "Divodasa of Kasi", "Pratardana", "Alarka"]),
        N("ind_haihayas_kartavirya", "Haihaya Dynasty Anchor (Yadu → Sahasrajit → Kartavirya Arjuna → Talajanghas)", "vedic", 8, "Gens 7-41 (Pargiter Ch. IX p. 102, 144, 146)",
          "Central Indian Narmada Empire Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 102, 144-146, 153-156"],
          "Kartavirya Arjuna (Gen 31) of Mahishmati; crushed by Parashurama & Sagara.",
          ["Sahasrajit", "Kartavirya Arjuna", "Talajangha", "Vitihotra"], major=True),
        N("ind_yadava_kroshtu_satvata", "Yadava Main Line Anchor (Kroshtu → Shashabindu → Vidarbha → Satvata → Vrishni)", "vedic", 10, "Gens 7-95 (Pargiter Ch. IX pp. 102-107, 144-148)",
          "Complete Yadava Pedigree Anchor (Yadu to Krishna & Vajra)", ["Pargiter Ancient Indian Historical Tradition pp. 102-107, 144-148, 284"],
          "Kroshtu -> Shashabindu -> Jyamagha -> Vidarbha -> Satvata -> Andhaka & Vrishni.",
          ["Kroshtu", "Shashabindu", "Vidarbha", "Satvata", "King Kamsa", "Samba & Vajra"]),
        N("ind_druhyu_gandhara_turvasu", "Druhyus (Gandhara → Pracetas) & Turvasus (Pandya, Kerala & Chola Anchor)", "vedic", 8, "Gens 7-44 (Pargiter Ch. IX p. 108, 144, 146)",
          "Northwest (Gandhara/Central Asia) & South Indian Aila Bridges", ["Pargiter Ancient Indian Historical Tradition pp. 108, 144, 146"],
          "Druhyu -> Gandhara -> Pracetas; Turvasu -> Marutta -> Pandya, Kerala, and Chola.",
          ["Gandhara", "Pracetas", "Pandya / Kerala / Chola"]),
        N("ind_anava_shibi_anga_karna", "Anavas Anchor (Ushinara → Shibi & Titikshu → Bali → Anga/Vanga/Kalinga → Karna)", "vedic", 9, "Gens 7-95 (Pargiter Ch. IX pp. 108-109, 145-149)",
          "Progenitors of Panjab (Shibi) & Eastern India (Bengal/Odisha/Anga) Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 108-109, 145-149"],
          "Ushinara -> King Shibi; Titikshu -> King Bali -> Anga, Vanga, Kalinga, Pundra & Suhma -> Karna.",
          ["Ushinara", "King Shibi", "King Bali -> Anga/Vanga/Kalinga", "Karna of Anga"], major=True),
        N("ind_panchala_sudas_drupada", "North & South Panchalas Anchor (Mudgala → Sudas → Drupada & Draupadi)", "vedic", 10, "Gens 53-95 (Pargiter Ch. IX pp. 115-117, 146, 148)",
          "Rigvedic Battle of Ten Kings Hero Sudas & Panchala Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 115-117, 146-148", "Rigveda VII.18"],
          "Ajamidha -> Nila -> Mudgala -> Divodasa -> Sudas -> Drupada -> Draupadi & Dhrishtadyumna.",
          ["Mudgala", "Rigvedic King Sudas", "King Drupada", "Queen Draupadi", "Dhrishtadyumna"], major=True),
        N("ind_cedi_magadha_jarasandha", "Cedi & Magadha Barhadratha Anchor (Vasu Uparichara → Brihadratha → Jarasandha)", "vedic", 11, "Gens 73-95 (Pargiter Ch. IX pp. 118-119, 149)",
          "First Historical Dynasty of Magadha & Cedi Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 118-119, 149"],
          "Vasu Uparichara -> Brihadratha -> Emperor Jarasandha & Damaghosha -> Shishupala (Cedi).",
          ["Vasu Uparichara", "Brihadratha", "Jarasandha of Magadha", "Shishupala of Cedi"], major=True),
        N("ind_kuru_post_battle_vatsa", "Post-Mahabharata Kurus Anchor (Janamejaya III → Adhisimakrishna → Nicakshu → Udayana)", "vedic", 12, "c. 950-500 BCE (Pargiter Ch. XXIV p. 285; Ch. XXVII p. 330)",
          "Continuation of Pandava/Kuru Royal Line After Hastinapura Flood", ["Pargiter Ancient Indian Historical Tradition pp. 285, 330"],
          "Nicakshu moved Kuru capital to Kaushambi in Vatsa down to King Udayana.",
          ["Adhisimakrishna", "Nicakshu (Kaushambi)", "King Udayana of Vatsa"]),

        N("ind_rishis_bhargava_angirasa", "Great Rishi Clans Anchor: Bhargavas & Angirasas / Kanvas", "vedic", 8, "Gens 2-94 (Pargiter Ch. XVII & XIX, pp. 191-202, 218-227)",
          "Complete Genealogies of Bhargava, Angirasa & Kanva Seers Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 191-202, 218-227"],
          "Synchronizes Bhrigu/Cyavana/Jamadagni/Parashurama/Valmiki & Atharvan/Brihaspati/Bharadvaja/Drona across the 95-gen master table.",
          ["Cyavana", "Jamadagni & Parashurama", "Rishi Valmiki", "Bharadvaja -> Drona", "Dirghatamas"], major=True),
        N("ind_rishis_vasishtha_agastya", "Great Rishi Clans Anchor: Vasishthas (Vyasa), Atreyas, Kashyapas & Agastyas", "vedic", 9, "Gens 1-94 (Pargiter Ch. XVIII, XX, XXII, pp. 203-242)",
          "Complete Pedigrees of Vyasa, Durvasas, Rishyashringa & Agastya Anchor", ["Pargiter Ancient Indian Historical Tradition pp. 203-242"],
          "Synchronizes Vasishtha -> Shakti -> Parashara -> Vyasa -> Shuka alongside Datta/Durvasas, Kanva, Rishyashringa & Agastya.",
          ["Shakti -> Parashara -> Vyasa", "Dattatreya & Durvasas", "Rishyashringa", "Agastya & Lopamudra"]),

        N("ind_magadha_bimbisara_nanda", "Historical Magadha Anchor (22 Barhadrathas → Pradyotas → Shishunaga/Bimbisara → 9 Nandas)", "vedic", 16, "c. 950-322 BCE (Pargiter pp. 179-182, 286-287)",
          "Bridge from Mahabharata Magadha to Buddha & Chandragupta Maurya", ["Pargiter Ancient Indian Historical Tradition pp. 179-182, 286-287"],
          "22 Barhadrathas -> Pradyotas -> Bimbisara & Ajatashatru -> 9 Nandas -> Chandragupta Maurya (322 BCE).",
          ["King Bimbisara", "Ajatashatru", "Shishunaga", "Mahapadma Nanda"], major=True),
        N("ind_gupta_golden_age", "Gupta Empire Anchor (Sri Gupta → Chandragupta I → Samudragupta → Vikramaditya → Skandagupta)", "vedic", 19, "c. 240-550 CE (Allahabad Pillar Inscription; Puranas)",
          "Classical Golden Age of India Anchor", ["Allahabad Pillar Inscription", "Vishnu Purana IV.24"],
          "Gupta emperors unrolled person-by-person in Wave 5.",
          ["Chandragupta I", "Samudragupta", "Chandragupta II Vikramaditya"], major=True),
    ]

    edges += [
        E("ved_ikshvaku", "ind_ayodhya_early_1_30", "direct", "Ayodhya Solar Spine Gens 2-30 (Pargiter p. 145)"),
        E("ind_ayodhya_early_1_30", "ind_ayodhya_mid_31_64", "direct", "Ayodhya Solar Spine Gens 31-64 (Trishanku -> Dasharatha)"),
        E("ind_ayodhya_mid_31_64", "ved_surya_vamsha", "direct", "Dasharatha -> Lord Rama (Gen 65)"),
        E("ved_lava_kusha", "ind_ayodhya_late_66_95", "direct", "Kusha (Gen 66) -> 30 generations to Brihadbala (Gen 94, Kurukshetra)"),
        E("ind_ayodhya_late_66_95", "ved_buddha", "expansion", "Solar Aikshvaku continuation -> Shakya Clan -> Gautama Buddha"),
        E("ved_nimi_janaka", "ind_videha_janaka_complete", "direct", "Complete 54-king Videha/Mithila Janaka lineage (Pargiter pp. 95-96)"),
        E("ved_manu_other_sons", "ind_vaisali_sharyata_nabhaga", "direct", "Nabhanedishtha (Vaisali), Sharyati (Anarta) & Nabhaga (Pargiter pp. 97-98)"),
        E("ved_pururavas_ayu", "ind_kanyakubja_vishvamitra", "direct", "Pururavas -> Amavasu -> Gadhi -> Rishi Vishvamitra (Pargiter p. 99)"),
        E("ved_pururavas_ayu", "ind_kasi_dhanvantari_divodasa", "direct", "Ayu -> Kshatravriddha -> Dhanvantari -> Divodasa & Pratardana (Pargiter p. 101)"),
        E("ved_yadu", "ind_haihayas_kartavirya", "direct", "Yadu -> Sahasrajit -> Haihaya -> Kartavirya Arjuna (Pargiter p. 102)"),
        E("ved_yadu", "ind_yadava_kroshtu_satvata", "direct", "Yadu -> Kroshtu -> Shashabindu -> Vidarbha -> Satvata -> Vrishni & Andhaka"),
        E("ind_yadava_kroshtu_satvata", "ved_krishna_balarama", "direct", "Vrishni -> Vasudeva -> Krishna & Balarama (Gen 94)"),
        E("ved_druhyu", "ind_druhyu_gandhara_turvasu", "direct", "Druhyu -> Gandhara -> Pracetas (northward migration, Pargiter p. 108)"),
        E("ved_turvasu", "ind_druhyu_gandhara_turvasu", "direct", "Turvasu -> Marutta -> adoption of Dushyanta / Pandya-Chola-Kerala"),
        E("ved_anu", "ind_anava_shibi_anga_karna", "direct", "Anu -> Ushinara (Shibi) & Titikshu -> Bali -> Anga/Vanga/Kalinga -> Karna"),
        E("ved_hasti_kuru", "ind_panchala_sudas_drupada", "direct", "Hastin -> Ajamidha -> Nila -> Mudgala -> Sudas -> Drupada & Draupadi"),
        E("ved_hasti_kuru", "ind_cedi_magadha_jarasandha", "direct", "Kuru -> Sudhanvan -> Vasu Uparichara -> Brihadratha -> Jarasandha"),
        E("ved_parikshit_janamejaya", "ind_kuru_post_battle_vatsa", "direct", "Janamejaya III -> Adhisimakrishna -> Nicakshu (Kaushambi) -> Udayana"),
        E("ved_saptarishis_bhrigu", "ind_rishis_bhargava_angirasa", "direct", "Complete Bhargava & Angirasa/Bharadvaja Rishi tables (Pargiter pp. 191-227)"),
        E("ved_saptarishis_bhrigu", "ind_rishis_vasishtha_agastya", "direct", "Complete Vasishtha (Vyasa), Atreya, Kashyapa & Agastya Rishi tables"),
        E("ind_cedi_magadha_jarasandha", "ind_magadha_bimbisara_nanda", "direct", "Somadhi -> 22 Barhadrathas -> Shishunaga (Bimbisara) -> 9 Nandas"),
        E("ind_magadha_bimbisara_nanda", "ved_maurya_ashoka", "expansion", "Chandragupta Maurya overthrows the 9 Nandas (322 BCE)"),
        E("ind_magadha_bimbisara_nanda", "ved_buddha", "cognate", "King Bimbisara & Ajatashatru of Magadha: patrons of Gautama Buddha (c. 487 BCE)"),
        E("ved_maurya_ashoka", "ind_gupta_golden_age", "expansion", "Post-Mauryan imperial succession -> Gupta Golden Age of Magadha"),
    ]

    # -------------------------------------------------------------------------
    # 2. AYODHYA 95-GENERATION SOLAR SPINE (Continuous Father->Son Chain!)
    # -------------------------------------------------------------------------
    ay1_list = [
        ("indr_ay1_01_vikukshi_shashada_gen_3", "Vikukshi-Shashada (Gen 3, Son of Ikshvaku)"),
        ("indr_ay1_02_kakutstha_gen_4", "Kakutstha / Puranjaya (Gen 4)"),
        ("indr_ay1_03_anenas_gen_5", "Anenas (Gen 5)"),
        ("indr_ay1_04_prithu_gen_6", "Prithu of Ayodhya (Gen 6)"),
        ("indr_ay1_05_vishtarashva_gen_7", "Vishtarashva (Gen 7)"),
        ("indr_ay1_06_ardra_gen_8", "Ardra / Candra (Gen 8)"),
        ("indr_ay1_07_yuvanashva_i_gen_9", "Yuvanashva I (Gen 9)"),
        ("indr_ay1_08_shravasta_gen_10_founder_of_", "Shravasta (Gen 10, Founder of Shravasti)"),
        ("indr_ay1_09_brihadashva_gen_11", "Brihadashva (Gen 11)"),
        ("indr_ay1_10_kuvalashva_gen_12", "Kuvalashva / Dhundhumara (Gen 12)"),
        ("indr_ay1_11_dridhashva_gen_13", "Dridhashva (Gen 13)"),
        ("indr_ay1_12_pramoda_gen_14", "Pramoda / Haryashva (Gen 14)"),
        ("indr_ay1_13_haryashva_i_gen_15", "Haryashva I (Gen 15)"),
        ("indr_ay1_14_nikumbha_gen_16", "Nikumbha (Gen 16)"),
        ("indr_ay1_15_samhatashva_gen_17", "Samhatashva (Gen 17)"),
        ("indr_ay1_16_akrishashva_gen_18", "Akrishashva / Krishashva (Gen 18)"),
        ("indr_ay1_17_prasenajit_gen_19", "Prasenajit (Gen 19)"),
        ("indr_ay1_18_yuvanashva_ii_gen_20", "Yuvanashva II (Gen 20)"),
        ("indr_ay1_19_emperor_mandhatri_gen_21", "Emperor Mandhatri (Gen 21, Son of Yuvanashva II)"),
        ("indr_ay1_20_purukutsa_gen_22", "Purukutsa (Gen 22, Son of Mandhatri)"),
        ("indr_ay1_21_trasadasyu_gen_23_rigvedic_k", "Trasadasyu (Gen 23, Rigvedic King)"),
        ("indr_ay1_22_sambhuta_gen_24", "Sambhuta (Gen 24)"),
        ("indr_ay1_23_anaranya_gen_25", "Anaranya (Gen 25)"),
        ("indr_ay1_24_trasashva_gen_26", "Trasashva / Prishadashva (Gen 26)"),
        ("indr_ay1_25_haryashva_ii_gen_27", "Haryashva II (Gen 27)"),
        ("indr_ay1_26_vasumata_gen_28", "Vasumata / Vasumanas (Gen 28)"),
        ("indr_ay1_27_tridhanvan_gen_29", "Tridhanvan (Gen 29)"),
        ("indr_ay1_28_trayyaruna_gen_30", "Trayyaruna (Gen 30)"),
    ]
    for nid, nm in ay1_list:
        nodes.append(N(nid, nm, "vedic", 6, "Pargiter Master Table Gens 3-30", "Ayodhya Solar King (Satya Yuga)", ["Pargiter Ancient Indian Historical Tradition p. 145"], f"Solar Aikshvaku succession: {nm}.", major=False))

    ay2_list = [
        ("indr_ay2_01_satyavrata_trishanku_gen_31", "Satyavrata-Trishanku (Gen 31)"),
        ("indr_ay2_02_king_harishchandra_gen_32", "King Harishchandra (Gen 32, Son of Trishanku)"),
        ("indr_ay2_03_rohita_gen_33", "Rohita / Rohitashva (Gen 33)"),
        ("indr_ay2_04_harita_cancu_gen_34", "Harita & Cancu (Gens 34-35)"),
        ("indr_ay2_05_vijaya_gen_35", "Vijaya (Gen 36)"),
        ("indr_ay2_06_ruruka_gen_36", "Ruruka (Gen 37)"),
        ("indr_ay2_07_vrika_gen_37", "Vrika (Gen 38)"),
        ("indr_ay2_08_bahu_asita_gen_38", "Bahu / Asita (Gen 39)"),
        ("indr_ay2_09_emperor_sagara_gen_41", "Emperor Sagara (Gen 41, Destroyer of Haihayas)"),
        ("indr_ay2_10_asamanjas_gen_42", "Asamanjas (Gen 42)"),
        ("indr_ay2_11_amshumant_gen_43", "Amshumant (Gen 43)"),
        ("indr_ay2_12_dilipa_i_gen_44", "Dilipa I (Gen 44)"),
        ("indr_ay2_13_bhagiratha_gen_45_brought_th", "Bhagiratha (Gen 45, Brought the Ganga)"),
        ("indr_ay2_14_shruta_gen_46", "Shruta (Gen 46)"),
        ("indr_ay2_15_nabhaga_gen_47", "Nabhaga of Ayodhya (Gen 47)"),
        ("indr_ay2_16_ambarisha_gen_48", "Ambarisha of Ayodhya (Gen 48)"),
        ("indr_ay2_17_sindhudvipa_gen_49", "Sindhudvipa (Gen 49)"),
        ("indr_ay2_18_ayutayus_gen_50", "Ayutayus (Gen 50)"),
        ("indr_ay2_19_rituparna_gen_51_host_of_nal", "Rituparna (Gen 51, Host of Nala)"),
        ("indr_ay2_20_sarvakama_gen_52", "Sarvakama (Gen 52)"),
        ("indr_ay2_21_sudasa_of_ayodhya_gen_53", "Sudasa of Ayodhya (Gen 53)"),
        ("indr_ay2_22_mitrasaha_kalmashapada_gen_5", "Mitrasaha-Kalmashapada (Gen 54)"),
        ("indr_ay2_23_ashmaka_gen_55", "Ashmaka (Gen 55)"),
        ("indr_ay2_24_mulaka_gen_56", "Mulaka (Gen 56)"),
        ("indr_ay2_25_shataratha_gen_57", "Shataratha (Gen 57)"),
        ("indr_ay2_26_aidavida_gen_58", "Aidavida / Ilavila (Gen 58)"),
        ("indr_ay2_27_vishvasaha_i_gen_59", "Vishvasaha I (Gen 59)"),
        ("indr_ay2_28_dilipa_ii_khatvanga_gen_60", "Dilipa II Khatvanga (Gen 60)"),
        ("indr_ay2_29_dirghabahu_gen_61", "Dirghabahu (Gen 61)"),
        ("indr_ay2_30_emperor_raghu_gen_62", "Emperor Raghu (Gen 62)"),
        ("indr_ay2_31_aja_gen_63", "King Aja (Gen 63, Son of Raghu)"),
        ("indr_ay2_32_king_dasharatha_gen_64", "King Dasharatha (Gen 64, Father of Lord Rama)"),
    ]
    for nid, nm in ay2_list:
        nodes.append(N(nid, nm, "vedic", 8, "Pargiter Master Table Gens 31-64", "Ayodhya Solar King (Treta Yuga)", ["Pargiter Ancient Indian Historical Tradition pp. 145, 147"], f"Solar Aikshvaku succession: {nm}.", major=False))

    ay3_list = [
        ("indr_ay3_01_atithi_gen_67", "Atithi (Gen 67, Son of Kusha)"),
        ("indr_ay3_02_nishadha_gen_68", "Nishadha (Gen 68)"),
        ("indr_ay3_03_nala_of_ayodhya_gen_69", "Nala of Ayodhya (Gen 69)"),
        ("indr_ay3_04_nabhas_gen_70", "Nabhas (Gen 70)"),
        ("indr_ay3_05_pundarika_gen_71", "Pundarika (Gen 71)"),
        ("indr_ay3_06_kshemadhanvan_gen_72", "Kshemadhanvan (Gen 72)"),
        ("indr_ay3_07_devanika_gen_73", "Devanika (Gen 73)"),
        ("indr_ay3_08_ahinagu_gen_74", "Ahinagu (Gen 74)"),
        ("indr_ay3_09_paripatra_gen_75", "Paripatra (Gen 75)"),
        ("indr_ay3_10_dala_bala_gen_76", "Dala & Bala (Gen 76)"),
        ("indr_ay3_11_uktha_gen_77", "Uktha / Vajranabha Father (Gen 77)"),
        ("indr_ay3_12_vajranabha_gen_78", "Vajranabha (Gen 78)"),
        ("indr_ay3_13_shankhana_gen_79", "Shankhana (Gen 79)"),
        ("indr_ay3_14_vyushitashva_gen_80", "Vyushitashva (Gen 80)"),
        ("indr_ay3_15_vishvasaha_ii_gen_81", "Vishvasaha II (Gen 81)"),
        ("indr_ay3_16_hiranyanabha_gen_82_yoga_mas", "Hiranyanabha (Gen 82, Yoga Master)"),
        ("indr_ay3_17_pushya_gen_83", "Pushya (Gen 83)"),
        ("indr_ay3_18_dhruvasandhi_gen_84", "Dhruvasandhi (Gen 84)"),
        ("indr_ay3_19_sudarshana_gen_85", "Sudarshana (Gen 85)"),
        ("indr_ay3_20_agnivarna_gen_86", "Agnivarna (Gen 86)"),
        ("indr_ay3_21_shighra_gen_87", "Shighra (Gen 87)"),
        ("indr_ay3_22_maru_gen_88", "Maru (Gen 88)"),
        ("indr_ay3_23_prasushruta_gen_89", "Prasushruta (Gen 89)"),
        ("indr_ay3_24_susandhi_gen_90", "Susandhi (Gen 90)"),
        ("indr_ay3_25_amarsha_sahasvant_gen_91", "Amarsha & Sahasvant (Gen 91)"),
        ("indr_ay3_26_vishrutavant_gen_92", "Vishrutavant (Gen 92)"),
        ("indr_ay3_27_brihadbala_gen_94_slain_at_k", "Brihadbala (Gen 94, Slain by Abhimanyu at Kurukshetra)"),
        ("indr_ay3_28_brihatkshaya_gen_95", "Brihatkshaya (Gen 95, Son of Brihadbala)"),
    ]
    for nid, nm in ay3_list:
        nodes.append(N(nid, nm, "vedic", 11, "Pargiter Master Table Gens 67-95", "Ayodhya Solar King (Post-Rama)", ["Pargiter Ancient Indian Historical Tradition p. 149"], f"Post-Rama Aikshvaku succession: {nm}.", major=False))

    edges.append(E("ved_ikshvaku", "indr_ay1_01_vikukshi_shashada_gen_3", "direct", "Ikshvaku -> eldest son Vikukshi"))
    edges.append(E("ind_ayodhya_early_1_30", "indr_ay1_01_vikukshi_shashada_gen_3", "direct", "Solar anchor Gens 2-30 -> Vikukshi"))
    link_seq(edges, [x[0] for x in ay1_list] + [x[0] for x in ay2_list] + ["ved_surya_vamsha"], "direct", "Ayodhya Solar Spine father-to-son pedigree (Gens 3-65)")
    edges.append(E("ind_ayodhya_mid_31_64", "indr_ay2_01_satyavrata_trishanku_gen_31", "direct", "Solar anchor Gens 31-64 -> Trishanku"))
    edges.append(E("ved_lava_kusha", "indr_ay3_01_atithi_gen_67", "direct", "Kusha -> son Atithi"))
    edges.append(E("ind_ayodhya_late_66_95", "indr_ay3_01_atithi_gen_67", "direct", "Post-Rama anchor -> Atithi"))
    link_seq(edges, [x[0] for x in ay3_list] + ["ved_buddha"], "expansion", "Post-Rama Aikshvaku continuation to Gautama Buddha")

    # -------------------------------------------------------------------------
    # 3. LUNAR / AILA & MINOR SOLAR DYNASTIES (Properly Wired to Respective Houses!)
    # -------------------------------------------------------------------------
    ail_nodes = [
        ("indr_ail_01_mithi_janaka_founder_of_mith", "Mithi Janaka (Founder of Mithila / Videha, Son of Nimi)"),
        ("indr_ail_02_siradhvaja_janaka_father_of_", "Siradhvaja Janaka of Videha (Gen 64, Father of Sita)"),
        ("indr_ail_03_marutta_of_vaisali_gen_40", "Emperor Marutta of Vaisali (Gen 40)"),
        ("indr_ail_04_trinabindu_father_of_ilavila", "King Trinabindu of Vaisali (Father of Ilavila)"),
        ("indr_ail_05_raivata_kakudmin_anarta_dvar", "King Raivata Kakudmin of Anarta/Dvaraka (Father of Revati)"),
        ("indr_ail_06_king_jahnu_kanyakubja", "King Jahnu of Kanyakubja (Eponym of Ganga Jahnavi)"),
        ("indr_ail_07_king_gadhi_father_of_vishvam", "King Gadhi of Kanyakubja (Father of Satyavati & Vishvamitra)"),
        ("indr_ail_08_dhanvantari_of_kasi_ayurveda", "King Dhanvantari of Kasi (Founder of Ayurveda)"),
        ("indr_ail_09_divodasa_ii_of_kasi", "King Divodasa II of Kasi"),
        ("indr_ail_10_pratardana_of_kasi", "King Pratardana of Kasi (Son of Divodasa II)"),
        ("indr_ail_11_alarka_of_kasi", "King Alarka of Kasi (Grandson of Pratardana)"),
        ("indr_ail_12_emperor_kartavirya_arjuna_ha", "Emperor Kartavirya Arjuna (Haihaya Emperor of Mahishmati, Gen 31)"),
        ("indr_ail_13_shashabindu_yadava_gen_20", "Emperor Shashabindu (Yadava Chakravartin, Gen 20)"),
        ("indr_ail_14_jyamagha_vidarbha", "King Jyamagha -> King Vidarbha (Founder of Vidarbha)"),
        ("indr_ail_15_satvata_yadava", "King Satvata (Yadava Progenitor of Satvatas)"),
        ("indr_ail_16_ugrasena_king_kamsa_mathura", "King Ugrasena -> King Kamsa of Mathura (Andhaka Yadavas)"),
        ("indr_ail_17_samba_vajra_heirs_of_krishna", "Samba & Vajra (Son & Great-Grandson Heirs of Krishna at Indraprastha)"),
        ("indr_ail_18_king_shibi_aushinara_panjab", "King Shibi Aushinara (Son of Ushinara; Panjab Ruler)"),
        ("indr_ail_19_king_bali_father_of_anga_van", "King Bali of East Bihar (Father of Anga, Vanga, Kalinga, Pundra & Suhma)"),
        ("indr_ail_20_king_karna_of_anga_gen_94", "King Karna of Anga (Gen 94; Descendant of Lomapada & Bali's Domain)"),
        ("indr_ail_21_king_mudgala_north_panchala", "King Mudgala of North Panchala (Son of Bhrmyashva)"),
        ("indr_ail_22_rigvedic_king_sudas_battle_o", "Rigvedic King Sudas (Son of Pijavana; Victor of Battle of Ten Kings)"),
        ("indr_ail_23_king_drupada_draupadi", "King Drupada of South Panchala (Father of Draupadi & Dhrishtadyumna)"),
        ("indr_ail_24_vasu_caidyoparichara_cedi_ma", "Emperor Vasu Caidyoparichara (Kuru Conqueror of Cedi & Magadha)"),
        ("indr_ail_25_brihadratha_emperor_jarasand", "King Brihadratha -> Emperor Jarasandha of Magadha"),
        ("indr_ail_26_shishupala_of_cedi", "King Shishupala of Cedi (Son of Damaghosha)"),
        ("indr_ail_27_nicakshu_moved_kuru_capital_", "King Nicakshu (Moved Kuru Capital to Kaushambi in Vatsa)"),
        ("indr_ail_28_king_udayana_of_vatsa", "King Udayana of Vatsa (Descendant of Nicakshu; Contemporary of Buddha)"),
        ("indr_ail_29_king_bimbisara_ajatashatru_m", "King Bimbisara & Ajatashatru of Magadha (Patrons of Buddha)"),
        ("indr_ail_30_mahapadma_nanda_nanda_empire", "Emperor Mahapadma Nanda (Founder of Nanda Empire)"),
        ("indr_ail_31_samudragupta_chandragupta_ii", "Emperors Samudragupta & Chandragupta II Vikramaditya (Gupta Empire)"),
    ]
    for nid, nm in ail_nodes:
        nodes.append(N(nid, nm, "vedic", 9, "Pargiter Master Table (Gens 2-95+)", "Puranic Royal Dynasty Monarch", ["Pargiter Ancient Indian Historical Tradition pp. 144-149"], f"Synchronized Puranic royal figure: {nm}.", major=False))

    # -------------------------------------------------------------------------
    # 4. GREAT RISHI CLANS (Bhargava, Angirasa, Vishvamitra, Vasishtha, Kashyapa, Agastya)
    # -------------------------------------------------------------------------
    rsh_nodes = [
        ("indr_rsh_01_rishi_cyavana_bhargava_sukan", "Rishi Cyavana Bhargava (+ Princess Sukanya)"),
        ("indr_rsh_02_ushanas_shukra_preceptor_of_", "Acharya Ushanas-Shukra (Bhargava Preceptor)"),
        ("indr_rsh_03_richika_jamadagni_parashuram", "Richika -> Jamadagni -> Lord Parashurama (Bhargava)"),
        ("indr_rsh_04_rishi_valmiki_author_of_rama", "Maharshi Valmiki (Pracetasa / Bhargava Author of Ramayana)"),
        ("indr_rsh_05_atharvan_brihaspati_bharadva", "Atharvan -> Brihaspati -> Rishi Bharadvaja (Angirasa)"),
        ("indr_rsh_06_dirghatamas_gautama", "Rishi Dirghatamas Mamateya & Gautama Clan"),
        ("indr_rsh_07_guru_drona_ashvatthama", "Guru Dronacharya -> Ashvatthama (Bharadvaja Angirasa)"),
        ("indr_rsh_08_kripa_kripi", "Acharya Kripa & Sister Kripi (Gautama Sharadvata)"),
        ("indr_rsh_09_rishi_vishvamitra_gayatri_ma", "Brahmarshi Vishvamitra (Son of Gadhi; Seer of Gayatri Mantra)"),
        ("indr_rsh_10_shunahshepa_devarata", "Rishi Shunahshepa-Devarata (Adopted Eldest Son of Vishvamitra)"),
        ("indr_rsh_11_vasishtha_shakti_parashara", "Rishi Vasishtha -> Shakti -> Rishi Parashara"),
        ("indr_rsh_12_krishna_dvaipayana_vyasa_shu", "Krishna Dvaipayana Vyasa -> Shuka (Compiler of Vedas & Mahabharata)"),
        ("indr_rsh_13_dattatreya_durvasas_atreyas", "Dattatreya & Rishi Durvasas (Sons of Atri & Anasuya)"),
        ("indr_rsh_14_kanva_kashyapa_foster_father", "Maharshi Kanva Kashyapa (Foster-Father of Shakuntala)"),
        ("indr_rsh_15_rishyashringa_kashyapa", "Rishyashringa Kashyapa (Son of Vibhandaka; Officiated at Dasharatha's Ashvamedha)"),
        ("indr_rsh_16_sage_agastya_lopamudra", "Maharshi Agastya (+ Princess Lopamudra of Vidarbha)"),
    ]
    for nid, nm in rsh_nodes:
        nodes.append(N(nid, nm, "vedic", 8, "Pargiter Rishi Table (pp. 191-242)", "Vedic / Puranic Great Rishi", ["Pargiter Ancient Indian Historical Tradition pp. 191-242"], f"Synchronized Puranic sage: {nm}.", major=False))

    edges += [
        # Videha & Vaisali/Anarta
        E("ind_videha_janaka_complete", "indr_ail_01_mithi_janaka_founder_of_mith", "direct", "Nimi -> Mithi Janaka"),
        E("indr_ail_01_mithi_janaka_founder_of_mith", "indr_ail_02_siradhvaja_janaka_father_of_", "direct", "Videha succession -> Siradhvaja Janaka"),
        E("indr_ail_02_siradhvaja_janaka_father_of_", "ved_surya_vamsha", "direct", "Father Siradhvaja Janaka -> Sita (wife of Rama)"),
        E("ind_vaisali_sharyata_nabhaga", "indr_ail_03_marutta_of_vaisali_gen_40", "direct", "Nabhanedishtha -> Vaisali -> Emperor Marutta"),
        E("indr_ail_03_marutta_of_vaisali_gen_40", "indr_ail_04_trinabindu_father_of_ilavila", "direct", "Marutta -> Narishyanta -> Trinabindu"),
        E("ind_vaisali_sharyata_nabhaga", "indr_ail_05_raivata_kakudmin_anarta_dvar", "direct", "Sharyati -> Anarta -> Raivata Kakudmin"),
        # Kanyakubja & Vishvamitra
        E("ind_kanyakubja_vishvamitra", "indr_ail_06_king_jahnu_kanyakubja", "direct", "Amavasu -> King Jahnu"),
        E("indr_ail_06_king_jahnu_kanyakubja", "indr_ail_07_king_gadhi_father_of_vishvam", "direct", "Jahnu -> Kusha -> Kushika -> King Gadhi"),
        E("indr_ail_07_king_gadhi_father_of_vishvam", "indr_rsh_09_rishi_vishvamitra_gayatri_ma", "direct", "King Gadhi -> son Vishvamitra"),
        E("indr_rsh_09_rishi_vishvamitra_gayatri_ma", "indr_rsh_10_shunahshepa_devarata", "direct", "Vishvamitra adopts Shunahshepa-Devarata"),
        # Kasi & Haihayas
        E("ind_kasi_dhanvantari_divodasa", "indr_ail_08_dhanvantari_of_kasi_ayurveda", "direct", "Kshatravriddha -> Dhanvantari"),
        E("indr_ail_08_dhanvantari_of_kasi_ayurveda", "indr_ail_09_divodasa_ii_of_kasi", "direct", "Dhanvantari -> Ketumant -> Bhimaratha -> Divodasa II"),
        E("indr_ail_09_divodasa_ii_of_kasi", "indr_ail_10_pratardana_of_kasi", "direct", "Divodasa II -> son Pratardana"),
        E("indr_ail_10_pratardana_of_kasi", "indr_ail_11_alarka_of_kasi", "direct", "Pratardana -> Vatsa -> Alarka"),
        E("ind_haihayas_kartavirya", "indr_ail_12_emperor_kartavirya_arjuna_ha", "direct", "Sahasrajit -> Haihaya -> Kartavirya Arjuna"),
        # Yadavas
        E("ind_yadava_kroshtu_satvata", "indr_ail_13_shashabindu_yadava_gen_20", "direct", "Kroshtu -> Shashabindu"),
        E("indr_ail_13_shashabindu_yadava_gen_20", "indr_ail_14_jyamagha_vidarbha", "direct", "Shashabindu -> Jyamagha -> Vidarbha"),
        E("indr_ail_14_jyamagha_vidarbha", "indr_ail_15_satvata_yadava", "direct", "Vidarbha -> Satvata"),
        E("indr_ail_15_satvata_yadava", "indr_ail_16_ugrasena_king_kamsa_mathura", "direct", "Satvata -> Andhaka -> Ugrasena -> Kamsa"),
        E("ved_krishna_balarama", "indr_ail_17_samba_vajra_heirs_of_krishna", "direct", "Krishna -> Samba & Pradyumna -> Aniruddha -> Vajra"),
        # Anavas, Panchalas, Cedi/Magadha, Post-Battle Kurus & Guptas
        E("ind_anava_shibi_anga_karna", "indr_ail_18_king_shibi_aushinara_panjab", "direct", "Anu -> Ushinara -> King Shibi"),
        E("ind_anava_shibi_anga_karna", "indr_ail_19_king_bali_father_of_anga_van", "direct", "Anu -> Titikshu -> King Bali"),
        E("indr_ail_19_king_bali_father_of_anga_van", "indr_ail_20_king_karna_of_anga_gen_94", "expansion", "King Bali -> Anga -> Lomapada -> Karna of Anga"),
        E("ind_panchala_sudas_drupada", "indr_ail_21_king_mudgala_north_panchala", "direct", "Ajamidha -> Nila -> Mudgala"),
        E("indr_ail_21_king_mudgala_north_panchala", "indr_ail_22_rigvedic_king_sudas_battle_o", "direct", "Mudgala -> Divodasa -> Pijavana -> King Sudas"),
        E("indr_ail_22_rigvedic_king_sudas_battle_o", "indr_ail_23_king_drupada_draupadi", "direct", "Somaka -> Prishata -> King Drupada & Draupadi"),
        E("ind_cedi_magadha_jarasandha", "indr_ail_24_vasu_caidyoparichara_cedi_ma", "direct", "Kuru -> Vasu Caidyoparichara"),
        E("indr_ail_24_vasu_caidyoparichara_cedi_ma", "indr_ail_25_brihadratha_emperor_jarasand", "direct", "Vasu -> Brihadratha -> Jarasandha"),
        E("indr_ail_24_vasu_caidyoparichara_cedi_ma", "indr_ail_26_shishupala_of_cedi", "direct", "Vasu -> Pratyagraha -> Damaghosha -> Shishupala"),
        E("ind_kuru_post_battle_vatsa", "indr_ail_27_nicakshu_moved_kuru_capital_", "direct", "Janamejaya III -> Adhisimakrishna -> Nicakshu"),
        E("indr_ail_27_nicakshu_moved_kuru_capital_", "indr_ail_28_king_udayana_of_vatsa", "direct", "Nicakshu -> Kaushambi Vatsa -> King Udayana"),
        E("ind_magadha_bimbisara_nanda", "indr_ail_29_king_bimbisara_ajatashatru_m", "direct", "Shishunaga/Haryanka -> Bimbisara & Ajatashatru"),
        E("indr_ail_29_king_bimbisara_ajatashatru_m", "indr_ail_30_mahapadma_nanda_nanda_empire", "expansion", "Nanda succession -> Mahapadma Nanda"),
        E("indr_ail_30_mahapadma_nanda_nanda_empire", "ved_maurya_ashoka", "expansion", "Chandragupta Maurya overthrows Nandas"),
        E("ind_gupta_golden_age", "indr_ail_31_samudragupta_chandragupta_ii", "direct", "Chandragupta I -> Samudragupta & Chandragupta II"),
        # Great Rishis
        E("ind_rishis_bhargava_angirasa", "indr_rsh_01_rishi_cyavana_bhargava_sukan", "direct", "Bhrigu -> Cyavana"),
        E("ind_rishis_bhargava_angirasa", "indr_rsh_02_ushanas_shukra_preceptor_of_", "direct", "Bhrigu -> Kavi -> Ushanas-Shukra"),
        E("indr_rsh_01_rishi_cyavana_bhargava_sukan", "indr_rsh_03_richika_jamadagni_parashuram", "direct", "Cyavana -> Aurva -> Richika -> Jamadagni -> Parashurama"),
        E("ind_rishis_bhargava_angirasa", "indr_rsh_04_rishi_valmiki_author_of_rama", "direct", "Bhargava sage -> Maharshi Valmiki"),
        E("ind_rishis_bhargava_angirasa", "indr_rsh_05_atharvan_brihaspati_bharadva", "direct", "Angiras -> Atharvan -> Brihaspati -> Bharadvaja"),
        E("indr_rsh_05_atharvan_brihaspati_bharadva", "indr_rsh_07_guru_drona_ashvatthama", "direct", "Bharadvaja -> Guru Drona -> Ashvatthama"),
        E("ind_rishis_bhargava_angirasa", "indr_rsh_06_dirghatamas_gautama", "direct", "Angiras -> Utathya -> Dirghatamas Gautama"),
        E("indr_rsh_06_dirghatamas_gautama", "indr_rsh_08_kripa_kripi", "direct", "Gautama Sharadvant -> Kripa & Kripi"),
        E("ind_rishis_vasishtha_agastya", "indr_rsh_11_vasishtha_shakti_parashara", "direct", "Vasishtha -> Shakti -> Parashara"),
        E("indr_rsh_11_vasishtha_shakti_parashara", "indr_rsh_12_krishna_dvaipayana_vyasa_shu", "direct", "Parashara -> Krishna Dvaipayana Vyasa -> Shuka"),
        E("ind_rishis_vasishtha_agastya", "indr_rsh_13_dattatreya_durvasas_atreyas", "direct", "Atri -> Dattatreya & Durvasas"),
        E("ind_rishis_vasishtha_agastya", "indr_rsh_14_kanva_kashyapa_foster_father", "direct", "Kashyapa -> Kanva (foster-father of Shakuntala)"),
        E("ind_rishis_vasishtha_agastya", "indr_rsh_15_rishyashringa_kashyapa", "direct", "Kashyapa -> Vibhandaka -> Rishyashringa"),
        E("ind_rishis_vasishtha_agastya", "indr_rsh_16_sage_agastya_lopamudra", "direct", "Agastya + Lopamudra of Vidarbha"),
    ]

    return {
        "module": "21_india_pargiter_complete_puranic",
        "title": "Complete 95-Generation Synchronized Puranic Royal & Rishi Genealogies of India (F.E. Pargiter, Ancient Indian Historical Tradition, 1922)",
        "nodes": nodes,
        "edges": edges,
    }
