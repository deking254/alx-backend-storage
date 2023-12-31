-- calculates the weighted average
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE IF NOT EXISTS ComputeAverageWeightedScoreForUser (IN user_id INT) MODIFIES SQL DATA
BEGIN
	-- DECLARE total_weight INT;
	-- DECLARE weighted_average FLOAT;
	-- SELECT SUM(weight) INTO total_weight FROM projects;
	-- SELECT SUM((weight / total_weight) * score) INTO weighted_average FROM corrections JOIN projects WHERE corrections.project_id = projects.id AND corrections.user_id = user_id;
	-- UPDATE users SET average_score = weighted_average WHERE id = user_id;
	SELECT * FROM users;
END;//
DELIMITER ;
