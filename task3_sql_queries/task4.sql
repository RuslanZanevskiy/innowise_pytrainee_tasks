-- Вывести названия фильмов, которых нет в inventory. Написать запрос без использования оператора IN

SELECT 
    film.title
FROM
    film
WHERE NOT EXISTS (
    SELECT 1
    FROM inventory
    WHERE inventory.film_id = film.film_id 
);
