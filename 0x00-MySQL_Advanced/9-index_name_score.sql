-- creates an index on table and first name of field name and score
ALTER TABLE names ADD INDEX idx_name_first (name, score) KEY_BLOCK_SIZE = 1;
