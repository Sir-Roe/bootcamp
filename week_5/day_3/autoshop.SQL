--I created a new postgres database and ran this entire 
--section of code and it works, so you should be able to
--do the same and validate on your end should you choose.


--employee table
CREATE TABLE IF NOT EXISTS employee(
	emp_id SERIAL PRIMARY KEY, 
	emp_first_name VARCHAR(100),
	emp_last_name VARCHAR(100),
    emp_email varchar(150)
);

--customer table
CREATE TABLE IF NOT EXISTS customer(
	customer_id SERIAL PRIMARY KEY, 
	first_name VARCHAR(100),
	last_name VARCHAR(100),
    email VARCHAR(150)
);

--car table
CREATE TABLE IF NOT EXISTS car(
	car_id SERIAL PRIMARY KEY,
	make VARCHAR(50),
	model VARCHAR(50),
    car_year INTEGER,
	mileage NUMERIC(12,2),
    car_color varchar(25)
);

---- create customer car ownership 
CREATE TABLE IF NOT EXISTS customer_car(
   customer_id INTEGER NOT NULL,
   car_id INTEGER NOT NULL,
   FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
   FOREIGN KEY(car_id) REFERENCES car(car_id),
   PRIMARY KEY(customer_id,car_id) 
);

--- sales_invoice
--- add constraint that a car can only be sold once
--  populate with procedure

CREATE TABLE IF NOT EXISTS sales_invoice(
   invoice_no SERIAL PRIMARY KEY,
   customer_id INTEGER NOT NULL,
   car_id INTEGER NOT NULL,
   emp_id INTEGER NOT NULL,
   sales_date DATE,
   sales_amount NUMERIC(10,2),
   FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
   FOREIGN KEY(car_id) REFERENCES car(car_id),
   FOREIGN KEY(emp_id) REFERENCES employee(emp_id),
   CONSTRAINT singlesell UNIQUE(car_id)
);

--I did not add customer here assuming we could join it with car_id 
--from customer car. this would maybe create a real world issue if 
--someone took your car in and paid for your service work? idk.
--service invoice
CREATE TABLE IF NOT EXISTS service_invoice(
   service_no SERIAL PRIMARY KEY,
   car_id INTEGER NOT NULL,
   service_type VARCHAR(100),
   sales_date DATE,
   service_amount DECIMAL(12,2),
   FOREIGN KEY(car_id) REFERENCES car(car_id)
);


CREATE TABLE IF NOT EXISTS service_work(
   service_no INTEGER NOT NULL,
   emp_id INTEGER NOT NULL,
   FOREIGN KEY(emp_id) REFERENCES employee(emp_id)
);


-------------Bulk Insert Section--------------------------------

