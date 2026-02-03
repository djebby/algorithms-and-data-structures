CREATE TABLE IF NOT EXISTS customers (id INT, name VARCHAR(255));
TRUNCATE TABLE customers;
INSERT INTO customers VALUES (1, 'Joe'), (2, 'Henry'), (3, 'Sam'), (4, 'Max');

CREATE TABLE IF NOT EXISTS orders (id INT, customerId INT);
TRUNCATE TABLE orders;
INSERT INTO orders VALUES (1, 3), (2, 1);

-- PostgreSQL query statement below
SELECT customers.name as Customers 
FROM customers 
LEFT JOIN orders on customers.id = orders.customerid
WHERE orders.id IS NULL;

