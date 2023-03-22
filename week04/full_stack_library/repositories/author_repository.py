from db.run_sql import run_sql
from models.author import Author

def select(id):
    sql_string = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    author_row = run_sql(sql_string, values)
    author = Author(author_row[0]['first_name'], author_row[0]['last_name'], id)
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'] )
        authors.append(author)
    return authors