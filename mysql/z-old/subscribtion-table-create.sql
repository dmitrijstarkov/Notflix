CREATE TABLE `subscription_db`.`subscriptions` (
    
    `subscr_id` VARCHAR(120),
    `sub_start_date`  VARCHAR(120),
    `user_id` BIGINT,
    `ipn_id`  VARCHAR(120),
    `paypal_email`  VARCHAR(120),
    `payer_id`  VARCHAR(120)
  
  PRIMARY KEY (`subscr_id`));
