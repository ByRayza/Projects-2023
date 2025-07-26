SELECT
    cstmrtable.email_address,
    COUNT(DISTINCT odt.order_id) AS order_count
FROM
    customers cstmrtable
JOIN
    orders odt
ON
    cstmrtable.customer_id = odt.customer_id
GROUP BY
    cstmrtable.email_address
HAVING
    COUNT(DISTINCT odt.order_id) > 1
ORDER BY
    cstmrtable.email_address ASC;