# Write your MySQL query statement below
SELECT machine_id, 
	ROUND(SUM(IF(activity_type='start', -timestamp, timestamp)) / COUNT(DISTINCT process_id), 3) AS processing_time
from Activity
GROUP BY machine_id
ORDER BY machine_id