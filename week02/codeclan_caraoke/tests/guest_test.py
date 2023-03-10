import unittest
from src.guest import *

class TestGuest(unittest.TestCase):
    
    def test_guest_has_name(self):
        guest = Guest("Claire")
        self.assertEqual("Claire",guest.name)