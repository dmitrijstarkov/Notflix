CREATE TABLE `logins_db`.`login` (
    `user_id` BIGINT AUTO_INCREMENT,
    `user_email` VARCHAR(120),
    `user_password` VARCHAR(200),
    PRIMARY KEY (`user_id`));