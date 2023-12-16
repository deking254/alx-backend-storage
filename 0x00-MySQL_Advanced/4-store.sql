-- create a trigger that reduces the number in the items table when a new order is inserted
DROP TRIGGER IF EXISTS new_order;
CREATE TRIGGER new_order AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
