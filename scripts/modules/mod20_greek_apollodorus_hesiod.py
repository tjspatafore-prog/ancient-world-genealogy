"""
Module 20: Complete Greek Mythological & Heroic Genealogical System
from Pseudo-Apollodorus's Bibliotheca (Loeb/Frazer) & Hesiod's Theogony / Catalogue of Women.

Covers all 8 great heroic houses:
1. Hesiodic Cosmogony, Titans, Pontus/Nereids, 12 Olympians & 9 Muses
2. Deucalionids, Aeolids (7 sons & 5 daughters), Aetolians (Meleager/Diomedes) & Argonauts (Jason/Medea)
3. Inachids, Belus/Danaids (Hypermnestra/Lynceus), Perseus/Perseids & Complete Heracles / Heraclidae
4. Agenorids: Europa -> Minos (Crete/Minotaur/Idomeneus) & Cadmus -> Thebes (Dionysus, Oedipus, Seven & Epigoni)
5. Pelasgids (Arcadia: Lycaon, Callisto, Arcas, Telephus, Atalanta)
6. Atlantids (7 Pleiades -> Hermes, Sparta [Lacedaemon, Tyndareus, Leda, Helen, Castor/Pollux], Troy [Dardanus -> Priam & Aeneas])
7. Asopids (Aeacus -> Peleus/Achilles/Neoptolemus & Telamon/Ajax/Teucer)
8. Cecropids/Erechtheids (Kings of Athens: Cecrops, Erichthonius, Pandion, Erechtheus, Aegeus, Theseus) & Pelopids (Tantalus, Pelops, Atreus, Agamemnon, Orestes)
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    # 1. Primordials, Titans, Pontus, Olympians & Muses (Apollodorus I.i-vi; Hesiod Theogony)
    nodes += [
        N("grk_nyx_pontus_nereids", "Hesiodic Primordials: Chaos → Nyx/Erebus & Gaia → Pontus (Phorcys, Ceto, Gorgons, Nereus & 50 Nereids incl. Thetis)", "greek", 1, "Greek Cosmogony (Hesiod Theog. 116-264; Apollodorus I.ii.6)",
          "Sea Deities, Gorgons & Ancestors of Achilles's Mother Thetis", ["Hesiod Theogony 116-264", "Apollodorus Library I.ii.6-7"],
          "Pontus + Gaia -> Phorcys & Ceto (Graiae, Gorgons Stheno/Euryale/Medusa -> Pegasus & Chrysaor -> Geryon & Echidna!) and Nereus + Doris -> 50 Nereids (Amphitrite, Thetis [mother of Achilles!], Calypso, Galatea).",
          ["Nyx & Erebus", "Pontus", "Medusa & Pegasus", "Nereus & 50 Nereids"]),
        N("grk_titans_complete", "Complete 12 Titans: Oceanus/Tethys, Coeus/Phoebe (Leto/Asteria), Hyperion/Theia (Helios/Selene/Eos), Crius (Astraeus/Pallas/Perses → Hecate), Iapetus & Cronus/Rhea", "greek", 2, "Titanomachy Era (Apollodorus I.i.3-I.ii.4; Hesiod Theog.)",
          "Complete Titan Generation & Sun/Moon/Dawn Lineages", ["Apollodorus Library I.i.3-I.ii.4", "Hesiod Theogony 337-452"],
          "Hyperion + Theia -> Helios (father of Circe, Pasiphae & Aeetes of Colchis -> Medea!), Selene, Eos (mother of Memnon & Phaethon). Coeus + Phoebe -> Leto (mother of Apollo & Artemis) & Asteria (mother of Hecate). Pallas + Styx -> Nike, Cratos, Zelus, Bia.",
          ["Helios -> Aeetes -> Medea", "Leto -> Apollo & Artemis", "Hecate", "Nike"]),
        N("grk_muses_orpheus", "Zeus & Mnemosyne → 9 Muses (Calliope → Orpheus & Linus), Horae, Moerae (Fates) & Charites (Graces)", "greek", 3, "Olympian Generation (Apollodorus I.iii.1-4; Hesiod Theog. 901-920)",
          "Divine Patrons of Arts, Fate & Mythic Poets", ["Apollodorus Library I.iii.1-4", "Hesiod Theogony 901-920"],
          "Calliope + Oeagrus (or Apollo) -> Orpheus (Argonaut & singer) & Linus; Zeus + Themis -> 3 Horae (Eirene, Eunomia, Dike) & 3 Fates (Clotho, Lachesis, Atropos); Zeus + Demeter -> Persephone; Zeus + Metis -> Athena.",
          ["9 Muses", "Orpheus", "Persephone", "Three Fates"]),

        # 2. Deucalionids, Aeolids, Aetolians & Argonauts (Apollodorus I.vii-ix)
        N("grk_aetolia_meleager_diomedes", "Aethlius & Calyce → Endymion → Aetolus → Porthaon → Oeneus → Meleager, Deianira & Tydeus → Diomedes", "greek", 9, "Heroic Age (Apollodorus I.vii.5-I.viii.6)",
          "Aetolian Royal House (Calydonian Boar Hunt & Hero Diomedes of Troy)", ["Apollodorus Library I.vii.5-I.viii.6"],
          "Calyce (daughter of Aeolus) + Aethlius (son of Protogonia dau. of Deucalion) -> Endymion -> Aetolus -> Pleuron/Calydon -> Agenor -> Porthaon -> Oeneus (+ Althaea -> Meleager & Deianira [wife of Heracles!]; + Periboea -> Tydeus [Seven Against Thebes] -> Diomedes [Iliad hero!]).",
          ["Endymion", "Meleager", "Deianira", "Tydeus", "Diomedes"]),
        N("grk_neleus_nestor_pelias", "Salmoneus → Tyro (+ Poseidon) → Pelias (Iolcus) & Neleus (Pylos) → Nestor (Trojan War Counselor)", "greek", 9, "Heroic Age (Apollodorus I.ix.8-9)",
          "Neleid Kings of Pylos & Pelias of Iolcus", ["Apollodorus Library I.ix.8-9"],
          "Tyro bore twins Pelias (usurped Iolcus -> Alcestis & Acastus) and Neleus (+ Chloris -> 12 sons, of whom only Nestor survived Heracles's raid, becoming the wise elder king of Pylos at Troy -> Antilochus & Pisistratus!).",
          ["Tyro", "Pelias", "Neleus", "King Nestor of Pylos"]),
        N("grk_jason_argonauts_medea", "Cretheus → Aeson → Jason (Argonauts + Medea of Colchis), Amythaon (Melampus/Adrastus) & Pheres (Admetus)", "greek", 9, "Generation Before Troy (Apollodorus I.ix.11-28)",
          "Cretheid House of Iolcus, Seer Melampus & Leader of the Argonauts", ["Apollodorus Library I.ix.11-28", "Hesiod Theogony 992-1002"],
          "Aeson -> Jason (led the Argonauts to Colchis to win the Golden Fleece from King Aeetes; married Medea -> Medeus/Medus, eponymous ancestor of the Medes in Greek myth!). Amythaon -> Melampus (seer -> Amphiaraus) & Bias -> Talaus -> King Adrastus of Argos.",
          ["Jason & the Argonauts", "Medea", "Melampus", "Adrastus", "Admetus & Alcestis"], major=True),
        N("grk_bellerophon_glaucus", "Sisyphus (+ Merope) → Glaucus → Bellerophon (Slayer of the Chimera) & Phrixus/Helle (Athamas)", "greek", 9, "Heroic Age (Apollodorus I.ix.1-3)",
          "Corinthian & Boeotian Aeolids (Pegasus, Chimera & Golden Fleece)", ["Apollodorus Library I.ix.1-3"],
          "Sisyphus (founder of Corinth) -> Glaucus -> Bellerophon (rode winged Pegasus to slay the Chimera in Lycia -> grandfather of Trojan War allies Glaucus & Sarpedon!). Athamas -> Phrixus & Helle (origin of the Golden Fleece & Hellespont!).",
          ["Bellerophon", "Phrixus & Helle"]),

        # 3. Inachids, Danaids, Perseus & Complete Heraclidae (Apollodorus II.i-viii)
        N("grk_hypermnestra_abas_danae", "Hypermnestra & Lynceus → Abas → Acrisius (→ Danaë → Perseus) & Proetus (Tiryns)", "greek", 9, "Argive Heroic Era (Apollodorus II.i.5-II.iv.4)",
          "Sole Surviving Danaid Line Bridging Egypt (Belus/Aegyptus) to Perseus", ["Apollodorus Library II.i.5-II.iv.4"],
          "Hypermnestra spared her husband Lynceus (son of Aegyptus), becoming ancestor of all later Argive & Mycenaean kings: Abas -> twin kings Acrisius (Argos -> Danae + Zeus -> Perseus!) and Proetus (Tiryns -> Megapenthes).",
          ["Hypermnestra & Lynceus", "Abas", "Acrisius", "Danae"]),
        N("grk_perseids_alcmene", "Perseus & Andromeda → Perses, Alcaeus (→ Amphitryon), Sthenelus (→ Eurystheus) & Electryon (→ Alcmene → Heracles)", "greek", 10, "Mycenaean Heroic Era (Apollodorus II.iv.5-8)",
          "Complete Perseid Royal House of Mycenae & Tiryns", ["Apollodorus Library II.iv.5-8"],
          "Perseus's sons married daughters of Pelops: Sthenelus -> Eurystheus (taskmaster of Heracles's 12 Labors); Alcaeus -> Amphitryon; Electryon -> Alcmene (bore Heracles by Zeus & twin Iphicles -> Iolaus by Amphitryon!).",
          ["Alcmene", "Amphitryon", "Eurystheus", "Iphicles & Iolaus"]),
        N("grk_heraclidae_return", "Return of the Heraclidae: Heracles → Hyllus → Cleodaeus → Aristomachus → Temenus (Argos), Cresphontes (Messene) & Aristodemus (→ Eurysthenes & Procles of Sparta!)", "greek", 12, "c. 1104 BCE Traditional (Apollodorus II.viii.1-5)",
          "Dorian Conquest of the Peloponnese & Dual Kingship of Sparta", ["Apollodorus Library II.viii.1-5"],
          "Three generations after Hyllus, the Heraclidae conquered the Peloponnese with the Dorians: Temenus received Argos (ancestors of the Argead Kings of Macedon -> Alexander the Great!); Cresphontes took Messene; Aristodemus's twins Eurysthenes & Procles founded the Agiad & Eurypontid dual royal dynasties of Sparta (down to Leonidas of Thermopylae!).",
          ["Hyllus", "Temenus (Argos/Macedon)", "Eurysthenes & Procles (Sparta)", "King Leonidas"], major=True),

        # 4. Agenorids: Crete (Minos) & Thebes (Cadmus -> Oedipus -> Epigoni) (Apollodorus III.i-vii)
        N("grk_minos_crete_family", "Minos & Pasiphaë → Catreus (→ Aerope), Deucalion (→ Idomeneus), Ariadne, Phaedra & Minotaur", "greek", 10, "Minoan Crete Heroic Era (Apollodorus III.i.2-III.iii.2)",
          "Complete Cretan Royal Family (Bridging Minos to Agamemnon & Theseus!)", ["Apollodorus Library III.i.2-III.iii.2"],
          "Minos's son Catreus fathered Aerope (mother of Agamemnon & Menelaus!) and Clymene (mother of Palamedes); son Deucalion fathered Trojan War commander Idomeneus; daughters Ariadne & Phaedra linked Crete to Theseus of Athens.",
          ["Pasiphae", "Ariadne", "Phaedra", "Idomeneus", "Aerope"]),
        N("grk_thebes_oedipus_epigoni", "Cadmus & Harmonia → Polydorus → Labdacus → Laius (+ Jocasta) → Oedipus → Eteocles, Polynices, Antigone & Ismene (Seven Against Thebes & Epigoni)", "greek", 10, "Theban Cycle (Apollodorus III.iv.1-III.vii.7)",
          "Complete Labdacid Dynasty of Thebes (Plus Semele → Dionysus & Illyrius)", ["Apollodorus Library III.iv.1-III.vii.7"],
          "Cadmus's daughters: Semele (mother of Dionysus), Ino, Autonoe (mother of Actaeon), Agave (mother of Pentheus). Son Illyrius (eponym of Illyria!). Polydorus -> Labdacus -> Laius -> Oedipus -> Seven Against Thebes (Polynices, Adrastus, Tydeus, Amphiaraus, Capaneus, Hippomedon, Parthenopaeus) & Epigoni (Alcmaeon, Diomedes, Thersander).",
          ["Labdacus", "Laius & Jocasta", "Oedipus", "Antigone", "Illyrius", "Alcmaeon"], major=True),

        # 5. Pelasgids (Arcadia) & Atlantids (Pleiades -> Sparta) (Apollodorus III.viii-xi)
        N("grk_arcadia_pelasgus_atalanta", "Pelasgus → Lycaon (50 Sons & Callisto) → Arcas → Aleus (→ Auge + Heracles → Telephus) & Atalanta", "greek", 9, "Arcadian Heroic Era (Apollodorus III.viii.1-III.ix.2)",
          "Autochthonous Pelasgian Kings of Arcadia & Heroine Atalanta", ["Apollodorus Library III.viii.1-III.ix.2"],
          "Lycaon's impiety triggered Deucalion's Flood (only son Nyctimus survived); Callisto + Zeus -> Arcas (eponym of Arcadia & Ursa Major) -> Elatus & Aphidas -> Aleus -> Auge (+ Heracles -> King Telephus of Mysia!) & Lycurgus -> Iasus -> Atalanta (mother of Parthenopaeus).",
          ["Pelasgus", "Lycaon", "Callisto & Arcas", "Telephus of Mysia", "Atalanta"]),
        N("grk_sparta_tyndareus_helen", "Atlas & Pleione → 7 Pleiades (Maia → Hermes; Taygete → Lacedaemon → Tyndareus + Leda → Helen, Clytemnestra, Castor & Pollux; Icarius → Penelope)", "greek", 10, "Spartan Heroic Era (Apollodorus III.x.1-III.xi.2)",
          "Complete Atlantid Line of Hermes, Sparta, Helen of Troy & Penelope", ["Apollodorus Library III.x.1-III.xi.2", "Hesiod Catalogue fr. 66"],
          "Lacedaemon (+ Sparta) -> Amyclas -> Cynortes -> Perieres/Oebalus -> Tyndareus (+ Leda -> Helen, Clytemnestra, Dioscuri Castor & Pollux) & Icarius (father of Penelope, wife of Odysseus!). Leucippus's daughter Arsinoe/Coronis + Apollo -> Asclepius (god of medicine!).",
          ["7 Pleiades", "Hermes", "Lacedaemon", "Tyndareus & Leda", "Helen of Troy", "Castor & Pollux", "Penelope", "Asclepius"], major=True),

        # 6. Asopids (Aeacus -> Achilles & Ajax) & Cecropids (Athens -> Theseus) (Apollodorus III.xii-xv)
        N("grk_asopids_aeacus_ajax", "Asopus → Aegina (+ Zeus) → Aeacus → Telamon (→ Ajax & Teucer) & Peleus (+ Thetis → Achilles → Neoptolemus)", "greek", 10, "Aegina, Salamis & Phthia (Apollodorus III.xii.6-III.xiii.8)",
          "Aeacid Heroes of the Trojan War & Ancestors of Olympias/Alexander!", ["Apollodorus Library III.xii.6-III.xiii.8"],
          "Aeacus (Judge of the Dead) fathered Telamon (King of Salamis -> Ajax the Great & Teucer [founder of Salamis in Cyprus!]) and Peleus (+ Nereid Thetis -> Achilles -> Neoptolemus/Pyrrhus, ancestor of the Molossian Kings of Epirus, Queen Olympias [mother of Alexander the Great!], and King Pyrrhus!).",
          ["Aeacus", "Telamon & Ajax", "Peleus & Thetis", "Neoptolemus / Pyrrhus"], major=True),
        N("grk_athens_cecrops_theseus", "Kings of Athens: Cecrops → Erichthonius → Pandion I (Procne/Philomela) → Erechtheus (Creusa/Orithyia) → Aegeus → Theseus → Demophon", "greek", 10, "Attic Heroic Era (Apollodorus III.xiv.1-Epit. I; Eusebius)",
          "Complete Mythic Royal Genealogy of Athens (Slayer of the Minotaur)", ["Apollodorus Library III.xiv.1-III.xv.8", "Eusebius Chronicle (Athenian Kings)"],
          "Earth-born Cecrops (1st King of Athens) -> Erichthonius -> Pandion I -> Erechtheus (daughter Creusa married Xuthus -> Ion, eponym of Ionians!) -> Pandion II -> Aegeus (+ Aethra of Troezen, dau. of Pittheus son of Pelops!) -> Theseus (slew Minotaur; + Antiope -> Hippolytus; + Phaedra -> Acamas & Demophon).",
          ["Cecrops", "Erichthonius", "Erechtheus", "Aegeus", "Theseus of Athens"], major=True),
        N("grk_pelopids_orestes", "Tantalus → Niobe & Pelops (+ Hippodamia) → Atreus, Thyestes & Pittheus → Agamemnon, Menelaus, Aegisthus, Iphigenia, Electra & Orestes", "greek", 10, "Mycenaean Pelopid Cycle (Apollodorus Epit. II-VI)",
          "Complete House of Atreus from Tantalus to Orestes & Tisamenus", ["Apollodorus Library Epitome II-VI"],
          "Tantalus -> Pelops (eponym of Peloponnese!) -> Atreus (+ Aerope of Crete -> Agamemnon & Menelaus), Thyestes (-> Aegisthus), Pittheus (grandfather of Theseus!), plus daughters Astydamia/Nicippe/Lysidice (mothers of Perseids!). Agamemnon + Clytemnestra -> Orestes (+ Hermione -> Tisamenus, slain by Heraclidae!), Electra & Iphigenia.",
          ["Tantalus", "Niobe", "Thyestes & Aegisthus", "Orestes & Electra", "Iphigenia"]),
    ]

    edges += [
        E("grk_chaos_gaia", "grk_nyx_pontus_nereids", "direct", "Hesiod Theogony: Chaos -> Nyx/Erebus; Gaia -> Pontus -> Nereus & 50 Nereids"),
        E("grk_oceanus_hyperion", "grk_titans_complete", "direct", "Complete Titan offspring (Helios, Leto, Hecate, Nike)"),
        E("grk_zeus_olympians", "grk_muses_orpheus", "direct", "Zeus + Mnemosyne/Themis -> 9 Muses (Orpheus), Horae & Fates"),
        E("grk_aeolus", "grk_aetolia_meleager_diomedes", "direct", "Calyce (dau. of Aeolus) -> Endymion -> Aetolus -> Oeneus -> Meleager & Diomedes"),
        E("grk_salmoneus", "grk_neleus_nestor_pelias", "direct", "Salmoneus -> Tyro -> Pelias & Neleus -> King Nestor of Pylos"),
        E("grk_cretheus", "grk_jason_argonauts_medea", "direct", "Cretheus -> Aeson -> Jason (Argonauts + Medea) & Melampus/Adrastus"),
        E("grk_titans_complete", "grk_jason_argonauts_medea", "direct", "Helios -> Aeetes of Colchis -> Medea (wife of Jason)"),
        E("grk_sisyphus", "grk_bellerophon_glaucus", "direct", "Sisyphus -> Glaucus -> Bellerophon (Pegasus & Chimera)"),
        E("grk_aegyptus_danaus", "grk_hypermnestra_abas_danae", "direct", "Hypermnestra + Lynceus -> Abas -> Acrisius -> Danae -> Perseus"),
        E("grk_hypermnestra_abas_danae", "grk_perseus", "direct", "Danae + Zeus -> Perseus (Apollodorus II.iv.1)"),
        E("grk_perseus", "grk_perseids_alcmene", "direct", "Perseus + Andromeda -> Electryon -> Alcmene & Sthenelus -> Eurystheus"),
        E("grk_perseids_alcmene", "grk_heracles", "direct", "Alcmene + Zeus -> Heracles (Apollodorus II.iv.8)"),
        E("grk_heracles", "grk_heraclidae_return", "direct", "Heracles -> Hyllus -> Cleodaeus -> Aristomachus -> Temenus, Cresphontes & Aristodemus"),
        E("grk_heraclidae_return", "grk_sparta_macedon", "direct", "Eurysthenes & Procles (Sparta) + Temenids (Argos -> Macedon)"),
        E("grk_europa_minos", "grk_minos_crete_family", "direct", "Minos + Pasiphae -> Catreus (Aerope), Deucalion (Idomeneus), Ariadne, Phaedra"),
        E("grk_cadmus", "grk_thebes_oedipus_epigoni", "direct", "Cadmus + Harmonia -> Polydorus -> Labdacus -> Laius -> Oedipus -> Epigoni"),
        E("grk_thebes_oedipus_epigoni", "grk_dionysus_oedipus", "direct", "Semele -> Dionysus & Labdacid Oedipus cycle"),
        E("grk_inachus_io", "grk_arcadia_pelasgus_atalanta", "direct", "Niobe (dau. of Phoroneus) -> Pelasgus -> Lycaon -> Arcas -> Telephus & Atalanta"),
        E("grk_atlas", "grk_sparta_tyndareus_helen", "direct", "Atlas + Pleione -> 7 Pleiades (Maia -> Hermes; Taygete -> Sparta/Helen/Penelope)"),
        E("grk_sparta_tyndareus_helen", "grk_dardanus_tros", "direct", "Electra (Pleiades) + Zeus -> Dardanus (founder of Troy)"),
        E("grk_oceanus_hyperion", "grk_asopids_aeacus_ajax", "direct", "Asopus -> Aegina -> Aeacus -> Peleus (Achilles) & Telamon (Ajax)"),
        E("grk_nyx_pontus_nereids", "grk_asopids_aeacus_ajax", "direct", "Nereid Thetis + Peleus -> Achilles (Apollodorus III.xiii.5)"),
        E("grk_asopids_aeacus_ajax", "grk_achilles_odysseus", "direct", "Peleus -> Achilles -> Neoptolemus (ancestor of Alexander's mother Olympias!)"),
        E("grk_asopids_aeacus_ajax", "grk_alexander", "expansion", "Olympias of Epirus (mother of Alexander) descended from Achilles's son Neoptolemus!"),
        E("grk_chaos_gaia", "grk_athens_cecrops_theseus", "direct", "Autochthonous Kings of Athens: Cecrops -> Erechtheus -> Aegeus -> Theseus"),
        E("grk_athens_cecrops_theseus", "grk_xuthus", "direct", "Creusa (dau. of King Erechtheus of Athens) marries Xuthus -> Ion & Achaeus"),
        E("grk_pelops_atreus", "grk_pelopids_orestes", "direct", "Tantalus -> Pelops -> Atreus/Thyestes -> Agamemnon/Menelaus -> Orestes"),
        E("grk_minos_crete_family", "grk_pelopids_orestes", "direct", "Aerope (granddaughter of Minos) marries Atreus -> Agamemnon & Menelaus"),
        E("grk_pelopids_orestes", "grk_agamemnon_menelaus", "direct", "Atreids Agamemnon & Menelaus -> Orestes"),
    ]

    # Individual-level rosters for complete Greek heroic searchability
    add_roster(nodes, edges, "grk_muses_orpheus", "grkr_div", "greek", 3, "Hesiod Theogony & Apollodorus I", "Olympian / Titan / Muse", ["Apollodorus Library Book I", "Hesiod Theogony"], [
        "Hestia (Eldest Olympian)", "Demeter (Goddess of Harvest)", "Hera (Queen of Olympus)", "Hades / Pluto (Underworld)",
        "Poseidon (Lord of the Sea)", "Athena (Daughter of Zeus & Metis)", "Apollo & Artemis (Twins of Zeus & Leto)",
        "Aphrodite (Goddess of Love)", "Ares (God of War)", "Hephaestus (Divine Smith)", "Persephone (Queen of Underworld)",
        "Orpheus (Son of Calliope)", "Helios (Sun Titan)", "Selene & Eos (Moon & Dawn)", "Hecate (Daughter of Perses & Asteria)",
        "Chiron the Centaur (Son of Cronus & Philyra)", "Medusa & Pegasus"
    ], edge_type="direct", edge_label="Greek Divine Lineage (Apollodorus & Hesiod)")

    add_roster(nodes, edges, "grk_jason_argonauts_medea", "grkr_aeo", "greek", 9, "Apollodorus Book I.vii-ix", "Aeolid / Argonaut / Aetolian Hero", ["Apollodorus Library I.vii-ix"], [
        "Endymion (Founder of Elis)", "Aetolus (Eponym of Aetolia)", "King Oeneus of Calydon", "Meleager (Calydonian Boar)",
        "Deianira (Wife of Heracles)", "Tydeus (Seven Against Thebes)", "Diomedes (Hero of the Iliad)", "Phrixus & Helle (Golden Fleece)",
        "Bellerophon (Slayer of Chimera)", "Tyro (Daughter of Salmoneus)", "Pelias of Iolcus", "Neleus of Pylos",
        "King Nestor of Pylos", "Aeson (Father of Jason)", "Jason (Leader of Argonauts)", "Medea of Colchis (Granddaughter of Helios)",
        "Melampus the Seer", "Amphiaraus (Seven Against Thebes)", "King Adrastus of Argos", "Admetus & Alcestis"
    ], edge_type="direct", edge_label="Deucalionid / Aeolid Hero (Apollodorus I)")

    add_roster(nodes, edges, "grk_heraclidae_return", "grkr_her", "greek", 11, "Apollodorus Book II.i-viii", "Perseid / Heraclid Hero", ["Apollodorus Library Book II"], [
        "Phoroneus (First Man of Argos)", "Argus Panoptes", "Hypermnestra & Lynceus", "Abas (King of Argos)",
        "Acrisius & Proetus", "Danaë (Mother of Perseus)", "Alcmene (Mother of Heracles)", "Amphitryon & Iphicles",
        "King Eurystheus of Mycenae", "Hyllus (Son of Heracles & Deianira)", "Telephus of Mysia (Son of Heracles & Auge)",
        "Temenus (Conqueror of Argos -> Macedon)", "Cresphontes (Conqueror of Messene)", "Aristodemus (Father of Spartan Twins)",
        "Eurysthenes (Agiad Founder of Sparta)", "Procles (Eurypontid Founder of Sparta)"
    ], edge_type="direct", edge_label="Inachid / Perseid / Heraclid Lineage (Apollodorus II)")

    add_roster(nodes, edges, "grk_thebes_oedipus_epigoni", "grkr_b3", "greek", 10, "Apollodorus Book III", "Cretan / Theban / Spartan / Trojan / Athenian Hero", ["Apollodorus Library Book III"], [
        "Pasiphaë & the Minotaur", "Ariadne & Phaedra (Daughters of Minos)", "King Idomeneus of Crete", "Semele & Dionysus",
        "Polydorus -> Labdacus -> Laius", "King Oedipus of Thebes (+ Jocasta)", "Eteocles & Polynices", "Antigone & Ismene",
        "Illyrius (Son of Cadmus, Eponym of Illyria)", "Alcmaeon (Leader of Epigoni)", "Pelasgus & Lycaon of Arcadia",
        "Callisto & Arcas", "Atalanta the Huntress", "Lacedaemon & Sparta", "Tyndareus & Leda", "Helen of Troy & Clytemnestra",
        "Castor & Pollux (Dioscuri)", "Penelope (Daughter of Icarius, Wife of Odysseus)", "Asclepius (God of Medicine)",
        "Aeacus -> Telamon -> Ajax the Great", "Teucer (Founder of Cypriot Salamis)", "Peleus & Thetis -> Neoptolemus",
        "King Cecrops of Athens", "King Erechtheus of Athens", "King Aegeus & Theseus of Athens", "Tantalus & Niobe",
        "Thyestes & Aegisthus", "Orestes, Electra & Iphigenia", "Paris (Alexander), Cassandra & Helenus of Troy"
    ], edge_type="direct", edge_label="Heroic Lineage (Apollodorus Book III)")

    return {
        "module": "20_greek_apollodorus_hesiod_complete",
        "title": "Complete Greek Mythological & Heroic Genealogies (Apollodorus The Library Loeb/Frazer & Hesiod Theogony / Catalogue of Women)",
        "nodes": nodes,
        "edges": edges,
    }
