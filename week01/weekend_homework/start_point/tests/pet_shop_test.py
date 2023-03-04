
import unittest
import pdb
from src.pet_shop import *

class TestPetShop(unittest.TestCase):

    def setUp(self):
        self.customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

        self.new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

        self.cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

    def test_pet_shop_name(self):
        name = get_pet_shop_name(self.cc_pet_shop)
        self.assertEqual("Camelot of Pets", name)

    # @unittest.skip("delete this line to run the test")
    def test_total_cash(self):
        sum = get_total_cash(self.cc_pet_shop)
        self.assertEqual(1000, sum)

    # @unittest.skip("delete this line to run the test")
    def test_add_or_remove_cash__add(self):
        add_or_remove_cash(self.cc_pet_shop,10)
        cash = get_total_cash(self.cc_pet_shop)
        self.assertEqual(1010, cash)

    # @unittest.skip("delete this line to run the test")
    def test_add_or_remove_cash__remove(self):
        add_or_remove_cash(self.cc_pet_shop,-10)
        cash = get_total_cash(self.cc_pet_shop)
        self.assertEqual(990, cash)

    # @unittest.skip("delete this line to run the test")
    def test_pets_sold(self):
        sold = get_pets_sold(self.cc_pet_shop)
        self.assertEqual(0, sold)

    # @unittest.skip("delete this line to run the test")
    def test_increase_pets_sold(self):
        increase_pets_sold(self.cc_pet_shop,2)
        sold = get_pets_sold(self.cc_pet_shop)
        self.assertEqual(2, sold)

    # @unittest.skip("delete this line to run the test")
    def test_stock_count(self):
        count = get_stock_count(self.cc_pet_shop)
        self.assertEqual(6, count)

    # @unittest.skip("delete this line to run the test")
    def test_all_pets_by_breed__found(self):
        pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
        self.assertEqual(2, len(pets))

    # @unittest.skip("delete this line to run the test")
    def test_all_pets_by_breed__not_found(self):
        pets = get_pets_by_breed(self.cc_pet_shop, "Dalmation")
        self.assertEqual(0, len(pets))

    # @unittest.skip("delete this line to run the test")
    def test_find_pet_by_name__returns_pet(self):
        pet = find_pet_by_name(self.cc_pet_shop, "Arthur")
        self.assertEqual("Arthur", pet["name"])

    # @unittest.skip("delete this line to run the test")
    def test_find_pet_by_name__returns_None(self):
        pet = find_pet_by_name(self.cc_pet_shop, "Fred")
        self.assertIsNone(pet)

    # @unittest.skip("delete this line to run the test")
    def test_remove_pet_by_name(self):
        remove_pet_by_name(self.cc_pet_shop, "Arthur")
        pet = find_pet_by_name(self.cc_pet_shop,"Arthur")
        self.assertIsNone(pet)

    # @unittest.skip("delete this line to run the test")
    def test_add_pet_to_stock(self):
        add_pet_to_stock(self.cc_pet_shop, self.new_pet)
        count = get_stock_count(self.cc_pet_shop)
        self.assertEqual(7, count)

    # @unittest.skip("delete this line to run the test")
    def test_customer_cash(self):
        cash = get_customer_cash(self.customers[0])
        self.assertEqual(1000, cash)

    # @unittest.skip("delete this line to run the test")
    def test_remove_customer_cash(self):
        customer = self.customers[0]
        remove_customer_cash(customer, 100)
        self.assertEqual(900, customer["cash"])

    # @unittest.skip("delete this line to run the test")
    def test_customer_pet_count(self):
        count = get_customer_pet_count(self.customers[0])
        self.assertEqual(0, count)

    # @unittest.skip("delete this line to run the test")
    def test_add_pet_to_customer(self):
        customer = self.customers[0]
        add_pet_to_customer(customer, self.new_pet)
        self.assertEqual(1, get_customer_pet_count(customer))

    # --- OPTIONAL ---

    # @unittest.skip("delete this line to run the test")
    def test_customer_can_afford_pet__sufficient_funds(self):
        customer = self.customers[0]
        can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
        self.assertEqual(True, can_buy_pet)

    # @unittest.skip("delete this line to run the test")
    def test_customer_can_afford_pet__insufficient_funds(self):
        customer = self.customers[1]
        can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
        self.assertEqual(False, can_buy_pet)

    # @unittest.skip("delete this line to run the test")
    def test_customer_can_afford_pet__exact_funds(self):
        customer = self.customers[2]
        can_buy_pet = customer_can_afford_pet(customer, self.new_pet)
        self.assertEqual(True, can_buy_pet)

    # These are 'integration' tests so we want multiple asserts.
    # If one fails the entire test should fail
    #
    # @unittest.skip("delete this line to run the test")
    def test_sell_pet_to_customer__pet_found(self):
        customer = self.customers[0]
        pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

        sell_pet_to_customer(self.cc_pet_shop, pet, customer)

        self.assertEqual(1, get_customer_pet_count(customer))
        self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
        self.assertEqual(100, get_customer_cash(customer))
        self.assertEqual(1900, get_total_cash(self.cc_pet_shop))

    # @unittest.skip("delete this line to run the test")
    def test_sell_pet_to_customer__pet_not_found(self):
        customer = self.customers[0]
        pet = find_pet_by_name(self.cc_pet_shop,"Dave")

        sell_pet_to_customer(self.cc_pet_shop, pet, customer)

        self.assertEqual(0, get_customer_pet_count(customer))
        self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
        self.assertEqual(1000, get_customer_cash(customer))
        self.assertEqual(1000, get_total_cash(self.cc_pet_shop))

    # @unittest.skip("delete this line to run the test")
    def test_sell_pet_to_customer__insufficient_funds(self):
        customer = self.customers[1]
        pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

        sell_pet_to_customer(self.cc_pet_shop, pet, customer)

        self.assertEqual(0, get_customer_pet_count(customer))
        self.assertEqual(0, get_pets_sold(self.cc_pet_shop))
        self.assertEqual(50, get_customer_cash(customer))
        self.assertEqual(1000, get_total_cash(self.cc_pet_shop))
