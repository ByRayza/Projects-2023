SELECT
    product1alias.product_name,
    product1alias.list_price
FROM
    products product1alias
INNER JOIN
    products product2alias
ON
    product1alias.list_price = product2alias.list_price AND product1alias.product_id <> product2alias.product_id
ORDER BY
    product1alias.product_name;