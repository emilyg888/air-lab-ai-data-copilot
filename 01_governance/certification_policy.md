# Certification Policy

This policy defines how glossary terms and datasets move between
DRAFT and CERTIFIED status.

Certification is a **governance gate**, not a formality.

---

## Certification Status Definitions

### CERTIFIED
An asset that is:
- approved for enterprise reporting
- safe for AI-assisted explanation
- governed by a named owner and steward
- supported by documented logic and lineage

### DRAFT
An asset that is:
- under review
- incomplete or unstable
- not approved for automated explanation or decision support

---

## Certification Requirements

To be marked CERTIFIED, an asset must have:

### For Business Glossary Terms
- Clear, unambiguous definition
- Agreed calculation logic (if applicable)
- Named business owner and data steward
- Mapped implementation (semantic view)

### For Semantic Views
- Documented source tables
- Explicit join and aggregation logic
- Defined freshness SLA
- Allowed and excluded fields
- Named owner and steward

---

## AI Enforcement Rules

- CERTIFIED assets: AI may use and explain
- DRAFT assets: AI must refuse
- Mixed usage (CERTIFIED + DRAFT): AI must refuse

Certification is enforced **before runtime**, not negotiated at runtime.

---

## Promotion Process (Conceptual)

1. Asset created as DRAFT
2. Review by domain owner and steward
3. Logic and lineage validated
4. Certification approved
5. Asset added or updated in registry

Only then may the AI use it.

---

## Design Principle

**Certification happens before automation.  
**AI is never the place where meaning is finalised.**

---

## Summary

Certification:
- protects trust
- enables scale
- makes AI explainable

Without certification, AI remains a demo.
