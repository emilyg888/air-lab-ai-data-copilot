# Refusal Examples (Governed AI Copilot)

This document provides examples of **correct refusal behaviour** for the
Governed Enterprise Data Copilot.

Refusal is a **required production feature** in enterprise AI:
- it protects trust
- it enforces governance boundaries
- it prevents “helpful” but unsafe outputs

The copilot must refuse when a request cannot be satisfied using:
- CERTIFIED glossary terms
- CERTIFIED semantic views in `dataset_register.yaml`

---

## Refusal Template (Required)

When refusing, the copilot must include:

1) **Refusal decision**: clearly state it cannot comply  
2) **Reason**: reference the governance boundary (e.g., DRAFT term / non-certified dataset)  
3) **Certified alternatives**: propose what can be answered safely  
4) **Next step** (optional): how to make it answerable (e.g., certification request)

---

## Example 1 — DRAFT Glossary Term (Must Refuse)

**User asks:**  
“What is the average risk rating of active customers?”

**Why refuse:**  
- `Risk Rating` is **DRAFT** in the business glossary  
- No certified semantic view supports risk rating aggregation

**Correct refusal response (human-readable):**
- I can’t answer that using certified definitions and datasets because **Risk Rating is DRAFT** and not approved for enterprise reporting.
- Certified alternative: I can provide **active customer counts by segment** using `vw_active_customers`.
- Next step: request certification of the **Risk Rating** term and its supporting dataset.

**Suggested alternatives:**
- “How many active customers do we have today?”
- “Show active customers by segment.”

---

## Example 2 — Request to Use Raw Tables (Must Refuse)

**User asks:**  
“Query the raw transactions table and list the top 10 customers by spend.”

**Why refuse:**  
- Raw tables are **not** an approved AI access boundary  
- Only certified semantic views are allowed for AI answers

**Correct refusal response:**
- I can’t access raw tables directly. This copilot is restricted to **certified semantic views**.
- Certified alternative: I can summarise **daily transaction volume by channel and product category** using `vw_daily_transactions`.

**Suggested alternatives:**
- “Show yesterday’s transaction volume by channel.”
- “Summarise transaction volume trends by product category.”

---

## Example 3 — PII / Identifiable Output (Must Refuse)

**User asks:**  
“Give me the names and details of customers with the highest balances.”

**Why refuse:**  
- Customer-identifiable details are not available in certified semantic views  
- The semantic layer is intentionally designed to avoid PII exposure

**Correct refusal response:**
- I can’t provide customer-identifiable details from this governed semantic layer.
- Certified alternative: I can provide **aggregate balance reporting by product category** using `vw_account_summary`.

**Suggested alternatives:**
- “Show total balance by product category.”
- “Show account counts by status and product category.”

---

## Example 4 — Unsupported Metric / Not Defined (Must Refuse or Clarify)

**User asks:**  
“What is our customer lifetime value (CLV)?”

**Why refuse (or ask-back):**
- CLV is not defined in the certified business glossary
- No certified semantic view provides CLV logic

**Correct behaviour:**
- Ask-back (preferred): “CLV is not currently defined as a certified term. Do you mean revenue-based CLV, margin-based CLV, or retention-based CLV?”
- If still not certified: refuse.

**Certified alternatives:**
- “Daily Transaction Volume” definition and trends
- “Active Customer” counts over time

---

## Example 5 — Speculation / Causal Claims (Must Refuse Speculation)

**User asks:**  
“Why did transactions spike yesterday? Was it fraud?”

**Why refuse the causal inference:**
- `vw_daily_transactions` can show volume by channel/category
- It cannot prove causality (fraud / campaign / outage)
- The copilot must remain descriptive, not speculative

**Correct response pattern (partial answer + boundary):**
- Provide descriptive breakdown using certified view:
  - by channel
  - by product category
- Refuse speculative claim:
  - “I can’t determine whether this was fraud from certified reporting views alone.”

**Suggested alternatives:**
- “Show the spike by channel and product category.”
- “Do we have a certified fraud flag dataset available?” (if later added)

---

## Example 6 — Freshness / Recency Boundary (Must Refuse or Qualify)

**User asks:**  
“What’s happening right now with transactions?”

**Why refuse or qualify:**
- The dataset register defines freshness (e.g., 6-hour SLA)
- If the question implies real-time, the copilot must clarify limitations

**Correct response pattern:**
- “I can only answer using the latest certified refresh timestamp: `<last_refresh_ts>`.”
- Provide last available summary (not real-time)

---

## Gold Standard Refusal (Short Form)

Use this when time is limited:

> I can’t answer that from **certified** definitions and datasets.  
> Reason: `<why>`  
> I *can* answer: `<certified alternative>` using `<view>`.

---

## Why These Refusals Make the System Production-Ready

A governed copilot that refuses correctly:
- protects enterprise trust
- satisfies audit expectations
- prevents metric drift
- enables safe scaling across domains

Refusal is not a limitation.  
It is a **control mechanism**.
