CREATE TABLE `payment_db`.`payments`(
	`sub_id` VARCHAR(120),
	`payment_date` DATETIME,
	`user_id` BIGINT,
	`ipn_id` VARCHAR(120),
	`verif_id` VARCHAR(200),
	`amount` DECIMAL(6,2),
	`status` VARCHAR(120),
	`txn_id` VARCHAR(120),
    PRIMARY KEY (`txn_id`));