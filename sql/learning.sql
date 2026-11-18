use sql_practice;
SELECT DATABASE();

select * from employees;
select * from departments;

-- a subquery is an sql query which is placed inside another sql query. 

-- ques1- find the employees whose salary is more than the average salary earned by all employees.
-- answer: we will break the query in two parts:
-- -->avg salary earned by all employees
-- -->filter employees based on above output

select avg(salary) from employees; 
-- 1st part done
select * from employees where salary >(select avg(salary) from employees);
-- complete answer

-- scalar subquery
-- it always return 1 row and 1 column
-- above example is good 

-- write above query with join 
select * from employees as e join (select avg(salary) as sal from employees) as avg_salary on e.salary>avg_salary.sal ;

-- multiple row subquery
-- type 1: multiple rows and multiple columns

-- eg: find the employees who earn the highest salary in each department.CACHE INDEX
-- answer: dividing in two parts: 
-- -->highest salary in each department
-- -->filter employees based on above output

select max(salary),department_id from employees group by department_id;
-- 1st part done
select * from employees where (salary,department_id)  in (select max(salary),department_id from employees group by department_id);
-- multiple columns should be written in paranthesis.
-- complete answer


-- type2: single column,multiple row subquery
-- eg1: find department who do not have any employees

-- answer:
select distinct department_id from employees;
-- 1st part done
select department_id from departments where department_id not in(select distinct department_id from employees);
-- complete answer


-- correlated subquery
-- in above parts the subquery was independent. it can run independently.

-- eg:find the employees in each department who earn more than the avg salary in that department.
-- answer:
-- -->avg salary of each department 
-- -->salary of employees in each department 
-- -->compare the outputs of both the queries.

select avg(salary) from employees group by department_id;
-- 1st part done
select * from employees e1 where salary >(select avg(salary) from employees e2 where e1.department_id=e2.department_id);
-- complete answer

-- eg: find department who do not have any employees
-- answer: 

select * from departments as d where not exists(select * from employees as e where d.department_id=e.department_id); 


-- nested subquery
select * from store_products;
-- eg: find stores whose sales were better than the avg sales across all stores.
-- -->find total sales for each store 
-- -->find avg sales across all store 
-- -->compare 1 and 2

select store_name,sum(price)as total_sales from store_products group by store_name;
-- 1st part done
-- hume upr wala jo output h uska avg lena hai 
select avg(total_sales) as avg_sales from (select store_name,sum(price)as total_sales from store_products group by store_name) as store_summary;
-- 2nd part done

select * from  (select store_name,sum(price)as total_sales from store_products group by store_name) as sales join (select avg(total_sales) as avg_sales from (select store_name,sum(price)as total_sales from store_products group by store_name) as store_summary ) as avg where sales.total_sales>avg.avg_sales;











