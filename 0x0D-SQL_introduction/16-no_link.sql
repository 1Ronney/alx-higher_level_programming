-- list all records of 'second_table' of db 'hbtn_0c_0'
-- avoid lising rows with no 'name' value
-- results to display score & name
-- records to list descending score
-- db name to be passed as arg in mysql cmd
-- selective JOIN or UNION use
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score desc;