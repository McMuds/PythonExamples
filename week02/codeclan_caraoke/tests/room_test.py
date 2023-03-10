import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Claire")
        self.guest2 = Guest("Mar")
        self.guest3 = Guest("Toby")
        self.guest4 = Guest("Alex")
        self.guest_list = [self.guest1, self.guest2, self.guest3]
        self.song1 = Song("Wichita Lineman", "Glen Campbell", "Country", 1)
        self.room1 = Room(1,[self.guest1],[])
        self.empty_room = Room(2,[],[])
   
    def test_room_has_id(self):
        self.assertEqual(1,self.room1.id)

    def test_room_has_guest(self):
        self.assertEqual([self.guest1],self.room1.guests)

    def test_can_create_empty_room(self):
        self.assertEqual([],self.empty_room.guests)

    def test_can_create_busy_room(self):
        busy_room = Room(3,self.guest_list,[self.song1])
        self.assertEqual(3,len(busy_room.guests))

    def test_can_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual(2,len(self.room1.guests))

    def test_can_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1,len(self.room1.songs))