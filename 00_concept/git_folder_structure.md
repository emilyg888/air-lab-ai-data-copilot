air-lab-ai-data-copilot/
├── README.md
├── LICENSE
├── .gitignore
│
├── 00_concept/
│   ├── 01_one_page_concept_diagram.png
│   ├── 02_problem_statement.md
│   ├── 03_scope_and_non_goals.md
│   └── 04_user_stories.md
│
├── 01_governance/
│   ├── glossary.yaml
│   ├── governance_rules.md
│   ├── dataset_register.yaml
│   ├── certification_policy.md
│   └── examples/
│       ├── certified_vs_draft.md
│       └── refusal_examples.md
│
├── 02_semantic_layer/
│   ├── README.md
│   ├── semantic_views.md
│   └── view_definitions/
│       ├── vw_active_customers.md
│       ├── vw_account_summary.md
│       └── vw_daily_transactions.md
│
├── 03_data/
│   ├── README.md
│   ├── sample_data/
│   │   ├── customers.csv
│   │   ├── accounts.csv
│   │   ├── transactions.csv
│   │   └── products.csv
│   └── data_dictionary.md
│
├── 04_copilot_contract/
│   ├── README.md
│   ├── prompt_contract.md
│   ├── response_schema.json
│   ├── example_responses.md
│   └── question_bank.md
│
├── 05_evaluation/
│   ├── README.md
│   ├── acceptance_criteria.md
│   ├── test_cases.md
│   └── scoring_rubric.md
│
├── 06_architecture/
│   ├── README.md
│   ├── local_vs_enterprise.md
│   ├── controls_and_risks.md
│   └── lineage/
│       ├── lineage_tables_to_views_to_copilot.png
│       └── lineage_explanation.md
│
├── 07_runtime_local/
│   ├── README.md
│   ├── config/
│   │   └── runtime_config.yaml
│   │
│   ├── ingest/
│   │   ├── load_glossary.py
│   │   ├── load_dataset_register.py
│   │   └── load_semantic_views.py
│   │
│   ├── rag/
│   │   ├── build_index.py
│   │   ├── retrieve_context.py
│   │   ├── index.faiss
│   │   ├── store.json
│   │   └── index_config.yaml
│   │
│   ├── query_engine/              # NEW – deterministic execution layer
│   │   ├── __init__.py
│   │   ├── build_sql.py           # SQL template builder (view-scoped)
│   │   ├── enforce_policy.py      # Policy Enforcement Point (PEP)
│   │   └── execute_query.py       # Database execution layer
│   │
│   ├── copilot/
│   │   ├── system_prompt.txt
│   │   ├── answer.py              # Orchestrator
│   │   ├── refusal.py
│   │   └── llm_generate.py        # Narrative layer (LLM explanation only)
│   │
│   └── outputs/
│       └── sample_runtime_answers.json
│
└── 99_future_extensions/
    ├── README.md
    ├── ontology_optional.md
    └── cloud_execution_plane.md
