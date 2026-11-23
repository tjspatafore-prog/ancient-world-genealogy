# Ancient World Genealogy Atlas

An exhaustive, modular, comparative worldwide ancient genealogy tree and graph database accounting for every individual across ancient religious, extra-biblical, Near Eastern, Egyptian, Asian, and Steppe texts.

## Current Coverage (Phase 2 — 370 Individuals • 421 Typed Links)
- **Module 1 — Antediluvian Era (36 nodes):** Full Sethite & Cainite lineages, matriarchs from *Book of Jubilees*, all extra-biblical children of Kenan (Enan, Mered, Adah, Zillah), Enoch (Methuselah, Elisha, Elimelech, Melca, Naamah), and Methuselah (Eliakim) from *Book of Jasher*, plus *1 Enoch* Watchers & *Qumran Book of Giants* (Ohya, Hahya, Mahaway, Gilgamesh).
- **Module 2 — Complete Table of Nations (119 nodes):** Every son and grandson of **Japheth**, **Ham**, and **Shem** in Genesis 10 + *Jubilees 8–9* + ALL additional children in *Book of Jasher Ch. 7 & 10* (including Togarmah's 10 sons such as *Tarki*/*Buzar*/*Balgar*, Nimrod's son *Mardon*, all 13 sons of Joktan/Qahtan, Phut's 4 sons, Elam's *Shushan*, etc.).
- **Module 3 — Complete Descendants of Abraham & Extended House of Terah (169 nodes):**
  - **Haran** → Lot (Moab & Ammon), Milcah, Sarah/Iscah
  - **Nahor II** → all 12 children (including Bethuel → Rebekah & Laban)
  - **Ishmael** → all 12 princes (Nebaioth, Kedar, Adbeel, etc. → Adnanite Arabs) + Mahalath
  - **Keturah's 6 Sons** → Zimran, Jokshan, Medan, Midian, Ishbak, Shuah + ALL Genesis 25 & *Book of Jasher 25* grandchildren (including Bildad, Jethro/Zipporah, Sheba, Dedan)
  - **Esau (Edom)** → all 5 sons, all grandchildren (Eliphaz, Amalek, Teman, Reuel) + *Jasher 57–64* **Zepho → Janeus** bridge to Kittim/Italy
  - **Jacob (Israel)** → all 12 sons, Dinah (and *Jasher 49* Asenath link), all ~50 Genesis 46 grandchildren, full Levitical line to **Moses** & Aaron, and Judahite line via Boaz (+ Ruth of Moab) → David → **Solomon** → **Menelik I** of Ethiopia (*Kebra Nagast*)
- **Module 4 — Egyptian Cross-Traditions, Mesopotamia, Phoenicia & Iran (20 nodes):**
  - Egyptian & Greco-Egyptian cross-identifications: **Enoch ↔ Thoth / Hermes / King Saurid**, **Noah ↔ Osiris / Nun**, **Joseph (Zaphenath-Paneah) ↔ Imhotep**, **Moses ↔ Osarseph (Manetho) / Musaeus (Artapanus) / King of Cush with Queen Adoniah (*Jasher 72–76*)**, **Mizraim ↔ Phoenician Misor / Menes / Baysar**
  - *Sumerian King List* (Enmeduranki, Ziusudra, Gilgamesh, Sargon), *Avesta* / *Shahnameh* (Gayomart, Vivanghant, Yima/Jamshid, Fereydun → Salm, Tur, Iraj)
- **Module 5 — Vedic/Puranic India, China, Korea, Japan & Steppe (26 nodes):**
  - *Rigveda* / *Puranas* (Vivasvan = Vivanghant, Yama = Yima, Vaivasvata Manu, Surya Vamsha → Rama & Buddha, Chandra Vamsha → Yayati's 5 sons individualized → Bharata/Pandavas)
  - *Shiji* (Fuxi & Nüwa, Yandi, Huangdi, Zhuanxu, Yu the Great/Xia, Shang, Zhou, Chunwei → Xiongnu), *Kojiki* (Amaterasu → Jimmu), *Samguk Yusa* (Dangun), *Jami' al-Tawarikh* (Japheth → Oghuz Khagan)

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
