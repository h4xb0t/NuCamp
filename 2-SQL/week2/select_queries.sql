SELECT * FROM books;

SELECT title, year FROM books;

SELECT title AS book_title, year AS book_year FROM books;

SELECT title AS book_title, year AS book_year FROM books
ORDER BY book_year DESC;

SELECT title AS book_title, year AS book_year FROM books
WHERE title LIKE 'B%'
ORDER BY book_year DESC;

-- ILIKE IS CASE AGNOSTIC
SELECT b.title title_of_da_book, b.year year_of_da_book FROM books b
WHERE b.title ILIKE 'f%'
ORDER BY title_of_da_book ASC;



-- Select all values in the company_name column of the customers
-- table that begin with the letters 'Q' through 'Z' (inclusive); sort values in descending order.
SELECT c.company_name name_of_company FROM customers c
WHERE c.company_name >= 'Q'
ORDER BY c.company_name DESC;

-- can also write like this
SELECT c.company_name name_of_company FROM customers c
WHERE c.company_name >= 'Q'
ORDER BY name_of_company DESC;


-- Get first and last name of each employee with a title of "Sales Representative"; sort by last_name
-- and within the same last name, sort by first_name.
SELECT first_name, last_name FROM employees e
WHERE e.title = 'Sales Representative'
ORDER BY last_name, first_name;

--Get first_name and home_phone of each employee whose first_name begins with the capital letter 'A'
-- and whose home_phone includes the number '4'. Order by employee_id.
SELECT e.first_name, e.home_phone FROM employees e
WHERE e.first_name LIKE 'A%' AND e.home_phone LIKE '%4%'
ORDER BY employee_id;

-- use count to find the number of unique book generes in the genre column of books table
SELECT COUNT (DISTINCT genre)
AS genre_count
FROM books;

-- COUNT number of books per genre, return a single row for each group
SELECT genre, COUNT(*) AS book_count
FROM books GROUP BY genre;

-- COUNT number of books per genre, return a single row for each group - only show genres with count > 1
SELECT genre, COUNT(*) AS book_count
FROM books GROUP BY genre
HAVING(COUNT(*)) > 1;



