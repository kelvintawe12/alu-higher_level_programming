-- This query lists all genres of the show Dexter from the database hbtn_0d_tvshows.
-- It selects the name of genres where the show title is Dexter.
-- The results are sorted in ascending order by the genre name.

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
