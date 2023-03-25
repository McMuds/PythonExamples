from flask import render_template, redirect, request
# from repositories.categories_repository import category_repository as category_repo
from repositories import categories_repository as category_repo
from models.category import Category
 
from flask import Blueprint
category_blueprint = Blueprint("category",__name__)
 
@category_blueprint.route('/categories')
def index():
    categories = category_repo.select_all()
    return render_template('/categories/index.html', categories = categories)