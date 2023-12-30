-- creates an index on table and first name of field name and score
ALTER TABLE names ADD INDEX idx_name_first_score USING BTREE (name (1), score);
