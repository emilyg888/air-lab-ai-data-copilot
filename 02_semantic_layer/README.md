# Semantic Layer (Certified AI Access Boundary)

The **semantic layer** defines the approved, governed interface through which
analytics and AI are allowed to consume enterprise data.

In this lab, the semantic layer is the **AI contract boundary**.

- The AI copilot may consume **semantic views**
- The AI copilot may **not** consume raw tables
- Business meaning is enforced *before* automation

---

## Why the Semantic Layer Exists

Enterprises introduce a semantic layer to solve three recurring problems:

1. **Inconsistent meaning**
   - The same metric calculated differently across teams
2. **Unsafe access**
   - Raw joins exposing sensitive or misleading data
3. **Interpretation risk**
   - Correct numbers explained incorrectly

For AI, these risks are amplified.

The semantic layer ensures:
- consistent interpretation
- approved calculations
- explainable lineage
- safe consumption patterns

---

## What a Certified Semantic View Is

A **certified semantic view** is an approved interface that:

- implements one or more business glossary definitions
- applies approved joins, filters, and aggregations
- exposes only allowed fields
- has a defined grain and usage intent
- is registered and certified in governance

Certification status, lineage, and freshness are defined in:
- `01_governance/dataset_register.yaml`

---

## What Lives in This Folder

02_semantic_layer/
├── README.md # This file
├── semantic_views.md # Inventory and overview of certified views
└── view_definitions/ # Detailed view-level documentation


### `semantic_views.md`
Provides a **human-readable inventory** of certified semantic views:
- what each view represents
- which business concepts it supports
- when it should be used

### `view_definitions/`
Contains **one file per semantic view**, documenting:
- purpose and business intent
- grain and source tables
- joins, filters, and aggregations
- allowed and excluded usage
- AI-specific governance notes

These definitions make semantic intent explicit and enforceable.

---

## Relationship to Other Layers

The semantic layer sits between governance and physical data:

Business Glossary
↓
Semantic View Definitions
↓
Dataset Register (Certification & Enforcement)
↓
Raw Tables / Physical Data

- **Glossary** defines meaning
- **Semantic views** encode that meaning for consumption
- **Dataset register** enforces what is allowed
- **Physical data** remains an implementation detail

---

## How the AI Copilot Uses the Semantic Layer

The AI copilot:
- selects views from the **dataset register**
- explains answers using **view definitions**
- refuses questions that cannot be answered from certified views

The copilot does **not**:
- invent joins
- infer new metrics
- reinterpret business meaning
- bypass semantic constraints

This mirrors how BI and regulatory reporting already operate in enterprises.

---

## What the Semantic Layer Is Not

This layer is intentionally **not**:
- a raw data access layer
- a data engineering tutorial
- a metric experimentation playground
- a knowledge graph or ontology

Those concerns belong elsewhere.

---

## Design Principle

> **AI should consume meaning, not data structures.**

The semantic layer is where that meaning is stabilised.

---

## Next Steps

To explore this layer in detail:
- Review `semantic_views.md` for the certified view inventory
- Read individual files in `view_definitions/`
- See `01_governance/dataset_register.yaml` for certification enforcement

This layer is the foundation that allows AI to scale safely in enterprises.
