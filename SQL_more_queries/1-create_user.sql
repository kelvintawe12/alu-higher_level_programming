-- This script creates the MySQL user user_0d_1 with all privileges.
-- The user is given the password user_0d_1_pwd.
-- If the user already exists, the script will not fail.

-- Create the user user_0d_1 if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1 on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Make sure to flush privileges to apply changes
FLUSH PRIVILEGES;
