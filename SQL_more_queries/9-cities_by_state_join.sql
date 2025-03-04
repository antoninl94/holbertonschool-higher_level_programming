-- In this task we have to list all the cities contained in the database
-- This script provide to list all the cities contained in a given database
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
