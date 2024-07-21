-- This query lists all cities along with their corresponding state names
-- from the database hbtn_0d_usa, sorted in ascending order by cities.id
SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id;
