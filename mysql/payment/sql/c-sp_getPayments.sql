DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getPayments`(
	IN p_user_id BIGINT )
BEGIN
    select payment_date, amount, status, txn_id from payments;
END $$
DELIMITER ;