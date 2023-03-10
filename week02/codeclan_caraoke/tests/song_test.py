import unittest
from src.song import *

class TestSong(unittest.TestCase):

    def test_song_has_name(self):
        self.assertEqual("Holiday",Song("Holiday").name)