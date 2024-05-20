SELECT name
FROM people
WHERE id IN(
    SELECT director_id
    FROM movies
    WHERE ratings >=9.0
);
