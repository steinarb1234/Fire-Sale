
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
('Electronics'),
('Cars'),
('Bikes'),
('Boats');

INSERT INTO category_category (name, parent_id)
VALUES
('Men''s fashion', '1'),
('Women''s fashion', '1'),
('Computers', '4'),
('Phones', '4'),
('Headphones', '4'),
('Microphones', '4');

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
--     Fashion
('Sun hat', 99.99, 1, 1),
('Leather shoes', 79.99, 1, 1),
('Rolex watch', 59.99, 1, 1),
('Luvon coat S', 1329.99, 1, 1),
('Brown coat', 99.99, 1, 1),
('Vintage Levi Jeans', 49.99, 1, 1),
('Yeezy Boost 350 Shoes', 300.99, 1, 2),
('Gucci Marmont Bag', 1899.99, 1, 3),
('Rolex Submariner Watch', 8999.99, 1, 4),
('Ray-Ban Aviator Sunglasses', 159.99, 1, 5),
('Burberry Trench Coat', 1799.99, 1, 1),
('Tiffany & Co. Necklace', 299.99, 1, 2),
('Prada Wallet', 449.99, 1, 3),
('Nike Air Jordan Sneakers', 159.99, 1, 4),
('Hermes Silk Scarf', 349.99, 1, 5),
('Versace Dress', 699.99, 1, 1),
('Tom Ford Leather Jacket', 2599.99, 1, 2),
('Cartier Love Bracelet', 4999.99, 1, 3),
('Louis Vuitton Speedy Bag', 1099.99, 1, 4),
('Adidas Tracksuit', 99.99, 1, 5),
('Balenciaga Triple S Sneakers', 849.99, 1, 1),
('Chanel Pearl Earrings', 499.99, 1, 2),
('Zara Linen Dress', 49.99, 1, 3),
('Uniqlo Cashmere Sweater', 79.99, 1, 4),
('Topshop Mom Jeans', 69.99, 1, 5),

-- Books
('Harry Potter and the Philosophers Stone', 14.99, 2, 1),
('1984 by George Orwell', 9.99, 2, 2),
('To Kill a Mockingbird by Harper Lee', 12.99, 2, 3),
('The Great Gatsby by F. Scott Fitzgerald', 10.99, 2, 4),
('The Catcher in the Rye by J.D. Salinger', 8.99, 2, 5),
('Pride and Prejudice by Jane Austen', 11.99, 2, 1),
('Moby-Dick by Herman Melville', 14.99, 2, 2),
('War and Peace by Leo Tolstoy', 19.99, 2, 3),
('Ulysses by James Joyce', 16.99, 2, 4),
('The Odyssey by Homer', 14.99, 2, 5),
('Don Quixote by Miguel de Cervantes', 18.99, 2, 1),
('The Divine Comedy by Dante Alighieri', 24.99, 2, 2),
('The Iliad by Homer', 15.99, 2, 3),
('Madame Bovary by Gustave Flaubert', 12.99, 2, 4),
('The Brothers Karamazov by Fyodor Dostoevsky', 17.99, 2, 5),
('The Lord of the Rings by J.R.R. Tolkien', 29.99, 2, 1),
('A Tale of Two Cities by Charles Dickens', 12.99, 2, 2),
('Wuthering Heights by Emily Bronte', 11.99, 2, 3),
('Jane Eyre by Charlotte Bronte', 10.99, 2, 4),
('Dracula by Bram Stoker', 9.99, 2, 5),

-- Plants & gardening
('Monstera Deliciosa', 24.99, 3, 1),
('Fiddle Leaf Fig', 29.99, 3, 2),
('Snake Plant', 19.99, 3, 3),
('ZZ Plant', 21.99, 3, 4),
('Spider Plant', 18.99, 3, 5),
('Succulent Collection - Set of 5', 15.99, 3, 1),
('Japanese Maple Tree', 59.99, 3, 2),
('Bonsai Tree Kit', 39.99, 3, 3),
('Herb Garden Starter Kit', 24.99, 3, 4),
('Orchid Plant', 29.99, 3, 5),
('Rose Bush', 24.99, 3, 1),
('Bamboo Plant', 18.99, 3, 2),
('Mushroom Grow Kit', 34.99, 3, 3),
('Lavender Plant', 16.99, 3, 4),
('Garden Tool Set', 39.99, 3, 5),
('Garden Gnome', 14.99, 3, 1),
('Compost Bin', 49.99, 3, 2),
('Bird Feeder', 29.99, 3, 3),
('Ceramic Plant Pot', 19.99, 3, 4),
('Terrarium Kit', 34.99, 3, 5),

