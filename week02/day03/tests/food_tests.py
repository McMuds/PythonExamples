import unittest
from src.food import Food

class FoodTests(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("Muffin",2.75, 30)
        
    def test_food_has_name(self):
        self.assertEqual("Muffin",self.food.name)

    def test_food_has_price(self):
        price = self.food.return_price()
        self.assertEqual(2.75,price)

    def test_food_has_caffeine(self):
        result = self.food.return_rejuv_level()
        self.assertEqual(30, result)

    
    