"""
Deterministic SQL builder.
No model-generated SQL allowed.
"""

def build_sql(view_name: str, question: str) -> str:
    """
    Build SQL for a certified semantic view.
    Only predefined templates are allowed.
    """

    if view_name == "vw_daily_transactions":
        return """
        SELECT
            transaction_date,
            product_category,
            SUM(total_count) AS total_count,
            SUM(total_value) AS total_value
        FROM vw_daily_transactions
        GROUP BY transaction_date, product_category
        ORDER BY transaction_date DESC
        LIMIT 5
        """

    if view_name == "vw_account_summary":
        return """
        SELECT
            account_id,
            product_category,
            balance,
            currency
        FROM vw_account_summary
        ORDER BY balance DESC
        LIMIT 5
        """

    if view_name == "vw_active_customers":
        return """
        SELECT
            segment,
            COUNT(customer_id) AS active_customer_count
        FROM vw_active_customers
        GROUP BY segment
        ORDER BY active_customer_count DESC
        """

    if view_name == "vw_account_transactions":
        return """
        SELECT
            account_id,
            product_category,
            total_count,
            total_value
        FROM vw_account_transactions
        ORDER BY total_value DESC
        LIMIT 10
        """

    raise ValueError(f"No SQL template defined for view: {view_name}")
