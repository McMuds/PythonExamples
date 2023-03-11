class Guest:
    def __init__(self,name, amount, age, song):
        self.name = name
        self.wallet = amount
        self.age = age
        self.favourite_song = song

    def decrease_wallet(self,amount):
        self.wallet -= amount

    def sings_song(self,song):
        if song == self.favourite_song:
            return "Woohoo! That's my favourite song!"