DROP TABLE IF EXISTS list_items;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS shopping_list;
DROP TABLE IF EXISTS categories;

 
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
 
CREATE TABLE shopping_list (
    id SERIAL PRIMARY KEY,
    date_created DATE NOT NULL,
    date_shopped DATE,
    name VARCHAR(255)
);
 
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cat_id int REFERENCES categories(id) ON DELETE CASCADE
);
 
CREATE TABLE  list_items(
    id SERIAL PRIMARY KEY,
    list_id int REFERENCES shopping_list(id) ON DELETE CASCADE,
    item_id int REFERENCES items(id) ON DELETE CASCADE,
    selected boolean NOT NULL,
    quantity int
);
 
INSERT INTO categories (name) VALUES ('Dairy'); --1
INSERT INTO categories (name) VALUES ('Fruit'); --2
INSERT INTO categories (name) VALUES ('Vegetables');  --3
INSERT INTO categories (name) VALUES ('Meat'); --4
INSERT INTO categories (name) VALUES ('Needy'); --5
INSERT INTO categories (name) VALUES ('Bakery'); --6
INSERT INTO categories (name) VALUES ('Home Baking'); --7
INSERT INTO categories (name) VALUES ('Store Cupboard'); --8
INSERT INTO categories (name) VALUES ('Tins'); --9
INSERT INTO categories (name) VALUES ('World Food'); --10
INSERT INTO categories (name) VALUES ('Eggs'); --11


INSERT INTO shopping_list (date_created, name) VALUES ('2023-03-20', 'Pizza Party');
INSERT INTO shopping_list (date_created, date_shopped, name) VALUES ('2023-03-24','2023-03-25', 'Camping Trip');
INSERT INTO shopping_list (date_created, date_shopped, name) VALUES ('2023-03-24', '2023-03-27', 'Mum');

INSERT INTO items (name, cat_id) VALUES ('Milk',1);  --1
INSERT INTO items (name, cat_id) VALUES ('Yoghurt',1);  --2
INSERT INTO items (name, cat_id) VALUES ('Mozzerella',1);  --3
INSERT INTO items (name, cat_id) VALUES ('Bananas',2); --4
INSERT INTO items (name, cat_id) VALUES ('Apples',2); --5
INSERT INTO items (name, cat_id) VALUES ('Bread',6); --6
INSERT INTO items (name, cat_id) VALUES ('Peanut Butter',8); --7
INSERT INTO items (name, cat_id) VALUES ('Eggs',11); --8
INSERT INTO items (name, cat_id) VALUES ('Chicken',4); --9
INSERT INTO items (name, cat_id) VALUES ('Potatoes',3); --10
INSERT INTO items (name, cat_id) VALUES ('Onions',3); --11
INSERT INTO items (name, cat_id) VALUES ('Strawberries',2); --12
INSERT INTO items (name, cat_id) VALUES ('Mince',4); --12
INSERT INTO items (name, cat_id) VALUES ('Basil',3); --14
INSERT INTO items (name, cat_id) VALUES ('Passata',9); --15
INSERT INTO items (name, cat_id) VALUES ('Peppers',3); --16
INSERT INTO items (name, cat_id) VALUES ('Flour',7); --17
INSERT INTO items (name, cat_id) VALUES ('Teabags',8); --17
INSERT INTO items (name, cat_id) VALUES ('Coffee',8); --17
INSERT INTO items (name, cat_id) VALUES ('Fajita Seasoning',10); --17
INSERT INTO items (name, cat_id) VALUES ('Noodles',10); --17
INSERT INTO items (name, cat_id) VALUES ('Sugar',7); --17


INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,11,3, False); -- shopping list 1, mozz
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,3, 5, False); -- shopping list 1, bananas
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,14, 1, False); -- shopping list 1, basil
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,15, 1, False); -- shopping list 1, Passata
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,16, 2, False); -- shopping list 1, Peppers
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (1,17, 2, False); -- shopping list 1, flour
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (2,1, 1, False); -- shopping list 2, milk
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (2,2, 4, True); -- shopping list 2, yoghurt
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (2,4, 6, True); -- shopping list 2, apples
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (2,5, 1, True); -- shopping list 2, bread
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (2,6, 1, True); -- shopping list 2, peanut butter
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (3,1, 2, True); -- shopping list 3, apples
INSERT INTO list_items (list_id, item_id, quantity, selected) VALUES (3,12, 1, True); -- shopping list 3, potatoes