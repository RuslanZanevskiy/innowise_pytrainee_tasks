CREATE INDEX IF NOT EXISTS idx_students_room_id ON Students (room_id);
CREATE INDEX IF NOT EXISTS idx_students_room_id_sex ON Students (room_id, sex);