-- Electronics
('Apple iPhone 12', 699.99, 4, 1),
('Samsung Galaxy S21', 799.99, 4, 2),
('Sony PlayStation 5', 499.99, 4, 3),
('Nintendo Switch Console', 299.99, 4, 4),
('Canon EOS M50 Camera', 579.99, 4, 5),
('Apple MacBook Pro 15 inch', 1299.99, 4, 1),
('Dell XPS 13 Laptop', 999.99, 4, 2),
('Bose QuietComfort 35 Headphones', 299.99, 4, 3),
('Apple iPad Pro 11 inch', 799.99, 4, 4),
('Samsung QLED 4K TV', 999.99, 4, 5),
('Google Pixel 6', 699.99, 4, 1),
('Amazon Echo Dot', 49.99, 4, 2),
('Apple Watch Series 6', 399.99, 4, 3),
('Sonos One Speaker', 199.99, 4, 4),
('Microsoft Surface Pro 7', 899.99, 4, 5),
('Apple AirPods Pro', 249.99, 4, 1),
('GoPro Hero9', 399.99, 4, 2),
('HP OfficeJet Pro 9015 Printer', 229.99, 4, 3),
('Roku Streaming Stick+', 49.99, 4, 4),
('Fitbit Charge 4', 129.99, 4, 5),

-- Cars
('2022 BMW 3 Series', 41000.00, 5, 1),
('2023 Mercedes Benz C-Class', 42000.00, 5, 2),
('2022 Audi A4', 39000.00, 5, 3),
('2023 Tesla Model 3', 45000.00, 5, 4),
('2022 Lexus IS', 38000.00, 5, 5),
('2022 Honda Accord', 24000.00, 5, 1),
('2023 Toyota Camry', 25000.00, 5, 2),
('2022 Ford Mustang', 27000.00, 5, 3),
('2022 Chevrolet Camaro', 26000.00, 5, 4),
('2022 Porsche 911 Carrera', 99000.00, 5, 5),
('2023 Audi R8', 142000.00, 5, 1),
('2022 Lamborghini Huracan', 207000.00, 5, 2),
('2023 Ferrari 488', 250000.00, 5, 3),
('2022 Bentley Continental', 200000.00, 5, 4),
('2023 Rolls-Royce Ghost', 311000.00, 5, 5),
('2022 Aston Martin DB11', 205000.00, 5, 1),
('2022 Subaru Impreza', 19000.00, 5, 2),
('2022 Hyundai Sonata', 23000.00, 5, 3),
('2023 Mazda3', 21000.00, 5, 4),
('2022 Nissan Altima', 24000.00, 5, 5),

-- Bikes
('Trek Marlin 5 Mountain Bike', 539.99, 6, 1),
('Giant Defy Advanced 2 Road Bike', 2199.99, 6, 2),
('Cannondale Trail 8 Mountain Bike', 485.99, 6, 3),
('Specialized Roubaix Sport Road Bike', 2900.99, 6, 4),
('Cervelo P-Series Triathlon Bike', 3200.99, 6, 5),
('Bianchi Via Nirone 7 Road Bike', 1150.99, 6, 1),
('Santa Cruz Hightower Mountain Bike', 2999.99, 6, 2),
('Scott Foil 10 Road Bike', 4999.99, 6, 3),
('Yeti SB130 Mountain Bike', 5299.99, 6, 4),
('Cube Aim Race Mountain Bike', 579.99, 6, 5),
('Merida Reacto 5000 Road Bike', 2400.99, 6, 1),
('Canyon Neuron AL 6.0 Mountain Bike', 2199.99, 6, 2),
('Orbea Orca M20iLTD Road Bike', 4499.99, 6, 3),
('Ghost Kato 5.9 Mountain Bike', 999.99, 6, 4),
('Ribble Endurance AL Disc Road Bike', 1399.99, 6, 5),
('GT Aggressor Expert Mountain Bike', 649.99, 6, 1),
('Pinarello Dogma F12 Road Bike', 12000.99, 6, 2),
('Mongoose Dolomite Fat Tire Mountain Bike', 329.99, 6, 3),
('Schwinn Phocus 1400 Road Bike', 549.99, 6, 4),
('Diamondback Overdrive 29 Mountain Bike', 649.99, 6, 5),

