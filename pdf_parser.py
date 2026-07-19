
import hashlib
import os
from dataclasses import dataclass, field
from typing import List, Dict, Any

import fitz  


@dataclass
class PageData:
    page_num: int  # 1-indexed
    text: str
    images: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class ParsedDocument:
    doc_id: str
    source_path: str
    pages: List[PageData]


def compute_doc_id(pdf_path: str) -> str:
    """
    Deterministic ID derived from the absolute path + file content.
    Re-ingesting the same file always produces the same doc_id, which lets
    downstream upserts overwrite rather than duplicate.
    """
    hasher = hashlib.sha1()
    hasher.update(os.path.abspath(pdf_path).encode("utf-8"))
    with open(pdf_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()[:16]

    
def parse_pdf(pdf_path: str) -> ParsedDocument:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    doc_id = compute_doc_id(pdf_path)
    doc = fitz.open(pdf_path)
    pages: List[PageData] = []

    try:
        for page_index in range(len(doc)):
            page = doc[page_index]
            text = page.get_text("text") or ""

            images = []
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                try:
                    base_image = doc.extract_image(xref)
                except Exception:
                    # Some xrefs (e.g. inline masks) fail to extract cleanly — skip them.
                    continue

                images.append({
                    "xref": xref,
                    "img_index": img_index,
                    "bytes": base_image.get("image"),
                    "ext": base_image.get("ext", "png"),
                    "width": base_image.get("width", 0),
                    "height": base_image.get("height", 0),
                })

            pages.append(PageData(page_num=page_index + 1, text=text, images=images))
    finally:
        doc.close()

    return ParsedDocument(doc_id=doc_id, source_path=pdf_path, pages=pages)

