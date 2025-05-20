import config
import random
from src.managers.spawn_logic import SpawnPolicy, SpawnSide
from src.game_objects.car import Car

class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = 5
        self.spawn_policy = SpawnPolicy.RIGHT
        self.spawn_threshold = 0.9 # The lower the threshold, the bigger the chance of a car spawning
        self.spawn_threshold_decrease = 0.05

    # Called at each game loop
    def generate_and_move_wrapper(self):
        self.generate_car_random()
        self.move_cars()

    def generate_car_random(self):
        generate_car = random.random() > self.spawn_threshold
        if generate_car:
            self.generate_car()

    def generate_car(self):
        # The first few levels, cars only spawn on the right
        if self.spawn_policy == SpawnPolicy.RIGHT:
            self.car_list.append(Car(spawn_side=SpawnSide.RIGHT))
        # Later on, they can spawn on both sides
        if self.spawn_policy == SpawnPolicy.BOTH:
            spawn_side = random.choice(list(SpawnSide))
            self.car_list.append(Car(spawn_side=spawn_side))

    def move_cars(self):
        cars_to_remove = []
        # Moving the cars
        for car in self.car_list:
            car.move(self.move_distance)
            # If the car is 50 pixels out of the grid on either side, then we remove it from the game
            # Be careful that the cars spawn less than 50 pixels out of the grid!
            # otherwise they get removed as soon as they spawn
            if config.SCREEN_WIDTH / 2 + 50 < car.xcor() \
                    or car.xcor() < - config.SCREEN_WIDTH / 2 - 50:
                car.hideturtle()
                cars_to_remove.append(car)
        self.car_list = [car for car in self.car_list if car not in cars_to_remove]


    def increase_difficulty(self, current_level):
        # Starting from level 3, cars come from both sides!
        # We also set a bugger spawn threshold decrease, otherwise the screen is not populated enough
        if current_level == 3:
            self.spawn_policy = SpawnPolicy.BOTH
            self.spawn_threshold_decrease = 0.1
        self.spawn_threshold -= self.spawn_threshold_decrease
        self.move_distance += 3