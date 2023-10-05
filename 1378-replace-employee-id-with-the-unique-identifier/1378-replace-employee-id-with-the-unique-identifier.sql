# Write your MySQL query statement below
SELECT unique_id,name
FROM Employees
LEFT JOIN EmployeeUNI
ON IF(Employees.id = EmployeeUNI.id,Employees.id,NULL);