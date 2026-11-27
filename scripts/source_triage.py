"""
Source Library Triage & Catalog Manifest Generator (Hybrid Plan Stage 1).

Scans sources/ (read-only) and classifies every file into:
- excluded_incomplete (.crdownload partial downloads)
- excluded_fiction_non_genealogical (novels, astronomy satire, standalone essays)
- clean_text_sources (clean embedded text PDFs, HTML, EPUB ready for chunked mining)
- image_only_hybrid_sources (scanned PDFs handled via clean public-domain text / visual charts)
"""

import json
from collections import Counter
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources"
OUT_CATALOG = ROOT / "data" / "source_catalog.json"

FICTION_NON_GENEALOGICAL_PATTERNS = (
    "donquixote",
    "daphnisandchloe",
    "discoveryofanewworld",
    "johnwilkins",
    "worksoflucian",
)


def classify_sources():
    rows = []
    counts = Counter()

    if not SOURCES_DIR.exists():
        raise FileNotFoundError(f"Missing sources directory: {SOURCES_DIR}")

    for fp in sorted(SOURCES_DIR.iterdir(), key=lambda p: p.name.lower()):
        if not fp.is_file():
            continue
        fn = fp.name
        low = fn.lower()
        sz_mb = round(fp.stat().st_size / 1048576.0, 2)
        ext = fp.suffix.lower()

        if ext == ".crdownload" or low.startswith("unconfirmed "):
            cat = "excluded_incomplete"
            rows.append({"file": fn, "category": cat, "mb": sz_mb, "pages": 0, "reason": "Incomplete browser download (.crdownload)"})
            counts[cat] += 1
            continue

        if any(pat in low for pat in FICTION_NON_GENEALOGICAL_PATTERNS):
            cat = "excluded_fiction_non_genealogical"
            rows.append({"file": fn, "category": cat, "mb": sz_mb, "pages": 0, "reason": "Pure fiction / non-genealogical work"})
            counts[cat] += 1
            continue

        if ext in (".htm", ".html", ".epub"):
            cat = "clean_text_sources"
            rows.append({"file": fn, "category": cat, "mb": sz_mb, "pages": 0, "ext": ext})
            counts[cat] += 1
            continue

        if ext == ".pdf":
            try:
                doc = pymupdf.open(fp)
                np = len(doc)
                sample_idxs = sorted({min(np - 1, int(np * f)) for f in (0.1, 0.3, 0.5, 0.7, 0.9)}) if np > 0 else []
                chars = 0
                alpha = 0
                for pno in sample_idxs:
                    txt = doc[pno].get_text("text")
                    chars += len(txt)
                    alpha += sum(c.isalpha() for c in txt)
                doc.close()
                avg_chars = chars / max(1, len(sample_idxs))
                alpha_ratio = alpha / max(1, chars)
                if avg_chars < 50:
                    cat = "image_only_hybrid_sources"
                elif avg_chars < 400 or alpha_ratio < 0.55:
                    cat = "image_only_hybrid_sources"
                else:
                    cat = "clean_text_sources"
                rows.append({
                    "file": fn,
                    "category": cat,
                    "mb": sz_mb,
                    "pages": np,
                    "avg_chars_sample": round(avg_chars),
                    "alpha_ratio": round(alpha_ratio, 2),
                })
                counts[cat] += 1
            except Exception as exc:
                cat = "excluded_error"
                rows.append({"file": fn, "category": cat, "mb": sz_mb, "pages": 0, "reason": str(exc)})
                counts[cat] += 1
            continue

        cat = "excluded_other"
        rows.append({"file": fn, "category": cat, "mb": sz_mb, "pages": 0})
        counts[cat] += 1

    manifest = {
        "summary": {
            "total_files": len(rows),
            "counts_by_category": dict(counts),
            "active_genealogical_sources": counts["clean_text_sources"] + counts["image_only_hybrid_sources"],
            "excluded_sources": counts["excluded_incomplete"] + counts["excluded_fiction_non_genealogical"],
        },
        "sources": rows,
    }
    OUT_CATALOG.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CATALOG, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"SOURCE TRIAGE OK: {len(rows)} files -> {OUT_CATALOG.name}")
    for k, v in counts.most_common():
        print(f"  - {k}: {v}")


if __name__ == "__main__":
    classify_sources()
