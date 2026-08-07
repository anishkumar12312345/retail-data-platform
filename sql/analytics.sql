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


SELECT AVG(quantity) AS average_quantity
FROM fact_orders;


SELECT MAX(quantity) AS highest_quantity
FROM fact_orders;


SELECT MIN(quantity) AS lowest_quantity
FROM fact_orders;


SELECT
    SUM(amount) AS total_revenue
FROM fact_orders;


SELECT
    COUNT(*) AS total_orders
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


SELECT
    c.customer_name,
    SUM(f.amount) AS total_sales
FROM fact_orders f
JOIN dim_customer c
ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_sales DESC
LIMIT 5;


SELECT
    p.product_name,
    SUM(f.quantity) AS total_quantity
FROM fact_orders f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 5;


SELECT
    payment_method,
    COUNT(*) AS total_orders,
    SUM(amount) AS total_revenue
FROM fact_orders
GROUP BY payment_method
ORDER BY total_revenue DESC;


SELECT
    ROUND(AVG(amount), 2) AS average_order_value
FROM fact_orders;


SELECT
    p.category,
    SUM(f.amount) AS total_revenue
FROM fact_orders f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;