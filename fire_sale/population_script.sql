
INSERT INTO user_user (user_name, email)
VALUES
('steinarb1234', 'steinarb20@ru.is'),
('magnusb', 'magnus.brarnfredsson@gmail.com'),
('thorhilduramma', 'thorhildurr20@ru.is'),
('bjarkibjarki', 'bjarkiss20@ru.is'),
('beinteinn ', 'beinteinn@gmail.is');

INSERT INTO user_userinfo (user_id, full_name, avg_rating, image)
VALUES
(1, 'Steinar Björnsson', 5, 'https://images.unsplash.com/photo-1518882570151-157128e78fa1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80'),
(2, 'Magnús Bjarnfreðsson', 3, 'https://images.unsplash.com/photo-1518882570151-157128e78fa1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80'),
(3, 'Þórhildur Anna Ragnarsdóttir', 4.9, 'https://images.unsplash.com/photo-1579880651719-3cef00eae7de?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1964&q=80'),
(4, 'Bjarki Smári Smárason', 0, 'https://images.unsplash.com/photo-1518882570151-157128e78fa1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80'),
(5, 'Beinteinn', 5, 'https://plus.unsplash.com/premium_photo-1677507321948-d3f8b80fe6d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80');


INSERT INTO user_userprofile (user_info_id, country, address, city, zip_code, bio)
VALUES
(1, 'USA', '123 Any Street', 'New York', '10001', 'I love coding and databases.'),
(2, 'Saudi Arabia', '123 Any Street', 'Ryadh', '10001', 'I love coding and databases.'),
(3, 'Iceland', '123 tossa', 'Vesturgata 4', '10001', 'I love big wine glasses.'),
(4, 'Canada', '456 Another Ave', 'Toronto', 'M5B2G9', 'I am a software developer.'),
(5, 'Iceland', 'Ásvallagata 11', 'Reykjavík', '101', 'Mergur og bein.');

INSERT INTO category_category (name)
VALUES
('Fashion'),
('Books'),
('Plants & gardening'),
('Electr0incs'),
('Cars'),
('Bikes'),
('Boats');

INSERT INTO category_category (name, parent_id)
VALUES
('Men´s fashion', '1'),
('Women´s fasion', '1'),
('Computers', '6'),
('Phones', '6'),
('Headphones', '6'),
('Microphones', '6');

INSERT INTO category_categoryviews (category_id, user_id, category_views)
VALUES
(1, 1, 10),
(2, 1, 15),
(3, 1, 12),
(4, 1, 8),
(5, 1, 16),
(6, 1, 9),
(7, 1, 14),
(8, 1, 11),
(9, 1, 13),
(10, 1, 7),
(11, 1, 16),
(12, 1, 10),
(13, 1, 9),
(1, 2, 12),
(2, 2, 16),
(3, 2, 8),
(4, 2, 14),
(5, 2, 9),
(6, 2, 11),
(7, 2, 13),
(8, 2, 7),
(9, 2, 10),
(10, 2, 9),
(11, 2, 12),
(12, 2, 16),
(13, 2, 8),
(1, 3, 10),
(2, 3, 15),
(3, 3, 12),
(4, 3, 8),
(5, 3, 16),
(6, 3, 9),
(7, 3, 14),
(8, 3, 11),
(9, 3, 13),
(10, 3, 7),
(11, 3, 16),
(12, 3, 10),
(13, 3, 9),
(1, 4, 12),
(2, 4, 16),
(3, 4, 8),
(4, 4, 14),
(5, 4, 9),
(6, 4, 11),
(7, 4, 13),
(8, 4, 7),
(9, 4, 10),
(10, 4, 9),
(11, 4, 12),
(12, 4, 16),
(13, 4, 8),
(1, 5, 10),
(2, 5, 15),
(3, 5, 12),
(4, 5, 8),
(5, 5, 16),
(6, 5, 9),
(7, 5, 14),
(8, 5, 11),
(9, 5, 13),
(10, 5, 7),
(11, 5, 16),
(12, 5, 10),
(13, 5, 9);


INSERT INTO item_item (name, price, category_id, seller_id)
VALUES
('Sun hat', 99.99, 1, 1),
('Leather shoes', 79.99, 1, 1),
('Rolex watch', 59.99, 1, 1),
('Luvon coat S', 1329.99, 1, 1);

INSERT INTO item_itemstats (item_id, views, watchers, status)
VALUES
('1', '100', '10', 'Not sold'),
('2', '150', '10', 'Not sold'),
('3', '50' , '10', 'Not sold'),
('4', '50' , '10', 'Not sold');

INSERT INTO item_itemdetails (item_stats_id, condition, description)
VALUES
('1', 'New', 'This is a brand new item.'),
('2', 'Used', 'This item is slightly used but in good condition.'),
('3', 'New', 'This item is brand new and unopened.'),
('4', 'New', 'This item is brand new and unopened.');

INSERT INTO item_itemimage (item_id, image)
VALUES
('1', 'https://images.unsplash.com/photo-1485462537746-965f33f7f6a7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('2', 'https://images.unsplash.com/photo-1487222477894-8943e31ef7b2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=795&q=80'),
('3', 'https://images.unsplash.com/photo-1469334031218-e382a71b716b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'),
('4', 'https://images.unsplash.com/photo-1574201635302-388dd92a4c3f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=765&q=80');


INSERT INTO offer_offer (amount, buyer_id, item_id, seller_id)
VALUES
(100.00, 3 , 1, 2),
(200.00, 2, 2, 3),
(150.00, 4, 3, 1),
(300.00, 2, 1, 1),
(250.00, 1, 2, 2);




INSERT INTO offer_offerdetails (start_date, end_date, message, offer_id)
VALUES
('2023-01-01', '2023-01-31', 'Offer valid for the month of January', 1),
('2023-02-01', '2023-02-28', 'Offer valid for the month of February', 2),
('2023-03-01', '2023-03-31', 'Offer valid for the month of March', 3),
('2023-04-01', '2023-04-30', 'Offer valid for the month of April', 4),
('2023-05-01', '2023-05-31', 'Offer valid for the month of May', 5);


INSERT INTO watchlist_watchlistitem (item_id, user_id)
VALUES 
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(1, 3),
(2, 3),
(3, 4),
(4, 4),
(5, 5),
(1, 5),
(2, 4),
(3, 2),
(4, 1),
(5, 3);


