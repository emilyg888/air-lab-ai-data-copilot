# Scope and Non-Goals

This document defines the **explicit scope boundaries** of the
air-lab-ai-data-copilot project.

These boundaries are intentional. They reflect how enterprise AI platforms
are successfully designed, governed, and adopted.

---

## In Scope

### 1. Governed Enterprise AI Pattern
This project focuses on **how AI should be integrated into an enterprise data platform**, including:

- Business glossary as the authoritative source of meaning
- Executable governance rules
- Certified semantic views as the AI access boundary
- Explainable answers with source, certification, and freshness

The emphasis is on **architecture and control**, not model novelty.

---

### 2. Concept-First, Platform-Led Design
The project is designed to be valuable **even without running code**.

In scope:
- Conceptual architecture diagrams
- Governance artefacts (glossary, dataset register, certification rules)
- Semantic view definitions
- Lineage documentation
- Explicit refusal behaviour

The runtime implementation exists only to **automate already-defined contracts**.

---

### 3. Read-Only AI Copilot Use Cases
All AI interactions in scope are:

- Read-only
- Descriptive or explanatory
- Bound to certified datasets

The copilot answers questions *about* the enterprise data platform —
it does not act on systems.

---

### 4. Local Runtime as an Execution Plane
A minimal local RAG runtime is included to demonstrate:

- How governance rules can be enforced programmatically
- How LLMs fit into an enterprise architecture
- How execution planes can be swapped (local → cloud)

The local runtime is **not the centrepiece** of the project.

---

## Explicit Non-Goals

### 1. Not a Chatbot or Conversational Product
This project does **not** aim to build:

- A general-purpose chatbot
- A conversational UX
- A customer-facing assistant

Conversation quality, personality, and UX design are out of scope.

---

### 2. Not a Model Benchmarking Exercise
This project does **not** focus on:

- Comparing LLM providers
- Model performance benchmarks
- Prompt engineering tricks
- Temperature tuning or creativity optimisation

The LLM is treated as a **replaceable reasoning component**.

---

### 3. Not a Production Deployment
This project intentionally excludes:

- High availability
- Security hardening
- Access management (IAM)
- CI/CD pipelines
- Monitoring and alerting

These are important in real systems, but distract from the architectural lesson.

---

### 4. Not a Data Engineering Tutorial
This project does **not** attempt to teach:

- ETL/ELT pipeline development
- Advanced SQL optimisation
- Streaming or real-time ingestion

Sample data and views are simplified to support semantic clarity.

---

### 5. Not an Ontology or Knowledge Graph Build
While ontology and knowledge graphs are discussed as **future extensions**,
they are intentionally out of scope for the core lab.

The focus remains on:
- Business glossary
- Semantic views
- Governance as the foundation

---

## Summary

This lab is deliberately:
- Narrow in scope
- Strong in governance
- Representative of real enterprise constraints

It optimises for **architectural correctness**, not feature breadth.
