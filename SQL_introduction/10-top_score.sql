-- This script lists all records of the table second_table, ordered by score (top first)
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 10-top_score.sql

SELECT score, name FROM second_table ORDER BY score DESC;
