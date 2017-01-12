DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createPayment`(
	IN p_sub_id VARCHAR(120),
	IN p_date VARCHAR(120),
	IN p_user_id BIGINT,
	IN p_ipn_id VARCHAR(120),
	IN p_verif VARCHAR(200),
	IN p_amount DECIMAL(6,2),
	IN p_status VARCHAR(120),
	IN p_txn_id BIGINT)
BEGIN
insert into payments 
(subscr_id,payment_date,user_id,ipn_id,verification_id,amount,payment_status,txn_id)
values
(p_sub_id,p_date,p_user_id,p_ipn_id,p_verif,p_amount,p_status,p_txn_id);
END $$ 
DELIMITER ;