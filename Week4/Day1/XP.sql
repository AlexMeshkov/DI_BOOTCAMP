CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	item VARCHAR(50),
	price FLOAT (50)
);
CREATE TABLE customers(
	first_name VARCHAR (50),
	last_name VARCHAR(100)
);

INSERT INTO items(item, price)
VALUES ('Small Desk',100),
('Large desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson')

SELECT * from items;

SELECT * from items WHERE price > 80 ;

SELECT * from items WHERE price <= 300;

SELECT * from customers WHERE last_name LIKE 'Smit';

SELECT * from customers WHERE last_name LIKE 'Jones';

SELECT * from customers WHERE last_name NOT LIKE 'Scott';

