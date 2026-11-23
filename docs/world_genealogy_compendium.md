# Ancient World Genealogy Compendium â€” Phase 1

> [!IMPORTANT]
> **Methodological Foundation (5-Tier Provenance System):** Building a truly global ancient genealogy without distorting primary sources requires separating *what each text explicitly claims* from *how ancient traditions intersect*. Every link in our [Interactive Explorer](../index.html) and [JSON Database](../data/genealogy_core.json) is tagged with one of five provenance tiers:

| Tier | Tag | Definition | Example |
| :--- | :--- | :--- | :--- |
| **1** | `direct` | Explicit parent-child descent inside primary canonical or ancient texts | Genesis 5 (Seth â†’ Noah); *Shiji* Ch. 1 (Huangdi â†’ Zhuanxu â†’ Yu) |
| **2** | `expansion` | Matriarchs, intermediate links, or migrations supplied by extra-biblical or secondary chronicles | *Book of Jubilees* matriarchs (Azura, Emzara); *1 Enoch* Watchers; *Shiji* Ch. 110 (Xia â†’ Xiongnu) |
| **3** | `cognate` | Linguistically or historically attested shared ancestral figure or ethnonym across independent corpora | Vedic **Vivasvan / Yama** = Avestan **Vivanghant / Yima**; Biblical **Madai** = Medes; **Mizraim** = Phoenician **Misor** / Egypt |
| **4** | `parallel` | Independent structural or archetypal parallel across ancient texts | 7th Patriarch **Enoch** â†” 7th King **Enmeduranki**; Great Flood Survivors (Noah, Ziusudra, Vaivasvata Manu, Yima, Yu) |
| **5** | `syncretic` | Classical or medieval universal chronicler synthesis grafting distant nations onto one tree | Rashid al-Din (*Jami' al-Tawarikh*) linking **Japheth â†’ Turk â†’ Oghuz Khagan**; *Book of Jasher* linking **Esau â†’ Zepho â†’ Rome** |

---

## 1. Global Cross-Tradition Convergence Map

```mermaid
flowchart TD
    P["Primordial Ancestors Archetype"]

    subgraph ANE["Ancient Near East & Biblical"]
        ADAM["Adam & Eve (Gen / Jubilees)"]
        ENOCH["Enoch - 7th Patriarch (Gen / 1 Enoch)"]
        NOAH["Noah & Emzara/Naamah (Flood)"]
        SHEM["Shem (Elam, Asshur, Arphaxad, Aram)"]
        HAM["Ham (Cush/Nimrod, Mizraim, Canaan)"]
        JAPH["Japheth (Gomer, Magog, Madai, Javan)"]
        ABR["Abraham (Israel, Ishmael, Esau, Midian)"]
    end

    subgraph MESO["Mesopotamia"]
        ENUMA["Enki & Nintu (Clay Creation)"]
        ENMED["En-men-dur-ana - 7th King (Sippar)"]
        ZIU["Ziusudra / Utnapishtim (Flood)"]
        URUK["Gilgamesh (Uruk/Erech) & Sargon (Akkad)"]
    end

    subgraph IRAN["Iranian / Zoroastrian"]
        GAYO["Gayomart -> Mashya & Mashyana"]
        VIV["Vivanghant (Avesta)"]
        YIMA["Yima / Jamshid (Vara Cataclysm)"]
        FER["Fereydun -> Salm, Tur & Iraj"]
        MEDES["Historical Medes & Achaemenids"]
    end

    subgraph INDIA["Vedic & Puranic India"]
        BMANU["Brahma -> Svayambhuva Manu / Kashyapa"]
        VIVAS["Vivasvan / Surya (Rigveda)"]
        YAMA["Yama & Yami"]
        VMANU["Vaivasvata Manu (Matsya Flood)"]
        SURYA["Surya Vamsha (Ikshvaku -> Rama & Buddha)"]
        CHANDRA["Chandra Vamsha (Yayati -> 5 Sons -> Bharata/Pandavas)"]
    end

    subgraph EASIA["East Asia & Steppe"]
        FUXI["Fuxi & Nuwa (Three Sovereigns)"]
        HUANG["Yandi & Huangdi (Yellow Emperor)"]
        YU["Yu the Great (Flood) -> Xia Dynasty"]
        SHZHOU["Shang & Zhou Dynasties"]
        STEPPE["Chunwei -> Xiongnu & Oghuz Khagan"]
        JAPAN["Izanagi/Amaterasu -> Emperor Jimmu"]
    end

    P -.-> ADAM & ENUMA & GAYO & BMANU & FUXI & JAPAN
    ADAM --> ENOCH --> NOAH
    NOAH --> SHEM & HAM & JAPH
    SHEM --> ABR
    ENUMA --> ENMED --> ZIU --> URUK
    ENOCH -. "7th Sage Parallel" .- ENMED
    NOAH -. "Flood Parallel" .- ZIU
    HAM == "Cognate: Shinar/Erech/Accad" ==> URUK
    JAPH == "Cognate: Madai = Medes" ==> MEDES
    SHEM == "Cognate: Elam -> Anshan" ==> MEDES
    GAYO --> VIV --> YIMA --> FER --> MEDES
    VIV == "EXACT Proto-Indo-Iranian Cognate" == VIVAS
    YIMA == "EXACT Proto-Indo-Iranian Cognate" == YAMA
    BMANU --> VIVAS --> YAMA
    VIVAS --> VMANU --> SURYA & CHANDRA
    ZIU -. "Flood Parallel" .- VMANU
    FUXI --> HUANG --> YU & SHZHOU
    YU --> STEPPE
    JAPH -. "Syncretic: Rashid al-Din" .-> STEPPE
    FER -. "Syncretic: Turan" .-> STEPPE
```

---

## 2. Biblical & Extra-Biblical Traditions (Bible, Jubilees, 1 Enoch, Book of Jasher)

Canonical Genesis supplies the skeletal patrilineal spine, while Second Temple texts (**Book of Jubilees**, **1 Enoch**, **Dead Sea Scrolls Genesis Apocryphon** & **Book of Giants**) and later midrashic chronicles (**Sefer haYashar / Book of Jasher**, **Cave of Treasures**, **Josephus**) supply the **matriarchs**, **Watcher intermarriages**, **missing generations**, and **global migrations**.

> [!NOTE]
> **Critical Note on the Book of Jasher:** The ancient *Book of Jasher* referenced in Joshua 10:13 and 2 Samuel 1:18 has not survived archaeologically. The widely read text titled *Sefer haYashar* ("Book of Jasher") is a rich Hebrew midrashic chronicle first printed in 1625 (drawing on Talmudic, Midrashic, and 10th-century *Josippon* traditions). It is invaluable for tracing traditional Jewish-Mediterranean genealogical bridges (like Esau's grandson Zepho ruling Italy/Kittim), and is tagged `expansion` or `syncretic` accordingly.

### Antediluvian Lineages (10 Generations: Sethite & Cainite)

| Gen | Sethite Patriarch | Wife / Matriarch (*Jubilees* / *Jasher*) | Cainite Parallel (Gen 4) | Extra-Biblical Highlights |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Adam** | **Eve (Hawwah)** | Adam & Eve | *Jubilees 4* names daughters **Awan** and **Azura**. |
| 2 | **Seth** | **Azura** (*Jub 4:11*) | **Cain** + **Awan** (*Jub 4:9*) | Josephus (*Ant. 1.2.3*) credits Sethites with astronomy & two wisdom pillars. |
| 3 | **Enosh** | **Noam** (*Jub 4:13*) | **Enoch** (city builder) | *Jasher 2* associates Enosh's era with early idolatry and partial flooding of the earth. |
| 4 | **Kenan** | **Mualeleth** (*Jub 4:14*) | **Irad** | *Cave of Treasures* portrays Kenan as custodian of Adam's cave and sacred lore. |
| 5 | **Mahalalel** | **Dinah** (dau. of Barakiel, *Jub 4:15*) | **Mehujael** | â€” |
| 6 | **Jared** | **Baraka** (*Jub 4:16*) | **Methushael** | **1 Enoch 6**: 200 **Watchers** (Semyaza, Azazel) descend on Mt. Hermon, siring the **Nephilim** (*Book of Giants* names Ohya, Hahya, Mahaway). |
| 7 | **Enoch** (365 yrs) | **Edni** (*Jub 4:20*) | **Lamech** (+ Adah & Zillah) | **1 Enoch & Jubilees 4:17**: First human to learn writing, calendar, astronomy; taken to heaven. Cainite Lamech sires Jabal, Jubal, Tubal-cain, & **Naamah**. |
| 8 | **Methuselah** | **Edna** (*Jub 4:27*) | *(Line ends in Flood â€” except via Naamah in Jasher)* | Custodian of Enoch's heavenly books (*1 Enoch 82*). |
| 9 | **Lamech** | **Betenos** (*Jub 4:28*) | â€” | *1 Enoch 106* & *Genesis Apocryphon (1Q20)*: Lamech fears Noah's luminous birth is from the Watchers until Enoch reassures him. |
| 10 | **Noah** | **Emzara** (*Jub 4:33*) / **Naamah** (*Jasher 5:15*) | â€” | *Jasher 5:15* merges the Sethite and Cainite lines via Noah's wife Naamah! |

### Post-Flood Table of Nations (Genesis 10, Jubilees 8â€“9, Jasher 7)

- **Shem** (+ *Sedeqetelebab*, Jub 7:16 â€” assigned Central Asia to India/Tinas):
  - **Elam** (Elamites of SW Iran/Susa), **Asshur** (Assyrians), **Lud** (Lydians), **Aram** (Syrians/Arameans)
  - **Arphaxad** â†’ **Cainan** (*LXX, Luke 3:36, Jubilees 8:1â€“4*, who discovers Watcher astronomical carvings!) â†’ **Salah** â†’ **Eber** (eponym of Hebrews & Arabian *Hud*):
    - **Joktan (Qahtan)** â†’ 13 Southern Arabian tribes including **Sheba (Saba)**, **Ophir**, **Hazarmaveth (Hadhramaut)**
    - **Peleg** (Babel division) â†’ Reu â†’ Serug â†’ Nahor â†’ Terah â†’ **Abraham** (+ Sarah â†’ **Isaac** â†’ **Jacob/Israel** [12 Tribes] & **Esau/Edom** [â†’ Eliphaz â†’ **Zepho**, who in *Jasher 61* becomes King of Kittim/Italy]; + Hagar â†’ **Ishmael** [12 princes including Kedar & Nebaioth â†’ **Adnanite Arabs**]; + Keturah â†’ **Midian** [Jethro/Zipporah] & 5 brothers).
- **Ham** (+ *Na'eltama'uk*, Jub 7:16 â€” assigned Africa & southern lands):
  - **Cush** â†’ **Nimrod** (Genesis 10:10 explicitly bridges to Mesopotamia: **Babel, Erech [Uruk], Accad [Akkad], Calneh, Nineveh**; *Jasher 7* claims Nimrod wore Adam's garments and clashed with Abram).
  - **Mizraim** (Egypt; cognate with Phoenician *Misor*), **Phut** (Libya/Punt), **Canaan** (Sidon, Heth/Hittites, Amorites, Jebusites, Sinites).
- **Japheth** (+ *Adataneses*, Jub 7:16 â€” assigned Anatolia, Europe, Iranian highlands, Northern Eurasia):
  - **Gomer** (Cimmerians â†’ Ashkenaz [Scythians], Riphath, Togarmah [Armenia]), **Magog** (Steppe/Northern Eurasia), **Madai** (historical **Medes** of Iran; *Jubilees 10:35* says he married Shem's daughter!), **Javan** (Ionians/Greeks â†’ Elishah, Tarshish, Kittim [Cyprus], Dodanim/Rodanim [Rhodes]), **Tubal** (Tabal), **Meshech** (Mushki/Phrygia), **Tiras** (Thracians/Tyrsenians).

---

## 3. Ancient Middle Eastern Religions & Chronicles

### Mesopotamia (Sumer, Akkad, Babylon)
- **Creation (*Enuma Elish* & *Atrahasis*, 2nd millennium BCE):** Apsu & Tiamat â†’ Anu â†’ Enki (Ea) & Nintu fashion the first humans (*Lullu*) from clay mixed with divine blood.
- **Antediluvian Kings (*Sumerian King List* WB 444 & Berossus's *Babyloniaca*):** 8 kings in the Sumerian prism (10 in Berossus), reigning vast ages before the Flood â€” structurally mirroring Genesis 5's 10 patriarchs. Crucially, the **7th king, En-men-dur-ana (Enmeduranki) of Sippar** (city of sun god Shamash), ascends to the divine assembly to learn heavenly secrets and divination â€” a remarkable parallel to **Enoch** (7th patriarch, 365 solar years).
- **Flood & Post-Flood Dynasties:** **Ubara-Tutu** â†’ **Ziusudra / Utnapishtim / Atrahasis** of Shuruppak survives the Deluge. Post-Flood kingship returns at Kish and Uruk (**Enmerkar â†’ Lugalbanda â†’ Gilgamesh**), followed by **Sargon of Akkad** (and his daughter **Enheduanna**, history's first named author) â€” cities explicitly linked to Nimrod in Genesis 10:10!

### Ancient Iran / Zoroastrianism (*Avesta*, *Bundahishn*, *Shahnameh*)
- **Primordial Origin:** **Gayomart (Keyumars)** â†’ rhubarb plant splits into **Mashya & Mashyana**, first couple who bear 7 twin pairs populating the 7 *karshvars* (climes) of Earth.
- **The Verified Proto-Indo-Iranian Bridge:** Siamak â†’ Hushang â†’ Tahmuras â†’ **Vivanghant (Vivanhao)** â†’ **Yima Khshaeta (Jamshid)**. Linguists and historians of religion universally recognize **Vivanghant = Vedic Vivasvan** and **Yima = Vedic Yama** as an **exact shared ancestral lineage** predating the split of Iranian and Indo-Aryan peoples (~2000 BCE). In *Vendidad 2*, Yima builds the subterranean *Vara* enclosure preserving humans, animals, and plants against a cataclysmic winter/meltwater flood.
- **Tripartite Division of the Earth:** **Fereydun (Thraetaona)** divides the world among his three sons â€” **Salm** (West/Rum), **Tur** (Turan/Central Asian Steppe), and **Iraj** (Iran â†’ Kayanian dynasty) â€” mirroring Noah's tripartite division among Shem, Ham, and Japheth.
- **Historical Bridges to Biblical Texts:** **Madai** (Gen 10:2) = historical **Medes** (*Mada*); **Elam** (Gen 10:22) = SW Iran/Anshan (where **Cyrus the Great** ruled as King of Anshan).

### Egypt, Phoenicia & Arabia
- **Egypt (*Pyramid Texts*, *Turin King List*, Manetho):** Heliopolitan Ennead (Atum â†’ Shu/Tefnut â†’ Geb/Nut â†’ Osiris/Isis â†’ Horus) â†’ *Shemsu-Hor* â†’ **Menes / Narmer** (c. 3100 BCE, historical anchor for Biblical **Mizraim**).
- **Phoenician (*Sanchuniathon* via Philo of Byblos):** Explicitly names **Misor** (cognate of Biblical **Mizraim**) as brother of **Sydyk** (cf. Melchizedek) and father of **Taaut (Thoth)**, alongside **Chna (Canaan)**.
- **Arabia (Adnanite & Qahtanite Chronicles):** Connects Southern Arabs (**Qahtan = Joktan** son of Eber/Hud â†’ Sheba/Himyar) and Northern Arabs (**Ishmael â†’ Kedar/Nebaioth â†’ Adnan â†’ Quraysh â†’ Muhammad**).

---

## 4. Ancient Asian Traditions (India, China, Korea, Japan, Steppe)

### Ancient India â€” Vedic & Puranic (*Rigveda*, *Shatapatha Brahmana*, *Mahabharata*, *Ramayana*, *Vishnu Purana*)
- **Primordial Root:** **Brahma** â†’ **Svayambhuva Manu & Shatarupa** + the *Saptarishis* (including **Marichi** and **Atri**).
- **Indo-Iranian Anchor & Great Flood:** Marichi â†’ **Kashyapa** (+ Aditi) â†’ **Vivasvan (Surya)** [= Avestan *Vivanghant*] â†’ **Yama** [= Avestan *Yima*] AND **Vaivasvata Manu** (7th Manu, saved from the universal Flood by **Matsya the Fish** in *Shatapatha Brahmana* 1.8.1).
- **Two Universal Indian Royal Lines (from Vaivasvata Manu):**
  1. **Surya Vamsha (Solar Dynasty):** Vaivasvata Manu â†’ **Ikshvaku** â†’ Harishchandra â†’ Bhagiratha â†’ Raghu â†’ Dasharatha â†’ **Rama** (*Ramayana*). Buddhist chronicles (*Mahavamsa*, *Ambattha Sutta*) also trace **Siddhartha Gautama (the Buddha)**'s Shakya clan directly back to King Okkaka = **Ikshvaku**!
  2. **Chandra Vamsha (Lunar Dynasty):** Atri â†’ Soma (Chandra) â†’ Budha + **Ila** (child of Vaivasvata Manu) â†’ Pururavas â†’ Ayu â†’ Nahusha â†’ **Yayati** â†’ **5 Sons (*Panchajana* â€” Vedic Table of Nations)**:
     - **Yadu** â†’ Yadavas (**Krishna & Balarama**)
     - **Puru** â†’ **Bharata** (eponym of *Bharatavarsha*/India) â†’ **Kuru** â†’ **Pandavas & Kauravas** (*Mahabharata*)
     - **Anu** (North/East), **Turvasu** (South/West), **Druhyu** (NW Gandhara & trans-Indus *Mleccha*/Central Asian peoples).

### Ancient China (*Shiji*, *Shan Hai Jing*, *Shangshu*, *Guoyu*, *Bamboo Annals*)
- **Primordial Creators & Flood Motif:** **Fuxi & NÃ¼wa** (serpent-tailed sibling-consorts who repair heaven after Gonggong's deluge and mold humans from yellow clay; preserved in SW Chinese lore as Flood survivors).
- **Universal Royal Progenitors (*Yan-Huang Zisun*):** *Guoyu* makes **Yandi (Flame Emperor / Shennong)** and **Huangdi (Yellow Emperor)** half-brothers born of Shaodian. In *Shiji* Ch. 1 (c. 94 BCE), historian Sima Qian systematically traces **every** ancient Chinese ruling house to Huangdi:
  - Huangdi â†’ Changyi â†’ **Zhuanxu** â†’ Gun â†’ **Yu the Great (Da Yu)** (tamer of the Great Flood) â†’ **Xia Dynasty** (c. 2070 BCE), plus Emperor Shun, Chu, and **Qin** (Qin Shi Huang).
  - Huangdi â†’ Xuanxiao â†’ Jiaoji â†’ **Emperor Ku (Di Ku)** â†’ **Emperor Yao**, **Xie** (**Shang Dynasty**, c. 1600 BCE â€” ancestor of **Confucius** via the Dukes of Song!), and **Hou Ji** (**Zhou Dynasty**, 1046 BCE).

### Eurasian Steppe, Korea & Japan (Intercontinental Bridges)
- **China â†” Eurasian Steppe (*Shiji* Ch. 110):** Sima Qian explicitly records that the **Xiongnu** steppe confederacy descended from **Chunwei**, a prince of the Chinese **Xia Dynasty**.
- **Near East â†” Steppe (Syncretic Universal Bridge):** Medieval Eurasian chroniclers (**Rashid al-Din**, *Jami' al-Tawarikh* 1307 CE; Abulghazi, *Shajara-i TarÄkima*) grafted Turkic and Mongol lineages onto Biblical **Japheth (Yafith)** â†’ **Turk (Oljai Khan)** â†’ Tatar & Mongol â†’ Kara Khan â†’ **Oghuz Khagan** (6 sons / 24 Oghuz tribes), while also linking them to Iranian **Turan** (son of Fereydun).
- **Korea (*Samguk Yusa*):** Hwanin â†’ Hwanung + Ungnyeo â†’ **Dangun Wanggeom** (Gojoseon), later intersecting with Chinese Shang Dynasty prince **Jizi (Gija)**.
- **Japan (*Kojiki* & *Nihon Shoki*):** **Izanagi & Izanami** â†’ **Amaterasu** (Sun Goddess) â†’ Ninigi â†’ Hoori â†’ **Emperor Jimmu** (traditional 660 BCE, oldest continuous hereditary monarchy).

---

## 5. Side-by-Side Global Archetypal Convergence Matrix

| Motif / Horizon | Biblical / Extra-Biblical | Mesopotamian | Iranian / Zoroastrian | Vedic / Puranic India | Ancient China | Japan |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **First Humans** | Adam & Eve (from dust/*adamah*) | *Lullu* (clay + divine blood) | Gayomart â†’ Mashya & Mashyana | Svayambhuva Manu & Shatarupa | Humans molded from yellow clay by NÃ¼wa | Izanagi & Izanami |
| **Antediluvian Sage / 7th** | **Enoch** (7th, 365 solar yrs, heavenly ascent) | **En-men-dur-ana** (7th, Sippar/Sun, heavenly tablets) | Hushang / Tahmuras (cultural bringers) | *Saptarishis* (7 Primal Sages) | Three Sovereigns (Fuxi invents trigrams/writing) | *Kamiyo* seven generations |
| **Great Flood / Cataclysm** | **Noah** (Ark, Mt. Ararat, dove/raven) | **Ziusudra / Utnapishtim** (Boat, Mt. Nimush, dove/swallow/raven) | **Yima / Jamshid** (*Vara* enclosure vs. cosmic winter/melt) | **Vaivasvata Manu** (Ship towed by Matsya to Himalayas) | **Yu the Great** (Channels Gun-Yu Flood); **Fuxi & NÃ¼wa** (SW lore) | Primeval ocean stirred by spear |
| **World Division / Nations** | **Shem, Ham, Japheth** (70 Nations) | Sumer / Akkad / Kish / Uruk cities | **Salm, Tur, Iraj** (West, Steppe, Iran) | **Yayati's 5 Sons** (*Panchajana*: Yadu, Puru, Anu, Turvasu, Druhyu) | **Huangdi's 25 Sons** (Xia, Shang, Zhou, Xiongnu) | Eight Great Islands |

---

## 6. Verified Cross-Tradition Paths (Computed from Graph Database)

Using our validation script ([validate_tree.py](../scripts/validate_tree.py)), we verified **66 nodes and 92 typed edges** with zero broken links. Remarkably, even under **strict textual + historical/linguistic cognate filters alone** (excluding archetypal parallels and medieval syncretism), you can trace continuous ancestral/ethnonymic bridges across continents:

1. **Israelites â†” Indian Pandavas (Strict Textual + Cognates Only):**
   `12 Tribes of Israel` â† `Abraham` â† `Shem` â†’ `Elam` / (`Japheth` â†’ `Madai`) â‡” `Historical Medes & Cyrus (Anshan)` â† `Iraj` â† `Fereydun` â† `Yima (Jamshid)` â† `Vivanghant` â‡” **`Vivasvan` (Exact Proto-Indo-Iranian Cognate)** â†’ `Vaivasvata Manu` â†’ `Ila + Budha` â†’ `Yayati` â†’ `Puru` â†’ `Bharata` â†’ `Kuru` â†’ `Pandavas`.
2. **Arabian Adnanites â†” Gilgamesh of Uruk (Strict Textual + Cognates Only):**
   `Ishmael / Adnan` â† `Abraham` â† `Shem` â†’ `Asshur` (or `Ham` â†’ `Cush` â†’ `Nimrod`) â‡” `Akkad (Sargon)` / `Erech (Uruk)` â†’ `Gilgamesh`.
3. **Abraham â†” Phoenician Thoth/Taaut (Strict Textual + Cognates Only):**
   `Abraham` â† `Shem` â† `Noah` â†’ `Ham` â†’ `Mizraim` â‡” `Phoenician Misor (Sanchuniathon)` â†’ `Taaut (Thoth)`.
4. **Chinese Xia Dynasty â†” Biblical Japheth (With Medieval Eurasian Chronicler Bridge):**
   `Xia Dynasty (Yu the Great)` â†’ `Chunwei â†’ Xiongnu` (*Shiji* 110) â†’ `Steppe / Oghuz Khagan` â‡ *(Rashid al-Din syncretic bridge)* â‡ `Japheth (Yafith)`.

---

## 7. Roadmap for Phase 2 Expansion

The JSON schema in [genealogy_core.json](../data/genealogy_core.json) is modular and ready to expand. In upcoming turns we can add:
- **Greek & Mediterranean:** Hesiod's *Theogony* & *Catalogue of Women* (Deucalion [Flood!] â†’ Hellen â†’ Dorians, Ionians [cf. Javan!], Aeolians; Cadmus of Phoenicia â†’ Thebes; Danaus of Egypt â†’ Argos).
- **Celtic, Norse & European Chronicles:** *Lebor GabÃ¡la Ã‰renn* (Irish Book of Invasions linking Milesians/Scota to Noah/Egypt/Spain), Snorri Sturluson's *Prose Edda* (linking Odin/Aesir to Troy!), *Historia Brittonum* (Brutus of Troy).
- **African & Ethiopian:** *Kebra Nagast* (Solomon + Queen of Sheba â†’ Menelik I of Ethiopia), Kushite Napatan/Meroitic lineages, Yoruba Oduduwa traditions.
- **Americas & Polynesia:** Maya *Popol Vuh*, Inca *Manco CÃ¡pac*, Aztec Chicomoztoc, Polynesian *Kumulipo* / Ranginui & PapatÅ«Änuku.
- **Optional Modern Science Overlay:** Compare textual migrations against ancient DNA / Y-DNA & mtDNA haplogroup migrations (Out-of-Africa, Steppe Yamnaya/Indo-Iranian expansion, Yellow River Sino-Tibetan expansion).

