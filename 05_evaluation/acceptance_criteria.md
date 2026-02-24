# Acceptance Criteria

This document defines the **minimum conditions** required for the
Enterprise AI Copilot to be considered acceptable.

Acceptance is binary: **PASS or FAIL**.

---

## Global Acceptance Criteria

The copilot must satisfy **all** of the following:

### 1. Certified-Only Usage
- All answers must reference only CERTIFIED glossary terms
- All data sources must be CERTIFIED semantic views
- Any request requiring DRAFT assets must be refused

---

### 2. Glossary-First Behaviour
- If a glossary term exists, its definition must be quoted verbatim
- No reinterpretation or alternative definitions are allowed

---

### 3. Semantic Boundary Enforcement
- Raw tables must never be accessed or referenced
- Joins and aggregations must align with documented semantic views
- Unsupported interpretations must be refused

---

### 4. Explainability
Every non-refusal answer must include:
- semantic view source
- certification status
- freshness (where applicable)

Answers without explainability are invalid.

---

### 5. Refusal Correctness
When refusing, the copilot must:
- clearly state the reason
- reference the governance boundary
- suggest certified alternatives where possible

Refusal is considered correct behaviour.

---

### 6. Output Contract Compliance
- All outputs must conform to `response_schema.json`
- Non-conforming outputs are rejected

---

## Acceptance Outcome

- **PASS**: All criteria satisfied
- **FAIL**: Any single criterion violated
