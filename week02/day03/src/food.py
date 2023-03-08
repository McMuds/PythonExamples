class Food:
    def __init__(self,p_name, p_price, p_rejuv):
        self.name = p_name
        self.price = p_price
        self.rejuv_level = p_rejuv

    def return_price(self):
        return self.price
    
    def return_rejuv_level(self):
        return self.rejuv_level
    