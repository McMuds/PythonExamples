import unittest
from src.drink import Drink

class DrinkTests(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Mocha",5.99, 50)
        
    def test_drink_has_name(self):
        self.assertEqual("Mocha",self.drink.name)

    def test_drink_has_price(self):
        price = self.drink.return_price()
        self.assertEqual(5.99,price)

    def test_drink_has_caffeine(self):
        caffeine = self.drink.return_caffeine()
        self.assertEqual(50, caffeine)
    