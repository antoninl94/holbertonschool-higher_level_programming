-- In this task we will lists all shows,
-- and all genres linked to that show, from the database
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT OUTER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
