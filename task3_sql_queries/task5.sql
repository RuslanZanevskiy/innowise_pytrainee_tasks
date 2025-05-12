-- Вывести топ 3 актеров, которые больше всего появлялись в фильмах в категории “Children”. Если у нескольких актеров одинаковое кол-во фильмов, вывести всех

SELECT 
    actor_id,   
    first_name, 
    last_name
FROM (
    SELECT 
        actor.actor_id,   
        actor.first_name, 
        actor.last_name, 
        DENSE_RANK() 
            OVER (ORDER BY COUNT(film_category.film_id) DESC) 
        AS dense_rank
    FROM 
        actor
    LEFT JOIN 
        film_actor ON film_actor.actor_id = actor.actor_id
    LEFT JOIN 
        film_category ON film_category.film_id = film_actor.film_id
    LEFT JOIN 
        category ON category.category_id = film_category.category_id
    WHERE
        category.name = 'Children'
    GROUP BY 
        actor.actor_id,
        actor.first_name,
        actor.last_name
) AS RankedActors
WHERE dense_rank <= 3;