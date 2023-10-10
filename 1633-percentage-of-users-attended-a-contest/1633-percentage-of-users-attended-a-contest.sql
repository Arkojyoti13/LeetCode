# Write your MySQL query statement below
SELECT r.contest_id AS contest_id, 
    round(100*count(DISTINCT r.user_id)/count(DISTINCT u.user_id), 2) AS percentage
FROM Register r, Users u
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id