-- create a trigger that reduces the number in the items table when a new order is inserted
create trigger new_order after insert on orders for each row update items set quantity = quantity - NEW.number where name = NEW.item_name;
