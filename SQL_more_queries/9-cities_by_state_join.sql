-- Select cities with their state names using a subquery to get the state name
SELECT c.id, c.name, 
    (SELECT s.name 
     FROM states s 
     WHERE s.id = c.state_id) AS state_name
FROM cities c
ORDER BY c.id ASC;
