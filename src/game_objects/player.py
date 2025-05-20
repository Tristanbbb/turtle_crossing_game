import config
from src.game_objects.game_object import GameObject

class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.to_starting_position()

    def move(self):
        self.forward(config.MOVE_DISTANCE)
        self.refresh_hitbox_coordinates()

    def to_starting_position(self):
        self.goto(config.STARTING_POSITION)
        self.refresh_hitbox_coordinates()

    def refresh_hitbox_coordinates(self):
        super().refresh_hitbox_coordinates(config.PLAYER_HITBOX)