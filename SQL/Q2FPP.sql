SELECT
    item_id,
    item_price,
    discount_amount,
    quantity,
    item_price * quantity AS price_total,
    discount_amount * quantity AS discount_total,
    (item_price - discount_amount) * quantity AS item_total
FROM
    order_Items
WHERE
    (item_price - discount_amount) * quantity > 500
ORDER BY
    item_total DESC;