# Write your MySQL query statement below
SELECT l1.Num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE (l1.Num = l2.Num AND 
      l2.Num = l3.Num AND
      l1.Id = l2.Id + 1 AND 
      l2.Id = l3.Id + 1)
GROUP BY l1.Num