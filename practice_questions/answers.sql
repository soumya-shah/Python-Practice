use sql_practice;
SELECT DATABASE();
-- SECTION A
-- 1.
select * from employees;
-- 2.
select employee_name,salary,city from employees;
-- 3.
select * from employees where salary>60000;
-- 4.
select * from employees where salary>=40000 and salary<=80000;
-- 5.
select * from employees where city="jaipur" or city="delhi";
-- 6.
select * from employees where employee_name LIKE "a%";
-- 7.
select * from employees where employee_name like "%an%";
-- 8.
select * from employees order by salary DESC;
-- 9.
select * from employees order by salary DESC limit 5;
-- 10.
select DISTINCT city from employees;
-- 11.
select * from employees where manager_id is null;
-- 12.
select * ,
case
when salary<=55000 then "low salary"
when salary>55000 and salary<=75000 then "medium salary"
when salary>75000 then "high salary"
else "no salary defined"
end 
from employees;

-- SECTION B
-- 1.
select count(*) from employees;
-- 2.
select AVG(salary) from employees;
-- 3.
select MAX(salary),MIN(salary) from employees;
-- 4.
select SUM(salary) as total_salary from employees;
-- 5.
select department_id, COUNT(*) from employees group by department_id;
-- 6.
select department_id,AVG(salary) as average_salary from employees group by department_id;
-- 7.
select department_id,count(*) from employees group by department_id having count(*)>5;
-- 8.
select department_id,avg(salary) as average_salary from employees group by department_id having avg(salary)>70000;
-- 9.
select department_id,max(salary) as maximum_salary from employees group by department_id;
-- 10.
select department_id,max(salary)-min(salary) as difference from employees group by department_id;
-- 11.
select city,count(*) as no_of_employees from employees group by city having count(*)>=3;
-- 12.
-- where is a clause for giving condition in a normal situation whereas having is used with group by. where is used before grouping the table or something whereas having is used afterwards.

-- SECTION C
-- 1.
SELECT employees.employee_name,departments.department_name from employees inner join departments on employees.department_id=departments.department_id;
-- 2.
SELECT employees.employee_name,departments.department_name from employees LEFT join departments on employees.department_id=departments.department_id;
-- 3.
select departments.department_name,count(employees.employee_id) as no_of_employees from employees right JOIN departments on employees.department_id=departments.department_id group by departments.department_id ;
-- 4.
select employees.employee_name from employees inner join departments on employees.department_id=departments.department_id where department_name="it";
-- 5.
select a.employee_name,b.employee_name,a.salary from employees as a,employees as b where a.manager_id=b.employee_id;
-- 6.
select c.customer_name,o.order_id from customers as c LEFT join orders as o on c.customer_id=o.customer_id;
-- 7.
select c.customer_name,o.order_id from customers as c LEFT join orders as o on c.customer_id=o.customer_id where o.order_id is not null;
-- 8.
select c.customer_name,o.order_id,o.order_date,o.amount from customers as c inner join orders as o on c.customer_id=o.customer_id;
-- 9.
select p.product_name,o.order_id from products as p left join order_items as o on p.product_id=o.product_id where o.order_id is null;
-- 10.
select c.customer_name, sum(o.amount)as total_amount from customers as c INNER join orders as o on c.customer_id=o.customer_id group by c.customer_id;
-- 11.
select p.product_name,sum(o.quantity) as total_sales from products as p inner join order_items as o on p.product_id=o.product_id group by o.product_id;
-- 12.
-- INNER JOIN is used to return only matched rows from both table. null values not included
-- LEFT JOIN is used to return the matched rows from both tables along with empty rows from left table
-- RIGHT JOIN is used to return the matched rows from both tables along with empty rows from right table
-- SELF JOIN is used to join the table with itself. 

-- SECTION D
-- 1.
select employee_name from employees where salary >(select avg(salary) from employees);
-- 2.
select employee_name,salary from employees where salary=(select max(salary) as max_salary from employees);
-- 3.
select * from employees where salary=(select max(salary) from employees where salary < (select max(salary) from employees));
-- 4.
select * from employees e1 where salary > (select avg(salary) as avg_salary from employees e2 where e1.department_id=e2.department_id);
-- 5.
select department_id,avg(salary) as avg_salary from employees group by department_id having avg_salary>(select avg(salary) from employees);
-- 6.
select customer_id from customers where customer_id  in (select distinct customer_id from orders);
-- 7.
select customer_name,customer_id from customers where customer_id  not in (select distinct customer_id from orders);
-- 8.
select * from products where price > (select avg(price) from products);
-- 9.
select * from orders where amount = (select max(amount) from orders);
-- 10.
select * from employees where department_id=(select department_id from employees where employee_name="rahul");


-- SECTION E
-- 1.
-- using limit and offset
select distinct salary from employees order by salary desc limit 1 OFFSET 1;
-- using subquery
select * from employees where salary =(select max(salary) from employees where salary < (select max(salary) from employees));
-- 2.   
-- using limit and offset
select DISTINCT salary from employees order by  salary desc limit 1 offset 2;
-- using subquery
select * from employees where salary =(select max(salary) from employees where salary < (select max(salary) from employees where salary <(select max(salary) from employees)));
-- 3.    
select email from customers group by email having count(email) >1;
-- 4.    
select * from employees where salary in (select salary from employees group by salary having count(salary) > 1);
-- == expects subquery to return 1 value whereas in expects subquery to return multiple VALUES
-- 5.    
select department_name, department_id from departments where department_id not in(select distinct department_id from employees);
-- 6.    
select customer_id,customer_name from customers where customer_id in (select customer_id from orders group by customer_id having count(customer_id) >3);
-- 7.   
 select customer_id,sum(amount) as total_spendings from orders group by customer_id having sum(amount) in (select max(total_spending) from  (select customer_id,sum(amount) as total_spending from orders group by customer_id) as max_amount);
-- 8.    
select product_id,sum(quantity) as total_quantity from order_items group by product_id having sum(quantity) in (select max(total_quantity) from (select product_id,sum(quantity) as total_quantity from order_items group by product_id) as max_quantity);
-- 9.    
select sum(amount) from (select amount,order_id from orders where status="completed") as total_revenue;
-- 10.
select customer_id,avg(amount) from orders group by customer_id;
-- 11.    
select customer_id from orders group by customer_id having sum(amount) >(select avg(total_spending) from (select customer_id,sum(amount) as total_spending from orders group by customer_id) as avg_spending);
-- 12.    
select employee_name,hire_date from employees where hire_date>="2024-01-01";
-- 13.    
select e1.hire_date,e2.hire_date as manager_date from employees e1 INNER join employees e2 on e1.manager_id=e2.employee_id where e1.hire_date<e2.hire_date;
-- 14.    
select department_id from (select avg(salary) as avg_salary,department_id from employees group by department_id) as department where avg_salary=(select max(avg_salary) as max_salary from (select avg(salary) as avg_salary,department_id from employees group by department_id)as avg_department);
-- 15.    
select * from employees where (salary,department_id)in (select max(salary),department_id from employees group by department_id);
-- 16.    
select order_id,amount from orders where amount>(select avg(amount) as avg_order_amount from orders);
-- 17.   
select product_id,stock from products where product_id in (select p.product_id from order_items o inner join products p on p.product_id=o.product_id) and stock =0 ;






























