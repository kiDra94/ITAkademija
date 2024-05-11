CREATE FUNCTION `movie_over_2_hours` (id_film INT)
RETURNS TINYINT(1) 
BEGIN
DECLARE film_duration INT;

SELECT length INTO film_duration
FROM film
WHERE film_id = id_film;

IF film_duration > 120 THEN RETURN TRUE; END IF;
IF film_duration < 120 THEN RETURN FALSE; END IF;

END