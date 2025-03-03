-- In this task we will list all records with score >= 10
-- This is the script to list all records where score is >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