------Customers first
INSERT INTO customer(first_name,last_name,email)
VALUES
('Kenyon','Preston','interdum.feugiat@aol.couk'),
('Burke','Hernandez','ante.nunc@aol.couk'),
('Abra','Carey','at@outlook.ca'),
('Chadwick','Nichols','dui.quis@icloud.ca'),
('Cade','Salinas','semper.rutrum@hotmail.ca'),
('Leilani','Pearson','eu.elit@outlook.com'),
('Hu','Thomas','urna@icloud.org'),
('Beatrice','Tran','nulla.facilisis@outlook.org'),
('Montana','English','lacus@hotmail.com'),
('Grace','Farley','posuere@yahoo.com'),
('Wade','Nielsen','pulvinar.arcu@aol.ca'),
('Wynter','Young','amet.consectetuer.adipiscing@outlook.couk'),
('Hiram','Munoz','nunc.lectus@hotmail.net'),
('Cody','Silva','nec.metus@yahoo.net'),
('Roary','Harding','elit.pede.malesuada@outlook.edu'),
('Dieter','Cabrera','ipsum.curabitur@yahoo.net'),
('Rhonda','Lowery','sem@aol.com'),
('Timothy','Hutchinson','in@outlook.org'),
('Jolene','Cline','mi.fringilla.mi@aol.couk'),
('Meredith','Fry','ut.cursus@yahoo.couk'),
('Morgan','Jimenez','dui@hotmail.org'),
('Eve','Glass','dui.nec@protonmail.couk'),
('Yetta','Reynolds','amet.dapibus.id@icloud.net'),
('Hermione','Landry','lacinia.mattis.integer@outlook.org'),
('Dominique','Kent','natoque@hotmail.ca'),
('Hayes','Nelson','enim.consequat@google.net'),
('Ainsley','Shaffer','lectus.quis@aol.ca'),
('Yoshi','Schultz','non.bibendum@hotmail.com'),
('Boris','Nicholson','volutpat.nulla@aol.ca'),
('Morgan','Vinson','phasellus@yahoo.edu'),
('Jillian','Gillespie','lacus.quisque@yahoo.edu'),
('Demetria','Stokes','pellentesque.a@outlook.edu'),
('Camden','Gardner','arcu.sed.et@yahoo.org'),
('Linus','Newman','sapien@protonmail.edu'),
('Eric','Lancaster','dui.lectus.rutrum@yahoo.org'),
('Fulton','Price','mauris.blandit@yahoo.com'),
('Isaiah','Whitney','aliquam.fringilla@outlook.edu'),
('Bert','Prince','nec.mollis@google.com'),
('Mallory','Vega','ligula.donec.luctus@aol.edu'),
('Heidi','Burton','amet@aol.couk'),
('Raphael','Murphy','fringilla.porttitor.vulputate@outlook.ca'),
('Xyla','Palmer','magna.et@icloud.org'),
('Kimberly','Preston','aliquam.erat@hotmail.ca'),
('Clark','Foreman','at@outlook.ca'),
('Ahmed','Sears','urna.nec.luctus@icloud.couk'),
('Lani','Fowler','dictum@yahoo.com'),
('Drake','George','ut.nec.urna@aol.net'),
('Suki','Vazquez','in.scelerisque@icloud.ca'),
('Kameko','Molina','dui.augue@google.couk'),
('Clayton','Cooper','sodales.elit@outlook.com');


----------employee data insert
INSERT INTO employee(emp_first_name,emp_last_name,emp_email)
VALUES
('Chaney','Stokes','ut.quam.vel@aol.ca'),
('Brady','Bolton','tristique@yahoo.ca'),
('Erin','Richmond','lacus.etiam@yahoo.net'),
('Plato','Nguyen','dolor.fusce@icloud.net'),
('Breanna','Brewer','in.mi.pede@icloud.net'),
('Sebastian','Mann','nam.consequat@icloud.com'),
('Amaya','Whitfield','nisi.aenean@icloud.com'),
('Laith','Stein','id.nunc@icloud.couk'),
('Lawrence','Guzman','praesent@hotmail.ca'),
('Ciaran','Mcconnell','purus.in@icloud.edu'),
('Stewart','Marsh','quisque.imperdiet.erat@outlook.edu'),
('Carlos','Rich','luctus.et.ultrices@protonmail.org'),
('Steel','Morrison','ligula@hotmail.edu'),
('Giselle','Valentine','eros.nam@google.edu'),
('Cara','Duffy','non.nisi@icloud.org'),
('Emerson','Winters','amet@google.com'),
('Chadwick','Peterson','turpis.non@outlook.net'),
('Rachel','Harper','enim.nec@aol.couk'),
('Oliver','Barnes','ultricies@icloud.org'),
('Raymond','Hudson','lectus.ante@yahoo.com'),
('Phillip','Dean','elit.pretium.et@yahoo.ca'),
('Kane','Romero','vel.faucibus@hotmail.com'),
('Acton','Boyer','vestibulum.ante@aol.edu'),
('April','Bradford','vulputate.lacus@yahoo.org'),
('Neville','Levine','et.arcu@outlook.couk'),
('Morgan','Shelton','non.luctus.sit@icloud.couk'),
('Jack','Shaw','viverra@yahoo.ca'),
('Fulton','Mcdonald','laoreet@aol.couk'),
('Kieran','Wooten','ipsum.phasellus.vitae@icloud.edu'),
('Charissa','Wyatt','vitae@outlook.org'),
('Kadeem','Gordon','pede.nec@google.net'),
('Magee','Zamora','hendrerit@hotmail.org'),
('Karen','Acevedo','magna@hotmail.net'),
('Pamela','West','ut.cursus@aol.com'),
('Roth','Herman','fringilla.porttitor@icloud.com'),
('Edan','Lang','libero.morbi@protonmail.org'),
('Azalia','Madden','sapien.imperdiet@hotmail.ca'),
('Dara','Hester','sapien.cras@outlook.couk'),
('Pascale','Vinson','ullamcorper@protonmail.edu'),
('Bert','Townsend','purus@outlook.org'),
('Tarik','Kramer','ac@icloud.com'),
('Candice','Howard','a.neque.nullam@google.edu'),
('Denton','Bridges','lectus.quis@outlook.edu'),
('Amelia','Pitts','elit.sed@hotmail.edu'),
('Linus','Humphrey','lacinia.mattis.integer@hotmail.ca'),
('Ross','Wall','magnis.dis@hotmail.org'),
('Moses','Hutchinson','lorem.auctor@hotmail.edu'),
('Regan','Grant','tortor.at@protonmail.ca'),
('Wesley','Foster','sapien@protonmail.com'),
('Hayden','Mcknight','quam.curabitur@hotmail.edu');

