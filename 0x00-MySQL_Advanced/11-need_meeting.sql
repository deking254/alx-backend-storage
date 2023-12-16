-- creates a view that has has no last_meeting
CREATE VIEW need_meeting AS SELECT name, last_meeting FROM students;
