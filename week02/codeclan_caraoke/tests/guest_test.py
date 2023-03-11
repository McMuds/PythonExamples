import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Locomotion","Kylie","Pop",1)
        self.guest = Guest("Claire",100.0, 49,self.song)
        self.room = Room(1,self.guest,[self.song],"Pop")

    def test_guest_has_name(self):
        self.assertEqual("Claire",self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(100.0,self.guest.wallet)

    def test_decrease_wallet(self):
        self.guest.decrease_wallet(10)
        self.assertEqual(90,self.guest.wallet)

    def test_guest_has_age(self):
        self.assertEqual(49,self.guest.age)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual(self.song,self.guest.favourite_song)

    def test_sings_song__favourite(self):
        result = self.guest.sings_song(self.song)
        self.assertEqual("Woohoo! That's my favourite song!",result)
