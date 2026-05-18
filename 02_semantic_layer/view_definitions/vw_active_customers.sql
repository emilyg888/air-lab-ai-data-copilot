-- Certified Semantic View
-- vw_active_customers

CREATE OR REPLACE VIEW vw_active_customers AS
SELECT
    c.customer_id,
    c.segment,
    c.status,
    c.onboard_date,
    COUNT(a.account_id) AS open_account_count
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE c.status = 'ACTIVE'
  AND a.account_status = 'OPEN'
GROUP BY
    c.customer_id,
    c.segment,
    c.status,
    c.onboard_date;
