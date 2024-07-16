-- This script removes all records with a score <= 5 in the table second_table
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 13-change_class.sql

DELETE FROM second_table WHERE score <= 5;
