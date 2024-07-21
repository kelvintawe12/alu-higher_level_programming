-- This script creates the table id_not_null with the specified columns.
-- The table will have an id column of type INT with a default value of 1
-- and a name column of type VARCHAR(256).
-- If the table already exists, the script will not fail.

-- Use the specified database
USE hbtn_0d_2;

-- Create the table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
