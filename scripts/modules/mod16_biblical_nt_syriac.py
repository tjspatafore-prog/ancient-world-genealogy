"""
Module 16: Exhaustive Biblical Tribal Lineages (1 Chronicles 1-9), Second Temple High Priests,
Maccabees/Hasmoneans, Complete Herodian Dynasty, Complete New Testament Families & 12 Apostles,
plus Syriac Cave of Treasures & Josephus Antiquities Expansions.

Sources mined from sources/:
- Copy of M_F_Gervais UsefulChart Book of Genesis.pdf
- Copy of M_F_Gervais UsefulChart Exodus to Nebuchadnezzar.pdf
- Copy of M_F_Gervais UsefulChart Jesus Christ.pdf
- Copy of M_F_Gervais UsefulChart New Testament.pdf
- familytree.PDF (1975 Adam & Eve Family Tree Wall Chart)
- 124482365-Bible-Genealogy-a1-Chart.pdf (Dr. M.D. Bennett 1967 Chart)
- JesusGenealogy.PDF (Anno Mundi Chronology)
- complete.pdf (Flavius Josephus, Antiquities of the Jews & Wars)
- Budge_1927_Cave_of_Treasures.pdf (Syriac Me'arath Gazze)
"""

from . import N, E, add_children, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. COMPLETE 1 CHRONICLES 1-9 TRIBAL SUB-LINEAGES & DAVIDIC HOUSEHOLD
    # -------------------------------------------------------------------------
    nodes += [
        # Judah -> Hezron's branches (1 Chr 2:9-55, familytree.PDF, Bennett 1967, Gervais Exodus)
        N("chr_hezron_ram", "Hezron → Jerahmeel, Ram, Caleb (Chelubai) & Ashhur", "biblical", 14, "Egypt / Wilderness (1 Chr 2:9-24)",
          "Founders of the Four Great Clans of Judah", ["1 Chronicles 2:9-24", "Bennett 1967 Chart", "1975 FamilyTree Chart"],
          "Hezron (son of Perez) fathers Jerahmeel, Ram (ancestral line to David via Amminadab -> Nahshon -> Salmon + Rahab -> Boaz), Caleb/Chelubai (+ Azubah, Jerioth, Ephrath -> Hur), and posthumously Ashhur (father of Tekoa via Abijah).",
          ["Hezron", "Jerahmeel", "Caleb ben Hezron", "Ashhur"]),
        N("chr_hur_bezalel", "Hur (son of Caleb & Ephrath) → Uri → Bezalel (Tabernacle Architect)", "biblical", 15, "Exodus Era (Ex 31:2; 1 Chr 2:19-20)",
          "Chief Craftsman of the Ark & Tabernacle", ["Exodus 31:2", "1 Chronicles 2:19-20", "1975 FamilyTree Chart"],
          "Hur (who held up Moses's hands at Rephidim alongside Aaron) fathers Uri -> Bezalel, Shobal (father of Kiriath-jearim), Salma (father of Bethlehem), and Hareph (father of Beth-gader).",
          ["Hur", "Uri", "Shobal", "Salma of Bethlehem"]),
        N("chr_elimelech_naomi", "Elimelech & Naomi → Mahlon (+ Ruth) & Chilion (+ Orpah)", "biblical", 15, "Judges Era (Book of Ruth 1)",
          "Bethlehem Ephrathite Family of Ruth", ["Ruth 1:1-5", "Gervais UsefulChart Exodus"],
          "Elimelech and Naomi migrate from Bethlehem to Moab; their sons Mahlon and Chilion marry Moabite women Ruth and Orpah. After Mahlon's death, Boaz redeems Ruth, fathering Obed -> Jesse -> King David.",
          ["Naomi", "Ruth the Moabite", "Orpah"]),
        N("chr_jesse_nitzevet", "Jesse & Nitzevet → Eliab, Abinadab, Shimea, Nethanel, Raddai, Ozem & David", "biblical", 15, "c. 1070-1010 BCE (1 Chr 2:13-17; Talmud)",
          "Complete Household of Jesse of Bethlehem", ["1 Chronicles 2:13-17", "Talmud Bava Batra 91a", "Gervais UsefulChart Exodus"],
          "Talmudic tradition names David's mother Nitzevet bat Adael. Jesse's seven sons (Eliab, Abinadab, Shimea/Shammah -> Jonadab, Nethanel, Raddai, Ozem, David) and two daughters (Zeruiah -> Joab/Abishai/Asahel; Abigail + Ithra/Jether -> Amasa).",
          ["Nitzevet", "Abinadab", "Shimea", "Nethanel", "Raddai", "Ozem"]),
        N("chr_david_wives_sons", "King David's Complete Household (8 Wives & 19 Named Sons + Tamar)", "biblical", 16, "c. 1010-970 BCE (2 Sam 3; 1 Chr 3:1-9)",
          "Full Royal House of David in Hebron & Jerusalem", ["2 Samuel 3:2-5, 5:14-16", "1 Chronicles 3:1-9", "Gervais UsefulChart Exodus"],
          "Hebron sons: Amnon (by Ahinoam), Chileab/Daniel (by Abigail), Absalom & Tamar (by Maacah bat Talmai of Geshur), Adonijah (by Haggith), Shephatiah (by Abital), Ithream (by Eglah). Jerusalem sons: Shammua, Shobab, Nathan (Luke 3 line!), Solomon (by Bathsheba), plus Ibhar, Elishua, Eliphelet, Nogah, Nepheg, Japhia, Elishama, Eliada & Jerimoth.",
          ["Amnon", "Chileab", "Absalom", "Adonijah", "Nathan ben David", "Bathsheba", "Maacah of Geshur"], major=True),

        # Reuben, Simeon, Levi, Joseph, Benjamin sub-lineages from 1975 FamilyTree & Bennett 1967
        N("chr_reuben_dathan", "Eliab (Reuben) → Nemuel, Dathan & Abiram (Korah's Rebellion)", "biblical", 15, "Wilderness Era (Num 16:1, 26:8-9)",
          "Reubenite Leaders of the Wilderness Revolt", ["Numbers 16:1, 26:8-9", "1975 FamilyTree Chart", "Bennett 1967 Chart"],
          "Pallu -> Eliab -> Dathan and Abiram, who joined Korah the Levite in challenging Moses and Aaron in the wilderness. Also Reubenite Prince Elizur son of Shedeur & Shammua son of Zaccur (spy).",
          ["Dathan", "Abiram", "Elizur ben Shedeur"]),
        N("chr_levi_24_courses", "24 Levitical Priestly Courses (Jehoiarib, Abijah, Zadok) & Temple Musicians", "biblical", 16, "c. 1000 BCE (1 Chr 6 & 24)",
          "24 Priestly Divisions + Asaph, Heman & Ethan (Jeduthun)", ["1 Chronicles 6, 24-25", "1975 FamilyTree Chart"],
          "King David organized Aaron's descendants (16 courses of Eleazar, 8 of Ithamar) into 24 priestly rotations: 1. Jehoiarib (Hasmonean/Maccabee clan!), 8. Abijah (Zechariah father of John the Baptist!). Alongside Temple Choirs of Gershon (Asaph), Kohath (Heman), and Merari (Ethan/Jeduthun).",
          ["Course of Jehoiarib", "Course of Abijah", "Ethan/Jeduthun"]),
        N("chr_manasseh_machir", "Machir (Manasseh) → Gilead → Hepher → Zelophehad & Jair", "biblical", 15, "Wilderness / Conquest (Num 26:29-33; 1 Chr 7:14)",
          "Transjordanian House of Manasseh", ["Numbers 26:29-33", "1 Chronicles 7:14-19", "1975 FamilyTree Chart"],
          "Machir (son of Manasseh & an Aramean concubine) -> Gilead -> Iezer (ancestor of Gideon!), Helek, Asriel, Shechem, Shemida, and Hepher -> Zelophehad (whose 5 daughters Mahlah, Noah, Hoglah, Milcah, Tirzah established female inheritance law in Israel!).",
          ["Machir", "Gilead", "Hepher"]),
        N("chr_ephraim_joshua", "Ephraim → Beriah & Sherah → Resheph → Elishama → Nun → Joshua", "biblical", 15, "Egypt / Exodus (1 Chr 7:20-27)",
          "Complete 10-Generation Ephraimite Lineage to Joshua", ["1 Chronicles 7:20-27", "Bennett 1967 Chart", "1975 FamilyTree Chart"],
          "1 Chronicles 7 records Ephraim's daughter Sherah (who built Lower & Upper Beth-horon!) and traces Beriah -> Rephah -> Resheph -> Telah -> Tahan -> Ladan -> Ammihud -> Elishama (Prince of Ephraim) -> Nun -> Joshua (Yehoshua).",
          ["Sherah", "Elishama", "Nun"]),
        N("chr_saul_ner_abner", "Jeiel / Abiel → Ner → General Abner & Kish → King Saul's Sons", "biblical", 16, "c. 1050-1000 BCE (1 Sam 9, 14; 1 Chr 8-9)",
          "Complete Benjamite Royal House of Saul", ["1 Samuel 9:1, 14:50", "1 Chronicles 8:33-40", "Gervais UsefulChart Exodus"],
          "Abiel fathers Kish (father of King Saul) and Ner (father of General Abner, commander of Saul's army). Saul's sons: Jonathan (-> Mephibosheth -> Mica), Abinadab, Malchishua, Ish-bosheth (Eshbaal), plus Armoni & Mephibosheth (by Rizpah bat Aiah), and daughters Merab & Michal.",
          ["General Abner", "Ish-bosheth", "Mephibosheth", "Rizpah"]),
        N("chr_jeroboam_ano", "Jeroboam I & Queen Ano (Egyptian Princess) → Abijah & Nadab", "biblical", 17, "c. 930-909 BCE (1 Kgs 11-14; Septuagint 3 Kgdms 12)",
          "Egyptian Royal Marriage of Israel's First Northern King", ["1 Kings 11:40, 14:1", "Septuagint 3 Kingdoms 12:24e", "Gervais UsefulChart Exodus"],
          "The Greek Septuagint preserves the name Ano, sister-in-law of Pharaoh Shishak (Shoshenq I), given in marriage to Jeroboam I during his Egyptian exile — linking the Northern Kingdom of Israel directly to Egypt's 22nd Dynasty!",
          ["Queen Ano of Egypt", "Zeruah"]),
        N("chr_edom_kings", "8 Early Kings of Edom (Bela ben Beor through Hadar & Queen Mehetabel)", "biblical", 14, "Pre-Monarchic Edom (Gen 36:31-39; 1 Chr 1:43-50)",
          "Elective Pre-Israelite Kings of Edom", ["Genesis 36:31-39", "1 Chronicles 1:43-50", "1975 FamilyTree Chart"],
          "Eight kings who reigned in Edom before any king reigned over Israel: 1. Bela ben Beor (Dinhabah), 2. Jobab ben Zerah of Bozrah, 3. Husham (Temanites), 4. Hadad ben Bedad (defeated Midian), 5. Samlah (Masrekah), 6. Shaul (Rehoboth), 7. Baal-hanan ben Achbor, 8. Hadar/Hadad (+ Mehetabel bat Matred).",
          ["Bela ben Beor", "Jobab of Bozrah", "Baal-hanan", "Hadar & Mehetabel"]),

        # -------------------------------------------------------------------------
        # 2. SECOND TEMPLE ZADOKITE & ONIAD HIGH PRIESTS (Josephus & Gervais NT)
        # -------------------------------------------------------------------------
        N("pri_jeshua_eliashib", "High Priest Jeshua (Joshua) → Joiakim → Eliashib → Joiada → Johanan → Jaddua", "biblical", 17, "c. 538-320 BCE (Neh 12:10-22; Josephus Ant. XI)",
          "Persian-Era High Priests of the Second Temple", ["Nehemiah 12:10-22", "Josephus Antiquities XI.7-8", "Gervais UsefulChart NT"],
          "Continuous post-exilic Zadokite succession from Seraiah -> Jehozadak -> Jeshua (rebuilt Second Temple with Zerubbabel) down to Jaddua, who according to Josephus (Ant. XI.8.5) met Alexander the Great at Jerusalem in 332 BCE! Jaddua's brother Manasseh married Nikaso daughter of Sanballat and founded the Samaritan Temple on Mount Gerizim.",
          ["Joiakim", "Eliashib", "Joiada", "Johanan", "Jaddua", "Manasseh of Gerizim"], major=True),
        N("pri_onias_dynasty", "Oniad High Priests: Onias I → Simon I the Just → Eleazar → Onias II → Simon II → Onias III", "biblical", 18, "c. 320-175 BCE (Josephus Ant. XII; 2 Maccabees)",
          "Hellenistic-Era Zadokite High Priests", ["Josephus Antiquities XII.2-5", "2 Maccabees 3-4", "Gervais UsefulChart NT"],
          "Eleazar sent the 72 scholars to Ptolemy II Philadelphus in Alexandria to translate the Torah into Greek (the Septuagint!). Onias III's brother Jason Hellenized Jerusalem; Onias III's son Onias IV fled to Egypt and built the Jewish Temple at Leontopolis, fathering Helkias & Ananias (generals of Queen Cleopatra III!).",
          ["Onias I", "Simon the Just", "High Priest Eleazar (Septuagint)", "Onias III", "Jason", "Onias IV of Leontopolis"]),

        # -------------------------------------------------------------------------
        # 3. COMPLETE MACCABEES & HASMONEAN DYNASTY (1-2 Maccabees, Josephus Ant. XII-XV, Gervais NT)
        # -------------------------------------------------------------------------
        N("has_mattathias", "Mattathias of Modi'in (Priest of Course of Jehoiarib)", "biblical", 18, "c. 167 BCE (1 Macc 2; Josephus Ant. XII.6)",
          "Patriarch of the Maccabean Revolt", ["1 Maccabees 2:1-5", "Josephus Antiquities XII.6", "Gervais UsefulChart NT"],
          "Priest of the line of Joarib/Jehoiarib (son of John, son of Simeon, son of Asamonaeus/Hasmon) who sparked the revolt against Seleucid King Antiochus IV Epiphanes. Father of 5 sons: John Gaddi, Simon Thassi, Judas Maccabeus, Eleazar Avaran, and Jonathan Apphus.",
          ["Mattathias ben Johanan", "Hasmon"], major=True),
        N("has_judas_maccabeus", "Judas Maccabeus ('The Hammer'), John Gaddi, Eleazar Avaran & Jonathan Apphus", "biblical", 18, "166-143 BCE (1 Macc 3-12; Josephus Ant. XII-XIII)",
          "Maccabean Commanders & Hanukkah Liberators", ["1 Maccabees 3-12", "Josephus Antiquities XII-XIII", "Gervais UsefulChart NT"],
          "Judas Maccabeus rededicated the Second Temple in 164 BCE (origin of Hanukkah); Eleazar Avaran died crushing a Seleucid war elephant; Jonathan Apphus became the first Hasmonean High Priest (152-143 BCE).",
          ["Judah Maccabee", "Jonathan Apphus", "Eleazar Avaran", "John Gaddi"], major=True),
        N("has_simon_hyrcanus1", "Simon Thassi (Ethnarch) → John Hyrcanus I (134-104 BCE)", "biblical", 18, "142-104 BCE (1 Macc 13-16; Josephus Ant. XIII.7-10)",
          "Founders of the Independent Hasmonean State", ["1 Maccabees 13-16", "Josephus Antiquities XIII", "Gervais UsefulChart NT"],
          "Simon Thassi won full independence from the Seleucids; his son John Hyrcanus I expanded Judea, conquered Samaria and Idumea (converting the Edomites/Idumeans — ancestors of Herod the Great!).",
          ["Simon Thassi", "John Hyrcanus I"]),
        N("has_jannaeus_salome", "Aristobulus I (1st King) & Alexander Jannaeus + Queen Salome Alexandra", "biblical", 18, "104-67 BCE (Josephus Ant. XIII.11-16)",
          "Hasmonean Kings & Sole Regnant Queen of Judea", ["Josephus Antiquities XIII.11-16", "Gervais UsefulChart NT"],
          "Aristobulus I (Judah) assumed the royal diadem; his brother Alexander Jannaeus married Salome Alexandra, who ruled Judea in her own right (76-67 BCE) — a golden age of Pharisaic scholarship.",
          ["Aristobulus I", "Alexander Jannaeus", "Queen Salome Alexandra"], major=True),
        N("has_hyrcanus2_aristobulus2", "Hyrcanus II & Aristobulus II → Alexander II, Antigonus II & Mariamne I", "biblical", 18, "67-37 BCE (Josephus Ant. XIV-XV)",
          "Last Hasmonean Rulers & Bridge to the Herodian Dynasty", ["Josephus Antiquities XIV-XV", "Gervais UsefulChart NT"],
          "Civil war between brothers Hyrcanus II and Aristobulus II brought Pompey and Rome into Jerusalem (63 BCE). Hyrcanus II's daughter Alexandra married Aristobulus II's son Alexander II, producing Aristobulus III (last Hasmonean High Priest) and Princess Mariamne I — who married Herod the Great!",
          ["Hyrcanus II", "Aristobulus II", "Antigonus II Mattathias", "Mariamne I", "Aristobulus III"]),

        # -------------------------------------------------------------------------
        # 4. COMPLETE HERODIAN DYNASTY (Josephus Ant. XIV-XX, New Testament, Gervais NT)
        # -------------------------------------------------------------------------
        N("her_antipater_cypros", "Antipas → Antipater the Idumean & Cypros (Nabataean Princess)", "biblical", 18, "c. 100-43 BCE (Josephus Ant. XIV)",
          "Idumean-Nabataean Founders of the Herodian House", ["Josephus Antiquities XIV.1, 7", "Gervais UsefulChart NT"],
          "Antipater (chief minister of Hyrcanus II, appointed Procurator of Judea by Julius Caesar) married Nabataean princess Cypros, fathering Phasael I, Herod I the Great, Joseph I, Pheroras, and Salome I (+ Costobarus).",
          ["Antipater I", "Cypros of Nabataea", "Phasael I", "Salome I"]),
        N("her_herod_great_family", "Herod I the Great (10 Wives) → Antipater II, Alexander, Aristobulus IV, Archelaus, Antipas & Philip", "biblical", 18, "37-4 BCE (Josephus Ant. XV-XVII; Matt 2)",
          "Roman Client King of Judea & Builder of the Second Temple", ["Josephus Antiquities XV-XVII", "Matthew 2", "Gervais UsefulChart NT"],
          "Married Doris (Antipater II), Hasmonean Mariamne I (Alexander + Glaphyra of Cappadocia; Aristobulus IV + Berenice), Mariamne II bat Simon Boethus (Herod II Philip), Malthace (Archelaus, Herod Antipas), Cleopatra of Jerusalem (Philip the Tetrarch), and 5 other wives.",
          ["Herod the Great", "Herod Antipas", "Herod Archelaus", "Philip the Tetrarch", "Glaphyra of Cappadocia"], major=True),
        N("her_agrippa_herodias", "Aristobulus IV & Berenice → King Herod Agrippa I, Herod of Chalcis & Herodias (+ Salome)", "biblical", 19, "c. 10 BCE – 93 CE (Acts 12, 25-26; Josephus Ant. XVIII-XX)",
          "Final Herodian Monarchs & Emesa/Armenia Royal Marriages", ["Acts 12, 25-26", "Josephus Antiquities XVIII-XX", "Gervais UsefulChart NT"],
          "Herod Agrippa I (+ Cypros) fathered King Herod Agrippa II, Berenice II, Mariamne, and Drusilla (+ Roman Governor Felix). Herodias (wife of Herod II Philip, then Herod Antipas) was mother of Princess Salome. Aristobulus Minor married Salome; Mariamne's line intermarried with Sampsiceramus II (Priest-King of Emesa) and Tigranes V/VI of Armenia!",
          ["Herod Agrippa I", "Herod Agrippa II", "Herodias", "Salome", "Drusilla", "Sampsiceramus II of Emesa"]),

        # -------------------------------------------------------------------------
        # 5. COMPLETE NEW TESTAMENT FAMILIES & ALL 12 APOSTLES (Gervais UsefulChart NT & Jesus)
        # -------------------------------------------------------------------------
        N("nt_joachim_anne", "Joachim (Heli) & Saint Anne → Blessed Virgin Mary", "biblical", 18, "1st c. BCE (Luke 3:23; Protoevangelium of James)",
          "Maternal Grandparents of Jesus of Nazareth", ["Luke 3:23", "Protoevangelium of James", "Gervais UsefulChart NT"],
          "Early Christian tradition (Protoevangelium of James) names Mary's parents Joachim (often harmonized with Heli of Luke 3:23) and Anne; Anne's sister Sobe is traditionally mother of Elizabeth (mother of John the Baptist).",
          ["Joachim", "Saint Anne", "Sobe"]),
        N("nt_mary_clopas_alphaeus", "Alphaeus (Clopas) & Mary of Clopas → James the Lesser & Jude Thaddeus", "biblical", 19, "1st c. CE (Matt 10:3; John 19:25; Eusebius HE III.11)",
          "Holy Family Kinsmen & Early Bishops of Jerusalem", ["Matthew 10:3", "John 19:25", "Gervais UsefulChart NT", "Eusebius"],
          "Hegesippus (in Eusebius) records Clopas as brother of Joseph of Nazareth; his son Simeon became the 2nd Bishop of Jerusalem after James the Just! Gervais UsefulChart links Alphaeus/Clopas & Mary of Clopas to Apostles James the Lesser and Jude Thaddeus.",
          ["Clopas", "Alphaeus", "Mary of Clopas", "James the Lesser", "Jude Thaddeus"]),
        N("nt_zebedee_salome", "Zebedee & Salome → Apostle James the Great & Apostle John the Evangelist", "biblical", 19, "1st c. CE (Matt 4:21, 27:56; Mark 15:40)",
          "Sons of Thunder (Boanerges) — Inner Circle Apostles", ["Matthew 4:21, 27:56", "Mark 3:17", "Gervais UsefulChart NT"],
          "Galilean fishermen brothers James the Great (martyred under Herod Agrippa I, Acts 12:2) and John the Beloved/Evangelist (author of Fourth Gospel & Revelation).",
          ["Zebedee", "Salome", "James the Great", "John the Apostle"], major=True),
        N("nt_jonah_peter_andrew", "Jonah (John) of Bethsaida → Apostle Simon Peter & Apostle Andrew", "biblical", 19, "1st c. CE (Matt 16:17; John 1:40-44)",
          "Chief Apostles of Galilee, Rome & Constantinople", ["Matthew 16:17", "John 1:40-44", "Gervais UsefulChart NT"],
          "Simon Peter (Cephas, traditional 1st Bishop of Rome) and his brother Andrew (traditional founder of Byzantium/Constantinople see).",
          ["Simon Peter", "Andrew the Apostle", "Jonah of Bethsaida"], major=True),
        N("nt_remaining_apostles", "Apostles Philip, Bartholomew (Nathanael), Matthew (Levi), Thomas, Simon the Zealot, Judas Iscariot & Matthias", "biblical", 19, "1st c. CE (Matt 10:2-4; Acts 1:26)",
          "Complete College of the Twelve Apostles", ["Matthew 10:2-4", "Acts 1:13, 26", "Gervais UsefulChart NT"],
          "Completes the Twelve Apostles: Philip of Bethsaida, Bartholomew/Nathanael, Matthew/Levi (son of Alphaeus), Thomas Didymus (traditional Apostle to India!), Simon the Zealot, Judas Iscariot (son of Simon), and his replacement Matthias.",
          ["Philip", "Bartholomew", "Matthew Levi", "Thomas Didymus", "Simon the Zealot", "Judas Iscariot", "Matthias"]),
        N("nt_disciples_bethany", "Mary Magdalene, Joseph of Arimathea, Nicodemus, Lazarus/Martha/Mary, Mark, Luke & Timothy", "biblical", 19, "1st c. CE (Gospels; Acts; 2 Tim 1:5)",
          "Key New Testament Households & Early Church Chroniclers", ["Gospels", "Acts", "2 Timothy 1:5", "Gervais UsefulChart NT"],
          "Includes Mary Magdalene, Sanhedrin disciples Joseph of Arimathea & Nicodemus, Bethany siblings Lazarus/Martha/Mary, Barnabas & John Mark (cousins, Col 4:10), Luke the Physician, and Timothy (son of Eunice, grandson of Lois, 2 Tim 1:5).",
          ["Mary Magdalene", "Joseph of Arimathea", "Nicodemus", "Lazarus", "John Mark", "Timothy/Eunice/Lois"]),

        # -------------------------------------------------------------------------
        # 6. JOSEPHUS ANTIQUITIES BOOK I ETHNONYM SYNCHRONISMS
        # -------------------------------------------------------------------------
        N("jos_table_ethnonyms", "Josephus's Table of Nations Key (Gomer=Gauls, Magog=Scythians, Tubal=Iberians, Meshech=Cappadocians, Tiras=Thracians)", "biblical", 6, "93 CE (Josephus Antiquities I.6)",
          "Earliest Classical Greek-to-Genesis Ethnographic Key", ["Josephus Antiquities I.6 (pp. 66-68)"],
          "Flavius Josephus systematically mapped Genesis 10 into 1st-century Greco-Roman geography: Gomer=Galatians/Gauls, Magog=Scythians, Madai=Medes, Javan=Ionians/Greeks, Tubal=Iberes, Meshech=Cappadocians (Mazaca), Tiras=Thracians, Ashkenaz=Rheginians, Riphath=Paphlagonians, Togarmah=Phrygians, Elishah=Aeolians, Tarshish=Cilicia (Tarsus), Kittim=Cyprus (Kition).",
          ["Josephus Antiquities I.6"], major=False),
        # -------------------------------------------------------------------------
        # 7. SYRIAC CAVE OF TREASURES (Budge 1927): TWINS, 63 MATRIARCHS, YONTON, MELCHIZEDEK & MAGI
        # -------------------------------------------------------------------------
        N("syr_adam_twins_matriarchs", "Syriac Antediluvian Matriarchs: Lebhûdhâ (Cain's Twin/Wife), Ķelîmath/Aklia (Abel's Twin, Seth's Wife) & Haykêl bat Namûs (Noah's Wife)", "biblical", 2, "Antediluvian Syriac Tradition (Cave of Treasures pp. 69-100, 197-198)",
          "Complete Syriac Matriarchal Chain from Eve to Noah's Wife Haykêl", ["Syriac Cave of Treasures (Budge 1927 pp. 69-100, 197-198)"],
          "Names every matriarch across 10 antediluvian generations: Cain + twin Lebhûdhâ; Seth + Ķelîmath (Abel's twin); Enos + Ḥannâ; Cainan + Peryath; Mahalalel + Şeḥatpar; Jared + Zebhîdhâ; Enoch + Zadhkîn; Methuselah + Sâkhûth; Lamech + Kîpâr; Noah + Haykêl (daughter of Namûs)! Also names Terah's 2 wives: Yônâ (mother of Abraham) & Salmûth (mother of Sarah).",
          ["Lebhûdhâ", "Ķelîmath / Aklia", "Haykêl (Wife of Noah)", "Yônâ & Salmûth (Terah's Wives)"], major=True),
        N("syr_yonton_4th_son", "Yonton / Jonitus (Yônṭôn — 4th Son of Noah)", "biblical", 5, "Post-Flood East (Cave of Treasures pp. 122, 143-144; Bar Hebraeus)",
          "Post-Diluvian 4th Son of Noah & Origin of Eastern Wisdom", ["Cave of Treasures (Budge p. 143)", "Bar Hebraeus Chronography", "Apocalypse of Pseudo-Methodius"],
          "Born to Noah after the Flood and sent east to Yôkdôrâ of Nôdh by Lake Aṭrâs ('Land of the Rising Sun'). Nimrod journeyed east to Yonton (Jonitus) for 3 years and received the astronomical 'Revelation (Gelyânâ) of Nimrod' — the star-prophecy later followed by the Magi to Bethlehem!",
          ["Yonton", "Jonitus", "Jonithus", "Yônṭôn", "Yoniton"], major=True),
        N("syr_melchizedek_parents", "Syriac Melchizedek Lineage: Mâlâkh (son of Arphaxad/Cainan) & Yôzâdhâk → Melchizedek", "biblical", 8, "Post-Flood Salem (Cave of Treasures pp. 122-131, 152-153)",
          "Syriac Parentage of Melchizedek & Guardian of Adam's Body at Golgotha", ["Syriac Cave of Treasures (Budge 1927 pp. 126-130, 152)"],
          "Unlike rabbinic Shem=Melchizedek, the Syriac Cave of Treasures names Melchizedek's parents as Mâlâkh (brother of Salah, grandson of Arphaxad) and Yôzâdhâk (Book of the Bee variant: Harklêîm & Shêlâthîêl). Shem led 15-year-old Melchizedek to entomb Adam's body at Golgotha!",
          ["Mâlâkh & Yôzâdhâk", "Harklêîm & Shêlâthîêl"]),
        N("syr_twin_jacob_yonakhir", "Syriac Twin Fathers of Joseph & Mary: Matthan + Sebhrath → Twins Jacob (→ Joseph) & Yônâkhîr (+ Dînâ/Ḥannâ → Mary)", "biblical", 18, "1st c. BCE (Cave of Treasures pp. 194-195, 200-201)",
          "Syriac Harmonization Making Joseph & Virgin Mary First Cousins!", ["Syriac Cave of Treasures (Budge 1927 pp. 194-201)"],
          "Preserves EVERY post-exilic matriarch from Zerubbabel (+ Malkath bat Ezra!) through Abiud (+ Zakhyath bat Joshua) to Matthan (+ Sebhrath bat Phinehas), who bore TWINS Jacob (father of Joseph by Ḥadbhîth) and Yônâkhîr (father of Mary by Dînâ/Ḥannâ)!",
          ["Yônâkhîr & Dînâ/Ḥannâ", "Malkath bat Ezra", "Sebhrath"]),
        N("syr_magi_kings", "The Magi Kings of the East: Hôrmîzdâdh (Persia), Îzgarad (Sâbhâ) & Perôzadh (Sheba) + 12 Magi (Book of the Bee)", "biblical", 19, "1st c. CE (Cave of Treasures pp. 208-209; Book of the Bee Ch. 39)",
          "Persian & Sabaean Royal Astronomers Following Nimrod's Prophecy to Christ", ["Syriac Cave of Treasures (Budge 1927 pp. 208-209)", "Book of the Bee Ch. 39"],
          "Three kings: Hôrmîzdâdh of Mâkhôzdî (King of Kings of Persia), Îzgarad (Yazdegerd, King of Sâbhâ), and Perôzadh (King of Sheba). Book of the Bee expands to 12 named Magi with patronymics (Zarwândâd s/o Artabân, Gûshnâsâph s/o Gûndaphar [Indo-Parthian Gondophares!], Arshakh, Merôdâch, etc.)!",
          ["Hôrmîzdâdh", "Îzgarad", "Perôzadh", "Gûshnâsâph s/o Gûndaphar"]),
        # -------------------------------------------------------------------------
        # 8. DUTRIPON BIBLIORUM SACRORUM CONCORDANTIAE (pp. 22-23): COMPLETE HIGH PRIESTS TO 70 CE & EDOMITE BRIDGES
        # -------------------------------------------------------------------------
        N("dut_first_temple_priests", "First Temple High Priests (Dutripon p. 23, #4–34): Abishua → Bukki → Uzzi → Zadok → Ahimaaz → Jehoiada → Hilkiah → Seraiah", "biblical", 17, "c. 1450-586 BCE (Dutripon Concordantiae p. 23; 1 Chr 6)",
          "Complete Pre-Exilic High Priestly Succession from Aaron to the Babylonian Exile", ["Dutripon Bibliorum Sacrorum Concordantiae (p. 23)", "1 Chronicles 6:4-15", "Josephus Antiquities X.8"],
          "Dutripon's Tabula Pontificum apud Judaeos harmonizes Chronicles, Josephus & Eusebius across all 34 pre-exilic High Priests, including Jehoiada (who sheltered young King Joash from Queen Athaliah) and Hilkiah (who discovered the Book of the Law under King Josiah).",
          ["Bukki & Uzzi", "High Priest Jehoiada", "High Priest Hilkiah"]),
        N("dut_herodian_nt_priests", "Herodian & Roman-Era High Priests (Dutripon p. 23, #63–91): Ananelus → Simon ben Boethus → Annas (Ananus) → Joseph Caiaphas → Ananias ben Nebedeus → Ananus II → Phannias (70 CE)", "biblical", 19, "37 BCE – 70 CE (Dutripon Concordantiae p. 23; Gospels; Acts 23; Josephus Ant. XV-XX)",
          "Complete Final 29 High Priests of the Second Temple Down to the Fall of Jerusalem (70 CE)", ["Dutripon Bibliorum Sacrorum Concordantiae (p. 23)", "John 18:13", "Acts 23:2", "Josephus Antiquities XV-XX"],
          "Complete chronological table from Herod's appointee Ananelus & Simon ben Boethus (Herod's father-in-law) through Annas (Ananus) and son-in-law Joseph Caiaphas (Trial of Jesus), Annas's 5 High Priest sons (Eleazar, Jonathan, Theophilus, Matthias, Ananus II — who executed James the Just in 62 CE!), Ananias ben Nebedeus (Trial of Paul, Acts 23), down to Phannias/Phanacius, the VERY LAST High Priest chosen by lot during the 70 CE siege!",
          ["High Priest Annas (Ananus)", "High Priest Joseph Caiaphas", "Simon ben Boethus", "Ananias ben Nebedeus", "Phannias (Last High Priest, 70 CE)"], major=True),
        N("dut_esau_11_dukes_jobab", "11 Territorial Dukes of Esau (Timna, Alvah, Jetheth, Oholibamah, Elah, Pinon, Kenaz, Teman, Mibzar, Magdiel, Iram) & Jobab = Job Bridge", "biblical", 14, "Genesis 36:33, 40-43 (Dutripon Concordantiae p. 22)",
          "Final Edomite Chiefs & Septuagint/Vulgate Identification of King Jobab with Patriarch Job", ["Dutripon Bibliorum Sacrorum Concordantiae (p. 22)", "Genesis 36:33, 40-43", "Job 42:17 (LXX)"],
          "Dutripon's Series Principum Regumque Idumaeorum explicitly records the ancient Septuagint/Vulgate tradition ('Jobab iste est Job speculum patientiae') identifying Edomite King #2 Jobab ben Zerah of Bozrah with the Biblical Patriarch Job, followed by the 11 territorial Dukes of Edom.",
          ["King Jobab = Patriarch Job", "11 Dukes of Esau"]),
        N("dut_deuterocanon_lineages", "Deuterocanonical & Vulgate Households (Dutripon pp. 10-15): Tobit & Tobias (+ Sarah bat Raguel), Judith of Bethulia, Susanna, Eleazar & 7 Maccabean Martyrs, Ben Sira & Prophetesses Huldah & Anna", "biblical", 18, "c. 744 BCE – 1 CE (Dutripon Index Chronologicus pp. 10-15)",
          "Biblical & Intertestamental Families Preserved in the Latin Vulgate Chronology", ["Dutripon Concordantiae (pp. 10-11, 14-15)", "Books of Tobit, Judith, Sirach, 2 Maccabees", "Luke 2:36"],
          "Tobit (Tribe of Naphtali, exiled to Nineveh under Shalmaneser) -> Tobias (+ Sarah daughter of Raguel); Widow Judith of Bethulia (slew General Holofernes); Susanna (vindicated by Daniel); Eleazar & 7 Maccabean Martyrs (168 BCE); Jesus ben Sirach (Sirach/Ecclesiasticus, translated in Alexandria 131 BCE); Prophetess Huldah (Josiah's reign) & Prophetess Anna bat Phanuel (Tribe of Asher, Temple of Jerusalem!).",
          ["Tobit & Tobias", "Judith of Bethulia", "Susanna", "Eleazar & 7 Martyrs", "Jesus ben Sirach", "Prophetess Huldah & Anna"], major=True),
        N("dut_canaan_foes_kings", "Intersecting Ancient Near Eastern Kings in Dutripon's Sacred Chronology (pp. 9-14): Chedorlaomer of Elam, Sihon & Og of Bashan, Cushan-Rishathaim, Eglon of Moab, Jabin & Sisera, Zerah the Cushite & Tibni", "biblical", 15, "c. 1949-880 BCE (Dutripon pp. 9-14; Gen 14; Num 21; Judges 3-4; 2 Chr 14)",
          "Foreign Kings & Rivals Synchronized Across Dutripon's Six Ages of the World", ["Dutripon Concordantiae (pp. 9-14)", "Genesis 14", "Numbers 21", "Judges 3-4", "2 Chronicles 14:9"],
          "Key intersecting monarchs in Dutripon's Six Ages tables: Chedorlaomer of Elam (vs. Abraham, Gen 14), Amorite Kings Sihon & Og of Bashan (Num 21), Cushan-Rishathaim of Aram-Naharaim (vs. Othniel), Eglon of Moab (vs. Ehud), Jabin of Hazor & Sisera (vs. Deborah/Barak), Zerah the Cushite/Ethiopian (vs. King Asa, 2 Chr 14), and rival King Tibni of Israel (vs. Omri, 1 Kgs 16).",
          ["Chedorlaomer of Elam", "King Sihon & Og of Bashan", "Cushan-Rishathaim", "Zerah the Cushite", "King Tibni"]),
        N("dut_vulgate_ethnonyms_etymology", "Dutripon's Vulgate Ethnographic & Onomastic Key (pp. 9-15, 24-26): Nimrod=Belus, Asshur=Ninus, Armenia=Ararat, Carthago=Tarshish, India=Ophir/Hodu, Greece=Javan, Libya=Lubim & Patriarch Etymologies", "biblical", 6, "Vulgate Onomasticon & Six Ages (Dutripon pp. 9-15, 24-26)",
          "Classical Latin Vulgate Cross-Cultural Identifications & Hebrew/Chaldean/Greek Name Meanings", ["Dutripon Bibliorum Sacrorum Concordantiae (pp. 9-15, 24-26)"],
          "Documents traditional Latin Vulgate & Ussher synchronisms: Nimrod=Belus, Asshur=Ninus (+ Semiramis & Ninyas), Aegialeus of Sicyon & Inachus of Argos, Ogygian Flood (1796 BC), Cecrops & Cadmus, PLUS pp. 24-26 Name Interpretations: Aethiopia=Chus, Africa=Phut, Alexandria=No-Ammon, Armenia=Ararat, Cappadoces=Caphthorim, Carthago=Tharsis, Graeci=Jevanim, Heliopolis=On, India=Ophir/Hodu, Libya=Lubim, Cyrus=Sun; Adam ('red earth'), Eva ('living'), Noe ('rest'), Abraham ('father of multitude'), Moyses ('drawn from water'), David ('beloved'), Jesus ('Savior').",
          ["Nimrod = Belus", "Asshur = Ninus", "Carthago = Tarshish", "India = Ophir / Hodu", "Armenia = Ararat"]),
    ]

    edges += [
        # Dutripon Concordantiae edges
        E("tri_naphtali", "dut_deuterocanon_lineages", "direct", "Tobit & Tobias (Tribe of Naphtali, exiled to Nineveh — Dutripon p. 10)"),
        E("tri_asher", "dut_deuterocanon_lineages", "direct", "Prophetess Anna bat Phanuel (Tribe of Asher — Dutripon p. 11; Luke 2:36)"),
        E("has_mattathias", "dut_deuterocanon_lineages", "cognate", "Eleazar & 7 Maccabean Martyrs (168 BCE, Dutripon p. 11)"),
        E("bib_elam", "dut_canaan_foes_kings", "expansion", "Chedorlaomer King of Elam (Gen 14; Dutripon p. 9)"),
        E("bib_cush", "dut_canaan_foes_kings", "expansion", "Zerah the Cushite/Ethiopian (2 Chr 14:9; Dutripon p. 10)"),
        E("bib_nimrod", "dut_vulgate_ethnonyms_etymology", "syncretic", "Dutripon p. 9: 'Regnat Nemrod, vel Belus in Babylone' & 'Ninus vel Assur'"),
        E("bib_tarshish", "dut_vulgate_ethnonyms_etymology", "syncretic", "Dutripon p. 25 Vulgate Onomasticon: 'Carthago, Hebraice Tharsis'"),
        E("bib_ophir", "dut_vulgate_ethnonyms_etymology", "syncretic", "Dutripon p. 25 Vulgate Onomasticon: 'India, Hebraice Ophir; Indus, Hebraice Hodu'"),
        E("bib_caphtorim", "dut_vulgate_ethnonyms_etymology", "syncretic", "Dutripon p. 25 Vulgate Onomasticon: 'Cappadoces, Hebraice Caphthorim'"),
        E("pri_eleazar_zadok", "dut_first_temple_priests", "direct", "Complete First Temple High Priests #4-34 (Dutripon p. 23)"),
        E("dut_first_temple_priests", "pri_ezra_jaddua", "direct", "Hilkiah -> Seraiah -> Jehozadak -> Jeshua"),
        E("has_hyrcanus2_aristobulus2", "dut_herodian_nt_priests", "expansion", "Post-Hasmonean High Priests appointed under Herod & Rome (Dutripon p. 23, #63-91)"),
        E("her_herod_great_family", "dut_herodian_nt_priests", "direct", "Herod married Mariamne II, daughter of High Priest Simon ben Boethus (#66)"),
        E("dut_herodian_nt_priests", "nt_jesus", "cognate", "High Priests Annas (#72) & Joseph Caiaphas (#74) preside at Trial of Jesus"),
        E("dut_herodian_nt_priests", "nt_paul", "cognate", "High Priest Ananias ben Nebedeus presides at Trial of Apostle Paul (Acts 23:2)"),
        E("chr_edom_kings", "dut_esau_11_dukes_jobab", "direct", "8 Kings of Edom followed by 11 Territorial Dukes of Esau (Dutripon p. 22)"),
        E("dut_esau_11_dukes_jobab", "bib_job", "syncretic", "LXX Job 42:17 & Dutripon p. 22 equate Edomite King #2 Jobab ben Zerah with Patriarch Job!"),

        # Syriac Cave of Treasures edges
        E("bib_adam", "syr_adam_twins_matriarchs", "expansion", "Syriac Cave of Treasures: Adam & Eve's twin daughters Lebhûdhâ & Ķelîmath"),
        E("bib_noah", "syr_yonton_4th_son", "expansion", "4th son of Noah born after the Flood (Cave of Treasures p. 122)"),
        E("syr_yonton_4th_son", "bib_nimrod", "expansion", "Nimrod journeys east to Yônṭôn and receives Gelyânâ astronomy (p. 143)"),
        E("bib_arphaxad", "syr_melchizedek_parents", "expansion", "Mâlâkh (grandson of Arphaxad) & Yôzâdhâk -> Melchizedek (p. 152)"),
        E("syr_melchizedek_parents", "bib_melchizedek", "expansion", "Syriac parentage of Melchizedek"),
        E("nt_matthew_joseph", "syr_twin_jacob_yonakhir", "expansion", "Matthan + Sebhrath -> twin sons Jacob (Joseph) & Yônâkhîr (Mary)"),
        E("syr_twin_jacob_yonakhir", "nt_jesus", "expansion", "Syriac first-cousin harmonization of Joseph & Mary"),
        E("syr_yonton_4th_son", "syr_magi_kings", "expansion", "Magi follow the Revelation of Nimrod/Yônṭôn to Bethlehem (p. 205-209)"),
        E("syr_magi_kings", "nt_jesus", "direct", "Adoration of the Magi (Matt 2; Cave of Treasures pp. 208-209)"),

        # 1 Chronicles Tribal & Davidic edges
        E("jud_perez", "chr_hezron_ram", "direct", "Son Hezron -> 4 great Judahite clans (1 Chr 2:9-24)"),
        E("chr_hezron_ram", "jud_boaz_jesse", "direct", "Ram -> Amminadab -> Nahshon -> Salmon -> Boaz (1 Chr 2:10-15)"),
        E("chr_hezron_ram", "chr_hur_bezalel", "direct", "Caleb ben Hezron + Ephrath -> Hur -> Uri -> Bezalel (1 Chr 2:19-20)"),
        E("chr_elimelech_naomi", "jud_boaz_jesse", "direct", "Ruth (widow of Mahlon) marries Boaz -> Obed -> Jesse (Ruth 4)"),
        E("jud_boaz_jesse", "chr_jesse_nitzevet", "expansion", "Complete family of Jesse & Nitzevet (1 Chr 2:13-17; Talmud)"),
        E("chr_jesse_nitzevet", "jud_david", "direct", "Youngest son of Jesse & Nitzevet"),
        E("jud_david", "chr_david_wives_sons", "direct", "Complete 8 wives & 19+ named children of King David (1 Chr 3:1-9)"),
        E("chr_david_wives_sons", "jud_solomon", "direct", "Son by Bathsheba (Royal Line)"),
        E("chr_david_wives_sons", "nt_luke_mary", "direct", "Son Nathan (Luke 3:31 messianic line)"),
        E("tri_reuben_pallu", "chr_reuben_dathan", "direct", "Pallu -> Eliab -> Dathan & Abiram (Num 26:8-9)"),
        E("lev_aaron", "chr_levi_24_courses", "direct", "24 Priestly Divisions of Eleazar & Ithamar (1 Chr 24)"),
        E("chr_levi_24_courses", "has_mattathias", "direct", "1st Course of Jehoiarib -> Hasmonean Priests (1 Macc 2:1)"),
        E("chr_levi_24_courses", "nt_john_baptist", "direct", "8th Course of Abijah -> Zechariah & John the Baptist (Luke 1:5)"),
        E("jos_manasseh", "chr_manasseh_machir", "direct", "Manasseh -> Machir -> Gilead -> Hepher -> Zelophehad (Num 26:29)"),
        E("chr_manasseh_machir", "bib_zelophehad_bezalel", "direct", "Hepher -> Zelophehad -> 5 Daughters (Num 27:1)"),
        E("jos_ephraim", "chr_ephraim_joshua", "direct", "Ephraim -> Beriah -> Elishama -> Nun -> Joshua (1 Chr 7:20-27)"),
        E("chr_ephraim_joshua", "bib_joshua_caleb", "direct", "Nun -> Joshua son of Nun"),
        E("bib_saul", "chr_saul_ner_abner", "direct", "Abiel -> Kish (Saul) & Ner (General Abner) (1 Chr 8:33)"),
        E("kg_i1_jeroboam", "chr_jeroboam_ano", "expansion", "Septuagint marriage to Egyptian Princess Ano (3 Kgdms 12:24e)"),
        E("eg_shoshenq1", "chr_jeroboam_ano", "expansion", "Pharaoh Shishak gives sister-in-law Ano to Jeroboam (LXX)"),
        E("bib_esau", "chr_edom_kings", "direct", "Pre-monarchic elective Kings of Edom (Gen 36:31-39)"),

        # Second Temple High Priests, Hasmoneans, Herodians & NT
        E("pri_ezra_jaddua", "pri_jeshua_eliashib", "direct", "Post-exilic Zadokite High Priest succession (Neh 12; Josephus Ant. XI)"),
        E("pri_jeshua_eliashib", "pri_onias_dynasty", "direct", "Jaddua -> Onias I -> Simon the Just -> Onias III & IV (Josephus Ant. XII)"),
        E("pri_jeshua_eliashib", "grk_alexander", "cognate", "High Priest Jaddua meets Alexander the Great in 332 BCE (Josephus Ant. XI.8)"),
        E("has_mattathias", "has_judas_maccabeus", "direct", "Sons of Mattathias (1 Macc 2:2-5)"),
        E("has_mattathias", "has_simon_hyrcanus1", "direct", "Son Simon Thassi -> John Hyrcanus I"),
        E("has_simon_hyrcanus1", "has_jannaeus_salome", "direct", "Sons Aristobulus I & Alexander Jannaeus (+ Salome Alexandra)"),
        E("has_jannaeus_salome", "has_hyrcanus2_aristobulus2", "direct", "Sons Hyrcanus II & Aristobulus II -> Mariamne I"),
        E("bib_esau", "her_antipater_cypros", "expansion", "Idumean/Edomite descent of the Herodians (Josephus Ant. XIV)"),
        E("her_antipater_cypros", "her_herod_great_family", "direct", "Antipater & Cypros -> Herod I the Great"),
        E("has_hyrcanus2_aristobulus2", "her_herod_great_family", "direct", "Hasmonean Princess Mariamne I marries Herod the Great"),
        E("her_herod_great_family", "nt_herodians", "direct", "Consolidation into NT Herodian rulers"),
        E("her_herod_great_family", "her_agrippa_herodias", "direct", "Aristobulus IV + Berenice -> Herod Agrippa I & Herodias"),
        E("nt_luke_mary", "nt_joachim_anne", "expansion", "Heli / Joachim & Anne -> Virgin Mary (Luke 3; Protoevangelium)"),
        E("nt_joachim_anne", "nt_jesus", "direct", "Maternal grandparents of Jesus"),
        E("nt_joachim_anne", "nt_john_baptist", "expansion", "Anne's sister Sobe -> Elizabeth -> John the Baptist (Traditional)"),
        E("nt_matthew_joseph", "nt_mary_clopas_alphaeus", "expansion", "Clopas, brother of Joseph of Nazareth (Hegesippus/Eusebius)"),
        E("nt_jesus", "nt_zebedee_salome", "direct", "Inner-circle Apostles James the Great & John (Mark 3:17)"),
        E("nt_jesus", "nt_jonah_peter_andrew", "direct", "Apostles Simon Peter & Andrew (Matt 4:18)"),
        E("nt_jesus", "nt_mary_clopas_alphaeus", "direct", "Apostles James the Lesser & Jude Thaddeus"),
        E("nt_jesus", "nt_remaining_apostles", "direct", "Remaining Apostles of the Twelve (Matt 10:2-4)"),
        E("nt_jesus", "nt_disciples_bethany", "direct", "Close disciples, Bethany household & early chroniclers"),

        # Josephus Table of Nations bridge
        E("bib_japheth", "jos_table_ethnonyms", "cognate", "Josephus Antiquities I.6 Greco-Roman ethnographic identifications"),
    ]

    # Exhaustive individual-level rosters for David's sons, Hasmoneans, Herodians, Oniad High Priests, Apostles & Syriac Matriarchs
    add_roster(nodes, edges, "chr_david_wives_sons", "bib16_dav", "biblical", 16, "c. 1010-970 BCE (1 Chr 3:1-9)", "Child / Wife of King David", ["1 Chronicles 3:1-9", "Gervais UsefulChart Exodus"], [
        "Amnon (Firstborn of David by Ahinoam)", "Chileab / Daniel (Son by Abigail)", "Absalom (Son by Maacah of Geshur)",
        "Princess Tamar (Daughter of David & Maacah)", "Adonijah (Son by Haggith)", "Shephatiah (Son by Abital)",
        "Ithream (Son by Eglah)", "Shammua (Son by Bathsheba)", "Shobab (Son by Bathsheba)", "Nathan ben David (Son by Bathsheba — Luke 3)",
        "Ibhar, Elishua & Eliphelet (Jerusalem Sons)", "Nogah, Nepheg & Japhia (Jerusalem Sons)", "Elishama, Eliada & Jerimoth (Jerusalem Sons)"
    ], edge_type="direct", edge_label="Child of King David (1 Chr 3)")

    add_roster(nodes, edges, "pri_onias_dynasty", "bib16_pri", "biblical", 18, "c. 538-145 BCE (Neh 12; Josephus)", "Second Temple High Priest", ["Josephus Antiquities XI-XII", "Gervais UsefulChart NT"], [
        "High Priest Jeshua ben Jehozadak", "High Priest Joiakim", "High Priest Eliashib", "High Priest Joiada",
        "High Priest Johanan", "High Priest Jaddua (Met Alexander 332 BCE)", "High Priest Onias I", "High Priest Simon I the Just",
        "High Priest Eleazar (Septuagint Translator Sponsor)", "High Priest Onias II", "High Priest Simon II",
        "High Priest Onias III", "High Priest Jason (Hellenizer)", "High Priest Onias IV (Built Leontopolis Temple in Egypt)"
    ], edge_type="direct", edge_label="Second Temple Zadokite High Priest")

    add_roster(nodes, edges, "has_jannaeus_salome", "bib16_has", "biblical", 18, "167-37 BCE (1-2 Maccabees; Josephus)", "Maccabean / Hasmonean Leader", ["1-2 Maccabees", "Josephus Antiquities XII-XV"], [
        "John Gaddi (Son of Mattathias)", "Eleazar Avaran (Son of Mattathias)", "Jonathan Apphus (1st Hasmonean High Priest)",
        "Simon Thassi (Ethnarch & High Priest)", "John Hyrcanus I (134-104 BCE)", "King Aristobulus I (104-103 BCE)",
        "King Alexander Jannaeus (103-76 BCE)", "Queen Salome Alexandra (76-67 BCE)", "Hyrcanus II (High Priest & Ethnarch)",
        "King Aristobulus II", "Alexander II of Judea", "King Antigonus II Mattathias (Last Hasmonean King)",
        "Queen Mariamne I (Wife of Herod the Great)", "High Priest Aristobulus III"
    ], edge_type="direct", edge_label="Hasmonean / Maccabean Dynasty")

    add_roster(nodes, edges, "her_herod_great_family", "bib16_her", "biblical", 18, "47 BCE – 93 CE (Josephus Ant. XIV-XX)", "Herodian Royal Family Member", ["Josephus Antiquities XIV-XX", "New Testament", "Gervais UsefulChart NT"], [
        "Phasael I (Brother of Herod)", "Salome I (Sister of Herod + Costobarus)", "Antipater II (Son of Herod & Doris)",
        "Prince Alexander (+ Glaphyra of Cappadocia)", "Prince Aristobulus IV (+ Berenice)", "Herod II Philip (Son by Mariamne II)",
        "Ethnarch Herod Archelaus", "Tetrarch Herod Antipas (+ Phasaelis & Herodias)", "Tetrarch Philip II (+ Salome)",
        "King Herod Agrippa I (Acts 12)", "King Herod of Chalcis", "Princess Herodias & Salome",
        "King Herod Agrippa II (Acts 25-26)", "Queen Berenice II & Drusilla (+ Felix)"
    ], edge_type="direct", edge_label="Herodian Dynasty Member")

    add_roster(nodes, edges, "nt_remaining_apostles", "bib16_apo", "biblical", 19, "1st c. CE (New Testament)", "Apostle / New Testament Figure", ["Gospels & Acts", "Gervais UsefulChart NT"], [
        "Apostle Simon Peter (Cephas)", "Apostle Andrew (Brother of Peter)", "Apostle James the Great (Son of Zebedee)",
        "Apostle John the Evangelist (Son of Zebedee)", "Apostle Philip of Bethsaida", "Apostle Bartholomew (Nathanael)",
        "Apostle Matthew (Levi)", "Apostle Thomas Didymus", "Apostle James the Lesser (Son of Alphaeus)",
        "Apostle Jude Thaddeus", "Apostle Simon the Zealot", "Judas Iscariot", "Apostle Matthias",
        "James the Just (Bishop of Jerusalem)", "Jude (Author of Epistle of Jude)", "Mary Magdalene",
        "Joseph of Arimathea & Nicodemus", "Lazarus, Martha & Mary of Bethany", "Barnabas & John Mark", "Luke the Evangelist", "Timothy (+ Eunice & Lois)"
    ], edge_type="direct", edge_label="New Testament Apostle / Household")

    add_roster(nodes, edges, "dut_herodian_nt_priests", "bib16_dutp", "biblical", 19, "37 BCE – 70 CE (Dutripon p. 23)", "Herodian / Roman-Era High Priest", ["Dutripon Bibliorum Sacrorum Concordantiae (p. 23)", "Josephus Antiquities XV-XX"], [
        "Menelaus & Lysimachus (Seleucid High Priests, #50)", "Alcimus (Pseudopontifex, #53)", "Ananelus (Herod's First Appointee, #63)",
        "Jesus ben Phabet (#65)", "Simon ben Boethus (Father of Mariamne II, #66)", "Matthias & Joazar (#67-68)",
        "Eleazar ben Boethus (#69)", "Jesus ben Sie (#70)", "Ananus / High Priest Annas (#72, 6-15 CE)",
        "Ishmael ben Fabus (#73)", "Eleazar ben Ananus (#74)", "Simon ben Camithus", "Joseph Caiaphas (18-36 CE, Trial of Jesus)",
        "Jonathan ben Ananus", "Simon Cantheras", "Matthias ben Ananus", "Elioneus", "Joseph ben Camydus",
        "Ananias ben Nebedeus (Trial of Paul, Acts 23)", "Ananus ben Ananus (Executed James the Just, 62 CE)",
        "Jesus ben Damneus & Jesus ben Gamaliel", "Matthias ben Theophilus", "Phannias / Phanacius (Last High Priest of Second Temple, 70 CE)"
    ], edge_type="direct", edge_label="Second Temple High Priest (Dutripon p. 23)")

    add_roster(nodes, edges, "dut_deuterocanon_lineages", "bib16_deut", "biblical", 18, "Dutripon pp. 10-15 (Vulgate)", "Deuterocanonical / Intertestamental Figure", ["Dutripon Concordantiae (pp. 10-15)"], [
        "Tobit & Tobias (+ Sarah bat Raguel, Book of Tobit)", "Judith of Bethulia (Book of Judith)", "General Holofernes (Assyrian/Babylonian Commander)",
        "Susanna (Vindicated by Daniel, Dan 13)", "Eleazar & the Seven Maccabean Martyrs (2 Macc 6-7)",
        "Jesus ben Sirach / Ben Sira (Author of Ecclesiasticus, 131 BCE)", "Dositheus (Purim Letter to Egypt)",
        "Prophetess Huldah (Reign of King Josiah, 2 Kgs 22)", "Prophetess Anna bat Phanuel (Tribe of Asher, Luke 2:36)"
    ], edge_type="expansion", edge_label="Vulgate Chronology Figure (Dutripon pp. 10-15)")

    add_roster(nodes, edges, "dut_canaan_foes_kings", "bib16_foes", "biblical", 15, "Dutripon pp. 9-14", "Intersecting Ancient Near Eastern Monarch", ["Dutripon Concordantiae (pp. 9-14)"], [
        "Chedorlaomer, King of Elam (Gen 14)", "King Sihon of the Amorites (Num 21)", "King Og of Bashan (Rephaim, Num 21)",
        "King Cushan-Rishathaim of Mesopotamia (Judges 3)", "King Eglon of Moab (Judges 3)", "King Jabin of Hazor & General Sisera (Judges 4)",
        "Zerah the Cushite / Ethiopian (2 Chr 14:9)", "King Tibni of Israel (Rival of Omri, 1 Kgs 16:21)"
    ], edge_type="expansion", edge_label="Intersecting Monarch (Dutripon pp. 9-14)")

    return {
        "module": "16_biblical_syriac_hasmonean_nt",
        "title": "Exhaustive 1 Chronicles Tribal Lineages, Second Temple High Priests, Hasmoneans, Herodians, Complete NT Apostles & Josephus (Sources: UsefulCharts, 1975 FamilyTree, Bennett 1967, Josephus)",
        "nodes": nodes,
        "edges": edges,
    }
