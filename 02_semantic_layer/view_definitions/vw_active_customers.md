# vw_active_customers (CERTIFIED)

## Purpose
Provides the **authoritative Active Customer population** for enterprise
reporting and AI explanation.

This view implements the certified business glossary definition of
**Active Customer** and is the single approved source for this concept.

---

## Business Definition
**Active Customer**  
A customer with status ACTIVE and at least one OPEN account as of the reporting date.

Source: Business Glossary (`Active Customer`, CERTIFIED)

---

## Grain
- One row per **active customer**

---

## Source Tables
- customers
- accounts

---

## Join Logic
- customers.customer_id = accounts.customer_id

---

## Filters
- customers.status = 'ACTIVE'
- accounts.account_status = 'OPEN'

---

## Derived Attributes
- open_account_count = COUNT(accounts.account_id)

---

## Exposed Fields
| Field | Description |
|------|------------|
| customer_id | Unique customer identifier |
| segment | Business segmentation |
| status | Customer lifecycle status |
| onboard_date | Customer onboarding date |
| open_account_count | Number of open accounts |

---

## Explicit Exclusions
The following are intentionally excluded:
- risk_rating (DRAFT glossary term)
- account balances
- product attributes
- transaction detail

These exclusions prevent:
- interpretation risk
- leakage of uncertified concepts
- misuse outside approved semantics

---

## Approved Usage
- Active customer counts
- Active customer trends
- Segmentation analysis

---

## Disallowed Usage
- Risk analysis
- Revenue attribution
- Product performance analysis

---

## AI Governance Notes
- AI must quote the glossary definition when explaining this view
- AI must not infer customer risk or value
- AI must refuse questions requiring excluded attributes