----- car dummy data insert, utilized mockaroo for this, actually an awesomne website

insert into car (make, model, car_year, mileage, car_color) values ('Lexus', 'IS-F', 2011, 174967, 'Fuscia');
insert into car (make, model, car_year, mileage, car_color) values ('Hummer', 'H3T', 2009, 212104, 'Turquoise');
insert into car (make, model, car_year, mileage, car_color) values ('Bentley', 'Continental Flying Spur', 2007, 144940, 'Blue');
insert into car (make, model, car_year, mileage, car_color) values ('GMC', 'Sonoma Club Coupe', 1994, 215140, 'Yellow');
insert into car (make, model, car_year, mileage, car_color) values ('BMW', '7 Series', 2010, 331193, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Isuzu', 'Trooper', 1992, 142349, 'Crimson');
insert into car (make, model, car_year, mileage, car_color) values ('Aston Martin', 'V8 Vantage', 2012, 117851, 'Maroon');
insert into car (make, model, car_year, mileage, car_color) values ('Toyota', 'MR2', 1993, 161422, 'Teal');
insert into car (make, model, car_year, mileage, car_color) values ('Mercury', 'Villager', 1993, 347087, 'Violet');
insert into car (make, model, car_year, mileage, car_color) values ('Toyota', 'Solara', 2004, 89852, 'Orange');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Econoline E250', 1997, 7946, 'Blue');
insert into car (make, model, car_year, mileage, car_color) values ('Land Rover', 'Discovery', 2007, 328593, 'Pink');
insert into car (make, model, car_year, mileage, car_color) values ('Mercury', 'Mountaineer', 2002, 226155, 'Red');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'Ram 1500', 1998, 175970, 'Yellow');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Econoline E350', 1998, 281163, 'Teal');
insert into car (make, model, car_year, mileage, car_color) values ('Chrysler', 'Town & Country', 2000, 70840, 'Puce');
insert into car (make, model, car_year, mileage, car_color) values ('Mercedes-Benz', 'CL-Class', 2010, 7773, 'Khaki');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'Viper RT/10', 1993, 243514, 'Yellow');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Focus', 2012, 246591, 'Fuscia');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'D250 Club', 1993, 318919, 'Puce');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Expedition', 2008, 186133, 'Mauv');
insert into car (make, model, car_year, mileage, car_color) values ('Infiniti', 'M', 2009, 426944, 'Red');
insert into car (make, model, car_year, mileage, car_color) values ('Oldsmobile', 'Ciera', 1996, 429236, 'Fuscia');
insert into car (make, model, car_year, mileage, car_color) values ('Suzuki', 'Equator', 2009, 91851, 'Maroon');
insert into car (make, model, car_year, mileage, car_color) values ('Volkswagen', 'Jetta', 1989, 318427, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'Ram 2500', 1994, 263655, 'Maroon');
insert into car (make, model, car_year, mileage, car_color) values ('Nissan', 'Cube', 2009, 195277, 'Aquamarine');
insert into car (make, model, car_year, mileage, car_color) values ('Saturn', 'VUE', 2005, 388901, 'Puce');
insert into car (make, model, car_year, mileage, car_color) values ('Maserati', 'GranSport', 2006, 461164, 'Khaki');
insert into car (make, model, car_year, mileage, car_color) values ('Mercedes-Benz', 'E-Class', 1990, 103402, 'Aquamarine');
insert into car (make, model, car_year, mileage, car_color) values ('Honda', 'CR-V', 2004, 166880, 'Khaki');
insert into car (make, model, car_year, mileage, car_color) values ('Pontiac', 'Vibe', 2006, 166974, 'Khaki');
insert into car (make, model, car_year, mileage, car_color) values ('Chevrolet', 'Camaro', 1992, 346352, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Audi', 'Q7', 2011, 104859, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Land Rover', 'Defender', 1997, 330136, 'Violet');
insert into car (make, model, car_year, mileage, car_color) values ('Chevrolet', 'Corvette', 2012, 42118, 'Pink');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Freestyle', 2005, 473828, 'Aquamarine');
insert into car (make, model, car_year, mileage, car_color) values ('Volvo', 'S40', 2002, 427080, 'Fuscia');
insert into car (make, model, car_year, mileage, car_color) values ('GMC', 'Yukon XL 2500', 2009, 196589, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Toyota', 'Avalon', 1996, 23846, 'Aquamarine');
insert into car (make, model, car_year, mileage, car_color) values ('Chevrolet', 'Monte Carlo', 1973, 243552, 'Turquoise');
insert into car (make, model, car_year, mileage, car_color) values ('Chevrolet', 'Avalanche 2500', 2005, 458913, 'Khaki');
insert into car (make, model, car_year, mileage, car_color) values ('Suzuki', 'Verona', 2005, 421149, 'Crimson');
insert into car (make, model, car_year, mileage, car_color) values ('Mazda', 'MX-5', 1996, 60070, 'Green');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'Ram 3500', 1995, 106389, 'Yellow');
insert into car (make, model, car_year, mileage, car_color) values ('Dodge', 'Viper', 2006, 442461, 'Indigo');
insert into car (make, model, car_year, mileage, car_color) values ('Toyota', 'Tercel', 1997, 46266, 'Goldenrod');
insert into car (make, model, car_year, mileage, car_color) values ('Chevrolet', 'Express 1500', 2010, 110127, 'Blue');
insert into car (make, model, car_year, mileage, car_color) values ('Ford', 'Aerostar', 1990, 387605, 'Fuscia');
insert into car (make, model, car_year, mileage, car_color) values ('GMC', 'Savana 3500', 2009, 86256, 'Turquoise');

