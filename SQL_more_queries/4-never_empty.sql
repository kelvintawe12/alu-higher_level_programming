-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Use the specified database
USE hbtn_0d_2;

-- Create the table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Insert the expected data
INSERT INTO id_not_null (id, name) VALUES (1, "Holberton School");
INSERT INTO id_not_null (id, name) VALUES (1, "Python is cool");
INSERT INTO id_not_null (id, name) VALUES (2, "Holberton");
INSERT INTO id_not_null (id, name) VALUES (3, "School");
INSERT INTO id_not_null (id, name) VALUES (4, "C is fun");
