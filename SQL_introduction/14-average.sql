-- This script computes the average score of all records in the table second_table
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 14-average.sql

SELECT AVG(score) AS average FROM second_table;
