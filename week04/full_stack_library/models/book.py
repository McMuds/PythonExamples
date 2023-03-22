class Book:
    def __init__(self,title, author, genre, checked_in = True, id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_in = checked_in
        self.id = id

    def toggle_check_in(self):
    # this should be in the class as it's playing with attributes
        if self.checked_in:
            self.checked_in = False
        else:
            self.checked_in = True