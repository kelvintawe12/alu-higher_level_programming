-- This script updates Bob's score to 10 in the table second_table
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 12-no_cheating.sql

UPDATE second_table SET score = 10 WHERE name = 'Bob';
