from flask import Flask, render_template
from controllers.category_controller import category_blueprint
from controllers.list_controller import shopping_list_blueprint
from controllers.item_controller import item_blueprint
from repositories import shopping_list_repository as list_repo, item_repository as item_repo
 
app = Flask(__name__)

app.register_blueprint(category_blueprint)
app.register_blueprint(shopping_list_blueprint)
app.register_blueprint(item_blueprint)
 
@app.route('/')
def home():
    item_list = item_repo.select_all()
    open_lists = list_repo.get_open_lists()
    return render_template('index.html', all_items = item_list, open_lists = open_lists) 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.html') 

if __name__ == "__main__":
    app.run(debug=True)
