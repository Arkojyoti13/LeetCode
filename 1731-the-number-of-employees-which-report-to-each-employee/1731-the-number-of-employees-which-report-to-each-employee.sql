# Write your MySQL query statement below
SELECT e1.reports_to AS employee_id,
       e2.name,
       COUNT(e1.reports_to) AS reports_count,
       round(AVG(e1.age),0) AS average_age
FROM employees e1
JOIN employees e2
ON e1.reports_to=e2.employee_id
GROUP BY e1.reports_to
ORDER BY e1.reports_to