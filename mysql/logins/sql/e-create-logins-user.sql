CREATE USER 'logins'@'172.24.0.7' IDENTIFIED BY 'w44tldsg4';
GRANT SELECT, INSERT, UPDATE on logins_db.login TO 'logins'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE logins_db.sp_createUser3 TO 'logins'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE logins_db.sp_login16 TO 'logins'@'172.24.0.7';
GRANT EXECUTE ON PROCEDURE logins_db.sp_updatePassword TO 'logins'@'172.24.0.7';
FLUSH PRIVILEGES;