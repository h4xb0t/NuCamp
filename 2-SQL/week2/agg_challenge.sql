
-- For each customer, list the customer_id and the order_date of their first order. Sort by customer_id.
SELECT customer_id, MIN(order_date) FROM orders
GROUP BY customer_id
ORDER BY customer_id;


-- For each customer, list customer ID and the average freight cost of their orders; sort by average freight cost.
SELECT customer_id, AVG(freight) AS avg_freight FROM orders
GROUP BY customer_id
ORDER BY avg_freight;



-- For each order, select the order_id and the number of distinct products in said order
-- (call this product_count). Filter to only include orders with a product_count of 5 or more Sort by product_count in descending order.
SELECT o.order_id, count(DISTINCT product_id) AS product_count
FROM order_details o
GROUP BY order_id HAVING(count(*)) >= 5
ORDER BY product_count DESC;


