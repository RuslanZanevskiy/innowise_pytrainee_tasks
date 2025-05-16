SELECT 
    rooms.name,
    COUNT(students.id) as students_count
FROM rooms
LEFT JOIN students
ON rooms.id = students.room_id
GROUP BY rooms.name;
