# Write your MySQL query statement below
SELECT name 
FROM Employee AS T1
JOIN (SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS T2
ON T1.Id = T2.ManagerId