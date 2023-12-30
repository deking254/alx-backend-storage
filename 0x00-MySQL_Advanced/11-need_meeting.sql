-- creates a view that has has no last_meeting
CREATE OR REPLACE VIEW need_meeting AS SELECT name FROM students WHERE score < 80  AND (ADDDATE(CURRENT_DATE, INTERVAL 0 MONTH) - last_meeting  > 100 OR last_meeting IS NULL);