-- Boats
('2023 Bayliner VR5 Bowrider', 34999.99, 7, 1),
('2022 Sun Tracker Bass Buggy 16 XL', 18999.99, 7, 2),
('2023 Yamaha AR210 Jet Boat', 43999.99, 7, 3),
('2022 Boston Whaler 130 Super Sport', 15999.99, 7, 4),
('2023 Sea Ray SDX 250 Outboard', 79999.99, 7, 5),
('2023 Tracker Targa V-19 Combo', 39999.99, 7, 1),
('2022 Bennington SX Series Pontoon', 34999.99, 7, 2),
('2023 Malibu 24 MXZ Wake Boat', 129999.99, 7, 3),
('2022 Barletta Cabrio Pontoon Boat', 59999.99, 7, 4),
('2023 Regal LS6 Surf Boat', 99999.99, 7, 5),
('2022 Mastercraft XStar Wakeboarding Boat', 169999.99, 7, 1),
('2023 Cobalt R30 Cruiser', 159999.99, 7, 2),
('2022 Chaparral 21 SSi Sport Boat', 49999.99, 7, 3),
('2023 Sea-Doo Fish Pro Sport Fishing Jet Ski', 15999.99, 7, 4),
('2022 Scarab 195 Open Jet Boat', 34999.99, 7, 5),
('2023 Glastron GTD 205 Deck Boat', 49999.99, 7, 1),
('2022 Lowe SS210 CL Pontoon Boat', 29999.99, 7, 2),
('2023 Harris Sunliner 230 Pontoon Boat', 39999.99, 7, 3),
('2022 Grady-White Freedom 215 Dual Console', 89999.99, 7, 4),
('2023 Nautique Super Air G23 Paragon Wake Boat', 239999.99, 7, 5),

-- Mens Fashion
('Tom Ford Leather Jacket', 2599.99, 8, 1),
('Rolex Submariner Watch', 8999.99, 8, 2),
('Ray-Ban Aviator Sunglasses', 159.99, 8, 3),
('Yeezy Boost 350 Shoes', 300.99, 8, 4),
('Burberry Trench Coat', 1799.99, 8, 5),
('Nike Air Jordan Sneakers', 159.99, 8, 1),
('Hugo Boss Suit', 699.99, 8, 2),
('Ralph Lauren Polo Shirt', 89.99, 8, 3),
('Versace Tie', 149.99, 8, 4),
('Calvin Klein Jeans', 79.99, 8, 5),
('Tommy Hilfiger Sweater', 69.99, 8, 1),
('Armani Exchange Belt', 49.99, 8, 2),
('Adidas Tracksuit', 99.99, 8, 3),
('Levis 501 Original Fit Jeans', 59.99, 8, 4),
('Timberland Boots', 129.99, 8, 5),
('Fred Perry Polo Shirt', 89.99, 8, 1),
('Lacoste Sneakers', 99.99, 8, 2),
('Dolce & Gabbana Wallet', 199.99, 8, 3),
('Puma Sports T-shirt', 29.99, 8, 4),
('G-Star Raw Denim Jacket', 159.99, 8, 5),

-- Womens fashion
('Chanel Little Black Dress', 3000.99, 9, 1),
('Gucci Marmont Bag', 1899.99, 9, 2),
('Prada Ballet Flats', 450.99, 9, 3),
('Burberry Trench Coat', 1799.99, 9, 4),
('Tiffany & Co. Heart Pendant Necklace', 199.99, 9, 5),
('Hermes Silk Scarf', 349.99, 9, 1),
('Versace Print Dress', 899.99, 9, 2),
('Louis Vuitton Speedy Bag', 1099.99, 9, 3),
('Cartier Love Bracelet', 5999.99, 9, 4),
('Dolce & Gabbana Lace Dress', 1999.99, 9, 5),
('Fendi Peekaboo Bag', 3299.99, 9, 1),
('Jimmy Choo Crystal Heels', 995.99, 9, 2),
('Christian Louboutin So Kate Pumps', 725.99, 9, 3),
('Valentino Rockstud Flats', 745.99, 9, 4),
('Givenchy Antigona Bag', 2390.99, 9, 5),
('Yves Saint Laurent Monogram Clutch', 1190.99, 9, 1),
('Chloe Marcie Bag', 1490.99, 9, 2),
('Bottega Veneta Padded Cassette Bag', 2899.99, 9, 3),
('Balenciaga Hourglass Bag', 2150.99, 9, 4),
('Alexander McQueen Skull Scarf', 345.99, 9, 5),

-- Computers
('Apple MacBook Pro 16''', 2399.99, 10, 1),
('Dell XPS 15', 1899.99, 10, 2),
('Microsoft Surface Laptop 3', 1299.99, 10, 3),
('HP Spectre x360', 1499.99, 10, 4),
('Lenovo ThinkPad X1 Carbon', 1399.99, 10, 5),
('ASUS ROG Strix Gaming Laptop', 1699.99, 10, 1),
('Acer Predator Helios 300', 1199.99, 10, 2),
('Alienware M17 R4', 2299.99, 10, 3),
('Apple MacBook Air', 999.99, 10, 4),
('Samsung Galaxy Book Flex', 1249.99, 10, 5),
('Razer Blade 15', 1999.99, 10, 1),
('Microsoft Surface Pro 7', 899.99, 10, 2),
('Lenovo Yoga C940', 1099.99, 10, 3),
('HP Pavilion 15', 649.99, 10, 4),
('ASUS VivoBook 15', 499.99, 10, 5),
('Dell Inspiron 15', 549.99, 10, 1),
('Acer Aspire 5', 399.99, 10, 2),
('Apple iMac 27''', 1799.99, 10, 3),
('Dell Alienware Aurora R10 Gaming Desktop', 1899.99, 10, 4),
('HP Envy Desktop', 899.99, 10, 5),

