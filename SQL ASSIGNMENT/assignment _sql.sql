use tops;
select *from employeessql;
select FIRST_NAME,HIRE_DATE from employeessql;
select FIRST_NAME,JOB_ID, concat_ws(" , ", FIRST_NAME,JOB_ID) as emp_title from employeessql;
select FIRST_NAME,HIRE_DATE,depARTMENT from employeessql where depARTMENT="clerk";
select concat_ws(",",EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL,
 PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT,
 MANAGER_ID, DEPARTMENT_ID, depARTMENT, LOCATION) as output from employeessql;
 select FIRST_NAME,SALARY from employeessql where salary>2000;
 select FIRST_NAME as f_name, HIRE_DATE as start_date from employeessql;
 select FIRST_NAME,HIRE_DATE from employeessql order by HIRE_DATE;
 select FIRST_NAME,SALARY from employeessql order by salary desc;
 select FIRST_NAME,SALARY from employeessql order by salary;
 select FIRST_NAME,DEPARTMENT_ID , COMMISSION_PCT  from employeessql where COMMISSION_PCT is not null  ;
 select LAST_NAME,JOB_ID , department from employeessql where depARTMENT<>"manager";
 select LAST_NAME,JOB_ID,SALARY from employeessql where JOB_ID="clerk" or "sales" and salary= 25000 or 5000 or 35000;
select max(salary) as max_salary , max(commission_pct) as max_commission from  employeessql ;
select min(salary)as min_salary ,min(COMMISSION_PCT)as min_commission from employeessql;
select avg(salary) as avg_salary , avg(commission_pct)as avg_commission  from employeessql;
select depARTMENT,sum(salary) as total_salary ,sum(COMMISSION_PCT) as total_commission from employeessql group by depARTMENT ;
select depARTMENT ,count(FIRST_NAME) as total_emp from employeessql group by department;
select FIRST_NAME from employeessql where commission_pct is null;
select  FIRST_NAME ,DEPARTMENT_ID,COMMISSION_PCT, case 
when commission_pct is not null then "yes"
else "no commission"
end as "description"
from employeessql;
alter table employeessql drop MyUnknownColumn;
select MANAGER_ID ,count(FIRST_NAME) as no_of_emp from employeessql group by manager_id;
select manager_id ,sum(salary) as total_salary from employeessql group by manager_id;
select FIRST_NAME,DEPARTMENT_ID,SALARY from employeessql where first_name like "a%";
select FIRST_NAME,DEPARTMENT_ID,SALARY,last_name from employeessql where last_name like "%r%";
select  department_id ,sum(salary) as total_salary from employeessql group by department_id ;
select department_id,  max(salary) as max_salary from employeessql group by department_id;
select COMMISSION_PCT, case 
when commission_pct is not null then "10% of salary"
else "1"
end as "description"
from employeessql;


