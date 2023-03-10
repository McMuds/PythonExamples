import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def test_room_has_id(self):
        room1 = Room(1)
        self.assertEqual(1,room1.id)