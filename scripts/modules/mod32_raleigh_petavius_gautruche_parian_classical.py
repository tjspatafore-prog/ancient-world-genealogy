"""
Module 32: Sir Walter Raleigh (1736 History of the World), Petavius (1659),
Gautruche (The Poetical History), The Parian Chronicle (1788), Lucian (De Dea Syria),
Classical Greco-Roman Historians (Livy, Echard, Tacitus, Xenophon, Curtius Rufus,
Ammianus, Mexia) & William Vincent (Periplus of the Erythrean Sea, 1800).

Sources integrated:
- Sir Walter Raleigh, The History of the World (1736 Folio Vols. 1-2, Book I Ch. VII-VIII & Dispersion Map)
- Alexander Ross, The History of the World, Second Part
- Dionysius Petavius, The History of the World or an Account of Time (1659)
- Pierre Gautruche, The Poetical History (pp. 8-15)
- The Parian Chronicle or the Chronicle of the Arundelian Marbles (1788 pp. 1-5)
- Lucian of Samosata, De Dea Syria (Syrian Flood of Deucalion / Noah)
- Livy (Vols. 1-6), Laurence Echard (Roman History, 5 Vols.), Tacitus (Vols. 1-4),
  Ammianus Marcellinus, Florus, Aurelius Victor, Pedro Mexia (Imperial History),
  Domitian to Constantine, Bridge of Livy to Tacitus
- Xenophon (Anabasis), Quintus Curtius Rufus, Thucydides, Plutarch, Cornelius Nepos,
  Lives of Ancient Philosophers
- William Vincent, The Periplus of the Erythrean Sea (1800)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("ral_methodius_suphene",
          "Raleigh & Methodius's 3 Post-Flood Leaders: Nimrod (Ham), Joktan (Shem) & Suphene (Japheth)",
          "biblical", 6,
          "Post-Flood Dispersion (Raleigh 1736 Vol. 1 Book I Ch. VII p. 69; Petavius 1659)",
          "Tripartite Dispersion Commanders of Ham, Shem & Japheth",
          ["Sir Walter Raleigh History of the World (1736 Vol. 1 Book I Ch. VII p. 69)", "Petavius History of the World (1659)"],
          "Sir Walter Raleigh (citing Methodius of Tyre) records the three post-Flood commanders who led the peoples after Babel: Nimrod over Ham's line, Joktan over Shem's line, and Suphene over Japheth's line — framed within Petavius's universal chronology from Creation.",
          ["Methodius of Tyre", "Suphene", "Petavius 1659"],
          major=True),

        N("ral_east_indies_shem",
          "Raleigh's Shemite Plantation of the East Indies: Joktan, Havilah & Ophir",
          "vedic", 9,
          "Eastward Dispersion (Raleigh 1736 Vol. 1 Book I Ch. VIII & Map)",
          "Biblical Shemite Pioneers of India & the East Indies",
          ["Sir Walter Raleigh History of the World (1736 Vol. 1 Book I Ch. VIII & Engraved Noahic Map)"],
          "Raleigh argues at length in Book I Ch. VIII (and marks on his engraved dispersion map) that Joktan's descendants Havilah and Ophir planted the regions stretching across Persia and India / the East Indies.",
          ["Joktan in the East", "Ophir / East Indies"],
          major=True),

        N("ral_arabia_felix_cush",
          "Raleigh's Cushite Arabia the Happy: Seba, Sabtah & Raamah (Sabe Regia & Aden)",
          "arabian", 8,
          "Post-Flood Arabia (Raleigh 1736 Vol. 1 Book I Ch. VIII & Map)",
          "Cushite Settlements of Arabia Felix",
          ["Sir Walter Raleigh History of the World (1736 Vol. 1 Book I Ch. VIII & Map)"],
          "Raleigh maps Cush's sons Seba, Sabtah, and Raamah (Rhegma) directly along the coasts and cities of Arabia the Happy (Arabia Felix), including Sabe Regia and Aden.",
          ["Sabe Regia", "Aden / Rhegma"],
          major=False),

        N("ral_cato_scythia_saga",
          "Cato's Scythia Saga (Raleigh p. 69): Post-Flood Scythians → Galli (Gauls) & Italian Umbri",
          "europe_norse", 7,
          "Post-Flood Westward Migration (Raleigh 1736 Vol. 1 p. 69)",
          "Classical Witness to mankind's Post-Flood Restoration via Scythia & Italy",
          ["Sir Walter Raleigh History of the World (1736 Vol. 1 Book I Ch. VII p. 69, citing Cato)"],
          "Raleigh quotes Cato (Fragments) that after mankind was restored following the Deluge, populations spread from Scythia Saga into the Galli (Gauls) and ancient Umbri of Italy.",
          ["Cato Origines", "Scythia Saga", "Umbri & Galli"],
          major=False),

        N("gau_poetical_noah_ages",
          "Gautruche's Poetical History Cognates: Golden Age (Saturn/Janus = Noah), Silver Age (Jupiter = Ham), Brazen Age (Nimrod), Vulcan (= Tubal-Cain) & Apollo (= Jubal)",
          "greek", 5,
          "Classical Mythic-Biblical Cognates (Gautruche pp. 8-15)",
          "Systematic Identification of Greco-Roman Mythic Figures with Genesis Patriarchs",
          ["Pierre Gautruche The Poetical History (pp. 8-15)"],
          "Gautruche translates Greco-Roman mythology back into Biblical history: the Golden Age under Saturn/Janus corresponds to Noah (threefold division of the world), the Silver Age to Jupiter (Ham/Cham), the Brazen Age to Nimrod, Vulcan to metal-worker Tubal-Cain, and Apollo to musician Jubal.",
          ["Golden Age = Noah", "Jupiter = Ham", "Vulcan = Tubal-Cain", "Apollo = Jubal"],
          major=True),

        N("par_cecrops_deucalion_flood",
          "The Parian Chronicle (264 BCE Marble) & Lucian: Epoch 1 Cecrops (1582 BCE) & Epoch 2 Deucalion's Flood (1529 BCE)",
          "greek", 5,
          "264 BCE Greek Inscription (The Parian Chronicle 1788 pp. 1-5; Lucian De Dea Syria)",
          "Epigraphic Greek Chronicle & Syrian Flood Witness",
          ["The Parian Chronicle or Chronicle of the Arundelian Marbles (1788 pp. 1-5)", "Lucian De Dea Syria"],
          "Inscribed in marble on Paros in 264 BCE, the Parian Chronicle anchors Greek chronology at Epoch 1 (Cecrops, first king of Athens, 1582 BCE) and Epoch 2 (Deucalion escaping the Great Flood to Athens from Parnassus, 1529 BCE), paired with Lucian's De Dea Syria preserving the Near Eastern Deluge tradition under Deucalion's name.",
          ["Arundel Marbles", "Epoch 1 Cecrops", "Lucian Syrian Flood"],
          major=True),

        N("xen_artaxerxes2_cyrus_younger",
          "Classical Persian-Greek Bridge (Xenophon, Curtius Rufus & Plutarch): Artaxerxes II Mnemon, Cyrus the Younger (401 BCE) & Darius III",
          "iranian", 18,
          "404–330 BCE (Xenophon Anabasis; Curtius Rufus; Plutarch)",
          "Late Achaemenid Emperors Leading to Alexander the Great",
          ["Xenophon Anabasis", "Quintus Curtius Rufus History of Alexander", "Plutarch Lives (Artaxerxes & Alexander)"],
          "Documented across Xenophon's Anabasis (Cyrus the Younger vs. his brother Artaxerxes II at Cunaxa, 401 BCE), Plutarch, and Curtius Rufus down to Darius III and Alexander the Great.",
          ["Artaxerxes II Mnemon", "Cyrus the Younger", "Darius III"],
          major=False),

        N("rom_echard_imperial_bridge",
          "Classical Roman Imperial Spine (Livy, Tacitus, Echard 5 Vols., Ammianus & Mexía): Vespasian & Titus (70 CE) → Trajan → Marcus Aurelius → Diocletian → Romulus Augustulus (476 CE)",
          "greek", 19,
          "69–476 CE (Echard Vols. 2-4; Tacitus; Ammianus Marcellinus; Mexía)",
          "Flavians, Five Good Emperors, Tetrarchy & Western Roman Finale",
          ["Laurence Echard Roman History Vols. 1-5", "Livy Vols. 1-6", "Tacitus Vols. 1-4", "Ammianus Marcellinus", "Pedro Mexía Imperial History"],
          "Synthesizes the Roman imperial succession across Echard's 5-volume Roman History, Tacitus, Ammianus Marcellinus, Florus, Aurelius Victor, and Mexía from Vespasian & Titus through Trajan, Marcus Aurelius, Diocletian, and Romulus Augustulus (476 CE) to Charlemagne (Echard Vol. 5).",
          ["Vespasian & Titus", "Trajan & Marcus Aurelius", "Diocletian", "Romulus Augustulus"],
          major=True),

        N("vin_periplus_ophir_zoscales",
          "Periplus of the Erythraean Sea (Vincent 1800): King Zoscales of Aksum, Saba/Sheba, Ophir & Red Sea–India Corridor",
          "african", 19,
          "1st c. CE (William Vincent Periplus of the Erythrean Sea, 1800)",
          "Classical Greco-Egyptian Maritime Bridge Linking Aksum, Sheba, Arabia & India",
          ["William Vincent The Periplus of the Erythrean Sea (1800)"],
          "Vincent's scholarly commentary identifies King Zoscales of Aksum (Adulis, 1st c. CE), maps classical Saba/Mariaba to Biblical Sheba, examines the Ophir trade corridor, and documents direct monsoon voyages linking Ethiopia and Arabia to western India.",
          ["Zoscales of Aksum", "Adulis & Saba", "Monsoon Route to India"],
          major=True),
    ]

    edges += [
        E("bib_noah", "ral_methodius_suphene", "syncretic", "Raleigh 1736 Vol. 1 p. 69 (Methodius) & Petavius 1659: Post-Flood dispersion under three commanders"),
        E("ral_methodius_suphene", "bib_nimrod", "syncretic", "Methodius/Raleigh: Nimrod led the Hamite division"),
        E("ral_methodius_suphene", "bib_joktan", "syncretic", "Methodius/Raleigh: Joktan led the Shemite division"),
        E("bib_japheth", "ral_methodius_suphene", "syncretic", "Methodius/Raleigh p. 69: Suphene appointed commander over Japheth's posterity"),
        E("bib_joktan", "ral_east_indies_shem", "syncretic", "Raleigh 1736 Book I Ch. VIII: Joktan's posterity planted regions extending into the East Indies"),
        E("bib_havilah_joktan", "ral_east_indies_shem", "syncretic", "Raleigh 1736 Book I Ch. VIII & Map: Havilah b. Joktan in East-Indian dispersion"),
        E("bib_ophir", "ral_east_indies_shem", "syncretic", "Raleigh 1736 Book I Ch. VIII & Map: Ophir planted eastern Indian territories"),
        E("ral_east_indies_shem", "ind_hind_sind_noah", "cognate", "Raleigh's Shemite East Indies converges with Tabari's Qahtan/Joktan -> Hind & Sind tradition"),
        E("bib_cush", "ral_arabia_felix_cush", "syncretic", "Raleigh 1736 Book I Ch. VIII & Map: Cushites settled Arabia Felix"),
        E("bib_seba", "ral_arabia_felix_cush", "syncretic", "Raleigh Map: Seba mapped to Sabe Regia"),
        E("bib_sabtah", "ral_arabia_felix_cush", "syncretic", "Raleigh Book I Ch. VIII: Sabtah along the Sabota / southern Arabian littoral"),
        E("bib_raamah", "ral_arabia_felix_cush", "syncretic", "Raleigh Map: Raamah (Rhegma) & Aden on the Persian Gulf / Arabian coast"),
        E("bib_noah", "ral_cato_scythia_saga", "syncretic", "Raleigh 1736 p. 69 (Cato): Post-Flood restoration beginning in Scythia Saga"),
        E("ral_cato_scythia_saga", "eur_gomer_samothes_gaul", "syncretic", "Cato via Raleigh p. 69: Old Galli sprung from the post-Flood Scythians"),
        E("ral_cato_scythia_saga", "eur_noah_janus_italy", "syncretic", "Cato via Raleigh p. 69: Janus & Italian Umbri traced from the post-Flood Scythians"),
        E("bib_elam", "ir_cyrus", "syncretic", "Raleigh 1736 Book I Ch. VIII & Map: Elam b. Shem planted Elymais & Persia"),
        E("bib_meshech", "arm_hayk_pat", "syncretic", "Raleigh 1736 Book I Ch. VIII & Map: Meshech b. Japheth planted Armenia / Ciracene regions"),
        E("bib_noah", "gau_poetical_noah_ages", "syncretic", "Gautruche Poetical History pp. 8-15: Saturn/Janus (Golden Age) identified with Noah"),
        E("bib_ham", "gau_poetical_noah_ages", "syncretic", "Gautruche Poetical History pp. 8-15: Jupiter (Silver Age) identified with Ham/Cham"),
        E("bib_nimrod", "gau_poetical_noah_ages", "syncretic", "Gautruche Poetical History: Brazen Age tyranny traced to Nimrod"),
        E("bib_tubalcain", "gau_poetical_noah_ages", "syncretic", "Gautruche Poetical History: Greco-Roman smith Vulcan identified with Tubal-Cain"),
        E("bib_jubal", "gau_poetical_noah_ages", "syncretic", "Gautruche Poetical History: Inventor of music Apollo compared with Jubal"),
        E("gau_poetical_noah_ages", "eur_noah_janus_italy", "cognate", "Same Janus = Noah tradition in Gautruche & Anderson"),
        E("gau_poetical_noah_ages", "sanch_chrysor_barhebraeus", "cognate", "Parallel Tubal-Cain = Vulcan/Chrysor identification across Gautruche & Sanchuniathon"),
        E("bib_noah", "par_cecrops_deucalion_flood", "syncretic", "Lucian De Dea Syria: Syrian Great Flood temple tradition of Deucalion / Noah"),
        E("grk_deucalion", "par_cecrops_deucalion_flood", "cognate", "Parian Chronicle (264 BCE) Epoch 2 dates Deucalion's escape from the Flood to 1529 BCE"),
        E("par_cecrops_deucalion_flood", "grk_athens_cecrops_theseus", "cognate", "Parian Chronicle Epoch 1 anchors Cecrops as 1st King of Athens (1582 BCE)"),
        E("par_cecrops_deucalion_flood", "grk_hellen", "cognate", "Parian Chronicle records Deucalion's son Hellen giving his name to the Hellenes"),
        E("ir_artaxerxes1", "xen_artaxerxes2_cyrus_younger", "direct", "Achaemenid succession: Artaxerxes I -> Darius II -> Artaxerxes II Mnemon & Cyrus the Younger -> Darius III"),
        E("xen_artaxerxes2_cyrus_younger", "grk_alexander", "cognate", "Curtius Rufus & Plutarch: Alexander the Great defeats Darius III of Persia"),
        E("rom_julio_claudians", "rom_echard_imperial_bridge", "expansion", "Tacitus & Echard Vols. 2-4: Julio-Claudians -> Flavians -> Five Good Emperors -> Diocletian -> Romulus Augustulus"),
        E("rom_echard_imperial_bridge", "rom_constantine_byzantium", "expansion", "Echard Vols. 4-5 & Ammianus: Diocletian -> Constantine the Great -> Byzantine Emperors"),
        E("rom_echard_imperial_bridge", "eur_merovingian_carolingian", "cognate", "Echard Vol. 5: Western imperial continuity crowned in Charlemagne (800 CE)"),
        E("eth_ezana", "vin_periplus_ophir_zoscales", "expansion", "Vincent Periplus (1800): Pre-Ezana Aksumite monarch King Zoscales of Adulis & Aksum (1st c. CE)"),
        E("eth_makeda", "vin_periplus_ophir_zoscales", "cognate", "Vincent Periplus discusses Queen of Sheba (Saba) & Ethiopian Aksumite antiquity"),
        E("bib_ophir", "vin_periplus_ophir_zoscales", "syncretic", "Vincent Periplus Dissertation on Ophir along the Erythraean Sea / Indian Ocean trade"),
        E("bib_sheba_joktan", "vin_periplus_ophir_zoscales", "cognate", "Vincent Periplus identifies classical Saba/Mariaba with Arabian Sheba"),
        E("vin_periplus_ophir_zoscales", "ral_east_indies_shem", "cognate", "Erythraean Sea monsoon route linking Red Sea, Sheba & Ophir directly to India"),
    ]

    return {
        "module": "32_raleigh_petavius_gautruche_parian_classical",
        "title": "Sir Walter Raleigh, Petavius, Gautruche Poetical Cognates, Parian Chronicle, Classical Rome & Periplus",
        "nodes": nodes,
        "edges": edges,
    }
