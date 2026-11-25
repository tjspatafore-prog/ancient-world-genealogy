"""
Module 26: Noahic & Biblical Bridges Across Russia, Armenia, the Goths,
Ireland, Scotland, Wales, Germany, Spain, Gaul & Italy.

Sources integrated:
- Russian Primary Chronicle (Laurentian Text, a011458.pdf pp. 51-64)
- Movses Khorenatsi, History of the Armenians (Book I, Xorenatsi_1913_grabar.pdf)
- Jordanes, Origin and Deeds of the Goths (Getica, gothichistoryofj00jorduoft.pdf)
- John O'Hart, Irish Pedigrees (cu31924092516297.pdf & irishpedigreeso02ohar.pdf)
- W.F. Skene, Chronicles of the Picts & Scots (chroniclesofpict00sken.pdf) & Four Ancient Books of Wales
- Brut y Tywysogion (brutytywysogiono00cara.pdf)
- James Anderson, Royal Genealogies (1732 EPUB)
- Flavius Josephus, Complete Works / Antiquities I.6 (complete.pdf)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    # 1. Russia & Slavs (Russian Primary Chronicle)
    nodes += [
        N("rus_japheth_slavs", "Slavs (Norici) & Rus' — Lot of Japheth", "europe_norse", 7,
          "Post-Flood Division (Russian Primary Chronicle pp. 51-53)",
          "Japhethic Ancestors of the Russians, Varangians & Slavic Nations",
          ["Russian Primary Chronicle (Laurentian Text pp. 51-53)", "Al-Tabari Vol. 2", "Al-Mas'udi"],
          "Opening genealogy of the Rus' Primary Chronicle: after the Flood, Japheth received the northern/western rivers (Danube, Dnieper, Volga, Baltic/Varangian Sea), explicitly numbering Rus', Varangians, Slavs (Norici), Moravians, Czechs, White Croats, Serbs, Polyanians, Derevlians & Poles (Lyakhs) in the race of Japheth.",
          ["Slavs (Norici)", "Lot of Japheth", "Saqalibah"], major=True),
        N("rus_kiev_founders", "Kiy, Shchek, Khoriv & Sister Lybed' (Founders of Kiev)", "europe_norse", 18,
          "Early Polyanian Princes (Russian Primary Chronicle p. 55)",
          "Legendary Eponymous Founders of Kiev",
          ["Russian Primary Chronicle (Laurentian Text pp. 55-56)"],
          "Three Polyanian Slavic brothers Kiy, Shchek, Khoriv and sister Lybed' founded Kiev on the Dnieper; Lyakh brothers Radim & Vyatko founded the Radimichians & Vyatichians.",
          ["Kiy of Kiev", "Radim & Vyatko"], major=True),
        N("rus_rurik_dynasty", "Rurik (+ Sineus & Truvor, 862 CE) → Oleg & Igor' (+ St. Olga of Kiev)", "europe_norse", 19,
          "862–969 CE (Varangian Founders of Rus')",
          "Varangian-Japhethic Founders of the Rurikid Dynasty",
          ["Russian Primary Chronicle (Laurentian Text pp. 52, 60-64)", "Anderson 1732 Royal Genealogies"],
          "Varangian prince Rurik (expressly placed under the race of Japheth in the Primary Chronicle p. 52) settled Novgorod with brothers Sineus & Truvor (862 CE); regent Oleg united Novgorod & Kiev for Rurik's son Igor' and St. Olga of Pskov.",
          ["Rurik of Novgorod", "Prince Igor' & St. Olga"], major=True),
        N("rus_svyatoslav", "Svyatoslav I of Kiev (Son of Igor' & Olga)", "europe_norse", 19,
          "942–972 CE (Kievan Rus')",
          "Warrior Prince of Kievan Rus'",
          ["Russian Primary Chronicle (Laurentian Text p. 59)"],
          "Son of Igor' and St. Olga; campaigned across the Volga, Khazaria, and the Danube; father of Vladimir the Great.",
          ["Svyatoslav Igorevich"], major=False),
        N("rus_vladimir_great", "St. Vladimir the Great of Kiev (Baptized Kievan Rus', 988 CE)", "europe_norse", 19,
          "958–1015 CE (Christianization of Rus')",
          "Grand Prince of Kiev",
          ["Russian Primary Chronicle (Laurentian Text p. 59)"],
          "Grandson of Rurik and St. Olga; married Byzantine Princess Anna Porphyrogenita and established Christianity across Rus' in 988 CE.",
          ["Vladimir I Svyatoslavich"], major=True),
        N("rus_yaroslav_wise", "Yaroslav the Wise (1019–1054 CE) → Royal Houses of Rus', France, Norway & Hungary", "europe_norse", 20,
          "978–1054 CE (Golden Age of Kievan Rus')",
          "Grand Prince of Kiev & Pan-European Ancestor",
          ["Russian Primary Chronicle (Laurentian Text p. 59)", "Anderson 1732 Royal Genealogies"],
          "Son of St. Vladimir; linked the Rurikid line into Western & Northern European monarchies through his daughters Anne of Kiev (Queen of France), Anastasia (Hungary) & Elisiv (Norway).",
          ["Yaroslav I Vladimirovich", "Anne of Kiev"], major=True),
    ]
    edges += [
        E("bib_japheth", "rus_japheth_slavs", "syncretic", "Russian Primary Chronicle pp. 51-53: After the Flood, Japheth's portion includes Rus', Varangians, Slavs (Norici on the Danube), Moravians, Czechs, White Croats, Serbs & Poles (Lyakhs)"),
        E("rus_japheth_slavs", "eur_slavic_brothers", "cognate", "Parallel Slavic ethnonym tradition linking Japheth's Slavic lot with Lech, Czech & Rus"),
        E("rus_japheth_slavs", "rus_kiev_founders", "expansion", "Russian Primary Chronicle p. 55: Polyanian Slavic founders of Kiev; plus Radim (Radimichians) & Vyatko (Vyatichians)"),
        E("rus_japheth_slavs", "rus_rurik_dynasty", "expansion", "Russian Primary Chronicle pp. 52 & 60: Varangian Russes of the race of Japheth invited to Novgorod & Kiev"),
        E("eur_rurik_harald_viking", "rus_rurik_dynasty", "cognate", "Same Rurikid dynasty of Novgorod and Kiev"),
        E("rus_rurik_dynasty", "rus_svyatoslav", "direct", "Father-to-son succession: Rurik -> Igor' (+ St. Olga) -> Svyatoslav I"),
        E("rus_svyatoslav", "rus_vladimir_great", "direct", "Father-to-son succession (Russian Primary Chronicle p. 59)"),
        E("rus_vladimir_great", "rus_yaroslav_wise", "direct", "Russian Primary Chronicle; Anderson 1732: Father of Anne of Kiev (Queen of France), Anastasia (Hungary) & Elisiv (Norway)"),
    ]

    # 2. Armenia (Movses Khorenatsi Book I)
    nodes += [
        N("arm_hayk_pat", "Hayk Nahapet (Patriarch of Armenia, Slayer of Bel/Nimrod)", "iranian", 8,
          "Post-Babel Horizon (Movses Khorenatsi I.5-11)",
          "Progenitor of the Armenian Nation",
          ["Movses Khorenatsi History of Armenia I.5-11", "Kartlis Tskhovreba"],
          "Movses Khorenatsi traces Hayk from Noah -> Japheth -> Gomer -> Tiras -> Togarmah (Torgom), describing his refusal to serve the tyrant Bel (Nimrod) at Babel and his victory over Bel near Lake Van.",
          ["Hayk", "Haos (Georgian Form)"], major=True),
        N("arm_haykid_line", "Aramaneak → Aramayis → Amasia → Gegham → Harma → Aram (Eponym of Armenia) → Ara the Handsome", "iranian", 9,
          "Haykid Patriarchs (Movses Khorenatsi I.12-15)",
          "Early Patriarchal Chiefs of Armenia",
          ["Movses Khorenatsi History of Armenia I.12-15"],
          "Direct Haykid generational succession in Movses Khorenatsi leading through Aram (from whom neighbors named Armenia) to Ara the Handsome, contemporary of Assyrian queen Semiramis.",
          ["Aramaneak", "Aram of Armenia", "Ara the Handsome"], major=True),
        N("arm_shambat_bagratuni", "Shambat (Jewish Noble Exiled by Nebuchadnezzar) → Armenian Bagratuni Dynasty", "biblical", 18,
          "6th c. BCE onward (Movses Khorenatsi I.22 & II.3)",
          "Judeo-Armenian Ancestor of the Bagratuni & Bagrationi Houses",
          ["Movses Khorenatsi History of Armenia I.22, II.3"],
          "Khorenatsi records that Armenian king Hracheay brought a prominent Jewish captive named Shambat (Smbat) from Nebuchadnezzar's Babylonian exile — establishing the Armenian Bagratuni & Georgian Bagrationi royal claim.",
          ["Shambat / Smbat", "Bagratids"], major=True),
    ]
    edges += [
        E("bib_togarmah", "arm_hayk_pat", "expansion", "Movses Khorenatsi Book I.5-10: Japheth -> Gomer -> Tiras/Togarmah -> Hayk, founder of Armenia who slew the giant Bel (Nimrod)"),
        E("geo_targamos_8sons", "arm_hayk_pat", "cognate", "Georgian chronicle identifies Targamos's firstborn son Haos directly with Armenian Hayk"),
        E("bib_nimrod", "arm_hayk_pat", "syncretic", "Khorenatsi I.10-11: Hayk defeats the Babylonian tyrant Bel (Nimrod) near Lake Van"),
        E("arm_hayk_pat", "arm_haykid_line", "direct", "Movses Khorenatsi Book I.12-15: Direct Haykid patriarchal succession; Ara the Handsome contemporary of Semiramis"),
        E("arm_haykid_line", "arm_shambat_bagratuni", "expansion", "Movses Khorenatsi I.22 & II.3: King Hracheay brings Jewish noble Shambat (Smbat) from Nebuchadnezzar's captives -> ancestor of Armenian Bagratunis & Georgian Bagrationis"),
    ]

    # 3. Goths (Jordanes Getica)
    nodes += [
        N("goth_magog_berig", "Goths / Scythians (Berig → Filimer) — Race of Magog", "europe_norse", 8,
          "Ancient Northern Migration (Jordanes Getica; Josephus)",
          "Japhethic Origin of the Gothic & Scythian Peoples",
          ["Jordanes Getica IV-V, XXIV", "Josephus Antiquities I.6.1"],
          "Jordanes (following Josephus) connects the Scythian & Gothic peoples to Magog son of Japheth and recounts King Berig leading three ships of Goths from Scandza across the Baltic to Gothiscandza, followed by Filimer to Oium.",
          ["Berig", "Filimer", "Getae / Scythians"], major=True),
        N("goth_amali_theoderic", "Gapt (Gaut) → Amal (Amali) → Hermanaric → Theoderic the Great (Ostrogoths) & Alaric I (Visigoths)", "europe_norse", 19,
          "1st–6th c. CE (Jordanes Getica XIII-LX)",
          "Royal Ostrogothic Amali & Visigothic Balthi Lines",
          ["Jordanes Getica XIII-LX"],
          "Complete royal genealogy of the Gothic Amali from Gapt (Gaut) -> Hulmul -> Augis -> Amal -> Ostrogotha -> Achiulf -> Hermanaric & Vandalarius -> Thiudimer -> Theoderic the Great, alongside Alaric I of the Visigoths.",
          ["Gapt / Gaut", "Hermanaric", "Theoderic the Great", "Alaric I"], major=True),
    ]
    edges += [
        E("bib_magog", "goth_magog_berig", "syncretic", "Jordanes Getica (citing Josephus): Scythians & Goths descend from Magog son of Japheth; King Berig leads Goths from Scandza"),
        E("goth_magog_berig", "goth_amali_theoderic", "expansion", "Jordanes Getica XIII-LX: Complete Amali & Balthae royal pedigrees"),
    ]

    # 4. Ireland, Scotland, Picts & Wales
    nodes += [
        N("irl_baath_fenius", "Baath (King of Scythia) → Fenius Farsa (Inventor of Letters at Shinar/Babel)", "europe_norse", 7,
          "Post-Babel Scythia (Annals of the Four Masters; O'Hart pp. 31-34)",
          "Magogian Patriarch of Gaelic & Scythian Learning",
          ["O'Hart Irish Pedigrees Part I pp. 31-35", "Annals of the Four Masters"],
          "O'Hart traces the stem of the Irish nation directly from Adam -> Seth -> ... -> Noah -> Japheth -> Magog -> Baath (King of Scythia) -> Fenius Farsa, who established a school of the 72 languages on the plain of Shinar after Babel.",
          ["Baath", "Fenius Farsa"], major=True),
        N("irl_niul_gaedhal", "Niul (+ Scota, Dau. of Pharaoh; Friend of Moses!) → Gaodhal Glas (Gael) → Asruth → Sruth → Heber Scot", "europe_norse", 9,
          "Mosaic Horizon (O'Hart pp. 6, 34-35)",
          "Egyptian-Milesian Bridge & Eponym of the Gaels",
          ["O'Hart Irish Pedigrees Part I pp. 6, 34-35", "Lebor Gabála Érenn"],
          "Fenius Farsa's younger son Niul was invited to Egypt by Pharaoh, married Princess Scota, befriended Moses & the Israelites at the Red Sea, and begat Gaodhal Glas (Gael), father of the Goidelic language and line through Asruth, Sruth & Heber Scot.",
          ["Niul", "Scota", "Gaodhal Glas", "Heber Scot"], major=True),
        N("irl_breoghan_milesius", "Breoghan (Brigus of Spain) → Bile → Milesius of Spain (Galamh)", "europe_norse", 12,
          "Gaelic-Iberian Horizon (O'Hart pp. 29-35)",
          "Progenitor of the Milesian High Kings of Ireland",
          ["O'Hart Irish Pedigrees Part I pp. 29-35"],
          "O'Hart generations #34-36 from Adam: Breoghan (Brigus, builder of Brigantia in Spain) -> Bile -> Galamh / Milesius of Spain, who married a second Pharaoh's daughter Scota.",
          ["Breoghan / Brigus", "Milesius / Galamh"], major=True),
        N("irl_milesian_sons", "Heber, Heremon, Ir & Uncle Ith (Milesian Monarchs of Ireland)", "europe_norse", 13,
          "Milesian Arrival in Ireland (O'Hart pp. 35-84)",
          "Joint Progenitors of the Major Irish & Scottish Houses",
          ["O'Hart Irish Pedigrees Part I pp. 49-84", "Annals of the Four Masters"],
          "Milesius's sons Heber (Munster lines), Heremon (Connacht, Leinster, High Kings & Dal Riada Scots), and Ir (Ulster), alongside uncle Ith, established the Milesian roll of Irish monarchs.",
          ["Heber Fionn", "Heremon", "Ir", "Ith"], major=True),
        N("irl_niall_brian_boru", "Conn of the Hundred Battles → Niall of the Nine Hostages (Uí Néill) & Brian Boru (Munster)", "europe_norse", 19,
          "2nd–11th c. CE (Irish Pedigrees)",
          "Historic High Kings of Ireland from Heremon & Heber",
          ["O'Hart Irish Pedigrees Parts I-II"],
          "Traces Heremon's line to Conn of the Hundred Battles -> Niall of the Nine Hostages (Uí Néill) and Heber's line to Brian Boru (d. 1014 CE) & MacCarthy/O'Brien families.",
          ["Niall of the Nine Hostages", "Brian Boru"], major=True),
        N("sco_picts_cruithne", "Cruithne (Founder of the Picts) → 7 Sons Dividing Alba (Fib, Fidach, Floclaid, Fortrenn, Got, Ce, Circinn)", "europe_norse", 10,
          "Pictish Origin Horizon (Pictish Chronicle pp. 209, 252)",
          "Eponymous Ancestor of the Picts of Alba (Scotland)",
          ["Skene Chronicles of the Picts & Scots pp. 209-252"],
          "The Pictish Chronicle derives both Scots and Picts from Scythia/Albani (Noah -> Japheth -> Magog/Gomer), recording Cruithne and his seven sons giving their names to the seven provinces of Pictish Scotland.",
          ["Cruithne mac Cinge", "7 Pictish Provinces"], major=True),
        N("sco_fergus_macalpin", "Fergus Mor mac Erc (King of Dal Riada, 498 CE) → Kenneth MacAlpin (1st King of Scots & Picts, 843 CE)", "europe_norse", 19,
          "498–858 CE (Dal Riada & Kingdom of Alba)",
          "Unifier of the Picts & Scots into the Scottish Crown",
          ["Skene Chronicles of the Picts & Scots pp. cx, 44", "O'Hart Irish Pedigrees"],
          "Fergus Mor mac Erc crossed from Irish Dal Riada (Heremon's Milesian line) to Argyll in 498 CE; his descendant Cináed mac Ailpín (Kenneth MacAlpin) united the Scottish and Pictish kingdoms in 843 CE.",
          ["Fergus Mor mac Erc", "Kenneth MacAlpin"], major=True),
        N("wal_cunedda_rhodri_llywelyn", "Cunedda → Cadwaladr → Rhodri Mawr → Hywel Dda → Llywelyn the Great (Princes of Wales)", "europe_norse", 19,
          "5th–13th c. CE (Brut y Tywysogion; Four Ancient Books of Wales)",
          "Welsh Royal Succession Descended from Brutus of Troy & Camber",
          ["Brut y Tywysogion (Caradoc / Williams ed.)", "Skene Four Ancient Books of Wales"],
          "Follows the Welsh chronicle tradition from Cunedda Wledig and Cadwaladr the Blessed through Rhodri Mawr (the Great), lawgiver Hywel Dda, Gruffudd ap Rhys & Llywelyn the Great, tracing Welsh sovereignty back to Brutus of Troy & Camber.",
          ["Cunedda Wledig", "Rhodri Mawr", "Hywel Dda", "Llywelyn the Great"], major=True),
    ]
    edges += [
        E("bib_magog", "irl_baath_fenius", "expansion", "O'Hart Irish Pedigrees Part I pp. 31-34 (Annals of the Four Masters): Adam -> Noah -> Japheth -> Magog -> Baath -> Fenius Farsa, founder of the school of 72 languages at Shinar"),
        E("irl_baath_fenius", "irl_niul_gaedhal", "direct", "O'Hart Part I pp. 6, 34-35: Fenius Farsa -> Niul (+ Princess Scota of Egypt) -> Gaodhal Glas -> Asruth -> Sruth -> Heber Scot"),
        E("irl_niul_gaedhal", "eur_scota_goidel", "cognate", "Same Milesian-Scota stem in O'Hart & Lebor Gabála Érenn"),
        E("irl_niul_gaedhal", "irl_breoghan_milesius", "direct", "O'Hart Part I pp. 29-35: Gen 34-36 from Adam via Agnon, Lamhfionn, Heber Glunfionn & Bratha"),
        E("irl_breoghan_milesius", "irl_milesian_sons", "direct", "Milesius of Spain -> Heber, Heremon & Ir (+ Uncle Ith)"),
        E("irl_milesian_sons", "irl_niall_brian_boru", "direct", "O'Hart Irish Pedigrees: Heremon -> Niall of the Nine Hostages; Heber -> Brian Boru (d. 1014)"),
        E("irl_milesian_sons", "sco_fergus_macalpin", "direct", "Skene Chronicles of the Picts & Scots pp. cx, 44; O'Hart: Milesian Heremon line -> Royal House of Scotland"),
        E("bib_magog", "sco_picts_cruithne", "syncretic", "Skene Pictish Chronicle pp. 209-252: Picts & Scots from Scythia/Albani (Japheth/Magog/Gomer)"),
        E("sco_picts_cruithne", "sco_fergus_macalpin", "expansion", "Union of Picts & Scots under Kenneth MacAlpin"),
        E("eur_brutus_troy", "wal_cunedda_rhodri_llywelyn", "expansion", "Brut y Tywysogion & Skene Four Ancient Books of Wales: Continuing British royal line from Brutus of Troy & Camber"),
    ]

    # 5. Germany, Spain, Gaul/France & Italy (Anderson 1732 & Josephus)
    nodes += [
        N("eur_ashkenaz_tuisco", "Ashkenaz = Tuisco / Tuisto (1st King of Germany)", "europe_norse", 8,
          "Post-Babel Germany (Anderson 1732 p. 464)",
          "Japhethic Patriarch of Germanic Peoples in Classical Chronography",
          ["James Anderson Royal Genealogies (1732 p. 464)", "Aventinus"],
          "Anderson Table p. 464 identifies Japheth's grandson Ashkenaz (Askanez) with Tacitus & Aventinus's Tuisco/Tuisto, pioneer ruler near the Tanais and Germany.",
          ["Tuisco / Tuisto", "Askanez"], major=True),
        N("eur_tubal_spain", "Tubal (Progenitor of Iberia / Ancient Kings of Spain)", "europe_norse", 7,
          "Post-Flood Iberia (Josephus Ant. I.6.1; Anderson 1732)",
          "Japhethic Founder of the Iberians of Spain",
          ["Josephus Antiquities I.6.1", "James Anderson Royal Genealogies (1732)"],
          "Josephus Antiquities I.6.1 identifies Tubal son of Japheth with the Iberi ('Thobelites'), later joined in royal chronologies to the ancient kingdoms of Spain.",
          ["Thobel / Iberi"], major=True),
        N("eur_gomer_samothes_gaul", "Gomer / Samothes (Progenitor of Gauls / Celts / Cimbri)", "europe_norse", 7,
          "Post-Flood Gaul & Britain (Josephus Ant. I.6.1; Anderson 1732 p. 464)",
          "Japhethic Patriarch of the Cimmerians, Cimbri, Celts & Gauls",
          ["Josephus Antiquities I.6.1", "James Anderson Royal Genealogies (1732 p. 464)"],
          "Josephus states 'Gomer founded those whom the Greeks now call Galatians [Gauls], but were then called Gomerites'; Anderson links Gomer (Cimbri) and his son Samothes/Meshech to the Celts.",
          ["Gomerites / Galatians", "Samothes", "Cimbri"], major=True),
        N("eur_noah_janus_italy", "Noah = Janus / Ogyges → Sabatius Saga → Italus (Ancient Kings of Italy / Tuscany)", "greek", 7,
          "Annius / Anderson Chronography (1732 Table CCCCXXIV p. 702)",
          "Renaissance-Baroque Noahic Synchronization of Pre-Roman Italy",
          ["James Anderson Royal Genealogies (1732 Table CCCCXXIV p. 702)"],
          "Anderson Table CCCCXXIV places Noah (identified as Janus / Ogyges) planting colonies in Italy with Gomer & Kittim, succeeded by Sabatius Saga and the ancient Kings of Tuscany & Italy.",
          ["Janus (Noah)", "Sabatius Saga", "Kings of Tuscany"], major=False),
    ]
    edges += [
        E("bib_ashkenaz", "eur_ashkenaz_tuisco", "syncretic", "Anderson 1732 Royal Genealogies p. 464: Noah -> Japheth -> Gomer -> Ashkenaz, called Tuisco/Tuisto, progenitor of Germans"),
        E("eur_ashkenaz_tuisco", "eur_tuisto_mannus", "cognate", "Same Tuisto/Mannus root synchronized with Gomer -> Ashkenaz"),
        E("bib_tubal", "eur_tubal_spain", "syncretic", "Josephus Antiquities I.6.1 & Anderson 1732: Tubal son of Japheth founded the Iberians/Spaniards"),
        E("bib_gomer", "eur_gomer_samothes_gaul", "syncretic", "Josephus Antiquities I.6.1 & Anderson 1732 p. 464: Gomer founded the Gomerites/Gauls/Cimbri"),
        E("bib_noah", "eur_noah_janus_italy", "syncretic", "Anderson 1732 Table CCCCXXIV p. 702: Chronicler bridge equating Noah with Janus & Gomer/Kittim planting Italy"),
        E("bib_kittim", "eur_noah_janus_italy", "syncretic", "Kittim / Cethim linked to Italian/Latin antiquity alongside Janus"),
    ]

    return {
        "module": "26_russia_armenia_europe_noahic",
        "title": "Noahic Lineages of Russia, Armenia, the Goths, Ireland, Scotland, Wales, Germany, Spain, Gaul & Italy",
        "nodes": nodes,
        "edges": edges,
    }
