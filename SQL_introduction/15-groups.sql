-- This script lists the number of records with the same score in the table second_table
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 15-groups.sql

SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
