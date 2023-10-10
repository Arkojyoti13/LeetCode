# Write your MySQL query statement below
SELECT round(a_frac.playerCount / COUNT(DISTINCT a_full.player_id), 2) AS fraction
FROM Activity a_full,
    (SELECT COUNT(DISTINCT a1.player_id) AS playerCount
    FROM Activity a1
    INNER JOIN
        (SELECT player_id, MIN(event_date) AS first_login
        FROM Activity 
        GROUP BY player_id) a2
    ON a1.player_id = a2.player_id AND datediff(a1.event_date, a2.first_login) = 1) a_frac