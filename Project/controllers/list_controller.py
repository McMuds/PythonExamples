from flask import render_template, redirect, request
from repositories import shopping_list_repository as list_repo
# from models.shopping_list import Shopping_List
 
from flask import Blueprint
shopping_list_blueprint = Blueprint("shopping_list",__name__)
 
@shopping_list_blueprint.route('/lists')
def index():
    lists = list_repo.select_all()
    return render_template('/lists/index.html', lists=lists)

@shopping_list_blueprint.route('/lists/<id>')
def show_list(id):
    list = list_repo.select(id)
    return render_template('/lists/show.html', list=list)

@shopping_list_blueprint.route('/lists/<id>/<display_order>')
def show_list_ordered(id,display_order):
    list = list_repo.select(id,display_order)
    return render_template('/lists/show.html', list=list, order=display_order)