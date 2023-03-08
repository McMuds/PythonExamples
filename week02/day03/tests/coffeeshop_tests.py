import pdb
import unittest
from src.coffeeshop import CoffeeShop
from src.drink import Drink
from src.food import Food
from src.customer import Customer

class CoffeeShopTests(unittest.TestCase):
    
    def setUp(self):
        self.coffeeshop = CoffeeShop("Tarbucks", 200.00)
        self.drink1 = Drink("Mocha", 5.99, 50)
        self.drink2 = Drink("Latte", 4.99, 40)
        self.drink_x = Drink("Espresso",2.99,80) #a drink we're not adding to the coffeeshop
        self.food1 = Food("Muffin", 4.99, 30)
        self.food2 = Food("Toastie", 8.99, 60)
        self.food_x = Drink("Crisps",0.99,10) #a food we're not adding to the coffeeshop
        self.coffeeshop.add_drink(self.drink1, 10)
        self.coffeeshop.add_drink(self.drink2, 5)
        self.coffeeshop.add_food(self.food1)
        self.coffeeshop.add_food(self.food2)
        self.customer_old = Customer("Claire", 100, 49, 40)
        self.customer_young = Customer("Laura", 5, 14, 20)

    def test_coffeeshop_has_name(self):
        self.assertEqual("Tarbucks",self.coffeeshop.name)

    def test_coffeeshop_has_money(self):
        self.assertEqual(200.00,self.coffeeshop.till)

    def test_coffeeshop_has_drinks(self): #i.e. add_drink worked
        self.assertEqual(2,len(self.coffeeshop.drinks))

    def test_coffeeshop_has_stock(self): #i.e. add_drink worked
        self.assertEqual(10,self.coffeeshop.drink_stock["Mocha"])

    def test_coffeeshop_has_foods(self): #i.e. add_food worked
        self.assertEqual(2,len(self.coffeeshop.foods))

    def test_can_increase_till(self):
        self.coffeeshop.increase_till(10)
        self.assertEqual(210,self.coffeeshop.till)

    def test_can_find_drink_by_name__pass(self):
        actual = self.coffeeshop.find_drink(self.drink1)
        self.assertEqual(self.drink1,actual)
    
    def test_can_find_drink_by_name__fail(self):
        self.assertEqual(None,self.coffeeshop.find_drink(self.drink_x))

    def test_coffeeshop_sell_drink__pass_age(self):
        # pdb.set_trace()
        successful_sale = self.coffeeshop.sell_drink(self.drink1, self.customer_old)
        self.assertEqual(True,successful_sale)    
        self.assertEqual(205.99,self.coffeeshop.till)
        self.assertEqual(1,len(self.coffeeshop.drinks))
    
    def test_coffeeshop_sell_drink__fail_age(self):
        unsuccessful_sale = self.coffeeshop.sell_drink(self.drink1, self.customer_young)
        self.assertEqual(False, unsuccessful_sale)    
        self.assertEqual(200,self.coffeeshop.till)
        self.assertEqual(2,len(self.coffeeshop.drinks))

    def test_coffeeshop_sell_drink__fail_energy(self):
        customer = Customer("TooMuchEnergy",25, 30, 60)
        unsuccessful_sale = self.coffeeshop.sell_drink(self.drink1, customer)
        self.assertEqual(False, unsuccessful_sale)
        # I'm no longer going to test all 3 as I did for the above age failure, as I figure
        # at this point if the full assert test above works once, it should work each time?
        # I'm not sure that's 100% accurate, but ... it's otherwise RABBIT CENTRAL!

    def test_coffeeshop_sell_drink__not_exists(self):
        unsuccessful_sale = self.coffeeshop.sell_drink(self.drink_x, self.customer_old)
        self.assertEqual(False, unsuccessful_sale)

    def test_can_find_food_by_name__pass(self):
        actual = self.coffeeshop.find_food(self.food1)
        self.assertEqual(self.food1,actual)
    
    def test_can_find_food_by_name__fail(self):
        self.assertEqual(None,self.coffeeshop.find_food(self.food_x))

    def test_coffeeshop_sell_food__pass_age(self):
        successful_sale = self.coffeeshop.sell_food(self.food1)
        self.assertEqual(True,successful_sale)    
        self.assertEqual(204.99,self.coffeeshop.till)
        self.assertEqual(1,len(self.coffeeshop.foods))

    def test_return_drink_names(self):
        actual = self.coffeeshop.return_drink_names()
        expected = ["Mocha","Latte"]
        self.assertEqual(expected,actual)

    def test_return_affordable_drink_names(self):
        actual = self.coffeeshop.return_affordable_drink_names(self.customer_young)
        expected = ["Latte"]
        self.assertEqual(expected,actual)

    def test_return_stock_value(self):
        actual = self.coffeeshop.return_stock_value()
        self.assertEqual(84.85, actual)