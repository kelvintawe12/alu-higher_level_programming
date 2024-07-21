-- This script creates the users 'user_0d_1' and 'user_0d_2' if they do not exist,
-- grants them all privileges, and then lists their privileges.
-- Ensure to execute this script with appropriate privileges.

-- Create user_0d_1 and user_0d_2 if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant all privileges to user_0d_1 and user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- List all privileges for user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
