-- In this task we have to display all the cities contained in the database hbtn_0d_usa
-- This script display all the cities in a given table
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
