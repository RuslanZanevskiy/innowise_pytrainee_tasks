-- Вывести 10 актеров, чьи фильмы большего всего арендовали, отсортировать по убыванию

SELECT 
    actor.actor_id,   
    actor.first_name, 
    COUNT(rental.rental_id) as rental_count 
FROM 
    actor
LEFT JOIN 
    film_actor ON film_actor.actor_id = actor.actor_id
LEFT JOIN
    inventory ON inventory.film_id = film_actor.film_id
LEFT JOIN
    rental ON rental.inventory_id = inventory.inventory_id
GROUP BY 
    actor.actor_id,
    actor.first_name
ORDER BY 
    rental_count DESC
LIMIT 10;