from flask import Flask, render_template
from controllers.book_controller import books_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='CodeClan Library')

if __name__ == "__main__":
	app.run(debug=True)
