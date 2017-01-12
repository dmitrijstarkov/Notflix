DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser3`(

    IN p_email VARCHAR(120),
    IN p_password VARCHAR(120)
)
BEGIN
    IF ( select exists (select 1 from login where user_email = p_email) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into login
        (  
            user_email,
            user_password
        )
        values
        (
            p_email,
            p_password
        );
    END IF ;
END $$ 
DELIMITER ;