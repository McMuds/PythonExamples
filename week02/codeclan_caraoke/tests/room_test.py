import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Claire",10.0)
        self.guest2 = Guest("Mar",50)
        self.guest3 = Guest("Toby",50)
        self.guest4 = Guest("Alex",50)
        self.guest_list = [self.guest1, self.guest2, self.guest3]
        self.song1 = Song("Wichita Lineman", "Glen Campbell", "Country", 1)
        self.song2 = Song("Jolene","Queen Dolly","Country",1)
        self.room1 = Room(1,[self.guest1],[])
        self.empty_room = Room(2,[],[])
        self.busy_room = Room(3,self.guest_list,[self.song1])
   
    def test_room_has_id(self):
        self.assertEqual(1,self.room1.id)

    def test_room_has_guest(self):
        self.assertEqual([self.guest1],self.room1.guests)

    def test_can_create_empty_room(self):
        self.assertEqual([],self.empty_room.guests)

    def test_can_create_busy_room(self):
        self.assertEqual(3,len(self.busy_room.guests))

    def test_can_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest4)
        self.assertEqual(2,len(self.room1.guests))

    def test_can_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1,len(self.room1.songs))

    def test_can_remove_guest_from_single_guest_room(self):
        self.room1.remove_guest(self.guest1)
        self.assertEqual([],self.room1.guests)

    def test_can_remove_guest_from_busy_room(self):
        self.busy_room.remove_guest(self.guest2)
        expected = [self.guest1,self.guest3]
        self.assertEqual(expected,self.busy_room.guests)

    def test_can_remove_guest_from_busy_room__guest_not_in_room(self):
        self.busy_room.remove_guest(self.guest4)
        expected = [self.guest1,self.guest2, self.guest3]
        self.assertEqual(expected,self.busy_room.guests)
    
    def test_can_remove_guest_from_empty_room__fail(self):
        self.empty_room.remove_guest(self.guest4)
        self.assertEqual([],self.empty_room.guests)

    def test_can_remove_song_from_single_song_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.remove_song(self.song1)
        self.assertEqual([],self.room1.songs)

    def test_can_remove_song_from_busy_song_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.busy_room.remove_song(self.song2)
        expected = [self.song1]
        self.assertEqual(expected,self.busy_room.songs)

    def test_can_remove_song_from_busy_song_room__song_not_in_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        song3 = Song("Come What May","Moulin Rouge","Musical",2)
        self.room1.remove_song(song3)
        expected = [self.song1, self.song2]
        self.assertEqual(expected,self.room1.songs)
    
    def test_can_remove_song_from_empty_song_room__fail(self):
        self.empty_room.remove_song(self.song1)
        self.assertEqual([],self.empty_room.songs)

    def test_can_set_room_size(self):
        self.empty_room.set_room_size(1)
        self.assertEqual(1,self.empty_room._room_size)

    def test_add_guest_to_full_room__fail(self):
        self.empty_room.set_room_size(0)
        result = self.empty_room.add_guest_to_room(self.guest2)
        self.assertEqual(False,result)

    def test_can_set_room_cost(self):
        self.empty_room.set_room_cost(10)
        self.assertEqual(10,self.empty_room._room_cost)