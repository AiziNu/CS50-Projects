SELECT title
FROM (
    SELECT title, person_id
    FROM movies
    JOIN stars ON movies.id = stars.movie_id
    WHERE person_id IN (
        SELECT person_id
        FROM people
        WHERE name = 'Bradley Cooper' OR name = 'Jennifer Lawrence'
    )
) AS subquery
GROUP BY title
HAVING COUNT(DISTINCT person_id) = 2;
