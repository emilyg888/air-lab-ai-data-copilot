import re


DISALLOWED_PATTERNS = [
    r"raw table",
    r"raw data",
    r"customer name",
    r"list customers",
    r"predict",
    r"forecast",
    r"why .* spike",
    r"cause of",
    r"fraud",
]


def detect_disallowed_intent(question: str):
    q = question.lower()
    for pattern in DISALLOWED_PATTERNS:
        if re.search(pattern, q):
            return pattern
    return None


def check_glossary_terms(question: str, glossary: dict):
    """
    Detect glossary terms referenced in the question and check certification.
    """
    referenced_terms = []
    for term_name, term_meta in glossary.items():
        if term_name in question.lower():
            referenced_terms.append(term_meta)

    for term in referenced_terms:
        if term["status"] != "CERTIFIED":
            return {
                "is_refused": True,
                "reason": f"Glossary term '{term['term']}' is {term['status']} and not approved for AI use.",
                "alternatives": []
            }

    return None


def check_dataset_register(register: dict, required_views: list | None):
    """
    Ensure required semantic views are registered and CERTIFIED.
    """

    # If no required views specified (auto-selection mode), skip early check
    if not required_views:
        return None

    for view in required_views:
        if view not in register:
            return {
                "is_refused": True,
                "reason": f"Semantic view '{view}' is not registered.",
                "alternatives": []
            }

        if register[view]["status"] != "CERTIFIED":
            return {
                "is_refused": True,
                "reason": f"Semantic view '{view}' is not CERTIFIED.",
                "alternatives": []
            }

    return None



def should_refuse(question: str, glossary: dict, register: dict, required_views: list | None):
    """
    Central refusal decision.
    """
    # 1. Disallowed intent
    pattern = detect_disallowed_intent(question)
    if pattern:
        return {
            "is_refused": True,
            "reason": "The request implies disallowed or speculative usage.",
            "alternatives": [
                "Ask for descriptive metrics from certified semantic views."
            ]
        }

    # 2. Glossary enforcement
    glossary_check = check_glossary_terms(question, glossary)
    if glossary_check:
        return glossary_check

    # 3. Dataset register enforcement
    dataset_check = check_dataset_register(register, required_views)
    if dataset_check:
        return dataset_check

    return {
        "is_refused": False,
        "reason": None,
        "alternatives": []
    }


if __name__ == "__main__":
    # Quick manual test
    from ..ingest.load_glossary import load_glossary
    from ..ingest.load_dataset_register import load_dataset_register

    glossary = load_glossary()
    register = load_dataset_register()

    q1 = "What is the average risk rating of active customers?"
    print(should_refuse(q1, glossary, register, ["vw_active_customers"]))

    q2 = "Show daily transaction volume by product category"
    print(should_refuse(q2, glossary, register, ["vw_daily_transactions"]))
