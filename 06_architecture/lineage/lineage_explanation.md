# Data Lineage: Tables → Views → AI Copilot

This document explains how data lineage flows through the
air-lab Enterprise AI Copilot.

Lineage is not documentation decoration —
it is a **trust and audit mechanism**.

---

## Lineage Diagram

See:
`lineage_tables_to_views_to_copilot.png`

This diagram shows:
- physical data sources
- semantic transformation
- AI consumption and explanation

---

## Physical Layer (Storage)

CUSTOMERS
1 ── * ACCOUNTS
1 ── * TRANSACTIONS * ── 1 PRODUCTS


- Normalised storage
- No business meaning embedded
- No AI access

---

## Semantic Layer (Meaning)

Certified semantic views:
- `vw_active_customers`
- `vw_account_summary`
- `vw_daily_transactions`

These views:
- encode business meaning
- apply approved joins and aggregations
- hide raw data complexity

---

## AI Copilot Layer (Consumption)

The AI copilot:
- queries semantic views only
- explains results using glossary definitions
- cites source, certification, and freshness
- refuses when lineage or certification is missing

---

## Why This Matters

With explicit lineage:
- every answer is traceable
- audits are explainable
- trust is repeatable

Without lineage:
- AI answers are opinions
- governance becomes reactive
- pilots fail to scale

---

## Key Takeaway

> **AI answers are only as trustworthy as the lineage behind them.**

This architecture makes that lineage explicit and enforceable.
