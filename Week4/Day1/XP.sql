CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	item VARCHAR(50) NOT NULL,
	price INTEGER NOT NULL
);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (100) NOT NULL,
	last_name VARCHAR(100) NOT NULL
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

SELECT * from customers WHERE last_name='Smit';

SELECT * from customers WHERE last_name='Jones';

SELECT * from customers WHERE last_name NOT LIKE 'Scott';

