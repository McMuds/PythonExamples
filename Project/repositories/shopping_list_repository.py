from db.run_sql import run_sql
from models.shopping_list import Shopping_List
from repositories import selection_repository as selection_repo
import pdb

def select_all(): 
    list_of_lists = []
    sql_string = "SELECT * FROM shopping_list ORDER BY id DESC"
    results = run_sql(sql_string)
    for row in results:
        selection = selection_repo.get_list_selection(row['id'])
        shopping_list = Shopping_List(row['date_created'], row['date_shopped'], selection, row['id'])
        list_of_lists.append(shopping_list)
    return list_of_lists

def get_open_lists(): 
    list_of_lists = []
    sql_string = "SELECT * FROM shopping_list WHERE date_shopped is Null ORDER BY date_created DESC"
    results = run_sql(sql_string)
    for row in results:
        selection = selection_repo.get_list_selection(row['id'])
        shopping_list = Shopping_List(row['date_created'], row['date_shopped'], selection, row['id'])
        list_of_lists.append(shopping_list)
    return list_of_lists

def select(id,order): 
    sql_string = "SELECT * FROM shopping_list WHERE id = %s"
    values = [id]
    result = run_sql(sql_string, values)
    selection = selection_repo.get_list_selection_ordered(result[0]['id'], order)
    shopping_list = Shopping_List(result[0]['date_created'], result[0]['date_shopped'], selection, id)
    return shopping_list

def create_new_list():
    sql_string = "INSERT INTO shopping_list (date_created) VALUES (now()) returning *"
    results = run_sql(sql_string)
    list_id = results[0]['id']
    return list_id

def get_prev_list(id):
    sql_string = "SELECT id FROM shopping_list WHERE id < %s ORDER BY id DESC"
    values = [id]
    result=[]
    result = run_sql(sql_string, values)
    # pdb.set_trace()
    if result == None or len(result) == 0:
        return 0
    else:
        return result[0]['id']

def get_next_list(id):
    sql_string = "SELECT id FROM shopping_list WHERE id > %s ORDER BY id"
    values = [id]
    result=[]
    result = run_sql(sql_string, values)
    # pdb.set_trace() #this caused all sorts of issues
    if result == None or len(result) == 0:
        return 0
    else:
        return result[0]['id']
    
def delete(id):
    sql_string = "DELETE FROM shopping_list where id = %s"
    values = [id]
    run_sql(sql_string, values)