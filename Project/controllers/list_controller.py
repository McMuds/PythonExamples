from flask import render_template, redirect, request
from repositories import shopping_list_repository as list_repo
# from models.shopping_list import Shopping_List
 
from flask import Blueprint
shopping_list_blueprint = Blueprint("shopping_list",__name__)
 
@shopping_list_blueprint.route('/shopping_lists')
def index():
    lists = list_repo.select_all()
    return render_template('/lists/index.html', lists=lists)