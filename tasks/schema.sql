PRAGMA foreign_keys = ON;

-- Реализуйте следующие таблицы:

-- 1. Users
-- id — первичный ключ
-- name — имя пользователя
-- role — строка ('student' | 'instructor')

-- 2. Courses
-- id — первичный ключ
-- title — название курса
-- instructor_id — внешний ключ на Users(id) (только преподаватель может быть владельцем курса)

-- 3. Lessons
-- id — первичный ключ
-- course_id — внешний ключ на Courses(id)
-- title — название урока

-- 4. Enrollments
-- student_id — внешний ключ на Users(id)
-- course_id — внешний ключ на Courses(id)
-- enrolled_at — дата регистрации на курс
-- (Первичный ключ составной: (student_id, course_id))

-- 5. LessonProgress
-- student_id — внешний ключ на Users(id)
-- lesson_id — внешний ключ на Lessons(id)
-- score — числовая оценка от 0 до 100
-- Первичный ключ: (student_id, lesson_id)