from flask import render_template, redirect, request
# from models.books import book_data, add_new_book, delete_book
from repositories import book_repository as book_repo
from repositories import author_repository as author_repo
from models.book import Book

from flask import Blueprint
books_blueprint = Blueprint("books",__name__)

@books_blueprint.route('/books')
def index():
    book_list = book_repo.select_all()
    return render_template('/books/books.html', title='CodeClan Library', book_list=book_list)
    
@books_blueprint.route('/books/<id>')
def book(id):
    book = book_repo.select(int(id))
    return render_template('/books/book.html', title='CodeClan Library', book = book, id=id)

@books_blueprint.route('/books/<id>', methods=['post'])
def update_book(id):
    book_title = request.form['book_title']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book_genre = request.form['book_genre']
    book = book_repo.select(id) #just want to retain the same value here
    checked_in_value = book.checked_in
    updated_book = Book(book_title, author, book_genre, checked_in_value, id)
    book_repo.update_book(updated_book)
    return redirect('/books/'+id)

@books_blueprint.route('/books/<id>/edit', methods=['post'])
def edit_book(id):
    book = book_repo.select(id)
    author_list = author_repo.select_all()
    return render_template("books/edit.html", book=book, all_authors = author_list)

@books_blueprint.route('/books/<id>/check', methods=['post'])
def book_check_in(id):
    print(f"hello - we're here at last!!")
    book = book_repo.select(id)
    book.toggle_check_in()
    book_repo.update_book(book)
    return redirect('/books/'+id)

@books_blueprint.route('/books/new') 
def new_book():
    author_list = author_repo.select_all()
    return render_template('/books/newbook.html', title='CodeClan Library', all_authors = author_list)

@books_blueprint.route('/books/new', methods=['post']) 
def create_new_book():
    book_title = request.form['book_title']
    author_id = request.form['author_id']
    author = author_repo.select(author_id)
    book_genre = request.form['book_genre']
    new_book = Book(book_title, author, book_genre)
    book_repo.add_book(new_book)
    return redirect('/books')
 
@books_blueprint.route("/books/<index>/delete", methods=["POST"])
def books_delete(index):
    book_repo.delete_book(int(index))
    return redirect("/books")

