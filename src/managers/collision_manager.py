import config
from src.managers.car_manager import CarManager
from src.game_objects.player import Player


class CollisionManager:
    def __init__(self, car_manager: CarManager, player: Player):
        self.car_manager = car_manager
        self.player = player

    # Returns True if the player collided with a car (in which case the game is over)
    def check_car_collision(self) -> bool:
        for car in self.car_manager.car_list:
            if self.check_vertical_overlap(car) and self.check_horizontal_overlap(car):
                # Useful for debugging the collision logic:
                car.print_hitbox_coordinates()
                self.player.print_hitbox_coordinates()
                return True
        return False

    # Checking if the car and the player overlap vertically
    def check_vertical_overlap(self,car) -> bool:
        return car.hitbox_top > self.player.hitbox_top > car.hitbox_bottom \
                or car.hitbox_top > self.player.hitbox_bottom > car.hitbox_bottom \
                or car.hitbox_top > self.player.ycor() > car.hitbox_bottom

    # Checking if the car and the player overlap horizontally
    def check_horizontal_overlap(self,car) -> bool:
        return car.hitbox_right > self.player.hitbox_right > car.hitbox_left \
                or car.hitbox_right > self.player.hitbox_left > car.hitbox_left

    # Returns True if the player reached the upper wall (in which case, level up)
    def check_upper_wall_collision(self) -> bool:
        return self.player.hitbox_top >= config.FINISH_LINE_Y
