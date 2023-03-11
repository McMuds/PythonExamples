import unittest
from src.venue import Venue
from src.room import Room
from src.guest import Guest
from src.drinks import Drink

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue1 = Venue("Karaoke Karnage",100.0)
        self.poproom = Room(1,[],[],"pop")
        self.guest1 = Guest("Katie Perry", 50, 35)
        self.guest2 = Guest("Edith Piaf",100, 100)
        self.baby_guest = Guest("Emma Bunton",1000, 14)
        self.raproom = Room(2,[self.guest2],[],"Rap")
        self.drink1 = Drink("Beer",4.0,3.50)
        self.drink2 = Drink("Chocolate Milk",0,2.99)

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
    def test_guest_check_in__fail_too_young(self):
        self.venue1.check_guest_in(self.poproom,self.baby_guest)
        self.assertEqual(0,len(self.poproom.guests))
        self.assertEqual(100,self.venue1.till)
        self.assertEqual(1000,self.baby_guest.wallet)

    def test_guest_check_in_exact_age(self):
        baby_guest = Guest("Emma Bunton",1000, 15)
        self.venue1.check_guest_in(self.poproom,baby_guest)
        self.assertEqual(1,len(self.poproom.guests))
        self.assertEqual(115,self.venue1.till)
        self.assertEqual(985,baby_guest.wallet)

    #Add Drinks/Bar to venue
    def test_add_drink_to_venue(self):
        self.venue1.add_drink(self.drink1)
        self.assertEqual(1,len(self.venue1.drinks))

    def test_sell_drink(self):
        self.venue1.add_drink(self.drink1)
        self.venue1.sell_drink(self.drink1,self.guest1)
        self.assertEqual(0,len(self.venue1.drinks))
        self.assertEqual(103.5,self.venue1.till)
        self.assertEqual(46.50,self.guest1.wallet)

    def test_sell_drink__fail_too_young(self):
        self.venue1.add_drink(self.drink1)
        self.venue1.sell_drink(self.drink1,self.baby_guest)
        self.assertEqual(1,len(self.venue1.drinks))
        self.assertEqual(100,self.venue1.till)
        self.assertEqual(1000,self.baby_guest.wallet)

    def test_sell_drink_without_alcohol_babyguest(self):
        self.venue1.add_drink(self.drink2)
        self.venue1.sell_drink(self.drink2,self.baby_guest)
        self.assertEqual(0,len(self.venue1.drinks))
        self.assertEqual(102.99,self.venue1.till)
        self.assertEqual(997.01,self.baby_guest.wallet)

    def test_sell_drink_without_alcohol_normalguest(self):
        self.venue1.add_drink(self.drink2)
        self.venue1.sell_drink(self.drink2,self.guest1)
        self.assertEqual(0,len(self.venue1.drinks))
        self.assertEqual(102.99,self.venue1.till)
        self.assertEqual(47.01,self.guest1.wallet)