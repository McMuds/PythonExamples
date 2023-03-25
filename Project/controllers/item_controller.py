from flask import render_template, redirect, request
# from repositories.categories_repository import category_repository as category_repo
from repositories import item_repository as item_repo
from models.item import Item
 
from flask import Blueprint
item_blueprint = Blueprint("item",__name__)
 
@item_blueprint.route('/items')
def index():
    items = item_repo.select_all()
    return render_template('/items/index.html', items = items)