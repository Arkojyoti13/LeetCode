# Write your MySQL query statement below
SELECT results
FROM (
  SELECT u.name results
  FROM MovieRating mr
  JOIN users u ON mr.user_id = u.user_id
  GROUP BY u.name
  ORDER BY COUNT(mr.rating) DESC, name
  LIMIT 1 
  ) AS ratings
UNION ALL
SELECT results 
FROM (
  SELECT m.title results
  FROM MovieRating mr2
  JOIN Movies m ON mr2.movie_id = m.movie_id 
  WHERE DATE_FORMAT(mr2.created_at, "%Y-%m") = '2020-02'
  GROUP BY m.title
  ORDER BY AVG(mr2.rating) DESC, m.title 
  LIMIT 1
) movie_ratings