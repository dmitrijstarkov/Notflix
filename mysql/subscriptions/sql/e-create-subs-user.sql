CREATE USER 'subs'@'172.24.0.7' IDENTIFIED BY 'this15anew_paw04d';
GRANT SELECT, INSERT, UPDATE on subscription_db.subscriptions TO 'subs'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE subscription_db.sp_createSub TO 'subs'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE subscription_db.sp_checkSub TO 'subs'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE subscription_db.sp_getSub TO 'subs'@'172.24.0.7';
FLUSH PRIVILEGES;