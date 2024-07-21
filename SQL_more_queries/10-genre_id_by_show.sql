-- This query lists all shows from the database hbtn_0d_tvshows that have at least one genre linked.
-- Each record displays the show title and the genre_id.
-- The results are sorted in ascending order by the show title and genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
