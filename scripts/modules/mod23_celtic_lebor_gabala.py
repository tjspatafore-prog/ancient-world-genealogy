"""
Module 23: Complete Irish Lebor Gabála Érenn (Part IV: Fir Bolg & Tuatha Dé Danann)
from R.A.S. Macalister (Irish Texts Society Vol. 41, leborgablare04macauoft.pdf).

Covers:
1. Universal Irish Pedigree: Noah -> Japheth -> Magog -> Fathacht -> Sera -> Agnomain -> Nemed
2. Complete Invasion Sequence: Cessair -> Partholón -> Nemed -> Fir Bolg -> Tuatha Dé Danann -> Milesians
3. Complete Fir Bolg Royal House: Dela's 5 Sons (Sláine, Gann, Sengann, Genann, Rudraige + 5 Wives) & ALL 9 Fir Bolg Kings down to Eochu mac Eirc & Queen Tailtiu
4. Complete Tuatha Dé Danann Pantheon & Kings: Tat -> Alldui -> Nuadu Airgetlám, Midir, Nét ->
   Esarg (Goibniu, Creidne, Luichtne, Dian Cécht -> Cian + Ethniu dau. of Balor -> Lugh Lámfada!) &
   Delbaeth -> Elada -> The Dagda (Eochu Ollathair -> Óengus Mac Óc, Brigit, Cermait -> Mac Cuill/Mac Cécht/Mac Gréine),
   Ogma (-> Delbaeth -> Fiachna -> Ériu, Banba, Fódla + Brian/Iuchar/Iucharba) & Bres (Fomorian bridge).
"""

from . import N, E, add_chain, add_roster


