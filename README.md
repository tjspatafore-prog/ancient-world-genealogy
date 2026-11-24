# Ancient World Genealogy Atlas

An exhaustive, modular, comparative worldwide ancient genealogy tree and graph database accounting for every individual across ancient religious, extra-biblical, Near Eastern, Egyptian, Asian, and Steppe texts.

## Current Coverage (Phase 10 — v10.0: 766 Nodes • 993 Typed Links across 15 Modules)
- **Modules 1–13 (Complete Global Textual & Historical Atlas — 691 nodes):** Biblical & Extra-Biblical (*Genesis, 1 Chronicles, Jubilees, 1 Enoch, Book of Jasher, Qumran*), Egyptian Dynasties (1–31 + Coptic-Arabic & *Jasher*), Mesopotamian (*Enuma Elish, Sumerian King List, Kish I, Uruk I, Akkad, Ur III, Babylon, Assyria*), Iranian/Zoroastrian (*Avesta, Bundahishn, Shahnameh, Zarathustra, Medes, Achaemenids*), Vedic & Puranic India (*Surya Vamsha, Chandra Vamsha, Rama, Krishna, Pandavas, Buddha, Ashoka*), African/Cushite/Ethiopian (Kush 25th Dyn, Meroe, *Kebra Nagast*, Yoruba, Hausa, Mali, Amazigh, Buganda/Kikuyu), Greek & Mediterranean (*Hesiod, Homer, Troy, Rome, Julius Caesar/Augustus, Carthage, Etruscans*), Ancient China (*Shiji*, Xia/Shang/Zhou/Qin/Chu/Confucius & Steppe Xiongnu/Oghuz), Korea & Japan (*Samguk Yusa, Kojiki, Nihon Shoki*), Celtic/Norse/European (*Prose Edda, Tacitus, Lebor Gabála Érenn, Historia Brittonum*, Slavic), and Americas & Polynesia (*Popol Vuh*, Aztec, Inca, Haudenosaunee, Diné, Lakota, Hawaiian *Kumulipo*, Māori *Whakapapa*, *Tuʻi Tonga*, Rapa Nui).
- **Module 14 — Modern Human Archaeogenetics Overlay (15 nodes, 40 links):** Scientific Y-DNA & mtDNA haplogroup tree isolated on its own toggleable `genetic` provenance tier.
- **Module 15 — Exhaustive Adam2Jesus Biblical Expansion (60 nodes, 94 links):** Seir the Horite, Melchizedek, Job & his friends, Joshua & Caleb, Zelophehad's 5 daughters, Bezalel, **ALL 12 Judges** + Eli & Samuel, House of Saul, **ALL 20 Monarchs of Judah**, **ALL 19 Kings of Northern Israel** (including Ahab & Jezebel ↔ Ethbaal of Sidon/Dido of Carthage!), complete **Aaron → Zadok → Ezra → John the Baptist** High Priestly line, Major & Minor Prophets, **Queen Esther, Mordecai & Haman**, complete **Matthew 1 & Luke 3 Dual Lineages to Jesus**, **Herodian Dynasty** (Edom/Idumea → Rome), Apostle Paul, plus Nebuchadnezzar, Sennacherib, Esarhaddon, Ashurbanipal, Hiram of Tyre, King Mesha of Moab, and Pharaoh Neco II!

## Four Interactive Views
1. **Tree Map** — Auto-layout multi-tradition genealogy with `+N` unfold pills, Focus Family Tree mode, and Common Ancestor / Bridge Pathfinder
2. **World Map** — Interactive global migration & bridge map plotting 29 civilization/DNA hubs and color-coded arcs (Y-DNA/mtDNA, Historical Cognates, Chronicler Bridges)
3. **Timeline** — Deep-Time Comparative Timeline stretching from 300,000 BCE DNA roots through every ancient mythic & historical epoch to 1500 CE
4. **Directory** — Instant searchable table across all 706 individuals, alternate/Egyptian names, sources, and DNA haplogroups

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
