# Architecture Overview

This folder documents the **end-to-end architecture** of the
air-lab Enterprise AI Copilot.

It explains:
- how the local lab mirrors enterprise platforms
- how controls and risks are addressed
- how lineage flows from physical data to AI answers

This is the layer intended for:
- architecture reviews
- stakeholder walkthroughs
- interview and portfolio discussions

---

## What Lives in This Folder

06_architecture/
├── README.md
├── local_vs_enterprise.md # Local lab vs enterprise stack mapping
├── controls_and_risks.md # Control points and risk mitigation
└── lineage/
├── lineage_tables_to_views_to_copilot.png
└── lineage_explanation.md


---

## How to Read This Folder

Recommended order:
1. `local_vs_enterprise.md` — understand the architectural mirror
2. `controls_and_risks.md` — understand why this design is safe
3. `lineage/` — understand traceability and explainability

Together, these documents show **why this design scales beyond pilots**.
