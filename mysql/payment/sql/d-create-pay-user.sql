CREATE USER 'pay'@'172.24.0.7' IDENTIFIED BY '385dgh439';
GRANT SELECT, INSERT, UPDATE on payment_db.payments TO 'pay'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE payment_db.sp_createPayment TO 'pay'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE payment_db.sp_getPayments TO 'pay'@'172.24.0.7';
FLUSH PRIVILEGES;