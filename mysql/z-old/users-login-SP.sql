DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_login16`(

IN p_email VARCHAR(120),
IN p_password VARCHAR(120)
)

BEGIN

select user_id,user_password from login where user_email = p_email;

END $$ ;