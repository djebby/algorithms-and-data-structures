-- https://leetcode.com/problems/rising-temperature/
CREATE TABLE IF NOT EXISTS Weather (id INT, recordDate DATE, temperature INT);
TRUNCATE TABLE Weather;
INSERT INTO Weather VALUES (1, '2015-01-01', 10), (2, '2015-01-02', 25), (3, '2015-01-03', 20), (4, '2015-01-04', 30);

-- PostgreSQL query statement below
SELECT w2.id
FROM Weather w1
JOIN Weather w2
ON w1.recordDate + 1 = w2.recordDate AND w1.temperature < w2.temperature;
