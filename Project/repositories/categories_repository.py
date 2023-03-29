from db.run_sql import run_sql
from models.category import Category

def select_all(): 
    list_of_categories = []
    sql_string = "SELECT * FROM categories order by upper(name)"
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

def update(category): 
    sql_string = "UPDATE categories SET name = %s WHERE id = %s"
    values = [category.name, category.id]
    run_sql(sql_string, values)

def delete(id):
    sql_string = "DELETE FROM categories WHERE id = %s"
    values = [int(id)]
    run_sql(sql_string,values) 

def insert_new(category):
    sql_string = "INSERT INTO categories (name) VALUES (%s) RETURNING *"
    values = [category.name]
    results = run_sql(sql_string,values) 
    category.id = results[0]['id']