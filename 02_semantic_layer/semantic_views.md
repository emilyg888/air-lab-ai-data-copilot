# Certified Semantic Views (AI Access Boundary)

This document describes the **certified semantic views** that form the
approved consumption layer for the air-lab Enterprise AI Copilot.

In this lab, the semantic layer is the **contract boundary**:
- analytics and AI consume **semantic views**
- raw tables remain an internal implementation detail
- governance (certification, freshness, allowed fields) is enforced upstream

---

## Why Semantic Views Exist

Enterprises standardise on semantic views to ensure:
- **consistent meaning** (definitions match reporting)
- **approved calculations** (no metric drift)
- **safe access patterns** (no raw joins or sensitive exposure)
- **auditability** (lineage + freshness is explicit)

For AI use cases, semantic views prevent the “LLM + raw database” anti-pattern.

---

## What Is a Certified Semantic View?

A certified semantic view is an approved interface that:
- implements business glossary definitions (where applicable)
- exposes only **allowed fields**
- applies approved joins / filters / aggregations
- has a named owner/steward, SLA, and refresh timestamp

Certification status and lineage are defined in:
- `01_governance/dataset_register.yaml`

Detailed documentation for each view is in:
- `02_semantic_layer/view_definitions/`

---

## View Inventory (Certified)

### 1) `vw_active_customers` (CERTIFIED)
**Purpose:** Authoritative Active Customer population for reporting and AI explanation.

- Implements glossary term: **Active Customer**
- Grain: customer-level (one row per active customer)
- Key controls:
  - excludes draft terms (e.g., `risk_rating`)
  - no product or transaction detail at this grain

See: `view_definitions/vw_active_customers.md`

---

### 2) `vw_account_summary` (CERTIFIED)
**Purpose:** Trusted account lifecycle and end-of-day balance reporting.

- Implements glossary term: **Account B**
