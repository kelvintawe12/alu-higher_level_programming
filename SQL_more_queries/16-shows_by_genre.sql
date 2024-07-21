-- This query lists all shows and their associated genres from the database hbtn_0d_tvshows.
-- If a show does not have a genre, it displays NULL in the genre column.
-- The results are sorted in ascending order by the show title and genre name.

-- Select the title of the show and the name of the genre
SELECT tv_shows.title, tv_genres.name
-- From the tv_shows table
FROM tv_shows
-- Left join with tv_show_genres to get the association between shows and genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Left join with tv_genres to get the genre names
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Order the results by show title and genre name in ascending order
ORDER BY tv_shows.title, tv_genres.name;
