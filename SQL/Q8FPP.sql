CREATE USER 'MGSuserexample'@'localhost' IDENTIFIED BY 'mgs12345';

GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.customers TO 'MGSuserexample'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.addresses TO 'MGSuserexample'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.orders TO 'MGSuserexample'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.order_Items TO 'MGSuserexample'@'localhost';
GRANT SELECT ON my_guitar_shop.products TO 'MGSuserexample'@'localhost';
GRANT SELECT ON my_guitar_shop.categories TO 'MGSuserexample'@'localhost';

SHOW GRANTS FOR 'MGSuserexample'@'localhost';