--1. List all customers who live in Texas (use
--JOINs)

select * from customer as a
inner Join address as b
on a.address_id = b.address_id
where b.district = 'Texas';

--2. Get all payments above $6.99 with the Customer's Full
--Name

select concat(b.first_name,' ',b.last_name) as fullname,a.amount 
from payment as a
inner join customer as b
on a.customer_id = b.customer_id
where amount > 6.99;

--3. Show all customers names who have made payments over $175(use
--subqueries)

select concat(first_name,' ',last_name) as fullname
from 
	customer
where 
	customer_id in(
		select 
			customer_id 
		from 
			payment 
		group by 
			customer_id
		having sum(amount)>175);



--4. List all customers that live in Nepal (use the city
--table)

select first_name,last_name from customer as a
inner join address as b 
on a.address_id=b.address_id
inner join city as c
on b.city_id = c.city_id
inner join country as d
on c.country_id = d.country_id
where d.country = 'Nepal'


--5. Which staff member had the most
--transactions?
select * 
from staff 
where staff_id in
(select a.staff_id
from rental as a
group by staff_id
order by count(a.rental_id) desc limit 1)

--6. What film had the most actors in it?
-- on my life I have never heard of this film
--but 0 chance oppenheimer doesn't have 90 plus actors in it now lmao
select title,description from film
where film_id in
(select a.film_id
from film_actor as a
group by a.film_id
order by count(a.actor_id) desc limit 1)

--7.Show all customers who have made a single payment
--above $6.99 (Use Subqueries)

select concat(b.first_name,' ',b.last_name) as fullname
from customer as b
where customer_id in
(select customer_id from payment
where amount>6.99)

--8. Which category is most prevalent in the
--films?

select name from category
where category_id in
(select a.category_id
from film_category as a
group by a.category_id
order by count(a.film_id) desc limit 1)