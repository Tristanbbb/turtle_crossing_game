import config
import time
from src.managers.collision_manager import CollisionManager
from src.managers.car_manager import CarManager
from src.managers.game_manager import GameManager
from src.score.scoreboard import Scoreboard
from src.screen.turtlecrossingscreen import TurtleCrossingScreen


# Initialization
game_manager = GameManager()

# Generating and moving cars so that the screen is populated when the game starts
game_manager.spawn_initial_cars()

# Main game loop
game_manager.start_game()
game_is_on = True
while game_is_on:
    game_manager.game_state_update()
    time.sleep(config.REFRESH_INTERVAL)

    if game_manager.check_upper_wall_collision():
        game_manager.level_up()
    if game_manager.check_car_collision():
        break

game_manager.game_over()