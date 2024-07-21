-- This query lists all cities along with their corresponding state names
-- from the database hbtn_0d_usa, sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
