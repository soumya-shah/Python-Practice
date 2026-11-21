USE sql_practice;
SELECT DATABASE();

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    location VARCHAR(100)
);

INSERT INTO departments
(department_id, department_name, location)
VALUES
(1, 'IT', 'Jaipur'),
(2, 'HR', 'Delhi'),
(3, 'Finance', 'Mumbai'),
(4, 'Marketing', 'Bangalore'),
(5, 'Sales', 'Pune'),
(6, 'Operations', 'Hyderabad'),
(7, 'Legal', 'Delhi');

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    manager_id INT,
    salary DECIMAL(10,2),
    hire_date DATE,
    city VARCHAR(50),

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

INSERT INTO employees
(employee_id, employee_name, department_id, manager_id, salary, hire_date, city)
VALUES
(101, 'Aarav', 1, NULL, 95000, '2021-03-15', 'Jaipur'),
(102, 'Riya', 1, 101, 75000, '2022-06-10', 'Delhi'),
(103, 'Karan', 1, 101, 75000, '2023-01-20', 'Jaipur'),
(104, 'Neha', 1, 101, 60000, '2024-04-05', 'Mumbai'),

(105, 'Rahul', 2, NULL, 85000, '2020-08-12', 'Delhi'),
(106, 'Ananya', 2, 105, 65000, '2023-07-18', 'Delhi'),

(107, 'Vikram', 3, NULL, 100000, '2019-11-25', 'Mumbai'),
(108, 'Priya', 3, 107, 80000, '2022-02-14', 'Pune'),

(109, 'Arjun', 4, NULL, 90000, '2021-09-01', 'Bangalore'),
(110, 'Meera', 4, 109, 70000, '2024-01-10', 'Bangalore'),

(111, 'Kabir', 5, NULL, 88000, '2020-05-22', 'Pune'),
(112, 'Simran', 5, 111, 55000, '2025-02-11', 'Delhi'),

(113, 'Dev', 6, NULL, 72000, '2025-01-15', 'Hyderabad');


CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    email VARCHAR(150),
    signup_date DATE
);

INSERT INTO customers
(customer_id, customer_name, city, email, signup_date)
VALUES
(201, 'Aditi Sharma', 'Jaipur', 'aditi@gmail.com', '2022-01-10'),
(202, 'Rohan Mehta', 'Delhi', 'rohan@gmail.com', '2022-03-15'),
(203, 'Sneha Kapoor', 'Mumbai', 'sneha@gmail.com', '2023-05-20'),
(204, 'Yash Verma', 'Pune', 'yash@gmail.com', '2023-08-12'),
(205, 'Ishita Jain', 'Jaipur', 'ishita@gmail.com', '2024-01-05'),
(206, 'Aditya Singh', 'Delhi', 'aditya@gmail.com', '2024-02-18'),
(207, 'Kriti Shah', 'Mumbai', 'kriti@gmail.com', '2024-06-22'),
(208, 'Manav Gupta', 'Bangalore', 'manav@gmail.com', '2024-09-10'),
(209, 'Nisha Agarwal', 'Pune', 'nisha@gmail.com', '2025-01-15'),
(210, 'Varun Malhotra', 'Jaipur', 'varun@gmail.com', '2025-03-01'),

-- duplicate email intentionally added for practice
(211, 'Anjali Mehta', 'Delhi', 'rohan@gmail.com', '2025-04-12');


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT
);

INSERT INTO products
(product_id, product_name, category, price, stock)
VALUES
(301, 'Laptop', 'Electronics', 75000, 10),
(302, 'Smartphone', 'Electronics', 45000, 20),
(303, 'Headphones', 'Electronics', 5000, 50),
(304, 'Keyboard', 'Accessories', 2500, 30),
(305, 'Mouse', 'Accessories', 1500, 40),
(306, 'Monitor', 'Electronics', 18000, 15),
(307, 'Office Chair', 'Furniture', 12000, 8),
(308, 'Desk', 'Furniture', 15000, 5),
(309, 'Notebook', 'Stationery', 300, 100),
(310, 'Pen Set', 'Stationery', 200, 200),
(311, 'Webcam', 'Electronics', 7000, 0),
(312, 'Printer', 'Electronics', 22000, 3);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    status VARCHAR(30),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

