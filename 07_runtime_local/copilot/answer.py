import requests

import json
from pathlib import Path
from datetime import datetime, timezone

from ..ingest.load_glossary import load_glossary
from ..ingest.load_dataset_register import load_dataset_register
from ..rag.retrieve_context import retrieve_context
from .refusal import should_refuse


RESPONSE_SCHEMA_PATH = Path("04_copilot_contract/response_schema.json")


def load_response_schema():
    with open(RESPONSE_SCHEMA_PATH, "r") as f:
        return json.load(f)


def current_timestamp():
    return datetime.now(timezone.utc).isoformat()


def build_refusal_response(reason, alternatives=None):
    return {
        "answer": f"Refusal: {reason}",
        "definitions_used": [],
        "sources": [],
        "governance": {
            "certified_only": True,
            "refusal": {
                "is_refused": True,
                "reason": reason,
                "suggested_alternatives": alternatives or []
            }
        }
    }


def build_answer_response(answer_text, definitions, sources):
    return {
        "answer": answer_text,
        "definitions_used": definitions,
        "sources": sources,
        "governance": {
            "certified_only": True,
            "refusal": {
                "is_refused": False,
                "reason": None,
                "suggested_alternatives": []
            }
        }
    }


def answer_question(question: str, required_views: list | None = None):

    glossary = load_glossary()
    dataset_register = load_dataset_register()

    # Step 1 — Pre-inference governance
    refusal = should_refuse(
        question=question,
        glossary=glossary,
        register=dataset_register,
        required_views=required_views
    )

    if refusal["is_refused"]:
        return build_refusal_response(
            reason=refusal["reason"],
            alternatives=refusal.get("alternatives")
        )

    # Step 2 — RAG retrieval
    context_chunks = retrieve_context(
        question=question,
        allowed_views=None,
        top_k=5
    )

    # Step 3 — Extract glossary definitions
    definitions_used = [
        {
            "term": c["name"],
            "definition": c["text"].split(":", 1)[1].strip(),
            "status": "CERTIFIED"
        }
        for c in context_chunks
        if c["type"] == "glossary"
    ]

    # Step 4 — Select semantic view
    semantic_views = [
        c["name"] for c in context_chunks
        if c["type"] == "semantic_view"
    ]

    if not semantic_views:
        return build_refusal_response(
            reason="No certified semantic view matched the question.",
            alternatives=["Rephrase the question."]
        )

    selected_view = semantic_views[0]

    # Step 5 — Governance validation of selected view
    dataset_meta = dataset_register.get(selected_view)

    if not dataset_meta:
        return build_refusal_response(
            reason=f"Semantic view '{selected_view}' is not registered.",
            alternatives=[]
        )

    if dataset_meta["status"] != "CERTIFIED":
        return build_refusal_response(
            reason=f"Semantic view '{selected_view}' is not certified.",
            alternatives=[]
        )

    sources = [{
        "name": selected_view,
        "status": dataset_meta["status"],
        "last_refresh_ts": dataset_meta.get("last_refresh_ts")
    }]

    # Step 6 — Deterministic SQL
    from ..query_engine.build_sql import build_sql
    from ..query_engine.enforce_policy import enforce_policy
    from ..query_engine.execute_query import execute_query
    from .llm_generate import generate_answer

    sql = build_sql(selected_view, question)

    enforce_policy(sql, selected_view)

    rows = execute_query(sql)

    if not rows:
        return build_refusal_response(
            reason="Query returned no results.",
            alternatives=["Refine the question scope."]
        )

    # Step 7 — LLM narrative
    answer_text = generate_answer(
        question=question,
        semantic_context=context_chunks,
        query_results=rows
    )

    # Step 8 — Wrap governance envelope
    return build_answer_response(
        answer_text=answer_text,
        definitions=definitions_used,
        sources=sources
    )




def call_llm(
    system_prompt: str,
    user_prompt: str,
    base_url: str,
    model: str,
    max_retries: int = 2
):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.0
    }

    for attempt in range(1, max_retries + 1):
        resp = requests.post(
            f"{base_url}/chat/completions",
            json=payload,
            timeout=60
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            # Strengthen instruction on retry
            payload["messages"].append({
                "role": "system",
                "content": (
                    "ERROR: Your previous response was not valid JSON. "
                    "Return ONLY a single valid JSON object. "
                    "Do not include any other text."
                )
            })

    raise ValueError("LLM failed to produce valid JSON after retries")



if __name__ == "__main__":
    question = input("\nAsk a question: ").strip()

    print("-" * 60)

    response = answer_question(question)
    print(json.dumps(response, indent=2))




