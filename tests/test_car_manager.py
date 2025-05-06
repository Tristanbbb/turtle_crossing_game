import unittest
from src.car_manager import CarManager
from src.screen_setup import screen_setup

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.car_manager = CarManager()

    def test_generate_car(self):
        self.car_manager.generate_car()
        self.assertEqual(1, len(self.car_manager.car_list))
        self.car_manager.generate_car()
        self.assertEqual(2, len(self.car_manager.car_list))