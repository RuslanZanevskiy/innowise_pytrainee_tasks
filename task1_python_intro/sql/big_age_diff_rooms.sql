SELECT 
    rooms.name,
    MAX(students.birthday) - MIN(students.birthday) as age_diff
FROM rooms
INNER JOIN students
ON rooms.id = students.room_id
GROUP BY rooms.name
ORDER BY age_diff DESC 
LIMIT 5;
