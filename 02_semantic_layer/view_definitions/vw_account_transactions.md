# vw_account_transactions (CERTIFIED)

## Purpose

Provides aggregated transaction metrics at the account level,
segmented by product category.

Supports account-level transaction analysis without exposing
row-level transaction detail.

---

## Grain

- One row per:
  - account_id
  - product_category

---

## Source Tables

- accounts
- transactions
- products

---

## Exposed Fields

| Field            | Description               |
| ---------------- | ------------------------- |
| account_id       | Unique account identifier |
| product_category | Product grouping          |
| total_count      | Number of transactions    |
| total_value      | Total transaction amount  |

---

## Governance Controls

- No transaction-level detail exposed
- No customer-identifiable information beyond account_id
- Descriptive aggregation only

---

## Approved Usage

- Account transaction analysis
- Product exposure analysis
- Concentration monitoring

---

## Disallowed Usage

- Predictive modeling
- Customer profiling
- Risk scoring
