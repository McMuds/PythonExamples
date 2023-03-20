from models.book import Book

book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book2 = Book("Zen and the Art of Motorcycle Maintenance",
             "Robert M. Pirsig", "self-help")
book3 = Book("The Girl Who Saved the King of Sweden", "Jonas Jonasson", "Fiction")
book4 = Book("The Life of Pi","Yann Martel","Fiction")
book5 = Book("The Princess Bride", "William Goldman", "Fiction")
book6 = Book("The Food Lab", "Kenji Lopez-Alt", "Cookery")

book_data = [book1, book2, book3, book5, book4, book6]

def add_new_book(book):
    book_data.append(book)

def delete_book(book):
    book_data.remove(book)

