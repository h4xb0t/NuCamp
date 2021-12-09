SELECT COUNT(*) FROM books;

SELECT MAX(year) FROM books;

SELECT genre, COUNT(*) FROM books
GROUP BY genre;

SELECT genre, COUNT(*) FROM books
GROUP BY genre
HAVING COUNT(*) > 1;

SELECT title, COUNT(*) FROM books
GROUP BY title;