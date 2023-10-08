# Write your MySQL query statement below
SELECT t.student_id, t.student_name, t.subject_name, 
    IF(e.attended_exams IS NULL, 0, e.attended_exams) AS attended_exams
FROM
    (SELECT *
    FROM Students
    CROSS JOIN Subjects) t
LEFT JOIN 
    (SELECT *, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name) e
ON t.student_id = e.student_id AND t.subject_name = e.subject_name
ORDER BY student_id, subject_name