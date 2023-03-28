from flask import render_template, redirect, request
from repositories import shopping_list_repository as list_repo
from repositories import selection_repository as selection_repo
from repositories import item_repository as item_repo
# from models.shopping_list import Shopping_List
import pdb
 
from flask import Blueprint
shopping_list_blueprint = Blueprint("shopping_list",__name__)
 
def insert_item_to_list(list_id, item_id, quantity):
    # pdb.set_trace()
    s_list = list_repo.select(list_id,1)
    item = item_repo.select(item_id)
    selection_repo.insert_item(s_list, item, quantity)

@shopping_list_blueprint.route('/lists')
def index():
    lists = list_repo.select_all()
    return render_template('/lists/index.html', all_lists=lists)

@shopping_list_blueprint.route('/lists/shop/<id>/<order>')
def shop_list(id,order):
    # pdb.set_trace()
    list = list_repo.select(id,1)
    prev_id = list_repo.get_prev_list(int(id))
    next_id = list_repo.get_next_list(int(id))
    return render_template('/lists/show.html', list=list, order=int(order), prev_id=prev_id, next_id=next_id, active=True)

# @shopping_list_blueprint.route('/lists/<id>')
# def show_list(id):
#     pdb.set_trace()
#     list = list_repo.select(id,1)
#     return render_template('/lists/show.html', list=list, order=1, active=False)

@shopping_list_blueprint.route('/lists/<id>/<display_order>')
def show_list_ordered(id,display_order):
    # pdb.set_trace()
    list = list_repo.select(int(id), int(display_order))
    prev_id = list_repo.get_prev_list(int(id))
    next_id = list_repo.get_next_list(int(id))
    return render_template('/lists/show.html', list=list, order=int(display_order), prev_id=prev_id, next_id=next_id, active = False)

@shopping_list_blueprint.route('/lists/add', methods=['post'])
def add_item_to_list():
    pdb.set_trace()
    item_id = request.form['item_id']
    if item_id == None or item_id == '':
        pass
    else:
        list_id = request.form['list_id']
        quantity = request.form['quantity']
        insert_item_to_list(int(list_id), int(item_id), quantity)
    return redirect('/')

@shopping_list_blueprint.route('/lists/new')
def new_list():
    list_of_items = item_repo.select_all()
    return render_template('/lists/new.html', all_items=list_of_items)

@shopping_list_blueprint.route('/lists/new', methods=['post'])
def create_new_list():
    # pdb.set_trace()
    list_id = list_repo.create_new_list()
    item_id = request.form['item_id']
    qty = request.form['quantity']
    insert_item_to_list(int(list_id), int(item_id), qty)
    # list_of_items = item_repo.select_all()
    return redirect('/lists')

@shopping_list_blueprint.route('/lists/<list_id>/delete/<item_id>', methods=['post'])
def delete_item_from_list(list_id, item_id):
    selection_repo.remove_item(int(list_id),int(item_id))
    return redirect('/lists/'+list_id)

@shopping_list_blueprint.route('/lists/<list_id>/update/<item_id>')
def toggle_selected(list_id,item_id):
    selection_repo.toggle_item_selected(int(list_id), int(item_id))
    return redirect('/lists/shop/' + list_id + '/1')

@shopping_list_blueprint.route('/lists/delete', methods=['post'])
def delete():
    list_id = request.form['list_id']
    list_repo.delete(int(list_id))
    return redirect('/lists')

@shopping_list_blueprint.route('/lists/<list_id>/edit/<item_id>')
def edit_quantity(list_id, item_id):
    item = item_repo.select(int(item_id))
    p_item_id = selection_repo.get_prev_item(int(list_id), item.id)
    n_item_id = selection_repo.get_next_item(int(list_id), item.id)
    print(f"item_id is {item.id}")
    return render_template('/lists/edit.html', list_id=list_id, item=item, n_i_id = n_item_id, p_i_id = p_item_id)

@shopping_list_blueprint.route('/lists/<list_id>/edit/<item_id>', methods=['post'])
def update_quantity(list_id, item_id):
    pdb.set_trace()
    qty = request.form['quantity']
    if qty == None or qty == '':
        pass
    else:
        selection_repo.update_qty(int(list_id), int(item_id), qty)

    return redirect('/lists/' + list_id +'/1')