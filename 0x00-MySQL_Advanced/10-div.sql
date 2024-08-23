-- Task 10: Safe Divide
-- Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

-- Delete SafeDiv if it exists
DROP FUNCTION IF EXISTS SafeDiv;
-- Change Delimiter
DELIMITER $$
-- Create function
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
READS SQL DATA
BEGIN
	-- Declare result
	DECLARE result FLOAT DEFAULT 0;

	-- Calculate
	IF b = 0 THEN
		SET result = 0;
	ELSE
		SET result = a / b;
	END IF;

	-- Return result
	RETURN result;
END $$

DELIMITER ;
