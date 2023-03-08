class Drink:
    def __init__(self,p_name, p_price, p_caffeine):
        self.name = p_name
        self.price = p_price
        self.caffeine = p_caffeine

    def return_price(self):
        return self.price
    
    def return_caffeine(self):
        return self.caffeine
    