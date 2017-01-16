DELIMITER $$
CREATE DEFINER=`admin`@`localhost` PROCEDURE `sp_updatePassword`(

    IN p_id BIGINT,
    IN p_password VARCHAR(200)
)
BEGIN
UPDATE login SET user_password = p_password WHERE user_id = p_id;
END $$
DELIMITER ;