-- This script displays the number of records with id = 89 in the table first_table in the specified database
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 8-count_89.sql

SELECT COUNT(*) FROM first_table WHERE id = 89;
