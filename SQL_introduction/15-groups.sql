-- In this task we have to count occurence in a given table
-- This script will count occurence in a given tabe
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score;
