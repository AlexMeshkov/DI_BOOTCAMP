-- CREATE TABLE students(
-- 	id SERIAL PRIMARY KEY,
-- 	last_name VARCHAR(50) NOT NULL,
-- 	first_name VARCHAR (50) NOT NULL,
-- 	birth_date DATE NOT NULL)

-- INSERT INTO students (last_name, first_name, birth_date)
-- 	VALUES 
-- 		('Benichu', 'Mark', '02/11/1998'),
-- 		('Cohen', 'Yoan', '03/12/2010'),
-- 		('Benichu', 'Lea', '07/07/1987'),
-- 		('Dux', 'Amelia', '07/04/1996'),
-- 		('Grez', 'David', '10/06/2003'),
-- 		('Simpson', 'Omer', '03/10/1980');

-- SELECT * FROM students;

-- SELECT first_name, last_name FROM students;

-- SELECT * FROM students WHERE id =2;

-- SELECT * FROM students WHERE last_name = 'Benichu' and first_name = 'Mark'

-- SELECT * FROM students WHERE first_name LIKE '%a%';

-- SELECT first_name FROM students WHERE first_name LIKE '%A%';

-- SELECT first_name FROM students WHERE first_name ilike '%a';

-- SELECT first_name, last_name FROM students WHERE (RIGHT(first_name, 2) LIKE 'a%')

-- SELECT first_name, last_name FROM students WHERE (id= 1) and (id =3)

SELECT * FROM students WHERE birth_DATE >='01/01/2000'
