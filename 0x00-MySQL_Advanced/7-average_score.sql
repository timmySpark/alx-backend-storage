-- Task 7: Average Score
-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
--	user_id, a users.id value (you can assume user_id is linked to an existing users)

-- Drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Change Delimiter
DELIMITER $$

-- Create procedure
CREATE PROCEDURE ComputeAverageScoreForUser (
	user_id INT
)
BEGIN
	-- Declare average
	DECLARE average_score FLOAT;

	-- Search for User
	SELECT AVG(score) INTO average_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET users.average_score = average_score
	WHERE users.id = user_id;
END $$

DELIMITER ;
