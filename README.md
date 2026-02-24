# 07_runtime_local

This folder contains the **local execution plane** for the air-lab AI Data Copilot.

It implements the full governed runtime flow:

Governance → RAG → Deterministic SQL → Policy Enforcement → Data Execution → LLM Narrative

This layer demonstrates how an enterprise AI copilot should operate safely on certified semantic data.

---

# 🔷 Runtime Architecture Overview


The runtime is deliberately split into deterministic and probabilistic layers.

The LLM is never allowed to:
- execute SQL
- access raw tables
- enforce governance rules
- modify response schema

---

# 🔹 Folder Responsibilities

## config/
Runtime configuration (model name, endpoints, environment settings).

---

## ingest/
Loads certified governance and semantic artifacts into memory:

- `load_glossary.py`
- `load_dataset_register.py`
- `load_semantic_views.py`

These define the **AI access boundary**.

---

## rag/

### Purpose
Implements semantic retrieval over certified artifacts.

### Components

- `build_index.py`
  - Embeds certified glossary + semantic views
  - Writes `index.faiss` (vector index)
  - Writes `store.json` (document store)

- `retrieve_context.py`
  - Searches FAISS
  - Filters to allowed semantic views
  - Returns certified context only

RAG retrieves **meaning**, not data.

---

## query_engine/

### Purpose
Implements deterministic execution over semantic views.

This is the **Policy Enforcement Point (PEP)**.

### Components

- `build_sql.py`
  - Builds view-scoped SQL templates
  - No model-generated SQL allowed

- `enforce_policy.py`
  - Ensures only certified semantic views are used
  - Blocks raw table access
  - Prevents schema drift

- `execute_query.py`
  - Executes SQL against the data layer
  - Returns structured result rows
  - Replace mock execution with real DB connector in production

This layer ensures governance remains deterministic and external to the model.

---

## copilot/

### Purpose
Orchestrates the full runtime flow.

- `answer.py`
  - Main entrypoint
  - Coordinates governance → RAG → SQL → execution → LLM
  - Wraps final response in certified schema

- `llm_generate.py`
  - LLM narrative layer
  - Receives:
    - question
    - certified semantic context
    - query results
  - Produces explanation only

- `refusal.py`
  - Handles governance refusal scenarios

The LLM only generates explanation text.
All governance metadata is injected by Python.

---

## outputs/

Stores sample runtime responses for evaluation.

---

# 🔷 End-to-End Flow

1. **Pre-inference governance**
   - Validate required semantic views
   - Refuse if uncertified

2. **RAG retrieval**
   - Retrieve glossary + semantic view definitions
   - Certified context only

3. **SQL build**
   - Deterministic template generation

4. **Policy enforcement**
   - Block raw table access
   - Enforce semantic boundary

5. **Query execution**
   - Retrieve structured result rows

6. **LLM narrative generation**
   - Explain results using certified context
   - No SQL generation
   - No governance control

7. **Response wrapping**
   - Inject definitions_used
   - Inject source metadata
   - Inject governance envelope

---

# 🔷 Key Design Principles

- Semantic views are the AI access boundary
- Governance remains outside the LLM
- SQL is deterministic and template-driven
- No raw table access
- Response schema is enforced by code
- The LLM is a reasoning layer, not a control plane

---

# 🔷 Local vs Enterprise

This local runtime demonstrates the architecture pattern.

In enterprise deployment:

- FAISS → managed vector service
- execute_query → Snowflake / Databricks / Fabric
- Orchestrator → API service (FastAPI)
- Governance → centralized policy engine
- Observability → audit logs + traceability

---

# 🔷 Current Status

✔ RAG semantic retrieval  
✔ Deterministic SQL templates  
✔ Policy enforcement layer  
✔ LLM narrative generation  
✔ Certified response schema enforcement  

This is no longer a RAG demo.

It is a governed enterprise AI data copilot runtime.

---

