import time
import turtle
import config
from src.game_objects.player import Player
from src.managers.car_manager import CarManager
from src.managers.collision_manager import CollisionManager
from src.score import scoreboard
from src.score.scoreboard import Scoreboard
from src.screen.turtlecrossingscreen import TurtleCrossingScreen


# The manager class orchestrating the game logic

class GameManager:
    def __init__(self):
        self.game_screen = TurtleCrossingScreen()
        self.player = Player()
        self.game_screen.listen_for_keyboard_events(player=self.player)
        self.car_manager = CarManager()
        self.scoreboard = Scoreboard(config.SCORES_FILE_PATH)
        self.collision_manager = CollisionManager(car_manager=self.car_manager, player=self.player)
        self.time_start = None # Initialized in start_game()
        self.current_level = 1
        self.time_to_current_level = None # Initialized in level_up()
        self.player_name = None # Initialized in set_player_name()


    def set_player_name(self):
        self.player_name = turtle.textinput(title="Player name", prompt="What is your name?")
        self.game_screen.screen.listen()

    # Function used to populate the screen with cars as soon as the game is started
    def spawn_initial_cars(self):
        for i in range(200):
            self.car_manager.generate_and_move_wrapper()

    def game_state_update(self):
        self.car_manager.generate_and_move_wrapper() # Creating new cars and moving all of the cars
        self.game_screen.score_writer.write_current_level_and_top_level(current_level=self.current_level, top_level=self.scoreboard.get_top_level())
        self.game_screen.screen.update() # Updating the screen

    def check_car_collision(self) -> bool:
        return self.collision_manager.check_car_collision()

    def check_upper_wall_collision(self):
        return self.collision_manager.check_upper_wall_collision()

    def start_game(self):
        self.set_player_name()
        self.time_start = time.time()

    def game_over(self):
        self.game_screen.screen.update()
        self.game_screen.write_game_over(level=self.current_level, time_to_level=self.time_to_current_level)
        self.save_score()
        self.game_screen.screen.exitonclick()

    def save_score(self):
        score_to_save = {
            "player": self.player_name,
            "level": self.current_level,
            "time": self.time_to_current_level
        }
        self.scoreboard.save_score(score_to_save)

    def level_up(self):
        self.current_level += 1
        self.time_to_current_level = time.time() - self.time_start
        self.game_screen.score_writer.write_current_level_and_top_level(current_level=self.current_level, top_level=self.scoreboard.get_top_level())
        self.player.to_starting_position()
        self.car_manager.increase_difficulty(current_level=self.current_level)
