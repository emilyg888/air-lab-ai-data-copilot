# Local Lab vs Enterprise Architecture

This document explains how the **air-lab local environment**
mirrors a **typical enterprise AI data platform**.

The goal is architectural fidelity, not infrastructure parity.

---

## Core Principle

> **Only the execution plane changes.  
> Semantics, governance, and contracts remain the same.**

---

## Side-by-Side Mapping

| Local Lab (air-lab) | Enterprise Platform |
|--------------------|---------------------|
| YAML governance files | Collibra / Purview |
| Semantic view docs | Certified BI datasets / data products |
| DuckDB / CSV | Snowflake / Databricks |
| Local vector index | Managed vector database |
| Local LLM (LM Studio) | Azure OpenAI / Bedrock |
| CLI runtime | BI tool / internal app |

---

## What the Local Lab Proves

The local lab demonstrates that:
- enterprise AI is primarily a **data architecture problem**
- governance and semantics can be enforced independently of scale
- AI behaviour is governed by contracts, not prompts

This makes the design:
- inspectable
- testable
- portable

---

## What the Local Lab Deliberately Omits

The local lab does not include:
- IAM and RBAC
- network security
- HA/DR
- CI/CD pipelines

These are important in production, but **orthogonal** to the core lesson:
> AI fails when meaning and governance are missing.

---

## Enterprise Takeaway

If the architecture works on a laptop with strict contracts,
it will work at enterprise scale once execution is swapped.

If it fails locally, scale will not save it.
