"""
Module 35: Assyrian Eponym Canon (George Smith 1875), Records of the Past (Vols. 9 & 11),
Turin Royal Canon (Kim Ryholt), Sir Isaac Newton's Chronology Amended (1728),
Archbishop Ussher's Annals of the World (1658), Justin / Pompeius Trogus (Jews & Parthians),
Suetonius / Herodian / Pliny, Herodotus / Polybius & Samuel Cradock's Apostolical History.

Sources integrated:
- George Smith, The Assyrian Eponym Canon (1875, pp. 10-77)
- Records of the Past, Vols. 9 & 11 (Khorsabad, Nebbi Yunus, Rimmon-Nirari I, Ashurbanipal, Eshmunazar)
- Kim Ryholt, The Turin King-List (aeundl135_156.pdf)
- Sir Isaac Newton, The Chronology of Ancient Kingdoms Amended (1728, pp. 5-93)
- Archbishop James Ussher, Annals of the World (1658, p. 7), John Blair (1753), William Guthrie (1764 Vols. 1-13),
  William Betham (Genealogical Tables, 1795), Universal History of the Holy Bible & British Family Bible
- Justin / Pompeius Trogus (Watson 1853, Book XXXVI pp. 245-249 & Book XLI p. 272)
- Suetonius (Twelve Caesars), Pliny (Panegyrick on Trajan), Herodian (After Marcus), Basil Kennett
- Herodotus (Vols. 1-2) & Polybius (General History in Five Books)
- Samuel Cradock, The Apostolical History (1672, Preface)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("asm_smith_eponym_canon",
          "Assyrian Eponym Canon Synchronisms (George Smith 1875): Shalmaneser III (↔ Ahab & Jehu), Tiglath-Pileser III (↔ Uzziah/Menahem/Ahaz) & Sargon II (722 BCE Samaria)",
          "mesopotamian", 17,
          "860–648 BCE (George Smith Assyrian Eponym Canon 1875)",
          "Cuneiform Year-by-Year Lock Linking Biblical Kings of Israel & Judah with Assyria",
          ["George Smith The Assyrian Eponym Canon (1875) pp. 10-77"],
          "British Museum Assyriologist George Smith edits the limmu eponym canon from Shalmaneser III through Sennacherib and Esarhaddon, locking Biblical reigns (Ahab, Jehu, Uzziah, Menahem, Pekah, Ahaz, Hezekiah & Tirhakah) to astronomical & eponym dates.",
          ["Limmu Eponym Canon", "George Smith 1875", "Biblical-Assyrian Synchronism"],
          major=True),

        N("asm_records_past_inscriptions",
          "Records of the Past Vols. 9 & 11 (Cuneiform & Phoenician): Rimmon-Nirari I, Khorsabad Palace, Sennacherib Nebbi Yunus (46 Cities of Hezekiah), Ashurbanipal & King Eshmunazar of Sidon",
          "mesopotamian", 17,
          "1320–5th c. BCE (Records of the Past Vols. 9 & 11)",
          "Primary Translated Assyrian, Babylonian & Phoenician Royal Inscriptions",
          ["Records of the Past Vol. 9 (Oppert, Pinches, George Smith)", "Records of the Past Vol. 11 (Sayce, Budge)"],
          "Primary translations of Adad-nirari I (son of Pudil, grandson of Bel-nirari, great-grandson of Assur-uballit I), Sargon's Khorsabad Annals, Sennacherib's Bavian & Nebbi Yunus inscriptions (46 cities of Hezekiah & Luli/Tubali of Sidon), Ashurbanipal's Cylinder B, and Sidon King Eshmunazar's sarcophagus.",
          ["Nebbi Yunus Prism", "Khorsabad Palace", "Rimmon-Nirari I", "Eshmunazar of Sidon"],
          major=True),

        N("eg_turin_royal_canon",
          "The Turin King-List / Royal Canon of Turin (Kim Ryholt): Gods → Spirit Kings (Ax.w / Shemsu-Hor) → Historical Human Pharaohs",
          "levant_egypt", 5,
          "Ramesside Papyrus inv. 1874 verso (Kim Ryholt)",
          "Only Native Pre-Ptolemaic True Royal Canon of Ancient Egypt",
          ["Kim Ryholt The Turin King-List (Papyrus Turin inv. 1874 verso)"],
          "Ryholt analyzes the 19th-Dynasty Turin King-List structuring Egyptian kingship into three tiers: mythological gods (Cols. I-II, ending in Seth & Horus), spirit/demigod kings (Ax.w / Shemsu-Hor), and exact human pharaohs through the Second Intermediate Period.",
          ["Papyrus Turin 1874", "Ax.w Spirit Kings"],
          major=True),

        N("nwt_newton_chronology_1728",
          "Sir Isaac Newton's Chronology Amended (1728): Sesostris = Shishak (1 Kings 14), Canaanites Fleeing Joshua, Danaus & Nabonassar (747 BCE)",
          "biblical", 16,
          "Newtonian Synchronism Model (Sir Isaac Newton 1728 pp. 9-93)",
          "Sir Isaac Newton's Compression of Pagan Chronologies to Biblical Anchors",
          ["Sir Isaac Newton The Chronology of Ancient Kingdoms Amended (1728) pp. 9-93"],
          "Newton synchronizes Mediterranean antiquity to Scripture by identifying Egyptian conqueror Sesostris with Biblical Shishak (1 Kings 14), tracing the Canaanite flight from Joshua into Egypt and Greece (Danaus), and anchoring Babylon & Assyria at Pul (747 BCE) and Nabonassar.",
          ["Sesostris = Shishak", "Canaanites from Joshua", "Newton 1728"],
          major=True),

        N("ush_ussher_annals_4004",
          "Archbishop Ussher's Annals of the World (1658), Blair (1753), Guthrie (1764) & Betham Tables (1795): Universal Biblical-Classical Chronology (4004 BCE – 70 CE)",
          "biblical", 4,
          "Universal Chronography (Ussher 1658 p. 7; Blair 1753; Guthrie 1764; Betham 1795)",
          "Grand Comparative Synchronism Unifying Creation, Patriarchs, Egypt & Greece",
          ["Archbishop James Ussher Annals of the World (1658) p. 7", "John Blair Chronology (1753)", "Guthrie & Gray General History (1764 Vols. 1-13)", "William Betham Genealogical Tables (1795)"],
          "Ussher's Annals (with Blair's Tables, Guthrie & Gray's 13-volume Universal History, the Universal History of the Holy Bible & British Family Bible) align Creation (4004 BCE), the Flood, Abraham, Jacob, Sicyon/Argos (Aegialeus/Inachus), and Manetho's Hyksos Pharaohs into one continuous timeline.",
          ["Ussher 4004 BCE", "Guthrie 13 Vols", "Blair 1753"],
          major=True),

        N("jus_trogus_jews_moses",
          "Justin / Pompeius Trogus Book XXXVI (Pagan Roman Testimony): Damascus → Abraham → Israhel (Jacob) → Judah, Joseph in Egypt & Moses",
          "biblical", 11,
          "1st c. BCE / 2nd c. CE (Justin Epitome of Pompeius Trogus XXXVI.2)",
          "Independent Greco-Roman Ethnographic Summary of Israelite Origins",
          ["Justin / Pompeius Trogus Book XXXVI (Watson 1853 p. 245)"],
          "Trogus & Justin independently attest Hebrew patriarchs as historical kings/rulers in Syria ('Damascus -> Azelus -> Adores -> Abraham -> Israhel' with ten/twelve sons, Judas, Joseph in Egyptian dreamcraft & magic, and Moses leading the Exodus).",
          ["Trogus Book XXXVI", "Israhel & Judas", "Pagan Testimony"],
          major=True),

        N("jus_parthians_scythians",
          "Justin Book XLI (Scythian Origin of Parthia): Exiled Scythians ('Parthi') → King Arsaces I → Mithridates I → Phraates",
          "iranian", 18,
          "247 BCE – 20 CE (Justin Epitome Book XLI pp. 272-297)",
          "Classical Testimony Tracing the Arsacid Parthian Empire to Scythia",
          ["Justin / Pompeius Trogus Book XLI (Watson 1853 pp. 272-297)"],
          "Justin Book XLI explains that the Parthians — rivals who divided the world with Rome — originated as 'Parthi' (exiles) from Scythia before rising under Arsaces I, Mithridates I, and Phraates.",
          ["Scythian Parthi", "Arsaces I", "Mithridates I"],
          major=False),

        N("rom_suetonius_herodian_severans",
          "Suetonius (Twelve Caesars), Pliny & Herodian: Commodus → Pertinax → Septimius Severus → Caracalla → Elagabalus → Severus Alexander",
          "greek", 19,
          "49 BCE – 238 CE (Suetonius; Pliny; Herodian; Basil Kennett)",
          "Julio-Claudian / Flavian Documentation & Severan Roman Emperors",
          ["Suetonius Lives of the Twelve Caesars", "Herodian History of the Roman Emperors (1689 / 1749)", "Pliny Panegyrick on Trajan", "Basil Kennett Antiquities of Rome"],
          "Combines Suetonius's biographies of the Twelve Caesars, Pliny's Panegyrick on Trajan, Kennett's Roman Antiquities, and Herodian's eyewitness narrative from Marcus Aurelius & Commodus through Pertinax, Septimius Severus (campaigns in Britain), Caracalla, Elagabalus, and Severus Alexander.",
          ["Twelve Caesars", "Septimius Severus", "Severus Alexander"],
          major=True),

        N("cls_herodotus_polybius_bridge",
          "Herodotus (Egypt, Persia & Greece) & Polybius (Punic Wars / Scipio & Hannibal): Classical Mediterranean Synchronisms",
          "greek", 18,
          "5th–2nd c. BCE (Herodotus Vols. 1-2; Polybius Books I-V)",
          "Father of History (Egypt/Cyrus/Xerxes) & Carthage–Rome Constitutional Bridge",
          ["Herodotus Egyptian and Grecian History (Vols. 1-2)", "Polybius General History in Five Books"],
          "Anchors Achaemenid, Saitic Egyptian, and Ionian/Athenian lineages (Herodotus Vols. 1-2) alongside Polybius's analytical account of the Punic Wars uniting Barcid Carthage, Numidia, Hellenistic Macedon/Seleucids, and Republican Rome.",
          ["Herodotus Father of History", "Polybius Punic Bridge"],
          major=False),

        N("nt_cradock_apostolic_missions",
          "Cradock's Apostolical History (1672): Global Missions of the Apostles — Paul's 5 Journeys to Rome, Peter, James, John, Thomas & the Early Churches",
          "biblical", 19,
          "30–68 CE (Samuel Cradock 1672)",
          "Complete Narrative Chronotaxis of the Apostolic Era & Epistles",
          ["Samuel Cradock The Apostolical History (1672) Preface"],
          "Cradock maps all five missionary journeys of Apostle Paul (Syria, Cyprus, Galatia, Macedonia, Greece, Ephesus & Rome), alongside the churches founded by Peter, James, John, and the Twelve Apostles.",
          ["Paul's 5 Journeys", "Apostolic Churches"],
          major=True),
    ]

    edges += [
        E("for_neo_assyria", "asm_smith_eponym_canon", "cognate", "George Smith 1875 edits the Assyrian Eponym Canon directly underlying Neo-Assyrian royal chronology"),
        E("asm_smith_eponym_canon", "kg_i3_omri_ahab", "cognate", "Shalmaneser III Kurkh Monolith / Eponym Canon synchronizes 853 BCE Battle of Qarqar with Ahab of Israel"),
        E("asm_smith_eponym_canon", "kg_i4_jehu", "cognate", "Black Obelisk & Eponym Canon record tribute of Jehu ('Son of Omri') to Shalmaneser III"),
        E("asm_smith_eponym_canon", "kg_i5_hoshea", "cognate", "Eponym Canon fixes Tiglath-Pileser III (Menahem/Pekah/Hoshea) and Sargon II's 722 BCE fall of Samaria"),
        E("for_neo_assyria", "asm_records_past_inscriptions", "cognate", "Records of the Past Vols. 9 & 11 provide full translations of Rimmon-Nirari I, Khorsabad, Nebbi Yunus & Ashurbanipal"),
        E("asm_records_past_inscriptions", "kg_j9_hezekiah", "cognate", "Records of the Past Vol. 11 p. 47 (Nebbi Yunus): Sennacherib captures 46 fortified cities of Hezekiah"),
        E("asm_records_past_inscriptions", "af_taharqa", "cognate", "George Smith (Vol. 9) & Esarhaddon/Ashurbanipal texts detail Assyrian campaigns against Pharaoh Tirhakah (Taharqa)"),
        E("asm_records_past_inscriptions", "bib_sidon", "cognate", "Records of the Past Vol. 9 p. 109 (Eshmunazar of Sidon) & Vol. 11 p. 51 (Luli/Tubali of Sidon)"),
        E("asm_records_past_inscriptions", "ir_cyrus", "cognate", "Records of the Past Vol. 9 p. 67 translates the Persian Inscriptions of Cyrus the Achaemenian"),
        E("eg_manetho_demigods", "eg_turin_royal_canon", "cognate", "Kim Ryholt compares the native Papyrus Turin Royal Canon (Gods -> Ax.w -> Pharaohs) with Manetho"),
        E("eg_turin_royal_canon", "eg_dyn15_17_hyksos_thebes", "cognate", "Turin King-List spans Egyptian pharaohs down to the end of the Second Intermediate Period / Hyksos"),
        E("eg_shoshenq1", "nwt_newton_chronology_1728", "syncretic", "Isaac Newton 1728 identifies Egyptian conqueror Sesostris directly with Biblical Shishak (Shoshenq I)"),
        E("kg_j1_rehoboam", "nwt_newton_chronology_1728", "cognate", "Newton anchors Shishak's invasion in the 5th year of King Rehoboam (1 Kings 14)"),
        E("bib_joshua_caleb", "nwt_newton_chronology_1728", "syncretic", "Newton 1728 p. 10: Canaanites fleeing Joshua migrate into Egypt and across the Mediterranean"),
        E("bib_canaan", "nwt_newton_chronology_1728", "syncretic", "Canaanite/Phoenician mariners spreading letters and navigation west (Newton 1728)"),
        E("grk_aegyptus_danaus", "nwt_newton_chronology_1728", "syncretic", "Newton 1728 p. 71 synchronizes Danaus's flight from Egypt into Greece with Shishak's era"),
        E("bib_noah", "ush_ussher_annals_4004", "expansion", "Ussher (1658), Blair (1753) & Guthrie (1764) frame universal world history from Creation and Noah's Flood"),
        E("ush_ussher_annals_4004", "bib_abraham", "cognate", "Ussher 1658 p. 6-7 fixes Terah, Abraham, Isaac, Jacob & Arphaxad/Salah patriarchal years"),
        E("ush_ussher_annals_4004", "eg_dyn15_17_hyksos_thebes", "cognate", "Ussher 1658 p. 7 (citing Manetho, Apion & Josephus) equates Hyksos expulsion with early Israelite-Egyptian synchronisms"),
        E("bib_abraham", "jus_trogus_jews_moses", "cognate", "Justin Book XXXVI (Watson 1853 p. 245) names Abraham and Israhel among ancient Syrian rulers"),
        E("bib_jacob", "jus_trogus_jews_moses", "cognate", "Justin XXXVI.2 records Israhel dividing his people under his sons and Joseph's rise in Egypt"),
        E("bib_moses", "jus_trogus_jews_moses", "cognate", "Justin XXXVI.2 documents Moses leading Israel out of Egypt toward Sinai"),
        E("bib_magog", "jus_parthians_scythians", "syncretic", "Justin XLI.1 derives the Parthians as exiles ('Parthi') from Scythia (Magog horizon)"),
        E("bir_parthians_ashkanians", "jus_parthians_scythians", "cognate", "Same Arsacid Parthian dynasty (Arsaces I -> Mithridates -> Artabanus) across Al-Biruni & Justin"),
        E("rom_julio_claudians", "rom_suetonius_herodian_severans", "cognate", "Suetonius Twelve Caesars covers Julius Caesar & Julio-Claudians -> Flavians"),
        E("rom_echard_imperial_bridge", "rom_suetonius_herodian_severans", "expansion", "Herodian extends Imperial Rome from Marcus Aurelius & Commodus across the Severan dynasty (180-238 CE)"),
        E("ir_cyrus", "cls_herodotus_polybius_bridge", "cognate", "Herodotus Books I-III chronicle Cyrus, Cambyses & Darius across Lydia, Babylon & Egypt"),
        E("grk_dido_carthage", "cls_herodotus_polybius_bridge", "cognate", "Polybius Books I-V chronicle Carthaginian-Roman Punic Wars"),
        E("rom_echard_imperial_bridge", "cls_herodotus_polybius_bridge", "cognate", "Roman Mediterranean hegemony documented in Polybius & Livy"),
        E("nt_jesus", "nt_cradock_apostolic_missions", "expansion", "Cradock Apostolical History (1672): Post-Resurrection commissions of the Apostles"),
        E("nt_paul", "nt_cradock_apostolic_missions", "expansion", "Cradock 1672 Preface maps Paul's five apostolic journeys from Antioch to Rome (63 CE)"),
        E("nt_remaining_apostles", "nt_cradock_apostolic_missions", "expansion", "Cradock 1672 summarizes acts and epistles of Peter, James, John & the Twelve"),
    ]

    return {
        "module": "35_newton_ussher_smith_records_classical",
        "title": "George Smith Eponym Canon, Records of the Past, Turin Canon, Sir Isaac Newton, Ussher, Justin, Suetonius/Herodian & Cradock",
        "nodes": nodes,
        "edges": edges,
    }
