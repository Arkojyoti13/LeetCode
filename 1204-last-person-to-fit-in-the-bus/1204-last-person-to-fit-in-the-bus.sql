# Write your MySQL query statement below
SELECT  person_name
FROM (
    SELECT
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn, person_id) as total_weight
    FROM Queue
    ) x
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1