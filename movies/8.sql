SELECT name
FROM people
WHERE id IN(
    SELECT person_id
    FROM roles
    WHERE movie_id =(
        SELECT id
        FROM movies
        WHERE title = 'Toy Story'
    )
);
