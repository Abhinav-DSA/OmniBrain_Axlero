from typing import List, Dict, Any

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import settings


def chunk_page_text(
    doc_id: str,
    source_path: str,
    page_num: int,
    text: str,
) -> List[Dict[str, Any]]:
    if not text or not text.strip():
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    pieces = splitter.split_text(text)
