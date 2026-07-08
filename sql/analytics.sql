SELECT SUM(amount) AS total_revenue
FROM fact_orders;

SELECT COUNT(*) AS total_orders
FROM fact_orders;

SELECT
product_id,
SUM(quantity) AS total_quantity
FROM fact_orders
GROUP BY product_id
ORDER BY total_quantity DESC;

SELECT
customer_id,
SUM(amount) AS total_sales
FROM fact_orders
GROUP BY customer_id
ORDER BY total_sales DESC;

SELECT
DATE_TRUNC('month', order_date) AS month,
SUM(amount) AS revenue
FROM fact_orders
GROUP BY month
ORDER BY month;

SELECT AVG(amount) AS average_order_value
FROM fact_orders;