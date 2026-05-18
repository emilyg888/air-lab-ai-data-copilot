# Air Lab AI Data Copilot

## Overview

Air Lab AI Data Copilot is a governed enterprise AI data copilot reference project. It demonstrates how certified business glossary terms, semantic views, deterministic SQL, policy enforcement, and a constrained LLM narrative layer can work together without giving the model direct control over data access or governance decisions.

The repository is intentionally organized as a handoff-ready architecture and local runtime example, not as a packaged production service.

## Architecture Summary

The runtime follows this pattern:

```text
Governance artifacts -> RAG retrieval -> SQL templates -> Policy enforcement -> DuckDB execution -> LLM narrative -> Governed response
```

Key principles:

- semantic views define the AI access boundary;
- governance checks happen before inference;
- SQL is template-driven, not model-generated;
- raw sample tables are hidden behind certified semantic views;
- the LLM explains certified context and query results only.

## Repository Structure

| Path | Purpose |
|---|---|
| `00_concept/` | Concept diagrams, architecture notes, and presentation material. |
| `01_governance/` | Business glossary, dataset register, certification policy, and governance examples. |
| `02_semantic_layer/` | Certified semantic view documentation and SQL definitions. |
| `03_data/` | Local sample CSV data and data dictionary. |
| `04_copilot_contract/` | Prompt contract, response schema, question bank, and example responses. |
| `05_evaluation/` | Evaluation criteria, scoring rubric, and test cases. |
| `06_architecture/` | Architecture diagrams and lineage documentation. |
| `07_runtime_local/` | Local Python runtime for governed retrieval, SQL execution, and response generation. |
| `design/` | Current architecture document and pending review issue log. |
| `notes_ai/` | Working notes and synthesis material pending review. |

## Setup

Use the existing local virtual environment if present:

```bash
.venv/bin/python -m compileall -q 07_runtime_local
```

The runtime expects dependencies such as `duckdb`, `faiss`, `sentence-transformers`, `requests`, and `pyyaml` to be installed in the active Python environment.

## Run

Build or refresh the local RAG index when governance or semantic-layer documents change:

```bash
.venv/bin/python -m 07_runtime_local.rag.build_index
```

Run the interactive copilot locally:

```bash
.venv/bin/python -m 07_runtime_local.copilot.answer
```

The narrative layer currently calls an OpenAI-compatible local endpoint at `http://127.0.0.1:1234/v1`.

## Test / SIT

Current smoke/SIT commands:

```bash
.venv/bin/python -m compileall -q 07_runtime_local
.venv/bin/python -m 07_runtime_local.copilot.refusal
.venv/bin/python -c "import importlib; b=importlib.import_module('07_runtime_local.query_engine.build_sql'); p=importlib.import_module('07_runtime_local.query_engine.enforce_policy'); e=importlib.import_module('07_runtime_local.query_engine.execute_query'); sql=b.build_sql('vw_active_customers','Show active customers by segment'); p.enforce_policy(sql,'vw_active_customers'); print(e.execute_query(sql))"
```

See `design/issues-pending-review.md` for the latest SIT results.

## Configuration

Runtime configuration lives in `07_runtime_local/config/runtime_config.yaml`. Do not commit secret values or local `.env` files. The repository `.gitignore` excludes common environment files, virtual environments, caches, and editor artifacts.

## Documentation

- Architecture: `design/architecture.md`
- Pending review issues: `design/issues-pending-review.md`
- Runtime notes: `07_runtime_local/dev_folder_structure.md`
- Concept notes: `00_concept/README.md`

## Current Status

The local runtime demonstrates governed RAG, deterministic SQL templates, certified semantic view execution, and policy-based refusal behavior. Formal automated tests and CI/CD are not yet present.
