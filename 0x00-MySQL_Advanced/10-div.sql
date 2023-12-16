-- creates a function that returns the division of two ints
DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	IF b != 0 THEN
		BEGIN
			SET result = a / b;
		END;
	ELSE
		BEGIN
			SET result = 0;
		END;
	END IF;
	RETURN result;
END; //
DELIMITER ;
