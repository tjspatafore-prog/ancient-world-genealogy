# Ancient World Genealogy Atlas

An exhaustive, modular, comparative worldwide ancient genealogy tree and graph database accounting for every individual across ancient religious, extra-biblical, Near Eastern, Egyptian, Asian, and Steppe texts.

## Current Coverage (Phase 6 — 634 Individuals • 767 Typed Links across 11 Modules)
- **Module 1 — Antediluvian Era (36 nodes):** Full Sethite & Cainite lineages, *Jubilees* matriarchs, *Book of Jasher* extra-biblical children, *1 Enoch* Watchers & *Qumran Book of Giants*.
- **Module 2 — Complete Table of Nations (119 nodes):** Every son and grandson of Japheth, Ham, and Shem in Genesis 10 + *Jubilees 8–9* + ALL *Book of Jasher Ch. 7 & 10* children.
- **Module 3 — Complete Descendants of Abraham & Extended House of Terah (169 nodes):** Haran/Lot, Nahor II's 12, Ishmael's 12, Keturah's 6 + all Gen 25/*Jasher 25* grandchildren, Esau + *Jasher* Zepho → Janeus, and Jacob's 12 tribes + all ~50 Gen 46 grandchildren → Moses, David, Solomon & Menelik I.
- **Module 4 — Exhaustive Ancient Egyptian Dynasties (36 nodes):** Ennead, Ptah (*Na-Ptah* = Naphtuhim), Thoth/Saurid (↔ Enoch), Coptic-Arabic Baysar/Misrayim, *Jasher* Pharaohs, Dynasties 1–22 (Narmer, Imhotep, Khufu, Hyksos, Hatshepsut, Akhenaten, Tutankhamun, Ramesses II, Merneptah Israel Stele, Shoshenq I/Shishak), Ptolemies/Cleopatra, and Osarseph/Musaeus.
- **Module 5 — Exhaustive Mesopotamian Genealogy (75 nodes):** *Enuma Elish*, Adapa, ALL 10 Antediluvian Kings & 7th sage Utuabzu, ALL 23 Kish I kings, ALL 12 Uruk/Erech kings (Enmerkar, Gilgamesh), Akkad (Sargon, Enheduanna, Naram-Sin), ALL 5 Ur III kings, Hammurabi, and Assyria.
- **Module 6 — Exhaustive Iranian & Zoroastrian Genealogy (70 nodes):** Gayomart → *Bundahishn Ch. 14* Table of Nations, full Pishdadian, Turanian, Sistan (Zal/Rudabeh/Rostam), and Kayanian dynasties, **Prophet Zarathustra's full family**, plus historical Medes (*Madai*) and Achaemenids (Cyrus, Darius I, Xerxes I/Ahasuerus).
- **Module 7 — Vedic & Puranic India (14 nodes):** Core Indo-Iranian cognates, Vaivasvata Manu, Solar & Lunar Dynasties (ready for Phase 7 deep expansion!).
- **Module 8 — Exhaustive African, Cushite/Nubian & Ethiopian Genealogies (29 nodes + Menelik I):** Kush 25th Dynasty (Piye, **Taharqa = Tirhakah**), Meroitic **Kandakes** (**Amanitore = Candace**), Ethiopian *Tarika Nagast* & *Kebra Nagast*, Yoruba **Oduduwa**, Hausa **Bayajidda**, Mali **Sundiata/Mansa Musa**, Amazigh **Mazigh**, and East African **Kintu & Gikuyu**.
- **Module 9 — Exhaustive Greek & Mediterranean Genealogy (43 nodes):** Hesiod's *Theogony*, **Deucalion & Pyrrha**, **Hellen → Ion (= Javan)**, Afro-Asiatic ↔ Greek bridge (**Inachus → Io → Epaphus → Libya → Agenor/Cadmus/Europa/Minos & Belus/Aegyptus/Danaus/Cepheus/Perseus → Perses & Heracles → Sparta/Alexander**), **Troy → Aeneas → Romulus & Remus**, **Queen Dido (Carthage)**, and **Lydus/Tyrrhenus**.
- **Module 10 — Exhaustive Ancient Chinese & Steppe Genealogy (28 nodes):** `Pangu`, `Fuxi & Nüwa`, `Shaodian`, `Yandi/Shennong` (Jiang clan → Chiyou & Jiang Ziya), `Huangdi (Yellow Emperor)` → `Shaohao → Emperor Ku` (`Yao → Han`, `Xie → Shang → Wu Ding & Fu Hao → Weizi Qi → Confucius & Jizi/Korea`, `Hou Ji → King Wen & Wu of Zhou → Duke of Zhou & King Mu`), AND `Changyi → Zhuanxu` (`Gun → Yu the Great/Xia → Shao Kang/Yue`, `Emperor Shun`, `Boyi → Qin Shi Huang`, `Zhurong → Pengzu [800 yrs] → State of Chu/Qu Yuan`), plus `Chunwei → Modu Chanyu (Xiongnu)` & `Oghuz Khagan → 6 Sons (24 Oghuz Tribes)`!
- **Module 11 — Exhaustive Ancient Korean & Japanese Genealogy (15 nodes):** Korea (`Hwanin → Hwanung + Ungnyeo → Dangun [Gojoseon]`, `Jumong [Goguryeo]`, `Onjo [Baekje ↔ Japan]`, `Park/Seok/Kim [Silla]`, and `King Suro of Gaya + Queen Heo Hwang-ok of Ayuta/Ayodhya, India!`) and Japan (`Kotoamatsukami → Izanagi & Izanami → Amaterasu, Tsukuyomi & Susanoo/Okuninushi → Ninigi → Hoori → Emperor Jimmu → Sujin → Yamato Takeru → Empress Jingu → Emperor Ojin → Prince Shotoku`)!

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
