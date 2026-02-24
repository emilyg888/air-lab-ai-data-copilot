# Evaluation Framework

This folder defines how the **Enterprise AI Copilot** is evaluated.

Evaluation in this lab is not about:
- model accuracy benchmarks
- response creativity
- conversational fluency

It is about:
- governance compliance
- semantic correctness
- explainability
- refusal behaviour

A copilot that answers incorrectly is a failure.  
A copilot that refuses correctly is a success.

---

## Evaluation Objectives

The evaluation framework ensures that the copilot:

1. Uses **only certified assets**
2. Respects semantic usage boundaries
3. Produces explainable outputs
4. Refuses unsafe or unsupported requests
5. Conforms to a stable response contract

---

## What Lives in This Folder

05_evaluation/
├── README.md # Evaluation intent and scope
├── acceptance_criteria.md # Pass/fail conditions
├── test_cases.md # Test scenarios
└── scoring_rubric.md # Structured assessment


---

## Relationship to Other Layers

- Governance defines **what is allowed**
- Semantic layer defines **what is meaningful**
- Copilot contract defines **how AI behaves**
- Evaluation verifies **that all of the above are enforced**

This layer closes the loop between design and runtime behaviour.
