"""
Module 28: North African Amazigh/Berber & Sudanese/Nubian Noahic Lineages.

Sources integrated:
- Ibn Khaldun, Histoire des Berbères et des dynasties musulmanes (Vols. 1, 3, 4)
- H.A. MacMichael, History of the Arabs in the Sudan (historyofarabsin00macm.pdf)
- H.A. MacMichael, The Tribes of Northern and Central Kordofán (tribesofnorthern00macmuoft.pdf)
- A.J. Arkell, A History of the Sudan (2015.103135.History-Of-Sudan-From-The-Earliest-Times-To-1821_text.pdf)
"""

from . import N, E


def build_module():
    nodes, edges = [], []

    nodes += [
        N("ber_branes_botr", "Berr → Bernes (Branes: Sanhaja, Masmuda, Kutama, Auréba) & Madghis al-Abtar (Botr: Zenata, Luwata, Hawwara)", "african", 8,
          "Maghreb Tribal Origins (Ibn Khaldun Vol. 3 pp. 189-191)",
          "Two Great Amazigh Branches Descended from Canaan b. Ham / Mazigh",
          ["Ibn Khaldun Histoire des Berbères Vol. 1, 3 & 4"],
          "Ibn Khaldun transmits the Berber genealogies dividing the Imazighen into the Branes (Sanhaja, Masmuda, Kutama, Auréba) and Botr / Madghis al-Abtar (Zenata, Luwata, Hawwara, Nefzaoua), explicitly preserving Ibn Hazm's chain tracing Madghis through Ber -> Herik -> Bedian -> Canaan -> Ham -> Noah.",
          ["Branes", "Botr (Madghis al-Abtar)", "Zenata & Sanhaja"], major=True),
        N("ber_koceila_kahina", "Koceila (Auréba) & Queen al-Kahina / Dihya (Jerawa Zenata, 7th c. CE)", "african", 19,
          "7th c. CE (Ibn Khaldun Vol. 3 p. 193)",
          "Sovereign Amazigh Leaders Descended from Branes & Botr",
          ["Ibn Khaldun Histoire des Berbères Vol. 3 p. 193"],
          "Koceila (leader of the Branes Auréba) and Queen al-Kahina / Dihya (queen of the Botr Jerawa Zenata confederation) led the Amazigh resistance across North Africa.",
          ["Koceila", "Queen al-Kahina / Dihya"], major=False),
        N("sud_cush_nuba_beja", "Nubians (Nuba) & Beja (Blemmyes) — Christian Kingdoms of Nobatia, Makuria & Alodia", "african", 8,
          "Ancient to Medieval Sudan (MacMichael Vol. 1 pp. 12-51; Arkell)",
          "Cushitic/Nubian Lineages of the Middle Nile",
          ["MacMichael History of Arabs in Sudan pp. 12-51", "Arkell History of Sudan"],
          "Documents the pre-Islamic Cushite/Nubian and Beja populations (Blemmyes) of Northern Sudan who formed the Christian kingdoms of Nobatia, Makuria (Dongola) & Alodia (Soba).",
          ["Nuba / Nobatia / Makuria", "Beja / Blemmyes"], major=True),
        N("sud_jaaliyyin_abbas", "Ja'aliyyin Confederation of Sudan (Descent from al-'Abbas b. 'Abd al-Muttalib → Ishmael)", "african", 20,
          "Medieval–Modern Sudan (MacMichael Vol. 1 pp. xi, 131-195)",
          "Sudanese 'Abbasid Nisba Lineages Blended with Nubia",
          ["MacMichael History of Arabs in Sudan Vol. 1 pp. xi, 131-195", "Tribes of Kordofán"],
          "MacMichael catalogs dozens of Sudanese Arab nisba manuscripts uniting the Ja'aliyyin, Danagla, Shayqiya, Batahin & Rubatab via Ibrahim Ja'al back to al-'Abbas, uncle of Prophet Muhammad (Quraysh/Ishmael), while intermarrying with Nubian princesses.",
          ["Ibrahim Ja'al", "Ja'aliyyin & Danagla", "'Abbasid Nisba"], major=True),
        N("sud_juhayna_qahtan", "Juhayna (Guhayna), Baqqara, Kababish & Shukriya of Sudan & Kordofan (Qahtan / Joktan Line)", "african", 20,
          "Medieval–Modern Sudan & Darfur (MacMichael pp. 131, 271-319)",
          "Yemenite Qahtanite Migrations via Egypt & Red Sea into Sudan",
          ["MacMichael History of Arabs in Sudan pp. 131, 271-319", "MacMichael Tribes of Kordofán"],
          "Sudanese chronicles trace the Juhayna/Guhayna confederation (Baqqara, Kababish, Shukriya, Hamar, Rizayqat) back to southern Arabian Himyar & Qahtan (Joktan), migrating through Egypt and the Red Sea into Kordofan & Darfur.",
          ["Juhayna / Guhayna", "Baqqara & Kababish"], major=True),
        N("sud_funj_sennar", "Funj Sultanate of Sennar (1504–1821 CE — Umayyad / Nubian Pedigree)", "african", 21,
          "1504–1821 CE (Arkell History of Sudan; MacMichael)",
          "Black Sultanate of Sudan Linking Umayyad & Nubian Royal Traditions",
          ["Arkell History of Sudan", "MacMichael History of Arabs in Sudan"],
          "Amara Dunqas founded the Funj Sultanate at Sennar in 1504 CE; Funj royal genealogies claimed descent from Umayyad refugees passing through Abyssinia and Nubia.",
          ["Amara Dunqas", "Sultanate of Sennar"], major=False),
    ]

    edges += [
        E("bib_canaan", "ber_branes_botr", "expansion", "Ibn Khaldun Histoire des Berbères Vol. 3 pp. 189-191 (citing Ibn Hazm): Berbers descend from Canaan (Kenan) b. Ham b. Noah via Mazigh/Madghis"),
        E("af_mazigh", "ber_branes_botr", "direct", "Mazigh -> Berr -> Bernes (Branes) & Madghis al-Abtar (Botr)"),
        E("ber_branes_botr", "ber_koceila_kahina", "direct", "Ibn Khaldun Vol. 3 p. 193: Amazigh resistance leaders descended from Branes & Botr"),
        E("bib_cush", "sud_cush_nuba_beja", "expansion", "MacMichael History of the Arabs in the Sudan Vol. 1 pp. 12-51 & Arkell History of Sudan: Pre-Islamic Cushite/Hamitic kingdoms of Nubia & Sudan"),
        E("isl_umayyad_abbasid_fatimid", "sud_jaaliyyin_abbas", "expansion", "MacMichael Vol. 1 pp. xi, 131-195: Sudanese nisbas tracing the Ja'aliyyin & Danagla to al-'Abbas, uncle of Muhammad"),
        E("sud_cush_nuba_beja", "sud_jaaliyyin_abbas", "expansion", "Intermarriage with Nubian Cushite kingdoms"),
        E("tab_yarub_jurhum_himyar", "sud_juhayna_qahtan", "expansion", "MacMichael History of Arabs in Sudan pp. 131, 271-319 & Tribes of Kordofan: Yemenite Qahtanite/Himyarite migrations across the Red Sea & Egypt into Sudan & Darfur"),
        E("isl_umayyad_abbasid_fatimid", "sud_funj_sennar", "expansion", "Arkell History of Sudan & MacMichael: Funj royal pedigree claiming Umayyad descent via Abyssinia & Nubia"),
        E("sud_cush_nuba_beja", "sud_funj_sennar", "expansion", "Nubian-Sudanese territorial synthesis at Sennar"),
    ]

    return {
        "module": "28_africa_berbers_sudan_noahic",
        "title": "Ibn Khaldun Amazigh (Berbers) & Sudanese/Nubian Noahic Lineages",
        "nodes": nodes,
        "edges": edges,
    }
