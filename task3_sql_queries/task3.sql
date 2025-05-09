-- Вывести категорию фильмов, на которую потратили больше всего денег

SELECT 
    category.category_id,
    category.name, 
    SUM(payment.amount) as money_amount 
FROM 
    category
LEFT JOIN 
    film_category ON film_category.category_id = category.category_id
LEFT JOIN
    inventory ON inventory.film_id = film_category.film_id
LEFT JOIN
    rental ON rental.inventory_id = inventory.inventory_id
LEFT JOIN 
    payment ON payment.rental_id = rental.rental_id
GROUP BY 
    category.category_id, 
    category.name
ORDER BY 
    money_amount DESC
LIMIT 1;