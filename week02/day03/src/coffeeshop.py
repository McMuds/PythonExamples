import pdb

class CoffeeShop:
    def __init__(self,p_name, p_till):
        self.name = p_name
        self.till = p_till
        self.drinks = []
        self.foods = []
        self.drink_stock = {}

    def add_drink(self, p_drink, p_qty):
        if p_qty > 0:
            self.drinks.append(p_drink)
            self.drink_stock[p_drink.name] = p_qty

    def add_food(self,p_food):
        self.foods.append(p_food)

    def increase_till(self,p_amount):
        self.till += p_amount

    def find_drink(self,p_drink):
        for drink in self.drinks:
            if drink == p_drink:
                return drink
        return None
        # result = [drink for drink in self.drinks if drink == p_drink]
        # return result

    def find_food(self,p_food):
        for food in self.foods:
            if food == p_food:
                return food
        return None

    def sell_drink(self, p_drink, p_customer):
        age = p_customer.get_age()
        energy = p_customer.get_energy()
        drink_exists = (self.find_drink(p_drink) == p_drink)
        if age >= 16 and energy < 50 and drink_exists:
            self.drinks.remove(p_drink)
            self.increase_till(p_drink.price)
            return True
        else:
            return False

    def sell_food(self, p_food):
        food_exists = (self.find_food(p_food) == p_food)
        if food_exists:
            self.foods.remove(p_food)
            self.increase_till(p_food.price)
            return True
        else:
            return False
        
    def return_drink_names(self):
        # result = []
        # for drink in self.drinks:
        #     result.append(drink.name)
        result_lc = [drink.name for drink in self.drinks]
        return result_lc

    def return_affordable_drink_names(self, p_customer):
        wallet = p_customer.get_wallet()
        result_lc = [drink.name for drink in self.drinks if drink.price <= wallet]
        return result_lc
    
    def return_stock_value(self):
        total_sum = 0
        for drink in self.drinks:
            total_sum += (drink.return_price() * self.drink_stock[drink.name])
        return round(total_sum,2)    #Otherwise the value is 84.85000000000001