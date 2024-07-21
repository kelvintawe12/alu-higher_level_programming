-- This query lists all shows from the database hbtn_0d_tvshows that do not have a genre linked.
-- It selects the show title and the genre_id, displaying NULL for genre_id if no genre is linked.
-- The results are sorted in ascending order by the show title and genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
