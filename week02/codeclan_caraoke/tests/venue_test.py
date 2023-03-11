import unittest
from src.venue import Venue
from src.room import Room
from src.guest import Guest

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue1 = Venue("Karaoke Karnage",100.0)
        self.poproom = Room(1,[],[],"pop")
        self.guest1 = Guest("Katie Perry", 50, 35)
        self.guest2 = Guest("Edith Piaf",100, 100)
        self.raproom = Room(2,[self.guest2],[],"Rap")

    def test_venue_has_name(self):
        self.assertEqual("Karaoke Karnage",self.venue1.name)

    def test_venue_has_money(self):
        self.assertEqual(100.0,self.venue1.till)

    def test_venue_has_rooms(self):
        self.venue1.add_room(self.poproom)
        self.assertEqual(1,len(self.venue1.rooms))

    def test_add_money_to_till(self):
        self.venue1.add_money_to_till(10)
        self.assertEqual(110,self.venue1.till)

    def test_check_guest_in__pass(self):
        self.venue1.check_guest_in(self.poproom, self.guest1)
        self.assertEqual(35,self.guest1.wallet)
        self.assertEqual(1,len(self.poproom.guests))
        self.assertEqual(115,self.venue1.till)

    def test_check_guest_in__fail_room_full(self):
        self.poproom.set_room_size(0)
        self.venue1.check_guest_in(self.poproom, self.guest1)
        self.assertEqual(50,self.guest1.wallet)
        self.assertEqual(0,len(self.poproom.guests))
        self.assertEqual(100,self.venue1.till)
    
    def test_check_guest_in__fail_room_cost(self):
        self.poproom.set_room_cost(100)
        self.venue1.check_guest_in(self.poproom, self.guest1)
        self.assertEqual(50,self.guest1.wallet)
        self.assertEqual(0,len(self.poproom.guests))
        self.assertEqual(100,self.venue1.till)

    def test_transfer_guest(self):
        self.venue1.transfer_guest(self.guest2,self.raproom,self.poproom)
        self.assertEqual(0,len(self.raproom.guests))
        self.assertEqual(1,len(self.poproom.guests))
        self.assertEqual(85,self.guest2.wallet)
        self.assertEqual(115,self.venue1.till)

    def test_transfer_guest__fail_guest_not_in_room(self):
        self.venue1.transfer_guest(self.guest1,self.raproom,self.poproom)
        self.assertEqual(1,len(self.raproom.guests))
        self.assertEqual(0,len(self.poproom.guests))
        self.assertEqual(50,self.guest1.wallet)
        self.assertEqual(100,self.venue1.till)

    def test_transfer_guest__fail_new_room_busy(self):
        self.poproom.set_room_size(0)
        self.venue1.transfer_guest(self.guest2,self.raproom,self.poproom)
        self.assertEqual(1,len(self.raproom.guests))
        self.assertEqual(0,len(self.poproom.guests))
        self.assertEqual(100,self.guest2.wallet)
        self.assertEqual(100,self.venue1.till)

    #Advanced idea: Venue has lower age limit
