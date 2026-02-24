# vw_account_summary (CERTIFIED)

## Purpose
Provides a **trusted, account-level summary** of account lifecycle and
end-of-day balance information for reporting and AI explanation.

This view standardises how accounts are described and consumed.

---

## Business Context
Supports glossary concepts such as:
- Account Balance (CERTIFIED)

---

## Grain
- One row per **account**

---

## Source Tables
- accounts


---

## Exposed Fields
| Field | Description |
|------|------------|
| account_id | Unique account identifier |
| customer_id | Owning customer |
| account_status | OPEN / CLOSED |
| open_date | Account open date |
| close_date | Account close date |
| balance | End-of-day account balance |
| currency | Account currency |

---

## Governance Controls
- Balance is **descriptive only**
- No forecasting, valuation, or optimisation logic
- Product attributes are limited to approved category fields
- No customer-identifiable attributes beyond IDs

---

## Approved Usage
- Account balance reporting
- Account lifecycle analysis
- Balance by product category

---

## Disallowed Usage
- Customer profiling
- Predictive balance analysis
- Credit or risk scoring

---

## AI Governance Notes
- AI may summarise balances and counts
- AI must not speculate about future balance changes
- AI must refuse requests for customer-level financial profiling
