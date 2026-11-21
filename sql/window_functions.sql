-- Window functions use OVER().

-- FUNCTION_NAME() OVER (
--     PARTITION BY column_name
--     ORDER BY column_name
-- )

-- PARTITION BY: Divides data into groups.
-- ORDER BY: Determines the order of rows.
-- OVER(): Defines the window on which the function works.

-- example:
SELECT
    employee_name,
    department_id,
    salary,
    RANK() OVER(
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS ranking
FROM employees;
-- it works like this: 
-- --> First divide employees department-wise.
-- -->Then rank employees according to salary.
-- -->Highest salary gets rank 1 in each department.

-- 1.ROW_NUMBER()
-- ROW_NUMBER() assigns a unique sequential number to each row.
-- Even if two employees have the same salary, they will get different row numbers.

-- Assign a unique row number to employees based on their salary, from highest to lowest.
select employee_id ,employee_name ,department_id,salary, row_number() over(order by salary desc)as ranking from employees;
-- ROW_NUMBER() assigns unique numbers.
-- OVER() defines the window.
-- ORDER BY salary DESC sorts salaries from highest to lowest.
-- AS ranking gives the calculated column a name.

-- Assign row numbers separately to employees in each department.
select employee_id ,employee_name ,department_id,salary, row_number() over(partition by department_id order by salary desc)as ranking from employees;

-- practice questions by ownself: 
-- 1. Assign row numbers to all employees based on salary in descending order.
select * ,row_number() over(order by salary desc) as row_num from employees;
-- 2. Assign row numbers separately to employees in each department.
select *,row_number() over(partition by department_id)as ranking from employees;
-- 3. Find the highest-paid employee from each department using ROW_NUMBER().
WITH highest_paid as(
    select *,row_number() over(partition by department_id order by salary desc) as ranking from employees
)
select * from highest_paid where ranking=1;
-- 4. Find the top 2 highest-paid employees from each department.
with second as(
    select *,row_number() over(partition by department_id order by salary desc)as ranking  from employees 
)
select * from second where ranking=2 or ranking=1;

-- 2.RANK()
-- RANK() assigns rankings to records based on a specified column.
-- If two or more records have the same value, they receive the same rank.However, the next rank is skipped.

-- Example 1: Rank all employees according to salary
-- SELECT
--     name,
--     salary,
--     RANK() OVER(
--         ORDER BY salary DESC
--     ) AS ranking
-- FROM employees;

-- PRACTICE_QUESTIONS:
-- 1. Rank all employees based on salary.
SELECT *,RANK() OVER(ORDER BY SALARY DESC ) AS RANKING FROM EMPLOYEES;
-- 2.Rank employees department-wise.
SELECT *,RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC ) AS RANKING FROM EMPLOYEES;
-- 3.Find all employees who share the highest salary rank.
WITH HIGHEST_RANK AS(
    SELECT *,RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC ) AS RANKING FROM EMPLOYEES
)
SELECT * FROM HIGHEST_RANK WHERE RANKING=1;
-- 4.Find employees who have rank 2 or below in every department.
WITH SECOND AS(
    SELECT *,RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC ) AS RANKING FROM EMPLOYEES
)
SELECT * FROM SECOND WHERE RANKING=2 OR RANKING <2;
-- 5.Rank products based on their selling price.
SELECT PRODUCT_NAME,RANK() OVER(ORDER BY PRICE DESC) AS RANKING FROM PRODUCTS;

-- 3.DENSE_RANK()
-- DENSE_RANK() assigns ranks to records based on a specified column.
-- If multiple records have the same value, they receive the same rank.
-- Unlike RANK(), it does not skip the next rank.

-- EXAMPLE1: Assign dense rankings to employees according to salary.
-- SELECT
--     name,
--     salary,
--     DENSE_RANK() OVER(
--         ORDER BY salary DESC
--     ) AS dense_ranking
-- FROM employees;

