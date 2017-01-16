CREATE USER 'admin'@'localhost' IDENTIFIED BY '125ksdhg3hvk';
GRANT SELECT, INSERT, UPDATE, DELETE ON logins_db.login TO 'admin'@'localhost';
GRANT ALTER ROUTINE, CREATE ROUTINE, EXECUTE ON *.* TO 'admin'@'localhost'; 
FLUSH PRIVILEGES;