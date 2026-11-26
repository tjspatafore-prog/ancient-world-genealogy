"""
Module 37: Individualized Sovereigns, Emperors, Queens & Caliphs Across Existing
Noahic-Connected Chronicles (Roman Republic/Empire/Byzantium, England/Britain,
France, Spain, Portugal, HRE/Germany, Russia, Ottomans, Caliphates, Safavids,
Mughals/India, Ethiopia & Songhai).

All nodes anchor cleanly into already-verified Noahic lines (major=False so default
'Landmarks' remains clean, while 'Expand All' or clicking a house reveals every king!).
"""

from . import N, E


def add_monarchs(nodes, edges, parent_id, items, tradition, sources, edge_type="direct"):
    prev = parent_id
    for item in items:
        nid, name, tier, era = item[0], item[1], item[2], item[3]
        role = item[4] if len(item) > 4 else "Sovereign / Monarch"
        nodes.append(N(nid, name, tradition, tier, era, role, sources, f"{name} ({', '.join(sources)}).", major=False))
        edges.append(E(prev, nid, edge_type, f"{', '.join(sources)}: succession"))
        prev = nid


def build_module():
    nodes, edges = [], []

    # 1. ROMAN REPUBLIC, EMPIRE & BYZANTIUM (~40 individuals)
    add_monarchs(nodes, edges, "grk_julius_augustus", [
        ("mon_rom_brutus_founder", "Lucius Junius Brutus (1st Consul of Rome, 509 BCE)", 15, "509 BCE", "Consul"),
        ("mon_rom_cincinnatus", "Lucius Quinctius Cincinnatus (458 BCE Dictator)", 15, "c. 519–430 BCE", "Dictator"),
        ("mon_rom_scipio_africanus", "Scipio Africanus (Victor of Zama, 202 BCE)", 18, "236–183 BCE", "Roman General"),
        ("mon_rom_cato_elder", "Cato the Elder (234–149 BCE)", 18, "234–149 BCE", "Censor & Historian"),
        ("mon_rom_gracchi", "Tiberius & Gaius Gracchus (133–121 BCE)", 18, "2nd c. BCE", "Tribunes of the Plebs"),
        ("mon_rom_marius_sulla", "Gaius Marius & Lucius Cornelius Sulla", 18, "157–78 BCE", "Consuls & Dictator"),
        ("mon_rom_pompey_cicero", "Pompey the Great & Marcus Tullius Cicero", 18, "106–43 BCE", "Consul & Statesman"),
        ("mon_rom_mark_antony", "Mark Antony (Triumvir, d. 30 BCE)", 18, "83–30 BCE", "Roman Triumvir"),
    ], "greek", ["Livy", "Plutarch Lives", "Echard Roman History"], edge_type="expansion")

    add_monarchs(nodes, edges, "rom_julio_claudians", [
        ("mon_rom_tiberius", "Emperor Tiberius (14–37 CE)", 19, "14–37 CE"),
        ("mon_rom_caligula", "Emperor Caligula (37–41 CE)", 19, "37–41 CE"),
        ("mon_rom_claudius", "Emperor Claudius (41–54 CE, Conquest of Britain)", 19, "41–54 CE"),
        ("mon_rom_nero", "Emperor Nero (54–68 CE)", 19, "54–68 CE"),
    ], "greek", ["Suetonius Twelve Caesars", "Tacitus Annals"])

    add_monarchs(nodes, edges, "rom_echard_imperial_bridge", [
        ("mon_rom_vespasian", "Emperor Vespasian (69–79 CE, Flavian Founder)", 19, "69–79 CE"),
        ("mon_rom_titus", "Emperor Titus (79–81 CE, Siege of Jerusalem 70 CE)", 19, "79–81 CE"),
        ("mon_rom_domitian", "Emperor Domitian (81–96 CE)", 19, "81–96 CE"),
        ("mon_rom_nerva", "Emperor Nerva (96–98 CE)", 19, "96–98 CE"),
        ("mon_rom_trajan", "Emperor Trajan (98–117 CE, Imperial Zenith)", 19, "98–117 CE"),
        ("mon_rom_hadrian", "Emperor Hadrian (117–138 CE, Hadrian's Wall)", 19, "117–138 CE"),
        ("mon_rom_antoninus_pius", "Emperor Antoninus Pius (138–161 CE)", 19, "138–161 CE"),
        ("mon_rom_marcus_aurelius", "Emperor Marcus Aurelius (161–180 CE, Philosopher)", 19, "161–180 CE"),
        ("mon_rom_commodus", "Emperor Commodus (180–192 CE)", 19, "180–192 CE"),
        ("mon_rom_septimius_severus", "Emperor Septimius Severus (193–211 CE)", 19, "193–211 CE"),
        ("mon_rom_caracalla", "Emperor Caracalla (198–217 CE)", 19, "198–217 CE"),
        ("mon_rom_elagabalus", "Emperor Elagabalus (218–222 CE)", 19, "218–222 CE"),
        ("mon_rom_severus_alexander", "Emperor Severus Alexander (222–235 CE)", 19, "222–235 CE"),
        ("mon_rom_aurelian", "Emperor Aurelian (270–275 CE, Conqueror of Palmyra)", 19, "270–275 CE"),
        ("mon_rom_diocletian", "Emperor Diocletian (284–305 CE, Tetrarchy)", 19, "284–305 CE"),
    ], "greek", ["Echard Roman History", "Herodian", "Pliny", "Suetonius"], edge_type="expansion")

    add_monarchs(nodes, edges, "rom_constantine_byzantium", [
        ("mon_rom_constantine1", "Emperor Constantine I the Great (306–337 CE)", 19, "306–337 CE"),
        ("mon_rom_julian", "Emperor Julian (361–363 CE)", 19, "361–363 CE"),
        ("mon_rom_theodosius1", "Emperor Theodosius I the Great (379–395 CE)", 19, "379–395 CE"),
        ("mon_rom_justinian1", "Emperor Justinian I & Empress Theodora (527–565 CE)", 19, "527–565 CE"),
        ("mon_rom_heraclius", "Emperor Heraclius (610–641 CE)", 19, "610–641 CE"),
        ("mon_rom_leo3", "Emperor Leo III the Isaurian (717–741 CE)", 19, "717–741 CE"),
        ("mon_rom_basil1", "Emperor Basil I the Macedonian (867–886 CE)", 19, "867–886 CE"),
        ("mon_rom_basil2", "Emperor Basil II Bulgaroktonos (976–1025 CE)", 20, "976–1025 CE"),
        ("mon_rom_alexios1", "Emperor Alexios I Komnenos (1081–1118 CE)", 20, "1081–1118 CE"),
        ("mon_rom_michael8", "Emperor Michael VIII Palaiologos (1259–1282 CE)", 20, "1259–1282 CE"),
        ("mon_rom_constantine11", "Emperor Constantine XI Palaiologos (d. 1453 CE)", 20, "1449–1453 CE"),
    ], "greek", ["Echard Roman History Vol. 4-5", "Ammianus Marcellinus"], edge_type="expansion")

    # 2. KINGS & QUEENS OF ENGLAND & GREAT BRITAIN (~40 individuals)
    add_monarchs(nodes, edges, "eur_wessex_alfred_norman", [
        ("mon_eng_egbert", "King Egbert of Wessex (802–839 CE)", 19, "802–839 CE"),
        ("mon_eng_ethewulf", "King Ethelwulf of Wessex (839–858 CE)", 19, "839–858 CE"),
        ("mon_eng_alfred", "King Alfred the Great (871–899 CE)", 19, "871–899 CE"),
        ("mon_eng_edward_elder", "King Edward the Elder (899–924 CE)", 19, "899–924 CE"),
        ("mon_eng_athelstan", "King Athelstan (1st King of All England, 924–939)", 19, "924–939 CE"),
        ("mon_eng_edgar", "King Edgar the Peaceful (959–975 CE)", 19, "959–975 CE"),
        ("mon_eng_ethelred2", "King Ethelred II the Unready (978–1016 CE)", 19, "978–1016 CE"),
        ("mon_eng_canute", "King Canute / Cnut the Great (1016–1035 CE)", 20, "1016–1035 CE"),
        ("mon_eng_edward_confessor", "King St. Edward the Confessor (1042–1066)", 20, "1042–1066 CE"),
        ("mon_eng_harold2", "King Harold II Godwinson (1066)", 20, "1066 CE"),
        ("mon_eng_william1", "King William I the Conqueror (1066–1087)", 20, "1066–1087 CE"),
        ("mon_eng_william2", "King William II Rufus (1087–1100)", 20, "1087–1100 CE"),
        ("mon_eng_henry1", "King Henry I Beauclerc (1100–1135)", 20, "1100–1135 CE"),
        ("mon_eng_stephen", "King Stephen of Blois (1135–1154)", 20, "1135–1154 CE"),
    ], "europe_norse", ["William Howell 1685", "Strutt 1779"])

    add_monarchs(nodes, edges, "eng_plantagenet_kings", [
        ("mon_eng_henry2", "King Henry II Plantagenet (1154–1189)", 20, "1154–1189 CE"),
        ("mon_eng_richard1", "King Richard I the Lionheart (1189–1199)", 20, "1189–1199 CE"),
        ("mon_eng_john", "King John of England (Magna Carta, 1199–1216)", 20, "1199–1216 CE"),
        ("mon_eng_henry3", "King Henry III (1216–1272)", 20, "1216–1272 CE"),
        ("mon_eng_edward1", "King Edward I Longshanks (1272–1307)", 20, "1272–1307 CE"),
        ("mon_eng_edward2", "King Edward II (1307–1327)", 20, "1307–1327 CE"),
        ("mon_eng_edward3", "King Edward III (1327–1377)", 20, "1327–1377 CE"),
        ("mon_eng_richard2", "King Richard II (1377–1399)", 20, "1377–1399 CE"),
        ("mon_eng_henry4", "King Henry IV of Lancaster (1399–1413)", 20, "1399–1413 CE"),
        ("mon_eng_henry5", "King Henry V (Agincourt, 1413–1422)", 20, "1413–1422 CE"),
        ("mon_eng_henry6", "King Henry VI (1422–1461)", 20, "1422–1461 CE"),
        ("mon_eng_edward4", "King Edward IV of York (1461–1483)", 20, "1461–1483 CE"),
        ("mon_eng_richard3", "King Richard III (1483–1485)", 20, "1483–1485 CE"),
    ], "europe_norse", ["William Howell 1685"])

    add_monarchs(nodes, edges, "eng_tudor_monarchs", [
        ("mon_eng_henry7", "King Henry VII Tudor (1485–1509)", 21, "1485–1509 CE"),
        ("mon_eng_henry8", "King Henry VIII (1509–1547)", 21, "1509–1547 CE"),
        ("mon_eng_edward6", "King Edward VI (1547–1553)", 21, "1547–1553 CE"),
        ("mon_eng_mary1", "Queen Mary I of England (1553–1558)", 21, "1553–1558 CE"),
        ("mon_eng_elizabeth1", "Queen Elizabeth I (1558–1603)", 21, "1558–1603 CE"),
    ], "europe_norse", ["William Howell 1685"])

    add_monarchs(nodes, edges, "eng_stuart_great_britain", [
        ("mon_eng_james1", "King James VI & I (1603–1625, KJV Bible)", 21, "1603–1625 CE"),
        ("mon_eng_charles1", "King Charles I (1625–1649)", 21, "1625–1649 CE"),
        ("mon_eng_charles2", "King Charles II (Restoration, 1660–1685)", 21, "1660–1685 CE"),
        ("mon_eng_james2", "King James II & VII (1685–1688)", 21, "1685–1688 CE"),
        ("mon_eng_william_mary", "King William III & Queen Mary II (1689–1702)", 21, "1689–1702 CE"),
        ("mon_eng_queen_anne", "Queen Anne (Act of Union, 1702–1714)", 21, "1702–1714 CE"),
        ("mon_eng_george1", "King George I of Hanover (1714–1727)", 21, "1714–1727 CE"),
        ("mon_eng_george2", "King George II (1727–1760)", 21, "1727–1760 CE"),
        ("mon_eng_george3", "King George III (1760–1820)", 21, "1760–1820 CE"),
        ("mon_eng_victoria", "Queen Victoria (1837–1901)", 21, "1837–1901 CE"),
    ], "europe_norse", ["William Howell 1685", "Anderson 1732"])

    # 3. KINGS OF FRANCE (~34 individuals)
    add_monarchs(nodes, edges, "fra_mezeray_pharamond_clovis", [
        ("mon_fra_clovis1", "King Clovis I of the Franks (481–511 CE)", 19, "481–511 CE"),
        ("mon_fra_chlothar1", "King Chlothar I (511–561 CE)", 19, "511–561 CE"),
        ("mon_fra_dagobert1", "King Dagobert I (629–639 CE)", 19, "629–639 CE"),
    ], "europe_norse", ["Mézeray History of France 1683"])

    add_monarchs(nodes, edges, "eur_merovingian_carolingian", [
        ("mon_fra_charles_martel", "Charles Martel (Tours, 732 CE)", 19, "714–741 CE"),
        ("mon_fra_pepin_short", "King Pepin the Short (751–768 CE)", 19, "751–768 CE"),
        ("mon_fra_charlemagne", "Emperor Charlemagne (768–814 CE)", 19, "768–814 CE"),
        ("mon_fra_louis_pious", "Emperor Louis the Pious (814–840 CE)", 19, "814–840 CE"),
        ("mon_fra_charles_bald", "King & Emperor Charles the Bald (843–877 CE)", 19, "843–877 CE"),
    ], "europe_norse", ["Mézeray 1683", "Modern Universal History Vol. 9"])

    add_monarchs(nodes, edges, "fra_capet_stlouis", [
        ("mon_fra_hugh_capet", "King Hugh Capet (987–996 CE)", 20, "987–996 CE"),
        ("mon_fra_robert2", "King Robert II the Pious (996–1031 CE)", 20, "996–1031 CE"),
        ("mon_fra_henry1", "King Henry I of France (+ Anne of Kiev, 1031–1060)", 20, "1031–1060 CE"),
        ("mon_fra_philip1", "King Philip I of France (1060–1108)", 20, "1060–1108 CE"),
        ("mon_fra_louis6", "King Louis VI the Fat (1108–1137)", 20, "1108–1137 CE"),
        ("mon_fra_louis7", "King Louis VII of France (1137–1180)", 20, "1137–1180 CE"),
        ("mon_fra_philip2", "King Philip II Augustus (1180–1223)", 20, "1180–1223 CE"),
        ("mon_fra_louis8", "King Louis VIII the Lion (1223–1226)", 20, "1223–1226 CE"),
        ("mon_fra_louis9", "King St. Louis IX (1226–1270)", 20, "1226–1270 CE"),
        ("mon_fra_philip4", "King Philip IV the Fair (1285–1314)", 20, "1285–1314 CE"),
    ], "europe_norse", ["Modern Universal History Vol. 9"])

    add_monarchs(nodes, edges, "fra_valois_bourbon", [
        ("mon_fra_philip6", "King Philip VI of Valois (1328–1350)", 21, "1328–1350 CE"),
        ("mon_fra_charles5", "King Charles V the Wise (1364–1380)", 21, "1364–1380 CE"),
        ("mon_fra_charles6", "King Charles VI (1380–1422)", 21, "1380–1422 CE"),
        ("mon_fra_charles7_joan", "King Charles VII & St. Joan of Arc (1422–1461)", 21, "1422–1461 CE"),
        ("mon_fra_louis11", "King Louis XI (1461–1483)", 21, "1461–1483 CE"),
        ("mon_fra_francis1", "King Francis I of France (1515–1547)", 21, "1515–1547 CE"),
        ("mon_fra_henry2", "King Henry II of France (1547–1559)", 21, "1547–1559 CE"),
        ("mon_fra_charles9", "King Charles IX (1560–1574)", 21, "1560–1574 CE"),
        ("mon_fra_henry3", "King Henry III of France (1574–1589)", 21, "1574–1589 CE"),
        ("mon_fra_henry4", "King Henry IV of Navarre (1st Bourbon, 1589–1610)", 21, "1589–1610 CE"),
        ("mon_fra_louis13", "King Louis XIII (1610–1643)", 21, "1610–1643 CE"),
        ("mon_fra_louis14", "King Louis XIV the Sun King (1643–1715)", 21, "1643–1715 CE"),
        ("mon_fra_louis15", "King Louis XV (1715–1774)", 21, "1715–1774 CE"),
        ("mon_fra_louis16", "King Louis XVI (1774–1792)", 21, "1774–1792 CE"),
        ("mon_fra_napoleon", "Emperor Napoleon I Bonaparte (1804–1815)", 21, "1804–1815 CE", "Emperor of the French"),
    ], "europe_norse", ["Modern Universal History Vol. 9"])

    # 4. SPAIN, PORTUGAL, HRE & RUSSIA (~49 individuals)
    add_monarchs(nodes, edges, "esp_visigoths_reccared_roderick", [
        ("mon_esp_reccared1", "King Reccared I of the Visigoths (586–601 CE)", 19, "586–601 CE"),
        ("mon_esp_roderick", "King Roderick of Toledo (d. 711 CE)", 19, "710–711 CE"),
    ], "europe_norse", ["Mariana General History of Spain 1699"])

    add_monarchs(nodes, edges, "esp_pelayo_castile_aragon", [
        ("mon_esp_pelayo", "King Don Pelayo of Asturias (718–737 CE)", 20, "718–737 CE"),
        ("mon_esp_alfonso3", "King Alfonso III the Great of Asturias (866–910)", 20, "866–910 CE"),
        ("mon_esp_alfonso6", "King Alfonso VI of Castile & Leon (1065–1109)", 20, "1065–1109 CE"),
        ("mon_esp_el_cid", "Rodrigo Díaz de Vivar ('El Cid Campeador', d. 1099)", 20, "c. 1043–1099 CE", "Castilian Noble"),
        ("mon_esp_alfonso8", "King Alfonso VIII of Castile (Las Navas de Tolosa)", 20, "1158–1214 CE"),
        ("mon_esp_ferdinand3", "King St. Ferdinand III of Castile & Leon (1217–1252)", 20, "1217–1252 CE"),
        ("mon_esp_alfonso10", "King Alfonso X the Wise of Castile (1252–1284)", 20, "1252–1284 CE"),
    ], "europe_norse", ["Mariana 1699"])

    add_monarchs(nodes, edges, "esp_ferdinand_isabella_habsburg", [
        ("mon_esp_isabella_ferdinand", "Queen Isabella I of Castile & King Ferdinand II of Aragon", 21, "1474–1516 CE"),
        ("mon_esp_charles5", "Emperor Charles V / Charles I of Spain (1516–1556)", 21, "1516–1556 CE"),
        ("mon_esp_philip2", "King Philip II of Spain & Portugal (1556–1598)", 21, "1556–1598 CE"),
        ("mon_esp_philip3", "King Philip III of Spain (1598–1621)", 21, "1598–1621 CE"),
        ("mon_esp_philip4", "King Philip IV of Spain (1621–1665)", 21, "1621–1665 CE"),
        ("mon_esp_philip5", "King Philip V of Spain (1st Bourbon of Spain, 1700)", 21, "1700–1746 CE"),
    ], "europe_norse", ["Mariana 1699"])

    add_monarchs(nodes, edges, "por_afonso_henriques", [
        ("mon_por_afonso1", "King Afonso I Henriques (1139–1185)", 20, "1139–1185 CE"),
        ("mon_por_sancho1", "King Sancho I the Populator (1185–1211)", 20, "1185–1211 CE"),
        ("mon_por_dinis", "King Dinis the Farmer-Poet (1279–1325)", 20, "1279–1325 CE"),
    ], "europe_norse", ["Sandford 1662", "History of Portugal 1661"])

    add_monarchs(nodes, edges, "por_aviz_discoveries", [
        ("mon_por_john1", "King John I of Aviz (1385–1433)", 21, "1385–1433 CE"),
        ("mon_por_henry_nav", "Infante Prince Henry the Navigator (1394–1460)", 21, "1394–1460 CE", "Portuguese Prince"),
        ("mon_por_afonso5", "King Afonso V the African (1438–1481)", 21, "1438–1481 CE"),
        ("mon_por_john2", "King John II the Perfect Prince (1481–1495)", 21, "1481–1495 CE"),
        ("mon_por_manuel1", "King Manuel I the Fortunate (1495–1521)", 21, "1495–1521 CE"),
        ("mon_por_john3", "King John III of Portugal (1521–1557)", 21, "1521–1557 CE"),
        ("mon_por_sebastian", "King Sebastian I of Portugal (1557–1578)", 21, "1557–1578 CE"),
    ], "europe_norse", ["History of Portugal 1661 & 1726", "Portuguese Asia"])

    add_monarchs(nodes, edges, "por_braganza_restoration", [
        ("mon_por_john4", "King John IV the Restorer (1640–1656)", 21, "1640–1656 CE"),
        ("mon_por_peter2", "King Peter II of Portugal (1683–1706)", 21, "1683–1706 CE"),
        ("mon_por_john5", "King John V the Magnanimous (1706–1750)", 21, "1706–1750 CE"),
    ], "europe_norse", ["History of Portugal 1726"])

    add_monarchs(nodes, edges, "eur_merovingian_carolingian", [
        ("mon_hre_otto1", "Emperor Otto I the Great (962–973 CE, HRE)", 19, "936–973 CE"),
        ("mon_hre_henry4", "Emperor Henry IV (1056–1105 CE)", 20, "1056–1105 CE"),
        ("mon_hre_barbarossa", "Emperor Frederick I Barbarossa (1155–1190 CE)", 20, "1152–1190 CE"),
        ("mon_hre_frederick2", "Emperor Frederick II Hohenstaufen (1220–1250 CE)", 20, "1212–1250 CE"),
        ("mon_hre_rudolf1", "King Rudolf I of Habsburg (1273–1291 CE)", 20, "1273–1291 CE"),
        ("mon_hre_maximilian1", "Emperor Maximilian I of Habsburg (1493–1519)", 21, "1493–1519 CE"),
        ("mon_hre_leopold1", "Emperor Leopold I of Habsburg (1658–1705)", 21, "1658–1705 CE"),
        ("mon_hre_maria_theresa", "Empress Maria Theresa of Austria (1740–1780)", 21, "1740–1780 CE"),
        ("mon_hre_frederick_great", "King Frederick II the Great of Prussia (1740–1786)", 21, "1740–1786 CE"),
    ], "europe_norse", ["Modern Universal History Vols. 10-11", "Mascou 1737"], edge_type="expansion")

    add_monarchs(nodes, edges, "rus_nevsky_ivan_tsars", [
        ("mon_rus_nevsky", "Grand Prince St. Alexander Nevsky (1221–1263 CE)", 20, "1221–1263 CE"),
        ("mon_rus_kalita", "Grand Prince Ivan I Kalita of Moscow (1325–1340)", 20, "1325–1340 CE"),
        ("mon_rus_donskoy", "Grand Prince Dmitry Donskoy (Kulikovo, 1380 CE)", 20, "1359–1389 CE"),
        ("mon_rus_ivan3", "Grand Prince Ivan III the Great (1462–1505)", 20, "1462–1505 CE"),
        ("mon_rus_vasili3", "Grand Prince Vasili III of Moscow (1505–1533)", 21, "1505–1533 CE"),
        ("mon_rus_ivan4", "Tsar Ivan IV the Terrible (1st Tsar of All Russia, 1547)", 21, "1533–1584 CE"),
        ("mon_rus_boris_godunov", "Tsar Boris Godunov (1598–1605)", 21, "1598–1605 CE"),
    ], "europe_norse", ["Modern Universal History Vol. 13"])

    add_monarchs(nodes, edges, "rus_romanov_peter_great", [
        ("mon_rus_michael1", "Tsar Michael I Romanov (1613–1645)", 21, "1613–1645 CE"),
        ("mon_rus_alexis1", "Tsar Alexis I Mikhailovich (1645–1676)", 21, "1645–1676 CE"),
        ("mon_rus_peter1", "Emperor Peter I the Great (1682–1725)", 21, "1682–1725 CE"),
        ("mon_rus_elizabeth", "Empress Elizabeth Petrovna of Russia (1741–1762)", 21, "1741–1762 CE"),
        ("mon_rus_catherine2", "Empress Catherine II the Great (1762–1796)", 21, "1762–1796 CE"),
    ], "europe_norse", ["Modern Universal History Vol. 13"])

    # 5. OTTOMANS, CALIPHATES, PERSIA, MUGHALS, INDIA, ETHIOPIA & SONGHAI (~58 individuals)
    add_monarchs(nodes, edges, "ott_osman_ertughrul", [
        ("mon_ott_osman1", "Sultan Osman I (Founder of Ottoman Empire, 1299–1324)", 20, "1299–1324 CE"),
        ("mon_ott_orhan", "Sultan Orhan Ghazi (1324–1362)", 20, "1324–1362 CE"),
        ("mon_ott_murad1", "Sultan Murad I (1362–1389)", 20, "1362–1389 CE"),
        ("mon_ott_bayezid1", "Sultan Bayezid I Yildirim (1389–1402)", 20, "1389–1402 CE"),
        ("mon_ott_mehmed1", "Sultan Mehmed I Celebi (1413–1421)", 20, "1413–1421 CE"),
        ("mon_ott_murad2", "Sultan Murad II (1421–1451)", 20, "1421–1451 CE"),
    ], "steppe", ["Knolles & Rycaut The Turkish History Vols. 1-3"])

    add_monarchs(nodes, edges, "ott_mehmed2_suleiman", [
        ("mon_ott_mehmed2", "Sultan Mehmed II Fatih (1451–1481)", 21, "1451–1481 CE"),
        ("mon_ott_bayezid2", "Sultan Bayezid II (1481–1512)", 21, "1481–1512 CE"),
        ("mon_ott_selim1", "Sultan Selim I Yavuz (1512–1520)", 21, "1512–1520 CE"),
        ("mon_ott_suleiman1", "Sultan Suleiman I the Magnificent (1520–1566)", 21, "1520–1566 CE"),
        ("mon_ott_selim2", "Sultan Selim II (1566–1574)", 21, "1566–1574 CE"),
        ("mon_ott_murad3", "Sultan Murad III (1574–1595)", 21, "1574–1595 CE"),
        ("mon_ott_ahmed1", "Sultan Ahmed I (Blue Mosque, 1603–1617)", 21, "1603–1617 CE"),
        ("mon_ott_murad4", "Sultan Murad IV (1623–1640)", 21, "1623–1640 CE"),
        ("mon_ott_mehmed4", "Sultan Mehmed IV (1648–1687)", 21, "1648–1687 CE"),
        ("mon_ott_mahmud2", "Sultan Mahmud II (1808–1839)", 21, "1808–1839 CE"),
    ], "steppe", ["Knolles & Rycaut Vols. 1-3"])

    add_monarchs(nodes, edges, "isl_umayyad_abbasid_fatimid", [
        ("mon_isl_abubakr", "Caliph Abu Bakr al-Siddiq (1st Rashidun Caliph, 632–634)", 20, "632–634 CE"),
        ("mon_isl_umar", "Caliph Umar ibn al-Khattab (634–644 CE)", 20, "634–644 CE"),
        ("mon_isl_uthman", "Caliph Uthman ibn Affan (644–656 CE)", 20, "644–656 CE"),
        ("mon_isl_ali", "Caliph Ali ibn Abi Talib (656–661 CE)", 20, "656–661 CE"),
        ("mon_isl_muawiya1", "Caliph Mu'awiya I (Umayyad Founder, 661–680)", 20, "661–680 CE"),
        ("mon_isl_abd_al_malik", "Caliph Abd al-Malik (Dome of the Rock, 685–705)", 20, "685–705 CE"),
        ("mon_isl_al_mansur", "Caliph Al-Mansur (Founder of Baghdad, 754–775)", 20, "754–775 CE"),
        ("mon_isl_harun_rashid", "Caliph Harun al-Rashid (House of Wisdom, 786–809)", 20, "786–809 CE"),
        ("mon_isl_al_mamun", "Caliph Al-Ma'mun (813–833 CE)", 20, "813–833 CE"),
        ("mon_isl_abdarrahman1", "Emir Abd al-Rahman I of Cordoba (756–788)", 20, "756–788 CE"),
        ("mon_isl_abdarrahman3", "Caliph Abd al-Rahman III of Cordoba (912–961)", 20, "912–961 CE"),
        ("mon_isl_saladin", "Sultan Saladin (Salah ad-Din al-Ayyubi, 1174–1193)", 20, "1174–1193 CE"),
        ("mon_isl_baybars", "Mamluk Sultan Baybars I (1260–1277)", 20, "1260–1277 CE"),
        ("mon_isl_mahmud_ghazni", "Sultan Mahmud of Ghazni (998–1030)", 20, "998–1030 CE"),
    ], "arabian", ["Al-Tabari", "Modern Universal History Vols. 1-2", "Ibn 'Abd al-Hakam"], edge_type="expansion")

    add_monarchs(nodes, edges, "bir_sasanians_complete", [
        ("mon_ir_shah_ismail1", "Shah Ismail I (Founder of Safavid Persia, 1501–1524)", 21, "1501–1524 CE"),
        ("mon_ir_tahmasp1", "Shah Tahmasp I (1524–1576)", 21, "1524–1576 CE"),
        ("mon_ir_abbas1", "Shah Abbas I the Great (Isfahan, 1588–1629)", 21, "1588–1629 CE"),
        ("mon_ir_nader_shah", "Nader Shah Afshar (1736–1747)", 21, "1736–1747 CE"),
        ("mon_ir_karim_khan", "Karim Khan Zand (1751–1779)", 21, "1751–1779 CE"),
        ("mon_ir_agha_mohammad", "Agha Mohammad Khan Qajar (Founder of Qajar Iran, 1789)", 21, "1789–1797 CE"),
    ], "iranian", ["Persian Chronicles", "Modern Universal History Vol. 4"], edge_type="expansion")

    add_monarchs(nodes, edges, "mug_akbar_aurangzeb", [
        ("mon_mug_babur_ind", "Emperor Babur (1526–1530, Panipat)", 21, "1526–1530 CE"),
        ("mon_mug_humayun_ind", "Emperor Humayun (1530–1556)", 21, "1530–1556 CE"),
        ("mon_mug_akbar_ind", "Emperor Akbar the Great (1556–1605)", 21, "1556–1605 CE"),
        ("mon_mug_jahangir_ind", "Emperor Jahangir (1605–1627)", 21, "1605–1627 CE"),
        ("mon_mug_shahjahan_ind", "Emperor Shah Jahan (Taj Mahal, 1628–1658)", 21, "1628–1658 CE"),
        ("mon_mug_aurangzeb_ind", "Emperor Aurangzeb Alamgir (1658–1707)", 21, "1658–1707 CE"),
    ], "vedic", ["Modern Universal History Vol. 3", "Abulghazi"])

    add_monarchs(nodes, edges, "ind_gupta_golden_age", [
        ("mon_ind_harsha", "Emperor Harshavardhana of Kannauj (606–647 CE)", 19, "606–647 CE"),
        ("mon_ind_rajaraja1", "Rajaraja Chola I (Thanjavur Brihadisvara, 985–1014)", 20, "985–1014 CE"),
        ("mon_ind_rajendra1", "Rajendra Chola I (1014–1044)", 20, "1014–1044 CE"),
        ("mon_ind_krishnadevaraya", "Emperor Krishnadevaraya of Vijayanagara (1509–1529)", 21, "1509–1529 CE"),
        ("mon_ind_shivaji", "Chhatrapati Shivaji Bhonsle (Founder of Maratha Empire, 1674)", 21, "1630–1680 CE"),
        ("mon_ind_ranjit_singh", "Maharaja Ranjit Singh (Founder of Sikh Empire, 1799–1839)", 21, "1780–1839 CE"),
    ], "vedic", ["Indian Royal Chronicles", "Modern Universal History Vol. 3"], edge_type="expansion")

    add_monarchs(nodes, edges, "eth_ludolf_gondar_kings", [
        ("mon_eth_ezana", "Emperor Ezana of Aksum (Christianized Aksum, 4th c.)", 19, "320s–360 CE"),
        ("mon_eth_kaleb", "Emperor Kaleb / Elesbaan of Aksum (c. 520 CE)", 19, "c. 520 CE"),
        ("mon_eth_lalibela", "King Gebre Mesqel Lalibela (Rock Churches, 12th c.)", 20, "c. 1181–1221 CE"),
        ("mon_eth_yekuno_amlak", "Emperor Yekuno Amlak (Solomonic Restoration, 1270)", 20, "1270–1285 CE"),
        ("mon_eth_zara_yaqob", "Emperor Zara Yaqob (1434–1468)", 20, "1434–1468 CE"),
        ("mon_eth_lebna_dengel", "Emperor Lebna Dengel (1508–1540)", 21, "1508–1540 CE"),
        ("mon_eth_galawdewos", "Emperor Galawdewos (1540–1559)", 21, "1540–1559 CE"),
        ("mon_eth_susenyos", "Emperor Susenyos I (1607–1632)", 21, "1607–1632 CE"),
        ("mon_eth_fasilides", "Emperor Fasilides (Founder of Gondar, 1632–1667)", 21, "1632–1667 CE"),
        ("mon_eth_tewodros2", "Emperor Tewodros II (1855–1868)", 21, "1855–1868 CE"),
        ("mon_eth_menelik2", "Emperor Menelik II (Battle of Adwa, 1896)", 21, "1889–1913 CE"),
    ], "african", ["Hiob Ludolf 1684", "Kebra Nagast"], edge_type="expansion")

    add_monarchs(nodes, edges, "sng_sonni_askia_timbuktu", [
        ("mon_afr_mansa_musa", "Mansa Musa I of Mali (Pilgrimage 1324 CE)", 20, "1312–1337 CE"),
        ("mon_afr_sonni_ali", "Emperor Sonni Ali of Songhai (1464–1492)", 20, "1464–1492 CE"),
        ("mon_afr_askia_mohammed", "Emperor Askia Mohammed I the Great (1493–1528)", 20, "1493–1528 CE"),
    ], "african", ["Tarikh es-Soudan"])

    return {
        "module": "37_individual_monarchs_world_chronicles",
        "title": "Individualized Roman, European, Ottoman, Caliphate, Persian, Mughal, Indian, Ethiopian & West African Sovereigns",
        "nodes": nodes,
        "edges": edges,
    }
