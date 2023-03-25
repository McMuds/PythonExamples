from db.run_sql import run_sql
from models.selection import Selection
from repositories import item_repository as item_repo

def get_list_selection(list_id):
    sql_string = "SELECT l_i.* FROM list_items as l_i WHERE l_i.list_id = %s"
    values=[list_id]
    results = run_sql(sql_string, values)
    selection_list = []
    for row in results:
        item = item_repo.select_item(row['item_id'])
        selection = Selection(item, row['selected'])
        selection_list.append(selection)

    return selection_list
