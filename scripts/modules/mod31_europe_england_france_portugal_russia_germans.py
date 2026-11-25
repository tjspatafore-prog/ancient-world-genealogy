"""
Module 31: European Royal Dynasties & Ancient Germanic Confederations Rooted in Noah
(England/Britain, France, Burgundy, Savoy, Portugal & Romanov Russia).

Sources integrated:
- William Howell, Medulla Historiae Anglicanae / History of the Lives and Reigns of the Monarchs of England (1685)
- Sir Walter Raleigh, The History of the World (1736 Folio Preface p. ix on Stuart Union)
- John Jacob Mascou, The History of the Ancient Germans (1737)
- Tacitus, Germania (Complete Works Vols. 1-4)
- The Modern Part of an Universal History (Folio Vols. 8-14: France, Burgundy, Savoy, Russia)
- A Compendious Chronicle of the Kingdom of Portugal
- The History of Portugal (1661 & 1726) & The Portuguese Asia
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("ger_mascou_confederations",
          "Ancient Germanic Nations (Mascou 1737 & Tacitus): Cimbri & Teutones, Suevi, Alemanni, Saxons, Franks, Vandals (Gaiseric) & Lombards (Alboin)",
          "europe_norse", 18,
          "3rd c. BCE – 6th c. CE (J.J. Mascou 1737; Tacitus Germania)",
          "Early Germanic Tribal Confederations Rooted in Tuisto / Mannus / Ashkenaz",
          ["John Jacob Mascou History of the Ancient Germans (1737)", "Tacitus Germania"],
          "Mascou traces the major Germanic confederations from Tacitus's Tuisto and Mannus (linked in universal chronologies to Ashkenaz/Gomer) through the Cimbri & Teutones, Suevi, Alemanni, Saxons, Franks, Vandals (Gaiseric), and Lombards (Alboin).",
          ["Cimbri & Teutones", "Vandals (Gaiseric)", "Lombards (Alboin)", "Franks & Saxons"],
          major=True),

        N("bur_gonderic_gundobad",
          "Kingdom of Burgundy: King Gonderic → King Gundobad (Burgundian Law) → King Sigismund",
          "europe_norse", 19,
          "5th–6th c. CE (Mascou 1737; Mod. Univ. Hist. Vol. 14)",
          "Burgundian Royal House of the Rhone & Geneva",
          ["John Jacob Mascou History of the Ancient Germans (1737)", "Modern Universal History Vol. 14"],
          "Mascou and Modern Universal History Vol. 14 trace the Burgundian kings from Gonderic and Gundobad (codifier of Lex Burgundionum) to St. Sigismund before Frankish absorption and the later Kingdom of Burgundy/Arles.",
          ["Gonderic", "Gundobad", "King Sigismund"],
          major=False),

        N("sav_witichind_hubert_victor",
          "House of Savoy & Sardinia: Duke Witichind of Saxony (Contemp. of Charlemagne) → Bertold → Hubert of the White Hands → Amadeo → King Victor Amadeus I & II",
          "europe_norse", 20,
          "8th–18th c. CE (Mod. Univ. Hist. Vol. 14 pp. 125-140)",
          "Ducal House of Savoy & Royal House of Sardinia",
          ["Modern Universal History Vol. 14 pp. 125-140"],
          "Mod. Univ. Hist. Vol. 14 p. 125 derives the House of Savoy from Saxony's Duke Witichind (contemporary of Charlemagne) via Bertold (who received Savoy from Rodolf of Burgundy) and Hubert with the White Hands (d. c. 1050) to Amadeo and King Victor Amadeus II.",
          ["Witichind of Saxony", "Bertold", "Hubert of the White Hands", "Victor Amadeus II"],
          major=False),

        N("fra_capet_stlouis",
          "Capetian Kings of France: Hugh Capet (987 CE) → Henry I (+ Anne of Kiev!) → Philip II Augustus → St. Louis IX",
          "europe_norse", 20,
          "987–1270 CE (Mod. Univ. Hist. Vol. 9)",
          "Direct Capetian Dynasty Bridging Kievan Rus' & Western Europe",
          ["Modern Universal History Vol. 9 (History of France)"],
          "Hugh Capet (crowned 987 CE) founded the Capetian line; King Henry I married Yaroslav the Wise's daughter Anne of Kiev, uniting Rurikid Rus' and France through Philip II Augustus and St. Louis IX.",
          ["Hugh Capet", "Henry I & Anne of Kiev", "Philip II Augustus", "St. Louis IX"],
          major=True),

        N("fra_valois_bourbon",
          "Valois & Bourbon Kings of France: Philip VI → Francis I → Henry IV of Navarre (Bourbon, 1589) → Louis XIII → Louis XIV",
          "europe_norse", 21,
          "1328–1715 CE (Mod. Univ. Hist. Vol. 9)",
          "Cadet Capetian Royal Houses of Valois & Bourbon",
          ["Modern Universal History Vol. 9 (History of France)"],
          "Mod. Univ. Hist. Vol. 9 traces the Capetian cadet successions from Philip VI of Valois and Francis I to Henry IV of Navarre (first Bourbon King of France, 1589), Louis XIII, and Louis XIV.",
          ["Valois", "Henry IV of Bourbon", "Louis XIV"],
          major=True),

        N("eng_howell_roman_saxon",
          "Roman, British & Danish Rulers in Britain (Howell 1685): Julius Caesar → Claudius → King Lucius → King Canute (Cnut)",
          "europe_norse", 19,
          "55 BCE – 1042 CE (William Howell 1685 pp. 1-50)",
          "Roman Imperial Governors, British Kings & Danish Crown in England",
          ["William Howell Lives and Reigns of the Monarchs of England (1685)"],
          "Howell (1685) opens the English monarchy with Julius Caesar and Claudius, Christian British king Lucius, the Saxon Heptarchy unified under Egbert and Alfred the Great, and the Danish conquest under Canute (Cnut).",
          ["King Lucius", "King Canute"],
          major=False),

        N("eng_plantagenet_kings",
          "House of Plantagenet (England): Henry II → Richard I Lionheart → King John → Edward I → Edward III → Henry V",
          "europe_norse", 20,
          "1154–1485 CE (William Howell 1685)",
          "Angevin / Plantagenet Kings of England",
          ["William Howell Lives and Reigns of the Monarchs of England (1685)"],
          "Ascending from the Anglo-Norman & Wessex heritage via Empress Matilda, Henry II inaugurated the Plantagenet line leading through Richard I, King John, Edward I, Edward III, and Henry V.",
          ["Henry II", "Richard I", "Edward III", "Henry V"],
          major=True),

        N("eng_tudor_monarchs",
          "House of Tudor (Welsh-English Royal Union): Owen Tudor → Henry VII (1485) → Henry VIII → Edward VI → Queen Elizabeth I",
          "europe_norse", 21,
          "1485–1603 CE (William Howell 1685)",
          "Tudor Sovereigns Linking Welsh Princes & English Crown",
          ["William Howell Lives and Reigns of the Monarchs of England (1685)"],
          "Owen Tudor's grandson Henry VII (uniting Lancaster and York at Bosworth Field, 1485) brought Welsh royal pedigree onto the English throne through Henry VIII, Edward VI, and Elizabeth I.",
          ["Owen Tudor", "Henry VII", "Henry VIII", "Elizabeth I"],
          major=True),

        N("eng_stuart_great_britain",
          "House of Stuart (Union of Scotland & England): King James VI & I (1603) → Charles I → Charles II → James II",
          "europe_norse", 21,
          "1603–1688 CE (William Howell 1685; Raleigh 1736 Preface p. ix)",
          "Unified Crown of Great Britain (Scottish Milesian & English Tudor Union)",
          ["William Howell Lives and Reigns of the Monarchs of England (1685)", "Sir Walter Raleigh History of the World (1736 Preface p. ix)"],
          "Descended both from Scottish Dal Riada (Fergus Mor & Kenneth MacAlpin) and from Henry VII's daughter Margaret Tudor, King James VI of Scotland became James I of Great Britain in 1603 (celebrated in Raleigh's 1736 Preface p. ix), continuing through Charles I, Charles II, and James II.",
          ["James VI & I", "Charles I", "Charles II", "James II"],
          major=True),

        N("por_afonso_henriques",
          "Foundation of Portugal: Alfonso VI of Castile + Teresa & Count Henry of Burgundy → King Afonso I Henriques (1139, Battle of Ourique)",
          "europe_norse", 20,
          "1093–1185 CE (History of Portugal 1661 & 1726; Compendious Chronicle)",
          "Burgundian-Capetian Founder of the Kingdom of Portugal",
          ["History of Portugal (1661 & 1726)", "A Compendious Chronicle of the Kingdom of Portugal"],
          "Connecting Iberian monarchy (Tubal/Spain -> Castile) with the Capetian House of Burgundy: Count Henry of Burgundy married Alfonso VI's daughter Teresa, and their son Afonso I Henriques won independence at the Battle of Ourique (1139).",
          ["Count Henry of Burgundy", "Teresa of Leon", "Afonso I Henriques"],
          major=True),

        N("por_aviz_discoveries",
          "House of Aviz & Portuguese Asia: King John I → Prince Henry the Navigator → King Manuel I (Vasco da Gama to India, 1498)",
          "europe_norse", 21,
          "1385–1580 CE (History of Portugal 1661/1726; The Portuguese Asia)",
          "Aviz Dynasty & Oceanic Sea Route to East Africa & India",
          ["History of Portugal (1661 & 1726)", "Faria y Sousa The Portuguese Asia"],
          "King John I of Aviz (son-in-law of John of Gaunt / Plantagenet) and Prince Henry the Navigator launched the Atlantic voyages culminating under King Manuel I in Vasco da Gama's 1498 voyage to India.",
          ["King John I of Aviz", "Henry the Navigator", "King Manuel I"],
          major=True),

        N("por_braganza_restoration",
          "House of Braganza (Portuguese Restoration): King John IV (1640) → King Afonso VI (1656) → Peter II",
          "europe_norse", 21,
          "1640–1706 CE (History of Portugal 1661 & 1726)",
          "Royal House of Braganza",
          ["History of Portugal (1661 & 1726)", "A Compendious Chronicle of the Kingdom of Portugal"],
          "John, Duke of Braganza (descending from Afonso, son of King John I of Aviz), restored Portuguese independence as King John IV in 1640, succeeded by Afonso VI and Peter II.",
          ["King John IV", "King Afonso VI", "Peter II"],
          major=False),

        N("rus_nevsky_ivan_tsars",
          "Grand Princes & Tsars of Muscovy: St. Alexander Nevsky → Ivan III the Great (1480) → Tsar Ivan IV the Terrible",
          "europe_norse", 20,
          "1221–1584 CE (Mod. Univ. Hist. Vol. 13: History of Russia)",
          "Rurikid Grand Princes of Vladimir-Moscow & First Tsar of All Russia",
          ["Modern Universal History Vol. 13 (History of Russia)"],
          "Mod. Univ. Hist. Vol. 13 continues the Rurikid lineage from Yaroslav the Wise via St. Alexander Nevsky and Ivan III the Great (who ended Golden Horde tribute at the Ugra in 1480) to Tsar Ivan IV the Terrible.",
          ["Alexander Nevsky", "Ivan III the Great", "Ivan IV the Terrible"],
          major=True),

        N("rus_romanov_peter_great",
          "House of Romanov (Russian Empire): Tsar Michael I Romanov (1613) → Alexis I → Emperor Peter the Great (1682–1725)",
          "europe_norse", 21,
          "1613–1725 CE (Mod. Univ. Hist. Vol. 13: History of Russia)",
          "Imperial Romanov Dynasty of Russia",
          ["Modern Universal History Vol. 13 (History of Russia)"],
          "Connected to the Rurikids through Tsar Ivan IV's marriage to Anastasia Romanovna, the House of Romanov ascended in 1613 under Michael I, continuing via Alexis I to Emperor Peter the Great.",
          ["Michael I Romanov", "Alexis I", "Peter the Great"],
          major=True),
    ]

    edges += [
        E("eur_tuisto_mannus", "ger_mascou_confederations", "expansion", "Tacitus Germania & Mascou 1737: Ancient Germanic nations descending from Tuisto & Mannus"),
        E("eur_ashkenaz_tuisco", "ger_mascou_confederations", "expansion", "Chronicle identification of Tuisto/Ashkenaz with the founding ancestors of the Germans (Mascou)"),
        E("eur_gomer_samothes_gaul", "ger_mascou_confederations", "syncretic", "Mascou notes Cimbri & Celtic-Germanic antiquity linked to Gomerites"),
        E("goth_magog_berig", "ger_mascou_confederations", "cognate", "East Germanic Gothic peoples documented alongside Vandals, Lombards & Franks in Mascou"),
        E("ger_mascou_confederations", "eur_merovingian_carolingian", "expansion", "Salian & Ripuarian Franks establish Merovingian & Carolingian France/Germany"),
        E("ger_mascou_confederations", "bur_gonderic_gundobad", "expansion", "Mascou & Mod. Univ. Hist. Vol. 14: Germanic Burgundians -> Gonderic -> Gundobad -> Sigismund"),
        E("eur_merovingian_carolingian", "sav_witichind_hubert_victor", "expansion", "Mod. Univ. Hist. Vol. 14 p. 125: Saxon contemporary of Charlemagne Duke Witichind -> Savoy"),
        E("bur_gonderic_gundobad", "sav_witichind_hubert_victor", "expansion", "Mod. Univ. Hist. Vol. 14 p. 125: Bertold acquired Savoy & Maurienne under Rodolf of Burgundy"),
        E("eur_merovingian_carolingian", "fra_capet_stlouis", "expansion", "Mod. Univ. Hist. Vol. 9: West Frankish throne passes to Hugh Capet (987 CE)"),
        E("rus_yaroslav_wise", "fra_capet_stlouis", "direct", "Anne of Kiev (daughter of Yaroslav the Wise) marries King Henry I of France -> ancestor of Philip II & St. Louis IX"),
        E("fra_capet_stlouis", "fra_valois_bourbon", "direct", "Mod. Univ. Hist. Vol. 9: Direct Capetian patrilineal succession into Valois & Bourbon"),
        E("grk_julius_augustus", "eng_howell_roman_saxon", "expansion", "Howell 1685: Roman Britain under Julius Caesar & Claudius"),
        E("eur_king_arthur", "eng_howell_roman_saxon", "expansion", "Howell 1685: Christian British sovereigns (Lucius, Arthur) preceding Anglo-Saxon & Danish rule"),
        E("eng_howell_roman_saxon", "eur_wessex_alfred_norman", "expansion", "Howell 1685: Heptarchy unification -> Egbert, Alfred the Great, Canute & William I"),
        E("eur_wessex_alfred_norman", "eng_plantagenet_kings", "direct", "Howell 1685: Wessex-Norman inheritance via Empress Matilda -> Henry II Plantagenet"),
        E("fra_capet_stlouis", "eng_plantagenet_kings", "cognate", "Anglo-French Capetian marriage alliances across the Plantagenet dynasty"),
        E("eng_plantagenet_kings", "eng_tudor_monarchs", "direct", "Howell 1685: Plantagenet descent through Margaret Beaufort & Elizabeth of York -> Henry VII"),
        E("wal_cunedda_rhodri_llywelyn", "eng_tudor_monarchs", "expansion", "Welsh royal pedigree of Owen Tudor uniting with the English crown in 1485"),
        E("eng_tudor_monarchs", "eng_stuart_great_britain", "direct", "Howell 1685: Henry VII's daughter Margaret Tudor -> James IV/V -> Mary Queen of Scots -> James VI & I"),
        E("sco_fergus_macalpin", "eng_stuart_great_britain", "expansion", "Scottish royal descent from Fergus Mor & Kenneth MacAlpin uniting Scotland & England under James VI & I"),
        E("eur_tubal_spain", "por_afonso_henriques", "expansion", "Iberian royal succession from Tubal's Spain through Castile-Leon -> Princess Teresa & Afonso I Henriques"),
        E("fra_capet_stlouis", "por_afonso_henriques", "direct", "Count Henry of Burgundy (Capetian line) + Teresa of Castile -> King Afonso I Henriques of Portugal (1139)"),
        E("por_afonso_henriques", "por_aviz_discoveries", "direct", "History of Portugal 1661/1726: House of Burgundy -> House of Aviz (John I -> Manuel I)"),
        E("por_aviz_discoveries", "por_braganza_restoration", "direct", "History of Portugal 1661/1726: Aviz descent -> House of Braganza (John IV, 1640 -> Afonso VI)"),
        E("rus_yaroslav_wise", "rus_nevsky_ivan_tsars", "direct", "Mod. Univ. Hist. Vol. 13: Rurikid patriline Yaroslav -> Vsevolod -> Vladimir Monomakh -> Alexander Nevsky -> Ivan III & IV"),
        E("abg_jochi_golden_horde", "rus_nevsky_ivan_tsars", "cognate", "Rus'-Golden Horde relations ending with Ivan III's Stand on the Ugra River (1480)"),
        E("rus_nevsky_ivan_tsars", "rus_romanov_peter_great", "expansion", "Mod. Univ. Hist. Vol. 13: Romanov succession from Tsar Ivan IV's marriage to Anastasia Romanovna -> Michael I -> Peter the Great"),
    ]

    return {
        "module": "31_europe_england_france_portugal_russia_germans",
        "title": "Noahic-Anchored Royal Houses of England/Britain, France, Burgundy, Savoy, Portugal, Romanov Russia & Germanic Nations",
        "nodes": nodes,
        "edges": edges,
    }
