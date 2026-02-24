import json
from pathlib import Path

import faiss
from numpy import indices
from sentence_transformers import SentenceTransformer


INDEX_PATH = Path("07_runtime_local/rag/index.faiss")
STORE_PATH = Path("07_runtime_local/rag/store.json")


def retrieve_context(
    question: str,
    allowed_views: list,
    top_k: int = 5
):
    """
    Retrieve relevant context chunks for a question,
    filtered to allowed (CERTIFIED) semantic views.
    """

    if not INDEX_PATH.exists() or not STORE_PATH.exists():
        raise RuntimeError("RAG index not found. Run build_index.py first.")

    # Load index + store
    index = faiss.read_index(str(INDEX_PATH))
    with open(STORE_PATH, "r") as f:
        documents = json.load(f)

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    query_embedding = model.encode([question])

    distances, indices = index.search(query_embedding, top_k * 2)

    results = []
    seen = set()

    for idx in indices[0]:
        doc = documents[idx]
        key = (doc["type"], doc["name"])

        if key in seen:
            continue

        if doc["type"] == "glossary":
            results.append(doc)
            seen.add(key)

        elif doc["type"] == "semantic_view":
            if allowed_views is None or doc["name"] in allowed_views:
                results.append(doc)
                seen.add(key)

        if len(results) >= top_k:
            break

    return results

