import unittest
from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Holiday","Madonna","pop",1)

    def test_song_has_name(self):
        self.assertEqual("Holiday",self.song1.name)

    def test_song_has_artist(self):
        self.assertEqual("Madonna",self.song1.artist)
    
    def test_song_has_genre(self):
        self.assertEqual("pop",self.song1.genre)