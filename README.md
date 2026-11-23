# Ancient World Genealogy Atlas

An interactive, comparative worldwide ancient genealogy tree and structured graph database uniting ancestral lineages across ancient religious, mythic, and historical texts.

## Traditions Covered (Phase 1)
- **Biblical & Extra-Biblical:** Genesis, 1 Chronicles, *Book of Jubilees*, *1 Enoch*, *Book of Jasher (Sefer haYashar)*, *Qumran Book of Giants*, *Genesis Apocryphon*
- **Mesopotamian:** *Sumerian King List*, *Enuma Elish*, *Atrahasis*, *Epic of Gilgamesh*, Berossus's *Babyloniaca*
- **Iranian / Zoroastrian:** *Avesta*, *Bundahishn*, Ferdowsi's *Shahnameh*
- **Egyptian, Phoenician & Arabian:** Heliopolitan Ennead, *Turin King List*, *Sanchuniathon* (Philo of Byblos), Adnanite & Qahtanite Chronicles (*al-Tabari*, *Ibn Ishaq*)
- **Vedic & Puranic Indian:** *Rigveda*, *Shatapatha Brahmana*, *Mahabharata*, *Ramayana*, *Vishnu Purana*, Pali Buddhist chronicles
- **Ancient East Asian & Steppe:** Sima Qian's *Shiji*, *Shan Hai Jing*, *Shangshu*, *Bamboo Annals*, *Kojiki*, *Nihon Shoki*, *Samguk Yusa*, *Oghuzname*, Rashid al-Din's *Jami' al-Tawarikh*

## 5-Tier Provenance Taxonomy
Every connection in the graph is explicitly tagged so direct canonical descent is never conflated with comparative parallels or medieval syncretism:
1. `direct` — Explicit parent-child descent inside primary texts
2. `expansion` — Matriarchs, intermediate links, or migrations from extra-biblical/secondary chronicles
3. `cognate` — Linguistically or historically attested cross-tradition bridges (e.g., Vedic *Vivasvan/Yama* = Avestan *Vivanghant/Yima*; Biblical *Madai* = Medes; *Mizraim* = Phoenician *Misor*/Egypt)
4. `parallel` — Independent structural/archetypal parallels (Great Flood survivors, 7th antediluvian sage, tripartite world division)
5. `syncretic` — Classical/medieval chronicler bridges grafting distant nations onto one universal tree

## Repository Structure
- `index.html` — Zero-build, Vercel-ready interactive SVG World Genealogy Explorer (pan/zoom, search, 5-tier provenance filters, dark/light theme, and Common Ancestor / Bridge Pathfinder)
- `data/genealogy_core.json` — Extensible graph dataset (66 nodes, 92 typed edges)
- `docs/world_genealogy_compendium.md` — Full comparative reference, matriarch tables, Mermaid diagrams, and Phase 2 roadmap
- `scripts/validate_tree.py` — Graph validator and shortest-path ancestry tracer

## Deploying to Vercel
This project is a zero-build static web application (`index.html`). Import this repository into Vercel with the default framework preset (**Other / Static**) and leave the Build Command empty — it will deploy directly to Vercel's Edge Network.

## Local Validation
```bash
python scripts/validate_tree.py
```
