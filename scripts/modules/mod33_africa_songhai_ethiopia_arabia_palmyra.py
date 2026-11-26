"""
Module 33: West Africa (Tarikh es-Soudan — Songhai & Timbuktu from Yemen),
North Africa & Al-Andalus (Ibn 'Abd al-Hakam — Futuh Misr), Pre-Islamic Arabia
(Caussin de Perceval), Ethiopia (Hiob Ludolf 1684), and Palmyra / Tadmor
(Abednego Seller 1696 — King Solomon, Nabataean Aretas & Queen Zenobia).

Sources integrated:
- Abderrahman es-Sa'di, Tarikh es-Soudan (tr. O. Houdas, 1900, Ch. 1-3 pp. 35-44)
- Ibn 'Abd al-Hakam, Futuh Misr / History of the Conquest of Egypt, North Africa & Spain
  (ed. Charles C. Torrey, Yale Oriental Series III)
- A. P. Caussin de Perceval, Essai sur l'Histoire des Arabes avant l'Islamisme Vol. 1 (1847, pp. 21-39)
- Hiob Ludolf, A New History of Ethiopia (1684, pp. 166-167 & Gondar Kings)
- Abednego Seller, The Antiquities of Palmyra (1696, Preface & History of Zenobia)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("sng_za_al_ayaman",
          "Za-Al-Ayaman ('Came from Yemen' → Kukya on the Niger) → 14 Pre-Islamic Za Kings → Za-Kosoi (1st Muslim King of Songhai, 1009 CE)",
          "african", 18,
          "Early Niger Bend → 1010 CE (Tarikh es-Soudan Ch. 1 pp. 35-38)",
          "Yemeni-Originated Founder of the Songhai Za Dynasty on the Niger",
          ["Abderrahman es-Sa'di Tarikh es-Soudan (tr. Houdas 1900) Ch. 1 pp. 35-38"],
          "Tarikh es-Soudan derives the royal Za (Dia) dynasty of Kukya/Songhai from two brothers who traveled from Yemen ('dja men el-Yemen' -> Za-Al-Ayaman), slaying the pagan river-idol and ruling through 14 pre-Islamic kings until Za-Kosoi (Moslem-dam) embraced Islam in AH 400 (1009-1010 CE).",
          ["Za-Al-Ayaman", "Dja men el-Yemen", "Za-Kosoi (1009 CE)"],
          major=True),

        N("sng_sonni_askia_timbuktu",
          "Songhai Empire & Timbuktu: Sonni Ali-Kolon → Sonni Ali (1464) → Askia El-Hadj Mohammed (Askia the Great, 1493)",
          "african", 20,
          "13th–16th c. CE (Tarikh es-Soudan Ch. 2-3 pp. 39-44)",
          "Imperial Sultans of Gao & Timbuktu Following Mali Supremacy",
          ["Abderrahman es-Sa'di Tarikh es-Soudan (tr. Houdas 1900) Ch. 2-3 pp. 39-44"],
          "Brothers Ali-Kolon and Selman-Nar (sons of Za-Yasiboy) freed Songhai from Mansa Musa's Mali suzerainty, inaugurating the Sonni line culminating in Sonni Ali before Askia El-Hadj Mohammed (the Great, 1493) elevated Timbuktu and Songhai.",
          ["Sonni Ali-Kolon", "Sonni Ali", "Askia El-Hadj Mohammed"],
          major=True),

        N("hak_futuh_misr_andalus",
          "Futuh Misr (Ibn 'Abd al-Hakam): 'Amr ibn al-'As (Egypt), Uqba ibn Nafi (Maghreb) & Tariq ibn Ziyad (Al-Andalus, 711 CE)",
          "african", 19,
          "7th–8th c. CE (Ibn 'Abd al-Hakam Futuh Misr, Torrey ed.)",
          "Earliest Arabic Chronicle of Egypt, Berbers of North Africa & Al-Andalus",
          ["Ibn 'Abd al-Hakam Futuh Misr (ed. C.C. Torrey, Yale Oriental Series III)"],
          "Earliest extant Arabic historical narrative covering 'Amr ibn al-'As's Coptic treaty in Egypt (Misr), Uqba ibn Nafi's campaigns across the Amazigh/Berber Maghreb, and Tariq ibn Ziyad & Musa ibn Nusayr's 711 CE crossing into Visigothic Spain.",
          ["'Amr ibn al-'As", "Uqba ibn Nafi", "Tariq ibn Ziyad"],
          major=True),

        N("cdp_ariba_cush_amaliqa",
          "Ancient Arabian Ariba (Caussin de Perceval Vol. 1): Cushites of Arabia, 'Ad (Loqman) & Amaliqa / Samayda of Ayla",
          "arabian", 8,
          "Pre-Islamic Antiquity (Caussin de Perceval Vol. 1 pp. 21-39)",
          "Extinct Ancient Arabian Tribes Bridged to Cush, Uz/Aram & Ham",
          ["Caussin de Perceval Essai sur l'Histoire des Arabes Vol. 1 (1847) pp. 21-39"],
          "Caussin de Perceval synthesizes Jewish and classical Arab genealogies (Ibn Sa'id, Ibn Habib, Tabari) tracing the primitive Arab al-'Ariba — Cushites along the Arabian peninsula, 'Ad (Uz b. Aram / Amalek b. Ham, including Loqman of the Seven Vultures), and the Samayda Amaliqa of Ayla.",
          ["Al-'Ariba", "Samayda of Ayla", "Loqman"],
          major=False),

        N("cdp_qahtan_adnan_tribes",
          "Pre-Islamic Arabian Tribal Tree (Caussin de Perceval Vol. 1): Qahtan (Himyar, Kahlan, Azd, Kindah) & Adnan (Ma'add → Nizar → Mudar & Rabi'a)",
          "arabian", 13,
          "Bronze Age → 6th c. CE (Caussin de Perceval Vol. 1 pp. 23-39+)",
          "Complete Bifurcation of Southern Qahtanite & Northern Adnanite Arab Confederations",
          ["Caussin de Perceval Essai sur l'Histoire des Arabes Vol. 1 (1847) pp. 23-39+"],
          "Maps the dual trunk of Arabian ethnogenesis: Southern Al-'Ariba / Mutariba descending from Qahtan (Joktan b. Eber -> Ya'rub -> Himyar, Kahlan, Azd, Ghassan, Lakhm & Kindah) and Northern Musta'riba descending from Ishmael via Adnan -> Ma'add -> Nizar -> Mudar & Rabi'a.",
          ["Himyar & Kahlan", "Azd & Kindah", "Mudar & Rabi'a"],
          major=True),

        N("eth_ludolf_kaleb_himyar",
          "Ludolf's Ethiopian-Himyarite War (1684): King Kaleb (Elesbaan) vs. Dhu Nuwas, Abreha & Saif ibn Dhi Yazan (+ Khosrow I Anushirvan)",
          "african", 19,
          "525–575 CE (Hiob Ludolf 1684 pp. 166-167)",
          "6th c. Aksumite–Himyarite–Sasanian Geopolitical Pedigree Bridge",
          ["Hiob Ludolf A New History of Ethiopia (1684) pp. 166-167"],
          "Ludolf chronicles King Kaleb (Caleb / Elesbaan) of Aksum avenging the Christian martyrs of Najran against Himyarite king Dhu Nuwas, placing Abreha in Yemen until Himyarite prince Saif ibn Dhi Yazan regained Yemen with Sasanian Emperor Khosrow I Anushirvan's aid.",
          ["Elesbaan (Kaleb)", "Abreha", "Saif ibn Dhi Yazan"],
          major=True),

        N("eth_ludolf_gondar_kings",
          "Gondar Solomonic Emperors (Ludolf 1684): Lebna Dengel → Galawdewos → Emperor Susenyos → Emperor Fasilides (Founder of Gondar, 1632)",
          "african", 21,
          "1508–1667 CE (Hiob Ludolf 1684)",
          "Renaissance & Early Modern Ethiopian Solomonic Sovereign Succession",
          ["Hiob Ludolf A New History of Ethiopia (1684)"],
          "Continues the Ethiopian Solomonic line documented in Ludolf's 1684 chronicle from Lebna Dengel (Dawit II) and Galawdewos (Claudius) through Emperor Susenyos I and his son Emperor Fasilides, who established the royal capital at Gondar in 1632.",
          ["Lebna Dengel", "Susenyos I", "Emperor Fasilides"],
          major=True),

        N("pal_solomon_aretas_tadmor",
          "Palmyra / Tadmor (Seller 1696): Founded by King Solomon → Nabataean King Aretas (Al-Harith of Ghassan / Petra)",
          "arabian", 16,
          "10th–1st c. BCE (Abednego Seller 1696 Preface)",
          "Solomonic Foundation of Tadmor & Arab-Nabataean Princes of Syria",
          ["Abednego Seller The Antiquities of Palmyra (1696) Preface", "1 Kings 9:18 / 2 Chr 8:4"],
          "Seller (1696) links ancient Palmyra directly to Biblical Tadmor fortified by King Solomon in the Syrian desert, tracing subsequent Arabian mastery from Nabataean king Aretas (equated by Seller with the Al-Harith rulers of Petra and Ghassan, contemporary of Pompey c. 63 BCE).",
          ["Tadmor in the Wilderness", "King Aretas / Al-Harith"],
          major=True),

        N("pal_odenathus_zenobia",
          "Palmyrene Empire (Seller 1696): King Odenathus → Queen Zenobia (Claiming Descent from Cleopatra VII & Dido) & Vaballathus",
          "greek", 19,
          "250–274 CE (Abednego Seller 1696)",
          "Palmyrene Imperial House Claiming Ptolemaic & Phoenician Royal Bloodlines",
          ["Abednego Seller The Antiquities of Palmyra (1696)", "Historia Augusta"],
          "Seller details the rise of Palmyra under Septimius Odaenathus ('King of Kings') and his learned queen Zenobia Bat-Zabbai — who claimed royal ancestry from Egypt's Cleopatra VII and Carthaginian Dido while ruling Syria, Egypt & Anatolia before Aurelian's triumph.",
          ["Odaenathus", "Queen Zenobia", "Vaballathus"],
          major=True),
    ]

    edges += [
        E("bib_joktan", "sng_za_al_ayaman", "syncretic", "Tarikh es-Soudan Ch. 1 pp. 36-38: Za-Al-Ayaman ('dja men el-Yemen') originates in Yemeni / Qahtanite migration to the Niger River"),
        E("bir_himyar_lakhmid_ghassan", "sng_za_al_ayaman", "syncretic", "Yemeni royal dispersion tradition connecting South Arabia to Kukya / Songhai (Tarikh es-Soudan)"),
        E("bib_moses", "sng_za_al_ayaman", "syncretic", "Tarikh es-Soudan p. 37 records traditional association of Kukya antiquity with Pharaoh's magicians vs. Moses"),
        E("sng_za_al_ayaman", "sng_sonni_askia_timbuktu", "direct", "Tarikh es-Soudan Ch. 2-3 pp. 39-44: Za-Yasiboy -> Sonni Ali-Kolon -> Sonni Ali -> Askia El-Hadj Mohammed"),
        E("af_sundiata", "sng_sonni_askia_timbuktu", "cognate", "Tarikh es-Soudan pp. 36, 42-44: Kankan-Mousa (Mansa Musa of Mali) -> liberation of Songhai under Sonni Ali-Kolon"),
        E("isl_umayyad_abbasid_fatimid", "hak_futuh_misr_andalus", "expansion", "Ibn 'Abd al-Hakam Futuh Misr: Quraysh/Companions & Umayyad commanders across Egypt, Maghreb & Spain"),
        E("bib_mizraim", "hak_futuh_misr_andalus", "cognate", "Futuh Misr opens with pre-Islamic traditions of Misr/Egypt before 'Amr ibn al-'As"),
        E("ber_branes_botr", "hak_futuh_misr_andalus", "cognate", "Futuh Misr documents Uqba ibn Nafi & Tariq ibn Ziyad alongside North African Berber tribes"),
        E("bib_cush", "cdp_ariba_cush_amaliqa", "syncretic", "Caussin de Perceval Vol. 1 p. 21: Ancient Jewish & Arab traditions placing Cushites across Arabia prior to Ethiopia"),
        E("tab_ad_thamud_hud_salih", "cdp_ariba_cush_amaliqa", "cognate", "Caussin de Perceval Vol. 1 pp. 28-32: 'Ad, Prophet Hud & survivor Loqman"),
        E("tab_lud_amalek_tasm", "cdp_ariba_cush_amaliqa", "cognate", "Caussin de Perceval Vol. 1 pp. 35-39: Amaliqa & Samayda princes of Ayla on the Red Sea"),
        E("bib_joktan", "cdp_qahtan_adnan_tribes", "direct", "Caussin de Perceval Vol. 1 p. 23: Qahtan (Yoktan/Joktan b. Eber) progenitor of Yemenite Arab tribes"),
        E("bib_ishmael", "cdp_qahtan_adnan_tribes", "expansion", "Caussin de Perceval Vol. 1 p. 23: Ishmael b. Abraham -> Adnanite northern tribes"),
        E("ar_adnan_quraysh", "cdp_qahtan_adnan_tribes", "cognate", "Same Adnan -> Ma'add -> Nizar northern Arab tribal genealogy"),
        E("bir_himyar_lakhmid_ghassan", "cdp_qahtan_adnan_tribes", "cognate", "Southern Qahtanite confederations (Himyar, Lakhm, Ghassan, Kindah) mapped in Caussin de Perceval Vol. 1"),
        E("keb_kaleb_gabramaskal_yekuno", "eth_ludolf_kaleb_himyar", "cognate", "Ludolf 1684 pp. 166-167: Detailed synchronism of King Kaleb (Elesbaan) of Aksum with Himyar"),
        E("bir_himyar_lakhmid_ghassan", "eth_ludolf_kaleb_himyar", "cognate", "Ludolf 1684 pp. 166-167: Dhu Nuwas, Abreha & Saif ibn Dhi Yazan of the Homerites (Himyar)"),
        E("bir_sasanians_complete", "eth_ludolf_kaleb_himyar", "cognate", "Ludolf 1684 p. 166: Khosrow I Anushirvan aids Saif ibn Dhi Yazan in Yemen"),
        E("eth_haile_selassie", "eth_ludolf_gondar_kings", "expansion", "Ludolf 1684: Solomonic line Lebna Dengel -> Galawdewos -> Susenyos -> Fasilides (Gondar)"),
        E("jud_solomon", "pal_solomon_aretas_tadmor", "direct", "Seller 1696 & 1 Kings 9:18: King Solomon built Tadmor / Palmyra in the Syrian desert"),
        E("bib_ishmael", "pal_solomon_aretas_tadmor", "expansion", "Seller 1696 connects Nabataean Arabs under King Aretas directly with Palmyrene desert sovereignty"),
        E("her_antipater_cypros", "pal_solomon_aretas_tadmor", "cognate", "Nabataean royal dynasty of Petra allied/intermarried with Idumeans & Herodians"),
        E("bir_himyar_lakhmid_ghassan", "pal_solomon_aretas_tadmor", "cognate", "Seller 1696 Preface explicitly identifies Appian's Aretas with the Al-Harith princes of Ghassan"),
        E("pal_solomon_aretas_tadmor", "pal_odenathus_zenobia", "expansion", "Seller 1696: Imperial Palmyra rising to Odaenathus, Queen Zenobia & Vaballathus"),
        E("eg_ptolemies_complete", "pal_odenathus_zenobia", "syncretic", "Seller 1696 & Historia Augusta: Queen Zenobia claimed descent from Cleopatra VII of Egypt"),
        E("grk_dido_carthage", "pal_odenathus_zenobia", "syncretic", "Seller 1696: Palmyrene tradition linking Zenobia's Syrian lineage with Dido of Tyre/Carthage"),
        E("rom_echard_imperial_bridge", "pal_odenathus_zenobia", "cognate", "Emperor Aurelian defeats Zenobia (272-274 CE) and integrates Palmyra into Rome"),
    ]

    return {
        "module": "33_africa_songhai_ethiopia_arabia_palmyra",
        "title": "Songhai & Timbuktu (Tarikh es-Soudan), Futuh Misr, Arabian Ariba/Qahtan/Adnan, Ludolf Ethiopia & Palmyra/Zenobia",
        "nodes": nodes,
        "edges": edges,
    }
