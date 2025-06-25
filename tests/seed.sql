INSERT INTO Users (name, role) VALUES
("Alice", "student"),
("Bob", "student"),
("Dr. Smith", "instructor"),
("Charlie", "student");

INSERT INTO Courses (title, instructor_id) VALUES
("SQL Basics", 3),
("Advanced SQL", 3);

INSERT INTO Lessons (course_id, title) VALUES
(1, "SELECT Basics"),
(1, "WHERE Conditions"),
(2, "JOIN Mastery");

INSERT INTO Enrollments (student_id, course_id, enrolled_at) VALUES
(1, 1, "2025-06-01"),
(2, 1, "2025-06-02");

INSERT INTO LessonProgress (student_id, lesson_id, score) VALUES
(1, 1, 90),
(1, 2, 85),
(2, 1, 70);
