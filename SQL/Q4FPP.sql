SELECT
    cattable.category_name,
    prodtable.product_id
FROM
    categories cattable
LEFT JOIN
    products prodtable
ON
    cattable.category_id = prodtable.category_id
WHERE
    prodtable.product_id IS NULL;