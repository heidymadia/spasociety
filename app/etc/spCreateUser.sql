CREATE PROCEDURE `spCreateUser` (
	IN p_firstname varchar(47),
    IN p_lastname varchar(47),
    IN p_username varchar(47),
    IN p_email text,
    IN p_password varchar(47)
)
BEGIN
	IF (SELECT EXISTS(SELECT 1 FROM `SPASOCIETY_STORE`.`user` WHERE username = p_username)) THEN
		SELECT "Username Exist !!";
    ELSE
		INSERT INTO `SPASOCIETY_STORE`.`user`
        (
			firstname,
            lastname,
            username,
            email,
            password
		)
        VALUES
        (
			p_firstname,
            p_lastname,
            p_username,
            p_email,
            p_password
        );
	END IF;
END
