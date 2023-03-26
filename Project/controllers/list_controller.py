from flask import render_template, redirect, request
from repositories import shopping_list_repository as list_repo
from repositories import selection_repository as selection_repo
from repositories import item_repository as item_repo
# from models.shopping_list import Shopping_List
import pdb
 
from flask import Blueprint
shopping_list_blueprint = Blueprint("shopping_list",__name__)
 
@shopping_list_blueprint.route('/lists')
def index():
    lists = list_repo.select_all()
    return render_template('/lists/index.html', lists=lists)

@shopping_list_blueprint.route('/lists/shop/<id>/<order>')
def shop_list(id,order):
    # pdb.set_trace()
    list = list_repo.select(id,1)
    return render_template('/lists/show.html', list=list, order=int(order), active=True)

# @shopping_list_blueprint.route('/lists/<id>')
# def show_list(id):
#     pdb.set_trace()
#     list = list_repo.select(id,1)
#     return render_template('/lists/show.html', list=list, order=1, active=False)

@shopping_list_blueprint.route('/lists/<id>/<display_order>')
def show_list_ordered(id,display_order):
    # pdb.set_trace()
    list = list_repo.select(int(id), int(display_order))
    return render_template('/lists/show.html', list=list, order=int(display_order))

@shopping_list_blueprint.route('/shopping_lists/add', methods=['post'])
def add_item_to_list():
    list_id = request.form['list_id']
    item_id = request.form['item_id']
    list = list_repo.select(list_id,1)
    item = item_repo.select(item_id)
    selection_repo.insert_item(list, item)
    return redirect('/')

@shopping_list_blueprint.route('/shopping_lists/new', methods=['post'])
def new_list():
    # pdb.set_trace()
    list_repo.create_new_list()
    return redirect('/lists')

@shopping_list_blueprint.route('/lists/<list_id>/delete/<item_id>', methods=['post'])
def delete_item_from_list(list_id, item_id):
    selection_repo.remove_item(int(list_id),int(item_id))
    return redirect('/lists/'+list_id)