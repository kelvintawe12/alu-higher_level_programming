-- Ensure the database hbtn_0d_2 exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the specified database
USE hbtn_0d_2;

-- Create the table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
