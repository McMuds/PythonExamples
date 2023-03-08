import unittest
import pdb
from src.customer import Customer
from src.drink import Drink
from src.food import Food
from src.coffeeshop import CoffeeShop

class CustomerTests(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Claire", 100.0, 49, 50)
        self.drink = Drink("Mocha", 5.99, 50)
        self.food = Food("Muffin", 2.50, 30)
        self.coffeeshop = CoffeeShop("Tarbucks", 200.0)
        self.coffeeshop.add_drink(self.drink, 3)

    def test_customer_has_name(self):
        self.assertEqual("Claire",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100.0,self.customer.get_wallet())

    def test_customer_has_age(self):
        self.assertEqual(49,self.customer.get_age())

    def test_customer_has_energy(self):
        self.assertEqual(50,self.customer.get_energy())

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.coffeeshop.sell_drink(self.drink, self.customer)
        self.assertEqual(94.01,self.customer.wallet)
        self.assertEqual(100, self.customer.get_energy())
        # self.assertEqual(205.99,self.coffeeshop.till)
        # could start adding things to check that the drink has been removed
        # from the coffee shop, but I think that's where the rabbit hole starts.

    def test_add_or_reduce_energy__add(self):
        self.customer.add_or_reduce_energy(10)
        self.assertEqual(60,self.customer.get_energy())

    def test_add_or_reduce_energy__remove(self):
        self.customer.add_or_reduce_energy(-10)
        self.assertEqual(40,self.customer.get_energy())

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(15)
        self.assertEqual(85, self.customer.get_wallet())

    def test_customer_can_buy_food(self):
        self.customer.buy_food(self.food)
        self.assertEqual(97.50,self.customer.wallet)
        self.assertEqual(20, self.customer.get_energy())

