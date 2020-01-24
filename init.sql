

--Cameron Wertelka
--Lab1
--SQL Statements to create tables

drop table if exists cars cascade;
drop table if exists customers cascade;
drop table if exists sales cascade;

create table cars (
	id serial,
	make text,
	model text,
	price decimal(10,2),
	primary key(id)
);

create table customers (
	id serial,
	first_name text,
	last_name text,
	sex char(1),
	primary key(id)
);

create table sales (
	id serial,
	car_id integer references cars(id),
	customer_id integer references customers(id),
	primary key(id)
);

create or replace view sales_view as
	select cars.id as carid, cars.make, cars.model, cars.price,
	customers.id as custid, customers.first_name, customers.last_name, 
	customers.sex from cars join sales on cars.id=sales.car_id join
	customers on sales.customer_id=customers.id;
