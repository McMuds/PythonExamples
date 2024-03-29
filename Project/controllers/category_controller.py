from flask import render_template, redirect, request
from repositories import categories_repository as category_repo
from models.category import Category
 
from flask import Blueprint
category_blueprint = Blueprint("category",__name__)
 
@category_blueprint.route('/categories')
def index():
    categories = category_repo.select_all()
    return render_template('/categories/index.html', categories = categories)

@category_blueprint.route('/categories/<id>')
def show_cat(id):
    category = category_repo.select(id)
    return render_template('/categories/show.html', category=category)

@category_blueprint.route('/categories/<id>', methods=['post'])
def save_cat(id):
    name = request.form['category_name']
    category = Category(name, id)
    category_repo.update(category)
    return redirect('/categories')

@category_blueprint.route('/categories/<id>/delete', methods=['post'])
def delete(id):
    category_repo.delete(int(id))
    return redirect('/categories')

@category_blueprint.route('/categories/new')
def add_new():
    categories = category_repo.select_all()
    return render_template('/categories/new.html', all_categories = categories)

@category_blueprint.route('/categories/new', methods=['post'])
def save_new():
    name = request.form['category_name']
    category = Category(name)
    category_repo.insert_new(category)
    categories = category_repo.select_all()
    return redirect('/categories')