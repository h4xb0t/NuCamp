-- Problem: How can we find duplicate last names, in the combined list of last names from both the students and students tables?​
-- ​Approach: We must get the count of each last name. Then we will know that any last name with a count > 1 is a duplicate.
-- Let's begin by looking at how to get all the last names of both the students and professors tables from the week2 database, including duplicates.
-- Enter into the Query Editor for week2:
SELECT  last_name FROM professors
UNION ALL
SELECT last_name FROM students;

-- Now, let's update the query to create a Common Table Expression using the WITH keyword, aliased as all_names:
WITH all_names AS (
    SELECT last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)

-- We can now further update this query to group by last name, and count the number in each group:
WITH all_names AS (
    SELECT  last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)
SELECT last_name, COUNT(*)
FROM all_names
GROUP BY last_name;

-- Update the query once more, using the HAVING clause to filter out last names that appear only once (i.e. have no duplicates):
WITH all_names AS (
    SELECT  last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)
SELECT last_name, COUNT(*)
FROM all_names
GROUP BY last_name
HAVING COUNT(*) > 1;
-- Run this query. The result set should show only the last names that appear more than once:



-- Example 2
-- ​For this example, we will look at how we can retrieve a result set that shows the occupation (student/professor), first name, last name, and department code  for all students and professors.
-- Enter the following query into the Query Editor and run it:
SELECT first_name, last_name, department_id FROM professors
UNION ALL
SELECT first_name, last_name, major_department_id FROM students;
-- From the result set, you should be able to see that we have retrieved the first and last names, but we do not yet have the occupation nor the department code columns.
-- Enter and run the following query:
SELECT 'professor' AS occupation, first_name, last_name, department_id
FROM professors
UNION ALL
SELECT 'student' AS occupation, first_name, last_name, major_department_id
FROM students;

-- The above syntax sets a string literal, either "professor" or "student", as the value for a column aliased as occupation.
-- We must still solve for the department code, based on the department id.
-- Update the query to appear as follows:

WITH people AS (
    SELECT 'professor' AS occupation, first_name, last_name, department_id
    FROM professors
    UNION ALL
    SELECT 'student' AS occupation, first_name, last_name, major_department_id
    FROM students
)
SELECT occupation, first_name, last_name, d.code
FROM people
JOIN departments d
ON department_id = d.id;

-- This creates a CTE (Common Table Expression) named people from the result set of the union between the professors and students tables.
-- Then, we can select from the temporary people table and join it with the departments table, then retrieve the code for each department (e.g. "MATH" for the Mathematics department).
-- Run this query, and you should be able to see that the department codes are retrieved.
-- However, this result set does not include students who have not yet declared a major.
-- To include those students who have a null value for their major department, we must use a LEFT JOIN.
-- Update the JOIN to a LEFT JOIN so that the query appears as follows:

WITH PEOPLE AS (
    SELECT 'professor' AS occupation, first_name, last_name, department_id
    FROM professors
    UNION ALL
    SELECT 'student' AS occupation, first_name, last_name, major_department_id
    FROM students
)
SELECT occupation, first_name, last_name, d.code
FROM people
LEFT JOIN departments d
ON department_id = d.id;

-- When you run this query, you should be able to see that the result set includes students with null as their department code.
-- By composing subqueries in this way, we can break down complicated queries into chunks that are easier to understand.