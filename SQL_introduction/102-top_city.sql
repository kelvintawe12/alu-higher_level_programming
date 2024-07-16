-- This script displays the top 3 cities by average temperature during July and August
-- Replace `temperature_table` with the actual table name containing temperature data

SELECT city, AVG(temperature) AS avg_temp
FROM temperature_table  -- Replace with the actual table name
WHERE MONTH(date) IN (7, 8)  -- Assuming there's a date column
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
