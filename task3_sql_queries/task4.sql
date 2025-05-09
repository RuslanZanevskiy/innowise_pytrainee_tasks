-- Вывести названия фильмов, которых нет в inventory. Написать запрос без использования оператора IN

SELECT 
    film.title
FROM
    film
LEFT JOIN
    inventory ON inventory.film_id = film.film_id
WHERE
    inventory.inventory_id IS NULL;