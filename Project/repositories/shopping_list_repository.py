from db.run_sql import run_sql
from models.shopping_list import Shopping_List
from repositories import selection_repository as selection_repo
 
def select_all(): 
    list_of_lists = []
    sql_string = "SELECT * FROM shopping_list"
    results = run_sql(sql_string)
    for row in results:
        selection = selection_repo.get_list_selection(row['id'])
        shopping_list = Shopping_List(row['date_created'], row['date_shopped'], selection, row['id'])
        list_of_lists.append(shopping_list)
    return list_of_lists
