# Data Dictionary (Physical Data Model)

This data dictionary documents the **physical data structures** used in the
air-lab Enterprise AI Copilot.

It describes **how data is stored**, not how it is interpreted.
Business meaning and approved usage are defined in:
- `01_governance/glossary.yaml`
- `02_semantic_layer/`

The AI copilot does **not** consume this layer directly.

---

## Design Principles

- Physical tables are **normalised**
- Business meaning is **not embedded** in storage
- Product attribution is **event-based**
- Semantic interpretation happens in the **semantic layer**
- No personally identifiable information (PII) is stored

---

## CUSTOMERS

Stores customer lifecycle and segmentation attributes.

### Primary Key
- `customer_id`

### Columns

| Column | Type | Description |
|------|------|-------------|
| customer_id | STRING | Unique customer identifier |
| status | STRING | Customer lifecycle status (e.g. ACTIVE, INACTIVE) |
| segment | STRING | Business segmentation |
| onboard_date | DATE | Customer onboarding date |

### Notes
- No PII (names, addresses, DOB)
- Used for population definition only
- Supports Active Customer logic via semantic views

---

## ACCOUNTS

Stores account lifecycle and balance information.
Accounts are intentionally **product-agnostic**.

### Primary Key
- `account_id`

### Foreign Keys
- `customer_id` → CUSTOMERS.customer_id

### Columns

| Column | Type | Description |
|------|------|-------------|
| account_id | STRING | Unique account identifier |
| customer_id | STRING | Owning customer |
| account_status | STRING | Account lifecycle status (OPEN, CLOSED) |
| open_date | DATE | Account open date |
| close_date | DATE | Account close date (nullable) |
| balance | DECIMAL | End-of-day balance (descriptive only) |
| currency | STRING | Account currency |

### Notes
- No product attributes stored here
- Balance is descriptive, not predictive
- Product meaning resolved at transaction level

---

## TRANSACTIONS

Stores individual business events.
This is the **only table** where product attribution exists.

### Primary Key
- `transaction_id`

### Foreign Keys
- `account_id` → ACCOUNTS.account_id
- `product_id` → PRODUCTS.product_id

### Columns

| Column | Type | Description |
|------|------|-------------|
| transaction_id | STRING | Unique transaction identifier |
| account_id | STRING | Related account |
| product_id | STRING | Product involved in the transaction |
| transaction_date | DATE | Transaction posting date |
| channel | STRING | Transaction channel (ONLINE, BRANCH, API) |
| amount | DECIMAL | Transaction amount |
| currency | STRING | Transaction currency |

### Notes
- Product attribution is **event-scoped**
- No customer identifiers stored directly
- Supports aggregation and lineage without duplication
- Raw transaction detail is not exposed to AI

---

## PRODUCTS

Reference table defining enterprise products.

### Primary Key
- `product_id`

### Columns

| Column | Type | Description |
|------|------|-------------|
| product_id | STRING | Unique product identifier |
| product_name | STRING | Human-readable product name |
| product_category | STRING | High-level product grouping (DEPOSIT, LOAN) |

### Notes
- Single source of product truth
- Used for aggregation and categorisation only
- No pricing, eligibility, or rules embedded

---

## Relationship Summary

```text
CUSTOMERS
   1 ── *  ACCOUNTS
               1 ── *  TRANSACTIONS  * ── 1  PRODUCTS
