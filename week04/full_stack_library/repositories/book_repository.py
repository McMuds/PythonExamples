from db.run_sql import run_sql
import pdb
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['checked_in'], row['id'] )
        books.append(book)
    return books


def select(id):    
    sql_string = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql_string, values)
    author_id = results[0]['author_id']
    author = author_repo.select(author_id)
    book = Book(results[0]['title'], author, results[0]['genre'],results[0]['checked_in'],id)

    return book
 
def delete_book(id):
    sql_string = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql_string,values)

def add_book(book):
    sql_string = "INSERT INTO books (title, genre, checked_in, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.checked_in, book.author.id]
    new_id = run_sql(sql_string, values)
    book.id = new_id

def update_book(book):
    sql_string = "UPDATE books SET (title, genre, checked_in, author_id) = \
            (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.checked_in, book.author.id, book.id]
    run_sql(sql_string, values)