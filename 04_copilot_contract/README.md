# AI Copilot Contract

This folder defines the **behavioural and output contract** for the
air-lab Enterprise AI Copilot.

The copilot contract specifies:
- what the AI is allowed to answer
- how it must reason
- how it must refuse
- what a valid response looks like

This contract is **model-agnostic** and **runtime-agnostic**.
It applies equally to local LLMs, cloud LLMs, and future execution planes.

---

## Why a Copilot Contract Exists

In enterprise environments, AI systems must be:
- predictable
- auditable
- explainable
- governable

These properties cannot be delegated to the model.

The copilot contract ensures that:
- governance rules are enforced consistently
- AI behaviour is stable over time
- outputs can be validated programmatically

---

## What Lives in This Folder

04_copilot_contract/
├── README.md # This file
├── prompt_contract.md # System-level AI rules
├── response_schema.json # Machine-enforceable output format
├── example_responses.md # Correct answer and refusal patterns
└── question_bank.md # Approved test questions

---

## Relationship to Other Layers

- **Governance** defines *what is allowed*
- **Semantic layer** defines *what data means*
- **Copilot contract** defines *how AI behaves*
- **Runtime** simply executes the contract

The AI is not the authority.  
The contract is.