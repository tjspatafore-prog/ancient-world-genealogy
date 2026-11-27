"""
Module 46: Wave 4 Person-by-Person Medes, Achaemenids, Late Kayanians, Parthian Arsacids,
Armenian Haikid Patriarchs, Complete 21-Generation Quraysh Stem, Caliphal Houses
(Rashidun / Umayyad / Abbasid / Alid), Qahtanite Himyarites / Lakhmids / Ghassanids,
Palmyra & Amazigh / Berber Patriarchs.

Sources mined from sources/:
- TheAegyptianAndGrecianHistoryOfHerodotus-Vol.1.pdf & Vol.2.pdf (Medes & Achaemenids)
- Tabari_Volume_01..06.pdf (Complete 21-Generation Quraysh Lineage, Caliphs, Sasanians & Himyarites)
- chronologyofanci00biru.pdf (Al-Biruni Parthian / Ashkanian & Sasanian Synchronisms)
- Kartlis Cxovreba 2012 Eng.pdf (Armenian Haos / Haykid & Georgian Synchronisms)
- Ibn Khaldun Histoire des Berberes v4.pdf (Amazigh Branes & Botr Genealogies)
"""

from . import N, E


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
    # 1. MEDES, ACHAEMENIDS, LATE KAYANIANS & PARTHIAN ARSACIDS
    # =========================================================================
    chain([
        "ir_deioces",
        ("per4_deioces", "King Deioces of Media (Daiukku, r. c. 700–647 BCE)", 16, "c. 700–647 BCE (Herodotus I.96–102)", "Founder of Median Kingdom at Ecbatana", "Son of Phraortes; first king of unified Media according to Herodotus.", False),
        ("per4_phraortes", "King Phraortes of Media (Fravartish, Son of Deioces, r. c. 647–625 BCE)", 16, "c. 647–625 BCE (Herodotus I.102)", "Son of Deioces", "Subjugated Persians and fell against Assyria.", False),
        ("per4_cyaxares", "King Cyaxares of Media (Uvakhshatra, Son of Phraortes, r. 625–585 BCE)", 17, "625–585 BCE (Herodotus I.103–106; Babylonian Chronicles)", "Conqueror of Nineveh (612 BCE)", "Allied with Nabopolassar of Babylon to overthrow Assyria; father of Astyages & Amytis.", False),
        ("per4_astyages", "King Astyages of Media (Ishtumegu, Son of Cyaxares, r. 585–550 BCE)", 17, "585–550 BCE (Herodotus I.107–130; Nabonidus Chronicle)", "Last King of Media & Maternal Grandfather of Cyrus", "Father of Princess Mandane; defeated by his grandson Cyrus the Great in 550 BCE.", False),
        "ir_mandane",
        "ir_cyrus",
    ], "iranian", ["Herodotus Book I", "Babylonian Chronicles"], "Median Royal Succession")
    edges.append(E("per4_cyaxares", "ir_cyaxares", "direct", "Cyaxares individual -> Median anchor"))

    # Achaemenid Senior & Junior Lines
    chain([
        "ir_achaemenes",
        ("per4_achaemenes", "Achaemenes (Hakhamanish, Eponymous Founder of Achaemenids)", 16, "c. 705–675 BCE (Behistun Inscription)", "Patriarch of Achaemenid Persia", "Ancestor of both royal branches proclaimed in Darius I's Behistun Inscription.", False),
        ("per4_teispes", "King Teispes of Anshan (Chishpish, Son of Achaemenes)", 16, "c. 675–640 BCE (Cyrus Cylinder)", "King of Anshan", "Father of Cyrus I (Senior line) and Ariaramnes (Junior line).", False),
        ("per4_cyrus1", "King Cyrus I of Anshan (Kurash I, Son of Teispes)", 17, "c. 640–600 BCE (Cyrus Cylinder)", "Early King of Anshan", "Paid tribute to Ashurbanipal; father of Cambyses I.", False),
        ("per4_cambyses1", "King Cambyses I of Anshan (Kambujiya I, Father of Cyrus the Great)", 17, "c. 600–559 BCE (Herodotus I.107; Cyrus Cylinder)", "Father of Cyrus the Great", "Married Median Princess Mandane (daughter of Astyages).", False),
        "ir_cyrus",
        ("per4_cambyses2", "Shahanshah Cambyses II (Son of Cyrus the Great, r. 530–522 BCE; Conquered Egypt)", 17, "530–522 BCE (Herodotus III; Udjahorresnet)", "Conqueror of Saite Egypt (27th Dynasty)", "Eldest son of Cyrus the Great; defeated Psamtik III at Pelusium (525 BCE).", False),
    ], "iranian", ["Behistun Inscription", "Cyrus Cylinder", "Herodotus Books I–IX"], "Achaemenid Senior Succession")

    nodes += [
        N("per4_bardiya", "Prince Bardiya / Smerdis (Younger Son of Cyrus the Great, d. 522 BCE)", "iranian", 17, "d. 522 BCE (Behistun; Herodotus III)", "Younger Son of Cyrus the Great", ["Behistun Inscription", "Herodotus Book III"], "Brother of Cambyses II."),
        N("per4_atossa", "Queen Atossa (Daughter of Cyrus the Great; Wife of Darius I; Mother of Xerxes I)", "iranian", 17, "c. 550–475 BCE (Herodotus III.88, VII.2–3)", "Achaemenid Empress Uniting Senior & Junior Lines", ["Herodotus Books III & VII"], "Daughter of Cyrus the Great; married Darius I and bore Xerxes I, uniting both Achaemenid branches.", major=True),
    ]
    edges += [
        E("per4_cambyses1", "ir_cambyses1", "direct", "Cambyses I individual -> Anshan anchor"),
        E("ir_cyrus", "per4_bardiya", "direct", "Cyrus the Great -> son Bardiya"),
        E("ir_cyrus", "per4_atossa", "direct", "Cyrus the Great -> daughter Queen Atossa"),
        E("ir_cambyses2_atossa", "per4_cambyses2", "direct", "Cambyses II / Atossa anchor -> Cambyses II"),
        E("per4_atossa", "ir_xerxes1", "direct", "Mother Queen Atossa -> Shahanshah Xerxes I"),
    ]

    # Achaemenid Junior Line -> Late Imperial Line -> Alexander the Great
    chain([
        "per4_teispes",
        ("per4_ariaramnes", "Ariaramnes (Ariyaramna, Son of Teispes)", 16, "c. 640 BCE (Behistun DB I.4)", "Junior Achaemenid Patriarch", "Younger son of Teispes.", False),
        ("per4_arsames", "Arsames (Arshama, Son of Ariaramnes)", 17, "c. 600–550 BCE (Behistun DB I.4)", "Father of Hystaspes", "Grandfather of Darius I the Great.", False),
        ("per4_hystaspes", "Hystaspes / Vishtaspa (Satrap of Parthia; Father of Darius I)", 17, "c. 570–520 BCE (Behistun; Herodotus I.209)", "Father of Darius I the Great", "Son of Arsames; father of Darius I.", False),
        "ir_darius1",
        "ir_xerxes1",
        ("per4_artaxerxes1", "Shahanshah Artaxerxes I Longimanus (Son of Xerxes I, r. 465–424 BCE; Ezra 7 & Nehemiah 2)", 17, "465–424 BCE (Ezra 7; Nehemiah 2; Thucydides)", "Persian Patron of Ezra & Nehemiah", "Commissioned Ezra (458 BCE) and Nehemiah (445 BCE) to restore Jerusalem.", True),
        ("per4_darius2", "Shahanshah Darius II Ochus (Son of Artaxerxes I, r. 423–404 BCE)", 17, "423–404 BCE (Xenophon Hellenica; Elephantine)", "Son of Artaxerxes I", "Married half-sister Parysatis; father of Artaxerxes II & Cyrus the Younger.", False),
        ("per4_artaxerxes2", "Shahanshah Artaxerxes II Mnemon (Son of Darius II, r. 404–358 BCE)", 17, "404–358 BCE (Plutarch Artaxerxes; Xenophon)", "Victor of Cunaxa", "Reigned 46 years; father of Artaxerxes III.", False),
        ("per4_artaxerxes3", "Shahanshah Artaxerxes III Ochus (Son of Artaxerxes II, r. 358–338 BCE)", 18, "358–338 BCE (Diodorus XVI; Manetho)", "Reconqueror of Egypt (343 BCE)", "Ended the 30th native dynasty of Egypt.", False),
        ("per4_arses", "Shahanshah Arses / Artaxerxes IV (Son of Artaxerxes III, r. 338–336 BCE)", 18, "338–336 BCE (Diodorus XVII.5)", "Short-Reigning Achaemenid Heir", "Son of Artaxerxes III.", False),
        ("per4_darius3", "Shahanshah Darius III Codomannus (Great-Grandson of Darius II, r. 336–330 BCE)", 18, "380–330 BCE (Arrian Anabasis; Diodorus XVII)", "Last Achaemenid Shahanshah", "Grandson of Ostanes (brother of Artaxerxes II); defeated by Alexander the Great at Gaugamela (331 BCE); father of Stateira II.", True),
        ("per4_stateira2", "Princess Stateira II (Daughter of Darius III; Married Alexander the Great at Susa, 324 BCE)", 18, "d. 323 BCE (Arrian Anabasis VII.4; Plutarch Alexander 70)", "Achaemenid Princess Married to Alexander the Great", "United the Achaemenid Persian and Argead Macedonian royal houses at the Susa Weddings (324 BCE).", False),
        "grk_alexander",
    ], "iranian", ["Behistun Inscription", "Ezra / Nehemiah", "Arrian Anabasis"], "Achaemenid Junior & Late Imperial Line")
    nodes.append(N("per4_cyrus_younger", "Prince Cyrus the Younger (Son of Darius II; Battle of Cunaxa 401 BCE)", "iranian", 17, "d. 401 BCE (Xenophon Anabasis)", "Patron of Xenophon's Ten Thousand", ["Xenophon Anabasis I"], "Younger son of Darius II & Parysatis who fell at Cunaxa."))
    edges += [
        E("per4_hystaspes", "ir_hystaspes", "direct", "Hystaspes individual -> Junior Achaemenid anchor"),
        E("ir_darius1", "per4_atossa", "direct", "Marriage of Darius I & Atossa"),
        E("per4_artaxerxes1", "ir_artaxerxes1", "direct", "Artaxerxes I individual -> Late Achaemenid anchor"),
        E("per4_darius2", "per4_cyrus_younger", "direct", "Darius II -> son Cyrus the Younger"),
    ]

    # Late Kayanians (Shahnameh)
    chain([
        "ir_bahman",
        ("per4_homai", "Queen Homai Chehrzad (Daughter & Successor of Kay Bahman)", 17, "Kayanian Era (Shahnameh; Al-Biruni p. 111)", "Mythic Kayanian Queen", "Mother of Darab.", False),
        ("per4_darab", "King Darab (Son of Kay Bahman & Homai; Father of Dara II & Iskandar in Shahnameh)", 18, "Kayanian Era (Shahnameh)", "Shahnameh King Linking Iran & Alexander", "In Ferdowsi's Shahnameh, fathered both Dara II and (via Nahid daughter of Failaqus/Philip) Iskandar.", False),
        ("per4_dara2", "King Dara II ibn Darab (Last Kayanian Shah)", 18, "c. 336–330 BCE (Shahnameh / Tabari)", "Persian Epic Counterpart of Darius III", "Fought half-brother Iskandar (Alexander) in Shahnameh epic chronology.", False),
    ], "iranian", ["Ferdowsi Shahnameh", "Al-Biruni Chronology"], "Late Kayanian Succession")

    # Parthian Arsacids (Al-Biruni pp. 116-120)
    chain([
        "bir_parthians_ashkanians",
        ("per4_arsaces1", "King Arsaces I / Ashk ben Ashkan (Founder of Parthia, 247–217 BCE)", 18, "247–217 BCE (Al-Biruni p. 116; Strabo XI)", "Founder of Parthian Empire (Al-Biruni -> Siyavush)", "Progenitor of the Ashkanian/Arsacid Dynasty traced by Al-Biruni to Kayanian Siyavush.", True),
        ("per4_tiridates1", "King Tiridates I / Arsaces II (Brother of Arsaces I, c. 217–211 BCE)", 18, "c. 217–211 BCE (Justin XLI.5)", "Early Arsacid Consolidator", "Brother of Arsaces I.", False),
        ("per4_mithridates1", "King Mithridates I the Great of Parthia (171–132 BCE)", 18, "171–132 BCE (Justin XLI; Al-Biruni)", "Creator of the Parthian Empire", "Conquered Media and Mesopotamia from the Seleucids.", False),
        ("per4_phraates2", "King Phraates II of Parthia (Son of Mithridates I, 132–127 BCE)", 18, "132–127 BCE (Justin XLII)", "Son of Mithridates I", "Defeated Antiochus VII Sidetes.", False),
        ("per4_mithridates2", "King Mithridates II the Great of Parthia (124–91 BCE; 'King of Kings')", 18, "124–91 BCE (Justin XLII.2)", "Parthian Hegemon From Euphrates to Bactria", "Established the Silk Road embassy with Han China & allied with Sulla.", False),
        ("per4_orodes2", "King Orodes II of Parthia (57–37 BCE; Victor of Carrhae 53 BCE)", 18, "57–37 BCE (Plutarch Crassus; Dio XL)", "Parthian Monarch at Carrhae", "Father of Pacorus I & Phraates IV.", False),
        ("per4_phraates4", "King Phraates IV of Parthia (37–2 BCE; Returned Crassus's Eagles to Augustus)", 18, "37–2 BCE (Tacitus Annals II.1)", "Son of Orodes II", "Made 20 BCE treaty with Emperor Augustus.", False),
        ("per4_vologases1", "King Vologases I of Parthia (51–78 CE; Patron of Avesta Compilation)", 19, "51–78 CE (Tacitus; Denkard IV)", "Placed Brother Tiridates on Armenian Throne", "Preserved Zoroastrian Avestan texts and founded Vologesocerta.", False),
        ("per4_artabanus4", "King Artabanus IV / Ardawan (Last Parthian Shahanshah, d. 224 CE at Hormozdgan)", 19, "213–224 CE (Al-Biruni p. 118; Cassius Dio)", "Last Arsacid Monarch of Persia", "Fell in battle against Ardashir I, ending the 470-year Arsacid Empire.", False),
        "birr_sas_02_ardashir_i_founder_224_242_c",
    ], "iranian", ["Al-Biruni Chronology pp. 116-120", "Justin XLI-XLII"], "Parthian Arsacid Succession")

    # =========================================================================
    # 2. ARMENIAN HAIKID PATRIARCHS (Movses Khorenatsi / Kartlis Tskhovreba)
    # =========================================================================
    chain([
        "arm_hayk_pat",
        ("arm4_aramaneak", "Aramaneak (Eldest Son of Hayk Nahapet)", 7, "c. 21st c. BCE (Movses Khorenatsi I.12)", "Armenian Patriarch", "Settled in Ayrarat plain.", False),
        ("arm4_aramayis", "Aramayis (Son of Aramaneak; Builder of Armavir)", 8, "c. 20th c. BCE (Khorenatsi I.12)", "Builder of Armavir", "Built capital Armavir on the Araxes.", False),
        ("arm4_amasia", "Amasia (Son of Aramayis; Named Mt. Masis)", 8, "Khorenatsi I.12", "Armenian Patriarch", "Father of Gegham.", False),
        ("arm4_gegham", "Gegham (Son of Amasia; Eponym of Lake Sevan / Gegharkunik)", 9, "Khorenatsi I.12", "Armenian Patriarch", "Father of Harma & Sisak (Syunik).", False),
        ("arm4_harma", "Harma (Son of Gegham)", 9, "Khorenatsi I.12", "Armenian Patriarch", "Father of Aram.", False),
        ("arm4_aram", "Patriarch Aram (Son of Harma; Classical Eponym of Armenia)", 10, "Khorenatsi I.12–14", "Great Armenian Warrior Patriarch", "Extended borders into Cappadocia and Assyria; father of Ara.", False),
        ("arm4_ara_beautiful", "Ara the Handsome (Son of Aram; Coveted by Queen Semiramis)", 10, "Khorenatsi I.15", "Heroic Patriarch-King of Armenia", "Fell defending Armenia against Semiramis (Shammuramat).", False),
    ], "iranian", ["Movses Khorenatsi History of Armenia I.12-15", "Kartlis Tskhovreba"], "Armenian Haikid Patriarchal Line")
    edges += [
        E("arm4_ara_beautiful", "arm_haykid_line", "direct", "Ara the Handsome -> Haykid royal anchor"),
        E("arm_haykid_line", "cls3_artaxias1", "expansion", "Orontid / Artaxiad succession -> Artaxias I of Armenia"),
    ]

    # =========================================================================
    # 3. COMPLETE 21-GEN QURAYSH STEM & CALIPHAL HOUSES (Tabari Vol. 6)
    # =========================================================================
    chain([
        "tab_adnan_21gen_quraysh",
        ("ar4_maadd", "Ma'add ibn Adnan (Son of Adnan)", 15, "Pre-Islamic Arabia (Tabari Vol. 6 p. 36)", "2nd Gen Northern Arab Ancestor", "Son of Adnan.", False),
        ("ar4_nizar", "Nizar ibn Ma'add (Father of Mudar & Rabi'ah)", 16, "Tabari Vol. 6 p. 36", "3rd Gen Ancestor", "Progenitor of the Nizarite Arab confederations.", False),
        ("ar4_mudar", "Mudar ibn Nizar (Brother of Rabi'ah)", 16, "Tabari Vol. 6 p. 35", "4th Gen Ancestor of Mudarites", "Eponym of the Mudar tribes.", False),
        ("ar4_ilyas", "Ilyas ibn Mudar", 16, "Tabari Vol. 6 p. 34", "5th Gen Ancestor", "Married Khindif.", False),
        ("ar4_mudrikah", "Mudrikah ('Amr) ibn Ilyas", 16, "Tabari Vol. 6 p. 33", "6th Gen Ancestor", "Son of Ilyas.", False),
        ("ar4_khuzaymah", "Khuzaymah ibn Mudrikah", 17, "Tabari Vol. 6 p. 32", "7th Gen Ancestor", "Father of Kinanah & Asad.", False),
        ("ar4_kinanah", "Kinanah ibn Khuzaymah", 17, "Tabari Vol. 6 p. 31", "8th Gen Ancestor of Banu Kinanah", "Ancestor of Quraysh and allied Hijazi clans.", False),
        ("ar4_al_nadr", "Al-Nadr ibn Kinanah", 17, "Tabari Vol. 6 p. 29", "9th Gen Ancestor", "Considered founder of Quraysh in some traditions.", False),
        ("ar4_malik", "Malik ibn al-Nadr", 17, "Tabari Vol. 6 p. 28", "10th Gen Ancestor", "Father of Fihr.", False),
        ("ar4_fihr_quraysh", "Fihr ibn Malik (Quraysh — Eponym of Tribe of Quraysh)", 17, "c. 200 CE (Tabari Vol. 6 p. 28)", "11th Gen Eponym of Quraysh", "United the Hijazi clans around Mecca as Quraysh.", True),
        ("ar4_ghalib", "Ghalib ibn Fihr", 17, "Tabari Vol. 6 p. 27", "12th Gen Ancestor", "Son of Fihr.", False),
        ("ar4_luayy", "Lu'ayy ibn Ghalib", 18, "Tabari Vol. 6 p. 27", "13th Gen Ancestor", "Father of Ka'b.", False),
        ("ar4_kab", "Ka'b ibn Lu'ayy", 18, "Tabari Vol. 6 p. 26", "14th Gen Ancestor", "Preached at Mecca; father of Murrah & Adi (Umar's line).", False),
        ("ar4_murrah", "Murrah ibn Ka'b", 18, "Tabari Vol. 6 p. 26", "15th Gen Ancestor", "Father of Kilab & Taym (Abu Bakr's clan).", False),
        ("ar4_kilab", "Kilab ibn Murrah", 18, "c. 4th c. CE (Tabari Vol. 6 p. 25)", "16th Gen Ancestor", "Married Fatimah bint Sa'd; father of Qusayy.", False),
        ("ar4_qusayy", "Qusayy ibn Kilab (Zayd — Unifier & Custodian of Mecca, c. 400–480 CE)", 18, "c. 400–480 CE (Tabari Vol. 6 pp. 18–25)", "17th Gen Unifier of Mecca", "Reclaimed custody of the Ka'bah and established Dar al-Nadwah in Mecca.", True),
        ("ar4_abd_manaf", "'Abd Manaf ibn Qusayy (Al-Mughirah — Father of Hashim & 'Abd Shams)", 18, "c. 430–500 CE (Tabari Vol. 6 p. 16)", "18th Gen Common Ancestor of Prophet, Umayyads & Abbasids", "Fathered twin lines: Hashim (Prophet, Alids, Abbasids) and 'Abd Shams (Umayyads).", False),
    ], "arabian", ["Al-Tabari Vol. 6 (Muhammad at Mecca)", "Ibn Hisham"], "21-Generation Quraysh Lineage (Tabari Vol. 6)")
    edges.append(E("ar_adnan_quraysh", "ar4_maadd", "direct", "Adnan -> son Ma'add"))

    # Banu Hashim, Prophetic Family, Alids & Abbasids
    chain([
        "ar4_abd_manaf",
        ("ar4_hashim", "Hashim ibn 'Abd Manaf ('Amr al-'Ula — Eponym of Banu Hashim, d. c. 497 CE)", 19, "c. 464–497 CE (Tabari Vol. 6 pp. 9–15)", "19th Gen Ancestor & Eponym of Hashemites", "Led the winter & summer trade caravans of Quraysh; married Salma bint 'Amr of Medina.", False),
        ("ar4_abd_al_muttalib", "'Abd al-Muttalib ibn Hashim (Shaybah al-Hamd, c. 497–578 CE — Rediscovered Zamzam)", 19, "c. 497–578 CE (Tabari Vol. 6 pp. 1–9)", "20th Gen Chief of Quraysh", "Custodian of Mecca during the Year of the Elephant (570 CE); father of 'Abdallah, Abu Talib, Hamza & al-'Abbas.", True),
        ("ar4_abdallah", "'Abdallah ibn 'Abd al-Muttalib (545–570 CE; Father of Prophet Muhammad)", 19, "545–570 CE (Tabari Vol. 6 p. 1)", "21st Gen Father of Prophet Muhammad", "Wed Aminah bint Wahb and passed away before Muhammad's birth.", False),
        ("ar4_prophet_muhammad", "Prophet Muhammad ibn 'Abdallah (570–632 CE; Seal of the Prophets in Islam)", 19, "570–632 CE (Tabari Vols. 6–9)", "Prophet of Islam & Unifier of Arabia", "Son of 'Abdallah & Aminah bint Wahb; married Khadijah bint Khuwaylid; father of Fatimah al-Zahra.", True),
        ("ar4_fatimah", "Fatimah al-Zahra bint Muhammad (c. 605–632 CE; Wife of Caliph Ali)", 20, "c. 605–632 CE (Tabari)", "Daughter of Prophet Muhammad & Khadijah", "Married cousin Ali ibn Abi Talib; mother of Imams Hasan and Husayn.", True),
        ("ar4_imam_hasan", "Imam al-Hasan ibn Ali (625–670 CE; Eldest Grandson of Prophet Muhammad)", 20, "625–670 CE (Tabari)", "5th Caliph & Ancestor of Hashemites & Alaouites", "Father of Hasan al-Muthanna -> living Hashemites of Jordan & Alaouites of Morocco.", True),
        "mod_hasan_muthanna",
    ], "arabian", ["Al-Tabari Vol. 6", "Hashemite Royal Registers"], "Banu Hashim Patrilineal & Prophetic Stem")

    nodes += [
        N("ar4_aminah_bint_wahb", "Aminah bint Wahb ibn 'Abd Manaf ibn Zuhrah (d. 577 CE; Mother of Prophet Muhammad)", "arabian", 19, "d. 577 CE (Tabari Vol. 6)", "Mother of Prophet Muhammad", ["Al-Tabari Vol. 6"], "Noblewoman of Banu Zuhrah (descended from Kilab ibn Murrah); mother of Prophet Muhammad."),
        N("ar4_khadijah", "Khadijah bint Khuwaylid (c. 555–619 CE; First Wife of Prophet Muhammad)", "arabian", 19, "c. 555–619 CE (Tabari Vol. 6)", "Mother of Fatimah & First Believer", ["Al-Tabari Vol. 6"], "Merchant of Quraysh (descended from Qusayy's brother 'Abd al-'Uzza); bore Fatimah al-Zahra."),
        N("ar4_abu_talib", "Abu Talib ibn 'Abd al-Muttalib ('Abd Manaf, c. 535–619 CE; Uncle & Protector of Muhammad)", "arabian", 19, "c. 535–619 CE (Tabari Vol. 6)", "Chief of Banu Hashim & Father of Ali", ["Al-Tabari Vol. 6"], "Father of Ja'far al-Tayyar and Caliph Ali ibn Abi Talib."),
        N("ar4_imam_husayn", "Imam al-Husayn ibn Ali (626–680 CE; Martyr of Karbala)", "arabian", 20, "626–680 CE (Tabari Vol. 19)", "Grandson of Prophet Muhammad", ["Al-Tabari Vol. 19"], "Son of Ali & Fatimah; ancestor of Husaynid Sayyids and Nizari Ismaili Imams.", major=True),
        N("ar4_ali_zayn_abidin", "Imam Ali Zayn al-Abidin (659–713 CE; Son of Imam Husayn)", "arabian", 20, "659–713 CE (Nizari Archives)", "4th Husaynid Imam", ["Al-Tabari", "Nizari Archives"], "Survived Karbala; father of Muhammad al-Baqir."),
        N("ar4_muhammad_baqir", "Imam Muhammad al-Baqir (677–733 CE; Son of Zayn al-Abidin)", "arabian", 20, "677–733 CE", "5th Husaynid Imam", ["Al-Tabari"], "Father of Ja'far al-Sadiq."),
        N("ar4_jafar_sadiq", "Imam Ja'far al-Sadiq (702–765 CE; Jurist & 6th Husaynid Imam)", "arabian", 20, "702–765 CE", "Ancestor of Fatimids & Aga Khan V", ["Al-Tabari", "Nizari Archives"], "Teacher of Sunni & Shia jurists; father of Isma'il -> Fatimids -> Aga Khan V.", major=True),
        N("ar4_al_abbas", "Al-'Abbas ibn 'Abd al-Muttalib (c. 566–653 CE; Eponym of the Abbasid Caliphate)", "arabian", 19, "c. 566–653 CE (Tabari)", "Paternal Uncle of Muhammad & Progenitor of Abbasids", ["Al-Tabari"], "Father of scholar 'Abdallah ibn al-'Abbas."),
        N("ar4_abdallah_ibn_abbas", "'Abdallah ibn al-'Abbas (619–687 CE; Foremost Qur'anic Exegete & Grandfather of Caliphs)", "arabian", 20, "619–687 CE (Tabari)", "Companion & Father of Ali ibn 'Abdallah", ["Al-Tabari"], "Grandfather of Abbasid caliphs al-Saffah and al-Mansur via Ali ibn 'Abdallah -> Muhammad."),
        N("ar4_al_saffah", "Caliph Abu al-'Abbas al-Saffah (1st Abbasid Caliph, r. 750–754 CE)", "arabian", 20, "721–754 CE (Tabari Vol. 27)", "Founder of the Abbasid Caliphate", ["Al-Tabari Vol. 27"], "Brother of Caliph al-Mansur."),
        N("ar4_al_mahdi", "Caliph al-Mahdi (Son of al-Mansur; Father of Harun al-Rashid, r. 775–785 CE)", "arabian", 20, "744–785 CE (Tabari Vol. 29)", "3rd Abbasid Caliph", ["Al-Tabari Vol. 29"], "Father of Caliphs al-Hadi and Harun al-Rashid."),
    ]
    edges += [
        E("ar4_kilab", "ar4_aminah_bint_wahb", "direct", "Kilab -> Zuhrah -> Wahb -> Aminah bint Wahb"),
        E("ar4_aminah_bint_wahb", "ar4_prophet_muhammad", "direct", "Mother Aminah -> Prophet Muhammad"),
        E("ar4_prophet_muhammad", "ar_hashim_muhammad_caliphs", "direct", "Prophet Muhammad -> Hashimite Caliphal anchor"),
        E("ar4_qusayy", "ar4_khadijah", "direct", "Qusayy's brother 'Abd al-'Uzza -> Asad -> Khuwaylid -> Khadijah"),
        E("ar4_khadijah", "ar4_fatimah", "direct", "Mother Khadijah -> Fatimah al-Zahra"),
        E("ar4_abd_al_muttalib", "ar4_abu_talib", "direct", "'Abd al-Muttalib -> son Abu Talib"),
        E("ar4_abu_talib", "mon_isl_ali", "direct", "Abu Talib -> Caliph Ali ibn Abi Talib"),
        E("mon_isl_ali", "ar4_imam_hasan", "direct", "Father Ali -> Imam al-Hasan"),
        E("ar4_fatimah", "ar4_imam_husayn", "direct", "Fatimah & Ali -> Imam al-Husayn"),
        E("mon_isl_ali", "ar4_imam_husayn", "direct", "Father Ali -> Imam al-Husayn"),
        E("ar4_imam_husayn", "ar4_ali_zayn_abidin", "direct", "Imam Husayn -> Ali Zayn al-Abidin"),
        E("ar4_ali_zayn_abidin", "ar4_muhammad_baqir", "direct", "Zayn al-Abidin -> Muhammad al-Baqir"),
        E("ar4_muhammad_baqir", "ar4_jafar_sadiq", "direct", "Muhammad al-Baqir -> Ja'far al-Sadiq"),
        E("ar4_jafar_sadiq", "mod_agakhan5_ismaili", "direct", "Ja'far al-Sadiq -> Isma'il -> Fatimids -> Living Aga Khan V"),
        E("ar4_abd_al_muttalib", "ar4_al_abbas", "direct", "'Abd al-Muttalib -> son al-'Abbas"),
        E("ar4_al_abbas", "ar4_abdallah_ibn_abbas", "direct", "Al-'Abbas -> 'Abdallah ibn al-'Abbas"),
        E("ar4_abdallah_ibn_abbas", "ar4_al_saffah", "direct", "'Abdallah -> Ali -> Muhammad -> 1st Abbasid Caliph al-Saffah"),
        E("ar4_abdallah_ibn_abbas", "mon_isl_al_mansur", "direct", "'Abdallah -> Ali -> Muhammad -> Caliph al-Mansur"),
        E("mon_isl_al_mansur", "ar4_al_mahdi", "direct", "Caliph al-Mansur -> son Caliph al-Mahdi"),
        E("ar4_al_mahdi", "mon_isl_harun_rashid", "direct", "Caliph al-Mahdi -> son Harun al-Rashid"),
        E("mon_isl_harun_rashid", "mon_isl_al_mamun", "direct", "Harun al-Rashid -> son al-Ma'mun"),
        E("ar4_murrah", "mon_isl_abubakr", "direct", "Murrah -> Taym -> Quraysh Abu Quhafa -> Caliph Abu Bakr"),
        E("ar4_kab", "mon_isl_umar", "direct", "Ka'b -> 'Adi -> al-Khattab -> Caliph Umar ibn al-Khattab"),
    ]

    # Banu Umayyah (Damascus & Cordoba)
    chain([
        "ar4_abd_manaf",
        ("ar4_abd_shams", "'Abd Shams ibn 'Abd Manaf (Progenitor of the Umayyad Caliphs)", 19, "c. 464–520 CE (Tabari Vol. 6 p. 16)", "Son of 'Abd Manaf & Twin Brother of Hashim", "Father of Umayyah.", False),
        ("ar4_umayyah", "Umayyah ibn 'Abd Shams (Eponym of Banu Umayyah)", 19, "6th c. CE (Tabari)", "Eponym of the Umayyad Dynasty", "Father of Harb (Sufyanids) and Abu al-'As (Caliph Uthman & Marwanids).", False),
        ("ar4_harb", "Harb ibn Umayyah (Commander of Quraysh at Fijar)", 19, "6th c. CE (Tabari)", "Son of Umayyah", "Father of Abu Sufyan.", False),
        ("ar4_abu_sufyan", "Abu Sufyan Sakhr ibn Harb (c. 565–653 CE; Father of Mu'awiya I)", 19, "c. 565–653 CE (Tabari)", "Meccan Leader & Umayyad Patriarch", "Father of Caliph Mu'awiya I.", False),
        "mon_isl_muawiya1",
        ("ar4_yazid1", "Caliph Yazid I ibn Mu'awiya (r. 680–683 CE)", 20, "647–683 CE (Tabari Vol. 19)", "2nd Umayyad Caliph", "Son of Mu'awiya I.", False),
    ], "arabian", ["Al-Tabari Vols. 6, 15, 19", "Lane-Poole"], "Umayyad Sufyanid Lineage")

    nodes += [
        N("ar4_abu_al_as", "Abu al-'As ibn Umayyah (Son of Umayyah; Ancestor of Uthman & Marwanids)", "arabian", 19, "6th c. CE (Tabari)", "Father of 'Affan & al-Hakam", ["Al-Tabari"], "Brother of Harb; ancestor of Caliph Uthman and the Marwanid Umayyad Caliphs of Damascus and Cordoba."),
        N("ar4_affan", "'Affan ibn Abi al-'As (Father of Caliph Uthman)", "arabian", 19, "6th c. CE (Tabari)", "Grandson of Umayyah", ["Al-Tabari"], "Father of 3rd Rashidun Caliph Uthman ibn 'Affan."),
        N("ar4_al_hakam", "Al-Hakam ibn Abi al-'As (Brother of 'Affan; Father of Marwan I)", "arabian", 19, "d. 652 CE (Tabari)", "Father of Caliph Marwan I", ["Al-Tabari"], "Uncle of Caliph Uthman."),
        N("ar4_marwan1", "Caliph Marwan I ibn al-Hakam (623–685 CE; Founder of Marwanid Umayyads)", "arabian", 20, "623–685 CE (Tabari Vol. 20)", "4th Umayyad Caliph", ["Al-Tabari Vol. 20"], "Father of Caliph 'Abd al-Malik."),
        N("ar4_al_walid1", "Caliph al-Walid I (r. 705–715 CE; Builder of Damascus Mosque & Expansion to Spain/Sindh)", "arabian", 20, "668–715 CE (Tabari Vol. 23)", "6th Umayyad Caliph", ["Al-Tabari Vol. 23"], "Eldest son of 'Abd al-Malik; under his reign Muslim armies reached Iberia & the Indus."),
        N("ar4_hisham", "Caliph Hisham ibn 'Abd al-Malik (r. 724–743 CE; Grandfather of 'Abd al-Rahman I)", "arabian", 20, "691–743 CE (Tabari Vol. 25)", "10th Umayyad Caliph", ["Al-Tabari Vol. 25"], "Son of 'Abd al-Malik; grandfather of Emir 'Abd al-Rahman I of Cordoba via Mu'awiya ibn Hisham."),
    ]
    edges += [
        E("ar4_umayyah", "ar4_abu_al_as", "direct", "Umayyah -> son Abu al-'As"),
        E("ar4_abu_al_as", "ar4_affan", "direct", "Abu al-'As -> 'Affan"),
        E("ar4_affan", "mon_isl_uthman", "direct", "'Affan -> Caliph Uthman ibn 'Affan"),
        E("ar4_abu_al_as", "ar4_al_hakam", "direct", "Abu al-'As -> al-Hakam"),
        E("ar4_al_hakam", "ar4_marwan1", "direct", "Al-Hakam -> Caliph Marwan I"),
        E("ar4_marwan1", "mon_isl_abd_al_malik", "direct", "Marwan I -> Caliph 'Abd al-Malik"),
        E("mon_isl_abd_al_malik", "ar4_al_walid1", "direct", "'Abd al-Malik -> son Caliph al-Walid I"),
        E("mon_isl_abd_al_malik", "ar4_hisham", "direct", "'Abd al-Malik -> son Caliph Hisham"),
        E("ar4_hisham", "mon_isl_abdarrahman1", "direct", "Caliph Hisham -> Mu'awiya -> Emir 'Abd al-Rahman I of Cordoba"),
        E("ar_hashim_muhammad_caliphs", "isl_umayyad_abbasid_fatimid", "direct", "Umayyad, Abbasid & Fatimid Caliphal anchor"),
    ]

    # =========================================================================
    # 4. QAHTANITE SOUTH ARABIA (HIMYAR, LAKHMIDS, GHASSANIDS) & PALMYRA
    # =========================================================================
    chain([
        "bib_joktan",
        ("ar4_yarub", "King Ya'rub ibn Qahtan (1st Arabic-Speaking King of Yemen)", 9, "Proto-Arabian Era (Tabari; Caussin de Perceval Vol. 1)", "Son of Qahtan / Joktan", "Ancestor of Yemeni & South Arabian Arabized tribes.", False),
        ("ar4_yashjub", "Yashjub ibn Ya'rub", 10, "South Arabian Tradition", "Father of 'Abd Shams / Saba", "Son of Ya'rub.", False),
        ("ar4_saba", "Saba ibn Yashjub ('Abd Shams — Builder of Marib Dam)", 11, "South Arabian Tradition (Tabari)", "Eponym of Sabaeans; Father of Himyar & Kahlan", "Fathered twin branches Himyar (Tubba kings) and Kahlan (Lakhmids, Ghassanids & Azd).", False),
        ("ar4_himyar", "Himyar ibn Saba (Eponym of Himyarite Kingdom of Yemen)", 12, "South Arabian Tradition (Al-Biruni)", "Founder of Himyarite Lineage", "Eponym of the Himyarite Tubba monarchs.", False),
        ("ar4_tubba_abu_karib", "Tubba As'ad Abu Karib of Himyar (c. 390–440 CE; Embraced Judaism in Yathrib)", 19, "c. 390–440 CE (Tabari Vol. 5; Himyarite Inscriptions)", "Greatest Himyarite Unifier & Tubba King", "Adopted Judaism in Yathrib and clothed the Ka'bah.", False),
        ("ar4_dhu_nuwas", "King Yusuf As'ar Dhu-Nuwas of Himyar (r. 517–525 CE; Clashed with King Kaleb of Aksum)", 19, "517–525 CE (Tabari Vol. 5; Kebra Nagast Ch. 117)", "Last Independent Jewish Tubba of Himyar", "Defeated at the Red Sea by Aksumite King Kaleb (Elesbaan) in 525 CE.", False),
        ("ar4_sayf_ibn_dhi_yazan", "Sayf ibn Dhi Yazan (Restorer of Himyar against Aksum, c. 575 CE)", 19, "c. 575 CE (Tabari Vol. 5)", "Late Himyarite Hero-King", "Reclaimed Yemen from Aksumite rule.", False),
    ], "arabian", ["Al-Tabari Vol. 5", "Al-Biruni Chronology", "Caussin de Perceval"], "Qahtanite / Himyarite Succession")

    nodes += [
        N("ar4_kahlan", "Kahlan ibn Saba (Brother of Himyar; Ancestor of Lakhmids, Ghassanids & Ansar of Medina)", "arabian", 12, "South Arabian Tradition", "Progenitor of Azd, Lakhm & Ghassan", ["Al-Tabari Vol. 5", "Caussin de Perceval"], "Son of Saba; ancestral trunk of the Lakhmid kings of Al-Hirah and Ghassanid kings of Syria."),
        N("ar4_jafnah_ghassan", "Jafnah ibn 'Amr (1st Ghassanid King of Syria, c. 220 CE)", "arabian", 18, "c. 220 CE (Al-Biruni p. 49)", "Founder of Christian Ghassanid Dynasty", ["Al-Biruni", "Caussin de Perceval"], "Founded the Arab Christian Jafnid/Ghassanid kingdom allied with Rome/Byzantium."),
        N("ar4_al_harith_ghassan", "King al-Harith V ibn Jabalah of Ghassan (Arethas, r. 529–569 CE; Ally of Justinian I)", "arabian", 19, "529–569 CE (Procopius; Al-Biruni)", "Patricius & Paramount Phylarch of the Arabs", ["Procopius Wars", "Al-Biruni"], "Elevated by Byzantine Emperor Justinian I to king over Syria's Arab foederati."),
        N("ar4_imru_al_qays_lakhmid", "King Imru' al-Qays I ibn 'Amr of Al-Hirah (d. 328 CE; Namara Inscription)", "arabian", 19, "d. 328 CE (Namara Arabic Inscription)", "Early Lakhmid 'King of All Arabs'", ["Namara Inscription (328 CE)", "Tabari Vol. 5"], "Attested in the 328 CE Namara inscription — oldest dated classical Arabic royal epitaph."),
        N("ar4_al_mundhir3", "King al-Mundhir III ibn al-Nu'man of Al-Hirah (r. 505–554 CE)", "arabian", 19, "505–554 CE (Tabari Vol. 5; Procopius)", "Paramount Lakhmid Rival of Ghassan", ["Al-Tabari Vol. 5", "Procopius"], "Fought Roman-allied Ghassanid King al-Harith V across Syria."),
        N("ar4_al_numan3", "King al-Nu'man III ibn al-Mundhir of Al-Hirah (r. 582–602 CE)", "arabian", 19, "582–602 CE (Tabari Vol. 5; Kitab al-Aghani)", "Last Christian Lakhmid King of Al-Hirah", ["Al-Tabari Vol. 5"], "Patron of Pre-Islamic Arabic poets; executed by Khosrow II Parviz, sparking the Battle of Dhu Qar."),
    ]
    edges += [
        E("tab_yarub_jurhum_himyar", "ar4_yarub", "direct", "Qahtanite anchor -> Ya'rub"),
        E("bir_himyar_lakhmid_ghassan", "ar4_himyar", "expansion", "Al-Biruni South Arabian anchor -> Himyar"),
        E("ar4_dhu_nuwas", "mon_eth_kaleb", "cognate", "Aksumite King Kaleb defeats Dhu-Nuwas in Yemen (525 CE)"),
        E("ar4_saba", "ar4_kahlan", "direct", "Saba -> son Kahlan"),
        E("ar4_kahlan", "ar4_jafnah_ghassan", "expansion", "Kahlan -> Azd -> Jafnah of Ghassan"),
        E("ar4_jafnah_ghassan", "ar4_al_harith_ghassan", "direct", "Jafnah -> Ghassanid King al-Harith V ibn Jabalah"),
        E("ar4_kahlan", "ar4_imru_al_qays_lakhmid", "expansion", "Kahlan -> Lakhm -> Imru' al-Qays I of Al-Hirah"),
        E("ar4_imru_al_qays_lakhmid", "ar4_al_mundhir3", "direct", "Imru' al-Qays -> Lakhmid succession -> al-Mundhir III"),
        E("ar4_al_mundhir3", "ar4_al_numan3", "direct", "Al-Mundhir III -> al-Mundhir IV -> last king al-Nu'man III"),
    ]

    # Palmyrene Royal House
    nodes += [
        N("pal4_odenathus", "King Septimius Odaenathus of Palmyra (Husband of Zenobia, d. 267 CE)", "levant_egypt", 19, "d. 267 CE (Historia Augusta; Seller 1696)", "Corrector Totius Orientis & King of Kings of Palmyra", ["Seller 1696 (Antiquities of Palmyra)", "Historia Augusta"], "Defeated Shapur I of Persia after Valerian's capture; husband of Zenobia."),
        N("pal4_zenobia", "Empress Zenobia / Bat-Zabbai of Palmyra (r. 267–272 CE)", "levant_egypt", 19, "240–c. 275 CE (Historia Augusta; Seller 1696)", "Queen of the Palmyrene Empire", ["Seller 1696", "Zosimus Book I"], "Ruled Syria, Egypt, and Anatolia; claimed descent from Cleopatra VII of Egypt and Dido of Carthage.", major=True),
        N("pal4_vaballathus", "Emperor Vaballathus of Palmyra (Son of Odaenathus & Zenobia, r. 267–272 CE)", "levant_egypt", 19, "c. 259–273 CE (Palmyrene Coins; Zosimus)", "Son & Co-Ruler Under Zenobia", ["Seller 1696", "Zosimus"], "Bore titles of Augustus until defeated by Roman Emperor Aurelian in 272 CE."),
    ]
    edges += [
        E("pal_odenathus_zenobia", "pal4_odenathus", "direct", "Palmyrene anchor -> King Odaenathus"),
        E("pal4_odenathus", "pal4_zenobia", "direct", "Marriage of Odaenathus & Zenobia"),
        E("pal4_odenathus", "pal4_vaballathus", "direct", "Odaenathus -> son Vaballathus"),
        E("pal4_zenobia", "pal4_vaballathus", "direct", "Queen Zenobia -> son Vaballathus"),
        E("eg_ptolemy_cleopatra", "pal4_zenobia", "syncretic", "Palmyrene royal tradition claiming Zenobia descended from Cleopatra VII"),
        E("grk_dido_carthage", "pal4_zenobia", "syncretic", "Seller 1696 / Historia Augusta: Zenobia claimed kinship with Dido"),
        E("pal4_zenobia", "mon_rom_aurelian", "cognate", "Emperor Aurelian captures Queen Zenobia & Palmyra (272 CE)"),
    ]

    # =========================================================================
    # 5. AMAZIGH / BERBER PATRIARCHS (Ibn Khaldun Histoire des Berberes)
    # =========================================================================
    nodes += [
        N("ber4_berr", "Berr / Mazigh (Patriarch of the Imazighen in Ibn Khaldun)", "african", 9, "Ibn Khaldun Histoire des Berberes v4", "Patriarch of Branes & Botr", ["Ibn Khaldun Histoire des Berberes"], "Ancestor of Bernes (Branes) and Madghis al-Abtar (Botr)."),
        N("ber4_bernes", "Bernes (Progenitor of Sanhaja, Masmuda & Kutama Berbers)", "african", 10, "Ibn Khaldun v4", "Founder of the Branes Confederation", ["Ibn Khaldun"], "Father of the great sedentary Amazigh confederations."),
        N("ber4_sanhaja", "Sanhaja (Son of Bernes; Ancestor of Almoravids & Zirids)", "african", 11, "Ibn Khaldun v4", "Patriarch of Sanhaja", ["Ibn Khaldun"], "Forebear of the Sahara and Maghreb Sanhaja confederations."),
        N("ber4_masmuda", "Masmuda (Son of Bernes; Ancestor of Atlas Almohads)", "african", 11, "Ibn Khaldun v4", "Patriarch of Masmuda", ["Ibn Khaldun"], "Forebear of the High Atlas Masmuda tribes."),
        N("ber4_kutama", "Kutama (Son of Bernes; Supporters of Fatimid North Africa)", "african", 11, "Ibn Khaldun v4", "Patriarch of Kutama", ["Ibn Khaldun"], "Kabyle confederation key to North African state formation."),
        N("ber4_madghis", "Madghis al-Abtar (Progenitor of Zenata, Luwata & Hawwara Berbers)", "african", 10, "Ibn Khaldun v4", "Founder of the Botr Confederation", ["Ibn Khaldun"], "Progenitor of the Zenata nomadic confederations."),
        N("ber4_zenata", "Zana / Zenata (Descendant of Madghis al-Abtar; Ancestor of Marinids & Zayyanids)", "african", 12, "Ibn Khaldun v4", "Patriarch of the Zenata", ["Ibn Khaldun"], "Progenitor of Queen al-Kahina's Jerawa Zenata tribe."),
        N("ber4_koceila", "King Kusayla / Aksil of Altava (d. 688 CE; Awraba Berber Monarch)", "african", 20, "d. 688 CE (Ibn Khaldun)", "Leader of Awraba Amazigh Confederation", ["Ibn Khaldun"], "United Amazigh and Byzantine forces in Numidia."),
        N("ber4_kahina", "Queen Dihya al-Kahina (d. 703 CE; Jerawa Zenata Queen of the Aures)", "african", 20, "d. 703 CE (Ibn Khaldun)", "Berber Queen & Military Commander", ["Ibn Khaldun"], "Jerawa Zenata queen who led Amazigh resistance in the Aures Mountains.", major=True),
    ]
    edges += [
        E("ber_branes_botr", "ber4_berr", "direct", "Berber Noahic anchor -> Berr / Mazigh"),
        E("ber4_berr", "ber4_bernes", "direct", "Berr -> son Bernes"),
        E("ber4_berr", "ber4_madghis", "direct", "Berr -> son Madghis al-Abtar"),
        E("ber4_bernes", "ber4_sanhaja", "direct", "Bernes -> Sanhaja"),
        E("ber4_bernes", "ber4_masmuda", "direct", "Bernes -> Masmuda"),
        E("ber4_bernes", "ber4_kutama", "direct", "Bernes -> Kutama"),
        E("ber4_madghis", "ber4_zenata", "direct", "Madghis -> Zenata"),
        E("ber4_zenata", "ber4_kahina", "expansion", "Jerawa Zenata -> Queen Dihya al-Kahina"),
        E("ber_koceila_kahina", "ber4_koceila", "direct", "Berber sovereign anchor -> King Kusayla"),
        E("ber_koceila_kahina", "ber4_kahina", "direct", "Berber sovereign anchor -> Queen al-Kahina"),
    ]

    return {
        "module": "46_wave4_mesopotamia_persia_arabia_chronicles",
        "title": "Wave 4 Person-by-Person Medes, Achaemenids, Parthians, Armenian Haikids, 21-Gen Quraysh, Caliphal Houses, Himyar, Palmyra & Amazigh Patriarchs",
        "nodes": nodes,
        "edges": edges,
    }
