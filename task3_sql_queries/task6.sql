-- Вывести города с количеством активных и неактивных клиентов (активный — customer.active = 1). Отсортировать по количеству неактивных клиентов по убыванию

SELECT 
    city.city_id,
    city.city, 
    COUNT(customer.customer_id) - COALESCE(SUM(customer.active), 0)
    as count_inactive
FROM 
    city
LEFT JOIN 
    address ON address.city_id = city.city_id
LEFT JOIN 
    customer ON customer.address_id = address.address_id
GROUP BY 
    city.city_id,
    city.city
ORDER BY 
    count_inactive DESC;