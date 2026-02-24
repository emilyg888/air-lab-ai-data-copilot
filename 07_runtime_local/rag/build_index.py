import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

from ..ingest.load_glossary import load_glossary
from ..ingest.load_semantic_views import load_semantic_views




INDEX_PATH = Path("07_runtime_local/rag/index.faiss")
STORE_PATH = Path("07_runtime_local/rag/store.json")


def build_documents():
    """
    Build the list of text documents to embed.
    Only CERTIFIED glossary terms and semantic view definitions are included.
    """
    documents = []

    # 1. Glossary terms
    glossary = load_glossary()
    for term, meta in glossary.items():
        if meta["status"] == "CERTIFIED":
            documents.append({
                "type": "glossary",
                "name": meta["term"],
                "text": f"{meta['term']}: {meta['definition']}"
            })

    # 2. Semantic view definitions
    views = load_semantic_views()
    for view_name, text in views.items():
        documents.append({
            "type": "semantic_view",
            "name": view_name,
            "text": text
        })

    return documents


def build_index():
    print("🔧 Building RAG index...")

    documents = build_documents()
    texts = [doc["text"] for doc in documents]

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(INDEX_PATH))

    with open(STORE_PATH, "w") as f:
        json.dump(documents, f, indent=2)

    print(f"✅ Index written to {INDEX_PATH}")
    print(f"✅ Store written to {STORE_PATH}")
    print(f"📦 Documents indexed: {len(documents)}")


if __name__ == "__main__":
    build_index()
