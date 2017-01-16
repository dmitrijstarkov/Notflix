DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createSub`(
	IN p_sub_id VARCHAR(120),
	IN p_date DATETIME,
	IN p_user_id BIGINT,
	IN p_ipn_id VARCHAR(120),
	IN p_paypal_email VARCHAR(120),
	IN p_payer_id VARCHAR(120))
BEGIN

IF 
    (select exists (select 1 from subscriptions where p_user_id = user_id))
THEN
    select 'Already-Active';
ELSE
    insert into subscriptions 
        (sub_id,sub_start_date,user_id,ipn_id,paypal_email,payer_id)
    values
        (p_sub_id,p_date,p_user_id,p_ipn_id,p_paypal_email,p_payer_id);
END IF ;
END $$
DELIMITER ;