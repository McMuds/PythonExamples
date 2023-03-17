import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Princess Bride", "William Goldman", "Fiction")

    def test_book_has_title(self):
        self.assertEqual("Princess Bride", self.book1.title)
    
    def test_book_has_author(self):
        self.assertEqual("William Goldman", self.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Fiction", self.book1.genre)

    def test_book_is_checked_in(self):
        self.assertEqual(True, self.book1.checked_in)
        