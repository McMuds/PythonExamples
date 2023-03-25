from db.run_sql import run_sql
from models.category import Category
 
def select_all(): 
    list_of_categories = []
    sql_string = "SELECT * FROM categories"
    results = run_sql(sql_string)
    for row in results:
        category = Category(row['name'], row['id'])
        list_of_categories.append(category)
    return list_of_categories

def select(id): 
    sql_string = "SELECT * FROM categories WHERE id = %s"
    values = [id]
    results = run_sql(sql_string, values)
    category = Category(results[0]['name'], results[0]['id'])
    return category
