-- This script creates the table force_name with the specified columns.
-- The table will have an id column of type INT and a name column of type VARCHAR(256).
-- If the table already exists, the script will not fail.

-- Use the specified database
USE hbtn_0d_2;

-- Create the table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
