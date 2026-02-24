-- Certified Semantic View
-- vw_daily_transactions

CREATE OR REPLACE VIEW vw_daily_transactions AS
SELECT
    t.transaction_date,
    p.product_category,
    COUNT(*) AS total_count,
    SUM(t.amount) AS total_value
FROM transactions t
JOIN products p
    ON t.product_id = p.product_id
GROUP BY
    t.transaction_date,
    p.product_category;
