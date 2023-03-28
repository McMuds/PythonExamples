import pdb
from db.run_sql import run_sql
from models.selection import Selection
from repositories import item_repository as item_repo

def get_list_selection(list_id):
    sql_string = "SELECT l_i.* FROM list_items as l_i WHERE l_i.list_id = %s"
    values=[list_id]
    results = run_sql(sql_string, values)
    selection_list = []
    for row in results:
        item = item_repo.select(row['item_id'])
        selection = Selection(item, row['quantity'], row['selected'])
        selection_list.append(selection)
    return selection_list

def get_list_selection_ordered(list_id,order):
    sql_string = "SELECT l_i.* FROM list_items as l_i WHERE l_i.list_id = %s"
    values=[list_id]
    results = run_sql(sql_string, values)
    selection_list = []
    for row in results:
        item = item_repo.select(row['item_id'])
        selection = Selection(item, row['quantity'], row['selected'])
        selection_list.append(selection)
    if order==1:
        selection_list.sort(key=lambda x: x.item.category.id)
    elif order == 2:
        selection_list.sort(key= lambda x: x.item.name)
    else:
        selection_list.sort(key= lambda x: x.selected)
    return selection_list

def insert_item(p_list, p_item, quantity):
    # todo: check for dups first. Either here or where it's called
    # pdb.set_trace()
    # for selection in p_list.selection:
    #     if selection.item.id == p_item.id:
    #         duplicate = True          
    duplicate = [True for selection in p_list.selection if selection.item.id == p_item.id]
    if duplicate:
        pass
    else:
        sql_string = "INSERT INTO list_items (list_id, item_id, quantity, selected) \
                VALUES (%s, %s, %s, False)"
        values = [p_list.id, p_item.id, quantity]
        run_sql(sql_string,values)

def remove_item(list_id, item_id):
    # should be sorted by not allowing dups, but you never know, right?
    # you might need to check count(*) first.
    sql_string = "DELETE FROM list_items WHERE list_id = %s AND item_id = %s"
    values = [list_id, item_id]
    run_sql(sql_string, values)

def get_selection(list_id, item_id):
    sql_string = "SELECT l_i.* FROM list_items as l_i WHERE l_i.list_id = %s and l_i.item_id = %s"
    values=[list_id, item_id]
    # pdb.set_trace()
    results = run_sql(sql_string, values)
    item = item_repo.select(item_id)
    selection = Selection(item, results[0]['quantity'], results[0]['selected'])
    return selection

def toggle_item_selected(list_id, item_id):
    # should be sorted by not allowing dups, but you never know, right?
    # you might need to check count(*) first.
    # pdb.set_trace()
    selection = get_selection(list_id, item_id)
    sql_string = "UPDATE list_items SET selected = %s WHERE list_id = %s AND item_id = %s"
    values = [not(selection.selected), list_id, item_id]
    run_sql(sql_string, values)

def get_prev_item(list_id, item_id):
    sql_string = "SELECT * FROM list_items WHERE list_id = %s and item_id < %s ORDER BY id"
    values = [list_id, item_id]
    result = run_sql(sql_string, values)
    if result == None or len(result) == 0:
        return 0
    else:
        return result[0]['item_id']

def get_next_item(list_id, item_id):
    sql_string = "SELECT * FROM list_items WHERE list_id = %s and item_id > %s ORDER BY id"
    values = [list_id, item_id]
    result = run_sql(sql_string, values)
    if result == None or len(result) == 0:
        return 0
    else:
        return result[0]['item_id']
    
def update_qty(list_id, item_id, qty):
    print(f"Quantity is {qty} and is of type {type(qty)}")
    sql_string = "UPDATE list_items SET quantity = %s WHERE list_id = %s and item_id = %s"
    values = [qty, list_id, item_id]
    run_sql(sql_string, values)