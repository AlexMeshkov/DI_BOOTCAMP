
select name from language;



select f.title, f.description, l.name from film as f
join language as l on f.language_id = l.language_id;


select f.title, f.description, l.name from film as f
left join language as l on f.language_id = l.language_id;

select f.title, f.description, l.name from film as f
right join language as l on f.language_id = l.language_id;



create table new_film (
	id serial primary key,
	name varchar(30) not null
);

insert into new_film(name)
values 
('Drunken Master'),
('All Quiet on the Western Front'),
('Ghost in the Shell');


-
create table customer_review(
	review_id serial primary key,
	film_id integer references new_film(id) on delete cascade,
	language_id integer references language(language_id),
	title varchar(30) not null,
	score smallint check(between 1 and 10),
	review_text text not null,
	last_update date
);

insert into customer_review(film_id, language_id, title, score, review_text, last_update)
values (2, 6, 'The harsh reality of WWI', 7, 'HUGE TEXT', '2023-03-16'),
 	(3, 3, 'What future are we heading to?', 9, 'HUGE TEXT ABOUT DYSTOPIA', '2018-04-18');



delete from new_film where id = 2;


select * from customer_review;