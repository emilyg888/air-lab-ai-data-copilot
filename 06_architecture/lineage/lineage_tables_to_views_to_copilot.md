┌──────────────────────────┐
│      PHYSICAL TABLES     │
│  (Storage / Not Exposed) │
└──────────────────────────┘

┌──────────────┐
│  CUSTOMERS   │
│──────────────│
│ PK customer_id
│    status
│    segment
│    onboard_date
└───────┬──────┘
        │ 1
        │
        │ *
┌───────▼──────┐
│   ACCOUNTS   │
│──────────────│
│ PK account_id
│ FK customer_id
│    account_status
│    open_date
│    close_date
│    balance
│    currency
└───────┬──────┘
        │ 1
        │
        │ *
┌───────▼──────────────┐
│     TRANSACTIONS      │
│──────────────────────│
│ PK transaction_id
│ FK account_id
│ FK product_id
│    transaction_date
│    channel
│    amount
│    currency
└───────┬──────────────┘
        │ *
        │
        │ 1
┌───────▼──────────────┐
│      PRODUCTS         │
│──────────────────────│
│ PK product_id
│    product_name
│    product_category
└──────────────────────┘


┌─────────────────────────────────────────────┐
│          CERTIFIED SEMANTIC VIEWS            │
│        (AI / Analytics Access Boundary)      │
└─────────────────────────────────────────────┘

┌──────────────────────────────┐
│  vw_active_customers         │  CERTIFIED
│──────────────────────────────│
│ • customers + accounts
│ • ACTIVE customers only
│ • ≥ 1 OPEN account
│ • No product or transaction detail
└──────────────────────────────┘

┌──────────────────────────────┐
│  vw_account_summary          │  CERTIFIED
│──────────────────────────────│
│ • accounts only
│ • One row per account
│ • Descriptive balance
│ • Product-agnostic
└──────────────────────────────┘

┌──────────────────────────────┐
│  vw_daily_transactions       │  CERTIFIED
│──────────────────────────────│
│ • transactions + products
│ • Daily aggregates
│ • Channel + product_category
│ • No row-level exposure
└──────────────────────────────┘


┌─────────────────────────────────────────────┐
│              AI COPILOT                      │
│        (Governed Consumption Layer)          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  • Uses CERTIFIED semantic views only        │
│  • Quotes business glossary definitions      │
│  • Enforces governance rules                 │
│  • Refuses unsupported or unsafe questions  │
└─────────────────────────────────────────────┘


┌─────────────────────────────────────────────┐
│          FINAL JSON RESPONSE                 │
│─────────────────────────────────────────────│
│  ANSWER (PASS)                               │
│   • Explanation                              │
│   • Source semantic view                    │
│   • Certification status                   │
│   • Freshness                               │
│                                             │
│  REFUSAL (FAIL)                              │
│   • Reason                                  │
│   • Governance boundary hit                 │
│   • Certified alternatives (if any)         │
└─────────────────────────────────────────────┘
