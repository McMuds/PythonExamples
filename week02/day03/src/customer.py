class Customer:
    def __init__(self, p_name, p_wallet, p_age, p_energy):
        self.name = p_name
        self.wallet = p_wallet
        self.age = p_age
        self.energy = p_energy

    def get_age(self):
        return self.age
    
    def get_energy(self):
        return self.energy

    def get_wallet(self):
        return self.wallet
    
    def reduce_wallet(self, p_amount):
        self.wallet -= p_amount

    def add_or_reduce_energy(self, p_energy):
        self.energy += p_energy

    def buy_drink(self,p_drink):
        price = p_drink.return_price()
        energy = p_drink.return_caffeine()
        self.reduce_wallet(price)
        self.add_or_reduce_energy(energy)

    def buy_food(self,p_food):
        price = p_food.return_price()
        energy = p_food.return_rejuv_level()
        self.reduce_wallet(price)
        self.add_or_reduce_energy(energy * -1)