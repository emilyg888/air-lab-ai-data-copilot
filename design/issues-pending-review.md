# Issues Pending Review

## Summary

| ID | Severity | Area | Issue | Recommended action | Status |
|---|---|---|---|---|---|
| ISSUE-001 | Medium | Tests | No formal automated test suite or CI exists. | Add focused tests for ingest, policy enforcement, SQL execution, refusal behavior, and response schema wrapping. | Pending review |
| ISSUE-002 | Medium | Architecture | Runtime package directory starts with a digit, so normal `from 07_runtime_local...` imports are invalid Python syntax. | Consider renaming the package directory or adding a conventional package entrypoint before productionization. | Pending review |
| ISSUE-003 | Medium | Runtime | Full copilot SIT depends on a local OpenAI-compatible LLM endpoint at `127.0.0.1:1234`. | Externalize the endpoint/model into config and add a mockable LLM adapter for tests. | Pending review |
| ISSUE-004 | Low | Repository hygiene | Worktree was already dirty before housekeeping with deleted concept files and untracked diagrams/notes/scripts. | Review whether these files should be retained, archived, or committed as intentional project assets. | Pending review |
| ISSUE-005 | Low | Code | `07_runtime_local/query_engine/init.py` appears to be a likely placeholder or typo for `__init__.py`, but it is not harmful and was left in place. | Confirm whether to rename, replace with `__init__.py`, or archive in a later cleanup. | Pending review |

## SIT Results

| Command | Result | Notes |
|---|---|---|
| `.venv/bin/python -m compileall -q 07_runtime_local` | Passed | Python runtime files compile successfully. |
| `.venv/bin/python -m 07_runtime_local.ingest.load_glossary` | Passed | Loaded glossary statuses including certified and draft terms. |
| `.venv/bin/python -m 07_runtime_local.ingest.load_dataset_register` | Passed | Loaded certified semantic view register entries. |
| `.venv/bin/python -m 07_runtime_local.copilot.refusal` | Passed after fix | Manual refusal smoke test now works with package-relative imports. |
| `.venv/bin/python -c "import importlib; b=importlib.import_module('07_runtime_local.query_engine.build_sql'); p=importlib.import_module('07_runtime_local.query_engine.enforce_policy'); e=importlib.import_module('07_runtime_local.query_engine.execute_query'); sql=b.build_sql('vw_active_customers','Show active customers by segment'); p.enforce_policy(sql,'vw_active_customers'); print(e.execute_query(sql))"` | Passed after fix | Initially failed because `vw_active_customers.sql` was missing. Added the SQL view to align with the certified semantic-view documentation and dataset register. |

## Archived Code Review

| Original path | Archived path | Reason | Review needed? |
|---|---|---|---|
| None | N/A | No low-risk redundant tracked code met the two-signal archive threshold during this pass. | No |

## Detailed Issues

### ISSUE-001 - No formal automated test suite or CI

- Severity: Medium
- Area: Tests
- Evidence: No `pyproject.toml`, `requirements.txt`, test folder, or CI workflow was found during baseline inspection.
- Impact: Runtime regressions currently rely on manual smoke/SIT checks.
- Recommended action: Add a small automated suite for ingest loaders, policy enforcement, SQL execution, refusal behavior, and response schema wrapping.
- Status: Pending review

### ISSUE-002 - Runtime package directory starts with a digit

- Severity: Medium
- Area: Architecture
- Evidence: `python -m 07_runtime_local...` works, but direct syntax such as `from 07_runtime_local.query_engine.execute_query import execute_query` fails because identifiers cannot start with a digit.
- Impact: The current folder name makes conventional imports awkward and encourages `importlib` workarounds.
- Recommended action: Consider renaming the runtime package before this becomes a production API boundary.
- Status: Pending review

### ISSUE-003 - LLM endpoint is hard-coded

- Severity: Medium
- Area: Config
- Evidence: `07_runtime_local/copilot/llm_generate.py` hard-codes `http://127.0.0.1:1234/v1` and `qwen3-4b-instruct-2507-mlx`.
- Impact: Full copilot SIT depends on one local server/model setup and is hard to automate.
- Recommended action: Move endpoint/model settings into `07_runtime_local/config/runtime_config.yaml` and provide a mockable adapter for tests.
- Status: Pending review

### ISSUE-004 - Worktree was already dirty before housekeeping

- Severity: Low
- Area: Repository hygiene
- Evidence: Baseline `git status --short` showed deleted tracked concept diagram files and untracked diagrams, notes, scripts, `config`, and `task.txt`.
- Impact: The repository needs owner review to decide which concept artifacts and local working files are intentional.
- Recommended action: Review and classify the pending files before any permanent cleanup.
- Status: Pending review

### ISSUE-005 - Possible placeholder `init.py`

- Severity: Low
- Area: Code
- Evidence: `07_runtime_local/query_engine/init.py` exists while sibling packages use `__init__.py`; no references were found during housekeeping.
- Impact: Low. It may confuse readers but does not currently block runtime execution.
- Recommended action: Confirm whether it should become `__init__.py` or be archived in a later cleanup.
- Status: Pending review
