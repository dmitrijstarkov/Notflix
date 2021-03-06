DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createPayment`(
	IN p_sub_id VARCHAR(120),
	IN p_date DATETIME,
	IN p_user_id BIGINT,
	IN p_ipn_id VARCHAR(120),
	IN p_verif VARCHAR(200),
	IN p_amount DECIMAL(6,2),
	IN p_status VARCHAR(120),
	IN p_txn_id VARCHAR(120))
BEGIN
IF 
    (select exists (select 1 from payments where p_txn_id = txn_id))
THEN
    select "already-paid";
ELSE
    insert into payments 
    (sub_id,payment_date,user_id,ipn_id,verif_id,amount,status,txn_id)
    values
        (p_sub_id,p_date,p_user_id,p_ipn_id,p_verif,p_amount,p_status,p_txn_id);
END IF ;
END $$
DELIMITER ;