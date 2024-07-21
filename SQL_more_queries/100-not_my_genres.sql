-- Select the ID of the show "Dexter"
SELECT @dexter_id := id FROM tv_shows WHERE title = 'Dexter';

-- List all genres not linked to the show "Dexter"
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = @dexter_id
)
ORDER BY name ASC;
