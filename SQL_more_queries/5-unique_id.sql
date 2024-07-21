-- Ensure the database hbtn_0d_2 exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the specified database
USE hbtn_0d_2;

-- Create the table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

-- Insert data into the table
INSERT IGNORE INTO unique_id (id, name) VALUES 
(1, 'Holberton School'),
(2, 'Holberton'),
(3, 'School'),
(4, 'C is fun'),
(5, 'Python is cool');
