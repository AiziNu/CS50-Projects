SELECT title
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM stars
    WHERE person_id IN (
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper' OR name = 'Jennifer Lawrence'
    )
)
GROUP BY title
HAVING COUNT(DISTINCT actor_id) = 2;
