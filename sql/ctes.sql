-- What is a CTE?
-- CTE stands for Common Table Expression.
-- A CTE is a temporary, named result set that you can create inside a SQL query and use in the main query.Suppose you have a complicated SQL query. Instead of writing everything in one query, you can break it into smaller parts using CTEs.

-- Important points:
-- - A CTE is defined using the WITH keyword.
-- - It has a name.
-- - You can use it in the main SQL query.
-- - It exists only for the execution of that statement.
-- - It does not permanently store data as a physical table.

-- Basic CTE Syntax
-- WITH cte_name AS (
--     SELECT column1, column2
--     FROM table_name
--     WHERE condition
-- )

-- SELECT *
-- FROM cte_name;

-- example 1: Find employees whose salary is greater than 50,000.
with high_salary as(
    select * from employees where salary>50000
)

select * from high_salary;

-- example 2:First find all employees, then display only 1st department employees.
with it_employees as (
    select * from employees
)

select * from it_employees where department_id=1;

-- Aggregation Using CTE
-- example 1:Find the total salary of each department.
with each_dept as(
    select department_id,sum(salary) from employees group by department_id
)
select * from each_dept;

-- example 2:Find departments whose total salary is greater than 90,000.
with each_dept as(
    select department_id,sum(salary) as total_salary from employees group by department_id
)

select * from each_dept where total_salary>90000;

-- CTE vs Subquery
-- 2.3 Difference Between CTE and Subquery
-- Basis	                                            CTE	                                                           Subquery
-- Definition	                              Named temporary result set	                                   Query inside another query
-- Keyword                                            	WITH	                                                   No special keyword
-- Readability	                          Generally easier for complex queries	                             Can become difficult when nested
-- Reusability	                      Can be referenced multiple times within the statement                      Often needs to be repeated
-- Multiple steps	                      Easy to divide into separate named steps	                             Can become deeply nested
-- Recursive queries	                            Supported	                                             Not a substitute for recursive CTEs

-- Use a subquery when:
-- - The logic is simple.
-- - You need a result only once.
-- - You are filtering using IN, EXISTS, or comparison operators.
-- Use a CTE when:
-- - The query has multiple steps.
-- - You want better readability.
-- - You need to use the same intermediate result multiple times.
-- - You are working with window functions and ranking problems.

-- Multiple CTEs
-- Multiple CTEs mean creating two or more CTEs inside the same SQL statement.

-- syntax:
-- WITH cte1 AS (
--     SELECT ...
-- ),
-- cte2 AS (
--     SELECT ...
-- ),
-- cte3 AS (
--     SELECT ...
-- )
-- SELECT *
-- FROM cte1;

-- example 1:Find departments whose total salary are greater than the average salary across all department.
with total_sales as(
    select department_id,sum(salary) as total_salary from employees group by department_id
),
avg_sales as(
    select avg(total_salary) as avg_salary  from total_sales
)

select * from total_sales where total_salary>(select avg_salary from avg_sales);


-- CTE VS VIEW VS TEMP TABLE 
-- A CTE is a temporary, named result set that you can create inside a SQL query and use in the main query.

-- A View is a virtual table created using a saved SQL query.
-- It does not normally store the actual query result data itself.
-- EXAMPLE 1: 
CREATE VIEW high_salary AS
SELECT *
FROM employees
WHERE salary > 50000;
-- A view is stored as a database object.
-- It can be reused across multiple queries.
-- A normal view does not store its result data separately.

-- A temporary table is a table created temporarily in the database.
-- It stores actual data in a temporary table structure.
-- EXAMPLE 1:
CREATE TEMPORARY TABLE high_salary AS
SELECT *
FROM employees
WHERE salary > 50000;
-- It stores the selected data.
-- It can be used across multiple statements within its session.
-- In MySQL, it is automatically dropped when the session ends.
-- You can also drop it manually.


-- Difference Between CTE, View and Temp Table
-- Basis	                        CTE	                            View	                     Temp Table
-- Storage	              No separate persistent storage	 Stores query definition	         Stores data
-- Lifetime	                   One statement	                 Until dropped	              Usually session-based
-- Reusability	             Within one statement	             Across queries	            Across statements in session
-- Creation	                        WITH                         CREATE VIEW	               CREATE TEMPORARY TABLE
-- Data stored?	           No separate result table	             Normally no	                      Yes
-- Main purpose	               Simplify queries	                Reuse queries	              Store intermediate data














