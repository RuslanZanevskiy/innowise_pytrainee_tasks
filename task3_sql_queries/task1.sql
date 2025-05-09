-- Вывести количество фильмов в каждой категории, отсортировать по убыванию

SELECT 
    category.category_id,
    category.name, 
    COUNT(film_category.film_id) as count 
FROM 
    category
LEFT JOIN 
    film_category ON film_category.category_id = category.category_id
GROUP BY 
    category.category_id, 
    category.name
ORDER BY 
    count DESC;