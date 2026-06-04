-- 1. Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Total transactions by fund
SELECT amfi_code, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY amfi_code;

-- 4. Total investment amount by fund
SELECT amfi_code, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY amfi_code;

-- 5. Average expense ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- 6. Funds with expense ratio less than 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Top 5 funds by 5-year return
SELECT amfi_code, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 8. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average investment amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 10. Highest NAV recorded
SELECT amfi_code, MAX(nav)
FROM fact_nav
GROUP BY amfi_code;