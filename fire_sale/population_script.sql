
INSERT INTO user_user (user_name, email)
VALUES 
('steinarb1234', 'steinarb20@ru.is'),
('bjarkibjarki', 'bjarkiss20@ru.is');

INSERT INTO user_userinfo (user_id, full_name, avg_rating, image)
VALUES 
(1, 'Steinar Björnsson', 5, ''),
(2, 'Bjarki Smári Smárason', 0, '');

INSERT INTO user_userprofile (user_info_id, country, address, city, zip_code, bio)
VALUES 
(1, 'USA', '123 Any Street', 'New York', '10001', 'I love coding and databases.'),
(2, 'Canada', '456 Another Ave', 'Toronto', 'M5B2G9', 'I am a software developer.');

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

INSERT INTO offer_offer (amount, buyer_id, item_id, seller_id)
VALUES 
(100.00, , 1, 2),
(200.00, 2, 2, 3),
(150.00, , 3, 1),
(300.00, 2, 1, 1),
(250.00, 1, 2, 2);

INSERT INTO offer_offerdetails (start_date, end_date, message, offer_id)
VALUES 
('2023-01-01', '2023-01-31', 'Offer valid for the month of January', 1),
('2023-02-01', '2023-02-28', 'Offer valid for the month of February', 2),
('2023-03-01', '2023-03-31', 'Offer valid for the month of March', 3),
('2023-04-01', '2023-04-30', 'Offer valid for the month of April', 4),
('2023-05-01', '2023-05-31', 'Offer valid for the month of May', 5);




