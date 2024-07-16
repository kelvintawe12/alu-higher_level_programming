-- This script creates a table called first_table with columns id and name in the specified database
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 4-first_table.sql

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
