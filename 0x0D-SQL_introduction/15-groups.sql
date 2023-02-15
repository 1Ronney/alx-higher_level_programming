-- list record numbers with some score in 'second_table'
-- of db 'hbtn_0c_0'
-- results to display score & 
-- number of score indexed 'number'
-- descending order for list of number of records
-- db name passed as arg in mysql cmd
SELECT score, COUNT(1) as number FROM second_table
GROUP BY score
ORDER BY number desc;