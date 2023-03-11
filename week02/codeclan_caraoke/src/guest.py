class Guest:
    def __init__(self,name, amount, age):
        self.name = name
        self.wallet = amount
        self.age = age

    def decrease_wallet(self,amount):
        self.wallet -= amount