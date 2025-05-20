import time

import config
from turtle import Screen

from src.game_objects.player import Player
from src.screen.writerturtle import ScoreWriterTurtle, GameOverWriterTurtle


class TurtleCrossingScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=config.SCREEN_WIDTH, height=config.SCREEN_HEIGHT)
        self.screen.tracer(0)  # Turns animation off so that we can refresh the screen with the desired rhythm
        self.screen.bgcolor('pink')
        self.screen.title('Turtle Crossing Game')

        # Listening for events
        self.screen.listen()

        # The turtle writing the current score and the record
        self.score_writer = ScoreWriterTurtle()
        # The turtle writing the game over screen
        self.game_over_writer = GameOverWriterTurtle()

    def listen_for_keyboard_events(self, player: Player):
        self.screen.onkeypress(key="Up", fun=player.move)

    def write_game_over(self, level:int, time_to_level:float):
        self.game_over_writer.write_game_over(level, time_to_level)

