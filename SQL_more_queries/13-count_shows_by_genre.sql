-- This query lists all genres from the database hbtn_0d_tvshows and displays the number of shows linked to each genre.
-- Each record displays the genre name and the number of shows linked to it.
-- The results are sorted in descending order by the number of shows linked.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
