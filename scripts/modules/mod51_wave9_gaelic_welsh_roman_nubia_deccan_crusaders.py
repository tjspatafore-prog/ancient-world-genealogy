"""
Module 51: Wave 9 — 4,000+ Node Milestone Edition:
Gaelic Ireland (Annals of the Four Masters & O'Hart) & Scotland (Dal Riata -> Bruce -> Stewart -> James VI & I),
Welsh Royal Houses (Gwynedd, Deheubarth & Tudors), Roman Republican/Imperial Women, Severan Emesa &
Pausanias Regional Greek Stemmata, Christian Nubia & Funj Sultanate of Sennar,
South Indian Dynasties (Chalukyas, Pallavas, Cholas, Vijayanagara, Marathas) & Portuguese Asia,
Crusader Kingdom of Jerusalem, Norman Sicily, Renaissance Medici/Sforza, Orange-Nassau & Modern Spain (2026).
"""

from . import N, E


def add_chain(nodes, edges, parent_id, items, tradition, era_default, sources, default_type="direct"):
    prev = parent_id
    for item in items:
        nid, name, tier = item[0], item[1], item[2]
        era = item[3] if len(item) > 3 else era_default
        role = item[4] if len(item) > 4 else "Sovereign / Royal Lineage"
        notes = item[5] if len(item) > 5 else f"Chronicle succession in {', '.join(sources)}."
        major = item[6] if len(item) > 6 else False
        nodes.append(N(nid, name, tradition, tier, era, role, sources, notes, major=major))
        if prev:
            edges.append(E(prev, nid, default_type, f"{', '.join(sources)}: succession"))
        prev = nid


