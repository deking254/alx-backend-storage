-- calculates the weighted average
DELIMITER //
CREATE PROCEDURE IF NOT EXISTS ComputeAverageWeightedScoreForUser(IN userid INT) MODIFIES SQL DATA
BEGIN
	DECLARE total_weight INT;
	DECLARE weighted_average INT;
	SELECT SUM(weight) INTO total_weight FROM projects;
	SELECT SUM((weight / total_weight) * score) INTO weighted_average from corrections join projects where corrections.project_id = projects.id AND corrections.user_id = userid;
	UPDATE users SET average_score = weighted_average WHERE id = userid;
END;//
DELIMITER ;
