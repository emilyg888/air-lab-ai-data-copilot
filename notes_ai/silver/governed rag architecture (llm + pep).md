# governed rag architecture (llm + pep separation)

tags: [rag, governance, semantic-layer]
project: air-lab-ai-data-copilot
source: raw/governed-rag-sql-separation.md

## Summary

- LLM should not execute SQL directly
- Introduce a Policy Enforcement Point (PEP) outside the model
- Use semantic layer as controlled access interface
- Separate reasoning (LLM) from execution (data system)

## Key ideas

### Idea 1: LLM as reasoning engine

- Generates SQL or structured intent
- Does not access database directly
- Works on context + results only

### Idea 2: Policy Enforcement Point (PEP)

- Validates SQL before execution
- Enforces:
  - allowed views
  - RBAC/ABAC
  - PII masking
- Acts as control boundary

### Idea 3: Semantic layer as contract

- Only expose certified views:
  - vw_daily_transactions
  - vw_account_summary
- LLM operates within these constraints

## Architecture flow

```text
User Question
   ↓
retrieve_context (RAG)
   ↓
build_sql
   ↓
enforce_policy (PEP)
   ↓
execute_query (DuckDB/Snowflake)
   ↓
llm_generate (final answer)

Trade-offs

Pros
strong governance
auditable decisions
deterministic execution

Cons
added complexity
requires semantic layer discipline
limits flexibility

Open questions
how strict should PEP be in exploration mode?
can LLM suggest new views dynamically?
how to balance flexibility vs control?

My interpretation
This architecture separates probabilistic reasoning from deterministic execution, aligning with enterprise governance requirements while still leveraging LLM capabilities.
```
