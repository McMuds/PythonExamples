class Guest:
    def __init__(self,name, amount):
        self.name = name
        self.wallet = amount

    def decrease_wallet(self,amount):
        self.wallet -= amount