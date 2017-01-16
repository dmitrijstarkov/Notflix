CREATE USER 'admin'@'localhost' IDENTIFIED BY 'sdgkj48ih487';
GRANT SELECT, INSERT, UPDATE on subscription_db.subscriptions TO 'admin'@'localhost';
GRANT ALTER ROUTINE, CREATE ROUTINE, EXECUTE ON *.* TO 'admin'@'localhost'; 
FLUSH PRIVILEGES;