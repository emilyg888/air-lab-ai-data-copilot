# Controls and Risk Management

This document outlines the **primary risks** in enterprise AI systems
and how the air-lab architecture mitigates them.

---

## Key Enterprise AI Risks

### 1. Semantic Drift
Different teams interpret the same metric differently.

**Control:**
- Business glossary as the source of truth
- Certified semantic views as the only consumption interface

---

### 2. Unauthorised Data Use
AI accesses raw or sensitive data.

**Control:**
- Semantic layer boundary
- Dataset register enforcement
- Raw tables never exposed to AI

---

### 3. Hallucination and Over-Inference
AI invents meaning or causality.

**Control:**
- Descriptive-only semantic views
- Explicit disallowed usage
- Mandatory refusal behaviour

---

### 4. Audit and Explainability Failure
Answers cannot be traced or justified.

**Control:**
- Lineage documentation
- Source + certification + freshness in every response
- Stable JSON response contract

---

### 5. Pilot-Only Success
AI works in demos but fails governance review.

**Control:**
- Governance enforced before and after inference
- Evaluation framework with pass/fail criteria
- Refusal treated as correct behaviour

---

## Control Summary

| Risk | Control Mechanism |
|----|------------------|
| Meaning ambiguity | Business glossary |
| Unsafe access | Semantic layer |
| Hallucination | Governance gates |
| Audit failure | Lineage + explainability |
| Scale failure | Contract-first design |

---

## Design Principle

> **AI does not reduce risk.  
> Architecture does.**

This project demonstrates how risk is managed
*before* AI is introduced.
