# Write your MySQL query statement below
SELECT Today.id
FROM Weather Today
JOIN Weather Yesterday
ON  DATE(Yesterday.recordDate) = DATE_SUB(DATE(Today.recordDate), INTERVAL 1 DAY)
    AND Today.temperature > Yesterday.temperature