import unittest
from src.guest import *

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Claire",100.0, 49)

    def test_guest_has_name(self):
        self.assertEqual("Claire",self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(100.0,self.guest.wallet)

    def test_decrease_wallet(self):
        self.guest.decrease_wallet(10)
        self.assertEqual(90,self.guest.wallet)

    def test_guest_has_age(self):
        self.assertEqual(49,self.guest.age)