"""
LLM narrative generator.
LLM explains results.
Does NOT build SQL or enforce governance.
"""

from pathlib import Path
from .answer import call_llm


def generate_answer(
    question: str,
    semantic_context: list,
    query_results: list
) -> str:

    system_prompt = Path(
        "07_runtime_local/copilot/system_prompt.txt"
    ).read_text()

    context_text = "\n\n".join(
        f"[{c['type'].upper()}] {c['name']}\n{c['text']}"
        for c in semantic_context
    )

    user_prompt = f"""
    Question:
    {question}

    Certified Semantic Context:
    {context_text}

    Query Results:
    {query_results}

    Explain the result clearly.
    Use only the certified context.
    Do not fabricate values.
    Return JSON with an 'answer' field only.
    """

    parsed = call_llm(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        base_url="http://127.0.0.1:1234/v1",
        model="qwen3-4b-instruct-2507-mlx"
    )

    return parsed["answer"]
