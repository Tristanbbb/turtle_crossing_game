import unittest
import config
from src.player import Player
from src.screen_setup import screen_setup


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.screen = screen_setup()

    def test_move(self):
        player = Player()
        self.assertEqual(player.ycor(),-280)
        player.move()
        self.assertEqual(player.ycor(),-270)
        player.move()
        player.move()
        self.assertEqual(player.ycor(), -250)

    # Testing that the hitbox coordinates are correct
    def test_hitbox_coordinates(self):
        player = Player()

        # At 0,0, the player's hitbox coordinates should just be the hitbox size
        player.goto(0,0)
        player.refresh_hitbox_coordinates()
        self.assertEqual(config.PLAYER_HITBOX['top'], player.hitbox_top)
        self.assertEqual(config.PLAYER_HITBOX['bottom'], player.hitbox_bottom)
        self.assertEqual(config.PLAYER_HITBOX['left'], player.hitbox_left)
        self.assertEqual(config.PLAYER_HITBOX['right'],player.hitbox_right)

        player.move()
        self.assertEqual(player.ycor() + config.PLAYER_HITBOX['top'], player.hitbox_top)
        self.assertEqual(player.ycor() + config.PLAYER_HITBOX['bottom'], player.hitbox_bottom)
        self.assertEqual(player.xcor() + config.PLAYER_HITBOX['left'], player.hitbox_left)
        self.assertEqual(player.xcor() + config.PLAYER_HITBOX['right'],player.hitbox_right)
