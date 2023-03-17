from flask import render_template, redirect, request
from app import app
from models.books import book_data, add_new_book, delete_book
from models.book import Book

@app.route('/')
def home():
    return render_template('index.html', title='CodeClan Library')

@app.route('/books')
def index():
    return render_template('books.html', title='CodeClan Library', book_list=book_data)
    
@app.route('/books/<id>')
def book(id):
    return render_template('book.html', title='CodeClan Library', book=book_data[int(id)])

@app.route('/books/new') 
def new_book():
    return render_template('newbook.html', title='CodeClan Library')

@app.route('/books/new', methods=['post']) 
def create_new_book():
    book_title = request.form['book_title']
    book_author = request.form['book_author']
    book_genre = request.form['book_genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('newbook.html', title='CodeClan Library')
    # return redirect('/books')
 
@app.route("/books/<index>/delete", methods=["POST"])
def books_delete(index):
    delete_book(book_data[int(index)])
    return redirect("/books")

# @app.route('/books/delete/<index>', methods=['post']) 
# def delete_book(index):
#     book_to_delete = request.form[int(index)]
#     delete_book(book_data[book_to_delete])
#     return redirect('/books')
    # return render_template('books.html', title='CodeClan Library')
