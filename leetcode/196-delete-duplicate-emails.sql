-- https://leetcode.com/problems/delete-duplicate-emails/
CREATE TABLE IF NOT EXISTS Person (id INT, email VARCHAR(255));
TRUNCATE TABLE Person;
INSERT INTO Person VALUES (1, 'john@example.com'), (2, 'bob@example.com'), (3, 'john@example.com');

-- PostgreSQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);
