import unittest

import config
from src.collision_manager import CollisionManager
from src.car_manager import CarManager
from src.car import Car
from src.player import Player
from src.screen_setup import screen_setup, draw_grid, draw_line

DRAW_GRID = False # Set to True/False to draw grid

def print_coordinates(extended_turtle):
    if isinstance(extended_turtle, Car):
        print("Car hitbox coord")
    elif isinstance(extended_turtle, Player):
        print("Player hitbox coord")
    else:
        raise ValueError('Error: print_coordinates takes either a Car or a Player as argument.')
    print(f"xcor = {extended_turtle.xcor()}, ycor = {extended_turtle.ycor()}")
    print(f"    TOP:{extended_turtle.hitbox_top}    ")
    print(f"L:{extended_turtle.hitbox_left}        R:{extended_turtle.hitbox_right}")
    print(f"    BOTTOM:{extended_turtle.hitbox_bottom}    ")
    print("    ----    ")

class CollisionManagerBase(unittest.TestCase):
    # Setting up the screen and player for all subsequent tests
    def setUp(self):
        self.screen = screen_setup()
        if DRAW_GRID:
            draw_grid(10)
        self.player = Player()
        self.player.refresh_hitbox_coordinates()

        self.car_manager = CarManager()
        self.collision_manager = CollisionManager(car_manager=self.car_manager,
                                                 player=self.player)

class CollisionManagerPlayerToTopTest(CollisionManagerBase):

    # def tearDown(self):
    #     self.screen.exitonclick()

    def test_near_finish_line(self):
        #draw_line("horizontal", config.FINISH_LINE_Y)
        for i in range(56):
            self.player.move()
        self.screen.update()
        self.assertFalse(self.collision_manager.check_upper_wall_collision())

    def test_finish_line_crossed(self):
        for i in range(57):
            self.player.move()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_upper_wall_collision())


class CollisionManagerPlayerToCarTest(CollisionManagerBase):

    def setUp(self):
        super().setUp()
        self.car_manager.generate_car()
        self.player.goto(0, 0)
        self.player.refresh_hitbox_coordinates()

    # One pixel short of collision, no collision expected
    def test_front_near_collision(self):
        self.car_manager.car_list[0].goto(0,27)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()

        print_coordinates(self.player)
        print_coordinates(self.car_manager.car_list[0])
        self.screen.update()
        self.assertFalse(self.collision_manager.check_car_collision())

    # One pixel into a front collision, collision expected
    def test_front_collision(self):
        self.car_manager.car_list[0].goto(0,26)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        print_coordinates(self.player)
        print_coordinates(self.car_manager.car_list[0])
        self.assertTrue(self.collision_manager.check_car_collision())

    def test_left_of_car_no_collision(self):
        # no collision
        self.car_manager.car_list[0].goto(30, 0)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertFalse(self.collision_manager.check_car_collision())

    def test_left_of_car_collision(self):
        # collision
        self.car_manager.car_list[0].goto(29, 0)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_car_collision())

    def test_right_of_car_no_collision(self):
        # no collision
        self.car_manager.car_list[0].goto(-30, 0)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertFalse(self.collision_manager.check_car_collision())

    def test_right_of_car_collision(self):
        # collision
        self.car_manager.car_list[0].goto(-29, 0)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_car_collision())

    def test_back_no_collision(self):
        # no collision
        self.car_manager.car_list[0].goto(0, -19)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertFalse(self.collision_manager.check_car_collision())

    def test_back_collision(self):
        # collision
        self.car_manager.car_list[0].goto(0, -18)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.car_manager.car_list[0].print_hitbox_coordinates()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_car_collision())

    def test_diagonal_no_collision(self):
        # no collision
        self.car_manager.car_list[0].goto(28, -18)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_car_collision())

    def test_diagonal_collision(self):
        # collision
        self.car_manager.car_list[0].goto(27, -18)
        self.car_manager.car_list[0].refresh_hitbox_coordinates()
        self.screen.update()
        self.assertTrue(self.collision_manager.check_car_collision())

