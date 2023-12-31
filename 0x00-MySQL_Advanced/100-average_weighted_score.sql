-- calculates the weighted average
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE IF NOT EXISTS ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE total_weight INT;
	DECLARE weighted_average FLOAT;
	SELECT SUM(weight) INTO total_weight FROM projects;
	SELECT SUM((weight / total_weight) * score) INTO weighted_average FROM corrections JOIN projects ON corrections.project_id = projects.id AND corrections.user_id = user_id;
	UPDATE users SET average_score = weighted_average WHERE id = user_id;
END //
DELIMITER ;
