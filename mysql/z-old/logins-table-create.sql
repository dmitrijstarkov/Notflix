CREATE TABLE `users`.`user` (
        `user_id` BIGINT AUTO_INCREMENT,
        `user_email` VARCHAR(120),
        `user_password` VARCHAR(120)
    PRIMARY KEY (`user_id`));