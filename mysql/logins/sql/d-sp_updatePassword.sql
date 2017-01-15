DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updatePassword`(

    IN p_id VARCHAR(120),
    IN p_password VARCHAR(120)
)
BEGIN
UPDATE login SET user_password = p_password WHERE user_id = p_id;
END $$
DELIMITER ;