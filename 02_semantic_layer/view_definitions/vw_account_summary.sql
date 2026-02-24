-- Certified Semantic View
-- vw_account_summary

CREATE VIEW vw_account_summary AS
SELECT
    account_id,
    customer_id,
    account_status,
    open_date,
    close_date,
    balance,
    currency
FROM accounts;
