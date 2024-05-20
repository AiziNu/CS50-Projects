SELECT name
FROM people
WHERE id IN(
    SELECT director_id
    FROM movies
    WHERE rating >=9.0
);
