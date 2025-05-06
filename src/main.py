import time
import config
from src.collision_manager import CollisionManager
from src.screen_setup import screen_setup
from src.player import Player
from src.car_manager import CarManager
from src.scoreboard import Scoreboard

# Initialization
screen = screen_setup()
screen.listen()
player = Player()
player.to_starting_position()
screen.onkeypress(key="Up",fun=player.move)
car_manager = CarManager()
scoreboard = Scoreboard()
collision_manager = CollisionManager(car_manager=car_manager, player=player)

# Generating and moving cars so that the screen is populated when the game starts
for i in range(200):
    car_manager.car_manager_actions_wrapper()

scoreboard.write_current_level() # Level 1

# Main game loo
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(config.REFRESH_INTERVAL)
    car_manager.car_manager_actions_wrapper() # Generate and move cars
    if collision_manager.check_upper_wall_collision(): # Then level up
        scoreboard.increase_level()
        scoreboard.write_current_level()
        car_manager.increase_difficulty(current_level=scoreboard.current_level)
        player.to_starting_position()
        pass
    if collision_manager.check_car_collision(): # Then game over!
        screen.update()
        break


scoreboard.write_game_over()
screen.exitonclick()