-- PRACTICE QUESTIONS:
-- 1.Find the dense ranking of all employees based on salary.
SELECT *,DENSE_RANK() OVER(ORDER BY SALARY DESC) AS RANKING FROM EMPLOYEES;
-- 2.Find the second-highest distinct salary.
SELECT DISTINCT SALARY,EMPLOYEE_NAME,DENSE_RANK() OVER(ORDER BY SALARY DESC) AS RANKING FROM EMPLOYEES;
-- 3.Find the third-highest distinct salary.
WITH THIRD AS(
    SELECT DISTINCT SALARY,EMPLOYEE_NAME,DENSE_RANK() OVER(ORDER BY SALARY DESC) AS RANKING FROM EMPLOYEES
)
SELECT * FROM THIRD WHERE RANKING=3;
-- 4.Rank employees department-wise using DENSE_RANK().
SELECT *,DENSE_RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS RANKING FROM EMPLOYEES;
-- 5.Find employees earning the second-highest distinct salary in each department.
WITH SECOND_DEPT AS(
    SELECT DISTINCT SALARY,DENSE_RANK() OVER(PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS RANKING FROM EMPLOYEES
)
SELECT * FROM SECOND_DEPT WHERE RANKING=2;


-- 4. LAG()
-- LAG() is a window function that allows us to access the value of a previous row without performing a self-join.
-- It helps us compare the current row with a previous row.

-- SYNTAX:
-- SELECT
--     column_name,
--     LAG(column_name, offset, default_value)
--     OVER(
--         ORDER BY column_name
--     ) AS previous_value
-- FROM table_name;

-- Component	              Meaning
-- LAG()	          Accesses a previous row's value
-- column_name	      Column whose previous value we need
-- offset	          Number of rows to look back
-- default_value	  Value returned when the previous row doesn't exist
-- OVER()	          Defines the window
-- ORDER BY	          Determines the row sequence

-- EXAMPLE1:Display every month's sales along with the previous month's sales.
-- SELECT
--     month,
--     sales,
--     LAG(sales) OVER(
--         ORDER BY month_no
--     ) AS previous_sales
-- FROM monthly_sales;

-- PRACTICE QUESTIONS:
-- 1. Display every month's sales with the previous month's sales.
SELECT MONTH,SALES,LAG(SALES) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES;
-- 2. Find sales from two months earlier.
SELECT MONTH,SALES,LAG(SALES,2) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES;
-- 3. Calculate the difference between current and previous month's sales.
WITH MONTHLY_SALES AS(SELECT MONTH,SALES,LAG(SALES) OVER(ORDER BY MONTH_NO) AS RANKING  FROM MONTHLY_SALES)
SELECT *,SALES-RANKING AS SALES_DIFFERENCE FROM MONTHLY_SALES;
-- 4. Find months where sales decreased compared to the previous month.
WITH MONTHLY_SALES AS(
    SELECT MONTH,SALES,LAG(SALES) OVER(ORDER BY MONTH_NO) AS RANKING  FROM MONTHLY_SALES
),
SALES_DIFFERENCE AS(
    SELECT *,SALES-RANKING AS DIFFERENCE FROM MONTHLY_SALES
)

SELECT * FROM SALES_DIFFERENCE WHERE DIFFERENCE<0;
-- 5. Calculate the percentage growth in sales compared to the previous month.
WITH MONTHLY_SALES AS(
    SELECT MONTH,SALES,LAG(SALES) OVER(ORDER BY MONTH_NO) AS RANKING  FROM MONTHLY_SALES
),
SALES_DIFFERENCE AS(
    SELECT *,((SALES-RANKING)/RANKING)*100 AS PERCENTAGE_GROWTH FROM MONTHLY_SALES
)

SELECT * FROM SALES_DIFFERENCE;

-- 5.LEAD()
-- LEAD() allows us to access the value of a future or following row without performing a self-join.
-- SYNTAX:
-- SELECT
--     column_name,
--     LEAD(column_name, offset, default_value)
--     OVER(
--         ORDER BY column_name
--     ) AS next_value
-- FROM table_name;

-- EXAMPLE1:Display every month's sales along with the next month's sales.
-- SELECT
--     month,
--     sales,
--     LEAD(sales) OVER(
--         ORDER BY month_no
--     ) AS next_sales
-- FROM monthly_sales;

-- PRACTICE QUESTIONS:
-- 1.Display each month's sales with next month's sales.
SELECT MONTH,SALES,LEAD(SALES) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES;
-- 2.Find sales from two months ahead.
SELECT MONTH,SALES,LEAD(SALES,2) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES;
-- 3.Find the difference between next month's sales and current month's sales.
with current as (
    SELECT MONTH,SALES,LEAD(SALES) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES
)
select month,sales,ranking,ranking-sales as difference from current;
-- 4.Identify months where next month's sales are higher than current month's sales.
with current as (
    SELECT MONTH,SALES,LEAD(SALES) OVER(ORDER BY MONTH_NO) AS RANKING FROM MONTHLY_SALES
),
sales_difference as(
    select month,sales,ranking,ranking-sales as difference from current
)
select * from sales_difference where difference>0;
-- 5.Compare current month's sales with both previous and next month's sales using LAG() and LEAD().
select month,sales,lag(sales) over(order by month_no) as previous_sales,lead(sales) over(order by month_no) as next_sales from monthly_sales;

-- 6.SUM() OVER() – Running Total
-- SUM() OVER() calculates the sum of values across a specified window without combining the individual rows.

-- example1:Calculate cumulative sales month-wise.
-- SELECT
--     month,
--     sales,
--     SUM(sales) OVER(
--         ORDER BY month_no
--         ROWS BETWEEN UNBOUNDED PRECEDING
--         AND CURRENT ROW
--     ) AS running_total
-- FROM monthly_sales;

-- practice questions:
-- 1. Calculate the running total of monthly sales.
select month,sales,sum(sales) over(order by month_no rows between unbounded preceding and current row)as total from monthly_sales;
-- 2. Calculate the running salary total department-wise.
select name,salary,department,sum(salary) over(partition by department order by name rows between unbounded preceding and current row)as total from department_salary;
-- 3. Display each employee's salary with the overall salary total.
select name,salary,department,sum(salary) over() as overall_salary from department_salary;
-- 4. Calculate cumulative sales for each month.
select month,sales,sum(sales) over(order by month_no rows between unbounded preceding and current row)as total from monthly_sales;
-- 5. Calculate the running total of orders placed by each customer.
select customer_id,amount,sum(amount) over(partition by customer_id order by order_id rows BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)as total_orders from orders;

-- 7.AVG() OVER()
-- AVG() OVER() calculates the average of values across a specified window without collapsing individual records.

-- example 1: Calculate the average sales of the current month and the previous two months.
-- SELECT
--     month,
--     sales,
--     AVG(sales) OVER(
--         ORDER BY month_no
--         ROWS BETWEEN 2 PRECEDING
--         AND CURRENT ROW
--     ) AS moving_avg
-- FROM monthly_sales;

-- remember:For an N-row moving average, use N-1 PRECEDING.


-- Practice questions
-- 1. Calculate the overall average salary of all employees.
select name,salary,avg(salary) over() as avg_salary from department_salary ;
-- 2. Calculate the department-wise average salary.
select name,department,avg(salary) over(partition by department) as avg_salary from department_salary;
-- 3. Calculate the average salary of employees in each department while retaining individual records.
select name,department,salary,avg(salary) over(partition by department) as avg_salary from department_salary;
-- 4. Calculate a 3-month moving average of sales.
select month,sales,avg(sales) over(order by month_no rows between 2 PRECEDING AND CURRENT ROW) as moving_avg from monthly_sales;
-- 5. Find the difference between each employee's salary and their department's average salary.
with department_avg as(
    select name,department,salary,avg(salary)  over(partition by department) as avg_salary from department_salary
)
select name,department,salary,avg_salary,salary-avg_salary as difference from department_avg;

-- 8.COUNT() OVER()
-- COUNT() OVER() counts records within a specified window without collapsing individual rows.

-- COUNT(*) counts every row, including rows containing NULL values in individual columns.
-- COUNT(column_name) counts only rows where that column is NOT NULL.

-- example 1: Assign a running count to employees based on their employee ID.
-- SELECT
--     emp_id,
--     name,
--     COUNT(*) OVER(
--         ORDER BY emp_id
--         ROWS BETWEEN UNBOUNDED PRECEDING
--         AND CURRENT ROW
--     ) AS running_count
-- FROM employees;

-- Practice questions
-- 1. Count all employees using COUNT(*) OVER().
select * from employees;
select employee_name,count(*) over() as total_employees from employees;
-- 2. Count employees department-wise.
select employee_name,department_id,count(*) over(partition by department_id) as department_wise from employees;
-- 3. Calculate the running count of employees according to emp_id.
select employee_name, count(*) over(order by employee_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total from employees;
-- 4. Count the number of orders placed by each customer while retaining every order.
select * from orders;
SELECT order_id,customer_id,count(*) over(partition by customer_id) as total_orders from orders;
-- 5. Find the total number of employees in each department and display it alongside every employee.
select employee_name,department_id,count(*) over(partition by department_id) as department_wise from employees;

-- 9.NTILE()
-- NTILE() divides records into a specified number of approximately equal groups, also called buckets.

-- example 1: Divide eight employees into three approximately equal salary groups.
-- SELECT
--     name,
--     salary,
--     NTILE(3) OVER(
--         ORDER BY salary DESC
--     ) AS salary_group
-- FROM employees;

-- Practice questions
-- 1. Divide employees into two salary groups.
select employee_name,employee_id,ntile(2) over(order by salary) as salary_group from employees;
-- 2. Divide employees into four salary groups.
select employee_name,employee_id,ntile(4) over(order by salary desc) as salary_group from employees;
-- 3. Divide customers into three groups based on total spending.
select * from orders;
with customer_total as(
    select customer_id,sum(amount) as total_spend from orders group by customer_id
)
select customer_id,ntile(3) over(order by total_spend) as group_spend from customer_total;
-- 4. Divide products into five groups based on sales.
select * from order_items;
with total_sales as(
    select product_id,sum(quantity) as total_quantity from order_items group by product_id
)
select *,ntile(5) over(order by total_quantity desc ) as group_sales from total_sales;

-- 5. Find which bucket each employee belongs to when divided into three groups according to salary.
select employee_name,salary,ntile(3) over(order by salary desc) as group_salary from employees;




