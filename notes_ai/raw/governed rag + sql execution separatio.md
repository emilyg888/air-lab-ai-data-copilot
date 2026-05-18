# governed rag + sql execution separation

date: 2026-04-05
source: chatgpt
project: air-lab-ai-data-copilot

## Prompt

How should I design a governed AI copilot where the LLM answers data questions but does not execute SQL directly?

## Key responses (raw)

- LLM should generate SQL but not execute it
- Introduce a policy enforcement layer (PEP) outside the model
- Flow:
  retrieve_context → build_sql → enforce_policy → execute_query → llm_generate
- Semantic layer should define certified views (vw_daily_transactions, vw_account_summary)
- Only certified views should be accessible
- LLM receives results, not direct DB access

## Interesting bits

- “LLM is reasoning layer, not execution engine”
- “Policy Enforcement Point outside model”
- separation of deterministic vs probabilistic

## Why this matters

Core architecture decision for copilot — impacts governance, auditability, and trust
