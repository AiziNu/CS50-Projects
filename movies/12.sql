SELECT title
FROM (
    SELECT m.title, COUNT(*) AS num_actors
    FROM movies m
    JOIN stars s ON m.id = s.movie_id
    JOIN people p ON s.person_id = p.id
    WHERE p.name IN ('Bradley Cooper', 'Jennifer Lawrence')
    GROUP BY m.title
) AS subquery
WHERE num_actors = 2;
