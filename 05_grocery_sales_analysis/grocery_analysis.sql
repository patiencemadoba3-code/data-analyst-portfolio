-- =============================================
-- Project: FoodYum Grocery Sales Analysis
-- Practical Exam: Data Analyst Associate Certification
-- =============================================

-- TASK 1: Count missing year_added values
SELECT COUNT(*) AS missing_year
FROM products
WHERE year_added IS NULL;


-- TASK 2: Clean and standardise product data
SELECT
    product_id,
    COALESCE(NULLIF(product_type, '-'), 'Unknown') AS product_type,
    COALESCE(NULLIF(brand, '-'), 'Unknown') AS brand,
    ROUND(
        COALESCE(
            CAST(REPLACE(weight, ' grams', '') AS NUMERIC),
            (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY CAST(REPLACE(weight, ' grams', '') AS NUMERIC)) FROM products)
        ), 2
    ) AS weight,
    ROUND(
        COALESCE(
            price,
            (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) FROM products)
        ), 2
    ) AS price,
    COALESCE(average_units_sold, 0) AS average_units_sold,
    COALESCE(year_added, 2022) AS year_added,
    COALESCE(UPPER(NULLIF(stock_location, '-')), 'Unknown') AS stock_location
FROM products;


-- TASK 3: Get min and max price per product type
SELECT
    product_type,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM products
GROUP BY product_type;


-- TASK 4: List high-volume Meat & Dairy products
SELECT
    product_id,
    price,
    average_units_sold
FROM products
WHERE product_type IN ('Meat', 'Dairy')
  AND average_units_sold > 10;
