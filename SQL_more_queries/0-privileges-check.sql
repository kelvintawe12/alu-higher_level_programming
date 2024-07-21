SELECT IF(EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'), 'EXISTS', 'DOES NOT EXIST') AS 'User_0d_1 Status';
SELECT IF(EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'), 'EXISTS', 'DOES NOT EXIST') AS 'User_0d_2 Status';
