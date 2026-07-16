
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

