-- calculates the weighted average
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
	DROP VIEW IF EXISTS weights_view;
	CREATE VIEW weights_view AS SELECT user_id, (weight / (SELECT SUM(weight) FROM projects)) * score AS weighted_score FROM corrections JOIN projects WHERE corrections.project_id = projects.id;
	DROP VIEW IF EXISTS aggregated_weights;
	CREATE VIEW aggregated_weights AS SELECT user_id, SUM(weighted_score) AS aggregate_weight from weights_view GROUP BY user_id;
	UPDATE users, aggregated_weights SET users.average_score = aggregated_weights.aggregate_weight WHERE users.id = user_id;
END //
DELIMITER ;
