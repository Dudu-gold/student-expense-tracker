SELECT category,
       SUM(amount) AS total_spent
FROM expenses
GROUP BY category
ORDER BY total_spent DESC;