"""
Module 40: Deep Mining of Flavius Josephus (Antiquities of the Jews & Wars — sources/complete.pdf)
+ Intercultural Alias Atlas & Global Bloodline Bridges.

Highlights:
- Complete Esau -> Amalek -> King Agag -> Haman ben Hammedatha line (Ant. VI.7 & XI.6)
- Complete Esau -> Idumea -> Herod the Great's 10 wives & Herodian royal marriages into
  Armenia (Tigranes V & VI), Cappadocia (Glaphyra), Cilicia, Commagene, Emesa & Roman Senate (Ant. XVII-XX)
- Josephus / Rabbinic / Jasher / Tabari Edom = Rome & Byzantium Syncretism
- 1 Maccabees 12:21 & Josephus Ant. XII.4.10 Sparta–Abraham Fraternity (Graduates Sparta!)
- Josephus Ant. I.15 (Cleodemus Malchus): Abraham + Keturah -> Epher ('Africa') -> Heracles -> Mauretania (Juba II & Cleopatra Selene)
- Josephus Ant. II.10 Moses & Ethiopian Princess Tharbis + Ant. XX.2-4 Queen Helena & King Izates of Adiabene
- Dedicated Intercultural Alias cards for Abraham, Moses, Noah, Enoch, Nimrod, Joseph & Solomon
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # 1. ESAU'S COMPLETE HIDDEN GLOBAL BLOODLINE (AMALEK, HAMAN, HEROD, ARMENIA, ROME)
    # =========================================================================
    nodes += [
        N("jos_king_agag", "King Agag of Amalek (1 Sam 15; Josephus Ant. VI.7 pp.339–342)", "biblical", 15,
          "c. 1030 BCE (Josephus Ant. VI.7; 1 Sam 15)",
          "Amalekite Monarch Descended from Esau → Eliphaz → Amalek",
          ["Flavius Josephus Antiquities VI.7 (pp.339–342)", "1 Samuel 15", "Pseudo-Philo Ch. 58"],
          "Captured by King Saul and executed by Samuel; Pseudo-Philo Ch. 58 & Rabbinic Targum record Agag siring an heir before death whose line produced Haman the Agagite.",
          ["Agag ben Amalek"], major=False),
        N("jos_haman_amalekite", "Haman ben Hammedatha the Agagite/Amalekite (+ Wife Zeresh & 10 Sons, Josephus Ant. XI.6.5)", "biblical", 18,
          "5th c. BCE (Susa / Persia — Josephus Ant. XI.6.5 p.618)",
          "Grand Vizier of Xerxes I / Agagite-Amalekite Descendant of Esau",
          ["Flavius Josephus Antiquities XI.6.5 (p.618)", "Book of Esther 3 & 9"],
          "Josephus explicitly calls Haman 'by birth an Amalekite' (Ant. XI.6.5) — connecting Esau's grandson Amalek and King Agag straight into the Achaemenid Persian court opposite Benjaminite Mordecai & Queen Esther! Sons: Parshandatha, Dalphon, Aspatha, Poratha, Adalia, Aridatha, Parmashta, Arisai, Aridai & Vaizatha.",
          ["Haman the Amalekite", "Zeresh"], major=True),
        N("jos_herod_remaining_wives", "Herod the Great's Remaining 5 Wives & Children (Josephus Ant. XVII.1.3): Pallas (→ Phasael II), Phaedra (→ Roxane), Elpis (→ Salome II), Niece & Cousin", "biblical", 18,
          "37–4 BCE (Josephus Ant. XVII.1.3 p.1197)",
          "Complete 10-Wife Roster of Herod the Great",
          ["Flavius Josephus Antiquities XVII.1.3 (p.1197)", "Wars I.28.4"],
          "Completes Josephus's full inventory of Herod the Great's ten wives and their offspring: Pallas (Phasael II), Phaedra (Roxane), Elpis (Salome II), plus his unnamed niece and cousin.",
          ["Pallas, Phaedra & Elpis"], major=False),
        N("jos_herod_armenia_cilicia", "Herodian Kings of Armenia & Cilicia (Josephus Ant. XVIII.5.4): Alexander + Glaphyra → Kings Tigranes V & Tigranes VI of Armenia → Gaius Julius Alexander (+ Iotape) → Roman Consuls", "biblical", 19,
          "c. 15 BCE – 115 CE (Josephus Ant. XVII.1, XVIII.5.4 p.1196)",
          "Esau/Idumean & Hasmonean Royal Bloodline Ruling Armenia, Cilicia & Entering Roman Senate",
          ["Flavius Josephus Antiquities XVIII.5.4", "Tacitus Annals XV", "Cassius Dio"],
          "Herod's son Alexander (+ Cappadocian princess Glaphyra, also widow of King Juba II of Mauretania!) fathered King Tigranes V of Armenia and Alexander II -> King Tigranes VI of Armenia -> King Gaius Julius Alexander of Cetis/Cilicia (+ Iotape of Commagene!) -> Roman suffect consuls Julius Agrippa & Julius Alexander Berenicianus!",
          ["Tigranes V of Armenia", "Tigranes VI of Armenia", "Gaius Julius Alexander", "Glaphyra of Cappadocia"], major=True),
        N("jos_herod_emesa_rome", "Herodian–Roman–Emesa Marriages (Josephus Ant. XX.7): Berenice II (+ Emperor Titus & Polemon II), Drusilla (+ Azizus of Emesa & Felix → Agrippa, d. 79 CE Vesuvius!) & Mariamne", "biblical", 19,
          "40–79 CE (Josephus Antiquities XX.7; Acts 24:24)",
          "Final Herodian Intermarriages With Emesa, Cilicia & Flavian Rome",
          ["Flavius Josephus Antiquities XX.7", "Tacitus Histories II", "Acts 24:24"],
          "Herod Agrippa I's daughters carried the Idumean-Hasmonean bloodline across the Roman Empire: Queen Berenice II (+ Marcus Julius Alexander, Herod of Chalcis, King Polemon II of Pontus & future Roman Emperor Titus!), and Drusilla (+ King Azizus of Emesa, then Roman Procurator Felix -> son Agrippa, who perished at Pompeii in the 79 CE eruption of Mt. Vesuvius!).",
          ["Queen Berenice II", "Drusilla & Felix", "King Azizus of Emesa"], major=False),
        N("jos_esau_edom_rome_bridge", "Esau / Edom = Rome & Byzantium Cross-Tradition Bridge (Josephus, Talmud, Jasher 60–61 Zepho/Janus & Al-Tabari Banu al-Asfar)", "biblical", 13,
          "Antiquity → Medieval Chronicles",
          "Classical Jewish & Islamic Identification of Rome/Byzantium With Esau (Edom)",
          ["Book of Jasher 60–61", "Al-Tabari Vol. 2 p.17", "Talmud Megillah 6a", "Ibn Ezra Gen 27"],
          "Explains why Jewish, Sefer ha-Yashar (Zepho/Janus king of Kittim/Rome), and early Islamic (Banu al-Asfar / al-Rum descended from Esau) traditions link Rome and Byzantium spiritually and genealogically to Esau.",
          ["Edom = Rome", "Banu al-Asfar (al-Rum)"], major=True),
    ]
    edges += [
        E("esa_amalek", "jos_king_agag", "direct", "1 Sam 15 & Josephus Ant. VI.7: Agag royal house of Amalek (Esau)"),
        E("jos_king_agag", "jos_haman_amalekite", "direct", "Esth 3:1 & Josephus Ant. XI.6.5: Haman ben Hammedatha the Agagite/Amalekite"),
        E("jos_haman_amalekite", "bib_esther_mordecai", "cognate", "Purim confrontation: Haman (Esau/Amalek) vs. Esther & Mordecai (Benjamin/Kish)"),
        E("her_herod_great_family", "jos_herod_remaining_wives", "direct", "Josephus Ant. XVII.1.3: remaining 5 wives & children of Herod the Great"),
        E("her_herod_great_family", "jos_herod_armenia_cilicia", "direct", "Josephus Ant. XVIII.5.4: Alexander (+ Glaphyra) -> Armenian Kings Tigranes V/VI & Cilician/Roman lines"),
        E("her_agrippa_herodias", "jos_herod_emesa_rome", "direct", "Josephus Ant. XX.7: Berenice II (+ Titus) & Drusilla (+ Emesa & Felix -> Pompeii 79 CE)"),
        E("bib_esau", "jos_esau_edom_rome_bridge", "syncretic", "Jasher 60–61, Talmud & Tabari: Edom / Zepho (Janus) -> Rome & al-Rum"),
        E("esa_zepho", "jos_esau_edom_rome_bridge", "syncretic", "Jasher 60–61: Zepho ben Eliphaz ben Esau becomes 1st King of Kittim/Italy"),
        E("jos_esau_edom_rome_bridge", "grk_romulus_remus", "syncretic", "Syncretic Jewish & Islamic identification of Edom/Kittim with Rome"),
        E("jos_esau_edom_rome_bridge", "rom_constantine_byzantium", "syncretic", "Al-Tabari & Talmudic Edom/al-Rum identification with Eastern Rome (Byzantium)"),
    ]

    # =========================================================================
    # 2. ABRAHAM'S CROSS-CULTURAL BLOODLINES: SPARTA CHARTER + HERACLES/AFRICA
    # =========================================================================
    nodes += [
        N("jos_sparta_areus_abraham", "King Areus I of Sparta → High Priest Onias (1 Macc 12:21; Josephus Ant. XII.4.10): Spartans & Jews Brethren From Abraham!", "greek", 18,
          "c. 309–265 BCE (1 Macc 12:20–23; Josephus Ant. XII.4.10)",
          "Diplomatic Blood-Brotherhood Charter Linking Sparta Directly to Abraham",
          ["Flavius Josephus Antiquities XII.4.10 (p.661)", "1 Maccabees 12:20–23"],
          "Both 1 Maccabees 12 and Josephus Ant. XII.4.10 preserve King Areus I of Sparta's official sealed letter to High Priest Onias in Jerusalem declaring: 'It has been found in writing that the Spartans and the Jews are brethren, and that they are of the stock of Abraham!' Graduates classical Sparta into Biblically Connected!",
          ["Spartan-Abraham Charter", "King Areus I"], major=True),
        N("jos_sparta_lycurgus_leonidas", "Spartan Royal Houses (Agiad & Eurypontid): Lawgiver Lycurgus → King Leonidas I (Thermopylae, 480 BCE) → Agesilaus II → Cleomenes III", "greek", 17,
          "c. 8th–3rd c. BCE (Herodotus; Plutarch; Josephus)",
          "Kings & Lawgiver of Lacedaemon (Graduated via Abraham–Sparta Charter!)",
          ["Josephus Antiquities XII.4.10", "Herodotus VII", "Plutarch Lives"],
          "Moved out of Pending Bridge via the explicit Abraham-descent claim attested in 1 Maccabees 12:21 and Josephus Ant. XII.4.10, uniting Lawgiver Lycurgus, Leonidas I (+ Queen Gorgo), Agesilaus II, and Agiad King Areus I.",
          ["King Leonidas I", "Lawgiver Lycurgus", "Queen Gorgo"], major=True),
        N("jos_cleodemus_heracles_africa", "Josephus Ant. I.15 (Cleodemus Malchus): Abraham + Keturah → Epher / Apher ('Africa') → Heracles Weds Abraham's Granddaughter → Diodorus → Sophax (Mauretania / Juba II)", "biblical", 11,
          "Patriarchal → African-Greek Mythic Horizon (Josephus Ant. I.15 p.102)",
          "Oldest Quoted Greek-Jewish Bloodline Bridging Abraham, Heracles & North Africa",
          ["Flavius Josephus Antiquities I.15 (quoting Alexander Polyhistor / Cleodemus Malchus)", "Plutarch Life of Sertorius"],
          "Josephus Ant. I.15 cites Hellenistic Jewish historian Cleodemus Malchus: Abraham's sons by Keturah (Epher/Apher, Asshur & Japhran) conquered Libya — giving AFRICA its name from Apher — and Heracles wed Apher's daughter, siring Diodorus -> Sophax (ancestor of King Juba II & Cleopatra Selene of Mauretania!).",
          ["Cleodemus Malchus", "Apher ('Africa')", "Sophax"], major=True),
        N("jos_moses_tharbis", "Princess Tharbis of Ethiopia (Meroe/Saba) — Wife of General Moses (Josephus Ant. II.10 pp.152–154)", "biblical", 15,
          "2nd Millennium BCE (Josephus Ant. II.10.2)",
          "Ethiopian Royal Daughter Married to Moses During Nile Campaign",
          ["Flavius Josephus Antiquities II.10.2 (pp.152–154)"],
          "Josephus recounts how Moses commanded Egypt's army against Ethiopia using stork/ibis baskets against serpents, besieged Saba (Meroe), and wed Ethiopian royal princess Tharbis (matching the 'Cushite woman' of Numbers 12:1).",
          ["Tharbis of Meroe"], major=False),
        N("jos_adiabene_helena_izates", "Royal House of Adiabene (Assyria/Kurdistan, Josephus Ant. XX.2–4): King Monobazus I + Queen Helena → King Izates II & Monobazus II", "mesopotamian", 19,
          "c. 1–70 CE (Josephus Ant. XX.2–4 pp.1069–1075)",
          "Mesopotamian Royal Converts to Judaism Buried in Jerusalem",
          ["Flavius Josephus Antiquities XX.2–4 (pp.1069–1075)"],
          "King Monobazus I (Bazeus) and Queen Helena of Adiabene (ancient Assyria/Erbil) and their son King Izates II converted to Judaism, fed Jerusalem during the famine of Acts 11:28, and built the monumental Tomb of the Kings in Jerusalem.",
          ["Queen Helena of Adiabene", "King Izates II"], major=True),
    ]
    edges += [
        E("bib_abraham", "jos_sparta_areus_abraham", "syncretic", "1 Macc 12:21 & Josephus Ant. XII.4.10: Spartan King Areus declares Spartans 'of the stock of Abraham'"),
        E("jos_sparta_areus_abraham", "pri_onias_dynasty", "cognate", "Areus I of Sparta sends fraternal letter & seal to High Priest Onias in Jerusalem"),
        E("jos_sparta_areus_abraham", "jos_sparta_lycurgus_leonidas", "direct", "Agiad/Eurypontid Spartan royal house uniting Lycurgus, Leonidas I & Areus I"),
        E("ket_midian", "jos_cleodemus_heracles_africa", "expansion", "Josephus Ant. I.15 (Cleodemus): Midian's son Epher/Apher -> eponym of Africa"),
        E("mid_epher", "jos_cleodemus_heracles_africa", "expansion", "Abraham -> Midian -> Epher (Apher) -> daughter marries Heracles"),
        E("jos_cleodemus_heracles_africa", "grk_heracles", "syncretic", "Cleodemus Malchus: Heracles marries Abraham's granddaughter -> Diodorus -> Sophax"),
        E("jos_cleodemus_heracles_africa", "eg_ptolemy_cleopatra", "cognate", "Mauretania (Sophax -> Juba II) + Cleopatra Selene (daughter of Cleopatra VII!)"),
        E("bib_moses", "jos_moses_tharbis", "expansion", "Josephus Ant. II.10.2: Ethiopian Princess Tharbis marries Moses at Saba/Meroe"),
        E("bib_asshur", "jos_adiabene_helena_izates", "expansion", "Adiabene (ancient Assyria/Hadiab) -> King Monobazus I & Queen Helena"),
        E("her_agrippa_herodias", "jos_adiabene_helena_izates", "cognate", "Royal converts Queen Helena & Izates allied with 1st-c. Jerusalem & Judean famine relief"),
    ]

    # =========================================================================
    # 3. MASTER INTERCULTURAL ALIAS ATLAS (SAME CHARACTER ACROSS CULTURES)
    # =========================================================================
    nodes += [
        N("alias_abraham_cross", "Intercultural Aliases of Abraham: Abram / Ibrahim (Arabic) / Berossus's 10th Chaldean / Cleodemus's Africa-Heracles / Spartan Kinsman / Brahma-Syncretic", "biblical", 9,
          "Cross-Cultural Patriarchal Resonance",
          "Unified Alias Index Across Hebrew, Arabic, Greek, Babylonian & Indian Traditions",
          ["Genesis 11–25", "Josephus Ant. I.7, I.15, XII.4.10", "Quran / Ibn Kathir", "Post-Medieval Syncretists"],
          "Maps how Abraham appears across world traditions: Hebrew Abram/Abraham; Arabic Prophet Ibrahim (Ibn Kathir / Sirah); Berossus's 'righteous Chaldean skilled in heavenly lore' (Ant. I.7.2); Cleodemus's grandfather-in-law of Heracles & ancestor of Africa (Ant. I.15); Spartan kindred charter (1 Macc 12:21); and 17th-c. folkloric comparison of Abraham/Sarah <-> Brahma/Saraswati.",
          ["Ibrahim", "Abram", "Chaldean Astronomer", "Brahma (Syncretic)"], major=True),
        N("alias_moses_cross", "Intercultural Aliases of Moses: Moshe / Musa (Arabic) / Osarseph (Manetho) / Musaeus (Artapanus) / King of Cush (Jasher 73) / Husband of Tharbis (Josephus)", "biblical", 15,
          "Cross-Cultural Prophet-King Resonance",
          "Unified Alias Index Across Bible, Egypt, Greece, Nubia & Arabia",
          ["Exodus–Deuteronomy", "Josephus Ant. II.10 & Against Apion I.26", "Artapanus", "Book of Jasher 73"],
          "Unites Moses's names across ancient accounts: Hebrew Moshe; Quranic Prophet Musa; Egyptian priest-chronicler Manetho's Osarseph; Greco-Jewish Artapanus's Musaeus (teacher of Orpheus & Hermes); Book of Jasher's 40-year King of Cush (+ Adoniah); and Josephus's victorious Egyptian general (+ Tharbis).",
          ["Musa", "Osarseph", "Musaeus", "King of Cush"], major=True),
        N("alias_noah_cross", "Intercultural Aliases of Noah: Noach / Nuh / Ziusudra (Sumer) / Utnapishtim (Atrahasis) / Xisuthros (Berossus) / Vaivasvata Manu (India) / Yima (Iran) / Deucalion (Greece) / Janus / Fuxi (Figurist)", "biblical", 4,
          "Universal Great Flood Survivor Matrix",
          "Global Cognate & Parallel Hub Linking Humanity After the Deluge",
          ["Genesis 6–9", "Epic of Gilgamesh XI", "Shatapatha Brahmana", "Apollodorus", "Bar Hebraeus"],
          "Side-by-side comparison showing Noah's exact equivalents/parallels: Sumerian Ziusudra, Akkadian Atrahasis/Utnapishtim, Berossus's Xisuthros, Indian Vaivasvata Manu, Avestan Yima, Greek Deucalion & Ogyges, 18th-c. Janus/Oenotrus (Betham/Anderson), and Jesuit Figurist Fuxi.",
          ["Nuh", "Ziusudra", "Utnapishtim", "Vaivasvata Manu", "Deucalion"], major=True),
        N("alias_enoch_cross", "Intercultural Aliases of Enoch: Khanokh / Idris (Arabic) / Hermes Trismegistus / Thoth (Egypt) / King Saurid (Pyramid Builder) / Enmeduranki (7th Sage)", "biblical", 3,
          "Antediluvian 7th Patriarch / Astronomer Scribe Matrix",
          "Greco-Egyptian, Coptic-Arabic & Mesopotamian 7th-Sage Matrix",
          ["Genesis 5:21–24", "1 Enoch", "Al-Mas'udi", "Ibn Kathir", "Mesopotamian SKL (Enmeduranki)"],
          "Tracks how the 7th Patriarch Enoch (inventor of writing & calendar in Jubilees 4:17) is identified in Coptic-Arabic chronicles with King Saurid (builder of Great Pyramids), in Hermeticism with Thoth/Hermes Trismegistus, in Islam with Prophet Idris, and compared structurally with Enmeduranki of Sippar.",
          ["Idris", "Thoth / Hermes", "King Saurid", "Enmeduranki"], major=True),
        N("alias_nimrod_cross", "Intercultural Aliases of Nimrod: Nebrod / Belus (Babylon) / Ninus (Assyria) / Al-Dahhak (Shahnameh) / Lamurudu (Yoruba Oduduwa Chronicle) / Orion", "biblical", 7,
          "First Post-Flood Empire Builder Matrix",
          "Near Eastern, Persian & West African Royal Syncretisms",
          ["Genesis 10:8–12", "Dutripon p.9", "Al-Tabari", "Samuel Johnson History of the Yorubas"],
          "Maps Nimrod son of Cush across chronicles: Latin Vulgate/Dutripon Belus; classical Ninus of Nineveh; Persian/Arabic tyrants Zuhhak/Al-Dahhak (Tabari); and West African Yoruba chronicle ancestor Lamurudu -> Oduduwa.",
          ["Belus", "Ninus", "Lamurudu", "Al-Dahhak"], major=True),
        N("alias_joseph_solomon_cross", "Intercultural Aliases of Joseph & Solomon: Zaphenath-Paneah / Yusuf / Imhotep Parallel; Sulayman / King of Tadmor-Palmyra / Father of Menelik I (Ethiopia)", "biblical", 14,
          "Egyptian Vizier & Near Eastern Sovereign Matrix",
          "Biblical-Egyptian-Ethiopic-Palmyrene Royal Resonances",
          ["Genesis 41", "Kebra Nagast", "Seller Antiquities of Palmyra (1696)", "Quran / Ibn Kathir"],
          "Collects Joseph's Egyptian court title Zaphenath-Paneah (Arabic Yusuf, and 7-year-famine vizier parallel to Djoser's Imhotep) alongside Solomon (Sulayman), revered across Jerusalem, Aksumite Ethiopia (Menelik I), Yemen (Sheba/Bilqis), and Tadmor/Palmyra.",
          ["Zaphenath-Paneah", "Yusuf", "Sulayman"], major=True),
    ]
    edges += [
        E("bib_abraham", "alias_abraham_cross", "cognate", "Cross-cultural aliases & attestations of Abraham"),
        E("bib_moses", "alias_moses_cross", "cognate", "Cross-cultural aliases & attestations of Moses"),
        E("bib_noah", "alias_noah_cross", "cognate", "Global Great Flood hero aliases & parallels of Noah"),
        E("bib_enoch", "alias_enoch_cross", "cognate", "7th-Patriarch / Hermes / Thoth / Idris / Saurid aliases of Enoch"),
        E("bib_nimrod", "alias_nimrod_cross", "cognate", "First world-monarch aliases (Belus / Ninus / Lamurudu) of Nimrod"),
        E("tri_joseph", "alias_joseph_solomon_cross", "cognate", "Egyptian title Zaphenath-Paneah & Yusuf aliases of Joseph"),
        E("jud_solomon", "alias_joseph_solomon_cross", "cognate", "Pan-Afro-Eurasian royal traditions of King Solomon / Sulayman"),
    ]

    return {
        "module": "40_josephus_esau_herod_intercultural_bridges",
        "title": "Josephus Deep Bloodlines (Esau → Agag → Haman, Herod → Armenia/Cilicia/Rome, Sparta–Abraham Charter & Cleodemus–Heracles) + Intercultural Alias Atlas",
        "nodes": nodes,
        "edges": edges,
    }
