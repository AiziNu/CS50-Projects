SELECT name
FROM people
WHERE id IN(
    SELECT person_id
    FROM stars
    WHERE movie_id = (
        SELECT id
        FROM movies
        WHERE year = 2004
    )
)
AND birth_year IS NOT NULL
ORDER BY birth_year;
