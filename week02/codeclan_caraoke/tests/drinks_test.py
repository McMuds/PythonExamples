import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer",4.0,2.60)

    def test_drink_has_name(self):
        self.assertEqual("Beer",self.drink1.name)

    def test_drink_has_abv(self):
        self.assertEqual(4.0,self.drink1.abv)

    def test_drink_has_price(self):
        self.assertEqual(2.6,self.drink1.price)