INSERT INTO orders
(order_id, customer_id, order_date, amount, status)
VALUES
(401, 201, '2025-01-05', 75000, 'Completed'),
(402, 202, '2025-01-12', 45000, 'Completed'),
(403, 201, '2025-02-10', 5000, 'Completed'),
(404, 203, '2025-02-18', 18000, 'Pending'),
(405, 204, '2025-03-05', 15000, 'Completed'),
(406, 202, '2025-03-22', 2500, 'Cancelled'),
(407, 205, '2025-04-10', 12000, 'Completed'),
(408, 206, '2025-04-15', 5000, 'Completed'),
(409, 201, '2025-05-01', 18000, 'Completed'),
(410, 207, '2025-05-12', 45000, 'Completed'),
(411, 208, '2025-06-03', 1500, 'Pending'),
(412, 209, '2025-06-18', 22000, 'Completed'),
(413, 203, '2025-07-05', 7000, 'Completed'),
(414, 204, '2025-07-20', 2500, 'Completed'),
(415, 202, '2025-08-10', 12000, 'Completed'),
(416, 201, '2025-08-25', 20000, 'Completed');

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),

    PRIMARY KEY (order_id, product_id),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

INSERT INTO order_items
(order_id, product_id, quantity, unit_price)
VALUES
(401, 301, 1, 75000),

(402, 302, 1, 45000),

(403, 303, 1, 5000),

(404, 306, 1, 18000),

(405, 308, 1, 15000),

(406, 304, 1, 2500),

(407, 307, 1, 12000),

(408, 303, 1, 5000),

(409, 306, 1, 18000),

(410, 302, 1, 45000),

(411, 305, 1, 1500),

(412, 312, 1, 22000),

(413, 309, 5, 300),

(414, 304, 1, 2500),

(415, 307, 1, 12000),

(416, 303, 2, 5000);

SHOW TABLES;

SELECT * FROM employees;
select * from customers;
select * from departments;
select * from products;
select * from orders;
select * from order_items;


CREATE TABLE store_products (
    store_id INT,
    store_name VARCHAR(50),
    product_name VARCHAR(50),
    quantity INT,
    price INT
);

INSERT INTO store_products
(store_id, store_name, product_name, quantity, price)
VALUES
(1, 'Apple Store 1', 'iPhone 13 Pro', 1, 1000),
(1, 'Apple Store 1', 'MacBook pro 14', 3, 6000),
(1, 'Apple Store 1', 'AirPods Pro', 2, 500),
(2, 'Apple Store 2', 'iPhone 13 Pro', 2, 2000),
(3,"apple store 3","iPhone 13 Pro",4,75000);

CREATE TABLE MONTHLY_SALES (
    MONTH_NO INT PRIMARY KEY,
    MONTH VARCHAR(20),
    SALES INT
);

INSERT INTO MONTHLY_SALES (MONTH_NO, MONTH, SALES)
VALUES
(1, 'January', 10000),
(2, 'February', 15000),
(3, 'March', 12000),
(4, 'April', 20000),
(5, 'May', 25000);

SELECT * FROM MONTHLY_SALES;

CREATE TABLE department_salary (
    NAME VARCHAR(50),
    DEPARTMENT VARCHAR(50),
    SALARY INT
);

INSERT INTO department_salary (NAME, DEPARTMENT, SALARY)
VALUES
('Aisha', 'IT', 50000),
('Rahul', 'IT', 60000),
('Priya', 'IT', 55000),
('Karan', 'HR', 40000),
('Neha', 'HR', 50000),
('Aman', 'HR', 30000);

SELECT * FROM department_salary;

