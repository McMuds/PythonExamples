import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Claire")
        self.room1 = Room(1,self.guest1)

    def test_room_has_id(self):
        self.assertEqual(1,self.room1.id)

    def test_room_has_guest(self):
        self.assertEqual(self.room1.guest,self.room1.guest)
