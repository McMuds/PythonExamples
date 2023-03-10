import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Claire")
        self.guest2 = Guest("Mar")
        self.guest3 = Guest("Toby")
        self.guest4 = Guest("Alex")
        self.guest_list = [self.guest1, self.guest2, self.guest3]
        self.room1 = Room(1,self.guest1)

    def test_room_has_id(self):
        self.assertEqual(1,self.room1.id)

    def test_room_has_guest(self):
        self.assertEqual(self.room1.guest,self.room1.guest)

    def test_can_create_empty_room(self):
        empty_room = Room(2,[])
        self.assertEqual([],empty_room.guest)

    def test_can_create_busy_room(self):
        busy_room = Room(3,self.guest_list)
        self.assertEqual(3,len(busy_room.guest))
