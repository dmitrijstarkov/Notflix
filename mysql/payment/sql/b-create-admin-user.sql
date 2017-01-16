CREATE USER 'admin'@'localhost' IDENTIFIED BY 'dkgjb4i4ifnbw';
GRANT SELECT, INSERT, UPDATE on payment_db.payments TO 'admin'@'localhost';
GRANT ALTER ROUTINE, CREATE ROUTINE, EXECUTE ON *.* TO 'admin'@'localhost'; 
FLUSH PRIVILEGES;