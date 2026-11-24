"""
Module 18: Complete 31 Dynasties of Ancient Egypt, Manetho's Gods/Demigods/Spirits of the Dead,
Palermo Stone Predynastic Kings, Theban Priest-Kings, Pasenhor Libyan Genealogy,
Complete Ptolemaic Dynasty, and Complete Napatan & Meroitic Kings of Nubia/Kush.

Sources mined from sources/:
- manethowithengli00maneuoft.pdf (Manetho's Aegyptiaca, Loeb Classical Library, Waddell 1940)
- Ancient Records Of Egypt Vol-1.pdf (J.H. Breasted, Palermo Stone & Dynasties I-XVII)
- King list 1-6.pdf (Sjef Willockx 2006, Dynasties I-VI critical synchronization)
- The book of the kings of Egypt.pdf (E.A. Wallis Budge Vol. II, Dynasties XX-XXX, Ptolemies & Napata/Meroe)
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # -------------------------------------------------------------------------
    # 1. MANETHO'S PREDYNASTIC GODS, DEMIGODS, SHEMSU-HOR & PALERMO STONE KINGS
    # -------------------------------------------------------------------------
    nodes += [
        N("eg_manetho_demigods", "Manetho's Pre-Dynastic Rulers: Gods (Ptah→Re→Shu→Geb→Osiris→Seth→Horus), Demigods & Shemsu-Hor ('Spirits of the Dead')", "levant_egypt", 3, "Predynastic Mythic Era (Manetho Fr. 1-4, Loeb pp. 3-19)",
          "24,900 Lunar Years of Divine & Demigod Kingship Before Menes", ["Manetho Aegyptiaca Fr. 1-4 (Loeb)", "Turin Royal Canon"],
          "Manetho's opening sequence: 6 Great Gods (Hephaestus/Ptah -> son Helios/Re -> Agathodaemon/Shu -> Cronos/Geb -> Osiris & Isis -> Typhon/Seth), 9 Demigods (Horus, Ares/Anhur, Anubis, Heracles/Khonsu, Apollo, Ammon, Tithoes, Sosus, Zeus), down to Bydis/Bites and the Shemsu-Hor ('Followers of Horus / Spirits of the Dead').",
          ["Shemsu-Hor", "Bydis/Bites", "Manetho Divine Dynasties"], major=True),
        N("eg_palermo_predynastic", "Palermo Stone Predynastic Kings of Lower Egypt (Seka, Khayu, Tiu, Thesh, Neheb, Wazner, Mekh) & King Scorpion", "levant_egypt", 5, "c. 3200-3000 BCE (Breasted Vol. I §90, p. 57)",
          "Earliest Historically Inscribed Rulers of the Nile Before Narmer", ["Palermo Stone (Breasted Vol. I p. 57)", "Dynasty 0 Inscriptions"],
          "Row 1 of the 5th-Dynasty Palermo Stone preserves actual names of Pre-Unification Red Crown Kings of Lower Egypt: Seka, Khayu, Teyew/Tiu, Thesh, Neheb, Wazenez/Wazner, and Mekh — alongside Upper Egyptian Dynasty 0 rulers Iry-Hor, Ka, and King Scorpion.",
          ["Seka", "Khayu", "Tiu", "Thesh", "Neheb", "Wazner", "Mekh", "King Scorpion"]),
    ]

    # -------------------------------------------------------------------------
    # 2. COMPLETE DYNASTIES I–VI (Willockx King List 1-6 + Manetho Loeb)
    # -------------------------------------------------------------------------
    dyn1_6 = [
        ("eg_dyn1_complete", "Dynasty I Complete (Thinite, 8 Kings): Narmer/Menes → Hor-Aha (Athothis) → Djer (Kenkenes) → Djet (Uenephes) → Queen Merneith → Den (Usaphais) → Adjib (Miebis) → Semerkhet (Semempses) → Qa'a (Bieneches)", 6, "c. 2982-2803 BCE (Willockx pp. 7-8; Manetho Fr. 6-7)", "Complete Unification Dynasty (Africanus Makes Every King Son of His Predecessor)", "179 historical years (Manetho: 253 yrs). Queen Merneith ruled as regent/mother of Den. Every Abydos royal tomb and Horus-name matched with Manetho's Greek names.", {"altNames": ["Djer / Kenkenes", "Djet / Uenephes", "Queen Merneith", "Adjib / Miebis", "Semerkhet / Semempses"]}),
        ("eg_dyn2_complete", "Dynasty II Complete (9 Kings): Hotepsekhemwy (Boethos) → Nebre (Kaiechos) → Nynetjer (Binothris) → Weneg (Tlas) → Sened (Sethenes) → Sneferka → Sekhemib → Seth-Peribsen (Sesochris) → Khasekhemwy (Cheneres)", 6, "c. 2803-2657 BCE (Willockx pp. 9-10; Manetho Fr. 8-10)", "Consolidation of Memphis & Horus/Seth Reconciliation", "Manetho notes under Nynetjer (Binothris) it was decreed that women could hold the royal dignity; Peribsen took a Seth-name before Khasekhemwy united both Horus and Seth above his serekh!", {"altNames": ["Hotepsekhemwy", "Nebre", "Nynetjer / Binothris", "Seth-Peribsen"]}),
        ("eg_dyn3_complete", "Dynasty III Complete (Memphite, 5 Kings): Sanakht (Necherophes) → Netjerykhet/Djoser (Tosorthros + Imhotep) → Sekhemkhet (Tyris) → Khaba → Huni (Kerpheres)", 7, "c. 2657-2589 BCE (Willockx p. 11; Manetho Fr. 11-12)", "Dawn of Stone Pyramid Architecture (Saqqara Step Pyramid)", "Djoser & architect Imhotep (Greek: Imuthes/Asclepius) built the first monumental stone pyramid; Huni inaugurated the royal cartouche.", {"altNames": ["Sanakht", "Sekhemkhet", "Khaba", "Huni"]}),
        ("eg_dyn4_complete", "Dynasty IV Complete (Pyramid Builders, 7 Kings): Sneferu (Soris) → Khufu (Suphis I) → Djedefre (Ratoises) → Khafre (Suphis II) → Baka (Bicheris) → Menkaure (Mencheres) → Shepseskaf (Sebercheres) & Queen Khentkawes", 7, "c. 2589-2454 BCE (Willockx p. 12; Manetho Fr. 14-16)", "Complete Great Pyramid Dynasty of Dahshur & Giza", "Sneferu built 3 giant pyramids; sons/grandsons Khufu, Djedefre, Khafre, and Menkaure erected Giza; Menkaure's daughter Queen Khentkawes bridged Dynasties IV and V!", {"altNames": ["Djedefre / Ratoises", "Baka / Bicheris", "Shepseskaf", "Queen Khentkawes"]}),
        ("eg_dyn5_complete", "Dynasty V Complete (Solar Kings, 9 Kings): Userkaf (Usercheres) → Sahure (Sephres) → Neferirkare Kakai → Shepseskare → Neferefre → Nyuserre Ini → Menkauhor → Djedkare Isesi → Unas (Onnus, Pyramid Texts!)", 8, "c. 2454-2297 BCE (Willockx pp. 13-14; Manetho Fr. 18)", "Sun Temple Builders & Oldest Religious Texts (Pyramid Texts of Unas)", "Userkaf's era compiled the Palermo Stone Annals; Unas inscribed the oldest corpus of sacred funerary liturgy in human history (Pyramid Texts) inside his Saqqara pyramid.", {"altNames": ["Userkaf", "Sahure", "Neferirkare", "Nyuserre", "Djedkare Isesi", "Unas"]}),
        ("eg_dyn6_complete", "Dynasty VI Complete (6-7 Kings): Teti (Othoes) → Userkare → Pepi I (Phius) → Merenre I → Pepi II (Phiops, 94-yr reign!) → Merenre II → Queen Nitocris (Neith-iqerty)", 8, "c. 2297-2168 BCE (Willockx pp. 15-16; Manetho Fr. 20-21)", "Longest Reign in History (Pepi II) & End of the Old Kingdom", "Pepi II ascended at age 6 and ruled into his 90s (Manetho: 94 yrs!). Manetho & Herodotus name Queen Nitocris ('bravest and most beautiful woman of her time') closing the Old Kingdom.", {"major": True, "altNames": ["Teti", "Pepi I", "Pepi II / Phiops", "Queen Nitocris"]}),
    ]
    add_chain(nodes, edges, dyn1_6, start_parent="eg_menes", start_edge_type="direct",
              start_edge_label="Complete Dynasties I–VI Critical Sequence (Willockx & Manetho)",
              tradition="levant_egypt", default_edge_type="direct", default_sources=["Manetho Aegyptiaca (Loeb)", "Willockx King List 1-6"])

    # -------------------------------------------------------------------------
    # 3. FIRST INTERMEDIATE, MIDDLE KINGDOM & HYKSOS (DYNASTIES VII–XVII)
    # -------------------------------------------------------------------------
    dyn7_17 = [
        ("eg_dyn7_10_fip", "First Intermediate Period (Dynasties VII–X): Memphite Ephemerals (Neferkare Pepyseneb) & Heracleopolitan Kings (Khety / Achthoes I–III, Merikare)", 9, "c. 2168-2040 BCE (Manetho Fr. 23-30; Breasted Vol. I)", "Fragmented Rival Houses of Memphis & Heracleopolis", "Manetho's famous '70 kings in 70 days' (Dyn. VII) and Khety/Achthoes of Heracleopolis (Dyn. IX-X, author of 'Teaching for King Merikare').", {"altNames": ["Achthoes / Khety", "Merikare"]}),
        ("eg_dyn11_complete", "Dynasty XI Complete (Theban Reunifiers): Intef I → Intef II → Mentuhotep I → Intef III → Mentuhotep II (Reunified Egypt!) → Mentuhotep III → Mentuhotep IV", 10, "c. 2160-2000 BCE (Breasted Vol. I §63; Manetho Fr. 31-32)", "Theban Unifiers of the Middle Kingdom", "Mentuhotep II defeated Heracleopolis, reunited Upper & Lower Egypt, and built the terraced mortuary temple at Deir el-Bahari.", {"altNames": ["Intef I–III", "Mentuhotep III & IV"]}),
        ("eg_dyn12_complete", "Dynasty XII Complete (Golden Age of Middle Kingdom): Amenemhat I → Senusret I (Sesonchosis) → Amenemhat II → Senusret II → Senusret III (Sesostris) → Amenemhat III (Lamares, Labyrinth!) → Amenemhat IV → Queen Sobekneferu (Scemiophris)", 11, "2000-1788 BCE (Breasted Vol. I §64; Manetho Fr. 34-36)", "Classical Peak of Egyptian Literature, Faiyum Irrigation & Nubian Fortresses", "Manetho preserves direct parent-child links: Amenemhat I -> son Senusret I -> Amenemhat II -> Senusret II -> Senusret III -> son Amenemhat III (built the Great Labyrinth at Hawara) -> Amenemhat IV -> sister Queen Sobekneferu (first fully attested female Pharaoh!).", {"major": True, "altNames": ["Amenemhat I", "Senusret I", "Amenemhat II", "Queen Sobekneferu / Scemiophris"]}),
        ("eg_dyn13_14_sip", "Dynasties XIII (60 Theban Kings: Sobekhotep IV / Chenephres, Dedumose / Tutimaeus) & XIV (76 Xoite Kings of the Eastern Delta)", 12, "c. 1788-1650 BCE (Manetho Fr. 38-42; Artapanus)", "Second Intermediate Period Fragmentation & Asiatic Delta Settlers", "Waddell notes Sobekhotep IV = Chenephres (in Artapanus's Moses account!) and Dedumose = Tutimaeus ('in whose reign a blast of God smote us' and the Hyksos entered Egypt!).", {"altNames": ["Sobekhotep IV / Chenephres", "Dedumose / Tutimaeus"]}),
        ("eg_dyn15_17_hyksos_thebes", "Dynasties XV–XVII: Great Hyksos Kings (Salitis, Bnon, Apachnan, Khyan/Iannas, Apophis/Apepi, Khamudi/Assis) vs. Theban Liberators (Seqenenre Tao & Kamose)", 13, "c. 1650-1550 BCE (Manetho Fr. 42-49 via Josephus Against Apion)", "Semitic Shepherd Kings of Avaris & War of Liberation", "Josephus (quoting Manetho verbatim!) preserved the 6 Great Hyksos rulers of Avaris (Salitis, Bnon, Apachnan, Apophis [traditional Pharaoh of Joseph in Syncellus!], Khyan, Assis) until Theban Seqenenre Tao & son Kamose launched the liberation finished by Ahmose I.", {"altNames": ["Salitis", "Khyan / Iannas", "Apophis / Apepi", "Kamose"]}),
    ]
    add_chain(nodes, edges, dyn7_17, start_parent="eg_dyn6_complete", start_edge_type="expansion",
              start_edge_label="First Intermediate, Middle Kingdom & Hyksos Era (Dynasties VII–XVII)",
              tradition="levant_egypt", default_edge_type="expansion", default_sources=["Manetho Aegyptiaca (Loeb)", "Breasted Ancient Records Vol. I"])

    # -------------------------------------------------------------------------
    # 4. COMPLETE NEW KINGDOM (DYNASTIES XVIII–XX: Manetho, Breasted, Budge)
    # -------------------------------------------------------------------------
    dyn18_20 = [
        ("eg_dyn18_early", "Dynasty XVIII Early–Mid: Ahmose I → Amenhotep I → Thutmose I → Thutmose II & Queen Hatshepsut (Amessis) → Thutmose III → Amenhotep II → Thutmose IV", 14, "1550-1391 BCE (Manetho Fr. 50-53; Breasted Vol. I)", "Imperial Expansion to the Euphrates & Sole Female Pharaoh Hatshepsut", "Hatshepsut (Manetho's Amessis) sent the famous trade expedition to Punt; Thutmose III (Battle of Megiddo) expanded Egypt to its greatest extent; Thutmose IV erected the Dream Stele between the Sphinx's paws.", {"altNames": ["Amenhotep I", "Thutmose II", "Queen Hatshepsut", "Amenhotep II", "Thutmose IV"]}),
        ("eg_dyn18_amarna_end", "Dynasty XVIII Late (Amarna & Post-Amarna): Amenhotep III (+ Queen Tiye) → Akhenaten (+ Nefertiti) → Smenkhkare → Tutankhamun → Ay → Horemheb (Harmais = Danaus!)", 15, "1391-1292 BCE (Manetho Fr. 50-53; Amarna Letters)", "Monotheistic Amarna Revolution & Greco-Egyptian Danaus/Aegyptus Bridge", "Manetho explicitly equates General/Pharaoh Horemheb ('Harmais') with Greek Danaus and Ramesses/Seti with his brother Aegyptus — linking Greek Argive genealogy directly into Egypt's 18th/19th Dynasty transition!", {"altNames": ["Queen Tiye", "Nefertiti", "Smenkhkare", "Pharaoh Ay", "Horemheb / Harmais"]}),
        ("eg_dyn19_complete", "Dynasty XIX Complete: Ramesses I → Seti I (Sethos) → Ramesses II (Rapsaces, 67 yrs) → Merneptah (Israel Stele) → Amenmesse → Seti II & Siptah → Queen Twosret (Thuoris — Fall of Troy!)", 15, "1292-1189 BCE (Manetho Fr. 55-56; Breasted Vol. I)", "Ramesside Empire & Manetho's Synchronism with the Trojan War", "Manetho notes under Queen Twosret ('Thuoris', identified with Homer's Polybus & Alcandra) Troy was taken — synchronizing Egypt's 19th Dynasty directly with the Bronze Age Collapse & Trojan War!", {"altNames": ["Ramesses I", "Seti I", "Amenmesse", "Seti II", "Siptah", "Queen Twosret / Thuoris"]}),
        ("eg_dyn20_complete", "Dynasty XX Complete (10 Ramessides): Setnakhte → Ramesses III (Medinet Habu, Sea Peoples!) → Ramesses IV → V → VI → VII → VIII → IX → X → Ramesses XI", 16, "1189-1077 BCE (Budge Book of Kings Vol. II pp. 1-20; Manetho Fr. 57)", "Defense Against the Sea Peoples & End of the New Kingdom", "Budge Vol. II lists all 10 sons of Ramesses III from Medinet Habu (incl. Ramesses IV, VI, VIII) and the complete Ramesside succession down to Ramesses XI, when High Priest Herihor seized Upper Egypt.", {"altNames": ["Setnakhte", "Ramesses IV–XI"]}),
    ]
    add_chain(nodes, edges, dyn18_20, start_parent="eg_dyn15_17_hyksos_thebes", start_edge_type="direct",
              start_edge_label="New Kingdom Imperial Dynasties (XVIII–XX)",
              tradition="levant_egypt", default_edge_type="direct", default_sources=["Manetho Aegyptiaca (Loeb)", "Budge Book of the Kings of Egypt Vol. II"])

    # -------------------------------------------------------------------------
    # 5. COMPLETE THIRD INTERMEDIATE, LATE PERIOD, PTOLEMIES & NUBIA (DYNASTIES XXI–XXXI + NAPATA/MEROE)
    # -------------------------------------------------------------------------
    dyn21_31 = [
        ("eg_dyn21_tanite_theban", "Dynasty XXI (Divided Egypt): Tanite Kings (Smendes, Psusennes I [Silver Pharaoh!], Amenemope, Osochor, Siamun, Psusennes II) & Theban Priest-Kings (Herihor → Piankh → Pinudjem I → Menkheperre → Pinudjem II)", 16, "1077-943 BCE (Budge Vol. II pp. 20-34; Manetho Fr. 58-59)", "Biblical Era of David & Solomon (Siamun & Psusennes II)", "Psusennes I's intact silver sarcophagus was found at Tanis; Siamun campaigned in Philistia/Gezer (often identified as the Pharaoh whose daughter married King Solomon, 1 Kgs 3:1, 9:16!); Psusennes II's daughters Karamat & Maatkare married into the Libyan 22nd Dynasty!", {"major": True, "altNames": ["Herihor", "Pinudjem I & II", "Smendes", "Psusennes I", "Siamun", "Psusennes II"]}),
        ("eg_dyn22_libyan_pasenhor", "Dynasty XXII Complete (Libyan/Bubastite — Stele of Pasenhor): Buiu-uaua → Shoshenq I (Shishak!) → Osorkon I → Takelot I → Osorkon II → Shoshenq II → Takelot II → Shoshenq III → Pami → Shoshenq V", 17, "943-716 BCE (Budge Vol. II pp. 35-60; Manetho Fr. 60-61)", "Complete 15-Generation Meshwesh Libyan Genealogy & Shishak's Sack of Jerusalem", "The famous Serapeum Stele of Pasenhor (Budge pp. 35-39) traces Shoshenq I back 6 generations to Libyan chief Buyuwawa and forward through Osorkon II! Shoshenq I (= Biblical Shishak, 1 Kgs 14:25) invaded Rehoboam's Judah in 925 BCE.", {"altNames": ["Buyuwawa (Stele of Pasenhor)", "Osorkon I & II", "Takelot I & II", "Shoshenq III & V"]}),
        ("eg_dyn23_24_saite", "Dynasties XXIII (Pedubast I, Osorkon III, Takelot III, Rudamun) & XXIV (Tefnakht I → Bakenranef / Bocchoris)", 17, "818-715 BCE (Budge Vol. II pp. 60-69; Manetho Fr. 62-65)", "Libyan Delta Coalitions Resisting Kushite Reunification", "Tefnakht of Sais led the Delta coalition against Kushite King Piye (Piankhi Stele); his son Bakenranef (Greek: Bocchoris, famous lawgiver) was defeated by Kushite Shabaka.", {"altNames": ["Pedubast I", "Osorkon III", "Tefnakht I", "Bocchoris / Bakenranef"]}),
        ("eg_dyn25_kush_budge", "Dynasty XXV Complete (Kushite Pharaohs): Kashta (+ Pebatjma) → Piye & Shabaka (Sabacon) → Shabataka (Sebichos) → Taharqa (Tirhakah) → Tantamani (Ammeris)", 17, "744-656 BCE (Budge Vol. II pp. 70-78, 195-199; Manetho Fr. 66-67)", "Nubian Reunifiers of Egypt & Biblical Allies of Hezekiah", "Budge details the entire royal family including God's Wives of Amun Amenirdis I & Shepenupet II, linking Kushite bloodlines into Dynasty XXVI!", {"altNames": ["Shabaka / Sabacon", "Shabataka / Sebichos", "Amenirdis I"]}),
        ("eg_dyn26_saite_complete", "Dynasty XXVI Complete (Saite Renaissance): Necho I → Psamtik I (54 yrs) → Necho II (Battle of Megiddo/Carchemish!) → Psamtik II → Apries (Biblical Hophra!) → Amasis II (44 yrs) → Psamtik III", 17, "664-525 BCE (Budge Vol. II pp. 78-90; Manetho Fr. 68-69; Jer 44:30)", "Last Great Native Renaissance Before Persian Conquest", "Necho II slew King Josiah at Megiddo (609 BCE); Apries (Biblical Pharaoh Hophra, Jer 44:30) sheltered Judean refugees including Jeremiah; Amasis II allied with Croesus of Lydia & Polycrates of Samos; Psamtik III fell to Cambyses II (525 BCE).", {"major": True, "altNames": ["Psamtik I–III", "Apries / Pharaoh Hophra", "Amasis II"]}),
        ("eg_dyn27_31_late_native", "Dynasties XXVII–XXXI: 1st Persian (Cambyses, Darius I, Xerxes, Artaxerxes I), XXVIII (Amyrtaeus), XXIX (Nepherites I, Hakor/Achoris), XXX (Nectanebo I, Teos, Nectanebo II — Last Native Pharaoh!) & XXXI (Artaxerxes III, Arses, Darius III)", 18, "525-332 BCE (Budge Vol. II pp. 91-106; Manetho Fr. 70-75)", "Final Native Egyptian Resistance Through Nectanebo II to Alexander (332 BCE)", "Amyrtaeus freed Egypt from Persia (404 BCE); Nectanebo I & II (Dynasty XXX, builders of Philae & Karnak pylons) were the LAST native Egyptian Pharaohs in history before Alexander the Great entered Egypt in 332 BCE!", {"major": True, "altNames": ["Amyrtaeus", "Nepherites I", "Hakor / Achoris", "Nectanebo I & II"]}),
        ("eg_ptolemies_complete", "Complete Ptolemaic Dynasty (All 15 Ptolemies & 7 Cleopatras): Ptolemy I Soter → II Philadelphus (Septuagint!) → III Euergetes → IV Philopator → V Epiphanes (Rosetta Stone! + Cleopatra I Syra) → VI Philometor → VIII Euergetes II → IX Soter II → XII Auletes → Cleopatra VII & Caesarion", 18, "305-30 BCE (Budge Vol. II pp. 107-154)", "Macedonian-Greek Pharaohs of Alexandria (Septuagint & Rosetta Stone)", "Ptolemy II built the Library of Alexandria & commissioned the Greek Septuagint; Ptolemy V (+ Seleucid Cleopatra I Syra) issued the Rosetta Stone (196 BCE); Cleopatra VII & Caesarion (Ptolemy XV) closed 3,000 years of Pharaonic rule.", {"altNames": ["Ptolemy II Philadelphus", "Ptolemy V (Rosetta Stone)", "Cleopatra I Syra", "Caesarion"]}),
    ]
    add_chain(nodes, edges, dyn21_31, start_parent="eg_dyn20_complete", start_edge_type="expansion",
              start_edge_label="Third Intermediate, Late Period & Ptolemaic Dynasties (XXI–XXXI)",
              tradition="levant_egypt", default_edge_type="expansion", default_sources=["Manetho Aegyptiaca (Loeb)", "Budge Book of the Kings of Egypt Vol. II"])

    # -------------------------------------------------------------------------
    # 6. COMPLETE NAPATAN & MEROITIC KINGS OF NUBIA/KUSH (Budge Vol. II pp. 195-214)
    # -------------------------------------------------------------------------
    nodes += [
        N("af_napata_aspelta_nastasen", "Napatan Kings of Kush: Atlanersa → Senkamanisken → Anlamani → Aspelta → Harsiotef → Nastasen", "african", 18, "c. 653-315 BCE (Budge Vol. II pp. 199-205)",
          "Post-25th Dynasty Nubian Pyramid Builders of Nuri & Jebel Barkal", ["Budge Book of the Kings of Egypt Vol. II (pp. 199-205)"],
          "After Assyria pushed Dynasty XXV south of Aswan, Taharqa & Tantamani's successors (Atlanersa, Senkamanisken, Aspelta [moved capital to Meroe after Psamtik II's 593 BCE raid], Harsiotef, Nastasen) ruled Kush for centuries.",
          ["Atlanersa", "Senkamanisken", "Aspelta", "Harsiotef", "Nastasen"], major=True),
        N("af_meroe_ergamenes_natakamani", "Meroitic Kingdom: King Arqamani (Ergamenes) → King Natakamani & Queen Amanitore → Princes Arikhankharer & Shorkaror", "african", 19, "c. 270 BCE – 50 CE (Budge Vol. II pp. 205-214; Diodorus III.6; Acts 8:27)",
          "Golden Age of Meroe, Meroitic Script & Biblical Candace Dynasty", ["Budge Book of the Kings of Egypt Vol. II (pp. 205-214)", "Diodorus Siculus III.6", "Acts 8:27"],
          "Arqamani (Greek: Ergamenes, friend of Ptolemy II & IV!) broke priestly control and built Dakka temple; King Natakamani & Kandake Queen Amanitore (Biblical 'Candace' era!) built the Lion Temple at Naqa and restored Meroe.",
          ["Arqamani / Ergamenes", "Natakamani", "Amanitore", "Arikhankharer", "Shorkaror"]),
    ]

    edges += [
        E("eg_ptah", "eg_manetho_demigods", "expansion", "Manetho Fr. 1: Hephaestus (Ptah) -> Helios -> Geb -> Osiris -> Horus -> Demigods"),
        E("eg_manetho_demigods", "eg_palermo_predynastic", "expansion", "Transition from Shemsu-Hor to Palermo Stone Predynastic Kings"),
        E("eg_palermo_predynastic", "eg_menes", "direct", "Dynasty 0 / Predynastic -> Unification under Narmer/Menes"),
        E("eg_dyn18_amarna_end", "grk_aegyptus_danaus", "syncretic", "Manetho Fr. 50/53 explicitly equates Horemheb (Harmais) = Danaus & Seti/Ramesses = Aegyptus!"),
        E("eg_dyn19_complete", "grk_priam_hector", "cognate", "Manetho Fr. 55 synchronizes Queen Twosret (Thuoris) with the Fall of Troy"),
        E("eg_dyn21_tanite_theban", "jud_solomon", "cognate", "Pharaoh Siamun / Psusennes II era: Pharaoh's daughter marries King Solomon (1 Kgs 3:1, 9:16)"),
        E("eg_dyn22_libyan_pasenhor", "eg_shoshenq1", "direct", "Full Libyan Dynasty XXII genealogy (Stele of Pasenhor)"),
        E("eg_dyn25_kush_budge", "af_taharqa", "direct", "Kushite Dynasty XXV royal family (Budge Vol. II)"),
        E("eg_dyn26_saite_complete", "for_pharaoh_neco", "direct", "Saite Dynasty XXVI (Psamtik I -> Necho II -> Apries/Hophra -> Amasis II)"),
        E("eg_dyn26_saite_complete", "pro_jeremiah_ezekiel", "cognate", "Pharaoh Apries (Hophra, Jer 44:30) shelters Judean refugees in Egypt"),
        E("eg_dyn27_31_late_native", "ir_cambyses2_atossa", "cognate", "Cambyses II conquers Egypt (Dynasty XXVII, 525 BCE)"),
        E("eg_dyn27_31_late_native", "grk_alexander", "cognate", "Alexander the Great liberates Egypt from Dynasty XXXI (332 BCE)"),
        E("eg_ptolemies_complete", "eg_ptolemy_cleopatra", "direct", "All 15 Ptolemies & 7 Cleopatras (Budge Vol. II)"),
        E("cls_seleucids", "eg_ptolemies_complete", "direct", "Seleucid Princess Cleopatra I Syra marries Ptolemy V Epiphanes (193 BCE)"),
        E("af_tantamani", "af_napata_aspelta_nastasen", "direct", "Post-25th Dynasty Napatan Kings of Kush (Budge Vol. II pp. 199-205)"),
        E("af_napata_aspelta_nastasen", "af_meroe_ergamenes_natakamani", "direct", "Napatan -> Meroitic Kings & Kandakes (Ergamenes -> Natakamani & Amanitore)"),
        E("af_meroe_ergamenes_natakamani", "af_kandakes", "direct", "Meroitic Kandake Queens (Amanirenas, Amanishakheto, Amanitore)"),
    ]

    # -------------------------------------------------------------------------
    # 7. EXHAUSTIVE INDIVIDUAL PHARAOHS, PTOLEMIES & NUBIAN KINGS (Every Ruler Searchable!)
    # -------------------------------------------------------------------------
    add_roster(nodes, edges, "eg_dyn1_complete", "egr_d1_2", "levant_egypt", 6, "c. 2982-2657 BCE (Willockx; Manetho)", "Early Dynastic Pharaoh (Dyn. I–II)", ["Willockx King List 1-6", "Manetho Aegyptiaca"], [
        "Djer / Kenkenes (Dyn. I, 47 yrs)", "Djet / Uenephes (Dyn. I, 13 yrs)", "Queen Merneith (Regent of Dyn. I)", "Adjib / Miebis (Dyn. I)",
        "Semerkhet / Semempses (Dyn. I)", "Qa'a / Bieneches (Dyn. I)", "Hotepsekhemwy / Boethos (Dyn. II)", "Nebre / Kaiechos (Dyn. II)",
        "Nynetjer / Binothris (Dyn. II)", "Weneg / Tlas (Dyn. II)", "Sened / Sethenes (Dyn. II)", "Seth-Peribsen (Dyn. II)"
    ], edge_type="direct", edge_label="Dynasty I–II Pharaoh")

    add_roster(nodes, edges, "eg_dyn4_complete", "egr_d3_6", "levant_egypt", 7, "c. 2657-2168 BCE (Willockx; Manetho)", "Old Kingdom Pharaoh (Dyn. III–VI)", ["Willockx King List 1-6", "Manetho Aegyptiaca"], [
        "Sanakht / Necherophes (Dyn. III)", "Sekhemkhet / Tyris (Dyn. III)", "Khaba (Dyn. III)", "Huni / Kerpheres (Dyn. III)",
        "Djedefre / Ratoises (Dyn. IV)", "Baka / Bicheris (Dyn. IV)", "Shepseskaf (Dyn. IV)", "Queen Khentkawes (Dyn. IV/V Bridge)",
        "Userkaf / Usercheres (Dyn. V)", "Sahure / Sephres (Dyn. V)", "Neferirkare Kakai (Dyn. V)", "Shepseskare (Dyn. V)",
        "Neferefre (Dyn. V)", "Nyuserre Ini (Dyn. V)", "Menkauhor (Dyn. V)", "Djedkare Isesi (Dyn. V)", "Unas / Onnus (Dyn. V, Pyramid Texts)",
        "Teti / Othoes (Dyn. VI)", "Userkare (Dyn. VI)", "Pepi I / Phius (Dyn. VI)", "Merenre I (Dyn. VI)", "Pepi II / Phiops (Dyn. VI, 94 yrs)",
        "Merenre II (Dyn. VI)", "Queen Nitocris / Neith-iqerty (Dyn. VI)"
    ], edge_type="direct", edge_label="Old Kingdom Pharaoh (Dyn. III–VI)")

    add_roster(nodes, edges, "eg_dyn12_complete", "egr_mk", "levant_egypt", 11, "2160-1550 BCE (Breasted Vol. I; Manetho)", "Middle Kingdom / Hyksos Ruler (Dyn. XI–XVII)", ["Breasted Ancient Records Vol. I", "Manetho Aegyptiaca"], [
        "Intef I (Dyn. XI)", "Intef II (Dyn. XI)", "Intef III (Dyn. XI)", "Mentuhotep III (Dyn. XI)", "Mentuhotep IV (Dyn. XI)",
        "Amenemhat I (Dyn. XII)", "Senusret I / Sesonchosis (Dyn. XII)", "Amenemhat II (Dyn. XII)", "Senusret II (Dyn. XII)",
        "Amenemhat IV (Dyn. XII)", "Queen Sobekneferu / Scemiophris (Dyn. XII)", "Sobekhotep IV / Chenephres (Dyn. XIII)",
        "Dedumose / Tutimaeus (Dyn. XIII)", "Salitis (Hyksos Dyn. XV)", "Khyan / Iannas (Hyksos Dyn. XV)", "Apophis / Apepi (Hyksos Dyn. XV)",
        "Kamose (Theban Liberator, Dyn. XVII)"
    ], edge_type="expansion", edge_label="Middle Kingdom / Hyksos Ruler")

    add_roster(nodes, edges, "eg_dyn18_early", "egr_nk", "levant_egypt", 15, "1550-1077 BCE (Manetho; Budge Vol. II)", "New Kingdom Pharaoh (Dyn. XVIII–XX)", ["Manetho Aegyptiaca", "Budge Book of Kings Vol. II"], [
        "Amenhotep I (Dyn. XVIII)", "Thutmose II (Dyn. XVIII)", "Queen Hatshepsut / Amessis (Dyn. XVIII)", "Amenhotep II (Dyn. XVIII)",
        "Thutmose IV (Dyn. XVIII)", "Queen Tiye (Wife of Amenhotep III)", "Queen Nefertiti (Amarna Queen)", "Smenkhkare (Dyn. XVIII)",
        "Pharaoh Ay (Dyn. XVIII)", "Horemheb / Harmais = Danaus (Dyn. XVIII)", "Ramesses I (Dyn. XIX)", "Seti I / Sethos (Dyn. XIX)",
        "Amenmesse (Dyn. XIX)", "Seti II (Dyn. XIX)", "Siptah (Dyn. XIX)", "Queen Twosret / Thuoris (Dyn. XIX)",
        "Setnakhte (Dyn. XX)", "Ramesses IV (Dyn. XX)", "Ramesses V (Dyn. XX)", "Ramesses VI (Dyn. XX)",
        "Ramesses VII (Dyn. XX)", "Ramesses VIII (Dyn. XX)", "Ramesses IX (Dyn. XX)", "Ramesses X (Dyn. XX)", "Ramesses XI (Dyn. XX)"
    ], edge_type="direct", edge_label="New Kingdom Pharaoh (Dyn. XVIII–XX)")

    add_roster(nodes, edges, "eg_dyn21_tanite_theban", "egr_3ip", "levant_egypt", 17, "1077-332 BCE (Budge Vol. II; Manetho)", "Third Intermediate & Late Period Pharaoh (Dyn. XXI–XXX)", ["Budge Book of Kings Vol. II", "Manetho Aegyptiaca"], [
        "Herihor (Theban Priest-King)", "Piankh (Theban Priest-King)", "Pinudjem I (Theban Priest-King)", "Menkheperre (Theban Priest-King)",
        "Pinudjem II (Theban Priest-King)", "Smendes (Dyn. XXI)", "Psusennes I (Silver Pharaoh, Dyn. XXI)", "Amenemope (Dyn. XXI)",
        "Siamun (Dyn. XXI)", "Psusennes II (Dyn. XXI)", "Buyuwawa (Libyan Ancestor, Pasenhor Stele)", "Osorkon I (Dyn. XXII)",
        "Takelot I (Dyn. XXII)", "Osorkon II (Dyn. XXII)", "Shoshenq II (Dyn. XXII)", "Takelot II (Dyn. XXII)", "Shoshenq III (Dyn. XXII)",
        "Pami (Dyn. XXII)", "Shoshenq V (Dyn. XXII)", "Pedubast I (Dyn. XXIII)", "Osorkon III (Dyn. XXIII)", "Tefnakht I (Dyn. XXIV)",
        "Bakenranef / Bocchoris (Dyn. XXIV)", "Shabaka / Sabacon (Dyn. XXV)", "Shabataka / Sebichos (Dyn. XXV)",
        "Psamtik I (Dyn. XXVI, 54 yrs)", "Psamtik II (Dyn. XXVI)", "Apries / Pharaoh Hophra (Dyn. XXVI)", "Amasis II (Dyn. XXVI, 44 yrs)",
        "Psamtik III (Dyn. XXVI)", "Amyrtaeus (Dyn. XXVIII)", "Nepherites I (Dyn. XXIX)", "Hakor / Achoris (Dyn. XXIX)",
        "Nectanebo I (Dyn. XXX)", "Teos / Tachos (Dyn. XXX)", "Nectanebo II (Last Native Pharaoh, Dyn. XXX)"
    ], edge_type="expansion", edge_label="Dynasty XXI–XXX Pharaoh")

    add_roster(nodes, edges, "eg_ptolemies_complete", "egr_ptol", "levant_egypt", 18, "305-30 BCE (Budge Vol. II pp. 111-154)", "Ptolemaic Ruler of Egypt", ["Budge Book of Kings Vol. II (pp. 111-154)"], [
        "Ptolemy I Soter (+ Berenice I)", "Ptolemy II Philadelphus (+ Arsinoe II, Septuagint)", "Ptolemy III Euergetes (+ Berenice II)",
        "Ptolemy IV Philopator (+ Arsinoe III)", "Ptolemy V Epiphanes (+ Cleopatra I Syra, Rosetta Stone)", "Ptolemy VI Philometor (+ Cleopatra II)",
        "Ptolemy VIII Euergetes II (+ Cleopatra III)", "Ptolemy IX Soter II", "Ptolemy X Alexander I (+ Berenice III)",
        "Ptolemy XII Auletes", "Ptolemy XIII & XIV", "Ptolemy XV Caesarion (Son of Cleopatra VII & Julius Caesar)"
    ], edge_type="direct", edge_label="Ptolemaic Monarch")

    add_roster(nodes, edges, "af_napata_aspelta_nastasen", "afr_kush", "african", 18, "c. 653 BCE – 50 CE (Budge Vol. II pp. 195-214)", "Napatan / Meroitic Monarch of Kush", ["Budge Book of Kings Vol. II (pp. 195-214)"], [
        "Atlanersa (Napata)", "Senkamanisken (Napata)", "Anlamani (Napata)", "Aspelta (Moved Capital to Meroe)",
        "Harsiotef (Napata)", "Nastasen (Napata)", "Arqamani / Ergamenes (Meroe)", "King Natakamani (Meroe)",
        "Queen Amanitore (Kandake of Meroe)", "Prince Arikhankharer (Meroe)", "Prince Shorkaror (Meroe)"
    ], edge_type="direct", edge_label="Napatan / Meroitic Ruler")

    return {
        "module": "18_egypt_31_dynasties_manetho_budge",
        "title": "Complete 31 Dynasties of Egypt (Manetho Loeb, Palermo Stone/Breasted, Willockx 1-6, Budge Vol. II) + Complete Ptolemies & Napata/Meroe Kings",
        "nodes": nodes,
        "edges": edges,
    }
