from flask import render_template, redirect, request
from repositories import categories_repository as category_repo
from repositories import item_repository as item_repo
from models.item import Item
 
from flask import Blueprint
item_blueprint = Blueprint("item",__name__)
 
@item_blueprint.route('/items')
def index():
    items = item_repo.select_all()
    return render_template('/items/index.html', items = items)

@item_blueprint.route("/items/view/<display_order>")
def ordered_index(display_order):
    items = item_repo.select_all()
    if display_order == '2':
        items.sort(key= lambda x: x.name.lower())
        return render_template('/items/index.html', items=items)
    else:
        return redirect('/items')

@item_blueprint.route('/items/new')
def new_item():
    categories = category_repo.select_all()
    return render_template('/items/new.html', all_categories = categories)

@item_blueprint.route('/items/new', methods=['post'])
def save_new_item():
    item_name = request.form['item_name']
    category_id = request.form['category_id']
    category = category_repo.select(category_id)
    item = Item(item_name, category)
    item_id = item_repo.add_new(item)
    item.id = item_id
    return redirect ('/items')

@item_blueprint.route('/items/<id>')
def show_item(id):
    item = item_repo.select(id)
    categories = category_repo.select_all()
    return render_template('/items/show.html', item=item, all_categories=categories)

@item_blueprint.route('/items/<cat_id>/cat')
def show_category_items(cat_id):
    item_list = item_repo.select_cat_items(int(cat_id))
    return render_template('/items/index.html', items = item_list)

@item_blueprint.route('/items/<id>', methods=['post'])
def save_item(id):
    item_name = request.form['item_name']
    category_id = request.form['category_id']
    category = category_repo.select(category_id)
    item = Item(item_name, category, id)
    item_repo.save_item(item)
    return redirect ('/items')

@item_blueprint.route('/items/<id>/delete', methods=['post'])
def delete_item(id):
    item_repo.delete_item(id)
    return redirect('/items')