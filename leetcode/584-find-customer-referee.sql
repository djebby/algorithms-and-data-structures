-- https://leetcode.com/problems/find-customer-referee/
CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
TRUNCATE TABLE Customer;
INSERT INTO Customer 
VALUES (1, 'Will', null), (2, 'Jane', null), (3, 'Alex', 2), (4, 'Bill', null), (5, 'Zack', 1), (6, 'Mark', 2);

-- PostgreSQL query statement below
SELECT name FROM customer 
WHERE referee_id != 2 OR referee_id IS NULL;