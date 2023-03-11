import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Wichita Lineman", "Glen Campbell", "Country", 1)
        self.song2 = Song("Jolene","Queen Dolly","Country",1)
        self.song3 = Song("Lose Yourself","Eminem","Rap",1)
        self.guest1 = Guest("Claire",10.0, 49,self.song1)
        self.guest2 = Guest("Mar",50, 30,self.song2)
        self.guest3 = Guest("Toby",50, 26,self.song1)
        self.guest4 = Guest("Alex",50, 30,self.song1)
        self.guest_list = [self.guest1, self.guest2, self.guest3]
        self.countryroom = Room(1,[self.guest1],[],"Country")
        self.poproom = Room(1,[self.guest1],[],"Pop")
        self.empty_room = Room(2,[],[],"Rap")
        self.busy_room = Room(3,self.guest_list,[self.song1],"Country")
   
    def test_room_has_id(self):
        self.assertEqual(1,self.countryroom.id)

    def test_room_has_guest(self):
        self.assertEqual([self.guest1],self.countryroom.guests)

    def test_can_create_empty_room(self):
        self.assertEqual([],self.empty_room.guests)

    def test_can_create_busy_room(self):
        self.assertEqual(3,len(self.busy_room.guests))

    def test_add_guest_to_room(self):
        self.countryroom.add_guest_to_room(self.guest4)
        self.assertEqual(2,len(self.countryroom.guests))

    def test_add_song_to_room(self):
        self.countryroom.add_song_to_room(self.song1)
        self.assertEqual(1,len(self.countryroom.songs))

    def test_remove_guest_from_single_guest_room(self):
        self.countryroom.remove_guest(self.guest1)
        self.assertEqual([],self.countryroom.guests)

    def test_remove_guest_from_busy_room(self):
        self.busy_room.remove_guest(self.guest2)
        expected = [self.guest1,self.guest3]
        self.assertEqual(expected,self.busy_room.guests)

    def test_remove_guest_from_busy_room__guest_not_in_room(self):
        self.busy_room.remove_guest(self.guest4)
        expected = [self.guest1,self.guest2, self.guest3]
        self.assertEqual(expected,self.busy_room.guests)
    
    def test_remove_guest_from_empty_room__fail(self):
        self.empty_room.remove_guest(self.guest4)
        self.assertEqual([],self.empty_room.guests)

    def test_remove_song_from_single_song_room(self):
        self.countryroom.add_song_to_room(self.song1)
        self.countryroom.remove_song(self.song1)
        self.assertEqual([],self.countryroom.songs)

    def test_remove_song_from_busy_song_room(self):
        self.countryroom.add_song_to_room(self.song1)
        self.countryroom.add_song_to_room(self.song2)
        self.busy_room.remove_song(self.song2)
        expected = [self.song1]
        self.assertEqual(expected,self.busy_room.songs)

    def test_remove_song_from_busy_song_room__song_not_in_room(self):
        self.countryroom.add_song_to_room(self.song1)
        self.countryroom.add_song_to_room(self.song2)
        song3 = Song("Come What May","Moulin Rouge","Musical",2)
        self.countryroom.remove_song(song3)
        expected = [self.song1, self.song2]
        self.assertEqual(expected,self.countryroom.songs)
    
    def test_remove_song_from_empty_song_room__fail(self):
        self.empty_room.remove_song(self.song1)
        self.assertEqual([],self.empty_room.songs)

    # Extensions
    def test_set_room_size(self):
        self.empty_room.set_room_size(1)
        self.assertEqual(1,self.empty_room._room_size)

    def test_add_guest_to_full_room__fail(self):
        self.empty_room.set_room_size(0)
        result = self.empty_room.add_guest_to_room(self.guest2)
        self.assertEqual(False,result)

    def test_set_room_cost(self):
        self.empty_room.set_room_cost(10)
        self.assertEqual(10,self.empty_room._room_cost)

    def test_add_guest_to_expensive_room__fail(self):
        self.empty_room.set_room_cost(100)
        result = self.empty_room.add_guest_to_room(self.guest2)
        self.assertEqual(False,result)

    # Advanced Extensions ideas:
    # Room has style - only add songs in that style
    def test_room_has_style(self):
        self.assertEqual("Pop",self.poproom.room_style)

    def test_add_song__fail_incorrect_style(self):
        self.poproom.add_song_to_room(self.song1)
        self.assertEqual(0,len(self.countryroom.songs))

    # Play a song
    def test_play_song(self):
        self.countryroom.add_song_to_room(self.song1)
        self.countryroom.add_song_to_room(self.song2)
        self.countryroom.play_song(self.song2)
        self.assertEqual([self.song1],self.countryroom.songs)
    # ensure there's the right number of guests for the song
    def test_play_song__fail_not_enough_singers(self):
        duet = Song("Islands In The Stream","Dolly P", "Country", 2)
        self.countryroom.add_song_to_room(duet)
        self.countryroom.play_song(duet)
        self.assertEqual(1,len(self.countryroom.songs))

    # add drinks class
    # add alcoholic_drinks & stock_levels
    # customer can buy a drink? - have made venue.sell_drink
    # young guests can buy non-alcoholic drinks?
    # guest has favourite song
    def test_play_song_favourite(self):
        # self.countryroom.add_song_to_room(self.song1)
        self.countryroom.add_song_to_room(self.song2)
        self.countryroom.add_guest_to_room(self.guest2)
        result = self.countryroom.play_song(self.song2)
        self.assertEqual("Woohoo! That's my favourite song!",result)

    def test_play_song_favourite__fail_no_favourite(self):
        self.countryroom.add_song_to_room(self.song1)
        self.countryroom.add_song_to_room(self.song2)
        self.countryroom.add_song_to_room(self.song3)
        self.countryroom.add_guest_to_room(self.guest2)
        result = self.countryroom.play_song(self.song3)
        self.assertEqual(None,result)
