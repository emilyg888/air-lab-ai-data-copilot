
---

# 🥇 3. GOLD (reusable pattern)

👉 Now we distill into something you’ll reuse across projects

```markdown
# LLM as reasoning layer (PEP outside model)

type: pattern
tags: [rag, governance, semantic-layer]
maturity: gold

## Core idea
LLM performs reasoning only; all data access and execution is controlled by an external Policy Enforcement Point (PEP).

## When to use
- enterprise AI systems with governance requirements
- regulated environments (finance, compliance)
- any system requiring auditability and control

## When NOT to use
- quick prototypes or experiments
- low-risk internal tools
- scenarios where flexibility > control

## Pattern / structure
User Question
   ↓
Retrieve Context (RAG)
   ↓
LLM builds intent / SQL
   ↓
Policy Enforcement Point (PEP)
   ↓
Execute Query (data system)
   ↓
LLM generates response from results


# Steps
Restrict LLM to generating intent (not execution)
Define semantic layer with certified views
Implement PEP:
validate SQL
enforce RBAC/ABAC
apply masking rules
Execute query in controlled environment
Pass results back to LLM for explanation

# Example (air-lab-ai-data-copilot)
LLM generates query using vw_daily_transactions
PEP validates allowed view + filters
DuckDB executes query
LLM explains trends from returned dataset

# Variations
strict mode: only certified views allowed
exploration mode: allow suggested views but require approval
hybrid: partial execution + simulated results

# Related patterns
semantic layer abstraction
retrieval-augmented generation (RAG)
controlled execution pipelines

# Notes
Critical principle: LLM must not become a data access layer
Keeps deterministic and probabilistic responsibilities separated

