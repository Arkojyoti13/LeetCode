# Write your MySQL query statement below
WITH result AS (
SELECT
    product_id,
    new_price,
    rank() Over(PARTITION BY product_id order by change_date DESC) AS rnk
FROM products
WHERE change_date <= '2019-08-16'
) 

SELECT 
    DISTINCT p.product_id, 
    COALESCE(temp.new_price, 10) AS price
FROM Products AS p LEFT JOIN (SELECT * FROM result WHERE rnk=1) AS temp
ON p.product_id = temp.product_id