DROP TABLE IF EXISTS list_items;
DROP TABLE IF EXISTS grocery_item;
DROP TABLE IF EXISTS shopping_list;
DROP TABLE IF EXISTS categories;

 
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
 
CREATE TABLE shopping_list (
    id SERIAL PRIMARY KEY,
    date_shopped DATE
);
 
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cat_id int REFERENCES categories(id)
);
 
CREATE TABLE  list_items(
    id SERIAL PRIMARY KEY,
    list_id int REFERENCES shopping_list(id),
    item_id int REFERENCES items(id)
);
 
INSERT INTO categories (name) VALUES ('dairy'); --1
INSERT INTO categories (name) VALUES ('fruit'); --2
INSERT INTO categories (name) VALUES ('vegetables');  --3
INSERT INTO categories (name) VALUES ('meat'); --4
INSERT INTO categories (name) VALUES ('needy'); --5
INSERT INTO categories (name) VALUES ('bakery'); --6

INSERT INTO shopping_list (date_shopped) VALUES ('2023-03-24');
INSERT INTO shopping_list (date_shopped) VALUES ('2023-03-25');

INSERT INTO items (name, cat_id) VALUES ('milk',1);  --1
INSERT INTO items (name, cat_id) VALUES ('yoghurt',1);  --2
INSERT INTO items (name, cat_id) VALUES ('bananas',2); --3
INSERT INTO items (name, cat_id) VALUES ('apples',2); --4
INSERT INTO items (name, cat_id) VALUES ('bread',6); --5

INSERT INTO list_items (list_id, item_id) VALUES (1,1); -- shopping list 1, milk
INSERT INTO list_items (list_id, item_id) VALUES (1,3); -- shopping list 1, bananas
INSERT INTO list_items (list_id, item_id) VALUES (1,5); -- shopping list 1, bread
INSERT INTO list_items (list_id, item_id) VALUES (2,1); -- shopping list 2, milk
INSERT INTO list_items (list_id, item_id) VALUES (2,2); -- shopping list 2, yoghurt
INSERT INTO list_items (list_id, item_id) VALUES (2,4); -- shopping list 2, apples