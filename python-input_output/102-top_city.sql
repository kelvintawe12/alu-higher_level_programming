-- Calculate and display the top 3 cities by average temperature during July and August
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
