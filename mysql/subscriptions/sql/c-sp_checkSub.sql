DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_checkSub`(
	IN p_user_id BIGINT )
BEGIN

select user_id from subscriptions where p_user_id = user_id;

END $$
DELIMITER ;