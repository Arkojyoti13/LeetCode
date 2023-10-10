# Write your MySQL query statement below
SELECT query_name,
    round(SUM(rating/position)/count(query_name), 2) AS quality,
    round(100*SUM(IF(rating < 3, 1, 0))/count(query_name), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name