-- Phones
('Apple iPhone 13 Pro', 999.99, 11, 1),
('Samsung Galaxy S22 Ultra', 1199.99, 11, 2),
('Google Pixel 6 Pro', 899.99, 11, 3),
('OnePlus 10 Pro', 799.99, 11, 4),
('Huawei P50 Pro', 1099.99, 11, 5),
('Xiaomi Mi 12 Ultra', 899.99, 11, 1),
('OPPO Find X5 Pro', 1099.99, 11, 2),
('Sony Xperia 1 IV', 1199.99, 11, 3),
('Nokia 9.3 PureView', 799.99, 11, 4),
('Asus ROG Phone 5s Pro', 999.99, 11, 5),
('Motorola Moto G200', 399.99, 11, 1),
('Realme GT 2 Pro', 499.99, 11, 2),
('BlackBerry Key3', 699.99, 11, 3),
('LG Velvet 2', 599.99, 11, 4),
('ZTE Axon 30 Ultra', 749.99, 11, 5),
('Vivo X70 Pro Plus', 849.99, 11, 1),
('Honor Magic 3 Pro+', 999.99, 11, 2),
('Fairphone 4', 599.99, 11, 3),
('TCL 20 Pro 5G', 499.99, 11, 4),
('Lenovo Legion Phone Duel 2', 799.99, 11, 5),

-- Headphones
('Sony WH-1000XM4', 349.99, 12, 1),
('Bose QuietComfort 35 II', 299.99, 12, 2),
('Apple AirPods Pro', 249.99, 12, 3),
('Sennheiser HD 660 S', 499.99, 12, 4),
('Beats by Dre Studio3', 349.99, 12, 5),
('Jabra Elite 85h', 249.99, 12, 1),
('Audio-Technica ATH-M50x', 149.99, 12, 2),
('Beyerdynamic DT 990 Pro', 179.99, 12, 3),
('JBL Free X', 119.99, 12, 4),
('Anker Soundcore Life Q20', 59.99, 12, 5),
('Plantronics BackBeat Pro 2', 199.99, 12, 1),
('Samsung Galaxy Buds Pro', 199.99, 12, 2),
('AKG K702', 229.99, 12, 3),
('Grado SR80e', 99.99, 12, 4),
('Skullcandy Crusher Wireless', 149.99, 12, 5),
('Panasonic RP-HD805N', 249.99, 12, 1),
('Razer Nari Ultimate', 199.99, 12, 2),
('SteelSeries Arctis Pro', 179.99, 12, 3),
('HyperX Cloud II', 99.99, 12, 4),
('Astro A50', 299.99, 12, 5),

-- Microphones
('Audio-Technica AT2020', 99.99, 13, 1),
('Shure SM58', 99.99, 13, 2),
('Rode NT1', 269.99, 13, 3),
('Blue Yeti USB', 129.99, 13, 4),
('Neumann U87', 2699.99, 13, 5),
('AKG C414', 899.99, 13, 1),
('Sennheiser MKH416', 999.99, 13, 2),
('MXL 990', 69.99, 13, 3),
('Rode NT-USB', 169.99, 13, 4),
('Behringer C-1', 49.99, 13, 5),
('Samson Meteor Mic', 69.99, 13, 1),
('Heil PR40', 329.99, 13, 2),
('Blue Snowball iCE', 49.99, 13, 3),
('Audio-Technica ATR2100x-USB', 99.99, 13, 4),
('Shure SM7B', 399.99, 13, 5),
('Rode Procaster', 229.99, 13, 1),
('AKG D5', 69.99, 13, 2),
('Lewitt LCT 440 PURE', 269.99, 13, 3),
('Marantz Professional MPM-2000U', 149.99, 13, 4),
('Blue Spark Blackout SL XLR', 199.99, 13, 5)
;



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
('4', 'https://images.unsplash.com/photo-1574201635302-388dd92a4c3f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=765&q=80'),
('5', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('6', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('7', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('8', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('9', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('10', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('11', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'),
('12', 'https://plus.unsplash.com/premium_photo-1673757120930-6cab166776b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80');


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
(1, 3),
(2, 3),
(3, 4),
(4, 4),
(1, 5),
(2, 4),
(3, 2),
(4, 1);
