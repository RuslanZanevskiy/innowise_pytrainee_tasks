SELECT 
    rooms.name,
    EXTRACT(DAY FROM AVG(now() - students.birthday))::INT as mean_age_in_days
FROM rooms
INNER JOIN students
ON rooms.id = students.room_id
GROUP BY rooms.name
ORDER BY mean_age_in_days ASC
LIMIT 5;
