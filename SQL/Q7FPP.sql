SELECT
    IF(GROUPING(catstable.category_name) = 1, 'Grand Total', catstable.category_name) AS category_name,
    IF(GROUPING(prodtable.product_name) = 1, 'Category Total', prodtable.product_name) AS product_name,
    SUM(oitable.quantity) AS total_quantity_purchased
FROM
    categories catstable
LEFT JOIN
    products prodtable ON catstable.category_id = prodtable.category_id
LEFT JOIN
    order_items oitable ON prodtable.product_id = oitable.product_id
GROUP BY
    catstable.category_name, prodtable.product_name WITH ROLLUP;