class Book:
    def __init__(self,title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_in = True

    def toggle_check_in(self):
    # this should be in the class as it's playing with attributes
        if self.checked_in:
            self.checked_in = False
        else:
            self.checked_in = True