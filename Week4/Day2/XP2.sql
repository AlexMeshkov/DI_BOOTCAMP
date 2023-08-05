
-- select * from customer;

-- select concat(first_name, ' ', last_name) as full_name from customer;



-- select distinct(create_date) from customer;


-- select * from customer
-- ORDER BY first_name;

-- select film_id, title, description, release_year, rental_rate from film
-- order by rental_rate ASC;


-- select address, phone from address
-- where district = 'Texas';


-- select * from film
-- WHERE film_id in (15, 150);

-- select film_id, title, description, length, rental_rate from film
-- where title = 'Snatch';

-- select film_id, title, description, length, rental_rate from film
-- where title LIKE 'Sn%';

-- select * from film
-- order by rental_rate, title ASC
-- LIMIT 10;

-- select * from film
-- order by rental_rate, title ASC
-- OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

-- select C.first_name, C.last_name, P.amount, P.payment_date from customer as C
-- join payment as P on C.customer_id = P.customer_id
-- order by P.payment_id;

-- select F.title from film as F
-- LEFT JOIN inventory on F.film_id = inventory.film_id
-- where inventory.film_id IS NULL;

select city.city, country.country from city
join country on city.country_id = country.country_id;
