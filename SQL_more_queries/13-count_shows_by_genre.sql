-- In this task we will list all the genres that have at least one show+ linked
-- This is the script that will list all the shows
SELECT tv_genres.name, count(tv_show_genres.show_id) AS number
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number DESC;
