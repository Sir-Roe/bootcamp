--Customer table
CREATE TABLE IF NOT EXISTS customer(
	customer_id SERIAL PRIMARY KEY, 
	first_name VARCHAR(100),
	last_name VARCHAR(100)
);

--Movie table
CREATE TABLE IF NOT EXISTS movies(
	movie_id SERIAL PRIMARY KEY, 
	movie_name VARCHAR(100),
	movie_category VARCHAR(50)
);

--Ticket table
CREATE TABLE IF NOT EXISTS ticket(
	ticket_id SERIAL PRIMARY KEY,
	movie_date_time timestamp without time zone,
	price NUMERIC(5,2),
    customer_id INTEGER NOT NULL,
	movie_id INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);


--Product table
CREATE TABLE IF NOT EXISTS product(
	product_id SERIAL PRIMARY KEY, 
	prod_name VARCHAR(100),
    prod_desc VARCHAR(100),
	sales_price NUMERIC(5,2)
);

--concessions_order
CREATE TABLE IF NOT EXISTS concessions_order(
	order_id SERIAL PRIMARY KEY,
	sub_total NUMERIC(5,2),
	total_cost NUMERIC(5,2),
    customer_id INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

--order_item table (contains the line data for the concessions order)
CREATE TABLE IF NOT EXISTS order_item(
    quantity INTEGER,
	sales_amount NUMERIC(5,2),
    order_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	FOREIGN KEY(order_id) REFERENCES concessions_order(order_id),
	FOREIGN KEY(product_id) REFERENCES product(product_id)
);

-------------Bulk Insert Section--------------------------------

------Customers first
INSERT INTO customer(customer_id,first_name,last_name)
VALUES
  (1,'Trevor','Something'),
  (2,'John','Doe'),
  (3,'Andy','Travis'),
  (4,'Sara','Parker'),
  (5,'Jessica','Smith'),
  (6,'Alyssa','Niels'),
  (7,'Gandalf','Gray');

------Movies Second
INSERT INTO movies(movie_id,movie_name,movie_category)
VALUES
  (1,'Jaws','Horror'),
  (2,'Barbie','Comedy'),
  (3,'DREDD','Action'),
  (4,'Harry Potter 7','Fantasy'),
  (5,'Oppenheimer','Historical-Thriller');


---tickets-- to check for key restraints

INSERT INTO ticket(ticket_id,price,movie_date_time,customer_id,movie_id)
VALUES
(1,7.99,'2023-08-01 13:00:00',4,5),
(2,7.99,'2023-08-01 14:00:00',7,1),
(3,7.99,'2023-08-01 15:00:00',6,4),
(4,10.99,'2023-08-01 16:00:00',3,5),
(5,10.99,'2023-08-01 17:00:00',5,2),
(6,7.99,'2023-08-02 13:00:00',4,5),
(7,7.99,'2023-08-02 14:00:00',2,4),
(8,7.99,'2023-08-02 15:00:00',1,2),
(9,10.99,'2023-08-02 16:00:00',6,1),
(10,10.99,'2023-08-02 17:00:00',3,3),
(11,10.99,'2023-08-02 18:00:00',7,3);


--- Insert into products
INSERT INTO product(product_id,prod_name,prod_desc,sales_price)
VALUES
  (1,'Popcorn1','20oz bag of popcorn',5.99),
  (2,'Popcorn2','40oz bag of popcorn',7.99),
  (3,'Popcorn3','Bucket of popcorn',8.99),
  (4,'SodaL','20oz Fountain Drink',3.99),
  (5,'SodaXl','32oz Fountain Drink',5.99);


----- insert into concession_orders
INSERT INTO concessions_order(order_id,sub_total,total_cost,customer_id)
VALUES
(1,7.99,8.79,4),
(2,7.99,8.79,7),
(3,7.99,8.79,6),
(4,10.99,12.09,3),
(5,10.99,12.09,5),
(6,7.99,8.79,4),
(7,7.99,8.79,2),
(8,7.99,8.79,1),
(9,10.99,12.09,6),
(10,10.99,12.09,3),
(11,10.99,12.09,7);

---- order_item

---- random dummy data for order_items
INSERT INTO order_item(quantity,sales_amount,order_id,product_id)
VALUES
(1,7.99,1,4),
(2,14.99,2,4),
(3,21.99,3,2),
(2,10.99,4,2),
(1,10.99,5,2),
(3,7.99,6,2),
(1,7.99,7,2),
(1,7.99,8,4),
(2,10.99,9,4),
(1,10.99,10,3),
(3,10.99,11,3),
(1,7.99,1,5),
(2,14.99,2,3),
(3,21.99,3,4),
(2,10.99,4,3),
(1,10.99,5,5),
(3,7.99,6,5),
(1,7.99,7,1),
(1,7.99,8,2),
(2,10.99,9,3),
(1,10.99,10,1),
(3,10.99,11,4),
(1,7.99,1,3),
(2,14.99,2,1),
(3,21.99,3,3),
(2,10.99,4,1),
(1,10.99,5,3),
(3,7.99,6,2),
(1,7.99,7,3),
(1,7.99,8,3),
(2,10.99,9,3),
(1,10.99,10,4),
(3,10.99,11,5);


--- fix my dummy data to make subtotal be the sum based on the order_item table
UPDATE  concessions_order
SET     sub_total = (select b.col2
					from (select order_id,sum(sales_amount) as "col2" from order_item group by order_id)as b
					where concessions_order.order_id = b.order_id);
--fix the dummy data to make the total cost reflect 10% sales tax					
UPDATE  concessions_order
SET     total_cost = sub_total*1.1;				
-- check work, looked good!		
select * from concessions_order

