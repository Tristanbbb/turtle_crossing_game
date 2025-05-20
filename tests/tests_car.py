import unittest

import config
from src.game_objects.car import Car
from src.managers.spawn_logic import SpawnSide


class PlayerTest(unittest.TestCase):

    def test_move(self):
        car = Car(spawn_side=SpawnSide.RIGHT)
        prev_x, prev_y = car.xcor(), car.ycor()
        car.move(5)
        self.assertEqual(prev_x-5, car.xcor())
        self.assertEqual(prev_y, car.ycor()) # No vertical change


    # Testing that the hitbox coordinates are correct
    def test_hitbox_coordinates(self):
        car = Car(spawn_side=SpawnSide.RIGHT)
        car.goto(0,0)

        move_distance = 5
        car.move(move_distance)
        self.assertEqual(car.ycor() + config.CAR_HITBOX['top'], car.hitbox_top)
        self.assertEqual(car.ycor() + config.CAR_HITBOX['bottom'], car.hitbox_bottom)
        self.assertEqual(car.xcor() + config.CAR_HITBOX['left'], car.hitbox_left)
        self.assertEqual(car.xcor() + config.CAR_HITBOX['right'], car.hitbox_right)
