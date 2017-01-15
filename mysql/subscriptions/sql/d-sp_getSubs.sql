DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getSub`(
	IN p_user_id BIGINT )
BEGIN
    select sub_start_date, paypal_email from subscriptions;
END $$
DELIMITER ;