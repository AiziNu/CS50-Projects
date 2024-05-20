SELECT name
FROM people
WHERE id IN(
    SELECT director_id
    FROM directors
    WHERE movie_id IN(
        SELECT id
        FROM movie
        
    ) >=9.0
);
