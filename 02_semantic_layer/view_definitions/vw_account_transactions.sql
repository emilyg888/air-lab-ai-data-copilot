-- Certified Semantic View
-- vw_account_transactions

CREATE OR REPLACE VIEW vw_account_transactions AS
SELECT
    a.account_id,
    p.product_category,
    COUNT(t.transaction_id) AS total_count,
    SUM(t.amount) AS total_value
FROM accounts a
JOIN transactions t
    ON a.account_id = t.account_id
JOIN products p
    ON t.product_id = p.product_id
GROUP BY
    a.account_id,
    p.product_category;
