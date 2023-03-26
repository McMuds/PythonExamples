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
    date_shopped DATE
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
    selected boolean
);
 
INSERT INTO categories (name) VALUES ('dairy'); --1
INSERT INTO categories (name) VALUES ('fruit'); --2
INSERT INTO categories (name) VALUES ('vegetables');  --3
INSERT INTO categories (name) VALUES ('meat'); --4
INSERT INTO categories (name) VALUES ('needy'); --5
INSERT INTO categories (name) VALUES ('bakery'); --6

INSERT INTO shopping_list (date_created, date_shopped) VALUES ('2023-03-20','2023-03-24');
INSERT INTO shopping_list (date_created) VALUES ('2023-03-25');

INSERT INTO items (name, cat_id) VALUES ('milk',1);  --1
INSERT INTO items (name, cat_id) VALUES ('yoghurt',1);  --2
INSERT INTO items (name, cat_id) VALUES ('bananas',2); --3
INSERT INTO items (name, cat_id) VALUES ('apples',2); --4
INSERT INTO items (name, cat_id) VALUES ('bread',6); --5

INSERT INTO list_items (list_id, item_id, selected) VALUES (1,1, True); -- shopping list 1, milk
INSERT INTO list_items (list_id, item_id, selected) VALUES (1,3, True); -- shopping list 1, bananas
INSERT INTO list_items (list_id, item_id, selected) VALUES (1,5, True); -- shopping list 1, bread
INSERT INTO list_items (list_id, item_id, selected) VALUES (2,1, False); -- shopping list 2, milk
INSERT INTO list_items (list_id, item_id, selected) VALUES (2,2, True); -- shopping list 2, yoghurt
INSERT INTO list_items (list_id, item_id, selected) VALUES (2,4, True); -- shopping list 2, apples