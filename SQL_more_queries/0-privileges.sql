-- Create users
CREATE USER 'user_0d_1'@'localhost';
CREATE USER 'user_0d_2'@'localhost';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Grant all privileges to user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
