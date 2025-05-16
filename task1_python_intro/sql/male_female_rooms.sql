SELECT 
    rooms.name
FROM rooms
WHERE EXISTS (
    SELECT 1
    FROM students
    WHERE students.room_id = rooms.id AND students.sex = 'M'
) AND EXISTS (
    SELECT 1
    FROM students
    WHERE students.room_id = rooms.id AND students.sex = 'F'
);
