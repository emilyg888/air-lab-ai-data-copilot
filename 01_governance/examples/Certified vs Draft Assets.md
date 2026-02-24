# Certified vs Draft Assets

This document explains the difference between **CERTIFIED** and **DRAFT**
assets in the context of the **Governed Enterprise Data Copilot**.

The distinction is intentional and foundational.  
It determines **what the AI is allowed to use**.

---

## Why This Matters

In enterprise environments, not all data and definitions are equal.

Some are:
- approved
- trusted
- safe for decision-making

Others are:
- under review
- experimental
- incomplete
- context-dependent

A governed AI system **must respect this boundary**.

---

## Certified Assets

### Definition
A **CERTIFIED** asset is approved for:
- enterprise reporting
- decision support
- AI-assisted explanation

Certification indicates that:
- the definition is agreed
- the logic is approved
- ownership is clear
- quality and freshness expectations exist

---

### Examples of Certified Assets

#### Business Glossary
- Term: **Active Customer**
- Status: CERTIFIED
- Definition: Approved and authoritative
- Owner and steward assigned

#### Semantic Views
- `vw_active_customers`
- `vw_account_summary`
- `vw_daily_transactions`

These views:
- expose only approved fields
- apply approved calculations
- hide raw or sensitive data
- are safe for AI consumption

---

### AI Behaviour with Certified Assets

When using CERTIFIED assets, the copilot:
- may answer questions
- must quote glossary definitions verbatim
- must cite the source semantic view
- must include certification status and freshness

This is the **happy path**.

---

## Draft Assets

### Definition
A **DRAFT** asset is:
- incomplete
- under review
- not yet approved for enterprise use

Draft assets exist to:
- support exploration
- allow iteration
- enable review and refinement

They are **not safe** for automated explanation or decision support.

---

### Examples of Draft Assets

#### Business Glossary
- Term: **Risk Rating**
- Status: DRAFT
- Definition: Subject to policy interpretation
- Approval pending

#### Data Attributes
- Columns present in raw tables
- Fields not exposed via certified semantic views

---

### AI Behaviour with Draft Assets

When a question requires a DRAFT asset, the copilot **must refuse**.

The copilot must:
- clearly state that the asset is DRAFT
- explain that it is not approved for use
- suggest certified alternatives if available

The copilot must **not**:
- infer meaning
- reinterpret draft logic
- combine draft and certified concepts
- “do its best anyway”

---

## Example: Allowed vs Refused

### Allowed (Certified)

**Question:**  
What is an Active Customer?

**Reason:**  
- Term is CERTIFIED  
- Implemented by `vw_active_customers`  
- Safe for explanation  

---

### Refused (Draft)

**Question:**  
What is the average risk rating of active customers?

**Reason:**  
- *Risk Rating* is a DRAFT glossary term  
- No certified semantic view supports this calculation  

**Correct response behaviour:**  
- Refuse with explanation  
- Reference certification status  
- Suggest an alternative (e.g. active customer counts by segment)

---

## Why Draft ≠ “Almost Certified”

In enterprises, the difference between DRAFT and CERTIFIED is not academic.

Using draft assets can lead to:
- inconsistent reporting
- regulatory breaches
- audit findings
- loss of trust in the platform

A governed AI system must treat this boundary as **hard**, not flexible.

---

## Design Principle

> **AI should never be the place where unapproved concepts are normalised.**

Certification happens *before* automation.

---

## Summary

| Aspect | CERTIFIED | DRAFT |
|-----|-----------|-------|
| Approved for AI use | Yes | No |
| Safe for reporting | Yes | No |
| Definition stable | Yes | No |
| AI may answer | Yes | Must refuse |
| AI may infer | No | No |

This distinction is a **core control mechanism**, not metadata decoration.
