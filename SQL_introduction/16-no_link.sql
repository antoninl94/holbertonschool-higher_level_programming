-- In This task, we have to only list rows with a name value
-- This script display the list of rows with a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