def build_module():
    nodes, edges = [], []

    nodes += [
        N("cel_nemed_pedigree", "Irish Universal Pedigree: Noah → Japheth → Magog → Fathacht → Sera → Agnomain → Nemed (Ancestor of Fir Bolg, Britons & Tuatha Dé Danann!)", "europe_norse", 8, "Mythic Irish Settlements (Lebor Gabála Érenn R1 ¶316, p. 127)",
          "Bridge Uniting Genesis 10 (Magog) to Ireland's Pre-Milesian Peoples", ["Lebor Gabála Érenn Part IV (Macalister ¶280, ¶316, pp. 9, 127)"],
          "Macalister R1 ¶316 traces Nemed directly from Noah -> Japheth -> Magog -> Fathacht -> Braimend -> Esru -> Sru -> Sera -> Tat -> Pamp -> Agnomain -> Nemed! Nemed's surviving branches produced the Fir Bolg (via Starn -> Semeon -> Dela), the Britons (Britán Máel), and the Tuatha Dé Danann (via Iarbonel the Soothsayer -> Bethach -> Tat)!",
          ["Nemed mac Agnomain", "Cessair", "Partholón", "Iarbonel Fatha", "Semeon"], major=True),
        N("cel_fir_bolg_kings", "Complete Fir Bolg Dynasty (Dela's 5 Sons & All 9 Kings): Sláine, Rudraige, Gann, Genann, Sengann → Fiacha → Rindail → Fodbgenid → Eochu mac Eirc (+ Queen Tailtiu)", "europe_norse", 9, "Pre-Tuatha Dé Ireland (Lebor Gabála Part IV Sect. VI, pp. 7-21)",
          "First Organizers of Ireland's Five Provinces & Tailteann Games", ["Lebor Gabála Érenn Part IV (Macalister ¶278-289, pp. 7-21)"],
          "Dela's 5 sons & 5 wives (Sláine+Fuat, Gann+Etar, Sengann+Anust, Genann+Cnucha, Rudraige+Liber) divided Ireland into its 5 provinces (Cóiceda). Last king Eochu mac Eirc married Spanish princess Tailtiu (foster-mother of Lugh!) before falling at 1st Battle of Mag Tuired.",
          ["Dela", "Sláine", "Eochu mac Eirc", "Queen Tailtiu"], major=True),
        N("cel_tdd_nuadu_dian_cecht", "Tuatha Dé Danann Line A & B1: Nuadu Airgetlám ('Silver Hand'), Midir & Esarg's 4 Sons (Goibniu, Creidne, Luichtne & Dian Cécht → Cian + Ethniu → Lugh Lámfada!)", "europe_norse", 10, "Battle of Mag Tuired (Lebor Gabála Part IV Sect. VII, pp. 113-159)",
          "Silver-Handed King Nuadu, Divine Craftsmen & Hero-King Lugh Lámfada", ["Lebor Gabála Érenn Part IV (Macalister ¶310-316, ¶341, pp. 113-159)"],
          "Nuadu Airgetlám ruled 27 yrs after healer Dian Cécht & Creidne forged his silver hand. Dian Cécht's son Cian married Ethniu (daughter of Fomorian King Balor of the Evil Eye!), fathering Lugh Lámfada ('Long-Arm', master of all arts!), who slew grandfather Balor at 2nd Mag Tuired and reigned 40 yrs!",
          ["Nuadu Airgetlám", "Dian Cécht", "Goibniu", "Balor of the Evil Eye", "Lugh Lámfada"], major=True),
        N("cel_tdd_dagda_ogma_eriu", "Tuatha Dé Danann Line B2 (Elada's Sons): The Dagda (Eochu Ollathair → Óengus Mac Óc, Brigit & Cermait → Mac Cuill/Mac Cécht/Mac Gréine) & Ogma (→ Delbaeth → Ériu, Banba, Fódla & 3 Sons of Danu)", "europe_norse", 10, "Tuatha Dé Danann Golden Age (Lebor Gabála Part IV Sect. VII, pp. 121-197)",
          "The Great Dagda, Goddess Brigit, Ogma & Eponymous Queens of Ireland", ["Lebor Gabála Érenn Part IV (Macalister ¶313-317, ¶335-344, pp. 121-197)"],
          "Elada fathered Eochu Ollathair (The Great Dagda, reigned 80 yrs -> Óengus Mac Óc, poetess-goddess Brigit, and Cermait -> joint kings Mac Cuill, Mac Cécht, Mac Gréine), Ogma (inventor of Ogham -> Delbaeth -> Fiachna -> Ériu [Ireland!], Banba & Fódla, plus the 3 Gods of Danann: Brian, Iuchar, Iucharba), and Bres (half-Fomorian king)!",
          ["The Dagda (Eochu Ollathair)", "Óengus Mac Óc", "Goddess Brigit", "Ogma", "Ériu / Banba / Fódla", "Bres"], major=True),
    ]

    add_roster(nodes, edges, "cel_fir_bolg_kings", "celr_fb", "europe_norse", 9, "Lebor Gabála Sect. VI (Macalister)", "Fir Bolg Sovereign", ["Lebor Gabála Érenn Part IV (pp. 7-21)"], [
        "1. Sláine / Slanga mac Dela (+ Fuat)", "2. Rudraige mac Dela (+ Liber)", "3. Gann mac Dela (+ Etar)",
        "4. Genann mac Dela (+ Cnucha)", "5. Sengann mac Dela (+ Anust)", "6. Fiacha Cendfindan mac Starn",
        "7. Rindail mac Genann", "8. Fodbgenid mac Sengann", "9. Eochu mac Eirc (+ Queen Tailtiu of Spain)", "Oengus mac Umor (Dún Aengusa)"
    ], edge_type="direct", edge_label="Fir Bolg King (Macalister Sect. VI)")

    add_roster(nodes, edges, "cel_tdd_nuadu_dian_cecht", "celr_tdd1", "europe_norse", 10, "Lebor Gabála Sect. VII (Macalister)", "Tuatha Dé Danann Deity / Sovereign", ["Lebor Gabála Érenn Part IV (pp. 113-159)"], [
        "Tat mac Tabarn (Common Ancestor of TDD)", "Nuadu Airgetlám (King 27 yrs)", "Midir of Brí Léith", "Nét (War God, + Fea & Neman)",
        "Goibniu (Divine Smith)", "Creidne (Divine Brazier)", "Luichtne (Divine Carpenter)", "Dian Cécht (Divine Physician)",
        "Cian / Scal Balb (Father of Lugh)", "Miach & Airmed (Healers)", "Ethniu (Daughter of Balor, Mother of Lugh)",
        "Balor of the Evil Eye (Fomorian King)", "Lugh Lámfada (King 40 yrs, Victor at Mag Tuired)", "Manannán mac Lir (Sea God)"
    ], edge_type="direct", edge_label="Tuatha Dé Danann Lineage (Macalister)")

    add_roster(nodes, edges, "cel_tdd_dagda_ogma_eriu", "celr_tdd2", "europe_norse", 10, "Lebor Gabála Sect. VII (Macalister)", "Tuatha Dé Danann Sovereign / Deity", ["Lebor Gabála Érenn Part IV (pp. 121-197)"], [
        "Elada / Elathan (Father of Dagda, Ogma & Bres)", "Bres mac Elathan (Half-Fomorian King)", "Eochu Ollathair / The Dagda (King 80 yrs)",
        "Óengus Mac Óc (Son of Dagda, Brú na Bóinne)", "Brigit the Poetess (Daughter of Dagda)", "Cermait Milbel (Son of Dagda)",
        "Mac Cuill / Sethor (+ Queen Banba)", "Mac Cécht / Tethor (+ Queen Fódla)", "Mac Gréine / Cethor (+ Queen Ériu)",
        "Ogma (Champion & Inventor of Ogham)", "Delbaeth / Tuirenn (King 10 yrs)", "Fiachna mac Delbaeth (King 10 yrs)",
        "Brian, Iuchar & Iucharba (Three Gods of Danu)", "Ériu, Banba & Fódla (Sovereignty Goddesses of Ireland)", "Ernmas & The Morrígan"
    ], edge_type="direct", edge_label="House of Elada / Dagda / Ogma (Macalister)")

    edges += [
        E("bib_magog", "cel_nemed_pedigree", "syncretic", "Lebor Gabála Érenn R1 ¶316 traces Nemed from Noah -> Japheth -> Magog"),
        E("cel_nemed_pedigree", "cel_fir_bolg_kings", "direct", "Nemed -> Starn -> Semeon -> Dela -> 5 Sons & 9 Fir Bolg Kings"),
        E("cel_nemed_pedigree", "cel_tdd_nuadu_dian_cecht", "direct", "Nemed -> Iarbonel -> Bethach -> Tat -> Nuadu Airgetlám & Dian Cécht -> Lugh"),
        E("cel_nemed_pedigree", "cel_tdd_dagda_ogma_eriu", "direct", "Nemed -> Tat -> Nét -> Elada -> The Dagda, Ogma & Ériu"),
        E("cel_tdd_dagda_ogma_eriu", "eur_tuatha_de", "direct", "Complete Tuatha Dé Danann royal & divine pantheon"),
        E("cel_tdd_dagda_ogma_eriu", "eur_milesians", "expansion", "Sons of Míl defeat Mac Cuill, Mac Cécht & Mac Gréine (Ériu gives her name to Ireland!)"),
    ]

    return {
        "module": "23_celtic_lebor_gabala",
        "title": "Complete Irish Lebor Gabála Érenn Part IV: Nemedian Pedigree from Magog, All 9 Fir Bolg Kings & Complete Tuatha Dé Danann Pantheon (Macalister)",
        "nodes": nodes,
        "edges": edges,
    }
