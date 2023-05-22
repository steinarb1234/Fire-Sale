

INSERT INTO user_user (user_name, email)
VALUES 
('Fashion', '');

INSERT INTO category_category (name, image)
VALUES 
('Fashion', '');


INSERT INTO item_item (name, price, category_id, seller_id)
VALUES 
('Sun hat', 99.99, 1, 1),
('Leather shoes', 79.99, 1, 1),
('Rolex watch', 59.99, 1, 1);

INSERT INTO item_itemstats (item_id, views, watchers, status)
VALUES 
('1', '100', '10', 'Unsold'),
('2', '150', '10', 'Unsold'),
('3', '50' , '10', 'Unsold');

INSERT INTO item_itemdetails (item_stats_id, condition, description)
VALUES 
('1', 'New', 'This is a brand new item.'),
('2', 'Used', 'This item is slightly used but in good condition.'),
('3', 'New', 'This item is brand new and unopened.');








