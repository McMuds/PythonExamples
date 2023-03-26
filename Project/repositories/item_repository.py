from db.run_sql import run_sql
from models.item import Item
from repositories import categories_repository as cat_repo
import pdb

def select(id):
    sql_string = "SELECT * FROM items WHERE id = %s"
    values = [int(id)]
    result = run_sql(sql_string,values)
    category = cat_repo.select(result[0]['cat_id'])
    item = Item(result[0]['name'], category, result[0]['id'])
    return item

def select_all():
    sql_string = "SELECT * FROM items ORDER BY cat_id"
    result = run_sql(sql_string)
    items = []
    for row in result:
        category = cat_repo.select(row['cat_id'])
        item = Item(row['name'], category, row['id'])
        items.append(item)
    return items

def add_new(item):
    sql_string = "INSERT INTO items (name, cat_id) VALUES (%s, %s) RETURNING *"
    values = [item.name, item.category.id]
    result = run_sql(sql_string, values)
    item.id = result[0]['id']
    return item

def save_item(item):
    sql_string = "UPDATE items SET (name, cat_id) = (%s, %s) WHERE id = %s"
    values = [item.name, item.category.id, item.id]
    run_sql(sql_string,values)

def delete_item(id):
    sql_string = "DELETE FROM items WHERE id = %s"
    values = [int(id)]
    run_sql(sql_string,values)

def select_cat_items(cat_id):
    sql_string = "SELECT * FROM items WHERE cat_id = %s"
    values = [cat_id]
    result = run_sql(sql_string,values)
    items = []
    for row in result:
        category = cat_repo.select(row['cat_id'])
        item = Item(row['name'], category, row['id'])
        items.append(item)
    return items