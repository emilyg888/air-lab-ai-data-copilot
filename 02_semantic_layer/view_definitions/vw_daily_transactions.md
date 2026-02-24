# vw_daily_transactions (CERTIFIED)

## Purpose
Provides **daily aggregated transaction metrics** by channel and product
category for enterprise reporting and AI explanation.

This view supports **descriptive analysis only** and is designed to expose
approved transaction behaviour without revealing row-level or identifiable data.

---

## Business Definition
**Daily Transaction Volume**  
The total count and total value of transactions processed per day,
segmented by channel and product category.

Source: Business Glossary (`Daily Transaction Volume`, CERTIFIED)

---

## Grain
- One row per:
  - transaction_date
  - channel
  - product_category
  - currency

---

## Physical Source Tables
- transactions
- accounts
- products

---

## Join Path (Explicit)

This view resolves product attribution through the **approved semantic join path**:

```text
TRANSACTIONS.transaction_id
        ↓
TRANSACTIONS.account_id
        ↓
ACCOUNTS.account_id

TRANSACTIONS.transaction_id
        ↓
TRANSACTIONS.product_id
        ↓
PRODUCTS.product_id