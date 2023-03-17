from flask import render_template, redirect, request
from app import app
from models.books import book_data, add_new_book
from models.book import Book

@app.route('/')
def home():
    return render_template('index.html', title='CodeClan Library')

@app.route('/books')
def index():
    return render_template('books.html', title='CodeClan Library', book_list=book_data)
    
@app.route('/books/new') 
def new_book_get():
    return render_template('newbook.html', title='CodeClan Library')

@app.route('/books/new', methods=['POST']) 
def new_book_post():
    book_title = request.form['book_title']
    book_author = request.form['book_author']
    book_genre = request.form['book_genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return render_template('newbook.html', title='CodeClan Library')
    # return redirect('/books')
