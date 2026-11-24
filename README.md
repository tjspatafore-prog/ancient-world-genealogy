# Ancient World Genealogy Atlas

An exhaustive, modular, comparative worldwide ancient genealogy tree and graph database accounting for every individual across ancient religious, extra-biblical, Near Eastern, Egyptian, Asian, and Steppe texts.

## Current Coverage (Phase 4 — 561 Individuals • 661 Typed Links across 8 Modules)
- **Module 1 — Antediluvian Era (36 nodes):** Full Sethite & Cainite lineages, matriarchs from *Book of Jubilees*, all extra-biblical children of Kenan, Enoch, and Methuselah from *Book of Jasher*, plus *1 Enoch* Watchers & *Qumran Book of Giants* (Ohya, Hahya, Mahaway, Gilgamesh).
- **Module 2 — Complete Table of Nations (119 nodes):** Every son and grandson of **Japheth**, **Ham**, and **Shem** in Genesis 10 + *Jubilees 8–9* + ALL additional children in *Book of Jasher Ch. 7 & 10* (Togarmah's 10 sons, Nimrod's son *Mardon*, all 13 sons of Joktan/Qahtan, etc.).
- **Module 3 — Complete Descendants of Abraham & Extended House of Terah (169 nodes):** Haran/Lot, Nahor II's 12 children, Ishmael's 12 princes, Keturah's 6 sons + all Gen 25 & *Jasher 25* grandchildren, Esau + *Jasher* Zepho → Janeus/Italy, and Jacob's 12 tribes + all ~50 Gen 46 grandchildren → Moses, David, Solomon, and Menelik I.
- **Module 4 — Exhaustive Ancient Egyptian Dynasties (36 nodes):** Heliopolitan Ennead & Memphite Ptah (*Na-Ptah* = Naphtuhim!), Horus & *Shemsu-Hor*, **Thoth / Hermes / King Saurid** (↔ Enoch) → Priest **Philemon** on Noah's Ark, Coptic-Arabic **Baysar → Misrayim → Qift (Copts)**, *Jasher* Pharaohs (**Rikayon, Melol, Adikam**), Dynasties 1–6 (Narmer/Menes, Djoser & **Imhotep** [7-year famine ↔ Joseph], Sneferu, Khufu, Khafre, Menkaure, Unas, Pepi II), Middle Kingdom & **15th Dynasty Hyksos** (Salitis, Apepi), New Kingdom Dynasties 18–22 (Ahmose I, Hatshepsut, Thutmose III, Amenhotep III & Tiye, **Akhenaten & Nefertiti**, Tutankhamun, **Ramesses II**, **Merneptah** [Israel Stele 1208 BCE!], Ramesses III [Philistines/Peleset], **Shoshenq I** [Biblical Shishak]), Ptolemy II / Manetho (**Osarseph** ↔ Moses) → Cleopatra VII, plus Phoenician *Sanchuniathon*.
- **Module 5 — Exhaustive Mesopotamian Genealogy (75 nodes):** Full *Enuma Elish* theogony, Adapa (↔ Adam), ALL 10 Antediluvian Kings & 7th sage Utuabzu (↔ Enoch), ALL 23 Kish I kings, ALL 12 Uruk/Erech kings (Enmerkar, Lugalbanda, Gilgamesh), Ur I, Akkad (Sargon, Enheduanna, Naram-Sin), ALL 5 Ur III kings (Ur of the Chaldees), Hammurabi, and Assyria.
- **Module 6 — Exhaustive Iranian & Zoroastrian Genealogy (70 nodes):** Gayomart → Mashya & Mashyana → *Bundahishn Ch. 14* Table of Nations, full Pishdadian Dynasty (Vivanghant = Vivasvan, Yima = Yama, Athwya = Aptya, Fereydun = Trita → Salm, Tur, Iraj), Turanian House (Afrasiab), Sistan Heroes (Zal, Rudabeh, Rostam, Sohrab), full Kayanian Dynasty (Kay Kavus = Kavi Ushanas, Kay Khosrow, Goshtasp), **Prophet Zarathustra's full family**, plus historical Medes (*Madai*) and Achaemenids (Cyrus the Great, Darius I, Xerxes I/Ahasuerus, Artaxerxes I).
- **Module 7 — Vedic/Puranic India, China, Korea, Japan & Steppe (27 nodes):** Ready for Phase 5 person-by-person expansion!
- **Module 8 — Exhaustive African, Cushite/Nubian & Ethiopian Genealogies (29 nodes + Menelik I):** Kingdom of Kush 25th Dynasty (Alara, Kashta, Piye, Shabaka, **Taharqa = Biblical Tirhakah** [2 Kings 19:9!], Tantamani), Meroitic **Kandakes** (Amanirenas, **Amanitore = Biblical Candace** [Acts 8:27!]), *Jasher* Cushite King **Kikanos & Queen Adoniah**, Ethiopian *Tarika Nagast* & *Kebra Nagast* (**Cush → Ityopis → Aksumawi → Angabo → Queen Makeda of Sheba → Menelik I → Ezana → Lalibela [Zagwe] → Yekuno Amlak → Haile Selassie I**), Yoruba **Oduduwa → Okanbi → 7 Crowned Monarchs** (Oranmiyan → Oyo & Eweka I of Benin), Hausa **Bayajidda → Bawo → 7 Hausa Bakwai**, Mali **Sundiata Keita → Mansa Musa**, North African **Amazigh (Mazigh → Meshwesh/Queen Dihya)**, and East African **Kintu & Nambi / Gikuyu & Mumbi**.

## Features
- **Auto-Layout Layered Tree** with clickable **`+N` unfold badges** and one-click **Landmarks / Expand All (370)** toggle
- **Focus Family Tree Mode** — isolate any individual's full ancestral chain, all descendants, and cross-tradition bridges (e.g., *Abraham's Full Tree*, *Noah's Table of Nations*, *Moses & Egypt*)
- **Searchable People Directory** — search all 370 individuals by name, Egyptian/alternate name, or text citation (`Jasher 7`, `Jasher 25`, `1 Enoch`)
- **Common Ancestor / Cross-Tradition Pathfinder** — trace shortest paths across any two people under selectable provenance tiers

## Rebuild & Validate
```bash
python scripts/build_dataset.py
python scripts/validate_tree.py
```
