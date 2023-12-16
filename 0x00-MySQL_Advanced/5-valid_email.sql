-- checks for the validity of the email
CREATE TRIGGER valid BEFORE UPDATE ON users FOR EACH ROW
	SET NEW.valid_email = IF(NEW.email != OLD.email, 0, 1)
