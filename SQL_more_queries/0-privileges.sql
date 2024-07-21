-- This script ensures user_0d_1 exists, assigns the necessary privileges,
-- and then lists the grants for verification.

-- Check if user_0d_1 exists and drop it if necessary
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Recreate user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Make sure to flush privileges to apply changes
FLUSH PRIVILEGES;

-- List all privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
