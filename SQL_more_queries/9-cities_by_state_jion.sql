-- This query lists all cities from the database hbtn_0d_usa along with their corresponding state names.
-- Each record displays the city ID, city name, and state name.
-- The results are sorted in ascending order by the city ID.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
