import config
import random
from src.game_object import GameObject
from src.spawn_logic import SpawnSide

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(GameObject):
    def __init__(self, spawn_side: SpawnSide):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.spawn_side = spawn_side
        self.set_heading_and_initial_position(spawn_side=spawn_side)

    # Calls set_heading_and_initial_position_right or set_heading_and_initial_position_left
    def set_heading_and_initial_position(self,spawn_side):
        if spawn_side == SpawnSide.RIGHT:
            self.set_heading_and_initial_position_right()
        elif spawn_side == SpawnSide.LEFT:
            self.set_heading_and_initial_position_left()

    # For cars spawning on the right
    def set_heading_and_initial_position_right(self):
        self.setheading(180)
        self.goto(
            x= config.SCREEN_WIDTH/2, # Starts all the way to the right
            y= random.uniform( # Random y position across the whole height of the screen
                a= (-config.SCREEN_HEIGHT/2) +50, # 50 additional padding so that cars can't start where the turtle starts
                b=  (config.SCREEN_HEIGHT/2) -10
            )
        )

    # For cars spawning on the right
    def set_heading_and_initial_position_left(self):
        self.setheading(0)
        self.goto(
            x= -config.SCREEN_WIDTH/2, # Starts all the way to the left
            y= random.uniform( # Random y position across the whole height of the screen
                a= (-config.SCREEN_HEIGHT/2) +50, # 50 additional padding so that cars can't start where the turtle starts
                b=  (config.SCREEN_HEIGHT/2) -10
            )
        )

    def move(self,distance):
        self.forward(distance)
        self.refresh_hitbox_coordinates()

    def refresh_hitbox_coordinates(self):
        super().refresh_hitbox_coordinates(config.CAR_HITBOX)

