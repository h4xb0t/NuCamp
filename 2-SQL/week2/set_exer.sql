-- view tables
-- Begin by running SELECT queries to view all records from each table, using the Query Editor to run each query in turn:
SELECT * FROM departments;
SELECT * FROM professors;
SELECT * FROM students;

-- union
-- Run the following query to retrieve a result set of all unique student and professor last names:
--Recall that UNION by default removes duplicates, ensuring that the result set will only contain unique values for a column.
SELECT s.last_name FROM students s
UNION
SELECT p.last_name FROM professors p;


-- union all
-- Run the following query to retrieve a result set of all student and professor last names, without removing duplicates:
SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p;

-- union all - order by
-- Run the following query to retrieve a result set of all student and professor last names, without removing duplicates, and in alphabetical order:
SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p
ORDER BY last_name;

-- inner join
-- Run the following query to retrieve a result set of all students
-- by first and last name, as well as the department in which they have declared their major:
SELECT s.first_name, s.last_name, d.name
FROM departments d
INNER JOIN students s
ON d.id = s.major_department_id;
-- The result set should contain 8 students, even though there are 11 students total in the students table.
-- This is because INNER JOIN filters out any students who have not declared a major and thus have NULL for their major_department_id column.


-- right join - Update the query to use RIGHT JOIN instead of INNER JOIN:
-- Run this query. The result set should contain all 11 student records, including those who have not declared a major.
SELECT s.first_name, s.last_name, d.name
FROM departments d
RIGHT JOIN students s
ON d.id = s.major_department_id;

-- FULL JOIN
SELECT s.first_name, s.last_name, d.name
FROM departments d
FULL JOIN students s
ON d.id = s.major_department_id;
-- Run this query. The result set should contain all matching student-department relations,
-- with NULL placeholders for unmatched records. This means that the result set should contain 12 records -
-- the 11 student records, plus the 12th record for the Philosophy department, which does not have any students who have declared a major in it.


-- Finding departments without majors
-- If we are interested in a result set that contains only those departments without majors, there is a better way.
-- Enter and run this query:
SELECT name FROM departments d
EXCEPT
SELECT DISTINCT name FROM departments d
INNER JOIN students s
ON s.major_department_id = d.id;



-- For each product, list the product_name and the corresponding category_name
SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c
ON p.category_id = c.category_id;

-- For each order, list the order_id and the corresponding shipper company_name if available, else NULL.
SELECT o.order_id, s.company_name
FROM orders o
LEFT JOIN shippers s
ON o.ship_via = s.shipper_id;

-- For each customer order, list the company_name, order_id, and total quantity of products ordered.
SELECT c.company_name, o.order_id, SUM(od.quantity) FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY o.order_id, c.company_name;


