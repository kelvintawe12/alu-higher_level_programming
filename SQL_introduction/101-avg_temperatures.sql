SELECT city, AVG(temperature) AS avg_temp
FROM actual_table_name  -- Replace with the actual table name
GROUP BY city
ORDER BY avg_temp DESC;
