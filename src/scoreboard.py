import config
from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.writer = Turtle()
        self.writer.color("black")
        self.writer.up()
        self.writer.goto(x=-config.SCREEN_WIDTH/2+70,
                         y=config.SCREEN_HEIGHT/2-30)
        self.writer.hideturtle()

        self.current_level = 1

        self.game_over_writer = Turtle()
        self.game_over_writer.up()
        self.game_over_writer.hideturtle()
        self.game_over_writer.color("red")

    def write_current_level(self):
        self.writer.clear()
        self.writer.write(arg=f"Level {self.current_level}",
                          align="center", move=False, font=config.FONT)

    def increase_level(self):
        self.current_level += 1

    def write_game_over(self):
        self.game_over_writer.write("GAME OVER",align= 'center', font=('Arial', 15, 'normal'))
        self.game_over_writer.goto(0, -30)
        self.game_over_writer.write(f"Your final level: {self.current_level}",align= 'center', font=('Arial', 15, 'normal'))