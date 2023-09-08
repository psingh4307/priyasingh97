use tops;
create table ola_driver
(
driver_id int primary key ,
driver_name varchar(23),
pickup  varchar (23),
dropoff varchar(23),
available_vechile varchar(23),
fare int,
pickup_time date

);

create table customers
(
passenger_id int primary key  ,
passenger_name varchar (23),
pickup varchar(23),
dropoff varchar (23),
available_vechile varchar(23),
fare int,
pickup_time date,
common_id int,
foreign key customers(common_id) references 
ola_driver(driver_id)
);
select*from ola_driver
inner join customers
on ola_driver. driver_id = customers.common_id;

select*from ola_driver
left join customers
on ola_driver. driver_id = customers.common_id;

select*from ola_driver
right join customers
on ola_driver. driver_id = customers.common_id;




