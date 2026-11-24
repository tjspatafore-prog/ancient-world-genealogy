"""
Module 21: Complete 95-Generation Synchronized Puranic Royal & Rishi Genealogies of Ancient India
from F.E. Pargiter's Ancient Indian Historical Tradition (1922, Master Table pp. 144-149 & Chs. VII-XXVII).

Covers ALL 10 branches of Vaivasvata Manu & ALL 6 Great Rishi Clans:
1. Solar (Manava): Complete 95-gen Ayodhya (Ikshvaku -> Mandhatri -> Harishchandra -> Sagara -> Bhagiratha -> Raghu -> Rama -> Brihadbala),
   Complete Videha/Janaka (Nimi -> Mithi Janaka -> Siradhvaja -> Sita), Vaisali (Nabhanedishtha -> Marutta -> Visala), Sharyatas (Anarta/Dvarka), Nabhagas.
2. Lunar (Aila): Kanyakubja (Amavasu -> Jahnu -> Gadhi -> Vishvamitra), Kasi (Kshatravriddha -> Dhanvantari -> Divodasa -> Pratardana),
   Haihayas (Sahasrajit -> Kartavirya Arjuna -> Talajanghas), Yadavas (Kroshtu -> Shashabindu -> Vidarbha -> Satvata -> Andhaka/Kamsa & Vrishni/Vasudeva/Krishna/Vajra),
   Druhyus (Gandhara -> Pracetas), Turvasus (Pandya/Kerala/Chola), Anavas (Ushinara/Shibi & Bali -> Anga/Vanga/Kalinga/Pundra/Suhma -> Karna!),
   Pauravas/Kurus (Puru -> Dushyanta/Bharata -> Hastin -> Ajamidha -> Samvarana -> Kuru -> Shantanu -> Pandavas -> Parikshit -> Janamejaya III -> Nicakshu/Udayana),
   North & South Panchalas (Mudgala, Divodasa, Sudas [Battle of Ten Kings!], Drupada/Draupadi), Dvimidhas, Cedi (Shishupala) & Magadha (Brihadratha -> Jarasandha).
3. Complete 6 Great Rishi Clans (Bhargavas, Angirasas/Kanvas, Vasishthas, Atreyas/Kashyapas, Vishvamitras, Agastyas/Paulastyas).
4. Post-Mahabharata Magadha Dynasties (Barhadratha 22 kings -> Pradyota -> Shishunaga [Bimbisara/Ajatashatru] -> 9 Nandas -> Maurya -> Gupta).
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # 1. SOLAR (MANAVA) DYNASTIES (Pargiter Ch. VIII & Master Table pp. 145, 147, 149)
    nodes += [
        N("ind_ayodhya_early_1_30", "Ayodhya Solar Spine (Gens 2–30): Ikshvaku → Vikukshi → Kakutstha → Yuvanashva I → Shravasta → Kuvalashva → Yuvanashva II → Mandhatri → Purukutsa → Trasadasyu → Trayyaruna", "vedic", 6, "Satya Yuga (Pargiter Master Table Gens 2-30, p. 145)",
          "First 30 Generations of the Solar Dynasty of Ayodhya", ["Pargiter Ancient Indian Historical Tradition pp. 90-92, 145"],
          "Complete early Aikshvaku kings: Shravasta founded Shravasti; Emperor Mandhatri (Gen 21) conquered the Pauravas & Druhyus; son Purukutsa married Narmada; grandson Trasadasyu is celebrated in the Rigveda!",
          ["Vikukshi", "Kakutstha", "Mandhatri", "Purukutsa", "Trasadasyu"]),
        N("ind_ayodhya_mid_31_64", "Ayodhya Solar Spine (Gens 31–64): Trishanku → Harishchandra → Rohita → Bahu → Sagara → Asamanjas → Amshumant → Bhagiratha → Ambarisha → Rituparna → Kalmashapada → Dilipa II → Raghu → Aja → Dasharatha", "vedic", 8, "Treta Yuga (Pargiter Master Table Gens 31-64, pp. 145, 147)",
          "Golden Era of the Solar Dynasty Leading to Lord Rama", ["Pargiter Ancient Indian Historical Tradition pp. 92-94, 145-147"],
          "Satyavrata-Trishanku & truthful King Harishchandra (Gen 32); Emperor Sagara (Gen 41, destroyed the Haihaya raiders!); Bhagiratha (Gen 45, brought the Ganges to earth); Rituparna (Gen 51, host of Nala!); Dilipa II -> Raghu -> Aja -> Dasharatha (Gen 64).",
          ["Trishanku", "Harishchandra", "Sagara", "Bhagiratha", "Rituparna", "Dilipa II"]),
        N("ind_ayodhya_late_66_95", "Ayodhya Post-Rama Spine (Gens 66–95): Kusha → Atithi → Nishadha → Nala → Hiranyanabha (Yoga Master!) → Pushya → Agnivarna → Maru → Brihadbala (Slain at Kurukshetra) → Brihatkshaya", "vedic", 11, "Dvapara Yuga (Pargiter Master Table Gens 66-95, p. 149)",
          "30 Generations from Rama's Son Kusha to the Mahabharata War", ["Pargiter Ancient Indian Historical Tradition pp. 94-95, 149"],
          "Complete post-Rama Solar kings down to Gen 94 King Brihadbala of Kosala (slain by Arjuna's son Abhimanyu at the Bharata Battle, c. 950 BCE!) and continuing via Divakara to the Shakya clan of Gautama Buddha!",
          ["Atithi", "Hiranyanabha", "Agnivarna", "Brihadbala"]),
        N("ind_videha_janaka_complete", "Videha / Mithila Solar Dynasty (All 54 Kings): Nimi → Mithi Janaka → Udavasu → Hrasvaroman → Siradhvaja Janaka (Father of Sita!) & Kushadhvaja → Bahulashva → Kritakshana → Janaka-Ugrasena", "vedic", 9, "Gens 2-98 (Pargiter Ch. VIII pp. 95-96, 145-149, 330)",
          "Philosopher-Kings of Mithila (Upanishadic Janakas & Ramayana)", ["Pargiter Ancient Indian Historical Tradition pp. 95-96, 145-149"],
          "Founded by Ikshvaku's son Nimi -> Mithi Janaka (founder of Mithila). Siradhvaja Janaka (Gen 64, contemporary of Dasharatha) discovered Goddess Sita; post-battle Janaka-Ugrasena & Janaka-Dharmadhvaja appear in the Brihadaranyaka Upanishad with sage Yajnavalkya!",
          ["Mithi Janaka", "Siradhvaja Janaka (Father of Sita)", "Kushadhvaja", "Kritakshana"]),
        N("ind_vaisali_sharyata_nabhaga", "Manu's Other Solar Kingdoms: Vaisali (Nabhanedishtha → Bhalandana → Marutta → Trinabindu → Vishala → Pramati), Sharyatas (Anarta/Dvaraka → Raivata Kakudmin) & Nabhagas (Ambarisha → Rathitara)", "vedic", 7, "Gens 2-64 (Pargiter Ch. VIII pp. 97-98, 145, 147)",
          "Ancient Dynasties of North Bihar (Vaisali) & Gujarat (Anarta)", ["Pargiter Ancient Indian Historical Tradition pp. 97-98, 145-147"],
          "Nabhanedishtha's line produced Emperor Marutta (Gen 40), Trinabindu (whose daughter Ilavila married Rishi Pulastya -> Vishravas -> Kubera & Ravana!), and Vishala (founder of Vaisali). Sharyati's line ruled Anarta (Gujarat), whose princess Revati married Balarama!",
          ["Nabhanedishtha", "Marutta of Vaisali", "Trinabindu", "Vishala", "Sharyati -> Raivata Kakudmin"]),

        # 2. LUNAR (AILA) MINOR & MAJOR DYNASTIES (Pargiter Ch. IX & Master Table pp. 144-149)
        N("ind_kanyakubja_vishvamitra", "Kanyakubja Dynasty (Amavasu Line): Amavasu → Bhima → Jahnu → Kusha → Kushika → King Gadhi → Vishvamitra (Kshatriya-Turned-Brahmarshi!) → Ashtaka → Lauhi", "vedic", 8, "Gens 4-35 (Pargiter Ch. IX pp. 99-101, 144, 146)",
          "Aila Kingdom of Kanauj & Origin of the Gayatri Mantra Rishi Vishvamitra", ["Pargiter Ancient Indian Historical Tradition pp. 99-101, 234-237"],
          "Pururavas's second son Amavasu founded Kanyakubja -> Jahnu (adopted River Ganga as 'Jahnavi') -> Gadhi (whose daughter Satyavati married Bhargava Richika -> Jamadagni -> Parashurama!) -> Vishvaratha-Vishvamitra (composer of Rigveda Mandala III & Gayatri Mantra; adopted Shunahshepa-Devarata!).",
          ["Amavasu", "King Jahnu", "King Gadhi", "Rishi Vishvamitra"], major=True),
        N("ind_kasi_dhanvantari_divodasa", "Kasi (Varanasi) Dynasty: Kshatravriddha → Sunahotra → Kasha → Dhanvantari (Father of Ayurveda!) → Divodasa I & II → Pratardana → Alarka → Subahu", "vedic", 8, "Gens 5-94 (Pargiter Ch. IX p. 101; Ch. XIII pp. 153-155)",
          "Ancient Sacred Kingdom of Varanasi & Origin of Ayurveda", ["Pargiter Ancient Indian Historical Tradition pp. 101, 145-155"],
          "Ayu's son Kshatravriddha founded Kasi (Varanasi); King Dhanvantari is revered as the founder of Ayurvedic medicine; Divodasa II & Pratardana (Gen 41) broke Haihaya dominance alongside Sagara of Ayodhya!",
          ["Kshatravriddha", "Dhanvantari", "Divodasa of Kasi", "Pratardana", "Alarka"]),
        N("ind_haihayas_kartavirya", "Haihaya Dynasty (Yadu → Sahasrajit): Haihaya → Mahishmant (Mahishmati) → Bhadrashrenya → Kritavirya → Emperor Kartavirya Arjuna → Jayadhvaja → Talajanghas (5 Clans)", "vedic", 8, "Gens 7-41 (Pargiter Ch. IX p. 102, 144, 146)",
          "Central Indian Narmada Empire & Nemesis of Parashurama & Sagara", ["Pargiter Ancient Indian Historical Tradition pp. 102, 144-146, 153-156"],
          "Kartavirya Arjuna (Gen 31, thousand-armed emperor of Mahishmati) captured Ravana, raided Kasi and Ayodhya, and clashed fatally with Bhargava Parashurama; his descendants the 5 Talajangha clans (Vitihotras, Bhojas, Avantis, Sharyatas, Tundikeras) were finally crushed by Sagara (Gen 41).",
          ["Sahasrajit", "Kartavirya Arjuna", "Talajangha", "Vitihotra"], major=True),
        N("ind_yadava_kroshtu_satvata", "Yadava Main Line (Kroshtu → Satvata): Shashabindu → Jyamagha → Vidarbha (Cedi & Kratha-Bhima) → Madhu → Satvata → Andhaka (Kukura → Ugrasena → Kamsa) & Vrishni (Shura → Vasudeva → Krishna → Samba & Vajra)", "vedic", 10, "Gens 7-95 (Pargiter Ch. IX pp. 102-107, 144-148)",
          "Complete Yadava Pedigree from Yadu to Krishna, Kamsa & Surviving Heir Vajra", ["Pargiter Ancient Indian Historical Tradition pp. 102-107, 144-148, 284"],
          "Unites ALL Yadava branches: Shashabindu (Gen 20), Jyamagha -> Vidarbha (founder of Vidarbha & Cedi), Madhu (eponym of Mathura/Madhava), Satvata -> Andhaka (Ugrasena -> King Kamsa; Kritavarman) & Vrishni (Devamidhusha -> Shura -> Vasudeva & Kunti -> Krishna, Balarama, Satyaki; grandson Vajra installed at Indraprastha!).",
          ["Kroshtu", "Shashabindu", "Vidarbha", "Satvata", "King Kamsa", "Samba & Vajra"]),
        N("ind_druhyu_gandhara_turvasu", "Druhyus (Gandhara → Pracetas — Northward Migration Beyond India!) & Turvasus (Marutta → Adopted Dushyanta → Pandya, Kerala & Chola)", "vedic", 8, "Gens 7-44 (Pargiter Ch. IX p. 108, 144, 146)",
          "Northwest (Gandhara/Central Asia) & South Indian (Tamil) Aila Bridges", ["Pargiter Ancient Indian Historical Tradition pp. 108, 144, 146"],
          "Druhyu's descendant Gandhara gave his name to Gandhara (NW Pakistan/Afghanistan); Pracetas's 100 sons migrated north beyond the Himalayas into mleccha lands! Turvasu's line merged into the Pauravas via Marutta's adoption of Dushyanta, with southern Puranic tradition deriving Pandya, Kerala, and Chola from it.",
          ["Gandhara", "Pracetas", "Pandya / Kerala / Chola"]),
        N("ind_anava_shibi_anga_karna", "Anavas (Anu's Two Empires): NW Panjab (Ushinara → King Shibi → Kekaya, Madra, Sauvira) & East Bihar (Titikshu → Bali → Anga, Vanga, Kalinga, Pundra, Suhma → Lomapada → King Karna!)", "vedic", 9, "Gens 7-95 (Pargiter Ch. IX pp. 108-109, 145-149)",
          "Progenitors of Punjab (Shibi/Kekaya) & Eastern India (Bengal/Odisha/Anga)", ["Pargiter Ancient Indian Historical Tradition pp. 108-109, 145-149"],
          "Mahamanas split the Anavas: Ushinara -> famously compassionate King Shibi (and Kekaya/Madra, mothers of Bharata & Nakula/Sahadeva!); Titikshu -> King Bali -> 5 sons founding Anga, Vanga (Bengal!), Kalinga (Odisha!), Pundra & Suhma -> Lomapada (friend of Dasharatha) -> Mahabharata hero Karna -> Vrishasena!",
          ["Ushinara", "King Shibi", "King Bali -> Anga/Vanga/Kalinga", "Karna of Anga"], major=True),
        N("ind_panchala_sudas_drupada", "North & South Panchalas (Ajamidha → Nila & Brihadvasu): Mudgala → Divodasa (Atithigva) → King Sudas (Battle of the Ten Kings!) → Drupada → Draupadi & Dhrishtadyumna (+ Drona & Ashvatthama)", "vedic", 10, "Gens 53-95 (Pargiter Ch. IX pp. 115-117, 146, 148)",
          "Rigvedic Battle of Ten Kings Hero Sudas & Panchala Allies of the Pandavas", ["Pargiter Ancient Indian Historical Tradition pp. 115-117, 146-148", "Rigveda VII.18"],
          "Ajamidha's son Nila founded North Panchala (Ahicchattra): Bhrmyashva's 5 sons ('Panchalas') -> Mudgala -> Vadhryashva -> Divodasa (sister Ahalya!) -> King Sudas (victor of the Rigvedic Dasharajna / Battle of Ten Kings against Samvarana & the Ten Tribes!) -> Drupada (father of Draupadi & Dhrishtadyumna, rival of Guru Drona!).",
          ["Mudgala", "Rigvedic King Sudas", "King Drupada", "Queen Draupadi", "Dhrishtadyumna"], major=True),
        N("ind_cedi_magadha_jarasandha", "Cedi & Magadha (Kuru → Sudhanvan → Vasu Uparichara): Brihadratha → Jarasandha → Sahadeva → Somadhi (Magadha) & Damaghosha → Shishupala (Cedi)", "vedic", 11, "Gens 73-95 (Pargiter Ch. IX pp. 118-119, 149)",
          "First Historical Dynasty of Magadha (Barhadrathas) & Cedi", ["Pargiter Ancient Indian Historical Tradition pp. 118-119, 149"],
          "Kuru's son Sudhanvan's descendant Emperor Vasu Caidyoparichara conquered Cedi & Magadha; his eldest son Brihadratha founded the Barhadratha Dynasty of Magadha -> Emperor Jarasandha (slain by Bhima!) -> Sahadeva -> Somadhi (start of the 22 post-battle Barhadratha kings!).",
          ["Vasu Uparichara", "Brihadratha", "Jarasandha of Magadha", "Shishupala of Cedi"], major=True),
        N("ind_kuru_post_battle_vatsa", "Post-Mahabharata Kurus (Gens 96–105+): Parikshit II → Janamejaya III → Shatanika → Adhisimakrishna (c. 850 BCE) → Nicakshu (Moved Capital to Kaushambi!) → King Udayana of Vatsa", "vedic", 12, "c. 950-500 BCE (Pargiter Ch. XXIV p. 285; Ch. XXVII p. 330)",
          "Continuation of the Pandava/Kuru Royal Line After Hastinapura Flood", ["Pargiter Ancient Indian Historical Tradition pp. 285, 330"],
          "When the Ganges washed away Hastinapura c. 820 BCE, Arjuna's 6th-generation descendant Nicakshu moved the Kuru capital to Kaushambi in Vatsa — culminating in famed King Udayana of Vatsa, contemporary of Gautama Buddha!",
          ["Adhisimakrishna", "Nicakshu (Kaushambi)", "King Udayana of Vatsa"]),

        # 3. COMPLETE 6 GREAT RISHI CLANS (Pargiter Ch. XVI-XXII, Table pp. 191-192)
        N("ind_rishis_bhargava_angirasa", "Bhargavas (Bhrigu → Shukra, Cyavana, Urva → Richika → Jamadagni → Parashurama, Valmiki) & Angirasas (Atharvan → Brihaspati → Bharadvaja → Drona → Ashvatthama; Dirghatamas → Gautama → Kripa; Kanvas)", "vedic", 8, "Gens 2-94 (Pargiter Ch. XVII & XIX, pp. 191-202, 218-227)",
          "Complete Genealogies of the Bhargava, Angirasa & Kanva Seers", ["Pargiter Ancient Indian Historical Tradition pp. 191-202, 218-227"],
          "Synchronizes every great Vedic & Epic sage with the 95-generation royal table: Cyavana (Gen 2), Shukra (Gen 5), Richika/Jamadagni/Parashurama (Gens 31-33), Atharvan/Brihaspati/Dirghatamas/Bharadvaja (Gens 38-41), Valmiki (Gen 64, author of Ramayana!), and Bharadvaja -> Guru Drona -> Ashvatthama (Gens 92-94).",
          ["Cyavana", "Jamadagni & Parashurama", "Rishi Valmiki", "Bharadvaja -> Drona", "Dirghatamas"], major=True),
        N("ind_rishis_vasishtha_agastya", "Vasishthas (Vasishtha → Shakti → Parashara → Vyasa → Shuka), Atreyas (Datta & Durvasas), Kashyapas (Kanva, Rishyashringa) & Agastya (+ Lopamudra)", "vedic", 9, "Gens 1-94 (Pargiter Ch. XVIII, XX, XXII, pp. 203-242)",
          "Complete Pedigrees of Vyasa, Durvasas, Rishyashringa & Agastya", ["Pargiter Ancient Indian Historical Tradition pp. 203-242"],
          "Traces the genuine Vasishtha pedigree (Gen 68 Vasishtha with Sudas -> Shakti -> Parashara -> Krishna Dvaipayana Vyasa [Gen 92, compiler of Vedas & Mahabharata!] -> Shuka), Atreya sages Datta & Durvasas (Gen 31), Kashyapa foster-father Kanva (of Shakuntala) & Rishyashringa, and Agastya (+ Lopamudra of Vidarbha, Gen 42).",
          ["Shakti -> Parashara -> Vyasa", "Dattatreya & Durvasas", "Rishyashringa", "Agastya & Lopamudra"]),

        # 4. POST-MAHABHARATA MAGADHA TO GUPTA EMPIRES (Pargiter Ch. XV & XXIV, pp. 179-182, 286-287)
        N("ind_magadha_bimbisara_nanda", "Historical Magadha Empires: Barhadrathas (22 Kings) → Pradyotas (5 Kings) → Haryanka/Shishunaga (King Bimbisara & Ajatashatru — Patrons of Buddha!) → 9 Nandas (Mahapadma Nanda)", "vedic", 16, "c. 950-322 BCE (Pargiter pp. 179-182, 286-287)",
          "Bridge from Mahabharata Magadha to Buddha, Alexander & Chandragupta Maurya", ["Pargiter Ancient Indian Historical Tradition pp. 179-182, 286-287"],
          "Pargiter's critical chronology: 22 Barhadrathas (c. 950-619 BCE) -> 5 Pradyotas -> Shishunaga/Haryanka (Bimbisara & Ajatashatru, contemporaries of Buddha c. 487 BCE!) -> Mahapadma Nanda & 8 sons (exterminated all 10 ancient Kshatriya kingdoms c. 382 BCE, creating the vast empire seized by Chandragupta Maurya in 322 BCE!).",
          ["King Bimbisara", "Ajatashatru", "Shishunaga", "Mahapadma Nanda"], major=True),
        N("ind_gupta_golden_age", "Gupta Empire (Golden Age of India): Sri Gupta → Chandragupta I (+ Kumaradevi Licchavi) → Samudragupta → Chandragupta II Vikramaditya → Kumaragupta I → Skandagupta", "vedic", 19, "c. 240-550 CE (Allahabad Pillar Inscription; Puranas)",
          "Classical Golden Age of Sanskrit, Astronomy (Aryabhata) & Nalanda", ["Allahabad Pillar Inscription", "Vishnu Purana IV.24"],
          "Chandragupta I married Licchavi princess Kumaradevi (of ancient Vaisali!), launching India's Golden Age under Samudragupta & Chandragupta II Vikramaditya (court of Kalidasa!).",
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

    # Exhaustive individual-level rosters from Pargiter's 95-Generation Master Table!
    add_roster(nodes, edges, "ind_ayodhya_early_1_30", "indr_ay1", "vedic", 6, "Pargiter Master Table Gens 3-30", "Ayodhya Solar King (Satya Yuga)", ["Pargiter Ancient Indian Historical Tradition p. 145"], [
        "Vikukshi-Shashada (Gen 3)", "Kakutstha (Gen 4)", "Anenas (Gen 5)", "Prithu (Gen 6)", "Vishtarashva (Gen 7)",
        "Ardra (Gen 8)", "Yuvanashva I (Gen 9)", "Shravasta (Gen 10, Founder of Shravasti)", "Brihadashva (Gen 11)",
        "Kuvalashva (Gen 12)", "Dridhashva (Gen 13)", "Pramoda (Gen 14)", "Haryashva I (Gen 15)", "Nikumbha (Gen 16)",
        "Samhatashva (Gen 17)", "Akrishashva (Gen 18)", "Prasenajit (Gen 19)", "Yuvanashva II (Gen 20)",
        "Emperor Mandhatri (Gen 21)", "Purukutsa (Gen 22)", "Trasadasyu (Gen 23, Rigvedic King)", "Sambhuta (Gen 24)",
        "Anaranya (Gen 25)", "Trasashva (Gen 26)", "Haryashva II (Gen 27)", "Vasumata (Gen 28)", "Tridhanvan (Gen 29)", "Trayyaruna (Gen 30)"
    ], edge_type="direct", edge_label="Ayodhya Solar Spine (Gens 3-30)")

    add_roster(nodes, edges, "ind_ayodhya_mid_31_64", "indr_ay2", "vedic", 8, "Pargiter Master Table Gens 31-64", "Ayodhya Solar King (Treta Yuga)", ["Pargiter Ancient Indian Historical Tradition pp. 145, 147"], [
        "Satyavrata-Trishanku (Gen 31)", "King Harishchandra (Gen 32)", "Rohita (Gen 33)", "Harita & Cancu (Gen 34)",
        "Vijaya (Gen 35)", "Ruruka (Gen 36)", "Vrika (Gen 37)", "Bahu / Asita (Gen 38)", "Emperor Sagara (Gen 41)",
        "Asamanjas (Gen 42)", "Amshumant (Gen 43)", "Dilipa I (Gen 44)", "Bhagiratha (Gen 45, Brought the Ganga)",
        "Shruta (Gen 46)", "Nabhaga (Gen 47)", "Ambarisha (Gen 48)", "Sindhudvipa (Gen 49)", "Ayutayus (Gen 50)",
        "Rituparna (Gen 51, Host of Nala)", "Sarvakama (Gen 52)", "Sudasa of Ayodhya (Gen 53)", "Mitrasaha-Kalmashapada (Gen 54)",
        "Ashmaka (Gen 55)", "Mulaka (Gen 56)", "Shataratha (Gen 57)", "Aidavida (Gen 58)", "Vishvasaha I (Gen 59)",
        "Dilipa II Khatvanga (Gen 60)", "Dirghabahu (Gen 61)", "Emperor Raghu (Gen 62)", "Aja (Gen 63)", "King Dasharatha (Gen 64)"
    ], edge_type="direct", edge_label="Ayodhya Solar Spine (Gens 31-64)")

    add_roster(nodes, edges, "ind_ayodhya_late_66_95", "indr_ay3", "vedic", 11, "Pargiter Master Table Gens 66-95", "Ayodhya Solar King (Post-Rama)", ["Pargiter Ancient Indian Historical Tradition p. 149"], [
        "Atithi (Gen 67)", "Nishadha (Gen 68)", "Nala of Ayodhya (Gen 69)", "Nabhas (Gen 70)", "Pundarika (Gen 71)",
        "Kshemadhanvan (Gen 72)", "Devanika (Gen 73)", "Ahinagu (Gen 74)", "Paripatra (Gen 75)", "Dala & Bala (Gen 76)",
        "Uktha (Gen 77)", "Vajranabha (Gen 78)", "Shankhana (Gen 79)", "Vyushitashva (Gen 80)", "Vishvasaha II (Gen 81)",
        "Hiranyanabha (Gen 82, Yoga Master)", "Pushya (Gen 83)", "Dhruvasandhi (Gen 84)", "Sudarshana (Gen 85)",
        "Agnivarna (Gen 86)", "Shighra (Gen 87)", "Maru (Gen 88)", "Prasushruta (Gen 89)", "Susandhi (Gen 90)",
        "Amarsha & Sahasvant (Gen 91)", "Vishrutavant (Gen 92)", "Brihadbala (Gen 94, Slain at Kurukshetra)", "Brihatkshaya (Gen 95)"
    ], edge_type="direct", edge_label="Ayodhya Solar Spine (Gens 67-95)")

    add_roster(nodes, edges, "ind_yadava_kroshtu_satvata", "indr_ail", "vedic", 9, "Pargiter Master Table (Lunar Dynasties)", "Lunar (Aila) Dynasty Monarch", ["Pargiter Ancient Indian Historical Tradition pp. 144-149"], [
        "Mithi Janaka (Founder of Mithila)", "Siradhvaja Janaka (Father of Sita)", "Marutta of Vaisali (Gen 40)",
        "Trinabindu (Father of Ilavila)", "Raivata Kakudmin (Anarta/Dvaraka)", "King Jahnu (Kanyakubja)", "King Gadhi (Father of Vishvamitra)",
        "Dhanvantari of Kasi (Ayurveda)", "Divodasa II of Kasi", "Pratardana of Kasi", "Alarka of Kasi",
        "Emperor Kartavirya Arjuna (Haihaya, Gen 31)", "Shashabindu (Yadava, Gen 20)", "Jyamagha -> Vidarbha", "Satvata (Yadava)",
        "Ugrasena -> King Kamsa (Mathura)", "Samba & Vajra (Heirs of Krishna)", "King Shibi Aushinara (Panjab)",
        "King Bali (Father of Anga, Vanga, Kalinga, Pundra, Suhma)", "King Karna of Anga (Gen 94)",
        "King Mudgala (North Panchala)", "Rigvedic King Sudas (Battle of Ten Kings)", "King Drupada & Draupadi",
        "Vasu Caidyoparichara (Cedi/Magadha)", "Brihadratha -> Emperor Jarasandha (Magadha)", "Shishupala of Cedi",
        "Nicakshu (Moved Kuru Capital to Kaushambi)", "King Udayana of Vatsa", "King Bimbisara & Ajatashatru (Magadha)",
        "Mahapadma Nanda (Nanda Empire)", "Samudragupta & Chandragupta II (Gupta Empire)"
    ], edge_type="direct", edge_label="Pargiter Master Table Monarch")

    add_roster(nodes, edges, "ind_rishis_bhargava_angirasa", "indr_rsh", "vedic", 8, "Pargiter Rishi Table (pp. 191-242)", "Vedic / Puranic Great Rishi", ["Pargiter Ancient Indian Historical Tradition pp. 191-242"], [
        "Rishi Cyavana Bhargava (+ Sukanya)", "Ushanas-Shukra (Preceptor of Asuras)", "Richika -> Jamadagni -> Parashurama",
        "Rishi Valmiki (Author of Ramayana)", "Atharvan -> Brihaspati -> Bharadvaja", "Dirghatamas Gautama",
        "Guru Drona & Ashvatthama", "Kripa & Kripi", "Rishi Vishvamitra (Gayatri Mantra)", "Shunahshepa-Devarata",
        "Vasishtha -> Shakti -> Parashara", "Krishna Dvaipayana Vyasa -> Shuka", "Dattatreya & Durvasas (Atreyas)",
        "Kanva Kashyapa (Foster-Father of Shakuntala)", "Rishyashringa Kashyapa", "Sage Agastya & Lopamudra"
    ], edge_type="direct", edge_label="Pargiter Synchronized Rishi Lineage")

    return {
        "module": "21_india_pargiter_complete_puranic",
        "title": "Complete 95-Generation Synchronized Puranic Royal & Rishi Genealogies of India (F.E. Pargiter, Ancient Indian Historical Tradition, 1922)",
        "nodes": nodes,
        "edges": edges,
    }
