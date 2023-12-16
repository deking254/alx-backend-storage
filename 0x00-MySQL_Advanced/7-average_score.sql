-- a procedure to calucate the average score of the specified user
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE avg_score INT;
	SELECT AVG(score) INTO avg_score FROM corrections WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END;
//
DELIMITER ;
