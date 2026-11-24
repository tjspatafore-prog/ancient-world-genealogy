"""
Module 19: Caucasian / Georgian Chronicles (Kartlis Tskhovreba), Al-Biruni's Chronology of Ancient Nations
(Parthian/Ashkanian, Sasanian, Afrighid Khwarazmia, Himyarite & Lakhmid), and Budge's Ethiopic Kebra Nagast.

Sources mined from sources/:
- Kartlis Cxovreba 2012 Eng.pdf (Leonti Mroveli, Juansher & Sumbat Davitisdze, Georgian National Academy of Sciences)
- chronologyofanci00biru.pdf (Al-Biruni, Chronology of Ancient Nations, trans. C.E. Sachau 1879)
- queenofshebahero00kebr.pdf (The Kebra Nagast, trans. E.A. Wallis Budge 1922)
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. CAUCASIAN TABLE OF NATIONS & KINGS OF GEORGIA (Kartlis Tskhovreba, pp. 13-217)
    # -------------------------------------------------------------------------
    nodes += [
        N("geo_targamos_8sons", "Targamos (Togarmah) → 8 Caucasian Hero-Sons: Haos (Armenia), Kartlos (Georgia), Bardos, Movak'an, Lek' (Dagestan), Heros, K'avk'as (North Caucasus) & Egros (Colchis)", "iranian", 7, "Caucasian Table of Nations (Kartlis Tskhovreba pp. 13-18)",
          "Patriarchal Origin of All Peoples of the Caucasus", ["Kartlis Tskhovreba (Leonti Mroveli pp. 13-18)"],
          "Targamos (Togarmah, lived 600 yrs between Mt. Ararat & Masis) divided the Caucasus among 8 sons: eldest Haos (slew Nimrod/Nebroth with an arrow! Progenitor of Armenians), Kartlos (Georgians), Bardos (Barda), Movak'an (Albania), Lek' (Lezgins), Heros (Hereti), K'avk'as (Durdzuks/Vainakhs), Egros (Megrels/Colchis) — plus Khazar prince Uobos (Ossetians)!",
          ["Haos / Hayk (Armenia)", "Kartlos (Georgia)", "K'avk'as", "Egros", "Lek'", "Uobos (Ossetians)"], major=True),
        N("geo_kartlos_5sons_uplos", "Kartlos's 5 Sons (Mtskhetos, Gardabos, K'akhos, K'ukhos, Gachios) → Mtskhetos's 3 Sons (Uplos, Odzrkhos, Javakhos)", "iranian", 8, "Proto-Georgian Heroic Era (Kartlis Tskhovreba p. 16)",
          "Founders of Mtskheta, Kakheti, Gardabani, Uplistsikhe & Javakheti", ["Kartlis Tskhovreba (Leonti Mroveli p. 16)"],
          "Kartlos's widow divided Kartli among his 5 sons; preeminent Mtskhetos founded Mtskheta and fathered Uplos (Uplistsikhe — ancestor of King Parnavaz I!), Odzrkhos, and Javakhos.",
          ["Mtskhetos", "Uplos", "K'akhos", "Javakhos"]),
        N("geo_parnavaz_nebrothids", "Kings of Iberia/Kartli (1–23): Pharnavazids (Parnavaz I → Saurmag), Nebrotids (Mirvan I, Parnajom, Mirvan II) & Arshak'ids (Arshak I, Aderk'i, Parsman the Valiant, Rev I → Aspagur)", "iranian", 18, "c. 299 BCE – 284 CE (Kartlis Tskhovreba pp. 22-41)",
          "First Royal Dynasties of Georgia & Creator of the Georgian Script (Parnavaz I)", ["Kartlis Tskhovreba (Leonti Mroveli pp. 22-41)"],
          "Parnavaz I (kinsman of Uplos, mother from Isfahan, allied with Kuji of Egrisi) defeated Alexander's governor Azon and created the Georgian alphabet! Followed by Nimrodid ('Nebrotid') and Armenian-Parthian Arshak'id lines down to last Pharnavazid Aspagur -> daughter Abeshuru.",
          ["King Parnavaz I", "Saurmag", "Mirvan I (Nebrotid)", "Aderk'i", "Parsman the Valiant"], major=True),
        N("geo_chosroids_mirian_vakhtang", "Chosroid (Mihranid-Sasanian) Dynasty (24–33+): King Mirian III (+ St. Nino, Christianized Georgia 337 CE!) → Bakar → Archil → King Vakht'ang I Gorgasali (Founder of Tbilisi!) → Dachi", "iranian", 19, "284-580 CE (Kartlis Tskhovreba pp. 41-108)",
          "Christianizers of Georgia & Founder of Tbilisi (Sasanian-Iberian Bloodline)", ["Kartlis Tskhovreba (Leonti Mroveli & Juansher pp. 41-108)"],
          "Mirian III (Persian prince Mikhran, son of a Sasanian king; married Pharnavazid heiress Abeshuru & Queen Nana) embraced Christianity via St. Nino of Cappadocia! Descendant King Vakht'ang Gorgasali ('Wolf-Head', married both a Persian princess Balendukht & Byzantine princess Helen!) founded Tbilisi!",
          ["King Mirian III & St. Nino", "Vakht'ang Gorgasali", "King Dachi"], major=True),
        N("geo_bagrationi_davidic", "Bagrat'ioni Dynasty (Sumbat Davitisdze): King David → Joseph's Brother K'leop'a (26 Gens!) → 7 Brothers (Bagrat' & Guaram Kuropalates) → Ashot' the Great → Bagrat' III (1st King of Unified Georgia, 1008!) → David IV the Builder & Queen Tamar", "iranian", 19, "588-1213 CE (Kartlis Tskhovreba, Sumbat Davitisdze pp. 211-217)",
          "World's Longest-Reigning Christian Royal House (Claiming Direct Davidic Descent via Clopas!)", ["Kartlis Tskhovreba (Sumbat Davitisdze pp. 211-217)"],
          "Uniquely bridges Matthew 1 -> Joseph's brother K'leop'a -> 26 generations -> 7 brothers baptized by Queen Rakael -> Bagrat' & Guaram Kuropalates -> Ashot' I the Great (d. 826) -> Bagrat' III (united Abkhazia & Kartli, d. 1014) -> Giorgi I -> David IV the Builder -> Queen Tamar the Great!",
          ["Guaram Kuropalates", "Ashot' I the Great", "Bagrat' III", "David IV the Builder", "Queen Tamar"], major=True),

        # -------------------------------------------------------------------------
        # 2. AL-BIRUNI'S CHRONOLOGY OF ANCIENT NATIONS (Parthians, Sasanians, Afrighid Khwarazmia, Himyar)
        # -------------------------------------------------------------------------
        N("bir_parthians_ashkanians", "Parthian / Ashkanian Empire (Arsacids): Ashk ben Ashkan (Al-Biruni Traces to Kayanian Siyavush!) → Arsaces I → Mithridates I & II → Phraates → Orodes II → Vologases → Artabanus IV", "iranian", 18, "247 BCE – 224 CE (Al-Biruni pp. 116-120; Betham Tab. CV)",
          "470-Year Iranian Superpower Rivaling Rome (Bridged to Kayanian Siyavush!)", ["Al-Biruni Chronology (Sachau pp. 116-120, 401)", "Betham 1795 Tab. CV"],
          "Al-Biruni (p. 116) gives the Persian royal pedigree of Ashk ben Ashkan (Arsaces) directly back to Kayanian Prince Siyawush ben Kay Kavus — uniting historical Parthia with the Avestan/Shahnameh Kayanians! Defeated Crassus at Carrhae (53 BCE) and placed Tiridates on Armenia's throne.",
          ["Arsaces I / Ashk", "Mithridates I & II of Parthia", "Orodes II", "Vologases I", "Artabanus IV"], major=True),
        N("bir_sasanians_complete", "Sasanian Empire (Al-Biruni Pedigree from Kay Bahman & Esfandiyar!): Sasan → Papak → Ardashir I → Shapur I → Shapur II → Bahram V Gur → Kavadh I → Khosrow I Anushirvan → Khosrow II Parviz → Queen Boran → Yazdegerd III", "iranian", 19, "224-651 CE (Al-Biruni pp. 45-48, 122-130; Betham Tab. CVI-CVII)",
          "Last Pre-Islamic Persian Empire & Ancestor of Buwayhids, Bavandids & Samanids", ["Al-Biruni Chronology (Sachau pp. 45-48, 122-130)"],
          "Al-Biruni (p. 122) traces Ardashir I -> Babak -> Sasan -> Bahman -> Isfandiyar! Also preserves complete medieval pedigrees of the Buwayhids (14 gens from Bahram Gur, p. 45), Bavandids/Ziyarids (11 gens from Kavadh I, p. 47), and Samanids (9 gens from Bahram Chobin, p. 48)!",
          ["Ardashir I", "Shapur I & II", "Bahram V Gur", "Khosrow I Anushirvan", "Khosrow II", "Yazdegerd III"], major=True),
        N("bir_khwarazm_afrighids", "Afrighid Shahs of Khwarazm (Complete 22-Gen Line in Al-Biruni!): Siyawush → Kay Khosrow → Afrigh (305 CE) → Baghra → Arthamukh → Askajamuk → Shawushfar → Abu 'Abdallah Muhammad (d. 995 CE)", "iranian", 19, "305-995 CE (Al-Biruni pp. 40-42, 379)",
          "Al-Biruni's Own Homeland Dynasty — 22 Unbroken Generations from Kayanian Siyawush!", ["Al-Biruni Chronology (Sachau pp. 40-42, 379)"],
          "Preserved intact by Al-Biruni (himself a native of Khwarazm!): 22 unbroken father-to-son Khwarazmshahs starting with Afrigh's castle behind Alfir (305 CE) down to the last Afrighid martyr Abu 'Abdallah Muhammad (995 CE)!",
          ["Afrigh (305 CE)", "Arthamukh", "Askajamuk", "Shawushfar", "Abu 'Abdallah Muhammad"], major=True),
        N("bir_himyar_lakhmid_ghassan", "Pre-Islamic Arab Kingdoms: Himyarite Tubbas of Yemen (Bilkis, Castle Ghumdan, Dhu-Nuwas, Dhu-Yazan), Lakhmids of Al-Hirah (Imru' al-Qays → Al-Mundhir → Al-Nu'man III) & Ghassanids (Al-Harith)", "arabian", 19, "c. 110 BCE – 636 CE (Al-Biruni pp. 40-50, 311, 384; Kebra Nagast Ch. 117)",
          "Qahtanite / South Arabian & Syro-Mesopotamian Pre-Islamic Arab Monarchies", ["Al-Biruni Chronology (pp. 40-50, 311, 384)", "Kebra Nagast Ch. 117"],
          "Himyarite Tubba kings of Yemen (Castle Ghumdan in San'a, Dhu-al-Manar, Dhu-Nuwas [clashed with King Kaleb of Aksum over Najran in 525 CE!], Saif ibn Dhi-Yazan), Persian-allied Lakhmid kings of Al-Hirah (Battle of Dhu Qar!), and Byzantine-allied Christian Ghassanid kings of Syria!",
          ["Himyarite Tubbas", "Dhu-Nuwas (Yusuf As'ar)", "Al-Mundhir & Al-Nu'man (Lakhmids)", "Ghassanids"], major=True),

        # -------------------------------------------------------------------------
        # 3. ETHIOPIC KEBRA NAGAST EXPANSION (Budge 1922)
        # -------------------------------------------------------------------------
        N("keb_premakeda_tamrin_azaryas", "Kebra Nagast Royal Court: Pre-Makeda Kings (Arawi → Angabo → Gedur → Sebado → Kawnasya), Merchant Tamrin & High Priest 'Azaryas (Son of Zadok) + 21 Israelite Firstborn Nobles", "african", 16, "c. 960 BCE (Kebra Nagast Ch. 22-48, Intro p. xxxv)",
          "Bearers of the Ark of the Covenant (Zion) from Jerusalem to Aksum", ["Kebra Nagast (Budge 1922 Intro p. xxxv, Ch. 22-48, p. 62)"],
          "Budge's Oxford MS lists 5 pre-Makeda kings (Arawi -> Angabo -> Gedur -> Sebado -> Kawnasya -> Queen Makeda). Merchant Tamrin linked Ethiopia to Solomon; 'Azaryas (son of High Priest Zadok) and 20 named firstborn sons of Israelite nobles carried the Ark of the Covenant with Menyelek I (Bayna-Lehkem / David II) to Aksum!",
          ["Tamrin", "'Azaryas son of Zadok", "21 Israelite Firstborn Nobles", "Gedur / Kawnasya"]),
        N("keb_adrami_rome_shem", "Kebra Nagast World-Kingdoms Bridge: 'Adrami (Youngest Son of Solomon → King of Rome via 'Adlonya!), Fares → Persia & 'Akamhel (Son of Samson & Delilah → Philistia)", "african", 16, "Kebra Nagast Ch. 72-81 (Budge pp. 121-140)",
          "Ethiopic Universal Theology Tracing Rome, Ethiopia, Persia & Philistia to Israel!", ["Kebra Nagast (Budge 1922 Ch. 72-81, pp. 121-140)"],
          "Remarkable medieval cross-cultural genealogical synthesis: Solomon's youngest son 'Adrami marries 'Adlonya (daughter of Roman king Baltasar) to become King of Rome/Byzantium! Also traces Fars (Persia) to Judah's son Perez (Fares) and Philistia's kings to Samson & Delilah's posthumous son 'Akamhel (Menahem)!",
          ["'Adrami (Solomonic King of Rome)", "Zanbares & Baltasar", "'Akamhel (Son of Samson)"]),
        N("keb_kaleb_gabramaskal_yekuno", "Aksumite & Solomonic Restoration: King Kaleb of Aksum (Allied with Emperor Justinus!) → Israel & Gabra Maskal → Zagwe Lalibala → Emperor Yekuno 'Amlak (1270 CE)", "african", 19, "c. 520-1285 CE (Kebra Nagast Ch. 117 & Colophon, Budge pp. 225-229)",
          "6th-Century Aksumite Expedition to Yemen & 1270 CE Solomonic Restoration", ["Kebra Nagast (Budge 1922 Ch. 117, pp. 225-229)"],
          "King Kaleb of Aksum met Byzantine Emperor Justinus I in Jerusalem to divide the Christian world and defeated Himyarite King Dhu-Nuwas in Yemen (525 CE), abdicating to his son Gabra Maskal. After the Zagwe interlude (Takla Haymanot -> Lalibala), Yekuno 'Amlak restored the Solomonic Dynasty in 1270 CE!",
          ["King Kaleb of Aksum", "Gabra Maskal", "Takla Haymanot (Zagwe)", "Emperor Yekuno 'Amlak"], major=True),
    ]

    # Individual-level rosters for Caucasus, Georgia, Afrighids, Sasanians & Kebra Nagast 21 Nobles!
    add_roster(nodes, edges, "geo_targamos_8sons", "geor_8s", "iranian", 7, "Kartlis Tskhovreba pp. 13-18", "Caucasian Eponymous Ancestor", ["Kartlis Tskhovreba (Leonti Mroveli pp. 13-18)"], [
        "Haos / Hayk (Progenitor of Armenians, Slew Nimrod)", "Kartlos (Progenitor of Georgians)", "Bardos (Founder of Barda)",
        "Movak'an (Founder of Movak'neti / Albania)", "Lek' (Progenitor of Lezgins / Dagestan)", "Heros (Founder of Hereti)",
        "K'avk'as -> Durdzuk' (North Caucasians / Vainakhs)", "Egros (Founder of Egrisi / Colchis)", "Uobos (Khazar Ancestor of Ossetians)",
        "Mtskhetos -> Uplos, Odzrkhos & Javakhos", "Gardabos, K'akhos, K'ukhos & Gachios"
    ], edge_type="direct", edge_label="Caucasian Table of Nations (Kartlis Tskhovreba)")

    add_roster(nodes, edges, "geo_parnavaz_nebrothids", "geor_kgs", "iranian", 18, "299 BCE – 580 CE (Kartlis Tskhovreba)", "King of Kartli / Iberia", ["Kartlis Tskhovreba (pp. 22-108)"], [
        "1. Parnavaz I (1st King of Kartli, Georgian Script)", "2. Saurmag I", "3. Mirvan I (Nebrotid)", "4. Parnajom",
        "5. Arshak' I (Arshak'id)", "6. Art'ag", "7. Bart'om I", "8. Mirvan II", "9. Arshak' II", "10. Aderk'i (Birth of Christ Era)",
        "15. Parsman the Valiant (+ Queen Gadana)", "19. Rev I the Righteous", "23. Aspagur (Last Male Pharnavazid -> Abeshuru)",
        "24. Mirian III (+ Queen Nana & St. Nino)", "25. Bakar -> 26. Mirdat' -> 27. Varaz-Bakar", "31. Archil -> 32. Mirdat'",
        "33. Vakht'ang I Gorgasali (Founder of Tbilisi)", "34. King Dachi -> Bak'ur"
    ], edge_type="direct", edge_label="King of Kartli / Iberia")

    add_roster(nodes, edges, "geo_bagrationi_davidic", "geor_bag", "iranian", 19, "588-1213 CE (Sumbat Davitisdze)", "Bagrat'ioni Monarch", ["Kartlis Tskhovreba (Sumbat Davitisdze pp. 211-217)"], [
        "Bagrat' (Founder of Armenian/Georgian Bagratids)", "Guaram I Kuropalates", "St'epanoz I & Demet're (Jvari Church)",
        "Ashot' I Kuropalates the Great (d. 826)", "Bagrat' I & David I Kuropalates", "Adarnase IV (King of the Kartvels, d. 923)",
        "David III the Great Kuropalates (d. 1001)", "Gurgen King of Kings (d. 1008)", "Bagrat' III (1st King of Unified Georgia, d. 1014)",
        "King Giorgi I", "King David IV the Builder (1089-1125)", "Queen Tamar the Great (1184-1213)"
    ], edge_type="direct", edge_label="Bagrat'ioni Royal Lineage")

    add_roster(nodes, edges, "bir_khwarazm_afrighids", "birr_afr", "iranian", 19, "305-995 CE (Al-Biruni pp. 40-42)", "Afrighid Shah of Khwarazm", ["Al-Biruni Chronology (Sachau pp. 40-42)"], [
        "1. Afrigh (305 CE)", "2. Baghra", "3. Sakhassak", "4. Askajamuk I", "5. Azkajawar I", "6. Sakhr I",
        "7. Shawush", "8. Khamgri", "9. Buzkar", "10. Arthamukh (Time of Prophet Muhammad)", "11. Sakhr II", "12. Sabri",
        "13. Azkajawar II", "14. Askajamuk II", "15. Shawushfar", "16. Turkasbatha", "17. 'Abdallah", "18. Mansur",
        "19. 'Irak", "20. Muhammad", "21. 'Ahmad", "22. Abu 'Abdallah Muhammad (Last Afrighid, d. 995)"
    ], edge_type="direct", edge_label="Afrighid Khwarazmshah (Al-Biruni)")

    add_roster(nodes, edges, "bir_sasanians_complete", "birr_sas", "iranian", 19, "224-651 CE (Al-Biruni; Betham)", "Sasanian / Medieval Persian Ruler", ["Al-Biruni Chronology (Sachau pp. 45-48, 122-130)", "Betham Tab. CVI-CVII"], [
        "Sasan & Papak (Ancestors of Sasanians)", "Ardashir I (Founder, 224-242 CE)", "Shapur I (Captured Roman Emperor Valerian)",
        "Shapur II (70-yr Reign, 309-379)", "Yazdegerd I & Bahram V Gur (Ancestor of Buwayhids)", "Kavadh I (Ancestor of Bavandids)",
        "Khosrow I Anushirvan ('Immortal Soul')", "Khosrow II Parviz", "Queen Boran (First Female Sasanian Shah)",
        "Yazdegerd III (Last Sasanian Shah, d. 651)", "Buwaihi (Founder of Buwayhid Dynasty)", "Isma'il Samani (Founder of Samanids, via Bahram Chobin)"
    ], edge_type="direct", edge_label="Sasanian / Post-Sasanian Persian Lineage")

    add_roster(nodes, edges, "keb_premakeda_tamrin_azaryas", "kebr_21", "african", 16, "Kebra Nagast Ch. 43 (Budge p. 62)", "Kebra Nagast Noble / Ruler", ["Kebra Nagast (Budge 1922 p. 62)"], [
        "Arawi -> Angabo -> Gedur -> Sebado -> Kawnasya (Pre-Makeda Kings)", "Tamrin (Chief Merchant of Queen Makeda)",
        "'Azaryas son of Zadok (Stole Ark of Zion)", "'Elyas son of 'Arni (Archdeacon)", "'Adram son of 'Arderones",
        "Fankera, 'Akonhel, Samneyas & Fikaros", "Lewandos, Fakuten, Matan & Ad'araz", "Dalakem, 'Adaryos, 'Awsteran & 'Astar'ayon",
        "Imi, Makri, 'Abis, Lik Wendeyos, Karmi & Seranyas"
    ], edge_type="expansion", edge_label="Kebra Nagast Court & 21 Firstborn Nobles")

    edges += [
        E("bib_togarmah", "geo_targamos_8sons", "expansion", "Kartlis Tskhovreba: Targamos (Togarmah) -> 8 Caucasian Hero-Sons"),
        E("geo_targamos_8sons", "geo_kartlos_5sons_uplos", "direct", "Kartlos -> 5 Sons -> Mtskhetos -> Uplos, Odzrkhos & Javakhos"),
        E("geo_kartlos_5sons_uplos", "geo_parnavaz_nebrothids", "direct", "Uplos -> King Parnavaz I -> Pharnavazid, Nebrotid & Arshak'id Kings"),
        E("bib_nimrod", "geo_parnavaz_nebrothids", "syncretic", "Kartlis Tskhovreba: Nebrotid (Nimrodid) Kings Mirvan I & Parnajom of Kartli"),
        E("geo_parnavaz_nebrothids", "geo_chosroids_mirian_vakhtang", "direct", "Last Pharnavazid Aspagur's daughter Abeshuru marries Sasanian Prince Mirian III"),
        E("bir_sasanians_complete", "geo_chosroids_mirian_vakhtang", "direct", "Sasanian Prince Mikhran (Mirian III) founds Georgia's Chosroid Dynasty"),
        E("nt_mary_clopas_alphaeus", "geo_bagrationi_davidic", "syncretic", "Sumbat Davitisdze (p. 211) traces Bagrat'ionis via Joseph's brother K'leop'a -> 26 gens -> Guaram & Bagrat'"),
        E("jud_david", "geo_bagrationi_davidic", "syncretic", "Georgian Bagrat'ioni royal claim of direct Davidic descent"),
        E("ir_siyavash", "bir_parthians_ashkanians", "expansion", "Al-Biruni p. 116 traces Parthian founder Ashk ben Ashkan to Kayanian Siyawush!"),
        E("ir_bahman", "bir_sasanians_complete", "expansion", "Al-Biruni p. 122 traces Sasanian founder Ardashir I to Kay Bahman & Esfandiyar!"),
        E("ir_kay_khosrow", "bir_khwarazm_afrighids", "expansion", "Al-Biruni pp. 40-42 traces all 22 Afrighid Khwarazmshahs to Siyawush & Kay Khosrow!"),
        E("bib_joktan", "bir_himyar_lakhmid_ghassan", "expansion", "Qahtanite South Arabian Kingdoms (Himyarite Tubbas, Lakhmids & Ghassanids)"),
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
