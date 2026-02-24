"""
Policy Enforcement Point (PEP)
Ensures SQL respects semantic boundary.
"""

FORBIDDEN_KEYWORDS = [
    " transactions ",
    " accounts ",
    " products ",
    " customers "
]


def enforce_policy(sql: str, allowed_view: str):
    """
    Enforce semantic boundary rules.
    """

    sql_lower = sql.lower()

    # Must reference allowed semantic view only
    if allowed_view.lower() not in sql_lower:
        raise PermissionError(
            "Query must reference certified semantic view only."
        )

    # Block raw table references
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_lower:
            raise PermissionError(
                f"Raw table access detected: {keyword.strip()}"
            )

    return True