def build_module():
    nodes, edges = [], []

    # =========================================================================
    # SECTION A: GAELIC IRELAND (FOUR MASTERS / O'HART) & SCOTTISH STEWARTS (31 nodes)
    # =========================================================================
    add_chain(nodes, edges, "irl_niall_brian_boru", [
        ("gael9_tigernmas", "High King Tigernmas of Ireland (Introduced Gold Smelting, Four Masters)", 11, "Traditional Milesian Era", "High King of Ireland"),
        ("gael9_ollom_fodla", "High King Ollom Fódla (Founder of Feis Temrach / Assembly of Tara)", 12, "Traditional Milesian Era", "Lawgiver High King"),
        ("gael9_cimbaeth_macha", "High King Cimbáeth & Queen Macha Mong Ruad (Founders of Emain Macha)", 14, "c. 4th c. BCE", "High King & Sole Queen of Ireland"),
        ("gael9_ugaine_mor", "High King Úgaine Mór (Ancestral Sovereign of Leinster & Tara)", 14, "Traditional Milesian Era", "High King of Ireland"),
        ("gael9_labraid_loingsech", "High King Labraid Loingsech (Progenitor of the Laigin / Leinster Kings)", 14, "c. 3rd c. BCE", "Founder of Leinster"),
        ("gael9_conn_ceadchathach", "High King Conn of the Hundred Battles (Conn Cétchathach, 2nd c. CE)", 18, "2nd c. CE", "High King of Tara"),
        ("gael9_art_mac_cuinn", "High King Art mac Cuinn (Father of Cormac mac Airt)", 18, "c. 195–220 CE", "High King of Tara"),
    ], "europe_norse", "Ancient Ireland", ["Annals of the Four Masters", "O'Hart Irish Pedigrees Vols. 1–2"])
    edges.append(E("gael9_art_mac_cuinn", "eur5_cormac_mac_airt", "direct", "Father of High King Cormac mac Airt"))

    add_chain(nodes, edges, "eur5_cormac_mac_airt", [
        ("gael9_cairbre_lifechair", "High King Cairbre Lifechair (Son of Cormac mac Airt, Battle of Gabhra)", 19, "3rd c. CE", "High King of Tara"),
        ("gael9_eochaid_mugmedon", "High King Eochaid Mugmedón (+ Mongfind & Cairenn; Father of Niall)", 19, "4th c. CE", "High King of Tara"),
        ("gael9_loegaire_patrick", "High King Lóegaire mac Néill (Met St. Patrick at Slane & Tara, 432 CE)", 19, "r. 428–458 CE", "High King of Ireland"),
    ], "europe_norse", "3rd–5th c. CE", ["Annals of the Four Masters", "Keating Foras Feasa"])
    nodes += [
        N("gael9_conall_gulban", "Conall Gulban (Son of Niall; Founder of Cenél Conaill / Donegal)", "europe_norse", 19, "5th c. CE", "Progenitor of O'Donnell & St. Columba", ["O'Hart Vol. 1", "Annals of the Four Masters"], "Ancestral prince of Cenél Conaill."),
        N("gael9_st_columba", "St. Columba / Colm Cille (Prince of Cenél Conaill & Abbot of Iona, 521–597 CE)", "europe_norse", 19, "521–597 CE", "Saint & Royal Missionary of Iona", ["Adomnán Life of Columba", "O'Hart Vol. 1"], "Great-great-grandson of Niall of the Nine Hostages; founded Iona and ordained King Áedán mac Gabráin of Dál Riata.", True),
        N("gael9_eogan_mac_neill", "Éogan mac Néill (Son of Niall; Founder of Cenél nEógain / Ailech)", "europe_norse", 19, "5th c. CE", "Progenitor of O'Neill Dynasty", ["O'Hart Irish Pedigrees Vol. 1"], "Founder of the Northern Uí Néill kings of Ailech & Tyrone."),
        N("gael9_hugh_oneill", "Hugh O'Neill, 2nd Earl of Tyrone (The Great O'Neill, 1550–1616 CE)", "europe_norse", 21, "c. 1550–1616 CE", "O'Neill Chief & Nine Years' War Leader", ["O'Hart Irish Pedigrees Vol. 1", "Annals of the Four Masters"], "Direct Cenél nEógain descendant of Niall of the Nine Hostages."),
    ]
    edges += [
        E("gael9_eochaid_mugmedon", "gael9_conall_gulban", "direct", "Brother / son line of Niall of the Nine Hostages"),
        E("gael9_conall_gulban", "gael9_st_columba", "direct", "Cenél Conaill pedigree (great-grandfather of St. Columba)"),
        E("gael9_eochaid_mugmedon", "gael9_eogan_mac_neill", "direct", "Northern Uí Néill line via Éogan mac Néill"),
        E("gael9_eogan_mac_neill", "gael9_hugh_oneill", "direct", "Cenél nEógain / O'Neill succession"),
    ]
    add_chain(nodes, edges, "eur5_brian_boru", [
        ("gael9_mael_sechnaill2", "High King Máel Sechnaill II (Clontarf Contemporary & Predecessor/Successor, d. 1022 CE)", 20, "949–1022 CE", "High King of Ireland"),
        ("gael9_turlough_oconnor", "High King Toirdelbach Ua Conchobair / Turlough O'Connor (1088–1156 CE)", 20, "1088–1156 CE", "High King of Ireland (Connacht)"),
        ("gael9_rory_oconnor", "High King Ruaidrí Ua Conchobair / Rory O'Connor (Last High King of Ireland, r. 1166–1186)", 20, "c. 1116–1198 CE", "Last High King of Ireland"),
    ], "europe_norse", "10th–12th c. CE", ["Annals of the Four Masters", "O'Hart Irish Pedigrees"])

    # Dál Riata -> Scottish Kings -> Bruce -> Stewart -> James VI & I
    nodes.append(N("gael9_aedan_mac_gabrain", "King Áedán mac Gabráin of Dál Riata (Ordained by St. Columba, r. 574–608 CE)", "europe_norse", 19, "c. 532–608 CE", "King of Dál Riata (Argyll & Antrim)", ["Adomnán", "Lebor Gabála", "O'Hart"], "Grandson/descendant of Fergus Mór; consecrated king by St. Columba at Iona."))
    edges += [
        E("sco_fergus_macalpin", "gael9_aedan_mac_gabrain", "direct", "Dál Riata royal descent from Fergus Mór mac Erc"),
        E("gael9_st_columba", "gael9_aedan_mac_gabrain", "expansion", "574 CE Royal Ordination of King Áedán by St. Columba on Iona"),
        E("gael9_aedan_mac_gabrain", "eur5_kenneth_macalpin", "direct", "Dál Riata succession to King Kenneth I MacAlpin"),
    ]
    add_chain(nodes, edges, "eur5_kenneth_macalpin", [
        ("gael9_malcolm2_scotland", "King Malcolm II of Scotland (victor at Carham 1018; r. 1005–1034 CE)", 20, "c. 954–1034 CE", "King of Alba"),
        ("gael9_duncan1", "King Duncan I of Scotland (Grandson of Malcolm II, r. 1034–1040 CE)", 20, "c. 1001–1040 CE", "King of Scotland"),
    ], "europe_norse", "10th–11th c. CE", ["Scottish Chronicles", "Anderson 1732"])
    nodes.append(N("gael9_macbeth", "King Macbeth of Scotland (Mac Bethad mac Findláich, Mormaer of Moray, r. 1040–1057 CE)", "europe_norse", 20, "c. 1005–1057 CE", "King of Scotland", ["Chronicle of Melrose", "Howell 1685"], "Cousin-successor of Duncan I; married Gruoch (granddaughter of Kenneth III)."))
    edges += [
        E("gael9_malcolm2_scotland", "gael9_macbeth", "expansion", "Grandson-cousin succession (Kenneth II / III rivalry)"),
        E("gael9_duncan1", "eur5_malcolm3", "direct", "Father of King Malcolm III Canmore"),
    ]
    add_chain(nodes, edges, "eur5_malcolm3", [
        ("gael9_st_margaret_scotland", "Queen St. Margaret of Scotland (Wessex Princess; Mother of Scottish & English Lines, d. 1093 CE)", 20, "c. 1045–1093 CE", "Queen of Scots & Wessex Heiress"),
        ("gael9_david1_scotland", "King St. David I of Scotland (Davidian Revolution, r. 1124–1153 CE)", 20, "1084–1153 CE", "King of Scots"),
        ("gael9_william_lion", "King William I the Lion of Scotland (Grandson of David I, r. 1165–1214 CE)", 20, "c. 1142–1214 CE", "King of Scots"),
        ("gael9_alexander3_scotland", "King Alexander II → King Alexander III of Scotland (d. 1286 CE)", 20, "1241–1286 CE", "Last Dunkeld King of Scots"),
    ], "europe_norse", "11th–13th c. CE", ["Howell 1685", "Anderson Royal Genealogies 1732"])
    edges += [
        E("mon_eng_edward_confessor", "gael9_st_margaret_scotland", "expansion", "Great-niece of St. Edward the Confessor (House of Wessex)"),
        E("gael9_alexander3_scotland", "eur5_robert_bruce", "expansion", "Dunkeld-Huntingdon inheritance claimed by Robert I the Bruce"),
    ]
    add_chain(nodes, edges, "eur5_robert_bruce", [
        ("gael9_marjorie_bruce_stewart", "Princess Marjorie Bruce (+ Walter Stewart; Mother of Robert II)", 20, "1296–1316 CE", "Daughter of Robert the Bruce & Stewart Ancestress"),
        ("gael9_robert2_stewart", "King Robert II of Scotland (1st Stewart Monarch, 1371–1390 CE)", 21, "1316–1390 CE", "Founder of House of Stewart"),
        ("gael9_james1_scotland", "King James I → James II → James III of Scotland (1406–1488 CE)", 21, "1394–1488 CE", "Stewart Kings of Scots"),
        ("gael9_james4_margaret_tudor", "King James IV (+ Queen Margaret Tudor, Daughter of Henry VII, 1488–1513)", 21, "1473–1513 CE", "King of Scots & Tudor Union"),
        ("gael9_james5_scotland", "King James V of Scotland (+ Mary of Guise, 1513–1542 CE)", 21, "1512–1542 CE", "King of Scots"),
        ("gael9_mary_queen_scots", "Mary, Queen of Scots (+ Henry Stuart, Lord Darnley; 1542–1587)", 21, "1542–1587 CE", "Queen Regnant of Scotland", "Granddaughter of Henry VII & Margaret Tudor; mother of King James VI & I uniting Scotland and England.", True),
    ], "europe_norse", "14th–16th c. CE", ["William Howell 1685", "Anderson 1732"])
    edges += [
        E("mon_eng_henry7", "gael9_james4_margaret_tudor", "direct", "1503 CE Marriage of Thistle & Rose: Margaret Tudor (dau. of Henry VII) & James IV"),
        E("gael9_mary_queen_scots", "mon_eng_james1", "direct", "Mother of King James VI & I of Great Britain"),
    ]

    # =========================================================================
    # SECTION B: WELSH ROYAL HOUSES OF GWYNEDD, DEHEUBARTH & TUDORS (10 nodes)
    # =========================================================================
    add_chain(nodes, edges, "eur_wal_cunedda", [
        ("wal9_maelgwn_gwynedd", "King Maelgwn Gwynedd (6th c. High King of Britain in Gildas & Lloyd)", 19, "d. c. 547 CE", "King of Gwynedd"),
        ("wal9_cadwallon_cadwaladr", "Kings Cadwallon ap Cadfan & Cadwaladr Fendigaid (7th c. Welsh Kings)", 19, "d. 682 CE", "Kings of Gwynedd"),
        ("wal9_merfyn_frych", "King Merfyn Frych (+ Esyllt of Gwynedd; Father of Rhodri Mawr, d. 844 CE)", 19, "d. 844 CE", "King of Gwynedd"),
    ], "europe_norse", "6th–9th c. CE", ["J.E. Lloyd History of Wales (2edhistoryofwale01lloyuoft.pdf)"])
    edges.append(E("wal9_merfyn_frych", "chr6_rhodri_mawr", "direct", "Father of Rhodri Mawr / Rhodri the Great"))

    add_chain(nodes, edges, "chr6_hywel_dda", [
        ("wal9_rhys_ap_tewdwr", "King Rhys ap Tewdwr of Deheubarth (Killed 1093 CE)", 20, "d. 1093 CE", "Prince of Deheubarth"),
        ("wal9_nest_ferch_rhys", "Princess Nest ferch Rhys ('The Helen of Wales'; Ancestress of FitzGeralds & Tudors)", 20, "c. 1085–c. 1140 CE", "Welsh Princess & Cambro-Norman Matriarch"),
        ("wal9_lord_rhys", "Rhys ap Gruffydd / The Lord Rhys (Founder of the National Eisteddfod, 1176 CE)", 20, "1132–1197 CE", "Prince of Deheubarth"),
    ], "europe_norse", "11th–12th c. CE", ["Lloyd History of Wales"])

    nodes += [
        N("wal9_joan_wales", "Princess Joan / Siwan (+ Llywelyn the Great; Daughter of King John of England)", "europe_norse", 20, "1191–1237 CE", "Lady of Wales & Daughter of King John", ["Lloyd History of Wales"], "Natural daughter of King John who wed Llywelyn the Great of Gwynedd."),
        N("wal9_llywelyn_ap_gruffudd", "Prince Llywelyn ap Gruffudd ('Llywelyn the Last', Prince of Wales, d. 1282 CE)", "europe_norse", 20, "c. 1223–1282 CE", "Final Sovereign Prince of Wales", ["Lloyd History of Wales"], "Grandson of Llywelyn the Great; last independent native Prince of Wales.", True),
        N("wal9_owain_glyndwr", "Owain Glyndŵr (Last Native Prince of Wales, 1400–1415 CE)", "europe_norse", 21, "c. 1359–c. 1415 CE", "Prince of Wales (Powys Fadog & Deheubarth)", ["Lloyd History of Wales", "Four Ancient Books of Wales"], "Claimed royal descent from both Powys & Deheubarth; proclaimed Prince of Wales in 1400 CE.", True),
        N("wal9_catherine_valois", "Queen Catherine of Valois (+ Henry V → Henry VI; + Owen Tudor → Edmund Tudor)", "europe_norse", 21, "1401–1437 CE", "Queen of England & Tudor Matriarch", ["William Howell 1685", "Lloyd History of Wales"], "Daughter of Charles VI of France; married Henry V of England and later Owen Tudor, mothering Henry VII's father Edmund Tudor."),
    ]
    edges += [
        E("chr6_owain_gwynedd", "wal9_joan_wales", "expansion", "Marriage of Llywelyn the Great (grandson of Owain Gwynedd) & Princess Joan"),
        E("mon_eng_john", "wal9_joan_wales", "direct", "Father of Princess Joan / Siwan"),
        E("wal9_joan_wales", "wal9_llywelyn_ap_gruffudd", "direct", "Grandson Llywelyn ap Gruffudd"),
        E("wal9_lord_rhys", "wal9_owain_glyndwr", "expansion", "Deheubarth & Powys Fadog royal descent of Owain Glyndŵr"),
        E("mon_fra_charles6", "wal9_catherine_valois", "direct", "Daughter of King Charles VI of France"),
        E("mon_eng_henry5", "wal9_catherine_valois", "direct", "1420 CE Treaty of Troyes Royal Marriage: Henry V & Catherine of Valois"),
        E("chr6_owen_tudor", "wal9_catherine_valois", "direct", "Royal Marriage uniting Welsh Tudor house with Valois"),
        E("wal9_catherine_valois", "mon_eng_henry7", "direct", "Grandmother of King Henry VII Tudor via Edmund Tudor"),
    ]

    # =========================================================================
    # SECTION C: ROMAN WOMEN, EMESA SEVERANS & PAUSANIAS GREEK STEMMATA (22 nodes)
    # =========================================================================
    nodes += [
        N("cls9_cornelia_africana", "Cornelia Africana (Daughter of Scipio Africanus; Mother of Tiberius & Gaius Gracchus)", "greek", 18, "c. 189–c. 110 BCE", "Roman Republican Matron", ["Plutarch Gracchi", "Livy"], "Daughter of Scipio Africanus; renowned Roman matron who raised the Gracchi brothers."),
        N("cls9_scipio_aemilianus", "Scipio Aemilianus Africanus (Adoptive Grandson of Scipio; Destroyer of Carthage 146 BCE)", "greek", 18, "185–129 BCE", "Roman Consul & General", ["Polybius", "Livy Epitome"], "Biological son of Lucius Aemilius Paullus & patron of Polybius."),
        N("cls9_aemilius_paullus", "Lucius Aemilius Paullus Macedonicus (Victor of Pydna 168 BCE)", "greek", 18, "c. 229–160 BCE", "Roman Consul", ["Plutarch Aemilius Paullus", "Polybius"], "Defeated Perseus of Macedon; biological father of Scipio Aemilianus."),
        N("cls9_polybius_historian", "Polybius of Megalopolis (c. 200–118 BCE; Mentor of Scipio Aemilianus)", "greek", 18, "c. 200–118 BCE", "Greek Historian of Rome", ["General History of Polybius"], "Achaean statesman-hostage whose Histories chronicled Rome & Carthage."),
        N("cls9_titus_livius", "Titus Livius / Livy of Patavium (59 BCE–17 CE; Author of Ab Urbe Condita)", "greek", 19, "59 BCE–17 CE", "Roman Historian", ["Roman History by Titus Livius Vols. 1–6"], "Preeminent historian of Rome from Aeneas & Romulus to Augustus."),
        N("cls9_cornelius_tacitus", "Publius Cornelius Tacitus (c. 56–120 CE; Senator & Author of Annals & Histories)", "greek", 19, "c. 56–120 CE", "Roman Senator & Historian", ["Works of Cornelius Tacitus Vols. 1–4"], "Chronicler of the Julio-Claudian & Flavian emperors and Germanic tribes."),
    ]
    edges += [
        E("mon_rom_scipio_africanus", "cls9_cornelia_africana", "direct", "Daughter of Scipio Africanus"),
        E("cls9_cornelia_africana", "mon_rom_gracchi", "direct", "Mother of Tiberius & Gaius Gracchus"),
        E("mon_rom_scipio_africanus", "cls9_scipio_aemilianus", "direct", "Adoptive grandfather of Scipio Aemilianus"),
        E("cls9_aemilius_paullus", "cls9_scipio_aemilianus", "direct", "Biological father of Scipio Aemilianus"),
        E("cls9_scipio_aemilianus", "cls9_polybius_historian", "expansion", "Friend & chronicler of the Scipionic Circle"),
        E("cls9_polybius_historian", "cls9_titus_livius", "cognate", "Primary historical source used by Livy"),
        E("mon_rom_tiberius", "cls9_cornelius_tacitus", "expansion", "Principal historical subject of Tacitus Annals"),
    ]

    nodes += [
        N("cls9_julia_caesaris_pompey", "Julia Caesaris (Daughter of Julius Caesar; Wife of Pompey the Great, d. 54 BCE)", "greek", 18, "c. 76–54 BCE", "Roman Noblewoman", ["Plutarch Caesar & Pompey"], "Her 59 BCE marriage to Pompey sealed the First Triumvirate."),
        N("cls9_faustina_elder_younger", "Empresses Faustina the Elder (+ Antoninus Pius) & Faustina the Younger (+ Marcus Aurelius)", "greek", 19, "100–175 CE", "Antonine Roman Empresses", ["Echard Roman History", "Suetonius / SHA"], "Transmitted Antonine imperial legitimacy to Marcus Aurelius & Commodus."),
        N("cls9_julia_domna", "Empress Julia Domna of Emesa (+ Septimius Severus; Mother of Caracalla, d. 217 CE)", "greek", 19, "c. 160–217 CE", "Syrian Priest-Princess & Roman Augusta", ["Herodian", "Echard Roman History Vol. 2"], "Daughter of High Priest Julius Bassianus of Emesa (Homs, Syria); intellectual & imperial Augusta of the Severan dynasty.", True),
        N("cls9_julia_maesa", "Julia Maesa of Emesa (Sister of Julia Domna; Grandmother of Elagabalus & Severus Alexander)", "greek", 19, "c. 165–224 CE", "Severan Augusta", ["Herodian", "Echard"], "Engineered the 218 CE Severan restoration."),
        N("cls9_julia_soaemias_mamaea", "Empresses Julia Soaemias & Julia Avita Mamaea (Mothers of Elagabalus & Severus Alexander)", "greek", 19, "c. 180–235 CE", "Severan Empresses Regent", ["Herodian", "Echard"], "Daughters of Julia Maesa."),
    ]
    edges += [
        E("rom3_julius_caesar", "cls9_julia_caesaris_pompey", "direct", "Daughter of Julius Caesar"),
        E("cls9_julia_caesaris_pompey", "mon_rom_pompey_cicero", "direct", "59 BCE Marriage: Julia Caesaris & Pompey the Great"),
        E("mon_rom_antoninus_pius", "cls9_faustina_elder_younger", "direct", "Antonine Empress & daughter wife of Marcus Aurelius"),
        E("cls9_faustina_elder_younger", "mon_rom_marcus_aurelius", "direct", "Marriage & mother of Emperor Commodus"),
        E("mon_rom_septimius_severus", "cls9_julia_domna", "direct", "Marriage: Septimius Severus & Julia Domna of Emesa"),
        E("cls9_julia_domna", "mon_rom_caracalla", "direct", "Mother of Emperors Caracalla & Geta"),
        E("cls9_julia_domna", "cls9_julia_maesa", "direct", "Sisters of the Emesa royal-priestly house"),
        E("cls9_julia_maesa", "cls9_julia_soaemias_mamaea", "direct", "Daughters of Julia Maesa; mothers of Severan emperors"),
        E("cls9_julia_soaemias_mamaea", "mon_rom_elagabalus", "direct", "Mother of Emperor Elagabalus"),
        E("cls9_julia_soaemias_mamaea", "mon_rom_severus_alexander", "direct", "Mother of Emperor Severus Alexander"),
    ]

    # Pausanias Regional Greek Stemmata (Arcadia, Elis, Messenia & Syracuse)
    add_chain(nodes, edges, "grk_arcadia_pelasgus_atalanta", [
        ("cls9_lycaon_callisto", "King Lycaon of Arcadia & Callisto (Pausanias VIII.2–3)", 11, "Mythic Pelasgian Era", "Early Arcadian Line"),
        ("cls9_arcas_arcadia", "King Arcas of Arcadia (Eponym of Arcadia; Father of Azan & Apheidas)", 12, "Heroic Greek Era", "Eponymous King of Arcadia"),
        ("cls9_telephus_mysia", "King Telephus of Mysia (Son of Heracles & Auge of Tegea; Pausanias VIII.48)", 13, "Trojan War Era", "King of Mysia"),
    ], "greek", "Heroic Greek Era", ["Pausanias Description of Greece Books IV, V, VIII"])
    edges.append(E("grk_heracles", "cls9_telephus_mysia", "direct", "Father Heracles & Princess Auge of Tegea"))

    nodes += [
        N("cls9_endymion_elis", "King Endymion of Elis (Son of Aethlius; Father of Epeius, Pausanias V.1)", "greek", 12, "Heroic Greek Era", "Early King of Elis", ["Pausanias Book V (Elis)"], "Founder of Epean / Elian royal genealogy."),
        N("cls9_oenomaus_hippodamia", "King Oenomaus of Pisa & Hippodamia (+ Pelops; Olympia Chariot Race)", "greek", 12, "Heroic Greek Era", "King of Pisa (Elis)", ["Pausanias Book V"], "Father-in-law of Pelops."),
        N("cls9_cresphontes_messenia", "King Cresphontes of Messenia (Heraclid Return & Partition of Peloponnese, Pausanias IV.3)", "greek", 14, "Heraclid Era", "1st Heraclid King of Messenia", ["Pausanias Book IV (Messenia)"], "Descendant of Heracles who drew Messenia by lot."),
        N("cls9_aristomenes_messenia", "Aristomenes of Messenia (Hero of the Second Messenian War, Pausanias IV.14–24)", "greek", 16, "7th c. BCE", "Messenian Hero & Aepytid Scion", ["Pausanias Book IV"], "Led Messenian independence struggle against Sparta."),
    ]
    edges += [
        E("grk_pelops_atreus", "cls9_endymion_elis", "expansion", "Pausanias Book V: Elian/Olympian royal house"),
        E("cls9_endymion_elis", "cls9_oenomaus_hippodamia", "expansion", "Elis/Pisa royal predecessors of Pelops"),
        E("cls9_oenomaus_hippodamia", "grk_pelops_atreus", "direct", "Marriage of Princess Hippodamia & Pelops"),
        E("grk_heracles", "cls9_cresphontes_messenia", "direct", "Heraclid descendant Cresphontes"),
        E("cls9_cresphontes_messenia", "cls9_aristomenes_messenia", "expansion", "Pausanias IV: Messenian royal hero tradition"),
    ]
    add_chain(nodes, edges, None, [
        ("cls9_gelon_hiero1", "Tyrants Gelon & Hiero I of Syracuse (Deinomenids, Victors of Himera 480 BCE)", 18, "485–466 BCE", "Deinomenid Rulers of Syracuse"),
        ("cls9_dionysius1_syracuse", "Dionysius I & Dionysius II of Syracuse (405–344 BCE)", 18, "405–344 BCE", "Tyrants of Syracuse"),
        ("cls9_timoleon_agathocles", "Timoleon & King Agathocles of Syracuse (344–289 BCE)", 18, "344–289 BCE", "Liberator & King of Sicily"),
        ("cls9_hiero2_syracuse", "King Hiero II of Syracuse (Kinsman & Patron of Archimedes, 270–215 BCE)", 18, "c. 308–215 BCE", "King of Syracuse", ["Polybius", "Plutarch Marcellus"], "Ruler of Syracuse & kinsman-patron of mathematician Archimedes.", False),
    ], "greek", "5th–3rd c. BCE", ["Diodorus Siculus", "Polybius", "Plutarch"])
    edges.append(E("cls9_hiero2_syracuse", "unb_grk_archimedes", "expansion", "Kinsman & royal patron of Archimedes at Syracuse"))

    # =========================================================================
    # SECTION D: CHRISTIAN NUBIA & FUNJ SULTANATE OF SENNAR (15 nodes)
    # =========================================================================
    add_chain(nodes, edges, "sud_cush_nuba_beja", [
        ("nub9_silko_nobatia", "King Silko of Nobatia (Kalabsha Inscription, c. 450 CE; Defeated Blemmyes)", 19, "c. 450 CE", "Christian/Early King of Nobatia"),
        ("nub9_qalidurut_baqt", "King Qalidurut of Makuria (652 CE Baqt Treaty at Dongola)", 19, "fl. 652 CE", "King of Christian Makuria", "Successfully defended Dongola and concluded the 600-year Baqt Peace Treaty.", True),
        ("nub9_merkurios_makuria", "King Merkurios of Makuria ('New Constantine', United Nobatia & Makuria, c. 697–710 CE)", 19, "r. c. 697–710 CE", "King of Makuria & Nobatia"),
        ("nub9_cyriacus_makuria", "King Cyriacus of Makuria (Marched on Fustat c. 745 CE)", 19, "8th c. CE", "King of Makuria"),
        ("nub9_georgios1_makuria", "King Georgios I of Makuria (836 CE Royal Embassy to Caliph Al-Mu'tasim / Al-Ma'mun)", 19, "c. 816–887 CE", "King of Makuria"),
        ("nub9_georgios2_solomon", "Kings Georgios II & Solomon of Makuria (10th–11th c. CE Golden Age)", 20, "10th–11th c. CE", "Kings of Makuria"),
        ("nub9_david_makuria", "King David of Makuria & King Shekanda (1272–1276 CE vs Sultan Baybars)", 20, "13th c. CE", "Late Makurian Kings"),
        ("nub9_siti_alodia", "King Siti of Makuria & Kings of Alodia / Soba (14th–15th c. CE)", 20, "14th–15th c. CE", "Final Christian Nubian Rulers"),
    ], "african", "5th–15th c. CE", ["Arkell History of the Sudan", "MacMichael Arabs in the Sudan Vol. 1"])
    edges += [
        E("nub9_georgios1_makuria", "mon_isl_al_mamun", "expansion", "836 CE Abbasid–Makurian diplomatic embassy to Baghdad & Samarra"),
        E("nub9_david_makuria", "mon_isl_baybars", "expansion", "1272–1276 CE Mamluk–Nubian wars between King David and Sultan Baybars"),
    ]

    add_chain(nodes, edges, "sud_funj_sennar", [
        ("nub9_amara_dunqas", "Sultan Amara Dunqas (Founder of Funj Sultanate of Sennar, 1504–1534 CE)", 21, "r. 1504–1534 CE", "1st Sultan of Sennar", "Allied with Abdallab Arab chieftain Abdallah Jamma to establish the Funj Sultanate.", True),
        ("nub9_abdallah_jamma", "Shaykh Abdallah Jamma & Shaykh Ajib al-Kafuta (Abdallab Arab Viceroys of Qerri)", 21, "1504–1611 CE", "Abdallab Viceroys of Northern Sudan"),
        ("nub9_ajib_kafuta", "Sultan Dakin & Sultan Unsa I (Late 16th–17th c. Sennar)", 21, "1568–1616 CE", "Funj Sultans"),
        ("nub9_badi2_sennar", "Sultan Badi II Abu Diqn (Golden Age of Sennar Mosque, 1644–1681 CE)", 21, "r. 1644–1681 CE", "Sultan of Sennar"),
        ("nub9_badi4_sennar", "Sultan Badi IV Abu Shulukh (Defeated Iyasu II of Ethiopia at Dindar 1744)", 21, "r. 1724–1762 CE", "Sultan of Sennar"),
        ("nub9_badi7_sennar", "Sultan Badi VII of Sennar (Final Funj Sultan, 1805–1821 CE)", 21, "r. 1805–1821 CE", "Last Sultan of Sennar"),
    ], "african", "1504–1821 CE", ["Funj Chronicle", "Arkell History of Sudan"])
    nodes.append(N("nub9_darfur_sulayman_solong", "Sultan Sulayman Solong (Keira Founder of Darfur, 1603–1637 CE) → Sultan Ali Dinar (d. 1916)", "african", 21, "17th–20th c. CE", "Keira Sultans of Darfur", ["MacMichael Vol. 1", "Arkell History of Sudan"], "Traditional Keira dynasty of Darfur claimed descent from Banu Hilal & Abbasid/Tunjur links."))
    edges += [
        E("nub9_abdallah_jamma", "sud_jaaliyyin_abbas", "expansion", "Arab-Sudanese Ja'aliyyin & Abdallab alliance on the Main Nile"),
        E("nub9_amara_dunqas", "nub9_darfur_sulayman_solong", "expansion", "Westward Sudanese Islamic sultanates (Sennar & Darfur)"),
    ]

    # =========================================================================
    # SECTION E: SOUTH INDIA (DECCAN/CHOLAS/VIJAYANAGARA/MARATHAS) & PORTUGUESE ASIA (24 nodes)
    # =========================================================================
    add_chain(nodes, edges, "mon_ind_harsha", [
        ("ind9_pulakeshin2", "Emperor Pulakeshin II of Vatapi (Badami Chalukya; Defeated Harsha & Diplomatic Envoy to Khosrow II)", 19, "r. 610–642 CE", "Chalukya Emperor of the Deccan", "Checked Harshavardhana at the Narmada and exchanged embassies with Sasanian Persia.", True),
        ("ind9_simhavishnu_mahendravarman", "Kings Simhavishnu & Mahendravarman I of Kanchi (Pallava Dynasty)", 19, "575–630 CE", "Pallava Kings of Kanchipuram"),
        ("ind9_narasimhavarman1", "Narasimhavarman I Mamalla (Builder of Mahabalipuram Shore Monuments, 630–668 CE)", 19, "r. 630–668 CE", "Great Pallava King"),
        ("ind9_dantidurga_rashtrakuta", "Dantidurga → Krishna I (Ellora Kailasa Temple; Rashtrakuta Founders, 753–774 CE)", 19, "735–774 CE", "Rashtrakuta Founders"),
        ("ind9_amoghavarsha", "Emperor Amoghavarsha I Nrupatunga (Author of Kavirajamarga, 814–878 CE)", 19, "800–878 CE", "Rashtrakuta Emperor"),
    ], "vedic", "6th–9th c. CE", ["Rickmers Chronology of India", "Epigraphia Indica"])

    nodes += [
        N("ind9_vijayalaya_aditya", "Vijayalaya Chola → Aditya I → Parantaka I (Imperial Chola Founders, 848–955 CE)", "vedic", 19, "848–955 CE", "Chola Emperors", ["Rickmers Chronology of India", "Chola Copper Plates"], "Ancestors of Rajaraja Chola I."),
        N("ind9_kulottunga1", "Emperor Kulottunga Chola I (Eastern Chalukya–Chola Union, r. 1070–1122 CE)", "vedic", 20, "1029–1122 CE", "Chalukya-Chola Emperor", ["Rickmers Chronology of India"], "Grandson of Rajendra Chola I via his daughter Ammangadevi."),
        N("ind9_sundara_pandya", "Jatavarman Sundara Pandyan I (Second Pandyan Empire, r. 1251–1268 CE)", "vedic", 20, "r. 1251–1268 CE", "Pandyan Emperor", ["Rickmers Chronology of India", "Marco Polo"], "Expanded Pandyan sovereignty from Madurai across Sri Lanka & South India."),
        N("ind9_vishnuvardhana_hoysala", "King Vishnuvardhana of Hoysala (Belur & Halebidu, r. 1108–1152 CE) → Ballala III", "vedic", 20, "1108–1343 CE", "Hoysala Kings", ["Rickmers Chronology of India"], "Built Chennakesava Temple; bridged Karnataka power to Vijayanagara."),
        N("ind9_rudrama_devi", "Rani Rudrama Devi of Warangal (Kakatiya Queen Regnant, r. 1262–1289 CE)", "vedic", 20, "r. 1262–1289 CE", "Kakatiya Sovereign Queen", ["Marco Polo", "Rickmers Chronology of India"], "One of India's few sovereign queens regnant; praised in Marco Polo's travels.", True),
    ]
    edges += [
        E("ind9_vijayalaya_aditya", "mon_ind_rajaraja1", "direct", "Imperial Chola grandfather-to-grandson line"),
        E("mon_ind_rajendra1", "ind9_kulottunga1", "direct", "Grandson of Rajendra Chola I via daughter Ammangadevi"),
        E("mon_ind_rajendra1", "sea_java_raden_wijaya", "expansion", "1025 CE Chola Naval Expedition across Srivijaya & Malay Peninsula"),
        E("mon_ind_rajendra1", "ind9_sundara_pandya", "expansion", "Chola–Pandya South Indian sovereignty"),
        E("ind9_kulottunga1", "ind9_vishnuvardhana_hoysala", "expansion", "12th c. Karnataka–Tamil royal contemporaries"),
        E("ind9_sundara_pandya", "ind9_rudrama_devi", "expansion", "13th c. Deccan–South India contemporary sovereigns"),
    ]

    nodes += [
        N("ind9_harihara_bukka", "Harihara I & Bukka Raya I (Sangama Founders of Vijayanagara Empire, 1336 CE)", "vedic", 20, "1336–1377 CE", "Founders of Vijayanagara", ["Rickmers Chronology", "Portuguese Asia"], "Former Hoysala/Kakatiya commanders who founded Vijayanagara at Hampi."),
        N("ind9_rama_raya_talikota", "Aliya Rama Raya & Venkatapati Deva Raya (Aravidu Dynasty after 1565)", "vedic", 21, "1542–1614 CE", "Vijayanagara Regents & Aravidu Kings", ["Faria y Sousa Portuguese Asia"], "Son-in-law of Krishnadevaraya; fell at Talikota (1565)."),
        N("ind9_chand_bibi", "Sultana Chand Bibi of Bijapur & Ahmadnagar (Defended Deccan vs Akbar, 1550–1599 CE)", "vedic", 21, "1550–1599 CE", "Deccan Sovereign Warrior Queen", ["Faria y Sousa", "Mughal Akbarnama"], "Regent of both Bijapur and Ahmadnagar; famously defended Ahmadnagar against Akbar's forces.", True),
        N("ind9_ibrahim_adil_shah2", "Sultan Ibrahim Adil Shah II of Bijapur (Author of Kitab-i-Nauras, 1580–1627 CE)", "vedic", 21, "1556–1627 CE", "Sultan of Bijapur", ["Mughal & Deccan Chronicles"], "Nephew of Chand Bibi; patron of Deccan music & architecture."),
        N("ind9_muhammad_quli_qutb", "Sultan Muhammad Quli Qutb Shah (Founder of Hyderabad & Charminar, 1580–1612 CE)", "vedic", 21, "1565–1612 CE", "Qutb Shahi Sultan of Golconda", ["Deccan Chronicles"], "Founded the city of Hyderabad in 1591 CE."),
        N("ind9_jijabai_shahaji", "Raja Shahaji Bhonsle & Rajmata Jijabai (Parents of Chhatrapati Shivaji)", "vedic", 21, "1594–1674 CE", "Maratha Founders' Parents", ["Maratha Bakhar Chronicles"], "Shahaji served Deccan sultanates; Jijabai (of Yadava Devagiri descent) raised Shivaji."),
        N("ind9_sambhaji_rajaram", "Chhatrapati Sambhaji, Rajaram I & Maharani Tarabai (Maratha Resistance vs Aurangzeb)", "vedic", 21, "1657–1761 CE", "Maratha Chhatrapatis & Regent Queen", ["Maratha Chronicles"], "Sons & daughter-in-law of Shivaji who preserved Maratha sovereignty."),
        N("ind9_shahu_baji_rao1", "Chhatrapati Shahu I & Peshwa Baji Rao I (Pan-Indian Maratha Confederacy, 1707–1740 CE)", "vedic", 21, "1682–1740 CE", "Maratha Sovereign & Peshwa", ["Maratha Chronicles"], "Expanded Maratha rule across Central & Northern India."),
    ]
    edges += [
        E("ind9_vishnuvardhana_hoysala", "ind9_harihara_bukka", "expansion", "Hoysala twilight -> Sangama founding of Vijayanagara (1336)"),
        E("ind9_harihara_bukka", "mon_ind_krishnadevaraya", "direct", "Vijayanagara imperial succession (Sangama -> Saluva -> Tuluva)"),
        E("mon_ind_krishnadevaraya", "ind9_rama_raya_talikota", "direct", "Son-in-law Aliya Rama Raya"),
        E("ind9_rama_raya_talikota", "ind9_chand_bibi", "expansion", "1565 Deccan Sultanate coalition"),
        E("ind9_chand_bibi", "mon_mug_akbar_ind", "expansion", "1596 Siege of Ahmadnagar: Chand Bibi vs Mughal Empire under Akbar"),
        E("ind9_chand_bibi", "ind9_ibrahim_adil_shah2", "direct", "Aunt & regent of Sultan Ibrahim Adil Shah II"),
        E("ind9_ibrahim_adil_shah2", "ind9_muhammad_quli_qutb", "expansion", "Deccan Sultanate alliance of Bijapur & Golconda-Hyderabad"),
        E("ind9_jijabai_shahaji", "mon_ind_shivaji", "direct", "Parents of Chhatrapati Shivaji"),
        E("mon_ind_shivaji", "ind9_sambhaji_rajaram", "direct", "Sons Sambhaji & Rajaram and Regent Tarabai"),
        E("ind9_sambhaji_rajaram", "ind9_shahu_baji_rao1", "direct", "Son of Sambhaji & Peshwa Baji Rao I"),
    ]

    add_chain(nodes, edges, "mon_por_manuel1", [
        ("ind9_francisco_almeida", "Dom Francisco de Almeida (1st Viceroy of Portuguese India, 1505–1509 CE)", 21, "1450–1510 CE", "1st Viceroy of Portuguese India"),
        ("ind9_afonso_albuquerque", "Afonso de Albuquerque (Goa 1510, Malacca 1511 & Hormuz; Governor of India)", 21, "1453–1515 CE", "Governor of Portuguese Asia", "Captured Goa (1510) and Malacca (1511), linking European & Southeast Asian crowns.", True),
        ("ind9_joao_de_castro", "Dom João de Castro (Viceroy of Portuguese India, 1545–1548 CE)", 21, "1500–1548 CE", "Viceroy of Portuguese India"),
    ], "europe_norse", "16th c. CE", ["Faria y Sousa Portuguese Asia", "History of Portugal 1726"])
    nodes += [
        N("ind9_zamorin_calicut", "Samoothiri / Zamorin of Calicut (Welcomed Vasco da Gama, 1498 CE)", "vedic", 21, "1498–1513 CE", "Sovereign of Kozhikode (Kerala)", ["Portuguese Asia", "Calicut Chronicles"], "Matrilineal Nediyiruppu Swaroopam ruler of the Malabar spice trade."),
        N("ind9_bahadur_shah_gujarat", "Sultan Bahadur Shah of Gujarat (1526–1537 CE; Treaty of Bassein & Diu)", "vedic", 21, "r. 1526–1537 CE", "Sultan of Gujarat", ["Portuguese Asia", "Mughal Humayunnama"], "Opponent of Humayun and Portuguese Diu governorate."),
        N("ind9_st_francis_xavier", "St. Francis Xavier (Navarrese Noble & First Jesuit Envoy to Goa, Malacca & Japan, 1542–1552)", "europe_norse", 21, "1506–1552 CE", "Basque-Navarrese Noble & Missionary", ["Portuguese Asia"], "Travelled from Lisbon through Goa & Malacca to Kagoshima, Japan (1549)."),
    ]
    edges += [
        E("ind9_afonso_albuquerque", "chr6_sultan_mahmud_shah", "expansion", "1511 CE Capture of Malacca: Albuquerque vs Sultan Mahmud Shah"),
        E("fam6_vasco_da_gama", "ind9_zamorin_calicut", "expansion", "1498 CE Landfall at Calicut: Vasco da Gama & the Zamorin"),
        E("ind9_afonso_albuquerque", "ind9_bahadur_shah_gujarat", "expansion", "16th c. Portuguese-Gujarati maritime treaties at Diu"),
        E("ind9_joao_de_castro", "ind9_st_francis_xavier", "expansion", "1545–1548 Portuguese Goa patronage of St. Francis Xavier"),
    ]

    # =========================================================================
    # SECTION F: CRUSADER JERUSALEM, HAUTEVILLES, MEDICI, ORANGE & LIVING SPAIN 2026 (26 nodes)
    # =========================================================================
    add_chain(nodes, edges, None, [
        ("eur9_godfrey_bouillon", "Godfrey of Bouillon (Advocate of the Holy Sepulchre, 1099–1100 CE)", 20, "1060–1100 CE", "1st Ruler of Crusader Jerusalem"),
        ("eur9_baldwin1_jerusalem", "King Baldwin I of Jerusalem (1100–1118 CE)", 20, "1060s–1118 CE", "1st King of Jerusalem"),
        ("eur9_baldwin2_jerusalem", "King Baldwin II of Jerusalem (Bourcq, 1118–1131 CE)", 20, "d. 1131 CE", "King of Jerusalem"),
        ("eur9_melisende_fulk", "Queen Melisende of Jerusalem (+ King Fulk V of Anjou; Grandfather of Henry II of England)", 20, "1105–1161 CE", "Queen Regnant of Jerusalem", "Melisende (Armenian-Frankish queen) & Fulk V of Anjou (father of Geoffrey Plantagenet -> Henry II).", True),
        ("eur9_amalric1_jerusalem", "King Amalric I of Jerusalem (+ Queen Maria Komnene, 1163–1174 CE)", 20, "1136–1174 CE", "King of Jerusalem"),
        ("eur9_baldwin4_leper", "King Baldwin IV the Leper of Jerusalem (Victory at Montgisard, 1174–1185 CE)", 20, "1161–1185 CE", "King of Jerusalem"),
        ("eur9_sibylla_isabella_jerusalem", "Queens Sibylla & Isabella I → Yolanda / Isabella II (+ Emperor Frederick II Hohenstaufen)", 20, "1160–1228 CE", "Heiresses of Jerusalem"),
    ], "europe_norse", "1099–1228 CE", ["William of Tyre", "Modern Universal History Vols. 8–9"])
    edges += [
        E("eur9_melisende_fulk", "mon_eng_henry2", "direct", "Father of Geoffrey of Anjou & grandfather of King Henry II Plantagenet"),
        E("eur9_amalric1_jerusalem", "byz8_maria_komnene_jerusalem", "direct", "1167 CE Marriage: King Amalric I & Byzantine Princess Maria Komnene"),
        E("eur9_sibylla_isabella_jerusalem", "mon_hre_frederick2", "expansion", "1225 CE Marriage: Isabella II of Jerusalem wed HRE Emperor Frederick II"),
    ]

    add_chain(nodes, edges, "mon_eng_william1", [
        ("eur9_tancred_hauteville", "Tancred of Hauteville (Norman Nobleman of Cotentin; Ancestor of Kings of Sicily)", 20, "c. 980–1041 CE", "Hauteville Founder"),
        ("eur9_robert_guiscard", "Robert Guiscard (Duke of Apulia & Calabria, 1059–1085 CE)", 20, "c. 1015–1085 CE", "Norman Duke of Apulia"),
        ("eur9_roger1_sicily", "Count Roger I Bosso of Sicily (Brother of Robert Guiscard, 1071–1101 CE)", 20, "c. 1031–1101 CE", "Great Count of Sicily"),
        ("eur9_roger2_sicily", "King Roger II of Sicily (Multicultural Norman-Arab-Byzantine Court at Palermo, 1130–1154)", 20, "1095–1154 CE", "1st King of Sicily", "patronized al-Idrisi's Tabula Rogeriana and united Sicily & Southern Italy.", True),
        ("eur9_constance_sicily", "Queen Constance of Sicily (+ HRE Emperor Henry VI; Mother of Frederick II, 1154–1198 CE)", 20, "1154–1198 CE", "Queen of Sicily & HRE Empress"),
    ], "europe_norse", "11th–12th c. CE", ["Modern Universal History Vol. 10", "Hauteville Chronicles"], default_type="expansion")
    edges.append(E("eur9_constance_sicily", "mon_hre_frederick2", "direct", "Mother of Emperor Frederick II Hohenstaufen"))

    add_chain(nodes, edges, None, [
        ("eur9_cosimo_medici", "Cosimo de' Medici ('Pater Patriae' of Florence, 1389–1464 CE)", 21, "1389–1464 CE", "Medici Founder of Florence"),
        ("eur9_lorenzo_magnificent", "Lorenzo de' Medici ('The Magnificent', Patron of Michelangelo & da Vinci, 1449–1492 CE)", 21, "1449–1492 CE", "Ruler of Florence", "Architect of Italian Renaissance diplomacy & art.", True),
        ("eur9_leo10_clement7", "Medici Popes Leo X & Clement VII → Alessandro & Duke Cosimo I de' Medici", 21, "1475–1574 CE", "Medici Popes & Grand Dukes of Tuscany"),
        ("eur9_catherine_medici", "Queen Catherine de' Medici (+ King Henry II of France; Mother of 3 French Kings, 1519–1589)", 21, "1519–1589 CE", "Queen of France & Valois Matriarch", "Great-granddaughter of Lorenzo the Magnificent; wed Henry II of France.", True),
        ("eur9_marie_medici", "Queen Marie de' Medici (+ King Henry IV of France; Mother of Louis XIII, 1575–1642)", 21, "1575–1642 CE", "Queen of France & Bourbon Matriarch"),
    ], "europe_norse", "15th–17th c. CE", ["Modern Universal History Vol. 9–11", "Anderson 1732"])
    nodes.append(N("eur9_francesco_ludovico_sforza", "Dukes Francesco I & Ludovico 'il Moro' Sforza of Milan (1450–1500 CE; Patrons of Leonardo)", "europe_norse", 21, "1401–1508 CE", "Sforza Dukes of Milan", ["Modern Universal History Vol. 11"], "Allies & marriage kin of the Medici and Gonzaga courts."))
    edges += [
        E("eur9_lorenzo_magnificent", "eur9_francesco_ludovico_sforza", "expansion", "15th c. Florence–Milan Renaissance alliance"),
        E("eur9_catherine_medici", "mon_fra_henry2", "direct", "1533 CE Marriage: Catherine de' Medici & King Henry II of France"),
        E("eur9_marie_medici", "mon_fra_henry4", "direct", "1600 CE Marriage: Marie de' Medici & King Henry IV of France"),
    ]

    add_chain(nodes, edges, None, [
        ("eur9_william_silent", "William I the Silent, Prince of Orange (Founder of Dutch Republic, 1533–1584 CE)", 21, "1533–1584 CE", "Father of the Netherlands", "Married Anna of Saxony & Louise de Coligny; ancestor of Dutch monarchs & British King William III.", True),
        ("eur9_maurice_frederick_nassau", "Princes Maurice & Frederick Henry of Orange-Nassau (1567–1647 CE)", 21, "1567–1647 CE", "Stadtholders of the Dutch Republic"),
        ("eur9_william2_orange", "Prince William II of Orange (+ Princess Mary Stuart, Daughter of Charles I, 1626–1650)", 21, "1626–1650 CE", "Prince of Orange & Father of William III"),
    ], "europe_norse", "16th–17th c. CE", ["Modern Universal History Vol. 13", "Anderson 1732"])
    edges.append(E("eur9_william2_orange", "mon_eng_william_mary", "direct", "Father of King William III of England & Orange"))

    add_chain(nodes, edges, "mon_esp_philip5", [
        ("eur9_charles3_spain", "King Charles III → Charles IV → Ferdinand VII of Bourbon Spain (1759–1833 CE)", 21, "1716–1833 CE", "Bourbon Kings of Spain"),
        ("eur9_isabella2_spain", "Queen Isabella II & King Alfonso XII of Spain (1833–1885 CE)", 21, "1830–1885 CE", "Spanish Bourbon Monarchs"),
        ("eur9_alfonso13_spain", "King Alfonso XIII (+ Victoria Eugenie of Battenberg, Granddaughter of Queen Victoria, 1886–1941)", 21, "1886–1941 CE", "King of Spain"),
        ("eur9_juan_carlos1", "King Juan Carlos I (+ Queen Sofía of Greece, 1938–Present; r. 1975–2014)", 21, "1938–Present CE", "King Emeritus of Spain (Living 2026)"),
        ("eur9_felipe6_leonor_2026", "LIVING (2026): King Felipe VI of Spain & Princess Leonor of Asturias", 21, "1968–Present CE", "Reigning King of Spain & Heir (Living 2026)", "Present-day reigning Bourbon monarch of Spain, carrying Capetian, Habsburg, Wessex & Windsor lines to 2026.", True),
    ], "europe_norse", "18th c. – 2026 CE", ["Almanach de Gotha", "Casa Real de España"])

    return {
        "module": "51_wave9_gaelic_welsh_roman_nubia_deccan_crusaders",
        "title": "Wave 9: Gaelic/Scottish, Welsh, Roman/Pausanias, Nubia/Funj, South India/Portuguese Asia, Crusaders/Medici & Living Spain 2026",
        "nodes": nodes,
        "edges": edges,
    }
