PHYSICAL DATA (Not Exposed)
──────────────────────────
CUSTOMERS ──┐
            ├─> ACCOUNTS ──┐
            │              ├─> TRANSACTIONS ──┐
            │              │                   ├─> PRODUCTS
            │              │
            │              │
SEMANTIC LAYER (CERTIFIED)
─────────────────────────
vw_active_customers
  • customers + accounts
  • ACTIVE + OPEN only

vw_account_summary
  • accounts
  • one row per account

vw_daily_transactions
  • transactions + products
  • daily aggregates only


AI COPILOT (Governed)
────────────────────
• Uses CERTIFIED views only
• Quotes business glossary
• Enforces governance rules
• Refuses unsafe requests


FINAL JSON RESPONSE
───────────────────
PASS → Answer + Source + Cert + Freshness
FAIL → Refusal + Reason + Alternatives
