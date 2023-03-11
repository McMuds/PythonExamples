import unittest
from src.venue import Venue

class TestVenue(unittest.TestCase):
    
    def test_venue_has_name(self):
        venue1 = Venue("Karaoke Karnage")
        self.assertEqual("Karaoke Karnage",venue1.name)