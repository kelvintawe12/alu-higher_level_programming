-- This script lists all records of the table second_table excluding rows without a name
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 16-no_link.sql

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
