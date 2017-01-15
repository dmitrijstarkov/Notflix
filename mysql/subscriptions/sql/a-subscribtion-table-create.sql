CREATE TABLE `subscription_db`.`subscriptions`(
    `sub_id` VARCHAR(120),
    `sub_start_date` DATETIME,
    `user_id` BIGINT,
    `ipn_id` VARCHAR(120),
    `paypal_email` VARCHAR(120),
    `payer_id` VARCHAR(120),
    PRIMARY KEY (`sub_id`));