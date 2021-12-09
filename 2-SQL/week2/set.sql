-- query for capital city name / country name pairs
-- (this is one-one because each country only has one capital and each capital belongs to only one country)
SELECT cc.name AS capital_city_name,
c.name AS county_name
FROM capital_cities cc
INNER JOIN countries c
ON cc.country_id = c.id;

-- query for customer name, amount spent for each order
-- (this is one-many because one customer can have many orders but one order can only have one customer)
SELECT c.name, o.dollar_amount_spent
FROM customers company_name
INNER JOIN
orders o
ON o.customer_id = c.id

-- many to many because books can have more than one author and authors can have more than one book
SELECT a.name AS author, b.name AS book
FROM authors a
INNER JOIN books_authors books_authors
ON a.id = ba.authors_id
INNER JOIN books b
ON b.id = ba.book_id;

