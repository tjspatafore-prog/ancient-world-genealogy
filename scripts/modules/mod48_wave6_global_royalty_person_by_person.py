"""
Module 48: Wave 6 Person-by-Person Global Royalty, Living 2026 European Monarchies,
European Chronicles (Lombards, Iceland/Vinland, Wales), Rajputs, Ladakh, Moghulistan,
Malay Annals, African Sovereign Queens & Famous Historical Figures.
"""

from . import N, E


def link_seq(edges, ids, edge_type="direct", label="Dynastic succession"):
    for a, b in zip(ids, ids[1:]):
        edges.append(E(a, b, edge_type, label))


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
    # SECTION A: NORTHERN & CENTRAL EUROPEAN ROYAL HOUSES (Sweden, Denmark, Poland, Lithuania, Hungary, Bohemia)
    # =========================================================================
    # Sweden
    chain([
        "eur42_eric_olof_sweden",
        ("eur6_eric_victorious", "King Eric VI the Victorious of Sweden (r. c. 970–995 CE)", 19, "c. 945–995 CE (Heimskringla)", "Munsö King of Sweden", "First historically verified king of unified Sweden; father of Olof Skötkonung.", False),
        ("eur6_olof_skotkonung", "King Olof Skötkonung of Sweden (r. 995–1022 CE; 1st Christian King)", 19, "c. 980–1022 CE (Heimskringla)", "1st Baptized King of Sweden", "Father of Ingegerd of Sweden (+ Yaroslav the Wise) and Anund Jacob.", False),
        ("eur6_ingegerd_sweden", "Princess Ingegerd Olofsdotter (St. Anna of Novgorod; Wife of Yaroslav the Wise)", 20, "1001–1050 CE (Primary Chronicle; Heimskringla)", "Grand Princess of Kiev Linking Sweden to France, Hungary & England", "Married Yaroslav the Wise (1019 CE), mothering Anne of Kiev, Anastasia of Hungary, Elizabeth of Norway & Vsevolod I.", False),
    ], "europe_norse", ["Snorri Sturluson Heimskringla", "Modern Universal History Vol. 12"], "Swedish Munsö Succession")
    nodes.append(N("eur6_birger_jarl", "Birger Jarl of Bjälbo (Founder of Stockholm, r. 1248–1266 CE)", "europe_norse", 20, "c. 1210–1266 CE", "Bjälbo Regent & Father of Kings Valdemar & Magnus", ["Erikskrönikan"], "Married Ingeborg of Sweden (descendant of Munsö kings); consolidated medieval Sweden."))
    edges += [
        E("eur6_olof_skotkonung", "eur6_birger_jarl", "expansion", "Swedish royal house -> Bjälbo -> Birger Jarl"),
        E("eur6_ingegerd_sweden", "rus_yaroslav_wise", "direct", "Marriage of Ingegerd of Sweden & Yaroslav the Wise"),
    ]
    chain([
        "eur42_gustav_vasa",
        ("eur6_charles9_sweden", "King Charles IX of Sweden (Son of Gustav I Vasa, r. 1604–1611)", 21, "1550–1611 CE", "Youngest Son of Gustav Vasa", "Father of Gustavus Adolphus.", False),
        ("eur6_gustavus_adolphus", "King Gustavus Adolphus of Sweden (r. 1611–1632; Lion of the North)", 21, "1594–1632 CE", "Thirty Years' War Champion", "Father of Queen Christina.", False),
        ("eur6_queen_christina", "Queen Christina of Sweden (r. 1632–1654)", 21, "1626–1689 CE", "Learned Sovereign Queen of Sweden", "Daughter of Gustavus Adolphus.", False),
        "eur42_gustavus_christina",
    ], "europe_norse", ["Modern Universal History Vol. 12"], "House of Vasa Succession")
    chain([
        "eur42_charles12_bernadotte",
        ("eur6_charles12_sweden", "King Charles XII of Sweden (r. 1697–1718)", 21, "1682–1718 CE", "Palatinate-Zweibrücken King of Sweden", "Great Northern War commander.", False),
        ("eur6_carl16_gustaf", "LIVING (2026): King Carl XVI Gustaf of Sweden (b. 1946; Great-Grandson of Queen Victoria via Princess Margaret!)", 22, "1946 – Present Day (2026)", "Reigning King of Sweden", "Descendant of both Gustav Vasa and Queen Victoria.", False),
        ("eur6_crown_princess_victoria", "LIVING (2026): Crown Princess Victoria of Sweden (b. 1977; Future Queen)", 22, "1977 – Present Day (2026)", "Heir Apparent to the Swedish Throne", "Eldest child of King Carl XVI Gustaf.", False),
    ], "europe_norse", ["European Royal Genealogies"], "Modern Swedish Royal Succession")

    # Denmark
    chain([
        "eur42_gorm_bluetooth_cnut",
        ("eur6_gorm_old", "King Gorm the Old of Denmark (r. c. 936–958 CE; Jelling Stones)", 19, "d. c. 958 CE", "Founder of Danish Jelling Dynasty", "Father of Harald Bluetooth.", False),
        ("eur6_harald_bluetooth", "King Harald I Bluetooth of Denmark & Norway (r. c. 958–986 CE; Christianizer)", 19, "d. c. 986 CE", "Baptized & Unified Denmark", "Father of Sweyn Forkbeard.", False),
        ("eur6_sweyn_forkbeard", "King Sweyn Forkbeard (+ Gunhild/Sigrid of Poland; King of Denmark & England, d. 1014)", 19, "963–1014 CE", "Father of Cnut the Great & Estrid", "Fathered Cnut the Great.", False),
        "mon_eng_canute",
        ("eur6_valdemar1", "King Valdemar I the Great of Denmark (r. 1157–1182; Grandson of Harald & Kiev!)", 20, "1131–1182 CE", "Restorer of Medieval Denmark", "Descendant of Estrid Svendsdatter & Yaroslav the Wise via Canute Lavard & Ingeborg of Kiev.", False),
        ("eur6_queen_margaret1", "Queen Margaret I of Denmark, Norway & Sweden (Architect of Kalmar Union, 1397)", 20, "1353–1412 CE", "6th-Gen Descendant of Valdemar I", "Founder of the Kalmar Union.", False),
        ("eur6_christian4_denmark", "King Christian IV of Denmark & Norway (r. 1588–1648; Oldenburg)", 21, "1577–1648 CE", "Brother of Queen Anne (+ James VI & I)", "Uncle of King Charles I of England.", False),
        ("eur6_king_frederik10", "LIVING (2026): King Frederik X of Denmark (b. 1968; Glücksburg Heir of Christian IV & Victoria)", 22, "1968 – Present Day (2026)", "Reigning King of Denmark", "Acceded in 2024.", False),
    ], "europe_norse", ["Heimskringla", "European Royal Genealogies"], "Danish Jelling-Oldenburg-Glücksburg Line")
    nodes.append(N("eur6_emma_normandy", "Queen Emma of Normandy (Daughter of Richard I; Wife of Ethelred II & Cnut; Mother of Edward the Confessor & Harthacnut)", "europe_norse", 20, "c. 984–1052 CE", "Twice Queen of England & Normandy Bridge", ["Anglo-Saxon Chronicle"], "Bridged Norman Dukes with Anglo-Saxon and Danish crowns."))
    edges += [
        E("eur6_sweyn_forkbeard", "eur6_emma_normandy", "cognate", "Emma wed Ethelred II and Sweyn's son Cnut the Great"),
        E("mon_eng_canute", "eur6_emma_normandy", "direct", "Marriage of King Cnut & Emma of Normandy"),
    ]

    # Poland & Lithuania
    chain([
        "eur_poland_mieszko",
        ("eur6_mieszko1", "Duke Mieszko I of Poland (r. c. 960–992 CE; Baptism of Poland 966)", 19, "c. 930–992 CE (Gallus Anonymus)", "Founder of Christian Polish State", "Father of Boleslaw I & Gunhild/Sigríðr.", False),
        ("eur6_boleslaw1_brave", "King Boleslaw I the Brave of Poland (r. 992–1025; 1st Crowned King)", 19, "967–1025 CE", "First Crowned King of Poland", "Father of Mieszko II.", False),
        ("eur6_mieszko2", "King Mieszko II Lambert of Poland (r. 1025–1034)", 20, "c. 990–1034 CE", "Son of Boleslaw I", "Father of Casimir I.", False),
        ("eur6_casimir1_poland", "Duke Casimir I the Restorer (+ Maria Dobroniega of Kiev, r. 1039–1058)", 20, "1016–1058 CE", "Piast-Rurikid Unifier", "Married Yaroslav the Wise's sister Maria Dobroniega of Kiev.", False),
        ("eur6_casimir3_great", "King Casimir III the Great of Poland (r. 1333–1370; Codifier & University Founder)", 20, "1310–1370 CE", "Last Piast King of Poland", "Great lawgiver; sister Elizabeth married Charles I of Hungary -> Louis the Great.", False),
    ], "europe_norse", ["Gallus Anonymus", "Modern Universal History Vol. 12"], "Polish Piast Succession")
    nodes += [
        N("eur6_gunhild_sigrid", "Princess Gunhild / Świętosława of Poland (Daughter of Mieszko I; Mother of Cnut the Great)", "europe_norse", 19, "10th–11th c. CE", "Queen of Sweden & Denmark", ["Adam of Bremen", "Sagas"], "Daughter of Mieszko I who wed Eric the Victorious of Sweden and Sweyn Forkbeard of Denmark."),
        N("eur6_maria_dobroniega", "Princess Maria Dobroniega of Kiev (Daughter of St. Vladimir; Wife of Casimir I)", "europe_norse", 20, "c. 1012–1087 CE", "Sister of Yaroslav & Duchess of Poland", ["Primary Chronicle"], "Daughter of St. Vladimir the Great of Kiev; mother of Boleslaw II & Wladyslaw Herman."),
    ]
    edges += [
        E("eur6_mieszko1", "eur6_gunhild_sigrid", "direct", "Mieszko I -> daughter Gunhild/Świętosława"),
        E("eur6_gunhild_sigrid", "eur6_sweyn_forkbeard", "direct", "Marriage of Gunhild & Sweyn Forkbeard -> Cnut the Great"),
        E("rus_vladimir_great", "eur6_maria_dobroniega", "direct", "St. Vladimir of Kiev -> daughter Maria Dobroniega"),
        E("eur6_maria_dobroniega", "eur6_casimir1_poland", "direct", "Marriage of Maria Dobroniega & Casimir I of Poland"),
        E("eur6_casimir1_poland", "eur42_casimir1_poland", "direct", "Casimir I -> Casimir anchor"),
    ]

    chain([
        "eur42_mindaugas_gediminas",
        ("eur6_mindaugas", "King Mindaugas of Lithuania (r. c. 1236–1263)", 20, "d. 1263 CE", "First Christian King of Lithuania", "United Baltic Aukštaitija.", False),
        ("eur6_gediminas", "Grand Duke Gediminas of Lithuania (r. 1316–1341; Founder of Vilnius)", 20, "c. 1275–1341 CE", "Progenitor of Gediminids", "Father of Algirdas and Kęstutis.", False),
        ("eur6_algirdas", "Grand Duke Algirdas (+ Uliana of Tver, r. 1345–1377)", 20, "c. 1296–1377 CE", "Father of King Jagiello", "Wed Rurikid Princess Uliana of Tver.", False),
        ("eur6_wladyslaw2_jagiello", "King Wladyslaw II Jagiello (1386–1434; Victor of Grunwald 1410)", 20, "c. 1352–1434 CE", "Founder of Jagiellonian Dynasty", "Wed Queen Jadwiga of Poland, uniting Poland and Lithuania.", False),
        ("eur6_casimir4", "King Casimir IV Jagiellon (Son of Jagiello, r. 1447–1492)", 21, "1427–1492 CE", "Father of Four Kings", "Father of Kings of Poland, Bohemia & Hungary.", False),
        ("eur6_sigismund1_old", "King Sigismund I the Old (+ Bona Sforza, r. 1506–1548)", 21, "1467–1548 CE", "Polish Renaissance Golden Age", "Son of Casimir IV.", False),
        ("eur6_john3_sobieski", "King John III Sobieski of Poland-Lithuania (r. 1674–1696; Relief of Vienna 1683)", 21, "1629–1696 CE", "Defender of Vienna (1683)", "Maternal lineage connected back to Rurikid & Polish nobility.", False),
    ], "europe_norse", ["Lithuanian Chronicles", "Jan Dlugosz"], "Lithuanian-Polish Jagiellonian Succession")
    nodes += [
        N("eur6_vytautas_great", "Grand Duke Vytautas the Great of Lithuania (Son of Kęstutis; Cousin of Jagiello, 1392–1430)", "europe_norse", 20, "c. 1350–1430 CE", "Great Sovereign of Lithuania (Grunwald 1410)", ["Lithuanian Chronicles"], "Daughter Sophia of Lithuania married Grand Prince Vasily I of Moscow."),
        N("eur6_queen_jadwiga", "Queen St. Jadwiga of Poland (Daughter of Louis I of Hungary; Rex Poloniae, 1384–1399)", "europe_norse", 20, "1373–1399 CE", "Piast-Capetian Queen Regnant of Poland", ["Jan Dlugosz"], "Married Grand Duke Jagiello (Wladyslaw II), uniting Poland & Lithuania."),
    ]
    edges += [
        E("eur6_gediminas", "eur6_vytautas_great", "direct", "Gediminas -> Kęstutis -> Vytautas the Great"),
        E("eur6_queen_jadwiga", "eur6_wladyslaw2_jagiello", "direct", "Marriage of Queen Jadwiga & Wladyslaw II Jagiello"),
    ]

    # Hungary & Bohemia
    chain([
        "eur42_almos_arpad_stephen",
        ("eur6_almos", "Chieftain Álmos (Father of Árpád, c. 820–895 CE)", 19, "c. 820–895 CE", "Progenitor of Hungarian Árpád House", "Led Magyars westward.", False),
        ("eur6_arpad", "Grand Prince Árpád of Hungary (r. c. 895–907 CE; Conquest of Carpathian Basin)", 19, "c. 845–907 CE", "Founder of Árpád Dynasty", "Father of Zoltán.", False),
        ("eur6_st_stephen1", "King St. Stephen I of Hungary (r. 1000–1038 CE; 1st Christian King)", 19, "c. 975–1038 CE", "Apostolic King & Patron of Hungary", "Great-great-grandson of Árpád; wed Gisela of Bavaria.", False),
        ("eur6_andrew1_hungary", "King Andrew I of Hungary (+ Anastasia of Kiev, r. 1046–1060)", 20, "c. 1015–1060 CE", "Árpád Cousin & Son-in-Law of Yaroslav", "Married Anastasia Yaroslavna of Kiev.", False),
        ("eur6_bela3", "King Béla III of Hungary (+ Margaret of France, r. 1172–1196)", 20, "c. 1148–1196 CE", "Árpád-Capetian Union", "Father of Andrew II.", False),
        ("eur6_andrew2", "King Andrew II of Hungary (r. 1205–1235; Golden Bull 1222)", 20, "c. 1177–1235 CE", "Father of St. Elizabeth & Béla IV", "Issued the Golden Bull of 1222.", False),
        ("eur6_bela4", "King Béla IV of Hungary (Rebuilder after Mongol Invasion, r. 1235–1270)", 20, "1206–1270 CE", "Second Founder of Hungary", "Grandfather of Charles I & Kunigunda of Bohemia.", False),
        ("eur6_louis1_great", "King Louis I the Great of Hungary & Poland (Anjou-Capet, r. 1342–1382)", 20, "1326–1382 CE", "Unifier of Hungary & Poland Crowns", "Father of Queen Jadwiga of Poland and Queen Mary of Hungary.", False),
    ], "europe_norse", ["Hungarian Illuminated Chronicle", "Modern Universal History"], "Hungarian Árpád & Anjou Succession")
    nodes += [
        N("eur6_st_elizabeth_hungary", "Princess St. Elizabeth of Hungary (Daughter of Andrew II, 1207–1231)", "europe_norse", 20, "1207–1231 CE", "Árpád Princess of Thuringia", ["Hungarian Chronicles"], "Daughter of King Andrew II & Gertrude of Merania."),
        N("eur6_john_hunyadi", "Regent John Hunyadi (Defender of Belgrade 1456, d. 1456)", "europe_norse", 20, "c. 1406–1456 CE", "Voivode & Regent of Hungary", ["European Chronicles"], "Father of King Matthias Corvinus."),
        N("eur6_matthias_corvinus", "King Matthias Corvinus of Hungary (r. 1458–1490; Bibliotheca Corviniana)", "europe_norse", 20, "1443–1490 CE", "Renaissance King of Hungary", ["European Chronicles"], "Son of John Hunyadi; famed Renaissance patron."),
        N("eur6_st_wenceslas1", "Duke St. Wenceslas I of Bohemia (Přemyslid Martyr, r. 921–935 CE)", "europe_norse", 19, "c. 907–935 CE", "Patron Saint of Bohemia / Czechia", ["Cosmas of Prague"], "Grandson of St. Ludmila & Bořivoj I."),
        N("eur6_ottokar2", "King Ottokar II of Bohemia (r. 1253–1278; + Kunigunda of Kiev/Hungary)", "europe_norse", 20, "c. 1233–1278 CE", "Iron and Golden King of Bohemia", ["Cosmas of Prague"], "Married Kunigunda (granddaughter of Béla IV & Rostislav of Kiev)."),
        N("eur6_emperor_charles4", "Emperor & King Charles IV of Bohemia (r. 1346–1378; Golden Bull & Charles Univ.)", "europe_norse", 20, "1316–1378 CE", "Přemyslid-Luxembourg Emperor", ["European Chronicles"], "Son of Queen Elisabeth of Bohemia (Přemyslid); father of Sigismund & Anne of Bohemia."),
        N("eur6_anne_bohemia", "Queen Anne of Bohemia (Daughter of Charles IV; Wife of King Richard II of England)", "europe_norse", 20, "1366–1394 CE", "Beloved Queen Consort of England", ["English Chronicles"], "Daughter of Emperor Charles IV who wed King Richard II."),
        N("eur6_bonne_bohemia", "Princess Bonne of Bohemia (Sister of Charles IV; Wife of King John II of France)", "europe_norse", 20, "1315–1349 CE", "Ancestral Mother of Valois Kings of France", ["French Chronicles"], "Mother of Charles V the Wise of France."),
        N("eur6_emperor_sigismund", "Emperor Sigismund of Luxembourg (Son of Charles IV; King of Hungary & Bohemia)", "europe_norse", 20, "1368–1437 CE", "Holy Roman Emperor & Knightly Sovereign", ["European Chronicles"], "Daughter Elizabeth of Luxembourg wed Habsburg Albert II."),
    ]
    edges += [
        E("eur5_anastasia_kiev", "eur6_andrew1_hungary", "direct", "Marriage of Anastasia of Kiev & King Andrew I of Hungary"),
        E("eur6_andrew2", "eur6_st_elizabeth_hungary", "direct", "Andrew II -> daughter St. Elizabeth of Hungary"),
        E("eur6_louis1_great", "eur6_queen_jadwiga", "direct", "Louis I the Great -> daughter Queen Jadwiga"),
        E("eur42_hunyadi_corvinus", "eur6_john_hunyadi", "direct", "Hunyadi anchor -> John Hunyadi"),
        E("eur6_john_hunyadi", "eur6_matthias_corvinus", "direct", "John Hunyadi -> Matthias Corvinus"),
        E("eur42_premysl_wenceslas", "eur6_st_wenceslas1", "direct", "Přemyslid anchor -> St. Wenceslas I"),
        E("eur6_st_wenceslas1", "eur6_ottokar2", "direct", "Přemyslid line -> Ottokar II"),
        E("eur6_bela4", "eur6_ottokar2", "direct", "Béla IV -> granddaughter Kunigunda (+ Ottokar II)"),
        E("eur6_ottokar2", "eur6_emperor_charles4", "direct", "Ottokar II -> Wenceslas II -> Elisabeth -> Emperor Charles IV"),
        E("eur6_ottokar2", "eur6_bonne_bohemia", "direct", "Ottokar II -> Elisabeth -> Bonne of Bohemia (+ John II of France)"),
        E("eur6_emperor_charles4", "eur6_anne_bohemia", "direct", "Charles IV -> Anne of Bohemia"),
        E("eur6_anne_bohemia", "mon_eng_richard2", "direct", "Marriage of Anne of Bohemia & King Richard II"),
        E("eur6_emperor_charles4", "eur6_emperor_sigismund", "direct", "Charles IV -> Emperor Sigismund"),
    ]

    # =========================================================================
    # SECTION B: MEDICI, HABSBURGS, WINDSORS TO LIVING 2026 & LATE ROMANOVS
    # =========================================================================
    nodes += [
        N("roy6_eleanor_aquitaine", "Queen Eleanor of Aquitaine (Duchess of Aquitaine; Queen of France & England, 1122–1204)", "europe_norse", 20, "1122–1204 CE", "Mother of Richard I, King John & Eleanor of Castile", ["Chronicles of England & France"], "Mother of Europe's greatest medieval royal network."),
        N("roy6_blanche_castile", "Queen Blanche of Castile (Granddaughter of Eleanor; Mother of King St. Louis IX of France)", "europe_norse", 20, "1188–1252 CE", "Queen Regent of France", ["French Royal Chronicles"], "Daughter of Alfonso VIII & Eleanor of England; mother of St. Louis IX."),
        N("roy6_juana_mad", "Queen Juana of Castile & Aragon ('Juana la Loca', Daughter of Ferdinand & Isabella, 1479–1555)", "europe_norse", 21, "1479–1555 CE", "Spanish-Habsburg Heiress", ["Mariana Spain"], "Married Philip the Handsome; mother of Emperor Charles V & Ferdinand I."),
        N("roy6_philip_handsome", "Archduke Philip the Handsome of Burgundy (Son of Emperor Maximilian I; Father of Charles V)", "europe_norse", 21, "1478–1506 CE", "Habsburg Prince & King Consort of Castile", ["Betham Tables"], "Son of Maximilian I & Mary of Burgundy."),
        N("roy6_catherine_aragon", "Queen Catherine of Aragon (Daughter of Ferdinand & Isabella; Mother of Mary I of England)", "europe_norse", 21, "1485–1536 CE", "Spanish Princess & 1st Queen of Henry VIII", ["English Chronicles"], "Mother of Queen Mary I."),
        N("roy6_ferdinand1_hre", "Emperor Ferdinand I (Son of Philip & Juana; King of Bohemia & Hungary, 1556–1564)", "europe_norse", 21, "1503–1564 CE", "Founder of Austrian Habsburg Line", ["Betham Tables"], "Brother of Charles V."),
        N("roy6_joseph2_hre", "Emperor Joseph II (Eldest Son of Maria Theresa, r. 1765–1790)", "europe_norse", 22, "1741–1790 CE", "Enlightened Habsburg Emperor", ["Betham Tables"], "Eldest son of Empress Maria Theresa."),
        N("roy6_leopold2_hre", "Emperor Leopold II (Son of Maria Theresa; Father of Emperor Francis II, r. 1790–1792)", "europe_norse", 22, "1747–1792 CE", "Holy Roman Emperor", ["Betham Tables"], "Grandfather of Habsburg Emperor Franz Joseph."),
        N("roy6_marie_antoinette", "Queen Marie Antoinette of France (Daughter of Maria Theresa; Wife of Louis XVI, d. 1793)", "europe_norse", 22, "1755–1793 CE", "Archduchess of Austria & Queen of France", ["French Chronicles"], "Daughter of Empress Maria Theresa."),
        N("roy6_napoleon2", "Napoleon II Bonaparte ('L'Aiglon', King of Rome; Son of Napoleon I & Marie Louise, 1811–1832)", "europe_norse", 22, "1811–1832 CE", "Son of Napoleon & Habsburg Archduchess", ["Modern European History"], "United Bonaparte and Habsburg bloodlines."),
        N("roy6_cosimo_medici", "Cosimo de' Medici ('Pater Patriae' of Florence, 1389–1464)", "europe_norse", 20, "1389–1464 CE", "Founder of Medici Political Dynasty", ["Florentine Chronicles"], "Patron of Renaissance humanism."),
        N("roy6_lorenzo_magnificent", "Lorenzo de' Medici ('Il Magnifico', 1449–1492; Patron of Leonardo & Michelangelo)", "europe_norse", 21, "1449–1492 CE", "Grandson of Cosimo; Father of Pope Leo X", ["Vasari Lives"], "Great Renaissance statesman."),
        N("roy6_catherine_medici", "Queen Catherine de' Medici (Great-Granddaughter of Lorenzo; Queen of France by Henry II)", "europe_norse", 21, "1519–1589 CE", "Mother of Francis II, Charles IX & Henry III", ["French Chronicles"], "Dominant Renaissance queen mother of Valois France."),
        N("roy6_marie_medici", "Queen Marie de' Medici (Granddaughter of Emperor Ferdinand I; Wife of King Henry IV of France)", "europe_norse", 21, "1575–1642 CE", "Mother of Louis XIII & Queen Henrietta Maria", ["French Chronicles"], "Mother of Louis XIII and grandmother of Charles II & James II of England."),
        N("roy6_kaiser_wilhelm1", "German Emperor Kaiser Wilhelm I of Prussia (1797–1888)", "europe_norse", 22, "1797–1888 CE", "1st German Emperor (1871)", ["German Imperial Registers"], "Descendant of Frederick William & Hohenzollern electors."),
        N("roy6_princess_victoria_royal", "Empress Victoria / Princess Royal (Eldest Daughter of Queen Victoria; Mother of Kaiser Wilhelm II)", "europe_norse", 22, "1840–1901 CE", "British Princess & German Empress", ["Burke's Royal Genealogies"], "Married Frederick III of Prussia."),
        N("roy6_frederick3_prussia", "German Emperor Frederick III (Son of Wilhelm I; Husband of Victoria, r. 1888)", "europe_norse", 22, "1831–1888 CE", "German Emperor & Father of Wilhelm II", ["Burke's Royal Genealogies"], "Father of Kaiser Wilhelm II."),
        N("roy6_kaiser_wilhelm2", "German Emperor Kaiser Wilhelm II (Son of Frederick III & Victoria, r. 1888–1918)", "europe_norse", 22, "1859–1941 CE", "Last German Emperor & Grandson of Queen Victoria", ["Burke's Royal Genealogies"], "First cousin of King George V and Tsaritsa Alexandra."),
    ]
    edges += [
        E("pc_eleanor_aquitaine", "roy6_eleanor_aquitaine", "direct", "Eleanor individual"),
        E("mon_eng_henry2", "roy6_eleanor_aquitaine", "direct", "Marriage of Henry II & Eleanor of Aquitaine"),
        E("roy6_eleanor_aquitaine", "roy6_blanche_castile", "direct", "Eleanor -> Eleanor of England -> Blanche of Castile"),
        E("roy6_blanche_castile", "mon_fra_louis9", "direct", "Blanche of Castile -> King St. Louis IX"),
        E("pc_ferdinand_isabella_kids", "roy6_juana_mad", "direct", "Ferdinand & Isabella -> Juana the Mad"),
        E("pc_ferdinand_isabella_kids", "roy6_catherine_aragon", "direct", "Ferdinand & Isabella -> Catherine of Aragon"),
        E("roy6_catherine_aragon", "mon_eng_mary1", "direct", "Catherine of Aragon -> Queen Mary I of England"),
        E("mon_hre_maximilian1", "roy6_philip_handsome", "direct", "Maximilian I -> Philip the Handsome"),
        E("roy6_philip_handsome", "roy6_juana_mad", "direct", "Marriage of Philip the Handsome & Juana"),
        E("roy6_juana_mad", "mon_esp_charles5", "direct", "Juana & Philip -> Emperor Charles V"),
        E("roy6_juana_mad", "roy6_ferdinand1_hre", "direct", "Juana & Philip -> Emperor Ferdinand I"),
        E("mon_hre_maria_theresa", "roy6_joseph2_hre", "direct", "Maria Theresa -> Emperor Joseph II"),
        E("mon_hre_maria_theresa", "roy6_leopold2_hre", "direct", "Maria Theresa -> Emperor Leopold II"),
        E("mon_hre_maria_theresa", "roy6_marie_antoinette", "direct", "Maria Theresa -> Marie Antoinette"),
        E("roy6_marie_antoinette", "mon_fra_louis16", "direct", "Marriage of Louis XVI & Marie Antoinette"),
        E("mon_fra_napoleon", "roy6_napoleon2", "direct", "Napoleon I (+ Marie Louise of Austria) -> Napoleon II"),
        E("pc_medici_house", "roy6_cosimo_medici", "direct", "Medici anchor -> Cosimo il Vecchio"),
        E("roy6_cosimo_medici", "roy6_lorenzo_magnificent", "direct", "Cosimo -> Piero -> Lorenzo the Magnificent"),
        E("roy6_lorenzo_magnificent", "roy6_catherine_medici", "direct", "Lorenzo -> Piero -> Lorenzo II -> Catherine de' Medici"),
        E("roy6_catherine_medici", "mon_fra_henry2", "direct", "Marriage of Catherine de' Medici & Henry II of France"),
        E("roy6_ferdinand1_hre", "roy6_marie_medici", "direct", "Joanna of Austria -> Marie de' Medici"),
        E("roy6_marie_medici", "mon_fra_henry4", "direct", "Marriage of Marie de' Medici & Henry IV"),
        E("pc_hohenzollern_prussia", "roy6_kaiser_wilhelm1", "direct", "Hohenzollern -> Kaiser Wilhelm I"),
        E("roy6_kaiser_wilhelm1", "roy6_frederick3_prussia", "direct", "Wilhelm I -> Frederick III"),
        E("mon_eng_victoria", "roy6_princess_victoria_royal", "direct", "Queen Victoria -> eldest daughter Victoria"),
        E("roy6_princess_victoria_royal", "roy6_frederick3_prussia", "direct", "Marriage of Princess Victoria & Frederick III"),
        E("roy6_frederick3_prussia", "roy6_kaiser_wilhelm2", "direct", "Frederick III & Victoria -> Kaiser Wilhelm II"),
        E("roy6_princess_victoria_royal", "roy6_kaiser_wilhelm2", "direct", "Mother Victoria -> Kaiser Wilhelm II"),
    ]

    # Living British Windsors (2026) & Late Romanovs / Byzantium
    chain([
        "pc_hanover_windsor_victoria",
        ("roy6_electress_sophia", "Electress Sophia of Hanover (Granddaughter of King James I; Act of Settlement 1701)", 21, "1630–1714 CE", "Stuart Mother of Hanoverian Line", "Daughter of Elizabeth Stuart & Frederick V; mother of King George I.", False),
        "mon_eng_george1",
        "mon_eng_victoria",
        ("roy6_edward7", "King Edward VII (Son of Queen Victoria & Prince Albert, r. 1901–1910)", 22, "1841–1910 CE", "First Saxe-Coburg-Gotha King", "Married Alexandra of Denmark.", False),
        ("roy6_george5", "King George V (Son of Edward VII; Renamed House of Windsor 1917, r. 1910–1936)", 22, "1865–1936 CE", "Founder of House of Windsor", "Father of Edward VIII & George VI.", False),
        ("roy6_george6", "King George VI (Son of George V, r. 1936–1952)", 22, "1895–1952 CE", "WWII British Monarch", "Father of Queen Elizabeth II.", False),
        ("roy6_elizabeth2", "Queen Elizabeth II (r. 1952–2022; Longest-Reigning British Monarch)", 22, "1926–2022 CE", "Queen of the United Kingdom & Commonwealth", "Daughter of George VI; wed Prince Philip of Greece & Denmark.", True),
        ("roy6_king_charles3", "LIVING (2026): King Charles III of the United Kingdom (b. 1948, r. 2022–present)", 22, "1948 – Present Day (2026)", "Reigning Sovereign of the United Kingdom", "Eldest son of Queen Elizabeth II & Prince Philip.", True),
        ("roy6_prince_william", "LIVING (2026): William, Prince of Wales (b. 1982; Son of King Charles III & Diana)", 22, "1982 – Present Day (2026)", "Heir Apparent to the British Crown", "Father of Prince George, Princess Charlotte & Prince Louis.", False),
        ("roy6_prince_george", "LIVING (2026): Prince George of Wales (b. 2013; Future Windsor Heir)", 22, "2013 – Present Day (2026)", "Eldest Child of Prince William", "2nd in line to the British throne.", False),
    ], "europe_norse", ["Burke's Royal Genealogies", "Howell (1685)"], "Hanover & Windsor Succession to 2026")
    nodes.append(N("roy6_prince_albert", "Prince Albert of Saxe-Coburg & Gotha (1819–1861; Consort of Queen Victoria)", "europe_norse", 22, "1819–1861 CE", "Father of Nine Royal Children Across Europe", ["Burke's Royal Genealogies"], "First cousin and husband of Queen Victoria."))
    edges += [
        E("mon_eng_victoria", "roy6_prince_albert", "direct", "Marriage of Queen Victoria & Prince Albert"),
        E("roy6_prince_albert", "roy6_edward7", "direct", "Prince Albert -> King Edward VII"),
    ]

    chain([
        "mon_rus_catherine2",
        ("roy6_tsar_paul1", "Emperor Paul I of Russia (Son of Peter III & Catherine II, r. 1796–1801)", 22, "1754–1801 CE", "Romanov-Holstein-Gottorp Emperor", "Father of Emperors Alexander I & Nicholas I.", False),
        ("roy6_tsar_alexander1", "Emperor Alexander I of Russia (r. 1801–1825; Defeated Napoleon 1812)", 22, "1777–1825 CE", "Victor of Patriotic War of 1812", "Eldest son of Paul I.", False),
        ("roy6_tsar_alexander2", "Emperor Alexander II the Liberator (Son of Nicholas I, r. 1855–1881)", 22, "1818–1881 CE", "Emancipator of the Serfs (1861)", "Father of Alexander III; grandfather of Nicholas II.", False),
        ("roy6_tsar_nicholas2", "Emperor Tsar Nicholas II (Son of Alexander III, r. 1894–1917)", 22, "1868–1918 CE", "Last Emperor of All Russia", "Married Alix of Hesse (Empress Alexandra, granddaughter of Queen Victoria).", False),
        ("roy6_anastasia_romanov", "Grand Duchess Anastasia Nikolaevna (Daughter of Nicholas II & Alexandra, 1901–1918)", 22, "1901–1918 CE", "Youngest Daughter of Tsar Nicholas II", "Great-granddaughter of Queen Victoria.", False),
    ], "europe_norse", ["Russian Imperial Registers", "Burke's Royal Genealogies"], "Late Romanov Imperial Succession")
    nodes += [
        N("roy6_empress_alexandra", "Empress Alexandra Feodorovna / Alix of Hesse (Granddaughter of Queen Victoria; Wife of Nicholas II)", "europe_norse", 22, "1872–1918 CE", "Last Tsaritsa of Russia", ["Burke's Royal Genealogies"], "Daughter of Princess Alice (daughter of Queen Victoria)."),
        N("roy6_anna_komnene", "Princess Anna Komnene (1083–1153; Historian Author of The Alexiad)", "greek", 20, "1083–1153 CE", "Daughter of Emperor Alexios I Komnenos", ["Anna Komnene Alexiad"], "Renowned medieval historian of the Komnenian Byzantine court."),
        N("roy6_sophia_palaiologina", "Princess Zoe / Sophia Palaiologina (Niece of Constantine XI; Wife of Ivan III of Moscow)", "greek", 21, "c. 1449–1503 CE", "Byzantine Heir Bridging Constantinople to Moscow", ["Russian Chronicles"], "Grandmother of Tsar Ivan IV the Terrible."),
    ]
    edges += [
        E("mon_eng_victoria", "roy6_empress_alexandra", "direct", "Queen Victoria -> Alice -> Empress Alexandra"),
        E("roy6_empress_alexandra", "roy6_tsar_nicholas2", "direct", "Marriage of Nicholas II & Empress Alexandra"),
        E("roy6_empress_alexandra", "roy6_anastasia_romanov", "direct", "Mother Alexandra -> Anastasia"),
        E("mon_rom_alexios1", "roy6_anna_komnene", "direct", "Alexios I Komnenos -> daughter Anna Komnene"),
        E("pc_byzantine_palaiologoi_moscow", "roy6_sophia_palaiologina", "direct", "Byzantine Palaiologoi -> Sophia Palaiologina"),
        E("roy6_sophia_palaiologina", "mon_rus_ivan3", "direct", "Marriage of Sophia Palaiologina & Grand Prince Ivan III of Moscow (1472)"),
    ]

    # =========================================================================
    # SECTION C: LOMBARDS, ICELAND/VINLAND, WALES, RAJPUTS, LADAKH, MOGHULISTAN, MALAY, AFRICA, ASIA
    # =========================================================================
    chain([
        "eur_lom_gambara",
        ("chr6_gambara", "Matriarch Gambara of the Winnili / Lombards (Paul the Deacon Book I)", 17, "c. 4th c. CE", "Founding Lombard Matriarch", "Counselor mother of Ibor and Aio.", False),
        ("chr6_ibor_aio", "Duke Ibor & Duke Aio (Sons of Gambara)", 17, "c. 4th c. CE", "Leaders of Lombard Migration", "Led the Lombards out of Scandinavia.", False),
        ("chr6_agelmund", "King Agelmund (Son of Aio; 1st King of Lombards, 33 yrs)", 18, "c. 5th c. CE", "1st Sovereign King of Lombards", "First crowned king in Historia Langobardorum.", False),
        ("chr6_alboin", "King Alboin of Lombardy (Son of Audoin; Conqueror of Italy 568 CE)", 19, "r. 560–572 CE", "Founder of Lombard Kingdom of Italy", "Conquered northern Italy (Lombardy).", False),
        ("chr6_authari", "King Authari (+ Catholic Queen Theodelinda of Bavaria, r. 584–590 CE)", 19, "r. 584–590 CE", "Lombard Monarch of Pavia", "Married Bavarian princess Theodelinda.", False),
        ("chr6_rothari", "King Rothari (Promulgated Edictum Rothari 643 CE)", 19, "r. 636–652 CE", "Lombard Lawgiver King", "Codified Lombard customary law.", False),
        ("chr6_liutprand", "King Liutprand of the Lombards (r. 712–744 CE)", 19, "r. 712–744 CE", "Greatest Lombard King of Italy", "Height of Lombard Italy.", False),
        ("chr6_desiderius", "King Desiderius of the Lombards (Last King, r. 756–774 CE; Father-in-Law of Charlemagne)", 19, "r. 756–774 CE", "Last Lombard King of Italy", "Daughter Desiderata wed Charlemagne.", False),
    ], "europe_norse", ["Paul the Deacon Historia Langobardorum"], "Lombard Royal Succession")
    nodes.append(N("chr6_theodelinda", "Queen Theodelinda of the Lombards (c. 570–628 CE; Correspondent of Pope Gregory I)", "europe_norse", 19, "c. 570–628 CE", "Bavarian-Garibalding Queen Converting Lombards", ["Paul the Deacon Book III-IV"], "Bridged Lombard royalty with Catholic Europe."))
    edges.append(E("chr6_authari", "chr6_theodelinda", "direct", "Marriage of Authari & Queen Theodelinda"))

    # Iceland & Vinland
    nodes += [
        N("chr6_ingolfur_arnarson", "Ingólfur Arnarson (1st Permanent Settler of Iceland at Reykjavik, 874 CE)", "europe_norse", 19, "874 CE (Landnámabók)", "Founding Settler of Iceland", ["Landnámabók"], "First Norse landnámsmaðr of Iceland."),
        N("chr6_ketil_flatnose", "Jarl Ketil Flatnose (Hebridean Norse Lord; Father of Aud the Deep-Minded)", "europe_norse", 19, "9th c. CE (Landnámabók)", "Hebridean Sea-Lord", ["Landnámabók"], "Father of Aud the Deep-Minded."),
        N("chr6_aud_deepminded", "Aud / Unn the Deep-Minded (Matriarch Settler of Western Iceland)", "europe_norse", 19, "c. 834–900 CE (Landnámabók)", "Ancestress of Snorri Sturluson & Western Clans", ["Landnámabók"], "Widow of Olaf the White of Dublin who settled Breiðafjörður."),
        N("chr6_erik_the_red", "Erik the Red / Eiríkr Þorvaldsson (Founder of Norse Greenland, 985 CE)", "europe_norse", 20, "950–c. 1003 CE (Vinland Sagas)", "Explorer of Greenland", ["Landnámabók", "Eirik's Saga"], "Father of Leif Erikson."),
        N("chr6_leif_erikson", "Leif Erikson ('Leif the Lucky', Landed in Vinland / North America c. 1000 CE)", "europe_norse", 20, "c. 970–1020 CE (Vinland Sagas)", "First Known European to Reach North America", ["Saga of the Greenlanders"], "Son of Erik the Red who explored Helluland, Markland & Vinland (Newfoundland).", major=True),
        N("chr6_gudrid_vinland", "Gudrid Thorbjarnardóttir (Mother of Snorri Thorfinnsson, First European Born in America)", "europe_norse", 20, "c. 980–1050 CE (Vinland Sagas)", "Matriarch Explorer of Vinland & Rome Pilgrim", ["Saga of the Greenlanders"], "Married Thorstein (son of Erik the Red) & Thorfinn Karlsefni."),
    ]
    edges += [
        E("eur_ice_ingolfur", "chr6_ingolfur_arnarson", "direct", "Iceland settler anchor -> Ingólfur"),
        E("eur_ice_aud_deepminded", "chr6_ketil_flatnose", "direct", "Landnámabók -> Ketil Flatnose"),
        E("chr6_ketil_flatnose", "chr6_aud_deepminded", "direct", "Ketil Flatnose -> daughter Aud the Deep-Minded"),
        E("eur_ice_erik_leif", "chr6_erik_the_red", "direct", "Thorvald Asvaldsson -> Erik the Red"),
        E("chr6_erik_the_red", "chr6_leif_erikson", "direct", "Erik the Red -> son Leif Erikson"),
        E("chr6_leif_erikson", "chr6_gudrid_vinland", "expansion", "Vinland expedition kinship: Erik's family & Gudrid Thorbjarnardóttir"),
    ]

    # Wales to Tudors
    chain([
        "eur_wal_cunedda",
        ("chr6_cunedda", "King Cunedda Wledig (Founder of Kingdom of Gwynedd, c. 400 CE)", 19, "c. 400 CE (Lloyd Wales)", "Patriarch of Gwynedd", "Migrated from Manaw Gododdin to North Wales.", False),
        ("chr6_maelgwn_gwynedd", "King Maelgwn Gwynedd (Great-Grandson of Cunedda, d. 547 CE)", 19, "d. 547 CE (Gildas; Lloyd)", "High King of Gwynedd", "Contemporary of Gildas.", False),
        ("chr6_cadwaladr", "King Cadwaladr ap Cadwallon ('Fendigaid', d. 682 CE; Red Dragon Ancestor)", 19, "d. 682 CE", "Son of Cadwallon", "Forebear of the Welsh Red Dragon banner.", False),
        ("chr6_rhodri_mawr", "King Rhodri Mawr / Rhodri the Great (r. 844–878 CE)", 20, "820–878 CE (Lloyd Vol. 1)", "Unifier of Gwynedd, Powys & Seisyllwg", "Ancestor of medieval Welsh royal lines.", False),
        ("chr6_hywel_dda", "King Hywel Dda ('Hywel the Good', Grandson of Rhodri Mawr; Lawgiver, d. 950)", 20, "880–950 CE", "Codifier of Welsh Laws", "United nearly all Wales.", False),
        ("chr6_gruffydd_llywelyn", "King Gruffydd ap Llywelyn (Sole Unifier of All Wales, r. 1055–1063)", 20, "c. 1007–1063 CE", "King of All Wales", "Contemporary of Edward the Confessor & Harold II.", False),
        ("chr6_owain_gwynedd", "King Owain Gwynedd (r. 1137–1170; Grandfather of Llywelyn the Great)", 20, "c. 1100–1170 CE", "1st Prince of Wales in Contemporary Charters", "Defeated Henry II's campaigns in Gwynedd.", False),
        ("chr6_llywelyn_great", "Prince Llywelyn ap Iorwerth / Llywelyn the Great (r. 1195–1240; + Joan dau. of King John!)", 20, "c. 1173–1240 CE", "Great Prince of Aberffraw & Lord of Snowdon", "Married Princess Joan (daughter of King John of England).", False),
        ("chr6_llywelyn_last", "Prince Llywelyn ap Gruffydd ('The Last', Grandson of Llywelyn the Great, d. 1282)", 20, "c. 1223–1282 CE", "Last Sovereign Prince of Independent Wales", "Fell in 1282 against Edward I.", False),
        ("chr6_owen_tudor", "Owen Tudor / Owain ap Maredudd (Kinsman of Llywelyn; + Queen Catherine of Valois)", 21, "c. 1400–1461 CE", "Grandfather of King Henry VII Tudor", "United Welsh Gwynedd royal line with French Valois & English Crown.", False),
        "mon_eng_henry7",
    ], "europe_norse", ["J.E. Lloyd History of Wales (1912)", "Welsh Royal Genealogies"], "Welsh Sovereign Succession to Tudors")

    # Rajputs, Ladakh, Moghulistan, Sikhs, Malay Annals, Africa, Qing & Heian
    chain([
        "ind_raj_mewar_sisodia",
        ("chr6_bappa_rawal", "Bappa Rawal / Kalbhoja (Founder of Mewar Sovereignty, 734 CE)", 20, "c. 713–753 CE (Tod Rajasthan)", "Solar Guhila Hero of Chittor", "Tradition traces from Lava -> Guhaditya -> Bappa Rawal.", False),
        ("chr6_rana_kumbha", "Rana Kumbha of Mewar (r. 1433–1468; Builder of Vijay Stambh & Kumbhalgarh)", 21, "1417–1468 CE", "Great Sisodia Builder & Scholar-King", "Repelled Malwa and Gujarat sultanates.", False),
        ("chr6_rana_sanga", "Rana Sanga / Sangram Singh (r. 1508–1528; Adversary of Babur at Khanwa)", 21, "1482–1528 CE", "Paramount Rajput Monarch", "Grandfather of Maharana Pratap.", False),
        ("chr6_maharana_pratap", "Maharana Pratap of Mewar (r. 1572–1597; Battle of Haldighati 1576)", 21, "1540–1597 CE (Tod Rajasthan)", "Icon of Rajput Independence", "Grandson of Rana Sanga; resisted Mughal Akbar from Kumbhalgarh & Chavand.", True),
    ], "vedic", ["James Tod Annals of Rajasthan Vols. 1-2"], "Mewar Suryavamshi Rajput Succession")
    edges.append(E("ind5_lava", "chr6_bappa_rawal", "expansion", "Solar Rama -> Lava -> Mewar Guhila/Sisodias -> Bappa Rawal"))

    nodes += [
        N("chr6_rao_jodha", "Rao Jodha of Marwar (Founded Jodhpur & Mehrangarh Fort, 1459 CE)", "vedic", 21, "1416–1489 CE (Tod Vol. 2)", "Rathore King of Marwar", ["Tod Rajasthan Vol. 2"], "Solar Rathore founder of Jodhpur."),
        N("chr6_sawai_jai_singh2", "Maharaja Sawai Jai Singh II of Amber/Jaipur (r. 1699–1743; Jantar Mantar Founder)", "vedic", 21, "1688–1743 CE (Tod Vol. 2)", "Founder of Jaipur & Astronomer-King", ["Tod Rajasthan Vol. 2"], "Kachwaha Suryavamshi king descended from Kusha."),
        N("chr6_prithviraj_chauhan", "Samrat Prithviraj Chauhan III of Ajmer & Delhi (r. 1178–1192 CE)", "vedic", 20, "c. 1166–1192 CE", "Last Hindu Emperor of Delhi-Ajmer", ["Prithviraj Raso", "Tod Vol. 1"], "Celebrated in North Indian epic history."),
        N("chr6_rawal_jaisal", "Rawal Jaisal of Jaisalmer (Founded Jaisalmer Fort, 1156 CE)", "vedic", 20, "12th c. CE", "Yadava Bhati Founder of Jaisalmer", ["Tod Vol. 2"], "Bhati Rajput tracing lineage from Krishna's Yadavas."),
        N("chr6_lhachen_palgyigon", "King Lhachen Palgyigon (1st Independent King of Ladakh / Maryul, c. 930 CE)", "vedic", 19, "10th c. CE (Chronicles of Ladakh)", "Eldest Son of Nyi-ma-mgon", ["A.H. Francke Chronicles of Ladakh"], "Established the Yarlung Tibetan dynasty of Ladakh."),
        N("chr6_king_bhagan", "King Lhachen Bhagan (Founder of Namgyal Dynasty of Ladakh, c. 1460 CE)", "vedic", 21, "c. 1460 CE", "Founder of Namgyal House", ["Francke Chronicles of Ladakh"], "Inaugurated the Namgyal line."),
        N("chr6_sengge_namgyal", "King Sengge Namgyal ('Lion King' of Ladakh, r. 1616–1642; Built Leh Palace)", "vedic", 21, "c. 1570–1642 CE", "Greatest Namgyal King of Ladakh", ["Francke Chronicles of Ladakh"], "Built nine-story Leh Palace & Hemis Monastery."),
    ]
    edges += [
        E("ind_raj_marwar_amber", "chr6_rao_jodha", "direct", "Marwar anchor -> Rao Jodha"),
        E("ind_raj_marwar_amber", "chr6_sawai_jai_singh2", "direct", "Amber Kachwaha anchor -> Sawai Jai Singh II"),
        E("ind_raj_chauhan_bhati", "chr6_prithviraj_chauhan", "direct", "Chauhan anchor -> Prithviraj Chauhan"),
        E("ind_raj_chauhan_bhati", "chr6_rawal_jaisal", "direct", "Bhati Yadava anchor -> Rawal Jaisal"),
        E("tib_ladakh_nyimagon", "chr6_lhachen_palgyigon", "direct", "Nyi-ma-mgon -> eldest son Lhachen Palgyigon"),
        E("tib_ladakh_sengge_namgyal", "chr6_king_bhagan", "direct", "Ladakh Namgyal anchor -> King Bhagan"),
        E("chr6_king_bhagan", "chr6_sengge_namgyal", "direct", "Bhagan -> Jamyang -> Sengge Namgyal"),
    ]

    nodes += [
        N("chr6_tughlugh_timur", "Khan Tughlugh Timur of Moghulistan (r. 1347–1363; 1st Muslim Eastern Chagatayid)", "steppe", 20, "1329–1363 CE (Tarikh-i-Rashidi)", "Founder of Moghulistan Line", ["Tarikh-i-Rashidi"], "Chagatayid khan of Kashgaria & Semirechye."),
        N("chr6_yunus_khan", "Khan Yunus Khan of Moghulistan (Maternal Grandfather of Mughal Emperor Babur, d. 1487)", "steppe", 21, "c. 1416–1487 CE", "Chagatayid Ancestor of Babur & Mughals", ["Tarikh-i-Rashidi", "Baburnama"], "Grandfather of Emperor Babur via daughter Qutlugh Nigar Khanum."),
        N("chr6_sultan_said_khan", "Sultan Said Khan of Yarkand (Founder of Yarkent Khanate, r. 1514–1533)", "steppe", 21, "1487–1533 CE", "Grandson of Yunus Khan", ["Tarikh-i-Rashidi"], "Led expeditions across the Pamirs & Ladakh."),
        N("chr6_mirza_haidar_dughlat", "Mirza Muhammad Haidar Dughlat (1499–1551; Ruler of Kashmir & Author of Tarikh-i-Rashidi)", "steppe", 21, "1499–1551 CE", "Mughal Cousin & Historian-Conqueror", ["Tarikh-i-Rashidi"], "First cousin of Emperor Babur; conquered Kashmir (1540–1551)."),
        N("chr6_guru_nanak", "Guru Nanak Dev Ji (1469–1539; Founder of Sikhism, Bedi Khatri Tradition)", "vedic", 21, "1469–1539 CE (Janamsakhis; Bachittar Natak)", "1st Sikh Guru", ["Janamsakhis", "Bachittar Natak"], "Founder of Sikhism."),
        N("chr6_guru_gobind_singh", "Guru Gobind Singh Ji (1666–1708; 10th Guru & Founder of Khalsa, Author of Bachittar Natak)", "vedic", 21, "1666–1708 CE", "10th Sikh Guru", ["Bachittar Natak"], "Founded the Khalsa (1699) and composed Bachittar Natak linking Sodhi/Bedi houses to Kusha/Lava."),
        N("chr6_sultan_mansur_shah", "Sultan Mansur Shah of Malacca (r. 1459–1477; Golden Age of Malacca)", "southeast_asia", 20, "d. 1477 CE (Sejarah Melayu)", "Greatest Sultan of Malacca", ["Sejarah Melayu Ch. 14–19"], "Expanded Malacca across the Malay Peninsula & Sumatra."),
        N("chr6_sultan_mahmud_shah", "Sultan Mahmud Shah of Malacca & Johor (r. 1488–1528)", "southeast_asia", 20, "d. 1528 CE (Sejarah Melayu)", "Last Sultan of Malacca & Founder of Johor Line", ["Sejarah Melayu Ch. 25–34"], "Reigned during 1511; sons founded Perak and Johor sultanates."),
        N("chr6_queen_amina_zazzau", "Queen Amina of Zazzau / Zaria (fl. 16th c. CE; Warrior Queen in Kano Chronicle)", "african", 20, "16th c. CE (Kano Chronicle)", "Hausa Sovereign Queen of Zaria", ["Kano Chronicle", "Sultan Bello"], "Expanded Zazzau's walled trade cities across northern Nigeria."),
        N("chr6_empress_eleni", "Empress Eleni of Ethiopia (d. 1522; Regent Who Initiated Portuguese Alliance)", "african", 20, "c. 1431–1522 CE", "Queen of Hadiya & Ethiopian Regent", ["Ethiopian Royal Chronicles"], "Reigned across Ba'eda Maryam, Eskender, Na'od & young Lebna Dengel."),
        N("chr6_empress_mentewab", "Empress Mentewab of Gondar (1706–1773; Regent for Iyasu II & Iyoas)", "african", 21, "1706–1773 CE", "Builder of Qusquam Complex in Gondar", ["Ethiopian Royal Chronicles", "James Bruce"], "Dominant Solomonic empress regent of 18th-century Gondar."),
        N("chr6_empress_taytu_betul", "Empress Taytu Betul (1851–1918; Wife of Emperor Menelik II & Strategist of Adwa)", "african", 21, "1851–1918 CE", "Consort Empress & Defender of Ethiopia", ["Ethiopian Imperial Chronicles"], "Co-architect of the Victory of Adwa (1896)."),
        N("chr6_empress_dowager_cixi", "Empress Dowager Cixi of Qing China (1835–1908; Regent of Tongzhi & Guangxu)", "chinese", 22, "1835–1908 CE", "De Facto Ruler of Late Qing China", ["Draft History of Qing"], "Consort of Xianfeng; dominant regent from 1861–1908."),
        N("chr6_emperor_puyi", "Emperor Puyi / Xuantong (1906–1967; Last Emperor of Qing China)", "chinese", 22, "1906–1967 CE", "Final Emperor of Imperial China", ["Draft History of Qing"], "Abdicated in 1912 as 12th and final Aisin Gioro emperor."),
        N("chr6_fujiwara_kamatari", "Fujiwara no Kamatari (614–669 CE; Co-Architect of Taika Reforms & Founder of Fujiwara)", "japan_korea", 19, "614–669 CE (Nihon Shoki)", "Founder of Fujiwara Regent Clan", ["Nihongi"], "Descendant of Nakatomi/Ame-no-Koyane."),
        N("chr6_murasaki_shikibu", "Lady Murasaki Shikibu (c. 973–1014 CE; Heian Court Author of The Tale of Genji)", "japan_korea", 20, "c. 973–1014 CE", "Fujiwara Author at Empress Shōshi's Court", ["Heian Literary Annals"], "Descendant of Fujiwara no Yoshifusa."),
    ]
    edges += [
        E("stp_moghul_tughlugh", "chr6_tughlugh_timur", "direct", "Moghulistan anchor -> Tughlugh Timur"),
        E("chr6_tughlugh_timur", "chr6_yunus_khan", "direct", "Tughlugh Timur -> Khizr Khoja -> Shir Ali -> Yunus Khan"),
        E("chr6_yunus_khan", "mon_mug_babur_ind", "direct", "Yunus Khan -> Qutlugh Nigar Khanum -> Emperor Babur"),
        E("chr6_yunus_khan", "chr6_sultan_said_khan", "direct", "Yunus Khan -> Sultan Ahmad Alaq -> Sultan Said Khan"),
        E("chr6_sultan_said_khan", "chr6_mirza_haidar_dughlat", "direct", "Dughlat kinsman & chronicler of Sultan Said Khan"),
        E("pc_sikh_guru_nanak", "chr6_guru_nanak", "direct", "Sikh Bedi anchor -> Guru Nanak Dev Ji"),
        E("chr6_guru_nanak", "chr6_guru_gobind_singh", "expansion", "Line of Ten Sikh Gurus -> Guru Gobind Singh Ji"),
        E("chr6_guru_gobind_singh", "mon_ind_ranjit_singh", "expansion", "Khalsa confederacy -> Maharaja Ranjit Singh"),
        E("mal_mansur_mahmud", "chr6_sultan_mansur_shah", "direct", "Malacca anchor -> Sultan Mansur Shah"),
        E("chr6_sultan_mansur_shah", "chr6_sultan_mahmud_shah", "direct", "Mansur Shah -> Alauddin Riayat Shah -> Mahmud Shah"),
        E("pc_african_kings_queens", "chr6_queen_amina_zazzau", "direct", "African sovereign queens -> Queen Amina"),
        E("pc_african_kings_queens", "chr6_empress_eleni", "direct", "African sovereign queens -> Empress Eleni"),
        E("chr6_empress_eleni", "chr6_empress_mentewab", "expansion", "Solomonic royal queens -> Empress Mentewab"),
        E("chr6_empress_mentewab", "chr6_empress_taytu_betul", "expansion", "Solomonic queens -> Empress Taytu Betul"),
        E("chr6_empress_taytu_betul", "mon_eth_menelik2", "direct", "Marriage of Emperor Menelik II & Empress Taytu Betul"),
        E("eas5_qing_qianlong", "chr6_empress_dowager_cixi", "direct", "Qianlong -> Jiaqing -> Daoguang -> Xianfeng (+ Empress Dowager Cixi)"),
        E("chr6_empress_dowager_cixi", "chr6_emperor_puyi", "direct", "Cixi -> Prince Chun Line -> Emperor Puyi"),
        E("pc_japan_nara_heian", "chr6_fujiwara_kamatari", "direct", "Heian court anchor -> Fujiwara no Kamatari"),
        E("chr6_fujiwara_kamatari", "chr6_murasaki_shikibu", "direct", "Fujiwara lineage -> Lady Murasaki Shikibu"),
    ]

    # =========================================================================
    # SECTION D: FAMOUS HISTORICAL FIGURES, EXPLORERS & FOUNDERS (Individual Nodes)
    # =========================================================================
    fam_nodes = [
        ("fam6_maimonides", "Rabbi Moses ben Maimon / Maimonides / Rambam (1138–1204; Mishneh Torah)", "biblical", 20, "1138–1204 CE", "Sephardic Nagid & Author of Guide for the Perplexed", False),
        ("fam6_abraham_ben_maimon", "Rabbi Abraham ben Maimon (1186–1237; Son & Nagid Successor of Rambam)", "biblical", 21, "1186–1237 CE", "Nagid of Egyptian Jewry", False),
        ("fam6_ibn_sina", "Ibn Sina / Avicenna (980–1037 CE; Author of Canon of Medicine)", "arabian", 20, "980–1037 CE", "Persian Polymath & Physician", False),
        ("fam6_ibn_rushd", "Ibn Rushd / Averroes (1126–1198 CE; Cordoba Philosopher & Jurist)", "arabian", 20, "1126–1198 CE", "Andalusian Philosopher", False),
        ("fam6_omar_khayyam", "Omar Khayyam (1048–1131 CE; Nishapur Astronomer, Mathematician & Poet)", "iranian", 20, "1048–1131 CE", "Astronomer of Sultan Malik-Shah I", False),
        ("fam6_rumi", "Mevlana Jalal al-Din Rumi (1207–1273 CE; Mystical Poet of Balkh & Konya)", "arabian", 20, "1207–1273 CE", "Sufi Poet & Founder of Mevlevi Tradition", False),
        ("fam6_sultan_walad", "Sultan Walad (1226–1312 CE; Son of Rumi & Organizer of Mevlevi Order)", "arabian", 21, "1226–1312 CE", "Son of Jalal al-Din Rumi", False),
        ("fam6_marco_polo", "Marco Polo (1254–1324 CE; Venetian Traveler at Kublai Khan's Court)", "europe_norse", 20, "1254–1324 CE", "Venetian Silk Road Chronicler", False),
        ("fam6_vasco_da_gama", "Vasco da Gama (c. 1460–1524 CE; Navigator to India Under Manuel I)", "europe_norse", 21, "c. 1460–1524 CE", "1st Count of Vidigueira & Viceroy of India", False),
        ("fam6_christopher_columbus", "Christopher Columbus (1451–1506 CE; Admiral of the Ocean Sea)", "europe_norse", 21, "1451–1506 CE", "Transatlantic Navigator for Ferdinand & Isabella", False),
        ("fam6_diego_columbus", "Diego Columbus (1479–1526 CE; Son of Columbus; + Maria de Toledo -> Dukes of Veragua)", "europe_norse", 21, "1479–1526 CE", "Viceroy of the Indies", False),
        ("fam6_leonardo_da_vinci", "Leonardo da Vinci (1452–1519 CE; Painter, Engineer & Polymath of Florence)", "europe_norse", 21, "1452–1519 CE", "Renaissance Polymath", True),
        ("fam6_michelangelo", "Michelangelo Buonarroti (1475–1564 CE; Sculptor, Painter & Architect)", "europe_norse", 21, "1475–1564 CE", "Renaissance Master Protected by Lorenzo de' Medici", False),
        ("fam6_galileo_galilei", "Galileo Galilei (1564–1642 CE; Astronomer & Physicist of Pisa/Florence)", "europe_norse", 21, "1564–1642 CE", "Father of Observational Astronomy", False),
        ("fam6_isaac_newton", "Sir Isaac Newton (1642–1727 CE; Principia & Author of Chronology of Ancient Kingdoms Amended 1728!)", "europe_norse", 21, "1642–1727 CE", "Physicist, Mathematician & Atlas Primary Source Author", True),
        ("fam6_william_shakespeare", "William Shakespeare (1564–1616 CE; Playwright Under Elizabeth I & James I)", "europe_norse", 21, "1564–1616 CE", "English Dramatist & Poet", False),
        ("fam6_susanna_hall", "Susanna Shakespeare Hall (1583–1649 CE; Eldest Daughter & Heir of William Shakespeare)", "europe_norse", 21, "1583–1649 CE", "Daughter of William Shakespeare", False),
        ("fam6_george_washington", "President George Washington (1732–1799 CE; 1st U.S. President; Gateway Descent from King Edward III)", "europe_norse", 22, "1732–1799 CE", "Father of the United States (Plantagenet-Wessex Descent)", True),
        ("fam6_thomas_jefferson", "President Thomas Jefferson (1743–1826 CE; 3rd U.S. President; Gateway Descent via King David I & Edward III)", "europe_norse", 22, "1743–1826 CE", "Author of Declaration of Independence (Scottish-Plantagenet Descent)", False),
        ("fam6_winston_churchill", "Sir Winston Churchill (1874–1965 CE; Spencer-Churchill Descendant of Duke of Marlborough & Edward I)", "europe_norse", 22, "1874–1965 CE", "British Prime Minister & Historian", False),
        ("fam6_abraham_lincoln", "President Abraham Lincoln (1809–1865 CE; 16th U.S. President)", "europe_norse", 22, "1809–1865 CE", "16th President of the United States", False),
        ("fam6_robert_todd_lincoln", "Robert Todd Lincoln (1843–1926 CE; Son of Abraham Lincoln & U.S. Secretary of War)", "europe_norse", 22, "1843–1926 CE", "Son of President Abraham Lincoln", False),
        ("fam6_laozi", "Laozi / Lao Tzu (Author of Dao De Jing; Ancestral Claim of Tang Dynasty Li Clan)", "chinese", 16, "c. 6th c. BCE", "Founder of Philosophical Daoism", False),
        ("fam6_sun_tzu", "Sun Tzu / Sun Wu (c. 544–496 BCE; Military Strategist & Author of Art of War)", "chinese", 16, "c. 544–496 BCE", "Spring & Autumn Military Philosopher", False),
        ("fam6_mencius", "Mencius / Meng Ke (c. 372–289 BCE; Confucian Sage Descended from Duke of Lu / Zhou)", "chinese", 17, "c. 372–289 BCE", "Second Sage of Confucianism", False),
        ("fam6_sima_qian", "Sima Qian (c. 145–86 BCE; Grand Historian & Author of Shiji Under Han Wudi)", "chinese", 18, "c. 145–86 BCE", "Author of Records of the Grand Historian (Shiji)", False),
        ("fam6_chanakya", "Chanakya / Kautilya (fl. 320 BCE; Architect of Maurya Empire & Author of Arthashastra)", "vedic", 18, "fl. 320 BCE", "Chief Counselor to Chandragupta Maurya", False),
        ("fam6_kalidasa", "Kalidasa (c. 4th–5th c. CE; Classical Sanskrit Poet at Chandragupta II's Court)", "vedic", 19, "c. 4th–5th c. CE", "Classical Poet of Abhijnanashakuntalam & Raghuvamsha", False),
        ("fam6_adi_shankara", "Adi Shankaracharya (c. 8th c. CE; Unifier of Advaita Vedanta & Four Mathas)", "vedic", 20, "c. 788–820 CE trad.", "Advaita Vedanta Philosopher-Saint", False),
    ]
    for nid, nm, trad, tr, er, rl, mj in fam_nodes:
        nodes.append(N(nid, nm, trad, tr, er, rl, ["Primary Biographical & Chronicle Archives"], f"{nm}.", major=mj))

    edges += [
        E("fam_maimonides", "fam6_maimonides", "direct", "Maimonides anchor -> Rambam"),
        E("fam6_maimonides", "fam6_abraham_ben_maimon", "direct", "Rambam -> son Nagid Abraham ben Maimon"),
        E("fam_ibn_sina_rushd_rumi", "fam6_ibn_sina", "direct", "Islamic Golden Age scholars -> Ibn Sina"),
        E("fam_ibn_sina_rushd_rumi", "fam6_ibn_rushd", "direct", "Islamic Golden Age scholars -> Ibn Rushd"),
        E("fam_ibn_sina_rushd_rumi", "fam6_omar_khayyam", "direct", "Islamic Golden Age scholars -> Omar Khayyam"),
        E("stp5_malik_shah1", "fam6_omar_khayyam", "cognate", "Sultan Malik-Shah I patronized Omar Khayyam's Jalali calendar"),
        E("fam_ibn_sina_rushd_rumi", "fam6_rumi", "direct", "Scholarly network -> Mevlana Rumi"),
        E("fam6_rumi", "fam6_sultan_walad", "direct", "Rumi -> son Sultan Walad"),
        E("fam_columbus_vasco_polo", "fam6_marco_polo", "direct", "Explorers -> Marco Polo"),
        E("mngr_imp_10_qubilai_qa_an_kublai_khan_fo", "fam6_marco_polo", "cognate", "Marco Polo served at Emperor Kublai Khan's Yuan court"),
        E("fam_columbus_vasco_polo", "fam6_vasco_da_gama", "direct", "Explorers -> Vasco da Gama"),
        E("mon_por_manuel1", "fam6_vasco_da_gama", "cognate", "King Manuel I commissioned Vasco da Gama's 1497 voyage to India"),
        E("fam_columbus_vasco_polo", "fam6_christopher_columbus", "direct", "Explorers -> Christopher Columbus"),
        E("fam6_christopher_columbus", "fam6_diego_columbus", "direct", "Christopher Columbus -> son Diego Columbus"),
        E("fam_renaissance_science", "fam6_leonardo_da_vinci", "direct", "Renaissance masters -> Leonardo da Vinci"),
        E("fam_renaissance_science", "fam6_michelangelo", "direct", "Renaissance masters -> Michelangelo"),
        E("fam_renaissance_science", "fam6_galileo_galilei", "direct", "Renaissance masters -> Galileo Galilei"),
        E("fam_renaissance_science", "fam6_isaac_newton", "direct", "Renaissance masters -> Sir Isaac Newton"),
        E("fam_shakespeare_joan", "fam6_william_shakespeare", "direct", "Tudor-Valois icons -> William Shakespeare"),
        E("fam6_william_shakespeare", "fam6_susanna_hall", "direct", "William Shakespeare -> daughter Susanna Hall"),
        E("fam_washington_jefferson", "fam6_george_washington", "direct", "Founders -> George Washington"),
        E("mon_eng_edward3", "fam6_george_washington", "direct", "Colonial Virginia gateway from King Edward III -> George Washington"),
        E("fam_washington_jefferson", "fam6_thomas_jefferson", "direct", "Founders -> Thomas Jefferson"),
        E("eur5_malcolm3", "fam6_thomas_jefferson", "direct", "Jane Randolph -> King David I (son of Malcolm III) -> Thomas Jefferson"),
        E("fam_churchill_lincoln", "fam6_winston_churchill", "direct", "Churchill/Lincoln anchor -> Sir Winston Churchill"),
        E("fam_churchill_lincoln", "fam6_abraham_lincoln", "direct", "Churchill/Lincoln anchor -> President Abraham Lincoln"),
        E("fam6_abraham_lincoln", "fam6_robert_todd_lincoln", "direct", "Abraham Lincoln -> son Robert Todd Lincoln"),
        E("fam_asian_sages", "fam6_laozi", "direct", "Asian classical masters -> Laozi"),
        E("fam_asian_sages", "fam6_sun_tzu", "direct", "Asian classical masters -> Sun Tzu"),
        E("fam_asian_sages", "fam6_mencius", "direct", "Asian classical masters -> Mencius"),
        E("fam_asian_sages", "fam6_sima_qian", "direct", "Asian classical masters -> Sima Qian"),
        E("eas5_han_wudi", "fam6_sima_qian", "cognate", "Sima Qian served as Grand Historian at Han Wudi's court"),
        E("fam_asian_sages", "fam6_chanakya", "direct", "Asian classical masters -> Chanakya"),
        E("ind5_chandragupta_maurya", "fam6_chanakya", "cognate", "Chanakya mentored Emperor Chandragupta Maurya"),
        E("fam_asian_sages", "fam6_kalidasa", "direct", "Asian classical masters -> Kalidasa"),
        E("ind5_chandragupta2", "fam6_kalidasa", "cognate", "Kalidasa adorned Chandragupta II Vikramaditya's court"),
        E("fam_asian_sages", "fam6_adi_shankara", "direct", "Asian classical masters -> Adi Shankaracharya"),
    ]

    return {
        "module": "48_wave6_global_royalty_person_by_person",
        "title": "Wave 6 Person-by-Person Global Royalty (Northern/Central Europe, Habsburgs, Windsors to 2026, Lombards, Iceland/Vinland, Wales, Rajputs, Ladakh, Moghulistan, Malay Annals, African Queens & Historical Figures)",
        "nodes": nodes,
        "edges": edges,
    }
