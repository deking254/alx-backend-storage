-- creates an index on table and first name of field name
ALTER TABLE names ADD INDEX idx_name_first (name) KEY_BLOCK_SIZE = 1;
