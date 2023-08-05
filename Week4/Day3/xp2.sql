
set language_id = 2
where film_id in (133, 3);



drop table customer_review;



select count(*) from rental
where return_date is null;


select title, replacement_cost
from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
order by replacement_cost desc
limit 30;


select title from film 
join film_actor on film_actor.film_id = film.film_id
join actor on actor.actor_id = film_actor.actor_id
where actor.first_name = 'Penelope' and actor.last_name = 'Monroe'
and (film.description ilike('%sumo wrestler%'));


select title from film 
join film_category as fc on fc.film_id = film.film_id
join category on category.category_id = fc.category_id
where film.length < 60 and rating = 'R' and category.name ilike 'documentary%';


select title from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
join customer on rental.customer_id = customer.customer_id
where rental.return_date between '2005-07-28' and '2005-08-1' and customer.first_name = 'Matthew'
and customer.last_name = 'Mahan' and film.rental_rate > 4;


select title, replacement_cost from film
join inventory on inventory.film_id = film.film_id
join rental on rental.inventory_id = inventory.inventory_id
join customer on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew'
and customer.last_name = 'Mahan' and (film.description ilike('%boat%') or film.title ilike('%boat%'))
order by replacement_cost desc;