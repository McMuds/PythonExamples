from db.run_sql import run_sql
from models.item import Item
from repositories import categories_repository as cat_repo

def select_item(id):
    sql_string = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql_string,values)
    category = cat_repo.select(result[0]['cat_id'])
    item = Item(result[0]['name'], category, result[0]['id'])
    return item

def select_all():
    sql_string = "SELECT * FROM items"
    result = run_sql(sql_string)
    items = []
    for row in result:
        category = cat_repo.select(row['cat_id'])
        item = Item(row['name'], category, row['id'])
        items.append(item)
    return items