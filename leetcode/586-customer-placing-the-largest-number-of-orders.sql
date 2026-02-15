-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
CREATE TABLE IF NOT EXISTS Orders (order_number INT, customer_number INT);
TRUNCATE TABLE Orders;
INSERT INTO Orders VALUES (1, 1), (2, 2), (3, 3), (4, 3);

-- PostgreSQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY count(order_number) DESC LIMIT 1;
