-- Find the state_id for California and list all cities in that state, excluding the state_id column from the result
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
