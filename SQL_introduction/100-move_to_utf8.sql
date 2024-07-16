-- This script converts the hbtn_0c_0 database to UTF8 (utf8mb4)
-- Usage: mysql -hlocalhost -uroot -p <database_name> < 100-move_to_utf8.sql

-- Convert the database character set
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table first_table character set
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the field name in first_table
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
