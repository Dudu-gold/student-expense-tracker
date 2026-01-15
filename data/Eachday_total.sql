SELECT DATE(datetime) AS day,
       SUM(amount) AS total_spent
FROM expenses
GROUP BY DATE(datetime)
ORDER BY total_spent DESC


