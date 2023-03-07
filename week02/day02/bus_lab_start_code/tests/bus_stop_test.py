import unittest
from src.bus_stop import BusStop
from src.person import Person

class TestBusStop(unittest.TestCase):
    def setUp(self):
        self.bus_stop = BusStop("Waverly Station")
        self.person = Person("Guido van Rossum", 64)

    # @unittest.skip("Delete this line to run the test")
    def test_bus_stop_has_name(self):
        self.assertEqual("Waverly Station", self.bus_stop.name)

    # @unittest.skip("Delete this line to run the test")
    def test_queue_starts_empty(self):
        self.assertEqual(0, self.bus_stop.queue_length())

    # @unittest.skip("Delete this line to run the test")
    def test_can_add_person_to_queue(self):
        self.bus_stop.add_to_queue(self.person)
        self.assertEqual(1, self.bus_stop.queue_length())

    # @unittest.skip("Delete this line to run the test")
    def test_can_clear_queue(self):
        self.bus_stop.add_to_queue(self.person)
        self.bus_stop.clear_queue()
        self.assertEqual(0, self.bus_stop.queue_length())