-- Procedures postgres
-- PROCEDURE: public.car_sale(integer, integer, integer, date, numeric)

-- DROP PROCEDURE IF EXISTS public.car_sale(integer, integer, integer, date, numeric);

CREATE OR REPLACE PROCEDURE public.car_sale(
	IN cust_id integer,
	IN cr_id integer,
	IN e_id integer,
	IN s_date date,
	IN s_amount numeric)
LANGUAGE 'sql'
AS $BODY$

INSERT INTO sales_invoice(customer_id,car_id, emp_id, sales_date, sales_amount)
VALUES (cust_id,cr_id, e_id, s_date, s_amount);
-- add to the customer_car relationship as well 
INSERT INTO customer_car(customer_id,car_id)
VALUES (cust_id,cr_id);

$BODY$;
ALTER PROCEDURE public.car_sale(integer, integer, integer, date, numeric)
    OWNER TO postgres;



CALL public.car_sale(
	3, 
	3, 
	6, 
	current_date, 
	33000
);

CALL public.car_sale(
	13, 
	23, 
	6, 
	current_date, 
	33000
);


select * from customer_car,sales_invoice;




--add service


CREATE OR REPLACE PROCEDURE public.car_service(
	IN cr_id integer,
	IN serv_type varchar(100),
	IN s_date date,
	in s_amount decimal(12,2)
	)
LANGUAGE 'sql'
AS $BODY$

INSERT INTO service_invoice(car_id,service_type,sales_date,service_amount)
VALUES (cr_id, serv_type, s_date, s_amount);

$BODY$

CALL public.car_service(
	3,
	'Transmission tune up',
	current_date,
	200 
);


CALL public.car_service(
	23,
	'Tire Rotation',
	current_date,
	40
);

select * from service_invoice

--add employee to service

CREATE OR REPLACE PROCEDURE public.emp_service(
	IN sr_id integer,
	IN e_id integer
    )
LANGUAGE 'sql'
AS $BODY$

INSERT INTO service_work(service_no,emp_id)
VALUES (sr_id,e_id);

$BODY$

CALL public.emp_service(
	1,
    3
);


CALL public.emp_service(
	1,
    15
);

CALL public.emp_service(
	2,
    7
);

select * from service_work
