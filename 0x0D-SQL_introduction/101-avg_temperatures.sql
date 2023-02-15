-- imported database weather info, disp avg temp by city
-- temprature descending order
SELECT city, AVG(value) AS avg_temp
FROM tempratures
GROUP BY city
ORDER BY avg_temp desc;