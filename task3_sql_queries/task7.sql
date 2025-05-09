-- Вывести категорию фильмов, у которой самое большое кол-во часов суммарной аренды в городах (customer.address_id в этом city), и которые начинаются на букву “a”. То же самое сделать для городов в которых есть символ “-”. Написать все в одном запросе

WITH CategoryRentalInfo AS (
    SELECT 
        category.category_id,
        category.name, 
        rental.rental_date,
        rental.return_date,
        city.city
    FROM 
        category
    LEFT JOIN 
        film_category ON film_category.category_id = category.category_id
    LEFT JOIN
        inventory ON inventory.film_id = film_category.film_id
    LEFT JOIN
        rental ON rental.inventory_id = inventory.inventory_id
    LEFT JOIN
        customer ON customer.customer_id = rental.customer_id
    LEFT JOIN
        address ON address.address_id = customer.address_id
    LEFT JOIN
        city ON city.city_id = address.city_id
)

(SELECT 
    'Starts with a' as criterion,
    info.category_id,
    info.name, 
    SUM(CASE
        WHEN info.return_date IS NOT NULL THEN
            EXTRACT(EPOCH FROM (info.return_date - info.rental_date)) / 3600.0
        ELSE 0
    END) AS rental_hours
FROM 
    CategoryRentalInfo AS info
WHERE
    info.city LIKE 'a%'
GROUP BY 
    info.category_id, 
    info.name
ORDER BY 
    rental_hours DESC
LIMIT 1)

UNION ALL

(SELECT 
    'Contains -' as criterion,
    info.category_id,
    info.name, 
    SUM(CASE
        WHEN info.return_date IS NOT NULL THEN
            EXTRACT(EPOCH FROM (info.return_date - info.rental_date)) / 3600.0
        ELSE 0
    END) AS rental_hours
FROM 
    CategoryRentalInfo AS info
WHERE
    info.city LIKE '%-%'
GROUP BY 
    info.category_id, 
    info.name
ORDER BY 
    rental_hours DESC
LIMIT 1);
