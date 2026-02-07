-- https://leetcode.com/problems/employee-bonus/
CREATE TABLE IF NOT EXISTS Employee (empId INT, name VARCHAR(255), supervisor INT, salary INT);
CREATE TABLE IF NOT EXISTS Bonus (empId INT, bonus INT);
TRUNCATE TABLE Employee;
INSERT INTO Employee VALUES (3, 'Brad', null, 4000), (1, 'John', 3, 1000), (2, 'Dan', 3, 2000), (4, 'Thomas', 3, 4000);
TRUNCATE TABLE Bonus;
INSERT INTO Bonus VALUES (2, 500), (4, 2000);

-- PostgreSQL query statement below
SELECT Employee.name, Bonus.bonus
FROM employee
LEFT JOIN Bonus ON Employee.empId = Bonus.empId
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL;
