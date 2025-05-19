CREATE TABLE IF NOT EXISTS Rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    sex CHAR(1) NOT NULL,
    room_id INT NOT NULL,

    CONSTRAINT fk_student_room
        FOREIGN KEY (room_id)
        REFERENCES Rooms (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
