"""
Module 34: Juan de Mariana's Spain (from Tubal b. Japheth to Habsburgs),
Aylett Sammes's Phoenician Britain, Strutt & Caesar's Ancient British Kings,
Venerable Bede's Anglo-Saxon Heptarchy, Mézeray's France & Sandford's Portugal.

Sources integrated:
- Juan de Mariana, The General History of Spain (tr. John Stevens, 1699, Book I Ch. I p. 1)
- Aylett Sammes, Britannia Antiqua Illustrata / Antiquities of Ancient Britain Until 800 (1676, p. 2)
- Venerable Bede, Ecclesiastical History of the English Nation (1723 ed.)
- Joseph Strutt, Chronicle of England: Ancient Britons and Saxons (1779) & Julius Caesar Commentaries
- François Eudes de Mézeray, A General Chronological History of France (1683, p. 10)
- Francis Sandford, A Genealogical History of the Kings of Portugal (1662, pp. 2-3)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("esp_mariana_tubal_iberia",
          "Mariana's General History of Spain (1699 Book I Ch. I): Tubal (5th Son of Japheth, 131 yrs after Flood) → Ancient Kings of Spain",
          "europe_norse", 7,
          "Post-Flood Dispersion (Mariana 1699 Book I Ch. I p. 1)",
          "Spaniards Traced Directly from Tubal, 5th Son of Japheth",
          ["Juan de Mariana The General History of Spain (tr. Stevens 1699) Book I Ch. I p. 1"],
          "Mariana opens his monumental history of Spain (p. 1): 'Tubal, the son of Japheth, was the first man that peopled Spain after the Flood... the 5th son of Japheth, was sent to the farthest regions westward, that is, to Spain, where he founded the Spanish monarchy.'",
          ["Tubal in Spain", "Hesperia / Celtiberia"],
          major=True),

        N("esp_visigoths_reccared_roderick",
          "Visigothic Kingdom of Spain (Mariana 1699): Ataulf → Leovigild → King Reccared I (589 CE) → King Roderick (711 CE)",
          "europe_norse", 19,
          "415–711 CE (Mariana 1699)",
          "Gothic Sovereigns of Hispania Bridged to Islamic Al-Andalus",
          ["Juan de Mariana The General History of Spain (1699)"],
          "Traces Visigothic Hispania from Alaric's successor Ataulf and Toledo unifier Leovigild to King Reccared I (589 CE) and last Visigothic king Roderick (711 CE).",
          ["Ataulf", "Leovigild", "Reccared I", "King Roderick"],
          major=True),

        N("esp_pelayo_castile_aragon",
          "Reconquista Spain (Mariana 1699): Don Pelayo of Asturias (718) → Alfonso VI of Castile & Leon → Ferdinand III & James I of Aragon",
          "europe_norse", 20,
          "718–13th c. CE (Mariana 1699)",
          "Asturian, Castilian, Leonese & Aragonese Christian Crowns",
          ["Juan de Mariana The General History of Spain (1699)"],
          "Follows the Christian continuity from Don Pelayo at Covadonga (718 CE) through Alfonso VI of Castile and Leon (father-in-law of Count Henry of Burgundy/Portugal), St. Ferdinand III, and James I the Conqueror of Aragon.",
          ["Don Pelayo", "Alfonso VI", "St. Ferdinand III", "James I of Aragon"],
          major=True),

        N("esp_ferdinand_isabella_habsburg",
          "Unified Catholic & Habsburg Spain (Mariana 1699): Ferdinand of Aragon & Isabella of Castile (1492) → Emperor Charles V → King Philip II",
          "europe_norse", 21,
          "1469–1598 CE (Mariana 1699)",
          "Unifiers of Aragon & Castile and Spanish Habsburg Dynasty",
          ["Juan de Mariana The General History of Spain (1699)"],
          "Unites Castile and Aragon under Ferdinand II and Isabella I (1492), continuing through Joanna the Mad and Philip the Handsome to Emperor Charles V (Charles I of Spain) and King Philip II.",
          ["Ferdinand & Isabella", "Emperor Charles V", "King Philip II"],
          major=True),

        N("bri_sammes_phoenicians_britain",
          "Aylett Sammes's Phoenician Britain (1676): Tyre & Sidon Tin Trade ('Bratanac') + Cimmerian / Gomerite Britons",
          "europe_norse", 9,
          "Bronze Age Britain (Aylett Sammes 1676 p. 2)",
          "Phoenician & Cimmerian-Gomerite Origin of Ancient Britain",
          ["Aylett Sammes Antiquities of Ancient Britain (1676) p. 2"],
          "Sammes rejects later fables in favor of classical Phoenician sources, arguing that Phoenician navigators from Sidon and Tyre ('Barat-anac' / land of tin) discovered and settled Britain alongside Gomerite Cimmerian peoples.",
          ["Phoenician Britain", "Bratanac (Tin)", "Sammes 1676"],
          major=True),

        N("bri_strutt_cassivellaunus_boadicea",
          "Ancient British Kings vs. Rome (Strutt 1779 & Caesar Commentaries): Cassivellaunus (54 BCE) → Cunobelinus → Caractacus & Queen Boadicea",
          "europe_norse", 18,
          "55 BCE – 61 CE (Strutt 1779; Julius Caesar Commentaries)",
          "Pre-Roman & Early Romano-British Dynasty",
          ["Joseph Strutt Chronicle of England (1779) p. 3", "Julius Caesar Commentaries"],
          "Combines Caesar's eyewitness Commentaries (55-54 BCE) and Strutt's Chronicle of England: Cassivellaunus (commander against Julius Caesar) -> Tasciovanus -> Cunobelinus ('Cymbeline') -> Caractacus, alongside Iceni Queen Boadicea.",
          ["Cassivellaunus", "Cunobelinus", "Caractacus", "Boadicea"],
          major=False),

        N("bri_bede_heptarchy_woden",
          "Venerable Bede's Anglo-Saxon Heptarchy (731 CE): Hengist & Horsa (from Woden) → King Ethelbert of Kent, Edwin & St. Oswald of Northumbria & Offa of Mercia",
          "europe_norse", 19,
          "449–796 CE (Venerable Bede 1723 ed.; Strutt 1779)",
          "Germanic-Wodenic Kingdoms of the Anglo-Saxon Heptarchy",
          ["Venerable Bede Ecclesiastical History of the English Nation (1723 ed.)", "Joseph Strutt Chronicle of England (1779)"],
          "Bede explicitly traces Kentish brothers Hengist & Horsa (and fellow Heptarchy dynasties of Kent, Northumbria, Mercia, East Anglia & Wessex) to Woden -> Ethelbert of Kent (baptized 597), St. Edwin & St. Oswald of Northumbria, and Offa of Mercia.",
          ["Hengist & Horsa", "Ethelbert of Kent", "St. Oswald", "Offa of Mercia"],
          major=True),

        N("fra_mezeray_pharamond_clovis",
          "Mézeray's First Race of France (1683): King Pharamond → Clodion → Meroveus (King III, Defeated Attila 451 CE) → Childeric I → Clovis I",
          "europe_norse", 19,
          "c. 420–511 CE (Mézeray 1683 p. 10)",
          "Salian Frankish Founders of the First Race (Merovingians)",
          ["François Eudes de Mézeray General Chronological History of France (1683) p. 10"],
          "Mézeray (1683) documents the First Race of French monarchs from Pharamond and Clodion through Meroveus (King III, p. 10, who allied with Aëtius and Theodoric against Attila at the Catalaunian Plains, 451 CE), Childeric I, and Clovis I.",
          ["Pharamond", "Clodion", "Meroveus", "Childeric I"],
          major=True),

        N("por_sandford_burgundy_capet",
          "Sandford's Genealogical Proof of Portugal (1662): Robert Duke of Burgundy (Capetian Male Line) → Count Henry of Burgundy → Kings of Portugal",
          "europe_norse", 20,
          "1032–1112 CE (Francis Sandford 1662 pp. 2-3)",
          "Strict Agnate Capetian Pedigree Refuting Alternative Legends for Count Henry",
          ["Francis Sandford Genealogical History of the Kings of Portugal (1662) pp. 2-3"],
          "Quoting Théodore Godefroy and ancient Fleury manuscripts (pp. 2-3), Sandford demonstrates Count Henry of Burgundy descended in direct male line from Robert the Pious & Robert I, Duke of Burgundy (House of France), marrying Alfonso VI's daughter Teresa in 1089/1090 to found Portugal's crown.",
          ["Robert I of Burgundy", "Count Henry of Bourgogne", "Théodore Godefroy"],
          major=False),
    ]

    edges += [
        E("bib_tubal", "esp_mariana_tubal_iberia", "syncretic", "Mariana 1699 Book I Ch. I p. 1: Tubal, 5th son of Japheth, first settled and founded the monarchy of Spain"),
        E("eur_tubal_spain", "esp_mariana_tubal_iberia", "cognate", "Same Japheth -> Tubal progenitor tradition across Josephus, Anderson & Mariana (1699)"),
        E("goth_amali_theoderic", "esp_visigoths_reccared_roderick", "direct", "Visigothic Balti succession from Alaric I -> Ataulf -> Leovigild -> Reccared -> Roderick (Mariana 1699)"),
        E("esp_mariana_tubal_iberia", "esp_visigoths_reccared_roderick", "expansion", "Hispania continuity from ancient Iberian realms into Visigothic Toledo (Mariana 1699)"),
        E("hak_futuh_misr_andalus", "esp_visigoths_reccared_roderick", "cognate", "711 CE conquest of Visigothic Spain recorded by both Ibn 'Abd al-Hakam & Mariana"),
        E("esp_visigoths_reccared_roderick", "esp_pelayo_castile_aragon", "expansion", "Mariana 1699: Visigothic noble Don Pelayo rallies Asturias (718 CE) -> Kings of Leon, Castile & Aragon"),
        E("esp_pelayo_castile_aragon", "esp_ferdinand_isabella_habsburg", "direct", "Mariana 1699: Direct Castile-Aragon marriage union (1469) -> Charles V -> Philip II"),
        E("esp_pelayo_castile_aragon", "por_afonso_henriques", "direct", "Sandford 1662 p. 3 & Mariana: King Alfonso VI of Castile gives daughter Teresa & County of Portugal to Henry of Burgundy"),
        E("bib_sidon", "bri_sammes_phoenicians_britain", "syncretic", "Sammes 1676 p. 2: Phoenician merchants from Sidon & Tyre colonized tin-rich Britain ('Bratanac')"),
        E("bib_canaan", "bri_sammes_phoenicians_britain", "syncretic", "Canaanite-Phoenician westward maritime expansion to Britain (Sammes 1676)"),
        E("eur_gomer_samothes_gaul", "bri_sammes_phoenicians_britain", "syncretic", "Sammes 1676 links early Britons with Continental Cimmerian / Gomerite peoples"),
        E("eur_brutus_troy", "bri_sammes_phoenicians_britain", "cognate", "Sammes 1676 critiques Brutus legend while mapping pre-Roman British antiquities"),
        E("bri_sammes_phoenicians_britain", "bri_strutt_cassivellaunus_boadicea", "expansion", "Pre-Roman British tribal continuity to Cassivellaunus, Cunobelinus & Caractacus (Strutt 1779 & Caesar)"),
        E("grk_julius_augustus", "bri_strutt_cassivellaunus_boadicea", "cognate", "Julius Caesar's 55-54 BCE British expeditions against Cassivellaunus (Caesar Commentaries; Strutt p. 3)"),
        E("eur_wessex_alfred_norman", "bri_bede_heptarchy_woden", "expansion", "Venerable Bede: Wodenic Heptarchy pedigrees shared with Cerdic & Wessex"),
        E("bri_strutt_cassivellaunus_boadicea", "bri_bede_heptarchy_woden", "expansion", "Strutt Chronicle of England: Transition from Romano-Britons to Hengist, Horsa & Anglo-Saxon Heptarchy"),
        E("eur_merovingian_carolingian", "fra_mezeray_pharamond_clovis", "cognate", "Mézeray 1683 p. 10 documents Pharamond -> Clodion -> Meroveus -> Childeric -> Clovis I"),
        E("fra_capet_stlouis", "por_sandford_burgundy_capet", "direct", "Sandford 1662 pp. 2-3 (Godefroy): Robert II of France -> Robert I Duke of Burgundy -> Count Henry of Burgundy"),
        E("por_sandford_burgundy_capet", "por_afonso_henriques", "direct", "Sandford 1662 p. 3: Count Henry of Burgundy + Teresa of Castile -> King Afonso I Henriques"),
    ]

    return {
        "module": "34_spain_britain_france_portugal_chronicles",
        "title": "Mariana's Spain (from Tubal), Sammes's Phoenician Britain, Strutt & Bede's Heptarchy, Mézeray's France & Sandford's Portugal",
        "nodes": nodes,
        "edges": edges,
    }
